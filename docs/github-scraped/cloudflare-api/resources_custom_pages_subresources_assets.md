# Assets | Cloudflare API

Source: https://developers.cloudflare.com/api/resources/custom_pages/subresources/assets

[API Reference][Custom Pages]
# Assets

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