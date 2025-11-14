from praisonaiagents import Agent, MCP

# Define environment variables
env_vars = {
    "MYSQL_HOST": "10.224.16.61",
    "MYSQL_PORT": "53306",
    "MYSQL_USER": "smart_intern",
    "MYSQL_PASS": "smart_intern",
    "MYSQL_DB": "sensors_database",
    "ALLOW_INSERT_OPERATION": "false",
    "ALLOW_UPDATE_OPERATION": "false",
    "ALLOW_DELETE_OPERATION": "false",
    #"PATH": "/Users/atlasborla/Library/Application Support/Herd/config/nvm/versions/node/v22.9.0/bin:/usr/bin:/bin",
    #"NODE_PATH": "/Users/atlasborla/Library/Application Support/Herd/config/nvm/versions/node/v22.9.0/lib/node_modules"
}

# Set up the MCP tool using the praisonaiagents library
mcp_tool = MCP(
    command="npx",
    args=["-y", "@benborla29/mcp-server-mysql"],
    env=env_vars
)

# Create the Agent
agent = Agent(
    instructions="""You are a MySQL querying assistant.""",
    llm="ollama/llama3.2",
    tools=mcp_tool
)

agent.start("fetch the last row from the table 'states' ordered by 'last_updated_ts' in sensors_database")