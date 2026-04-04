# Source: https://docs.acceldata.io/documentation/multi-user-collaboration.md

# Multi-User Collaboration

## Understanding Group Conversations

ADM transforms data management into a collaborative, real-time experience. Unlike ticketing systems or email threads, **ADM group conversations** maintain full context while allowing multiple participants to analyze data, share insights, and leverage AI assistance simultaneously.

Group conversations serve three core purposes in enterprise data management:

1. **Cross-functional collaboration** – Teams from different disciplines can jointly investigate issues, combining technical and business expertise.
2. **Living documentation** – Every message, decision, and rationale is recorded, creating a transparent decision trail.
3. **Democratized insights** – Team members with varying technical backgrounds can contribute meaningfully to governance and quality discussions.

When you initiate a group conversation, ADM retains full context across all participants. If a data engineer shares the conversation with a business analyst, both see the entire history, including AI-generated insights, visualizations, and suggested actions. ADM automatically enforces permission boundaries, ensuring users only see data they are authorized to access, maintaining security while fostering collaboration.

## Creating and Managing Group Conversations

### Starting a Group Conversation

You can create a collaborative workspace in two ways, depending on your workflow.

#### Option 1: Create a New Group Conversation

1. From the ADM home screen, click **New Conversation**.
2. In the conversation header, select **Share & Chat with Users**.
3. ADM converts the conversation into a collaborative workspace.
4. The system generates a shareable link and displays an **invitation dialog** where you can search colleagues by name or email.

As you type, ADM searches your organization’s directory and displays matching users with profile photos and roles. You can select multiple users simultaneously; invitations are sent as in-app notifications and (optionally) via email.

#### Option 2: Convert an Existing Conversation

If you start investigating alone and later need input, open the existing conversation and click **Share & Chat**. ADM preserves all prior context, queries, AI responses, and generated artifacts such as dashboards or policies.

When inviting new users, you can add an **introductory message** summarizing the current status, findings, and specific areas where you need feedback. New participants see this context first, helping them quickly understand the discussion without requiring backtracking.

### Real-Time Collaboration Features

#### Presence Indicators and Typing Awareness

Active participants appear as profile avatars at the top of the chat. ADM shows who’s currently viewing or typing, preventing message overlap and improving conversational flow.

#### Message Attribution and Threading

Each message displays the author’s name and avatar. Rapid consecutive messages from the same user are grouped for readability. You can use **@mentions** to reply to specific messages or direct questions to individuals, enabling light threading without clutter.

#### Synchronized Updates

All participants see new messages and ADM responses in real time, no refresh required. When ADM processes a query, results and the **AI thought process** appear for everyone simultaneously, promoting shared understanding and trust in the AI’s reasoning.

## Using @adm in Collaborative Contexts

The **@adm** feature turns ADM into an active team member. Mentioning `@adm` within your conversation invokes the AI assistant to answer questions, perform analysis, or generate recommendations based on the conversation’s full context.

### How @adm Works

When you type `@adm` followed by a query, the assistant interprets it using the entire conversation history. For example:

> `“@adm what are the most common data quality problems in the`customer_master`table over the last 30 days?”`

ADM understands that you’re investigating data quality, not asking for schema details.

### Effective Usage Patterns

Treat @adm as a **data expert** in the room, use it for targeted, high-value questions.
 Common productive uses include:

- **Fact checking:** `@adm what’s the freshness threshold for the sales_daily table?`
- **Summarization:** `@adm summarize key decisions made about policy updates.`
- **Scenario testing:** `@adm what happens if we change reconciliation frequency from daily to hourly?`

Avoid invoking @adm for every minor question. Batch related queries or reserve it for pivotal analysis moments. Remember, ADM provides data-driven insights, but human interpretation remains essential.

### Response Integration

ADM responses appear with the ADM logo and subtle background highlighting. Responses often include:

- Charts, data tables, or sample records
- Suggested next actions (e.g., “Create Policy,” “View Asset”)
- Links to relevant ADOC assets for deeper exploration

All participants see @adm’s responses immediately and can build on them with follow-up questions.

## Permission Models and Access Control

ADM’s collaboration model combines flexibility with security. Every conversation has layered permissions that govern both user actions and data visibility.

