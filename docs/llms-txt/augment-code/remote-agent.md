# Source: https://docs.augmentcode.com/using-augment/remote-agent.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.augmentcode.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Using Remote Agent

> Use Remote Agent to complete tasks across your workflow–implementing a feature, upgrade a dependency, or writing a pull request–all from the cloud and with the full power of Visual Studio Code when you need it.

export const Command = ({text}) => <span className="font-bold">{text}</span>;

## About Remote Agent

Augment Remote Agent is a powerful tool that can help you complete software development tasks end-to-end that runs in a secure, cloud environment. You can run multiple agents in parallel on independent tasks, and you'll monitor and manage their progress from within Visual Studio Code. Remote Agents can run in normal or auto mode, just like IDE-based agents, and will notify you when they need attention.

### How is Remote Agent different from Agent?

Remote Agent is a cloud version of the IDE-bound Agent. Each Remote Agent runs on its own secure environment, with its own workspace-all of which is managed for you. Each Remote Agent works independently and on its own branch, so you can have multiple agents working on the same repository at the same time.

## Accessing Remote Agent

To start a new Remote Agent, simply open the Augment panel and select Remote Agent from the drop down in the input box.

<img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-selector.png?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=b915365cbd1ba0b0b272899cb0aa32f7" alt="Augment Remote Agent" className="rounded-xl" data-og-width="1400" width="1400" data-og-height="738" height="738" data-path="images/remote-agent-selector.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-selector.png?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=23b52dee17b6abdb8006622c37e2f080 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-selector.png?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=dc85ccfab2d3058d17bfba609d343328 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-selector.png?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=ad0eea50ca4866a38f8a4d1d33b57db5 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-selector.png?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=1494fd89713449c5444bce132d68b447 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-selector.png?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=da8ddb5bc00d9760c37f2cf871f2a3cb 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-selector.png?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=a433a1a6db69a74b535b1f93c5f6ac4f 2500w" />

### Agent dashboard

You can view all of your remote agents in the Remote Agent dashboard by clicking the <Command text="Expand dashboard" /> icon in the top of the Augment panel. From the dashboard you are able to see the status of all of your agents, connect to them through SSH, or delete them when they are no longer needed.

<img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-dashboard.png?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=a973fa14491d8c99a348880e3ee73043" alt="Augment Agent" className="rounded-xl" data-og-width="1134" width="1134" data-og-height="640" height="640" data-path="images/remote-agent-dashboard.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-dashboard.png?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=445b4523e55e972d73394aa7950eea4e 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-dashboard.png?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=87bc074b950ea95ac85a53430c974d77 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-dashboard.png?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=b871b9516084db79bf35a1bd0f00f537 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-dashboard.png?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=ff93117d5b3cf69073587289588d0bf6 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-dashboard.png?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=0995d1b19016a912cae022d48c3c4d6b 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-dashboard.png?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=cf0fc2b471ef2c12fa027ba68f49366d 2500w" />

## Using Remote Agent

Remote Agents function nearly identically to IDE-bound agents as you work through your tasks and projects. Because they run asynchronously in the cloud, you can access and manage them while working on other projects in your editor. Access your Remote Agents from the threads menu at the top of the Augment panel or through the Remote Agent dashboard.

You can create and manage a Remote Agent for any repository you have access to through GitHub regardless of which project you are currently working on in your editor.

### Create a remote agent

<Note>
  Before you can use Remote Agent, you will need to connect your GitHub account to enable the agent to clone your repository, create branches, and open pull requests. See [Agent Integrations](/setup-augment/agent-integrations) for setup instructions.
</Note>

1. **Select the repository** you want the agent to work on
2. **Select the branch** or let the agent create a new branch for you
3. **Select an environment** or [create a new one](/using-augment/remote-agent-environment) for the agent to run in
4. Enter your prompt into the input box using natural language and click **Create agent**

<img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-new.png?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=1677b4b0e978f84ca87753d69617e5d9" alt="Create a Remote Agent" className="rounded-xl" data-og-width="962" width="962" data-og-height="950" height="950" data-path="images/remote-agent-new.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-new.png?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=9a324c04f5bf4d155197bc0efa9d2236 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-new.png?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=3f8caa0995808766fb0ad94af3db2d31 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-new.png?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=40caf3a505518828f41e233c2fec39e2 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-new.png?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=666583055ada1ba387c7ac9eabf9bded 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-new.png?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=b831ffe39c9ce1945d1b1daaff60be79 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-new.png?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=5fed4b0725c25eb6c4aa937439399182 2500w" />

