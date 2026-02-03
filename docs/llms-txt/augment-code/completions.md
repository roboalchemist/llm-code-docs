# Source: https://docs.augmentcode.com/using-augment/completions.md

# Source: https://docs.augmentcode.com/jetbrains/using-augment/completions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Completions

> Use code completions to get more done. Augment's radical context awareness means more relevant suggestions, fewer hallucinations, and less time hunting down documentation.

export const MoreVertIcon = () => <div className="inline-block w-4 h-4 mr-2">
    <svg xmlns="http://www.w3.org/2000/svg" height="20px" viewBox="0 -960 960 960" width="20px" fill="#5f6368">
      <path d="M479.79-192Q450-192 429-213.21t-21-51Q408-294 429.21-315t51-21Q510-336 531-314.79t21 51Q552-234 530.79-213t-51 21Zm0-216Q450-408 429-429.21t-21-51Q408-510 429.21-531t51-21Q510-552 531-530.79t21 51Q552-450 530.79-429t-51 21Zm0-216Q450-624 429-645.21t-21-51Q408-726 429.21-747t51-21Q510-768 531-746.79t21 51Q552-666 530.79-645t-51 21Z" />
    </svg>
  </div>;

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

export const Command = ({text}) => <span className="font-bold">{text}</span>;

## About Code Completions

Augment's Code Completions integrates with your IDE's native completions system to give you autocomplete-like suggestions as you type. You can accept all of a suggestion, accept partial suggestions a word or a line at a time, or just keep typing to ignore the suggestion.

## Using Code Completions

To use code completions, simply start typing in your IDE. Augment will provide suggestions based on the context of your code. You can accept a suggestion by pressing <Keyboard shortcut="Tab" />, or ignore it by continuing to type.

For example, add the following function to a TypeScript file:

```typescript  theme={null}
function getUser(): Promise<User>;
```

As you type `getUser`, Augment will suggest the function signature. Press <Keyboard shortcut="Tab" /> to accept the suggestion. Augment will continue to offer suggestions until the function is complete, at which point you will have a function similar to:

```typescript  theme={null}
function getUser(): Promise<User> {
  return fetch("/api/user/1")
    .then((response) => response.json())
    .then((json) => {
      return json as User;
    });
}
```

### Accepting Completions

<Tabs>
  <Tab title="MacOS">
    <Tip>
      We recommend configuring a custom keybinding to accept a word or line, see
      [Keyboard shortcuts](/setup-augment/vscode-keyboard-shortcuts) for more
      details.
    </Tip>

    | Action                         | Default keyboard shortcut                       |
    | :----------------------------- | :---------------------------------------------- |
    | Accept inline suggestion       | <Keyboard shortcut="Tab" />                     |
    | Accept next word of suggestion | <Keyboard shortcut="Cmd →" />                   |
    | Accept next line of suggestion | None (see above)                                |
    | Reject suggestion              | <Keyboard shortcut="Esc" />                     |
    | Ignore suggestion              | Continue typing through the suggestion          |
    | Toggle automatic completions   | VSCode: <Keyboard shortcut="Cmd Option A" />    |
    |                                | JetBrains: <Keyboard shortcut="Cmd Option 9" /> |
  </Tab>

  <Tab title="Windows/Linux">
    <Tip>
      We recommend configuring a custom keybinding to accept a word or line, see
      [Keyboard shortcuts](/setup-augment/vscode-keyboard-shortcuts) for more
      details.
    </Tip>

    | Action                         | Default keyboard shortcut                     |
    | :----------------------------- | :-------------------------------------------- |
    | Accept inline suggestion       | <Keyboard shortcut="Tab" />                   |
    | Accept next word of suggestion | <Keyboard shortcut="Ctrl →" />                |
    | Accept next line of suggestion | None (see above)                              |
    | Reject suggestion              | <Keyboard shortcut="Esc" />                   |
    | Ignore suggestion              | Continue typing through the suggestion        |
    | Toggle automatic completions   | VSCode: <Keyboard shortcut="Ctrl Alt A" />    |
    |                                | JetBrains: <Keyboard shortcut="Ctrl Alt 9" /> |
  </Tab>
</Tabs>

### Disabling Completions

<Tabs>
  <Tab title="Visual Studio Code">
    You can disable automatic code completions by clicking the overflow menu icon<MoreVertIcon />at the top-right of the Augment panel, then selecting <Command text="Turn Automatic Completions Off" />.
  </Tab>

  <Tab title="JetBrains IDEs">
    You can disable automatic code completions by clicking the Augment icon <img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=7564ed27ae27d8e8e8d37fc0c5390710" className="inline h-3 p-0 m-0" data-og-width="18" width="18" data-og-height="12" height="12" data-path="images/augment-icon-smile.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=e768e602ba7fbca6dee54bd80707a65f 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=2bff5c6e247ef06ee8c8aaf10b729fdb 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=f137c3896e95e4ae83d7374bde6fce21 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=30c491bbedc2350eeac401d6bdb88a1d 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=2b87100b107e7236c3c415c046fd988b 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=a39dac81c0ae990b2c8143421f4144c5 2500w" /> in the status bar at the bottom right corner of your IDE, then selecting <Command text="Disable Completions" />.
  </Tab>
</Tabs>

### Enable Completions

<Tabs>
  <Tab title="Visual Studio Code">
    If you've temporarily disabled completions, you can re-enable them by clicking the overflow menu icon<MoreVertIcon />at the top-right of the Augment panel, then selecting <Command text="Turn Automatic Completions On" />.
  </Tab>

  <Tab title="JetBrains IDEs">
    If you've temporarily disabled completions, you can re-enable them by clicking the Augment icon <img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=7564ed27ae27d8e8e8d37fc0c5390710" className="inline h-3 p-0 m-0" data-og-width="18" width="18" data-og-height="12" height="12" data-path="images/augment-icon-smile.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=e768e602ba7fbca6dee54bd80707a65f 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=2bff5c6e247ef06ee8c8aaf10b729fdb 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=f137c3896e95e4ae83d7374bde6fce21 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=30c491bbedc2350eeac401d6bdb88a1d 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=2b87100b107e7236c3c415c046fd988b 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/augment-icon-smile.svg?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=a39dac81c0ae990b2c8143421f4144c5 2500w" /> in the status bar at the bottom right corner of your IDE, then selecting <Command text="Enable Completions" />.
  </Tab>
</Tabs>
