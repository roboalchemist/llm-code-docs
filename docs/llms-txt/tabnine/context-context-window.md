# Source: https://docs.tabnine.com/main/getting-started/tabnine-chat/chat-context/context-context-window.md

# Understanding Context

Each interaction with Tabnine Chat is essentially a question or an instruction to perform a code-related task.

The basic cycle of the chat sequence is a chain of questions and answers:

* The user asks a question.
* Tabnine returns an answer.

However, the question (or prompt) that you ask is just one part of the equation. There's also the context — the extra layer of information that accompanies your question. This context is provided to the Tabnine model alongside your explicit question, enabling it to deliver more accurate and relevant responses.

Understanding the context can help you get the most out of Tabnine.

### Context used by the Tabnine Chat

The context (or context window) includes the following elements:

1. User questions or instructions
2. Selected block of code from the current file (or the cursor location)
3. Current open file
4. Chat history from the current conversation, including all the previous questions and answers (Note: Chat history isn't shared between different conversations)
5. Relevant files or code blocks from the current user workspace (if Tabnine finds such relevant files)

### Context size limit and priorities

The size of the context window is limited. Tabnine applies all kinds of algorithms and heuristics to pick and prioritize the most relevant parts of the context for each situation.

However, the most important part of the context, besides the question, is the selected code and the open file, especially the areas right above the cursor or the selected block.
