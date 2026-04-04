# Source: https://docs.tabnine.com/main/administering-tabnine/release-notes.md

# Release Notes

Learn about the recent releases of Tabnine.

### v6.0.0

<mark style="color:$primary;">March 11, 2026</mark>

#### Features and Improvements

* **Agent:**
  * **Models:**
    * **Support**: Added support for the <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FBFi46Yyjj0tL8xE8ZEad%2Ficons8-chatgpt-480.png?alt=media&#x26;token=74f6a8e1-8012-4e0c-922d-94c28a32aae9" alt="" data-size="line"> [**GPT 5.4** model](https://docs.tabnine.com/main/welcome/readme/ai-models) in Tabnine.
    * **Thinking Transparency:** Extended thinking block support to <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-64121828b35fbcbf113dba617435d1cf0d229a81%2Fgemini%20rainbow.png?alt=media" alt="" data-size="line"> [**Gemini** models](https://docs.tabnine.com/main/welcome/readme/ai-models)
  * **Tabnine CLI** <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FoKiOD9PIOGHc8pu4gXdV%2FTabnine%20CLI.png?alt=media&#x26;token=d136a4e1-e5c7-4046-bbe0-605272745733" alt="" data-size="line">**:** Added several features:
    * [**Skills**](https://docs.tabnine.com/main/getting-started/tabnine-cli/features/agent-skills): Predefined, reusable actions or protocols for executing specific commands
    * [**Subagents**](https://docs.tabnine.com/main/getting-started/tabnine-cli/features/subagents): Specialized “mini‑agents” focused on narrower tasks or domains (e.g., test generation, refactoring, etc.). The Enterprise Agent routes requests to the most relevant subagent.
    * [**Web Fetch**](https://docs.tabnine.com/main/getting-started/tabnine-cli/features/web-fetch): Grabs external HTTP/HTTPS content (URLs, APIs) as context, pulling in docs, JSON, HTML, etc.
  * **Accepted Code:** Tabnine now logs all accepted code changes accepted from Agent
  * **MCP** <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2F9qVoSl3DUPxts2Lloyge%2FMCP%20logo%20dark%20gray.png?alt=media&#x26;token=c1e24142-de9d-4476-bda3-6dcba49689d5" alt="" data-size="line">**:**&#x20;
    * **Tools:** Admins can now control which MCP tools are available to individual users
* [**Context Engine**](https://docs.tabnine.com/main/getting-started/context-engine)**:**
  * [**Admin Console**](https://docs.tabnine.com/main/getting-started/context-engine/admin-console)**:**
    * [**Runs**](https://docs.tabnine.com/main/getting-started/context-engine/admin-console/runs)**:** Added a Runs view that lets admins monitor and track the progress of agentic processing jobs, including current status and history.
    * [**Data Sources**](https://docs.tabnine.com/main/getting-started/context-engine/admin-console/data-sources)**:** Consolidating enablement for Context Engine, Git repos, and Perforce depots together
    * [**Coaching Guidelines**](https://docs.tabnine.com/main/getting-started/context-engine/admin-console/coaching-guidelines-v)**:** Moved Coaching Guidelines page to the Context Engine section
    * Skill: Context Engine is now exposed as a skill to make cross-repo context on command
* **Enterprise**:
  * [**Perforce**](https://docs.tabnine.com/main/getting-started/context-engine/admin-console/data-sources#perforce): Connecting Perforce depots now available out of the box for all customers
  * **IdP Sync/SCIM Support:** Added the option to sync SCIM groups to Tabnine teams
  * **SSO:** It is now possible to set SSO with OAuth (in addition to SAML)

#### Bug Fixes

* **Agent**:
  * **Tools**: Fixed issue with the `create file` tool so that requested files are now created successfully
  * **Analytics**: Fixed bug where error displayed on Agent analytics chart after staying open for a certain period of time
* **Models**:
  * **Changing Models**: Resolved inconsistent state issue when switching models (or between Chat and Agent) mid-conversation
  * **Thinking Mode**: Cleaned up Minimax “Thinking mode” behavior so that “thinking” is no longer triggered or displayed in multiple, incorrect locations

{% hint style="info" %}
Technical info (plugin versions) for ***6.0.0*****:**

* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c99f96542814962beffb0c344156d8bb85fa208b%2FTabnine%20red.png?alt=media" alt="" data-size="line"> Engine: ***4.331.4***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-b9a5693a952ab698fae8b49fa5dde2c27cc1b83a%2FVisual%20Studio%20Code%20(VS%20Code).svg?alt=media" alt="" data-size="line"> Visual Studio Code: ***3.346.0***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-74716d5d81d7c0b8ecb601c7d0ac00a6bda75c6b%2FJetBrains.png?alt=media" alt="" data-size="line"> JetBrains IDEs: ***1.300.0***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d8b6b66314cf445674a0cbcce3e803f082b76000%2FEclipse%20IDE.png?alt=media" alt="" data-size="line"> Eclipse: ***1.174.0***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ea81a5ec9acf7fe845aa25f6754cf1a1a852b9e9%2FVisual_Studio_Icon_2019.svg.png?alt=media" alt="" data-size="line"> Visual Studio 2022 ***&*** <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FnAs1fEuLCy9uwHFbqPXC%2FVs2026_logo.png?alt=media&#x26;token=a45e1da6-d62a-4139-a3e4-d9b985c3d090" alt="" data-size="line"> ***2026***: ***1.280.0***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FoKiOD9PIOGHc8pu4gXdV%2FTabnine%20CLI.png?alt=media&#x26;token=d136a4e1-e5c7-4046-bbe0-605272745733" alt="" data-size="line"> *Tabnine-CLI: **0.12.0***
  {% endhint %}

{% hint style="info" icon="exclamation" %}
A previous version of the release notes prematurely announced the release of certain features that are planned for *upcoming* releases: an `/ide` command, Extensions, and Sandboxing.
{% endhint %}

***

### v5.28.6

<mark style="color:$primary;">March 16, 2026</mark>

#### Bug Fixes:

* Fixed a Linux DNS issue that could cause the Tabnine plugin to freeze.
* Ensured Agent `run_command` tool in VSCode waits for commands to finish and captures all output

### v5.28.5&#x20;

<mark style="color:$primary;">March 5, 2026</mark>

#### Bug Fixes

* Resolved <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-7c750318da4477aa49b555b3a3f3f7e5c6060a2d%2Fazure.png?alt=media" alt="" data-size="line"> Azure integration issue where the new <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FBFi46Yyjj0tL8xE8ZEad%2Ficons8-chatgpt-480.png?alt=media&#x26;token=74f6a8e1-8012-4e0c-922d-94c28a32aae9" alt="" data-size="line"> GPT-5.2 Codex and <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FBFi46Yyjj0tL8xE8ZEad%2Ficons8-chatgpt-480.png?alt=media&#x26;token=74f6a8e1-8012-4e0c-922d-94c28a32aae9" alt="" data-size="line"> GPT-5.3 Codex model options in the Admin Console failed

***

### v5.28.4&#x20;

<mark style="color:$primary;">February 26, 2026</mark>

{% hint style="success" %}
*v5.28.3 included minor changes that are included in this version*
{% endhint %}

#### Bug Fixes

* Fixed an issue where the users could not log in or use Tabnine extension
* Fixed an issue where some supported self-managed models were missing from default model list in Admin UI

{% hint style="info" %}
Technical info (plugin versions) for ***5.28.4*****:**

* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c99f96542814962beffb0c344156d8bb85fa208b%2FTabnine%20red.png?alt=media" alt="" data-size="line"> Engine: **4.331.0**
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-b9a5693a952ab698fae8b49fa5dde2c27cc1b83a%2FVisual%20Studio%20Code%20(VS%20Code).svg?alt=media" alt="" data-size="line"> Visual Studio Code: ***3.342.4***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-74716d5d81d7c0b8ecb601c7d0ac00a6bda75c6b%2FJetBrains.png?alt=media" alt="" data-size="line"> JetBrains IDEs: ***1.296.4***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d8b6b66314cf445674a0cbcce3e803f082b76000%2FEclipse%20IDE.png?alt=media" alt="" data-size="line"> Eclipse: ***1.168.3***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ea81a5ec9acf7fe845aa25f6754cf1a1a852b9e9%2FVisual_Studio_Icon_2019.svg.png?alt=media" alt="" data-size="line"> Visual Studio 2022 ***&*** <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FnAs1fEuLCy9uwHFbqPXC%2FVs2026_logo.png?alt=media&#x26;token=a45e1da6-d62a-4139-a3e4-d9b985c3d090" alt="" data-size="line"> ***2026***: ***1.271.3***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FoKiOD9PIOGHc8pu4gXdV%2FTabnine%20CLI.png?alt=media&#x26;token=d136a4e1-e5c7-4046-bbe0-605272745733" alt="" data-size="line"> *Tabnine-CLI:* **0.5.3**
  {% endhint %}

#### Bug Fixes

* Monitoring: Fixed Prometheus monitoring labels for new installs

### v5.28.2

<mark style="color:$primary;">February 22, 2026</mark>

#### Features and Improvements

* **Agent**
  * **Reports UI:**
    * Added an [Agent Usage AI](https://docs.tabnine.com/main/administering-tabnine/private-installation/reporting#agent-usage-page) for viewing Agent usage and activity.
  * **Tabnine CLI:**
    * Now supports [Personal Access Tokens (PATs)](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/settings/access-tokens)
* **Teams:**
  * Added [team management APIs](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/tabnine-apis/team-management-apis) to help automate team administration.
* **Models:**
  * Expanded support for additional models in self-hosted environments.

#### Bug Fixes

* **IDE:**
  * Switching teams in the IDE now correctly refreshes connected repositories.
* **Core**
  * Fixed a regression that prevented the Tabnine core (Node.js) from running on some  <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-f7c9731c7a83ba2d75b0d17864d12091461bf38e%2FWindows_logo_-_2021.svg.png?alt=media" alt="" data-size="line"> Windows setups.

{% hint style="info" %}
Technical info (plugin versions) for **5.28.1:**

* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c99f96542814962beffb0c344156d8bb85fa208b%2FTabnine%20red.png?alt=media" alt="" data-size="line"> Engine: ***4.331.0***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-b9a5693a952ab698fae8b49fa5dde2c27cc1b83a%2FVisual%20Studio%20Code%20(VS%20Code).svg?alt=media" alt="" data-size="line"> Visual Studio Code: ***3.342.3***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-74716d5d81d7c0b8ecb601c7d0ac00a6bda75c6b%2FJetBrains.png?alt=media" alt="" data-size="line"> JetBrains IDEs: ***1.296.3***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d8b6b66314cf445674a0cbcce3e803f082b76000%2FEclipse%20IDE.png?alt=media" alt="" data-size="line"> Eclipse: ***1.168.2***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ea81a5ec9acf7fe845aa25f6754cf1a1a852b9e9%2FVisual_Studio_Icon_2019.svg.png?alt=media" alt="" data-size="line"> Visual Studio 2022 ***&*** <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FnAs1fEuLCy9uwHFbqPXC%2FVs2026_logo.png?alt=media&#x26;token=a45e1da6-d62a-4139-a3e4-d9b985c3d090" alt="" data-size="line"> ***2026***: ***1.271.2***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FoKiOD9PIOGHc8pu4gXdV%2FTabnine%20CLI.png?alt=media&#x26;token=d136a4e1-e5c7-4046-bbe0-605272745733" alt="" data-size="line"> *Tabnine-CLI: **0.5.3***
  {% endhint %}

### v5.28.1

<mark style="color:$primary;">February 18, 2026</mark>

#### Features and Improvements

* **Agent:**
  * **Reporting:**
    * **Metrics**: Added new usage and performance metrics for Tabnine Agent to Enterprise reports and API.
  * **Governance:**
    * **MCP Tools:** Introduced user controls to enable/disable MCP tools

#### Bug Fixes

* **Security:**
  * KEDA SSL secret: No longer generates when Kubernetes Event-Driven Autoscaler (KEDA) is disabled.
* **Teams**
  * Switching teams in the IDE now correctly refreshes connected repositories.
* **Safari:**
  * Resolved Safari sign-in failures.
* **Models:**
  * Updated the web console model list so all supported self‑managed models appear for self‑hosted customers.
  * **Thinking Transparency:** Fixed an issue that prevented adding the “thinking” model in the web console.

{% hint style="info" %}
Technical info (plugin versions) for **5.28.1:**

* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c99f96542814962beffb0c344156d8bb85fa208b%2FTabnine%20red.png?alt=media" alt="" data-size="line"> Engine: ***4.331.0***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-b9a5693a952ab698fae8b49fa5dde2c27cc1b83a%2FVisual%20Studio%20Code%20(VS%20Code).svg?alt=media" alt="" data-size="line"> Visual Studio Code: ***3.342.1***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-74716d5d81d7c0b8ecb601c7d0ac00a6bda75c6b%2FJetBrains.png?alt=media" alt="" data-size="line"> JetBrains IDEs: ***1.296.1***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d8b6b66314cf445674a0cbcce3e803f082b76000%2FEclipse%20IDE.png?alt=media" alt="" data-size="line"> Eclipse: ***1.168.1***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ea81a5ec9acf7fe845aa25f6754cf1a1a852b9e9%2FVisual_Studio_Icon_2019.svg.png?alt=media" alt="" data-size="line"> Visual Studio 2022 ***&*** <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FnAs1fEuLCy9uwHFbqPXC%2FVs2026_logo.png?alt=media&#x26;token=a45e1da6-d62a-4139-a3e4-d9b985c3d090" alt="" data-size="line"> ***2026***: ***1.271.1***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FoKiOD9PIOGHc8pu4gXdV%2FTabnine%20CLI.png?alt=media&#x26;token=d136a4e1-e5c7-4046-bbe0-605272745733" alt="" data-size="line"> *Tabnine-CLI: **0.9.1***
  {% endhint %}

### v5.28.0

<mark style="color:$primary;">February 10, 2026</mark>

#### Features and Improvements

* **Agent:**
  * **IDE:**
    * **Visual Studio 2022/2026:** Tabnine Agent is now available for <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FnAs1fEuLCy9uwHFbqPXC%2FVs2026_logo.png?alt=media&#x26;token=a45e1da6-d62a-4139-a3e4-d9b985c3d090" alt="" data-size="line"> VS26 in addition to VS22
    * **ripgrep‑based search:** The Tabnine IDE extension now includes a `ripgrep`‑powered search tool (**Search File Content**), enabling fast, code‑aware searches that the agent can use when answering queries or generating changes.
      * This is found under *Settings > Tools and MCPs > Native Tools > Search File Content*
    * **Readfile tool:** Reading large files now uses an Offset and limit mechanism to allow partial reading of files without bloating context size
    * **Extension Update:** Forces extension update upon updating the console to prevent issue when anymore admin console is using a newer version than the CLI extension
  * **Image Context:**
    * Enabled image context to <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-64121828b35fbcbf113dba617435d1cf0d229a81%2Fgemini%20rainbow.png?alt=media" alt="" data-size="line"> Gemini models allowing the agent to reason over screenshots and diagrams
  * ​[**Predefined Slash Commands**](https://app.gitbook.com/o/YLgwWrfxsDTaMMQ0WcKt/s/Y2qxVf5VTm3fmwP4B4Gx/getting-started/tabnine-agent/how-to-use-tabnine-agent#predefined-slash-commands)**:**
    * Added new slash commands `/code-review`
* **Context Engine:**&#x20;
  * **General Availability:** Context Engine is now *generally available* across Enterprise SaaS and self‑hosted deployments, including:&#x20;
    * **Service summary** per repository
    * **OpenAPI** specification per repository
  * **Admin UI:**
    * **Settings:** Added a dedicated Settings section in the Context Engine Admin UI. Admins can now configure availability, choose models, manage scheduling, and control which tools are exposed to the agent end users—directly from the admin UI.
    * **Assets:** Introduced an Assets view in the Admin UI, where admins can review the contextual assets generated by the engine (Service Summary or OpenAPI specs).
  * **Repositories:**&#x20;
    * Organization‑level repositories: Admins can now define Git repositories and Perforce depots at the organization level.
* **Enterprise:**
  * **Personal Access Tokens (PATs):** Introduced support for Tabnine PATs to authenticate scripts, tools, API calls, and integrations against Tabnine services.
  * **Bring Your Own AI – BYOAI:** Allows enterprises to integrate their own LLM providers or internal models into Tabnine’s orchestration, while preserving Tabnine’s governance and UX.

#### Bug Fixes

* **Agent:**
  * **Models:**
    * Fixed issue where Claude Agent costs displayed as negative
  * **Tabnine CLI:**
    * Fixed issue where Tabnine-native MCPs failed in Tabnine CLI
  * **Analytics:**
    * Fixed inconsistent token consumption between analytics and email
  * **IDE:**
    * Fixed errors when using MCP servers with Gemini models
* **Chat:**
  * **Windows:**&#x20;
    * Ensured Chat Apply works even if no workspace or current file is set
  * **Models:**&#x20;
    * Fixed issue where Gemini 2.5 returned “undefined” Chat responses
  * **Context:**&#x20;
    * Ensured even an empty “current file” is considered in Chat context&#x20;
  * **Quota:**&#x20;
    * Quota enforcement will only apply to Agent interactions
* **Enterprise:**
  * **Installer:**
    * Fixed issue with Node.js installer for versions 22.7 and 20.19

{% hint style="info" %}
Technical info (plugin versions) for **5.28.0:**

* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c99f96542814962beffb0c344156d8bb85fa208b%2FTabnine%20red.png?alt=media" alt="" data-size="line"> Engine: ***4.330.0***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-b9a5693a952ab698fae8b49fa5dde2c27cc1b83a%2FVisual%20Studio%20Code%20(VS%20Code).svg?alt=media" alt="" data-size="line"> Visual Studio Code: ***3.342.0***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-74716d5d81d7c0b8ecb601c7d0ac00a6bda75c6b%2FJetBrains.png?alt=media" alt="" data-size="line"> JetBrains IDEs: ***1.296.0***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d8b6b66314cf445674a0cbcce3e803f082b76000%2FEclipse%20IDE.png?alt=media" alt="" data-size="line"> Eclipse: ***1.168.0***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ea81a5ec9acf7fe845aa25f6754cf1a1a852b9e9%2FVisual_Studio_Icon_2019.svg.png?alt=media" alt="" data-size="line"> Visual Studio 2022 ***&*** <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FnAs1fEuLCy9uwHFbqPXC%2FVs2026_logo.png?alt=media&#x26;token=a45e1da6-d62a-4139-a3e4-d9b985c3d090" alt="" data-size="line"> ***2026***: ***1.271.0***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FoKiOD9PIOGHc8pu4gXdV%2FTabnine%20CLI.png?alt=media&#x26;token=d136a4e1-e5c7-4046-bbe0-605272745733" alt="" data-size="line"> *Tabnine-CLI: **0.5.2***
  {% endhint %}

### v5.27.4

<mark style="color:$primary;">February 9, 2026</mark>

#### Features and Improvements

* **Models:**
  * Added support for <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-a0ee6c6377a3b52463a58bdea0c387d39b46f04a%2FClaude%20logo.png?alt=media" alt="" data-size="line"> Claude Opus 4.6 <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FOuilkkNxykRs9PtRkcuu%2FThinking%20Icon.png?alt=media&#x26;token=e09424e2-bb50-437a-aaff-52674ec3c3fc" alt="" data-size="line">

### v5.27.3

<mark style="color:$primary;">January 29, 2026</mark>

#### Bug Fixes

* **Agent:**
  * Fixed issue where **Agent** fails to run during long token-consuming tasks on <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FOuilkkNxykRs9PtRkcuu%2FThinking%20Icon.png?alt=media&#x26;token=e09424e2-bb50-437a-aaff-52674ec3c3fc" alt="" data-size="line"> thinking models
* **Chat:**
  * Fixed issue with image uploads for <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-64121828b35fbcbf113dba617435d1cf0d229a81%2Fgemini%20rainbow.png?alt=media" alt="" data-size="line"> **Gemini** models
* **Mac/Intel Core Support:**
  * Tabnine plugin now works on MacBooks with <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fh0rctF7FtCHeAmJrPozD%2FIntel_Core_2023_logo.png?alt=media&#x26;token=52da1b05-9056-47c9-8cbc-e2204788c586" alt="" data-size="line"> **Intel** processors in addition to Apple Silicon chips

{% hint style="info" %}
Technical info (plugin versions) for **5.27.3:**

* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c99f96542814962beffb0c344156d8bb85fa208b%2FTabnine%20red.png?alt=media" alt="" data-size="line"> Engine: ***4.326.7***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-b9a5693a952ab698fae8b49fa5dde2c27cc1b83a%2FVisual%20Studio%20Code%20(VS%20Code).svg?alt=media" alt="" data-size="line"> Visual Studio Code: ***3.334.3***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-74716d5d81d7c0b8ecb601c7d0ac00a6bda75c6b%2FJetBrains.png?alt=media" alt="" data-size="line"> JetBrains IDEs: ***1.285.4***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d8b6b66314cf445674a0cbcce3e803f082b76000%2FEclipse%20IDE.png?alt=media" alt="" data-size="line"> Eclipse: ***1.166.3***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ea81a5ec9acf7fe845aa25f6754cf1a1a852b9e9%2FVisual_Studio_Icon_2019.svg.png?alt=media" alt="" data-size="line"> Visual Studio 2022, \[& 2026 (beta β)]: ***1.268.4***
  {% endhint %}

### v5.27.2

<mark style="color:$primary;">January 25, 2026</mark>

#### Features and Improvements

* **Agent:**
  * [**Prompts**](https://docs.tabnine.com/main/getting-started/tabnine-agent/how-to-use-tabnine-agent#prompt)**:** Added an option to collect **Agent** prompts (Enterprise Setting)
* **Installer:**
  * **Node.js:** Updated the installer to work correctly with <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-2e44ed2b284f0954259e5758b220fff68a890de7%2FNode.js_logo.svg%20(1).png?alt=media" alt="" data-size="line"> Node.js versions where ESM modules aren’t auto-detected
  * **Docs:** Removed outdated requirement for active web connection during [Installation](https://docs.tabnine.com/main/getting-started/install)

#### Bug Fixes

* **Agent:**
  * [**Models**](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/settings/models-settings)**:** Fixed issue where <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-a0ee6c6377a3b52463a58bdea0c387d39b46f04a%2FClaude%20logo.png?alt=media" alt="" data-size="line"> Claude Sonnet 4.5 chat did not work when accessed via <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FcuiXDPxLjJioBkJKa4Pd%2Fazure%20foundry.png?alt=media&#x26;token=e825e7d6-dcbc-458b-9dea-448756eaf4cb" alt="" data-size="line"> Azure Foundry&#x20;
  * [**Tabnine-CLI**](https://docs.tabnine.com/main/getting-started/tabnine-cli)**:** Improved reliability of native <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2F9qVoSl3DUPxts2Lloyge%2FMCP%20logo%20dark%20gray.png?alt=media&#x26;token=c1e24142-de9d-4476-bda3-6dcba49689d5" alt="" data-size="line"> MCP tools to prevent intermittently hanging or null returns
* **Chat:**
  * [**Apply**](https://docs.tabnine.com/main/getting-started/tabnine-chat)**:** Fixed a bug where Chat couldn’t create/apply changes on Windows when no workspace or file was set
  * [**Context**](https://docs.tabnine.com/main/getting-started/getting-the-most-from-tabnine-chat/chat-context)**:** Fixed bug where file scope was not in context if the file existed but was empty

{% hint style="info" %}
Technical info (plugin versions) for **5.27.2:**

* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c99f96542814962beffb0c344156d8bb85fa208b%2FTabnine%20red.png?alt=media" alt="" data-size="line"> Engine: 4.326.5
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-b9a5693a952ab698fae8b49fa5dde2c27cc1b83a%2FVisual%20Studio%20Code%20(VS%20Code).svg?alt=media" alt="" data-size="line"> Visual Studio Code: ***3.334.2***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-74716d5d81d7c0b8ecb601c7d0ac00a6bda75c6b%2FJetBrains.png?alt=media" alt="" data-size="line"> JetBrains IDEs: ***1.285.2***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d8b6b66314cf445674a0cbcce3e803f082b76000%2FEclipse%20IDE.png?alt=media" alt="" data-size="line"> Eclipse: ***1.166.2***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ea81a5ec9acf7fe845aa25f6754cf1a1a852b9e9%2FVisual_Studio_Icon_2019.svg.png?alt=media" alt="" data-size="line"> Visual Studio 2022, \[& <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FnAs1fEuLCy9uwHFbqPXC%2FVs2026_logo.png?alt=media&#x26;token=a45e1da6-d62a-4139-a3e4-d9b985c3d090" alt="" data-size="line"> 2026 (beta β)]: ***1.268.3***
  {% endhint %}

### v5.27.1

<mark style="color:$primary;">January 19, 2026</mark>

#### Features and Improvements

* **Agent:**
  * [**Tabnine CLI**](https://docs.tabnine.com/main/getting-started/tabnine-cli)**:**
    * Forked from Gemini-CLI, it requires Tabnine Auth and supports both switchable models and interacts with Tabnine context engine
  * **Tabs:**
    * **Default:** Agent is now the first and default tab in the IDE plugin
    * **Persistence:** Users upon reentering the Tabnine app will be shown the last tab they were using (Agent, Chat, Test, or Review)
  * **Web View:** Added loading screen in IDE web view for Agent (and **Chat**)
* **Chat:** Image uploads now available for <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-64121828b35fbcbf113dba617435d1cf0d229a81%2Fgemini%20rainbow.png?alt=media" alt="" data-size="line"> Gemini models

#### Bug Fixes

* **Agent:**
  * **MCP:** Fixed MCP config issue with Gemini 3 Pro
  * **Web View:** Fixed Eclipse IDE web view loading for Agent (and **Chat**)
  * Fixed minor UI issues
* **Chat:**
  * **Remote Fetch:** Fixed navigation link in Remote Fetch flow

{% hint style="info" %}
Technical info (plugin versions) for **5.27.1:**

* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c99f96542814962beffb0c344156d8bb85fa208b%2FTabnine%20red.png?alt=media" alt="" data-size="line"> Engine: ***4.326.5***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-b9a5693a952ab698fae8b49fa5dde2c27cc1b83a%2FVisual%20Studio%20Code%20(VS%20Code).svg?alt=media" alt="" data-size="line"> Visual Studio Code: ***3.334.1***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-74716d5d81d7c0b8ecb601c7d0ac00a6bda75c6b%2FJetBrains.png?alt=media" alt="" data-size="line"> JetBrains IDEs: ***1.285.2***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d8b6b66314cf445674a0cbcce3e803f082b76000%2FEclipse%20IDE.png?alt=media" alt="" data-size="line"> Eclipse: ***1.166.1***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ea81a5ec9acf7fe845aa25f6754cf1a1a852b9e9%2FVisual_Studio_Icon_2019.svg.png?alt=media" alt="" data-size="line"> Visual Studio 2022, \[& <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FnAs1fEuLCy9uwHFbqPXC%2FVs2026_logo.png?alt=media&#x26;token=a45e1da6-d62a-4139-a3e4-d9b985c3d090" alt="" data-size="line"> 2026 (beta β)]: ***1.268.2***<br>
  {% endhint %}

### v5.27.0

<mark style="color:$primary;">January 14, 2026</mark>

#### Features and Improvements

* **Agent:**
  * **Models:**&#x20;
    * Support added for GPT 5.2 <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FBFi46Yyjj0tL8xE8ZEad%2Ficons8-chatgpt-480.png?alt=media&#x26;token=74f6a8e1-8012-4e0c-922d-94c28a32aae9" alt="" data-size="line">
  * **Coaching:**
    * Exposed coaching guidelines as an MCP server
  * **MCP:**
    * Support OAuth and token authorization methods
    * Support `env` variables without overriding existing `env`
  * [**Predefined Slash Commands**](https://docs.tabnine.com/main/getting-started/tabnine-agent/how-to-use-tabnine-agent#predefined-slash-commands)**:**
    * Created new slash commands:&#x20;
      * `/describe-pr`
      * `/test`
  * **Thinking Transparency:**
    * Added feature that highlights the steps that the model took while processing its response. Models with thinking enabled are highlighted with ![](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAACwAAAAqCAYAAADI3bkcAAAC0klEQVR4AezWTWoUURAH8CaXSFTIFTSuA27FI2SleABdegSXegDRVY4gboWsJ84VAqKeQvs3pIZH0z3vo2fAgQ78p6rr1ce/671XnZPTs4d/jwkn3ZH9LYQPvWFLh5cODzqwHIlBQ/b+OLvDF5cvu9fvvm/w/OpD9+D8yYbklH2zOONnFmFEn16+2pZ/dH7Rvbj6uCE/Zt86zlCaCeumuj/vbrtP7591X6/fdHQ2oA/tum5tDqoJ23LQTYXXN1+I7tfdj+7b9duN7mfMrutIi+fTgmLCCjkCthyiGKKhpzK1pwSRFi9Xak9jd+lFhCVWKBLZ7tCthV4iVzeft0cH8dr4IsKP+0mADKLOpa0nndu0k3zGwIevmNv+CIlHnO/Z/VShl6CIcCRa98VCJxEhxzDs3ND3d3/mxZ0egvCf++Q13cj55ta9zBiKOlzbBYWceaNv2GlrKaIZqW2XniWsYIyw2MZdCdM1cS6WCZPa6c4y6cXG1q2NIUs4LpxLMzyHYwnD5oKJWfVTYepFrfGv2cEsYQlb4QV1khzLMfUiY75hyxK2rZynilprReSMGiV5JglHcGxbes6ca89k+OUkf0hjQjffc/GxniUcji4HXVEXyTPJVgL+IMb0EBP3Yz2Y79amkCXsDEYHfP8VlWzVXyaXil4CvmLkcgTkIj3H0SjJkyUsiU+pxHTSBPAiNYX4ipFLHpArfWbLoYiwJDHgQ7K1QqfFtuQqJqzA/4BqwnGG55CPD8VB5nAQc/5iK91y0wJiNIXfmOQXaL1skbeqw0i7KG63ToMxtYu0NX4BheWovWzioIqwAIXSEcUW/yrqomcIPWYtknZIrBx8WlBNWJHhiNI9W01aBzqb3fC87j8Odkis51Y0EU6L6ZjusZGr+w8KPWx85hKVC2YTRsQW+5iQ0UV62Pgotg/MJrwPEjU5FsI13WrxXTrc0rWamKPr8D8AAAD//xJInOAAAAAGSURBVAMA1pajxFXgoOoAAAAASUVORK5CYII=)
* **Context Engine:**
  * **Service Index (closed beta β):** Added new tools for advanced searching and navigation of services in remote codebases for discovering services, locating their definitions, and understanding where they are used across remote repositories:
    * `remote_search_assets`
    * `remote_openapi_spec_query`
    * `remote_get_asset`
* **Enterprise:**
  * [**Manage Users API**](https://docs.tabnine.com/main/managing-your-team/tabnine-apis#user-management-api)**:** Allows admins outside of the Admin UI to manage Tabnine users by organization/team:
    * Invite
    * Assign to a team
    * Assign to a role
    * Activate/Deactivate
  * [**Manage Repos API**](https://docs.tabnine.com/main/managing-your-team/tabnine-apis#repository-api)**:** New way to configure and manage which repos Tabnine indexes per organization or team:
    * Add
    * Edit
    * Delete
    * List repositories
    * Indexing status

#### Bug Fixes

* **Rider IDE** <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c53c4155bf5212ca6bd98cbbcaffb7a107902736%2Frider.png?alt=media" alt="" data-size="line">**:**&#x20;
  * Fixed issue where indexing did not work with Rider if project contained /.run folder
* **Remote Repos:**
  * **Remote Fetch:** Added alternate way to supply remote file content to Tabnine even when the native remote-fetch mechanism is unavailable

{% hint style="info" %}
Technical info (plugin versions) for **5.27.0:**

* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c99f96542814962beffb0c344156d8bb85fa208b%2FTabnine%20red.png?alt=media" alt="" data-size="line"> Engine: ***4.326.4***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-b9a5693a952ab698fae8b49fa5dde2c27cc1b83a%2FVisual%20Studio%20Code%20(VS%20Code).svg?alt=media" alt="" data-size="line"> Visual Studio Code: ***3.334.0***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-74716d5d81d7c0b8ecb601c7d0ac00a6bda75c6b%2FJetBrains.png?alt=media" alt="" data-size="line"> JetBrains IDEs: ***1.285.1***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d8b6b66314cf445674a0cbcce3e803f082b76000%2FEclipse%20IDE.png?alt=media" alt="" data-size="line"> Eclipse: ***1.166.0***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ea81a5ec9acf7fe845aa25f6754cf1a1a852b9e9%2FVisual_Studio_Icon_2019.svg.png?alt=media" alt="" data-size="line"> Visual Studio 2022, \[& <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FnAs1fEuLCy9uwHFbqPXC%2FVs2026_logo.png?alt=media&#x26;token=a45e1da6-d62a-4139-a3e4-d9b985c3d090" alt="" data-size="line"> 2026 (beta β)]: ***1.268.0***
  {% endhint %}

***

### v5.26.10

<mark style="color:$primary;">January 22, 2026</mark>

#### Bug Fixes

* **IDEs:** Fixed issue in JS application build where some web-view runtimes in <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-5c5cc41a7ab010d3008c633811cc3c426a04c5b6%2FIntelliJ_IDEA_Icon.svg.png?alt=media" alt="" data-size="line"> IntelliJ 2023.3.x, <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c53c4155bf5212ca6bd98cbbcaffb7a107902736%2Frider.png?alt=media" alt="" data-size="line"> Rider, and <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d8b6b66314cf445674a0cbcce3e803f082b76000%2FEclipse%20IDE.png?alt=media" alt="" data-size="line"> Eclipse IDEs failed to load Tabnine

***

### v5.26.9

<mark style="color:$primary;">January 5, 2026</mark>

#### Bug Fixes

* &#x20;Fixed **Apply** issue in certain edge cases on Windows machines

***

### v5.26.8

<mark style="color:$primary;">January 4, 2026</mark>

{% hint style="success" %}
*v5.26.6 and v5.26.7 were skipped as their changes are included in v5.26.8*
{% endhint %}

#### Features and Improvements

* UI: Notification pops up when changes are too large for Auto-Apply

{% hint style="info" %}
Technical info (plugin versions) for **5.26.8:**

* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c99f96542814962beffb0c344156d8bb85fa208b%2FTabnine%20red.png?alt=media" alt="" data-size="line"> Engine: 4.324.7
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-b9a5693a952ab698fae8b49fa5dde2c27cc1b83a%2FVisual%20Studio%20Code%20(VS%20Code).svg?alt=media" alt="" data-size="line"> Visual Studio Code: ***3.331.15***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-74716d5d81d7c0b8ecb601c7d0ac00a6bda75c6b%2FJetBrains.png?alt=media" alt="" data-size="line"> JetBrains IDEs: ***1.279.16***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d8b6b66314cf445674a0cbcce3e803f082b76000%2FEclipse%20IDE.png?alt=media" alt="" data-size="line"> Eclipse: ***1.164.16***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ea81a5ec9acf7fe845aa25f6754cf1a1a852b9e9%2FVisual_Studio_Icon_2019.svg.png?alt=media" alt="" data-size="line"> Visual Studio 2022, 2026 (beta β): ***1.264.17***
  {% endhint %}

***

### v5.26.5

<mark style="color:$primary;">December 23, 2025</mark>

{% hint style="success" %}
*v5.26.4 was skipped as its changes are included in v5.26.5*
{% endhint %}

#### Features and Improvements

* **Remote Files:** Introduced a workaround for setups where fetching remote files in takes too long

### v5.26.3

<mark style="color:$primary;">December 22, 2025</mark>

#### Features and Improvements

* **Agent:**
  * **Governance:**
    * [**MCP Governance**](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/settings/mcp-governance)**:** Admins can now manage MCP access in the Tabnine UI&#x20;
    * [**Native Tool Governance**](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/settings/native-tools)**:** Admins can now manage tool usage in the Tabnine UI

{% hint style="info" %}
Technical info (plugin versions) for **5.26.3:**

* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c99f96542814962beffb0c344156d8bb85fa208b%2FTabnine%20red.png?alt=media" alt="" data-size="line"> Engine: ***4.324.7***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-b9a5693a952ab698fae8b49fa5dde2c27cc1b83a%2FVisual%20Studio%20Code%20(VS%20Code).svg?alt=media" alt="" data-size="line"> Visual Studio Code: ***3.331.13***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-74716d5d81d7c0b8ecb601c7d0ac00a6bda75c6b%2FJetBrains.png?alt=media" alt="" data-size="line"> JetBrains IDEs: ***1.279.14***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d8b6b66314cf445674a0cbcce3e803f082b76000%2FEclipse%20IDE.png?alt=media" alt="" data-size="line"> Eclipse: ***1.164.14***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ea81a5ec9acf7fe845aa25f6754cf1a1a852b9e9%2FVisual_Studio_Icon_2019.svg.png?alt=media" alt="" data-size="line"> Visual Studio 2022, 2026 (beta β): ***1.264.15***
  {% endhint %}

### v5.26.2

<mark style="color:$primary;">December 17, 2025</mark>

#### Bug Fixes

* **Agent:**
  * Fixed issue with Agentic workflow in **IntelliJ** <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-5c5cc41a7ab010d3008c633811cc3c426a04c5b6%2FIntelliJ_IDEA_Icon.svg.png?alt=media" alt="" data-size="line">

{% hint style="info" %}
Technical info (plugin versions) for **5.26.2:**

* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c99f96542814962beffb0c344156d8bb85fa208b%2FTabnine%20red.png?alt=media" alt="" data-size="line"> Engine: *4.324.6*
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-b9a5693a952ab698fae8b49fa5dde2c27cc1b83a%2FVisual%20Studio%20Code%20(VS%20Code).svg?alt=media" alt="" data-size="line"> Visual Studio Code: *3.331.12*
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-74716d5d81d7c0b8ecb601c7d0ac00a6bda75c6b%2FJetBrains.png?alt=media" alt="" data-size="line"> JetBrains IDEs: ***1.279.13***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d8b6b66314cf445674a0cbcce3e803f082b76000%2FEclipse%20IDE.png?alt=media" alt="" data-size="line"> Eclipse: *1.164.13*
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ea81a5ec9acf7fe845aa25f6754cf1a1a852b9e9%2FVisual_Studio_Icon_2019.svg.png?alt=media" alt="" data-size="line"> Visual Studio 2022, 2026 (beta β): *1.264.14*
  {% endhint %}

### v5.26.1

<mark style="color:$primary;">December 17, 2025</mark>

#### Bug Fixes

* **Agent:**
  * Fixed issue with Agentic workflow in **VSCode** <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d6a3275f1b33c468b61ce3faf912a0fc5a134a7b%2Fvsc.webp?alt=media" alt="" data-size="line">

{% hint style="info" %}
Technical info (plugin versions) for **5.26.1:**

* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c99f96542814962beffb0c344156d8bb85fa208b%2FTabnine%20red.png?alt=media" alt="" data-size="line"> Engine: *4.324.6*
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-b9a5693a952ab698fae8b49fa5dde2c27cc1b83a%2FVisual%20Studio%20Code%20(VS%20Code).svg?alt=media" alt="" data-size="line"> Visual Studio Code: ***3.331.12***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-74716d5d81d7c0b8ecb601c7d0ac00a6bda75c6b%2FJetBrains.png?alt=media" alt="" data-size="line"> JetBrains IDEs: ***1.279.12***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d8b6b66314cf445674a0cbcce3e803f082b76000%2FEclipse%20IDE.png?alt=media" alt="" data-size="line"> Eclipse: ***1.164.13***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ea81a5ec9acf7fe845aa25f6754cf1a1a852b9e9%2FVisual_Studio_Icon_2019.svg.png?alt=media" alt="" data-size="line"> Visual Studio 2022, ***2026 (beta β)***: ***1.264.14***
  {% endhint %}

### v5.26.0

<mark style="color:$primary;">December 14, 2025</mark>

#### Features and Improvements

* **Agent:**
  * **IDE Settings:**
    * Added in new [“**+ Add MCP Server**” option](https://docs.tabnine.com/main/getting-started/tabnine-agent/agent-settings#add-new-mcp-servers) in the settings of the IDE plugin
    * [**Cost Controls:**](https://docs.tabnine.com/main/managing-your-team/settings/agent-settings#agent-cost-controls)
      * Admins can now configure monthly consumption caps for organizations and/or per user
    * **Providence & Attribution:**
      * [Attribution now available in Agent](https://docs.tabnine.com/main/welcome/readme/protection/provenance-and-attribution#attribution-in-agent)
    * **Governance:**
      * [**Guidelines** control at the Admin level](https://docs.tabnine.com/main/getting-started/tabnine-agent/guidelines#governance-for-agentic-guidelines)
* **Context Engine:**
  * [**Directory & Symbol Index**](https://docs.tabnine.com/main/getting-started/tabnine-agent/agent-settings#context-engine-tools)**:** Added new search tools for navigating and finding resources in remote codebases (repositories, source code, folders, files, classes, functions, variables, etc.)
    * `remote_repositories_list` - Lists all remote repositories available to your team
    * `remote_symbols_search` - Searches for code symbols (functions, classes, variables) in remote repos by prefix
    * `remote_symbol_content` - Gets complete source code content of symbols from remote repos
    * `remote_repository_folder_tree` - Gets folder structure of a remote repo
    * `remote_files_search` - Searches for files by path/name in remote repos
    * `remote_file_content` - Fetches full content of specific files from remote repos
    * `remote_semantic_and_textual_search` - \[previously called *`remote_codebase_search`*] Performs semantic RAG and lexical search across remote repos.&#x20;
* **Enterprise:**
  * **Teams:**
    * [Team lead role](https://docs.tabnine.com/main/managing-your-team/roles-in-an-enterprise#team-lead) can now manage connected repositories for their own team
    * Users can now [switch between subset of available teams](https://docs.tabnine.com/main/managing-your-team/roles-in-an-enterprise#multi-team-switching) (defined by the admin/manager)
  * **Visual Studio 2026 (beta β):**
    * The Tabnine Visual Studio extension is now available in **beta β** for VS26 <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FnAs1fEuLCy9uwHFbqPXC%2FVs2026_logo.png?alt=media&#x26;token=a45e1da6-d62a-4139-a3e4-d9b985c3d090" alt="" data-size="line">
  * **Admin UI:**&#x20;
    * UI Layout changes&#x20;

#### Bug Fixes

* **Visual Studio 2022**
  * Addressed various bugs with VS22 plugin <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-0920f6c4e65f036c6c903f4f4357aa6baf40aee1%2Fvs.webp?alt=media" alt="" data-size="line">
* **Memory:**
  * Fixed bug related to memory leak
* **Registry:**
  * Closed vulnerabilities related to registry images

{% hint style="info" %}
Technical info (plugin versions) for **5.26.0:**

* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c99f96542814962beffb0c344156d8bb85fa208b%2FTabnine%20red.png?alt=media" alt="" data-size="line"> Engine: ***4.324.6***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-b9a5693a952ab698fae8b49fa5dde2c27cc1b83a%2FVisual%20Studio%20Code%20(VS%20Code).svg?alt=media" alt="" data-size="line"> Visual Studio Code: ***3.331.11***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-74716d5d81d7c0b8ecb601c7d0ac00a6bda75c6b%2FJetBrains.png?alt=media" alt="" data-size="line"> JetBrains IDEs: ***1.279.11***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d8b6b66314cf445674a0cbcce3e803f082b76000%2FEclipse%20IDE.png?alt=media" alt="" data-size="line"> Eclipse: ***1.164.12***
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ea81a5ec9acf7fe845aa25f6754cf1a1a852b9e9%2FVisual_Studio_Icon_2019.svg.png?alt=media" alt="" data-size="line"> Visual Studio 2022: ***1.264.13***
  {% endhint %}

### v5.25.5

<mark style="color:$primary;">November 30, 2025</mark>

#### Features & Improvements

* **Chat:**
  * Added message in Chat to switch over to **Tabnine Agent**

{% hint style="info" %}
Technical info (plugin versions) for **5.25.5:**

* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c99f96542814962beffb0c344156d8bb85fa208b%2FTabnine%20red.png?alt=media" alt="" data-size="line"> Engine: 4.320.2
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-b9a5693a952ab698fae8b49fa5dde2c27cc1b83a%2FVisual%20Studio%20Code%20(VS%20Code).svg?alt=media" alt="" data-size="line"> Visual Studio Code: *3.326.4*
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-74716d5d81d7c0b8ecb601c7d0ac00a6bda75c6b%2FJetBrains.png?alt=media" alt="" data-size="line"> JetBrains IDEs: *1.274.3*
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d8b6b66314cf445674a0cbcce3e803f082b76000%2FEclipse%20IDE.png?alt=media" alt="" data-size="line"> Eclipse: *1.159.4*
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ea81a5ec9acf7fe845aa25f6754cf1a1a852b9e9%2FVisual_Studio_Icon_2019.svg.png?alt=media" alt="" data-size="line"> Visual Studio 2022: *1.254.3*
  {% endhint %}

### v5.25.4

<mark style="color:$primary;">November 26, 2025</mark>

#### Bug Fixes

* **Agent:**
  * Fixed bug where **Apply** drop down was empty account information failed to load
* **Chat:**
  * Fixed bug where Chat failed to load history

{% hint style="info" %}
Technical info (plugin versions) for **5.25.4:**

* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c99f96542814962beffb0c344156d8bb85fa208b%2FTabnine%20red.png?alt=media" alt="" data-size="line"> Engine: 4.320.2
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-b9a5693a952ab698fae8b49fa5dde2c27cc1b83a%2FVisual%20Studio%20Code%20(VS%20Code).svg?alt=media" alt="" data-size="line"> Visual Studio Code: *3.326.3*
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-74716d5d81d7c0b8ecb601c7d0ac00a6bda75c6b%2FJetBrains.png?alt=media" alt="" data-size="line"> JetBrains IDEs: *1.274.2*
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d8b6b66314cf445674a0cbcce3e803f082b76000%2FEclipse%20IDE.png?alt=media" alt="" data-size="line"> Eclipse: *1.159.2*
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ea81a5ec9acf7fe845aa25f6754cf1a1a852b9e9%2FVisual_Studio_Icon_2019.svg.png?alt=media" alt="" data-size="line"> Visual Studio 2022: *1.254.2*
  {% endhint %}

### v5.25.3

<mark style="color:$primary;">November 25, 2025</mark>

#### Features and Improvements

* **Azure** <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-9288c7921771207cbb2c42cb9b757df708a0e4fa%2Fazure%20logo.svg?alt=media" alt="" data-size="line">**:**
  * Added custom host support for Azure provider
  * Added support for Azure Government Cloud URLs
* VSCode <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d6a3275f1b33c468b61ce3faf912a0fc5a134a7b%2Fvsc%20(1).webp?alt=media" alt="" data-size="line">:&#x20;
  * Improved terminal handling

{% hint style="info" %}
Technical info (plugin versions) for **5.25.3:**

* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c99f96542814962beffb0c344156d8bb85fa208b%2FTabnine%20red.png?alt=media" alt="" data-size="line"> Engine: 4.320.2
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-b9a5693a952ab698fae8b49fa5dde2c27cc1b83a%2FVisual%20Studio%20Code%20(VS%20Code).svg?alt=media" alt="" data-size="line"> Visual Studio Code: *3.326.2*
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-74716d5d81d7c0b8ecb601c7d0ac00a6bda75c6b%2FJetBrains.png?alt=media" alt="" data-size="line"> JetBrains IDEs: 1.274.1
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d8b6b66314cf445674a0cbcce3e803f082b76000%2FEclipse%20IDE.png?alt=media" alt="" data-size="line"> Eclipse: 1.159.1
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ea81a5ec9acf7fe845aa25f6754cf1a1a852b9e9%2FVisual_Studio_Icon_2019.svg.png?alt=media" alt="" data-size="line"> Visual Studio 2022: 1.254.1
  {% endhint %}

### v5.25.2

<mark style="color:$primary;">November 24, 2025</mark>

#### Features and Improvements

* **Agent:**
  * <mark style="color:blue;">**Run**</mark> command: Added terminal pool management
* **UI/UX:**
  * Refinements for empty states in **Chat** & **Agent**

{% hint style="info" %}
Technical info (plugin versions) for **5.25.2:**

* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c99f96542814962beffb0c344156d8bb85fa208b%2FTabnine%20red.png?alt=media" alt="" data-size="line"> Engine: 4.320.2
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-b9a5693a952ab698fae8b49fa5dde2c27cc1b83a%2FVisual%20Studio%20Code%20(VS%20Code).svg?alt=media" alt="" data-size="line"> Visual Studio Code: 3.326.1
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-74716d5d81d7c0b8ecb601c7d0ac00a6bda75c6b%2FJetBrains.png?alt=media" alt="" data-size="line"> JetBrains IDEs: 1.274.1
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d8b6b66314cf445674a0cbcce3e803f082b76000%2FEclipse%20IDE.png?alt=media" alt="" data-size="line"> Eclipse: 1.159.1
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ea81a5ec9acf7fe845aa25f6754cf1a1a852b9e9%2FVisual_Studio_Icon_2019.svg.png?alt=media" alt="" data-size="line"> Visual Studio 2022: 1.254.1
  {% endhint %}

### v5.25.1

<mark style="color:$primary;">November 20, 2025</mark>

#### Features and Improvements

* **Models:**
  * Added support for Gemini3-Pro <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-64121828b35fbcbf113dba617435d1cf0d229a81%2Fgemini%20rainbow.png?alt=media" alt="" data-size="line">for **Chat** & **Agent**

#### Bug Fixes

* **Account Info:**
  * Fixed bug where account information failed to load
* **Provenance & Attribution:**
  * Fixed bug where feature didn't censor code properly in Chat (VSCode <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d6a3275f1b33c468b61ce3faf912a0fc5a134a7b%2Fvsc.webp?alt=media" alt="" data-size="line"> & IntelliJ <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-5c5cc41a7ab010d3008c633811cc3c426a04c5b6%2FIntelliJ_IDEA_Icon.svg.png?alt=media" alt="" data-size="line">)
* **Account Utilization:**
  * Fixed bug displaying all-time data instead of over previous 12 weeks
* **IntelliJ IDE** <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-5c5cc41a7ab010d3008c633811cc3c426a04c5b6%2FIntelliJ_IDEA_Icon.svg.png?alt=media" alt="" data-size="line">**:**
  * Fixed bugs involving fetching command output from terminal, Run command

### v5.25.0

<mark style="color:$primary;">November 17, 2025</mark>

#### Features and Improvements

* **Agent:**
  * **Provenance:**
    * Introduced censorship and attribution for **Agent**
  * **Reporting:**
    * Analytics provides overview of **Agent Usage**
  * **Quota:**
    * **Agent Usage** notes separate costs on the GCP level
* **Monitoring:**
  * [**Audit Logs API**](https://docs.tabnine.com/main/managing-your-team/tabnine-apis#audit-logs-api)**:** API access now available for audit logs by [token](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/tabnine-apis/usage-api-1)
* **Teams:**
  * Added new [**Team Lead rol**e](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/roles-in-an-enterprise) who can:
    * View analytics of their own team
    * Manage users of their own team
    * Invite users to their team
* **Chat:**
  * `workspace_search` has been split into Local Workspace Search and Remote Codebase Search. The original `workspace_search` tool will soon be deprecated.

{% hint style="info" %}
Technical info (plugin versions) for **5.25.0:**

* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c99f96542814962beffb0c344156d8bb85fa208b%2FTabnine%20red.png?alt=media" alt="" data-size="line"> Engine: 4.320.2
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-b9a5693a952ab698fae8b49fa5dde2c27cc1b83a%2FVisual%20Studio%20Code%20(VS%20Code).svg?alt=media" alt="" data-size="line"> Visual Studio Code: 3.325.0
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-74716d5d81d7c0b8ecb601c7d0ac00a6bda75c6b%2FJetBrains.png?alt=media" alt="" data-size="line"> JetBrains IDEs: 1.273.0
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d8b6b66314cf445674a0cbcce3e803f082b76000%2FEclipse%20IDE.png?alt=media" alt="" data-size="line"> Eclipse: 1.159.1
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ea81a5ec9acf7fe845aa25f6754cf1a1a852b9e9%2FVisual_Studio_Icon_2019.svg.png?alt=media" alt="" data-size="line"> Visual Studio 2022: 1.254.1
  {% endhint %}

### v5.24.7

<mark style="color:$primary;">November 12, 2025</mark>

#### Bug Fixes

* **Chat:**
  * Fixed issue where **Qwen** <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c800c1f921f0a9179574471daa68624e65ee8aa7%2FTransparent%20Qwen%20logo.png?alt=media" alt="" data-size="line"> model didn’t work for shared inference

### v5.25.0

<mark style="color:$primary;">November 16, 2025</mark>

#### Features and Improvements

* **Agent:**
  * **Provenance:**
    * Introduced censorship and attribution for **Agent**
  * **Reporting:**
    * Analytics provides overview of **Agent Usage**
  * **Quota:**
    * **Agent Usage** notes separate costs on the GCP level and Do It Reports
* Monitoring:
  * Audit Logs API: API access now available for audit logs
* **Teams:**
  * Added new Team Lead role who can:
    * View analytics of their own team
    * Manage users of their own team
    * Invite users to their team
* **Chat:**
  * `workspace_search` has been split into **Local Workspace Search** and **Remote Codebase Search**. The original `workspace_search` tool will soon be deprecated.

### v5.24.6

<mark style="color:$primary;">November 9, 2025</mark>

#### Features and Improvements

* **Models:**
  * Better support for Tabnine-provided **Qwen** <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c800c1f921f0a9179574471daa68624e65ee8aa7%2FTransparent%20Qwen%20logo.png?alt=media" alt="" data-size="line"> with PortKey

### v5.24.5

<mark style="color:$primary;">November 9, 2025</mark>

#### Features and Improvements

* **Agent:**
  * **IntelliJ** <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-5c5cc41a7ab010d3008c633811cc3c426a04c5b6%2FIntelliJ_IDEA_Icon.svg.png?alt=media" alt="" data-size="line">**:** Now runs commands in IntelliJ terminal tabs
  * Agent now stops the conversation when you <mark style="color:blue;">**Reject**</mark> a tool call
  * Added **Try Again** button, *replacing* 'Regenerate' button when Agent encounters error

#### Bug Fixes

* **Models:**
  * Fixed issue with HTTPS proxy for OpenAI <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FBFi46Yyjj0tL8xE8ZEad%2Ficons8-chatgpt-480.png?alt=media&#x26;token=74f6a8e1-8012-4e0c-922d-94c28a32aae9" alt="" data-size="line"> models
* **Chat:**
  * Apply: Fixed bug with file path to network folder
* **Rider IDE** <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c53c4155bf5212ca6bd98cbbcaffb7a107902736%2Frider.png?alt=media" alt="" data-size="line">**:**
  * Fixed issue with Rider indexer
* **Tools:**
  * Fixed issues with JSON syntax for create tool calls
* **Agent:**
  * Fixed issues with inconsistent token consumption
  * Fixed issue with endless loop of code diff

{% hint style="info" %}
Technical info (plugin versions) for **5.24.5:**

* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c99f96542814962beffb0c344156d8bb85fa208b%2FTabnine%20red.png?alt=media" alt="" data-size="line"> Engine: 4.318.2
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-b9a5693a952ab698fae8b49fa5dde2c27cc1b83a%2FVisual%20Studio%20Code%20(VS%20Code).svg?alt=media" alt="" data-size="line"> Visual Studio Code: 3.321.3
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-74716d5d81d7c0b8ecb601c7d0ac00a6bda75c6b%2FJetBrains.png?alt=media" alt="" data-size="line"> JetBrains IDEs: 1.268.7
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d8b6b66314cf445674a0cbcce3e803f082b76000%2FEclipse%20IDE.png?alt=media" alt="" data-size="line"> Eclipse: 1.156.5
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ea81a5ec9acf7fe845aa25f6754cf1a1a852b9e9%2FVisual_Studio_Icon_2019.svg.png?alt=media" alt="" data-size="line"> Visual Studio 2022: 1.251.6
  {% endhint %}

### v5.24.4

Oct 29, 2025

#### Features and Improvements

* **VSCode** <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-b9a5693a952ab698fae8b49fa5dde2c27cc1b83a%2FVisual%20Studio%20Code%20(VS%20Code).svg?alt=media" alt="" data-size="line">
  * Improved binary download and update mechanism to better support slower web connections
* **Chat:**
  * Apply: Improved resolution of file paths
* **Agent:**
  * **Apply:** Improved robustness, better UI rendering
  * **`workspace_search`**: now only searches remote repos, not local repos
  * **Admin Console:** Added fallback for Agent usage metrics even when no quota defined

{% hint style="info" %}
Technical info (plugin versions) for **5.24.4:**

* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c99f96542814962beffb0c344156d8bb85fa208b%2FTabnine%20red.png?alt=media" alt="" data-size="line"> Engine: 4.318.0
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-b9a5693a952ab698fae8b49fa5dde2c27cc1b83a%2FVisual%20Studio%20Code%20(VS%20Code).svg?alt=media" alt="" data-size="line"> Visual Studio Code: 3.321.2
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-74716d5d81d7c0b8ecb601c7d0ac00a6bda75c6b%2FJetBrains.png?alt=media" alt="" data-size="line"> JetBrains IDEs: 1.268.4
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d8b6b66314cf445674a0cbcce3e803f082b76000%2FEclipse%20IDE.png?alt=media" alt="" data-size="line"> Eclipse: 1.156.5
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ea81a5ec9acf7fe845aa25f6754cf1a1a852b9e9%2FVisual_Studio_Icon_2019.svg.png?alt=media" alt="" data-size="line"> Visual Studio 2022: 1.251.6
  {% endhint %}

### v5.24.3

Oct 22, 2025

Features and Improvements

* **Hybrid Search:**
  * Added Qdrant <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-f2878fbbdc38f38faea1b38814958aeee67e1354%2Fqdrant%20logo.png?alt=media" alt="" data-size="line">memory optimization to the new collections for hybrid search

{% hint style="info" %}
Technical info (plugin versions) for **5.24.3:**

* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c99f96542814962beffb0c344156d8bb85fa208b%2FTabnine%20red.png?alt=media" alt="" data-size="line"> Engine: 4.317.1
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-b9a5693a952ab698fae8b49fa5dde2c27cc1b83a%2FVisual%20Studio%20Code%20(VS%20Code).svg?alt=media" alt="" data-size="line"> Visual Studio Code: 3.320.3
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-74716d5d81d7c0b8ecb601c7d0ac00a6bda75c6b%2FJetBrains.png?alt=media" alt="" data-size="line"> JetBrains IDEs: 1.268.0
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d8b6b66314cf445674a0cbcce3e803f082b76000%2FEclipse%20IDE.png?alt=media" alt="" data-size="line"> Eclipse: 1.156.3
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ea81a5ec9acf7fe845aa25f6754cf1a1a852b9e9%2FVisual_Studio_Icon_2019.svg.png?alt=media" alt="" data-size="line"> Visual Studio 2022: 1.251.4
  {% endhint %}

### v5.24.2

Oct 22, 2025

#### Features and Improvements

* **Agent (beta β):**
  * Added **'Send Agent Message'** event option
  * Added retry support for portkey gateway

#### Bug Fixes

* **Initialization:**
  * Fixed slow initialization after updates
* **Agent (beta β):**
  * Quota: Fixed token difference between Chat and Analytics
  * Fixed error where Agent does not release MCP servers from Docker instances

### v5.24.1

October 20, 2025

#### Features and Improvements

* **Models**:
  * Added <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-a0ee6c6377a3b52463a58bdea0c387d39b46f04a%2FClaude%20logo.png?alt=media" alt="" data-size="line"> Claude Haiku 4.5 for Self-Hosted Deployments

### v5.24.0

October 16, 2025

#### Features and Improvements

* **Context Engine:**
  * **Markdown:** `.md` files can now appear as ***context*** from remote codebases
  * **Hybrid Search:** Introduced new hybrid search that combines dense search and sparse search for better results in context retrieval
* **Code Review / Coaching:**
  * **Self-Hosted Models:** Upgrade quality and support for Qwen <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c800c1f921f0a9179574471daa68624e65ee8aa7%2FTransparent%20Qwen%20logo.png?alt=media" alt="" data-size="line"> and Gemma <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-116ec367cae2d34bac1f517d81b756f60720af19%2Fgemma-seeklogo.svg?alt=media" alt="" data-size="line"> models in self-hosted deployments
  * Added option to review changes from any branch to the current branch
  * Reduced errors on CR and Test Agent
  * Now provides separate guideline recommendations from model recommendations
  * Admin can now control whether or nit to have model-based review
  * Can now trigger code review from code lens
* **Provenance & Attribution:**
  * **Provenance:** Allow system admin to define list of permissive licenses
* **Updates:**
  * **For Visual Studio Code** <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-b9a5693a952ab698fae8b49fa5dde2c27cc1b83a%2FVisual%20Studio%20Code%20(VS%20Code).svg?alt=media" alt="" data-size="line"> **and JetBrains** <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-74716d5d81d7c0b8ecb601c7d0ac00a6bda75c6b%2FJetBrains.png?alt=media" alt="" data-size="line">, plugins can now auto-update without restarting the app

#### Bug Fixes

* **Context Engine:**
  * Fixed issue where mentioning `.md` file in local workplace stopped working
  * Fixed issue where Rider IDE <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c53c4155bf5212ca6bd98cbbcaffb7a107902736%2Frider.png?alt=media" alt="" data-size="line"> indexer was not starting
* **Code Review / Coaching:**
  * Fixed bug that prevented guideline deletions
  * Fixed bug where guidelines can't be deleted
  * Fixed bug where there is no CR on untracked files

{% hint style="info" %}
Technical info (plugin versions) for **5.24.0:**

* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c99f96542814962beffb0c344156d8bb85fa208b%2FTabnine%20red.png?alt=media" alt="" data-size="line"> Engine: 4.317.0
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-b9a5693a952ab698fae8b49fa5dde2c27cc1b83a%2FVisual%20Studio%20Code%20(VS%20Code).svg?alt=media" alt="" data-size="line"> Visual Studio Code: 3.320.1
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-74716d5d81d7c0b8ecb601c7d0ac00a6bda75c6b%2FJetBrains.png?alt=media" alt="" data-size="line"> JetBrains IDEs: 1.267.3
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d8b6b66314cf445674a0cbcce3e803f082b76000%2FEclipse%20IDE.png?alt=media" alt="" data-size="line"> Eclipse: 1.156.2
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ea81a5ec9acf7fe845aa25f6754cf1a1a852b9e9%2FVisual_Studio_Icon_2019.svg.png?alt=media" alt="" data-size="line"> Visual Studio 2022: 1.251.3
  {% endhint %}

### v5.23.5

October 1, 2025

#### Features & Improvements

* Improved logging for Coaching / Code Review **(beta β)**
* Added support for Claude 4.5 <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-a0ee6c6377a3b52463a58bdea0c387d39b46f04a%2FClaude%20logo.png?alt=media" alt="" data-size="line">

***

### v5.23.4

September 29, 2025

#### Features and Improvements

* Admin page now manages connection to different teams
* Changed default configurations in Helm chart

{% hint style="info" %}
Technical info (plugin versions) for **5.23.4**:

* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c99f96542814962beffb0c344156d8bb85fa208b%2FTabnine%20red.png?alt=media" alt="" data-size="line"> Engine: 4.314.0
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-b9a5693a952ab698fae8b49fa5dde2c27cc1b83a%2FVisual%20Studio%20Code%20(VS%20Code).svg?alt=media" alt="" data-size="line"> Visual Studio Code: 3.315.0
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-74716d5d81d7c0b8ecb601c7d0ac00a6bda75c6b%2FJetBrains.png?alt=media" alt="" data-size="line"> JetBrains IDEs: 1.262.0
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d8b6b66314cf445674a0cbcce3e803f082b76000%2FEclipse%20IDE.png?alt=media" alt="" data-size="line"> Eclipse: 1.155.0
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ea81a5ec9acf7fe845aa25f6754cf1a1a852b9e9%2FVisual_Studio_Icon_2019.svg.png?alt=media" alt="" data-size="line"> Visual Studio 2022: 1.247.1
  {% endhint %}

### v5.23.3

September 25, 2025

#### Features & Improvements

* Updated port key was updated to Debian-based image (to fix DNS issues in Docker containers)

#### Bug Fixes

* Fixed issue with deleting guidelines
* Fixed issue with Visual Studio crashing

{% hint style="info" %}
Technical info (plugin versions) for **5.23.3**:

* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c99f96542814962beffb0c344156d8bb85fa208b%2FTabnine%20red.png?alt=media" alt="" data-size="line"> Engine: 4.309.3
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-b9a5693a952ab698fae8b49fa5dde2c27cc1b83a%2FVisual%20Studio%20Code%20(VS%20Code).svg?alt=media" alt="" data-size="line"> Visual Studio Code: 3.314.4
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-74716d5d81d7c0b8ecb601c7d0ac00a6bda75c6b%2FJetBrains.png?alt=media" alt="" data-size="line"> JetBrains IDEs: 1.261.1
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d8b6b66314cf445674a0cbcce3e803f082b76000%2FEclipse%20IDE.png?alt=media" alt="" data-size="line"> Eclipse: 1.155.2
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ea81a5ec9acf7fe845aa25f6754cf1a1a852b9e9%2FVisual_Studio_Icon_2019.svg.png?alt=media" alt="" data-size="line"> Visual Studio 2022: 1.248.7
  {% endhint %}

***

### v5.23.2

September 21, 2025

#### Bug Fixes

* Bug fix for Macbook x86 arch <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-fbbc3ef20d09b540c3d3bafc12234bfed099aa92%2Fimage.png?alt=media" alt="" data-size="line">

***

### v5.23.1

September 17, 2025

#### Features and Improvements

* **Agent (beta β):**
  * Proxy settings are disabled by default for the node process in Axios instances <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-2bb669212aff840b63d7de74b30aee6d46266405%2FAxios.svg?alt=media" alt="" data-size="line">

#### Bug Fixes

* **Apply:**
  * Fixed issue where **Apply** lags on larger files
* **Agent (beta β):**
  * Fixed bug where Agentic flow didn’t work in Rider IDE <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c53c4155bf5212ca6bd98cbbcaffb7a107902736%2Frider.png?alt=media" alt="" data-size="line">
* **Code Review / Coaching (beta β):**
  * Fixed bug where untracked files are not reviewed

{% hint style="info" %}
Technical info (plugin versions):

* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c99f96542814962beffb0c344156d8bb85fa208b%2FTabnine%20red.png?alt=media" alt="" data-size="line"> Engine: 4.309.1
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-b9a5693a952ab698fae8b49fa5dde2c27cc1b83a%2FVisual%20Studio%20Code%20(VS%20Code).svg?alt=media" alt="" data-size="line"> Visual Studio Code: 3.314.4
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-74716d5d81d7c0b8ecb601c7d0ac00a6bda75c6b%2FJetBrains.png?alt=media" alt="" data-size="line"> JetBrains IDEs: 1.261.1
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d8b6b66314cf445674a0cbcce3e803f082b76000%2FEclipse%20IDE.png?alt=media" alt="" data-size="line"> Eclipse: 1.155.2
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ea81a5ec9acf7fe845aa25f6754cf1a1a852b9e9%2FVisual_Studio_Icon_2019.svg.png?alt=media" alt="" data-size="line"> Visual Studio 2022: 1.248.2
  {% endhint %}

***

### v5.23.0 <a href="#v5.23.0" id="v5.23.0"></a>

September 14, 2025

**Features and Improvements**

* **Agent (beta β):**
  * **History:** Users can now view session history
  * **Automation Control:** Users can now give native tool permissions by switching between 1) *Automatic Approval*, 2) *Ask First*, and 3) *Disable*
* **Connection:**
  * Expanding filetypes to be covered by [Context Scope](https://docs.tabnine.com/main/getting-started/tabnine-chat/chat-context/context-scoping) (i.e.,, explicit mention of files from remote codebase): `.md, .mkd, .mdwn, .mdown, .mdtxt, .mdtext, .markdown, .yaml, .yml, .json, .xml, .gradle, bash, .sh, .txt, .ini, .properties, .prefs, .cfg, .cmake`
* **Reporting**:
  * Added thumbs-down data to visual and CSV usage reports
* **Provenance and Attribution**:
  * **Improved Attribution:** Not attempting to attribute imports and comments on the following languages: JavaScript, TypeScript, Java, Kotlin, Python, C#, Golang, and PHP
  * Have an indication when a specific code could not be attributed due to error
* **Jira Connection** <img src="https://open-2c.gitbook.com/url/preview/site_AIYf2/~gitbook/image?url=https%3A%2F%2F3436682446-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FY2qxVf5VTm3fmwP4B4Gx%252Fuploads%252F9xmJUTod1uqL3Z9Yt2jP%252FJira.svg%3Falt%3Dmedia%26token%3Dc49cc797-68b9-4398-b3b4-0062e7dc61a9&#x26;width=40&#x26;dpr=4&#x26;quality=100&#x26;sign=53e1628&#x26;sv=2" alt="" data-size="line">:
  * Support searching **Jira** by issue number

**Bug Fixes**

* **Visual Studio 2022** <img src="https://open-2c.gitbook.com/url/preview/site_AIYf2/~gitbook/image?url=https%3A%2F%2F3436682446-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FY2qxVf5VTm3fmwP4B4Gx%252Fuploads%252F3T285cXG0Bqkl9h9SLmR%252FVisual_Studio_Icon_2019.svg.png%3Falt%3Dmedia%26token%3D6067d910-4b35-4ec1-a1b9-96a24c3778dc&#x26;width=40&#x26;dpr=4&#x26;quality=100&#x26;sign=3bf5283e&#x26;sv=2" alt="" data-size="line">:
  * Fixed plugin installation error
  * Fixed issue where plugin fails to install
  * Fixed issue where Chat causes extension to stop
  * Fixed slow performance upon initial installation
* **Code Review (beta β):**
  * Fixed bug where staged files were not reviewed in JetBrains IDEs
* **Apply:**
  * Fixed bug where **Apply** button disappears
* **Reporting:**
  * Fixed bug where thumbs-down info was reported as thumbs-up
* **Testing:**
  * Fixed bug where test agent didn’t work with **Gemini 2.5 Flash** <img src="https://open-2c.gitbook.com/url/preview/site_AIYf2/~gitbook/image?url=https%3A%2F%2F3436682446-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FY2qxVf5VTm3fmwP4B4Gx%252Fuploads%252FzvyiWxINauHJ3oN4s8ue%252Fgemini%2520rainbow.png%3Falt%3Dmedia%26token%3D4e47efc6-8a26-4a12-9931-ca9766eb76ad&#x26;width=40&#x26;dpr=4&#x26;quality=100&#x26;sign=6a8e35f7&#x26;sv=2" alt="" data-size="line">
* **Jira** <img src="https://open-2c.gitbook.com/url/preview/site_AIYf2/~gitbook/image?url=https%3A%2F%2F3436682446-files.gitbook.io%2F%7E%2Ffiles%2Fv0%2Fb%2Fgitbook-x-prod.appspot.com%2Fo%2Fspaces%252FY2qxVf5VTm3fmwP4B4Gx%252Fuploads%252F9xmJUTod1uqL3Z9Yt2jP%252FJira.svg%3Falt%3Dmedia%26token%3Dc49cc797-68b9-4398-b3b4-0062e7dc61a9&#x26;width=40&#x26;dpr=4&#x26;quality=100&#x26;sign=53e1628&#x26;sv=2" alt="" data-size="line">**:**
  * Fixed connection issue with Jira Cloud

{% hint style="info" %}
Technical info (plugin versions):

* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c99f96542814962beffb0c344156d8bb85fa208b%2FTabnine%20red.png?alt=media" alt="" data-size="line"> Engine: 4.309.0
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-b9a5693a952ab698fae8b49fa5dde2c27cc1b83a%2FVisual%20Studio%20Code%20(VS%20Code).svg?alt=media" alt="" data-size="line"> Visual Studio Code: 3.314.1
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-74716d5d81d7c0b8ecb601c7d0ac00a6bda75c6b%2FJetBrains.png?alt=media" alt="" data-size="line"> JetBrains IDEs: 1.261.0
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d8b6b66314cf445674a0cbcce3e803f082b76000%2FEclipse%20IDE.png?alt=media" alt="" data-size="line"> Eclipse: 1.155.0
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ea81a5ec9acf7fe845aa25f6754cf1a1a852b9e9%2FVisual_Studio_Icon_2019.svg.png?alt=media" alt="" data-size="line"> Visual Studio 2022: 1.247.1
  {% endhint %}

***

### v5.22.10

September 14, 2025

#### Features and Improvements

* **GPT-OSS support**

***

### v5.22.9

September 9, 2025

#### Bug Fixes

* Agent **(beta β):**
  * Fixed issues with **prompts** on Windows
  * Fixed issues while working with **proxies**

{% hint style="info" %}
Technical info (plugin versions):

* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c99f96542814962beffb0c344156d8bb85fa208b%2FTabnine%20red.png?alt=media" alt="" data-size="line"> Engine: 4.302.5
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-b9a5693a952ab698fae8b49fa5dde2c27cc1b83a%2FVisual%20Studio%20Code%20(VS%20Code).svg?alt=media" alt="" data-size="line"> Visual Studio Code: 3.300.4
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-74716d5d81d7c0b8ecb601c7d0ac00a6bda75c6b%2FJetBrains.png?alt=media" alt="" data-size="line"> JetBrains IDEs: 1.249.4
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d8b6b66314cf445674a0cbcce3e803f082b76000%2FEclipse%20IDE.png?alt=media" alt="" data-size="line"> Eclipse: 1.149.5
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ea81a5ec9acf7fe845aa25f6754cf1a1a852b9e9%2FVisual_Studio_Icon_2019.svg.png?alt=media" alt="" data-size="line"> Visual Studio 2022: 1.241.6
  {% endhint %}

***

### v5.22.8

September 8, 2025

#### Bug Fixes

* **Visual Studio 2022** <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ea81a5ec9acf7fe845aa25f6754cf1a1a852b9e9%2FVisual_Studio_Icon_2019.svg.png?alt=media" alt="" data-size="line"> **:**
  * Fixed issue with LSP loading order

{% hint style="info" %}
Technical info (plugin versions):

* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c99f96542814962beffb0c344156d8bb85fa208b%2FTabnine%20red.png?alt=media" alt="" data-size="line"> Engine: 4.302.4
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-b9a5693a952ab698fae8b49fa5dde2c27cc1b83a%2FVisual%20Studio%20Code%20(VS%20Code).svg?alt=media" alt="" data-size="line"> Visual Studio Code: 3.300.4
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-74716d5d81d7c0b8ecb601c7d0ac00a6bda75c6b%2FJetBrains.png?alt=media" alt="" data-size="line"> JetBrains IDEs: 1.249.4
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d8b6b66314cf445674a0cbcce3e803f082b76000%2FEclipse%20IDE.png?alt=media" alt="" data-size="line"> Eclipse: 1.149.5
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ea81a5ec9acf7fe845aa25f6754cf1a1a852b9e9%2FVisual_Studio_Icon_2019.svg.png?alt=media" alt="" data-size="line"> Visual Studio 2022: **1.241.6**
  {% endhint %}

***

### v5.22.7

September 4, 2025

#### Bug Fixes

* **Apply:**
  * Fixed bug where Apply button missing for dedicated Apply models

{% hint style="info" %}
Technical info (plugin versions):

* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c99f96542814962beffb0c344156d8bb85fa208b%2FTabnine%20red.png?alt=media" alt="" data-size="line"> Engine: 4.302.4
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-b9a5693a952ab698fae8b49fa5dde2c27cc1b83a%2FVisual%20Studio%20Code%20(VS%20Code).svg?alt=media" alt="" data-size="line"> Visual Studio Code: 3.300.4
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-74716d5d81d7c0b8ecb601c7d0ac00a6bda75c6b%2FJetBrains.png?alt=media" alt="" data-size="line"> JetBrains IDEs: 1.249.4
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d8b6b66314cf445674a0cbcce3e803f082b76000%2FEclipse%20IDE.png?alt=media" alt="" data-size="line"> Eclipse: 1.149.5
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ea81a5ec9acf7fe845aa25f6754cf1a1a852b9e9%2FVisual_Studio_Icon_2019.svg.png?alt=media" alt="" data-size="line"> Visual Studio 2022: 1.241.5
  {% endhint %}

***

### v5.22.6

September 3, 2025

#### Features and Improvements

* **Models:**
  * Added <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-7c750318da4477aa49b555b3a3f3f7e5c6060a2d%2Fazure.png?alt=media" alt="" data-size="line"> **Azure** GPT-5 model support

#### Bug Fixes

* **Integrations:**
  * Fixed <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-400b99ab2a0a3969e4bea4ac1c1eebbfc65d0cd8%2FJira.svg?alt=media" alt="" data-size="line"> **Jira** integration failures caused by HTTP 410 errors

{% hint style="info" %}
Technical info (plugin versions):

* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-c99f96542814962beffb0c344156d8bb85fa208b%2FTabnine%20red.png?alt=media" alt="" data-size="line"> Engine: 4.302.3
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-b9a5693a952ab698fae8b49fa5dde2c27cc1b83a%2FVisual%20Studio%20Code%20(VS%20Code).svg?alt=media" alt="" data-size="line"> Visual Studio Code: 3.300.3
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-74716d5d81d7c0b8ecb601c7d0ac00a6bda75c6b%2FJetBrains.png?alt=media" alt="" data-size="line"> JetBrains IDEs: 1.249.3
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d8b6b66314cf445674a0cbcce3e803f082b76000%2FEclipse%20IDE.png?alt=media" alt="" data-size="line"> Eclipse: 1.149.4
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ea81a5ec9acf7fe845aa25f6754cf1a1a852b9e9%2FVisual_Studio_Icon_2019.svg.png?alt=media" alt="" data-size="line"> Visual Studio 2022: 1.241.4
  {% endhint %}

***

### v5.22.5

August 26, 2025

{% hint style="success" %}
Note: (5.22.2, 5.22.3 and 5.22.4 were superseded by changes in 5.22.5, so they were not released)
{% endhint %}

#### Features and Improvements

* **Indexing**:
  * Improved remote indexing

***

### v5.22.1

August 24, 2025

(Merges changes from [5.21.8](#v5.21.8) which were released separately from 5.22.0)

#### Bug Fixes

* **Agent (beta β):**
  * (from 5.21.8) Fixed bug where Apply didn't work on long files
  * (from 5.21.8) Fixed bug where run command hangs on (VSCode)
* **Code Review / Coaching (beta β):**
  * Fixed “deactivation” toggle

{% hint style="info" %}
Technical info (plugin versions):

* Engine: 4.302.2
* Visual Studio Code: 3.300.2
* JetBrains IDEs: 1.249.2
* Eclipse: 1.149.3
* Visual Studio 2022: 1.241.3
  {% endhint %}

***

### v5.22.0

August 19, 2025

#### Features and Improvements

* **Agent (beta β)**:
  * **Guidelines**: Agent Guidelines
  * **Models**: Additional support for GPT, Gemini
  * **IDE**: Additional support for JetBrains IDEs
* **Code Review/Coaching (beta β):**
  * **Guidelines**: Allows for multiple languages in guidelines
  * **Review**: Review selected code with the `/review` command
  * **Code Review Model:** Added support for Claude 3.7 & Claude 4.0
* [**Provenance and Attribution:**](https://docs.tabnine.com/main/welcome/readme/protection/provenance-and-attribution)
  * [**Logging**](https://docs.tabnine.com/main/getting-started/code-completion/code-acceptance-logs): Easy log export
* [**Connection**](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/settings/workspace-settings/connecting-to-remote-repositories):
  * [**Symbols**](https://docs.tabnine.com/main/getting-started/code-completion): Can now use mention for remote symbols (with % rather than @ to reference files)
    * Available Languages: Java, Python, JavaScript, TypeScript, C, C#, C++
* [**Visual Studio 2022**](https://docs.tabnine.com/main/getting-started/install/client-setup-private-installation/visual-studio-private-installation) <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-0920f6c4e65f036c6c903f4f4357aa6baf40aee1%2Fvs%20(1).webp?alt=media" alt="" data-size="line">:
  * Improved **Apply** flow
  * Improved performance
  * Reduced logs
* **Admin UI**:
  * Added “Last 30 days” time frame in **Analytics** home
  * Teams page now shows the number of connected repositories (if the remote codebase option is enabled)

#### Bug Fixes

* [**Chat**](https://docs.tabnine.com/main/getting-started/tabnine-chat/interact):
  * **Scoping**: Chat too sensitive to binary timeouts
* **Code Review/Coaching (beta β)**:
  * **Guidelines**: Can now enable or disable recompilation of rule upon status change
* **Plugin**:
  * **Updates**: Fixed bug affecting binary auto-update
* **Automation Factor**:
  * Fixed the calculation of the automation factor and chat consumption rate
* **User Management:**
  * Fix bug: add anonymize user - add validation that makes sure the user is deactivated
* [**Reports**](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/reporting):
  * Fixed bug where `"Last Used"` field in `user_summary.csv` excluded chat interactions

{% hint style="info" %}
Technical info (plugin versions):

* Engine: 4.302.0
* Visual Studio Code: 3.300.1
* JetBrains IDEs: 1.249.1
* Eclipse: 1.149.2
* Visual Studio 2022: 1.241.2
  {% endhint %}

***

### v5.21.8

August 19, 2025

#### Features & Improvements

* Now generates default UUID for inference queries

#### Bug Fixes

* **Agent (beta β)**:
  * Fixed bug where **Apply** didn't work on long files
  * Fixed bug where <mark style="color:orange;">**`run`**</mark> command hangs on (VSCode <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-d6a3275f1b33c468b61ce3faf912a0fc5a134a7b%2Fvsc%20(1).webp?alt=media" alt="" data-size="line"> )

***

### v5.21.7

August 13, 2025

#### Features & Improvements

* **Agent (beta β)**:
  * Added support for environment variable `DEFAULT_AGENT_RATE_LIMIT_CONFIG_BASE64` to allow overriding agent rate limits at runtime

***

### v5.21.6

August 10, 2025

#### Bug Fixes

* **Coaching (beta β)**:
  * Fixed bug where the Coaching server and Coaching worker pods could fail

***

### v5.21.5

August 7, 2025

#### Bug Fixes

* **Prompts**:
  * Fixed bug where mismatch in prompt size results in increased error rate
* **Grafana**:
  * Fixed bug in Grafana dashboards to account for changes in inference

***

### v5.21.4

August 5, 2025

#### Bug Fixes

* **CSV Import**:
  * Fixed CSV imports with partially missing `rule_id`
* **Kubernetes**:
  * Fixed bug where shared inference was not validated with helm template or `helm --dry-run`
* **Apply**:
  * Fixed bug where dealer timeout was missing on some Apply profiles

***

### v5.21.3

July 31, 2025

#### Features and Improvements

* **Qdrant**:
  * Support for external Qdrant connections

#### Bug Fixes

* **Redis**:
  * Fixed issue in the inference-gateway service to support Redis mTLS and existing secret configurations

***

### v5.21.2

July 28, 2025

#### Features and Improvements

* **Switchable Models**:
  * Upgraded <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-11ea2353753655e5e498e3c2d1602647bedee838%2FGemini.png?alt=media" alt="" data-size="line"> Gemini 2.5 Pro and Flash to latest version (not preview)
* **Coaching (beta β)**:
  * CSV Files:
    * Increased max file size for CSV imports

#### Bug Fixes

* **Authentication**:
  * Fixed problem where `/auth/refresh 401` created load on auth service
* **Chat**:
  * Fixed timeout on long request

{% hint style="info" %}
Technical info (plugin versions):

* Engine: 4.298.4
* Visual Studio Code: 3.296.2
* JetBrains: 1.244.1
* Eclipse: 1.146.1
* Visual Studio 2022: 1.237.2
  {% endhint %}

***

### v5.21.1

July 23, 2025

#### Features and Improvements

* **Switchable Models**:
  * Upgraded Gemini models

#### Bug Fixes

* **Kubernetes**:
  * Fix for RKE2: <mark style="color:orange;">`runtimeClassName4`</mark>

{% hint style="info" %}
Technical info (plugin versions):

* Engine: 4.298.3
* Visual Studio Code: 3.296.1
* JetBrains: 1.244.0
* Eclipse: 1.146.0
* Visual Studio 2022: 1.237.1
  {% endhint %}

***

### v5.21.0

July 14, 2025

#### Features and Improvements

* **Coaching (beta β)**:
  * Enabled on the team level
  * Renamed the tab to simply "Review"
  * Added new *Team* designation for Coaching Guidelines: It is now possible to define each guideline for all teams or for specific (single to multiple) teams
* **Integrations**:
  * [**Jira**](https://docs.tabnine.com/main/welcome/readme/integrations/atlassian-jira): Tabnine now supports multiple Jira Cloud instances
* [**Reports**](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/reporting): New metrics in analytics overview of Admin UI
  * Metrics cover data about productivity factor, active users in chat, and chat completion rate
* **Edit**:
  * Moved Edit into private beta 𝝱 mode
  * Added analytics dashboard for Edit Agent

#### Bug Fixes

* ﻿﻿**Connections**:
  * Scoping: Fixed mix up in colors between dark version and light version
* **Analytics**﻿﻿:
  * Fixed bug where events weren't reported for accepting diffs

{% hint style="info" %}
Technical info (plugin versions):|

* ﻿﻿Engine: 4.280.0
* ﻿﻿Visual Studio Code: 3.291.0
* ﻿﻿JetBrains: 1.240.0
* ﻿﻿Eclipse: 1.143.0
* ﻿﻿Visual Studio 2022: 1.233.0
  {% endhint %}

***

### v5.20.8

July 28, 2025

#### Bug Fixes

* Fixed `auth refresh` token

***

### v5.20.7

#### Bug Fixes

* Fixed 'ignore certificate error' in VS2022

***

### v5.20.6

#### Bug Fixes

* Fixed SMTP settings admin panel when authentication is not required

***

### v5.20.5

July 15, 2025

#### Features and Improvements

* Changed <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-06c1d54999cc8328fa90a7bd3ef3f81eb1ed17bd%2Ficon%3DQwen%402x.png?alt=media" alt="" data-size="line"> Qwen config for H100-3g to support customers with higher number of users

#### Bug Fixes

* Added debug logs that print times for fetching remote files

***

### v5.20.4

July 9, 2025

#### Bug Fixes

* **Code Review / Coaching (beta β)**:
  * Fixed issue in Coaching where guideline violation wouldn't be recognized in short lines

***

### v5.20.3

July 6, 2025

#### Features and Improvements

* Added L40 GPU support

***

### v5.20.2

July 2, 2025

#### Bug Fixes

* **Code Review / Coaching (beta β):**
  * Fixed connection issue and processing of TSX & JSX files

***

### v5.20.1

June 29, 2025

#### Features and Improvements

* [**Code Completions**](https://docs.tabnine.com/main/getting-started/code-completion)**:**
  * Added ability to pause code completions (currently available in <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-5c5cc41a7ab010d3008c633811cc3c426a04c5b6%2FIntelliJ_IDEA_Icon.svg.png?alt=media" alt="" data-size="line"> IntelliJ only)
* **Code Review / Coaching (beta β):**
  * Adjusted configuration for self-hosted deployments (Redis)
* [**Scoping**](https://docs.tabnine.com/main/getting-started/tabnine-chat/chat-context/context-scoping)**:**
  * Now reloads configuration every hour to ensure constant updating

#### Bug Fixes

* [**Provenance & Attribution:**](https://docs.tabnine.com/main/welcome/readme/protection/provenance-and-attribution)
  * Fixed bug where Attribution didn't work when certain other files were open
* **Apply:**
  * Fixed bug where Apply failed to recognize directory names with spaces
* [**IdP Sync:**](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/idp-sync)
  * Fixed <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-f2585704101b7119d821455dd3f0d42d636da0d7%2FSCIM.png?alt=media" alt="" data-size="line"> SCIM API bug – now supports pagination (needed for

    <picture><source srcset="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-5e007ad462944a955a0a5cdeb108fec4f05fbdd4%2FOkta_Aura_White_L.png?alt=media" media="(prefers-color-scheme: dark)"><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-498d994363f704ce6b160eee04153dd8ca5128bb%2Fokta-logo.png?alt=media" alt=""></picture>

    Okta SCIM sync)

{% hint style="info" %}
Technical info (plugin versions):

* Engine: 4.281.1
* Visual Studio Code: 3.292.1
* JetBrains: 1.241.1
* Eclipse: 1.441.1
* Visual Studio 2022: 1.234.1
  {% endhint %}

***

### v5.20.0

June 22, 2025

#### Features and Improvements

* [**Reports**](https://docs.tabnine.com/main/administering-tabnine/private-installation/managing-your-team/reporting/reports-glossary) – New metrics in analytics overview of admin UI:
  * Metrics cover data about [productivity factor](https://docs.tabnine.com/main/administering-tabnine/private-installation/managing-your-team/reporting/reports-glossary#productivity-factor-code-completions-and-chat), [active users in chat](https://docs.tabnine.com/main/administering-tabnine/private-installation/managing-your-team/reporting/reports-glossary#active-user), and [chat consumption rate](https://docs.tabnine.com/main/administering-tabnine/private-installation/managing-your-team/reporting/reports-glossary#chat-consumption-rate).
* **Edit**:
  * Launched in Alpha 𝝰 mode.
  * Enabled on the Team level
* **Code Review** (Private beta 𝝱):
  * Enabled on the Team level
  * Added new Team designation for Coaching Guidelines — It is now possible to define each guideline for all teams or for specific (single to multiple) teams.
  * Renamed the tab as simply Review.

#### Bug Fixes

* [**Connections**](https://docs.tabnine.com/main/welcome/readme/personalization/connection-global-codebase-awareness):
  * [**Scoping**](https://docs.tabnine.com/main/getting-started/tabnine-chat/chat-context/context-scoping): Fixed mix up in colors between dark version and light version
* **Analytics**:
  * Fixed bug where events weren’t reported for accepting diffs

{% hint style="info" %}
Technical info (plugin versions):

* Engine: 4.280.0
* Visual Studio Code: 3.291.0
* JetBrains: 1.240.0
* Eclipse: 1.143.0
* Visual Studio 2022: 1.233.0
  {% endhint %}

***

### v5.19.3

June 18, 2025

Features and Improvements

* **Coaching**:
  * Fixed some configurations for <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ebdd5d13957cc3c32defdf704d0a96495b39e3c7%2Ficon%3DQwen.svg?alt=media" alt="" data-size="line"> Qwen2.5-32B-Instruct

***

### v5.19.2

June 9, 2025

{% hint style="success" %}
*v5.19.1 was skipped as its changes are included in v5.19.2*
{% endhint %}

#### Features and Improvements

* **Switchable Models**:
  * Added support for <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-6d0552e35bb29b23f814b7a4d7e065c05632d79c%2Ficon%3DClaude%402x.png?alt=media" alt="" data-size="line"> Claude 4.0 Sonnet, <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-a2616c96f0989996759a26edb452d13ff42a714c%2Ficon%3Dgpt%402x.png?alt=media" alt="" data-size="line"> GPT 4.1, <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-11ea2353753655e5e498e3c2d1602647bedee838%2FGemini.png?alt=media" alt="" data-size="line"> Gemini 2.5 Flash, and <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-11ea2353753655e5e498e3c2d1602647bedee838%2FGemini.png?alt=media" alt="" data-size="line"> Gemini 2.5 Pro
  * Deprecated <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-a2616c96f0989996759a26edb452d13ff42a714c%2Ficon%3Dgpt%402x.png?alt=media" alt="" data-size="line"> GPT 3.5-Turbo and <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-a2616c96f0989996759a26edb452d13ff42a714c%2Ficon%3Dgpt%402x.png?alt=media" alt="" data-size="line"> GPT 4-Turbo
* **Chat**:
  * Improved file path support
  * Added support for private certificate authorities when using OpenAI API-compatible endpoints
* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-e95242b56b730fc5b58573b2aa4ef1d443003f90%2FPerforce%20logo%20gray.png?alt=media" alt="" data-size="line"> **Perforce**:
  * Local indexing support for `p4config` and `p4ignore` utilization
* **Local VDB Configuration**:
  * Added support for <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-3aaf7f76e5b623d5254b11f0427782253acdaf5c%2Fpodman%20logo.svg?alt=media" alt="" data-size="line"> Podman in addition to Docker

#### Bug Fixes

* Fixed local indexing stuck ignoring `.tabnineignore`
* Fixed Chat response freeze on IDE minimization or desktop change
* Fixed occasional failure with Apply for Gemma-generated code

{% hint style="info" %}
Technical info (plugin versions):

* Engine: 4.279.0
* Visual Studio Code: 3.288.0
* JetBrains: 1.236.0
* Eclipse: 1.141.0
* Visual Studio 2022: 1.229.0
  {% endhint %}

***

### v5.19.0

May 29, 2025

#### Features and Improvements

* **Chat**:
  * Increased the size of the context window
* **Provenance & Attribution**:
  * [**UI facelift**](https://docs.tabnine.com/main/welcome/readme/protection/provenance-and-attribution#walkthrough): Groups content by license, displays matching code snippets, and links to actual matches
* **Apply**:
  * Improved Apply UX that shows where (which files) applied changes successfully
* **Connections – Scope**:
  * Files now fully available to Context scope, not just search scope
* **Code Review (beta β)**:
  * Inserted default Tabnine Rules
* **Code Review / Coaching** **(Private β preview)**:
  * *Coaching Rules* are now called ***Coaching Guidelines***.
  * **Code Review in the IDE**: Added the option to review code changes in the IDE based on your organization’s coaching guidelines (Available in VSC, JetBrains)
  * **Code Review** now offers review suggestions based on the model, in addition to the suggestions that are based on the coaching guidelines
  * Introduced *default guidelines* for: Python, JavaScript, Java, TypeScript
  * **Import**: Introduced importing coaching guidelines:
    * Language is now part of the `.csv`
    * More detailed error messages for invalid input

Bug Fixes

* **Connections – Scope**:
  * UX: Fixed bug with light theme text colors
* **Jira**:
  * IDE: Fixed bug where user would disconnect from Jira within their IDE after an hour
* **Code Review / Coaching** (Private β preview):
  * **Coaching** – Guidelines:
    * Now shows the correct severity in the guidelines table
    * Various bug fixes for importing guidelines

#### Versions

{% hint style="info" %}
Technical info (plugin versions):

* Engine: 4.277.1
* Visual Studio Code: 3.286.0
* JetBrains: 1.234.0
* Eclipse: 1.139.0
* Visual Studio 2022: 1.227.0
  {% endhint %}

***

### v5.18.6

May 22, 2025

#### Features and Improvements

* Added `global.tabnine.telemetry.fluentd.enabled` to control whether Fluentd is used for log collection. Keeps things backward-compatible while moving toward OpenTelemetry.

#### Bug Fixes

* Fixed issue with worker configuration (Postgres and OpenTelemetry)

***

### v5.18.5

May 19, 2025

#### Feature Enhancements

* **Scoping**:
  * Retrieved remote files are directly attached to the prompt
  * Retrieved (local and remote) files will appear right after the current file but before retrieval snippets
  * If file retrieval fails, the user is notified

{% hint style="info" %}
Technical info (plugin versions):

* Engine: 4.262.1
* Visual Studio Code: 3.262.2
* JetBrains: 1.225.2
* Eclipse: 1.136.2
* Visual Studio 2022: 1.206.2
  {% endhint %}

***

### v5.18.4

May 15, 2025

#### Bug Fixes

* **VSCode**: Updated Tabnine Enterprise extension so IDE successfully reloads after version update

***

### v5.18.3

May 8, 2025

#### Bug Fixes

* Fixed bug in Coaching rules **(beta β)** in admin UI

***

### v5.18.2

May 5, 2025

#### Features and Improvements

* **Switchable Models**: Added Gemma model support for A100 40/80, H100, L40s

#### Bug Fixes

* **Tabnine Chat**: Fixed bug that double-pasted content into chat prompt window
* **Connection**: Improved algorithm for remote RAG retrieval

***

### v5.18.1

April 29, 2025

#### Features and Improvements

* **Tabnine Chat**: Launched model support for Gemma (private installations)

#### Bug Fixes

* **Switchable Models**: Fixed Admin UI
* **Perforce**: Fixed depot not properly connecting
* **Scoping**: Fixes file search not displaying certain results

{% hint style="info" %}
Technical info (plugin versions):

* Engine: 4.262.0
* Visual Studio Code: 3.262.0
* JetBrains: 1.223.0
* Eclipse: 1.135.0
* Visual Studio 2022: 1.205.0
  {% endhint %}

***

### v5.18.0

April 27, 2025

#### Features and Improvements

* [**Log All Accepted Code**](https://github.com/codota/docs/blob/main/main/administering-tabnine/private-installation/broken-reference/README.md): We now give private installation users the ability to log all Tabnine AI-generated code that their developers inserted into the codebase.
* **Dedicated Apply Model**: A specialized model for accurately applying code changes to existing projects has been developed and deployed for clients served by Tabnine model endpoints.
* [**Usage API**](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/tabnine-apis): The Usage API provides programmatic access to usage metrics across an organization. It complements existing enterprise reporting options—UI-based usage reports and CSV exports—by enabling integration into internal dashboards and tools via API.

#### Bug Fixes

* Remote Indexing

{% hint style="info" %}
Technical info (plugin versions):

* Engine: 4.262.0
* Visual Studio Code: 3.260.0
* JetBrains: 1.221.0
* Eclipse: 1.133.0
* Visual Studio 2022: 1.203.1
  {% endhint %}

***

### v5.17.3

April 23, 2025

#### Bug Fixes

* Various bug fixes

***

### v5.17.2

April 22, 2025

#### Bug Fixes

* Various bug fixes

***

### v5.17.1

April 21, 2025

#### Bug Fixes

* Fixed bug in [IdP sync](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/idp-sync) that caused DB locks

{% hint style="info" %}
Technical info (plugin versions):

* Engine: 4.257.2
* Visual Studio Code: 3.253.0
* JetBrains: 1.218.0
* Eclipse: 1.130.0
* Visual Studio: 1.200.1
  {% endhint %}

***

### v5.17.0

April 10, 2025

#### Features and Improvements

* [Code Review](https://docs.tabnine.com/main/administering-tabnine/broken-reference) (private preview):
  * Admin can now manage rules for Tabnine Code Review in the Admin UI.
  * Bug Fixes
* [Connection](#connection-global-rag):
  * Added option to connect to remote Perforce depots.
* [Switchable Models](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/settings/models-settings):
  * Added Qwen2.5-32B-Instruct <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ebdd5d13957cc3c32defdf704d0a96495b39e3c7%2Ficon%3DQwen.svg?alt=media" alt="" data-size="line"> to private endpoint options

#### Bug Fixes

* [Reporting](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/reporting/reporting):
  * Fixed bug that caused the Admin Console and CSV to report fewer active users than there were. Users who only performed Chat interactions were excluded.
    * *Impact*: The Tabnine Admin Console UI and CSV reports underreported active users. In addition, some users were reported in status “Connected” when they should be “Used.”

{% hint style="info" %}
Technical info (plugin versions):

* Engine: 4.257.0
* Visual Studio Code: 3.253.0
* JetBrains: 1.218.0
* Eclipse: 1.130.0
* Visual Studio: 1.200.1
  {% endhint %}

***

### v5.16.4

April 9, 2025

#### Features

* Added Llama 3.3 <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-46ec5493ccc6d53ef68f3b5808066815437ac54e%2Ficon%3Dlama.svg?alt=media" alt="" data-size="line"> support

***

### v5.16.3

April 6, 2025

#### Bug Fixes

* Various bug Fixes

***

### v5.16.2

March 27, 2025

#### **Bug Fixes**

* Various bug fixes

{% hint style="info" %}
Technical info (plugin versions):

* Engine: 4.254.0
* Visual Studio Code: 3.241.3
* JetBrains: 1.209.6
* Eclipse: 1.126.4
* Visual Studio: 1.194.4
  {% endhint %}

***

### v5.16.1

March 20, 2025

#### **Bug Fixes**

* Various bug fixes

***

### v5.16.0

March 19, 2025

#### Features and Improvements

* [**Context Scoping**](https://docs.tabnine.com/main/getting-started/getting-the-most-from-tabnine-chat/chat-context/context-scoping)**:**
  * Added the option to add remote folders and remote files to context scope.
  * Added the option to add terminal to context scope
* **IdP Sync**:
  * Added **Test Mode** to IdP Sync which allows simulation and preview of the expected impact on IdP sync (without actually applying the sync). This assures the IdP is set correctly to sync with Tabnine.
* **Enterprise (private installation)**:
  * Admins now have the option to configure an SMTP server with 0Auth (instead of user/password).
* **Provenance + Attribution**:
  * Turn on [**Censorship**](https://docs.tabnine.com/main/welcome/readme/protection/provenance-and-attribution#censorship) and keep your organization from using privileged code
* **Tabnine Chat**:
  * [**Apply buttons**](https://docs.tabnine.com/main/getting-started/quickstart/menus-and-icons#apply) redesign
  * Apply performance improvements
  * Chat indexing now supports Perforce
* **Switchable Models**:
  * We are adding <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-0dbc6c508c902dd575a9366c0762bea4f93e2442%2Ficon%3DClaude.svg?alt=media" alt="" data-size="line"> Claude 3.7 Sonnet as an available Chat [**AI model**](https://docs.tabnine.com/main/welcome/readme/ai-models) via the Tabnine endpoint.
  * <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-0dbc6c508c902dd575a9366c0762bea4f93e2442%2Ficon%3DClaude.svg?alt=media" alt="" data-size="line"> Claude 3.7 Sonnet is now the default model for new Enterprise SaaS customers \[via Tabnine endpoint], with GPT-4o enabled. A new toggle allows enabling or disabling all other models.
  * Added <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-11ea2353753655e5e498e3c2d1602647bedee838%2FGemini.png?alt=media" alt="" data-size="line"> Gemini 2.0 Flash as an available Chat AI model via Private endpoint. \[Supporting provider is <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-7d81bdf14a1abcf26f9fbb4b89313ad1ce39101f%2Fvertex-ai-logo-png_seeklogo-523075.png?alt=media" alt="" data-size="line"> GCP Vertex AI].
  * Enterprise customers can now use third-party AI models exclusively. Tabnine Protected is no longer mandatory and can be disabled. Admins can enable it manually via a new toggle in settings.

#### **Bug Fixes**

* <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-0920f6c4e65f036c6c903f4f4357aa6baf40aee1%2Fvs%20(1).webp?alt=media" alt="" data-size="line"> Visual Studio 2022 — Code Completion bug fixes
* Various bug fixes

***

### v5.15.7

March 13, 2025, 13:30

#### **Bug Fixes**

* Various bug fixes

***

### v5.15.6

March 13, 2025, 12:30

#### **Bug Fixes**

* Various bug fixes

***

### v5.15.5

March 6, 2025

#### Features

* Added <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-0dbc6c508c902dd575a9366c0762bea4f93e2442%2Ficon%3DClaude.svg?alt=media" alt="" data-size="line">Claude 3.7 Sonnet as an available Chat AI model via a Private endpoint connection.
  * \[Supporting providers are <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-e993ad944f9e1f2cf7153646832d154dcd0ff0e6%2Fbedrock-250-removebg-preview.86d95fc7f9a313f21091222ec7b63e1e30ea52ea.png?alt=media" alt="" data-size="line"> Amazon Bedrock and <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-7d81bdf14a1abcf26f9fbb4b89313ad1ce39101f%2Fvertex-ai-logo-png_seeklogo-523075.png?alt=media" alt="" data-size="line"> GCP Vertex AI]
* VDB run in Docker is disabled by default
* Support for <img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2Fgit-blob-ebdd5d13957cc3c32defdf704d0a96495b39e3c7%2Ficon%3DQwen.svg?alt=media" alt="" data-size="line"> Qwen2.5-32b

***

### v5.15.4

March 3, 2025

#### Features

* Better support for languages such as C and C++

Bug Fixes

* Various bug fixes

{% hint style="info" %}
Technical info (plugin versions):

* Engine 4.237.1
* Visual Studio Code: 3.232.0
* JetBrains: 1.201.1
* Eclipse: 1.124.0
* Visual Studio: 1.182.3
  {% endhint %}

***

### v5.15.3

February 27, 2025

#### Bug Fixes

* Various bug fixes

***

### v5.15.2

February 26, 2025

Features

* GCP Vertex AI is now available as an AI model provider, supporting the Claude series of AI models.

#### Bug Fixes

* Various bug fixes

***

### v5.15.1

February 19, 2025

#### Bug Fixes

* Various bug fixes

{% hint style="info" %}
Technical info (plugin versions):

* Engine: 4.237.1
* Visual Studio Code: 3.232.0
* JetBrains: 1.201.1
* Eclipse: 1.124.0
* Visual Studio: 1.182.1
  {% endhint %}

***

### v5.15.0

**February 16, 2025**

#### Features & Improvements

* **Admin UI**:
  * 'Workspace' setting page was renamed and is now called [**Personalization**](https://docs.tabnine.com/main/administering-tabnine/private-installation/managing-your-team/workspace-settings)**.**
* **Tabnine Chat**:
  * **Visual-to-Code: Allowed** for Tabnine Chat to use [image prompts](https://docs.tabnine.com/main/getting-started/getting-the-most-from-tabnine-chat/image-prompts)
  * [**Context Scoping**](https://docs.tabnine.com/main/getting-started/tabnine-chat/chat-context/context-scoping): Allowed for further specifying context
  * **UI:** Extensive UI updates
* **IdP Users Synchronization**:
  * Added option to deactivate all users when disabling IdP sync
* **Code Completion**:
  * **Faster Completions**: [Code completions](https://docs.tabnine.com/main/getting-started/getting-the-most-from-tabnines-code-completion) will be more responsive and quicker.
* **Enterprise**:
  * **Multiple allowed email domains**: Added the ability to configure multiple allowed email domains for accepting team invitations via link. This configuration can be set up with assistance from the Tabnine team.
* **CSV Usage Reports**: Enhanced `users_summary_daily.csv` with [additional data](https://docs.tabnine.com/main/managing-your-team/reporting/reporting#usage-data):
  * Accepted Lines of Code in code completions and chat.
  * User keystrokes

#### Bug Fixes

* No additional setup is required for integrating with Jira cloud on Tabnine Enterprise SaaS

{% hint style="info" %}
Technical info (plugin versions):

* Engine: 4.248.0
* Visual Studio Code: 3.232.0
* JetBrains: 1.201.1
* Eclipse: 1.124.0
* Visual Studio: 1.182.1
  {% endhint %}

***

### v5.14.3

**February 6, 2025**

#### Improvements

* Extended max number of tokens for OpenAI-compatible provider models

### v5.14.2

**January 30, 2025**

#### **Improvements**

* Added additional configuration options for the H100 private model.

#### Bug Fixes

* Added support for older Redis versions.

### v5.14.1

**January 22, 2025**

#### **Improvements**

* **Optimized experience for remote SSH setups**
* **CSV-based usage reports**: Improved Performance:
  * **'Teams' folder removed**: The 'teams' folder containing individual team reports has been removed from the `reports.zip` on the organizational level.
  * **Optional Configuration**: Added options to exclude the "Last 60 Days" and "Last 180 Days" time frames from the report for improved performance. By default, these time frames are included.

#### Bug Fixes

* **IntelliJ:** Fixed bugs when mentioning files mechanism

{% hint style="info" %}
Technical info (plugin versions):

* Engine: 4.228.0
* Visual Studio Code: 3.222.1
* JetBrains: 1.191.1
* Eclipse: 1.118.1
* Visual Studio: 1.175.2
  {% endhint %}

### v5.14.0

**January 15, 2025**

#### **Features and Improvements**

* **Switchable Models**: Allow customers to use the latest and greatest Claude model
* **IdP Users Synchronization:** Users who are added to Tabnine for the first time by the IdP sync will receive an email notifying them that they were added to the team.
* **@mentions**: Added indication for users when @mentions are unavailable.
* **Shared Custom Commands:** Users can now share their custom commands via their Source Control Management system.
* **Concise Chat**: The default setting for Chat answer response length is now set on 'Concise' mode

#### Bug Fixes

* Various bugs fixed

{% hint style="info" %}
Technical info (plugin versions):

* Engine: 4.228.0
* Visual Studio Code: 3.222.0
* JetBrains: 1.191.0
* Eclipse: 1.118.0
* Visual Studio: 1.175.1
  {% endhint %}

***

### **v5.13.1**

**January 2, 2025**

#### **Features and improvements**

* **IdP Users Synchronization:** Enables organizations to provision and de-provision Tabnine users based on their IdP status. This is implemented using the **SCIM** users protocol.
* **Email Visibility in Usage Reports:** Adds a setting to hide or show user email addresses in usage reports.
* **Streamlined Sign-In for Private Installations:** The sign-in screen now bypasses the email routing step in private installations.

### **v5.13.0**

**December 23, 2024**

#### **Features and improvements**

* **Custom System Behavior:** Users can now provide Tabnine's AI chat assistance instruction to tailor its behavior to their specific needs.
* Propagate configuration and data directories from the IDE to the Tabnine plugin and engine.

#### Connection (Global RAG)

* Added support for connecting to remote repositories via HTTPS using a personal access token.
* Included the team name in the connection section for better organization and visibility.

**Reporting** **Updates**

* Removed deprecated CSV-based usage reports. Only V2 reports are now supported, as V1 reports (deprecated since version 5.7.0) have been fully retired.

{% hint style="info" %}
Technical info (plugin versions):

* Engine: 4.215.0
* Visual Studio Code: 3.205.0
* JetBrains: 1.178.0
* Eclipse: 1.108.0
* Visual Studio: 1.160.2
  {% endhint %}

***

### **v5.12.3**

**December 9, 2024**

#### **Features and improvements**

* **Private installations:**
  * Added support for L40 GPUs.

### **v5.12.2**

**December 6, 2024**

#### **Features and improvements**

* **Chat switchable models:**
  * Team-level model configuration is now available.

### **v5.12.1**

**December 3, 2024**

#### **Features and improvements**

* **System Verilog:**
  * Code completion complete statements and blocks fix.
  * Fixed indentation issues.

### **v5.12.0**

**November 22, 2024**

#### **Features and improvements**

* **Integration with Atlassian Jira Cloud:** [Learn more](https://docs.tabnine.com/main/welcome/readme/integrations/atlassian-jira#setting-up-the-integration-for-jira-cloud-tabnine-enterprise-private-installation)
* **Personalization:**
  * **Connection (global RAG):** Added the option to set link patterns for source code navigation in references from connected repositories (specifically useful for self-hosted Git providers).
  * **Context (local RAG):** Added support for multi-git-repo project structures.
* **Chat improvements**
  * Added keybinding to open Chat (VS Code)
  * Added Inline Actions support for @mentions on JB.
  * Added support for non-Latin languages.
  * Redesigned the "New Conversation" button for a cleaner appearance.
* **Web App/Admin Console updates**
  * **Login flow:** Introduced an additional login screen to determine the organization’s login method: SSO or user password login.
  * **License-controlled features:** Advanced features (switchable models, Jira connection, and connection) are now controlled by the license.
  * **Instance Admin** (implicit role):
    * A new, implicit role called Instance Admin has been introduced. This role is automatically assigned to the initial seed user of the installation and is one of the account [admins](https://docs.tabnine.com/main/managing-your-team/roles-in-an-enterprise#admin).
    * To transfer the Instance Admin role to another admin, please contact <support@tabnine.com>.
    * Instance Admins have exclusive authority to:
      * Configure and modify system-wide [SMTP](https://docs.tabnine.com/main/managing-your-team/settings/email-settings#configure-smtp) settings.
      * Manage core system configuration parameters.
    * [UI Reports](https://docs.tabnine.com/main/managing-your-team/reporting#visual-usage-reports): Now include Inline Actions in SH Analytics.

#### Bug fixes:

* Fixed a broken link to Eclipse instructions.
* Resolved a bug in CSV email reports when users are unmasked.
* Improved VDB RAM consumption handling on Windows.

{% hint style="info" %}
Technical info (plugin versions):

* Engine: 4.205.0
* Visual Studio Code: 3.190.10
* JetBrains: 1.163.1
* Eclipse: 1.99.0
* Visual Studio 2022: 1.151.1
  {% endhint %}

***

### **v5.11.5**

**Nov 11, 2024**

#### Bug Fixes:

* Provenance + Attribution connectivity and installation issues.

***

### **v5.11.4**

**Nov 5, 2024**

#### Features:

* **Provenance + Attribution:** \[Private preview] Tabnine Chat can provide source tracing and attribution for six major languages: C, C++, Rust, JavaScript, TypeScript, and Python.

***

### **v5.11.3**

**October 25, 2024**

#### Bug fixes:

* Handled name hallucinations in Test Agent.

***

### **v5.11.2**

**October 24, 2024**

#### Bug fixes:

* Resolved connectivity issues with the Atlassian Jira integration.

***

### **v5.11.1**

**October 22, 2024**

#### Bug fixes:

* Changed the default value of the admin base URL to address configuration issues.

{% hint style="info" %}
Technical info (plugin versions):

* Engine: 4.198.0
* Visual Studio Code: 3.127.1
* JetBrains: 1.147.1
* Eclipse: 1.84.1
* Visual Studio 2022: 1.136.3
  {% endhint %}

***

### **v5.11.0**

**October 21, 2024**

#### **Features**

* **Integration with Atlassian Jira Data Center:** Added support for AI agents to implement and validate Jira issues, enabling code generation and validation based on Jira requirements with a single click. [Learn more](https://docs.tabnine.com/main/welcome/readme/integrations/atlassian-jira#supported-matrix)
* **Inline Actions Enhancements:** Improved the functionality and user experience for performing actions directly within the interface.
* **CSV Usage Reports:** Introduced [`teams_summary.csv`](https://docs.tabnine.com/main/managing-your-team/reporting/reporting#teams_summary.csv) providing a detailed per-team summary to help with usage analytics.
* **Enhanced Cluster Monitoring and Alerting:** Upgrades to improve system health visibility and proactive issue resolution.

#### Bug Fixes:

* Resolved an issue in the update mechanism.
* Fixed an edge case where CSV reports could be generated without data.

***

### **v5.10.2**

**October 10, 2024**

#### Bug fixing

* Fix empty CSV files in scheduled email reports

### **v5.10.1**

**September 30, 2024**

#### **Features**

* Multi-Step Retrieval-Augmented Generation (RAG) for chat

### **v5.10.0**

**September 18, 2024**

#### **Features**

* [**Inline actions**](https://docs.tabnine.com/main/getting-started/inline-actions)**:** Now available in both VS Code and JetBrains IDEs.
* **Tabnine chat - "New File"**: Added the option to insert a code suggestion directly into a new file.
* **CSV Usage Reports:** Enhanced `users_summary.csv` with additional data, including:

  * Accepted Lines of Code in code completions and chat.
  * Chat Consumption Rate
  * More usage time frames: Last 60, 90, and 180 days.

  [Learn more](https://docs.tabnine.com/main/managing-your-team/reporting/reporting#usage-data)

#### Bug fixing, including:

* Fixed an issue where long team names were not displayed correctly.
* Resolved a problem where chat model names appeared as "Unspecified model" in reports.

{% hint style="info" %}
Technical info (plugin versions):

* Engine: 4.186.0
* Visual Studio Code: 3.1540.0
* JetBrains: 1.133.1
* Eclipse: 1.73.0
* Visual Studio 2022: 1.128.1
  {% endhint %}

### **v5.9.0**

**August 16, 2024**

#### **Features**

* Custom onboarding page and support email are now included in team members' welcome emails.
* Support for Bedrock/Sonnet internal endpoints was added as an option for the chat model.

#### Bug fixing

* Reduce chat response error rates
* Various other bug fixes

{% hint style="info" %}
Technical info (plugin versions):

* Engine: 4.186.0
* Visual Studio Code: 3.140.0
* JetBrains: 1.121.0
* Eclipse: 1.64.0
* Visual Studio 2022: 1.118.1
  {% endhint %}

### **v5.8.2**

**July 24, 2024**

#### Fixes and changes

* Fixed a bug in a specific GPU configuration template.

### **v5.8.1**

**July 23, 2024**

#### Fixes and changes

* Fixed a bug in the connection for global code awareness feature.

### **v5.8.0**

**July 19, 2024**

#### **Features**

* [**Code Explorer**](https://docs.tabnine.com/main/administering-tabnine/broken-reference) **(previously the Onboarding Agent):** Helps developers step into new code, whether they’re new to your organization or just new to the codebase, and helps them explore the unfamiliar code and hit the ground running, writing code faster than ever before.
* **New Role: Account Manager:** A Manager[^1] can manage and monitor teams and users but cannot configure the account settings. [Learn more](https://docs.tabnine.com/main/managing-your-team/roles-in-an-enterprise#manager)
* **Default chat model:** Admins can [set the default chat mode](https://docs.tabnine.com/main/managing-your-team/settings/models-settings#setting-the-default-chat-model)l of the account.
* **New usage reports:**
  * [Total accepted lines of code per month](https://docs.tabnine.com/main/managing-your-team/reporting#id-2-monthly-accepted-lines-of-code-trend-chart) (for code completions and chat)
  * [Useful chat interaction by consumption type](https://docs.tabnine.com/main/managing-your-team/reporting#id-3-useful-chat-interactions-by-consumption-type)
  * [Account utilization](https://docs.tabnine.com/main/managing-your-team/reporting#account-utilization-history) has moved under Analytics
  * [user\_summary\_daily.csv](https://docs.tabnine.com/main/managing-your-team/reporting/reporting#users_summary_daily.csv): A new CSV report per user, per day (for the last 30 days)
* **Use @mentions in custom Commands:** Use @mentions within [custom commands](https://docs.tabnine.com/main/getting-started/tabnine-chat/interact#user-defined-quick-actions) for the first time. This lets you create custom commands based on your own templates or sample code.

#### Fixes and changes

* Fixed different bugs in @mentions
* Fixed bug in Document CodeLens
* Search user by email in the Tannine console is now case-insensitive

{% hint style="info" %}
Technical info (plugin versions):

* Engine: 4.178.1
* Visual Studio Code: 3.127.1
* JetBrains: 1.110.1
* Eclipse: 1.59.0
* Visual Studio 2022: 1.110.4
  {% endhint %}

***

### **v5.7.1**

**June 25, 2024**

#### **Features**

* Tabnine Chat Command Button shortcuts: Find button shortcuts for the Tabnine Chat text commands `@` and `/` right below the chat input field.
* Enable copy-paste for **@mentions:** From within the Tabnine Chat, you can now copy any `@symbol` string and paste it into the Tabnine Chat input to add the reference to your message.
* IntelliJ support for **@mention** of a file: in addition to @mention of symbols, you can @mention entire files in IntelliJ.

#### Fixes and changes

* Tabnine Chat now correctly uses @mentions of symbols that are not in your open file.

### **v5.7.0**

**June 21, 2024**

#### **Features**

* Updated usage reports with new content, including:
  * [Overview reports](https://docs.tabnine.com/main/managing-your-team/reporting#overview-page): A high-level usage overview and activity trend charts.
  * [User Management reports](https://docs.tabnine.com/main/managing-your-team/reporting#user-management-report): Provides a high-level overview and offers insights into how many users have successfully onboarded Tabnine.
  * [CSV-based reports version 2.0](https://docs.tabnine.com/main/managing-your-team/reporting/reporting#reports-in-version-5.7.0-or-higher): Includes a textual summary overview and a per-user summary CSV. (Old CSV-based reports are now deprecated but not yet removed.)
* Anonymize deactivated user: The Admin can [delete the PII data of deactivated users](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/deleting-pii-data-of-a-deactivated-user) who have left the organization.

#### Fixes and changes

* General bug fixes
* Fixed frequent indexing failures
* Fixed a bug in suggestion delay time (JetBrains plugin)

***

### **v5.6.1**

**June 3, 2024**

#### Fixes

* Fix issue where pods fail to start in certain setups

### **v5.6.0**

**May 23, 2024**

#### **Features**

* The new [Tabnine Protected Chat Model (Version 2)](https://github.com/codota/docs/blob/main/main/administering-tabnine/broken-reference/README.md) is now the default model, replacing the previous preview version. This update is automatic and requires no action from users.
* License settings and account utilization history [Learn more](https://docs.tabnine.com/main/administering-tabnine/managing-your-team/settings/license-settings)
* Team admin can see the users who are not assigned to a team [Learn more](https://docs.tabnine.com/main/managing-your-team/tabnine-teams#viewing-users-who-are-not-assigned-to-a-team)
* Improved audit logs [Learn more](https://github.com/codota/docs/blob/main/main/administering-tabnine/broken-reference/README.md)

#### Fixes and changes

* CSV report: Changed the Registered/Deactivated field in user\_details.csv [Learn more](https://docs.tabnine.com/main/managing-your-team/reporting#id-2-user-team-status-report-user_details.csv)
* Increase chat answer size to avoid truncated responses
* Fix some workspace indexing bugs (limit workspace indexing; indexing some files takes too long)

### **v5.5.1, v5.5.2**

**April 30, 2024**

* Fixing bugs

### **v5.5.0**

**April 25, 2024**

* Fixing bugs
* Preparing for design partners.

### **v5.4.1**

**April 21, 2024**

#### Fix

* Fix the issue where Tabnine Chat unintentionally taking focus away from Visual Studio Code.

### **v5.4.0**

**April 18, 2024**

#### Features

* Added options to [view](https://docs.tabnine.com/main/managing-your-team/inviting-users-to-your-team#viewing-invited-users) and [manage](https://docs.tabnine.com/main/managing-your-team/inviting-users-to-your-team#resend-an-invitation-or-revoke-an-existing-invitations) pending invitations. Invited users are also now included in the [CSV-based reports](https://docs.tabnine.com/main/managing-your-team/reporting#id-1-users-onboarding-status-all_times_users_onboarding_status.csv).
* [Customize users' help resources](https://docs.tabnine.com/main/managing-your-team/settings/general-settings#customize-users-help-resources-help-landing-page-and-support-email) (help landing page and support email) were added.
* [Single sign-on (SSO) configuration](https://docs.tabnine.com/main/managing-your-team/settings/general-settings#configuring-single-sign-on-sso) was moved to the admin console.
* [Email verification](https://docs.tabnine.com/main/managing-your-team/settings/email-settings#email-verification) toggle changes now take effect immediately.
* Password policies were hardened.

***

### **v5.3.3**

**April 9, 2024**

**Fix**

Better handling for NFS files.

***

### **v5.3.2**

**March 28, 2024**

#### **Fix**

Tabnine Chat app doesn't load due to race condition.

***

### **v5.3.1**

March 21, 2024

#### Additional features <a href="#additional-features" id="additional-features"></a>

* **We introduced a new settings section for Tabnine’s license key.**\
  Moved from the installation flow to the onboarding flow to avoid human errors, improve ease of use and flexibility, and improve the customer onboarding experience. Added notifications for license date expiration and seat limit exceeded.
* **The email invitation expiration time has been increased to 30 days from 14 days.**\
  We increased the expiration time to allow more time for onboarding. We also made it possible to custom change this value (currently only through values.yaml).
* **We made a few Chat updates:**

  1\. Added the option to include workspace in context and re-ask the last question.

  2\. Chat now proposes follow-up questions.

***

### **v5.3.0**

March 13, 2024

**Introduced a new settings section for Tabnine’s license key.**

#### Additional features <a href="#additional-features" id="additional-features"></a>

* Tabnine web application now has its version indication.
* **Email verification settings for invited users:**\
  This feature allows admins to turn on email verification for invitations from the web console, making the onboarding process more secure.
* **Email SMTP settings:**\
  This feature allows easier onboarding maintenance and administration of the customer environment. Customers can now add and edit their email SMTP server.
* **Self-registration onboarding:**\
  This feature allows users to self-register in the system without invitations and join a default team.
* **Context through local code awareness (code completions):**

  This feature gives much better results for code completion.

**Fixes**

* Workspace awareness bug fixes for Windows
* Sign-up issues
* Users onboarding analytics issues
* Various UI fixes
* Pagination bug in the Users tab

***

### **v5.2.2**

February 21, 2024

#### Features

* Eclipse plugin updates, including Show diff, Mentions, Snooze code completions, and more
* Completions model with reduced image size

#### Fixes

* Fix the bug in signing in with an auth token is not working
* Reporting date skewing (due to browser locale date casting)

### **v5.2.0**

February 18, 2024

#### Announcing new, more highly personalized AI coding recommendations in Tabnine

This release includes another leap forward in the performance and capability of the Tabnine AI coding assistant:[ highly personalized recommendations](https://docs.tabnine.com/main/welcome/readme/personalization) for every developer through contextual awareness. Tabnine can deliver a more precise and personalized experience across all product features. Context awareness provides the subtle nuances that make a developer and organization unique. Tabnine achieves this context awareness in two ways:

* **Context through local code awareness:** Tabnine can access locally available data in a developer’s IDE to provide more accurate and relevant results. Tabnine automatically identifies the relevant information and uses it as context to provide personalized results. Tabnine administrators can enable this feature for their organization in the admin console settings.
* **Connection to your software repository for global code awareness:** Tabnine administrators can connect Tabnine to their organization’s code repositories, significantly increasing the context Tabnine uses across product features. This capability is currently in Private Preview for Tabnine Enterprise customers with on-premises or VPC deployments.

**Mentions in Chat**: Developers can help Tabnine focus on specific elements in the workspace through [@mentions](https://docs.tabnine.com/main/getting-started/tabnine-chat/interact#mentions) (using the @ symbol to tag unopened files, classes, or methods in Tabnine Chat). This feature is supported across Visual Studio Code, JetBrains IDEs, and Visual Studio 2022.

**Improved test generation:** Test generation now considers the structure of actual test files and identifies similar existing tests more effectively.

#### Additional features

* **New visual dashboard:** Keep track of Tabnine's performance with a new visual dashboard tailored for team usage.
* **Accepting partial completions:** Users can now partially accept completions on a line-by-line basis. (This feature is supported in Visual Studio Code and JetBrains IDEs.)
* **JetBrains extension**
  * Expanded [Code Lens ](https://docs.tabnine.com/main/getting-started/tabnine-chat/interact#option-3-codelens-method-scope)support: Code Lens now supports GO, C/CPP, and C# languages.
* **Visual Studio 2022 extension**
  * We upgraded the Chat extension to enable the latest features, including better context, local repository awareness, chat code mentioning, and rich diff-view for applying suggested snippets.
  * New status bar item and [snooze button](https://docs.tabnine.com/main/getting-started/code-completion/pause-snooze#jetbrains-ides-eclipse-and-visual-studio-2022)
  * Introduced [Code Lens](https://docs.tabnine.com/main/getting-started/tabnine-chat/interact#option-3-codelens-method-scope) functionality
  * Enhanced proxy support: Better connectivity with extended proxy support

#### **Fixes**

* CSV reporting bug fixes
* Minor chat bug fixes and improvements

***

### **v5.1.1**

February 11, 2024

#### **Fixes**

* Under-the-hood bug fixes.

***

### **v5.1.0**

January 30, 2024

*<mark style="background-color:yellow;">**Attention: 5.1.0 brings breaking changes. please refer to the**</mark>* [*<mark style="background-color:yellow;">**upgrade guide**</mark>*](https://github.com/codota/docs/blob/main/main/administering-tabnine/broken-reference/README.md) *<mark style="background-color:yellow;">**before proceeding with upgrade.**</mark>*

#### **Fixes**

* Request and response size limits have been increased to accommodate large SAML responses.

#### **Features**

* Self Registration Mode: Users now have the option to sign up for the system and automatically join the default team. This feature can be toggled on or off based on preferences.
* The email verification process for user/password mode is now customizable. It can be enabled or disabled as needed.
* Administrators can now change their users’ passwords or send password reset links when operating in user/password mode.
* SMTP configuration is no longer a mandatory requirement during installation, streamlining the setup process.

***

### **v4.12.3**

#### Tabnine's private installation's release notes

### **v4.12.5**

January 22, 2024

#### **Fixes**

* Bug fix networkpolicy templating

***

### **v4.12.4**

January 15, 2024

#### **Fixes**

* Bug fix in loading fine tuned model from external volume

***

### **v4.12.3**

January 3, 2024\
\
**Fixes**

* Minor bug fixes and improvements regarding chat behavior in VSCode plugin.

**Features**

* VSCode chat now delivers a single, concise response.
* Reduced chat response latency in VSCode plugin
* Improved chat monitoring via Tabnine's metrics dashboard provides valuable insights into chat performance and usage.

***

### **v4.12.2**

December 20, 2023\
\
**Fixes:**

* bug fixes in installation process.

***

### **v4.12.1**

December 19, 2023\
\
**Fixes**

* minor bug fixes in installation process and chat responses.

**Features**

* More focused and precise chat responses.
* Introduced Code Lens functionality for JetBrains IDEs.
* Introducing the capability to schedule periodic CSV reports via email, allowing users to customize timing and recipients according to their preferences.

***

### **v4.12.0**

#### December 7, 2023 **Fixes**

* Fixed an issue with trailing slashes in proxy definitions.
* Fixed an issue reading configuration files in WSL environments.
* Fixed a bug causing formatting issues in chat transcript (.tsx) files.
* Improved synchronization between the binary and plugin for login and feature availability flows in JetBrains and VScode plugins.
* Enhanced code completion suggestions in VScode by considering context from nearby files.
* Improved markdown formatting in chat conversations.
* Refined error handling for situations with empty responses.

#### **Features**

* Introduced code lens functionality for VScode.
* Chat responses now prioritize information directly relevant to your question, minimizing irrelevant details and distractions.
* Improved free text responses by leveraging context from nearby files.
* Added a References box to chat responses, highlighting relevant code locations related to provided answers.
* Implemented a non-strict invitation mode that allows for SSO email mismatches from invitations (configurable in settings).
* Introduced Authentication token support to bypass login issues.
* Chat now requires team membership for authorization.
* Added a new report displaying user details such as team membership, activation status, identity validation, etc.
* Enhanced reports with chat usage statistics.

***

### v4.11.3

November 22, 2023

**Fixes**

* Addressed minor issues and made enhancements to tabnine chat models and deployments.

***

### v4.11.2

November 20, 2023

**Features**

* Enhanced flexibility and expanded support for various deployment types and hardware configurations.

***

### v4.11.1

November 9, 2023

**Features**

* Introduced a new "Current Team" column in user reports, providing enhanced visibility into team affiliations.

**Fixes**

* Enhanced the precision of chat diffs functionality for Windows users, resulting in clearer and more readable code fixes.
* Resolved a bug preventing login when switching between Single Sign-On (SSO) and built-in authentication (user/password) modes, and vice versa.
* Resolved an infrequent issue where users were mistakenly displayed a "Not part of team" message after joining a team.
* Improved user guidance by clearly indicating the requirement to sign in to access the chat.

***

### v4.11.0

November 7, 2023

**Features**

* Introduced a code "diff-view" for the fix\_code chat action in Visual Studio Code and JetBrains.
* Enhanced communication for cases where files are empty, or context lacking.
* Introducing a "Snooze" button to temporarily disable code suggestions in JetBrains and Visual Studio Code.
* Added the ability to edit team names via the admin console.
* Provided an option to include identified users in reports, enhancing user data insights.

**Fixes**

* Enhanced and fixed issues regarding SSH & WSL setups in Visual Studio Code to improve the onboarding experience.
* Resolved an issue causing faulty login indication in Visual Studio Code.
* Fixed a bug that was causing intermittent freezing in IntelliJ IDEA for some users.
* Addressed a 'chat intent' reporting issue, ensuring more accurate reporting.

***

### v4.10.3

October 30, 2023

**Features**

* Introducing new dashboards for monitoring system metrics and service monitoring

**Fixes**

* Addressed and fixed issues in tabnine's monitoring setup.

***

### v4.10.2

October 26, 2023

**Fixes**

* Improved email pattern validation when assigning users to a team.

***

### v4.10.1

October 26, 2023

**Fixes**

* Accelerated installation time, resulting in faster setup.
* Reduced image size, optimizing resource usage.

***

### v4.10.0

October 25, 2023

**Features**

* Extended support for routing issues in VScode and JetBrains, including advanced proxy configurations and improved handling of certificates.
* Enhanced suggestion context including open files and tabs for more profound and precise completions.
* Improved the “Fix Code” chat action for better code correction, providing a more efficient and streamlined development experience.
* Extended reporting capabilities, providing valuable insights into system performance.
  * Chat usage is now integrated throughout the reports, facilitating communication and collaboration.
  * Revised onboarding report for a smoother and more informative onboarding process.
* Added a built-in option for logs aggregation inside the Tabnine server, simplifying troubleshooting and monitoring.

**Fixes**

1. Fixed a bug causing the downgrade of privileges when onboarding a new team through an invitation link or by admin assignment.

***

### v4.9.7

October 18, 2023

**Fixes**

* Chat model improvements and fixes.

***

### v4.9.6

October 17, 2023

**Fixes**

* Fixing SAML issue to allow different unique identifier format policy

***

### v4.9.5

October 3, 2023

**Fixes**

* Fixing an issue preventing invitation emails from being sent due to missing resource.

***

### v4.9.4

October 3, 2023

**Fixes**

* Fixing an issue related to unsecured SMTP connection configuration when using unauthenticated connections

***

### v4.9.3

September 26, 2023

**Fixes**

* Fixing Single Sign-On (SSO) SAML authentication issue related to Azure Active Directory specific authentication context handling.\
  For more info: [see here](https://learn.microsoft.com/en-us/troubleshoot/azure/active-directory/error-code-aadsts75011-auth-method-mismatch) in MicroSoft official documentation.

***

### v4.9.2

September 21, 2023

**Fixes**

* Improved Tabnine service deployment strategy for enhanced performance.

***

### v4.9.1

September 20, 2023

**Fixes**

* Resolved bug related to unsecured SMTP connection configuration.

***

### v4.9.0

September 19, 2023

**Features**

* Introducing the new Tabnine Visual Studio 2022 plugin for self hosted environments, with full fledged functionality.
* Improved Single Sign-On (SSO) features to facilitate SAML authentication context configuration.
* Invitations are now obsolete: When adding a user, the admin chooses the team to which the user will be added.
  * Once added, users can signup directly (after downloading the plugin), with no need to click the email link.
  * Email notices were update according to new methodology.
* Enhance chat context for more accurate and detailed chat responses.
* New chat command: `/workspace` ask any question related to your current open workspace.
* Incorporation of a Toxicity Filter to Mitigate the Use of Offensive Language.

**Fixes**

* Fixes and improvements to existing chat commands `/fix-code`, `/explain-code` and `/generate-test-for-code`.
* Fixed an issue in JetBrains plugins causing RemoteUrl popup not to persist the url input to the settings.
* Fixed an issue of a break in the onboarding flow using invite link, where user is required to click on the invite link again in case he had to signup while onboarding ('You are not part of any team' message).

***

### v4.8.2

September 11, 2023

**Features**

* Allow disabling the SMTP security upgrade functionality on demand
* Fix random cases in which IntelliJ throws exception in while initializing due to race condition on userstate listener registration.

***

### v4.7.10

September 11, 2023

**Features**

* Allow disabling the SMTP security upgrade functionality on demand

***

### v4.7.9

September 11, 2023

#### Features

* Allow disabling the SMTP security upgrade functionality on demand

#### Fixes

* Fix random cases in which IntelliJ throws exception in while initializing due to race condition on userstate listener registration.

***

### v4.8.1

September 7, 2023

#### Fixes

* bug in Tabnine Chat on MacOS/Jetbrains IDEs causing IDE freeze when inserting chat suggested code.
* Timeout errors during signup prevent successful login in slow connections.

### v4.7.8

September 7, 2023

#### Fixes

* bug in Tabnine Chat on MacOS/Jetbrains IDEs causing IDE freeze when inserting chat suggested code.
* Timeout errors during signup prevent successful login in slow connections.

***

### v4.7.7

September 5, 2023

#### Fixes

* Added missing security headers on the root path

***

### v4.8.0

August 29, 2023

#### Features

* Deactivation of Organization Members by Admins:
  * Admins can now deactivate organization members.
  * Once deactivated, users will be automatically signed out from all devices.
  * Deactivated users won’t be able to sign in unless they are re-activated by an admin.
* Updates to Team Assignments:
  * The option for users to select their own teams has been discontinued.
  * Organizational administrators will now manage user team assignments. This can be done either through email invitations or using team invite link.

***

### v4.7.6

August 25, 2023

#### Fixes

* We have updated VSCode plugin startup process validation, to allow running in a low performance environments (mainly due to network issues)
* Fixed a bug in VSCode plugin during the installation process, that caused 'Tabnine Enterprise' in the status to indicate an error (red color) until the plugin is installed

***

### v4.7.5

#### Features

* Enhance chat with local context

#### Fixes

* Web App UI fixes

***

### v4.7.4

#### Fixes

* Fixed an issue that emerged as a result of breaking changes in the JetBrains Plugins SDK within the JetBrains 2023.2 release.

***

### v4.7.3

#### Features

* Adding support for email clients not supporting gradients in email body.

#### Fixes

* Fix Flickering in UI in app login screen

***

### v4.7.2

#### Features

* Invitation email change (layout + removing <support@tabnine.com> reference )

#### Security

* Harden cluster network policies for improved security

#### Fixes

* Fix JetBrains plugin custom repository issue, causing issues updating the plugin

***

### v4.7.0

#### Features

* Introducing self hosted chat(beta)
* Chat utility reporting to reflect activation usage and retention.
* Allows users to create the persistence layer locally within the Tabnine cluster.

#### Security

* Harden cluster network policies for improved security

#### Fixes

* Added recovery mechanism for cluster inter-module communication.

***

### v4.6.0

#### Features

* Enabled local user management (within the customer network), enhancing user authorization and security.
* Support for multiple teams for better collaboration and management.
* New admin console
* Allow logs and metrics write to customer services.
* Introducing local reporting functionality, including onboarding status, usage reports
* Making telemetry to tabnine optional and off by default for better monitoring and customer reporting.
* Full support for Eclipse, VSCode, and JetBrains IDE family, providing a secured and seamless experience across popular integrated development environments.

#### Security

* enhancing security and access control by Introducing authentication using built-in authentication (username & password) and SAML2/SSO

#### Fixes

* Enhanced plugin support for better onboarding.\\

[^1]: [Avichay Libeskind-Mulyan](https://app.gitbook.com/u/6G8rgj5XEdPYrwKgh1IhfUdpNfh2 "mention"), 'account manager' instead of 'manager'
