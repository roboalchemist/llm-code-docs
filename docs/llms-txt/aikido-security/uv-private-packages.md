# Source: https://help.aikido.dev/aikido-autofix/connect-private-packages/uv-private-packages.md

# UV - Private Packages

For Aikido to update dependencies that include private packages, it needs access to your private registries so it can generate accurate lockfile updates. For UV, this can be achieved by adding the appropriate **environment variables** in Aikido.

## Credentials for package indexes <a href="#adding-credentials-with-environment-variables" id="adding-credentials-with-environment-variables"></a>

If you're adding [package indexes](https://docs.astral.sh/uv/concepts/indexes/) that require authentication in your `pyproject.toml`, you can provide the username and password for the indexes by setting up environment variables in Aikido. The environment variables should be created in the following format:

* `UV_INDEX_[INDEX_NAME]_USERNAME`
* `UV_INDEX_[INDEX_NAME]_PASSWORD`

Where the `[INDEX_NAME]` is the name of the index which you specified in your `pyproject.toml` file in uppercase. For example, set `UV_INDEX_PYTORCH_USERNAME` and `UV_INDEX_PYTORCH_PASSWORD` for the following project file:

```
[[tool.uv.index]]
name = "pytorch"
url = "https://download.pytorch.org/whl/cpu"
```

When creating a PR via Autofix, Aikido will include these environment variables when running `uv` commands.

## Setting a default index <a href="#adding-credentials-for-gcp-artifact-registry" id="adding-credentials-for-gcp-artifact-registry"></a>

If you're overriding the default index instead of adding a index in your `pyproject.toml` file, you can set the `UV_DEFAULT_INDEX` environment variable in Aikido.

## Configuration in Aikido

You can configure Aikido to authenticate with your private registry by following the steps below:

1. Go to your account's settings page for AutoFix, [here](https://app.aikido.dev/issues/fix/settings).
2. Click on “Connect Registry”, the configuration modal will now be shown.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FYFWXexDS4Gx3i7om01g6%2Fimage.png?alt=media&#x26;token=b12aa66b-e89a-4137-af11-eb975a34abfe" alt=""><figcaption></figcaption></figure>

1. Select the “UV” section.

<figure><img src="https://3149773201-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FyKbzcQGrx7UtrG0nPZZ7%2Fuploads%2FvEjZi2AxKrTMEsJAWB3U%2Fimage.png?alt=media&#x26;token=b1ce62fe-779d-45e4-b29a-6376c1af25d5" alt=""><figcaption></figcaption></figure>

1. Add the environment variables (eg. `UV_DEFAULT_INDEX`) required for your build file. All environment variables that start with `UV_` are allowed.
2. Click “*Connect Registry*” to save the configuration.
