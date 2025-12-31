# Source: https://docs.augmentcode.com/codereview/setup-guide-otherplans.md

# Setup Guide for All Other Plans

> Get started with Augment Code Review for Indie, Standard and Max plans.

export const GitHubLogo = () => <svg width="24" height="24" viewBox="0 0 15 15" fill="none" xmlns="http://www.w3.org/2000/svg">
    <path fill-rule="evenodd" clip-rule="evenodd" d="M7.49933 0.25C3.49635 0.25 0.25 3.49593 0.25 7.50024C0.25 10.703 2.32715 13.4206 5.2081 14.3797C5.57084 14.446 5.70302 14.2222 5.70302 14.0299C5.70302 13.8576 5.69679 13.4019 5.69323 12.797C3.67661 13.235 3.25112 11.825 3.25112 11.825C2.92132 10.9874 2.44599 10.7644 2.44599 10.7644C1.78773 10.3149 2.49584 10.3238 2.49584 10.3238C3.22353 10.375 3.60629 11.0711 3.60629 11.0711C4.25298 12.1788 5.30335 11.8588 5.71638 11.6732C5.78225 11.205 5.96962 10.8854 6.17658 10.7043C4.56675 10.5209 2.87415 9.89918 2.87415 7.12104C2.87415 6.32925 3.15677 5.68257 3.62053 5.17563C3.54576 4.99226 3.29697 4.25521 3.69174 3.25691C3.69174 3.25691 4.30015 3.06196 5.68522 3.99973C6.26337 3.83906 6.8838 3.75895 7.50022 3.75583C8.1162 3.75895 8.73619 3.83906 9.31523 3.99973C10.6994 3.06196 11.3069 3.25691 11.3069 3.25691C11.7026 4.25521 11.4538 4.99226 11.3795 5.17563C11.8441 5.68257 12.1245 6.32925 12.1245 7.12104C12.1245 9.9063 10.4292 10.5192 8.81452 10.6985C9.07444 10.9224 9.30633 11.3648 9.30633 12.0413C9.30633 13.0102 9.29742 13.7922 9.29742 14.0299C9.29742 14.2239 9.42828 14.4496 9.79591 14.3788C12.6746 13.4179 14.75 10.7025 14.75 7.50024C14.75 3.49593 11.5036 0.25 7.49933 0.25Z" fill="currentColor" />
  </svg>;

## Using Augment Code Review

Augment Code Review is available as an add-on feature for individuals and teams. It provides automated code review directly in GitHub, helping you catch bugs and improve code quality before merging. Backed by Augment’s industry-leading Context Engine, the agent understands your codebase at a deep level, providing reviews that are more meaningful and account for codebase-wide effects. Augment prioritizes high signal-to-noise ratio by focusing on high-impact issues like bugs, security concerns, correctness, and cross-system problems while avoiding low-value style nags.

## About the installation process

