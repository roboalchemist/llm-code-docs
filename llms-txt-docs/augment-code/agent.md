# Source: https://docs.augmentcode.com/using-augment/agent.md

# Source: https://docs.augmentcode.com/jetbrains/using-augment/agent.md

# Source: https://docs.augmentcode.com/cli/acp/agent.md

# Source: https://docs.augmentcode.com/using-augment/agent.md

# Using Agent

> Use Agent to complete simple and complex tasks across your workflow–implementing a feature, upgrade a dependency, or writing a pull request.

export const type_0 = "changes"

export const AtIcon = () => <div className="inline-block w-4 h-4 mr-2">
    <svg xmlns="http://www.w3.org/2000/svg" height="20px" viewBox="0 -960 960 960" width="20px" fill="#5f6368">
      <path d="M480.39-96q-79.52 0-149.45-30Q261-156 208.5-208.5T126-330.96q-30-69.96-30-149.5t30-149.04q30-69.5 82.5-122T330.96-834q69.96-30 149.5-30t149.04 30q69.5 30 122 82.5t82.5 122Q864-560 864-480v60q0 54.85-38.5 93.42Q787-288 732-288q-34 0-62.5-17t-48.66-45Q593-321 556.5-304.5T480-288q-79.68 0-135.84-56.23-56.16-56.22-56.16-136Q288-560 344.23-616q56.22-56 136-56Q560-672 616-615.84q56 56.16 56 135.84v60q0 25.16 17.5 42.58Q707-360 732-360t42.5-17.42Q792-394.84 792-420v-60q0-130-91-221t-221-91q-130 0-221 91t-91 221q0 130 91 221t221 91h192v72H480.39ZM480-360q50 0 85-35t35-85q0-50-35-85t-85-35q-50 0-85 35t-35 85q0 50 35 85t85 35Z" />
    </svg>
  </div>;

## About Agent

Augment Agent is a powerful tool that can help you complete software development tasks end-to-end. From quick edits to complete feature implementation, Agent breaks down your requests into a functional plan and implements each step all while keeping you informed about what actions and changes are happening. Powered by Augment's Context Engine and powerful LLM architecture, Agent can write, document, and test like an experienced member of your team.

## Accessing Agent

To access Agent, simply open the Augment panel and select one of the Agent modes from the drop down in the input box.

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-selector.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=51d70e49f675669435e22fa95a1451bc" alt="Augment Agent" className="rounded-xl" data-og-width="1235" width="1235" data-og-height="434" height="434" data-path="images/agent-selector.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-selector.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=bf58d45da80eb95ddc3aa478add24e5c 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-selector.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=a44992db36a19f1f6a853691c1fd5967 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-selector.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=509265e75111915c1c542fa32a22471b 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-selector.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=925e22b37cb18461397e64cdcb040cc2 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-selector.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=94acc730b73f331885b659dbe623d6f7 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-selector.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=a8bcace31c370f0fcef0946d06b96efd 2500w" />

### Choosing a model

Use the model dropdown in the Augment panel to switch between models. Your selection applies only to Agent for the current workspace and can be changed at any time. See [Available Models](/models/available-models) for details.

## Using Agent

To use Agent, simply type your request into the input box using natural language and click the submit button. You will see the default context including current workspace, current file, and Agent memories. You can add additional context by clicking <AtIcon />and selecting files or folder, or add an image as context by clicking the paperclip. Agent can create, edit, or delete code across your workspace and can use tools like the terminal and external integrations through MCP to complete your request.

### Enhancing your prompt

You can improve the quality of your {type_0} by starting with a well crafted prompt. You can start with a quick or incomplete prompt and use the prompt enhancer to add relevant references, structure, and conventions from your codebase to improve the prompt before it is sent.

1. Write your prompt in the prompt input box
2. Click the Enhance Prompt ✨ button
3. Review and edit the enhanced prompt
4. Submit your prompt

### Reviewing changes

You can review every change Agent makes by clicking on the action to expand the view. Review diffs for file changes, see complete terminal commands and output, and the results of external integration calls.

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-edit.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=bab5fc7aed7f83ae499c9b5d72dfd03a" alt="Augment Agent" className="rounded-xl" data-og-width="1235" width="1235" data-og-height="543" height="543" data-path="images/agent-edit.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-edit.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=d0ba25bfbf7579dc11e03c5c610f5f9b 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-edit.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=24afe8b62ccaf04b7b8a38541c94eb7b 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-edit.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=cc170722a8152fada50217b03c08c013 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-edit.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=71ebbaa901d3740c0be592f243a47931 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-edit.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=a7befc70fed705adaa44a9af3b178134 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-edit.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=b847e3015c2963f15a77f3e2b648086b 2500w" />

### Checkpoints

Checkpoints are automatically saved snapshots of your workspace as Agent implements the plan allowing you to easily revert back to a previous step. This enables Agent to continue working while you review code changes and commands results. To revert to a previous checkpoint, click the reverse arrow icon to restore your code.

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-checkpoint.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=b74e713d55dd365ea383f4b16dc88205" alt="Augment Agent" className="rounded-xl" data-og-width="1235" width="1235" data-og-height="286" height="286" data-path="images/agent-checkpoint.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-checkpoint.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=0def9b44ce305366ba2f7abb482016a0 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-checkpoint.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=15298f09b3179ef13437e8db0ff91174 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-checkpoint.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=2cbde4f2c5522158a42c118c7dac95e5 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-checkpoint.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=1fbac8a7522674beab6176e0f04ac9c4 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-checkpoint.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=25b1363f04cd1d2e3f006db4fdd2f7a5 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-checkpoint.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=0d6b3f3786360d920c167c9c8147e34d 2500w" />

