# Source: https://docs.instabug.com/product-guides-and-integrations/product-guides/ai-features/resolve-agent/source-code-connection-github.md

# Source Code Connection - GitHub

Resolve Agent is an AI-powered feature designed to help developers quickly resolve app crashes by automating root cause analysis, code fix generation, and pull request creation. To enable SmartResolve, you need to connect your source code repository to Luciq using the **Luciq CodeLink** GitHub app. This guide walks you through the steps to complete the connection and start using Resolve Agent.

### Why Connect Your Codebase to Luciq?

Connecting your codebase enables Resolve Agent to:

* Analyze crash data and identify the root cause.
* Provide actionable code fix suggestions.
* Help generate pull requests with suggested fixes directly in your repository.

By linking your codebase, you’ll save time on diagnosing and resolving crashes, improve app stability, and reduce operational costs.

#### Step 1: Start the Connection Process

1. Navigate to **Settings → Source Code Management** in the Luciq dashboard.
2. Click on the **Connect** button, within **GitHub** connect widget.

   <div align="left"><figure><img src="https://files.readme.io/e6c86d98035aadd815f1c1bfd65adbb7488d3304c69a1c7cca0d0fbe42fc3524-product-guides-connect-github-5.png" alt="" width="563"><figcaption></figcaption></figure></div>

#### Step 2: Authenticate with GitHub

1. You’ll be redirected to the **Connect GitHub Source Code** setup screen.
2. Select "**Install Luciq on GitHub.**"
   * This will redirect you to GitHub, where you need to approve the installation.
   * If your organization owner has already installed the app, you can use the installation ID instead.
3. Click **Continue** once the installation is approved.<br>

   <div align="left"><figure><img src="https://files.readme.io/6258363af862d61b0d4dbb3ab722595c90d722ae23fa9d43de0f026f53312548-product-guides-connect-github-1.png" alt="" width="563"><figcaption></figcaption></figure></div>

#### Step 3: Select Repository and Branch

1. After authentication, you’ll be prompted to select the repository and branch where Luciq should analyze and generate code fixes.
2. Choose the correct repository and branch from the dropdown list.
3. Click **Continue** to proceed.<br>

   <div align="left"><figure><img src="https://files.readme.io/9a76506f763debc21b19927a80e3b732e4ce7c33979b1afa4d7f2e5ac5ae5fca-product-guides-connect-github-6.png" alt="" width="563"><figcaption></figcaption></figure></div>

#### Step 4: Connect the Codebase

1. Luciq will begin connecting to your GitHub repository.
2. This process may take a few moments.
3. Once completed, you’ll see a success message confirming the connection.

   <div align="left"><figure><img src="https://files.readme.io/1d9fbd62f6ea12a0cdb215cae52d0e99d97b0626e76f983b20c8839ba946b888-product-guides-connect-github-3.jpg" alt="" width="563"><figcaption></figcaption></figure></div>

#### Step 5: Verify Connection in Settings

1. Navigate to **Settings → Source Code Management** in the Luciq dashboard.
2. You should see a confirmation that GitHub Connect is set up successfully, showing the organization, repository, and branch.
3. You’re now ready to use SmartResolve to fix crashes automatically!<br>

   <div align="left"><figure><img src="https://files.readme.io/513550b79d2c58abefa3c12c21ce04b904e8b0984499b9e6d534c1c7cc57bef8-product-guides-connect-github-4.png" alt="" width="563"><figcaption></figcaption></figure></div>

#### Next Steps

* After connecting your codebase, you can use SmartResolve to:
  * Analyze crash details and identify root causes.
  * Generate up to three suggested code fixes.
  * Automatically create a pull request with the suggested fix.
  * Review and merge the pull request directly in your repository.

### Troubleshooting

* **Permission Issues**: Make sure you have the necessary permissions to install the GitHub app or contact your organization owner.
* **Repository Not Showing**: Ensure the repository is under the connected GitHub organization and that you have access to it.
* **Connection Errors**: If the connection fails, try reconnecting by first deleting the existing connection and repeating the steps above or checking your GitHub permissions.