Visit [app.augmentcode.com/settings/code-review](https://app.augmentcode.com/settings/code-review) and log in. Settings are accessible to all [Team members](https://docs.augmentcode.com/teams/teams-admin-guide), but only configurable by Administrators of the plan.

### Configure Repo Access inside of the Augment GitHub App

Administrators can configure repositories by clicking "Connect GitHub" to launch the Augment GitHub App. This will redirect you to GitHub to provide permissions for all the repos you grant Augment Code Review to engage.

<img src="https://mintcdn.com/augment-mtje7p526w/FgCJvC4YnrBH__na/images/code-review-config.png?fit=max&auto=format&n=FgCJvC4YnrBH__na&q=85&s=7550fe19d7325fb543f9397b69c96897" alt="Code Review Settings Configure button" className="rounded-xl" data-og-width="1684" width="1684" data-og-height="673" height="673" data-path="images/code-review-config.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/FgCJvC4YnrBH__na/images/code-review-config.png?w=280&fit=max&auto=format&n=FgCJvC4YnrBH__na&q=85&s=2b2253b7553ba011f15578054d9c935c 280w, https://mintcdn.com/augment-mtje7p526w/FgCJvC4YnrBH__na/images/code-review-config.png?w=560&fit=max&auto=format&n=FgCJvC4YnrBH__na&q=85&s=129012170849332ad91791c8b29444e6 560w, https://mintcdn.com/augment-mtje7p526w/FgCJvC4YnrBH__na/images/code-review-config.png?w=840&fit=max&auto=format&n=FgCJvC4YnrBH__na&q=85&s=a8cba3de4f8f49ed4863f5d3dc0cc54d 840w, https://mintcdn.com/augment-mtje7p526w/FgCJvC4YnrBH__na/images/code-review-config.png?w=1100&fit=max&auto=format&n=FgCJvC4YnrBH__na&q=85&s=d5e232fa66090da6f9a9de4963a643f1 1100w, https://mintcdn.com/augment-mtje7p526w/FgCJvC4YnrBH__na/images/code-review-config.png?w=1650&fit=max&auto=format&n=FgCJvC4YnrBH__na&q=85&s=ba16119830ce52ebc0289ad0a541695d 1650w, https://mintcdn.com/augment-mtje7p526w/FgCJvC4YnrBH__na/images/code-review-config.png?w=2500&fit=max&auto=format&n=FgCJvC4YnrBH__na&q=85&s=c1d8b0dbaf89db6ded5b44c99e37b3f2 2500w" />

If your firewall configuration, allowlist or network policy requires a static IP for this integration, please refer to our [static IP address](https://docs.augmentcode.com/setup-augment/static-ip-support#allow-augment-traffic-from-static-ips) documentation.

<AccordionGroup>
  <Accordion title="Who can install the Augment GitHub App?">
    To install the Augment GitHub App, you will need to be an Administrator of your GitHub organization. To find who the Administrators are, visit your GitHub organization settings page and click on "People." Administrators are listed under "Owners."

    <img src="https://mintcdn.com/augment-mtje7p526w/V_zyvyrMw4E2FxEk/images/code-review-owners.png?fit=max&auto=format&n=V_zyvyrMw4E2FxEk&q=85&s=0f6779df0d8a446bacbb4df0575c7cd0" alt="GitHub Admins" className="rounded-xl" data-og-width="2010" width="2010" data-og-height="1284" height="1284" data-path="images/code-review-owners.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/V_zyvyrMw4E2FxEk/images/code-review-owners.png?w=280&fit=max&auto=format&n=V_zyvyrMw4E2FxEk&q=85&s=2654775b944c43922376d86b98e22175 280w, https://mintcdn.com/augment-mtje7p526w/V_zyvyrMw4E2FxEk/images/code-review-owners.png?w=560&fit=max&auto=format&n=V_zyvyrMw4E2FxEk&q=85&s=63d0c59812fb1d4f0e747d67e65efa46 560w, https://mintcdn.com/augment-mtje7p526w/V_zyvyrMw4E2FxEk/images/code-review-owners.png?w=840&fit=max&auto=format&n=V_zyvyrMw4E2FxEk&q=85&s=ae3ce426fada48f9464c54981e1a93e7 840w, https://mintcdn.com/augment-mtje7p526w/V_zyvyrMw4E2FxEk/images/code-review-owners.png?w=1100&fit=max&auto=format&n=V_zyvyrMw4E2FxEk&q=85&s=cc6ca0802f7d540c107b4e414b8f96a3 1100w, https://mintcdn.com/augment-mtje7p526w/V_zyvyrMw4E2FxEk/images/code-review-owners.png?w=1650&fit=max&auto=format&n=V_zyvyrMw4E2FxEk&q=85&s=96124ffa1c0c7689a4b2b485189ac871 1650w, https://mintcdn.com/augment-mtje7p526w/V_zyvyrMw4E2FxEk/images/code-review-owners.png?w=2500&fit=max&auto=format&n=V_zyvyrMw4E2FxEk&q=85&s=1f74e1e9fb88262a6a1399af1db2e06c 2500w" />
  </Accordion>
</AccordionGroup>

Once you finish installing the GitHub app, you should see a green checkmark with the text "All set!". Then, back in the Augment Code Review Settings, should now show a green "Installed" badge. If you do not see either of these, you may need to uninstall the app through GitHub and reinstall it. See [Troubleshooting](/codereview/troubleshooting#stuck-on-install-button) for more help.

<img src="https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-github-integration-success.png?fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=f4a0990fb97f3348aa6479f7227ea882" alt="GitHub App Installed" className="rounded-xl" data-og-width="813" width="813" data-og-height="627" height="627" data-path="images/code-review-github-integration-success.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-github-integration-success.png?w=280&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=099cafaf756d8b53438815d57695a266 280w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-github-integration-success.png?w=560&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=67f73fe4016247bb8f4c331cf77a1b81 560w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-github-integration-success.png?w=840&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=83b3050a8120ec5ed27f63bc48dd311f 840w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-github-integration-success.png?w=1100&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=873defdc8762e23920704f7c618ee1e6 1100w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-github-integration-success.png?w=1650&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=c296b2b5bbfae6af4caf0e8f6c71323b 1650w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-github-integration-success.png?w=2500&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=7cccceea467427c5b923c4730f406b4e 2500w" />

### Permissions requested by the Augment GitHub App:

* Contents, read-only: Clone repositories

* Pull Requests, read and write: Read pull requests and post comments to pull requests

* Issues, read-only: Read top-level PRs / Issues

* Organization Members, read-only: Read members of an organization, to distinguish internal and external users and their access levels to Augment features

Organization owners and repository admins can install the app directly; others will need owner approval. See [GitHub documentation](https://docs.github.com/en/apps/using-github-apps/installing-a-github-app-from-a-third-party) for details.

<img className="block rounded-xl" src="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/install-github-app.png?fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=5e4084c99c0295b0f64244970b63b7c1" alt="Installing the GitHub app on a single repository" data-og-width="1372" width="1372" data-og-height="1387" height="1387" data-path="images/install-github-app.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/install-github-app.png?w=280&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=74db4d5e2ebb869baec7fa8a5542fe1e 280w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/install-github-app.png?w=560&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=124a9fff587698addbf6521b889b5c28 560w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/install-github-app.png?w=840&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=3141ed13276ff2da9a123ad94d1d98b9 840w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/install-github-app.png?w=1100&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=aa841e9121554b8c1a75c35097e0d84b 1100w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/install-github-app.png?w=1650&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=7abe3b886150b097a11ae90b41cae3f1 1650w, https://mintcdn.com/augment-mtje7p526w/r-azeXhOS4FbEUi5/images/install-github-app.png?w=2500&fit=max&auto=format&n=r-azeXhOS4FbEUi5&q=85&s=333c129e393ab4b32f04c3940492cf1c 2500w" />

You can modify repository access anytime in the Augment GitHub App settings.

### Configuring Triggers Per Repository

As the Administrator, you control when Augment Code Review triggers via [Settings](https://app.augmentcode.com/settings/code-review). Look for "Set Review Trigger" to the right of the repository name.

* **Automatic**: Augment Code Review will automatically review and post a comment as soon as the PR is opened for review in GitHub. Use it when your teams want immediate feedback on all pull requests.

* **Manual Command**: Augment Code Review is only triggered when someone comments on the PR with any of the following:  `auggie review`, `augment review`, or `augmentcode review` on GitHub. Use it when you want full control over when a review happens.

* **Disabled**: Augment Code Review will not run on the repository.

<img src="https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-settings-triggers.png?fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=96c0f0dfc2186287a71bba713f7c31a6" alt="Trigger Types" className="rounded-xl" data-og-width="685" width="685" data-og-height="403" height="403" data-path="images/code-review-settings-triggers.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-settings-triggers.png?w=280&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=ec552a7eb0b39e85a412d191bf3c9c19 280w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-settings-triggers.png?w=560&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=1cf11f2ee10f617961a22c17f36a6366 560w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-settings-triggers.png?w=840&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=61f0470d5754359fa3a4375cc3112b46 840w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-settings-triggers.png?w=1100&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=b2199c1921299daf014149220d31c120 1100w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-settings-triggers.png?w=1650&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=fc80b5456761c3cf534b3db831fb52af 1650w, https://mintcdn.com/augment-mtje7p526w/hzSJfA0z3IKtZraV/images/code-review-settings-triggers.png?w=2500&fit=max&auto=format&n=hzSJfA0z3IKtZraV&q=85&s=83c4d15d7a40b8253a01803de97354b8 2500w" />

If the repo is set to "Automatic" or "Manual Command", to run additional rounds of reviews on a subsequent commit of any PR, you can use the same manual trigger keywords (`auggie review`, `augment review`, or `augmentcode review`).

On public repositories, reviews are only triggered for PRs whose authors are members of the GitHub organization, outside collaborators to the organization or repository, or contributors to that repository.

<Note>
  If you are an Enterprise customer, please refer to the [Enterprise setup guide](/codereview/setup-guide-enterprise) for additional information.
</Note>

## Questions?

If you have questions about Augment Code Review or want to learn more about Enterprise features:

* Visit our [Support Center](https://support.augmentcode.com/)
* Join our [Subreddit](https://www.reddit.com/r/AugmentCodeAI/)
* Contact Us [Augment Support](https://portal.usepylon.com/augment-code/forms/augment-support)

## Related Resources

* [Code Review Overview](/codereview/overview) - Learn about Code Review features
* [Fix with Augment](/codereview/fix-with-augment) - Automatically fix issues in your IDE
* [Setup Guide for Enterprise](/codereview/setup-guide-enterprise) - Full setup instructions for Enterprise


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.augmentcode.com/llms.txt