# Source: https://help.cloudsmith.io/docs/entitlements-via-the-cloudsmith-cli.md

# Entitlements via the CLI

In the following examples:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Identifier
      </th>

      <th style={{ textAlign: "left" }}>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        OWNER
      </td>

      <td style={{ textAlign: "left" }}>
        Your Cloudsmith account name or organization name (namespace)
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        REPOSITORY
      </td>

      <td style={{ textAlign: "left" }}>
        Your Cloudsmith Repository name (also called "slug")
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        IDENTIFIER
      </td>

      <td style={{ textAlign: "left" }}>
        The unique identifier for an Entitlement Token
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        TOKEN-NAME
      </td>

      <td style={{ textAlign: "left" }}>
        The name of an Entitlement Token
      </td>
    </tr>

    <tr>
      <td style={{ textAlign: "left" }}>
        <span class="nobr">TOKEN-STRING</span>
      </td>

      <td style={{ textAlign: "left" }}>
        The token itself - It must only contain alphanumerics, dashes, dots or underscores and it must begin with an alphanumeric.
      </td>
    </tr>
  </tbody>
</Table>

## Listing Entitlement Tokens

To view all entitlement tokens for a repository, you use the `cloudsmith ents list` command:

```shell
cloudsmith ents list OWNER/REPOSITORY
```

Example:

```shell
cloudsmith ents list demo/examples-repo
```

This will show all the tokens associated with a repository and their creation / updated date and identifier.  The token identifier is unique to each individual entitlement token and is quite important, as you use it with other entitlement commands (such as delete)

<Image title="ents-list.png" alt={968} align="center" width="auto" src="https://files.readme.io/554186d-ents-list.png">
  ents list command
</Image>

Note that by default, the token itself is not shown.  To see the token, you must add the `--show-tokens` option to the command. For example:

```shell
cloudsmith ents list demo/examples-repo --show-tokens
```

<Image title="ents-list-show tokens.png" alt={970} align="center" width="auto" src="https://files.readme.io/060fd20-ents-list-show_tokens.png">
  ents list --show-tokens option
</Image>

***

## Creating Entitlement Tokens

To create an entitlement token via the Cloudsmith CLI, you use the `cloudsmith ents` command:

```shell
cloudsmith ents create OWNER/REPOSITORY --name=TOKEN-NAME
```

Example:

```shell
cloudsmith ents create demo/examples-repo --name=TestToken
```

The entitlement token identifier is shown in the output of the `cloudsmith create` command:

<Image title="ents-create.png" alt={968} align="center" width="auto" src="https://files.readme.io/b989057-ents-create.png">
  ents create command
</Image>

Additionally, you can manually specify the token itself (rather than have Cloudsmith create it for you) using the `--token=TOKEN-STRING` option:

```shell
cloudsmith ents create demo/examples-repo --name=TestToken --token=abcdef123456
```

