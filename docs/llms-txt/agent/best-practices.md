# Source: https://docs.agent.ai/knowledge-agents/best-practices.md

# Best Practices

> Advanced techniques and strategies for building exceptional knowledge agents

## Overview

This guide covers advanced best practices for creating knowledge agents that are powerful, reliable, and delightful to use. These techniques come from real-world usage and help you avoid common pitfalls.

## Prompt Engineering Best Practices

### Write for AI, Not Humans

System instructions should be explicit and structured, not conversational.

**Don't:**

```
You're really good at helping people and should try your best
to be helpful and nice when they ask you things.
```

**Do:**

```
You are a research assistant. When users ask questions:
1. Search your knowledge base first
2. If information isn't found, use the Web Research tool
3. Cite sources in your responses
4. Ask clarifying questions for ambiguous requests
```

**Why:** AI models follow explicit instructions better than vague guidance.

### Be Specific About Tool Usage

Tell the AI exactly when and how to use each tool.

**Vague (Bad):**

```
You have access to several tools to help users.
```

**Specific (Good):**

```
Tools available:
- "Company Research" workflow: Use when users ask about specific companies
  Input: Company name
  Output: Company data, funding, employee count

- "LinkedIn Enrichment" workflow: Use after Company Research to get people
  Input: Company name from previous research
  Output: Key decision-makers and their profiles

- HubSpot integration: Use to save contacts
  Input: Person name, email, company
  Action: Creates contact in CRM

Workflow order: Research → Enrich → Save to CRM
Always get user approval before saving to HubSpot.
```

**Why:** Specificity reduces guesswork and increases reliability.

### Use Examples in System Instructions

Show the agent what good looks like.

**Without Examples:**

```
Present research findings clearly.
```

**With Examples:**

```
Present research findings in this format:

## [Company Name]
- Industry: [industry]
- Size: [employee count]
- Funding: [total raised]

**Key People:**
- [Name] - [Title]
- [Name] - [Title]

**Recent News:**
- [News item 1]
- [News item 2]

**Competitive Positioning:**
[Analysis paragraph]

Sources: [List sources used]
```

**Why:** Examples create consistency and quality.

### Define Boundaries Clearly

Tell the agent what NOT to do is as important as what to do.

**Good boundaries:**

```
Do NOT:
- Make up information if you don't know something
- Claim certainty when data is uncertain
- Send emails without showing user the draft first
- Create CRM records without confirming details
- Provide financial or legal advice

If asked to do something outside your capabilities:
"I'm specialized in [your domain]. For [their request],
I recommend [alternative or human handoff]."
```

**Why:** Prevents the agent from hallucinating or overstepping.

### Iterative Prompting Strategy

Build your system instructions incrementally:

**Day 1: Basic role**

```
You are a marketing assistant that helps create campaigns.
```

**Day 2: Add workflow**

```
You are a marketing assistant. When users want campaigns:
1. Ask about goals and audience
2. Use "Competitor Research" workflow
3. Present findings and recommendations
```

**Day 3: Add output formatting**

```
[Previous instructions]

Format campaign plans like this:
**Objective:** [goal]
**Audience:** [target]
**Channels:** [list]
**Timeline:** [schedule]
**Budget:** [estimate]
```

**Day 4: Add error handling**

```
[Previous instructions]

If Competitor Research fails:
- Explain the error to the user
- Offer to proceed without competitor data
- Or suggest trying again later
```

**Why:** Gradual refinement based on real usage beats trying to write perfect prompts upfront.

## Knowledge Base Optimization

### Chunk Your Knowledge Strategically

**Poor knowledge structure:**

* One massive 100-page PDF with everything mixed together
* Lots of irrelevant content (legal boilerplate, footers, headers)

**Good knowledge structure:**

* Separate documents by topic: "Product Features.pdf", "Pricing.pdf", "API Docs.pdf"
* Remove boilerplate and navigation text
* Use clear headings and sections
* Each document focused on one topic area

**Why:** Better chunks = better retrieval = more accurate responses.

### Use Markdown Formatting in Knowledge

When creating knowledge documents, use structure:

**Poorly formatted:**

```
Our product has three features first is automation which does
X and Y second is reporting that shows Z third is integrations
that connect to A B and C.
```

**Well formatted:**

```
# Product Features

## 1. Automation
- Capability X: [description]
- Capability Y: [description]

## 2. Reporting
- Shows metric Z
- Exportable to CSV, PDF

## 3. Integrations
- Connect to: A, B, C
- Two-way sync available
```

