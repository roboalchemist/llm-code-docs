# Source: https://docs.augmentcode.com/quickstart.md

# Quickstart

> Augment is the developer AI for teams that deeply understands your codebase and how you build software. Your code, your dependencies, and your best practices are all at your fingertips.

export const Next = ({children}) => <div className="border-t border-b pb-8 border-gray dark:border-white/10">
    <h3>Next steps</h3>
    {children}
  </div>;

export const Keyboard = ({shortcut}) => <span className="inline-block border border-gray-200 bg-gray-50 dark:border-white/10 dark:bg-gray-800 rounded-md text-xs text-gray font-bold px-1 py-0.5">
    {shortcut}
  </span>;

### 1. Install the Augment extension

<CardGroup cols={3}>
  <Card href="https://marketplace.visualstudio.com/items?itemName=augment.vscode-augment">
    <img className="w-12 h-12" src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/vscode-icon.svg?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=1743e6c5d410f0c71016833690fa837e" alt="Visual Studio Code" data-og-width="64" width="64" data-og-height="64" height="64" data-path="images/vscode-icon.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/vscode-icon.svg?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=6cc12e25432edf2e06f49d14373ac02d 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/vscode-icon.svg?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=ed9401ed757b8de4c9d22f5293519da2 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/vscode-icon.svg?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=ae9c1a6c3d5a2c7ac3a8530141d306d6 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/vscode-icon.svg?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=b1a41a3a74fa9479caecca707cdc5325 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/vscode-icon.svg?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=7ae0cb9f27f612e21a7d60dc0fd6e817 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/vscode-icon.svg?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=1cc411059b25f0fde0a0406eb9a0fc42 2500w" />

    <h2 className="pt-4 font-semibold text-base text-gray-800 dark:text-white">
      Visual Studio Code
    </h2>

    <p>Install Augment for Visual Studio Code</p>
  </Card>

  <Card className="bg-red" href="https://plugins.jetbrains.com/plugin/24072-augment">
    <img className="w-12 h-12" src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/jetbrains-icon.svg?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=c66ced5a9325498d8bfd13c09f308737" alt="JetBrains IDEs" data-og-width="64" width="64" data-og-height="64" height="64" data-path="images/jetbrains-icon.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/jetbrains-icon.svg?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=19dbd0eee0903c4754190f5c5e14f204 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/jetbrains-icon.svg?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=256d16be8c5cee0ad668722591312714 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/jetbrains-icon.svg?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=47717f8a5dc2f992e7cd40bceea7dc7a 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/jetbrains-icon.svg?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=6de74610603515a436cdd6ebbe50758c 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/jetbrains-icon.svg?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=81875705a8d31362022665f5edcd7385 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/jetbrains-icon.svg?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=5cc81b977488e24b7a9ad9c2f305d084 2500w" />

    <h2 className="pt-4 font-semibold text-base text-gray-800 dark:text-white">
      JetBrains IDEs
    </h2>

    <p>Install Augment for JetBrains IDEs, including WebStorm, PyCharm, and IntelliJ</p>
  </Card>

  <Card className="bg-red" href="/cli/setup-auggie/install-auggie-cli">
    <img className="w-12 h-12" src="https://mintcdn.com/augment-mtje7p526w/nrmjd7ub006x_4Ro/images/cli.svg?fit=max&auto=format&n=nrmjd7ub006x_4Ro&q=85&s=296dbf9e9899ad6582c82bc3c7a44057" alt="Auggie CLI" data-og-width="230" width="230" data-og-height="230" height="230" data-path="images/cli.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/nrmjd7ub006x_4Ro/images/cli.svg?w=280&fit=max&auto=format&n=nrmjd7ub006x_4Ro&q=85&s=3821a862d7ae772e4b8f5c94763b938e 280w, https://mintcdn.com/augment-mtje7p526w/nrmjd7ub006x_4Ro/images/cli.svg?w=560&fit=max&auto=format&n=nrmjd7ub006x_4Ro&q=85&s=f466ec96e10fad60ee1efda5cbd9ca1d 560w, https://mintcdn.com/augment-mtje7p526w/nrmjd7ub006x_4Ro/images/cli.svg?w=840&fit=max&auto=format&n=nrmjd7ub006x_4Ro&q=85&s=e001eadbaa9a022e8eafac2c83f80157 840w, https://mintcdn.com/augment-mtje7p526w/nrmjd7ub006x_4Ro/images/cli.svg?w=1100&fit=max&auto=format&n=nrmjd7ub006x_4Ro&q=85&s=d2601529bf4c2f49fd28ef7b52d16d51 1100w, https://mintcdn.com/augment-mtje7p526w/nrmjd7ub006x_4Ro/images/cli.svg?w=1650&fit=max&auto=format&n=nrmjd7ub006x_4Ro&q=85&s=06faa3a54ba7278fedd6a85b208b1434 1650w, https://mintcdn.com/augment-mtje7p526w/nrmjd7ub006x_4Ro/images/cli.svg?w=2500&fit=max&auto=format&n=nrmjd7ub006x_4Ro&q=85&s=224824a6b754861089245e04a1a80cf0 2500w" />

    <h2 className="pt-4 font-semibold text-base text-gray-800 dark:text-white">
      Auggie CLI
    </h2>

    <p>
      All the power of Augment's agent, context engine, and tools in your terminal.
    </p>
  </Card>
</CardGroup>

### 2. Sign-in and sync your repository

For VS Code and JetBrains IDEs, follow the prompts in the Augment panel to [sign in](/setup-augment/sign-in) and [index your workspace](/setup-augment/workspace-indexing). If you don't see the Augment panel, press <Keyboard shortcut="Cmd/Ctrl L" /> or click the Augment icon in the side panel of your IDE.

For Auggie CLI, use the command `auggie login` to sign in.

### 3. Start coding with Augment

<Steps>
  <Step title="Using Agent">
    Augment agent enables you to complete tasks using natural language. Ask Agent to explain your codebase, debugging an
    issue, or writing entire functions, tests, or features. See [Using
    Agent](/using-augment/agent) for more details.
  </Step>

  <Step title="Using Next Edit">
    Augment Next Edit keeps you moving through your tasks by guiding you step-by-step through complex or repetitive changes. Jump to the next suggestion–in the same file or across your codebase–by pressing <Keyboard shortcut="Cmd/Ctrl ;" />. See
    [Using Next Edit](/using-augment/next-edit) for more details.
  </Step>

  <Step title="Using instructions">
    Start using an Instruction by hitting <Keyboard shortcut="Cmd/Ctrl I" /> and quickly write tests, refactor code, or craft any prompt in natural language to transform your code. See [Using
    Instructions](/using-augment/instructions) for more details.
  </Step>

  <Step title="Using completions">
    Augment provides inline code suggestions as you type. To accept the full
    suggestions, press <Keyboard shortcut="Tab" />, or accept the suggestion one
    word at a time with <Keyboard shortcut="Cmd/Ctrl →" />. See [Using
    Completions](/using-augment/completions) for more details.
  </Step>
</Steps>

<Next>
  * [Disable other code assistants](/troubleshooting/disable-copilot)
  * [Use keyboard shortcuts](/setup-augment/vscode-keyboard-shortcuts)
  * [Configure indexing](/setup-augment/workspace-indexing)
</Next>
