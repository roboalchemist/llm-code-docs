# Source: https://help.cloudsmith.io/docs/copy-a-package.md

# Package Copy

We provide two ways to copy a package from one repository to another:

* Copy via the API using tools/integrations (such as the Cloudsmith CLI)
* Copy via the Website UI.

***

## Copy via the Cloudsmith CLI

### Identify a Package

To copy a package using the Cloudsmith CLI, you first need to identify the package.  See [Package Identification](https://help.cloudsmith.io/docs/identifying-a-package) for full instructions on identifying packages.

### Copy a Package

Once you have identified the package, you use the `cloudsmith copy` command to copy it:

```shell
cloudsmith copy OWNER/SOURCE_REPO/UNIQUE_ID  DESTINATION_REPO
```

For example:

```
cloudsmith copy demo/examples-repo/IGgZrwGFAkyU examples-repo-public
```

In the above example, we identified that the package we wished to copy had the Unique ID "IGgZrwGFAkyU", and we copied it from the source repository "examples-repo" to the destination repository "examples-repo-public":

<Image title="copy-pkg-cli.png" alt={878} align="center" width="smart" src="https://files.readme.io/73d2343-copy-pkg-cli.png">
  cloudsmith copy CLI example
</Image>

### Advanced Example

The example below would move all packages defined by the `-q` query from `YOUR-ACCOUNT/YOUR-REPO` to `YOUR-DEST-REPO` (note that the destination is NOT qualified by a `YOUR-ACCOUNT` namespace - This is because you can only copy/move packages from repositories in the same account, and not across accounts yet).

```shell bash
cloudsmith ls pkg OWNER/SOURCE_REPO -q 'YOUR-QUERY'/
-F json | jq '.data[] | .namespace + "/" + .repository + "/" + .slug' -r / 
| xargs -Ipackage cloudsmith copy package DESTINATION_REPO
```

for the `-q` query you can use any terms that you would use when searching for a package (see [Search / Filter Packages](https://help.cloudsmith.io/docs/search-filter-packages) for full details). For example:

`-q 'format:maven AND name:cloudsmith-api AND version:^0.21'`

This query would target all Maven packages named cloudsmith-api with version 0.21.\*

You can remove the query to target all packages. The only downside to this approach is that it might require multiple invocations if you have more than the page size limit.

***

## Copy via the Website UI

You can copy a package using the Website UI:

* Via the repository packages list
* Via the package detail page

### Copy via Repository Packages List

To copy a package via the Repository packages list, click the traffic sign button next to the right of the package then click "Copy" in the dropdown menu

<Image align="center" src="https://files.readme.io/c0fe9e7f6a94d3e67481271bf3b87c87854bc8dcd530bd9257af9084eb249fe5-pckgcopy.png" />

<br />

### Copy via Package Details page

To copy a package via the package details page, click the traffic light button next to the "Use Package" button in the upper right hand corner, then click on "Copy" in the dropdown menu

<Image align="center" src="https://files.readme.io/ae80b5ebfb4cc08804fde42b194168add7dcc0af33192fd6d772aef4e1624867-pckgcopy2.png" />

<br />

After clicking a "copy" button you will be presented with the Copy Package form.  Select the destination repository from the drop-down menu and click "Copy" to complete the package copy:

<Image align="center" src="https://files.readme.io/5c4d3d82e60dfc5aab3d4866add99550c5b4ecb7e8d387fb0bd29ac927e3b697-Screenshot_2024-11-12_at_2.11.39_PM.png" />

You will then get an on-screen message confirming that the package copy was successful.

### Bulk Package Copy

To copy more than one package to another repository, use the checkboxes beside the package names and then click the blue "copy package" button that appears at the top of the package list:

<Image title="bulk-package-copy-ui.png" alt={1310} align="center" src="https://files.readme.io/0824a39-bulk-package-copy-ui.png">
  Bulk Package Copy
</Image>

> 📘
>
> If you have selected a checkbox beside a package name, then package operations under the orange 'tool' button will be disabled as you are now in bulk operation mode.