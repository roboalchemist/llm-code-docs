# Source: https://help.aikido.dev/code-scanning/connect-your-source-code/connect-github-account-to-aikido.md

# Connect GitHub Organization

**Table of contents:**

* [1. Logging in using GitHub](#1-logging-in-using-github)
* [2. Authorizing access to an organization](#2-authorizing-access-to-an-organization)
* [3. Checking results](#3-checking-results)

## Connect GitHub Account to Aikido

Aikido requests read-only access to your GitHub organization to analyze your repositories. We use the new GitHub App system, so we don't have to store any tokens in our database at all. After analysis, your code is always wiped from the system.

#### 1. Logging in using GitHub <a href="#id-1-logging-in-using-github" id="id-1-logging-in-using-github"></a>

To get started, navigate to <https://app.aikido.dev/> and log in with GitHub. This will look like the screenshot below. Here, Aikido only requests access to your identity on GitHub and the associated email address.

![Aikido Security requests GitHub authorization to access user identity and email addresses.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-def027deaa2ea84ba3f765c6e45e72e6e8d4338d%2Fconnect-github-account-to-aikido_86f8bf78-e871-4801-b0ec-5da21d111456.png?alt=media)

#### 2. Authorizing access to an organization <a href="#id-2-authorizing-access-to-an-organization" id="id-2-authorizing-access-to-an-organization"></a>

On the next screen, you can choose to connect a real organization or a sample workspace. If you choose a real organization you will be redirected back to GitHub. Once there, pick the organization you would like to authorize. You can optionally grant access to 1 or 2 repositories instead of all repositories as seen below:

![Authorize Aikido Security to access all repositories and read email addresses on GitHub.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-70b99cde218b1a974e192c31ddcdc77a30025d27%2Fconnect-github-account-to-aikido_c8faa94c-a2c8-4173-8dc3-d938951f8aae.png?alt=media)

#### 3. Checking results <a href="#id-3-checking-results" id="id-3-checking-results"></a>

After granting access and validating the repositories you want to scan, Aikido will automatically start scanning. After about 1 minute, you should see the first results come in!
