from openai import OpenAI
import os
from dotenv import load_dotenv

load_dotenv()


class LLMService:

    def __init__(self):

        self.client = OpenAI(
            # api_key=os.getenv("OPENAI_API_KEY")
            api_key=os.getenv("CLAUDE_API_KEY")
        )

    def generate(self, prompt):

        response = self.client.chat.completions.create(

            # model="gpt-4o-mini",
            model="claude-sonnet-4-6"
            messages=[
                {
                    "role": "user",
                    "content": prompt
                }
            ],

            temperature=0.3
        )

        return response.choices[0].message.content