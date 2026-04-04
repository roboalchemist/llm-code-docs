# Source: https://docs.qodo.ai/qodo-documentation/qodo-gen/chat/chat-history.md

# Chat History

Qodo Chat maintains a history of your 20 most recent conversations, allowing you to review past interactions, refresh your memory, or explore new topics. You can continue a past chat to dive deeper into a topic or request additional information.

### Using Chat History <a href="#using-chat-history" id="using-chat-history"></a>

1. **Initiate a Command:** Call a command by typing it in the chatbox.
2. **Continue the Conversation:** At the end of Qodo's response, continue the conversation as long as you wish. Qodo will maintain the context of your initial query, providing tailored responses to your follow-up questions.
3. **Start a new Conversation:** Click on plus **+** button on the top right of the chat interface to start a new conversation. Your current chat history will be cleared, and Qodo will be ready to start a new conversation.
4. **Check your Chat History:** Next to the **New Chat** button, find the History button (clock with a round arrow) and click on it. The chat history interface will open. You can see your latest 20 chats with Qodo, switch to each one and continue the conversation if you wish.

<figure><img src="https://782320861-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FhllduvO2nHKZ2vKzfcEn%2Fuploads%2Fsorg4oIoip1WVo3nNVtL%2FScreenshot%202025-03-30%20at%2012.23.03.png?alt=media&#x26;token=c25ce339-eb9e-4a58-8608-6ff9e1507a3e" alt="" width="375"><figcaption></figcaption></figure>

5. **Chat Persistency:** Your chat history is saved between sessions, allowing you to revisit previous conversations even after closing your IDE. Chat history is saved on a **per-project basis**, so you only see the conversations relevant to your current project in the chat history section.

<figure><img src="https://782320861-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FhllduvO2nHKZ2vKzfcEn%2Fuploads%2FPCwl8hUYmb9EYmh7LUZ8%2FScreenshot%202025-03-30%20at%2012.22.17.png?alt=media&#x26;token=84bba245-f9f1-4fda-b440-3b31bf1dc925" alt="" width="375"><figcaption></figcaption></figure>

### Chat History File

Chat history is saved locally in the user's home directory at `.qodo/history`. The file is named using a hash of the workspace path to ensure uniqueness.

This file is automatically maintained. Any history that hasn’t been accessed in over 90 days is deleted.

#### History Migration

**VSCode users**: Chat history is **not** migrated during upgrades. Installing a new version of VSCode will remove previous conversations.

**JetBrains users**: Chat history is migrated during upgrades. Previous conversations will remain available after updating your JetBrains IDE.
