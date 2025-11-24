# Source: https://dev.writer.com/agent-builder/tool-calling-intro.md

# Understand tool calling

> Learn how tool calling enables dynamic agent workflows. Understand ReAct patterns and why tool calling matters for intelligent agent orchestration.

Tool calling allows you to call external tools that you define and integrate them into your agent's responses.

Instead of requiring you to build static, hardcoded workflows, tool calling enables you to build agents that dynamically choose and orchestrate the right combination of tools based on the specific context of each request.

This document describes why tool calling matters and how it works behind the scenes.

Jump to [tool calling in Agent Builder](/agent-builder/tool-calling) to learn how to use tool calling in Agent Builder.

## Why tool calling matters

* **Traditional approach limitations**: With pre-defined API workflows, you'd need to hardcode every possible scenario: "If customer mentions shipping, call shipping API. If they mention returns, call returns API." This creates rigid, brittle systems that can't handle the complexity of real customer inquiries.

* **Tool calling's dynamic intelligence**:
  The model acts as an intelligent orchestrator, analyzing the customer's specific problem and dynamically selecting the most relevant tools. It handles parameter extraction, API sequencing, and data synthesis automatically.

* **Enables advanced reasoning patterns**: Tool calling naturally supports [ReAct (Reasoning and Acting)](https://klu.ai/glossary/react-agent-model) workflows, where the model can think through problems step-by-step, take actions by calling tools, observe the results, and then reason about what to do next.

### Customer service example

A customer writes to your support team:

> "I ordered two items last week but only received one and the item I got isn't working."

Your Agent Builder agent takes a customer's request and uses tool calling to dynamically select the most relevant tools to use. Available tools might include:

* `get_order_details(order_id)`
* `check_shipping_status(tracking_number)`
* `initiate_return_request(order_id, reason)`
* `check_inventory_status(product_id)`
* `create_support_ticket(customer_id, issue_type)`
* Support, policies, and other knowledge from your connected Knowledge Graphs

Given the tools provided to the model, it can review the user's request and automatically:

1. Extract the customer ID from context
2. Call `get_order_details()` to understand what was ordered
3. Call `check_shipping_status()` for the missing item
4. Look up return policies from your connected support Knowledge Graph
5. Synthesize all this information into a coherent, helpful response

## How tool calling works behind the scenes

While the AI model intelligently decides which tools to use and what parameters to call them with, the model doesn't actually execute the tools itself. Instead, there's a two-step handoff process:

* **The AI decides what to do**: The model analyzes the customer's request and says "I need to call `get_order_details` with order ID #12345"
* **Your system does the actual work**: Your blueprint receives this instruction, makes the real API call to your order database, and sends the results back to the AI

The AI then uses the results of the tool calls to continue reasoning and provide the final response.

### Project manager analogy

Think of it like a project manager coordinating subcontractors: The AI project manager understands the entire project scope and knows exactly which specialists to engage and what work needs to be done. When a customer has an issue, the AI says "I need the shipping contractor to check tracking #12345, then the inventory contractor to verify stock levels." But the AI doesn't do the actual work; each subcontractor (your systems) has their own expertise and tools to execute their piece, then reports back to the project manager who coordinates everything into the final deliverable.

<img src="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-architecture.png?fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=eda1439a71ace16caaaa361712101869" alt="Tool calling example with contractor analogy" data-og-width="3297" width="3297" data-og-height="1568" height="1568" data-path="images/agent-builder/tool-calling-architecture.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-architecture.png?w=280&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=339ffbd63c0fdb3b355726f0742069d7 280w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-architecture.png?w=560&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=e69fa1a0821ebf479492ecd639e3b69d 560w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-architecture.png?w=840&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=f987f3daf48ff182b65ca1103174c8b8 840w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-architecture.png?w=1100&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=f874f9103958d7194b0f9aa23fc3f934 1100w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-architecture.png?w=1650&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=166d65dfa8724d588f78cf5ac89c047d 1650w, https://mintcdn.com/writer/Ph7gAl4exSh0IC1l/images/agent-builder/tool-calling-architecture.png?w=2500&fit=max&auto=format&n=Ph7gAl4exSh0IC1l&q=85&s=9baa009a54847bbe87893283ec5281fb 2500w" />

This architecture provides several benefits:

* **Security and control**: You maintain full control over your data and system access
* **Flexibility**: You can easily add new tools or modify existing ones without changing the AI
* **Reliability**: Each system component can be optimized and maintained independently
* **Compliance**: Sensitive operations remain within your controlled infrastructure

## Next steps

Now that you understand why tool calling matters and how it works behind the scenes, [learn how to use tool calling in Agent Builder](/agent-builder/tool-calling).

<feedback />
