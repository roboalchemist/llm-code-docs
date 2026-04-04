# Source: https://plivo.com/docs/aiagent/aistudio/nodereference/aiconversation.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# AI Conversation

> AI Conversation Node facilitates natural language interactions between users and the AI agent

The **AI Conversation Node** enables natural language interactions between your users and the AI Agent. This is where you define how the AI should understand and respond to user input. It supports intelligent dialogue across multiple channels such as WhatsApp, Chat Widget, SMS, and Voice.

### **Configure the AI Conversation Node**

<Frame>
  <img src="https://mintcdn.com/plivo/R0bB3pSVhMhsNJEx/aiagent/images/aiconversation11.png?fit=max&auto=format&n=R0bB3pSVhMhsNJEx&q=85&s=2352cca05ae668485faabe38ba053f26" width="2762" height="1420" data-path="aiagent/images/aiconversation11.png" />
</Frame>

When adding an AI Conversation Node to your flow, you’ll need to configure the following:

#### **1. Channel**

Select the communication channel on which this AI interaction will occur.

* By default, this should match your **trigger channel**.
* If your flow branches across multiple channels (e.g., after an outbound message), you can select a different channel here.

#### **2. Model**

Choose the LLM model for this node.

* Supported models may include GPT-4.1 and others.
* We recommend testing across models to find the right balance between response quality and latency for your use case.

#### **3. Instructions (Prompt)**

This is where you define the AI's behavior and tone for the current interaction.

* Keep your prompt clear and concise, but include:
  * What the AI should do
  * How it should respond
  * Any business rules, tone, or structure it must follow
* Structure your prompt for **multi-turn conversation**, not just a single reply
* Include references to **preceding path context** only if relevant

**You can:**

* Insert variables (e.g., customer\_name, product\_name) to personalize responses
* Attach files if needed to provide additional context

Example:\
*“You are a customer support agent. If the user asks about order status, request their order ID. If they ask about pricing, summarize our latest plan details. Keep responses friendly and concise.”*

**Variable Extraction (Optional)**

<Frame>
  <img src="https://mintcdn.com/plivo/R0bB3pSVhMhsNJEx/aiagent/images/aiconversationvariable1.png?fit=max&auto=format&n=R0bB3pSVhMhsNJEx&q=85&s=44d2c2987df757bb59e16a758d1e8424" width="2766" height="1422" data-path="aiagent/images/aiconversationvariable1.png" />
</Frame>

Use the **Extract Variables** tab to capture specific user-provided values during the interaction.

* Define variables by name and describe the expected format or content
* The AI will infer values based on this description and extract them automatically
* These extracted variables can be used in later parts of the flow (e.g., to fill a form, trigger an API, or personalize the next step)

Example:\
**Variable Name:** preferred\_callback\_time\
**Description:** “Time or time range at which the user wants to be called back, such as 'tomorrow morning' or '3pm today'.”

### **Best Practices**

* **Name your node** clearly to reflect its function in the flow (e.g., Collect Issue Description, Handle Pricing Query)
* **Include examples** in your prompt when you expect nuanced interpretation
* **Avoid overly long or vague prompts**—specificity improves reliability
* **Use extracted variables** to maintain continuity and enable dynamic actions

**Test** with varied inputs to validate both response quality and variable extraction
