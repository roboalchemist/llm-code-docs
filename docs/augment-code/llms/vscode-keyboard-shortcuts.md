# Source: https://docs.augmentcode.com/setup-augment/vscode-keyboard-shortcuts.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Keyboard Shortcuts for Visual Studio Code

> Augment integrates with your IDE to provide keyboard shortcuts for common actions. Use these shortcuts to quickly accept suggestions, write code, and navigate your codebase.

export const Command = ({text}) => <span className="font-bold">{text}</span>;

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

## About keyboard shortcuts

Augment is deeply integrated into your IDE and utilizes many of the standard keyboard shortcuts you are already familiar with. These shortcuts allow you to quickly accept suggestions, write code, and navigate your codebase. We also suggest updating a few keyboard shortcuts to make working with code suggestions even easier.

<Tabs>
  <Tab title="MacOS">
    To update keyboard shortcuts, use one of the following:

    | Method          | Action                                                                                                  |   |
    | :-------------- | :------------------------------------------------------------------------------------------------------ | - |
    | Keyboard        | <Keyboard shortcut="Cmd K" /> then <Keyboard shortcut="Cmd S" />                                        |   |
    | Menu bar        | <Command text="Code > Settings... > Keyboard Shortcuts" />                                              |   |
    | Command palette | <Keyboard shortcut="Cmd Shift P" /> then search <Command text="Preferences: Open Keyboard Shortcuts" /> |   |

    ## General

    | Action                | Recommended shortcut                |
    | :-------------------- | :---------------------------------- |
    | Open Augment panel    | <Keyboard shortcut="Cmd L" />       |
    | Show Augment commands | <Keyboard shortcut="Cmd Shift A" /> |

    ## Chat

    | Action                   | Default shortcut              |
    | :----------------------- | :---------------------------- |
    | Focus or open Chat panel | <Keyboard shortcut="Cmd L" /> |

    ## Next Edit

    | Action            | Default shortcut                    |
    | :---------------- | :---------------------------------- |
    | Go to next        | <Keyboard shortcut="Cmd ;" />       |
    | Go to previous    | <Keyboard shortcut="Cmd Shift ;" /> |
    | Accept suggestion | <Keyboard shortcut="Enter" />       |
    | Reject suggestion | <Keyboard shortcut="Backspace" />   |

    ## Instructions

    | Action            | Default shortcut               |
    | :---------------- | :----------------------------- |
    | Start instruction | <Keyboard shortcut="Cmd I" />  |
    | Accept            | <Keyboard shortcut="Return" /> |
    | Reject            | <Keyboard shortcut="Esc" />    |

    ## Completions

    | Action                         | Default keyboard shortcut              |
    | :----------------------------- | :------------------------------------- |
    | Accept inline suggestion       | <Keyboard shortcut="Tab" />            |
    | Accept next word of suggestion | <Keyboard shortcut="Cmd →" />          |
    | Accept next line of suggestion | None (see below)                       |
    | Reject suggestion              | <Keyboard shortcut="Esc" />            |
    | Ignore suggestion              | Continue typing through the suggestion |
    | Toggle automatic completions   | <Keyboard shortcut="Cmd Option A" />   |

    **Recommended shortcuts**

    We recommend updating your keybindings to include the following shortcuts to
    make working with code suggestions even easier. These changes update the
    default behavior of Visual Studio Code.

    | Action                         | Recommended shortcut               |
    | :----------------------------- | :--------------------------------- |
    | Accept next line of suggestion | <Keyboard shortcut="Cmd Ctrl →" /> |
  </Tab>

  <Tab title="Windows/Linux">
    To update keyboard shortcuts, use one of the following:

    | Method          | Action                                                                                                   |
    | :-------------- | :------------------------------------------------------------------------------------------------------- |
    | Keyboard        | <Keyboard shortcut="Ctrl K" /> then <Keyboard shortcut="Ctrl S" />                                       |
    | Menu bar        | <Command text="File > Settings... > Keyboard Shortcuts" />                                               |
    | Command palette | <Keyboard shortcut="Ctrl Shift P" /> then search <Command text="Preferences: Open Keyboard Shortcuts" /> |

    ## General

    | Action                | Recommended shortcut                 |
    | :-------------------- | :----------------------------------- |
    | Open Augment panel    | <Keyboard shortcut="Ctrl L" />       |
    | Show Augment commands | <Keyboard shortcut="Ctrl Shift A" /> |

    ## Chat

    | Action                   | Default shortcut               |
    | :----------------------- | :----------------------------- |
    | Focus or open Chat panel | <Keyboard shortcut="Ctrl L" /> |

    ## Next Edit

    | Action            | Default shortcut                     |
    | :---------------- | :----------------------------------- |
    | Go to next        | <Keyboard shortcut="Ctrl ;" />       |
    | Go to previous    | <Keyboard shortcut="Ctrl Shift ;" /> |
    | Accept suggestion | <Keyboard shortcut="Enter" />        |
    | Reject suggestion | <Keyboard shortcut="Backspace" />    |

    ## Instructions

    | Action            | Default shortcut               |
    | :---------------- | :----------------------------- |
    | Start instruction | <Keyboard shortcut="Ctrl I" /> |
    | Accept            | <Keyboard shortcut="Return" /> |
    | Reject            | <Keyboard shortcut="Esc" />    |

    ## Completions

    | Action                         | Default keyboard shortcut              |
    | :----------------------------- | :------------------------------------- |
    | Accept inline suggestion       | <Keyboard shortcut="Tab" />            |
    | Accept next word of suggestion | <Keyboard shortcut="Ctrl →" />         |
    | Accept next line of suggestion | None (see below)                       |
    | Reject suggestion              | <Keyboard shortcut="Esc" />            |
    | Ignore suggestion              | Continue typing through the suggestion |
    | Toggle automatic completions   | <Keyboard shortcut="Ctrl Alt A" />     |

    **Recommended shortcuts**

    We recommend updating your keybindings to include the following shortcuts to
    make working with code suggestions even easier. These changes update default
    behavior of Visual Studio Code.

    | Action                         | Recommended shortcut               |
    | :----------------------------- | :--------------------------------- |
    | Accept next line of suggestion | <Keyboard shortcut="Ctrl Alt →" /> |
  </Tab>
</Tabs>
