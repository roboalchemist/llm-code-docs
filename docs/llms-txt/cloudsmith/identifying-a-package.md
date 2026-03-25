# Source: https://help.cloudsmith.io/docs/identifying-a-package.md

# Package Identification

To identify a package, you need to obtain the Unique ID for the package (also called *slug\_perm* for backward compatibility reasons)

You can get this either via the CLI or the Website UI.

***

## Obtaining Unique ID from the Cloudsmith CLI

You can get the Unique ID from the JSON output of the `cloudsmith list packages` command:

```shell
cloudsmith list packages OWNER/REPOSITORY -F pretty_json
```

The JSON output from this command includes the field `slug_perm` (Unique ID)

<Image title="UniqueID-CLI.png" alt={1201} align="center" src="https://files.readme.io/40d3d19-UniqueID-CLI.png">
  list packages JSON output
</Image>

You can use the `-q` flag to filter for a format or filename and pipe the output to a tool such as `jq` to further filter the fields from the JSON output.

Example:

```shell
 cloudsmith list packages demo/examples-repo -F pretty_json -q "format:cargo" | jq -r ".data[].filename, .data[].slug_perm"
```

<Image title="CLi-Slug-Perm-JQ.png" alt={825} align="center" src="https://files.readme.io/63d5fd8-CLi-Slug-Perm-JQ.png">
  Using jq to filter JSON output
</Image>

The Unique ID for a package is also displayed as part of the output when pushing a package to a repository using the `cloudsmith push` command:

<Image title="CLI-Push-slug-perm.png" alt={871} align="center" src="https://files.readme.io/c40c783-CLI-Push-slug-perm.png">
  Unique ID as part of `cloudsmith push` command output
</Image>

***

## Obtaining Unique ID from the Website UI

The Unique ID is also available in the Package information section of the package detail page.

<Image align="center" src="https://files.readme.io/e67ff4591a7b7a30a40c3086a0965c3db3812b09e8a5d82729604d5e2ccd6d04-package-identification.png" />