**Why:** Structured content is easier for the AI to parse and retrieve accurately.

### Name Files Descriptively

**Bad file names:**

* "Document1.pdf"
* "Final\_v2\_FINAL.docx"
* "Untitled.pdf"

**Good file names:**

* "\[POLICY] Refund and Return Policy.pdf"
* "\[GUIDE] API Authentication Guide.pdf"
* "\[FAQ] Common Customer Questions.pdf"

**Why:** File names provide context for retrieval.

### Keep Knowledge Current

**Weekly:**

* Check if any major facts changed
* Update URLs that may have refreshed content

**Monthly:**

* Review all knowledge for accuracy
* Remove outdated information
* Add new relevant content

**Quarterly:**

* Audit entire knowledge base
* Reorganize if needed
* Test retrieval quality

**Why:** Stale knowledge leads to incorrect responses.

### Quality Metrics for Knowledge

**Good knowledge base:**

* 80%+ of user questions can be answered from knowledge
* Responses cite relevant, accurate sources
* Knowledge is current (updated within 3 months)
* Focused on your domain (minimal irrelevant content)

**Poor knowledge base:**

* Agent frequently says "I don't have information about that"
* Cites wrong or irrelevant sources
* Information is outdated
* Too much noise (agent retrieves irrelevant chunks)

## Tool Orchestration Patterns

### Start with 1-2 Tools, Scale Gradually

**Phase 1: Single tool**

```
Enable: Web Research workflow
Test: "Research [topic]"
Perfect: Get this working reliably
```

**Phase 2: Add complementary tool**

```
Enable: Data Analysis workflow
Test: "Research [topic] and analyze trends"
Perfect: Ensure tools work together
```

**Phase 3: Add output tool**

```
Enable: Google Docs integration
Test: "Research [topic], analyze, and save report"
Perfect: Complete workflow end-to-end
```

**Why:** Testing sequentially isolates issues. Adding 10 tools at once makes debugging impossible.

### Design Tool Chains

Think about natural sequences:

**Research Chain:**

```
Input → Search → Enrich → Analyze → Output
```

**System instructions:**

```
For research requests:
1. Use Web Search to find companies
2. Use LinkedIn Enrichment to get key people
3. Use Company Analysis to assess fit
4. Use Google Docs to save findings
```

**Sales Chain:**

```
Identify → Research → Qualify → Enrich → Save
```

**System instructions:**

```
For lead generation:
1. Use Company Search to find prospects
2. Use Web Research to check recent news
3. Use Qualification Checklist to assess fit
4. Use LinkedIn Enrichment to find contacts
5. Use HubSpot integration to create deals
```

**Why:** Designed chains create reliable, repeatable workflows.

### Add Confirmation Gates

For sensitive or irreversible actions, add approval steps:

**Pattern:**

```
Tool call → Show results → Get approval → Execute action
```

**Implementation:**

```
System instructions:
"After using Company Research and Enrichment workflows,
show the user:

'I've found [N] prospects:
[List with key details]

Should I create these contacts in HubSpot?'

Only proceed if user explicitly confirms."
```

**Why:** Prevents unintended actions and builds user trust.

### Handle Tool Failures Gracefully

**Bad error handling:**

```
Agent: "Error occurred. Tool failed."
[Conversation stalls]
```

**Good error handling:**

```
System instructions:
"If a tool fails:
1. Explain what happened in plain language
2. Offer alternative approaches
3. Ask user what they'd prefer

Example:
'The LinkedIn Enrichment tool isn't responding (likely API rate limit).
I can:
- Continue with the data we have
- Use an alternative enrichment source
- Try again in a few minutes
What works best?'"
```

**Why:** Resilient agents maintain momentum even when tools fail.

## Testing Strategies

### The 3-Phase Testing Approach

**Phase 1: Unit testing (Individual capabilities)**

```
Test each tool separately:
- "Use Company Research to research Microsoft"
- "Use LinkedIn Enrichment for TechCorp"
- "Create a test contact in HubSpot"

Verify:
 Tool is called
 Returns expected data
 Agent presents results clearly
```

**Phase 2: Integration testing (Tool combinations)**

```
Test tool chains:
- "Research Company X and add to HubSpot"
- "Analyze data and save to Google Sheets"

Verify:
 Tools called in logical order
 Data flows between tools
 Final output is complete
```

