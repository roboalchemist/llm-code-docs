# Source: https://buildkite.com/docs/package-registries/ecosystems/javascript.md

# JavaScript

Buildkite Package Registries provides registry support for JavaScript-based (Node.js npm) packages.

Once your JavaScript source registry has been [created](/docs/package-registries/registries/manage#create-a-source-registry), you can publish/upload packages (generated from your application's build) to this registry by configuring your `~/.npmrc` and application's relevant `package.json` files.

## Publish a package

The **Publish Instructions** tab of your JavaScript source registry includes command/code snippets you can use to configure your environment for publishing packages to this registry. To view and copy the required command or code snippets for your `~/.npmrc` and `package.json` configurations:

1. Select **Package Registries** in the global navigation to access the **Registries** page.
1. Select your JavaScript source registry on this page.
1. Select the **Publish Instructions** tab and on the resulting page, use the copy icon at the top-right of each respective code box to copy the its snippet and paste it into your command line tool or the appropriate file.

    These file configurations contain the following:
    * `~/.npmrc`: the URL for your specific JavaScript source registry in Buildkite and a temporary API access token required to publish the package to this registry.
    * `package.json`: the URL for this source registry.

1. You can then run the `npm pack` and `npm publish` commands to publish the package to this source registry.

### Detailed instructions

You can also configure these files yourself (modifying the snippets as required), by following these detailed instructions.

1. Copy the following `npm` command, paste it into your terminal, and modify as required before running to update your `~/.npmrc` file:

    ```bash
    npm set //packages.buildkite.com/{org.slug}/{registry.slug}/npm/:_authToken registry-write-token
    ```

    where:
    <ul>

<li>
<code>{org.slug}</code> can be obtained from the end of your Buildkite URL, after accessing <strong>Package Registries</strong> or <strong>Pipelines</strong> in the global navigation of your organization in Buildkite.</li>
</ul>

    <ul>
<li>
<code>{registry.slug}</code> is the slug of your JavaScript source registry, which is the <a href="https://en.wikipedia.org/wiki/Letter_case#Kebab_case" class="external-link" target="_blank">kebab-case</a> version of this registry's name, and can be obtained after accessing <strong>Package Registries</strong> in the global navigation &gt; your JavaScript source registry from the <strong>Registries</strong> page.</li>
</ul>

    <ul>
<li>
<code>registry-write-token</code> is your <a href="https://buildkite.com/user/api-access-tokens">API access token</a> used to publish/upload packages to your JavaScript source registry. Ensure this access token has the <strong>Read Packages</strong> and <strong>Write Packages</strong> REST API scopes, which allows this token to publish packages to any source registry your user account has access to within your Buildkite organization.</li>
</ul>

    **Note:**
    * If your `.npmrc` file doesn't exist, this command automatically creates it for you.
    * This step only needs to be performed once for the life of your JavaScript source registry.

1. Copy the following JSON code snippet (or the line of code beginning `"publishConfig": ...`), paste it into your Node.js project's `package.json` file, and modify as required:

    ```json
    {
      ...,
      "publishConfig": {"registry": "https://packages.buildkite.com/{org.slug}/{registry.slug}/npm/"}
    }
    ```

    **Note:** Don't forget to add the separating comma between `"publishConfig": ...` and the previous field.

1. Build and publish your package:

    ```bash
    npm pack
    npm publish
    ```

## Access a package's details

A JavaScript package's details can be accessed from this registry through the **Releases** (tab) section of your JavaScript source registry page. To do this:

1. Select **Package Registries** in the global navigation to access the **Registries** page.
1. Select your JavaScript source registry on this page.
1. On your JavaScript source registry page, select the package to display its details page.

<p>The package's details page provides the following information in the following sections:</p>

<ul>
<li>
<strong>Installation</strong> (tab): the <a href="#access-a-packages-details-installing-a-package">installation instructions</a>.</li>
<li>
<strong>Contents</strong> (tab, where available): a list of directories and files contained within the package.</li>
<li>
<strong>Details</strong> (tab): a list of checksum values for this package—MD5, SHA1, SHA256, and SHA512.</li>
<li>
<strong>About this version</strong>: a brief (metadata) description about the package.</li>
<li>
<p><strong>Details</strong>: details about:</p>

<ul>
<li>the name of the package (typically the file name excluding any version details and extension).</li>
<li>the package version.</li>
<li>the source registry the package is located in.</li>
<li>the package's visibility (based on its registry's visibility)—whether the package is <strong>Private</strong> and requires authentication to access, or is publicly accessible.</li>
<li>the distribution name / version.</li>
<li>additional optional metadata contained within the package, such as a homepage, licenses, etc.</li>
</ul>
</li>
<li><p><strong>Pushed</strong>: the date when the last package was uploaded to the source registry.</p></li>
<li><p><strong>Total files</strong>: the total number of files (and directories) within the package.</p></li>
<li><p><strong>Dependencies</strong>: the number of dependency packages required by this package.</p></li>
<li><p><strong>Package size</strong>: the storage size (in bytes) of this package.</p></li>
<li><p><strong>Downloads</strong>: the number of times this package has been downloaded.</p></li>
</ul>