### Permission Levels

#### Viewer

- **Purpose:** Passive visibility for stakeholders and auditors.
- **Capabilities:** Read all messages and ADM responses, view artifacts and updates in real time.
- **Restrictions:** Cannot post, invoke @adm, invite others, or modify settings.
- **Typical roles:** Managers, auditors, or informed stakeholders.

#### Participant

- **Purpose:** Active contributors.
- **Capabilities:** Send messages, ask questions, invoke @adm, generate dashboards or PDFs, and star conversations.
- **Restrictions:** Cannot invite or modify other users.

#### Owner

- **Purpose:** Conversation administrators.
- **Capabilities:** All participant permissions plus:
    - Add or remove users
    - Modify permission levels
    - Rename or delete the conversation
    - Manage privacy and visibility settings

Owners are typically the conversation creators but can delegate ownership for continuity.

### Permission Inheritance and Data Access

ADM enforces **two layers of control**:

1. **Conversation permissions** – define user actions.
2. **Data permissions** – define what data each user can see (inherited from ADOC).

When ADM responds to a query, it automatically filters results based on each participant’s data permissions. If a user lacks access to certain datasets, ADM redacts those portions instead of exposing unauthorized data.

### Managing Permissions

Owners manage access through the **Participants Panel** in the conversation header.

- The panel lists each participant’s role, status, and join date.
- Changes take effect instantly, and users receive in-app notifications (e.g., _“You can now contribute to this conversation and use @adm.”_).
This transparency ensures clarity around user capabilities.

## Collaboration Best Practices

### Structuring Productive Conversations

Start with a clear objective or problem statement. Define what you’re investigating and why. For complex initiatives, create **separate conversations** for different workstreams (e.g., “Customer Data Quality – Root Cause” vs. “Customer Data Quality – Policy Review”).

Establish consistency:

- Begin daily sessions with quick status updates.
- Maintain a running list of key decisions and next steps.

### Optimizing Team Dynamics

Involve the right mix of roles, data engineers, business analysts, and compliance officers.
 Avoid overcrowding; excessive participants slow progress.
 Consider applying a **RACI framework**:

- **Responsible:** Core analysts
- **Accountable:** Conversation owners
- **Consulted:** SMEs via targeted @mentions
- **Informed:** Viewers and stakeholders

### Maintaining Conversation Hygiene

- Use `@adm summarize` periodically to create checkpoints before adding new participants.
- Archive completed conversations to preserve institutional knowledge instead of deleting them.
- Adopt a naming convention such as: `YYYY-MM-[Topic]-[DataAsset]-[Status]`
    - _Example:_ `2025-01-DataQuality-CustomerTable-Resolved`.

### Security and Compliance

- Restrict sensitive topics to smaller groups or private conversations.
- Review access lists regularly, especially for ongoing projects.
- ADM logs all permission changes, ensuring a complete compliance audit trail.

## Advanced Collaboration Scenarios

### Cross-Functional Investigations

For multi-system issues, create a **main investigation conversation** and **sub-conversations** for technical or domain-specific analysis. Example: A reconciliation issue may have:

- One thread for source data validation
- One for transformation logic
- One for business impact assessment

Each sub-conversation links back to the main thread for traceability.

### Policy Development Workflows

Use @adm to identify data quality gaps and draft policies collaboratively. Participants can refine rules, test logic, and finalize wording in real time. Once approved, owners can **create the policy directly from the conversation**, with ADM auto-populating metadata and rationale.

### Incident Response Coordination

During incidents, group conversations act as **command centers**.

- The owner (incident commander) manages participants dynamically.
- ADM provides live impact analysis, affected system lists, and remediation guidance.
After resolution, the conversation becomes a full **post-incident record**, complete with timelines, actions, and decisions.

## Integration with ADOC Features

ADM group conversations integrate seamlessly with ADOC’s governance platform.

### Asset and Policy Linking

References to assets or policies automatically hyperlink to their ADOC records. Clicking a link opens the corresponding detail view, allowing quick cross-navigation between context and data.

### Dashboard Generation

ADM can generate **interactive dashboards** directly from conversation insights. These remain linked to the originating thread, preserving context for future reference.