# Source: https://docs.agent.ai/knowledge-agents/troubleshooting.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Troubleshooting

> Diagnose and fix common issues with your knowledge agents

## Diagnostic Workflow

When your knowledge agent isn't working as expected, follow this systematic approach:

```
1. Identify the symptom
   ↓
2. Isolate the component
   (Configuration? Knowledge? Tools? Conversation?)
   ↓
3. Test in isolation
   (Test just that component)
   ↓
4. Check the basics
   (Is it enabled? Saved? Loaded?)
   ↓
5. Review recent changes
   (What was modified last?)
   ↓
6. Apply fix
   ↓
7. Verify fix works
```

## Quick Diagnostic Checklist

Before diving deep, check these common issues:

```
✓ Did you click "Save" after making changes?
✓ Did you start a new conversation to test changes?
✓ Are all files finished processing?
✓ Are all tools/integrations still connected?
✓ Is the agent set to public/private correctly?
✓ Did you test with a clear, specific request?
✓ Is your internet connection stable?
```

**80% of issues** come from forgetting to save or not starting a fresh conversation.

## Configuration Issues

### Agent Not Responding or Acting Generically

**Symptoms:**

* Agent gives generic chatbot responses
* Ignores system instructions
* Doesn't use its personality

**Possible Causes:**

1. System instructions not saved
2. Testing in old conversation (has cached behavior)
3. System instructions too vague
4. Conflicting instructions

**How to Fix:**

**Step 1: Verify save**

```
1. Go to Introduction tab
2. Check your system instructions are there
3. Click "Save Introduction Details" again
4. Wait for confirmation message
```

**Step 2: Test fresh**

```
1. Start a brand new conversation
2. Test with a sample question
3. Check if behavior changed
```

**Step 3: Simplify to test**

```
Temporarily replace system instructions with:

"You are a test agent. When users say hello, respond
with 'SYSTEM INSTRUCTIONS WORKING' in all caps."

Save, start new conversation, say "hello"
- If you get the response → System instructions work, original prompt was the issue
- If you don't → Deeper technical issue
```

**Step 4: Review prompt quality**

* Are instructions specific enough?
* Any contradictions?
* See [Configuration guide](/knowledge-agents/configuration) for writing better prompts

### Welcome Message or Sample Questions Not Showing

**Symptoms:**

* Old welcome message appears
* Sample questions missing or outdated

**Possible Causes:**

1. Changes not saved
2. Cached in browser
3. Testing in existing conversation

**How to Fix:**

```
1. Verify changes saved:
   - Go to Introduction / Sample Questions tab
   - Confirm your text is there
   - Click save again

2. Clear browser cache:
   - Refresh page (Cmd+Shift+R or Ctrl+Shift+R)
   - Or clear browser cache completely

3. Start new conversation:
   - Don't reuse old conversation
   - Click "New Chat" or equivalent
   - Welcome message should update
```

### Agent Ignoring Boundaries or Prompt Filtering

**Symptoms:**

* Agent responds to off-topic requests
* Doesn't follow content guidelines
* Hallucinating information

**Possible Causes:**

1. Boundary instructions too soft
2. Conflicting instructions (be helpful vs. stay on topic)
3. AI interpreting edge cases differently than expected

**How to Fix:**

**Strengthen boundaries:**

```
Don't:
"Try to stay on topic about [domain]."

Do:
"ONLY respond to questions about [domain].

If users ask about anything else, respond exactly:
'I specialize in [domain]. I can't help with [their topic].
For general questions, try [alternative].'

Topics outside scope:
- [Topic 1]
- [Topic 2]
- [Topic 3]"
```

**Add explicit do-not-hallucinate instructions:**

```
"Accuracy rules:
- NEVER make up information
- If you don't know, say: 'I don't have that information'
- Only use data from knowledge base or tool results
- When uncertain, acknowledge uncertainty explicitly"
```

## Knowledge Base Issues

### Agent Says "I Don't Have Information" About Uploaded Content

**Symptoms:**

* You uploaded knowledge but agent doesn't use it
* Agent says it doesn't know things clearly in your documents

**Possible Causes:**

