# Source: https://docs.socket.dev/docs/socket-for-github-installation.md

# Install the App

Socket is quick and easy to install.

* Takes 2 minutes to install
* Very minimal permissions
  * Does not use write permissions
  * Never uploads your source code
* The easiest security product you’ve ever installed! ✨

## Step 1

Install the [Socket Security App](https://github.com/apps/socket-security) from the GitHub Marketplace by visiting: [github.com/apps/socket-security](https://github.com/apps/socket-security).

![](https://files.readme.io/a417c65-Untitled.png "Untitled.png")

## Step 2

Select the repositories you want to protect.

![](https://files.readme.io/83f2bfe-Untitled_2.png "Untitled 2.png")

## Step 3.

# 🥳

You’re done! There’s no step 3.

We told you this would be the easiest security product you ever installed!

## What next?

You can always add or remove Socket from additional repositories by visiting the [Socket Security app settings](https://github.com/apps/socket-security/installations/new) within GitHub.

When you install the GitHub app to your GitHub user account or organization, Socket will begin analyzing all pull requests for changes to manifest files associated with the various supported ecosystem. See [Socket Ecosystem Support](https://docs.socket.dev/docs/language-support) for information on the currently supported ecosystems and manifest files.

For each commit to the default branch with npm related dependency manifests, a project report will be generated, which lists all dependencies found in the project.

If a pull request contains a dependency change to npm or python dependency manifests that introduces any of the following issues, a comment will be created in the pull request that includes more details about the change.

* [Potential Typo Squat](https://socket.dev/npm/issue/didYouMean)
* [Malware](https://socket.dev/npm/issue/malware)
* [Install scripts](https://socket.dev/npm/issue/installScripts)
* [Telemetry](https://socket.dev/npm/issue/telemetry)
* [Troll Package](https://socket.dev/npm/issue/troll)
* [Native code](https://socket.dev/npm/issue/hasNativeCode)
* [Bin script confusion](https://socket.dev/npm/issue/binScriptConfusion)
* [Bin script shell injection](https://socket.dev/npm/issue/shellScriptOverride)
* [Git dependency](https://socket.dev/npm/issue/gitDependency)
* [HTTP dependency](https://socket.dev/npm/issue/httpDependency)
* [Unresolved require](https://socket.dev/npm/issue/unresolvedRequire)