![](https://files.readme.io/0e2a0b4-ents-create-string-show.png "ents-create-string-show.png")

> 📘
>
> If you manually specify a token, it must be between 8 - 48 characters in length.  It must only contain alphanumerics, dashes, dots or underscores and it must begin with an alphanumeric.

### Batch Create Example

If you wanted to create a batch of Entitlement Tokens at once, you could script it with a loop using the Cloudsmith CLI:

```shell bash
for I in $(seq 1 10); do
  cloudsmith ents create OWNER/REPOSITORY --name "Customer $I"
done
```

You could then retrieve a list of all entitlements, plus their tokens with:

```shell
cloudsmith ents ls OWNER/REPOSITORY --show-tokens -F json | jq -r '.data[] | "\(.name) = \(.token)"'
```

***

## Deleting Entitlement Tokens

Before you can delete an entitlement token, you need to get the identifier for the entitlement token. This can be obtained from the `cloudsmith ents list` command or from the `cloudsmith ents create` command.

To delete an entitlement token, you use the `cloudsmith ents delete` command:

```shell
cloudsmith ents delete OWNER/REPOSITORY/IDENTIFIER
```

Example:

```shell
cloudsmith ents delete demo/example-repo/Ym4xadpEU4YS
```

<Image title="ents-delete.png" alt={966} align="center" width="auto" src="https://files.readme.io/0061338-ents-delete.png">
  cloudsmith ents delete
</Image>

> 📘
>
> A deleted token will still be able to be used for static assets (that are cached at the Package Delivery Network) for approximately 10 minutes until the PDN has to re-authenticate once its cache expires

***

## Refreshing Entitlement Tokens

Refreshing an entitlement token generates a new token, but retains any permissions granted by the token.  This has the effect of invalidating the current token.

You can refresh an entitlement token using the `cloudsmith ents refresh` command:

```shell
cloudsmith ents refresh OWNER/REPOSITORY/IDENTIFIER
```

Example:

```shell
cloudsmith ents refresh demo/examples-repo/RJol6tyAIssl
```

<Image title="ents-refresh.png" alt={969} align="center" width="auto" src="https://files.readme.io/842d68e-ents-refresh.png">
  ents refresh command
</Image>

The example above shows the **TestToken** before and after using the `cloudsmith ents refresh` command.

***

## Updating Entitlement Tokens

To modify a token name or the token itself, you use the `cloudsmith ents update` command:

```shell
cloudsmith ents update OWNER/REPOSITORY/IDENTIFIER --name=TOKEN-NAME --token=TOKEN-STRING
```

Examples:

```shell
cloudsmith ents update demo/examples-repo/RJol6tyAIssl --name=NewTestToken
```

<Image title="ents-update-name.png" alt={969} align="center" width="auto" src="https://files.readme.io/462ea4b-ents-update-name.png">
  ents update --name command
</Image>

```shell
cloudsmith ents update demo/examples-repo/RJol6tyAIssl --token=abcedf123456
```

<Image title="ents-update-token.png" alt={968} align="center" src="https://files.readme.io/5d828ee-ents-update-token.png">
  ents update --token command
</Image>

> 📘
>
> A refreshed token will still be able to be used for static assets (that are cached at the Package Delivery Network) for approximately 10 minutes until the PDN has to re-authenticate once its cache expires

***

## Synchronising Tokens

You can synchronise all of the entitlement tokens from one Repository to another Repository using the `cloudsmith ents sync` command:

```shell
cloudsmith ents sync OWNER/TARGET-REPO  SOURCE-REPO
```

Example:

```shell
cloudsmith ents sync demo/demo-repo examples-repo
```

This example synchronises all the entitlement tokens from the **examples-repo** repository to the **demo-repo** repository:

<Image title="ents-sync.png" alt={967} align="center" width="auto" src="https://files.readme.io/f63b9f9-ents-sync.png">
  cloudsmith ents sync command
</Image>

If we now list the entitlement tokens in each of these repositories, we can see that they contain the same entitlement tokens:

<Image title="ents-sync-examples.png" alt={967} align="center" width="auto" src="https://files.readme.io/90429e4-ents-sync-examples.png">
  cloudsmith ents list examples-repo
</Image>

<Image title="ents-sync-demo.png" alt={969} align="center" src="https://files.readme.io/b6b7442-ents-sync-demo.png">
  cloudsmith ents list demo repo
</Image>

> 📘
>
> The token identifiers are still unique to each token, the token names and any associated permissions that the tokens grant are synchronised.

***

## Token Restrictions

You can add usage restrictions to a token with the `cloudsmith ents restrict` command:

```shell
cloudsmith ents restrict OWNER/REPOSITORY/IDENTIFIER <restriction-flags>
```

The available flags that you can add to set restrictions are:

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th>
        Restrict Command Flag
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        \--limit-bandwidth
      </td>

      <td>
        The maximum download bandwidth allowed for the token.  Please note that since downloads are calculated asynchronously (after\
        the download happens), the limit may not be imposed immediately but at a later point.
      </td>
    </tr>

    <tr>
      <td>
        \--limit-bandwidth-unit
      </td>

      <td>
        The unit of bandwidth to limit by. Note that 1GB = 1000000000 Bytes.
      </td>
    </tr>

    <tr>
      <td>
        \--limit-num-clients
      </td>

      <td>
        The maximum number of unique clients allowed for the token. Please note that since clients are calculated asynchronously (after the download happens), the limit may not be imposed immediately but at a later point.
      </td>
    </tr>

    <tr>
      <td>
        \--limit-num-downloads
      </td>

      <td>
        The maximum number of downloads allowed for the token. Please note that since downloads are calculated asynchronously (after the download happens), the limit may not be imposed immediately but at a later point.
      </td>
    </tr>

    <tr>
      <td>
        \--limit-package-query
      </td>

      <td>
        The package-based search query to apply to restrict downloads to. This uses the same syntax as the standard search used for repositories (see [Searching / Filtering](https://help.cloudsmith.io/docs/search-packages) for more details). This will still allow access to non-package files, such as metadata. For package formats that support dynamic metadata indexes, the contents of the metadata will also be filtered.
      </td>
    </tr>

    <tr>
      <td>
        \--limit-path-query
      </td>

      <td>
        The path-based search query to apply to restrict downloads to. This supports boolean logic operators such as OR/AND/NOT and parentheses for grouping. The path evaluated does not include the domain name, the namespace, the entitlement code used, the package format, etc. and it always starts with a forward slash.
      </td>
    </tr>

    <tr>
      <td>
        <span class="nobr">--limit-date-range-from</span>
      </td>

      <td>
        The starting date/time (UTC) that the token is allowed to be used from.
      </td>
    </tr>

    <tr>
      <td>
        \--limit-date-range-to
      </td>

      <td>
        The ending date/time (UTC) that the token is allowed to be used until.
      </td>
    </tr>

    <tr>
      <td>
        \--refresh-token
      </td>

      <td>
        The reset period used will be used to automatically trigger a reset of the token limits. Available options are daily, weekly, fortnightly, monthly, bi-monthly, quarterly and annual
      </td>
    </tr>
  </tbody>
</Table>

For Example:

```shell
cloudsmith entitlements restrict demo/examples-repo/GYwg00eEElKs \
        --limit-bandwidth=1 \
        --limit-bandwidth-unit=gigabyte \
        --limit-num-clients=10 \
        --limit-num-downloads=1000 \
        --limit-package-query="package-darwin-amd64"  \
        --limit-path-query=tag:latest \
        --limit-date-range-from=2020-01-01T00:00:00Z \
        --limit-date-range-to=2077-01-01T00:00:00Z \
        --refresh-token=daily
```

***

## Token Usage Metrics

You can check the bandwidth usage and token metrics for a repository with the `cloudsmith metrics` command:

### Repository Usage

You can check the total bandwidth usage for a repository with the `cloudsmith metrics tokens` command:

```shell
cloudsmith metrics tokens OWNER/REPOSITORY
```

Example:

```shell
cloudsmith metrics tokens demo/examples-repo
```

![](https://files.readme.io/902c9e6-metrics-tokens.png "metrics-tokens.png")

### Specific Token Usage

To check the bandwidth used by a specific token you add the `--tokens` parameter and the token identifier, or a comma-separated list of token identifiers, to the `cloudsmith metrics tokens` command:

```shell
cloudsmith metrics tokens OWNER/REPOSITORY --tokens=IDENTIFIER
```

Example:

```
cloudsmith metrics tokens demo/examples-repo --tokens= YcLoVS7BsLHf
```

![](https://files.readme.io/542ebc1-metrics-per-token.png "metrics-per-token.png")

In addition, you can add the `--start` and `--finish` parameters, to display usage for a specific time period:

Example:

```shell
cloudsmith metrics tokens demo/examples-repo --tokens=YcLoVS7BsLHf \
--start=2020-04-01T00:00:00Z --finish=2020-09-07T00:00:00Z
```

![](https://files.readme.io/86d8def-metrics-token-date.png "metrics-token-date.png")