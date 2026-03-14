# Source: https://help.cloudsmith.io/docs/raw-repository.md

# Raw Repository

Cloudsmith provides public & private repositories for Raw files

![](https://files.readme.io/ad6ec1f-cloudsmith-raw-banner-hd.jpg "cloudsmith-raw-banner-hd.jpg")

Cloudsmith supports "Raw" files. Any file, any extension, suitable for datasets, images or whatever you want to throw at it. You get all the benefits of a Cloudsmith repository such as CLI uploads for automation, fine-grained access controls and logging/statistics (among others) - but for any file type at all.

<HTMLBlock>
  {`
  <div class="row cs-box-row">
    <div class="cs-box cs-box-66 cs-box-green">
      <div class="cs-box-title cs-box-title-green">Contextual Documentation</div><p>
      The examples in this document are generic. Cloudsmith provides contextual setup instructions within each repository, complete with copy n' paste snippets (with your namespace/repo/rsa-key pre-configured).
      </p></div>
    <div class="cs-box cs-box-33 cs-center-all cs-box-grey">
      <a href="https://youtu.be/t8fuyiGX328" target="_blank">
        <img src="https://files.readme.io/e39c2e6-cloudsmith-youtube-play-raw-small.png" /></a>
    </div>
  </div>
  </div>
  `}
</HTMLBlock>

> 📘
>
> RAW file support is not available on the Core (Free) Plan. Please see our [pricing page](https://cloudsmith.com/product/pricing/) for full details of features included at each plan level

In the following examples:

| Identifier  | Description                                                                               |
| :---------- | :---------------------------------------------------------------------------------------- |
| OWNER       | Your Cloudsmith account name or organization name (namespace)                             |
| REPOSITORY  | Your Cloudsmith Repository name (also called "slug")                                      |
| TOKEN       | Your Cloudsmith Entitlement Token (see [Entitlements](https://help.cloudsmith.io/docs/entitlements) for more details) |
| USERNAME    | Your Cloudsmith username                                                                  |
| PASSWORD    | Your Cloudsmith password                                                                  |
| API-KEY     | Your Cloudsmith API Key                                                                   |
| FILENAME    | The name of your file (i.e file.zip or file.txt etc)                                      |
| VERSION\_NO | The optional version number for a package                                                 |
| NAME        | The optional package name                                                                 |

## Upload a File

> 📘
>
> When you upload raw package, you can specify a package name with `--name` via the CLI, or via the Web UI upload form.
>
> If you specify a name that exactly matches the package filename, this is treated as if a name was not specified and the resulting [download links](https://help.cloudsmith.io/docs/raw-repository#download-via-command-line) will follow the format for a package that was uploaded without a name.

### Upload via the Cloudsmith CLI

For full details of how to install and setup the Cloudsmith CLI, see [Command Line Interface](https://help.cloudsmith.io/docs/cli)

The command to upload via the Cloudsmith CLI is:

```shell
cloudsmith push raw OWNER/REPOSITORY FILENAME
```

Example:

```shell
cloudsmith push raw your-account/your-repo file.zip
```

### Upload via Cloudsmith Website

Please see [upload a package](https://help.cloudsmith.io/docs/upload-package) for details of how to upload via the Website UI.

***

## Download a Package

### Download via Website UI

#### Public Repositories

When logged into Cloudsmith via a Web Browser, there's a "Download" button that's located within the traffic light button dropdown that provides a link to download a raw package on the package details page:

<Image align="center" src="https://files.readme.io/717e936e27b22feaee711ad6a412d1fade259c5768a4860d33ae5781152f8b68-download1.png" />

<br />

#### Private Repositories

For downloading from a private repository via the Website UI, you can use the "Use Package" button to download a raw package using the default Entitlement Token for the repository. You can also use the dropdown arrow within the pop-up window to pick a different way of authenticating for the download.

<Image align="center" src="https://files.readme.io/504971117e99871f745b0b730bb4a58894ae44fa903477f2cb7a0cde5f4b207c-Screenshot15.png" />

<Image align="center" src="https://files.readme.io/24ad1b20aff064e9bedd257dc6540675e6404f1ac4b8fd41ba5a3c0598fe70c2-Screenshot16.png" />

<br />

<Image align="center" src="https://files.readme.io/7e8cb09f8d0a00cf7a48375140d5a66d23c154720bfdc2912d9f7e569feda358-Screenshot17.png" />

<br />

### Download via Command Line

To download a Raw package, you'll need to fetch uploaded files using a well-crafted URL. You can find the specific URL for a raw package from the Cloudsmith CLI, with the `cloudsmith list packages` command and adding `-F pretty_json`.  The package URL is listed in the JSON output as `cdn_url`:

<Image title="cdn_url.png" alt={1155} align="center" src="https://files.readme.io/e123fa6-cdn_url.png">
  cdn\_url
</Image>

This URL is in the following formats; it varies based on if you uploaded the raw package with a package name, a version, both or none:

#### Public Repositories

```text Package Version
https://dl.cloudsmith.io/public/OWNER/REPOSITORY/raw/versions/VERSION_NO/FILENAME
```

```text Package Name and Version
https://dl.cloudsmith.io/public/OWNER/REPOSITORY/raw/names/NAME/versions/VERSION_NO/FILENAME
```

```text Package Name
https://dl.cloudsmith.io/public/OWNER/REPOSITORY/raw/names/NAME/files/FILENAME
```

```text None
https://dl.cloudsmith.io/public/OWNER/REPOSITORY/raw/files/FILENAME
```

Some example `curl` commands to download a raw package from a public repository:

A package with no package name or version specified at upload

```shell
curl -1sLf -O 'https://dl.cloudsmith.io/public/OWNER/REPOSITORY/raw/files/FILENAME'
```

A specific version of a package

```shell
curl -1sLf -O 'https://dl.cloudsmith.io/public/OWNER/REPOSITORY/raw/versions/VERSION_NO/FILENAME'
```

The latest version of the package

```shell
curl -1sLf -O 'https://dl.cloudsmith.io/public/OWNER/REPOSITORY/raw/versions/latest/FILENAME'
```

#### Private Repositories

> 📘
>
> Private Cloudsmith repositories require authentication.  You can choose between two types of authentication, Entitlement Token Authentication or HTTP Basic Authentication.
>
> The download URL will differ depending on what authentication type you choose to use.

> 🚧
>
> Entitlement Tokens, User Credentials and API-Keys should be treated as secrets, and you should ensure that you do not commit them in configurations files along with source code or expose them in any logs.

Raw Package uploaded with a version number:

```shell Entitlement Token Auth
https://dl.cloudsmith.io/TOKEN/OWNER/REPOSITORY/raw/versions/VERSION_NO/FILENAME
```

```shell HTTP Basic Auth
https://dl.cloudsmith.io/basic/OWNER/REPOSITORY/raw/versions/VERSION_NO/FILENAME'
```

Raw Package uploaded with a package name and version number:

```shell Entitlement Token Auth
https://dl.cloudsmith.io/TOKEN/OWNER/REPOSITORY/raw/names/NAME/versions/VERSION_NO/FILENAME
```

```shell HTTP Basic Auth
https://dl.cloudsmith.io/basic/OWNER/REPOSITORY/raw/names/NAME/versions/VERSION_NO/FILENAME'
```

Raw Package uploaded with a package name

```shell Entitlement Token Auth
https://dl.cloudsmith.io/TOKEN/OWNER/REPOSITORY/raw/names/NAME/files/FILENAME
```

```shell HTTP Basic Auth
https://dl.cloudsmith.io/basic/OWNER/REPOSITORY/raw/names/NAME/files/FILENAME
```

Raw Package uploaded without a package name or version number

```shell Entitlement Token Auth
https://dl.cloudsmith.io/TOKEN/OWNER/REPOSITORY/raw/files/FILENAME
```

```shell HTTP Basic Auth
https://dl.cloudsmith.io/basic/OWNER/REPOSITORY/raw/files/FILENAME
```

Some example `curl` commands to download a raw package from a private repository:

A package with no package name or version specified at upload using HTTP basic authentication:

```shell
curl -1sLf -u "USERNAME:PASSWORD" -O 'https://dl.cloudsmith.io/basic/OWNER/REPOSITORY/raw/files/FILENAME'
```

A specific version of a package using Entitlement Token authentication:

```shell
curl -1sLf -O 'https://dl.cloudsmith.io/TOKEN/OWNER/REPOSITORY/raw/versions/VERSION_NO/FILENAME'
```

## HTML / JSON Indexes

Cloudsmith supports serving Apache-style HTML and JSON formatted indexes of raw package files in the repository.  You can enable index generation in the [Repository Settings](https://help.cloudsmith.io/docs/repository-settings).

When enabled, the HTML index is available at:

#### Public Repositories

```
https://dl.cloudsmith.io/public/OWNER/REPOSITORY/raw/
```

#### Private Repositories

```shell Entitlement Token Auth
https://dl.cloudsmith.io/TOKEN/OWNER/REPOSITORY/raw/
```

```shell HTTP Basic Auth
https://dl.cloudsmith.io/basic/OWNER/REPOSITORY/raw/
```

The JSON index is available at:

#### Public Repositories

```
https://dl.cloudsmith.io/public/OWNER/REPOSITORY/raw/index.json
```

#### Private Repositories

```shell Entitlement Token Auth
https://dl.cloudsmith.io/TOKEN/OWNER/REPOSITORY/raw/index.json
```

```shell HTTP Basic Auth (User & Pass)
https://dl.cloudsmith.io/basic/OWNER/REPOSITORY/raw/index.json
```

***

## Upstream Proxying / Caching

<span class="cs-tag cs-tag-dark-grey">Not Supported</span>

## Key Signing Support

<span class="cs-tag cs-tag-blue">GPG</span>

### Viewing Package Signatures

Package signatures for raw files are presented in three ways:

* As a separate entry in the HTML index.
* As an object keyed by `signature` on each file entry with the JSON index.
* Directly, by appending `.asc` to a file URL.

#### HTML Index

HTML Indexes will output a separate `<li>` entry containing the URL for the signature for each file. Additionally, the checksum is available under the `data-checksum-sha256` attribute on the element:

<Image align="center" className="border" width="smart" border={true} src="https://files.readme.io/301d62a-Screenshot_2021-03-30_at_14.03.43.png" />

#### JSON Index

JSON indexes will attach the package signature URL and checksum values under the `checksum` key for each package object:

```json
{
   "packages" : [
      {
         "name" : "PACKAGE_NAME",
         "signature" : {
            "checksum_sha256" : "SIGNATURE_CHECKSUM",
            "url" : "https://dl.cloudsmith.io/TOKEN/OWNER/REPO/PACKAGE_IDENTIFIER/gpg.FILE_IDENTIFIER.asc"
         },
         ...
      }
   ]
}
```

#### File URL

For convenience, each of the file URLs listed above in 'Download a Package' can also map to the signature, by appending `.asc` to the URL. For example:

```shell
FILENAME="foo.zip"

# Retreive a file
curl -1sLf -O https://dl.cloudsmith.io/TOKEN/OWNER/REPO/raw/files/$FILENAME

# Retreive the signature for the file
curl -1sLf -O https://dl.cloudsmith.io/TOKEN/OWNER/REPO/raw/files/$FILENAME.asc
```

## Troubleshooting

Please see the [Troubleshooting](https://help.cloudsmith.io/docs/troubleshooting) page for further help and information.