# Custom Pages | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/custom_pages

[API Reference]
# Custom Pages

##### [List custom pages]
GET/{accounts_or_zones}/{account_or_zone_id}/custom_pages
##### [Get a custom page]
GET/{accounts_or_zones}/{account_or_zone_id}/custom_pages/{identifier}
##### [Update a custom page]
PUT/{accounts_or_zones}/{account_or_zone_id}/custom_pages/{identifier}
##### ModelsExpand Collapse
CustomPageListResponse  { id, created_on, description, 5 more } id: optional string[]created_on: optional stringformatdate-time[]description: optional string[]modified_on: optional stringformatdate-time[]preview_target: optional string[]required_tokens: optional array of string[]state: optional "default" or "customized"
The custom page state.
One of the following:"default"[]"customized"[][]url: optional string
The URL associated with the custom page.
formaturi[][]CustomPageGetResponse  { id, created_on, description, 5 more } id: optional string[]created_on: optional stringformatdate-time[]description: optional string[]modified_on: optional stringformatdate-time[]preview_target: optional string[]required_tokens: optional array of string[]state: optional "default" or "customized"
The custom page state.
One of the following:"default"[]"customized"[][]url: optional string
The URL associated with the custom page.
formaturi[][]CustomPageUpdateResponse  { id, created_on, description, 5 more } id: optional string[]created_on: optional stringformatdate-time[]description: optional string[]modified_on: optional stringformatdate-time[]preview_target: optional string[]required_tokens: optional array of string[]state: optional "default" or "customized"
The custom page state.
One of the following:"default"[]"customized"[][]url: optional string
The URL associated with the custom page.
formaturi[][]
#### Custom PagesAssets

##### [List custom assets]
GET/{accounts_or_zones}/{account_or_zone_id}/custom_pages/assets
##### [Get a custom asset]
GET/{accounts_or_zones}/{account_or_zone_id}/custom_pages/assets/{asset_name}
##### [Create a custom asset]
POST/{accounts_or_zones}/{account_or_zone_id}/custom_pages/assets
##### [Update a custom asset]
PUT/{accounts_or_zones}/{account_or_zone_id}/custom_pages/assets/{asset_name}
##### [Delete a custom asset]
DELETE/{accounts_or_zones}/{account_or_zone_id}/custom_pages/assets/{asset_name}
##### ModelsExpand Collapse
AssetListResponse  { description, last_updated, name, 2 more } description: optional string
A short description of the custom asset.
[]last_updated: optional stringformatdate-time[]name: optional string
The unique name of the custom asset. Can only contain letters (A-Z, a-z), numbers (0-9), and underscores (_).
minLength1[]size_bytes: optional number
The size of the asset content in bytes.
[]url: optional string
The URL where the asset content is fetched from.
formaturi[][]AssetGetResponse  { description, last_updated, name, 2 more } description: optional string
A short description of the custom asset.
[]last_updated: optional stringformatdate-time[]name: optional string
The unique name of the custom asset. Can only contain letters (A-Z, a-z), numbers (0-9), and underscores (_).
minLength1[]size_bytes: optional number
The size of the asset content in bytes.
[]url: optional string
The URL where the asset content is fetched from.
formaturi[][]AssetCreateResponse  { description, last_updated, name, 2 more } description: optional string
A short description of the custom asset.
[]last_updated: optional stringformatdate-time[]name: optional string
The unique name of the custom asset. Can only contain letters (A-Z, a-z), numbers (0-9), and underscores (_).
minLength1[]size_bytes: optional number
The size of the asset content in bytes.
[]url: optional string
The URL where the asset content is fetched from.
formaturi[][]AssetUpdateResponse  { description, last_updated, name, 2 more } description: optional string
A short description of the custom asset.
[]last_updated: optional stringformatdate-time[]name: optional string
The unique name of the custom asset. Can only contain letters (A-Z, a-z), numbers (0-9), and underscores (_).
minLength1[]size_bytes: optional number
The size of the asset content in bytes.
[]url: optional string
The URL where the asset content is fetched from.
formaturi[][]