# Source: https://docs.agent.ai/knowledge-agents/conversations.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Conversations & Sharing

> Manage conversations, share your knowledge agent, and create great user experiences

## How Conversations Work

When someone interacts with your knowledge agent, each interaction creates a **conversation**. Think of conversations like chat threads - they have:

* **History** - All messages in the conversation
* **Context** - The AI remembers previous messages
* **Auto-generated titles** - AI creates descriptive names
* **Shareable links** - Can be shared publicly
* **Forking** - Others can copy and continue from any point

Each conversation is isolated - what happens in one doesn't affect others.

## Conversation Lifecycle

```
User opens your knowledge agent
        ↓
New conversation created automatically
        ↓
User and agent exchange messages
        ↓
AI generates a descriptive title
        ↓
Conversation saved to history
        ↓
User can share, fork, or continue later
```

## Auto-Generated Titles

Your knowledge agent automatically generates descriptive titles for conversations after the first few messages.

**How it works:**

* AI analyzes the conversation topic
* Generates a concise, descriptive title
* Title appears in conversation history
* Makes it easy to find past conversations

**Examples of auto-generated titles:**

* "Researching AI automation competitors"
* "Creating social media campaign for product launch"
* "Analyzing Q3 sales data and trends"
* "Debugging authentication module errors"

**You can't customize the title format**, but you can influence it through:

