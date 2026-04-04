# Source: https://docs.asapp.com/generativeagent/configuring/task-best-practices.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Tasks Best Practices

> Improve task writing by following best practices

Before integrating GenerativeAgent, define the tasks and functions that GenerativeAgent will perform for your organization.

**Tasks** represent the issues or actions you want the generative agent to handle. Each task consists of **instructions** and the **functions** needed to perform those instructions.

* **Instructions** define the business logic and acceptance criteria for a task.
* **Functions** are the tools (such as APIs) needed to perform a task according to its instructions.

The goal of all instructions is to deliver the desired outcome using the minimum number of expressions.

## Best Practices

Clearly defining tasks is essential for configuring GenerativeAgent. GenerativeAgent acts on the tasks you ask it to perform and solves customer issues across your apps.

When writing or defining tasks, keep the following practices in mind:

### Know where to place information

Deciding which information belongs in tasks versus in the Knowledge Base can be challenging. Use this rule of thumb:

* **Task instructions** define procedures and courses of action for GenerativeAgent.

> Example: "Flip a coin. The result of coin\_flip determines whether the customer starts the game."

* **Knowledge Base articles** contain information and guides on how to operate during an action.

> Example: "Flipping coins must use quarters. Mark the result after the coin falls into your hand and stops moving. If the coin falls from your hand, the result is null."

For example, a task that uses the `refund_eligibility` API would be:

```
Use the refund_eligibility API to check if the purchase is eligible for a refund. 
If eligible, ask the customer if they want store credit or a refund to their original payment method
```

A Knowledge Base article for this task would be:

```
Refunds typically take 7-10 days to appear on credit card statements. 
Store credit will be sent via email within one hour of issuing the refund.
```

### Format Instructions

Use clear instructions for tasks.

Be consistent in how you use formatting elements, such as headers or bullet/numbered lists. Use markdown for task definitions.

* Use headers to organize sections within the instructions
* Use lists for clarity

```json  theme={null}
# Headers organize task sections
- Use headers to break down complex tasks into sections
- Use bullet points for clarity within each section
-- Use sub bullet points for further clarification on a specific point

# Task Format Example
- Verify the customer's order ID
- Use the order_status API to retrieve current status
- Communicate the status to the customer
-- If the status is pending, ask the customer to check back later.
```

### Provide Resolution Steps

Enumerate the steps that GenerativeAgent needs to resolve a task.

This provides a logical flow of actions that GenerativeAgent can follow to be more efficient.

Just as a human agent needs to check, read, resolve, and send information to a customer, GenerativeAgent needs these steps to be clearly defined.

```json  theme={null}
# Steps to take to check order status
1. Verify Purchase Eligibility
- Check the purchase date to ensure it is within the 30-day refund policy.
- Verify that the item is eligible for a refund
2. Gather Necessary Information
- Ask the customer for their order ID.
3. Check Order Status
- Call the `order_status` function to retrieve the current status of the order.
- Confirm that the order is eligible for a refund.
```

### Define Functions to Call

Functions represent the set of APIs needed alongside their instructions.

GenerativeAgent invokes functions to perform the necessary actions for a task.

Task instructions must specify how and when GenerativeAgent should invoke a function.

Here is an example of how to reference functions in task instructions:

Within the "FlightStatus" task, functions might include:

* `trip_details_extract_with_pnr`: Retrieves flight details using the customer's PNR and last name.
* `trip_details_pnr_emails`: Handles email addresses associated with the PNR.
* `send_itinerary_email_as_string`: Sends the trip receipt or itinerary to the customer via email.

Here is how the task instruction would be outlined to use the function:

```json  theme={null}
"The function `trip_details_extract_with_pnr` is used within the 'FlightStatus' task to retrieve the current schedule of a customer's flight using their confirmation code and last name."
```

### API Return Handling

Provide instructions for handling API call responses after performing a function.

Use the syntax `(data["APICallName"])` to reference specific data returned from an API call.

Here is an example of API Return Handling:

```json  theme={null}
When called, if there is a past due amount, you MUST tell them their exact soft disconnect date (data["softDisconnectDate"]), and let them know that after that day, their service will be shut off, but still be easy to turn back on.
```

### State Policies and Scenarios

Clearly define company policies and outline what GenerativeAgent must do in various scenarios.

Stating policies ensures consistency and compliance with your organization's standards.

Remember that a good portion of policies can be taken from your Knowledge Base.

```json  theme={null}
# Refund eligibility
- Customers can request a refund within 30 days of purchase.
- Refunds will be processed to the original payment method.
- Items must be returned in their original condition.
# Conversational Style
- Always refer to the customer as "customer."
- Do not address the customer by their name or title.
```