**Phase 3: User acceptance testing (Real scenarios)**

```
Test like a real user would:
- Ask vague questions
- Change mind mid-conversation
- Request edge cases
- Try to break it

Verify:
 Agent asks clarifying questions
 Handles ambiguity
 Recovers from errors
 Boundaries are respected
```

### Build a Test Suite

Create a document with standard test cases:

**Example test suite:**

```
BASIC FUNCTIONALITY
✓ Agent responds to greetings
✓ Sample questions all work
✓ Knowledge retrieval works
✓ Tool calling works

KNOWLEDGE TESTS
✓ "What do you know about [topic from knowledge]?"
✓ "Explain [concept from documentation]"
✓ "What's our policy on [policy from knowledge]?"

TOOL TESTS (for each tool)
✓ "[Simple tool request]"
✓ "[Complex tool request with multiple parameters]"
✓ "[Error scenario - invalid input]"

INTEGRATION TESTS
✓ "[Request requiring 2 tools]"
✓ "[Request requiring 3+ tools in sequence]"
✓ "[Request requiring approval gates]"

EDGE CASES
✓ Very long conversation (10+ turns)
✓ Ambiguous request
✓ Request outside capabilities
✓ Tool failure during workflow
✓ User says "no" to confirmation

USER EXPERIENCE
✓ Conversation feels natural
✓ Progress updates are clear
✓ Errors explained helpfully
✓ Responses are concise
```

Run through this suite:

* After every major change
* Before launching publicly
* Weekly for public agents

### A/B Test System Instructions

For public agents with traffic, test variations:

**Create two versions:**

```
Version A: Current system instructions
Version B: Modified instructions (one variable changed)
```

**Run both for a week, then:**

* Review conversations from each
* Which version led to better outcomes?
* Which had fewer errors?
* Which had better user engagement?

**Example A/B test:**

```
A: "Always cite sources"
B: "Cite sources when providing factual information"

Outcome: B was better - users found constant citations annoying
for conversational responses
```

## Performance Optimization

### Response Speed

**Slow agents are frustrating.** Optimize for speed:

**Knowledge base optimization:**

* Don't upload hundreds of documents (50-100 focused docs is plenty)
* Remove duplicate/overlapping content
* Keep individual documents under 25MB

**Tool optimization:**

* Ensure workflow agents complete quickly (under 30 seconds ideal)
* Use async operations when possible
* Add timeout handling

**Prompt optimization:**

* Shorter system instructions = faster processing
* Remove unnecessary examples
* Focus on essential guidance

### Reduce Hallucinations

**System instruction pattern:**

```
Accuracy guidelines:
- Only use information from your knowledge base or tool results
- If you're not certain, say so explicitly
- Never make up data, statistics, or quotes
- Use phrases like "Based on my knowledge..." or "I don't have information about..."
- When making inferences, clearly mark them as such

If you don't know: "I don't have that information in my knowledge base.
I can try to find it using [tool name] if you'd like."
```

**Why:** Explicit anti-hallucination instructions reduce confident but wrong answers.

### Token Efficiency

Long conversations can hit token limits:

**In system instructions:**

```
Conversation management:
- Keep responses concise (2-3 paragraphs max unless detailed output requested)
- Summarize long tool outputs instead of repeating everything
- After 10+ conversation turns, offer to start fresh if shifting topics
```

**Why:** Efficient token usage extends conversation length before context limits.

## User Experience Design

### Progressive Disclosure

Don't overwhelm users with all capabilities at once:

**Welcome message progression:**

```
Basic welcome:
"Hi! I can help with [primary use case]. What would you like to do?"

After 1-2 successful interactions:
"By the way, I can also [secondary capability]. Interested?"

After they're comfortable:
Mention advanced features as relevant
```

**Why:** Gradual exposure improves onboarding and reduces cognitive load.

### Conversation Pacing

**Too fast:**

```
User: "Research Acme Corp"
Agent: [Immediately dumps 500 words of research]
```

**Good pacing:**

```
User: "Research Acme Corp"
Agent: "I'll research Acme Corp for you. One moment..."
[Calls tool]
Agent: "Found it! Acme Corp is a B2B SaaS company ($50M revenue, 200 employees).
Would you like the full analysis or specific aspects?"

User: "Full analysis"
Agent: [Now provides complete details]
```

**Why:** Pacing gives users control and prevents information overload.

