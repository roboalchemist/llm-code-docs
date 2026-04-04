# Source: https://help.aikido.dev/code-scanning/connect-your-source-code/connect-bitbucket-account-to-aikido.md

# Connect Bitbucket Account

**Table of contents:**

* [1. Logging in using Bitbucket](#1-logging-in-using-bitbucket)
* [2. Authorizing access to an organization](#2-authorizing-access-to-an-organization)
* [3. Select your repos](#3-select-your-repos)
* [4. Checking results](#4-checking-results)

## Connect Bitbucket Account to Aikido

Aikido requests read-only access to your Bitbucket organization to analyze your repositories. After analysis, your code is always wiped from the system.

### 1. Logging in using Bitbucket <a href="#id-1-logging-in-using-bitbucket" id="id-1-logging-in-using-bitbucket"></a>

To get started, navigate to <https://app.aikido.dev/> and log in with Bitbucket. This will look like the screenshot below. Here, Aikido only requests access to your identity on Bitbucket and the associated email address.

![Access request screen for account information by Aikido User Authentication, with grant or cancel options.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-cfe1712ebee2f37ac0b729bdee750fc636d826d3%2Fconnect-bitbucket-account-to-aikido_10401885-4c52-4133-894a-48f9d2736781.png?alt=media)

### 2. Authorizing access to an organization <a href="#id-2-authorizing-access-to-an-organization" id="id-2-authorizing-access-to-an-organization"></a>

On the next screen, you can choose to connect a real organization or a sample workspace. If you choose a real organization you will be redirected back to Bitbucket. Once there, pick the organization you would like to authorize.

![Aikido requests account and repository access; user must approve or deny.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-4564ac5f4c41b0bcc1c126c072afcbf1670be22c%2Fconnect-bitbucket-account-to-aikido_76533a25-f878-4c97-a437-e35e38c780ea.png?alt=media)

### 3. Select your repos <a href="#id-3-select-your-repos" id="id-3-select-your-repos"></a>

You can optionally grant access to 1 or 2 repositories instead of all repositories as seen below:

![Select repositories to monitor for security with Aikido’s free or upgraded plan.](https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fgit-blob-9a584a4da4b5097c54d0e77e10ad7fefa40fe257%2Fconnect-bitbucket-account-to-aikido_89ce9a97-d113-4d2d-bb6c-8526fb67646c.png?alt=media)

### 4. Checking results <a href="#id-4-checking-results" id="id-4-checking-results"></a>

After granting access and validating the repositories you want to scan, Aikido will automatically start scanning. After about 1 minute, you should see the first results come in!
