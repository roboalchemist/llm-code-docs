# Source: https://docs.acceldata.io/documentation/core-concepts.md

# Core Concepts

## What Is a Conversation?

A **conversation** in ADM is an interactive session between you and the AI system, similar to a continuous dialogue where:

- Context is maintained throughout the session
- Each message builds upon the previous one
- The AI remembers prior exchanges
- You can branch naturally into related topics

This design allows ADM to understand your intent, maintain continuity, and deliver more accurate responses.

### Anatomy of A Conversation

![](https:\/\/uploads.developerhub.io\/prod\/Yoq2\/czkm2euabvmbyl6a8irqdyhvp8zbrzy4rcg7sk0xxfrl43xaeck4f8r4ojpjbjf0.png)

## Conversation Lifecycle

Each conversation follows a simple lifecycle:

| **Stage** | **Description** | 
| ---- | ---- | 
| **Initiation** | You start a new conversation or resume an existing one. ADM loads your context, preferences, and initial prompt. | 
| **Active** | Messages are exchanged. ADM processes input, invokes agents, triggers workflows, and updates context. | 
| **Paused** | The session is inactive but saved. Context is preserved, and the conversation appears in your history for later use. | 
| **Archived** | Older conversations are searchable but not active. You can restore them as needed. | 


## Context and Memory

### How ADM Maintains Context

ADM uses multiple layers of context to interpret and remember your interactions.

| **Source** | **What It Tracks** | 
| ---- | ---- | 
| **Conversation History** | Messages, previous questions, responses, and actions taken. | 
| **User Profile** | Your role, preferences, and frequently used terms. | 
| **Knowledge Base** | Organization-specific documents, uploaded files, and domain knowledge. | 
| **System State** | Current data catalog, recent policy changes, and asset status. | 


### Context Limits

Each conversation has a **context window** that determines how much past information ADM can reference.
 For very long or unrelated discussions:

- ADM may summarize earlier parts of the session.
- Start a new conversation for unrelated topics to maintain clarity and performance.

## Best Practices

### Do's

- Start conversations with clear intent
- Provide context for ambiguous terms
- Use follow-up questions to refine responses
- Star important conversations for later reference
- Use descriptive titles when renaming conversations

### Dont's

- Mix unrelated topics in same conversation
- Assume AI knows unstated context
- Use conversations for real-time monitoring
- Share sensitive information in conversation titles

## Conversation History and Management

### Accessing Conversation History

You can view and manage your past conversations to stay organized.

1. Click the **conversation icon** in the left sidebar.
2. The **History Panel** opens, displaying conversations grouped by:
    - **Last 7 days**
    - **Last 30 days**
    - **Older conversations**

### Filtering Options

| **Filter** | **Description** | 
| ---- | ---- | 
| **All** | Displays all your conversations. | 
| **Starred** | Shows conversations you’ve marked as important. | 
| **Shared** | Lists conversations shared with or by you. | 


### Conversation List View

Each conversation in the list shows:

- Title or first few words of the conversation
- Last activity timestamp
- Participant avatars (for shared items)
- Star indicator (if marked)
- **More options (⋮)** menu for management actions

### Managing Conversations

From the **More Options (⋮)** menu, you can:

- Rename a conversation
- Star or unstar it
- Share it with specific team members
- Delete it permanently
- View detailed metadata