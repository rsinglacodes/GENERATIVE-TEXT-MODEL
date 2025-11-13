from flask import Flask, render_template, request
import requests
import json

app = Flask(__name__)

# Local Ollama API endpoint
OLLAMA_API_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "llama3"  # Ensure you have this model downloaded via: ollama pull llama3

@app.route("/", methods=["GET", "POST"])
def index():
    generated_text = ""
    user_prompt = ""  # store prompt to keep it visible

    if request.method == "POST":
        user_prompt = request.form.get("prompt", "").strip()

        if not user_prompt:
            generated_text = "⚠️ Please enter a topic to generate text."
        else:
            full_prompt = (
                f"You are a creative and intelligent AI writer. Write a detailed, well-structured response "
                f"about the following topic:\n\n'{user_prompt}'\n\n"
                f"Generate around 2–3 paragraphs (150–250 words total). "
                f"Include examples, reasoning, and smooth transitions between ideas. "
                f"Keep the language natural, clear, and engaging."
            )

            try:
                response = requests.post(
                    OLLAMA_API_URL,
                    json={
                        "model": MODEL_NAME,
                        "prompt": full_prompt,
                        "stream": False
                    },
                    timeout=300
                )

                if response.status_code == 200:
                    data = response.json()
                    generated_text = data.get("response", "").strip() or "⚠️ No text was generated."
                else:
                    generated_text = f"❌ Error: Ollama returned status {response.status_code}"

            except requests.exceptions.ConnectionError:
                generated_text = "⚠️ Cannot connect to Ollama. Please ensure it’s running locally."
            except Exception as e:
                generated_text = f"❌ Unexpected error: {str(e)}"

    return render_template("index.html", generated_text=generated_text, user_prompt=user_prompt)


if __name__ == "__main__":
    app.run(debug=True)
