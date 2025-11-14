from praisonaiagents import Agent, MCP
search_agent = Agent(
    instructions="""you help analysis the temperature, humidity, CO2 level and pm 2.5 level of the database""",
    llm="ollama/llama3.2",
    tools=MCP("npx -y @modelcontextprotocol/server-postgres postgresql://smart_intern:smart_intern@10.224.16.61:53306/sensors_database")
)

search_agent.start("fetch the last row from the table 'states' ordered by 'last_updated_ts' in sensors_database")