1. File still processing
2. File failed to process
3. Search query doesn't match content semantically
4. Too much noise in knowledge base

**Diagnostic Steps:**

**Step 1: Check processing status**

```
1. Go to Training tab
2. Look at uploaded files
3. Check for:
   - Processing spinner (still working)
   -  Checkmark (successfully processed)
   -  Error icon (failed)

If stuck processing >5 minutes → refresh page or re-upload
If error → file may be corrupted or unsupported format
```

**Step 2: Test knowledge directly**

```
Ask: "What files are in your knowledge base?"
Or: "What do you know about [exact topic from your doc]?"

If agent doesn't mention your file → not successfully added
If it does mention it but retrieves wrong info → retrieval issue
```

**Step 3: Improve retrieval**

```
Problem: Content isn't semantically matching

Solutions:
1. Restructure document with clear headings
2. Remove boilerplate/noise
3. Break large docs into focused pieces
4. Use descriptive file names
5. Add metadata headers

Example:
Instead of: "Document.pdf"
Use: "[POLICY] Customer Refund Policy - Updated 2024.pdf"
```

**Step 4: Check knowledge base size**

```
If you have 100+ documents:
- Too much content can dilute retrieval
- Remove less relevant docs
- Focus on highest quality sources
```

### Knowledge Retrieval is Slow

**Symptoms:**

* Long delays before agent responds
* Timeout errors

**Possible Causes:**

1. Knowledge base too large
2. Files are very large (many MB each)
3. Too many sources

**How to Fix:**

```
1. Audit knowledge base:
   - How many files? (>100 is a lot)
   - File sizes? (>10MB each is large)
   - Duplicate content?

2. Optimize:
   - Remove duplicates
   - Delete least-used sources
   - Split large files into smaller focused docs
   - Keep total under 50-75 high-quality sources

3. If must keep large knowledge base:
   - Consider multiple specialized agents instead of one
   - Use more targeted search prompts
```

### Wrong Knowledge Retrieved

**Symptoms:**

* Agent cites sources but they're not relevant
* Retrieves outdated version of information

**Possible Causes:**

1. Multiple conflicting sources
2. Poor document structure
3. Outdated content not removed

**How to Fix:**

```
1. Check for conflicts:
   - Do you have multiple docs on same topic?
   - Contradictory information?
   → Keep only most authoritative/current version

2. Improve structure:
   - Add clear section headers
   - Use bullet points and lists
   - Separate topics clearly

3. Remove outdated:
   - Delete old versions
   - Update changed information
   - Refresh URL-based knowledge
```

## Tool Integration Issues

### Workflow Agent Not Being Called

**Symptoms:**

* Agent talks about the task but doesn't call the workflow
* Responds conversationally instead of taking action

**Diagnostic Steps:**

**Step 1: Verify enabled**

```
1. Go to Action Agents tab
2. Is the workflow checked?
3. Click "Save Action Agents Selection"
4. Start new conversation
```

**Step 2: Test directly**

```
Ask: "Use [exact workflow name] to [task]"

If called → Agent CAN use it, just doesn't know when
If not called → Configuration or connection issue
```

**Step 3: Check system instructions**

```
Do your system instructions mention the workflow?

Add:
"When users ask to [task], use the '[Workflow Name]' workflow.
Example: User says 'research Company X' → call 'Company Research' workflow"
```

**Step 4: Verify workflow name clarity**

```
Bad name: "Agent 1", "My Workflow"
Good name: "Company Research Tool", "Email Sender"

Rename workflow to be more descriptive
```

**Step 5: Test workflow independently**

```
1. Go to the workflow agent itself
2. Run it manually
3. Does it complete successfully?

If workflow is broken, knowledge agent can't call it
```

### Workflow Returns Errors

**Symptoms:**

* Agent calls workflow but gets error response
* "Tool failed" messages

**How to Fix:**

