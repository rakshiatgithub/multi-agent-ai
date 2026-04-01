from agents.planner import planner
from agents.researcher import researcher
from agents.critic import critic
from agents.summarizer import summarizer

query = input("Enter your question: ")

plan = planner(query)
print("\n--- PLAN ---\n", plan)

research = researcher(query)
print("\n--- RESEARCH ---\n", research)

review = critic(research)
print("\n--- CRITIC ---\n", review)

final = summarizer(review)
print("\n--- FINAL ANSWER ---\n", final)