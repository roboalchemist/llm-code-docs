# Source: https://buildkite.com/docs/package-registries/ecosystems/gradle-kotlin.md

# Gradle (Kotlin)

Buildkite Package Registries provides registry support for Gradle-based Java packages (using the [Maven Publish Plugin](https://docs.gradle.org/current/userguide/publishing_maven.html)), using the Gradle Kotlin DSL. If you're using Gradle's Groovy DSL, refer to the [Gradle (Groovy)](/docs/package-registries/ecosystems/gradle-groovy) page.

Once your Java source registry has been [created](/docs/package-registries/registries/manage#create-a-source-registry), you can publish/upload packages (generated from your application's build) to this registry by configuring your `build.gradle.kts` file.

## Publish a package

The **Publish Instructions** tab of your Java source registry includes a Gradle snippet you can use to configure your environment for publishing packages to this registry. To view and copy the required `build.gradle.kts` configuration:

1. Select **Package Registries** in the global navigation to access the **Registries** page.
1. Select your Java source registry on this page.
1. Select the **Publish Instructions** tab and on the resulting page, in the **Using Gradle with `maven-publish` plugin** section, select **Gradle (Kotlin)** to expand this section.
1. Use the copy icon at the top-right of the code box to copy the Gradle code snippet and paste it into the appropriate area/s of your `build.gradle.kts` file.

    These `build.gradle.kts` file configurations contain the:
    <ul>

<li>Maven coordinates for your package (which you will need to manually configure yourself).</li>
<li>URL for your specific Java source registry in Buildkite.</li>
<li>API access token required to publish the package to this source registry.</li>
</ul>

1. You can then run the `gradle publish` command to publish the package to this source registry.

### Detailed instructions

You can also configure this file yourself (modifying the snippet as required), by following these detailed instructions.

1. Copy the following Gradle (Kotlin) snippet, paste it into your `build.gradle.kts` file, and modify accordingly:

    ```kotlin
    plugins {
      `maven-publish`
      `java-library`
    }

    publishing {
      publications {
          create<MavenPublication>("maven") {
              // MODIFY: Define your Maven coordinates of your package
              groupId = "com.name.domain.my"
              artifactId = "my-java-package-name"
              version = "my-java-package-version"

              from(components["java"])
          }
      }

      repositories {
        maven {
          url = uri("https://packages.buildkite.com/{org.slug}/{registry.slug}/maven2/")
          authentication {
            create<HttpHeaderAuthentication>("header")
          }

          credentials(HttpHeaderCredentials::class) {
            name = "Authorization"
            value = "Bearer registry-write-token"
          }
        }
      }
    }
    ```

    where:
    <ul>

<li><p><code>com.name.domain.my</code> is the domain name of your Java package (in typical right-to-left order).</p></li>
<li><p><code>my-java-package-name</code> is the name of your Java package.</p></li>
<li><p><code>my-java-package-version</code> is the version number of your Java package.</p></li>
</ul>

    <ul>
<li>
<code>{org.slug}</code> can be obtained from the end of your Buildkite URL, after accessing <strong>Package Registries</strong> or <strong>Pipelines</strong> in the global navigation of your organization in Buildkite.</li>
</ul>

    <ul>
<li>
<code>{registry.slug}</code> is the slug of your Java source registry, which is the <a href="https://en.wikipedia.org/wiki/Letter_case#Kebab_case" class="external-link" target="_blank">kebab-case</a> version of this registry's name, and can be obtained after accessing <strong>Package Registries</strong> in the global navigation &gt; your Java source registry from the <strong>Registries</strong> page.</li>
</ul>

    <ul>
<li>
<code>registry-write-token</code> is your <a href="https://buildkite.com/user/api-access-tokens">API access token</a> used to publish/upload packages to your Java source registry. Ensure this access token has the <strong>Read Packages</strong> and <strong>Write Packages</strong> REST API scopes, which allows this token to publish packages to any source registry your user account has access to within your Buildkite organization.</li>
</ul>

1. Publish your package:

    ```bash
    gradle publish
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
1. Ensure the **Installation** (tab) > **Gradle (Kotlin)**  section is displayed.
1. Copy the code snippet, paste this into the `build.gradle.kts` Gradle file, and modify the required values accordingly.

    You can then run `gradle install` on this modified script file to install this package.

This code snippet is based on this format:

```kotlin
repositories {
  maven {
    url = uri("https://packages.buildkite.com/{org.slug}/{registry.slug}/maven2/")
    authentication {
      create<HttpHeaderAuthentication>("header")
    }

    credentials(HttpHeaderCredentials::class) {
      name = "Authorization"
      value = "Bearer registry-read-token"
    }
  }
}

dependencies {
  implementation("com.name.domain.my:my-java-package-name:my-java-package-version")
}
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

- `registry-read-token` is your [API access token](https://buildkite.com/user/api-access-tokens) or [registry token](/docs/package-registries/registries/manage#configure-registry-tokens) used to download packages from your Java source registry. Ensure this access token has the **Read Packages** REST API scope, which allows this token to download packages from any registry your user account has access to within your Buildkite organization.

    **Note:** Both the `authentication` and `credentials` sections are not required for registries that are publicly accessible.

<ul>
<li><p><code>com.name.domain.my</code> is the domain name of your Java package (in typical right-to-left order).</p></li>
<li><p><code>my-java-package-name</code> is the name of your Java package.</p></li>
<li><p><code>my-java-package-version</code> is the version number of your Java package.</p></li>
</ul>
