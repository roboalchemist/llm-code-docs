# Source: https://docs.envzero.com/guides/admin-guide/variables/access-tokens.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.envzero.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Manage Access Tokens

> Add and manage HTTP/S access tokens (Git tokens) for private VCS repository access in env zero

env zero can use HTTP/S Access tokens (aka Git Tokens) to access your infrastructure as code templates stored in private git repositories.

## Adding a New Access Token

1. Enter your organization's settings, and go to the **Credentials** tab
2. In the **Git Tokens** section, click **+ Add Token**
3. Choose any name that will help you recognize this token in the future.
4. Enter the token value in the `Value` text box.
5. Click **Add**

## Generating Access Tokens

Generate an access token is done in your VCS. This is vendor-specific and you can find further instructions here -

* Github - [Personal access tokens](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line)
* Gitlab - [Personal access tokens](https://docs.gitlab.com/ee/user/profile/personal_access_tokens)
* Bitbucket - [App Passwords](https://confluence.atlassian.com/bitbucket/app-passwords-828781300.html)

Built with [Mintlify](https://mintlify.com).
