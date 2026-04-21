from langchain_groq import ChatGroq
from langchain_core.output_parsers import StrOutputParser
import os

class LLMFallback:
    def __init__(self):
        self.parser = StrOutputParser()
        api_key = os.getenv("GROQ_API_KEY")

        if not api_key:
            self.llm = None
        else:
            self.llm = ChatGroq(
                model="llama-3.3-70b-versatile",
                temperature=0.2,
                api_key=api_key
            )

    def get_response(self, user_query: str) -> str:
        if not self.llm:
            return "I'm unable to access advanced help right now. Please contact IT support."

        prompt = f"""
You are an internal IT support assistant.
Give clear, short, step-by-step guidance.
If unsure, suggest contacting IT support.

User issue:
{user_query}
"""
        response = self.llm.invoke(prompt)
        return self.parser.parse(response.content)
