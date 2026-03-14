# Source: https://docs.acceldata.io/documentation/conversation.md

# Conversation

## Interface Layout

The Conversation Home is your central hub for starting, viewing, and collaborating on conversations.

### Left Sidebar — Starter Pane

- **Recommended**: AI-generated questions tailored to your role and usage. Updated daily.
- **Starred**: Your pinned conversations for quick access.
- **Recently Used**: The last 10 conversations for fast resume.

### Center Panel — Chat Window

- Large, responsive input for natural-language queries
- Full conversation thread with preserved context
- Rich responses (tables, charts, code blocks)
- Contextual action buttons and smart suggestions
- Real-time agent activity (“thinking”) visibility

### Top Navigation Bar

- **Logo**: Return to Conversation Home / start a new conversation
- **Profile & Settings**: Manage preferences
- **Notifications**: Shared items and system updates
- **Help**: Documentation and user guides

### Multi-User Conversation Features

- **Invite users** to any conversation (live or async)
- **Real-time collaboration** with teammates
- **@adm mentions** to invoke AI in team threads
- Seamless human + AI interaction in one place

## Starting and Managing Conversations

### Start a New Conversation

- **From Home**: Click the logo or **New Conversation**, type your query, then **Send**.
- **From History**: Open **History** in the sidebar **&gt;** **+ New Conversation** **&gt;** type and **Send**.
- **Using Slash Commands**: Type **/** to open the command palette, pick a command, follow prompts.

### Manage Conversations

- **Rename**: Open a conversation **&gt;** Click the title **&gt;** Enter a descriptive name **&gt;** **Enter**.
- **Delete**: In **History**, hover over a conversation **&gt;** click **🗑️ &gt;** confirm.
> **Important:** Deletion is permanent (messages and context are lost).

- **Star**: In the header, click **⭐** to pin/unpin. Starred items appear in the Starter Pane.

### Conversation Titles

Auto-generated titles summarize content. You can rename anytime to match team conventions.

## Response Styles

Response styles tailor tone and depth to your audience or task.

### Available Styles

1. **Data Engineer:** Technical depth, code/SQL where relevant, performance tips, lineage/schema details, troubleshooting.
2. **Business Analyst:** Business-friendly language, summary-first, visuals (charts/trends), executive-ready recommendations.
3. **Data Steward:** Governance focus, compliance terms, policy best practices, metadata and stewardship guidance.
4. **Casual:** Conversational, concise, low-jargon, ideal for quick lookups.

### Select a Style

Use the **Response Style** dropdown in the conversation header. The choice applies to the current conversation and persists until changed.

## Thought Process Visibility

The **Agent Thinking** panel explains how ADM interprets and answers your query.

### Benefits

- Understand the reasoning path
- Verify the agents, tools, and data sources used
- Debug unexpected results
- Improve prompts by seeing how questions are parsed
- Support audit and governance reviews

### What You’ll See

- Question analysis and time frame interpretation
- Agent selection and rationale
- Execution plan and data retrieval steps
- Processing/transformations
- Response formatting plan

### Interact with the Panel

- Click the header to expand/collapse
- Review during debugging, audits, or training

**Example**
 **Query:** “Show me failed data quality policies from the last 24 hours.”
 **Agent Thinking:** Identify policy results → filter `status=failed` and `time=24h` → query Data Quality Agent → prepare table view.

## Sharing and Collaboration

### Share a Conversation

1. Open the conversation → click **Share**.
2. Search and select recipients.
3. Set permissions:
    - **View Only**: Read-only
    - **Can Comment**: Add comments only
    - **Can Edit**: Read, continue, and interact with ADM

4. (Optional) Add a message → **Share**.

### Manage Access

- View who has access and their permissions
- Modify permissions or remove access
- Transfer ownership when needed

### Collaborative Features

- Real-time updates without refresh
- **@mentions** to notify teammates
- Threaded comments for complex topics
- Attribution for actions and messages
- **@adm** to bring AI into team discussions

> Note Sharing requires proper **view:user** permissions. Contact your administrator if access is restricted.

## Export and Documentation

### Download as PDF

Export complete conversation history with preserved formatting.

**Includes**

- Full message history with timestamps and authors
- Tables, charts, and code blocks
- (Optional) Agent Thinking steps
- Suggested actions and follow-ups

**How to Export**
 Open the conversation **&gt;** **Download as PDF** **&gt;** file downloads (e.g., `ADM_Conversation_2025-10-25.pdf`).

**Use Cases**

- Compliance/audit trails
- Stakeholder updates and summaries
- Knowledge base and training material
- Report appendices and documentation

### Dashboard View (Experimental)

Switch to an interactive dashboard summarizing conversation analytics (counts, response times, agents used, asset distributions, timelines). Export as image for presentations and reports.

> Features may change; share feedback to guide improvements.

## Conversation Actions and Follow-ups

### Contextual Actions

ADM suggests actions based on the current topic:

- **Asset management**: Tag assets, create workflows, visualize pipeline/lineage
- **Policy management**: Create/modify policies, schedule executions
- **Investigation**: Open asset details, inspect lineage, view incident reports

### Suggested Follow-up Questions

After each response, ADM proposes 3–5 targeted follow-ups:

- **Detail-oriented**: e.g., “List all columns and types for CUSTOMER_ADDRESS.”
- **Action-oriented**: e.g., “Create a data quality policy for this table.”
- **Exploratory**: e.g., “Which other tables reference customer addresses?”

Click any suggestion to add it to the conversation.

### Response Feedback

- **👍/👎** to rate quality
- **Copy** to clipboard
- **Regenerate** to try a new answer
 (Feedback informs future improvements.)

## Knowledge Base Integration

### Add Documents

Support formats: **PDF**, **DOCX**, **TXT**, **MD**
 **Settings &gt; Knowledge Base &gt; Upload Document** **&gt;** wait for indexing.

### What Indexing Does

- Extracts text
- Builds searchable embeddings
- Surfaces key concepts and relationships

### Use in Conversations

ADM automatically references relevant documents after indexing and may cite them in responses.
 Verify by asking about uploaded content and checking the Agent Thinking panel.

## Best Practices

### Write Effective Questions

- **Be specific**: “Show failed DQ policies for customer tables in the last 7 days.”
- **Provide context**: “Most accessed Snowflake tables in the `sales` database?”
- **Use natural language**: Ask as you would a colleague.

### Organize Conversations

- **Rename clearly**: e.g., “Q4 2025 Sales DQ Analysis,” “Customer Address Standardization”
- **Star** key threads (references, live investigations, major findings)
- **Archive/Delete** outdated or duplicate threads

### Collaborate Well

- Share for multi-party investigations, onboarding, cross-functional work
- Set permissions appropriately (View / Comment / Edit)
- Add context and @mention teammates

### Optimize Performance

- Start new threads for very long or unrelated topics
- Break complex prompts into smaller steps
- Constrain time ranges and sources where possible

## Troubleshooting

### ADM not responding / timing out

- Simplify the query or split steps
- Check your network connection
- Try again shortly (system load)
- Start a new conversation if the thread is very long

### Inaccurate responses

- Be more specific and add context
- Confirm required data sources are connected
- Ensure relevant agents are enabled
- Review Agent Thinking to verify reasoning and sources

### Cannot share conversations

- Confirm **view:user** permission
- Verify the recipient exists in your org
- Re-authenticate and retry
- Contact your administrator if the issue persists

### PDF export issues

- Allow pop-ups / check download permissions
- Ensure local disk space
- Try another browser
- For very long threads, export sections

### Dashboard view problems

- Refresh or clear cache
- Try a different browser
- Remember it’s experimental and may have limitations

### Getting help

- Use **Help** in the top bar for docs
- Review suggested follow-ups and Agent Thinking
- Contact your admin for permission issues
- Provide conversation IDs when reporting problems to support