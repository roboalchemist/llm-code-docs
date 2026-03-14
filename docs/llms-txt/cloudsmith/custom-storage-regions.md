# Source: https://help.cloudsmith.io/docs/custom-storage-regions.md

# Custom Storage Regions

Custom storage regions allow you to control where in the world your artifacts are geographically stored. For regulatory and compliance reasons you may wish to store your artifacts in a specific country or region. In addition, storing your artifacts closer to where your services and teams operate can also provide significant performance benefits (lower latency) in many cases.

You can choose a storage region when creating a new repository or you can transfer an existing repository to a different storage region.

***

## Choosing a Custom Storage Region for a new Repository

During the creation of a new package repository, you have the option to specify a custom storage region (other than the default region of Dublin, Ireland) for your new repository via the "Create Package Repository" form.

The currently supported storage regions are:

* Dublin, Ireland
* Frankfurt, Germany
* Montreal, Canada
* Northern California, United States
* Ohio, United States
* Oregon, United States
* Singapore
* Sydney, Australia

Selecting a storage region enables you to use one of our supported locations to store your packages at an edge location that is geographically closer to your region of operations. With some consideration regarding your intended usage, selecting your nearest storage region can significantly reduce latency.

<Image title="storage_region.png" alt={765} align="center" width="smart" src="https://files.readme.io/d0954bd-storage_region.png">
  Create Package Repository Form
</Image>

Use the "Storage Region" drop-down menu to select your custom storage region, and then click the green "Create" button to create a new repository in your chosen region.

***

## Transferring an existing Repository to a new storage region

To transfer an existing repository to a new storage region, click the repository "Settings" button on the left-hand menu, scroll to the bottom and click the orange "Transfer" button. By default, your storage region will be based in Dublin, Ireland if this is the first time you are specifying a storage region.

<Image title="Transfer_Repo_Button.png" alt={1183} align="center" width="smart" src="https://files.readme.io/4583ac7-Transfer_Repo_Button.png">
  Transfer Repository Button
</Image>

You will then be presented with the Transfer Repository Form:

<Image title="transfer-repo-form.png" alt={593} align="center" width="smart" border={true} src="https://files.readme.io/abd679b-transfer-repo-form.png">
  Transfer Repository Form
</Image>

In order to prevent accidental transfers, you need to confirm the identifier / slug for the repository by typing it into the "Confirm Current Repository Slug/Identifier" field.\
Then choose your new storage region from the drop-down menu, complete the Captcha and click the orange "Transfer" button to start the transfer.

> 🚧
>
> Whilst the transfer is processing, synchronisation for any new uploads will be paused and will not complete until the transfer is complete. However, downloads will continue to work as normal throughout the transfer process. The time taken to transfer to a new region is directly related to the number of packages stored within a repository.