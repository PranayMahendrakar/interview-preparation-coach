"""question_generator module"""
from .base import LlamaClient
class QuestionGenerator:
    def __init__(self):
        self.client = LlamaClient()
        self.system_prompt = "You are an expert interview coach helping students prepare for job interviews."
    def process(self, query: str, context: str = "") -> str:
        return self.client.generate(f"Interview coaching:\n{query}\nContext: {context}\n\nProvide helpful, practical advice.", self.system_prompt)
