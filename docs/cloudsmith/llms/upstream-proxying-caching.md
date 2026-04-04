# Source: https://help.cloudsmith.io/docs/upstream-proxying-caching.md

# Upstream Proxying

Upstream proxying and caching allows you to upload and use the packages you own, while Cloudsmith fetches and caches other packages (such as dependencies).

This enables you to use Cloudsmith as a first-class cache and a central source of truth for packages, to protect you from outages of external services (which is especially important when running behind your firewall).

## Upstream Concepts

Cloudsmith upstream support centers around several key concepts:

* *Proxying*: The act of transparently allowing access to a package that exists on an upstream repository. Package managers see the remote package as one which belongs to the Cloudsmith repository.
* *Caching*: An extension to the proxying functionality, where requested packages from an upstream are fetched and permanently stored in your Cloudsmith repository. This helps to ensure package dependencies are always available and helps to protect from upstream outages or security breaches.
* *Indexing*: In order to be aware of the packages available from an upstream, Cloudsmith builds an index. This process occurs when an upstream is first added to your Cloudsmith repository and is scheduled for a resync on a regular basis.

### Indexing

Index availability is a critical factor for upstream handling on Cloudsmith, helping to ensure deterministic performance for upstream requests and a deeper insight into the availability of packages.

The indexing process can differ, depending on the package format and upstream itself. Where possible, Cloudsmith will determine the availability of all packages on an upstream repository *ahead-of-time*, which generally means that an upstream repository is unavailable when first added, until this indexing process has occurred.

For package formats that do not maintain a centralized mechanism for retrieval of all packages, Cloudsmith employs a *just-in-time* indexing mechanism. In this approach, awareness of packages is made the first time a package is successfully cached from an upstream repository. Going forwards, Cloudsmith maintains a list of all versions available on the source upstream for the package and ensures this is kept in sync.

When neither indexing mechanism is available for an upstream, Cloudsmith falls back to a *real-time* unindexed approach. When requests are made for upstream packages, Cloudsmith determines availability across each upstream in your repository, in real-time. This is the least performant approach.

We strive to ensure that at least *just-in-time* indexing is available for each package format and upstream source, although this is not always possible.

### Priority

When defining upstreams for a repository, a *priority* can be specified. The priority of an upstream is used to determine the order in which upstream requests are resolved. Cloudsmith evaluates upstreams by the order of `1..n`.

A good approach when determining what priority to apply to upstreams is to ensure that the lowest value is specified for the upstream which is most likely to contain upstream packages you request. This helps to improve performance in the event that an upstream source does not support any of our indexing mechanisms.

## Supported Formats

