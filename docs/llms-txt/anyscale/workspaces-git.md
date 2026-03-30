# Source: https://docs.anyscale.com/platform/workspaces/workspaces-git.md

# Connect to GitHub

[View Markdown](/platform/workspaces/workspaces-git.md)

# Connect to GitHub

Workspaces integrate with Git and [GitHub](https://docs.github.com/en) for version control to match and enhance your development workflow. You keep the familiar actions of pushing, pulling, branching, and committing code while being able to program a scalable cluster. All committed and uncommitted changes persist across workspace restarts, with the exception of files specified in `.gitignore`.

In this way, you can rely on workspaces for daily development. You have a consistent developer experience whether you scale down to a small CPU node akin to a laptop or power up to a multi-GPU cluster for high performance AI workloads.

## Authenticating with GitHub[​](#authenticate "Direct link to Authenticating with GitHub")

To connect to a GitHub repository from a workspace, you need to authenticate using either HTTPS or SSH.

### Connect with HTTPS[​](#https "Direct link to Connect with HTTPS")

From a terminal in the workspace, run the following to [clone a remote repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository):

```
git clone https://github.com/user/repo.git # Replace with the repo HTTPS URL.
```

In Visual Studio Code, follow the UI to sign in using GitHub. Otherwise, when prompted, enter your GitHub username and [personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens) in place of a password.

tip

When you `git clone`, `git fetch`, `git pull`, or `git push` to a remote repository using HTTPS URLs on the command line, Git asks you for your GitHub username and password. See [Git passwords documentation](https://docs.github.com/en/get-started/getting-started-with-git/why-is-git-always-asking-for-my-password) for credential management options.

### Connect with SSH[​](#ssh "Direct link to Connect with SSH")

With SSH keys, you can connect to GitHub without entering your username and personal access token with each action. Anyscale generates a unique SSH key tied to your user identity. Follow these instructions for adding a new SSH authentication to your account on GitHub.com:

1. **Copy the Anyscale SSH key to your clipboard**

   To access the SSH key, start a Workspace, and run the following on the command line to show it:

   ```
   cat ~/.ssh/id_rsa.pub
   ```

   From here, copy the SSH key to your clipboard without adding any newlines or whitespace.

2. **Navigate to [GitHub.com](https://github.com/) settings**

   Sign in to your account, click your profile photo, then select **Settings**. In the "Access" section of the sidebar, click **SSH and GPG keys**.

3. **Add SSH key**

   Select **New SSH key**, give it a descriptive title. Then select **Authentication Key** in the dropdown. Paste in your key.

4. **Clone a repository over SSH**

   From a terminal in the workspace, run the following to [clone a remote repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository):

   ```
   git clone git@github.com:user/repo.git # Replace with the repo SSH URL.
   ```

warning

Anyscale SSH keys aren't stored securely in a key store, so it's possible for other users in the organization to access this key. Secure your SSH key with a passphrase for an extra layer of security. See the [GitHub documentation on SSH key passphrases](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/working-with-ssh-key-passphrases).

tip

For more information on security options and troubleshooting, see the [GitHub SSH guides](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/about-ssh).
