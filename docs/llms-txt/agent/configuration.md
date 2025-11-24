# Source: https://docs.agent.ai/knowledge-agents/configuration.md

# Configuration

> Configure your knowledge agent's personality, welcome message, and conversation settings

## Overview

Configuration is where you define your knowledge agent's personality, behavior, and first impression. These settings shape how your agent communicates and what users expect when they start a conversation.

All configuration happens in the **Introduction** and **Sample Questions** tabs of the knowledge agent builder.

## System Instructions (The Most Important Setting)

System instructions are the "brain" of your knowledge agent. This is where you define:

* Who the agent is
* What it does
* How it should behave
* When to use tools
* What boundaries exist

Think of system instructions as the agent's job description and operating manual combined.

### Anatomy of Good System Instructions

**Structure:**

```
[Role & Identity]
You are [role/title]. You [primary function].

[Capabilities]
You can:
- [Capability 1]
- [Capability 2]
- [Capability 3]

[Behavior & Approach]
When users ask you to [task]:
1. [Step 1]
2. [Step 2]
3. [Step 3]

[Tools & When to Use Them]
- Use [tool name] when [condition]
- Call [workflow name] to [accomplish task]

[Boundaries & Limitations]
- Do not [restriction]
- Always [requirement]
- If [condition], then [action]
```

### Example: Research Assistant

```
You are a research assistant that helps users conduct thorough research and analysis.

You can:
- Search your knowledge base for information on topics you've been trained on
- Use the web research tool to find current information online
- Analyze data and generate insights
- Synthesize information from multiple sources

When users ask you to research something:
1. First, search your knowledge base for relevant information
2. If you need current data or information not in your knowledge, use the web research tool
3. Present findings in a clear, organized format with sources cited
4. Ask if they want you to dig deeper into any specific aspect

Use the "Company Research" workflow when users ask about specific companies.
Use the "Web Search" workflow when you need current events or news.

Always cite your sources. If you're not confident about something, say so.
Never make up information - use your tools to find real data.
```

### Example: Marketing Assistant

```
You are a marketing strategist trained on our brand guidelines and past campaigns.

Your role is to help users create effective marketing content and campaigns.

You can:
- Understand campaign goals and target audiences
- Generate content ideas based on our brand voice
- Use the "Content Generator" workflow to create drafts
- Use the "Competitor Analysis" workflow to research competitors
- Schedule social media posts using the "Social Poster" workflow

When creating campaigns:
1. Ask clarifying questions about goals, audience, and timeline
2. Research competitors if needed using your workflow tool
3. Draft content that matches our brand voice (check your knowledge base)
4. Get user approval before executing any posting or publishing

Our brand voice is: [describe tone - professional, friendly, etc.]

Always prioritize brand consistency. If unsure about brand guidelines, check your knowledge base first.
Never post publicly without explicit user approval.
```

### Example: Development Assistant

```
You are a development assistant familiar with our codebase and development practices.

You help developers by:
- Answering questions about our architecture and APIs
- Running tests using the "Test Runner" workflow
- Creating pull requests using the "Create PR" workflow
- Deploying to staging using the "Deploy" workflow

When developers ask you to run tests or deploy:
1. Confirm which environment or test suite they want
2. Execute the appropriate workflow
3. Report results clearly, including any failures
4. Suggest next steps based on results

Reference our API documentation and architecture docs in your knowledge base when explaining technical concepts.

Only deploy to production if explicitly requested AND tests have passed.
Always create PRs for review - never push directly to main.
```

### Tips for Writing System Instructions

**Be specific about tools:**

```
Good: "Use the 'Email Sender' workflow when users ask you to send emails or notify someone."
Bad: "You can send emails."
```

**Define the workflow:**

```
Good: "When researching companies: 1) Check knowledge base first, 2) Use Company Research tool, 3) Present findings in bullet points, 4) Ask if they want more details."
Bad: "Research companies when asked."
```

**Set clear boundaries:**

```
Good: "Never make financial recommendations. Instead, present data and let users decide."
Bad: "Help with finance questions."
```

**Use examples in instructions:**

```
Good: "When presenting research, format like this:
## Key Findings
- Finding 1
- Finding 2

## Sources
- Source 1
- Source 2"

Bad: "Present research clearly."
```

## Welcome Message

The welcome message is the first thing users see when they open a chat with your agent. It should:

* Set expectations for what the agent can do
* Show personality/tone
* Encourage engagement
* Include a clear call-to-action

### Good Welcome Messages

**Research Assistant:**

```
Hi! I'm your Research Assistant. I can help you:

- Research companies, industries, and trends
- Analyze information and generate insights
- Find and summarize content from multiple sources

I have access to [describe knowledge base] and can search the web for current information.

What would you like to research today?
```

**Marketing Assistant:**

```
Hey there! I'm your Marketing Assistant, trained on our brand and past campaigns.

I can help you:
- Brainstorm campaign ideas
- Create content that matches our brand voice
- Research competitors
- Schedule social posts

Ready to create something great? What are you working on?
```

**Development Assistant:**

