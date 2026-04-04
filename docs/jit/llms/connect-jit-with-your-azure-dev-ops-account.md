# Source: https://docs.jit.io/docs/connect-jit-with-your-azure-dev-ops-account.md

# Connect Jit with your Azure DevOps Account

To connect Jit with your Azure DevOps account, follow the steps below.

## Create an account and begin the Quick Start flow

* [Start a free trial](https://platform.jit.io/login) to create a Jit account.
* This will bring you to our Quick Start Guide, where you’ll be directed to “Integrate Source Code Manager”. Hit the Azure DevOps icon.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f3c5a61b6132a435b8dabe753f533e19c14b0a528d2ed376867ffaa012a630b6-Screenshot_2025-07-02_at_16.15.48.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

## Connect Jit with your Azure DevOps Account

**Step 1: Enter Your Azure DevOps Organization Name**

To connect Jit with your Azure DevOps account, start by entering your organization name:

1. Sign in to your [Azure DevOps account](https://dev.azure.com).
2. Locate your **organization name**\
   Your organization name appears in the URL when you access your Azure DevOps organization: <https://dev.azure.com/{your-organization}>
3. Copy your organization name and paste it in the input field in the Jit wizard.

Once entered, click **Continue**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/c621d4532850280c835b40ec5a422cbcbcffaaaeea02d3f613d40446f16995ba-Screenshot_2025-12-11_at_11.15.52.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

**Step 2: Generate Azure DevOps Personal Access Token**

To allow Jit to access your Azure DevOps repositories, generate a personal access token:

1.From your home page, open User Settings in the top-right corner

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/fff7399b3d62f1953593c952bb16520d40e5527e4635750aeba5dd6994e9acba-Screenshot_2025-12-11_at_11.45.39.png",
        "",
        ""
      ],
      "align": "left",
      "sizing": "200px",
      "border": true
    }
  ]
}
[/block]

2. In the User Settings menu, select Personal access tokens.
3. Click **New Token**, enter a name for your token, select your organization, and set the expiration date to **1 year**.

   1. Under Scopes, select "**Code: Read & Write**".

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/c78f6847e43dbfc7204f9e2c473ce8690c153e651e0e679f3bb8e1ea0d268886-Screenshot_2025-12-11_at_11.50.02.png",
        "",
        ""
      ],
      "align": "left",
      "sizing": "400px",
      "border": true
    }
  ]
}
[/block]

4. Click **Create** to generate the token. Make sure to copy and securely store the token immediately - you won\`t be able to see it again once you close this page.
5. Paste the **generated token** it in the input field in the **Jit wizard**.

Click **Continue** to proceed.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/be7bff852843430406b0749f5acea0fc955f80a73eb17d6de8b2ed992c131c71-Screenshot_2025-12-11_at_11.21.10.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

**Step 3: Configure Pull Request Checks**

1. **Enable Pull Request checks (optional).**\
   When enabled, Jit will scan your Azure DevOps Pull Requests for security issues and display the results directly on the PR page. This helps in identifying and addressing vulnerabilities early in the development process.
2. **You can always update this setting later.**\
   Go to **Settings → Manage Resources** to enable or disable Pull Request checks at any time.

Click **Finish** to complete the integration.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/179e780492d06708f7ab8e57ff35ec5be0f582d1e5e5bd7404c890587080a34d-Screenshot_2025-12-11_at_12.04.51.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

ℹ️ After completing the integration, you can manage which Azure DevOps repositories Jit scans by navigating to **Settings → Manage Resources** in the Jit dashboard. Here, you can select or deselect repositories based on your preferences. Repositories that are not selected will not be scanned by Jit.

## Jit is now scanning your codebase!

Now that you’ve implemented the integration with Azure DevOps, Jit will automatically begin scanning your codebase (or the repositories you selected).

Specifically, Jit will activate the SCA, SAST, and Secrets detection tools – these scanners will detect known vulnerabilities in your open-source components, security flaws in your custom code, and hardcoded secrets, respectively.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/1cebf870a29a5dd84aa329703dfe95e204d5add31c13f547d9ddd5b7f5c652a8-Screenshot_2024-10-16_at_11.06.59_AM.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

* Once the scans are complete, hit “See Results”, which will bring you to the security scanners that have been activated. If the scanners are marked as "Failed", that means they detected security issues. You may need to wait a few minutes before the findings appear.
* Click on the findings, which will bring you to the Findings page where you can gather more details about the security issues.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/859d203d924fd85e362a491409cbd16a92f73230e214bb7878c41f65948727c1-Screenshot_2024-11-13_at_4.51.46_PM.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

> 👍 Success!
>
> You are good to go.
>
> Click [Explore Jit's features](https://docs.jit.io/docs/explore-jit) to learn how Jit prioritizes your security risks, enables continuous scanning for developers, integrates with a notification system, and much more.