<Table align={["left","left","left","left","left","left","left"]}>
  <thead>
    <tr>
      <th>
        Format
      </th>

      <th>
        <div class="cs-center">Fixed Proxy</div>
      </th>

      <th>
        <div class="cs-center">Configurable Proxy</div>
      </th>

      <th>
        <div class="cs-center">Caching</div>
      </th>

      <th>
        <div class="cs-center">Indexing</div>
      </th>

      <th>
        <div class="cs-center">Indexing Type</div>
      </th>

      <th>
        <div class="cs-center">Config Reference</div>
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        [Cargo (Rust)](https://help.cloudsmith.io/docs/cargo-registry)
      </td>

      <td>
        N/A
      </td>

      <td>
        ✅
      </td>

      <td>
        ✅
      </td>

      <td>
        ✅
      </td>

      <td>
        <div class="cs-center">Ahead-of-Time</div>
      </td>

      <td>
        [API](https://help.cloudsmith.io/reference/repos_upstream_cargo_create)
      </td>
    </tr>

    <tr>
      <td>
        [Composer](/formats/composer-repository)
      </td>

      <td>
        N/A
      </td>

      <td>
        ✅
      </td>

      <td>
        ✅
      </td>

      <td>
        ✅
      </td>

      <td>
        <div class="cs-center">Just-in-Time</div>
      </td>

      <td>
        [API](https://help.cloudsmith.io/reference/repos_upstream_composer_create)
      </td>
    </tr>

    <tr>
      <td>
        [CRAN](https://help.cloudsmith.io/docs/cran-repository)
      </td>

      <td>
        N/A
      </td>

      <td>
        ✅
      </td>

      <td>
        ✅
      </td>

      <td>
        ✅
      </td>

      <td>
        <div class="cs-center">Ahead-of-Time</div>
      </td>

      <td>
        [API](https://help.cloudsmith.io/reference/repos_upstream_cran_create)
      </td>
    </tr>

    <tr>
      <td>
        [Dart](https://help.cloudsmith.io/docs/dart-repository)
      </td>

      <td>
        N/A
      </td>

      <td>
        ✅
      </td>

      <td>
        ✅
      </td>

      <td>
        ✅
      </td>

      <td>
        <div class="cs-center">Ahead-of-Time</div>
      </td>

      <td>
        [API](https://help.cloudsmith.io/reference/repos_upstream_dart_create)
      </td>
    </tr>

    <tr>
      <td>
        [Debian](https://help.cloudsmith.io/docs/debian-repository)
      </td>

      <td>
        N/A
      </td>

      <td>
        ✅
      </td>

      <td>
        ✅
      </td>

      <td>
        ✅
      </td>

      <td>
        <div class="cs-center">Ahead-of-Time</div>
      </td>

      <td>
        [API](https://help.cloudsmith.io/reference/repos_upstream_deb_create)
      </td>
    </tr>

    <tr>
      <td>
        [Docker](https://help.cloudsmith.io/docs/docker-registry)
      </td>

      <td>
        N/A
      </td>

      <td>
        ✅
      </td>

      <td>
        ✅
      </td>

      <td>
        ✅
      </td>

      <td>
        <div class="cs-center">Just-in-Time</div>
      </td>

      <td>
        [API](https://help.cloudsmith.io/reference/repos_upstream_docker_create)
      </td>
    </tr>

    <tr>
      <td>
        [Golang](https://help.cloudsmith.io/docs/go-registry)
      </td>

      <td>
        N/A
      </td>

      <td>
        ✅
      </td>

      <td>
        ✅
      </td>

      <td>
        ✅
      </td>

      <td>
        <div class="cs-center">Ahead-of-Time</div>
      </td>

      <td>
        [API](https://help.cloudsmith.io/reference/repos_upstream_go_create)
      </td>
    </tr>

    <tr>
      <td>
        [Gradle ](https://help.cloudsmith.io/docs/gradle-repository)
      </td>

      <td>
        N/A
      </td>

      <td>
        ✅
      </td>

      <td>
        ✅
      </td>

      <td>
        ✅
      </td>

      <td>
        <div class="cs-center">Just-in-Time</div>
      </td>

      <td>
        [API](https://help.cloudsmith.io/reference/repos_upstream_maven_create)
      </td>
    </tr>

    <tr>
      <td>
        [Helm](https://help.cloudsmith.io/docs/helm-chart-repository)
      </td>

      <td>
        N/A
      </td>

      <td>
        ✅
      </td>

      <td>
        ✅
      </td>

      <td>
        ✅
      </td>

      <td>
        <div class="cs-center">Ahead-of-Time</div>
      </td>

      <td>
        [API](https://help.cloudsmith.io/reference/repos_upstream_helm_create)
      </td>
    </tr>

    <tr>
      <td>
        [Hex](https://help.cloudsmith.io/docs/hex-repository)
      </td>

      <td>
        N/A
      </td>

      <td>
        ✅
      </td>

      <td>
        ✅
      </td>

      <td>
        ✅
      </td>

      <td>
        <div class="cs-center">Ahead-of-Time</div>
      </td>

      <td>
        [API](https://help.cloudsmith.io/reference/repos_upstream_hex_create)
      </td>
    </tr>

    <tr>
      <td>
        [Maven](https://help.cloudsmith.io/docs/maven-repository)
      </td>

      <td>
        N/A
      </td>

      <td>
        ✅
      </td>

      <td>
        ✅
      </td>

      <td>
        ✅
      </td>

      <td>
        <div class="cs-center">Just-in-Time</div>
      </td>

      <td>
        [API](https://help.cloudsmith.io/reference/repos_upstream_maven_create)
      </td>
    </tr>

    <tr>
      <td>
        [npm](https://help.cloudsmith.io/docs/npm-registry)
      </td>

      <td>
        N/A
      </td>

      <td>
        ✅
      </td>

      <td>
        ✅
      </td>

      <td>
        ✅
      </td>

      <td>
        <div class="cs-center">Just-in-Time</div>
      </td>

      <td>
        [API](https://help.cloudsmith.io/reference/repos_upstream_npm_create)
      </td>
    </tr>

    <tr>
      <td>
        [NuGet](https://help.cloudsmith.io/docs/nuget-feed)
      </td>

      <td>
        N/A
      </td>

      <td>
        ✅
      </td>

      <td>
        ✅
      </td>

      <td>
        ✅
      </td>

      <td>
        <div class="cs-center">Ahead-of-Time</div>
      </td>

      <td>
        [API](https://help.cloudsmith.io/reference/repos_upstream_nuget_create)
      </td>
    </tr>

    <tr>
      <td>
        [Python](https://help.cloudsmith.io/docs/python-repository)
      </td>

      <td>
        N/A
      </td>

      <td>
        ✅
      </td>

      <td>
        ✅
      </td>

      <td>
        ✅
      </td>

      <td>
        <div class="cs-center">Ahead-of-Time</div>
      </td>

      <td>
        [API](https://help.cloudsmith.io/reference/repos_upstream_python_create)
      </td>
    </tr>

    <tr>
      <td>
        [RedHat](https://help.cloudsmith.io/docs/redhat-repository)
      </td>

      <td>
        N/A
      </td>

      <td>
        ✅
      </td>

      <td>
        ✅
      </td>

      <td>
        ✅
      </td>

      <td>
        <div class="cs-center">Ahead-of-Time</div>
      </td>

      <td>
        [API](https://help.cloudsmith.io/reference/repos_upstream_rpm_create)
      </td>
    </tr>

    <tr>
      <td>
        [Ruby](https://help.cloudsmith.io/docs/ruby-repository)
      </td>

      <td>
        N/A
      </td>

      <td>
        ✅
      </td>

      <td>
        ✅
      </td>

      <td>
        ✅
      </td>

      <td>
        <div class="cs-center">Ahead-of-Time</div>
      </td>

      <td>
        [API](https://help.cloudsmith.io/reference/repos_upstream_ruby_create)
      </td>
    </tr>

    <tr>
      <td>
        [sbt ](https://help.cloudsmith.io/docs/sbt-repository)
      </td>

      <td>
        N/A
      </td>

      <td>
        ✅
      </td>

      <td>
        ✅
      </td>

      <td>
        ✅
      </td>

      <td>
        <div class="cs-center">Just-in-Time</div>
      </td>

      <td>
        [API](https://help.cloudsmith.io/reference/repos_upstream_maven_create)
      </td>
    </tr>

    <tr>
      <td>
        [Swift](https://help.cloudsmith.io/docs/swift-registry)
      </td>

      <td>
        N/A
      </td>

      <td>
        ✅
      </td>

      <td>
        ✅
      </td>

      <td>
        ✅
      </td>

      <td>
        <div class="cs-center">Just-in-Time</div>
      </td>

      <td>
        [API](https://help.cloudsmith.io/reference/repos_upstream_swift_create)
      </td>
    </tr>
  </tbody>
</Table>

> 👍
>
> You can can also create and manage upstreams via the [Cloudsmith API](https://help.cloudsmith.io/reference/repos_upstream_maven_list)

## Create an Upstream Proxy

### Using the Quick Configure Wizard

Cloudsmith helps you proxying and caching canonical registries in a single click.

Just select the Upstream you need and it will be automatically configured to you. You can pull packages from them proxying and caching all of the content in Cloudsmith, hence applying all the controls you require.

### Using the CLI

You can create upstreams without leaving your terminal. For example, you can create a debian upstream with the Cloudsmith CLI.

1. Create a `upstream_config.json` file with the next fields:

```json
{
  "name": "Debian Upstream Demo Docs",
  "upstream_url": "http://archive.ubuntu.com/ubuntu",
  "mode": "Cache and Proxy",
  "distro_versions": ["debian/trixie"],
  "component": "main", 
  "auth_mode": "None",
  "priority": 1
}
```

2. Use the Cloudsmith CLI to create the Debian upstream in your workspace `WORKSPACE` and repository `REPOSITORY`:

```bash
cloudsmith upstream deb create WORKSPACE/REPOSITORY ./upstream_config.json
```

This command will return the details about your new configured upstream. Please, refer to the [Config Reference](#supported-formats) column in the supported formats table to review fields available for each of the supported formats.

### Using the manual configuration

Click the green "Create Upstream" button, and then select the format you want to create an upstream for:

<Image alt="Create Upstream button" align="center" width="80% " border={true} src="https://files.readme.io/4af4b58-create-upstream-button.png">
  Create Upstream button
</Image>

### Create a Maven Upstream

<Image title="create-maven-upstream.png" alt={593} align="center" width="50% " border={true} src="https://files.readme.io/06b0f27-create-maven-upstream.png">
  Create Maven Upstream Form
</Image>

| Form Field                | Description                                                                                                                                                                                                     |
| :------------------------ | :-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name                      | A descriptive name for this upstream source. A shortened version of this name will be used for tagging cached packages retrieved from this upstream.                                                            |
| Priority                  | The weighting of the Upstream source. Upstream sources are selected for resolving requests by sequential order (1..n), followed by creation date.                                                               |
| Upstream URL              | The URL for this upstream source. This must be a fully qualified URL including any path elements required to reach the root of the repository.                                                                  |
| Proxy Only                | (Default) Proxy requests through to upstream sources in order to match assets that are not present in this repository.                                                                                          |
| Cache and Proxy           | Proxy the initial request for an asset through to the upstream source and then store (cache) resolved assets in this repository for future requests.                                                            |
| Cache Only                | Requests made for packages that aren't yet in this repository will self-redirect until available. This mode ensures that packages served are guaranteed to be signed with the associated repository signing key |
| Verify SSL Certificates   | If enabled, SSL certificates are verified when requests are made to this upstream. We recommended leaving this enabled for all public sources to help mitigate Man-In-The-Middle (MITM) attacks.                |
| GPG key                   | The source of a package signing key. When a signing key is provided, the Cloudsmith setup script will ensure this signing key is deployed to allow packages available on this upstream to be installed          |
| Authentication (optional) | Optional credentials that can be provided if the upstream is not publicly accessible                                                                                                                            |
| Headers (optional)        | Optional Key-Value headers that can be passed to upstreams with each request.                                                                                                                                   |

> 📘 Note
>
> Package caching is only supported for for Maven packages that have a `.pom` file present on the upstream source.

### Create a Debian Upstream

<Image title="deb-upstream.png" alt={652} align="center" width="50% " border={true} src="https://files.readme.io/b97ce68-deb-upstream.png">
  Create Debian Upstream Form
</Image>

| Form Field                | Description                                                                                                                                                                                      |
| :------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name                      | A descriptive name for this upstream source. A shortened version of this name will be used for tagging cached packages retrieved from this upstream.                                             |
| Priority                  | The weighting of the Upstream source. Upstream sources are selected for resolving requests by sequential order (1..n), followed by creation date.                                                |
| Upstream URL              | The URL for this upstream source. This must be a fully qualified URL including any path elements required to reach the root of the repository.                                                   |
| Proxy Only                | (Default) Proxy requests through to upstream sources in order to match assets that are not present in this repository.                                                                           |
| Cache and Proxy           | Proxy the initial request for an asset through to the upstream source and then store (cache) resolved assets in this repository for future requests.                                             |
| Distribution Version      | The distribution version that packages from the upstream will be associated with.                                                                                                                |
| Upstream Component        | The component to fetch from the upstream.                                                                                                                                                        |
| Upstream Distribution     | (optional) The distribution to fetch from the upstream. Useful for repositories that have custom naming schemes. If left blank, the Distribution Version will be used.                           |
| Source Packages           | If selected, source packages will be available from the upstream.                                                                                                                                |
| Verify SSL Certificates   | If enabled, SSL certificates are verified when requests are made to this upstream. We recommended leaving this enabled for all public sources to help mitigate Man-In-The-Middle (MITM) attacks. |
| Authentication (optional) | Optional credentials that can be provided if the upstream is not publicly accessible                                                                                                             |
| Headers (optional)        | Optional Key-Value headers that can be passed to upstreams with each request.                                                                                                                    |

### Create a Docker Upstream

<Image alt="Create Docker Upstream Form" align="center" width="50% " border={true} src="https://files.readme.io/207f524-docker-upstream-form.png">
  Create Docker Upstream Form
</Image>

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Form Field
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Name
      </td>

      <td>
        A descriptive name for this upstream source. A shortened version of this name will be used for tagging cached packages retrieved from this upstream.
      </td>
    </tr>

    <tr>
      <td>
        Priority
      </td>

      <td>
        The weighting of the Upstream source. Upstream sources are selected for resolving requests by sequential order (1..n), followed by creation date.
      </td>
    </tr>

    <tr>
      <td>
        Upstream URL
      </td>

      <td>
        The URL for this upstream source. This must be a fully qualified URL including any path elements required to reach the root of the repository.
      </td>
    </tr>

    <tr>
      <td>
        Proxy Only
      </td>

      <td>
        Proxy requests through to upstream sources in order to match assets that are not present in this repository.
      </td>
    </tr>

    <tr>
      <td>
        Cache and Proxy
      </td>

      <td>
        Proxy the initial request for an asset through to the upstream source and then store (cache) resolved assets in this repository for future requests.
      </td>
    </tr>

    <tr>
      <td>
        Verify SSL Certificates
      </td>

      <td>
        If enabled, SSL certificates are verified when requests are made to this upstream. We recommended leaving this enabled for all public sources to help mitigate Man-In-The-Middle (MITM) attacks.
      </td>
    </tr>

    <tr>
      <td>
        Authentication (optional)
      </td>

      <td>
        Optional credentials that can be provided if the upstream is not publicly accessible.

        * \*Note\*\*: Docker Hub requires that requests to their service via an upstream proxy be authenticated. As such, when you configure an upstream to Docker Hub, you will be required to provide credentials for authentication.
      </td>
    </tr>

    <tr>
      <td>
        Headers (optional)
      </td>

      <td>
        Optional Key-Value headers that can be passed to upstreams with each request.
      </td>
    </tr>
  </tbody>
</Table>

### Create a RPM Upstream

<Image title="create-redhat-upstream.png" alt={590} align="center" width="50% " border={true} src="https://files.readme.io/298e572-create-redhat-upstream.png">
  Create RedHat Upstream Form
</Image>

| Form Field                 | Description                                                                                                                                                                                             |
| :------------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Name                       | A descriptive name for this upstream source. A shortened version of this name will be used for tagging cached packages retrieved from this upstream.                                                    |
| Weighting                  | The weighting of the Upstream source. Upstream sources are selected for resolving requests by sequential order (1..n), followed by creation date.                                                       |
| Upstream URL               | The URL for this upstream source. This must be a fully qualified URL including any path elements required to reach the root of the repository.                                                          |
| Proxy Only                 | (Default) Proxy requests through to upstream sources in order to match assets that are not present in this repository.                                                                                  |
| Cache and Proxy            | Proxy the initial request for an asset through to the upstream source and then store (cache) resolved assets in this repository for future requests.                                                    |
| Distribution               | The distribution version to index from the upstream, such as el/8r or fedora/32.                                                                                                                        |
| Source Packages            | If selected, source packages will be available from the upstream.                                                                                                                                       |
| Verify SSL Certificates    | If enabled, SSL certificates are verified when requests are made to this upstream. We recommended leaving this enabled for all public sources to help mitigate Man-In-The-Middle (MITM) attacks.        |
| GPG Key                    | The source of a package signing key. When a signing key is provided, the Cloudsmith setup script will ensure this signing key is deployed to allow packages available on this upstream to be installed. |
| Authentication  (optional) | Optional credentials that can be provided if the upstream is not publicly accessible                                                                                                                    |
| Headers (optional)         | Optional Key-Value headers that can be passed to upstreams with each request.                                                                                                                           |

### Create a NPM Upstream

<Image alt="Create NPM Upstream Form" align="center" width="50% " border={true} src="https://files.readme.io/f636a21-npm-upstream-form.png">
  Create NPM Upstream Form
</Image>

| Form Field                | Description                                                                                                                                                                                      |
| :------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name                      | A descriptive name for this upstream source. A shortened version of this name will be used for tagging cached packages retrieved from this upstream.                                             |
| Priority                  | The weighting of the Upstream source. Upstream sources are selected for resolving requests by sequential order (1..n), followed by creation date.                                                |
| Upstream URL              | The URL for this upstream source. This must be a fully qualified URL including any path elements required to reach the root of the repository.                                                   |
| Proxy Only                | Proxy requests through to upstream sources in order to match assets that are not present in this repository.                                                                                     |
| Cache and Proxy           | Proxy the initial request for an asset through to the upstream source and then store (cache) resolved assets in this repository for future requests.                                             |
| Verify SSL Certificates   | If enabled, SSL certificates are verified when requests are made to this upstream. We recommended leaving this enabled for all public sources to help mitigate Man-In-The-Middle (MITM) attacks. |
| Authentication (optional) | Optional credentials that can be provided if the upstream is not publicly accessible                                                                                                             |
| Headers (optional)        | Optional Key-Value headers that can be passed to upstreams with each request.                                                                                                                    |

### Create a NuGet Upstream

<Image title="create-nuget-upstream.png" alt={655} align="center" width="50% " border={true} src="https://files.readme.io/5571ac4-create-nuget-upstream.png">
  Create NuGet Upstream Form
</Image>

| Form Field                | Description                                                                                                                                                                                      |
| :------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name                      | A descriptive name for this upstream source. A shortened version of this name will be used for tagging cached packages retrieved from this upstream.                                             |
| Priority                  | The weighting of the Upstream source. Upstream sources are selected for resolving requests by sequential order (1..n), followed by creation date.                                                |
| Upstream URL              | The URL for this upstream source. This must be a fully qualified URL including any path elements required to reach the root of the repository.                                                   |
| Proxy Only                | (Default) Proxy requests through to upstream sources in order to match assets that are not present in this repository.                                                                           |
| Cache and Proxy           | Proxy the initial request for an asset through to the upstream source and then store (cache) resolved assets in this repository for future requests.                                             |
| Verify SSL Certificates   | If enabled, SSL certificates are verified when requests are made to this upstream. We recommended leaving this enabled for all public sources to help mitigate Man-In-The-Middle (MITM) attacks. |
| Authentication (optional) | Optional credentials that can be provided if the upstream is not publicly accessible                                                                                                             |
| Headers (optional)        | Optional Key-Value headers that can be passed to upstreams with each request.                                                                                                                    |

### Create a Python Upstream

<Image title="python-upstream-form.png" alt={596} align="center" width="50% " border={true} src="https://files.readme.io/ef8a9c3-python-upstream-form.png">
  Create Python Upstream Form
</Image>

| Form Field                | Description                                                                                                                                                                                      |
| :------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name                      | A descriptive name for this upstream source. A shortened version of this name will be used for tagging cached packages retrieved from this upstream.                                             |
| Priority                  | The weighting of the Upstream source. Upstream sources are selected for resolving requests by sequential order (1..n), followed by creation date.                                                |
| Upstream URL              | The URL for this upstream source. This must be a fully qualified URL including any path elements required to reach the root of the repository.                                                   |
| Proxy Only                | Proxy requests through to upstream sources in order to match assets that are not present in this repository.                                                                                     |
| Cache and Proxy           | Proxy the initial request for an asset through to the upstream source and then store (cache) resolved assets in this repository for future requests.                                             |
| Verify SSL Certificates   | If enabled, SSL certificates are verified when requests are made to this upstream. We recommended leaving this enabled for all public sources to help mitigate Man-In-The-Middle (MITM) attacks. |
| Authentication (optional) | Optional credentials that can be provided if the upstream is not publicly accessible                                                                                                             |
| Headers (optional)        | Optional Key-Value headers that can be passed to upstreams with each request.                                                                                                                    |

### Create a Dart Upstream

<Image title="dart-upstream-form.png" alt={651} align="center" width="50% " border={true} src="https://files.readme.io/4649c25-dart-upstream-form.png">
  Create Dart Upstream Form
</Image>

| Form Field                | Description                                                                                                                                                                                      |
| :------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name                      | A descriptive name for this upstream source. A shortened version of this name will be used for tagging cached packages retrieved from this upstream.                                             |
| Priority                  | The weighting of the Upstream source. Upstream sources are selected for resolving requests by sequential order (1..n), followed by creation date.                                                |
| Upstream URL              | The URL for this upstream source. This must be a fully qualified URL including any path elements required to reach the root of the repository.                                                   |
| Proxy Only                | Proxy requests through to upstream sources in order to match assets that are not present in this repository.                                                                                     |
| Verify SSL Certificates   | If enabled, SSL certificates are verified when requests are made to this upstream. We recommended leaving this enabled for all public sources to help mitigate Man-In-The-Middle (MITM) attacks. |
| Authentication (optional) | Optional credentials that can be provided if the upstream is not publicly accessible                                                                                                             |
| Headers (optional)        | Optional Key-Value headers that can be passed to upstreams with each request.                                                                                                                    |

### Create a Ruby Upstream

<Image title="ruby-upstream-form.png" alt={656} align="center" width="50% " border={true} src="https://files.readme.io/8f7c417-ruby-upstream-form.png">
  Create Ruby Upstream Form
</Image>

| Form Field                | Description                                                                                                                                                                                      |
| :------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name                      | A descriptive name for this upstream source. A shortened version of this name will be used for tagging cached packages retrieved from this upstream.                                             |
| Priority                  | The weighting of the Upstream source. Upstream sources are selected for resolving requests by sequential order (1..n), followed by creation date.                                                |
| Upstream URL              | The URL for this upstream source. This must be a fully qualified URL including any path elements required to reach the root of the repository.                                                   |
| Proxy Only                | Proxy requests through to upstream sources in order to match assets that are not present in this repository.                                                                                     |
| Cache and Proxy           | Proxy the initial request for an asset through to the upstream source and then store (cache) resolved assets in this repository for future requests.                                             |
| Verify SSL Certificates   | If enabled, SSL certificates are verified when requests are made to this upstream. We recommended leaving this enabled for all public sources to help mitigate Man-In-The-Middle (MITM) attacks. |
| Authentication (optional) | Optional credentials that can be provided if the upstream is not publicly accessible                                                                                                             |
| Headers (optional)        | Optional Key-Value headers that can be passed to upstreams with each request.                                                                                                                    |

### Create a Swift Upstream

<Image title="ruby-upstream-form.png" alt={656} align="center" width="50% " border={true} src="https://files.readme.io/a8a3d71-Screenshot_2024-04-24_at_12.13.26.png">
  Create Swift Upstream Form
</Image>

| Form Field                | Description                                                                                                                                                                                      |
| :------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name                      | A descriptive name for this upstream source. A shortened version of this name will be used for tagging cached packages retrieved from this upstream.                                             |
| Priority                  | The weighting of the Upstream source. Upstream sources are selected for resolving requests by sequential order (1..n), followed by creation date.                                                |
| Upstream URL              | The URL for this upstream source. This must be a fully qualified URL including any path elements required to reach the root of the repository.                                                   |
| Proxy Only                | Proxy requests through to upstream sources in order to match assets that are not present in this repository.                                                                                     |
| Cache and Proxy           | Proxy the initial request for an asset through to the upstream source and then store (cache) resolved assets in this repository for future requests.                                             |
| Verify SSL Certificates   | If enabled, SSL certificates are verified when requests are made to this upstream. We recommended leaving this enabled for all public sources to help mitigate Man-In-The-Middle (MITM) attacks. |
| Authentication (optional) | Optional credentials that can be provided if the upstream is not publicly accessible                                                                                                             |
| Headers (optional)        | Optional Key-Value headers that can be passed to upstreams with each request.                                                                                                                    |

### Create a Hex Upstream

> 📘 Hex upstreams are in Early-Access.

<Image alt="Create Hex Upstream Form" align="center" width="50% " border={true} src="https://files.readme.io/0c227cb1c91e5d30a3ace17d4fe1ad34d756d7abf8d1970eba434c4180de49a3-Screenshot_2024-11-20_at_16.39.33.png">
  Create Hex Upstream Form
</Image>

| Form Field                 | Description                                                                                                                                                                                      |
| :------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name                       | A descriptive name for this upstream source. A shortened version of this name will be used for tagging cached packages retrieved from this upstream.                                             |
| Weighting                  | The weighting of the Upstream source. Upstream sources are selected for resolving requests by sequential order (1..n), followed by creation date.                                                |
| Upstream URL               | The URL for this upstream source. This must be a fully qualified URL including any path elements required to reach the root of the repository.                                                   |
| Proxy Only                 | (Default) Proxy requests through to upstream sources in order to match assets that are not present in this repository.                                                                           |
| Cache and Proxy            | Proxy the initial request for an asset through to the upstream source and then store (cache) resolved assets in this repository for future requests.                                             |
| Verify SSL Certificates    | If enabled, SSL certificates are verified when requests are made to this upstream. We recommended leaving this enabled for all public sources to help mitigate Man-In-The-Middle (MITM) attacks. |
| Authentication  (optional) | Optional credentials that can be provided if the upstream is not publicly accessible                                                                                                             |
| Headers (optional)         | Optional Key-Value headers that can be passed to upstreams with each request.                                                                                                                    |

### Create a CRAN Upstream

<Image title="ruby-upstream-form.png" alt={656} align="center" width="50% " border={true} src="https://files.readme.io/3456f59-Screenshot_2024-04-24_at_12.13.41.png">
  Create CRAN Upstream Form
</Image>

| Form Field                | Description                                                                                                                                                                                      |
| :------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Name                      | A descriptive name for this upstream source. A shortened version of this name will be used for tagging cached packages retrieved from this upstream.                                             |
| Priority                  | The weighting of the Upstream source. Upstream sources are selected for resolving requests by sequential order (1..n), followed by creation date.                                                |
| Upstream URL              | The URL for this upstream source. This must be a fully qualified URL including any path elements required to reach the root of the repository.                                                   |
| Proxy Only                | Proxy requests through to upstream sources in order to match assets that are not present in this repository.                                                                                     |
| Cache and Proxy           | Proxy the initial request for an asset through to the upstream source and then store (cache) resolved assets in this repository for future requests.                                             |
| Verify SSL Certificates   | If enabled, SSL certificates are verified when requests are made to this upstream. We recommended leaving this enabled for all public sources to help mitigate Man-In-The-Middle (MITM) attacks. |
| Authentication (optional) | Optional credentials that can be provided if the upstream is not publicly accessible                                                                                                             |
| Headers (optional)        | Optional Key-Value headers that can be passed to upstreams with each request.                                                                                                                    |

## Edit an Upstream Proxy

Click the blue "Edit Upstream" button to edit an upstream source:

![](https://files.readme.io/3373e70-Screenshot_2020-06-11_at_17.04.53.png "Screenshot 2020-06-11 at 17.04.53.png")

## Disable an Upstream Proxy

Click the orange "Disable Upstream" button to disable an upstream source:

![](https://files.readme.io/585fc06-Screenshot_2020-06-11_at_17.06.24.png "Screenshot 2020-06-11 at 17.06.24.png")

## Delete an Upstream Proxy

Click the red "Disable Upstream" button to disable an upstream source:

![](https://files.readme.io/68b36e8-Screenshot_2020-06-11_at_17.07.52.png "Screenshot 2020-06-11 at 17.07.52.png")