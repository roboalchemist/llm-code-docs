# Source: https://docs.jit.io/docs/integrating-with-npm-registry.md

# NPM registry Integration

Integrating with npm registry

Integrating your private **npm** registry into Jit enhances your organization's security by enabling Jit to scan for dependencies vulnerabilities (SCA) in both your public and private **npm** packages. Our guide provides clear steps for a secure setting of this integration.

## Requirements

1. [Jit GitHub integration](https://docs.jit.io/docs/integrating-with-github) or [Jit GitLab integration](https://docs.jit.io/docs/integrating-with-gitlab)
2. **npm** private packages.
   * A private npm registry helps safeguard internal libraries by preventing public exposure and enables the consolidation of multiple registries from various sources into a single endpoint. Learn more [About private packages](https://docs.npmjs.com/about-private-packages) and [Creating and publishing private packages](https://docs.npmjs.com/creating-and-publishing-private-packages).
3. A **read-only** access token to integrate into the private npm packages.
   * For more details on creating the tokens, see [Using private packages in a CI/CD workflow](https://docs.npmjs.com/using-private-packages-in-a-ci-cd-workflow).

## Activating the SCA Plan

1. Go to **Security Plans**, locate **Jit MVS**, and click on **View Plan**.  (Learn more on [Jit MVS](https://docs.jit.io/docs/jit-mvs-for-appsec-plan))
2. In **Application Security**, locate **Scan Your Code Dependencies for Vulnerabilities (SCA)**, and click **Activate**. (Learn more on  [Scan Your Code Dependencies for Vulnerabilities (SCA)](https://docs.jit.io/docs/scan-code-dependencies-for-vulnerabilities))
3. A pop-up will appear. Mark **Integrate with a private registry** and click **Connect**

![](https://files.readme.io/25fffcb-image.png)

4. Enter the access token you've generated and click **Create secret**

[block:image]
{
  "images": [
    {
      "image": [
        "https://files.readme.io/dd3cef3-image.png",
        null,
        ""
      ],
      "align": "center"
    }
  ]
}
[/block]

> 👍 That's it. Jit will now scan your private packages as well.

## Additional options to activate, including existing users

1. Add the secret directly to [Secrets](https://docs.jit.io/docs/secrets). The name **must** be **NPM\_REGISTRY\_TOKEN**
2. Locate the tool under [Integrations](https://docs.jit.io/docs/integrations-page) and click **Connect**

![](https://files.readme.io/53647da-image.png)

If the security requirement is already activated (e.g., for existing users), the integration will start to take effect in the following scan

> 🚧 Pay attention! In these options, you will still need to click activate on the SCA security requirement under Jit MVS plan
>
> The pop-up will be skipped

## Deactivating the integration

1. Go to the [Secrets](https://docs.jit.io/docs/secrets) and delete the **NPM\_REGISTRY\_TOKEN** token.
2. Revoke the token on **npm** side, see [Revoking access tokens](https://docs.npmjs.com/revoking-access-tokens).