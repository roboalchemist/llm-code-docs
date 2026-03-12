# Source: https://help.cloudsmith.io/reference/repos_upstream_deb_read.md

# Retrieve a Debian upstream config for this repository.

Retrieve a Debian upstream config for this repository.

# OpenAPI definition

```json
{
  "openapi": "3.0.0",
  "info": {
    "title": "Cloudsmith API (v1)",
    "description": "The API to the Cloudsmith Service",
    "termsOfService": "https://help.cloudsmith.io",
    "contact": {
      "name": "Cloudsmith Support",
      "url": "https://help.cloudsmith.io",
      "email": "support@cloudsmith.io"
    },
    "license": {
      "name": "MIT",
      "url": "https://opensource.org/licenses/MIT"
    },
    "version": "v1"
  },
  "security": [
    {
      "apikey": []
    },
    {
      "basic": []
    }
  ],
  "paths": {
    "/repos/{owner}/{identifier}/upstream/deb/{slug_perm}/": {
      "get": {
        "operationId": "repos_upstream_deb_read",
        "summary": "Retrieve a Debian upstream config for this repository.",
        "description": "Retrieve a Debian upstream config for this repository.",
        "responses": {
          "200": {
            "description": "OK",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/DebUpstream"
                }
              }
            }
          },
          "400": {
            "description": "Request could not be processed (see detail).",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorDetail"
                }
              }
            }
          },
          "422": {
            "description": "Missing or invalid parameters (see detail).",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/ErrorDetail"
                }
              }
            }
          }
        },
        "tags": [
          "repos"
        ],
        "x-simplified": "fields[upstreams]=auth_mode,available,created_at,disable_reason_text,has_failed_signature_verification,is_active,name,mode,pending_validation,slug_perm,upstream_url,verify_ssl"
      },
      "parameters": [
        {
          "name": "owner",
          "in": "path",
          "required": true,
          "schema": {
            "type": "string"
          }
        },
        {
          "name": "identifier",
          "in": "path",
          "required": true,
          "schema": {
            "type": "string"
          }
        },
        {
          "name": "slug_perm",
          "in": "path",
          "required": true,
          "schema": {
            "type": "string"
          }
        }
      ]
    }
  },
  "servers": [
    {
      "url": "https://api.cloudsmith.io"
    }
  ],
  "components": {
    "securitySchemes": {
      "apikey": {
        "type": "apiKey",
        "name": "X-Api-Key",
        "in": "header"
      },
      "basic": {
        "type": "http",
        "scheme": "basic"
      }
    },
    "schemas": {
      "ErrorDetail": {
        "required": [
          "detail"
        ],
        "type": "object",
        "properties": {
          "detail": {
            "title": "Detail",
            "description": "An extended message for the response.",
            "type": "string",
            "minLength": 1
          },
          "fields": {
            "title": "Fields",
            "description": "A Dictionary of related errors where key: Field and value: Array of Errors related to that field",
            "type": "object",
            "additionalProperties": {
              "type": "array",
              "items": {
                "type": "string",
                "minLength": 1
              }
            }
          }
        }
      },
      "DebUpstream": {
        "required": [
          "distro_versions",
          "name",
          "upstream_url"
        ],
        "type": "object",
        "properties": {
          "auth_mode": {
            "title": "Auth mode",
            "description": "The authentication mode to use when accessing this upstream. ",
            "type": "string",
            "enum": [
              "None",
              "Username and Password"
            ],
            "default": "None"
          },
          "auth_secret": {
            "title": "Secret",
            "description": "Secret to provide with requests to upstream.",
            "type": "string",
            "maxLength": 4096,
            "nullable": true
          },
          "auth_username": {
            "title": "Username",
            "description": "Username to provide with requests to upstream.",
            "type": "string",
            "maxLength": 64,
            "nullable": true
          },
          "available": {
            "title": "Available",
            "description": "Whether the upstream is available for use.",
            "type": "boolean",
            "readOnly": true
          },
          "can_reindex": {
            "title": "Can reindex",
            "description": "Whether the upstream can be reindexed.",
            "type": "boolean",
            "readOnly": true
          },
          "component": {
            "title": "Component",
            "description": "The component to fetch from the upstream",
            "type": "string",
            "maxLength": 64,
            "minLength": 1
          },
          "created_at": {
            "title": "Created at",
            "description": "The datetime the upstream source was created.",
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "disable_reason": {
            "title": "Disable reason",
            "type": "string",
            "enum": [
              "N/A",
              "Upstream points to its own repository",
              "Missing upstream source",
              "Upstream was disabled by request of user"
            ],
            "readOnly": true,
            "default": "N/A"
          },
          "disable_reason_text": {
            "title": "Disable reason text",
            "description": "Human-readable explanation of why this upstream is disabled",
            "type": "string",
            "readOnly": true
          },
          "distro_versions": {
            "description": "The distribution version that packages found on this upstream could be associated with.",
            "type": "array",
            "items": {
              "description": "The distribution version that packages found on this upstream could be associated with.",
              "type": "string"
            },
            "uniqueItems": true
          },
          "extra_header_1": {
            "title": "Header #1",
            "description": "The key for extra header #1 to send to upstream.",
            "type": "string",
            "pattern": "^[-\\w]+$",
            "maxLength": 64,
            "nullable": true
          },
          "extra_header_2": {
            "title": "Header #2",
            "description": "The key for extra header #2 to send to upstream.",
            "type": "string",
            "pattern": "^[-\\w]+$",
            "maxLength": 64,
            "nullable": true
          },
          "extra_value_1": {
            "title": "Value #1",
            "description": "The value for extra header #1 to send to upstream. This is stored as plaintext, and is NOT encrypted.",
            "type": "string",
            "pattern": "^[^\\n\\r]+$",
            "maxLength": 128,
            "nullable": true
          },
          "extra_value_2": {
            "title": "Value #2",
            "description": "The value for extra header #2 to send to upstream. This is stored as plaintext, and is NOT encrypted.",
            "type": "string",
            "pattern": "^[^\\n\\r]+$",
            "maxLength": 128,
            "nullable": true
          },
          "gpg_key_fingerprint_short": {
            "title": "Gpg key fingerprint short",
            "type": "string",
            "readOnly": true
          },
          "gpg_key_inline": {
            "title": "GPG Key",
            "description": "A public GPG key to associate with packages found on this upstream. When using the Cloudsmith setup script, this GPG key will be automatically imported on your deployment machines to allow upstream packages to validate and install.",
            "type": "string",
            "nullable": true
          },
          "gpg_key_url": {
            "title": "GPG Key URL",
            "description": "When provided, Cloudsmith will fetch, validate, and associate a public GPG key found at the provided URL. When using the Cloudsmith setup script, this GPG key will be automatically imported on your deployment machines to allow upstream packages to validate and install.",
            "type": "string",
            "format": "uri",
            "maxLength": 254,
            "nullable": true
          },
          "gpg_verification": {
            "title": "Gpg verification",
            "description": "The GPG signature verification mode for this upstream.",
            "type": "string",
            "enum": [
              "Allow All",
              "Warn on Invalid",
              "Reject Invalid"
            ],
            "default": "Allow All"
          },
          "has_failed_signature_verification": {
            "title": "Has failed signature verification",
            "description": "Whether the upstream has failed signature verification.",
            "type": "boolean",
            "readOnly": true
          },
          "include_sources": {
            "title": "Source Packages",
            "description": "When true, source packages will be available from this upstream.",
            "type": "boolean"
          },
          "index_package_count": {
            "title": "Index package count",
            "description": "The number of packages available in this upstream source",
            "type": "integer",
            "readOnly": true,
            "nullable": true
          },
          "index_status": {
            "title": "Index status",
            "description": "The current indexing status of this upstream source",
            "type": "string",
            "readOnly": true
          },
          "is_active": {
            "title": "Is active",
            "description": "Whether or not this upstream is active and ready for requests.",
            "type": "boolean"
          },
          "last_indexed": {
            "title": "Last indexed",
            "description": "The last time this upstream source was indexed",
            "type": "string",
            "readOnly": true
          },
          "mode": {
            "title": "Mode",
            "description": "The mode that this upstream should operate in. Upstream sources can be used to proxy resolved packages, as well as operate in a proxy/cache or cache only mode.",
            "type": "string",
            "enum": [
              "Proxy Only",
              "Cache and Proxy"
            ],
            "default": "Proxy Only"
          },
          "name": {
            "title": "Name",
            "description": "A descriptive name for this upstream source. A shortened version of this name will be used for tagging cached packages retrieved from this upstream.",
            "type": "string",
            "pattern": "^\\w[\\w \\-'\\.\\/()]+$",
            "maxLength": 64,
            "minLength": 1
          },
          "pending_validation": {
            "title": "Pending validation",
            "description": "When true, this upstream source is pending validation.",
            "type": "boolean",
            "readOnly": true
          },
          "priority": {
            "title": "Priority",
            "description": "Upstream sources are selected for resolving requests by sequential order (1..n), followed by creation date.",
            "type": "integer",
            "maximum": 32767,
            "minimum": 1
          },
          "slug_perm": {
            "title": "Slug perm",
            "type": "string",
            "format": "slug",
            "pattern": "^[-a-zA-Z0-9_]+$",
            "readOnly": true,
            "minLength": 1
          },
          "updated_at": {
            "title": "Updated at",
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "upstream_distribution": {
            "title": "Upstream distribution",
            "description": "The distribution to fetch from the upstream",
            "type": "string",
            "maxLength": 64,
            "minLength": 1,
            "nullable": true
          },
          "upstream_url": {
            "title": "Upstream URL",
            "description": "The URL for this upstream source. This must be a fully qualified URL including any path elements required to reach the root of the repository. ",
            "type": "string",
            "format": "uri",
            "maxLength": 200,
            "minLength": 1
          },
          "verification_status": {
            "title": "Verification status",
            "description": "The signature verification status for this upstream.",
            "type": "string",
            "enum": [
              "Unknown",
              "Invalid",
              "Valid",
              "Invalid (No Key)"
            ],
            "readOnly": true,
            "default": "Unknown"
          },
          "verify_ssl": {
            "title": "Verify SSL Certificates",
            "description": "If enabled, SSL certificates are verified when requests are made to this upstream. It's recommended to leave this enabled for all public sources to help mitigate Man-In-The-Middle (MITM) attacks. Please note this only applies to HTTPS upstreams.",
            "type": "boolean"
          }
        }
      }
    }
  }
}
```