#### Agent environment

Each Remote Agent runs in an secure, independent environment in the cloud. This enables each agent to have its own workspace, copy of the repository, and virtualized operating system to run other tools and commands. You can use the [base environment](/using-augment/remote-agent-environment#base-environment), or setup a custom environment using a bash script to configure the tools the agent will need to complete the task.

See [Remote Agent Environment](/using-augment/remote-agent-environment) for more details on customizing the agent environment.

### Agent notifications

By default, you will receive a notification in VS Code when the agent has completed a task or needs your attention. You can disable notifications for a remote agent by clicking the bell icon in the theads list of the Augment panel.

### Iterating with an agent

Once an agent has completed the task, you can continue to iterate with the agent by sending additional messages. The agent will continue to work on the task, using its past conversations as context. If you need to switch to editing files directly, you can connect to the agent environment over SSH. See [Connecting to a Remote Agent](#connecting-to-a-remote-agent-environment) for more details.

### Reviewing changes

You can review every change Agent makes by clicking on the action to expand the view. Review diffs for file changes, see complete terminal commands and output, and the results of external integration calls.

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-edit.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=bab5fc7aed7f83ae499c9b5d72dfd03a" alt="Augment Agent" className="rounded-xl" data-og-width="1235" width="1235" data-og-height="543" height="543" data-path="images/agent-edit.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-edit.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=d0ba25bfbf7579dc11e03c5c610f5f9b 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-edit.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=24afe8b62ccaf04b7b8a38541c94eb7b 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-edit.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=cc170722a8152fada50217b03c08c013 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-edit.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=71ebbaa901d3740c0be592f243a47931 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-edit.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=a7befc70fed705adaa44a9af3b178134 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-edit.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=b847e3015c2963f15a77f3e2b648086b 2500w" />

### Stop or guide the Agent

You can interrupt the Agent at any time by clicking Stop. This will pause the action to allow you to correct something you see the agent doing incorrectly. While Agent is working, you can also prompt the Agent to try a different approach which will automatically stop the agent and prompt it to correct its course.

<img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-stop.png?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=1d3cbc704431241980fe8deca0118841" alt="Stopping the agent" className="rounded-xl" data-og-width="1290" width="1290" data-og-height="574" height="574" data-path="images/remote-agent-stop.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-stop.png?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=f148b2d42f38a9127c4fd78f4abae33c 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-stop.png?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=b9298bd27a06e0c3f34bf0e1c9f6e8c8 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-stop.png?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=45885224a221e2463f9aeb249e7aab90 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-stop.png?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=209dfa6202425a57063678e2815b7e40 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-stop.png?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=3415dfda919fa793cc8291a8e35f6fde 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-stop.png?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=3ea17b3dcb19e4b44da54c62582a50cb 2500w" />

### Connecting to a Remote Agent environment

<Note>
  You will need to have the [Remote-SSH extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh) installed in Visual Studio Code to connect to a remote agent. If you do not have it installed, you will be prompted to install it automatically.
</Note>

From time to time you may need to connect to a remote agent to view or edit files directly, in that case you can connect to the agent environment over SSH. From the Remote Agent dashboard, click the <Command text="SSH to agent" /> button in the agent card you with to connect to.

This will open a Visual Studio Code window connected to the agent's environment. If this is your first time opening the connection, you will be prompted by VS Code to trust the files in the remote folder. Click <Command text="Yes, I trust the authors" /> to continue.

<img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-trust.png?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=182e98219b6387fed988fad50c4759cb" alt="Augment Agent" className="rounded-xl" data-og-width="1362" width="1362" data-og-height="816" height="816" data-path="images/remote-agent-trust.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-trust.png?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=8380e170bf1d3d87b4dc254f3c4bb709 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-trust.png?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=e262b7c1c6516a8e7c10d698e1b49c71 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-trust.png?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=77342a498afbe40fa86f5bc81c37d786 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-trust.png?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=055371af3b44656a2338e8f703a9d225 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-trust.png?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=86544b81a1cc9794e8e191bb21fd0fbb 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-trust.png?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=4e2da851750f33d8d1762bf13ebc5d67 2500w" />

You can use the new VS Code window to view and edit files, run commands in the terminal, and generally interact with the agent just like you would a local IDE-bound agent.

### Opening a Pull Request

When the agent has completed the work, you can open a pull request to have your changes opened for review and merging into the main branch. Select the agent from the threads list and click <Command text="Create a PR" />. The agent will create a branch, commit the changes, and open a pull request for you. This will count against your credits quota.

<img src="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-pr.png?fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=92e70ec38eb113bb6850dd2ec582b00b" alt="Augment Agent Pull Request" className="rounded-xl" data-og-width="1290" width="1290" data-og-height="962" height="962" data-path="images/remote-agent-pr.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-pr.png?w=280&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=ec3b729b160ae86958b1ff565970e56c 280w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-pr.png?w=560&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=238d74d2e0ee38d2f312b92a893a70cb 560w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-pr.png?w=840&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=307a9f2bd706cd48cc9c9ca5f3d59c4c 840w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-pr.png?w=1100&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=589cf5049fe23ea64a955d58821d263d 1100w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-pr.png?w=1650&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=146faadaedd646fe0f34f9194258532f 1650w, https://mintcdn.com/augment-mtje7p526w/IEgTogsPIebDB-Bu/images/remote-agent-pr.png?w=2500&fit=max&auto=format&n=IEgTogsPIebDB-Bu&q=85&s=8ecd151ccfbe83eaa6c6e9737f921e07 2500w" />

### Resuming a Remote Agent

Remote Agents automatically pause after completing a request or remaining idle for a period of time. To resume a paused Remote Agent, either click <Command text="Open a remote workspace" /> or send a new message to the agent. Both actions will count against your credits quota.

## Comparison chart

Agent takes Chat to the next level by allowing Augment to do things for you-that is create and make modifications directly to your codebase. Chat can explain code, create plans, and suggest changes which you can smartly apply one-by-one, but Agent takes it a step further by automatically implementing the entire plan and all code changes for you.

| What are you trying to do?                       | Chat | Agent | Remote Agent |
| :----------------------------------------------- | :--: | :---: | :----------: |
| Ask questions about your code                    |  ☑️  |   ✅   |       ✅      |
| Get advice on how to refactor code               |  ☑️  |   ✅   |       ✅      |
| Add new features to selected lines of code       |  ☑️  |   ✅   |       ✅      |
| Add new feature spanning multiple files          |      |   ✅   |       ✅      |
| Document new features                            |      |   ✅   |       ✅      |
| Open Linear tickets or start a pull request      |      |   ✅   |       ✅      |
| Start a new branch in GitHub from recent commits |      |   ✅   |       ✅      |
| Automatically perform tasks on your behalf       |      |   ✅   |       ✅      |
| Work on multiple tasks in the same repository    |      |       |       ✅      |
| Continue working after closing VS Code           |      |       |       ✅      |

## Use cases

Use Remote Agent to handle various aspects of your software development workflow, from simple configuration changes to feature implementations. Remote Agent is best for discreet tasks that can be completed in isolation from other work. Remote Agent supports your daily engineering tasks like:

* **Make quick edits** - Create a pull request to adjust configuration values like feature flags from FALSE to TRUE
* **Fix papercuts** - Fix small bugs or issues in the codebase that never make it to the top of your TODO list
* **Perform refactoring** - Move functions between files while maintaining coding conventions and ensuring bug-free operation
* **Explore alternatives** - Run multiple remote agents to create alternative solutions to a problem
* **Start a first draft for new features** - Start a pull request (PR) with implementing entirely new functionality straight from a GitHub Issue or Linear Ticket
* **Start tickets in Linear or Jira** - Open tickets and ask Agent to suggest a plan to address the ticket
* **Create test coverage** - Generate unit tests for your newly developed features
* **Generate documentation** - Produce comprehensive documentation for your libraries and features

## Remote Agent Clean-up

Remote Agents automatically pause after completing a request or remaining idle for a period of time. Agents that remain idle for 30 days are automatically cleaned up by the system. This cleanup process removes all files in the Remote Workspace, conversation history, and any pending diffs.

## Next steps

* [Configure Agent Integrations](/setup-augment/agent-integrations)
* [Configure other tools with MCP](/setup-augment/mcp)
