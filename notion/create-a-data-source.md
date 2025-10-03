# Source: https://developers.notion.com/reference/create-a-data-source

Use this API to add an additional [data source](https://developers.notion.com/reference/data-source) to an existing [database](https://developers.notion.com/reference/database). The `properties` follow the [same structure](https://developers.notion.com/reference/property-object) as the initial schema passed to `initial_data_source[properties]` in the [Create a database](https://developers.notion.com/reference/database-create6ee911d9) API, but can be managed independently of the `properties` of any sibling data sources.
A standard "table" view is created alongside the new data source. To customize database views, use the Notion app. Managing views is not currently supported in the API.
parent
object
required
An object specifying the parent of the new data source to be created.
parent object
properties
object
required
Property schema of the new data source.
properties object
title
array of objects
Title of data source as it appears in Notion.
title
ADD object
icon
object
Icon to apply to the data source.
icon object
# 
200
object
object
string
id
string
created_time
string
last_edited_time
string
properties
object
+1
object
+1 object
In stock
object
In stock object
Price
object
Price object
Description
object
Description object
Last ordered
object
Last ordered object
Meals
object
Meals object
Number of meals
object
Number of meals object
Store availability
object
Store availability object
Photo
object
Photo object
Food group
object
Food group object
Name
object
Name object
parent
object
type
string
database_id
string
database_parent
object
type
string
page_id
string
archived
boolean
Defaults to true
is_inline
boolean
Defaults to true
icon
object
type
string
emoji
string
cover
object
type
string
external
object
external object
url
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
# 
404
json
* * *
Did this page help you?
Yes
No