### Ensure Knowledge Base Resourcing

Ensure that GenerativeAgent uses your Knowledge Base either through an API or the Knowledge Base tooling in the GenerativeAgent UI.

Reference Knowledge Base resources within the task so GenerativeAgent can access them during conversations.

You can test GenerativeAgent's behavior using the Previewer.

Store task-related information in the Knowledge Base with metadata tags.

Use metadata to ensure certain articles are only used by specific tasks. If an article and a task have the same metadata tags, GenerativeAgent will filter and only use that relevant information during a conversation.

### Outline Limitations

Be clear about the limitations of each task.

Provide instructions for handling customer requests that go beyond a task's limits.

This helps GenerativeAgent manage customer expectations, provide alternative solutions, and switch to tasks that align with the customer's needs.

```json  theme={null}
# Limitations
- Cannot process refunds for items purchased more than 30 days ago.
- Redirect customers to the website for refunds involving gift cards.
- No knowledge of specific reasons for payment failures.
```

### Use Conditional Templates

Use [conditional templating](/generativeagent/configuring/tasks-and-functions/conditional-templates) to make parts of the task instructions conditional on reference variables determined from API responses.

This ensures that only the contextually relevant task instructions are available at the right time in the conversation.

```json  theme={null}
{% if data["refundStatus"] == "approved" %}
- Inform the customer that their refund has been approved and will be processed shortly.
{% elif data["refundStatus"] == "pending" %}
- Let the customer know that their refund request is pending and provide an estimated time for resolution.
{% endif %}
```

### Use Reference Variables

[Reference variables](/generativeagent/configuring/tasks-and-functions/reference-variables) let you store and reuse specific data returned from function responses. They are powerful tools for creating dynamic and context-aware tasks.

Once a reference variable is created, you can use it to:

* Conditionally make other functions available
* Set conditional logic in prompt instructions
* Compare values across different parts of your GenerativeAgent workflow
* Control function exposure based on data from previous function calls
* Toggle conditional instructions in your task's prompt depending on returned data
* Extract and transform values without hard-coding logic into prompts or code

For example:

```json  theme={null}
val == "COMPLIANT" → returns True if the string is "COMPLIANT"  
val == true or val == false → checks if the value is a boolean true/false
val is not none and val|length > 0 → returns True if val has length > 0  
```

### Create Subtasks

Some tasks are larger and more complex than others.

GenerativeAgent is more efficient with cohesive and direct tasks. A good practice for complex tasks is to divide them into subtasks.

For example, to process a refund for a customer, GenerativeAgent might need to:

* Confirm the customer's status
* Confirm the policies allow for the refund
* Process the refund

```json  theme={null}
For a customer seeking a refund, consider splitting the task into:
OrderStatus: To check the status of the order and communicate the results to the customer.
IssueRefund: To gather the information necessary to process the refund and actually process the refund.
```

### Call Task Switch

Sometimes GenerativeAgent needs to switch from one task to another.

Be explicit about which tasks to switch to based on the context.

```json  theme={null}
# Damage Claims
- For claims regarding damaged products, use the 'DamageClaims' task
# Exchange Requests
- For exchange inquiries, use the 'ExchangeProducts' task
# No pets rule
- (#rule_1) no dogs in the house
- (#rule_2) no cats outside
- (#rule_3) if either #rule_1 or #rule_2 are broken escalate to agent.
```

### Outline Human Support

State scenarios in which GenerativeAgent needs to escalate the issue to a human agent.

This ensures GenerativeAgent's role in your organization is clearly defined.

```json  theme={null}
# Escalate to a Human Agent
- Refunds involving high-value items.
- Refunds where payment method issues are detected.
```

You can also state scenarios for HILA:

```json  theme={null}
# Call HILA and wait on approval
- Refunds of purchases older than 30 days
- Cancelation of high-value purchases
```

### Keep It Simple

Keep task instructions focused and concise.

The more details you add to tasks, the greater the chance that essential instructions could be overlooked or diluted. If instructions are too long or complex, GenerativeAgent might not follow the most important steps precisely.

We recommend not placing too much task-relevant information directly in the task. Instead, use the other tools GenerativeAgent provides, such as metadata, functions, and the Knowledge Base.

<Note>
  We do not recommend directly uploading an internal agent-facing knowledge base to the GenerativeAgent Knowledge Base.

  GenerativeAgent's Knowledge Base is meant for GenerativeAgent's use. Task instructions better suit instructions meant for agents.
</Note>