### Personality Consistency

Choose a tone and stick to it:

**Professional:**

```
"I'll analyze the competitive landscape and present findings.
One moment while I gather data..."
```

**Friendly:**

```
"Let me look into that for you! Gathering competitor info now..."
```

**Technical:**

```
"Executing competitor analysis workflow.
Estimated completion: 15 seconds.
Standby..."
```

**Why:** Consistent personality builds trust and feels more professional.

### Error Recovery

**Good error recovery pattern:**

```
1. Acknowledge the error
2. Explain what happened (simple terms)
3. Offer alternatives
4. Let user decide next step

Example:
"I tried to call the Company Research tool but it returned an error
(API rate limit). This means we've made too many requests recently.

I can:
1. Try a different research tool
2. Wait 2 minutes and retry
3. Continue without external research using my knowledge base

What would you prefer?"
```

**Why:** Users forgive errors if handled well.

## Security & Privacy

### Public Agent Considerations

If your agent is public, assume anyone might use it:

**Don't:**

* Give it access to sensitive integrations (your email, internal CRM)
* Upload confidential knowledge
* Enable destructive actions
* Store API keys in knowledge base

**Do:**

* Use read-only integrations when possible
* Curate knowledge for public consumption
* Add strong confirmation gates for any writes
* Review conversations regularly for misuse

### Sensitive Data Handling

**System instructions for sensitive scenarios:**

```
Data privacy:
- Never ask users for passwords, credit cards, or SSNs
- If users share sensitive information, remind them:
  "Please don't share sensitive personal information in this chat.
  Conversations may be logged."
- Don't store sensitive data in variables or tool calls
```

### Rate Limiting User Actions

For agents that call expensive or limited APIs:

**System instructions:**

```
Resource limits:
- Maximum 10 company researches per conversation
- After 10 researches: "We've hit the research limit for this conversation.
  Start a new chat to continue, or let me know if you want to analyze
  what we've found so far."
```

**Why:** Prevents abuse and runaway costs.

## Maintenance & Iteration

### The Weekly Review

Spend 30 minutes weekly reviewing your agent:

**What to check:**

```
1. Recent conversations (sample 10-20)
   - Any errors or confusion?
   - New use cases emerging?
   - Tools working properly?

2. Knowledge base
   - Anything outdated?
   - Missing information users asked about?

3. System instructions
   - Any patterns the agent isn't following?
   - Need to add new guidance?

4. Tools
   - All integrations still connected?
   - Workflows completing successfully?
```

**Make 1-2 improvements** based on what you find.

### Version Control for Prompts

Keep a changelog of system instruction changes:

**Example:**

```
Version 1.0 (2024-01-15)
- Initial system instructions
- Basic research capability

Version 1.1 (2024-01-22)
- Added: Explicit citation requirements
- Added: HubSpot confirmation gates
- Fixed: Too verbose responses

Version 1.2 (2024-02-01)
- Added: LinkedIn enrichment workflow
- Updated: Research workflow order
- Removed: Outdated policy reference
```

**Why:** You can roll back if a change makes things worse.

### Feedback Loops

Create mechanisms to gather feedback:

**In system instructions:**

```
After completing significant tasks:
"How did that go? Let me know if you'd like me to:
- Provide more detail
- Try a different approach
- Adjust anything"
```

**Via shared conversations:**

* Ask early users to share conversations
* Review what worked and what didn't
* Implement improvements

## Common Pitfalls & Solutions

