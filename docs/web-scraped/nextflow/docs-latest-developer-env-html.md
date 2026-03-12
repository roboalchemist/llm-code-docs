# Source: https://www.nextflow.io/docs/latest/developer-env.html

Title: Environment setup — Nextflow documentation

URL Source: https://www.nextflow.io/docs/latest/developer-env.html

Markdown Content:
Setting up a Nextflow development environment is a prerequisite for creating, testing, and optimizing data analysis pipelines.

### Recommended tools

* [VS Code](https://www.nextflow.io/docs/latest/developer-env.html#devenv-vscode): A versatile code editor that enhances your Nextflow development with features like syntax highlighting and debugging.

* [Extensions](https://www.nextflow.io/docs/latest/developer-env.html#devenv-extensions): The VS Code marketplace offers a variety of extensions to enhance development. The [Nextflow extension](https://www.nextflow.io/docs/latest/developer-env.html#devenv-nextflow) is specifically designed to enhance Nextflow development with diagnostics, hover hints, code navigation, code completion, and more.

* [Docker](https://www.nextflow.io/docs/latest/developer-env.html#devenv-docker): A containerization platform that ensures your Nextflow workflows run consistently across different environments by packaging dependencies into isolated containers.

* [Git](https://www.nextflow.io/docs/latest/developer-env.html#devenv-git): A version control system that helps manage and track changes in your Nextflow projects, making collaboration and code management more efficient.

The sections below outline the steps for setting up these tools.

Note

Nextflow must be installed separately. See [Installation](https://www.nextflow.io/docs/latest/install.html#install-page) for Nextflow installation instructions.

Note

If you are using a Windows computer, first install and configure the Windows Subsystem for Linux (WSL). See [Windows Subsystem for Linux](https://www.nextflow.io/docs/latest/developer-env.html#devenv-wsl) for installation instructions.

VS Code[](https://www.nextflow.io/docs/latest/developer-env.html#vs-code "Permalink to this heading")
------------------------------------------------------------------------------------------------------

An Integrated Development Environment (IDE) provides a user-friendly interface for writing, editing, and managing code. Installing one is an essential step for setting up your environment.

Visual Studio Code (VS Code) is a popular lightweight IDE known for its versatility and extensibility. It offers features like syntax highlighting, intelligent code completion, and integrated debugging tools for various programming languages. VS Code supports Windows, macOS, and Linux, and is a good choice for both new and experienced Nextflow developers.

To install VS Code on Windows:

1. Visit the [VS Code](https://code.visualstudio.com/download) website.

2. Download VS Code for Windows.

3. Double-click the installer executable (`.exe`) file and follow the setup steps.

Extensions[](https://www.nextflow.io/docs/latest/developer-env.html#extensions "Permalink to this heading")
------------------------------------------------------------------------------------------------------------

Extensions are a key feature of IDEs and allow you to customize your development environment by adding support for various programming languages, tools, and features. The [VS Code Marketplace](https://marketplace.visualstudio.com/vscode) offers thousands of extensions that can enhance your productivity and tailor the editor to your specific needs. Popular VS Code extensions for Nextflow developers are listed below:

**Nextflow**

The VS Code [Nextflow extension](https://marketplace.visualstudio.com/items?itemName=nextflow.nextflow) adds Nextflow language support to the editor. The Nextflow extension enhances development with:

* Diagnostics

* Hover hints

* Code navigation

* Code completion

* Formatting

* Renaming

* Parameter schemas

* DAG previews

See [VS Code integration](https://www.nextflow.io/docs/latest/vscode.html#vscode-page) for more information about the Nextflow extension features and how it enforces the Nextflow syntax.

**nf-core**

[nf-core](https://nf-co.re/) is a community effort to collect a curated set of analysis pipelines built using Nextflow. The [nf-core extension pack](https://marketplace.visualstudio.com/items?itemName=nf-core.nf-core-extensionpack) adds a selection of tools that support development. For example, it includes [Code Spell Checker](https://marketplace.visualstudio.com/items?itemName=streetsidesoftware.code-spell-checker), [Prettier](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode), [Todo Tree](https://marketplace.visualstudio.com/items?itemName=Gruntfuggly.todo-tree), and [Markdown Extended](https://marketplace.visualstudio.com/items?itemName=jebbs.markdown-extended).

See the [nf-core extension pack](https://marketplace.visualstudio.com/items?itemName=nf-core.nf-core-extensionpack) for more information about the included tools.

**Remote development**

The [Remote Development extension pack](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack) enables you to run WSL, SSH, or a development container for editing and debugging with the full set of VS Code features.

The pack includes the [Remote - SSH](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh), [Remote - Tunnels](https://marketplace.visualstudio.com/items?itemName=ms-vscode.remote-server), [Dev Containers](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers), and [WSL](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-wsl) extensions. See [Remote Development](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.vscode-remote-extensionpack) for more information about the tools included in the remote development extension pack.

Note

The Remote Development extension pack is required if you are developing using remote servers, Windows Subsystem for Linux, or Development Containers.

Installing VS Code extensions requires just a few clicks in the Extensions Marketplace.

To install a VS Code extension on Windows:

1. Open VS Code.

2. Open the **Extensions** view in the left-hand menu.

3. Search for the extension.

4. Select **Install**.

Docker[](https://www.nextflow.io/docs/latest/developer-env.html#docker "Permalink to this heading")
----------------------------------------------------------------------------------------------------

Docker is an open-source platform that simplifies application development, deployment, and execution by packaging applications and their dependencies into containers. Containerization enables the creation of self-contained and fully reproducible computational pipelines by bundling a script’s binary dependencies into a standardized and portable format. Containers can be executed on any platform that supports a container runtime and ensures consistency across different environments.

Docker Desktop provides a Graphical User Interface (GUI) for managing Docker containers. Installing Docker Desktop is a straightforward process that allows you to create, deploy, and manage applications within containers.

To install Docker Desktop on Windows:

1. Go to [Install Docker Desktop on Windows](https://docs.docker.com/desktop/setup/install/windows-install/).

2. Download the installer.

3. Double-click Docker Desktop `Installer.exe` to run the installer. By default, Docker Desktop is installed at `C:\Program Files\Docker\Docker`.

4. Depending on your choice of backend, select the **Use WSL 2 instead of Hyper-V** option on the Configuration page.

Note

You won’t be able to select which backend to use if your system only supports one of the two options.
5.   Follow the instructions on the installation wizard to authorize the installer and proceed with the install.

1. When the installation is complete, select **Close**.

2. Start Docker Desktop.

3. Review the Docker Subscription Service Agreement and select **Accept** to continue.

Note

Docker Desktop won’t run if you do not agree to the terms. You can choose to accept the terms at a later date by opening Docker Desktop.
9.   Docker Desktop starts after you accept the terms.

Nextflow supports multiple container technologies (e.g., Singularity and Podman) so you can choose the one that best fits your needs. See [Containers](https://www.nextflow.io/docs/latest/container.html#container-page) for more information about other supported container engines.

Git[](https://www.nextflow.io/docs/latest/developer-env.html#git "Permalink to this heading")
----------------------------------------------------------------------------------------------

Git provides powerful version control that helps track code changes. Git operates locally, meaning you don’t need an internet connection to track changes, but it can also be used with remote platforms like GitHub, GitLab, or Bitbucket for collaborative development.

Nextflow seamlessly integrates with Git for source code management providers to manage pipelines as version-controlled Git repositories.

Git is already installed on most WSL distributions. You can check if it is already installed by running `git version`.

To install the latest stable Git version on Linux Debian/Ubuntu distributions:

1. Open a terminal window and run `sudo apt-get install git-all`.

2. Once complete, run `git version` to verify Git was installed.

See [git-scm documentation](https://git-scm.com/downloads/linux) for more information about installing Git on other Linux distributions.

Windows Subsystem for Linux[](https://www.nextflow.io/docs/latest/developer-env.html#windows-subsystem-for-linux "Permalink to this heading")
----------------------------------------------------------------------------------------------------------------------------------------------

Developers can access the power of both Windows and Linux on a Windows machine. The Windows Subsystem for Linux (WSL) lets developers install a Linux distribution and use Linux applications, utilities, and Bash command-line tools directly on Windows without the overhead of a virtual machine or dual-boot setup.

WSL is an optional feature on Windows 10 version 2004 and higher (Build 19041 and higher) or Windows 11. You can enable it through PowerShell or Windows Command Prompt. The steps below outline the recommended setup.

To enable WSL on Windows using Powershell or Windows Command Prompt:

1. Right-click and select **Run as administrator** to use PowerShell or Windows Command Prompt in administrator mode.

2. Run `wsl --install`.

Note

This command will enable the features necessary to run WSL and install the Ubuntu distribution.
3.   When prompted, restart Windows.

1. After restarting Windows, open the Ubuntu distribution and create a new Linux **User Name** and **Password** when prompted.

Note

The **User Name** and **Password** is specific to each Linux distribution that you install and has no bearing on your Windows user name.

See [Set up a WSL development environment](https://learn.microsoft.com/en-us/windows/wsl/setup/environment) for more about installing WSL.
