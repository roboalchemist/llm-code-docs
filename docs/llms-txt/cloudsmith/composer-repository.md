# Source: https://help.cloudsmith.io/docs/composer-repository.md

# Composer Repository

Cloudsmith provides public & private repositories for Composer (php)

<Image align="center" width="100%" src="https://files.readme.io/7ed7d87-cloudsmith-composer-hd.jpg" />

Composer is a dependency management tool for PHP.

For more information on Composer, please see:

* [Composer](https://getcomposer.org/): The official website for Composer
* [Composer Documentation](https://getcomposer.org/doc/): The official docs for Composer

<HTMLBlock>
  {`
  <div class="row cs-box-row">
    <div class="cs-box cs-box-66 cs-box-green">
      <div class="cs-box-title cs-box-title-green">Contextual Documentation</div><p>
      The examples in this document are generic. Cloudsmith provides contextual setup instructions within each repository, complete with copy n' paste snippets (with your namespace/repo pre-configured).
      </p></div>
    <div class="cs-box cs-box-33 cs-box-grey cs-center-all">
      <a href="https://www.youtube.com/watch?v=DnqxKwJ6Oxs" target="_blank"><img src="https://files.readme.io/ac322ef-cloudsmith-youtube-play-composer-small.png" /></a></div>
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

### Upload via the Cloudsmith CLI

For full details of how to install and setup the Cloudsmith CLI, see [Command Line Interface](https://help.cloudsmith.io/docs/upload-via-cloudsmith-cli-api).

The command to upload a Composer package via the Cloudsmith CLI is:

```shell
cloudsmith push composer OWNER/REPOSITORY PACKAGE_NAME.phar
```

Example:

```shell
cloudsmith push composer org/repo your-package.phar
```

### Upload via Cloudsmith Website

Please see [Upload a Package](https://help.cloudsmith.io/docs/upload-via-website-ui) for details of how to upload via the Website UI.

***

## Download / Install a Package

### Setup

To enable the retrieval of Cloudsmith hosted packages via Composer, the first step is to add your repository to the repositories section of your `composer.json` file.  How you add your repository to your `composer.json` file differs if the repository is private or public.

#### Public Repositories

Add the following JSON snippet to your `composer.json` file:

```json
"repositories": [
  {
    "type": "composer",
    "url": "https://dl.cloudsmith.io/public/OWNER/REPOSITORY/composer/",
    "options": {
    }
  }
]
```

#### Private Repositories

<Callout icon="📘" theme="info">
  Private Cloudsmith repositories require authentication.  You can choose between two types of authentication, Entitlement Token Authentication or HTTP Basic Authentication.

  The setup method will differ depending on what authentication type you choose to use.
</Callout>

<Callout icon="🚧" theme="warn">
  Entitlement Tokens, User Credentials and API-Keys should be treated as secrets and you should ensure that you do not commit them in configurations files along with source code, or expose them in any logs
</Callout>

Add one of the following JSON snippets to your project `composer.json` file:

```json Entitlemet Token Auth
"repositories": [
  {
    "type": "composer",
    "url": "https://dl.cloudsmith.io/TOKEN/OWNER/REPOSITORY/composer/",
    "options": {
    }
  }
]
```

```json HTTP Basic Auth
"repositories": [
  {
    "type": "composer",
    "url": "https://dl.cloudsmith.io/basic/OWNER/REPOSITORY/composer/",
    "options": {
    }
  }
]
```

> 🚧 NOTE
>
> When using HTTP Basic Authentication you'll probably want to keep your credentials separately in your `auth.json` file instead of within the `composer.json` file. When you have your credentials ready, add one of the following JSON snippets to your `auth.json` file:

```json Username + Password
{
  "http-basic": {
    "dl.cloudsmith.io": {
      "username": "USERNAME",
      "password": "PASSWORD"
    }
  }
}
```

```json Username + API-Key
{
  "http-basic": {
    "dl.cloudsmith.io": {
      "username": "USERNAME",
      "password": "API-KEY"
    }
  }
}
```

```json Entitlement Token
{
  "http-basic": {
    "dl.cloudsmith.io": {
      "username": "token",
      "password": "TOKEN"
    }
  }
}
```

### Specifying Dependencies

After the repository is added to your `composer.json` file, you then specify the dependency in the **require** section of your `composer.json` file or using the `composer require` command:

#### via composer.json file

Add the following JSON snippet to your project `composer.json` file:

```json
{
  "require": {
    "PACKAGE_NAME": "PACKAGE_VERSION"
  }
}
```

#### via composer require

Use the following command:

```shell
composer require PACKAGE_NAME:PACKAGE_VERSION
```

***

### Installing a Package

To install the dependencies listed in your `composer.json` file use the command:

```shell
composer install
```

Composer will then resolve all dependencies listed in your `composer.json` file and download them into the `vendor` directory in your project.

### Configuration Example

The following is an example of a complete (but minimal) `composer.json` file with a public cloudsmith repository and a single dependency:

```json
{
  "repositories": [
    {
      "type": "composer",
      "url": "https://dl.cloudsmith.io/public/org/repo/composer/",
      "options": {}
    }
  ],
  "require": {
    "cloudsmith/cloudsmith-composer-example": "1.0.157954077030330"
  }
}
```

## Security Scanning

<br />

<span class="cs-tag cs-tag-dark-green">Supported</span>
Please see our

[Security Scanning](https://help.cloudsmith.io/docs/vulnerability-scanning) documentation for further information.

## Upstream Proxying / Caching

<span class="cs-tag cs-tag-dark-grey">Not Supported</span>

## Key Signing Support

<span class="cs-tag cs-tag-blue">GPG</span>

## Troubleshooting

Please see the [Troubleshooting](https://help.cloudsmith.io/docs/troubleshooting) page for further help and information.