### Agent memories

Memories help the Agent remember important details about your workspace and your preferences for working in it. Memories are stored locally and are applied to all Agent requests. Memories can be added automatically by Agent, by clicking the remember button under a message, asking Agent to remember something, or by editing the Memories files directly.

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-memories.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=6c97e0962bf72ab46c4a121a6d60496c" alt="Stopping the agent" className="rounded-xl" data-og-width="1235" width="1235" data-og-height="377" height="377" data-path="images/agent-memories.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-memories.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=f6c7fe852e448fe202b7e537f7687048 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-memories.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=e77d425d2cd9218c11b6e7f8be78e074 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-memories.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=4709bd2e26af695ff79e5751acc37e61 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-memories.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=e9ccb06085be6101caa2690c3180ea01 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-memories.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=ad9abafab8116ecee267db387a9c3c0a 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-memories.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=7306c0ea821e5129728993a0eb20b76a 2500w" />

### Agent vs Agent Auto

By default, Agent will pause work when it needs to execute a terminal command or access external integrations. After reviewing the suggested action, click the blue play button to have Agent execute the command and continue working. You tell Agent to skip a specific action by clicking on the three dots and then Skip.

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-approval.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=5c528efde3b96da6711dcecdda312294" alt="Augment Agent" className="rounded-xl" data-og-width="1212" width="1212" data-og-height="373" height="373" data-path="images/agent-approval.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-approval.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=6c5d2c65451676c4ab78e6835ec64451 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-approval.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=74f3b29a19c5d3dedb4d9cf7cd4c15e8 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-approval.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=7099350faa1efcc52f0d17534e747438 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-approval.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=ec6fe85dcb06538d1b4b2817e95c977c 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-approval.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=e2d66bbcf048da6d3783c5b247164002 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-approval.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=68093b6342af74a4aa90d521b1cd2a3a 2500w" />

In Agent Auto, Agent will act more independently. It will edit files, execute terminal commands, and access tools like MCP servers automatically.

### Stop or guide the Agent

You can interrupt the Agent at any time by clicking Stop. This will pause the action to allow you to correct something you see the agent doing incorrectly. While Agent is working, you can also prompt the Agent to try a different approach which will automatically stop the agent and prompt it to correct its course.

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-stop.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=3c195714aa08f74acb9d63a354acdc99" alt="Stopping the agent" className="rounded-xl" data-og-width="1235" width="1235" data-og-height="551" height="551" data-path="images/agent-stop.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-stop.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=ee1b6bd049826fbd882ce234e91b8d76 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-stop.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=0bb16c7d3efaf8e03e971c6ee7b8a470 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-stop.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=cd99b327ca87dd7e5df6671dab20594e 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-stop.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=4ab045596b20e4d325ba655179e98338 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-stop.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=ea995fe1122a55d05ea67bd99b4b51d5 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/agent-stop.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=280d36fadf5a41fa8d777be4ac1e4a96 2500w" />

### Quick Ask Mode

Quick Ask Mode is a toggle button in the agent chat interface that restricts the AI to read-only tools only. When activated, it adds a visual badge to the message and focuses the AI on information gathering without making any changes to your codebase.

<img src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/ask-mode.gif?s=c2c554fd010bb15d8267de15ad4f9dc5" alt="Quick Ask Mode toggle and usage" className="rounded-xl" data-og-width="800" width="800" data-og-height="450" height="450" data-path="images/ask-mode.gif" data-optimize="true" data-opv="3" />

### Comparison to Chat

Agent takes Chat to the next level by allowing Augment to do things for you-that is create and make modifications directly to your codebase. Chat can explain code, create plans, and suggest changes which you can smartly apply one-by-one, but Agent takes it a step further by automatically implementing the entire plan and all code changes for you.

| What are you trying to do?                       | Chat | Agent |
| :----------------------------------------------- | :--: | :---: |
| Ask questions about your code                    |  ☑️  |   ✅   |
| Get advice on how to refactor code               |  ☑️  |   ✅   |
| Add new features to selected lines of code       |  ☑️  |   ✅   |
| Add new feature spanning multiple files          |      |   ✅   |
| Document new features                            |      |   ✅   |
| Queue up tests for you in the terminal           |      |   ✅   |
| Open Linear tickets or start a pull request      |      |   ✅   |
| Start a new branch in GitHub from recent commits |      |   ✅   |
| Automatically perform tasks on your behalf       |      |   ✅   |

### Use cases

Use Agent to handle various aspects of your software development workflow, from simple configuration changes to complex feature implementations. Agent supports your daily engineering tasks like:

* **Make quick edits** - Create a pull request to adjust configuration values like feature flags from FALSE to TRUE
* **Perform refactoring** - Move functions between files while maintaining coding conventions and ensuring bug-free operation
* **Start a first draft for new features** - Start a pull request (PR) with implementing entirely new functionality straight from a GitHub Issue or Linear Ticket
* **Branch from GitHub** - Open a PR from GitHub based on recent commits that creates a new branch
* **Query Supabase tables directly** - Ask Agent to view the contents of a table
* **Start tickets in Linear or Jira** - Open tickets and ask Agent to suggest a plan to address the ticket
* **Add Pull Request descriptions** - Merge your PR into a branch then tell the agent to explain what the changes are and why they were made
* **Create test coverage** - Generate unit tests for your newly developed features
* **Generate documentation** - Produce comprehensive documentation for your libraries and features
* **Start a README** - Write a README for a new feature or updated function that you just wrote
* **Track development progress** - Review and summarize your recent Git commits for better visibility with the GitHub integration

## Next steps

* [Configure Agent Integrations](/setup-augment/agent-integrations)
* [Configure other tools with MCP](/setup-augment/mcp)
