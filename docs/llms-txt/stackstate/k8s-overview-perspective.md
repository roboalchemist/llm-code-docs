# Source: https://archivedocs.stackstate.com/views/k8s-view-structure/k8s-overview-perspective.md

# Overview perspective

The Overview Perspective shows a list of all the components in your view. Depending on the type of view and the components in the view, the structure of the overview perspective will be different.

For example, the table structure used on the [kubernetes views](https://archivedocs.stackstate.com/views/k8s-views) will reflect the most important properties of the component types included in each view: as seen below, the `services` view has a different table structure than the `pods` view.

![Overview table structure comparison](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-c1f29fff9642112ea0d2afc2e9c53c61b456b3e3%2Fk8s-overview-perspective-table-comparison.png?alt=media)

For [custom views](https://archivedocs.stackstate.com/views/k8s-custom-views) and [explore views](https://archivedocs.stackstate.com/views/k8s-explore-views), the overview perspective table will have a generic one-size-fits-all structure, composed out of the most common properties, because of the diversity of component types that might be included in the view.

![Overview table generic structure](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-075c595d8545819fa677ba478a5450840f3ac652%2Fk8s-overview-perspective-generic-table.png?alt=media)

Although a table layout will be used in most of the view types for the overview perspective, in some cases a cards layout will also be provided, allowing you to change between different modes of displaying the contents of the overview perspective.

![Overview cards layout](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-6fddd5b0f2d8d4dc45641c2360bf605f3cc4c6f6%2Fk8s-overview-perspective-cards-layout.png?alt=media)
