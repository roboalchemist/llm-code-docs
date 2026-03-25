# Source: https://docs.port.io/customize-pages-dashboards-and-plugins/page/folders.md

# Folders

Port allows you to create folders in your [software catalog](https://app.getport.io/services) that can be used to group pages by topic, team, or any other criteria that fits the needs of your organization.

Folders can contain both [catalog pages](/customize-pages-dashboards-and-plugins/page/catalog-page.md) and [dashboard pages](/customize-pages-dashboards-and-plugins/page/dashboard-page.md), and can be nested up to 3 levels deep.

## Create a folder[â](#create-a-folder "Direct link to Create a folder")

To create a folder, simply click on `+ New` and choose `New folder`:

![](/img/software-catalog/pages/createNewFolder.gif)

<br />

<br />

You can also create a folder within another folder by clicking on the `...` button:

![](/img/software-catalog/pages/createNestedFolder.gif)

## Move pages between folders[â](#move-pages-between-folders "Direct link to Move pages between folders")

To move a page into/out of a folder, hover over it, hold the `â ¿` icon and drag it to your desired location and depth:

![](/img/software-catalog/pages/movePagesBetweenFolders.gif)

## Folder identifiers[â](#folder-identifiers "Direct link to Folder identifiers")

Each folder has a unique identifier that can be used to reference it when working with the [Port API](/api-reference/port-api.md).

When creating a folder, you will be asked to provide it with a title. The identifier is automatically generated from the titie using [snake\_case](https://en.wikipedia.org/wiki/Snake_case), which means that spaces and slashes are replaced with underscores and all letters are lowercase.

For example:

* A folder with the title `My Folder` will have the identifier `my_folder`.
* A folder with the title `CI/CD` will have the identifier `ci_cd`.
