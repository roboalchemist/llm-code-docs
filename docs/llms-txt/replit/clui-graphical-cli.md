# Source: https://docs.replit.com/additional-resources/clui-graphical-cli.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.replit.com/llms.txt
> Use this file to discover all available pages before exploring further.

# The Graphical Command Line Interface

> Learn how to use CLUI, Replit's interactive command bar that lets you perform various actions across your Account, Workspace, and through Shortcuts.

CLUI (Command Line User Interface) is Replit's interactive command bar that lets you perform various actions quickly without navigating through menus. It combines the efficiency of a command line with a graphical interface.

## Features

CLUI provides powerful command-driven interactions across three different contexts in Replit:

* **Account management**: Manage your account settings, view warnings, and restore deleted Replit Apps
* **Quick navigation**: Move between your Replit Apps and access common features via shortcuts
* **Workspace operations**: Find files, search code, and access tools within your development environment

## Usage

### Account CLUI

The Account CLUI helps you manage your account, teams, and deleted Replit Apps.

<Frame>
  <img src="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/clui-account.png?fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=3181c380c560e9400da3efe0ed05cc8f" alt="Account CLUI" data-og-width="649" width="649" data-og-height="221" height="221" data-path="images/getting-started/clui-account.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/clui-account.png?w=280&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=177284171ed5ad37da7b8e027f03790a 280w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/clui-account.png?w=560&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=6881c8d53c740cce51e97a1e4177019a 560w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/clui-account.png?w=840&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=c5535f7becad1af4437da7cd18f1579d 840w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/clui-account.png?w=1100&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=917c8ae3417e7b0f3158bd1e82dec395 1100w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/clui-account.png?w=1650&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=271811ed5d92f74e0b069225028128d3 1650w, https://mintcdn.com/replit/h9U_mFqw8XzNXJwv/images/getting-started/clui-account.png?w=2500&fit=max&auto=format&n=h9U_mFqw8XzNXJwv&q=85&s=0b4372d6393d2bd7a5a8d9bc83ab17ca 2500w" />
</Frame>

**How to access**: Navigate to the [CLUI page](https://replit.com/~/cli), type in the input box to search for a command, and press Enter to execute it.

<Accordion title="Account commands">
  Type `account` to manage your account settings:

  * **view-warns**: View warnings you have been issued
  * **change-username**: Change your username (can only be done once)
</Accordion>

<Accordion title="Trash commands">
  Type `trash` to manage deleted Replit Apps:

  * **restore \<title>**: Restore a deleted Replit App by its title (restores the most recently deleted if multiple exist with the same name)
  * **view**: View your most recently deleted Replit Apps
</Accordion>

<Accordion title="Team commands">
  Type `team` to manage your teams:

  * **view**: View the members of a team you're in by its username
  * **fork-repl-to-project**: Fork an existing Replit App to create a Team Project
</Accordion>

<Accordion title="Clear command">
  Type `clear` to clear the screen of all past commands you've executed
</Accordion>

### Shortcuts CLUI

The Shortcuts CLUI provides quick access to common Replit features from any page.

<Frame>
  <img src="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/getting-started/shortcuts-clui.png?fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=99740913ac05919aa87656d986943a33" alt="Shortcuts CLUI" data-og-width="689" width="689" data-og-height="291" height="291" data-path="images/getting-started/shortcuts-clui.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/getting-started/shortcuts-clui.png?w=280&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=b8c095210a77c4fd8851713bd6abbd58 280w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/getting-started/shortcuts-clui.png?w=560&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=2e5321feaf07f9747d8f5e9b032e107c 560w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/getting-started/shortcuts-clui.png?w=840&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=0c12f9457e1131bbe0e244ca473b9342 840w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/getting-started/shortcuts-clui.png?w=1100&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=7646d0dd33934ffd5f6e31187bac1bcd 1100w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/getting-started/shortcuts-clui.png?w=1650&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=9ea14070cb1744619bc3836195d07d64 1650w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/getting-started/shortcuts-clui.png?w=2500&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=f36dfd563530735ec8b8e3856e166948 2500w" />
</Frame>

**How to access**: Press **CMD/CTRL + K** or click on the search icon in the top navigation bar on most Replit pages.

<Accordion title="Available commands">
  * **Search**: Search Replit for Replit Apps, Templates, Code, People, and more
  * **New**: Create a new Replit App
  * **My Replit Apps**: Browse and navigate to your Replit Apps
  * **My Code**: Search through the code in all of your Replit Apps
</Accordion>

### Workspace CLUI

The Workspace CLUI helps you perform operations, access tools, find files, and search your code while working in a Replit App.

<Frame>
  <img src="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/getting-started/ws-clui.png?fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=297576727cabb682ad242ef23c2d3e72" alt="Workspace CLUI" data-og-width="429" width="429" data-og-height="202" height="202" data-path="images/getting-started/ws-clui.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/getting-started/ws-clui.png?w=280&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=6732325e2cca0152931cbed8f6403673 280w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/getting-started/ws-clui.png?w=560&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=45f34dc21a535ff5b1b0a2b5f1778c9b 560w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/getting-started/ws-clui.png?w=840&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=3dbe54159f25f824f4144f84a32a1743 840w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/getting-started/ws-clui.png?w=1100&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=46eda5c467b805229aaaa0690187a1d3 1100w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/getting-started/ws-clui.png?w=1650&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=559a010c9fc1f2989237ff2829d05306 1650w, https://mintcdn.com/replit/rBzGsKp9NcWJ7sib/images/getting-started/ws-clui.png?w=2500&fit=max&auto=format&n=rBzGsKp9NcWJ7sib&q=85&s=ad2ccb8d41ce4ffa3e7fe7bdbaf74b82 2500w" />
</Frame>

**How to access**: Press **CMD/CTRL + K** or click the Search icon in the upper-left corner while in the Workspace.

<Accordion title="Common operations">
  * **Find files**: Quickly locate files in your project
  * **Search code**: Find specific code snippets across your files
  * **Access tools**: Open any tool or panel available in the Workspace
  * **Run commands**: Execute workspace-specific commands
</Accordion>
