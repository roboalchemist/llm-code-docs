# Ignore files, folders, and code

Source: https://semgrep.dev/docs/ignoring-files-folders-code

- [](/docs/)- Set up and deploy scans- Core deployment- Customize core deployment- Ignore files, folders, and code- Semgrep Code**On this page- [Semgrep AppSec Platform](/docs/tags/semgrep-app-sec-platform)Ignore files, folders, and code
This document describes two types of ignore operations:

- **Ignoring as exclusion.** Exclude or skip specific **files and folders** from the scope of Semgrep scans in your repository or working directory. Ignoring in this context means that Semgrep does not generate findings for the ignored files and folders.
- **Ignoring as triage action**. Ignore specific parts of code that would have generated a finding. Ignoring in this context means that Semgrep generates a finding record and automatically triages it as **Ignored**, a triage state.

All Semgrep environments (CLI, CI, and Semgrep AppSec Platform) adhere to user-defined or Semgrep-defined ignore patterns.

## Reference summary[​](#reference-summary)
MethodUsageTo ignore blocks of code: Add a `nosemgrep` annotationCreate a comment, followed by `nosemgrep`, at the first line or preceding line of the pattern match. This generates a finding that is automatically ignored. For example:` // nosemgrep`      `// nosemgrep: rule-id`  `# nosemgrep`For Semgrep AppSec Platform users: - Ignore files and folders through the use of Semgrep AppSec Platform&#x27;s **Project or Global ignores**- Override the implicit ignorelist through the use of a `.semgrepignore` file.Navigate to **Projects &gt; PROJECT_NAME &gt; Details &gt; Settings &gt; Path ignores**. *For Semgrep Community Edition (CE) users:Ignore files and folders through a `.semgrepignore` fileCreate a `.semgrepignore` file in your **repository&#x27;s root directory** or your **project&#x27;s working directory** and add patterns for files and folders there. Patterns follow `.gitignore` syntax with some caveats. See [Defining ignored files and folders in `.semgrepignore`](#define-ignored-files-and-folders-in-semgrepignore).
## Understand Semgrep defaults[​](#understand-semgrep-defaults)
Without user customization, Semgrep refers to the following to define ignored files and folders:

- Semgrep&#x27;s default `.semgrepignore` file
- Your repository&#x27;s `.gitignore` file (if it exists)
- For Semgrep AppSec Platform users: each project (repository or subfolder in monorepo) in Semgrep has a list of ignored files and folders in its project details page.

