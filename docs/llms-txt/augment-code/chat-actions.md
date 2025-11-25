# Source: https://docs.augmentcode.com/using-augment/chat-actions.md

# Source: https://docs.augmentcode.com/jetbrains/using-augment/chat-actions.md

# Source: https://docs.augmentcode.com/using-augment/chat-actions.md

# Source: https://docs.augmentcode.com/jetbrains/using-augment/chat-actions.md

# Using Actions in Chat

> Actions let you take common actions on code blocks without leaving Chat. Explain, improve, or find everything you need to know about your codebase.

export const ArrowUpIcon = () => <div className="inline-block w-4 h-4 mr-2">
    <svg xmlns="http://www.w3.org/2000/svg" height="20px" viewBox="0 -960 960 960" width="20px" fill="#5f6368">
      <path d="M444-192v-438L243-429l-51-51 288-288 288 288-51 51-201-201v438h-72Z" />
    </svg>
  </div>;

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-actions.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=db5e93308abefb7782a8684ad79e2a50" alt="Augment Chat Actions" className="rounded-xl" data-og-width="1233" width="1233" data-og-height="630" height="630" data-path="images/chat-actions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-actions.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=24ffba8783720d584f76090090aff0fe 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-actions.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=63f4c3aa42421df5ae79d40be85abfa8 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-actions.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=c9bfcc586feef6caa23ea46efa8fd1aa 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-actions.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=4fa3cd4a775a3865f92d954c842706cc 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-actions.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=ecc12c1fedeee7734b9e3a1bef2b434c 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/chat-actions.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=7e28137d1682a5b7c5d6376870b92a59 2500w" />

## Using actions in Chat

To use a quick action, you an use a <Keyboard shortcut="/" /> command or click the up arrow icon<ArrowUpIcon />to show the available actions. For explain, fix, and test actions, first highlight the code in the editor and then use the command.

| Action                           | Usage                                                                    |
| :------------------------------- | :----------------------------------------------------------------------- |
| <Keyboard shortcut="/find" />    | Use natural language to find code or functionality                       |
| <Keyboard shortcut="/explain" /> | Augment will explain the hightlighted code                               |
| <Keyboard shortcut="/fix" />     | Augment will suggest improvements or find errors in the highlighted code |
| <Keyboard shortcut="/test" />    | Augment will suggest tests for the highlighted code                      |

Augment will typically include code blocks in the response to the action. See [Applying code blocks from Chat](/using-augment/chat-apply) for more details.
