# Source: https://docs.jit.io/docs/gitlab-integration-method-fast.md

# GitLab integration method - Fast

## Step-by-step guide for the 'Fast' integration method

### Create Token

The "Fast" method requires a token to grant Jit access to your GitLab projects with maintainer-level permissions. This token is essential for automating security scans and ensuring Jit can monitor your repositories. By using a token, you maintain control over the permissions granted, aligning with your security preferences.

Follow these steps to create a group access token:

1. In GitLab, navigate to 'Group → Settings → Access tokens.’\
   & click 'Add new token.'
2. Fill out the form for 'Add a group access token' with the following data:

| Field           | Value                   |
| :-------------- | :---------------------- |
| Token name      | Any name of your choice |
| Expiration date | 1 year                  |
| Role            | Maintainer              |
| Scope           | api                     |

3. Click on Create group access token.
4. Paste the token you’ve created to the designated place.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/c65a79d557b81fa61ad8ad567f7b7718d472755cc04d3321f09a2a17f70da1ef-image.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "400px"
    }
  ]
}
[/block]

### Choose a Group

First, select the group you want Jit to integrate with from the first dropdown menu. Note that Jit integrates with only one group to simplify setup and ensure a streamlined security process. In the next step, Jit will create a dedicated project within the selected group to ensure smooth operation. This dedicated project allows Jit to run scans locally **without ever pulling your code to the cloud.**

By default, the project is created in the group's root folder. Using the second dropdown menu, you can select a specific subgroup for the dedicated project if you prefer a different location.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/736baca06eeb417cd3bbf988497ecf0d853e46f65194fdd354b128b1092409bf-image.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "400px"
    }
  ]
}
[/block]

### Create Webhooks

The "Fast" method requires you to manually create webhooks to enable Jit to trigger security scans for new merge requests, code changes, and new repository creation. Webhooks ensure that Jit receives the necessary notifications to initiate scans, providing real-time monitoring without requiring elevated permissions and scanning new repositories without the user having to add them to coverage manually. Follow these steps to set up webhooks in GitLab:

1. In GitLab, Navigate to Group Settings > Webhooks and click **add a new webhook**
2. Fill out the form using the following data:

[block:parameters]
{
  "data": {
    "h-0": "Field",
    "h-1": "Value",
    "0-0": "URL",
    "0-1": "<https://api.jit.io/gitlab/webhook>",
    "1-0": "Header Name",
    "1-1": "Tenant-Id",
    "2-0": "Header Value",
    "2-1": "Will be provided by Jit (the internal ID of your Jit Tenant)",
    "3-0": "Header Name",
    "3-1": "Installation-Id",
    "4-0": "Header Value",
    "4-1": "the group ID you plan to integrate with",
    "5-0": "Secret Token",
    "5-1": "choose a password",
    "6-0": "Trigger",
    "6-1": "Choose:  \n  \n- Push events (Wildcard pattern)\n- Project events\n- Comments\n- Subgroup events\n- Merge request events\n- Deployment events"
  },
  "cols": 2,
  "rows": 7,
  "align": [
    "left",
    "left"
  ]
}
[/block]

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/144a8cf10e4d5226c4052ade6cb699d948caf50818c904421ab56f8b8620ad8a-image.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "600px"
    }
  ]
}
[/block]

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f46b5d13d5eb56a8938f93d4418c5928451128d090872cecedc0a078567aa314-image.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "600px"
    }
  ]
}
[/block]

3. Press 'add webhook'
4. Paste the Secret Token you’ve created to the designated place in Jit's installation wizard

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2b6489dcdc14d3af46afd989fd4e9dae16aab94da82328c7f2ef3e8249f79f32-image.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "500px"
    }
  ]
}
[/block]

Once the webhooks are created, we’ll validate them to ensure they are configured correctly.

### Choose Projects

Choose which projects you would like Jit to cover:

**Recommended**: Select All projects to protect existing and newly created repositories automatically. This option ensures that Jit scans all repositories for security vulnerabilities, including new ones, without requiring any manual configuration. When needed, repositories can later be excluded in [Manage Resources](https://docs.jit.io/docs/manage-resources).

Alternatively, you can choose to have Jit cover only selected projects by selecting the second option. This allows for more granular control but requires manual updates to add new repositories to Jit’s coverage.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/45670915795118a14b8fc57cc0be9b26c201276e4cbc9a176d7c94d0d39a46ff-image.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "400px"
    }
  ]
}
[/block]

### Self-Hosted Runners

Specify whether you want to use GitLab SaaS runners or self-hosted runners. Once you make a selection, we’ll validate the runner configuration to ensure Jit has the required access.

* If you choose self-hosted runners, you will be directed to an additional configuration process.
* If you choose SaaS runners, the setup will proceed automatically.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/65a82a490fda61a4ce831e4f8bc40c68511aa1c4461377c662a2030a14cd359a-image.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "400px"
    }
  ]
}
[/block]

### Done!

Congratulations! Your GitLab integration is now complete. After pressing the 'Start Scanning' button, the scan will begin. You can then start monitoring your repositories via Jit and access detailed onboarding reports in the dashboard.

\*\*Note: Jit creates a project (repository) to store environmental configurations and run CI/CD pipelines. This project requires the 'Minimum role to use pipeline variables' setting in CI/CD settings to be set to 'Maintainer'. If after completing setup, control enablement appears to be stuck in a 'pending' state, verify this setting is configured correctly in the Jit project.