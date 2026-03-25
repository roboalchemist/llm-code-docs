# Source: https://docs.jit.io/docs/gitlab-integration-method-fastest.md

# GitLab integration method - Fastest

## Step-by-step guide for the 'Fastest' integration method

### OAuth Integration

Use Jit's OAuth integration to connect your GitLab account for a quick and seamless setup. Once connected, we’ll run validation tests on the token. If any issues arise, clear guidance will be provided to resolve them.

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