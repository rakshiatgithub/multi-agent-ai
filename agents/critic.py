from langchain_community.chat_models import ChatOllama

llm = ChatOllama(model="llama3")

def critic(answer):

    prompt=f"""
You are a Critic Agent.

Review the answer.

Check

- Accuracy
- Completeness
- Hallucinations
- Missing information
- Logical flow

Then produce

Critique

Improved Answer
"""

    return llm.invoke(prompt).content
