# Source: https://help.cloudsmith.io/docs/download-a-package.md

# Package Download

There are two basic ways to download a package from a Cloudsmith repository:

* via a native package manager
* via the Website UI

You cannot download a package directly using the API or CLI. However, you can use the API to obtain a URL that you can then use to download a package.

See the full [API documentation](https://api-prd.cloudsmith.io/v1/#/packages), including an interactive sandbox environment for you to test your API requests.

***

## Download via Native Package Manager

Each repository contains context-aware documentation for setting up and downloading packages using the native package managers (such as `apt`, `npm` or `gem` for example).  Click the "Push/Pull Packages" button:

<Image title="download-package-dropdown.png" alt={1313} align="center" width="80%" src="https://files.readme.io/1eca8f945afbcbd0def68f670005c0a0c1dbcc07f84f6c019ec019c91fdcaf07-Screenshot_2024-10-18_at_17.19.55.png">
  Select to Push/Pull a package
</Image>

This will bring you to a window with a list of all supported package manager formats:

<Image title="download-package-dropdown.png" alt={1313} align="center" width="80%" src="https://files.readme.io/ed2f3d085992aca572174bc5cb25082dbb0238fcbdc4e63733e84f6a6005035e-Screenshot_2024-10-18_at_17.33.23.png">
  Setup guides for native package managers
</Image>

For example, If you select "Ruby" from the window, you are then presented with the guide on how to Pull or Push a ruby package in this repository. Go to the Pull Package tab to learn how to download a ruby package from this repository:

<Image title="download-package-guide.png" alt={1303} align="center" width="80%" src="https://files.readme.io/50562fd781c105269f60131b2e591d7c6e3831a7014665fc83fe09f3b7644576-Screenshot_2024-10-18_at_17.35.26.png">
  Setup guide for Ruby packages
</Image>

The instructions for downloading and installing a package using a native package manager are available by pressing the  "Use Package" button on any package detail page:

<Image title="download-package-setup.png" alt={1313} align="center" width="80%" src="https://files.readme.io/7334dd0d345475a864276c376a8b42bcc363fac0e86241bc9771edd90b01b374-Screenshot_2024-10-18_at_17.41.26.png">
  Setup Tab on Package Detail page
</Image>

There you are presented with contextual instructions for how to use a package:

<Image title="download-package-setup.png" alt={1313} align="center" width="80%" src="https://files.readme.io/28159e2cca9d71bd9e49fdabc2838cbcdec26ee290e7498cc5177fafd8e8190e-Screenshot_2024-10-18_at_17.57.56.png">
  Instructions for using a package
</Image>

***

## Download via Website UI

You can download a package directly from the Cloudsmith Website.

### Public Repositories

You can download any package from the packages list by clicking the expose more button on the right of the page, or by clicking the green "Download" button on a package detail page:

<Image title="download-package-public.png" alt={1311} align="center" width="smart" src="https://files.readme.io/0a981bf89e760e965b64dd6a374fb30649f92babb75bc30b1d2a5b7559ee5f57-Screenshot_2024-10-18_at_18.03.30.png">
  Download buttons on packages list (public repository)
</Image>

<Image title="download-package-page-public.png" alt={1301} align="center" width="smart" src="https://files.readme.io/e1736e4e23c209e12d71d086223a665164c1d4dd733af34e0e72a71ef65d1ba3-Screenshot_2024-10-18_at_21.34.03.png">
  Download button on package detail page (public repository)
</Image>

***

### Private Repositories

Downloading packages from a private repository is a little different. Click the download button.

<Image title="download-package-auth.png" alt={1344} align="center" width="smart" src="https://files.readme.io/a82fde152f3f2e23d292ee0c2128fb81f5cb6313034d26ca7f86efe2f4e2dd45-Screenshot_2024-10-18_at_21.38.15.png">
  Download buttons on repository packages list (private repository)
</Image>

You will be prompted to enter an Entitlement token:

<Image title="download-package-auth.png" alt={1344} align="center" width="smart" src="https://files.readme.io/73d6a1bab060a26c5b9b9c9a9d83591ad9fd64e0e58ef49aa529b71f6a7b4373-Screenshot_2024-10-18_at_21.51.37.png">
  Download buttons on repository packages list (private repository)
</Image>

See [Entitlements](https://help.cloudsmith.io/docs/entitlements) and [Sharing a Private Package](https://help.cloudsmith.io/docs/sharing-a-private-package) for more details on Entitlement Tokens.

***

## Bulk Package Download

You cannot bulk download packages using the Website UI, but you can do it with a little scripting using the Cloudsmith CLI. The Cloudsmith CLI is Python-based, so it needs Python (2 or 3) installed, and is available via `pip` (`pip install cloudsmith-cli`).

The basic premise of these examples is that you use the Cloudsmith CLI to list the contents of the repository, extract the download URL for each package, and then download each package.

### Linux Example (bash)

Please ensure that you have first set up the Cloudsmith CLI with your API key (or pass it to the `cloudsmith` command using the `-k` flag). See the CLI documentation for full details: [Command-Line Interface](https://help.cloudsmith.io/docs/cli)

```shell Public Repository
account="your-account"
repository="your-repo"

urls=$(cloudsmith ls pkgs $account/$repository -F json | jq -r '.data[].cdn_url')
for url in $urls; do
  wget $url
done
```

```shell Private Repository
account="your-account"
repository="your-repo"
token="your-entitlement-token"

urls=$(cloudsmith ls pkgs $account/$repository -F json | jq -r '.data[].cdn_url')
for url in $urls; do
  wget  --http-user=$account --http-password=$token $url
done
```

These examples also use `jq` for filtering and processing the JSON returned by Cloudsmith CLI list packages (`cloudsmith ls`) command.

While using the `cdn_url` returned from the Cloudsmith CLI or API will work for downloading most packages, if you need to also download docker manifest files you can utilize a url in the following format to grab them\
`https://docker.cloudsmith.io/v2/<organization>/<repository>/<package name>/manifests/<tag>`

You can also add search queries to the command to limit what is downloaded, e.g:

To download files of version 1.0 only:\
`urls=$(cloudsmith ls pkgs $account/$repository -F json -q 'version:1.0' | jq -r '.data[].cdn_url')`

To download npm packages only:\
`urls=$(cloudsmith ls pkgs $account/$repository -F json -q 'format:npm' | jq -r '.data[].cdn_url')`

### Windows Example (Powershell 3.0)

Please ensure that you have added the Python scripts directory your PATH (when you install via `pip` it will tell you what the path is) and also that you've got your API key from [https://cloudsmith.io/user/settings/api/](https://cloudsmith.io/user/settings/api/) if the repository is private.

```powershell
$account = "your-account"
$repository = "your-repository"
$key = "your-API-key"

$json = $(cloudsmith.exe ls pkgs $account/$repository -F json -k $key)
$urls = $json | ConvertFrom-Json | ForEach-Object { $_.data.cdn_url }

$wc = New-Object System.Net.WebClient
$creds = new-object System.Net.NetworkCredential("token", $key)

Foreach ($url in $urls) {
  echo "Downloading $url ..."
  $filename = [System.IO.Path]::GetFileName($url)
  $cred_cache = new-object System.Net.CredentialCache
  $cred_cache.Add($url, "Basic", $creds)
  $wc.Credentials = $cred_cache
  $wc.DownloadFile($url, $filename)
}
```