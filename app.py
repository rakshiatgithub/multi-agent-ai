import streamlit as st

from agents.planner import planner
from agents.researcher import researcher
from agents.critic import critic
from agents.summarizer import summarizer

st.set_page_config(
    page_title="AI Research Assistant",
    page_icon="🤖",
    layout="wide"
)

st.title("🤖 Multi-Agent AI Research Assistant")

query = st.text_input("Ask anything")

if st.button("Research"):

    with st.spinner("Planner working..."):
        plan = planner(query)

    with st.spinner("Researching..."):
        research = researcher(query, plan)

    with st.spinner("Critiquing..."):
        review = critic(research)

    with st.spinner("Generating Final Answer..."):
        final = summarizer(review)

    tab1, tab2, tab3, tab4 = st.tabs([
        "Planner",
        "Researcher",
        "Critic",
        "Final Answer"
    ])

    with tab1:
        st.markdown(plan)

    with tab2:
        st.markdown(research)

    with tab3:
        st.markdown(review)

    with tab4:
        st.success(final)
