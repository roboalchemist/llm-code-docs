# Source: https://developers.make.com/custom-apps-documentation/best-practices/modules/bulk-actions.md

# Bulk actions

Bulk action modules can perform an action on multiple records in a single call.

To use bulk action modules, the user needs to create an array of records and map the array into the bulk module.

<figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-0c558d0799cd4de58cdd266df81d5b8ca7e4f11b%2Fbulkactions_array_bulkaddrows.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

* In the bulk module UI, the mapping should always be turned ON by default.
* Types of output:
  * If the response returns a single success / fail, the module should be an action module.
  * If the response returns an output bundle of success / fail for an individual record, the module should be a search module.
* If possible, bulk modules should output the updated range/rows.

For more information for labeling and describing bulk action modules, see the best practices guide to [module labels](https://developers.make.com/custom-apps-documentation/best-practices/naming-conventions/modules/module-labels) and [module descriptions](https://developers.make.com/custom-apps-documentation/best-practices/naming-conventions/modules/module-descriptions).
