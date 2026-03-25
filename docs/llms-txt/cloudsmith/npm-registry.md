# Source: https://help.cloudsmith.io/docs/npm-registry.md

# npm Registry

Cloudsmith provides public & private registries for npm (JavaScript)

<Image align="center" width="100%" src="https://files.readme.io/1a2340f-cloudsmith-npm-banner-hd.jpg" />

npm is an extremely popular package manager for the [JavaScript](https://en.wikipedia.org/wiki/JavaScript), and is used for creating and using packaged [Node.js](https://en.wikipedia.org/wiki/Node.js) modules. A public index of packages is available from npm, inc. on [npmjs.org](https://npmjs.org). npm, Inc also develop and maintain the official  `npm` client, ecosystem and tooling.

For more information on npm, please see:

* [npm](https://npmjs.org): The official website for npm

<HTMLBlock>
  {`
  <div class="row cs-box-row">
      <div class="cs-box cs-box-66 cs-box-green">
        <div class="cs-box-title cs-box-title-green">Contextual Documentation</div>
        <p>The examples in this document are generic. Cloudsmith provides contextual setup instructions within each repository, complete with copy n' paste snippets (with your namespace/repo pre-configured).</p>
      </div>
      <div class="cs-box cs-box-33 cs-center-all cs-box-grey">
        <a href="https://youtu.be/wjsXznlBBNA" target="_blank">
          <img src="https://files.readme.io/f4e7c30-cloudsmith-youtube-play-npm-small.png" /></a>
      </div>
    </div>
  `}
</HTMLBlock>

Cloudsmith is proud to support fully-featured registries for managing your own private and public npm packages.   We provide a high-level of compatibility with the official npmjs API meaning you can use the [official CLI client](https://docs.npmjs.com/cli/npm) -  `npm` - for installing, managing, and publishing npm packages to Cloudsmith. Or if you prefer you can use the Cloudsmith UI, API or  CLI - `cloudsmith`.

The Cloudsmith npm registry has been fully tested with the following:

* `npm` CLI version: v6.4.1
* `node` version: v6.11.3
* `yarn` version: v1.9.4

It is likely that it will work for other environments, including older and more recent  versions.  If you encounter any issues please [let us know](https://help.cloudsmith.io/docs/contact-us).

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
| TAG              | The name of an optional npm distribution tag                                              |

# Upload a Package

## Publish via npm

You can publish your npm packages to a Cloudsmith-based npm registry via the native npm tooling.

### Setup

The endpoint for the native npm API is:

```
https://npm.cloudsmith.io/OWNER/REPOSITORY/
```

To authenticate for native publishing, you can either use `npm login` or create an `npmrc` file (in your **$HOME** or in the project directory)

<Callout icon="📘" theme="info">
  NPM Version 9 introduced a change which consolidated the legacy authentication types.
  Please see the official NPM release notes **[here](https://github.blog/changelog/2022-10-24-npm-v9-0-0-released/)** for further details.
</Callout>

Use `npm login`:

```shell NPM < v9
npm login --registry=https://npm.cloudsmith.io/OWNER/REPOSITORY/
Username: USERNAME
Password: API-KEY
Email: YOUR-EMAIL-ADDRESS
```

```shell NPM v9 +
npm login --auth-type=legacy --registry=https://npm.cloudsmith.io/OWNER/REPOSITORY/
Username: USERNAME
Password: API-KEY
Email: YOUR-EMAIL-ADDRESS
```

Or create an `.npmrc` file with the following:

```
registry=https://npm.cloudsmith.io/OWNER/REPOSITORY/
//npm.cloudsmith.io/OWNER/REPOSITORY/:_authToken=API-KEY
```

### Publish

Once you have set up the registry, you can then publish from your project directory using `npm publish`:

```shell
npm publish --registry=https://npm.cloudsmith.io/OWNER/REPOSITORY/
```

For more details on `npm publish` see the official [npm documentation](https://docs.npmjs.com/cli/publish). (external link)

## Upload via the Cloudsmith CLI

For full details of how to install and setup the Cloudsmith CLI, see [Command Line Interface](https://help.cloudsmith.io/docs/cli).

To upload via the Cloudsmith CLI / API, you'll need to generate your package first. You can do this with:

```shell
npm pack
```

This will generate a tarball file (.tgz) like `your-package-1.2.3.tgz` that you can upload.

<Callout icon="📘" theme="info">
  This assumes that you've created a `project.json` file for your project. Please see the official npmjs \[package.json reference] ([https://docs.npmjs.com/files/package.json](https://docs.npmjs.com/files/package.json)) (external link) for more information.
</Callout>

The command to upload an npm package via the Cloudsmith CLI is:

```shell
cloudsmith push npm OWNER/REPOSITORY PACKAGE_NAME-PACKAGE_VERSION.tgz
```

Example:

```shell
cloudsmith push npm your-account/your-repo cloudsmithjs-1.0.0.tgz
```

## Upload via Cloudsmith Website

Please see [Upload a Package](https://help.cloudsmith.io/docs/upload-package#upload-via-website-ui) for details of how to upload via the Website UI.

## Scoped Packages

Using a package scope provides a different namespace to other similarly named packages to differentiate them.

To scope packages when publishing, add the scope to the name in your `package.json` file:

```json
{
  "name": "@SCOPE/PACKAGE-NAME"
}
```

<Callout icon="📘" theme="info">
  Replace **@SCOPE** with your own scope name
</Callout>

You can then [publish the package](https://help.cloudsmith.io/docs/npm-registry#upload-a-package) directly using `npm publish`, or generate the package with `npm pack` and then push via the Cloudsmith CLI or Website UI

You can find further information in the npm documentation on [scoped packages](https://docs.npmjs.com/misc/scope) (external link)

## Distribution Tags

Distribution tags allow npm packages to be tagged with a mnemonic that is associated with a specific package version.

Cloudsmith has full support for distribution tags and (mostly) follows the same rules for them as on npmjs.com:

1. A specific tag can point at one version of a package only.
2. A package version may have multiple unique tags.
3. Unless specified otherwise, the default tag for the last package published is latest.
4. When a package that is **latest** is deleted, the tag is moved to the next applicable version by [semver](https://docs.npmjs.com/misc/semver).
5. When a package is copied/moved to another repository, its tags are carried with it.
6. If the **latest** package is moved/deleted, then existing packages are sorted via SemVer to determine the next latest.

You can inspect a package to see what tags it has:

```shell
npm dist-tags ls PACKAGE_NAME --registry=https://npm.cloudsmith.io/OWNER/REPOSITORY/
```

You can add tags to a package:

```shell
npm dist-tags add PACKAGE_NAME@PACKAGE_VERSION TAG -
-registry=https://npm.cloudsmith.io/OWNER/REPOSITORY/
```

You can also remove tags from a package:

```shell
npm dist-tags rm PACKAGE_NAME TAG --registry=https://npm.cloudsmith.io/OWNER/REPOSITORY/
```

You can find out more about [distribution tags](https://docs.npmjs.com/adding-dist-tags-to-packages) in the npm documentation (external link).

***

# Download / Install a Package

## Setup

You can configure npm to use a Cloudsmith-based npm registry in one of two ways:

1. Specify the registry per user, as the global default or per-project
2. Provide the registry URL when executing `npm` commands

### Public Registries

To use/set the registry as the default for your user, execute the following:

```shell
npm config set registry https://npm.cloudsmith.io/OWNER/REPOSITORY/
```

You can set it globally (with permissions) by using the `-g` argument.

<Callout icon="📘" theme="info">
  Setting the registry globally will impact **all** npm commands unless they explicitly override the registry.
</Callout>

You can also add the registry directly to your user or project `.npmrc` file as follows:

```text
registry=https://npm.cloudsmith.io/OWNER/REPOSITORY/
```

Alternatively, you can specify the registry each time you execute `npm` commands, such as:

```shell
npm install PACKAGE_NAME --registry=https://npm.cloudsmith.io/OWNER/REPOSITORY/
```

### Private Registries

<Callout icon="📘" theme="info">
  Private Cloudsmith repositories require authentication.  You can choose between two types of authentication, Entitlement Token Authentication or HTTP Basic Authentication. The setup method will differ depending on what authentication type you choose to use.
</Callout>

<Callout icon="🚧" theme="warn">
  Entitlement Tokens, User Credentials and API-Keys should be treated as secrets, and you should ensure that you do not commit them in configurations files along with source code or expose them in any logs.
</Callout>

To set up the registry with authentication, add the one of the following to your user or project `.npmrc` file:

```text Entitlement Token Auth
registry=https://npm.cloudsmith.io/OWNER/REPOSITORY/
//npm.cloudsmith.io/OWNER/REPOSITORY/:_authToken=TOKEN
```

```shell HTTP Basic Auth (User & Pass)
registry=https://npm.cloudsmith.io/OWNER/REPOSITORY/
//npm.cloudsmith.io/OWNER/REPOSITORY/:username=USERNAME
//npm.cloudsmith.io/OWNER/REPOSITORY/:_password=PASSWORD
```

```shell HTTP Basic Auth (API-Key)
registry=https://npm.cloudsmith.io/OWNER/REPOSITORY/
//npm.cloudsmith.io/OWNER/REPOSITORY/:_authToken=API-KEY
```

```shell HTTP Basic Auth (Token)
registry=https://npm.cloudsmith.io/OWNER/REPOSITORY/
//npm.cloudsmith.io/OWNER/REPOSITORY/:username=token
//npm.cloudsmith.io/OWNER/REPOSITORY/:_password=TOKEN
```

> 📘 NOTE
>
> If using HTTP Basic Authentication with your Cloudsmith username and password or with a Cloudsmith Entitlement Token, you must encode your password or token in base64

## Install a Package

Once you have an authentication method configured, you can then install packages using:

```shell
npm install PACKAGE_NAME
```

If you have added tags to the package, then these tags  can be used as an alternative to the package version when installing packages, such as:

```shell
npm install PACKAGE_NAME@TAG --registry=https://npm.cloudsmith.io/OWNER/REPOSITORY/
```

### Scoped Registries

Using a registry scope tells npm to route installs for packages in that scope to Cloudsmith.
You can set it via the command-line using:

```shell
npm config set '@SCOPE:registry' https://npm.cloudsmith.io/OWNER/REPOSITORY/
```

You can also set it directly in your user or project `.npmrc` file:

```
@SCOPE:registry=https://npm.cloudsmith.io/OWNER/REPOSITORY/
```

Installing packages with a scope then requires putting the scope before the name:

```shell
npm install @SCOPE/PACKAGE_NAME
```

### Using Yarn with Cloudsmith

To ensure Yarn compatibility, enable `always-auth` by adding it to your user or project `.npmrc` or `.yarnrc.yml` file as shared below.

🔹 Yarn v1

Yarn v1 uses the same `.npmrc` format as npm:

```text .npmrc
registry=https://npm.cloudsmith.io/ORG/REPO/
//npm.cloudsmith.io/ORG/REPO/:_authToken=KEY
always-auth=true
```

🔹 Yarn v2 and later (Berry)

Yarn 2+ (*also known as Berry*) manages registries through `.yarnrc.yml` instead of `.npmrc`:

```Text .yarnrc.yml
npmRegistryServer: "https://npm.cloudsmith.io/ORG/REPO/"
npmAlwaysAuth: true
npmAuthIdent: "AUTHKEY"
```

The Auth key should be in base64, which you can get by running:

```
echo -n 'User:APIKEY' | base64
```

***

## Transparent Upstream Proxying

Cloudsmith supports transparent proxying of install requests to/from npmjs.com.
When enabled, requests for packages that don't exist in the registry will be automatically proxied.

With admin access to the registry, you can disable transparent upstream proxying by going to the settings page, unchecking the **Proxy npm Packages?** option, and then clicking Update:

<Image align="center" alt={1197} border={false} caption="npm proxy settings" title="npm-proxy-settings.png" src="https://files.readme.io/71451c4-npm-proxy-settings.png" />

<Callout icon="🚧" theme="warn">
  If transparent upstream proxying is disabled for the registry then you will need to fetch all dependencies of your packages manually. These can then be published into the registry, or you can bundle them with *bundleDependencies*.
</Callout>

***

## Security Auditing

Cloudsmith supports proxying of npm audit requests to detect vulnerabilities in dependencies, you just need to execute:

```shell
npm audit
```

> 📘 Note
>
> To use `npm audit`, you must authenticate using a Cloudsmith [API-Key](https://help.cloudsmith.io/docs/cli#getting-your-api-key), not an [Entitlement Token](https://help.cloudsmith.io/docs/entitlements).

You can find out more about [security auditing](https://docs.npmjs.com/getting-started/running-a-security-audit) in the npm documentation (external link).

# Current Limitations

The Cloudsmith npm registry implementation currently has the following limitations:

* The maximum size per-package file is currently limited to 100MiB (100 megabytes), but only when utilising the native npm-cli for publishing. If uploading using the cloudsmith-cli, then the absolute maximum size per-package file limit will be the standard 5GiB.

Cloudsmith is unlikely to support the following (out-of-scope):

* Profile, user, team or org commands; use the `cloudsmith-cli` instead.
* `npm access` and visibility; packages follow repository visibility.
* Viewing and changing collaborators of packages via 'npm owner'.
* Creating tokens via `npm token`; use the `cloudsmith-cli` or UI instead.
* Changes stream to implement followers; webhooks are a functional alternative.

Additionally, any search terms used are not passed to upstream repositories and are handled by Cloudsmith. Search results from upstream repositories are not blended into results; only Cloudsmith results are shown.

***

## Security Scanning

<br />

<span class="cs-tag cs-tag-dark-green">Supported</span>
Please see our

[Security Scanning](https://help.cloudsmith.io/docs/vulnerability-scanning) documentation for further information.

## Upstream Proxying / Caching

<span class="cs-tag cs-tag-dark-green">Configurable Proxying</span> <span class="cs-tag cs-tag-orange">Caching</span>
You can configure upstream NPM repositories you wish to use as additional package sources for your Cloudsmith repository. You can also choose to cache any requested packages for future use.

Please see our [Upstream Proxying](https://help.cloudsmith.io/docs/proxying) documentation for further instructions

## Key Signing Support

<span class="cs-tag cs-tag-blue">GPG</span>

## Troubleshooting

Please see the [Troubleshooting](https://help.cloudsmith.io/docs/troubleshooting) page for further help and information.