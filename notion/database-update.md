# Source: https://developers.notion.com/reference/database-update

Updates the attributes — the title, description, icon, or cover, etc. — of a specified database. 
Returns the updated [database object](https://developers.notion.com/reference/database).
To update the `properties` of the [data sources](https://developers.notion.com/reference/data-source) under a database, use the [Update a data source](https://developers.notion.com/reference/update-a-data-source) API starting from API version `2025-09-03`.
For an overview of how to use the REST API with databases, refer to the [Working with databases](https://developers.notion.com/docs/working-with-databases) guide.
Each Public API endpoint can return several possible error codes. See the [Error codes section](https://developers.notion.com/reference/status-codes#error-codes) of the Status codes documentation for more information.
database_id
string
required
ID of a Notion database, a container for one or more data sources. This is a UUIDv4, with or without dashes.
parent
object
The parent page or workspace to move the database to. If not provided, the database will not be moved.
parent object
title
array of objects
The updated title of the database, if any. If not provided, the title will not be updated.
title
ADD object
is_inline
boolean
Whether the database should be displayed inline in the parent page. If not provided, the inline status will not be updated.
true false
icon
object
The updated icon for the database, if any. If not provided, the icon will not be updated.
icon object
cover
object
The updated cover image for the database, if any. If not provided, the cover will not be updated.
cover object
in_trash
boolean
Whether the database should be moved to or from the trash. If not provided, the trash status will not be updated.
true false
is_locked
boolean
Whether the database should be locked from editing in the Notion app UI. If not provided, the locked state will not be updated.
true false
Notion-Version
string
required
The [API version](https://developers.notion.com/reference/versioning) to use for this request. The latest version is `2025-09-03`.
# 
200
object
object
string
id
string
title
array of objects
title
object
type
string
text
object
text object
annotations
object
annotations object
plain_text
string
href
string
parent
object
type
string
page_id
string
is_inline
boolean
Defaults to true
in_trash
boolean
Defaults to true
is_locked
boolean
Defaults to true
created_time
string
last_edited_time
string
data_sources
array of objects
data_sources
object
id
string
name
string
icon
string
cover
string
developer_survey
string
request_id
string
# 
400
object
* * *
Did this page help you?
Yes
No
