# Source: https://mintlify.com/docs/deploy/github.md

# GitHub

> Connect to a GitHub repository for automated deployments, pull request previews, and continuous synchronization.

Mintlify uses a GitHub App to automatically sync your documentation with your GitHub repository.

## Installing the GitHub App

<Note>
  You must have organization ownership or administrator permissions in a repository to install the app. If you lack the necessary permissions, the repository owner must approve the installation request.
</Note>

Install the Mintlify GitHub App through your [dashboard](https://dashboard.mintlify.com/settings/organization/github-app).

<Tip>
  We recommend granting access only to the repository where your docs are hosted.
</Tip>

<Frame>
  <img className="h-80" alt="Mintlify GitHub App installation page with the 'Only select repositories' option selected." src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/github/select-repos.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=35cc7fc3564471ccef7a54029ef18cd4" data-og-width="2980" width="2980" data-og-height="1702" height="1702" data-path="images/github/select-repos.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/github/select-repos.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=2bc537826e2a4b843f5550650a488b61 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/github/select-repos.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=1ee9087af342383e3e3600b3a21e5e26 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/github/select-repos.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=3b36b83d3d85a31b64cedb0886a79ab3 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/github/select-repos.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=4b05fcc79d53b9401c2bbe937ff5667f 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/github/select-repos.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=799d62da575693367a5fa9c787064968 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/github/select-repos.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=cab163dcf7b60ff032f7c7ae09a712de 2500w" />
</Frame>

## Permissions

When you install the GitHub app, you will be prompted to grant the following permissions:

Read permissions:

* `metadata`: Basic repository information

Read and write permissions:

* `checks`: Create status checks on pull requests
* `code`: Read file changes when you commit to your docs branch
* `deployments`: Generate preview deployments for pull requests
* `pull requests`: Create branches and pull requests from the web editor

<Info>
  The app only accesses repositories that you explicitly grant it access to. If you have branch protection rules enabled, the app can't push directly to protected branches.
</Info>

## Managing repository access

When installing our GitHub App, you can grant access to all of your repositories or specific ones. We recommend only granting access to the repositories where your documentation is located. You can modify this selection anytime in your [GitHub app settings](https://github.com/apps/mintlify/installations/new).

## Configuring docs source

Change the organization, repository, or branch that your documentation is built from in the [Git Settings](https://dashboard.mintlify.com/settings/deployment/git-settings) section of your dashboard.

## GitHub Enterprise with IP allowlists

If your GitHub Enterprise Cloud organization has an IP allowlist enabled, you need to add Mintlify's egress IP address (`54.242.90.151`) to your allowlist for the GitHub App to function properly.

Follow [GitHub's documentation](https://docs.github.com/en/enterprise-cloud@latest/organizations/keeping-your-organization-secure/managing-security-settings-for-your-organization/managing-allowed-ip-addresses-for-your-organization) to configure your IP allowlist.

## Troubleshooting

### GitHub app connection issues

If you encounter problems with the GitHub app, resetting the connection can solve most problems.

<Steps>
  <Step title="Uninstall the Mintlify app through GitHub.">
    1. In GitHub, go to [installations](https://github.com/settings/installations) and select **Configure** next to the Mintlify app. Scroll down and select **Uninstall**.
    2. Go to [Authorized GitHub Apps](https://github.com/settings/apps/authorizations) and select **Revoke** next to the Mintlify app.
  </Step>

  <Step title="Reinstall the Mintlify app.">
    1. In your Mintlify dashboard, go to [Git Settings](https://dashboard.mintlify.com/settings/deployment/git-settings) and install the GitHub app.
    2. Authorize your account in the [My Profile](https://dashboard.mintlify.com/settings/account) section of your dashboard.
  </Step>
</Steps>

### Feedback add-ons are unavailable

If you cannot enable the edit suggestions or raise issues options in your dashboard and your repository is public, revalidate your Git settings.

<Steps>
  <Step title="Navigate to Git Settings">
    Go to [Git Settings](https://dashboard.mintlify.com/settings/deployment/git-settings) in your dashboard.
  </Step>

  <Step title="Revalidate your settings">
    Click the green check mark in the corner of the Git settings box to revalidate your repository settings. This will force update your repository settings to reflect whether your repository is public or private.

    <Frame>
      <img src="https://mintcdn.com/mintlify/0GhkFxoI6iPIzBkf/images/github/revalidate-settings-light.png?fit=max&auto=format&n=0GhkFxoI6iPIzBkf&q=85&s=b3c7c421876bb4a2921ece22fc4b4777" alt="The Git Settings page in the Mintlify dashboard. An orange arrow points to the green check mark that revalidates the repository settings." className="block dark:hidden" data-og-width="1996" width="1996" data-og-height="1168" height="1168" data-path="images/github/revalidate-settings-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/0GhkFxoI6iPIzBkf/images/github/revalidate-settings-light.png?w=280&fit=max&auto=format&n=0GhkFxoI6iPIzBkf&q=85&s=5788d2b87586e6ae6b96b25a27c6d00f 280w, https://mintcdn.com/mintlify/0GhkFxoI6iPIzBkf/images/github/revalidate-settings-light.png?w=560&fit=max&auto=format&n=0GhkFxoI6iPIzBkf&q=85&s=e872c3b592d441835267a344b0024a17 560w, https://mintcdn.com/mintlify/0GhkFxoI6iPIzBkf/images/github/revalidate-settings-light.png?w=840&fit=max&auto=format&n=0GhkFxoI6iPIzBkf&q=85&s=cd4b7c7445b9b080a00687d341f4819c 840w, https://mintcdn.com/mintlify/0GhkFxoI6iPIzBkf/images/github/revalidate-settings-light.png?w=1100&fit=max&auto=format&n=0GhkFxoI6iPIzBkf&q=85&s=0707fcbc7f54ce1f4655ea14de94b001 1100w, https://mintcdn.com/mintlify/0GhkFxoI6iPIzBkf/images/github/revalidate-settings-light.png?w=1650&fit=max&auto=format&n=0GhkFxoI6iPIzBkf&q=85&s=e08810b8c1987134bb191385722f77e4 1650w, https://mintcdn.com/mintlify/0GhkFxoI6iPIzBkf/images/github/revalidate-settings-light.png?w=2500&fit=max&auto=format&n=0GhkFxoI6iPIzBkf&q=85&s=12ba6216beb5594c78bfafa9fb8c36d2 2500w" />

      <img src="https://mintcdn.com/mintlify/0GhkFxoI6iPIzBkf/images/github/revalidate-settings-dark.png?fit=max&auto=format&n=0GhkFxoI6iPIzBkf&q=85&s=9d2462cd3e07c9e7cf0835b3c50e3020" alt="The Git Settings page in the Mintlify dashboard. An orange arrow points to the green check mark that revalidates the repository settings." className="hidden dark:block" data-og-width="1998" width="1998" data-og-height="1170" height="1170" data-path="images/github/revalidate-settings-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/0GhkFxoI6iPIzBkf/images/github/revalidate-settings-dark.png?w=280&fit=max&auto=format&n=0GhkFxoI6iPIzBkf&q=85&s=7d5e0e13ef18a79ad21177dca48c0516 280w, https://mintcdn.com/mintlify/0GhkFxoI6iPIzBkf/images/github/revalidate-settings-dark.png?w=560&fit=max&auto=format&n=0GhkFxoI6iPIzBkf&q=85&s=a23c2cb529ab4a6764aa21a65dd1bc42 560w, https://mintcdn.com/mintlify/0GhkFxoI6iPIzBkf/images/github/revalidate-settings-dark.png?w=840&fit=max&auto=format&n=0GhkFxoI6iPIzBkf&q=85&s=d9ee92ccb7afbfea87ab21d47235da92 840w, https://mintcdn.com/mintlify/0GhkFxoI6iPIzBkf/images/github/revalidate-settings-dark.png?w=1100&fit=max&auto=format&n=0GhkFxoI6iPIzBkf&q=85&s=39fd714f39b4583a1f7c5dc8c5922765 1100w, https://mintcdn.com/mintlify/0GhkFxoI6iPIzBkf/images/github/revalidate-settings-dark.png?w=1650&fit=max&auto=format&n=0GhkFxoI6iPIzBkf&q=85&s=4bc8a85bfc148c6864423611db134c29 1650w, https://mintcdn.com/mintlify/0GhkFxoI6iPIzBkf/images/github/revalidate-settings-dark.png?w=2500&fit=max&auto=format&n=0GhkFxoI6iPIzBkf&q=85&s=2b00909bd2105e7ebbf59381c7bb9156 2500w" />
    </Frame>
  </Step>
</Steps>
