# Source: https://docs.base44.com/Building-your-app/AI-agents-for-apps.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.base44.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Setting up an AI agent for your app

> Turn chats into smart assistants that take action, connect to tools, and help you get more done in your Base44 app.

AI agents turn simple chats into actions in your Base44 app. Instead of only replying with text, they update records, trigger workflows, and connect to tools so you can run more of your process through one conversation.

<Frame caption="Using an AI agent to take actions and manage data in your app">
    <img src="https://mintcdn.com/base44/02mCHA3V8IoPuJPu/images/aiagentexample.png?fit=max&auto=format&n=02mCHA3V8IoPuJPu&q=85&s=69871b6fa784c49f5ecba618e29da429" alt="Aiagentexample" width="2252" height="1552" data-path="images/aiagentexample.png" />
</Frame>

Each agent understands your app’s data and can search the web, call backend functions, and follow detailed guidelines you define. You can shape its tone and persona, decide which tools it can use, and choose the AI model that powers its reasoning. By default, agents use an **Automatic** model that is optimized for fast, cost-effective responses, so everything keeps working the same as before unless you decide to change it.

When you enable memory, your agent can also remember important details across conversations, such as preferences, past choices, or shared knowledge. It then brings that context back the next time someone reaches out, so every interaction feels more personal and consistent.

Agents automatically figure out which tool to use based on your app and request.

<Tip>
  Examples:

  * “Mark my summer vacation booking as done” → uses the **update\_task** tool.
  * “What was the most visited location in Europe in 2024?” → uses the **google\_search** tool.
  * “Add 15 new tasks” → uses the **insert\_task\_records** tool.
</Tip>

***

## Setting up an AI agent

Before you can start working with AI agents, you need to enable them in your app dashboard. Then you can start creating them using the AI chat.

You can enable agents for all new apps by default in your account settings in your workspace.

<Note>
  When you chat with an AI agent, Base44 uses **integration credits**. Pricing starts at around **3 integration credits per message** with the default model and then varies based on the model you select and the length of the response.
</Note>

**To set up an AI agent:**

1. Go to **Dashboard** in your app editor.
2. Click **Agents**.
3. Turn on the **AI Agents** toggle.
4. Use the AI chat to create an agent and define its role and tasks.

<Frame caption="Enabling AI agents in your Base44 app">
  <img className="mx-auto hidden dark:block" style={{ width:"95%" }} src="https://mintcdn.com/base44/WI-Bgc-fu3HNvZuA/images/enableagent-1.png?fit=max&auto=format&n=WI-Bgc-fu3HNvZuA&q=85&s=6304835415e70fb77cca8b245eec5fb8" alt="Enabling AI agents in your Base44 app" width="2320" height="1482" data-path="images/enableagent-1.png" />

  <img className="mx-auto dark:hidden" style={{ width:"95%" }} src="https://mintcdn.com/base44/WI-Bgc-fu3HNvZuA/images/enableagent.png?fit=max&auto=format&n=WI-Bgc-fu3HNvZuA&q=85&s=401d9a3d2e8fbad8644239afa71f0bec" alt="Enabling AI agents in your Base44 app" width="2320" height="1482" data-path="images/enableagent.png" />
</Frame>

<Tip>
  **Example prompts:**

  * Build me a task manager with an AI assistant to help organize and manage my tasks.
  * Create a daily journal powered by a reflection agent that asks thoughtful questions and offers new perspectives.
  * Design a warehouse inventory system with an intelligent agent that tracks stock levels, flags shortages, and automates restocking suggestions.
</Tip>

***

## Customizing your AI agent

Each agent has its own configuration panel with 4 main sections:

* **Guidelines:** Define the agent’s behavior, persona, and AI model.
* **Tools:** Control what data and tools the agent can use.
* **Memory:** Decide how the agent remembers information across conversations.
* **WhatsApp:** Connect the agent to WhatsApp so people can chat from their phone.

### Guidelines and AI model

Use the **Guidelines** tab to set how your agent behaves and which AI model it uses.

<Frame caption="Configuring the description, instructions and AI model for your agent">
    <img src="https://mintcdn.com/base44/bahRR0tOrL8be9Ib/images/agentguidelines-2.png?fit=max&auto=format&n=bahRR0tOrL8be9Ib&q=85&s=82c9d17bfbf5bc51cfcc3faabe8320da" alt="Agentguidelines 2" width="2304" height="1754" data-path="images/agentguidelines-2.png" />
</Frame>

**To customize guidelines and the AI model:**

1. Go to **Dashboard** in your app editor.
2. Click **Agents**.
3. Click **Edit Agent** on the relevant agent.
4. Click **Guidelines**.
5. Update the **Description** to define the agent’s role and high-level behavior.
6. Update **Instructions** with detailed rules your agent should follow.
7. Under **AI Model**, choose how the agent is powered. Keep **Automatic** selected to use a fast, cost-effective model (based on **Gemini 2.5 Flash**), or select a different model from Google Gemini, OpenAI GPT, or Anthropic Claude if you need more advanced reasoning or specific provider behavior.
8. Click **Save**.

