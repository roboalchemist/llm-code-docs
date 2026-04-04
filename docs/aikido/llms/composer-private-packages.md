# Source: https://help.aikido.dev/aikido-autofix/connect-private-packages/composer-private-packages.md

# Composer - Private Packages

For Aikido to update dependencies that include private packages, it needs access to your private registries so it can generate accurate lockfile updates. A Composer registry can be set up by providing an `auth.json` file.

## Prerequisites <a href="#prerequisites" id="prerequisites"></a>

**Prepare auth.json**

For private Composer packages, Aikido uses a `auth.json` file to authenticate with the private registry. This file will overwrite the auth.json in the root of the repository before the AutoFix starts but will not be added as part of the Pull Request. It is possible to configure multiple private registries in this file.

Example `auth.json` for accessing private packages on GitHub's Composer registry:

```
{
    "github-oauth": {
        "github.com": "<your-github-token>"
    }
}
```

## Configuration in Aikido <a href="#configuration-in-aikido" id="configuration-in-aikido"></a>

Once write access to the repos is set up, you can configure Aikido to authenticate with your private Composer registry by following the steps below:

1. Go to your account's settings page for the Autofix in Aikido, [here](https://app.aikido.dev/issues/fix/settings).
2. Click on "*Connect Registry*", the modal below will now be shown

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FIhdNyFaaHutiDFqwW9xy%2Fimage.png?alt=media&#x26;token=b24934e5-1e56-416a-86a3-3b41d65b9b5e" alt=""><figcaption></figcaption></figure>

3. Select "Composer" as package manager

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FnpiXFcNK1q404DLXLI1M%2Fimage.png?alt=media&#x26;token=2656df79-b625-42d8-a20e-155ed90e1962" alt=""><figcaption></figcaption></figure>

4. Fill in your auth.json with authentication information. Aikido securely encrypts your configuration file until just before they are used.
5. Click "*Connect Registry*" to save the configuration
