# Source: https://help.aikido.dev/aikido-autofix/connect-private-packages/custom-config-private-packages.md

# Environment Variables - Private Packages

For Aikido to update dependencies that include private packages, it needs access to your private registries so it can generate accurate lockfile updates. Many package manager like Bundle, Poetry, UV use environment variables to configure authentication. In Aikido you can proivde environment variables, which will be encrypted and injected into your workflows.

This means when our system detects vulnerabilities in dependencies, it can seamlessly authenticate with private registries, automatically patch the affected packages, and update the lockfiles, all while keeping your credentials safe.

## Configuration in Aikido <a href="#configuration-in-aikido" id="configuration-in-aikido"></a>

Once write access to the repos is set up, you can configure Aikido to authenticate with your private registry by following the steps below:

1. Go to your account's settings page for AutoFix, [here](https://app.aikido.dev/issues/fix/settings).
2. Click on "*Connect registry*" to see the modal below

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FNs3O1MjUeQOdKV86Y4WV%2Fimage.png?alt=media&#x26;token=06ec9926-7fcc-499b-934e-5d3af50382fb" alt=""><figcaption></figcaption></figure>

3. When you select '*Environment variables*' you will be able to enter the environment variables needed to create automated fixes in your repositories. In the example below we show a setup for a private registry for Poetry.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FpkMrYA5v2rqege3bQyQa%2Fimage.png?alt=media&#x26;token=02fc06b7-0105-4dc2-8f96-226f7f09ad8d" alt=""><figcaption></figcaption></figure>

4. Fill in the "key" and "value" and add as many variables which are needed. Aikido will encrypt all values automatically for you.

## Using the environment variables <a href="#example-setups" id="example-setups"></a>

### NPM <a href="#npmrc" id="npmrc"></a>

A common way to authenticate with private registries for JS libraries, is by including an `.npmrc` file in your repository to tell your package manager where to download a package from. In order not to store the authentication token in the repository, an environment variable can be referenced.

Below you can find an example `.npmrc` file that defines a registry and uses the `NPM_TOKEN` environment variable for authentication:

```
//npm.pkg.github.com/:_authToken=${NPM_TOKEN}
@pied-piper:registry=https://npm.pkg.github.com
```

More NPM private registry options can be found [here](https://help.aikido.dev/~/revisions/27oApOKWT7NW06uHiiU1/aikido-autofix/connect-private-packages/github-registry-private-packages).

### Poetry

Documentation for setting up Poetry with environment variables can be found [here](https://help.aikido.dev/~/revisions/27oApOKWT7NW06uHiiU1/aikido-autofix/connect-private-packages/poetry-private-packages).

### Bundle

Documentation for setting up Bundle with environment variables can be found [here](https://help.aikido.dev/~/revisions/27oApOKWT7NW06uHiiU1/aikido-autofix/connect-private-packages/bundle-private-gems).
