# Source: https://help.cloudsmith.io/docs/swift-registry.md

# Swift Registry

Cloudsmith provides public & private registries for Swift

<Image align="center" width="100%" src="https://files.readme.io/a1b9b4c-swift-banner-hd.png" />

The Swift Package Manager is a tool for managing the distribution of Swift code. It’s integrated with the Swift build system to automate the process of downloading, compiling, and linking dependencies. Cloudsmith is fully compatible as a Swift registry.

With Swift, developers can create, share, and manage packages for their projects.

For more information on Swift, please see:

* [Swift](https://www.swift.org/): The official website for Swift
* The [Swift registry](https://swiftpackageregistry.com/)  is a HTML catalog of Swift Packages which helps direct users to third-party Git repositories. It does not host swift packages.
* The [Swift package manager](https://www.swift.org/documentation/package-manager/) is a tool for managing the distribution of Swift code. It’s integrated with the Swift build system to automate the process of downloading, compiling, and linking dependencies.
* [Creating a Swift package](https://www.swift.org/getting-started/library-swiftpm/): Creating a Swift package

More detailed information about registry configuration can be found at: [Package Registry Usage.](https://cloudsmith.io/~cloudsmith-test/repos/buildkite-demo/setup/?show_all_formats=true#formats-swift:~:text=Package%20Registry%20Usage)

In the following examples:

| Identifier           | Description                                                                               |
| :------------------- | :---------------------------------------------------------------------------------------- |
| WORKSPACE            | Your Cloudsmith workspace name (namespace)                                                |
| REPOSITORY           | Your Cloudsmith Repository name (also called "slug")                                      |
| GIT\_REPOSITORY\_URL | GIT repository URL                                                                        |
| TOKEN                | Your Cloudsmith Entitlement Token (see [Entitlements](https://help.cloudsmith.io/docs/entitlements) for more details) |
| USERNAME             | Your Cloudsmith username                                                                  |
| PASSWORD             | Your Cloudsmith password                                                                  |
| API-KEY              | Your Cloudsmith API Key                                                                   |
| PACKAGE\_NAME        | The name of your package                                                                  |
| APP\_NAME            | The name of your application                                                              |
| VERSION              | The version number of your package                                                        |
| SCOPE                | Namespaces for package names                                                              |

# Configure Cloudsmith as your Swift Registry

## Create a Cloudsmith Repository

If you haven't already, create a repository in Cloudsmith where you'll publish your package. Note down the repository URL, which should resemble:

`https://swift.cloudsmith.io/WORKSPACE/REPOSITORY`

Replace WORKSPACE with your Cloudsmith organization name and REPOSITORY with the name of your repository.

## Creating a Swift package

If you haven't created a package already, Swift can create a new package

```shell
swift package init --name PACKAGE_NAME --type executable
Creating executable package: your-package
Creating Package.swift
Creating .gitignore
Creating Sources/
Creating Sources/main.swift
```

Create the Swift package by using the `swift package archive-source` command:

```shell
swift package archive-source
```

The terminals will output `Created PACKAGE_NAME.zip` if successful.

## Configure Cloudsmith as your Swift Registry

Use Swift version 5.9 or above (verify your version with `swift -version`) to publish Swift package to Cloudsmith using the Swift Package Manager. Then, set your Cloudsmith repository for the project:

```shell
swift package-registry set https://swift.cloudsmith.io/WORKSPACE/REPOSITORY/
```

This creates a configuration file at `.swiftpm/configuration/registries.json`that looks like this:

```shell
{
  "authentication" : {

  },
  "registries" : {
    "[default]" : {
      "supportsAvailability" : false,
      "url" : "https://swift.cloudsmith.io/cloudsmith-test/buildkite-demo"
    }
  },
  "version" : 1
```

Login to your private Cloudsmith Swift registry

```shell username and token
swift package-registry login https://swift.cloudsmith.io/WORKSPACE/REPOSITORY/ --username USERNAME --password API-KEY
```

```shell token
swift package-registry login --token API-KEY
```

> 📘
>
> Note: the `swift package-registry set` command sets the registry for your current project. However, it is possible to configure this registry as Swift's global package registry using the --global flag. It will write the registry configuration into the user configuration file at `~/.swiftpm/configuration/registries.json`.

# Upload a Package

## Upload using Swift Package Manager

A Swift package consists of Swift source files and a manifest file. The manifest file, called Package.swift, defines the package’s name and its contents using the PackageDescription module.

Navigate to the Swift project directory that contains the `Package.swift` file for your package. Replace `SCOPE`, `PACKAGE_NAME` and `VERSION` with the scope of the package, package name and package version respectively.

```shell
swift package-registry publish SCOPE.PACKAGE_NAME VERSION
```

> 📘 Swift scopes
>
> In Swift, scope are namespaces for package names. You can publish any scope to your Cloudsmith repository. Package scopes are case-insensitive (for example, mona ≍ MONA).
>
> **Version numbers** should follow semantic versioning.

### Upload Verification

After publishing, You should receive a confirmation message similar to the following:

```shell
SCOPE.PACKAGE_NAME version VERSION was successfully published to https://swift.cloudsmith.io/WORKSPACE/REPOSITORY and is available at 'https://swift.cloudsmith.io/WORKSPACE/REPOSITORY/SCOPE/PACKAGE_NAME/VERSION'
```

You can verify that your package is available in your Cloudsmith repository by navigating to the repository URL in your browser or using the Cloudsmith CLI.

<Image align="center" src="https://files.readme.io/a3182b4eb9f00129a39275dd27296552135e82341568d5ac045a1e9f68ec7109-swift.png" />

## Alternative example: from source code

In the next steps we cover how to package an existing swift project from its source code in GitHub, and then upload it to a Cloudsmith repository. For this example, we'll be using **Alamofire**: a popular HTTP networking library written in Swift.

Download its source code and checkout version `5.9.1`:

```bash
cd .. # get back to the previous dir
git clone https://github.com/Alamofire/Alamofire.git --depth 1
cd Alamofire
git fetch --depth 1 origin tag 5.9.1
git checkout 5.9.1
```

To publish a package, you need to create a `package-metadata.json` file. This file provides essential details about the package.

Create this file in the root of the `Alamofire` directory and paste in the following content:

```json
{
    "author": {
        "name": "Alamofire Software Foundation",
        "email": "info@alamofire.org",
        "organization": {
            "name": "Alamofire Software Foundation"
        }
    },
    "description": "Elegant HTTP Networking in Swift",
    "licenseURL": "https://github.com/Alamofire/Alamofire/blob/master/LICENSE",
    "readmeURL": "https://github.com/Alamofire/Alamofire/blob/master/README.md",
    "repositoryURLs": [
        "https://github.com/Alamofire/Alamofire.git"
    ]
}
```

You are ready to publish the package to your Cloudsmith Registry. Follow the previous steps to configure and login to your registry (no need to run it again if you executed the previous example) and replace `WORKSPACE` and `REPOSITORY` with your own:

```bash
# swift package-registry set "https://swift.cloudsmith.io/WORKSPACE/REPOSITORY/"
# swift package-registry login https://swift.cloudsmith.io/WORKSPACE/REPOSITORY/ --username USERNAME --password API-TOKEN
swift package-registry publish alamofire.alamofire 5.9.1 --metadata-path ./package-metadata.json
```

**Done!** You've successfully published your Swift package to a Cloudsmith registry. You can now view the package in your Cloudsmith web app.

## Upload via the Cloudsmith CLI

> 📘 CLI installation and authentication
>
> For full details of how to install and setup the Cloudsmith CLI, see [Command Line Interface](/developer-tools/cli) documentation:
>
> * [Installation](/developer-tools/cli#installation).
> * [Authentication](/developer-tools/cli#getting-your-api-key).

To upload via the Cloudsmith CLI / API, you'll need to generate your package first. You can do this with:

```shell
swift package archive-source 
```

This will generate a zip file named `Alamofire.zip` that you can upload. Use the previous command to upload your new swift package via the Cloudsmith CLI and rememver to use a different version number (for example `5.9.2`):

```shell
cloudsmith push swift WORKSPACE/REPOSITORY PACKAGE_NAME.zip --name PACKAGE_NAME --version VERSION --scope SCOPE
```

The next output will be displayed:

```text
Checking swift package upload parameters ... OK
Checking Alamofire.zip file upload parameters ... OK
Requesting file upload for Alamofire.zip ... OK
Uploading Alamofire.zip:  [####################################]  100%
Creating a new swift package ... OK
Created: demo-docs/awesome-repo/alamofirezip-z54v (DIElCIDoFtvd)

Synchronising alamofirezip-z54v:  [####################################]  100%  Completed / Fully Synchronised                      

Package synchronised successfully in 51.71964 second(s)!
```

## Upload via Cloudsmith Website

Please see [Upload a Package](https://help.cloudsmith.io/docs/upload-package#upload-via-website-ui) for details of how to upload via the Website UI.

## Download / Install a Package

Now, let's see how to use the package from your registry in a new project:

1. Create a new directory for a sample project and `cd` into it.

```bash
cd ..
mkdir MySwiftApp && cd MySwiftApp
swift package init --type executable
```

2. **Configure the Registry for the New Project**: following the steps described above to configure Swift to use your Cloudsmith registry URL and then login to it.

3. **Add your project dependencies**:

> 📘 Package.swift
>
> Package dependencies are declared in the `Package.swift` file. Edit the `Package.swift` file in your application project folder to update the package dependencies to be used by your project:
>
> 1. In the dependencies section of `Package.swift`, add the package you want to use by adding its package identifier. The package identifier consists of the scope and package name separated by a period. See the code snippet following a later step for an example.
> 2. In the targets section of `Package.swift`, add the targets that will need to use the dependency.

The following is an example showing configured dependencies and targets sections in a `Package.swift` file to include Alamofire as a dependency:

```
// swift-tools-version: 5.9
import PackageDescription

let package = Package(
    name: "MySwiftApp",
    dependencies: [
        .package(id: "alamofire.alamofire", from: "5.9.1") // Add this line
    ],
    targets: [
        .executableTarget(
            name: "MySwiftApp",
            dependencies: [
                .product(name: "Alamofire", package: "alamofire.alamofire") // And this one
            ]
        ),
    ]
)
```

After this, use the `--replace-scm-with-registry` flag to prioritize fetching from your registry instead of Git.

```bash
swift package --replace-scm-with-registry resolve
```

You will see output indicating that Swift is downloading `alamofire.alamofire` directly from your Cloudsmith registry. You should see the following printed out when resolving dependancies

```
Computing version for alamofire.alamofire
Computed alamofire.alamofire at 5.9.2 (1.84s)
Fetching alamofire.alamofire
warning: 'alamofire.alamofire': alamofire.alamofire version 5.9.2 source archive from https://swift.cloudsmith.io/demo-docs/awesome-repo is not signed
Fetched alamofire.alamofire from cache (4.07s)
```

> 📘
>
> 📘 Using `id:` in your `Package.swift` is powerful. When you run `resolve` with the flag, Swift Package Manager will first try to find a matching version in your configured registry. If it fails, it can fall back to the Git repository specified in the `package-metadata.json` file. This provides a robust, hybrid approach.
>
> Downloading a large repository like Alamofire can take a significant amount of time, as you're cloning the entire history. Pulling a package from a registry is much faster. You only download a lightweight source archive (`.zip`) for the specific version you need, drastically reducing download times and CI/CD pipeline durations.

For a more detailed overview of Package Registries usage with Swift, visit their [docs](https://github.com/swiftlang/swift-package-manager/blob/main/Documentation/PackageRegistry/PackageRegistryUsage.md).

## Resetting your registry configuration

To reset your configuration:

```shell
swift package-registry unset
```

Or simply delete the `registries.json` files from your project and/or home directory:

```bash
rm -f ./.swiftpm/configuration/registries.json
```

To force Swift to re-resolve all your dependencies from scratch the next time you build or run your project and clear out the global Swift Package Manager cache on your machine, run:

```bash
swift package reset
swift package purge-cache
```

## Security Scanning

<span class="cs-tag cs-tag-dark-green">Supported</span>\
Please see our [Security Scanning](https://help.cloudsmith.io/docs/security-scanning) documentation for further information.

## Upstream Proxying / Caching

<span class="cs-tag cs-tag-dark-green">Configurable Proxying</span> <span class="cs-tag cs-tag-orange">Caching</span>

You can configure to proxy a private or public swift registry you wish to use for packages that are not available in your current Cloudsmith repository e.g. you can point to another Cloudsmith repository. In addition, you can also choose to cache any requested packages for future use.

> 📘 There is currently no public swift repository
>
> HTML catalogs of Swift Packages such as [Swift Package Registry](https://swiftpackageregistry.com/) that point to third-party Git repositories do not host any actual packages and so can't be added as an upstream.

Please see our [Upstream Proxying](https://help.cloudsmith.io/docs/proxying) documentation for further instructions.

## Key Signing Support

<span class="cs-tag cs-tag-red">Not supported</span>

## Troubleshooting

Please see the [Troubleshooting](https://help.cloudsmith.io/docs/troubleshooting) page for further help and information.