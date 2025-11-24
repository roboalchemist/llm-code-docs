# Source: https://docs.augmentcode.com/jetbrains/setup-augment/jetbrains-keyboard-shortcuts.md

# Keyboard Shortcuts for JetBrains IDEs

> Augment integrates with your IDE to provide keyboard shortcuts for common actions. Use these shortcuts to quickly accept suggestions, write code, and navigate your codebase.

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

export const Command = ({text}) => <span className="font-bold">{text}</span>;

## About keyboard shortcuts

Augment is deeply integrated into your IDE and utilizes many of the standard keyboard shortcuts you are already familiar with. These shortcuts allow you to quickly accept suggestions, write code, and navigate your codebase. We also suggest updating a few keyboard shortcuts to make working with code suggestions even easier.

<Tabs>
  <Tab title="MacOS">
    To update keyboard shortcuts, use one of the following:

    | Method   | Action                                                         |
    | :------- | :------------------------------------------------------------- |
    | Keyboard | <Keyboard shortcut="Cmd ," /> select <Command text="Keymap" /> |
    | Menu bar | <Command text="IntelliJ IDEA > Settings > Keymap" />           |

    ## General

    | Action             | Default shortcut                     |
    | :----------------- | :----------------------------------- |
    | Open Augment panel | <Keyboard shortcut="Cmd Option I" /> |

    ## Chat

    | Action                   | Default shortcut                     |
    | :----------------------- | :----------------------------------- |
    | Focus or open Chat panel | <Keyboard shortcut="Cmd Option I" /> |

    ## Completions

    | Action                       | Default shortcut                     |
    | :--------------------------- | :----------------------------------- |
    | Accept entire suggestion     | <Keyboard shortcut="Tab" />          |
    | Accept word-by-word          | <Keyboard shortcut="Option Right" /> |
    | Reject suggestion            | <Keyboard shortcut="Esc" />          |
    | Toggle automatic completions | <Keyboard shortcut="Cmd Option 9" /> |
  </Tab>

  <Tab title="Windows/Linux">
    To update keyboard shortcuts, use one of the following:

    | Method   | Action                                                               |
    | :------- | :------------------------------------------------------------------- |
    | Keyboard | <Keyboard shortcut="Ctrl ," /> then select <Command text="Keymap" /> |
    | Menu bar | <Command text="File > Settings > Keymap" />                          |

    ## General

    | Action             | Default shortcut                   |
    | :----------------- | :--------------------------------- |
    | Open Augment panel | <Keyboard shortcut="Ctrl Alt I" /> |

    ## Chat

    | Action                   | Default shortcut                   |
    | :----------------------- | :--------------------------------- |
    | Focus or open Chat panel | <Keyboard shortcut="Ctrl Alt I" /> |

    ## Completions

    | Action                       | Default shortcut                   |
    | :--------------------------- | :--------------------------------- |
    | Accept entire suggestion     | <Keyboard shortcut="Tab" />        |
    | Accept word-by-word          | <Keyboard shortcut="Ctrl Right" /> |
    | Reject suggestion            | <Keyboard shortcut="Esc" />        |
    | Toggle automatic completions | <Keyboard shortcut="Ctrl Alt 9" /> |
  </Tab>
</Tabs>
