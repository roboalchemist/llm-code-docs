# Source: https://developers.make.com/custom-apps-documentation/best-practices/naming-conventions/modules/module-labels.md

# Module labels

Every module should have a label that precisely describes the module's use. The label should be composed of the verb expressing the intended action (create, update, watch, etc.) and the name of the entity being processed (customer, invoice, table, etc.).

Module labels follow [sentence case](https://apastyle.apa.org/style-grammar-guidelines/capitalization/sentence-case). Only the first word is capitalized.

There may be times when the third-party UI does not match these suggested naming conventions. In such cases, use the third-party terminology that is familiar to your users.

## Watch modules <a href="#watch-modules" id="watch-modules"></a>

Watch modules watch for new data in a service and return it. They are trigger and instant trigger (webhook) modules.

<table><thead><tr><th valign="top">Format (plural)</th><th valign="top">Correct</th><th valign="top">Incorrect</th></tr></thead><tbody><tr><td valign="top">Watch [item]s</td><td valign="top">Watch contacts</td><td valign="top">Watch a contact</td></tr><tr><td valign="top">Watch new [item]s</td><td valign="top">Watch new contacts</td><td valign="top">Watch contacts created</td></tr><tr><td valign="top">Watch updated [item]s</td><td valign="top">Watch updated contacts</td><td valign="top">Watch contacts updated</td></tr><tr><td valign="top">Watch deleted [item]s</td><td valign="top">Watch deleted contacts</td><td valign="top">Watch contacts deleted</td></tr></tbody></table>

## Action modules <a href="#action-modules" id="action-modules"></a>

Action modules write data into a service, modify data in a service, or retrieve a single result.

<table><thead><tr><th valign="top">Module type</th><th valign="top">Format (singular)</th><th valign="top">Correct</th><th valign="top">Incorrect</th></tr></thead><tbody><tr><td valign="top">Add</td><td valign="top">Add a/an [item]</td><td valign="top"><p>Add a reaction</p><p>Add a user to a list</p></td><td valign="top"></td></tr><tr><td valign="top">Create</td><td valign="top">Create a/an [item]</td><td valign="top"><p>Create a message</p><p>Create a completion</p></td><td valign="top"></td></tr><tr><td valign="top">Create or Update</td><td valign="top">Create or update a/an [item]</td><td valign="top"><p>Create or update a record</p><p>Create or update a vector</p></td><td valign="top">Upsert a record</td></tr><tr><td valign="top">Delete</td><td valign="top">Delete a/an [item]</td><td valign="top"><p>Delete a message</p><p>Delete a user from a list</p></td><td valign="top"></td></tr><tr><td valign="top">Download</td><td valign="top">Download a/an [item]</td><td valign="top"><p>Download a message</p><p>Download an image</p></td><td valign="top"></td></tr><tr><td valign="top">Generate</td><td valign="top">Generate a/an [item]</td><td valign="top"><p>Generate an image</p><p>Generate an audio file</p></td><td valign="top"></td></tr><tr><td valign="top">Get</td><td valign="top">Get a/an [item]</td><td valign="top"><p>Get a message</p><p>Get a user</p></td><td valign="top"></td></tr><tr><td valign="top">Invite</td><td valign="top">Invite a/an [item]</td><td valign="top"><p>Invite a user</p><p>Invite a user to a channel</p></td><td valign="top"></td></tr><tr><td valign="top">Remove</td><td valign="top">Remove a/an [item]</td><td valign="top"><p>Remove a reaction</p><p>Remove a user from a list</p></td><td valign="top"></td></tr><tr><td valign="top">Send</td><td valign="top">Send a/an [item]</td><td valign="top"><p>Send a message</p><p>Send an email to a team member</p></td><td valign="top"></td></tr><tr><td valign="top">Update</td><td valign="top">Update a/an [item]</td><td valign="top"><p>Update a message</p><p>Update a product variant</p></td><td valign="top"></td></tr><tr><td valign="top">Upload</td><td valign="top">Upload a/an [item]</td><td valign="top"><p>Upload an image</p><p>Upload a product image</p></td><td valign="top"></td></tr></tbody></table>

## Search modules <a href="#search-modules" id="search-modules"></a>

Search modules retrieve data from a service and allow for one or more results.

<table><thead><tr><th valign="top">Module type</th><th valign="top">Format (plural)</th><th valign="top">Correct</th><th valign="top">Note</th></tr></thead><tbody><tr><td valign="top">List</td><td valign="top">List [item]s</td><td valign="top"><p>List users</p><p>List entity types</p></td><td valign="top">List modules are those that have no filtering options.</td></tr><tr><td valign="top">Search</td><td valign="top">Search [item]s</td><td valign="top"><p>Search users</p><p>Search contacts</p></td><td valign="top">Search modules are those that have one or more filtering options.</td></tr></tbody></table>

## Bulk modules <a href="#bulk-modules" id="bulk-modules"></a>

Bulk modules can perform an action on multiple records in a single call.

<table><thead><tr><th valign="top">Format (plural)</th><th valign="top">Correct</th></tr></thead><tbody><tr><td valign="top">Bulk [action] [parameter] (advanced)</td><td valign="top">Bulk upload call conversions (advanced)<br>Bulk create folders (advanced)</td></tr></tbody></table>

## Additional information <a href="#additional-information" id="additional-information"></a>

Some modules will require additional information in the name, such as (advanced) for bulk modules, or (beta). In these cases, the singular adjective should be lowercase and placed between ( ).

<table><thead><tr><th valign="top">Information type</th><th valign="top">Format</th><th valign="top">Correct</th><th valign="top">Incorrect</th></tr></thead><tbody><tr><td valign="top">Advanced</td><td valign="top">Module name (advanced)</td><td valign="top">Search rows (advanced)</td><td valign="top">Search rows (Advanced module)</td></tr><tr><td valign="top">Beta</td><td valign="top">Module name (beta)</td><td valign="top">List folder items (beta)</td><td valign="top">List folder items (BETA)</td></tr><tr><td valign="top">Advanced, beta (both tags)</td><td valign="top">Module name (advanced) (beta)</td><td valign="top">Update a campaign (advanced) (beta)</td><td valign="top">Update a campaign (advanced, beta)</td></tr><tr><td valign="top">Deprecated</td><td valign="top">Module name (deprecated)</td><td valign="top">Send a message (deprecated)</td><td valign="top">Send a message (Deprecated)</td></tr><tr><td valign="top">Rebrand</td><td valign="top">Module name (formerlyl [name])</td><td valign="top">X (formerly Twitter)</td><td valign="top">X (Formerly Twitter)</td></tr></tbody></table>