In the absence of a user-generated `.semgrepignore`, Semgrep refers to [its repository&#x27;s default template](https://github.com/semgrep/semgrep/blob/develop/cli/src/semgrep/templates/.semgrepignore):

`# Administrative folder or file used by popular version control systems.git.svn.hg_darcsCVS# Paths to files and folders that are typically large and ignorablebuild/vendor/dist/*.min.js.env/.tox/# Package managersnode_modules/.npm/.yarn/.venv/_opam/_build/_cargo/# Note that PHP composer uses vendor/ and C++ conan uses build/# .venv is used both by Go and Python.# Common test pathstest/tests/testsuite/*_test.go`
## Override defaults[​](#override-defaults)
The default `.semgrepignore` file causes Semgrep to skip these folders:

- `/tests`, `/test`
- `/vendors`

To include these folders:

- Create a `.semgrepignore` file at the repository root without those paths.
- For Platform users: remove the folders from the project ignore list in **Projects &gt; PROJECT_NAME &gt; Details page &gt; Settings &gt; Path ignores &gt; Code (SAST) &amp; Supply Chain (SCA)**.

## Files, folders, and code beyond Semgrep&#x27;s scope[​](#files-folders-and-code-beyond-semgreps-scope)
There are files that Semgrep ignores even without `.semgrepignore`:

- Large files (maximum file size defaults to 1 MB)
- Binary files
- Unknown file extensions (file extensions not matched with any supported programming language)

Large files and unknown file extensions are included or excluded through command line flags (See [CLI reference](/docs/cli-reference)). Binary files are never scanned.

This document defines **files, folders and code** as those that are **relevant to a Semgrep scan**. For example, `.jpg` files are not a part of Semgrep&#x27;s scope and therefore are not part of the scope of this document.

## Customize ignore behavior[​](#customize-ignore-behavior)
Semgrep provides several methods to customize ignore behavior. Refer to the following table to see which method suits your goal:

GoalMethodTo ignore custom files and folders each time you run a Code or Supply Chain scan.Add these files to your `.semgrepignore` file or [define them through Semgrep AppSec Platform](#define-ignored-files-and-folders-in-semgrep-appsec-platform).To ignore specific code blocks each time you run a scan.Create a comment with the word `nosemgrep`.To ignore files or folders for a particular scan.Run Semgrep with the flag `--exclude` followed by the pattern or file to be excluded. See [CLI reference](/docs/cli-reference).To include files or folders for a particular scan.Run Semgrep with the flag `--include` followed by the pattern or file to be included. Any file that isn&#x27;t matched is excluded. See CLI reference. When including a pattern from a `.gitignore` or `.semgrepignore` file, `--include` does not override either, resulting in the file&#x27;s exclusion.To scan all files within Semgrep&#x27;s scope each time you run Semgrep (only files in `.git` are ignored).Create an empty `.semgrepignore` file in your repository root directory, and for `semgrep ci` scans, [remove any entries listed in your **Path Ignores** list](#define-ignored-files-and-folders-in-semgrep-appsec-platform) in Semgrep AppSec Platform.To include files or folders defined within a `.gitignore` for a particular scan.Run Semgrep with the flag `--no-git-ignore`.To ignore files or folders for a particular rule.Edit the rule to set the `paths` key with one or more patterns. See [Rule syntax](/docs/writing-rules/rule-syntax#paths).
## Define ignored files and folders in `.semgrepignore`[​](#define-ignored-files-and-folders-in-semgrepignore)
Configure a `.semgrepignore` file to ignore files and folders each time you run a Code or Supply Chain scan.

cautionFor Secrets scans, Semgrep ignores both the default and user-defined `.semgrepignore` files. You can still configure secrets-specific ignores in [Semgrep AppSec Platform](#define-ignored-files-and-folders-in-semgrep-appsec-platform) or use the `--exclude` flag to ignore files or folders for a particular scan.

`.semgrepignore` syntax mirrors `.gitignore` syntax, with the following modifications:

- &quot;Character range&quot; patterns (lines including a collection of characters inside brackets) are unsupported.
- An `:include ...` directive is added, which allows another file to be included in the ignore pattern list; typically this included file would be the project `.gitignore`. No attempt at cycle detection is made.
- Any line that begins with a colon, but not `:include`, raises an error.
- `\:` is added to escape leading colons.

Unsupported patterns are silently removed from the pattern list (this is done so that `.gitignore` files may be included without raising errors). The removal is logged.

For a description of `.gitignore` syntax, see [.gitignore documentation](https://git-scm.com/docs/gitignore).

## Define ignored files and folders in Semgrep AppSec Platform[​](#define-ignored-files-and-folders-in-semgrep-appsec-platform)
Another method for users to define ignore patterns is through Semgrep AppSec Platform. These patterns follow the same syntax as `.semgrepignore` in the preceding section. You can either define patterns at the individual-project level or at the organization level, so they&#x27;re applied to all projects owned by that organization.

Ignoring files and folders through this method is **additive**.

Adding items to Semgrep AppSec Platform&#x27;s **Path Ignores** box **doesn&#x27;t** override default Semgrep ignore patterns included with its CLI tool, since the patterns are additive. To override a Semgrep default, both an existing local `.semgrepignore` file and the **Path ignores** box must be configured. See [Override defaults](#override-defaults).

All files and folders defined using Semgrep AppSec Platform&#x27;s **Path Ignores** feature, both for a specific project and globally, are additive.

tipThis method is utilized by the `semgrep ci` command. For `semgrep scan`, you can only define ignored files and folders through `.semgrepignore`.

### Define files and folders for a specific project[​](#define-files-and-folders-for-a-specific-project)

- Sign in to [* Semgrep AppSec Platform](https://semgrep.dev/login?return_path=/manage/projects).
- From the sidebar, click **[Projects](https://semgrep.dev/orgs/-/projects)**.
- Find the project you want to modify, then click its **** icon** under **Details**.
- Click the **Settings** tab.
- To define files and folders that Semgrep can ignore:

Click **Code (SAST) &amp; Supply Chain (SCA)** or **Secrets** to expand and display the **Path Ignores** box.
- Enter files and folders to ignore in the relevant **Path Ignores** box.
- Click **Save changes**.

*
***Figure**. Set ignore paths for a project in Semgrep AppSec Platform.*

### Define files and folders for all projects of an organization[​](#define-files-and-folders-for-all-projects-of-an-organization)

- Sign in to [* Semgrep AppSec Platform](https://semgrep.dev/login?return_path=/manage/projects).
- Click **Settings**. This takes you to the **General &gt; Global** settings tab.
- Enter files and folders to ignore in the **Ignore paths** box for the product to which the changes should apply.
- Click **Save changes**.

***Figure**. Set global ignore paths for all projects of an organization in Semgrep AppSec Platform.*

### Add items to `.semgrepignore` during findings triage[​](#add-items-to-semgrepignore-during-findings-triage)
You can also add files to `.semgrepignore` while triaging individual findings using Semgrep AppSec Platform:

- On the Semgrep Code [Findings](https://semgrep.dev/orgs/-/findings?tab=open) page, click the **Status** filter, and then select the **Open** status to see all open findings.
- Click the finding you want ignored to open its **Details** page.
- Select **Ignored**, and optionally, select an **Ignore reason**.
- Click to expand **Ignore files in future scans...**.
- Select the files you want ignored in future scans.
- Click **Change status** to save.

## Ignore code through nosemgrep[​](#ignore-code-through-nosemgrep)
To ignore blocks of code, define an **inline comment**, followed by the word `nosemgrep`, at either the **first line** or **the line preceding** the potential match. Semgrep ignores all rule pattern matches. This functionality works across all supported languages.

cautionIgnoring code through this method still generates a finding. The finding is automatically set to the **Ignored** triage state.

`nosemgrep` in Python:

`bad_func1()  # nosemgrep# nosemgrepbad_func2()`
`nosemgrep` in JavaScript:

`// nosemgrepbad_func1()bad_func2(); // nosemgrepbad_func3(   // nosemgrep    arg);`
To ignore blocks of code for a **particular rule**, enter its `rule-id` as follows: `nosemgrep: RULE_ID`. To ignore **multiple rules**, use a comma-delimited list. `rule-ids` must be referenced with their namespace.

Python examples:

`bad_func1()  # nosemgrep: rule-id-1# nosemgrep: rule-id-1, rule-id-2bad_func2()`
JavaScript examples wherein rules are stored in a `configs` subdirectory:

`// nosemgrep: configs.rule-id-3bad_func1()bad_func2(); // nosemgrep: configs.rule-id-3bad_func3(   // nosemgrep: configs.rule-id-3, configs.rule-id-4    arg);`
infoPrevious annotations for ignoring code inline, such as `nosem`, are deprecated.

## Disable rules on Semgrep AppSec Platform[​](#disable-rules-on-semgrep-appsec-platform)
Semgrep AppSec Platform users can disable rules and rulesets through the Policies page. See [Disable rules](/docs/semgrep-code/policies#disable-rules) and [Disable rulesets](/docs/semgrep-code/triage-remediation#disable-a-ruleset-or-a-rule).

## Ignore findings[​](#ignore-findings)
**Ignoring** can also be a triage action. In this case, the code is scanned rather than excluded, and if a pattern match occurs, a finding record is generated that you can then triage as **Ignored**. See [Triage and remediate Semgrep Code findings in Semgrep AppSec Platform](/docs/semgrep-code/triage-remediation#ignore-findings) to learn how to:

- [Manage findings](/docs/semgrep-code/triage-remediation#triage-and-remediation)
- [Ignore findings through PR and MR comments](/docs/semgrep-code/triage-remediation#triage-findings-through-pr-and-mr-comments)

## Troubleshooting[​](#troubleshooting)
### Tips to prevent unexpected ignore behavior[​](#tips-to-prevent-unexpected-ignore-behavior)
tipThis section focuses on ignoring as excluding or skipping files, not as a triage action.

Because Semgrep ignore logic is configured at the file, repository, and platform level, you may sometimes encounter unexpected behavior.

- If possible, only create a custom, user-defined `.semgrepignore` file if you are **overriding** Semgrep defaults. This means defining all other items to ignore through the global or project path ignores.

This method works well if your organization primarily scans using the `semgrep ci` command.

- Be aware that creating a user-defined `.semgrepignore` file enables developers to edit it.
- Include the `.semgrepignore` file in Git tracking to keep a log of changes and ensure it&#x27;s applied consistently.
- To **include** a file or folder for scanning, ensure it&#x27;s not in any of the following places:

Global path ignores
- Project path ignores
- User-defined `.semgrepignore`
- Semgrep defaults (implicit) `.semgrepignore`

### `SAST_EXCLUDED_PATHS`[​](#sast_excluded_paths)
**For GitLab users**: if you use [the `SAST_EXCLUDED_PATHS` variable](https://docs.gitlab.com/ee/user/application_security/sast/#vulnerability-filters) to specify paths excluded from analysis, you may find that Semgrep doesn&#x27;t honor these items. This is due to default Semgrep behavior. To explicitly exclude files, you must do one of the following steps:

- Create a `.semgrepignore` file that lists the files you want excluded.
- [Update the **Path Ignores** box](#define-ignored-files-and-folders-in-semgrep-appsec-platform) in Semgrep AppSec Platform.
Not finding what you need in this doc? Ask questions in our [Community Slack group](https://go.semgrep.dev/slack), or see [Support](/docs/support/) for other ways to get help.

Tags:**- [Semgrep AppSec Platform](/docs/tags/semgrep-app-sec-platform)[Edit this page](https://github.com/semgrep/semgrep-docs/edit/main/docs/ignoring-files-folders-code.md)Last updated on **Apr 4, 2025**