from dotenv import load_dotenv
import os
from pathlib import Path

load_dotenv(Path(__file__).resolve().parent / ".env")

def main():
    print("Hello from langchain-course!")
    print(os.environ.get("OPENAI_API_KEY"))


if __name__ == "__main__":
    main()  