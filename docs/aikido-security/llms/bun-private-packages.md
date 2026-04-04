# Source: https://help.aikido.dev/aikido-autofix/connect-private-packages/bun-private-packages.md

# Bun - Private Packages

When Aikido updates dependencies in repositories that use private packages, it needs access to those packages to correctly update your lockfiles. You can configure Aikido to authenticate with your private NPM registry to run these updates.

## Prerequisites <a href="#prerequisites" id="prerequisites"></a>

Bun can use either `.npmrc` or `bunfig.toml`. See the [NPM documentation](https://help.aikido.dev/aikido-autofix/connect-private-packages/npm-private-packages) for more information about `.npmrc`.

### **Configuring `bunfig.toml`**

Private package access is defined in a `bunfig.toml` file in your project. See the Bun documentation [here](https://bun.com/docs/pm/scopes-registries).

If a `bunfig.toml` file is set in Aikido, we write the `bunfig.toml` file next to your `bun.lock` file before updating the dependencies. If the `bunfig.toml` file is pressent in the repository, it will be overwritten by the `.bunfig.toml` file set in Aikido.

## Configuration in Aikido <a href="#configuration-in-aikido" id="configuration-in-aikido"></a>

To allow repositories using private packages to be updated, provide your private registry configuration in the Aikido UI. Aikido stores the credentials encrypted and credentials cannot be retrieved through the Aikido UI or API.

1. Go to *Autofix* > *Settings* in Aikido, [here](https://app.aikido.dev/issues/fix/settings).
2. Click on "*Connect Registry*", and the selection modal will now be shown.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FOh0MigmVYd9fTmgdigMH%2Fimage.png?alt=media&#x26;token=00e433dc-7c67-4ee4-b4c9-bf3b674a4a4f" alt=""><figcaption></figcaption></figure>

1. Select Bun to input your `bunfig.toml` file. (Note that for `.npmrc`, you will need to select NPM.)

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FkWWDoZMEsp9Knj9z4WwN%2Fimage.png?alt=media&#x26;token=8a5f0edf-dda0-42ee-95b0-31959387b53b" alt=""><figcaption></figcaption></figure>

1. Fill in the contents of the `bunfig.toml`  file. The example shows a configuration for a scoped package (`@piedpiper`) hosted on GitHub Packages.
2. Click "*Connect Registry*" to save the configuration.
