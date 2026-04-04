# Source: https://docs.augmentcode.com/troubleshooting/jetbrains-rendering-issues.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Jetbrains UI issues

> Fix issues where the Augment panel is white, blank or not showing anything in JetBrains IDEs.

export const Command = ({text}) => <span className="font-bold">{text}</span>;

## About UI issues in JetBrains IDEs

Some users on newer versions of JetBrains IDEs (2025.1 and above) have reported that the Augment panel is white, blank or not
displaying anything at all. These issues stem from a change to the way JetBrains renders webviews, which is now
done in an out-of-process manner. Disabling out-of-process rendering has resolved a number of problems for users.

This is a known issue that impacts multiple plugins in the Jetbrains ecosystem. JetBrains is tracking the issue in IJPL-186252.

**Note**: If you are using a **JetBrains IDE 2025.2.3 on Windows**, we do not recommend disabling out-of-process rendering due
to a bug where the WebViews will render JS and CSS in plain text making it difficult to use Augment and any other WebViews. There
is a workaround for this issue <a href="https://youtrack.jetbrains.com/issue/JBR-9462/Markdown-rendering-broken-with-ide.browser.jcef.out-of-process.enabledfalse-after-upgrading-to-PyCharm-2025.2.3#focus=Comments-27-12792022.0-0">described here</a>.

If you experience issues after following the steps below, please [contact support](https://support.augmentcode.com/)
for further assistance.

### Disable out-of-process rendering

<Steps>
  <Step title="Open the Custom Properties editor">
    From the menu bar, go to <Command text="Help > Edit Custom Properties..." />. If the `idea.properties` file doesn't exist yet, you'll be prompted to create it.
  </Step>

  <Step title="Add the out-of-process rendering property">
    Add the following line to the properties file:

    ```
    ide.browser.jcef.out-of-process.enabled=false
    ```
  </Step>

  <Step title="Save and restart your IDE">
    Save the file and restart your JetBrains IDE for the changes to take effect.
  </Step>
</Steps>

After restarting, the Augment panel should render more consistently.
