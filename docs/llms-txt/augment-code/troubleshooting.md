# Source: https://docs.augmentcode.com/codereview/troubleshooting.md

# Troubleshooting

> Common issues and solutions for Augment Code Review setup and configuration.

## Known issues and Remediations

### Stuck on Install button

If you still see the "Install" button on the Augment Code Review Settings page, then the Augment GitHub App installation failed. You will need to uninstall the Augment GitHub App from your organization and then reinstall it. Make sure the person installing the GitHub app has an Augment account and they see the "All set!" text after installing the app.

<Steps>
  <Step title="Navigate to the Augment GitHub App settings page on GitHub">
    Follow the steps on [GitHub Docs](https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps#navigating-to-the-github-app-you-want-to-review-or-modify) to modify the Augment GitHub App installation.
  </Step>

  <Step title="Uninstall the Augment GitHub App from your organization">
    In the Danger zone section, click on "Uninstall"
  </Step>

  <Step title="Reinstall the Augment GitHub App">
    Follow the steps in [Configure Repo Access](/codereview/setup-guide-enterprise#configure-repo-access-inside-of-the-augment-github-app) again to install the app
  </Step>
</Steps>

### Unable to see the repositories from Organization just added

If you are unable to see the repositories from an organization you just added, then the Augment GitHub App installation failed for that organization. You will need to uninstall the Augment GitHub App from your organization and then reinstall it. Make sure the GitHub administrator installing the GitHub app has an Augment account and they see the "All set!" text after installing the app.

<Steps>
  <Step title="Navigate to the Augment GitHub App settings page on GitHub">
    Follow the steps on [GitHub Docs](https://docs.github.com/en/apps/using-github-apps/reviewing-and-modifying-installed-github-apps#navigating-to-the-github-app-you-want-to-review-or-modify) to modify the Augment GitHub App installation.
  </Step>

  <Step title="Uninstall the Augment GitHub App from your organization">
    In the Danger zone section, click on "Uninstall"
  </Step>

  <Step title="Reinstall the Augment GitHub App">
    Follow the steps in [Configure Repo Access](/codereview/setup-guide-enterprise#configure-repo-access-inside-of-the-augment-github-app) again to install the app
  </Step>
</Steps>


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.augmentcode.com/llms.txt