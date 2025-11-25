# Source: https://docs.augmentcode.com/using-augment/chat.md

# Source: https://docs.augmentcode.com/jetbrains/using-augment/chat.md

# Source: https://docs.augmentcode.com/using-augment/chat.md

# Source: https://docs.augmentcode.com/jetbrains/using-augment/chat.md

# Using Chat

> Use Chat to explore your codebase, quickly get up to speed on unfamiliar code, and get help working through a technical problem.

export const type_0 = "chats"

export const DeleteIcon = () => <div className="inline-block w-4 h-4 mr-2">
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="#5f6368" viewBox="0 -960 960 960">
      <path d="M280-120q-33 0-56.5-23.5T200-200v-520h-40v-80h200v-40h240v40h200v80h-40v520q0 33-23.5 56.5T680-120H280Zm400-600H280v520h400v-520ZM360-280h80v-360h-80v360Zm160 0h80v-360h-80v360ZM280-720v520-520Z" />
    </svg>
  </div>;

export const ChevronRightIcon = () => <div className="inline-block w-4 h-4 mr-2">
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="#5f6368" viewBox="0 -960 960 960">
      <path d="M504-480 320-664l56-56 240 240-240 240-56-56 184-184Z" />
    </svg>
  </div>;

export const NewChatIcon = () => <div className="inline-block w-4 h-4 mr-2">
    <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" fill="#5f6368" viewBox="0 -960 960 960">
      <path d="M120-160v-600q0-33 23.5-56.5T200-840h480q33 0 56.5 23.5T760-760v203q-10-2-20-2.5t-20-.5q-10 0-20 .5t-20 2.5v-203H200v400h283q-2 10-2.5 20t-.5 20q0 10 .5 20t2.5 20H240L120-160Zm160-440h320v-80H280v80Zm0 160h200v-80H280v80Zm400 280v-120H560v-80h120v-120h80v120h120v80H760v120h-80ZM200-360v-400 400Z" />
    </svg>
  </div>;

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

export const Command = ({text}) => <span className="font-bold">{text}</span>;

## About Chat

Chat is a new way to work with your codebase using natural language. Chat will automatically use the current workspace as context and you can [provide focus](/using-augment/chat-context) for Augment by selecting specific code blocks, files, folders, or external documentation. Details from your current chat, including the additional context, are used to provide more relevant code suggestions as well.

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-explain.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=d375d6ded40f6ed3353e002a9d9fa7a0" alt="Augment Chat" className="rounded-xl" data-og-width="1120" width="1120" data-og-height="1209" height="1209" data-path="images/chat-explain.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-explain.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=72a74689a8d1160c2ec3831e752cb266 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-explain.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=559d3b76f96a2df576305440cf5c241e 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-explain.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=48570a3aa134abe6d23ec6c8cfa5e314 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-explain.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=d175cf3cfaa04e1e9de9d2894d91ecc3 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-explain.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=7cfebd57e867659d7e847fbd25d3b207 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-explain.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=a197d0a8fe4e010828796d78d172d43e 2500w" />

## Accessing Chat

Access the Chat sidebar by clicking the Augment icon <img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-chat.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=5a70e197b4ab16c79e9612aac74015cf" className="inline h-4 p-0 m-0" data-og-width="676" width="676" data-og-height="592" height="592" data-path="images/augment-icon-chat.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-chat.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=2a32c9463cef1c6647f0dd08dd827cd2 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-chat.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=4cba744eb472e888403e462429f3c10a 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-chat.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=c8393d6a3463c6e6a99eca871d66ae67 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-chat.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=573abbe9afb002028f79741b4fa4bad4 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-chat.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=998af121c45992d4121b3fb97ee42007 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-chat.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=aa776a96f49e4d86cb0a0d7cef78cc67 2500w" /> in the sidebar or the status bar. You can also open Chat by using one of the keyboard shortcuts below.

**Keyboard Shortcuts**

| Platform      | Shortcut                       |
| :------------ | :----------------------------- |
| MacOS         | <Keyboard shortcut="Cmd L" />  |
| Windows/Linux | <Keyboard shortcut="Ctrl L" /> |

## Using Chat

To use Chat, simply type your question or command into the input field at the bottom of the Chat panel. You will see the currently included context which includes the workspace and current file by default. Use Chat to explain your code, investigate a bug, or use a new library. See [Example Prompts for Chat](/using-augment/chat-prompts) for more ideas on using Chat.

### Enhancing your prompt

You can improve the quality of your {type_0} by starting with a well crafted prompt. You can start with a quick or incomplete prompt and use the prompt enhancer to add relevant references, structure, and conventions from your codebase to improve the prompt before it is sent.

1. Write your prompt in the prompt input box
2. Click the Enhance Prompt ✨ button
3. Review and edit the enhanced prompt
4. Submit your prompt

### Conversations about code

To get the best possible results, you can go beyond asking simple questions or commands, and instead have a back and forth conversation with Chat about your code. For example, you can ask Chat to explain a specific function and then ask follow-up questions about possible refactoring options. Chat can act as a pair programmer, helping you work through a technical problem or understand unfamiliar code.

### Starting a new chat

You should start a new Chat when you want to change the topic of the conversation since the current conversation is used as part of the context for your next question. To start a new chat, open the Augment panel and click the new chat icon <NewChatIcon /> at the top-right of the Chat panel.

### Previous chats

You can continue a chat by clicking the chevron icon<ChevronRightIcon />at the top-left of the Chat panel. Your previous chats will be listed in reverse chronological order, and you can continue your conversation where you left off.

### Deleting a chat

You can delete a previous chat by clicking the chevron icon<ChevronRightIcon />at the top-left of the Chat panel to show the list of previous chats. Click the delete icon <DeleteIcon /> next to the chat you want to delete. You will be asked to confirm that you want to delete the chat.
