# Source: https://docs.chatling.ai/ai-agent/actions/tutorials/fetch-and-email-order-confirmation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.chatling.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# 1. Fetch and Email Order Confirmation

In this tutorial, you'll build a simple but real-world flow that (1) fetches order data from an API via the [HTTP Request action](/ai-agent/actions/http-request), and (2) sends an email confirmation to the user with the [Send Email action](/ai-agent/actions/send-email).

By the end, your agent will automatically collect the user's email and order number, call your API to verify and fetch the order, and deliver a personalized confirmation email.

<img src="https://chatling-assets.b-cdn.net/send-email-action-sample-chat.jpg" width="350" alt="Send Email action preview" />

## Setup Guide

1. Open your agent dashboard and go to Actions.

2. Click the `New` button and choose `HTTP Request`.

3. Set up the action as follows:

**Action name**: get\_order

**When to use**: When user asks to get an email of their order confirmation, first use this action to fetch the order before using email\_order\_confirmation.

**Frequency**: Whenever applicable

**Input parameters**: Add the parameters that are required to fetch the user's order. In this case, we will add the following parameters:

* `email`: The email address of the order. Save it to a variable, such as "email".
* `order_number`: The user's order number. Save it to a variable, such as "order\_number".

<img src="https://chatling-assets.b-cdn.net/tutorial-1-http-request-input-parameters.jpg" width="600" alt="input parameters" />

**Request**: Configure the request by defining the API URL, method, payload, and headers that will be used to fetch the user's order.

For this tutorial, we'll use a dummy API that returns an order. However, in a real app, you'd point the HTTP Request to your own or third-party API, include auth (e.g., Bearer token), and the relevant payload such as the user's email and order number.

<img src="https://chatling-assets.b-cdn.net/tutorial-1-http-request-configuration.jpg" width="450" alt="HTTP Request configuration" />

4. Click the `Test Request` button to verify that the request runs successfully and that the agent receives a valid JSON response.

<img src="https://chatling-assets.b-cdn.net/tutorial-1-test-http-request.jpg" width="450" alt="test http request" />

5. Click `Create action` to save the action.
6. Go back to the `Actions` page.
7. Click the `New` button and choose `Send Email`.
8. Set up the action as follows:

**Action name**: email\_order\_confirmation

**When to use**: Use this action to send the order confirmation to the user. First use the get\_order action to get the user's order, then use this action to email the order confirmation to the user.

**Frequency**: Whenever applicable

**Input parameters**: We'll add the following parameters that are required to send the email:

* `email`:
  * Description: The email address where the order confirmation should be sent.
  * Save to variable: email
* `order_number`:
  * Description: The order number of the user's order.
  * Save to variable: order\_number
* `order_details`:
  * Description: The details of the order that you retrieve from the get\_order action. Format it as HTML with bullet points.
  * Save to variable: order\_details

<img src="https://chatling-assets.b-cdn.net/tutorial-1-send-email-input-parameters.jpg" width="600" alt="input parameters" />

**Email Setup**: configure the email as follows:

* Sender name: A name of your choice, for example `Apple`
* To: Type in `{{email}}` and press Enter to use the email address of the user.
* Subject: `Order confirmation for #{{order_number}}`
* Message:

```
Hi there!

As requested, here is your confirmation for order #​{{order_number}}​:

​{{order_details}}​
```

<img src="https://chatling-assets.b-cdn.net/tutorial-1-email-setup.jpg" width="600" alt="email setup" />

9. Click the `Create action` button to save the action.

## Test the actions

Now that you've set up the actions, it's time to test them.

From the `Actions` page, enable both the actions.

Go to the `Playground` page to start a chat with your agent. Ask the agent to email your order confirmation. It should fetch the order details from the API and email the order confirmation to the email address you specify.

Here's an example of how the agent would respond:

<img src="https://chatling-assets.b-cdn.net/send-email-action-sample-chat.jpg" width="350" alt="Send Email action preview" />
