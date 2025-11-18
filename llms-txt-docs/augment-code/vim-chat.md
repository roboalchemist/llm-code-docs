# Source: https://docs.augmentcode.com/vim/using-augment/vim-chat.md

# Chat

> Use Chat to explore your codebase, quickly get up to speed on unfamiliar code, and get help working through a technical problem.

export const Next = ({children}) => <div className="border-t border-b pb-8 border-gray dark:border-white/10">
    <h3>Next steps</h3>
    {children}
  </div>;

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

export const Command = ({text}) => <span className="font-bold">{text}</span>;

## Using chat

Chat is a new way to work with your codebase using natural language. Use Chat to explore your codebase, quickly get up to speed on unfamiliar code, and get help working through a technical problem.

| Command                                         | Action                           |
| :---------------------------------------------- | :------------------------------- |
| <Keyboard shortcut=":Augment chat <message>" /> | Send a chat message to Augment   |
| <Keyboard shortcut=":Augment chat-new" />       | Start a new chat conversation    |
| <Keyboard shortcut=":Augment chat-toggle" />    | Toggle the chat panel visibility |

### Sending a message

You can send a message to Chat using the <Keyboard shortcut=":Augment chat" /> command. You can send your message as an optional argument to the command or enter it into the command-line when prompted. Each new message will continue the current conversation which will be used as context for your next message.

**Focusing on selected text**

If you have text selected in `visual mode`, Augment will automatically include it in your message. This is useful for asking questions about specific code or requesting changes to the selected code.

### Starting a new conversation

You can start a new conversation by using the <Keyboard shortcut=":Augment chat-new" /> command.

<Next>
  * [Using Completions](/vim/using-augment/vim-completions)
  * [Configure keyboard shortcuts](/vim/setup-augment/vim-keyboard-shortcuts)
</Next>