<AccordionGroup>
  <Accordion title="Pitfall: Agent is too chatty">
    **Problem:** Agent writes paragraphs when users want quick answers

    **Solution:**
    Add to system instructions:

    ```
    Response length:
    - Default to concise responses (2-3 sentences)
    - Only provide detailed explanations if:
      a) User asks for more detail
      b) Request requires comprehensive analysis
      c) Complex topic needs context
    ```
  </Accordion>

  <Accordion title="Pitfall: Agent doesn't use tools">
    **Problem:** You enabled tools but agent just talks

    **Solution:**

    1. Check tools are actually enabled (Action Agents tab)
    2. Add explicit tool instructions to system prompt
    3. Test with direct requests: "Use \[tool name] to..."
    4. Verify tool names are clear
  </Accordion>

  <Accordion title="Pitfall: Knowledge retrieval isn't working">
    **Problem:** Agent doesn't use uploaded knowledge

    **Solution:**

    1. Verify files finished processing
    2. Ask directly: "What do you know about \[topic from knowledge]?"
    3. Check knowledge is well-structured with headings
    4. Remove duplicate/conflicting content
    5. Add to system instructions: "Always search knowledge base first"
  </Accordion>

  <Accordion title="Pitfall: Inconsistent behavior">
    **Problem:** Agent acts differently each time

    **Solution:**

    * AI is probabilistic by nature (some variation is normal)
    * Reduce variation by being MORE specific in system instructions
    * Use examples to show exact format you want
    * Test the same query 5 times - if wildly different, prompt needs work
  </Accordion>

  <Accordion title="Pitfall: Users confused about capabilities">
    **Problem:** Users ask for things agent can't do

    **Solution:**

    1. Improve welcome message clarity
    2. Better sample questions showing what agent CAN do
    3. Add to system instructions:
       "If asked about \[outside scope], say:
       'I specialize in \[your domain]. For \[their request], try \[alternative]."
  </Accordion>

  <Accordion title="Pitfall: Tool chains breaking">
    **Problem:** Multi-tool workflows fail midway

    **Solution:**

    1. Test each tool individually first
    2. Add error handling to system instructions
    3. Design tools to be independent (one tool failure doesn't break everything)
    4. Add checkpoints: After each tool, summarize what you have before calling next
  </Accordion>
</AccordionGroup>

## Advanced Patterns

### The Expert Escalation Pattern

```
System instructions:
"You are a Level 1 assistant. For simple requests, handle directly.

For complex requests involving [specific criteria]:
1. Gather initial information
2. Explain: 'This is a complex scenario. I recommend consulting
   [Knowledge Agent/Human] who specializes in [area].'
3. Offer to prepare a summary for handoff
4. Provide link to [specialized agent] if available

Complex scenarios include:
- [Criteria 1]
- [Criteria 2]
- [Criteria 3]"
```

**Use case:** Tiered support, specialized domains

### The Learning Agent Pattern

```
System instructions:
"After each conversation:
1. Note what worked well
2. Note what the user asked for that you couldn't provide
3. Suggest improvements:
   'I noticed you asked about [X]. While I can't help with that now,
   I've flagged it for my creator to add that capability.'

4. Keep a running list of feature requests in the conversation"
```

**Use case:** Continuous improvement, user research

### The Collaborative Builder Pattern

```
System instructions:
"You work iteratively with users to create [output].

Your process:
1. Understand requirements (ask questions)
2. Create initial draft (show user)
3. Get feedback (what to change)
4. Revise (incorporate feedback)
5. Repeat until user is satisfied
6. Finalize (execute output workflow)

Never deliver final output without at least 1 revision cycle.
Always show drafts before finalizing."
```

**Use case:** Content creation, design work, strategic planning

## Metrics for Success

Track these to measure your agent's effectiveness:

**Qualitative:**

* Are conversations achieving user goals?
* Do users return for multiple conversations?
* Are shared conversations examples of success?

**Quantitative:**

* Average conversation length (too short = not useful, too long = struggling)
* Tool call success rate (should be >90%)
* Knowledge retrieval frequency (are you using knowledge effectively?)

**User Feedback:**

* Explicit positive feedback
* Feature requests
* Bug reports

**Ideal Knowledge Agent:**

* Conversations: 5-15 messages to complete a task
* Tool success: 95%+ successful tool calls
* Knowledge usage: Cites knowledge in 70%+ of responses
* User satisfaction: Repeat usage, positive shared examples

## Next Steps

You now have advanced techniques for building exceptional knowledge agents:

<CardGroup cols={2}>
  <Card title="Troubleshooting" icon="triangle-exclamation" href="/knowledge-agents/troubleshooting">
    Solve specific issues and optimize performance
  </Card>

  <Card title="Configuration" icon="sliders" href="/knowledge-agents/configuration">
    Apply best practices to your system instructions
  </Card>

  <Card title="Tools Integration" icon="wrench" href="/knowledge-agents/tools-integration">
    Implement advanced tool orchestration patterns
  </Card>

  <Card title="Knowledge Base" icon="book" href="/knowledge-agents/knowledge-base">
    Optimize your knowledge for better retrieval
  </Card>
</CardGroup>

<Note>
  **Remember:** Building great knowledge agents is iterative. Start simple, launch quickly, learn from real usage, and continuously improve. The best agents evolve over time based on user feedback and measured outcomes.
</Note>
