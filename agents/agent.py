from dotenv import load_dotenv
from langchain_openai import ChatOpenAI
from langchain_classic.chains import LLMChain
from utils.models import DEFAULT_MODEL
from utils.prompts import AGENT_PROMPT

load_dotenv()

# We can pass temperature here ', temperature=0'
model = ChatOpenAI(model=DEFAULT_MODEL)


def run_agent(query: str):
    # We can pass verbose here ', verbose=True'
    chain = LLMChain(prompt=AGENT_PROMPT, llm=model)
    result = chain.invoke({"input": query})
    return result["text"]


if __name__ == "__main__":
    while True:
        q = input(">> ")
        if q.lower() in ["exit", "quit"]:
            break
        output = run_agent(q)
        print(f"\nAgent: {output}\n")