* Clear user requests (AI titles based on main topic)
* Focused conversations (don't jump between unrelated topics)

<Tip>
  If a conversation covers multiple topics, the AI typically titles it based on the first major topic discussed.
</Tip>

## Conversation History

All conversations are automatically saved and accessible from the conversation history panel.

### Accessing Your Conversations

**As the agent builder:**

1. Open your knowledge agent
2. Look for the conversation list (usually left sidebar)
3. See all conversations sorted by most recent
4. Click any conversation to reopen it

**For users interacting with your agent:**

1. Conversations are saved in their account
2. They can return and continue conversations
3. History persists across sessions

### What's Saved

Each conversation stores:

* All messages (user and agent)
* Tool calls made
* Knowledge retrieved
* Timestamps
* Auto-generated title

<Note>
  **Privacy note:** Builders can see conversations with their own knowledge agents. Consider this when deciding what features to enable on public agents.
</Note>

## Sharing Conversations

One of the most powerful features of knowledge agents is the ability to share individual conversations via public links.

### How to Share a Conversation

1. **Have a conversation** with your knowledge agent
2. **Look for the share icon** (usually top-right of conversation)
3. **Click to generate a shareable link**
4. **Copy and share** the link anywhere

The link looks like: `https://agent.ai/chat/[conversation-id]`

### What Shared Links Include

When someone opens a shared conversation link, they see:

* **Full conversation history** - All messages in the conversation
* **Read-only view** - They can read but not modify the original
* **Fork option** - They can copy the conversation and continue it
* **Agent information** - Who built it, description

### Use Cases for Sharing

**Showcase examples:**

```
Share great examples of your knowledge agent in action:
- Marketing campaigns it created
- Research it conducted
- Code it helped debug
- Reports it generated

Use these as portfolio pieces or demos.
```

**Collaborative work:**

```
Work with someone on a project:
- Start conversation with your knowledge agent
- Get to a point where you want input
- Share link with colleague
- They can fork and continue
```

**Support and troubleshooting:**

```
If something isn't working:
- Create a conversation showing the issue
- Share with support or the agent builder
- They can see exactly what happened
```

**Teaching and examples:**

```
Create example conversations showing:
- How to use the agent effectively
- What kinds of questions to ask
- Sample workflows end-to-end

Share these as tutorials.
```

### Privacy Considerations

<Warning>
  **Important:** Shared conversation links are **public** - anyone with the link can view the conversation.

  **Don't share conversations containing:**

  * Personal information (emails, phone numbers, addresses)
  * Confidential business data
  * API keys, passwords, or credentials
  * Private customer information
  * Sensitive internal discussions

  **Before sharing, review the entire conversation** to ensure nothing sensitive is included.
</Warning>

### Best Practices for Sharing

**Do:**

* Review the conversation before sharing
* Share conversations that demonstrate value
* Use as examples in documentation
* Share success stories and use cases
* Include context when sharing (explain why it's interesting)

**Don't:**

* Share sensitive information
* Share conversations with errors if showcasing capabilities
* Share incomplete conversations that might confuse viewers
* Assume shared links are private (they're public)

## Forking Conversations

**Forking** lets users copy a conversation and continue it themselves. This creates powerful collaboration and learning opportunities.

### How Forking Works

```
Original conversation (shared by builder)
        ↓
User clicks "Fork" or "Continue this conversation"
        ↓
Exact copy created in user's account
        ↓
User can now continue the conversation
        ↓
Original conversation unchanged
```

### When Users Might Fork

**To build on examples:**

```
Builder shares: "Here's how to research competitors"
User forks: Continues with their own competitor list
```

**To customize for their needs:**

```
Builder shares: "Campaign strategy for SaaS product"
User forks: Adapts strategy for their specific product
```

**To learn and experiment:**

```
Builder shares: "Complex data analysis workflow"
User forks: Tries with their own data
```

**To collaborate asynchronously:**

```
Team member 1 starts conversation
Shares link
Team member 2 forks and continues
Shares updated version back
```

### Enabling Productive Forking

As a builder, you can encourage forking by:

**Creating "template" conversations:**

* Start a conversation with your agent
* Walk through a complete workflow
* Stop at a point where users can customize
* Share with instruction: "Fork this and add your data"

**Example:**

```
Title: "Competitor Research Template"

Conversation:
Agent: "I'll help you research competitors. What industry are you in?"
[Builder]: "SaaS"
Agent: "Great! I'll research SaaS competitors. Which companies should I analyze?"
[Builder]: "Add your companies here →"

[Share this - users fork and replace with their companies]
```

**Building progressive examples:**

* Share multiple conversations showing progression
* Each one builds on the previous
* Users can fork at any stage
* Creates learning pathways

## Managing Conversations as a Builder

### Testing Your Agent

As you build and refine your knowledge agent, you'll have many test conversations:

**Organizing test conversations:**

* Use consistent naming in your test prompts
* Delete obviously failed test conversations
* Keep successful examples to share later
* Archive old tests after major updates

**Starting fresh tests:**

* Always start a new conversation for each test scenario
* Don't reuse old conversations (context bleeds through)
* Test with realistic user scenarios

### Monitoring Usage

Check your conversation history to understand:

* What users are asking for
* Where the agent succeeds
* Where it gets confused
* What workflows are most popular

**Use this feedback to:**

* Refine system instructions
* Add relevant knowledge
* Enable additional tools
* Update sample questions

<Tip>
  **Pro tip:** Review your first 10-20 real user conversations carefully. They'll reveal assumptions you made that users don't share, and unexpected use cases you didn't anticipate.
</Tip>

## User Experience Best Practices

### Setting Expectations in the First Message

Your welcome message is critical. It should:

**Be clear about capabilities:**

```
Good:
"Hi! I can research companies, enrich with LinkedIn data,
and add them to HubSpot. What would you like to research?"

Bad:
"Hello! How can I help you today?"
```

**Show example interactions:**

```
Include in your welcome message:
"Try asking me:
- 'Research TechCorp and its competitors'
- 'Find 10 AI startups in San Francisco'
- 'Enrich this list with funding data'"
```

**Set boundaries:**

```
"I specialize in company research and CRM enrichment.
For general questions, I recommend [alternative]."
```

### Conversational Flow

**Acknowledge long-running tasks:**

```
Bad:
[Agent calls tool, user sees nothing for 30 seconds, then results]

Good:
"Let me research that for you..."
[Calls tool]
"Found 15 companies, now enriching with LinkedIn data..."
[Calls tool]
"Analysis complete! Here are the results:"
```

**Ask clarifying questions early:**

```
User: "Research competitors"

Good agent response:
"I'd be happy to research competitors. A few questions:
- What industry or product category?
- Geographic focus?
- Should I include indirect competitors too?"

Bad agent response:
"Okay, researching competitors..."
[Doesn't know what to research]
```

**Confirm before sensitive actions:**

```
Good:
"I've drafted an email to the CEO. Here's what I'll send:
[Shows email]
Should I send this?"

Bad:
"Email sent to CEO."
[User had no chance to review]
```

### Error Handling

When things go wrong, your agent should:

**Explain what happened:**

```
Good:
"I tried to call the Company Research workflow but it returned
an error: 'API rate limit exceeded'. This means we've made too
many requests. I can try again in a few minutes, or we can
approach this differently. What would you prefer?"

Bad:
"Error occurred."
```

**Offer alternatives:**

```
"The LinkedIn enrichment tool isn't responding. I can:
1. Try a different enrichment source
2. Continue with the data we have
3. Wait and try again later

What works best for you?"
```

**Don't get stuck:**

```
If a tool fails repeatedly, don't keep trying.
Agent should: "This tool seems to be having issues. Let me try
a different approach..." or "I'll skip this step for now..."
```

## Conversation Analytics

While you can't export conversation data directly, you can learn from patterns:

### What to Look For

**Common question patterns:**

* Are users asking for things your agent can't do?
* → Consider adding new tools or knowledge

**Where conversations succeed:**

* Which workflows work smoothly?
* → Highlight these in examples

**Where conversations fail:**

* Where does the agent get confused?
* → Update system instructions or add knowledge

**Unexpected use cases:**

* Are users doing things you didn't anticipate?
* → Consider optimizing for these patterns

### Iterating Based on Conversations

**Weekly review process:**

1. Review 10-20 recent conversations
2. Identify 3 common issues
3. Make 1-2 specific improvements
4. Test improvements with new conversations
5. Repeat

**Example improvement cycle:**

```
Week 1 observation: Users often ask for data exports
Action: Enable Google Sheets integration

Week 2 observation: Agent doesn't explain what it's doing
Action: Update system instructions to narrate actions

Week 3 observation: Users confused about what agent can do
Action: Update welcome message and sample questions
```

## Advanced: Conversation Handoffs

For complex agents, you might want to design conversation handoffs:

### Handing Off to Humans

```
System instructions:
"If the user requests something outside your capabilities,
offer to connect them with a human:

'This requires human expertise. I can:
1. Summarize our conversation so far
2. Send a notification to [team/person]
3. Save our discussion for their review

What would you prefer?'"
```

### Handing Off to Other Agents

```
System instructions:
"For [specific task type], suggest forking to the
specialized agent:

'For advanced data analysis, I recommend forking this
conversation to our Data Analysis Knowledge agent:
[link]. It has specialized tools for [capability].
Should I prepare a summary to start there?'"
```

## Troubleshooting Conversations

<AccordionGroup>
  <Accordion title="Conversation history isn't saving">
    **Symptoms:** Conversations disappear or don't persist

    **Possible causes:**

    1. Browser cookies/storage disabled
    2. Incognito/private browsing mode
    3. Account authentication issues

    **Solutions:**

    * Ensure user is logged in
    * Check browser allows cookies and local storage
    * Try a different browser
    * Clear cache and reload
  </Accordion>

  <Accordion title="Agent loses context mid-conversation">
    **Symptoms:** Agent forgets what was discussed earlier

    **Possible causes:**

    1. Conversation is very long (approaching token limits)
    2. User jumped between multiple unrelated topics
    3. Technical issue with conversation state

    **Solutions:**

    * Start a new conversation for new topics
    * Keep conversations focused on one main task
    * If very long conversation, fork and continue fresh
    * This is rare - if it happens often, report to support
  </Accordion>

  <Accordion title="Shared link isn't working">
    **Symptoms:** Link shows error or "not found"

    **Possible causes:**

    1. Conversation was deleted
    2. Agent was made private
    3. Link was copied incorrectly

    **Solutions:**

    * Verify the agent is still public
    * Check conversation still exists in your history
    * Copy the share link again
    * Ensure full URL is included (including https\://)
  </Accordion>

  <Accordion title="How do I delete a conversation?">
    **Answer:**

    1. Find the conversation in your history
    2. Look for delete/trash icon (usually hover or right-click)
    3. Confirm deletion

    **Note:** Deleted conversations cannot be recovered. If you shared the conversation link, it will no longer work.
  </Accordion>

  <Accordion title="Can I edit messages in a conversation?">
    **Answer:** No, conversations are immutable. You cannot edit messages after they're sent. If you made a mistake:

    * Continue the conversation with clarification
    * Start a new conversation
    * Fork the conversation at an earlier point

    This ensures shared conversations remain truthful representations.
  </Accordion>

  <Accordion title="How do I export a conversation?">
    **Answer:** There's no built-in export feature currently, but you can:

    * Copy and paste the conversation text
    * Take screenshots
    * Share the link and reference it externally
    * Use the conversation as training data (upload as knowledge)
  </Accordion>
</AccordionGroup>

## Next Steps

Now that you understand conversation management and sharing:

<CardGroup cols={2}>
  <Card title="Best Practices" icon="star" href="/knowledge-agents/best-practices">
    Learn advanced techniques for building exceptional knowledge agents
  </Card>

  <Card title="Troubleshooting" icon="triangle-exclamation" href="/knowledge-agents/troubleshooting">
    Solve common issues and optimize your agent's performance
  </Card>

  <Card title="Configuration" icon="sliders" href="/knowledge-agents/configuration">
    Review how to write better system instructions and prompts
  </Card>

  <Card title="Tools Integration" icon="wrench" href="/knowledge-agents/tools-integration">
    Give your agent more capabilities to create better conversations
  </Card>
</CardGroup>

<Note>
  **Remember:** Every conversation is an opportunity to learn what works and what doesn't. Review conversations regularly, share your best examples, and continuously refine based on real usage.
</Note>
