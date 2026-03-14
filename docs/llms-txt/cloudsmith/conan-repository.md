# Source: https://help.cloudsmith.io/docs/conan-repository.md

# Conan Repository

Cloudsmith provides public & private repositories for Conan (C & C++)

<Image border={false} src="https://files.readme.io/29641a4-cloudsmith-pcb-conan.jpg" title="cloudsmith-pcb-conan.jpg" />

Conan is a dependency and package manager for C and C++. It is designed to help manage the development and Continuous Integration of C and C++ projects. We support both Conan v1 and v2.

> ⚠️ Note
>
> Conan v1 and v2 packages are not compatible with each other. If you have v1 packages uploaded in our platform these won't be visible when using the Conan v2 CLI and have to be re-uploaded with the proper recipe changes. Please refer to the [Conan v2 Migration Guide](https://docs.conan.io/1/conan_v2.html) on how to.

For more information please see:

* [Conan](https://conan.io/): The official Conan website
* [Conan Documentation](https://docs.conan.io/en/latest/index.html): The official docs for Conan

<HTMLBlock>
  {`
  <div class="row">
    <div class="cs-box cs-box-66 cs-box-green">
      <div class="cs-box-title cs-box-title-green">Contextual Documentation</div><p>
      The examples in this document are generic. Cloudsmith provides contextual setup instructions within each repository, complete with copy n' paste snippets (with your namespace/repo pre-configured).
      </p></div>
    <div class="cs-box cs-box-33 cs-box-grey cs-center-all">
      <a href="https://youtu.be/Jah8KHquwiM" target="_blank">
        <img src="https://files.readme.io/62b384d-cloudsmith-youtube-play-conan-small.png" /></a></div>
  </div>
  `}
</HTMLBlock>

In the following examples:

| Identifier       | Description                                                                               |
| :--------------- | :---------------------------------------------------------------------------------------- |
| OWNER            | Your Cloudsmith account name or organization name (namespace)                             |
| REPOSITORY       | Your Cloudsmith Repository name (also called "slug")                                      |
| TOKEN            | Your Cloudsmith Entitlement Token (see [Entitlements](https://help.cloudsmith.io/docs/entitlements) for more details) |
| USERNAME         | Your Cloudsmith username                                                                  |
| PASSWORD         | Your Cloudsmith password                                                                  |
| API-KEY          | Your Cloudsmith API Key                                                                   |
| PACKAGE\_NAME    | The name of your package                                                                  |
| PACKAGE\_VERSION | The version number of your package                                                        |

## Upload a Package

### Upload via Conan

The endpoint for the native Conan API is:

```
https://conan.cloudsmith.io/OWNER/REPOSITORY/
```

First, you need to set up the Repository as a Conan remote, with your Cloudsmith API-Key and Username for authentication:

```shell Shell - Conan v1
conan remote add OWNER-REPOSITORY https://conan.cloudsmith.io/OWNER/REPOSITORY/
conan user -p API-KEY -r OWNER-REPOSITORY USERNAME
```

```shell Shell - Conan v2
conan remote add OWNER-REPOSITORY https://conan.cloudsmith.io/OWNER/REPOSITORY/
conan remote login -p API-KEY OWNER-REPOSITORY USERNAME
```

You can then upload natively using [Conan](https://docs.conan.io/en/latest/reference/commands/creator/export.html) with the command:

```shell Shell - Conan v1
conan upload PACKAGE_NAME/PACKAGE_VERSION --all -r OWNER-REPOSITORY
```

```shell Shell - Conan v2
conan upload PACKAGE_NAME/PACKAGE_VERSION -r OWNER-REPOSITORY
```

An optional USER/CHANNEL can also be provided when uploading a package; this enables multiple versions of the same package to coexist using the user/channel to create a unique version of the package version:

```shell Shell - Conan v1
conan upload PACKAGE_NAME/PACKAGE_VERSION@USER/CHANNEL --all -r OWNER-REPOSITORY
```

```shell Shell - Conan v2
conan upload PACKAGE_NAME/PACKAGE_VERSION@USER/CHANNEL -r OWNER-REPOSITORY
```

The user/channel will also be used as a tag on the package which will allow for filtering within the UI.

### Upload via the Cloudsmith CLI or Website

> Note
>
> Uploading using the Cloudsmith CLI or Website is only supported for Conan v1 packages. For v2 packages please use the Conan CLI tooling.

#### Create a Package

To upload via the Cloudsmith API/CLI, you'll need to generate a package first. The following commands can be used to produce a package and collect the additional files required for upload (otherwise handled by `conan upload`).

<Callout icon="📘" theme="info">
  Please see the [Conan documentation](https://docs.conan.io/en/latest/reference/commands/creator/create.html) on creating packages for more information on building your own packages.
</Callout>

You can build a package with Conan by creating a new example project using new, create, and export:

```shell Shell - Conan v1
conan new PACKAGE_NAME/PACKAGE_VERSION -t
conan create .
conan install .
conan build .
conan package .
conan export .
```

To create a package, files need to be extracted from the Conan home directory:

```shell
export CLOUDSMITH_NAMESPACE=OWNER
export CLOUDSMITH_REPOSITORY=REPOSITORY
```

use `_` when user/channel is treated

```shell
path=/home/circleci/.conan/data/example-conan-package/0.0.1/_/_
```

List files in build directory (using wildcard to skip over autogenerated id):

```shell
info_file=$(ls -d $path/package/*/conaninfo.txt)
metadata_file=( "$path/export/conanfile.py" )
manifest_file=( "$path/export/conanmanifest.txt" )
package_directory=( "$path/export" )
```

Create an archive in the current directory for upload (metadata only):

```shell
tar -czf conan_package.tgz --absolute-names "$package_directory"
```

> 🚧 External network requests in conanfile.py
>
> When extracting metadata from the `conanfile.py`, Cloudsmith restricts all network access, meaning that any attempt to reach external services from within your `conanfile.py` will fail, potentially leading to package synchronization to fail.
>
> We recommend keeping your `conanfile.py` as simple as possible to ensure your upload does not encounter any issues.

#### Upload via Cloudsmith CLI

For full details of how to install and setup the Cloudsmith CLI, see [Command Line Interface](https://help.cloudsmith.io/docs/upload-via-cloudsmith-cli-api).

The package and additional files can then be uploaded via the Cloudsmith CLI. The following example shows an upload via the CLI.:

```shell
cloudsmith push conan "$CLOUDSMITH_NAMESPACE/$CLOUDSMITH_REPOSITORY" conan_package.tgz \
    --metadata-file "$metadata_file" \
    --info-file "$info_file"  \
    --manifest-file "$manifest_file"
```

#### Upload via Cloudsmith Website

Please see [Upload a Package](https://help.cloudsmith.io/docs/upload-via-website-ui) for details of how to upload via the Website UI.

***

## Download / Install a Package

### Setup

First, the remote repository must be created and then credentials can be added for a user as follows:

#### Public Repositories

```shell Shell - Conan v1
conan remote add OWNER-REPOSITORY https://conan.cloudsmith.io/OWNER/REPOSITORY/
conan user -p API-KEY -r OWNER-REPOSITORY USERNAME
```

```shell Shell - Conan v2
conan remote add OWNER-REPOSITORY https://conan.cloudsmith.io/OWNER/REPOSITORY/
conan remote login -p API-KEY OWNER-REPOSITORY USERNAME
```

#### Private Repositories

<Callout icon="📘" theme="info">
  Private Cloudsmith repositories require authentication.  You can choose between two types of authentication, Entitlement Token Authentication or HTTP Basic Authentication.

  The setup method will differ depending on what authentication type you choose to use.
</Callout>

<Callout icon="🚧" theme="warn">
  Entitlement Tokens, User Credentials and API-Keys should be treated as secrets, and you should ensure that you do not commit them in configurations files along with source code or expose them in any logs
</Callout>

```shell Entitlement Token Auth - Conan v1
conan remote add OWNER-REPOSITORY https://conan.cloudsmith.io/OWNER/REPOSITORY/
conan user -p TOKEN -r OWNER-REPOSITORY OWNER/REPOSITORY
```

```shell HTTP Basic Auth (User & Pass) - Conan v1
conan remote add OWNER-REPOSITORY https://conan.cloudsmith.io/OWNER/REPOSITORY/
conan user -p PASSWORD -r OWNER-REPOSITORY USERNAME
```

```shell HTTP Basic Auth (API Key) - Conan v1
conan remote add OWNER-REPOSITORY https://conan.cloudsmith.io/OWNER/REPOSITORY/
conan user -p API-KEY -r OWNER-REPOSITORY USERNAME
```

```shell HTTP Basic Auth (Token) - Conan v1
conan remote add OWNER-REPOSITORY https://conan.cloudsmith.io/OWNER/REPOSITORY/
conan user -p TOKEN -r OWNER-REPOSITORY token
```

```shell Entitlement Token Auth - Conan v2
conan remote add OWNER-REPOSITORY https://conan.cloudsmith.io/OWNER/REPOSITORY/
conan remote login -p TOKEN OWNER-REPOSITORY OWNER/REPOSITORY
```

```shell HTTP Basic Auth (User & Pass) - Conan v2
conan remote add OWNER-REPOSITORY https://conan.cloudsmith.io/OWNER/REPOSITORY/
conan remote login -p PASSWORD OWNER-REPOSITORY USERNAME
```

```shell HTTP Basic Auth (API Key) - Conan v2
conan remote add OWNER-REPOSITORY https://conan.cloudsmith.io/OWNER/REPOSITORY/
conan remote login -p API-KEY OWNER-REPOSITORY USERNAME
```

```shell HTTP Basic Auth (Token) - Conan v2
conan remote add OWNER-REPOSITORY https://conan.cloudsmith.io/OWNER/REPOSITORY/
conan remote login -p TOKEN OWNER-REPOSITORY token
```

### Install a Package

Once set up, Conan can download the package by running:

```shell Shell - Conan v1/v2
conan download PACKAGE_NAME/PACKAGE_VERSION@ -r OWNER-REPOSITORY
```

## Conan Revisions

> ⚠️ Note
>
> Package revisions uploads are only supported using Conan CLI. Uploading a v1 package with the Cloudsmith CLI or Website **doesn't create a revision**

Cloudsmith Conan repositores support [Package Revisions](https://docs.conan.io/1/versioning/revisions.html). By default all Conan v2 uploads use revisions.

### Enable revisions in Conan v1

When using the Conan v1 CLI you have to explicitly enable revisions by either:

* Adding `revisions_enabled=1` in the `[general]` section of your conan.conf file (preferred)
* Setting the `CONAN_REVISIONS_ENABLED=1` environment variable.

After enabling revisions, the `conan upload` command will upload revisions instead.

## Upstream Proxying / Caching

<span class="cs-tag cs-tag-dark-grey">Not Supported</span>

## Key Signing Support

<span class="cs-tag cs-tag-dark-grey">Not Supported by Format</span>

## Troubleshooting

Please see the [Troubleshooting Conan](https://help.cloudsmith.io/docs/troubleshooting-conan) page for further help and information.