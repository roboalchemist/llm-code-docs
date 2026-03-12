# Source: https://developers.make.com/custom-apps-documentation/app-components/groups.md

# Source: https://developers.make.com/custom-apps-documentation/best-practices/naming-conventions/groups.md

# Groups

If an app has over 10 modules, the modules should be put into groups. These groups should be named after the entity with which the modules work or the type of job the modules are executing.

Consider the following when you decide the order of groups and modules in your app:

* Triggers
  * All instant triggers
  * All polling triggers
* Generic modules
  * Sorted in groups, if possible
  * Example of a group: RECORDS
* Typical modules divided by business logic
  * Sorted in groups (examples: TASKS, DEALS, CONTACTS)
  * Sorted from the most important to the least important
  * Ordered by RCUD logic (read, create, update, delete)
* Other
  * Examples: Make an API call, Execute a GraphQL query

<table><thead><tr><th valign="top">Example of the order of groups</th><th valign="top">Example of the order of modules in a group</th></tr></thead><tbody><tr><td valign="top"><ul><li>TRIGGERS</li><li>FORMS</li><li>TASKS</li><li>DEALS</li><li>OTHER</li></ul></td><td valign="top"><p>FORMS</p><ul><li>List forms</li><li>Get a form</li><li>Create a form</li><li>Update a form</li><li>Delete a form</li></ul></td></tr></tbody></table>

When dividing modules into groups by business logic, if every group only has one module, do not apply custom grouping. Instead, use the default groups: ACTIONS and OTHER.

<table><thead><tr><th valign="top">Correct group structure</th><th valign="top">Incorrect group structure</th></tr></thead><tbody><tr><td valign="top"><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-0007927a654ab9c8a5121b154d29a95669a781dd%2Fcorrectgrouping.png?alt=media" alt=""></td><td valign="top"><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-3db3a283f4012b33f419d3549f2bc7acb12a0948%2Fgroups_incorrect.png?alt=media" alt=""></td></tr></tbody></table>
