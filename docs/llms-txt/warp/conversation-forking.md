# Source: https://docs.warp.dev/agents/using-agents/agent-conversations/conversation-forking.md

# Conversation Forking

Warp allows you to **fork conversations** to create a new thread that inherits all of the context, messages, and history from an existing conversation. This is useful when you want to branch off in a new direction without affecting the original conversation.

{% embed url="<https://www.loom.com/share/15164f2abc19437ebefb47a8c6b52eb8?t=54>" %}

### How conversation forking works

* When you fork a conversation, the new thread starts with the same context and history as the original.
* Any follow-ups in the forked conversation do **not** impact the original. Likewise, continuing in the original conversation does not change the fork.
* Forked conversations behave just like any other conversation: you can move them into new windows, panes, or tabs.

*Example*: You can fork a conversation to explore an alternate solution, ask “what if” questions, or continue down two separate paths in parallel.

### Ways to fork a conversation

There are four ways to fork an existing conversation:

#### **1. From the command palette**

Open the menu using the command palette (`CMD + Y` on macOS / `CTRL + SHIFT + Y` on Windows/Linux).

Select **Fork current conversation** to fork your current conversation, or fork a specific conversation from open conversations.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-76923961454a4ed5b990183d7b84aeed22f1697b%2Fconversation-forking-palette.png?alt=media" alt=""><figcaption></figcaption></figure>

In addition, when you hover over any open conversation in the command palette, you’ll see a **fork button**. This lets you fork not only active conversations, but also inactive and historical ones.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-78a0cc4938a84942ef2e0226cccb9d3d953a7718%2Fconversation-forking-open-conversations.png?alt=media" alt=""><figcaption></figcaption></figure>

You can also access this conversation view from the [universal input chip](https://docs.warp.dev/terminal/universal-input) in the current conversation.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-4ad356110556f0fd52eae5e17187ad633b484cef%2Fconversation-forking-chip.png?alt=media" alt=""><figcaption></figcaption></figure>

#### **2. From the footer of the most recent AI response block**

In any conversation in the blocklist, click the **fork button** in the footer of the most recent AI block. A new conversation opens in a separate pane with the full context of the original.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2Fgit-blob-4d05d9b53ff9e7c2efbbd96d0a0a659ac87a786e%2Fconversation-forking-footer.png?alt=media" alt=""><figcaption></figcaption></figure>

#### **3. Using the /fork slash command**

Type `/fork` in the input to fork the current conversation. You can optionally include a prompt after the command, and Warp will send that prompt in the newly forked conversation.

*Example*: `/fork Can you try a different approach?` Forks the selected conversation and immediately sends `Can you try a different approach?` in the forked conversation.

#### **4. Using the /fork-and-compact slash command**

Type `/fork-and-compact` to fork the current conversation and automatically compact the forked version. This combines forking with [context window management](https://docs.warp.dev/agents/using-agents/agent-conversations/..#context-window-management), giving you a fresh start with a summarized context.

<figure><img src="https://2297236823-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MbqIgTw17KQvq_DQuRr%2Fuploads%2FFx3AICg8vQltUuRPgGIT%2Fimage.png?alt=media&#x26;token=4676d2d2-f86a-4e24-9a86-3834e689cb7a" alt=""><figcaption></figcaption></figure>

### Fork from anywhere in a conversation

In addition to forking from the end of a conversation, you can fork from any point in the conversation history. This lets you return to an earlier agent response and branch off in a new direction from there.

{% embed url="<https://youtu.be/SlhF4_0bBxY>" %}

To fork from a specific point, **right-click** on any agent response block or click the three-dot menu in the top-right corner of the block.&#x20;

* Select **Fork conversation from here** to create a new conversation that includes everything up to and including that response, but excludes any queries or responses that came after it.

**This is particularly useful for:**

* **Exploring alternate paths** - Go back to a point where the conversation was on track and try a different approach.
* **Managing your context window** - If a conversation has grown too long, fork from an earlier point to continue with only the relevant context.
* **Preventing context pollution** - When a conversation has accumulated errors or gone off track, fork from before those issues occurred to start fresh.

### Using forked conversations <a href="#using-forked-conversations" id="using-forked-conversations"></a>

* Once forked, you can continue prompting as if you were still in the original conversation. The original conversation remains unchanged, allowing you to reference or continue both in parallel.
* For example, after forking you might ask *“Could you explain more?”* and Warp will respond using the inherited context.

**Forking is especially useful when:**

* You want to explore different approaches without losing the original thread.
* You need to keep one conversation “clean” while experimenting in another.
* You want to reuse context or specific blocks from older conversations.
