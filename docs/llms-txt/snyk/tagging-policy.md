# Source: https://docs.snyk.io/manage-risk/policies/assets-policies/use-cases-for-policies/tagging-policy.md

# Labeling policy

## Labeling policy

Categorize and label repository assets with [asset labels](https://docs.snyk.io/manage-assets/assets-inventory-components#tags). You can use the **Set Asset Labels** action to mark the repositories to which the filter criteria you have set apply.

Snyk Essentials has a number of pre-defined system labels that can be used for filtering and setting labels with policies. User-defined custom labels can be created using policies. You can create a Set Asset Label policy action and define a custom tag by typing your tag in the tag search bar and selecting **Create new: `label_name`**. In this example the `label_name` is payment.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-b7e6b7525e9153937982096948d5501d54bd2717%2Fset%20asset%20label%20new2.png?alt=media" alt="" width="182"><figcaption><p>Assets Policy - Creating a new label</p></figcaption></figure>

The following use case demonstrates how to apply the custom-defined `backend` label to assets that match certain naming conventions. This allows a quick filter for backend assets from the Inventory view.

This is how the policy should look after you finish setting up all filters and actions.

<figure><img src="https://2533899886-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MdwVZ6HOZriajCf5nXH%2Fuploads%2Fgit-blob-e2d279f18c698067029bfec87a512b24c296111a%2Fset%20asset%20label%20new.png?alt=media" alt=""><figcaption><p>Assets Policy - Labeling backend repositories</p></figcaption></figure>
