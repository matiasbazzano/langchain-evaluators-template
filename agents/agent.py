from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from utils.models import DEFAULT_MODEL
from utils.prompts import AGENT_PROMPT

load_dotenv()

# We can pass temperature/verbose here ', temperature=0, verbose=True'
model = ChatOpenAI(model=DEFAULT_MODEL)


def run_agent(query: str):
    chain = AGENT_PROMPT | model
    result = chain.invoke({"input": query})
    return result.content


if __name__ == "__main__":
    while True:
        q = input(">> ")
        if q.lower() in ["exit", "quit"]:
            break
        output = run_agent(q)
        print(f"\nAgent: {output}\n")
