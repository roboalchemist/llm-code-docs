# Source: https://docs.envzero.com/guides/collaborate-securely/authentication-tokens-and-ssh-keys/ssh-keys.md

# Source: https://docs.envzero.com/guides/admin-guide/variables/ssh-keys.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing SSH Keys

> Add and manage SSH keys at the organization and project level for secure Git repository access

## Add a new SSH Key to your Organization

To create a new SSH key in your *organization* scope, go to your organization's **Settings** page and select the **SSH Keys** tab.

The "SSH Keys" screen shows your existing SSH keys that are associated with your organization. The table shows the SSH key name in your organization and the user who initially created this key.

To create a new SSH key for your organization,

1. Enter your **Organization Settings** page, and go to the **SSH Keys** tab
2. Click **+ Add SSH Key**
3. Choose any name that will help you recognize this key in the future and enter it in the `Name` field
4. Paste the private key you generated in step 1, into the `SSH Key Value` box.
5. Click **Add SSH Key**

Generating SSH keys is vendor-specific and you can read more about this here -

* Github - [Adding a new SSH key to your GitHub account](https://help.github.com/en/github/authenticating-to-github/adding-a-new-ssh-key-to-your-github-account)
* Gitlab - [Create and add your SSH key pair](https://docs.gitlab.com/ee/ssh/index.html#generate-an-ssh-key-pair)
* Bitbucket - [Set up an SSH key](https://confluence.atlassian.com/bitbucket/set-up-ssh-for-git-728138079.html)

## Associate an existing SSH Key with your Template

After creating an SSH Key in your organization, you can now associate this key with your *template*. The *environment* created from that *template* would be able to use its associated keys during its run to establish SSH connectivity.

To associate a key with a template:

1. Go to the organization's **Templates** page.
2. Click the **Settings** button of your desired Template.
3. The **Template Settings** screen includes an `SSH Keys` dropdown. Associate your desired SSH key with your template
4. Click the **Save** button to commit your changes.

<img src="https://mintcdn.com/envzero-b61043c8/noVHY1C-wdNQ4iZn/images/guides/admin-guide/variables/24d9257-template_settings.png?fit=max&auto=format&n=noVHY1C-wdNQ4iZn&q=85&s=2197e29bc54fa31d1b7a8a5c9bcd31e1" alt="" width="1436" height="723" data-path="images/guides/admin-guide/variables/24d9257-template_settings.png" />

## Associate an existing SSH Key with your VCS Environment

The steps are similar to the template association, but in order to modify the environment, click on the kebab menu placed at the top right corner of the environment page.

Built with [Mintlify](https://mintlify.com).
