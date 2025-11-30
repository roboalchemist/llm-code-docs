# Source: https://developer.1password.com/docs/connect/api-reference

On this page

# 1Password Connect Server API reference

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiIgLz48L3N2Zz4=)]info

If you\'re new to 1Password Secrets Automation and 1Password Connect Server, [learn how to get started with a Secrets Automation workflow](/docs/connect/get-started/).

You can use the Connect API to work with the vaults and items in your account, and to list API activity on a Connect server:

- [List vaults](#list-vaults)
- [Get vault details](#get-vault-details)
- [List items](#list-items)
- [Add an item](#add-an-item)
- [Get item details](#get-item-details)
- [Replace an item](#replace-an-item)
- [Delete an item](#delete-an-item)
- [Update a subset of item attributes](#update-a-subset-of-item-attributes)
- [List files](#list-files)
- [Get file details](#get-file-details)
- [Get file content](#get-file-content)
- [List API activity](#list-api-activity)

To view the API in another tool, download the [1Password Connect API specification file (1.8.1)](https://i.1password.com/media/1password-connect/1password-connect-api_1.8.1.yaml).

## Requirements[â€‹](#requirements "Direct link to Requirements") 

Before you can use the 1Password Connect Server API, you\'ll need to:

- [Sign up for 1Password.](https://1password.com/pricing/password-manager)
- [Set up a Secrets Automation workflow.](/docs/connect/get-started#step-1).
- [Deploy 1Password Connect](/docs/connect/get-started#step-2-deploy-a-1password-connect-server) in your infrastructure.

## Request headers[â€‹](#request-headers "Direct link to Request headers") 

Each request to the API has to be authenticated with an [access token](/docs/connect/manage-connect#manage-access-tokens). Provide it and specify the content type:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

## List vaults[â€‹](#list-vaults "Direct link to List vaults") 

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

### Path parameters[â€‹](#path-parameters "Direct link to Path parameters") 

No path parameters

### Query parameters[â€‹](#query-parameters "Direct link to Query parameters") 

+-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter             | Type                  | Description                                                                                                                                                                |
+=======================+=======================+============================================================================================================================================================================+
| `filter`              | string                | Filter the vault collection using [SCIM-style filters](https://bookstack.soffid.com/books/scim/page/scim-query-syntax). Vaults can only be filtered by `name`. *Optional.* |
|                       |                       |                                                                                                                                                                            |
|                       |                       | \                                                                                                                                                                          |
|                       |                       | [For example: `name eq "Demo Vault"`]                                                                                                                              |
+-----------------------+-----------------------+----------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

### Responses[â€‹](#responses "Direct link to Responses") 

200
:   Returns an array of vault names and IDs

401
:   Invalid or missing token

## Get vault details[â€‹](#get-vault-details "Direct link to Get vault details") 

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

### Path parameters[â€‹](#get-vaults-vaultuuid-path-parameters "Direct link to Path parameters") 

  Parameter     Type     Description
  ------------- -------- -----------------------------------------------
  `vaultUUID`   string   The UUID of the vault to retrieve items from.

### Query parameters[â€‹](#get-vaults-vaultuuid-query-parameters "Direct link to Query parameters") 

No query parameters.

### Responses[â€‹](#get-vaults-vaultuuid-responses "Direct link to Responses") 

200
:   Returns a [Vault object](#vault-object)

401
:   Invalid or missing token

403
:   Unauthorized access

404
:   Vault not found

## List items[â€‹](#list-items "Direct link to List items") 

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

### Path parameters[â€‹](#get-vaults-vaultuuid-items-path-parameters "Direct link to Path parameters") 

  Parameter     Type     Description
  ------------- -------- ----------------------------------------------
  `vaultUUID`   string   The UUID of the vault to get the details of.

### Query parameters[â€‹](#get-vaults-vaultuuid-items-query-parameters "Direct link to Query parameters") 

+-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter             | Type                  | Description                                                                                                                                                                         |
+=======================+=======================+=====================================================================================================================================================================================+
| `filter`              | string                | Filter the item collection using [SCIM-style filters](https://bookstack.soffid.com/books/scim/page/scim-query-syntax) . Items can only be filtered by `title` or `tag`. *Optional.* |
|                       |                       |                                                                                                                                                                                     |
|                       |                       | \                                                                                                                                                                                   |
|                       |                       | [For example: `title eq "Example Item"` or `tag eq "banking"`]                                                                                                              |
+-----------------------+-----------------------+-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

### Responses[â€‹](#responses-1 "Direct link to Responses") 

200
:   Returns an array of [Item objects](#item-object) that don\'t include sections and fields

401
:   Invalid or missing token

404
:   Vault not found

## Add an item[â€‹](#add-an-item "Direct link to Add an item") 

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

The request must include a FullItem object, containing the information to create the item. For example:

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

+-----------------------+-----------------------+-----------------------------------------------------------------------------------------------+
| Parameter             | Type                  | Description                                                                                   |
+=======================+=======================+===============================================================================================+
| `title`               | string                | The title of the item.                                                                        |
+-----------------------+-----------------------+-----------------------------------------------------------------------------------------------+
| `vault`               | object                | An object containing an `id` property whose value is the UUID of the vault the item is in.    |
+-----------------------+-----------------------+-----------------------------------------------------------------------------------------------+
| `category`            | string                | The category of the item. One of:                                                             |
|                       |                       |                                                                                               |
|                       |                       | ::: section                                                                                   |
|                       |                       | - `"LOGIN"`                                                                                   |
|                       |                       | - `"PASSWORD"`                                                                                |
|                       |                       | - `"API_CREDENTIAL"`                                                                          |
|                       |                       | - `"SERVER"`                                                                                  |
|                       |                       | - `"DATABASE"`                                                                                |
|                       |                       | - `"CREDIT_CARD"`                                                                             |
|                       |                       | - `"MEMBERSHIP"`                                                                              |
|                       |                       | - `"PASSPORT"`                                                                                |
|                       |                       | - `"SOFTWARE_LICENSE"`                                                                        |
|                       |                       | - `"OUTDOOR_LICENSE"`                                                                         |
|                       |                       | - `"SECURE_NOTE"`                                                                             |
|                       |                       | - `"WIRELESS_ROUTER"`                                                                         |
|                       |                       | - `"BANK_ACCOUNT"`                                                                            |
|                       |                       | - `"DRIVER_LICENSE"`                                                                          |
|                       |                       | - `"IDENTITY"`                                                                                |
|                       |                       | - `"REWARD_PROGRAM"`                                                                          |
|                       |                       | - `"EMAIL_ACCOUNT"`                                                                           |
|                       |                       | - `"SOCIAL_SECURITY_NUMBER"`                                                                  |
|                       |                       | - `"MEDICAL_RECORD"`                                                                          |
|                       |                       | - `"SSH_KEY"`                                                                                 |
|                       |                       | :::                                                                                           |
|                       |                       |                                                                                               |
|                       |                       | You can\'t create items using the \"CUSTOM\" or \"DOCUMENT\" categories.                      |
+-----------------------+-----------------------+-----------------------------------------------------------------------------------------------+
| `urls`                | array                 | Array of [URL objects](#item-url-object) containing URLs for the item.                        |
+-----------------------+-----------------------+-----------------------------------------------------------------------------------------------+
| `favorite`            | boolean               | Mark the item as a favorite.                                                                  |
+-----------------------+-----------------------+-----------------------------------------------------------------------------------------------+
| `tags`                | string                | An array of strings of the tags assigned to the item.                                         |
+-----------------------+-----------------------+-----------------------------------------------------------------------------------------------+
| `fields`              | array                 | An array of [Field objects](#item-field-object) of the fields to include with the item.       |
+-----------------------+-----------------------+-----------------------------------------------------------------------------------------------+
| `sections`            | array                 | An array of [Section objects](#item-section-object) of the sections to include with the item. |
+-----------------------+-----------------------+-----------------------------------------------------------------------------------------------+

### Path parameters[â€‹](#post-vaults-vaultuuid-items-path-parameters "Direct link to Path parameters") 

  Parameter     Type     Description
  ------------- -------- ---------------------------------------------
  `vaultUUID`   string   The UUID of the vault to create an item in.

### Query parameters[â€‹](#post-vaults-vaultuuid-items-query-parameters "Direct link to Query parameters") 

No query parameters.

### Responses[â€‹](#responses-2 "Direct link to Responses") 

200
:   Returns [Item object](#item-object) containing the new item

400
:   Unable to create item due to invalid input

401
:   Invalid or missing token

403
:   Unauthorized access

404
:   Item not found

## Get item details[â€‹](#get-item-details "Direct link to Get item details") 

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

### Path parameters[â€‹](#get-vaults-vaultuuid-items-itemuuid-path-parameters "Direct link to Path parameters") 

  Parameter     Type     Description
  ------------- -------- --------------------------------------------------
  `vaultUUID`   string   The UUID of the vault to retrieve the item from.
  `itemUUID`    string   The UUID of the item to retrieve.

### Query parameters[â€‹](#get-vaults-vaultuuid-items-itemuuid-query-parameters "Direct link to Query parameters") 

No query parameters.

### Responses[â€‹](#get-vaults-vaultuuid-items-itemuuid-responses "Direct link to Responses") 

200
:   Returns an [Item object](#item-object)

401
:   Invalid or missing token

403
:   Unauthorized access

404
:   Item not found

## Replace an item[â€‹](#replace-an-item "Direct link to Replace an item") 

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

### Path parameters[â€‹](#put-vaults-vaultuuid-items-itemuuid-path-parameters "Direct link to Path parameters") 

  Parameter     Type     Description
  ------------- -------- --------------------------------------------------
  `vaultUUID`   string   The UUID of the vault to retrieve the item from.
  `itemUUID`    string   The UUID of the item to replace.

### Query parameters[â€‹](#put-vaults-vaultuuid-items-itemuuid-query-parameters "Direct link to Query parameters") 

No query parameters.

### Responses[â€‹](#put-vaults-vaultuuid-items-itemuuid-responses "Direct link to Responses") 

200
:   Returns an [Item object](#item-object)

400
:   Unable to create item due to invalid input

401
:   Invalid or missing token

403
:   Unauthorized access

404
:   Item not found

## Delete an item[â€‹](#delete-an-item "Direct link to Delete an item") 

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

### Path parameters[â€‹](#delete-vaults-vaultuuid-items-itemuuid-path-parameters "Direct link to Path parameters") 

  Parameter     Type     Description
  ------------- -------- --------------------------------------------------
  `vaultUUID`   string   The UUID of the vault to retrieve the item from.
  `itemUUID`    string   The UUID of the item to delete.

### Query parameters[â€‹](#delete-vaults-vaultuuid-items-itemuuid-query-parameters "Direct link to Query parameters") 

No query parameters.

### Responses[â€‹](#delete-vaults-vaultuuid-items-itemuuid-responses "Direct link to Responses") 

204
:   Successfully deleted an item

401
:   Invalid or missing token

403
:   Unauthorized access

404
:   Item not found

## Update a subset of item attributes[â€‹](#update-a-subset-of-item-attributes "Direct link to Update a subset of item attributes") 

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

Applies an `add`, `remove`, or `replace` operation on an item or the fields of an item. Uses the [RFC6902 JSON Patch](https://tools.ietf.org/html/rfc6902) document standard.

+-----------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter             | Type                  | Description                                                                                                                                                  |
+=======================+=======================+==============================================================================================================================================================+
| `op`                  | string                | The kind of operation to perform. One of:                                                                                                                    |
|                       |                       |                                                                                                                                                              |
|                       |                       | - `add`                                                                                                                                                      |
|                       |                       | - `remove`                                                                                                                                                   |
|                       |                       | - `replace`                                                                                                                                                  |
+-----------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `path`                | string                | An RFC6901 JSON Pointer to the item, an item attribute, an item field by field ID, or an item field attribute. For example: `"/fields/vy09gd8EXAMPLE/label"` |
+-----------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `value`               | any                   | The new value to apply at the path.                                                                                                                          |
+-----------------------+-----------------------+--------------------------------------------------------------------------------------------------------------------------------------------------------------+

### Path parameters[â€‹](#patch-vaults-vaultuuid-items-itemuuid-path-parameters "Direct link to Path parameters") 

  Parameter     Type     Description
  ------------- -------- ---------------------------------------
  `vaultUUID`   string   The UUID of the vault the item is in.
  `itemUUID`    string   The UUID of the item to update.

### Query parameters[â€‹](#patch-vaults-vaultuuid-items-itemuuid-query-parameters "Direct link to Query parameters") 

No query parameters.

### Responses[â€‹](#patch-vaults-vaultuuid-items-itemuuid-responses "Direct link to Responses") 

200
:   Returns an [Item object](#item-object) of the updated item.

401
:   Invalid or missing token

403
:   Unauthorized access

404
:   Item not found

## List files[â€‹](#list-files "Direct link to List files") 

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

### Path parameters[â€‹](#get-vaults-vaultuuid-items-itemuuid-files-path-parameters "Direct link to Path parameters") 

  Parameter     Type     Description
  ------------- -------- ----------------------------------------------
  `vaultUUID`   string   The UUID of the vault to get the details of.
  `itemUUID`    string   The UUID of the item to retrieve.

### Query parameters[â€‹](#get-vaults-vaultuuid-items-itemuuid-files-query-parameters "Direct link to Query parameters") 

  Parameter          Type      Description
  ------------------ --------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  `inline_content`   boolean   Whether to return the Base-64 encoded file content. The file size must be less than `OP_MAX_INLINE_FILE_SIZE_KB`, or 100 kilobytes if the file size isn\'t defined. *Optional.*

### Responses[â€‹](#get-vaults-vaultuuid-items-itemuuid-files-responses "Direct link to Responses") 

200
:   Returns an array of [File objects](#item-file-object)

401
:   Invalid or missing token

404
:   Item not found

413
:   File too large to display inline

## Get File details[â€‹](#get-file-details "Direct link to Get File details") 

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

### Path parameters[â€‹](#get-vaults-vaultuuid-items-itemuuid-files-fileuuid-path-parameters "Direct link to Path parameters") 

  Parameter     Type     Description
  ------------- -------- --------------------------------------------------
  `vaultUUID`   string   The UUID of the vault to retrieve the item from.
  `itemUUID`    string   The UUID of the item to retrieve the file from.
  `fileUUID`    string   The UUID of the file to retrieve.

### Query parameters[â€‹](#get-vaults-vaultuuid-items-itemuuid-files-fileuuid-query-parameters "Direct link to Query parameters") 

  Parameter          Type      Description
  ------------------ --------- ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  `inline_content`   boolean   Whether to return the Base-64 encoded file content. The file size must be less than `OP_MAX_INLINE_FILE_SIZE_KB`, or 100 kilobytes if the file size isn\'t defined. *Optional.*

### Responses[â€‹](#get-vaults-vaultuuid-items-itemuuid-files-fileuuid-responses "Direct link to Responses") 

200
:   Returns a [File object](#item-file-object)

401
:   Invalid or missing token

403
:   Unauthorized access

404
:   File not found

413
:   File too large to display inline

## Get file content[â€‹](#get-file-content "Direct link to Get file content") 

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

### Path parameters[â€‹](#get-vaults-vaultuuid-items-itemuuid-files-fileuuid-content-path-parameters "Direct link to Path parameters") 

  Parameter     Type     Description
  ------------- -------- --------------------------------------------------
  `vaultUUID`   string   The UUID of the vault to retrieve the item from.
  `itemUUID`    string   The UUID of the item to retrieve the file from.
  `fileUUID`    string   The UUID of the file to retrieve.

### Query parameters[â€‹](#get-vaults-vaultuuid-items-itemuuid-files-fileuuid-content-query-parameters "Direct link to Query parameters") 

No query parameters.

### Responses[â€‹](#get-vaults-vaultuuid-items-itemuuid-files-fileuuid-content-responses "Direct link to Responses") 

200
:   Returns the content of the file

401
:   Invalid or missing token

403
:   Unauthorized access

404
:   File not found

## List API activity[â€‹](#list-api-activity "Direct link to List API activity") 

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

Retrieve a list of API Requests that have been made.

### Query parameters[â€‹](#get-activity-query-parameters "Direct link to Query parameters") 

  Parameter   Type      Description
  ----------- --------- ----------------------------------------------------------------------------------
  `limit`     integer   How many API Events should be retrieved in a single request. *Optional.*
  `offset`    integer   How far into the collection of API Events should the response start. *Optional.*

## Server Heartbeat[â€‹](#server-heartbeat "Direct link to Server Heartbeat") 

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

Simple \"ping\" endpoint to check whether server is active.

### Query parameters[â€‹](#get-heartbeat-query-parameters "Direct link to Query parameters") 

No query parameters.

### Responses[â€‹](#get-heartbeat-responses "Direct link to Responses") 

200
:   Returns a `text/plain` response with a single \".\"

## Server Health[â€‹](#server-health "Direct link to Server Health") 

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

Query the state of the server and its service dependencies.

### Query parameters[â€‹](#query-parameters-1 "Direct link to Query parameters") 

No query parameters.

### Responses[â€‹](#get-heartbeat-responses "Direct link to Responses") 

200
:   Returns a [Server Health object](#server-health-object)

## Metrics[â€‹](#metrics "Direct link to Metrics") 

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

Returns Prometheus metrics collected by the server.

### Query parameters[â€‹](#query-parameters-2 "Direct link to Query parameters") 

No query parameters.

### Responses[â€‹](#get-heartbeat-responses "Direct link to Responses") 

200
:   Returns a plaintext list of Prometheus metrics. See the [Prometheus documentation](https://prometheus.io/docs/instrumenting/exposition_formats#text-based-format) for specifics.

## Response object models[â€‹](#response-object-models "Direct link to Response object models") 

### APIRequest object[â€‹](#apirequest-object "Direct link to APIRequest object") 

+-----------------------+-----------------------+---------------------------------------------------+
| Parameter             | Type                  | Description                                       |
+=======================+=======================+===================================================+
| `requestID`           | string                | The UUID for the request.                         |
+-----------------------+-----------------------+---------------------------------------------------+
| `timestamp`           | dateTime              | Date and time of the request.                     |
+-----------------------+-----------------------+---------------------------------------------------+
| `action`              | string                | The action taken. One of:                         |
|                       |                       |                                                   |
|                       |                       | - `"READ"`                                        |
|                       |                       | - `"CREATE"`                                      |
|                       |                       | - `"UPDATE"`                                      |
|                       |                       | - `"DELETE"`                                      |
+-----------------------+-----------------------+---------------------------------------------------+
| `result`              | string                | The result of the action. One of:                 |
|                       |                       |                                                   |
|                       |                       | - `"SUCCESS"`                                     |
|                       |                       | - `"DENY"`                                        |
+-----------------------+-----------------------+---------------------------------------------------+
| `actor`               | object                | An [Actor object](#apirequest-actor-object).      |
+-----------------------+-----------------------+---------------------------------------------------+
| `resource`            | object                | A [Resource object](#apirequest-resource-object). |
+-----------------------+-----------------------+---------------------------------------------------+

#### APIRequest: Actor object[â€‹](#apirequest-actor-object "Direct link to APIRequest: Actor object") 

  Parameter     Type     Description
  ------------- -------- ----------------------------------------------------------------
  `id`          string   The UUID of the Connect server that made the request.
  `account`     string   The UUID of the 1Password account the request went to.
  `jti`         string   The UUID of the access token used to authenticate the request.
  `userAgent`   string   The user agent string specified in the request.
  `ip`          string   The IP address the request originated from.

#### APIRequest: Resource object[â€‹](#apirequest-resource-object "Direct link to APIRequest: Resource object") 

+-----------------------+-----------------------+------------------------------------------------------------------------------------------+
| Parameter             | Type                  | Description                                                                              |
+=======================+=======================+==========================================================================================+
| `type`                | string                | The resource requested. One of:                                                          |
|                       |                       |                                                                                          |
|                       |                       | - `"ITEM"`                                                                               |
|                       |                       | - `"VAULT"`                                                                              |
+-----------------------+-----------------------+------------------------------------------------------------------------------------------+
| `vault`               | object                | An object containing an `id` property with the value of the UUID of the vault requested. |
+-----------------------+-----------------------+------------------------------------------------------------------------------------------+
| `item`                | object                | An object containing an `id` property with the value of the UUID of the item requested.  |
+-----------------------+-----------------------+------------------------------------------------------------------------------------------+
| `itemVersion`         | integer               | The version of the item.                                                                 |
+-----------------------+-----------------------+------------------------------------------------------------------------------------------+

### ErrorResponse object[â€‹](#errorresponse-object "Direct link to ErrorResponse object") 

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

  Parameter   Type      Description
  ----------- --------- --------------------------------
  `status`    integer   The HTTP status code.
  `message`   string    A message detailing the error.

### Vault object[â€‹](#vault-object "Direct link to Vault object") 

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

+-----------------------+-----------------------+-----------------------------------------------------------------+
| Parameter             | Type                  | Description                                                     |
+=======================+=======================+=================================================================+
| `id`                  | string                | The UUID of the vault.                                          |
+-----------------------+-----------------------+-----------------------------------------------------------------+
| `name`                | string                | The name of the vault.                                          |
+-----------------------+-----------------------+-----------------------------------------------------------------+
| `description`         | string                | The description for the vault.                                  |
+-----------------------+-----------------------+-----------------------------------------------------------------+
| `attributeVersion`    | integer               | The version of the vault metadata.                              |
+-----------------------+-----------------------+-----------------------------------------------------------------+
| `contentVersion`      | integer               | The version of the vault contents.                              |
+-----------------------+-----------------------+-----------------------------------------------------------------+
| `items`               | integer               | Number of active items in the vault.                            |
+-----------------------+-----------------------+-----------------------------------------------------------------+
| `type`                | string                | The type of vault. One of:                                      |
|                       |                       |                                                                 |
|                       |                       | - `"EVERYONE"`: The team Shared vault.                          |
|                       |                       | - `"PERSONAL"`: The Private vault for the Connect server.       |
|                       |                       | - `"USER_CREATED"`: A vault created by a user.                  |
+-----------------------+-----------------------+-----------------------------------------------------------------+
| `createdAt`           | dateTime              | Date and time when the vault was created.                       |
+-----------------------+-----------------------+-----------------------------------------------------------------+
| `updatedAt`           | dateTime              | Date and time when the vault or its contents were last changed. |
+-----------------------+-----------------------+-----------------------------------------------------------------+

### Item object[â€‹](#item-object "Direct link to Item object") 

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

+-----------------------+-----------------------+--------------------------------------------------------------------------------------------+
| Parameter             | Type                  | Description                                                                                |
+=======================+=======================+============================================================================================+
| `id`                  | string                | The UUID of the item.                                                                      |
+-----------------------+-----------------------+--------------------------------------------------------------------------------------------+
| `title`               | string                | The title of the item.                                                                     |
+-----------------------+-----------------------+--------------------------------------------------------------------------------------------+
| `vault`               | object                | An object containing an `id` property whose value is the UUID of the vault the item is in. |
+-----------------------+-----------------------+--------------------------------------------------------------------------------------------+
| `category`            | string                | The category of the item. One of:                                                          |
|                       |                       |                                                                                            |
|                       |                       | ::: section                                                                                |
|                       |                       | - `"LOGIN"`                                                                                |
|                       |                       | - `"PASSWORD"`                                                                             |
|                       |                       | - `"API_CREDENTIAL"`                                                                       |
|                       |                       | - `"SERVER"`                                                                               |
|                       |                       | - `"DATABASE"`                                                                             |
|                       |                       | - `"CREDIT_CARD"`                                                                          |
|                       |                       | - `"MEMBERSHIP"`                                                                           |
|                       |                       | - `"PASSPORT"`                                                                             |
|                       |                       | - `"SOFTWARE_LICENSE"`                                                                     |
|                       |                       | - `"OUTDOOR_LICENSE"`                                                                      |
|                       |                       | - `"SECURE_NOTE"`                                                                          |
|                       |                       | - `"WIRELESS_ROUTER"`                                                                      |
|                       |                       | - `"BANK_ACCOUNT"`                                                                         |
|                       |                       | - `"DRIVER_LICENSE"`                                                                       |
|                       |                       | - `"IDENTITY"`                                                                             |
|                       |                       | - `"REWARD_PROGRAM"`                                                                       |
|                       |                       | - `"DOCUMENT"`                                                                             |
|                       |                       | - `"EMAIL_ACCOUNT"`                                                                        |
|                       |                       | - `"SOCIAL_SECURITY_NUMBER"`                                                               |
|                       |                       | - `"MEDICAL_RECORD"`                                                                       |
|                       |                       | - `"SSH_KEY"`                                                                              |
|                       |                       | :::                                                                                        |
|                       |                       |                                                                                            |
|                       |                       | You can\'t create items using the \"CUSTOM\" or \"DOCUMENT\" categories.                   |
+-----------------------+-----------------------+--------------------------------------------------------------------------------------------+
| `urls`                | array                 | Array of [URL objects](#item-url-object) containing URLs for the item.                     |
+-----------------------+-----------------------+--------------------------------------------------------------------------------------------+
| `favorite`            | boolean               | Whether the item is marked as a favorite.                                                  |
+-----------------------+-----------------------+--------------------------------------------------------------------------------------------+
| `tags`                | array                 | An array of strings of the tags assigned to the item.                                      |
+-----------------------+-----------------------+--------------------------------------------------------------------------------------------+
| `version`             | integer               | The version of the item.                                                                   |
+-----------------------+-----------------------+--------------------------------------------------------------------------------------------+
| `createdAt`           | dateTime              | Date and time when the item was created.                                                   |
+-----------------------+-----------------------+--------------------------------------------------------------------------------------------+
| `updatedAt`           | dateTime              | Date and time when the vault or its contents were last changed.                            |
+-----------------------+-----------------------+--------------------------------------------------------------------------------------------+
| `lastEditedBy`        | string                | UUID of the account that last changed the item.                                            |
+-----------------------+-----------------------+--------------------------------------------------------------------------------------------+

#### Item: Field object[â€‹](#item-field-object "Direct link to Item: Field object") 

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

+-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| Parameter             | Type                  | Description                                                                                                                                                                                               |
+=======================+=======================+===========================================================================================================================================================================================================+
| `purpose` or `type`   | string                | Use `purpose` for the username, password, and notes fields. Possible values:                                                                                                                              |
|                       |                       |                                                                                                                                                                                                           |
|                       |                       | ::: section                                                                                                                                                                                               |
|                       |                       | - `"USERNAME"`                                                                                                                                                                                            |
|                       |                       | - `"PASSWORD"`                                                                                                                                                                                            |
|                       |                       | - `"NOTES"`                                                                                                                                                                                               |
|                       |                       | :::                                                                                                                                                                                                       |
|                       |                       |                                                                                                                                                                                                           |
|                       |                       | Use `type` for all other fields. Possible values are:                                                                                                                                                     |
|                       |                       |                                                                                                                                                                                                           |
|                       |                       | ::: section                                                                                                                                                                                               |
|                       |                       | - `"STRING"`                                                                                                                                                                                              |
|                       |                       | - `"EMAIL"`                                                                                                                                                                                               |
|                       |                       | - `"CONCEALED"`                                                                                                                                                                                           |
|                       |                       | - `"URL"`                                                                                                                                                                                                 |
|                       |                       | - `"OTP"` (format: `otpauth://`)                                                                                                                                                                          |
|                       |                       | - `"DATE"` (format: `YYYY-MM-DD`)                                                                                                                                                                         |
|                       |                       | - `"MONTH_YEAR"` (format: `YYYYMM` or `YYYY/MM`)                                                                                                                                                          |
|                       |                       | - `"MENU"`                                                                                                                                                                                                |
|                       |                       | :::                                                                                                                                                                                                       |
+-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `value`               | string                | The value to save for the field.                                                                                                                                                                          |
|                       |                       |                                                                                                                                                                                                           |
|                       |                       | You can specify a `generate` field instead of `value` to create a password or other random information for the value.                                                                                     |
+-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `generate`            | boolean               | Generate a password and save in the value for the field. By default, the password is a 32-characters long, made up of letters, numbers, and symbols. To customize the password, include a `recipe` field. |
+-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `recipe`              | object                | A [GeneratorRecipe object](#item-generatorrecipe-object).                                                                                                                                                 |
+-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+
| `section`             | object                | An object containing the UUID of a section in the item.                                                                                                                                                   |
+-----------------------+-----------------------+-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------+

#### Item: File object[â€‹](#item-file-object "Direct link to Item: File object") 

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

  Name             Type      Description
  ---------------- --------- ------------------------------------------------------------------------------
  `id`             string    The UUID of the file.
  `name`           string    The name of the file.
  `size`           integer   The size of the file in bytes.
  `content_path`   string    The path to download the contents of the file.
  `content`        string    The Base64-encoded contents of the file, if `inline_files` is set to `true`.
  `section`        object    An object containing the UUID of a section in the item.

#### Item: GeneratorRecipe object[â€‹](#item-generatorrecipe-object "Direct link to Item: GeneratorRecipe object") 

The recipe is used in conjunction with the \"generate\" property to set the character set used to generate a new secure value.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

+-----------------------+-----------------------+-----------------------------------------------------------------------------------------+
| Name                  | Type                  | Description                                                                             |
+=======================+=======================+=========================================================================================+
| `length`              | integer               | The length of the password to generate. *Optional.*                                     |
+-----------------------+-----------------------+-----------------------------------------------------------------------------------------+
| `characterSets`       | array                 | An array containing of the kinds of characters to include. *Optional.* Possible values: |
|                       |                       |                                                                                         |
|                       |                       | - `"LETTERS"`                                                                           |
|                       |                       | - `"DIGITS"`                                                                            |
|                       |                       | - `"SYMBOLS"`                                                                           |
+-----------------------+-----------------------+-----------------------------------------------------------------------------------------+
| `excludeCharacters`   | string                | A list of all characters that should be excluded from generated passwords. *Optional.*  |
+-----------------------+-----------------------+-----------------------------------------------------------------------------------------+

#### Item: PasswordDetails object[â€‹](#item-passworddetails-object "Direct link to Item: PasswordDetails object") 

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

+-----------------------+-----------------------+--------------------------------------------------------------------+
| Name                  | Type                  | Description                                                        |
+=======================+=======================+====================================================================+
| `entropy`             | integer               | The unpredictability of the password, measured in bits.            |
+-----------------------+-----------------------+--------------------------------------------------------------------+
| `generated`           | boolean               | Whether the password was generated using the password generator.   |
+-----------------------+-----------------------+--------------------------------------------------------------------+
| `strength`            | string                | The strength of the password. One of:                              |
|                       |                       |                                                                    |
|                       |                       | - `"TERRIBLE"`                                                     |
|                       |                       | - `"WEAK"`                                                         |
|                       |                       | - `"FAIR"`                                                         |
|                       |                       | - `"GOOD"`                                                         |
|                       |                       | - `"VERY_GOOD"`                                                    |
|                       |                       | - `"EXCELLENT"`                                                    |
|                       |                       | - `"FANTASTIC"`                                                    |
+-----------------------+-----------------------+--------------------------------------------------------------------+
| `history`             | array                 | An array of strings containing the previous passwords of the item. |
+-----------------------+-----------------------+--------------------------------------------------------------------+

#### Item: Section object[â€‹](#item-section-object "Direct link to Item: Section object") 

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

  Name      Type     Description
  --------- -------- --------------------------------------
  `id`      string   A unique identifier for the section.
  `label`   string   The label for the section.

#### Item: URL object[â€‹](#item-url-object "Direct link to Item: URL object") 

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

  Name        Type      Description
  ----------- --------- -----------------------------------------------
  `label`     string    The label for the URL.
  `primary`   boolean   Whether this is the primary URL for the item.
  `href`      string    The address.

### Server Health object[â€‹](#server-health-object "Direct link to Server Health object") 

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uSWNvbl9iTEpTIj48cGF0aCBmaWxsPSJjdXJyZW50Q29sb3IiIGQ9Ik0xOSwyMUg4VjdIMTlNMTksNUg4QTIsMiAwIDAsMCA2LDdWMjFBMiwyIDAgMCwwIDgsMjNIMTlBMiwyIDAgMCwwIDIxLDIxVjdBMiwyIDAgMCwwIDE5LDVNMTYsMUg0QTIsMiAwIDAsMCAyLDNWMTdINFYzSDE2VjFaIiAvPjwvc3ZnPg==)![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJjb3B5QnV0dG9uU3VjY2Vzc0ljb25fZnlVRiI+PHBhdGggZmlsbD0iY3VycmVudENvbG9yIiBkPSJNMjEsN0w5LDE5TDMuNSwxMy41TDQuOTEsMTIuMDlMOSwxNi4xN0wxOS41OSw1LjU5TDIxLDdaIiAvPjwvc3ZnPg==)]

  Name             Type     Description
  ---------------- -------- -----------------------------------------------------------------------
  `name`           string   Name of the server
  `version`        string   Version info of the Connect server
  `dependencies`   array    An array of [Service Dependencies](#server-health-dependency-object).

#### Server Health: Dependency object[â€‹](#server-health-dependency-object "Direct link to Server Health: Dependency object") 

  Name        Type     Description
  ----------- -------- ---------------------------------------------------------------
  `service`   string   Name of the dependency
  `status`    string   The service\'s reported status
  `message`   string   Extra information about the dependency\'s status. *Optional.*