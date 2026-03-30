# Source: https://docs.akeyless.io/reference/createtokenizer.md

# /create-tokenizer

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
    "/create-tokenizer": {
      "post": {
        "tags": [
          "v2"
        ],
        "operationId": "createTokenizer",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/createTokenizer"
              }
            }
          },
          "required": true,
          "x-go-name": "Body"
        },
        "responses": {
          "200": {
            "$ref": "#/components/responses/createTokenizerResponse"
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
      "createTokenizerResponse": {
        "description": "createTokenizerResponse wraps response body.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/createTokenizerOutput"
            }
          }
        }
      },
      "errorResponse": {
        "description": "errorResponse wraps any error to return it as a JSON object with one \"error\"\nfield.",
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/JSONError"
            }
          }
        }
      }
    },
    "schemas": {
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
      "createTokenizer": {
        "description": "createTokenizer is a command that creates a tokenizer item",
        "type": "object",
        "required": [
          "tokenizer-type",
          "template-type",
          "name"
        ],
        "properties": {
          "alphabet": {
            "description": "Alphabet to use in regexp vaultless tokenization",
            "type": "string",
            "x-go-name": "Alphabet"
          },
          "decoding-template": {
            "description": "The Decoding output template to use in regexp vaultless tokenization",
            "type": "string",
            "x-go-name": "DecodingTemplate"
          },
          "delete_protection": {
            "description": "Protection from accidental deletion of this object [true/false]",
            "type": "string",
            "x-go-name": "ObjectProtected"
          },
          "description": {
            "description": "Description of the object",
            "type": "string",
            "x-go-name": "Description"
          },
          "encoding-template": {
            "description": "The Encoding output template to use in regexp vaultless tokenization",
            "type": "string",
            "x-go-name": "EncodingTemplate"
          },
          "encryption-key-name": {
            "description": "AES key name to use in vaultless tokenization",
            "type": "string",
            "x-go-name": "EncryptionKeyName"
          },
          "item-custom-fields": {
            "description": "Additional custom fields to associate with the item",
            "type": "object",
            "additionalProperties": {
              "type": "string"
            },
            "x-go-name": "ItemCustomFields"
          },
          "json": {
            "description": "Set output format to JSON",
            "type": "boolean",
            "default": false,
            "x-go-name": "Json"
          },
          "metadata": {
            "description": "Deprecated - use description",
            "type": "string",
            "x-go-name": "Metadata"
          },
          "name": {
            "description": "Tokenizer name",
            "type": "string",
            "x-go-name": "TokenizerName"
          },
          "pattern": {
            "description": "Pattern to use in regexp vaultless tokenization",
            "type": "string",
            "x-go-name": "Pattern"
          },
          "tag": {
            "description": "List of the tags attached to this key",
            "type": "array",
            "items": {
              "type": "string"
            },
            "x-go-name": "Tags"
          },
          "template-type": {
            "description": "Which template type this tokenizer is used for [SSN,CreditCard,USPhoneNumber,Email,Regexp]",
            "type": "string",
            "x-go-name": "TemplateType"
          },
          "token": {
            "description": "Authentication token (see `/auth` and `/configure`)",
            "type": "string",
            "x-go-name": "Profile"
          },
          "tokenizer-type": {
            "description": "Tokenizer type",
            "type": "string",
            "default": "vaultless",
            "x-go-name": "TokenizerType"
          },
          "tweak-type": {
            "description": "The tweak type to use in vaultless tokenization [Supplied, Generated, Internal, Masking]",
            "type": "string",
            "x-go-name": "TweakType"
          },
          "uid-token": {
            "description": "The universal identity token, Required only for universal_identity authentication",
            "type": "string",
            "x-go-name": "UIDToken"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      },
      "createTokenizerOutput": {
        "type": "object",
        "properties": {
          "name": {
            "type": "string",
            "x-go-name": "Name"
          }
        },
        "x-go-package": "akeyless.io/akeyless-main-repo/go/src/client/commands"
      }
    }
  }
}
```