# patch-v1liveviewsid

Source: https://developer.ui.com/protect/v6.2.83/patch-v1liveviewsid

---

UniFi API

Endpoints combined into Ansible Modules for customized workflows.

# Patch live view configuration

PATCH`/v1/liveviews/{id}`

Patch the configuration about a specific live view

path Parameters

id

required

string

The primary key of liveview

request Body

id

required

string

The primary key of liveview

modelKey

required

string

The model key of the liveview

name

required

string

The name of this live view.

isDefault

required

boolean

Whether this live view is the default one for all viewers.

isGlobal

required

boolean

Whether this live view is global and available system-wide to all users

owner

required

string

The primary key of user

layout

required

number

The number of slots this live view contains. Which as a consequence also affects the layout of the live view.

slotsExpand

required

Array of object

List of cameras visible in each given slot. And cycling settings for each slot if it has multiple cameras listed.

## Responses

200

Response Schema: application/json

id

required

string

The primary key of liveview

modelKey

required

string

The model key of the liveview

name

required

string

The name of this live view.

isDefault

required

boolean

Whether this live view is the default one for all viewers.

isGlobal

required

boolean

Whether this live view is global and available system-wide to all users

owner

required

string

The primary key of user

layout

required

number

The number of slots this live view contains. Which as a consequence also affects the layout of the live view.

slotsExpand

required

Array of object

List of cameras visible in each given slot. And cycling settings for each slot if it has multiple cameras listed.