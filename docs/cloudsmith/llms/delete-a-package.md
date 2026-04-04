# Source: https://help.cloudsmith.io/docs/delete-a-package.md

# Package Delete

We provide two ways to remove your packages/files/assets from your repositories:

* Delete via the API using tools/integrations (such as the Cloudsmith CLI),
* Delete directly via the Website UI.

***

## Delete via Cloudsmith CLI

### Identify a Package

To delete a package using the Cloudsmith CLI, you first need to identify the package you wish to delete.  See [Package Identification](https://help.cloudsmith.io/docs/identifying-a-package) for instructions to do this.

### Delete a Package

Once you have identified the package, you use the `cloudsmith delete` command to delete it:

```shell
cloudsmith delete OWNER/REPO/UNIQUE_ID
```

For example:

```shell
cloudsmith delete demo/examples-repo/G0rDBWcVBMEm
```

In this example, we identified that the package we want to delete has the Unique ID "G0rDBWcVBMEm" and we are deleting it from the "my-example-repo" repository:

<Image title="Screenshot 2020-01-01 at 13.02.51.png" alt={906} align="center" src="https://files.readme.io/e1da36d-Screenshot_2020-01-01_at_13.02.51.png">
  cloudsmith delete CLI example
</Image>

***

## Delete via Website UI

You can delete a package via the Website UI:

* Via the repository packages list
* Via the package detail page

### Delete via Repository Packages List

To delete a package via the repository packages list, click the dots to the right of the package name, then click "Delete":

<Image title="delete-package-button.png" alt={1307} align="center" width="smart" src="https://files.readme.io/be49c4d7e893dc1b25fd782231f15ba60592560219f9cc28514a899e2f491f1c-delete-package-packages-list.png">
  Delete package button on repository packages list
</Image>

### Delete via the Package Detail page

To delete a package via the package detail page, click the "Delete" button to the right of the package name:

<Image title="delete-package-page-button.png" alt={1322} align="center" width="smart" src="https://files.readme.io/d6974a35e0c4fe829cbeb8abfb4488fa35515b9e4e1a2a3f256402634b5496b6-delete-packages-packages-detail.png">
  Delete package button on package detail page
</Image>

After clicking a "Delete" button, you will then be presented with a confirmation form. Click "Delete" again to confirm deletion of the package:

<Image title="delete-package-form.png" alt={595} align="center" width="80%" border={true} src="https://files.readme.io/d921030cd95b8c1260d26b9fa23d7ca5cbd89d325d1b36a3cdaa2c66f9f25033-delete-package-confirmation.png">
  Delete package form
</Image>

You will then get an on-screen message confirming that the package has been deleted.