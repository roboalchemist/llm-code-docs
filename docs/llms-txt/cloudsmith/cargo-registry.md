# Source: https://help.cloudsmith.io/docs/cargo-registry.md

# Cargo Registry

Cloudsmith provides public & private registries for Cargo (Rust)

<Image align="center" width="100%" src="https://files.readme.io/6a0092c-rustbanner_new.png" />

For more information on Rust, please see:

* [Rust](https://www.rust-lang.org/): The official website for Rust language
* [Cargo](https://doc.rust-lang.org/cargo/index.html): The official documentation for Cargo - the Rust package manager
* [Crates Public Registry](https://crates.io/): The official Rust community’s crate registry

<HTMLBlock>
  {`
  <div class="row cs-box-row">
    <div class="cs-box cs-box-66 cs-box-green">
      <div class="cs-box-title cs-box-title-green">Contextual Documentation</div><p>
      The examples in this document are generic. Cloudsmith provides contextual setup instructions within each repository, complete with copy n' paste snippets (with your namespace/repo pre-configured).
      </p></div>
    <div class="cs-box cs-box-33 cs-box-grey cs-center-all">
      <a href="https://youtu.be/d6gxK5jXBWA" target="_blank">
      <img src="https://files.readme.io/25e8209-cloudsmith-youtube-play-cargo-small.png" /></a></div>
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
| REGISTRY\_NAME   | A name for the Cargo registry                                                             |
| PACKAGE\_NAME    | The name of your package                                                                  |
| PACKAGE\_VERSION | The version number of your package                                                        |
| PROJECT\_NAME    | The name of your Rust project                                                             |

## Upload a Package

### Upload via Cargo Publish

#### Setup

A name and URL for the registry must be added to your `.cargo/config` file as follows:

**Public Repositories**

```toml
[registries]
REGISTRY_NAME = { index = "https://dl.cloudsmith.io/public/OWNER/REPOSITORY/cargo/index.git" }
```

**Private Repositories**

<Callout icon="📘" theme="info">
  Private Cloudsmith repositories require authentication.  You can choose between two types of authentication, Entitlement Token Authentication or HTTP Basic Authentication.

  The setup method will differ depending on what authentication type you choose to use.
</Callout>

<Callout icon="🚧" theme="warn">
  Entitlement Tokens, User Credentials and API-Keys should be treated as secrets and you should ensure that you do not commit them in configurations files along with source code, or expose them in any logs
</Callout>

```text Entitlement Token Auth
[registries]
REGISTRY_NAME = { index = "https://dl.cloudsmith.io/TOKEN/OWNER/REPOSITORY/cargo/index.git" }
```

```toml HTTP Basic Auth
[registries]
REGISTRY_NAME = { index = "https://dl.cloudsmith.io/basic/OWNER/REPOSITORY/cargo/index.git" }
```

If using HTTP basic authentication, you'll need to configure Git with credentials. Git's standard authentication mechanisms are used by Cargo and can be configured in the normal way. For example, you could use git's per-user credential store as follows:

```shell HTTP Basic Auth (User & Pass)
git config --global credential.helper store
echo "https://USERNAME:PASSWORD@dl.cloudsmith.io" > ~/.git-credentials
```

```shell HTTP Basic Auth (API-Key)
git config --global credential.helper store
echo "https://USERNAME:API-KEY@dl.cloudsmith.io" > ~/.git-credentials
```

```shell HTTP Basic Auth (Token)
git config --global credential.helper store
echo "https://token:TOKEN@dl.cloudsmith.io" > ~/.git-credentials
```

For further details or other configuration options, see the [Official Git Documentation](https://git-scm.com/docs/gitcredentials).

In order to authenticate for publishing via cargo, you can either enter your credentials using the command:

```shell
cargo login --registry REGISTRY_NAME
```

Or, add your credentials to your `.cargo/credentials` file:

```toml
[registries.REGISTRY_NAME]
token = API-KEY
```

#### Publish

To publish a crate, you can do so from your project directory using cargo publish as follows:

```shell
cargo publish --registry REGISTRY_NAME
```

If you haven't specified credentials using one of the methods above, you'll be asked to provide them using `cargo login`.

You can also set the following environment variables:
`CARGO_REGISTRIES_<REGISTRY_NAME>_INDEX` - instead of setting the registry URL in `~/.cargo/config`
`CARGO_REGISTRIES_<REGISTRY_NAME>_TOKEN` - instead of providing credentials via `cargo login` or writing them to `~/.cargo/credentials`:

### Upload via the Cloudsmith CLI

For full details of how to install and setup the Cloudsmith CLI, see [Command Line Interface](https://help.cloudsmith.io/docs/upload-via-cloudsmith-cli-api).

The command to upload a cargo crate via the Cloudsmith CLI is:

```shell
cloudsmith push cargo OWNER/REPOSITORY PACKAGE_NAME.crate
```

Example:

```shell
cloudsmith push cargo org/repo your-package.crate
```

### Upload via Cloudsmith Website

Please see [Upload a Package](https://help.cloudsmith.io/docs/upload-via-website-ui) for details of how to upload via the Website UI.

***

## Download a Package

### Configure a new Upstream

Cloudsmith supports [https://index.crates.io](https://index.crates.io) as an upstream. This allows you to proxy and cache external Rust crates that are not part of your repository.

To enable the upstream, browse to your repository overview page and click in the Upstreams tab. Then, click on **+ Add Upstream Proxy** and then choose the **Cargo** Upstream.

In the Upstream creation menu, define a name your Upstream and in the **Proxy URL** field insert `https://index.crates.io/`. Click on **+ Create Upstream Proxy** and the upstream should become immediately available.

### Registry Setup

It is easy to add a Cloudsmith-based Cargo registry.

> 📘 Cargo Sparse Registry
>
> Cargo Sparse Registries are a new addition to Cargo as of v1.68.0, and are the recommended way to interact with your Cloudsmith Repositories - they offer significant performance advantages over the old Git-based registries, such as reducing the bandwidth used and improving dependency resolution times.

First, the name and config for the registry must be added to your `.cargo/config.toml` or `.cargo/config` file as follows:

#### Cargo >= v1.74 (HTTP Sparse Registry)

```toml API Key Auth
[registries.OWNER-REPOSITORY]
index = "sparse+https://cargo.cloudsmith.io/OWNER/REPOSITORY/"
token = "Token API-KEY"
credential-provider = "cargo:token"
```

```toml Entitlement Token Auth
[registries.OWNER-REPOSITORY]
index = "sparse+https://cargo.cloudsmith.io/OWNER/REPOSITORY/"
token = "Token TOKEN"
credential-provider = "cargo:token"
```

**Cargo\< v1.74 (HTTP Sparse Registry)**
If you are using Cargo version `< 1.74`, the only way to authenticate with a private sparse registry is using Cloudsmith's URL-based authentication.

```toml Entitlement Token Auth
[registries.OWNER-REPOSITORY]
index = "sparse+https://dl.cloudsmith.io/TOKEN/OWNER/REPOSITORY/cargo/"
```

#### Cargo \< v1.68 (Legacy Git Registry)

```toml HTTP Basic Auth (API-Key)
[registries]
OWNER-REPOSITORY = { index = "https://dl.cloudsmith.io/basic/OWNER/REPOSITORY/cargo/index.git" }
```

```toml URL Auth (Entitlement Token)
[registries]
OWNER-REPOSITORY = { index = "https://dl.cloudsmith.io/TOKEN/OWNER/REPOSITORY/cargo/index.git" }
```

### Registry Authentication

You must configure Git with the proper credentials to clone the registry when using HTTP basic authentication. Git's standard authentication mechanisms are used by Cargo and can be configured normally. For example, you could use git's per-user credential store like so:

```shell
git config --global credential.helper store
echo "https://USERNAME:API-KEY@dl.cloudsmith.io" > ~/.git-credentials
```

When using URL-based authentication, no further configuration is required, you're all set up and ready to go.

### Install a Package

Once you have configured a registry using one of the methods described above, a crate can then depend on a crate from your registry by specifying the registry key and a value of the registry's name in that dependency's entry in `Cargo.toml`:

```TOML
[package]
name = "PROJECT_NAME"
version = "0.1.0"
[dependencies]
PACKAGE_NAME = { version = "PACKAGE_VERSION", registry = "REGISTRY_NAME" }
```

You can also install a crate directly by specifying the registry on the command line:

```shell
cargo install PACKAGE_NAME --registry REGISTRY_NAME`
```

***

## Security Scanning

<br />

<span class="cs-tag cs-tag-dark-green">Supported</span>
Please see our

[Security Scanning](https://help.cloudsmith.io/docs/vulnerability-scanning) documentation for further information.

## Key Signing Support

<span class="cs-tag cs-tag-dark-grey">Not Supported.</span>

## Troubleshooting

Please see the [Troubleshooting](https://help.cloudsmith.io/docs/troubleshooting-cargo) page for further help and information.

<br />