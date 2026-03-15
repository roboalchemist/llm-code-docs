# Source: https://docs.akeyless.io/reference/gettarget.md

# /get-target

# OpenAPI definition

```json
{
  "openapi": "3.0.0",
  "info": {
    "description": "The purpose of this application is to provide access to Akeyless API.",
    "title": "Akeyless API",
    "contact": {
      "name": "Akeyless",
      "url": "http://akeyless.io",
      "email": "support@akeyless.io"
    },
    "version": "3.0"
  },
  "paths": {
    "/get-target": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "getTarget",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/getTarget"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/getTargetResponse"
          },
          "default": {
            "$ref": "#/components/responses/errorResponse"
          }
        }
      }
    }
  },
  "servers": [
    {
      "url": "https://api.akeyless.io"
    }
  ],
  "components": {
    "responses": {
      "errorResponse": {
        "description": "errorResponse wraps any error to return it as a JSON object with one \"error\"\nfield.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/JSONError"
            }
          }
        }
      },
      "getTargetResponse": {
        "description": "getTargetResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/Target"
            }
          }
        }
      }
    },
    "schemas": {
      "AssocRelationship": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "CertificateStatus": {
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "CertificateVersionInfo": {
        "type": "object",
        "properties": {
          "not_after": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "NotAfter"
          },
          "not_before": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "NotBefore"
          },
          "status": {
            "$ref": "#/components/schemas/CertificateStatus"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "ItemState": {
        "description": "ItemState defines the different states an Item can be in",
        "type": "string",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "ItemType": {
        "type": "string",
        "title": "ItemType defines types supported by AKEYLESS.",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "ItemVersion": {
        "type": "object",
        "title": "ItemVersion describes an item version in AKEYLESS.",
        "properties": {
          "access_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "AccessDate"
          },
          "access_date_display": {
            "type": "string",
            "x-go-name": "AccessDateDisplay"
          },
          "access_id": {
            "type": "string",
            "x-go-name": "AccessId"
          },
          "certificate_version_info": {
            "$ref": "#/components/schemas/CertificateVersionInfo"
          },
          "creation_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "CreationDate"
          },
          "customer_fragment_id": {
            "type": "string",
            "x-go-name": "CustomerFragmentId"
          },
          "deletion_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "DeletionDate"
          },
          "item_version_state": {
            "$ref": "#/components/schemas/ItemState"
          },
          "modification_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "ModificationDate"
          },
          "protection_key_name": {
            "type": "string",
            "x-go-name": "ProtectionKeyName"
          },
          "unique_identifier": {
            "type": "string",
            "x-go-name": "UniqueIdentifier"
          },
          "version": {
            "type": "integer",
            "format": "int32",
            "x-go-name": "Version"
          },
          "with_customer_fragment": {
            "type": "boolean",
            "x-go-name": "WithCustomerFragment"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "JSONError": {
        "type": "object",
        "title": "JSONError wraps an error with JSON object.",
        "properties": {
          "error": {
            "type": "string",
            "x-go-name": "Err"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client"
      },
      "Target": {
        "type": "object",
        "title": "Target includes target details.",
        "properties": {
          "access_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "AccessDate"
          },
          "access_date_display": {
            "type": "string",
            "x-go-name": "AccessDateDisplay"
          },
          "access_request_status": {
            "type": "string",
            "x-go-name": "AccessRequestStatus"
          },
          "attributes": {
            "description": "this is not \"omitempty\" since an empty value causes no update\nwhile an empty map will clear the attributes",
            "type": "object",
            "additionalProperties": {},
            "x-go-name": "Attributes"
          },
          "client_permissions": {
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "ClientPermissions"
          },
          "comment": {
            "type": "string",
            "x-go-name": "Comment"
          },
          "creation_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "CreationDate"
          },
          "is_access_request_enabled": {
            "type": "boolean",
            "x-go-name": "IsAccessRequestEnabled"
          },
          "last_version": {
            "type": "integer",
            "format": "int32",
            "x-go-name": "LastVersion"
          },
          "modification_date": {
            "type": "string",
            "format": "date-time",
            "x-go-name": "ModificationDate"
          },
          "parent_target_name": {
            "type": "string",
            "x-go-name": "ParentTargetName"
          },
          "protection_key_name": {
            "type": "string",
            "x-go-name": "ProtectionKeyName"
          },
          "target_details": {
            "type": "string",
            "x-go-name": "TargetDetails"
          },
          "target_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "TargetID"
          },
          "target_items_assoc": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/TargetItemAssociation"
            },
            "x-go-name": "TargetItemsAssoc"
          },
          "target_name": {
            "type": "string",
            "x-go-name": "TargetName"
          },
          "target_sub_type": {
            "$ref": "#/components/schemas/TargetSubType"
          },
          "target_type": {
            "$ref": "#/components/schemas/TargetType"
          },
          "target_versions": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/ItemVersion"
            },
            "x-go-name": "TargetVersions"
          },
          "with_customer_fragment": {
            "type": "boolean",
            "x-go-name": "WithCustomerFragment"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "TargetItemAssociation": {
        "description": "TargetItemAssociation includes details of an association between a target\nand an item. Also, between targets in case of child target or Linked target.",
        "type": "object",
        "properties": {
          "assoc_id": {
            "type": "string",
            "x-go-name": "AssociationID"
          },
          "attributes": {
            "type": "object",
            "additionalProperties": {
              "type": "string"
            },
            "x-go-name": "Attributes"
          },
          "cluster_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "GWClusterID"
          },
          "item_id": {
            "type": "integer",
            "format": "int64",
            "x-go-name": "ItemID"
          },
          "item_name": {
            "type": "string",
            "x-go-name": "ItemName"
          },
          "item_type": {
            "$ref": "#/components/schemas/ItemType"
          },
          "relationship": {
            "$ref": "#/components/schemas/AssocRelationship"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "TargetSubType": {
        "type": "string",
        "title": "TargetSubType ..",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "TargetType": {
        "type": "string",
        "title": "TargetType ..",
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/infra/types"
      },
      "getTarget": {
        "description": "getTarget is a command that returns target. [Deprecated: Use target-get command]",
        "type": "object",
        "required": [
          "name"
        ],
        "properties": {
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "name": {
            "description": "Target name",
            "type": "string",
            "x-go-name": "TargetName"
          },
          "show-versions": {
            "description": "Include all target versions in reply",
            "type": "boolean",
            "default": false,
            "x-go-name": "ShowVersions"
          },
          "token": {
            "description": "Authentication token (see `/auth` and `/configure`)",
            "type": "string",
            "x-go-name": "Profile"
          },
          "uid-token": {
            "description": "The universal identity token, Required only for universal_identity authentication",
            "type": "string",
            "x-go-name": "UIDToken"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```