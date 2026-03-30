# Create an OpenAI model using the configuration
openai_model = ModelFactory.create(
    model_platform=ModelPlatformType.OPENAI,
    model_type=ModelType.GPT_4O_MINI,
    model_config_dict=config,
)

assistant_sys_msg = """You are a helpful assistant to answer question,
         I will give you the Original Query and Retrieved Context,
        answer the Original Query based on the Retrieved Context,
        if you can't answer the question just say I don't know."""

qdrant_agent = ChatAgent(system_message=assistant_sys_msg, model=openai_model)

```

* * *

## [Anchor](https://qdrant.tech/documentation/agentic-rag-camelai-discord/\#step-6-create-and-configure-the-discord-bot)**Step 6: Create and Configure the Discord Bot**

Now let’s bring the bot to life! It will serve as the interface through which users can interact with the agentic RAG system you’ve built.

### [Anchor](https://qdrant.tech/documentation/agentic-rag-camelai-discord/\#create-a-new-discord-bot) Create a New Discord Bot

1. Go to the [Discord Developer Portal](https://discord.com/developers/applications) and log in with your Discord account.

2. Click on the **New Application** button.

3. Give your application a name and click **Create**.

4. Navigate to the **Bot** tab on the left sidebar and click **Add Bot**.

5. Once the bot is created, click **Reset Token** under the **Token** section to generate a new bot token. Copy this token securely as you will need it later.


### [Anchor](https://qdrant.tech/documentation/agentic-rag-camelai-discord/\#invite-the-bot-to-your-server) Invite the Bot to Your Server

1. Go to the **OAuth2** tab and then to the **URL Generator** section.

2. Under **Scopes**, select **bot**.

3. Under **Bot Permissions**, select the necessary permissions:

   - Send Messages

   - Read Message History
4. Copy the generated URL and paste it into your browser.

5. Select the server where you want to invite the bot and click **Authorize**.


### [Anchor](https://qdrant.tech/documentation/agentic-rag-camelai-discord/\#grant-the-bot-permissions) Grant the Bot Permissions

1. Go back to the **Bot** tab.

2. Enable the following under **Privileged Gateway Intents**:

   - Server Members Intent

   - Message Content Intent

Now, the bot is ready to be integrated with your code.

## [Anchor](https://qdrant.tech/documentation/agentic-rag-camelai-discord/\#step-7-build-the-discord-bot)**Step 7: Build the Discord Bot**

Add to your `.env` file:

```bash
DISCORD_BOT_TOKEN=<your-discord-bot-token>

```

We’ll use `discord.py` to create a simple Discord bot that interacts with users and retrieves context from Qdrant before responding.

```python
from camel.bots import DiscordApp
import nest_asyncio
import discord

nest_asyncio.apply()
discord_q_bot = DiscordApp(token=os.getenv("DISCORD_BOT_TOKEN"))

@discord_q_bot.client.event # triggers when a message is sent in the channel
async def on_message(message: discord.Message):
    if message.author == discord_q_bot.client.user:
        return

    if message.type != discord.MessageType.default:
        return

    if message.author.bot:
        return
    user_input = message.content

    retrieved_info = vector_retriever.query(
        query=user_input, top_k=10, similarity_threshold=0.6
    )

    user_msg = str(retrieved_info)
    assistant_response = qdrant_agent.step(user_msg)
    response_content = assistant_response.msgs[0].content

    if len(response_content) > 2000: # discord message length limit
        for chunk in [response_content[i:i+2000] for i in range(0, len(response_content), 2000)]:
            await message.channel.send(chunk)
    else:
        await message.channel.send(response_content)

discord_q_bot.run()

```

* * *

## [Anchor](https://qdrant.tech/documentation/agentic-rag-camelai-discord/\#step-9-test-the-bot)**Step 9: Test the Bot**

1. Invite your bot to your Discord server using the OAuth2 URL from the Discord Developer Portal.

2. Run the notebook.

3. Start chatting with the bot in your Discord server. It will retrieve context from Qdrant and provide relevant answers based on your queries.


![agentic-rag-discord-bot-what-is-quantization](https://qdrant.tech/documentation/examples/agentic-rag-camelai-discord/example.png)

* * *

## [Anchor](https://qdrant.tech/documentation/agentic-rag-camelai-discord/\#conclusion) Conclusion

Nice work! You’ve built an agentic RAG-powered Discord bot that retrieves relevant information with Qdrant, generates smart responses with OpenAI, and handles multi-step reasoning using CAMEL-AI. Here’s a quick recap:

- **Smart Knowledge Retrieval:** Your chatbot can now pull relevant info from large datasets using Qdrant’s vector search.

- **Autonomous Reasoning with CAMEL-AI:** Enables multi-step reasoning instead of just regurgitating text.

- **Live Discord Deployment:** You launched the chatbot on Discord, making it interactive and ready to help real users.


One of the biggest advantages of CAMEL-AI is the abstraction it provides, allowing you to focus on designing intelligent interactions rather than worrying about low-level implementation details.

You’re now well-equipped to tackle more complex real-world problems that require scalable, autonomous knowledge systems.

##### Was this page useful?

![Thumb up icon](https://qdrant.tech/icons/outline/thumb-up.svg)
Yes
![Thumb down icon](https://qdrant.tech/icons/outline/thumb-down.svg)
No

Thank you for your feedback! 🙏

We are sorry to hear that. 😔 You can [edit](https://qdrant.tech/github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/agentic-rag-camelai-discord.md) this page on GitHub, or [create](https://github.com/qdrant/landing_page/issues/new/choose) a GitHub issue.

On this page:

- [Edit on Github](https://github.com/qdrant/landing_page/tree/master/qdrant-landing/content/documentation/agentic-rag-camelai-discord.md)
- [Create an issue](https://github.com/qdrant/landing_page/issues/new/choose)

×

[Powered by](https://qdrant.tech/)

<|page-167-lllmstxt|>
## llama-index-multitenancy
- [Documentation](https://qdrant.tech/documentation/)
- [Examples](https://qdrant.tech/documentation/examples/)
- Multitenancy with LlamaIndex