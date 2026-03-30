# Source: https://buildkite.com/docs/package-registries/ecosystems/maven.md

# Maven

Buildkite Package Registries provides registry support for Maven-based Java packages.

Once your Java source registry has been [created](/docs/package-registries/registries/manage#create-a-source-registry), you can publish/upload packages (generated from your application's build) to this registry by configuring your `~/.m2/settings.xml` and application's relevant `pom.xml` files.

## Publish a package

The **Publish Instructions** tab of your Java source registry includes Maven XML snippets you can use to configure your environment for publishing packages to this registry. To view and copy the required `~/.m2/settings.xml` and `pom.xml` configurations:

1. Select **Package Registries** in the global navigation to access the **Registries** page.
1. Select your Java source registry on this page.
1. Select the **Publish Instructions** tab and on the resulting page, in the **Using Maven** section, select **Maven** to expand this section.
1. Use the copy icon at the top-right of each respective code box to copy the relevant XML snippets and paste it into its appropriate file.

    These file configurations contain the following:
    * `~/.m2/settings.xml`: the ID for your specific Java source registry in Buildkite and a temporary API access token required to publish the package to this registry.
    * `pom.xml`: the ID and URL for this source registry.

1. You can then run the `mvn deploy` command to publish the package to this source registry.

### Detailed instructions

You can also configure these files yourself (modifying the snippets as required), by following these detailed instructions.

1. Copy the following XML snippet, paste it into your `~/.m2/settings.xml` file, and modify accordingly:

    ```xml
    <settings xmlns="http://maven.apache.org/SETTINGS/1.0.0"
      xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
      xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.0.0
        http://maven.apache.org/xsd/settings-1.0.0.xsd">
      <servers>
        <server>
          <id>org-slug-registry-slug</id>
          <configuration>
            <httpHeaders>
              <property>
                <name>Authorization</name>
                <value>Bearer registry-write-token</value>
              </property>
            </httpHeaders>
          </configuration>
        </server>
      </servers>
    </settings>
    ```

    where:
    <ul>

<li>
<code>org-slug-registry-slug</code> is the ID of your Java registry, based on the org and this registry's slugs separated by a hyphen. The org slug can be obtained from the end of your Buildkite URL, after accessing <strong>Package Registries</strong> or <strong>Pipelines</strong> in the global navigation of your organization in Buildkite. The registry slug is the <a href="https://en.wikipedia.org/wiki/Letter_case#Kebab_case" class="external-link" target="_blank">kebab-case</a> version of your registry name, and can be obtained after accessing <strong>Package Registries</strong> in the global navigation &gt; your Java registry from the <strong>Registries</strong> page. The Java registry ID can actually be any valid unique value, as long as the same value is used in both your <code>settings.xml</code> and <code>pom.xml</code> files.</li>
</ul>

    <ul>
<li>
<code>registry-write-token</code> is your <a href="https://buildkite.com/user/api-access-tokens">API access token</a> used to publish/upload packages to your Java source registry. Ensure this access token has the <strong>Read Packages</strong> and <strong>Write Packages</strong> REST API scopes, which allows this token to publish packages to any source registry your user account has access to within your Buildkite organization.</li>
</ul>

    **Note:** This step only needs to be performed once for the life of your Java source registry, and API access token.

1. Copy the following XML snippet, paste it into your `pom.xml` configuration file, and modify accordingly:

    ```xml
    <distributionManagement>
      <repository>
        <id>org-slug-registry-slug</id>
        <url>https://packages.buildkite.com/{org.slug}/{registry.slug}/maven2/</url>
      </repository>
      <snapshotRepository>
        <id>org-slug-registry-slug</id>
        <url>https://packages.buildkite.com/{org.slug}/{registry.slug}/maven2/</url>
      </snapshotRepository>
    </distributionManagement>
    ```

    where:
    * `org-slug-registry-slug` is the ID of your Java source registry (above).

    <ul>

<li>
<code>{org.slug}</code> can be obtained from the end of your Buildkite URL, after accessing <strong>Package Registries</strong> or <strong>Pipelines</strong> in the global navigation of your organization in Buildkite.</li>
</ul>

    <ul>
<li>
<code>{registry.slug}</code> is the slug of your Java source registry, which is the <a href="https://en.wikipedia.org/wiki/Letter_case#Kebab_case" class="external-link" target="_blank">kebab-case</a> version of this registry's name, and can be obtained after accessing <strong>Package Registries</strong> in the global navigation &gt; your Java source registry from the <strong>Registries</strong> page.</li>
</ul>

1. Publish your package:

    ```bash
    mvn deploy
    ```

## Access a package's details

<p>A Java package's details can be accessed from its source registry through the <strong>Releases</strong> (tab) section of your Java source registry page. To do this:</p>

<ol>
<li>Select <strong>Package Registries</strong> in the global navigation to access the <strong>Registries</strong> page.</li>
<li>Select your Java source registry on this page.</li>
<li>On your Java source registry page, select the package to display its details page.</li>
</ol>

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

A Java package can be downloaded from the package's details page. To do this:

1. [Access the package's details](#access-a-packages-details).
1. Select **Download**.

<h3 id="access-a-packages-details-installing-a-package"></h3>

### Installing a package from a source registry

A Java package can be installed using code snippet details provided on the package's details page. To do this:

1. [Access the package's details](#access-a-packages-details).
1. Ensure the **Installation** tab is displayed and select the **Maven** section to expand it.
1. Copy each code snippet, and paste them into their respective `~/.m2/settings.xml` and `pom.xml` files (under the `project` XML tag), modifying the required values accordingly.

    **Note:** The `~/.m2/settings.xml` configuration:
    * Is _not_ required if your registry is publicly accessible.
    * Only needs to be performed once for the life of your Java registry.

    You can then run `mvn install` on this modified `pom.xml` to install this package.

The `~/.m2/settings.xml` code snippet is based on this format:

```xml
<settings xmlns="http://maven.apache.org/SETTINGS/1.0.0"
  xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/SETTINGS/1.0.0
    http://maven.apache.org/xsd/settings-1.0.0.xsd">
  <servers>
    <server>
      <id>org-slug-registry-slug</id>
      <configuration>
        <httpHeaders>
          <property>
            <name>Authorization</name>
            <value>Bearer registry-read-token</value>
          </property>
        </httpHeaders>
      </configuration>
    </server>
  </servers>
</settings>
```

where:

<ul>
<li>
<code>org-slug-registry-slug</code> is the ID of your Java registry, based on the org and this registry's slugs separated by a hyphen. The org slug can be obtained from the end of your Buildkite URL, after accessing <strong>Package Registries</strong> or <strong>Pipelines</strong> in the global navigation of your organization in Buildkite. The registry slug is the <a href="https://en.wikipedia.org/wiki/Letter_case#Kebab_case" class="external-link" target="_blank">kebab-case</a> version of your registry name, and can be obtained after accessing <strong>Package Registries</strong> in the global navigation &gt; your Java registry from the <strong>Registries</strong> page. The Java registry ID can actually be any valid unique value, as long as the same value is used in both your <code>settings.xml</code> and <code>pom.xml</code> files.</li>
</ul>

* `registry-read-token` is your [API access token](https://buildkite.com/user/api-access-tokens) or [registry token](/docs/package-registries/registries/manage#configure-registry-tokens) used to download packages from your Java source registry. Ensure this access token has the **Read Packages** REST API scope, which allows this token to download packages from any registry your user account has access to within your Buildkite organization.

The `pom.xml` code snippet is based on this format:

```xml
<repositories>
  <repository>
    <id>org-slug-registry-slug</id>
    <url>https://packages.buildkite.com/{org.slug}/{registry.slug}/maven2/</url>
    <releases>
      <enabled>true</enabled>
    </releases>
    <snapshots>
      <enabled>true</enabled>
    </snapshots>
  </repository>
</repositories>

<dependencies>
  <dependency>
    <groupId>com.name.domain.my</groupId>
    <artifactId>my-java-package-name</artifactId>
    <version>my-java-package-version</version>
  </dependency>
</dependencies>
```

where:

<ul>
<li>
<code>org-slug-registry-slug</code> is the ID of your Java registry, based on the org and this registry's slugs separated by a hyphen. The org slug can be obtained from the end of your Buildkite URL, after accessing <strong>Package Registries</strong> or <strong>Pipelines</strong> in the global navigation of your organization in Buildkite. The registry slug is the <a href="https://en.wikipedia.org/wiki/Letter_case#Kebab_case" class="external-link" target="_blank">kebab-case</a> version of your registry name, and can be obtained after accessing <strong>Package Registries</strong> in the global navigation &gt; your Java registry from the <strong>Registries</strong> page. The Java registry ID can actually be any valid unique value, as long as the same value is used in both your <code>settings.xml</code> and <code>pom.xml</code> files.</li>
</ul>

* `{org.slug}` is the org slug, which can be obtained as described above.

<ul>
<li>
<code>{registry.slug}</code> is the slug of your registry, which is the <a href="https://en.wikipedia.org/wiki/Letter_case#Kebab_case" class="external-link" target="_blank">kebab-case</a> version of your registry name, and can be obtained after accessing <strong>Package Registries</strong> in the global navigation &gt; your registry from the <strong>Registries</strong> page.</li>
</ul>

<ul>
<li><p><code>com.name.domain.my</code> is the domain name of your Java package (in typical right-to-left order).</p></li>
<li><p><code>my-java-package-name</code> is the name of your Java package.</p></li>
<li><p><code>my-java-package-version</code> is the version number of your Java package.</p></li>
</ul>