<Card icon="sparkles" title="Choosing an AI model">
  For most agents you can use the **Automatic** option. It is optimized for general-purpose tasks and interactive workflows and typically costs about **3 integration credits per message**.

  If you need more control, you can pick a different model. Below is an estimation of credit usafe with different models:

  | Model                        | Best for                                     | Approx. credits / message |
  | ---------------------------- | -------------------------------------------- | ------------------------- |
  | Automatic (Gemini 2.5 Flash) | General-purpose, fast responses              | \~3                       |
  | Gemini 3 Flash               | Stronger reasoning at moderate cost          | \~5                       |
  | GPT-5                        | Complex analysis and accuracy-critical tasks | \~15                      |

  Credits are approximate and vary based on response length. Lighter models use fewer credits, while more powerful models use more. You can switch models at any time if your needs change.
</Card>

<Tip>
  If you are not sure which model to use, leave **Automatic** selected. You can always move to a more powerful model later for advanced reasoning or analysis-heavy workflows.
</Tip>

### Tools and data access

Use the **Tools** tab to decide what your agent can do and which data it can access.

<Frame caption="Setting the tools and capabilities of your agent">
    <img src="https://mintcdn.com/base44/02mCHA3V8IoPuJPu/images/agenttools.png?fit=max&auto=format&n=02mCHA3V8IoPuJPu&q=85&s=9512edabe4533884db18973a2531e037" alt="Setting the tools and capabilities of your agent" width="2304" height="1626" data-path="images/agenttools.png" />
</Frame>

**To manage an agent’s tools:**

1. Go to **Dashboard** in your app editor.
2. Click **Agents**.
3. Click **Edit Agent** on the relevant agent.
4. Click **Tools**.
5. Choose which tools the agent can use. For example:
   * Entity tools to create, read, update, or delete records.
   * Backend functions to send notifications, trigger automations, or call external APIs.
6. Adjust any tool-specific permissions so the agent only accesses the data it needs.
7. Click **Save**.

<Tip>
  You can add or remove tools at any time as your app evolves. For example, you might start with read-only entity tools and later allow updates once you have tested the agent.
</Tip>

### Agent memory

Agent memory lets your agent remember important information across conversations, such as preferences, key facts, or shared knowledge. You control whether memories are shared across everyone or kept specific to each person.

<Frame caption="Enabling memory for your agent">
    <img src="https://mintcdn.com/base44/Fcx-XLjjXXAVJ8ud/images/memory.png?fit=max&auto=format&n=Fcx-XLjjXXAVJ8ud&q=85&s=e7aaf596fd7bc9bd790036cd57f01696" alt="Enabling memory for your agent" width="2300" height="1628" data-path="images/memory.png" />
</Frame>

**To turn on memory for your agent:**

1. Go to **Dashboard** in your app editor.
2. Click **Agents**.
3. Click **Edit Agent** on the relevant agent.
4. Click **Memory**.
5. Click the **Enable Memory** toggle to turn memory on.
6. Under **Memory Scope**, choose how this agent saves memories:
   * **Global & Per User:** The agent can create shared memories for everyone and personal memories for each person.
   * **Global Only:** The agent creates memories that are shared across everyone who chats with it.
   * **Per User Only:** The agent creates memories that are specific to each person.
7. In **Memory Instructions**, enter guidance that explains when to save memories and what to include.
8. After your agent has a few conversations, review **Saved Memories** to see what the agent has stored. Click **Refresh** to load new memories.
9. Click **Save**.

<Tip>
  Use memory instructions to keep your agent focused. For example:

  * Save global memories for product updates, company announcements, and shared knowledge.
  * Save user memories for personal preferences such as communication style, tone, and specific interests.
</Tip>

### Connecting your agent to WhatsApp

Connect your agent to WhatsApp so people can message your app’s agent directly from their phone, without even opening the app.

<Frame caption="Connecting your agent to WhatsApp">
  <img src="https://mintcdn.com/base44/CZhPr69886UYCUiS/images/2025-09-21_21-37-57.png?fit=max&auto=format&n=CZhPr69886UYCUiS&q=85&s=d318fe0c20651efe061b44b4539c7bcd" alt="Connecting your agent to WhatsApp" title="Connecting your agent to WhatsApp" className="mx-auto" style={{ width:"53%" }} width="812" height="836" data-path="images/2025-09-21_21-37-57.png" />
</Frame>

A WhatsApp-connected agent can do everything your in-app agent does. This includes creating, reading, updating, or deleting entities in your app, triggering backend functions such as sending notifications or starting automations, and managing your app’s data, like updating tasks and adding records. If your agent can do it inside your app, it can do it in WhatsApp too.

<Frame caption="Using your agent in WhatsApp">
    <img src="https://mintcdn.com/base44/nl5ZIfqz-UsozDtU/images/2025-09-21_21-49-13.png?fit=max&auto=format&n=nl5ZIfqz-UsozDtU&q=85&s=ed40adc03dcad3cf219bb778fbbc0ff9" alt="Using your agent in WhatsApp" width="2274" height="1142" data-path="images/2025-09-21_21-49-13.png" />
