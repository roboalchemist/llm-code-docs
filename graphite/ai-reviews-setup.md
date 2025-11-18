# Source: https://graphite-58cc94ce.mintlify.dev/docs/ai-reviews-setup.md

# Setup & configuration

> Get started with AI reviews in under 5 minutes

## Getting started with AI reviews

AI reviews can be enabled in just a few clicks, with no configuration required to start catching bugs in your pull requests.

### Enabling AI reviews

1. Navigate to the [AI code review settings page](https://app.graphite.com/ai-reviews)

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-0.png?fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=c93f873df83987fa690cbd5cb1596185" data-og-width="2560" width="2560" data-og-height="1504" height="1504" data-path="images/ai-reviews-0.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-0.png?w=280&fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=32e47daee026863bc223dd7af8ebb2a8 280w, https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-0.png?w=560&fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=c6f02f81ca7811bb671c817884125ff6 560w, https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-0.png?w=840&fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=7296f326b5a8f789acdf27d92acd287e 840w, https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-0.png?w=1100&fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=e6ae203e53994de04ea9c9b5ed2fe659 1100w, https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-0.png?w=1650&fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=3156ff930c22f48b3a12b57df07ff689 1650w, https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-0.png?w=2500&fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=2e465d8e8d70d084028d9b344e24a65a 2500w" />
</Frame>

2. Click "Enable automatic reviews" to set up Graphite Agent to review PRs automatically

3. Select the repositories where you want AI reviews enabled
   * You can choose specific repositories or enable AI reviews across your entire organization
   * If you don't see the repositories you're looking for, make sure they're [synced with Graphite](https://app.graphite.com/settings/synced-repos)

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-1.png?fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=621edc4550a8583f0270d3c7c1299403" data-og-width="2560" width="2560" data-og-height="1504" height="1504" data-path="images/ai-reviews-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-1.png?w=280&fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=e27e6ac0b5c379c4d32e72c76fc8616f 280w, https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-1.png?w=560&fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=e11f69fec61b6041b35789f35d6d8c0f 560w, https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-1.png?w=840&fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=6ba302f98069c99128407f944da1b1be 840w, https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-1.png?w=1100&fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=62266dd6b1aa3f42633cdad8748fe2db 1100w, https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-1.png?w=1650&fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=4d564c8635511e3366ecfccef0681527 1650w, https://mintcdn.com/graphite-58cc94ce/ICBXK7d1j0p5cvvq/images/ai-reviews-1.png?w=2500&fit=max&auto=format&n=ICBXK7d1j0p5cvvq&q=85&s=1de9e1d19efb3f35212f51dd75e4b30e 2500w" />
</Frame>

4. Click "Done" to save your settings. Graphite Agent will now automatically review all new pull requests in the selected repositories

### What happens next

Once enabled, Graphite Agent:

* Automatically analyzes new pull requests in the selected repositories
* Comments directly on pull requests when it finds potential issues
* Suggests fixes for the problems it identifies

Graphite Agent works behind the scenes, with no changes required to your existing PR workflow. Your team can continue using GitHub just as they do today, with Graphite Agent providing additional feedback alongside human reviewers.

For teams using continuous integration, Graphite Agent works alongside your test suite to catch issues that tests often miss, like logic bugs, edge cases, and security vulnerabilities.

## Enabling AI reviews on personal repositories

In order to enable AI reviews on your personal repositories, you must first install the Graphite GitHub App on your personal account.

1. Navigate to your [GitHub authentication settings page](https://app.graphite.com/settings)

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/fea9a14c-1752606292-diamond-product-images_0004_01-enabling-personal.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=b4789c7b73c1c0ab577b728a1c79ab57" data-og-width="2840" width="2840" data-og-height="2160" height="2160" data-path="images/fea9a14c-1752606292-diamond-product-images_0004_01-enabling-personal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/fea9a14c-1752606292-diamond-product-images_0004_01-enabling-personal.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=3d94cfef51da895fecc12274c147fbb9 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/fea9a14c-1752606292-diamond-product-images_0004_01-enabling-personal.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=b01150fee43820fa027e45b8fe1e629e 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/fea9a14c-1752606292-diamond-product-images_0004_01-enabling-personal.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=317bf76986e066a284540b72c6ce6db1 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/fea9a14c-1752606292-diamond-product-images_0004_01-enabling-personal.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=ada9f41ad3961dde58ea8393172a8e80 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/fea9a14c-1752606292-diamond-product-images_0004_01-enabling-personal.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=54f679ac0bd2c0848682bb9a1bd59e9d 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/fea9a14c-1752606292-diamond-product-images_0004_01-enabling-personal.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=7949f9ad67e04aa2ff2eb734441917c8 2500w" />
</Frame>

2. If this is your first time authenticating Graphite using the GitHub App, select the "Install GitHub App" button; otherwise, select the "Add organization" button.

3. Install the Graphite GitHub App using the pop-up window that appears, selecting your personal account's login.

<Frame>
  <img src="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/93c5fe56-1752606392-diamond-product-images_0004_02-installing-personal.png?fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=b3e957118043903a50ad26ffe51e0dfb" data-og-width="780" width="780" data-og-height="910" height="910" data-path="images/93c5fe56-1752606392-diamond-product-images_0004_02-installing-personal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/93c5fe56-1752606392-diamond-product-images_0004_02-installing-personal.png?w=280&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=6e16b8923bbebb2bd15ba61a0fb15c2a 280w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/93c5fe56-1752606392-diamond-product-images_0004_02-installing-personal.png?w=560&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=25a39d4b4ffd042177b331e43e79b11e 560w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/93c5fe56-1752606392-diamond-product-images_0004_02-installing-personal.png?w=840&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=f3c28c80f8d673e28d4659319006c617 840w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/93c5fe56-1752606392-diamond-product-images_0004_02-installing-personal.png?w=1100&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=1c3a8197b707cd63c8cc5ad283e4b33e 1100w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/93c5fe56-1752606392-diamond-product-images_0004_02-installing-personal.png?w=1650&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=b1c44e10dc81dfb913ced16048565d57 1650w, https://mintcdn.com/graphite-58cc94ce/v5snjlX4njZhFyeg/images/93c5fe56-1752606392-diamond-product-images_0004_02-installing-personal.png?w=2500&fit=max&auto=format&n=v5snjlX4njZhFyeg&q=85&s=36340374f27e21e8bffad5064428493b 2500w" />
</Frame>

4. After returning to the GitHub authentication settings page, click the "Join team" button next to your personal account's login.

After completing these steps, you can enable AI reviews on your personal account following the instructions for [Getting started with AI reviews](/ai-reviews-setup#getting-started-with-ai-reviews).

<Info>
  You can only enable AI reviews on personal repositories that you own.
</Info>

## Advanced configuration

While AI reviews work great out of the box, you can customize them to better fit your team's workflow and standards. See our [Customization](/ai-review-customization) page for details on:

* Setting up exclusions to prevent Graphite Agent from commenting on certain types of issues
* Creating custom rules that match your team's coding guidelines
* Excluding files from AI review analysis
