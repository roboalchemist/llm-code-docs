# Sign in to Semgrep

Source: https://semgrep.dev/docs/for-developers/signin

- [](/docs/)- [For developers](/docs/for-developers/overview)- Sign in to Semgrep**On this page- [Developer education](/docs/tags/developer-education)- [Semgrep AppSec Platform](/docs/tags/semgrep-app-sec-platform)Sign in to Semgrep
Signing in to the [** Semgrep AppSec Platform web app](https://semgrep.dev/login) enables you to:

- View and triage your findings in bulk.
- Use your organization&#x27;s custom Semgrep rules and configurations when you perform local scans with Semgrep. This ensures that everyone in the organization uses the same rules and analyses.

Is this document for you?
- Not all organizations require their developers to create a Semgrep account.
- You can resolve or triage (ignore) findings in pull request or merge request comments, even **without** a Semgrep account, by replying to the comment. See [Resolve findings in your pull request or merge request](/docs/for-developers/resolve-findings-through-comments).

## Semgrep in multiple environments[​](#semgrep-in-multiple-environments)
If you have not yet created a Semgrep account, it is **recommended** to first sign in to the Semgrep web app. This process creates a **personal** account, which you can then use to **join** your organization&#x27;s Semgrep account. This lets you use your organization&#x27;s Semgrep configuration, such as custom rules and scan parameters.

If you use Semgrep in your CLI or IDE, you must sign in from those environments as well. It is recommended to sign in from these interfaces **after** you have signed in to your organization account in the web app.

## Prerequisites[​](#prerequisites)

- Confirm with your security team that there is an existing organization account for you to join.
- For CLI and IDE scans, see [Prerequisites &gt; Command line tool](/docs/prerequisites#semgrep-command-line-tool) to ensure that your machine meets Semgrep&#x27;s requirements.

## Sign in to the web app[​](#sign-in-to-the-web-app)
In a typical Semgrep deployment, your company creates an **org** that you can sign in to and join using your GitHub, GitLab, or SSO credentials. Your organization will let you know through a notice or announcement once you can sign in.

- GitHub or GitLab- SSOTo join an existing org in GitHub or GitLab:

- Sign in to [** Semgrep AppSec Platform](https://semgrep.dev/login) with the account credentials specified by your admin.
- Follow the on-screen prompts to grant Semgrep the needed permissions and proceed. This creates your **personal** Semgrep account.
- Click **Join an existing organization**.
- Click your organization&#x27;s name. The web app signs you in to your organization&#x27;s Semgrep account. You can verify this by viewing the account name in the navigation menu.
To join an existing org through your SSO provider:

- Sign in to [** Semgrep AppSec Platform](https://semgrep.dev/login) with the account credentials specified by your admin.
- You are automatically signed in to all organizations that your admin has set up for you.

After signing in to your org&#x27;s account, you can now sign in and scan with Semgrep from other environments, such as your CLI or IDE.

## Set up Semgrep in the CLI[​](#set-up-semgrep-in-the-cli)
### Install the Semgrep CLI tool[​](#install-the-semgrep-cli-tool)

- **Homebrew users:** Ensure that you&#x27;ve [added Homebrew to your PATH](https://docs.brew.sh/FAQ#my-mac-apps-dont-find-homebrew-utilities).

Install the Semgrep CLI tool and confirm the installation:

`# macOS users onlybrew install semgrep# macOS, Linux, Windows userspython3 -m pip install semgrep# if you get the following error &quot;error: externally-managed-environment&quot;,# see semgrep.dev/docs/kb/semgrep-appsec-platform/error-externally-managed-environment # confirmsemgrep --version`
### Sign in to Semgrep from the CLI[​](#sign-in-to-semgrep-from-the-cli)
To sign in to Semgrep:

- Ensure that you are signed in to your **[org account](#sign-in-to-the-web-app)** in the Semgrep web app.
- Enter the following command in your CLI:
`semgrep login`

- Running this command launches a browser window, but you can also use the link that&#x27;s returned in the CLI to proceed.
- In the Semgrep CLI login dialog, click **Activate** to proceed.

You are now ready to run local scans with your org&#x27;s Semgrep configuration.

Not finding what you need in this doc? Ask questions in our [Community Slack group](https://go.semgrep.dev/slack), or see [Support](/docs/support/) for other ways to get help.

Tags:**- [Developer education](/docs/tags/developer-education)- [Semgrep AppSec Platform](/docs/tags/semgrep-app-sec-platform)[Edit this page](https://github.com/semgrep/semgrep-docs/edit/main/docs/for-developers/developer-signin.md)Last updated on **Apr 8, 2025**