```
1. Test workflow independently:
   - Run the workflow agent by itself
   - Does it work outside knowledge agent?
   - If no → fix the workflow first

2. Check data being passed:
   - What data is knowledge agent sending to workflow?
   - Does it match workflow's expected inputs?
   - Update system instructions to format data correctly

3. Check workflow requirements:
   - Does workflow need authentication?
   - API keys configured?
   - Rate limits hit?

4. Add error handling:
   System instructions:
   "If [Workflow Name] fails:
   1. Tell user what happened
   2. Offer alternative approach
   3. Don't keep retrying blindly"
```

### Composio Integration Not Working

**Symptoms:**

* "Authentication failed" errors
* Integration shows disconnected
* Actions don't execute

**How to Fix:**

**Step 1: Re-authenticate**

```
1. Go to Integrations tab
2. Find the integration
3. Click "Disconnect"
4. Click "Connect" again
5. Complete OAuth flow
6. Verify "Connected" status
```

**Step 2: Check permissions**

```
1. During OAuth, did you grant all needed permissions?
2. Some integrations need specific scopes
3. Re-connect and ensure all permissions granted
```

**Step 3: Test integration directly**

```
Ask agent: "Use [Integration] to [simple action]"
Example: "Use Slack to send a test message to #test"

If simple action works → complex use case is the issue
If simple action fails → integration configuration problem
```

**Step 4: Check service status**

```
Is the external service down?
- Check service status page (e.g., status.slack.com)
- Try accessing service directly in browser
- Wait and retry if service is down
```

### MCP Server Not Connecting

**Symptoms:**

* MCP tools not available
* Connection errors

**How to Fix:**

```
1. Verify server is running:
   - Check server endpoint is accessible
   - Test server health endpoint
   - Review server logs

2. Check configuration:
   - Correct server URL?
   - Authentication credentials correct?
   - Network access allowed?

3. Review MCP server implementation:
   - Following MCP specification?
   - See [MCP Server docs](/mcp-server)

4. Test with minimal MCP server:
   - Create simple "hello world" MCP server
   - If that works → your custom server has issues
   - If that fails → MCP configuration in agent is wrong
```

## Conversation & Chat Issues

### Conversations Not Saving

**Symptoms:**

* Conversation history disappears
* Can't find past conversations

**Possible Causes:**

1. Not logged in (guest mode)
2. Browser privacy mode
3. Cookies/storage disabled

**How to Fix:**

```
1. Verify logged in:
   - Check if you see your account name
   - If not, sign in
   - Try conversation again

2. Check browser settings:
   - Not in incognito/private mode?
   - Cookies enabled?
   - Local storage enabled?

3. Try different browser:
   - Test in Chrome/Firefox/Safari
   - If works in one browser → original browser settings issue
```

### Agent Losing Context Mid-Conversation

**Symptoms:**

* Agent forgets what was discussed earlier
* Doesn't remember previous tool results

**Possible Causes:**

1. Conversation too long (token limit)
2. Technical glitch

**How to Fix:**

```
1. Start new conversation:
   - Very long conversations (20+ turns) may hit limits
   - Fork or start fresh
   - Summarize what you need agent to remember

2. Keep conversations focused:
   - Don't jump between unrelated topics
   - One main task per conversation
   - Start new conversation for new topics

3. If happens in short conversations:
   - Report to support (this shouldn't happen)
   - Include conversation link
```

### Shared Conversation Link Not Working

**Symptoms:**

* "Not found" or error when opening shared link
* Link shows different content

**How to Fix:**

```
1. Verify link is complete:
   - Full URL including https://
   - No characters cut off
   - Copy link again fresh

2. Check conversation still exists:
   - Did you delete it?
   - Is agent still public?
   - Log in and view in your history

3. Check agent visibility:
   - Is knowledge agent set to public?
   - Private agents can't have public shared conversations
```

### Can't Start New Conversation

**Symptoms:**

* "New Chat" button not working
* Stuck in existing conversation

**How to Fix:**

```
1. Refresh page (Cmd+R or Ctrl+R)

2. Clear browser cache

3. Log out and log back in

4. Try different browser

5. If persists → technical issue, contact support
```

## Performance Issues

### Agent Responses Are Slow

**Symptoms:**

* Long wait times (>30 seconds) for responses
* Timeouts

**Diagnostic:**

