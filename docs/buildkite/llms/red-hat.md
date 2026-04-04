# Source: https://buildkite.com/docs/package-registries/ecosystems/red-hat.md

# Red Hat

Buildkite Package Registries provides registry support for Red Hat-based (RPM) packages for Red Hat Linux operating systems.

Once your Red Hat source registry has been [created](/docs/package-registries/registries/manage#create-a-source-registry), you can publish/upload packages (generated from your application's build) to this registry.

## Publish a package

You can use two approaches to publish an RPM package to your Red Hat source registry—[`curl`](#publish-a-package-using-curl) or the [Buildkite CLI](#publish-a-package-using-the-buildkite-cli).

### Using curl

The **Publish Instructions** tab of your Red Hat source registry includes a `curl` command you can use to upload a package to this registry. To view and copy this `curl` command:

1. Select **Package Registries** in the global navigation to access the **Registries** page.
1. Select your Red Hat source registry on this page.
1. Select the **Publish Instructions** tab and on the resulting page, use the copy icon at the top-right of the relevant code box to copy this `curl` command and run it (with the appropriate values) to publish the package to this source registry.

This command provides:

- The specific URL to publish a package to your specific Red Hat source registry in Buildkite.
- A temporary API access token to publish packages to this source registry.
- The Red Hat (RPM) package file to be published.

You can also create this command yourself using the following `curl` command (which you'll need to modify as required before submitting):

```bash
curl -X POST https://api.buildkite.com/v2/packages/organizations/{org.slug}/registries/{registry.slug}/packages \
  -H "Authorization: Bearer $REGISTRY_WRITE_TOKEN" \
  -F "file=@path/to/red-hat/package.rpm"
```

where:

<ul>
<li>
<code>{org.slug}</code> can be obtained from the end of your Buildkite URL, after accessing <strong>Package Registries</strong> or <strong>Pipelines</strong> in the global navigation of your organization in Buildkite.</li>
</ul>

<ul>
<li>
<code>{registry.slug}</code> is the slug of your Red Hat registry, which is the <a href="https://en.wikipedia.org/wiki/Letter_case#Kebab_case" class="external-link" target="_blank">kebab-case</a> version of your Red Hat registry name, and can be obtained after accessing <strong>Package Registries</strong> in the global navigation &gt; your Red Hat registry from the <strong>Registries</strong> page.</li>
</ul>

- `$REGISTRY_WRITE_TOKEN` is your [API access token](https://buildkite.com/user/api-access-tokens) used to publish/upload packages to your Red Hat source registry. Ensure this access token has the **Read Packages** and **Write Packages** REST API scopes, which allows this token to publish packages to any source registry your user account has access to within your Buildkite organization. Alternatively, you can use an OIDC token that meets your Red Hat source registry's [OIDC policy](/docs/package-registries/security/oidc#define-an-oidc-policy-for-a-registry). Learn more about these tokens in [OIDC in Buildkite Package Registries](/docs/package-registries/security/oidc).

<ul>
<li>
<code>path/to/red-hat/package.rpm</code> is the full path to the RPM package, including the file's name. If the file is located in the same directory that this command is running from, then no path is required.</li>
</ul>

For example, to upload the file `my-red-hat-package_1.0-2.x86_64.rpm` from the current directory to the **My Red Hat packages** source registry in the **My organization** Buildkite organization, run the `curl` command:

```bash
curl -X POST https://api.buildkite.com/v2/packages/organizations/my-organization/registries/my-red-hat-packages/packages \
  -H "Authorization: Bearer $REPLACE_WITH_YOUR_REGISTRY_WRITE_TOKEN" \
  -F "file=@my-red-hat-package_1.0-2.x86_64.rpm"
```

### Using the Buildkite CLI

The following [Buildkite CLI](/docs/platform/cli) command can also be used to publish an RPM package to your Red Hat source registry from your local environment, once it has been [installed](/docs/platform/cli/installation) and [configured with an appropriate token](#token-usage-with-the-buildkite-cli):

```bash
bk package push registry-slug path/to/red-hat/package.rpm
```

where:

- `registry-slug` is the slug of your Red Hat source registry, which is the [kebab-case](https://en.wikipedia.org/wiki/Letter_case#Kebab_case) version of this registry's name, and can be obtained after accessing **Package Registries** in the global navigation > your file source registry from the **Registries** page.

<ul>
<li>
<code>path/to/red-hat/package.rpm</code> is the full path to the RPM package, including the file's name. If the file is located in the same directory that this command is running from, then no path is required.</li>
</ul>

<h4 id="token-usage-with-the-buildkite-cli">Token usage with the Buildkite CLI</h4>

<p>When <a href="/docs/platform/cli/configuration">configuring the Buildkite CLI with an API access token</a>, ensure it has the <strong>Read Packages</strong> and <strong>Write Packages</strong> REST API scopes, which allows this token to publish files to any source registry your user account has access to within your Buildkite organization.</p>

<p>You can also override this configured token by passing in a different token value using the <code>BUILDKITE_API_TOKEN</code> environment variable when running the <code>bk</code> command:</p>
<div class="highlight"><pre class="highlight shell"><code><span class="nv">BUILDKITE_API_TOKEN</span><span class="o">=</span><span class="nv">$another_token_value</span> bk package push organization-slug/registry-slug ./path/to/my/file.ext
</code></pre></div>
<p>If you have <a href="/docs/platform/cli/installation">installed the Buildkite CLI</a> to your <a href="/docs/agent/self-hosted/install">self-hosted agents</a>, you can also do the following:</p>

<ul>
<li><p>Use the <code>bk</code> command from within your Buildkite pipelines.</p></li>
<li><p>Using the <code>BUILDKITE_API_TOKEN</code> environment variable, pass in a Buildkite OIDC token value generated from your agents that meets your source registry's <a href="/docs/package-registries/security/oidc#define-an-oidc-policy-for-a-registry">OIDC policy</a>. Learn more about these tokens in <a href="/docs/package-registries/security/oidc">OIDC in Buildkite Package Registries</a>.</p></li>
</ul>

## Access a package's details

A Red Hat (RPM) package's details can be accessed from this registry through the **Releases** (tab) section of your Red Hat source registry page. To do this:

1. Select **Package Registries** in the global navigation to access the **Registries** page.
1. Select your Red Hat source registry on this page.
1. On your Red Hat source registry page, select the package to display its details page.

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

A Red Hat (RPM) package can be downloaded from the package's details page. To do this:

1. [Access the package's details](#access-a-packages-details).
1. Select **Download**.

### Installing a package

A Red Hat package can be installed using code snippet details provided on the package's details page. To do this:

1. [Access the package's details](#access-a-packages-details).
1. Ensure the **Installation** > **Instructions** section is displayed.
1. For each required command in the relevant code snippets, copy the relevant code snippet, paste it into your terminal, and run it.

The following set of code snippets are descriptions of what each code snippet does and where applicable, its format:

#### Registry configuration

Configure your Red Hat registry as the source for your Red Hat (RPM) packages:

```bash
sudo sh -c 'echo -e "[{registry.slug}]\nname={registry.name}\nbaseurl=https://buildkite:{registry.read.token}@packages.buildkite.com/{org.slug}/{registry.slug}/rpm_any/rpm_any/\$basearch\nenabled=1\nrepo_gpgcheck=1\ngpgcheck=0\ngpgkey=https://buildkite:{registry.read.token}@packages.buildkite.com/{org.slug}/{registry.slug}/gpgkey\npriority=1"' > /etc/yum.repos.d/{registry.slug}.repo
```

where:

<ul>
<li>
<code>{registry.slug}</code> is the slug of your Red Hat registry, which is the <a href="https://en.wikipedia.org/wiki/Letter_case#Kebab_case" class="external-link" target="_blank">kebab-case</a> version of your Red Hat registry name, and can be obtained after accessing <strong>Package Registries</strong> in the global navigation &gt; your Red Hat registry from the <strong>Registries</strong> page.</li>
</ul>

- `{registry.name}` is the name of your Red Hat registry.

- `{registry.read.token}` is your [API access token](https://buildkite.com/user/api-access-tokens) or [registry token](/docs/package-registries/registries/manage#configure-registry-tokens) used to download packages from your Red Hat registry. Ensure this access token has the **Read Packages** REST API scope, which allows this token to download packages from any registry your user account has access to within your Buildkite organization. This URL component, along with its surrounding `buildkite:` and `@` components are not required for registries that are publicly accessible.

<ul>
<li>
<code>{org.slug}</code> can be obtained from the end of your Buildkite URL, after accessing <strong>Package Registries</strong> or <strong>Pipelines</strong> in the global navigation of your organization in Buildkite.</li>
</ul>

#### Package installation

Use `dnf` to install the package:

```bash
dnf install -y package-name
```

where `package-name` is the name of your package, which usually includes the version number and distribution type.
