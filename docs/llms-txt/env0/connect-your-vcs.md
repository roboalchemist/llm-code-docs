# Source: https://docs.envzero.com/guides/getting-started/getting-started/connect-your-vcs.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Connect Your VCS

> Connect your Git repository to env zero using SSH or HTTPS authentication

env zero needs access to your relevant git repositories, in order to read your Terraform code.

If your git repository is public, or if you use GitHub, GitLab, or Bitbucket as your VCS, you can go on to **[Create Your First Template](/guides/getting-started/getting-started/create-your-first-template)**.

If your git repository is private, authentication can be done in one of two ways - using SSH or HTTPS.

## Connect using SSH

### Generate SSH keys and add them to your VCS

This is vendor-specific and you can read more about this here -

* GitHub - [Adding a new SSH key to your GitHub account](https://help.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account)
* Gitlab - [Create and add your SSH key pair](https://docs.gitlab.com/ee/user/ssh.html#generate-an-ssh-key-pair)
* Bitbucket - [Set up an SSH key](https://confluence.atlassian.com/bitbucket/set-up-ssh-for-git-728138079.html)

### Add the SSH key to your organization

1. Enter your **Organization Settings** page, and go to the **SSH Keys** tab

<Frame caption="SSH Keys Screen">
  <img src="https://mintcdn.com/envzero-b61043c8/A22trGA9OCusm4S6/images/guides/getting-started/getting-started/2294.png?fit=max&auto=format&n=A22trGA9OCusm4S6&q=85&s=6c8dc1ef9404db95573ebfba8b183be3" alt="Organization Settings SSH Keys tab showing the interface for managing SSH keys" width="2294" height="1182" data-path="images/guides/getting-started/getting-started/2294.png" />
</Frame>

1. Click **+ Add SSH Key**
2. Choose any name that will help you recognize this key in the future in the `SSH Key Name` box
3. Paste the private key you generated in step 1, into the `SSH Key Value` box
4. Click **Add SSH Key**

<Frame caption="Add new SSH Key Dialog">
  <img src="https://mintcdn.com/envzero-b61043c8/A22trGA9OCusm4S6/images/guides/getting-started/getting-started/1262.png?fit=max&auto=format&n=A22trGA9OCusm4S6&q=85&s=3ad46fbb55858057c821993d295e5cb8" alt="Add new SSH Key dialog box with fields for SSH Key Name and SSH Key Value" width="1262" height="1208" data-path="images/guides/getting-started/getting-started/1262.png" />
</Frame>

## Connect via HTTP/S Tokens

### Generate an access token in your VCS

This is vendor-specific and you can find further instructions here -

* GitHub - [Personal access tokens](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line)
* Gitlab - [Personal access tokens](https://docs.gitlab.com/ee/user/profile/personal_access_tokens)
* Bitbucket - [App Passwords](https://confluence.atlassian.com/bitbucket/app-passwords-828781300.html)

### Add the token to your organization

1. Enter your **Organization Settings**, and go to the **Credentials** tab

<Frame caption="Git Tokens Screen">
  <img src="https://mintcdn.com/envzero-b61043c8/A22trGA9OCusm4S6/images/guides/getting-started/getting-started/2268.png?fit=max&auto=format&n=A22trGA9OCusm4S6&q=85&s=bb230901df3bdbb59b9a8adca9fa6bbb" alt="Organization Settings Credentials tab showing Git Tokens section" width="2268" height="930" data-path="images/guides/getting-started/getting-started/2268.png" />
</Frame>

1. In the **Git Tokens** section, click **+ Add Token**
2. Enter any name that will help you recognize this token in the future in the `Name` box
3. Enter the token value in the `Value` text box.
4. Click **Add**

<Frame caption="Add a new Git token">
  <img src="https://mintcdn.com/envzero-b61043c8/A22trGA9OCusm4S6/images/guides/getting-started/getting-started/1796.png?fit=max&auto=format&n=A22trGA9OCusm4S6&q=85&s=e27d5653d7dd6a432ed69aa343cccf02" alt="Add new Git token dialog box with fields for Name and Value" width="1796" height="154" data-path="images/guides/getting-started/getting-started/1796.png" />
</Frame>

Built with [Mintlify](https://mintlify.com).