### Downloading a package

A JavaScript package can be downloaded from the package's details page. To do this:

1. [Access the package's details](#access-a-packages-details).
1. Select **Download**.

<h3 id="access-a-packages-details-installing-a-package"></h3>

### Installing a package from a source registry

A JavaScript package can be installed using code snippet details provided on the package's details page. To do this:

1. [Access the package's details](#access-a-packages-details).
1. Ensure the **Installation** > **Instructions** section is displayed.
1. If your JavaScript source registry is _private_  (the default configuration for source registries) and you haven't already performed this `.npmrc` configuration step, copy the `npm set` command from the [**Registry Configuration**](#registry-configuration) section, paste it into your terminal, and modify as required before running to update your `~/.npmrc` file.
1. Copy the `npm install ...` command from the [**Package Installation**](#package-installation) section, paste it into your terminal, and modify as required before running it.

<h4 id="registry-configuration">Registry Configuration</h4>

If your JavaScript source registry is _private_, set its authentication details in the `.npmrc` file by running the `npm set` command:

```bash
npm set //packages.buildkite.com/{org.slug}/{registry.slug}/npm/:_authToken registry-read-token
```

where:

<ul>
<li>
<code>{org.slug}</code> can be obtained from the end of your Buildkite URL, after accessing <strong>Package Registries</strong> or <strong>Pipelines</strong> in the global navigation of your organization in Buildkite.</li>
</ul>

<ul>
<li>
<code>{registry.slug}</code> is the slug of your registry, which is the <a href="https://en.wikipedia.org/wiki/Letter_case#Kebab_case" class="external-link" target="_blank">kebab-case</a> version of your registry name, and can be obtained after accessing <strong>Package Registries</strong> in the global navigation &gt; your registry from the <strong>Registries</strong> page.</li>
</ul>

* `registry-read-token` is your [API access token](https://buildkite.com/user/api-access-tokens) or [registry token](/docs/package-registries/registries/manage#configure-registry-tokens) used to download packages from your JavaScript source registry. Ensure this access token has the **Read Packages** REST API scope, which allows this token to download packages from any registry your user account has access to within your Buildkite organization.

> 📘
> If your `.npmrc` file doesn't exist, this command automatically creates it for you.
> This step only needs to be performed once for the life of your JavaScript registry, and it is not required for public JavaScript registries.

<h4 id="package-installation">Package Installation</h4>

Install your JavaScript package by running the `npm install` command:

```bash
npm install nodejs-package-name@version.number \
  --registry https://packages.buildkite.com/{org.slug}/{registry.slug}/npm/
```

where:

* `nodejs-package-name` is the name of your Node.js package (that is, the `name` field value from its `package.json` file).

* `version.number` is the version of your Node.js package (that is, the `version` field value from its `package.json` file).

<ul>
<li>
<code>{org.slug}</code> can be obtained from the end of your Buildkite URL, after accessing <strong>Package Registries</strong> or <strong>Pipelines</strong> in the global navigation of your organization in Buildkite.</li>
</ul>

<ul>
<li>
<code>{registry.slug}</code> is the slug of your registry, which is the <a href="https://en.wikipedia.org/wiki/Letter_case#Kebab_case" class="external-link" target="_blank">kebab-case</a> version of your registry name, and can be obtained after accessing <strong>Package Registries</strong> in the global navigation &gt; your registry from the <strong>Registries</strong> page.</li>
</ul>