```
Identify bottleneck:

1. Simple question, no tools/knowledge:
   - "Hello, how are you?"
   - Should be <3 seconds
   - If slow → platform performance issue

2. Knowledge retrieval:
   - Ask about knowledge base content
   - Should be 3-8 seconds
   - If slow → knowledge base too large

3. Tool calling:
   - Ask to use workflow
   - Timing = workflow execution time + overhead
   - If slow → workflow is slow or tool issue

4. Multiple tools:
   - Complex request with 3+ tools
   - Can take 30-60+ seconds (normal)
   - If >2 minutes → investigate individual tools
```

**Fixes Based on Bottleneck:**

```
If knowledge base is slow:
- Reduce number of documents
- Remove large files
- Optimize document structure

If tools are slow:
- Optimize workflow agents (see workflow docs)
- Use faster integrations
- Reduce number of sequential tool calls

If platform is slow:
- Check status page
- Try during off-peak hours
- Report persistent issues to support
```

### Agent Making Too Many Tool Calls

**Symptoms:**

* Calls 5+ tools for simple requests
* Over-complicates tasks

**How to Fix:**

**Add efficiency guidelines:**

```
System instructions:

"Efficiency rules:
- Use minimum tools needed to complete task
- Don't call tools 'just in case'
- If 1 tool can do the job, don't call 3
- Ask yourself: 'Is this tool call necessary?'

Example:
User: 'What is Company X's website?'
L Bad: Call research tool, enrichment tool, database tool
 Good: Search knowledge base or call 1 research tool"
```

### High API Costs or Rate Limits

**Symptoms:**

* Hitting rate limits frequently
* Unexpected costs

**How to Fix:**

```
1. Add usage controls:
   System instructions:
   "Resource limits:
   - Max [N] tool calls per conversation
   - After limit: 'We've reached the tool usage limit.
     Start new conversation to continue.'"

2. Optimize tool usage:
   - Review system instructions
   - Are you calling tools unnecessarily?
   - Can you batch operations?

3. Use caching:
   - Store common queries in knowledge base
   - Reduce repeated API calls

4. Monitor usage:
   - Review conversation patterns
   - Identify expensive operations
   - Optimize or restrict those operations
```

## Advanced Debugging

### Enable Verbose Logging (Builder Testing)

When testing, ask the agent to explain its thinking:

```
Test prompt:
"Research Company X. After responding, explain:
1. What knowledge you retrieved
2. Which tools you called and why
3. How you decided what to do"

This reveals the agent's decision-making process.
```

### Isolation Testing

Test components separately:

**Test knowledge only:**

```
System instructions (temporary):
"You can ONLY use your knowledge base. Do not call any tools.
If asked to do something requiring tools, say 'Tools disabled for testing.'"

Test: Does knowledge retrieval work?
```

**Test tools only:**

```
System instructions (temporary):
"Ignore your knowledge base. Only use tools to answer questions."

Test: Do tools work correctly?
```

**Test system instructions only:**

```
Remove all knowledge and tools temporarily.

Test: Does agent follow personality and boundaries?
```

### A/B Testing for Debugging

Create two versions of your agent:

```
Version A: Current (broken) configuration
Version B: Minimal working configuration

Compare:
- Which one works?
- What's different?
- Gradually add features from A to B until it breaks
- That feature is the culprit
```

### Check Browser Console

For technical issues:

```
1. Open browser developer tools (F12 or Cmd+Option+I)
2. Go to Console tab
3. Start conversation with agent
4. Look for error messages (red text)
5. Screenshot errors and report to support
```

## When to Contact Support

Contact support if:

* Issue persists after trying all troubleshooting steps
* Technical errors appear consistently
* Platform features aren't working (can't save, can't upload, etc.)
* Integrations fail repeatedly
* Performance degraded significantly
* Data appears corrupted or lost

**What to include in support request:**

```
1. Clear description of issue:
   "When I [action], I expect [result], but instead [actual result]"

2. Steps to reproduce:
   "1. Go to [location]
    2. Click [button]
    3. Error appears"

3. Screenshots:
   - Show the issue
   - Include any error messages
   - Show browser console if technical

4. Conversation link:
   - Share specific conversation where issue occurs
   - Helps support see exact problem

5. What you've tried:
   - List troubleshooting steps already attempted
   - Saves time ruling out common fixes
```