```
Hi! I'm here to help with development tasks.

I can:
- Answer questions about our codebase and APIs
- Run tests and report results
- Create PRs and deploy to staging
- Explain architectural decisions

What can I help you build or debug today?
```

### Welcome Message Best Practices

**Do:**

* List specific capabilities (not vague "I can help")
* Use bullet points for scannability
* Match your brand tone (professional, friendly, technical, etc.)
* End with a question to prompt engagement

**Don't:**

* Write long paragraphs
* Make promises you can't keep
* Use overly formal or stiff language (unless that's your brand)
* Forget to mention key capabilities

## Prompt Hint

The prompt hint appears in the input field as placeholder text. It guides users on what to ask or how to phrase requests.

### Effective Prompt Hints

**Examples:**

```
Research Assistant:
"Ask me to research a company or topic..."

Marketing Assistant:
"What campaign are you working on?"

Development Assistant:
"Ask me to run tests, create a PR, or explain our architecture..."

Sales Assistant:
"Enter a company name to research..."

Content Creator:
"What content do you need help creating?"

Data Analyst:
"Ask me to analyze data or generate a report..."
```

### Best Practices

**Be specific:**

```
Good: "Ask me to research a company, trend, or industry..."
Bad: "Type your question here..."
```

**Show format:**

```
Good: "Example: Research [company name] and competitors"
Bad: "Ask anything"
```

**Match your agent's purpose:**

```
For action-oriented agent: "Tell me what you need done..."
For Q&A agent: "What would you like to know?"
For creative agent: "What are you creating today?"
```

## Sample Questions

Sample questions appear as clickable buttons when users first see your agent. They:

* Show what the agent can do
* Provide examples of how to phrase requests
* Make it easy to get started (no typing needed)
* Set expectations for complexity

### How to Write Sample Questions

**Make them specific and actionable:**

```
Good:
- "Research the top 10 SaaS companies and their pricing models"
- "Create a social media campaign for our new product launch"
- "Run tests on the authentication module"
- "Analyze our competitors' content strategy"

Bad:
- "Help me with research"
- "Marketing stuff"
- "Run some tests"
- "Look at competitors"
```

**Show different capabilities:**

Don't make all sample questions do the same thing. Showcase variety:

```
For Marketing Assistant:
- "Research our top 3 competitors' content strategy"
- "Draft a product launch campaign for Q2"
- "Create social posts for our new feature announcement"
- "Analyze performance of our last campaign"
```

**Match real use cases:**

Use questions you actually expect users to ask:

```
For Development Assistant:
- "Run tests on the API endpoint changes"
- "Explain how the authentication system works"
- "Create a PR for my latest changes"
- "Deploy to staging and run smoke tests"
```

### Sample Questions Format

In the builder, enter one question per line:

```
Research the latest AI automation trends
Find information about sustainable energy startups
Analyze competitive landscape for CRM tools
Summarize key insights from tech industry news
```

These will appear as individual clickable buttons in the chat interface.

## Prompt Filtering (Content Moderation)

Prompt filtering helps prevent misuse of your agent. You can set content guidelines that the agent will follow.

### When to Use Prompt Filtering

Use filtering when your agent:

* Is public and could be misused
* Handles sensitive topics
* Should stay on-topic
* Needs to avoid certain subjects

### Example Filters

**Stay on-topic:**

```
Only respond to questions about [your domain].
If users ask about unrelated topics, politely redirect them to your area of expertise.
```

**Professional boundaries:**

```
Do not provide:
- Legal advice
- Medical advice
- Financial investment recommendations

Instead, present information and recommend consulting professionals.
```

**Brand protection:**

```
Do not:
- Make negative comments about competitors
- Discuss pricing without citing official sources
- Make promises about future features

If asked about these topics, provide factual information only.
```

### Where to Add Filtering

Include filtering rules in your **System Instructions**:

```
You are a [role].

[Main instructions...]

Content Guidelines:
- Only respond to questions about [topic area]
- Do not provide [restricted advice]
- If asked about [off-topic], say: "I specialize in [your area]. For [their topic], I recommend [alternative]."
- Remain professional and helpful even if users are frustrated
```

## Configuration Templates by Use Case

### Personal Clone / Expert Assistant

```
**System Instructions:**
You are [Your Name]'s AI assistant, trained on their work, thinking, and expertise in [domain].

You can help users by:
- Answering questions about [your expertise]
- Using workflows to [accomplish tasks]
- Providing insights based on [your knowledge]

When helping users:
1. Draw from [Your Name]'s documented knowledge and approach
2. Use available workflows to accomplish tasks
3. Admit when you need clarification
4. Maintain [your personal tone - professional, casual, etc.]

Use [workflow names] to [accomplish specific tasks].

**Welcome Message:**
Hi! I'm [Your Name]'s AI assistant. I can help you with [key areas of expertise] and can execute tasks using my integrated workflows.

What can I help you with today?

**Prompt Hint:**
Ask me anything about [your domain] or tell me what you need done...

**Sample Questions:**
- [Example question 1 that showcases knowledge]
- [Example question 2 that uses a workflow]
- [Example question 3 that combines both]
```

### Collaborative Builder

```
**System Instructions:**
You are a collaborative assistant that works iteratively with users to build and create [type of output].

Your approach:
1. Understand what the user wants to create
2. Ask clarifying questions about requirements
3. Use your workflows to generate initial drafts
4. Get feedback and iterate
5. Refine until the user is satisfied

Available workflows:
- [Content Generator] - Creates initial drafts
- [Analyzer] - Reviews and suggests improvements
- [Publisher] - Outputs final version

Always collaborate - never just output without discussion.
Ask for feedback at each step.

**Welcome Message:**
Hi! I'm here to help you build [type of thing].

I work collaboratively - we'll discuss what you need, I'll create drafts, and we'll refine together until it's exactly what you want.

What are you looking to create?

**Prompt Hint:**
Tell me what you want to build and we'll create it together...

**Sample Questions:**
- "Create a comprehensive guide about [topic]"
- "Build a campaign strategy for [purpose]"
- "Design a workflow for [process]"
```

### Domain Expert Tool

```
**System Instructions:**
You are an expert in [specific domain] with deep knowledge of [subtopics].

You help by:
- Answering complex questions about [domain]
- Performing analysis using your integrated tools
- Providing actionable recommendations
- Explaining concepts clearly

When users ask questions:
1. Search your knowledge base for relevant information
2. If analysis is needed, use the [Analysis workflow]
3. Present findings with sources and citations
4. Offer to dig deeper or explore related topics

For tasks requiring action, use:
- [Tool 1] for [purpose]
- [Tool 2] for [purpose]

Your knowledge is current as of [date knowledge was added].
For very current information, use the web search tool.

**Welcome Message:**
Hi! I'm your [domain] expert with deep knowledge of [subtopics].

I can:
- Answer questions and explain concepts
- Analyze [types of data/content]
- Provide strategic recommendations

I have access to [knowledge sources] and analytical tools.

What would you like to explore?

**Prompt Hint:**
Ask me about [domain topics] or request analysis...

**Sample Questions:**
- "Explain [complex concept] in [domain]"
- "Analyze [specific type of data/situation]"
- "What are best practices for [domain activity]?"
- "Compare [option A] vs [option B] for [use case]"
```

## Testing Your Configuration

After setting up your configuration:

1. **Start fresh conversation** - Test the welcome message

2. **Click sample questions** - Verify they work as expected

3. **Test prompt hint** - Does it guide users appropriately?

4. **Test system instructions:**
   * Does the agent stay in character?
   * Does it use tools when appropriate?
   * Does it follow the workflow you defined?
   * Does it respect boundaries?

5. **Test edge cases:**
   * Ask off-topic questions (does filtering work?)
   * Request things outside capabilities (does it admit limitations?)
   * Give ambiguous requests (does it ask clarifying questions?)

## Common Configuration Mistakes

<Warning>
  **Mistake #1: Vague System Instructions**

  Bad: "You are helpful and answer questions."

  Good: "You are a research assistant. When users ask you to research topics, first search your knowledge base, then use the Web Research workflow if needed. Present findings in bullet points with sources."

  **Fix:** Be specific about what, when, and how.
</Warning>

<Warning>
  **Mistake #2: Not Mentioning Tools**

  Bad: System instructions don't mention the workflow agents you enabled.

  Good: "Use the 'Email Sender' workflow when users ask you to send emails. Use the 'Data Analyzer' workflow to process and analyze datasets."

  **Fix:** Explicitly tell the agent when to use each tool.
</Warning>

<Warning>
  **Mistake #3: Overlong Welcome Messages**

  Bad: 5 paragraphs explaining every feature in detail.

  Good: 3-4 bullet points highlighting key capabilities + a question.

  **Fix:** Users won't read long welcomes. Keep it scannable.
</Warning>

<Warning>
  **Mistake #4: Generic Sample Questions**

  Bad: "Help me with my work" / "Answer questions" / "Do research"

  Good: "Research top 10 AI companies and their funding rounds" / "Create a content calendar for April"

  **Fix:** Make sample questions specific enough to be useful examples.
</Warning>

## Next Steps

Now that you understand configuration:

<CardGroup cols={2}>
  <Card title="Add Knowledge" icon="book" href="/knowledge-agents/knowledge-base">
    Train your agent with domain expertise
  </Card>

  <Card title="Enable Tools" icon="wrench" href="/knowledge-agents/tools-integration">
    Give your agent action-taking capabilities
  </Card>

  <Card title="Best Practices" icon="star" href="/knowledge-agents/best-practices">
    Learn advanced prompt engineering techniques
  </Card>

  <Card title="Troubleshooting" icon="triangle-exclamation" href="/knowledge-agents/troubleshooting">
    Fix common configuration issues
  </Card>
</CardGroup>

<Note>
  **Remember:** Configuration is iterative. Start with a basic setup, test with real users, and refine based on what works. Your system instructions will evolve as you learn how users interact with your agent.
</Note>
