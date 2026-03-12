# Source: https://help.cloudsmith.io/docs/dart-repository.md

# Dart Repository

Cloudsmith provides public & private repositories for Dart packages

![](https://files.readme.io/96fb6eb-banner_dart_hd.jpg "banner_dart_hd.jpg")

> 📘 Dart SDK
>
> Dart SDK version >= 2.15 is required to use Dart Repositories.

Dart is a client-optimized programming language developed by Google.

For more information on Dart, please see:

* [Dart.dev](https://dart.dev/): The official website for Dart
* [Pub.dev](https://pub.dev/): The official public repository for Dart packages

<HTMLBlock>
  {`
  <div class="row cs-box-row">
      <div class="cs-box cs-box-66 cs-box-green">
        <div class="cs-box-title cs-box-title-green">Contextual Documentation</div>
        <p>The examples in this document are generic. Cloudsmith provides contextual setup instructions within each repository, complete with copy n' paste snippets (with your namespace/repo pre-configured).</p>
      </div>
      <div class="cs-box cs-box-33 cs-box-grey cs-center-all">
        <a href="https://youtu.be/cpW4fK_y4zU" target="_blank">
          <img src="https://files.readme.io/2c343eb-cloudsmith-youtube-play-dart-small.png" /></a>
      </div>
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
| DEPENDENCY\_NAME | A name for a dependency in a pubspec file                                                 |

## Upload a Package

### Publish via Dart

<Callout icon="📘" theme="info">
  Please note that Dart SDK version 2.15.1 or newer is required for native upload support. For older client versions, please continue to use the Cloudsmith CLI/API.
</Callout>

The endpoint for the native Dart API is:

```
https://dart.cloudsmith.io/OWNER/REPOSITORY/
```

Your project `pubspec.yaml` defines the location that artifacts should be published to. Add the following to the root of this file:

```yaml
publish_to: https://dart.cloudsmith.io/OWNER/REPOSITORY/
```

In order to authenticate for native publishing, you'll need run `dart pub token`, as follows:

```shell
echo 'API-KEY' | dart pub token add https://dart.cloudsmith.io/OWNER/REPOSITORY/
Enter secret token:
Requests to "https://dart.cloudsmith.io/OWNER/REPOSITORY/" will now be authenticated using the secret token.
```

You can then publish from your project directory using `dart pub publish`:

```
dart pub publish
Uploading...
Upload complete. Package will available following synchronisation.
```

> 📘 Limitation:
>
> When publishing via the native API package sizes are limited to 200.0 MB per file. If this is an issue, please use the Cloudsmith CLI or API (which support up to 5GB for single-part uploads and beyond for multi-part), or contact us if that's not an option.

### Upload via the Cloudsmith CLI

<Callout icon="📘" theme="info">
  Please see Dart's [documentation on creating packages](https://dart.dev/guides/libraries/create-library-packages) for more information on building your own packages.
</Callout>

#### Creating Dart Packages

To upload via the Cloudsmith API/CLI, you'll need to generate a package first. While we expect the tooling in this area to improve over time, currently the process is a manual one and can be a little tricky.

You can build a package with standard command-line tooling like `tar`. To illustrate the process we'll use [cli\_util](https://github.com/dart-lang/cli_util) as an example:

First, check out the version of cli\_util we want to pack (**v0.1.3** for example purposes):

```shell
git clone https://github.com/dart-lang/cli_util@v0.1.3
cd cli_util
```

```shell
tar --exclude='.dart_tool' -czvf cli_util_0.1.3.tar.gz ./*
```

For full details of how to install and setup the Cloudsmith CLI, see [Command Line Interface](https://help.cloudsmith.io/docs/upload-via-cloudsmith-cli-api).

The command to upload a Dart package via the Cloudsmith CLI is:

```shell
cloudsmith push dart OWNER/REPOSITORY PACKAGE_NAME-PACKAGE_VERSION.tgz
```

Example:

```shell
cloudsmith push dart org/repo your-package-1.0.0.tgz
```

### Upload via Cloudsmith Website

Please see [Upload a Package](https://help.cloudsmith.io/docs/upload-via-website-ui) for details of how to upload via the Website UI.

***

## Download / Install a Package

### Setup

**Public Repositories**

No further setup is required with public repositories, you can add a dependency from this repository to your package `pubspec.yaml` automatically with `dart pub`. See [Installing a Package](https://help.cloudsmith.io/docs/dart-repository#sdk-version--215)

**Private Repositories**

In order to authenticate, you need to run `dart pub token`, as follows:

```shell Entitlement Token Auth
echo 'TOKEN' | dart pub token add https://dart.cloudsmith.io/OWNER/REPOSITORY/
Enter secret token:
Requests to "https://dart.cloudsmith.io/OWNER/REPOSITORY/" will now be authenticated using the secret token.
```

```yaml HTTP Basic Auth (User & Pass)
echo 'PASSWORD' | dart pub token add https://dart.cloudsmith.io/OWNER/REPOSITORY/
Enter secret token:
Requests to "https://dart.cloudsmith.io/OWNER/REPOSITORY/" will now be authenticated using the secret token.
```

```yaml HTTP Basic Auth (API-Key)
echo 'API-KEY' | dart pub token add https://dart.cloudsmith.io/OWNER/REPOSITORY/
Enter secret token:
Requests to "https://dart.cloudsmith.io/OWNER/REPOSITORY/" will now be authenticated using the secret token.
```

```yaml HTTP Basic Auth (Token)
echo 'TOKEN' | dart pub token add https://dart.cloudsmith.io/OWNER/REPOSITORY/
Enter secret token:
Requests to "https://dart.cloudsmith.io/OWNER/REPOSITORY/" will now be authenticated using the secret token.
```

***

### Installing a Package

`dart pub` is capable of adding a dependency from this repository to your package `pubspec.yaml` automatically:

**Public Or Private Repositories**

```shell
dart pub add PACKAGE_NAME:PACKAGE_VERSION --hosted-url https://dart.cloudsmith.io/OWNER/REPOSITORY/
Resolving dependencies...
+ your-package 1.2.3
Downloading your-package 1.2.3...
Changed 1 dependency!
```

***

Please also see the [pubspec docs](https://dart.dev/tools/pub/pubspec) for further examples of pubspec files.

## Security Scanning

<span class="cs-tag cs-tag-dark-green">Supported</span>

Please see our [Security Scanning](https://help.cloudsmith.io/docs/vulnerability-scanning) documentation for further information.

## Upstream Proxying / Caching

<span class="cs-tag cs-tag-dark-green">Configurable Proxying</span> <span class="cs-tag cs-tag-orange">Caching</span>
You can configure upstream Dart repositories that you wish to use for packages that are not available in your Cloudsmith repository. Proxied Dart packages cannot currently be cached.

Please see our [Upstream Proxying](https://help.cloudsmith.io/docs/proxying) documentation for further instructions.

## Key Signing Support

<span class="cs-tag cs-tag-dark-grey">Not Supported by Format</span>

## Troubleshooting

Please see the [Troubleshooting](https://help.cloudsmith.io/docs/troubleshooting) page for further help and information.