## Issue Prevention

### Pre-Launch Checklist

Before making your agent public:

```
→ Test all sample questions work
→ Test all workflows individually
→ Test multi-workflow scenarios
→ Test with ambiguous requests
→ Test error scenarios (tool failures)
→ Review 5-10 test conversations
→ Check knowledge retrieval accuracy
→ Verify all integrations connected
→ Confirm no sensitive data in knowledge
→ Test shared conversation links work
→ Review system instructions for clarity
→ Check welcome message and prompt hint
```

### Ongoing Maintenance

**Weekly:**

```
→ Review 10-20 recent conversations
→ Check for new error patterns
→ Verify integrations still connected
→ Test 3-5 common scenarios
```

**Monthly:**

```
→ Full test suite run
→ Knowledge base audit
→ Review and update system instructions
→ Check for broken workflow agents
→ Update outdated information
```

**After Major Changes:**

```
→ Full regression testing
→ Compare before/after behavior
→ Review first 10 conversations post-change
→ Be ready to rollback if issues appear
```

## Common Error Messages

<AccordionGroup>
  <Accordion title="'Tool execution failed'">
    **Meaning:** Workflow agent or integration returned an error

    **Fix:**

    1. Test the tool independently
    2. Check tool configuration (API keys, auth)
    3. Review what data was passed to tool
    4. Check tool error logs if available
    5. Add error handling to system instructions
  </Accordion>

  <Accordion title="'Knowledge retrieval timeout'">
    **Meaning:** Knowledge base search took too long

    **Fix:**

    1. Knowledge base too large → reduce size
    2. Large files → split into smaller docs
    3. Temporary platform issue → try again
    4. Persistent → contact support
  </Accordion>

  <Accordion title="'Rate limit exceeded'">
    **Meaning:** Too many requests to an API/tool

    **Fix:**

    1. Wait before retrying (usually 1-5 minutes)
    2. Add rate limit handling to system instructions
    3. Reduce tool call frequency
    4. Implement caching for common requests
    5. Consider upgrading API tier if consistently hitting limits
  </Accordion>

  <Accordion title="'Authentication failed'">
    **Meaning:** Can't connect to integration or tool

    **Fix:**

    1. Re-authenticate the integration
    2. Check credentials/API keys
    3. Verify permissions granted
    4. Check if service credentials changed
    5. Ensure service is accessible (not behind firewall)
  </Accordion>

  <Accordion title="'Invalid configuration'">
    **Meaning:** Something in agent setup is wrong

    **Fix:**

    1. Review all configuration tabs
    2. Ensure required fields filled
    3. Check for special characters in names
    4. Try simplifying configuration
    5. Contact support with details
  </Accordion>
</AccordionGroup>

## Getting Help

### Documentation Resources

<CardGroup cols={2}>
  <Card title="Configuration Guide" icon="sliders" href="/knowledge-agents/configuration">
    Review how to write system instructions
  </Card>

  <Card title="Knowledge Base" icon="book" href="/knowledge-agents/knowledge-base">
    Troubleshoot knowledge retrieval issues
  </Card>

  <Card title="Tools Integration" icon="wrench" href="/knowledge-agents/tools-integration">
    Debug workflow and integration problems
  </Card>

  <Card title="Best Practices" icon="star" href="/knowledge-agents/best-practices">
    Learn patterns that prevent common issues
  </Card>
</CardGroup>

### Community & Support

* **Community Forum:** [community.agent.ai](https://community.agent.ai) - Ask questions, share solutions
* **Support:** [agent.ai/feedback](https://agent.ai/feedback) - Report bugs and request help
* **Status Page:** Check platform status for ongoing issues
* **Documentation:** [docs.agent.ai](https://docs.agent.ai) - Full documentation

<Note>
  **Remember:** Most issues have simple solutions. Work through the diagnostic checklist systematically, isolate the problem component, and apply targeted fixes. The knowledge agent community is also a great resource for troubleshooting uncommon issues.
</Note>
