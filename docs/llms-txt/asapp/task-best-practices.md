# Source: https://docs.asapp.com/generativeagent/configuring/task-best-practices.md

# Tasks Best Practices

> Improve task writing by following best practices

Before any technical integration with GenerativeAgent, you must first define the tasks and the functions that the GenerativeAgent will perform to help your organization.

**Tasks** are the issues or actions you want generative agent to handle. They are primarily a set of **instructions** and the **Functions** needed to perform the instructions.

* **Instructions** define the business logic and acceptance criteria of a task.
* **Functions** are the set of tools (e.g. APIs) needed to perform a task with its instructions.

The goal of all instructions is to deliver the desired outcome using the minimum number expressions.

## Best Practices

Clearly defining tasks is key in configuring GenerativeAgent, as the GenerativeAgent acts on the tasks you as it to perform and solve customer issues across your apps.

When writing or defining Tasks, have the following methods in mind:

### Know where to place information

Deciding which information belongs in a Tasks or in the Knowledge Base can be challenging. To make it simple, we offer this recommendation as a rule of thumb:

* Task instructions are procedures and course of action for GenerativeAgent.

> Example: "Flip a coin, the result of coin\_flip decides whether the customer kickoffs the game."

* Knowledge Base Articles are a place to hold information and guides on how to make operate during an action.

> Example: "Flipping coins must be quarters, the result of the flip is marked after the coin falls in your hand and stops moving. If the coin falls from your hand, the result is null.""

For example, an example of the Task that uses the `refund_eligibility` API would be:

```
Use the refund_eligibility API to check if the purchase is eligible for a refund. 
If eligible, ask the customer if they want store credit or a refund to their original payment method
```

And the example of the Knowledge Base Article for the Task would be:

```
Refunds typically take 7-10 days to appear on credit card statements. 
Store credit will be sent via email within one hour of issuing the refund.
```

### Format Instructions

Use clear instructions for the Task.

Be consistent in the way you use marks, like Headers or bullet/numbered lists. Use markdown for the task definition.

* Use Headers to organize sections within the instructions
* Use lists for clarity

```json  theme={null}
# Headers
- Task section
- Bullet 2
-- Secondary Section
--- Tertiary Section
--- Tertiary Section 2
Here are instructions on how to use the api calls to solve problems:
# Section
1blah blah blah
# Section
2blah blah blah
```

### Provide Resolution Steps

Enumerate the steps that GenerativeAgent needs to resolve a task.

This provides a logical flow of actions that the GenerativeAgent can use to be more efficient.

Just as a human agent needs to check, read, resolve, and send information to a customer, GenerativeAgent needs these steps to be more detailed.

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

Functions are the set of APIs needed alongside their instructions.

GenerativeAgent invokes Functions to perform the necessary actions for a task.

Task instructions must outline how and when does GenerativeAgent invokes a Function.

Here is an example of how to call out functions in the task instruction:

Within the "FlightStatus" task, functions might include:

* `trip_details_extract_with_pnr`: Retrieves flight details using the customer's PNR and last name.
* `trip_details_pnr_emails`: Handles email addresses associated with the PNR.
* `send_itinerary_email_as_string`: Sends the trip receipt or itinerary to the customer via email.

Here is how the task instruction would be outlined to use the function:

```json  theme={null}
"The function `trip_details_extract_with_pnr` is used within the 'FlightStatus' task to retrieve the current schedule of a customer's flight using their confirmation code and last name."
```

### API Return Handling

Provide instructions for handle the returns of API Calls after performing a Function.

Use the syntax `(data["APICallName"])` to let GenerativeAgent know that that precise piece of writing is the data return from an API Call.

Here is an example of API Return Handling:

```json  theme={null}
When called, if there is a past due amount, you MUST tell them their exact soft disconnect date (data["softDisconnectDate"]), and let them know that after that day, their service will be shut off, but still be easy to turn back on.
```

### State Policies and Scenarios

Clearly define company policies and outline what GenerativeAgent must do in various scenarios.

Stating Policies ensure consistency and compliance with your Organization's standards.

Remember than a good part of the Policies can be taken from your Knowledge Base.

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

Ensure that GenerativeAgent is making use of your Knowledge Base either by API or by the Knowledge Base Tooling in the Generative Agent UI.

Provide the Knowledge Base Resources within the task, so GenerativeAgent references them when active.
Remember that you can try out GenerativeAgent's behavior by using the Previewer.

It is recommended to store task-related information in the Knowledge Base with metadata tags.

You can use metadata to ensure certain articles are only used by specific tasks. If an Article and a Task have the same metadata tags, GenerativeAgent will filter and only use that specific relevant information during a conversation.

### Outline limitations

Be clear about the limitations of each task.

Provide instructions on what to do in scenarios when customers ask for things that go beyond the limits of a task.
This helps GenerativeAgent to manage customer expectations, provide alternative solutions, and switch to tasks that are in line with the customer's needs.

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

* Conditionally make other Functions available
* Set conditional logic in prompt instructions
* Compare values across different parts of your GenerativeAgent workflow
* Control Function exposure based on data from previous function calls.
* Toggle conditional instructions in your Task s prompt depending on returned data
* Extract and transform values without hard‐coding logic into prompts or code

For example:

```json  theme={null}
val == "COMPLIANT" → returns True if the string is "COMPLIANT"  
val == true or val == false → checks if the value is a boolean true/false
val is not none and val|length > 0 → returns True if val has length > 0  
```

### Create Subtasks

Some tasks might be bigger and more complex than others.

GenerativeAgent is more efficient with cohesive and direct tasks. A good practice for complex tasks is to divide them into subtasks.

For example, to give a refund to a client, GenerativeAgent might need to:

* Confirm the customer's status
* Confirm the policies allow for the refund
* Confirm the refund

```json  theme={null}
For a customer seeking a refund, consider splitting the task into:
OrderStatus: To check the status of the order and communicate the results to the customer.
IssueRefund: To gather the information necessary to process the refund and actually process the refund.
```

### Call Task Switch

As all tasks are outlined, sometimes GenerativeAgent needs to switch from one task to another.

Be explicit about the tasks to switch to, given a context.

```json  theme={null}
# Damage Claims
- For claims regarding damaged products, use use the 'DamageClaims' task
# Exchange Requests
- For exchange inquiries, use the 'ExchangeProducts' task
# No pets rule
- (#rule_1) no dogs in the house
- (#rule_2) no cats outside
- (#rule_3) if either #rule_1 or #rule_2 are broken escalate to agent.
```

### Outline Human Support

State the scenarios where GenerativeAgent needs to escalate the issue to a human agent.

This ensures GenerativeAgent's role in your organization is well contained.

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

### Keep it simple

It is generally best to keep task instructions focused and concise.

The more details you add to tasks, the greater the chance that essential instructions could be overlooked or diluted. GenerativeAgent might not follow the most important steps as precisely if the instructions are too long or complex.

So, we recommend to not place many task-relevant information directly into the task. It is better to make use of the other tools GenerativeAgent has at your disposal, like metadata, Functions, and the Knowledge Base.

<Note>
  We do not recommend  to directly upload an internal agent-facing knowledge base to the GenerativeAgent Knowledge Base.

  GenerativeAgent's Knowledge Base is meant for GenerativeAgent's use. Instructions meant for agents are better suited to task instructions.
</Note>
