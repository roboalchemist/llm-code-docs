# Source: https://docs.agent.ai/knowledge-agents/quickstart.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Knowledge Agent Quickstart

> Build your first action-taking knowledge agent in under 10 minutes

## What You'll Build

In this quickstart, you'll create a **Research Assistant** knowledge agent that can:

* Understand research requests in natural language
* Search its knowledge base for relevant information
* Call a workflow agent to gather additional data
* Present results conversationally

This will show you the core power of knowledge agents: combining knowledge with the ability to take action.

**Time required:** 10 minutes

## Prerequisites

Before you begin, make sure you have:

* An Agent.AI account (sign up at [agent.ai](https://agent.ai))
* Builder access enabled (click "Agent Builder" in the menu)
* At least one workflow agent created (or use one from the marketplace)

<Note>
  Don't have a workflow agent yet? That's okay! You can start with knowledge-only and add tools later. Or clone a simple workflow from the marketplace to use as a tool.
</Note>

## Step 1: Create Your Knowledge Agent

Navigate to the [Agent Builder](https://agent.ai/builder/agents) and click **"Create Agent"**.

In the modal that appears:

1. Select **"Knowledge Agent"** as the type (not workflow agent)
2. Give it a name: "Research Assistant"
3. Add a description: "Helps conduct research and gather insights"
4. Click **"Create"**

You'll be taken to the knowledge agent builder interface with 5 tabs across the top.

## Step 2: Configure Introduction Settings

You're now on the **Introduction** tab. This is where you define how your agent behaves and greets users.

### Welcome Message

In the "Welcome Message" field, enter:

```
Hi! I'm your Research Assistant. I can help you:
- Answer questions about topics in my knowledge base
- Gather additional research from the web
- Analyze information and provide insights

What would you like to research today?
```

### System Instructions

In the "System Instructions" field, enter:

```
You are a helpful research assistant. Your role is to:

1. Understand what the user wants to research
2. Search your knowledge base for relevant information
3. If needed, use the web research tool to gather additional data
4. Synthesize findings into clear, actionable insights
5. Ask clarifying questions when requests are ambiguous

Always cite your sources and be thorough in your research.
```

### Prompt Hint

In the "Prompt Hint" field (the placeholder text users see), enter:

```
Ask me to research a topic or company...
```

Click **"Save Introduction Details"** at the bottom.

<Check>
  **Checkpoint:** Your agent now has personality and clear expectations for users!
</Check>

## Step 3: Add Sample Questions

Click the **"Sample Questions"** tab at the top.

Add these example questions (one per line):

```
Research the latest trends in AI automation
Find information about sustainable energy companies
Analyze the competitive landscape for SaaS tools
Summarize key insights from recent tech news
```

These will appear as clickable suggestions when users first interact with your agent.

Click **"Update Sample Questions"**.

## Step 4: Add Knowledge to Your Agent

Click the **"Training"** tab at the top. You'll see sub-tabs for different knowledge sources.

### Option A: Upload a File (Easiest)

1. Click the **"Files"** sub-tab
2. Click **"Upload"** or drag and drop a PDF, Word doc, or text file
3. Wait for it to process (usually under 30 seconds)

Good test files to use:

* A whitepaper or research paper in your field
* Company documentation or product guides
* Meeting notes or reports

### Option B: Add a Web URL

1. Click the **"URLs"** sub-tab
2. Paste a URL (e.g., a blog post, documentation page, Wikipedia article)
3. Click **"Add URL"**
4. The content will be scraped and added to your knowledge base

### Option C: Add YouTube Video

1. Click the **"YouTube Videos"** sub-tab
2. Paste a YouTube URL
3. Click **"Add Video"**
4. The transcript will be extracted automatically

<Tip>
  Start with just ONE knowledge source for testing. You can always add more later!
</Tip>

## Step 5: Add a Workflow Agent as a Tool (Optional but Powerful)

This is where knowledge agents become truly powerful - giving them the ability to **take action**.

Click the **"Action Agents"** tab at the top.

You'll see a list of your workflow agents. Select one that makes sense for research:

**Good examples:**

* **Web Search** workflow - Searches the internet
* **Company Research** - Looks up company information
* **Data Analyzer** - Analyzes data you provide
* **Any workflow you've built** that does a specific task

Check the box next to the workflow agent(s) you want to enable.

Click **"Save Action Agents Selection"**.

<Note>
  If you don't have any workflow agents yet, skip this step for now. Your agent will still work using just its knowledge base. You can add tools later!
</Note>

<Check>
  **Checkpoint:** Your agent can now call workflow agents to accomplish tasks!
</Check>

## Step 6: Test Your Knowledge Agent

Time to see it in action!

### Start a Conversation

1. Look for the **chat interface** on the right side of your screen
2. You should see your welcome message and sample questions

### Test Knowledge Retrieval

Type a question related to the knowledge you added. For example:

* If you uploaded a research paper: "What were the main findings?"
* If you added a URL: "Summarize the key points from \[topic]"
* If you added a YouTube video: "What did they discuss about \[topic]?"

**What you should see:**

* The agent searches its knowledge base
* Responds with information from your uploaded content
* May show "\[file search]" indicator (if you're the builder)

### Test Tool Calling (if you added workflow agents)

Ask the agent to do something that requires the workflow:

* "Research the latest news about AI"
* "Find information about \[company name]"
* "Analyze \[some data or topic]"

**What you should see:**

* Agent recognizes it needs to use a tool
* Calls the appropriate workflow agent
* Shows "Calling \[workflow name]..."
* Processes the results
* Responds conversationally with the findings

<Warning>
  **If the agent doesn't call the workflow:** Make sure your system instructions mention the tool or task. Example: "Use the web search tool when you need current information."
</Warning>

## Step 7: Iterate and Improve

Based on your testing, you might want to:

### Refine System Instructions

Go back to the **Introduction** tab and adjust your system instructions to:

* Be more specific about when to use tools
* Define the tone and style you want
* Set boundaries ("Don't make things up if you don't know")

### Add More Knowledge

Go to the **Training** tab and add more documents, URLs, or videos to expand what your agent knows.

### Enable More Tools

Go to **Action Agents** and add more workflow agents for different capabilities.

### Adjust Sample Questions

Update the **Sample Questions** to better reflect what users should ask.

## What You've Built

Congratulations! You now have a working knowledge agent that:

 Greets users with a custom welcome message
 Has a defined personality and role
 Searches a custom knowledge base to answer questions
 Can call workflow agents to take actions
 Engages in natural, multi-turn conversations

## Next Steps

Now that you have a basic knowledge agent, here's how to make it even more powerful:

<CardGroup cols={2}>
  <Card title="Deep Dive: Configuration" icon="sliders" href="/knowledge-agents/configuration">
    Learn advanced system prompt techniques and personality configuration
  </Card>

  <Card title="Master the Knowledge Base" icon="book" href="/knowledge-agents/knowledge-base">
    Add all types of knowledge sources and optimize for better retrieval
  </Card>

  <Card title="Add More Tools" icon="wrench" href="/knowledge-agents/tools-integration">
    Enable MCP servers and Composio integrations for even more capabilities
  </Card>

  <Card title="Share Your Agent" icon="share-nodes" href="/knowledge-agents/conversations">
    Learn how to share conversations and make your agent public
  </Card>
</CardGroup>

## Common Issues & Solutions

<AccordionGroup>
  <Accordion title="My agent isn't using the knowledge I uploaded">
    **Possible causes:**

    * File still processing (check Training tab for status)
    * Question doesn't match knowledge content
    * Knowledge base search not finding relevant chunks

    **Solutions:**

    * Wait for file to finish processing
    * Ask questions more directly related to your content
    * Try uploading different/better formatted content
    * Check the Training tab - is the document listed?
  </Accordion>

  <Accordion title="The agent isn't calling my workflow agent">
    **Possible causes:**

    * Workflow agent not properly enabled in Action Agents tab
    * System instructions don't mention using tools
    * Agent doesn't think the tool is relevant to the request

    **Solutions:**

    * Confirm workflow is checked in Action Agents tab
    * Update system instructions to explicitly mention when to use the tool
    * Ask more directly: "Use \[workflow name] to research..."
    * Make sure your workflow agent has a clear name/description
  </Accordion>

  <Accordion title="I can't find the chat interface">
    **Solution:** The chat interface should appear on the right side of the builder. If you don't see it:

    * Make sure you're viewing an Knowledge Agent (not Workflow Agent)
    * Try refreshing the page
    * Check that you're in the builder view, not settings
  </Accordion>

  <Accordion title="Changes I made aren't showing up">
    **Solution:** Make sure you clicked the "Save" button for each section:

    * "Save Introduction Details" for Introduction tab
    * "Update Sample Questions" for Sample Questions tab
    * "Save Action Agents Selection" for Action Agents tab

    If you saved and still don't see changes, start a new conversation in the chat.
  </Accordion>

  <Accordion title="How do I start a new test conversation?">
    Look for the "New Agent Run" or "+ New Chat" button in the chat interface, usually at the top of the conversation area.
  </Accordion>
</AccordionGroup>

## Pro Tips

<Tip>
  **Tip 1: Test Early, Test Often**
  Don't wait until you've configured everything to test. Add one piece at a time and test after each change. This helps you understand what each piece does.
</Tip>

<Tip>
  **Tip 2: Start Simple, Add Complexity**
  Begin with just knowledge and a simple system prompt. Once that works, add one tool. Test again. Then add more. This iterative approach prevents overwhelming yourself.
</Tip>

<Tip>
  **Tip 3: Be Specific in System Instructions**
  Instead of "You are helpful," try "You help users research companies by first searching your knowledge base, then using the web research tool if needed, and presenting findings in bullet points."
</Tip>

<Tip>
  **Tip 4: Use Sample Questions to Guide Users**
  Your sample questions train users on what your agent can do. Make them specific and actionable, like examples you want users to follow.
</Tip>

<Tip>
  **Tip 5: Name Tools Clearly**
  If you're enabling workflow agents, make sure they have descriptive names like "Web Search Tool" or "Company Research Agent" so the AI knows when to use them.
</Tip>

## You're Ready!

You've built your first knowledge agent and seen how it combines conversational AI with knowledge and action. The pattern is the same for any knowledge agent you build:

1. Define personality (system instructions)
2. Add knowledge (training)
3. Enable tools (action agents, MCP, integrations)
4. Test and iterate

Now go build something amazing!
