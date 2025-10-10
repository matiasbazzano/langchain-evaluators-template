from langchain.prompts import PromptTemplate

AGENT_PROMPT = PromptTemplate.from_template(
    """
    You are a generic agent who answers different questions appropriately.

    Question: {input}
    Answer:
    """
)
