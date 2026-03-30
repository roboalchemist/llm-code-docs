# Allow the ecb_interest_rate_agent to handoff the conversation to the graph_agent or calculator_agent
ecb_interest_rate_agent = client.beta.agents.update(
    agent_id=ecb_interest_rate_agent.id,
    handoffs=[graph_agent.id, calculator_agent.id]
)