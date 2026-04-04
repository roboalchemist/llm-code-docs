# Source: https://plivo.com/docs/aiagent/aistudio/nodereference/customerinput.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Customer Input

> Customer Input Nodes allow you to collect data use data and personalize the agent flow 

Customer Input Nodes are essential tools for gathering valuable information from users during or after a conversation. These nodes help you collect feedback or structured data like names, emails, or phone numbers, enabling more personalized and effective interactions. Whether it's collecting customer feedback or turning form submissions into conversational tasks, these nodes enhance your agent’s ability to capture relevant user inputs seamlessly.

## Types of Customer Input Nodes

### 1. **Customer Feedback Node**

The **Customer Feedback Node** is used to gather post-interaction feedback from users, typically at the end of a conversation. It allows you to measure the user’s satisfaction and make decisions based on the feedback score.

**Configuration Options**:

* **Feedback Scale**: Collect a score from **1 (lowest)** to **5 (highest)**.
* **Next Steps Based on Feedback**:
  * **High Feedback**: If the user gives a high rating (e.g., 4 or 5), proceed to a thank you message or a positive follow-up.
  * **Low Feedback**: If the user gives a low rating (e.g., 1 or 2), you can escalate the conversation to a human agent for further support or handle the low feedback in a different manner.

**Use Case**:\
After a customer support interaction, you can ask the user for a rating. If they rate the service highly, the workflow continues to a "Thank You" message. If the rating is low, the system can escalate the issue to a human specialist for further resolution.

### 2. **Collect Data Node**

The **Collect Data Node** is used to gather structured input from users, such as **name**, **email**, **phone number**, or any other data points you need to capture. This is especially useful when converting traditional forms into a conversational format.

**Configuration Options**:

* **Data Fields**: Choose which fields you need to collect (e.g., first name, email address, phone number).
* **Input Validation**: Set validation rules for the inputs to ensure that the data provided is in the correct format (e.g., valid email, phone number).

**Use Case**:\
If you are collecting customer information, you can use this node to ask for details like the user’s name, email, or phone number, and validate the responses to ensure that the data is accurate and complete.
