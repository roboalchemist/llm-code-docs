# Architecture

## 10-Step Workflow with Specialized Agents

The integration demonstrates a **10-step agentic workflow** coordinated by Microsoft AutoGen’s **Swarm pattern**. Each agent has a clear, specialized role:

1. **Planning Agent**

   * Entry point for user queries.
   * Routes requests through the appropriate workflow.
   * Maintains orchestration logic and conversation state.

2. **Skyfire Find Seller Agent**

   * Searches Skyfire’s marketplace directory.
   * Locates the Dappier service listing and retrieves its metadata.

3. **Skyfire KYA Agent (Know Your Agent)**

   * Issues **authentication tokens** for secure agent-to-service interactions.
   * Ensures buyer and seller identity verification.

4. **JWT Decoder Agent**

   * Validates JWT tokens created by Skyfire.
   * Decodes payloads to ensure token integrity and extract claims.
   * Used twice in the workflow (auth tokens and payment tokens).

5. **MCP Connector Agent**

   * Connects to the Dappier MCP server ([mcp.dappier.com](https://mcp.dappier.com/mcp)).
   * Retrieves available tools and pricing information.

6. **Dappier Price Calculator Agent**

   * Estimates the cost of the requested Dappier query.
   * Uses pricing logic (mocked with static JSON for the demo).

7. **Skyfire KYA Payment Token Agent**

   * Creates **payment tokens** with estimated amounts.
   * Prepares the payment flow before execution.

8. **JWT Decoder Agent (second usage)**

   * Decodes and verifies the payment token payload.
   * Ensures correctness before charging.

9. **Dappier Agent**

   * Executes the actual query against Dappier’s real-time data tools.
   * Handles results from finance, news, research, and more.

10. **Skyfire Charge Token Agent**

    * Processes payment by charging the token through Skyfire’s API.
    * Completes the loop with secure settlement.

***