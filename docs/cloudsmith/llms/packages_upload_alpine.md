# Source: https://help.cloudsmith.io/reference/packages_upload_alpine.md

# Create a new Alpine package

Create a new Alpine package

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
    "/packages/{owner}/{repo}/upload/alpine/": {
      "post": {
        "operationId": "packages_upload_alpine",
        "summary": "Create a new Alpine package",
        "description": "Create a new Alpine package",
        "requestBody": {
          "$ref": "#/components/requestBodies/AlpinePackageUploadRequest"
        },
        "responses": {
          "201": {
            "description": "Upload acknowledged and queued for synchronization.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/AlpinePackageUpload"
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
          "404": {
            "description": "Namespace (owner) or repository not found",
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
          "packages"
        ]
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
          "name": "repo",
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
    "requestBodies": {
      "AlpinePackageUploadRequest": {
        "content": {
          "application/json": {
            "schema": {
              "$ref": "#/components/schemas/AlpinePackageUploadRequest"
            }
          }
        }
      }
    },
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
      "DistributionVersion": {
        "description": "A list of the versions for this distribution",
        "type": "object",
        "properties": {
          "name": {
            "title": "Name",
            "description": "The textual name for this version.",
            "type": "string",
            "maxLength": 64
          },
          "slug": {
            "title": "Slug",
            "description": "The slug identifier for this version",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          }
        }
      },
      "Distribution": {
        "description": "The distributions supported by this package format",
        "required": [
          "name"
        ],
        "type": "object",
        "properties": {
          "name": {
            "title": "Name",
            "type": "string",
            "maxLength": 32,
            "minLength": 1
          },
          "self_url": {
            "title": "Self url",
            "type": "string",
            "format": "uri",
            "readOnly": true
          },
          "slug": {
            "title": "Slug",
            "description": "The slug identifier for this distribution",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          },
          "variants": {
            "title": "Variants",
            "type": "string",
            "maxLength": 128,
            "nullable": true
          }
        },
        "nullable": true
      },
      "Architecture": {
        "required": [
          "name"
        ],
        "type": "object",
        "properties": {
          "description": {
            "title": "Description",
            "type": "string",
            "maxLength": 64,
            "nullable": true
          },
          "name": {
            "title": "Name",
            "type": "string",
            "maxLength": 128,
            "minLength": 1
          }
        }
      },
      "PackageFile": {
        "type": "object",
        "properties": {
          "cdn_url": {
            "title": "Cdn url",
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "checksum_md5": {
            "title": "Checksum md5",
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "checksum_sha1": {
            "title": "Checksum sha1",
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "checksum_sha256": {
            "title": "Checksum sha256",
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "checksum_sha512": {
            "title": "Checksum sha512",
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "downloads": {
            "title": "Downloads",
            "type": "integer",
            "readOnly": true
          },
          "filename": {
            "title": "Filename",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          },
          "is_downloadable": {
            "title": "Is downloadable",
            "type": "boolean",
            "readOnly": true
          },
          "is_primary": {
            "title": "Is primary",
            "type": "boolean",
            "readOnly": true
          },
          "is_synchronised": {
            "title": "Is synchronised",
            "type": "boolean",
            "readOnly": true
          },
          "signature_url": {
            "title": "Signature url",
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "size": {
            "title": "Size",
            "description": "The calculated size of the file.",
            "type": "integer",
            "readOnly": true
          },
          "slug_perm": {
            "title": "Slug perm",
            "type": "string",
            "format": "slug",
            "pattern": "^[-a-zA-Z0-9_]+$",
            "readOnly": true,
            "minLength": 1
          },
          "tag": {
            "title": "Tag",
            "description": "Freeform descriptor that describes what the file is.",
            "type": "string",
            "readOnly": true,
            "nullable": true
          }
        }
      },
      "Tags": {
        "description": "All tags on the package, grouped by tag type. This includes immutable tags, but doesn't distinguish them from mutable. To see which tags are immutable specifically, see the tags_immutable field.",
        "type": "object",
        "properties": {}
      },
      "AlpinePackageUploadRequest": {
        "required": [
          "distribution",
          "package_file"
        ],
        "type": "object",
        "properties": {
          "distribution": {
            "title": "Distribution",
            "description": "The distribution to store the package for.",
            "type": "string",
            "minLength": 1
          },
          "package_file": {
            "title": "Package file",
            "description": "The primary file for the package.",
            "type": "string",
            "minLength": 1
          },
          "republish": {
            "title": "Republish",
            "description": "If true, the uploaded package will overwrite any others with the same attributes (e.g. same version); otherwise, it will be flagged as a duplicate.",
            "type": "boolean"
          },
          "tags": {
            "title": "Tags",
            "description": "A comma-separated values list of tags to add to the package.",
            "type": "string",
            "maxLength": 1024,
            "minLength": 1,
            "nullable": true
          }
        }
      },
      "AlpinePackageUpload": {
        "type": "object",
        "properties": {
          "architectures": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/Architecture"
            },
            "readOnly": true
          },
          "cdn_url": {
            "title": "Cdn url",
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "checksum_md5": {
            "title": "Checksum md5",
            "type": "string",
            "readOnly": true
          },
          "checksum_sha1": {
            "title": "Checksum sha1",
            "type": "string",
            "readOnly": true
          },
          "checksum_sha256": {
            "title": "Checksum sha256",
            "type": "string",
            "readOnly": true
          },
          "checksum_sha512": {
            "title": "Checksum sha512",
            "type": "string",
            "readOnly": true
          },
          "dependencies_checksum_md5": {
            "title": "Dependencies checksum md5",
            "description": "A checksum of all of the package's dependencies.",
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "dependencies_url": {
            "title": "Dependencies url",
            "type": "string",
            "format": "uri",
            "readOnly": true
          },
          "description": {
            "title": "Description",
            "description": "A textual description of this package.",
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "display_name": {
            "title": "Display name",
            "type": "string",
            "readOnly": true
          },
          "distro": {
            "$ref": "#/components/schemas/Distribution"
          },
          "distro_version": {
            "$ref": "#/components/schemas/DistributionVersion"
          },
          "downloads": {
            "title": "Downloads",
            "type": "integer",
            "readOnly": true
          },
          "epoch": {
            "title": "Epoch",
            "description": "The epoch of the package version (if any).",
            "type": "integer",
            "readOnly": true,
            "nullable": true
          },
          "extension": {
            "title": "Extension",
            "type": "string",
            "readOnly": true
          },
          "filename": {
            "title": "Filename",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          },
          "files": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/PackageFile"
            },
            "readOnly": true
          },
          "format": {
            "title": "Format",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          },
          "format_url": {
            "title": "Format url",
            "type": "string",
            "format": "uri",
            "readOnly": true
          },
          "freeable_storage": {
            "title": "Freeable storage",
            "description": "Amount of storage that will be freed if this package is deleted",
            "type": "integer",
            "readOnly": true
          },
          "fully_qualified_name": {
            "title": "Fully qualified name",
            "type": "string",
            "readOnly": true,
            "minLength": 1,
            "nullable": true
          },
          "identifier_perm": {
            "title": "Identifier perm",
            "description": "Unique and permanent identifier for the package.",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          },
          "identifiers": {
            "title": "Identifiers",
            "description": "Return a map of identifier field names and their values.",
            "type": "object",
            "additionalProperties": {
              "type": "string",
              "nullable": true
            },
            "readOnly": true
          },
          "indexed": {
            "title": "Indexed",
            "type": "boolean",
            "readOnly": true
          },
          "is_cancellable": {
            "title": "Is cancellable",
            "type": "boolean",
            "readOnly": true
          },
          "is_copyable": {
            "title": "Is copyable",
            "type": "boolean",
            "readOnly": true
          },
          "is_deleteable": {
            "title": "Is deleteable",
            "type": "boolean",
            "readOnly": true
          },
          "is_downloadable": {
            "title": "Is downloadable",
            "type": "boolean",
            "readOnly": true
          },
          "is_moveable": {
            "title": "Is moveable",
            "type": "boolean",
            "readOnly": true
          },
          "is_quarantinable": {
            "title": "Is quarantinable",
            "type": "boolean",
            "readOnly": true
          },
          "is_quarantined": {
            "title": "Is quarantined",
            "type": "boolean",
            "readOnly": true
          },
          "is_resyncable": {
            "title": "Is resyncable",
            "type": "boolean",
            "readOnly": true
          },
          "is_security_scannable": {
            "title": "Is security scannable",
            "type": "boolean",
            "readOnly": true
          },
          "is_sync_awaiting": {
            "title": "Is sync awaiting",
            "type": "boolean",
            "readOnly": true
          },
          "is_sync_completed": {
            "title": "Is sync completed",
            "type": "boolean",
            "readOnly": true
          },
          "is_sync_failed": {
            "title": "Is sync failed",
            "type": "boolean",
            "readOnly": true
          },
          "is_sync_in_flight": {
            "title": "Is sync in flight",
            "type": "boolean",
            "readOnly": true
          },
          "is_sync_in_progress": {
            "title": "Is sync in progress",
            "type": "boolean",
            "readOnly": true
          },
          "license": {
            "title": "License",
            "description": "The license of this package.",
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "name": {
            "title": "Name",
            "description": "The name of this package.",
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "namespace": {
            "title": "Namespace",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          },
          "namespace_url": {
            "title": "Namespace url",
            "type": "string",
            "format": "uri",
            "readOnly": true
          },
          "num_files": {
            "title": "Num files",
            "type": "integer",
            "readOnly": true
          },
          "origin_repository": {
            "title": "Origin repository",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          },
          "origin_repository_url": {
            "title": "Origin repository url",
            "type": "string",
            "format": "uri",
            "readOnly": true
          },
          "package_type": {
            "title": "Package type",
            "description": "The type of package contents.",
            "type": "integer",
            "enum": [
              1,
              2,
              3,
              9
            ],
            "readOnly": true
          },
          "policy_violated": {
            "title": "Policy violated",
            "description": "Whether or not the package has violated any policy.",
            "type": "boolean",
            "readOnly": true
          },
          "raw_license": {
            "title": "Raw license",
            "description": "The raw license string.",
            "type": "string",
            "readOnly": true,
            "minLength": 1,
            "nullable": true
          },
          "release": {
            "title": "Release",
            "description": "The release of the package version (if any).",
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "repository": {
            "title": "Repository",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          },
          "repository_url": {
            "title": "Repository url",
            "type": "string",
            "format": "uri",
            "readOnly": true
          },
          "security_scan_completed_at": {
            "title": "Security scan completed at",
            "description": "The datetime the security scanning was completed.",
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "security_scan_started_at": {
            "title": "Security scan started at",
            "description": "The datetime the security scanning was started.",
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "security_scan_status": {
            "title": "Security scan status",
            "type": "string",
            "enum": [
              "Awaiting Security Scan",
              "Security Scanning in Progress",
              "Scan Detected Vulnerabilities",
              "Scan Detected No Vulnerabilities",
              "Security Scanning Disabled",
              "Security Scanning Failed",
              "Security Scanning Skipped",
              "Security Scanning Not Supported"
            ],
            "readOnly": true,
            "default": "Awaiting Security Scan",
            "nullable": true
          },
          "security_scan_status_updated_at": {
            "title": "Security scan status updated at",
            "description": "The datetime the security scanning status was updated.",
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "self_html_url": {
            "title": "Self html url",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          },
          "self_url": {
            "title": "Self url",
            "type": "string",
            "format": "uri",
            "readOnly": true
          },
          "self_webapp_url": {
            "title": "Self webapp url",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          },
          "signature_url": {
            "title": "Signature url",
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "size": {
            "title": "Size",
            "description": "The calculated size of the package.",
            "type": "integer",
            "readOnly": true
          },
          "slug": {
            "title": "Slug",
            "description": "The public unique identifier for the package.",
            "type": "string",
            "format": "slug",
            "pattern": "^[-a-zA-Z0-9_]+$",
            "readOnly": true,
            "minLength": 1
          },
          "slug_perm": {
            "title": "Slug perm",
            "type": "string",
            "format": "slug",
            "pattern": "^[-a-zA-Z0-9_]+$",
            "readOnly": true,
            "minLength": 1
          },
          "spdx_license": {
            "title": "Spdx license",
            "description": "The SPDX license identifier for this package.",
            "type": "string",
            "readOnly": true,
            "minLength": 1,
            "nullable": true
          },
          "stage": {
            "title": "Stage",
            "description": "The synchronisation (in progress) stage of the package.",
            "type": "integer",
            "enum": [
              0,
              1,
              2,
              3,
              4,
              5,
              6,
              7,
              8,
              9,
              10,
              11,
              12
            ],
            "readOnly": true
          },
          "stage_str": {
            "title": "Stage str",
            "type": "string",
            "readOnly": true
          },
          "stage_updated_at": {
            "title": "Stage updated at",
            "description": "The datetime the package stage was updated at.",
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "status": {
            "title": "Status",
            "description": "The synchronisation status of the package.",
            "type": "integer",
            "enum": [
              1,
              2,
              3,
              4,
              5,
              6,
              7
            ],
            "readOnly": true
          },
          "status_reason": {
            "title": "Status reason",
            "description": "A textual description for the synchronous status reason (if any",
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "status_str": {
            "title": "Status str",
            "type": "string",
            "readOnly": true
          },
          "status_updated_at": {
            "title": "Status updated at",
            "description": "The datetime the package status was updated at.",
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "status_url": {
            "title": "Status url",
            "type": "string",
            "format": "uri",
            "readOnly": true
          },
          "subtype": {
            "title": "Subtype",
            "type": "string",
            "readOnly": true
          },
          "summary": {
            "title": "Summary",
            "description": "A one-liner synopsis of this package.",
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "sync_finished_at": {
            "title": "Sync finished at",
            "description": "The datetime the package sync was finished at.",
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "sync_progress": {
            "title": "Sync progress",
            "description": "Synchronisation progress (from 0-100)",
            "type": "integer",
            "readOnly": true
          },
          "tags_automatic": {
            "$ref": "#/components/schemas/Tags"
          },
          "tags_immutable": {
            "$ref": "#/components/schemas/Tags"
          },
          "type_display": {
            "title": "Type display",
            "type": "string",
            "readOnly": true
          },
          "uploaded_at": {
            "title": "Uploaded at",
            "description": "The date this package was uploaded.",
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "uploader": {
            "title": "Uploader",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          },
          "uploader_url": {
            "title": "Uploader url",
            "type": "string",
            "format": "uri",
            "readOnly": true
          },
          "version": {
            "title": "Version",
            "description": "The raw version for this package.",
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "version_orig": {
            "title": "Version orig",
            "type": "string",
            "readOnly": true
          },
          "vulnerability_scan_results_url": {
            "title": "Vulnerability scan results url",
            "type": "string",
            "format": "uri",
            "readOnly": true
          }
        }
      }
    }
  }
}
```