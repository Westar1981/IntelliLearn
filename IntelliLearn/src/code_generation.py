
import openai

class CodeGenerator:
    def __init__(self, api_key):
        openai.api_key = api_key

    def generate_code(self, prompt):
        response = openai.completions.create(
            engine="davinci-codex",
            prompt=prompt,
            max_tokens=150
        )
        return response.choices[0].text.strip()

if __name__ == "__main__":
    api_key = "your_openai_api_key"
    generator = CodeGenerator(api_key)
    prompt = "Create a Python function to calculate the factorial of a number."
    code = generator.generate_code(prompt)
    print(code)
