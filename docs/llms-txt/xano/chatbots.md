# Source: https://docs.xano.com/building-backend-features/chatbots.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Chatbots

<CardGroup>
  <Card icon="youtube" img="/images/f0f46ccf-image.jpeg" href="https://www.xano.com/learn/introduction-to-building-with-llms-in-xano/">
    Intro to LLMs in Xano
  </Card>

  <Card icon="youtube" img="/images/bee7ac8d-image.jpeg" href="/building-backend-features/chatbots#building-a-chatbot-with-openai-chatgpt-and-xano">
    Build a Chatbot with ChatGPT & Xano
  </Card>
</CardGroup>

***

## Building a Chatbot with OpenAI/ChatGPT and Xano

<Frame>
  <iframe width="609" height="342" src="https://www.youtube.com/embed/fnH8KjiUjYc" title="Build a Chatbot with ChatGPT and Xano" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />
</Frame>

This guide will walk you through building a chatbot using ChatGPT and Xano.

Before we begin, it's important that you understand the following key concepts:

[Database Basics](/the-database/database-basics)

[Building with Visual Development](/the-function-stack/building-with-visual-development)

[APIs & Lambdas](/the-function-stack/functions/apis-and-lambdas)

[User Authentication & User Data](/building-backend-features/user-authentication-and-user-data)

You should know how to build a database table, build basic function stacks, work with user authentication, and utilize the External API Request function.

***

<Steps>
  <Step title="Understanding the OpenAI Chat Completions Endpoint">
    **Objective:** To create a chatbot, you'll primarily use OpenAI's chat completions API endpoint.

    **Endpoint:** The specific endpoint is `/v1/chat/completions`. You'll make `POST` requests to this endpoint.

    **Authentication:** All requests to the OpenAI API require authentication. This is done by including an `Authorization` header with a bearer token (your OpenAI API key).

    **Request Body:**

    * `model`: Specifies which OpenAI model to use (e.g., `gpt-3.5-turbo`). You can find compatible models in the [OpenAI documentation](https://platform.openai.com/docs/models).

    * `messages`: This is a crucial part. It's an *array* containing the *entire* conversation history. Unlike interacting directly with ChatGPT, the API requires you to send all previous messages in each request.

    * **Message Object Structure**: Each object in the `messages` array needs a `role` and `content`:

      * `role`: Defines who sent the message.

        * `system`: Sets the initial context or persona for the chatbot (the first "training" prompt).

        * `user`: Represents messages sent by the end-user interacting with the bot.

        * `assistant`: Represents messages sent *by* the chatbot (responses from the API).

      * `content`: The actual text of the message.

    **Benefits of Sending Full History:** This allows for fine-tuning or guiding the conversation by potentially modifying or constructing messages within the history you send to the API.

    **Other Parameters:** There are optional parameters like `temperature`, but they aren't required to get started.
  </Step>

  <Step title="Define Database Schema">
    **User Table:** Create at least one test user for authentication purposes later.

    **Conversation Table (**`conversation`**)**: This acts as the parent table. Add the following fields:

    * `name` (Type: text): To easily identify conversations.

    * `model` (Type: text): To store which OpenAI model is used for this conversation (e.g., "gpt-3.5-turbo").

    * `user_id` (Type: Table Reference -> `user`): To link the conversation to the user who initiated it.

    **Messages Table (**`messages`**)**: This stores individual messages. Add the following fields, mirroring the structure needed for the OpenAI API request:

    * `role` (Type: text): Stores "system", "user", or "assistant".

    * `content` (Type: text): Stores the actual message text.

    * `index` (Type: integer): A number to track the order of messages within a conversation (0, 1, 2, ...). This is crucial for sorting messages correctly for display and for sending them in the right order to the API.

    * `conversation_id` (Type: Table Reference -> `conversation`): To link the message back to its parent conversation.
  </Step>

  <Step title="Create an endpoint to call OpenAI">
    **API Group:** Navigate to your API groups in Xano. You can use the default group or create a new one.

    **New API Endpoint:** Add a new API endpoint. Choose "Start from scratch" or "Custom". Name it something descriptive, like `send_message_to_openai`.

    **Inputs:** Define the necessary inputs for this endpoint. You'll likely need:

    * `conversation_id` (Input Type: Table Reference -> `conversation`): To know which conversation this message belongs to.

    * `user_message` (Input Type: text): The new message typed by the user.

    **Function Stack:** This is where the logic happens using Xano's visual builder.

    1. **Get OpenAI API Key:** Securely retrieve your OpenAI API key. Store it in Xano's [Environment Variables](/the-function-stack/environment-variables) for security rather than hardcoding it.

    2. **Get Conversation History:**

    * Add a `Query All Records` step for the `messages` table.

    * Filter by the input `conversation_id`.

    * **Sort** by the `index` field in ascending order. This ensures messages are retrieved chronologically.

    3. **Add User's New Message to History (Temporary):** Add the incoming `user_message` to the list/array of messages retrieved in the previous step. Make sure it has the correct format: `{ "role": "user", "content": user_message }`.

    4. **Add External API Request:** This is the core step to call OpenAI.

    * Click the "+" button in the function stack and select "External API Request".

    * **Import cURL:** Use the OpenAI documentation's cURL example for the chat completions endpoint. Copy the cURL command and use Xano's "Import cURL" feature. This will pre-fill most settings.

    * **URL:** Should be `https://api.openai.com/v1/chat/completions`.

    * **Method:** `POST`.

    * **Headers:**

      * Ensure `Content-Type` is `application/json`.

      * Add the `Authorization` header. The value should be `Bearer YOUR_API_KEY`, replacing `YOUR_API_KEY` dynamically using the environment variable retrieved in step 1. Use Xano's concatenation filters or sprintf for this.

    * **Parameters/Body:**

      * Set `model` to your desired model (e.g., "gpt-3.5-turbo"). You could make this dynamic based on the `conversation` record if needed.

      * Set `messages` to the *full* conversation history array you prepared in step 3 (including the new user message).

    5. **Process API Response:** The response from OpenAI will contain the assistant's reply. You'll typically find it in `response.result.choices[0].message.content`. Add steps to extract this content.

    6. **Store Messages in Database:**

    * Add a `Add Record` step for the `messages` table to save the *user's* new message. Include `conversation_id`, `role` ("user"), `content` (`user_message`), and the next `index` number.

    * Add another `Add Record` step for the `messages` table to save the *assistant's* response. Include `conversation_id`, `role` ("assistant"), `content` (the extracted response), and the subsequent `index` number.

    7. **Response:** Define what the Xano API endpoint should return to your frontend (e.g., the assistant's message content, or the updated full conversation).
  </Step>

  <Step title="Calling from a Frontend">
    Call the Xano API endpoint (`send_message_to_openai`) from your frontend application whenever a user sends a message.

    Pass the `conversation_id` and the `user_message`.

    Display the conversation history, potentially fetching it separately using the auto-generated Xano [CRUD endpoints](/the-function-stack/building-with-visual-development/apis#auto-generated-apis) for the `messages` table, ensuring you sort by the `index` field.
  </Step>
</Steps>


Built with [Mintlify](https://mintlify.com).