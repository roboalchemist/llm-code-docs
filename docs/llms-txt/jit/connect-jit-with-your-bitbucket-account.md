# Source: https://docs.jit.io/docs/connect-jit-with-your-bitbucket-account.md

# Connect Jit with your Bitbucket Account

To connect Jit with your Bitbucket account, follow the steps below.

## Create an account and begin the Quick Start flow

* [Start a free trial](https://platform.jit.io/login) to create a Jit account.
* This will bring you to our Quick Start Guide, where you’ll be directed to “Integrate Source Code Manager”. Hit the Bitbucket icon.

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

## Connect Jit with your Bitbucket Account

**Step 1: Enter Your Bitbucket Workspace Slug**

To connect Jit with your Bitbucket account, start by entering your workspace slug:

1. Navigate to your Bitbucket [workspace](https://bitbucket.org/account/workspaces/).
2. Locate your **workspace slug** (e.g., my-company).
3. Copy the slug and paste it in the input field in the Jit wizard.

Once entered, click **Continue**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/684dc4d59d756db5f5063a78f64fef54e97d19280c90a034dccc76254faf092f-Screenshot_2025-07-02_at_16.21.00.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

**Step 2: Generate Bitbucket Token**

To allow Jit to access your Bitbucket repositories, generate a workspace-level access token:

1. Navigate to your Bitbucket [workspace](https://bitbucket.org/account/workspaces/).
2. Go to **Settings** (workspace-level settings, not project-level).

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/18edfa3b66cda377e832d15923bc33ef8dff801c482460a38c96b3cb28e23cdc-Screenshot_2025-07-03_at_9.58.06.png",
        "",
        ""
      ],
      "align": "center",
      "sizing": "350px",
      "border": true
    }
  ]
}
[/block]

3. Select **Access tokens** from the sidebar.
4. Create an access token with the following configuration:

   * **Name**: Choose a descriptive name, such as `Jit Integration`, to identify this token.
   * **Expiration**: Set to 1 year to balance security with the convenience of fewer token renewals.
   * **Scopes**:

     * **Pull requests: Write**

     * **Webhooks: Read and Write**

[block:image]{"images":[{"image":["https://files.readme.io/296557fcb9856656b32a6fcb38e913d26b6b32d0ecbff98b82a425b34ca023f9-Screenshot_2025-07-03_at_10.00.27.png","",""],"align":"left","sizing":"600px","border":true}]}[/block]

5. Copy the **generated token** and paste it in the input field in the **Jit wizard**.

Click **Continue** to proceed.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/4d24fca54d2c1d4a7d0e8f5a7d475f94313ab6d139da269a940ebb38f0c2d297-Screenshot_2025-07-02_at_16.28.16.png",
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
   When enabled, Jit will scan your Bitbucket Pull Requests for security issues and display the results directly on the PR page. This helps in identifying and addressing vulnerabilities early in the development process.
2. **You can always update this setting later.**\
   Go to **Settings → Manage Resources** to enable or disable Pull Request checks at any time.

Click **Finish** to complete the integration.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/e2feac4440c97270f99d140fe4cb4d8d243493299888fdf274057d517b9605f3-Screenshot_2025-07-03_at_10.31.29.png",
        "",
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

ℹ️ After completing the integration, you can manage which Bitbucket repositories Jit scans by navigating to **Settings → Manage Resources** in the Jit dashboard. Here, you can select or deselect repositories based on your preferences. Repositories that are not selected will not be scanned by Jit.

## Jit is now scanning your codebase!

Now that you’ve implemented the integration with Bitbucket, Jit will automatically begin scanning your codebase (or the repositories you selected).

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
* Click on the findings, which will bring you to the findings page where you can gather more details about the security issues.

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