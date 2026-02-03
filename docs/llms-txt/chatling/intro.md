# Source: https://docs.chatling.ai/api-reference/v2/intro.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.chatling.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# API Introduction

> The Chatling API allows you to manage your chatbots programmatically.

Integrate Chatling into your application or interact with your chatbots programmatically using our API.

This documentation guides you through creating your API key, authenticating requests, and sending requests to the API.

## Generate your API key

To send requests to the API, you must include your API key. Here's how to create it:

1. Go to your Chatling account and open the Project Settings.
2. Click the API Keys tab.
3. Press the `New API key` button.
4. Enter a name for the key and press `Generate key`.
5. Copy the newly created key. For security purposes, the API key will be displayed once only. Note it down and store it in a secure place.

If you forget your API key, you must delete it and generate a new one.

## Authentication

Your API key acts as the Bearer token and must be supplied in the `Authorization` header of every request.

<Accordion title="Example">
  ```
  Authorization: Bearer <API_KEY>
  ```
</Accordion>

## Retrieving the chatbot ID

Some endpoints require that you pass a chatbot ID as the path parameter. Here's a couple of ways to retrieve it:

* **Recommended method**: Using the `List chatbots` endpoint, you can fetch all the chatbots along with their IDs.
* Open the chatbot's settings in your account and you will find its ID listed there.
