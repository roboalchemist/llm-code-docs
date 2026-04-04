# Source: https://help.aikido.dev/aikido-autofix/connect-private-packages/bundle-private-gems.md

# Bundler - Private Gems

For Aikido to update dependencies that include private gems, it needs access to your private gems so it can generate accurate AutoFixes. You can now provide private gem registry configuration in Aikido for this.

## Configuration in Aikido - Private RubyGems Registry <a href="#configuration-in-aikido---private-rubygems-registry" id="configuration-in-aikido---private-rubygems-registry"></a>

You can configure Aikido to authenticate with your private RubyGems registry when updating the dependencies by following the steps below:

1. Go to your account's settings page for the autofixer in Aikido, [here](https://app.aikido.dev/issues/fix/settings).
2. Click on "Connect Registry", the private registry modal will now be shown

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FGXsRHrinCvphowNcPbue%2Fimage.png?alt=media&#x26;token=693408d1-efc8-4ca0-bbd4-8e92d572df57" alt=""><figcaption></figcaption></figure>

1. Select "Bundler". In the example below, we show a possible setup for a private GitHub RubyGems registry. The environment variable key is `BUNDLE_RUBYGEMS__PKG__GITHUB__COM`, and the value is a GitHub access token with the `read:packages` scope. This will vary depending on the private registry you use.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2Fvc2ImefLErtPLmBIxREq%2Fimage.png?alt=media&#x26;token=a6f99f3f-e9bd-48d7-82a2-6543c539e2ed" alt=""><figcaption></figcaption></figure>

1. Click "Connect Registry" to save the configuration.

## Configuration in Aikido - Private Git Repository <a href="#configuration-in-aikido---private-rubygems-repository" id="configuration-in-aikido---private-rubygems-repository"></a>

### Same SCM organization <a href="#same-scm-organization" id="same-scm-organization"></a>

If the private git repository for the gem is in the same organization as the code being autofixed, you can extend the permissions of the existing access token to include access to the private repository [here](https://app.aikido.dev/issues/fix/settings).

### Different SCM organization <a href="#different-scm-organization" id="different-scm-organization"></a>

You can configure Aikido to authenticate with your private RubyGems git repositories when updating the dependencies by following the steps below:

1. Go to your account's settings page for the autofixer in Aikido, [here](https://app.aikido.dev/issues/fix/settings).
2. Click on "Connect Registry" and then select Bundler.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FGlAvdh72thMDVKT3PPdP%2Fimage.png?alt=media&#x26;token=d25cff3b-5052-4976-a7ca-d71c263a6d2e" alt=""><figcaption></figcaption></figure>

In the example above, we show a possible setup for a private GitHub Git repository. The environment variable key is `BUNDLE_GITHUB__COM`, and the value is a GitHub access token with repository access.

| Provider     | Environment Variable Key | Value Format                       |
| ------------ | ------------------------ | ---------------------------------- |
| GitHub       | `BUNDLE_GITHUB__COM`     | `x-access-token:your-access-token` |
| GitLab       | `BUNDLE_GITLAB__COM`     | `oauth2:your-access-token`         |
| Bitbucket    | `BUNDLE_BITBUCKET__ORG`  | `x-token-auth:your-access-token`   |
| Azure DevOps | `BUNDLE_DEV__AZURE__COM` | `:your-access-token`               |

1. Click "Connect Registry" to save the configuration.
