# Source: https://docs.jit.io/docs/integrating-with-github.md

# Connect Jit with your GitHub Account

To connect Jit with your GitHub account, follow the steps below. You can also watch this [3 minute demonstration](https://www.youtube.com/watch?v=ILSeFZV3uMc\&list=PL3n0k_nT7KkDtJ4gZF_ZhZAa-K7KBkHuq\&index=18).

## Create an account and begin the Quick Start flow

* [Log in](https://platform.jit.io/login) to your Jit account.
* This will bring you to our Quick Start Guide, where you’ll be directed to “Integrate Source Code Manager”. Hit the GitHub icon.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/1328dbbd6a2248f194828cb341fb3a095e4c92e755f6be628b99945b54d301c7-Screenshot_2024-11-13_at_4.32.45_PM.png",
        "",
        ""
      ],
      "align": "center",
      "sizing": "600px",
      "border": true
    }
  ]
}
[/block]

## Install the Jit app on GitHub through the Integration Wizard

* You’ll be prompted to install the Jit app on GitHub. This will provide Jit access to your repositories and enable continuous scanning. To learn more about the relevant permissions, see the “Required permissions” section at the bottom of the page. Hit “Install”.
* Select the relevant GitHub Organization.
* Choose whether to scan all repositories in the GitHub Organization or select specific repositories to scan. **Selecting “All repositories” will automatically scan future repositories as they’re created.**

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/c7a61ce303f670783097ef2186a6162d7d04144853ebc4db0312fea4c948a603-Screenshot_2024-11-13_at_4.45.13_PM.png",
        "",
        ""
      ],
      "align": "center",
      "sizing": "600px",
      "border": true
    }
  ]
}
[/block]

* Click on the **Install & Authorize** button.
* Click on the **Next** button and select a repo to store Jit’s config files, or create a new repository. This enables Jit to trigger scans within your GitHub environment, so that Jit doesn’t need to pull your code to our environment. This also enables users to manage Jit configs as code.
* Click on the **Finish** button.

## Jit is now scanning your codebase!

Now that you’ve implemented the integration with GitHub, Jit will automatically begin scanning your codebase (or the repositories you selected).

Specifically, Jit will activate the SCA, SAST, and Secrets Detection tools – these scanners will detect known vulnerabilities in your open-source components, security flaws in your custom code, and hardcoded secrets, respectively.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/1cebf870a29a5dd84aa329703dfe95e204d5add31c13f547d9ddd5b7f5c652a8-Screenshot_2024-10-16_at_11.06.59_AM.png",
        "",
        ""
      ],
      "align": "center",
      "sizing": "600px",
      "border": true
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
      "align": "center",
      "sizing": "600px",
      "border": true
    }
  ]
}
[/block]

> 👍 Success!
>
> You are good to go.
>
> Click [Explore Jit's features](https://docs.jit.io/docs/explore-jit) to learn how Jit prioritizes your security risks, enables continuous scanning for developers, integrates with a notification system, and much more.

## Required permissions

When installed, the Jit GitHub app requires the following permissions in GitHub:

| Permission                                                             | Purpose                                                                                                                    |
| :--------------------------------------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- |
| Read access to administration, issues, and metadata                    | Enables Jit to monitor repository creation or deletion events, and access repository metadata.                             |
| Read and write access to actions, checks, pull requests, and workflows | Enables Jit to trigger workflows, create and update PR checks, create and update pull requests, and modify workflow files. |
| Read and write access to content                                       | Enables Jit to detect vulnerabilities in code and open remediation PRs in a new branch.                                    |
| Read access to members                                                 | Enables Jit to list and map teams and membership                                                                           |
| Read and write access to deployment (future feature)                   | Enables Jit to run security requirements on new deployments and block deployments based on security findings.              |

## Connecting Multiple GitHub Organizations

Jit supports connecting multiple GitHub organizations to a single tenant.\
This is useful for companies that split repositories across several GitHub orgs but want unified security visibility and orchestration.

### How it works

* Jit uses a GitHub App for integration.
* To connect multiple organizations, the same GitHub App must be installed separately on each GitHub organization.
* Each installation is authorized independently at the organization level.
* Repositories are grouped by organization and managed under the same Jit tenant.

### Adding another GitHub organization

You can add additional GitHub organizations in one of the following ways:

* **During initial setup** via the Quick Start SCM setup step.

1. Navigate to the **Quick Start Guide → View all steps → SCM Setup**
2. Click the **+ Add GitHub Org** button found within the GitHub card

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/2240beb3d40c0df054167ca728598f9843e57e2d6e056c448feb4117909f107a-image.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "600px",
      "border": true
    }
  ]
}
[/block]

* **After onboarding** from **Settings → Integrations → GitHub**, by selecting **Add GitHub Org**.

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/13f752b627246edfa2c235d0376c2770358b7cef97d8e9826f8a06a464fd5276-image.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "500px"
    }
  ]
}
[/block]

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/f59afd127e6919e989b0a9b26ba006643aab33f61e5fc7225448f1b40e8978b7-image.png",
        null,
        ""
      ],
      "align": "center",
      "sizing": "500px"
    }
  ]
}
[/block]