# Source: https://docs.augmentcode.com/troubleshooting/jetbrains-stealing-focus.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Jetbrains panel steals focus

> Fix issue where the Augment panel takes focus while typing in JetBrains IDEs.

export const Command = ({text}) => <span className="font-bold">{text}</span>;

## About focus issues in JetBrains IDEs

Some users on Linux systems have reported that the Augment Chat window steals focus from the editor while typing. This can interrupt your workflow and make it difficult to use the IDE effectively. This issue can be resolved by enabling off-screen rendering in your JetBrains IDE.

### Enable off-screen rendering

<Steps>
  <Step title="Open the Custom Properties editor">
    From the menu bar, go to <Command text="Help > Edit Custom Properties..." />. If the `idea.properties` file doesn't exist yet, you'll be prompted to create it.
  </Step>

  <Step title="Add the off-screen rendering property">
    Add the following line to the properties file:

    ```
    augment.off.screen.rendering=true
    ```
  </Step>

  <Step title="Save and restart your IDE">
    Save the file and restart your JetBrains IDE for the changes to take effect.
  </Step>
</Steps>

After restarting, the Augment panel should no longer steal focus from the editor while you're typing.
