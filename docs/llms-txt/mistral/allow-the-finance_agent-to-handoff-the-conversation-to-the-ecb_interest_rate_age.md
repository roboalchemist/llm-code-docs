# Allow the finance_agent to handoff the conversation to the ecb_interest_rate_agent or web_search_agent
finance_agent = client.beta.agents.update(
    agent_id=finance_agent.id,
    handoffs=[ecb_interest_rate_agent.id, web_search_agent.id]
)