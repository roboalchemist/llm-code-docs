# Source: https://www.mintlify.com/docs/deploy/monorepo.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.mintlify.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Monorepo setup

> Configure documentation path and content directory for monorepo projects.

Configure Mintlify to deploy documentation from a specific directory within a monorepo. This setup allows you to maintain documentation alongside your code in repositories that contain multiple projects or services.

## Prerequisites

* Admin access to your Mintlify project.
* Documentation files organized in a dedicated directory within your monorepo.
* A valid `docs.json` in your documentation directory.

## Configure monorepo deployment

<Steps>
  <Step title="Access Git settings">
    Navigate to [Git Settings](https://dashboard.mintlify.com/settings/deployment/git-settings) in your dashboard.

    <Frame>
      <img className="block dark:hidden my-0 pointer-events-none" src="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/monorepo-light.png?fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=796f90a80651694cb858c77f4f1145a8" alt="The project settings panel in the Git Settings menu. The Set up as monorepo toggle button is enabled and a path to the /docs directory is specified." data-og-width="1350" width="1350" data-og-height="900" height="900" data-path="images/monorepo-light.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/monorepo-light.png?w=280&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=097e11d375af49c9617962a77d2ce9c0 280w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/monorepo-light.png?w=560&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=f960d33286f33cd98ffd3e9f62b25be0 560w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/monorepo-light.png?w=840&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=e26e53043300bb5d6ff3bc2188403a18 840w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/monorepo-light.png?w=1100&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=dbbd8b22e7da94e7c7cb5dff758c4c21 1100w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/monorepo-light.png?w=1650&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=1c6427d476468f4a3377ad9c948b7058 1650w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/monorepo-light.png?w=2500&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=3e745697b35f6aa8c09ec488847b029a 2500w" />

      <img className="hidden dark:block my-0 pointer-events-none" src="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/monorepo-dark.png?fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=03624a6ce64b3c3d504e27585cf857aa" alt="The project settings panel in the Git Settings menu. The Set up as monorepo toggle button is enabled and a path to the /docs directory is specified." data-og-width="1350" width="1350" data-og-height="900" height="900" data-path="images/monorepo-dark.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/monorepo-dark.png?w=280&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=afcec75c9db2d7ecfff4a1930f991fc3 280w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/monorepo-dark.png?w=560&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=ec31e2a26d6e744530db890ffaa3e435 560w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/monorepo-dark.png?w=840&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=6d2915f5e45882bdc0c333e9db950939 840w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/monorepo-dark.png?w=1100&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=85f043394c8d5eb8b97b75bfa4f56e4c 1100w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/monorepo-dark.png?w=1650&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=5efddceac87ddd8ca95c627f9c8ac8b4 1650w, https://mintcdn.com/mintlify/Y6rP0BmbzgwHuEoU/images/monorepo-dark.png?w=2500&fit=max&auto=format&n=Y6rP0BmbzgwHuEoU&q=85&s=c5d92cfbf8d90ddf69325c206c50e577 2500w" />
    </Frame>
  </Step>

  <Step title="Set your documentation path">
    1. Select the **Set up as monorepo** toggle button.
    2. Enter the relative path to your docs directory. For example, if your docs are in the `docs` directory, enter `/docs`.

    <Note>
      Do not include a trailing slash in the path.
    </Note>

    3. Select **Save changes**.
  </Step>
</Steps>
