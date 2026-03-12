# Source: https://docs.qodo.ai/qodo-documentation/whats-new/changelog.md

# Changelog

This changelog provides a chronological record of changes to Qodo, including new features, improvements, and bug fixes. Each version is grouped first by release number and then by release date so developers, teams, and stakeholders can easily see what has changed. For a quick overview of key updates and highlights, see our [What’s New](https://docs.qodo.ai/qodo-documentation/whats-new) page.

### Qodo 2.1 \[17 Feb 26]

#### **Rule System** (Beta, currently supported for GitHub single and multi-tenant only.)&#x20;

* Rule System for centralized standards management and enforcement
* Automatic conversion of existing rule files into structured standards
* Rule generation from natural language
* Automatic rule discovery from codebase and PR history
* Scoped enforcement at organization and repository levels
* Rule health management including duplicate and conflict detection
* Rule adoption and violation metrics
* In context rule enforcement during pull request review

#### Azure DevOps Integration <a href="#azure-devops-integration" id="azure-devops-integration"></a>

* Native Azure DevOps integration for Enterprise customers
* AI powered pull request reviews inside Azure DevOps
* Ticket compliance checks using Azure Boards work items
* Repository and project level configuration

### Qodo 2.0 \[4 Feb 26] <a href="#qodo-2.0" id="qodo-2.0"></a>

#### **Agentic Code Review** (Beta) <a href="#qodo-2.0" id="qodo-2.0"></a>

* Next generation agentic PR review with multi agent architecture
* Full repository context and PR history analysis
* Prioritized findings with structured remediation guidance
* Higher precision and recall
* Review experience focused on critical issues over noise

### Qodo 1.7 \[21 Oct 25]

* **New:** Local Review – review your local changes before commit with categorized insights and quick fixes
* **Removed:** Standard Mode (deprecated)
* **Updated:** New Welcome Screen with quick access to top workflows

### Qodo 1.6.35 \[29 Sep 25]

* Bug fixes and performance improvements

### Qodo 1.6.34 \[25 Sep 25]

* Add new custom MCP to all workflows by default
* Bug fixes and performance improvements

### Qodo 1.6.33 \[11 Sep 25]

* Custom MCPs are now added to all modes
* Fixed quota usage display issues
* Added `agent.md` support

### Qodo 1.6.32 \[11 Sep 25]

#### Bug Fixes

* Fix Qodo Aware issue in Custom Modes
* Fix missing workflows in Windows
* Fix close modal on logout

### Qodo 1.6.31 \[9 Sep 25]

* Improved error handling in new login flow

### Qodo 1.6.30 \[9 Sep 25]

#### New Feature

* **File and Image Attachment Support** Users can now add files and images directly in chat.\
  This allows providing richer context to the agent — for example:
  * Share **design images** to guide implementation.
  * Upload **CSV or PDF files** to supply data, logs, or specs.

#### Fixes

* Fixed quota usage display issue
* Fixed send button not working with history messages.

### **Qodo 1.6.29 \[**&#x34; Sep 25]

#### Bug Fixes

* General bug fixes and performance improvements.

### **Qodo 1.6.28 \[4 Sep 25]**

#### Features

* Added interactive sign-in button for authentication prompts with chat panel
* Added retry logic with exponential backoff to authentication API calls

### **Qodo 1.6.27 \[**&#x32; Sep 25]

#### Fixes

* Updated filesystem tool parameter descriptions

#### Bug Fixes

* General bug fixes and performance improvements.

### Qodo 1.6.26 \[21 Aug 25]

#### Bug Fixes

* General bug fixes and performance improvements.

### Qodo 1.6.25 \[20 Aug 25]

#### Bug Fixes

* General bug fixes and performance improvements.

### Qodo 1.6.24 \[19 Aug 25]

#### Features and Improvements

* Git Diff in Context Menu – Tag your local changes or compare branches (against `main` or any other branch). Reviewing just got faster and more intuitive.
* Auto Approve in Chat – Automatically approving the next tools in the same chat.
* Workflow Menu Revamp – A sleeker design with better usability for navigating and managing workflows.
* Models Menu Update – Enterprise users no longer see credit usage, and titles have been cleaned up for clarity.
* Smarter AutoScroller – If you scroll up during a live stream, auto-scroll won’t drag you back down until you’re ready.
* Main Menu Upgrade – The chat’s main menu now includes MCP tools, and grouped properly for better navigation.

#### Fixes

* Regex Crash Resolved – In chat context menu.
* Best Practices Workflow – Generated files now follow lowercase naming conventions consistently.

### Qodo 1.6.23 \[17 Aug 25]

#### Features

* Improved login flow on VSCode.

#### Bug Fixes

* General bug fixes and performance improvements.

### Qodo 1.6.22 \[13 Aug 25]

#### Bug Fixes

* General bug fixes and performance improvements.

### Qodo 1.6.21 \[12 Aug 25]

#### Features

* `Auto Approve` toggle: When enabled, all tools and terminal commands in this chat session will be approved automatically
* Updated models menu – Refreshed look & feel with clearer descriptions of credit usage for each model.
* Standard Chat update – Revised welcome screen text to announce its **upcoming deprecation** (shown only to users with agentic chat).

#### Bug Fixes

* General bug fixes and performance improvements.

### Qodo 1.6.20 \[7 Aug 25]

#### Features

* Qodo Aware is now available to use in Qodo Gen!\
  Qodo Aware is your team’s AI assistant for deep code understanding, spanning repositories, services, and history. Get fast answers or thorough multi-step reasoning without context switching.\
  Press the **Qodo Aware** button above the chatbox to use Qodo Aware.
* [Built-in workflows](https://docs.qodo.ai/qodo-documentation/qodo-gen/agent/workflows) are now uneditable. If you'd like to edit a workflow, duplicate it and edit the copy.

#### Bug Fixes

* General bug fixes and performance improvements.

### Qodo 1.6.19 \[5 Aug 25]

#### Features

* Workflows in the workflows list now include descriptions.

#### Bug Fixes

* General bug fixes and performance improvements.

### Qodo 1.6.18 \[30 July 25]

* **Workflows:** Improved structure and clarity. Use slash commands like `/unit-test`, `/review`, `/fix`.
* **Modes:** Persistent AI collaborators for tasks like coding, planning, and architecture.
* **Share Agents:** Create, export, and share custom Workflows or Modes with your team.
* **New:** Fully integrated **Qodo Aware** — click the eye icon to activate Ask or Deep Research agents. Tag repos for better context.

### Qodo 1.5.12 \[21 July 25]

#### **Fixes**

* Improved quota bar behavior — now shows only after reaching 80%.

#### **Improvements & Clean-up:**

* Removed the "Generate Tests" panel and related functionality.\
  We're removing the right-hand Test panel to reduce visual clutter and simplify your workspace. Test generation and interaction will now appear directly in the chat with the `/test` command, where they’re most relevant, helping you stay focused without losing functionality.

### Qodo 1.5.11 \[11 July 25]

#### **Fixes**

* Improved error handling for quota-related issues in VSCode.

### Qodo 1.5.10 \[10 July 25]

#### **Features**

* Quota information is now displayed on button click for users.
* Enterprise users will no longer see the quota button.

### Qodo 1.5.9 \[9 July 25]

#### **Features**

* Full file content is now returned when editing files, rather than only diffs.
* Workflow now prints debug inputs for easier troubleshooting.

### Qodo 1.5.8 \[3 July 25]

#### Bug fixes

* General bug fixes and performance improvements.

### Qodo 1.5.7 \[1 July 25]

#### Bug fixes

* General bug fixes and performance improvements.

### Qodo 1.5.6 \[30 June 25]

#### **Fixes**

* Logging and analytics improvements.

### Qodo 1.5.5 \[26 June 25]

#### **Features**

* Login screen added to chat panel.
* Show changes summary when message is manually stopped.

#### **Fixes**

* Removed test-only right-click panel option.

#### Bug fixes

* General bug fixes and performance improvements.

### Qodo 1.5.4 \[23 June 25]

#### **Features**

* Git commit tracking added and integrated with analytics.

#### **Fixes**

* IDE now avoids unnecessary file loading when not focused.

#### Bug fixes

* General bug fixes and performance improvements.

### Qodo 1.5.3 \[18 June 25]

#### Bug fixes

* General bug fixes and performance improvements.

### Qodo 1.5.2 \[16 June 25]

#### Improvements

* Extension name shortened in VSCode
* Error messages improvements
* In VSCode: the "Auto commit message" button switched to the Qodo logo

### Qodo 1.5.1 \[2 June 25]

#### Bug fixes

* General bug fixes and performance improvements.

### Qodo 1.5.0 \[28 May 25]

#### Features

* **Terminal Agentic Tool (MCP) with command control**: The new Terminal Agentic Tool allows your local terminal to run directly within the IDE, letting developers execute tests and commands seamlessly, resulting in a more integrated and fluent development experience.\
  You can control which terminal commands are allowed or blocked to run via chat preferences, giving you greater security and flexibility when running commands directly from the IDE.
* **SSE MCPs**: You can now add SSE MCPs using just a URL, making the setup process more secure, faster, and easier to manage.
* **Codebase Intelligence Agentic Tool (MCP):** Qodo Gen's agent can now use your **Company Codebase (RAG)** in **Agentic Mode**. This enables real-time code retrieval, deeper context awareness, and smarter code generation, refactoring, and debugging, all based on your actual codebase.
* **Agent following `best-practices.md`**: The agent can now read [the best practices file](https://docs.qodo.ai/qodo-documentation/qodo-gen/qodo-gen-chat/standard-mode/commands/generate-best-practices#the-best_practicesmd-file) and follow your company's best practices.
* **Agentic Mode has been significantly improved** to handle more complex, multi-step tasks. It is now more dynamic and adaptable, enabling deeper interactions and more sophisticated workflows.
* **Live diff**: View real-time changes as you request adjustments from Qodo Gen.
* **Tooling throughout the process**: Tools are now accessible throughout the entire development process, not just at the beginning of a query. This allows for more flexibility and control as you iterate and refine your code.
* **New and improved design**: The platform features a refreshed and improved design.
* [**Qodo Merge**](https://www.qodo.ai/products/qodo-merge/) **Agentic Tool:** Qodo Merge, Qodo's code review tool designed to automate review workflows and elevate code quality, **is now fully integrated into Qodo Gen!**\
  With Qodo Merge MCP, Qodo becomes a complete shift-left platform, streamlining the workflow from coding and testing to merging.\
  The Qodo Merge Agentic Tool introduces built-in review assistance, including smart suggestions and auto-generated change descriptions directly from your diffs, helping ensure timely and high-quality code reviews.

### Qodo 1.0.11 \[22 May 25]

#### Bug fixes

* General bug fixes and performance improvements.

### Qodo 1.0.10 \[11 May 25]

#### Features

* **Enterprise Allow-list management MCP:** Enterprise customers can now control which Agentic Tools can be used within their organization. This is the first step toward a broader Agentic Tools Hub coming in the future!
* **All non-enterprise features of Qodo Gen are now available to all!**
* Improvements in chat interactions and user interface.

#### Fixes

* Enhanced error messaging for improved clarity.
* General bug fixes and performance improvements.
* Improved test reliability and consistency.

### Qodo 1.0.9 \[28 April 25]

#### Bug fixes

* General bug fixes and performance improvements.

### Qodo 1.0.8 \[24 April 25]

#### Features:

* **Improved Agentic Tools List UI:** It's now easier to view, add, and manage Agentic Tools. You can also add new tools directly via a script, making setup much faster for advanced users.
* **Editor Content Persistence:** Your editor content is now saved when switching between different chat modes, preventing accidental loss of your work.

#### Improvements:

* **History File Location:** The History file is now named `.qodo/history` and has been moved to the user folder for better file organization. The file is named using a hash of the workspace path to ensure uniqueness.

#### Fixes:

* **Code Completion Preferences Cleanup:** The "User Instructions" field has been removed to simplify the Code Completion settings.
* **Chat Mode Detection:** Fixed the logic for determining the correct chat mode when opening a new chat. This ensures the right mode is selected, even if the previous chat context was inconsistent.

### Qodo 1.0.6 \[9 April 25]

#### Bug fixes

* General bug fixes and performance improvements.

### Qodo 1.0.5 \[3 April 25]

#### Bug fixes

* Resolved an issue where the agent could become unresponsive.
* Fixed compatibility problems with Agent Tools on Windows systems.

### Qodo 1.0.4 \[27 March 25]

#### Improvements

* New welcome screen design
* Some bug fixes and improvements

### Qodo 1.0.3 \[19 March 25]

#### Improvements

* Behavior improvements.
* Enhanced API error handling.
* Fixed broken link in marketplace page.

### Qodo 1.0.2 \[4 March 25]

#### Improvements

* Updated Marketplace page.
* Show/hide chat history button based on context.
* Added config file step & fixes.

#### Bug fixes

* Fixed login issue: clear refresh token & handle expired token.

### Qodo 1 \[11 March 25]

We’re thrilled to introduce **Qodo Gen Version 1**, packed with game-changing features to make your Qodo experience more intuitive than ever.

#### New features

* **Agentic Mode:** Choose between Standard or Agentic mode. Agentic mode is a game-changing flow of Qodo Gen Chat that dynamically uses tools to analyze requests and provide smarter, more adaptive responses.
* **Agentic Tools (Custom MCPs):** Integrate external services like Jira with Qodo Gen using the open MCP protocol, allowing dynamic interactions with external tools.
* **All-New Test Generation Flow in-Chat:** Creating tests is now easier with full integration into Qodo Gen Chat. Just type /test, and Qodo Gen will guide you through generating a complete test suite. You can refine tests, add cases and choose behaviors to test —all without switching tools.
* **Artifacts:** Keep your chat clean—open large code snippets as separate files in your IDE for easy application and comparison.
* **Inline Context:** Quickly reference project files, functions, and classes in chat using @, improving searchability and response accuracy.
* **Chat Preferences:** Customize commands and responses, code editor settings, code completion, and indexing for a tailored Qodo Gen experience.

### Qodo 0.14.8 \[20 Feb 25]

#### New features

* Qodo rebrand: Updated logo and color scheme.

### Qodo 0.14.7 \[9 Feb 25]

#### Improvements

* Enhanced analytics for better insights.

### Qodo 0.14.1 \[29 Jan 25]

#### Bug fixes

* Fixed login issue affecting some users.

### Qodo 0.14.0 \[28 Jan 25]

#### Changes

* Rolled back to v0.12.7 due to login issues.

### Qodo 0.12.8 \[27 Jan 25]

#### New features

* Chat history now persists across IDE sessions.

### Qodo 0.12.7 \[25 Dec 24]

#### Improvements

* Introduced new event structure for analytics.

### Qodo 0.12.6 \[17 Dec 24]

#### New features

* Added `/help` command in chat: get information and answers to questions about Qodo Gen, taken directly from Qodo's documentation platform.
* Added feedback buttons in chat.

### Qodo 0.12.5 \[8 Dec 24]

#### Improvements

* Internal analytics enhancements.

### Qodo 0.12.4 \[4 Dec 24]

#### New features

* Enabled batch processing for file indexing.
* Added RAG tags for remote retrieval-augmented generation.

#### Bug fixes

* Fixed file focus issues in chat.
* Made reference paths clickable in chat.

### Qodo 0.12.3 \[19 Nov 24]

#### New features

* Clickable links added to reference links in repositories.
* Context updates when files change.
* Added `/generate-best-practices` command in chat.

#### Bug fixes

* Fixed "no content selected" error on file change.
* README updates and improvements.

### Qodo 0.12.2 \[4 Nov 24]

#### New features

* **Enhanced Model Selection**: Unleash the full potential of AI with our new model selection feature. Seamlessly switch between the world's most advanced AI models in real-time. Available Models:
  * 🧠 GPT-4.0 - The gold standard for advanced reasoning
  * 🔮 GPT-o1-preview - Enhanced reasoning and extensive knowledge base
  * ⚡ GPT-o1-mini - Lightning-fast coding specialist, optimized for efficiency
  * 🎯 Claude 3.5 Sonnet - Anthropic's latest, built for precision
  * 💫 Gemini 1.5 Pro - Google's cutting-edge multimodal AI
* **Introducing support for best practices**: Qodo Gen now reads a `best_practices.md` file from the root of the project. when interacting with the chat, Qodo Gen takes into account those best practices when suggesting code.\
  It currently supports all free chat and code chat commands.\
  It does not support diff commands, advanced panel test generation, and code completion.\
  Qodo Gen supports up to 1500 lines in the best practices file.
* Added an option to copy messages from chat.

#### Bug fixes

* General bug fixes and performance improvements.

### Qodo 0.11.2 \[28 Oct 24]

#### New features

* Change color to be more visible across themes

#### Bug fixes

* Fixed enterprise report analytics issues.

### Qodo 0.11.1 \[18 Oct 24]

#### Bug fixes

* Fixed reopening free chat after closing all editors.

### Qodo 0.11.0 \[15 Oct 24]

#### New features

* **Chat History:** Users can now switch between and revisit up to 20 recent chats.

### Qodo 0.10.4 \[11 Oct 24]

#### Bug fixes

* Fixed Linux path issues.

### Qodo 0.10.3 \[8 Oct 24]

#### Changes

* Various naming updates.

### Qodo 0.10.2 \[30 Sep 24]

#### Bug fixes

* Fixed logout bug.

### Qodo 0.10.1 \[30 Sep 24]

#### Bug fixes

* Fixed login lock issue after repeated failures.

### Qodo 0.10.0 \[30 Sep 24]

#### Changes

* **Codiumate is now Qodo Gen!** Same features, new name.
* **Extend Test Suite sunsetting:** The "Add more tests" inline option above generated tests, as well as the Extend Test Suite tab, will no longer be available. This change is necessary as part of Test Generation upgrading.

#### New features

* **Codebase Selection in Test Panel:** Enterprise RAG users can now select RAG usage.

#### Bug fixes

* Various bug fixes and improvements.

### v0.9.15 \[8 Sep 24]

#### New features

* Added chat history to Codiumate Chat.

### v0.9.14 \[29 Aug 24]

#### New features

* Added option to Add to Codiumate as context From the terminal
* Codebase Selection: For Enterprise RAG users, you can now turn RAG usage on or off

#### Changes

* Codiumate Chat: Focus behavior now more intuitive
* Improved code completion

### v0.9.13 \[13 Aug 24]

#### Changes

* UI Improvements: The code snippet button has been relocated for easier access. Button labeling has been added, and action buttons are now always visible. Adjustments were made to color schemes for better visual consistency.
* Error messages phrasing: Improved clarity in error explanations, detailing causes and necessary actions. Enhanced consistency in error message phrasing.

#### Bug fixes

* PHP support: Resolved an issue with the static analysis of PHP code.

### v0.9.12 \[5 Aug 24]

#### Changes

* UI improvements.

#### New features

* Clear previously indexed context (cache) from the chat panel menu

#### Bug fixes

* Fixed freezing issue when chatting with small indexed snippets.

### v0.9.11 \[28 July 25]

#### Bug fixes

* Increased max prefix/suffix length for code completion context.
* Improved suffix handling in code completion requests.

### v0.9.10 \[17 July 25]

#### Bug fixes

* Fixed recurring illegal line bug.

### v0.9.9 \[16 July 25]

#### Bug fixes

* Fixed test panel issues.

### v0.9.8 \[16 July 25]

#### Bug fixes

* Fixed `type_identifier` bug.

### v0.9.7 \[16 July 25}

#### Bug fixes

* Fixed focus selection bug.

### v0.9.6 \[15 July 25]

#### Bug fixes

* Fixed Java context builder.

### v0.9.5 \[15 July 25]

#### Bug fixes

* Fixed illegal line bug.

### v0.9.4 \[11 July 25]

#### Changes

* Improved context selection.
* UI enhancements.

### v0.9.3 \[11 June 25]

#### Changes

* UI improvements.

### v0.9.2 \[5 June 25]

#### Changes

* Fixed extension uninstall event.

### v0.9.1 \[2 June 25]

#### Changes

* Updated icons.

### v0.9.0 \[30 May 24]

#### New features

* **New Codiumate Chat Interface:** Streamlined UI for easier navigation.
* **Flexible Focus Selection:** Use `@` or `+` button to focus on specific code.
* **Enhanced Context Options:** Index snippets, files, folders, or entire projects.
* **Coding-Agent Activation:** Click the robot icon for coding assistance.

### v0.8.10 \[23 May 24]

#### Changed

* Code completion enhancements
* Added extension uninstall event

#### Bug fixes

* Fix: no wrap code block display in chat
* Fix: display scrollbar for code in chat panel
* Fix: error in thread after first message interrupt
* Fix: formatting issues in codebase

### v0.8.9 \[9 May 24]

#### Bug fixes

* Fixed performance issue

### v0.8.8 \[7 May 24]

#### Bug fixes

* Fixed stopping and removing thread messages
* Removed listener to fix slowness bug

### v0.8.7 \[2 May 24]

#### Changed

* Changed the location of "Add folder to context"
* Fixed parsing of paths on Windows
* Improved Local RAG filtering

### v0.8.6 \[30 April 24]

#### Changed

* Improved error handling in chat context reducer to provide more informative feedback on unknown actions.
* Updated error message to advise saving file before re-selection.
* Disabled Auto-Commands if the chat is open.

### v0.8.5 \[17 April 24]

#### Bug fixes

* Normalize RAG settings key naming and change value types.

### v0.8.4 \[17 April 24}

#### New Features

* Indexing Support for Folders and Files: You can now enhance your Codiumate experience by indexing entire folders or individual files. This update allows you to add your code directly as context for more precise and relevant Codiumate queries.

### v0.8.3 \[17 April 24]

#### New features

* **Image Integration in Chat:** You can now paste images directly into the chat in both Free Chat and the new Coding Agent! This enhancement allows you to ask contextual questions about the images you upload. For instance, upload a design to request its HTML implementation, paste a UML diagram to have the Coding Agent plan according to it, and much more.

#### Bug fixes

* **Thread Response Continuity:** We've resolved a critical issue where threads would unexpectedly stop responding. You can now enjoy uninterrupted conversations without disruptions.
* **Code Snippet Context Retention:** A bug in threads involving code snippets has been fixed. Previously, threads would lose the initial context when discussing code snippets; this issue has been addressed to ensure consistent and context-aware interactions.

### v0.8.2 \[9 April 24]

#### Bug fixes

* Forward automatically triggered commands flag to the reducer

### v0.8.1 \[4 April 24]

#### Bug fixes

* Fixed handling of revoked refresh tokens
* Fixed command parsing in the chat panel

### v0.8.0 \[4 April 24]

#### New features

* **Codiumate-Agent Alpha Release**: We're thrilled to announce the alpha release of our Codiumate-Agent, integrated within the VSCode extension. This marks the first introduction of our coding agent designed to assist developers in completing tasks efficiently within their projects.

**Codiumate-Agent Highlights:**

* **Task Specification:** Users can now write specifications for tasks directly within VSCode.
* **Context Selection:** Offers the ability to select the relevant context for the task at hand.
* **Automated Planning:** Codiumate-Agent can automatically write a plan based on the task specification.
* **Code Auto-Completion:** Enhances coding efficiency by providing auto-completion for code based on the task's plan.

### v0.7.58 \[3 April 24]

#### Added

* Enabling code completion when using task agent

### v0.7.57 \[3 April 24]

#### New features

* Introduced Codiumate Agent Task Planner - Transform your task descriptions and contexts into a structured plan and implement with auto-complete.

### v0.7.56 \[1 April 24]

#### Changed

* Fixed reading configuration file.
* Updated docs links.

### v0.7.55 \[28 March 24]

#### New features

* Added clipboard content to code completion context
* Added Snippet types to code completion snippets
* Added debug logs for code completion

### v0.7.54 \[22 March 24]

#### Changed

* Renamed "Code Completion" to "Code Auto-complete" in settings for clarity.
* Updated descriptions for code auto-completion settings to reflect service availability for subscribed members and support for custom instructions.
