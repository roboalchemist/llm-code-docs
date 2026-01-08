# Quickstart

Source: https://semgrep.dev/docs/getting-started/quickstart

- [](/docs/)- [Scan](/docs/getting-started/quickstart)- Get started- Quickstart**On this page- [quickstart](/docs/tags/quickstart)QuickstartLearn how to set up Semgrep, scan your first project for security issues, and view your findings. A **project** can be any codebase, repository, or folder within a monorepo.

prerequisitesYou must have Python 3.10 or later installed on the machine where the Semgrep CLI is running.

- 
Navigate to [Semgrep AppSec Platform](https://semgrep.dev/login), and sign up by clicking on **Continue with GitHub** or **Continue with GitLab**. Follow the on-screen prompts to grant Semgrep the necessary permissions.

- 
Provide the **Organization display name** you&#x27;d like to use, then click **Create new organization**.

- 
When asked **Where do you want to scan?** click **Run on CLI**.

- 
Launch your CLI, and follow the instructions on the [**Scan a project on your machine**](https://semgrep.dev/onboarding/scan) page. For your convenience, the same information is presented below, along with instructions for Windows users.

macOS- Linux- Windows (beta)- Docker
- 
Install the Semgrep CLI and confirm the installation:

`# install through homebrewbrew install semgrep# install through pippython3 -m pip install semgrep# confirm installation succeeded by printing the currently installed versionsemgrep --version`
note**Homebrew users:** ensure that you&#x27;ve [added Homebrew to your PATH](https://docs.brew.sh/FAQ#my-mac-apps-dont-find-homebrew-utilities).

- 
Log in to your Semgrep account. Running this command launches a browser window, but you can also use the link that&#x27;s returned in the CLI to proceed:

`semgrep login`

- 
In the **Semgrep CLI login**, click **Activate** to proceed.

- 
Return to the CLI, navigate to the root of your project, and run your first scan:

`semgrep ci`

- 
Install the Semgrep CLI and confirm the installation:

`# install through pippython3 -m pip install semgrep# if you get the following error &quot;error: externally-managed-environment&quot;,# see semgrep.dev/docs/kb/semgrep-appsec-platform/error-externally-managed-environment # confirm installation succeeded by printing the currently installed versionsemgrep --version`

- 
Log in to your Semgrep account. Running this command launches a browser window, but you can also use the link that&#x27;s returned in the CLI to proceed:

`semgrep login`

- 
In the **Semgrep CLI login**, click **Activate** to proceed.

- 
Return to the CLI, navigate to the root of your project, and run your first scan:

`semgrep ci`

- 
[Download](https://www.python.org/downloads/) and install Python. Make sure to check the box to add python.exe to the PATH, otherwise you will have difficulty running Pip and Semgrep.

- 
Configure your system to run Python with UTF-8 text encodings by default. In PowerShell, run:

`[System.Environment]::SetEnvironmentVariable(&#x27;PYTHONUTF8&#x27;, &#x27;1&#x27;, &#x27;User&#x27;)`

- 
Install the Semgrep CLI and confirm the installation. In PowerShell, run:

`# install through pippip install –upgrade semgrep# if you get the following error &quot;error: externally-managed-environment&quot;,# see semgrep.dev/docs/kb/semgrep-appsec-platform/error-externally-managed-environment # confirm installation succeeded by printing the currently installed versionsemgrep --version`

- 
Log in to your Semgrep account. Running this command launches a browser window, but you can also use the link that&#x27;s returned in the CLI to proceed:

`semgrep login`

- 
In the **Semgrep CLI login**, click **Activate** to proceed.

- 
Return to the CLI, navigate to the root of your project, and run your first scan:

`semgrep ci`

PrerequisitesEnsure that you have [Docker installed](https://docs.docker.com/desktop/) before proceeding.

- 
Pull the latest image and confirm the version:

`docker pull semgrep/semgrep# confirm versiondocker run --rm semgrep/semgrep semgrep --version`

- 
For users running Docker on **macOS or Linux** Docker:

Log in to your Semgrep account (running this command will launch a browser window, but you can also use the link that&#x27;s returned in the CLI to proceed):

`docker run -it semgrep/semgrep semgrep login`

- 
In the **Semgrep CLI login**, click **Activate** to proceed. Return to the CLI and copy the login token that&#x27;s shown.

- 
Navigate into the root of your project, and run your first scan. Be sure to substitute `YOUR_TOKEN` with the login token value you copied in the previous step:

`docker run -e SEMGREP_APP_TOKEN=YOUR_TOKEN --rm -v &quot;${PWD}:/src&quot; semgrep/semgrep semgrep ci`
The provided `-v` option mounts the current directory into the container to be scanned. Navigate into a different project or provide a specific local directory in the command to scan a different project.

- 
For users running Docker on **Windows**:

Log in to your Semgrep account (running this command will launch a browser window, but you can also use the link that&#x27;s returned in the CLI to proceed):

`docker run -it semgrep/semgrep semgrep login`

- 
In the **Semgrep CLI login**, click **Activate** to proceed. Return to the CLI, and copy the login token that&#x27;s shown.

- 
Navigate into the root of your project, and run your first scan. Be sure to substitute `YOUR_TOKEN` with the login token value you copied in the previous step:

`docker run -e SEMGREP_APP_TOKEN=YOUR_TOKEN --rm -v &quot;%cd%:/src&quot; semgrep/semgrep semgrep ci`
The provided `-v` option mounts the current directory into the container to be scanned. Navigate into a different project or provide a specific local directory in the command to scan a different project.

- 
Once you&#x27;ve scanned your first application, return to Semgrep AppSec Platform, and click **View findings** to see the security vulnerabilities in your project. Alternatively, you can view your results in Semgrep AppSec Platform&#x27;s **Dashboard** page. For detailed information, click **Code** to access your SAST findings or **Supply Chain** to access your SCA findings.

info**Code is not uploaded.** Only **findings** are sent to Semgrep AppSec Platform.

## Scan without a GitHub or GitLab account[​](#scan-without-a-github-or-gitlab-account)
If you don&#x27;t have a GitHub or GitLab account, you can use `semgrep scan` in your CLI. See [Scan your project](/docs/getting-started/cli#scan-your-project) for more details.

Not finding what you need in this doc? Ask questions in our [Community Slack group](https://go.semgrep.dev/slack), or see [Support](/docs/support/) for other ways to get help.

Tags:**- [quickstart](/docs/tags/quickstart)[Edit this page](https://github.com/semgrep/semgrep-docs/edit/main/docs/getting-started/quickstart.md)Last updated on **Nov 17, 2025**