</Frame>

<Card icon="hexagon-exclamation" title="Information about using WhatsApp with your agent">
  * This feature is available for free on all plans.
  * A total of 3 agents can be connected to WhatsApp across all your apps. If you try to connect more than 3, you’ll be prompted to disconnect one before continuing.
  * Each agent is assigned its own WhatsApp number.
  * Every message sent or received with your WhatsApp agent uses **1 integration credit**. Credits are also used for agent actions like calling LLMs, querying your database, generating images, or sending emails.
  * Your app visitors don’t need to install anything to use WhatsApp agents. They simply tap the WhatsApp button in your app to start a chat. People must send the first message, to help prevent spam and keep them safe. Once the conversation begins, the agent can reply just like it does inside your app.
  * WhatsApp conversation supports both images and voice messages.
  * If your app is public, people need to log in to your app before they can use the WhatsApp agent. This makes sure the agent can identify who it is chatting with and respond based on their data.
</Card>

**To enable WhatsApp for your agent:**

1. Go to **Dashboard** in your app editor.
2. Click **Agents**.
3. Click **Edit Agent** on the relevant agent.
4. Click **WhatsApp**.
5. Click **Send to Chat** under **Add WhatsApp to Your App** to add a WhatsApp button to your app.
6. Customize the WhatsApp welcome message.
7. Click **Save**.

***

## FAQs

Click a question below to learn more about AI agents.

<AccordionGroup>
  <Accordion title="Why do I see a “Failed to send message” or 404 error when messaging an agent?">
    This can happen if there’s an empty entity in the agent’s **Tools and Capabilities** settings.

    **To resolve this:**

    1. Open your agent’s settings.
    2. Click the **Tools and Capabilities** tab.
    3. Either update or remove the empty entity.
    4. Click **Save**.

        <img src="https://mintcdn.com/base44/6XWEgotcf7zRG5nD/images/AgentToolsEntities.png?fit=max&auto=format&n=6XWEgotcf7zRG5nD&q=85&s=59d51c6d903d1f9965119453c8ae6d13" alt="Tools and capabilities to configure for your Base44 AI agent." width="1143" height="733" data-path="images/AgentToolsEntities.png" />

    After updating, you should be able to send messages without errors.
  </Accordion>

  <Accordion title="Can I use agents on the free plan?">
    Yes. Agents are available on all plans, including the Free plan.
  </Accordion>

  <Accordion title="Can I enable agents for all apps in my account?">
    You can turn agents on by default for every new app you create.

    When the **Enable agents for new apps by default** toggle is on in your **Account settings**, each new app automatically has the **AI Agents** toggle enabled in its dashboard so you can start adding and configuring agents right away.

    This setting does not change existing apps. To enable or disable agents for an existing app, open that app’s **Dashboard**, click **Agents**, and adjust the **AI Agents** toggle there.

    **To turn on agents by default for new apps:**

    1. Click your profile icon at the top right of your workspace.
    2. Click **Settings**.
    3. Click **Account settings**.
    4. Turn on the **Enable agents for new apps by default** toggle in the **Default Agents** section.

    <Frame>
            <img src="https://mintcdn.com/base44/WI-Bgc-fu3HNvZuA/images/defaultagentsaccount.png?fit=max&auto=format&n=WI-Bgc-fu3HNvZuA&q=85&s=13eeb7216755ab853bbadc84124068bf" alt="Defaultagentsaccount" width="3064" height="1036" data-path="images/defaultagentsaccount.png" />
    </Frame>
  </Accordion>

  <Accordion title="What are the benefits of using agents?">
    Agents are flexible powerful tools that help you:

    * Automate repetitive tasks.
    * Get informed, real-time answers.
    * Keep your workflow inside one app.
    * Pick the right tools automatically.
  </Accordion>

  <Accordion title="Where can I find my conversation history with an agent?">
    **To view conversation history:**

    1. Go to **Dashboard** in your app editor.
    2. Click the **Agents** tab.
    3. Click the **Conversation** tab.
    4. Click on a past conversation you want to review or reenter.

        <img src="https://mintcdn.com/base44/6XWEgotcf7zRG5nD/AIAgentsManage.png?fit=max&auto=format&n=6XWEgotcf7zRG5nD&q=85&s=6b2d6ac6b019db6254925a8c4b9733f6" alt="Managing your AI Agents and conversations in Base44." width="1177" height="838" data-path="AIAgentsManage.png" />
  </Accordion>

  <Accordion title="How does the AI model I choose affect credits and behavior?">
    The AI model you choose affects both how your agent behaves and how many integration credits it uses.

    * The default **Automatic** option (based on Gemini 2.5 Flash) gives you fast, general-purpose responses at around **3 credits per message**.
    * Models such as **Gemini 3 Flash** provide stronger reasoning at a moderate increase in credits.
    * Higher-end models such as **GPT-5** are designed for complex analysis and accuracy-critical decisions and generally use more credits per message.

    If you are not sure which model to use, keep **Automatic** selected so you get a good balance of speed, quality, and cost.
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).