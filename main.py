import os
from dotenv import load_dotenv
from google import genai


def main():
    print("Hello from agentic-gemini-thingy!")
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")
    if api_key == None:
        raise RuntimeError("couldn't get api key")
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(model="gemini-3.1-flash-lite", contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum.")
    if response.usage_metadata != None:
        print("Prompt tokens:", response.usage_metadata.prompt_token_count)
        print("Response tokens:", response.usage_metadata.candidates_token_count)
    else:
        raise RuntimeError("no tokens used, likely failed api request")
    print(response.text)


if __name__ == "__main__":
    main()
