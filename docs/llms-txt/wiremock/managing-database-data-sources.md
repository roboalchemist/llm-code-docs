# Source: https://docs.wiremock.io/data-sources/managing-database-data-sources.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.wiremock.io/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating & Editing Database Data Sources

> Setting up your external test data from a database

<Tip>
  The database data source feature is currently in **private beta**.  If you would like access to this feature contact us
  via the `Get Support` link in the menu bar
</Tip>

## Creating a database data source

Data sources can be created at the organisation level, meaning that the Data sources you create can be shared among the
members of your organisation.

To create a database data source, you first need to create a [database connection](./managing-database-connections)

To create a data source:

* Navigate to the Data Sources page.

  <img alt="Data source menu item" src="https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/data-source-navigate.png?fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=1b64f35035513087e69a7daa9820af54" data-og-width="616" width="616" data-og-height="328" height="328" data-path="images/screenshots/data-sources/data-source-navigate.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/data-source-navigate.png?w=280&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=9b0f9ddaa52e13307f0059117302edec 280w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/data-source-navigate.png?w=560&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=108c6613e18feeb6de1785fdaea87fd1 560w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/data-source-navigate.png?w=840&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=9e3f30d1d61c676725d2edee51e0b779 840w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/data-source-navigate.png?w=1100&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=310c750ae203f8f28936d2db011a4ccb 1100w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/data-source-navigate.png?w=1650&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=b113fb546ad1914e78323a52b3961308 1650w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/data-source-navigate.png?w=2500&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=1aeae217392a2c6baf855ebd1283f89c 2500w" />

* Click on the button, `+Create new data source`.

  <img alt="Create Data source button" src="https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/data-source-create-button.png?fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=ad3a8c540fa41d185dd2b18592889d19" data-og-width="557" width="557" data-og-height="312" height="312" data-path="images/screenshots/data-sources/data-source-create-button.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/data-source-create-button.png?w=280&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=e5267a865e1c9836a7d416391bdf5c86 280w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/data-source-create-button.png?w=560&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=5aca6707ea38ab0877b6415ba15142cb 560w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/data-source-create-button.png?w=840&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=a5602080e043f15b6d6480e344c10b3e 840w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/data-source-create-button.png?w=1100&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=f21af18b7b1fa06803d9217fd24c70d4 1100w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/data-source-create-button.png?w=1650&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=f1bbf908fa66c6c0143233f5587e9689 1650w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/data-source-create-button.png?w=2500&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=7b6ff96862fd27ea589b4e1d968245e0 2500w" />

* Choose `Database based` from the dropdown

  <img alt="Create database data source" src="https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/data-source-database-create.png?fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=d77979ebb95efd91249ac47b75434501" data-og-width="842" width="842" data-og-height="690" height="690" data-path="images/screenshots/data-sources/data-source-database-create.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/data-source-database-create.png?w=280&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=548a9d1f88018491008912a2959a9e0e 280w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/data-source-database-create.png?w=560&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=ea015aa36ef1ab43e93812ae59b00f33 560w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/data-source-database-create.png?w=840&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=661a7e82812f27f4bdc036774bb5163b 840w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/data-source-database-create.png?w=1100&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=97a7be9f3e0f3ad9deabd4dcf44dedc1 1100w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/data-source-database-create.png?w=1650&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=760d8abbf5df7674710e19647d387135 1650w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/data-source-database-create.png?w=2500&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=d75867b6332ad68dc8887fdc3f8ece96 2500w" />

* Provide a name for your data source.

* Select the database connection you wish to use with this data source

* Enter the name of the table you wish to use with this data source. This can be the name of a table, or a view within
  your database.

* Click `save` at the bottom of the page.

Once the data source has been saved you can view a preview (the first 10 rows) of the data returned from the specified
table by navigating to the data sources page and clicking on the data source you wish to preview.

If the specified table could not be found, an error will be displayed.

<img alt="Edit database data source" src="https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/data-source-database-preview-error.png?fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=da908ee894f4943e40e84319a058801c" data-og-width="705" width="705" data-og-height="528" height="528" data-path="images/screenshots/data-sources/data-source-database-preview-error.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/data-source-database-preview-error.png?w=280&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=3ed0c097bef29d69fe601f68f12f98ed 280w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/data-source-database-preview-error.png?w=560&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=5400b1eca26ce38ddfd58bdbccf1cacf 560w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/data-source-database-preview-error.png?w=840&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=b6da1b1314421fe97433507c8083d887 840w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/data-source-database-preview-error.png?w=1100&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=7be57d72b426ac8de3dcbf62823695ad 1100w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/data-source-database-preview-error.png?w=1650&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=8b5c1485ab31591b6f3e08cc6a73f804 1650w, https://mintcdn.com/wiremockinc/TMB5bBMjkV05sCok/images/screenshots/data-sources/data-source-database-preview-error.png?w=2500&fit=max&auto=format&n=TMB5bBMjkV05sCok&q=85&s=dca70f056cc53015b6bb4ee3873ccf5e 2500w" />

## Editing a database data source

Data sources can be updated after creation.

To edit a data source:

* Navigate to the Data Sources page.
* Click on the data source you wish to edit, from the list provided.
* Update your data source.
* Click on the `save` at the bottom of the page.

Once in the data source page, you will be able to:

* Change the name of the data source
* Change the database connection used by the data source
* Change the table name referenced by the data source
