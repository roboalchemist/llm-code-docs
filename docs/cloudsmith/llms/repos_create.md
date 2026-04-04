# Source: https://help.cloudsmith.io/reference/repos_create.md

# Create a new repository in a given namespace.

Create a new repository in a given namespace.

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
    "/repos/{owner}/": {
      "post": {
        "operationId": "repos_create",
        "summary": "Create a new repository in a given namespace.",
        "description": "Create a new repository in a given namespace.",
        "requestBody": {
          "content": {
            "application/json": {
              "schema": {
                "$ref": "#/components/schemas/RepositoryCreateRequest"
              }
            }
          }
        },
        "responses": {
          "201": {
            "description": "The repository was created.",
            "content": {
              "application/json": {
                "schema": {
                  "$ref": "#/components/schemas/RepositoryCreate"
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
            "description": "Owner namespace not found.",
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
      "RepositoryEcdsaKey": {
        "type": "object",
        "properties": {
          "active": {
            "title": "Active",
            "description": "If selected this is the active key for this repository.",
            "type": "boolean",
            "readOnly": true
          },
          "created_at": {
            "title": "Created at",
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "default": {
            "title": "Default",
            "description": "If selected this is the default key for this repository.",
            "type": "boolean",
            "readOnly": true
          },
          "fingerprint": {
            "title": "Fingerprint",
            "description": "The long identifier used by ECDSA for this key.",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          },
          "fingerprint_short": {
            "title": "Fingerprint short",
            "type": "string",
            "readOnly": true
          },
          "public_key": {
            "title": "Public key",
            "description": "The public key given to repository users.",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          },
          "ssh_fingerprint": {
            "title": "Ssh fingerprint",
            "description": "The SSH fingerprint used by ECDSA for this key.",
            "type": "string",
            "readOnly": true,
            "nullable": true
          }
        }
      },
      "RepositoryGpgKey": {
        "required": [
          "comment"
        ],
        "type": "object",
        "properties": {
          "active": {
            "title": "Active",
            "description": "If selected this is the active key for this repository.",
            "type": "boolean",
            "readOnly": true
          },
          "comment": {
            "title": "Comment",
            "type": "string",
            "minLength": 1
          },
          "created_at": {
            "title": "Created at",
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "default": {
            "title": "Default",
            "description": "If selected this is the default key for this repository.",
            "type": "boolean",
            "readOnly": true
          },
          "fingerprint": {
            "title": "Fingerprint",
            "description": "The long identifier used by GPG for this key.",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          },
          "fingerprint_short": {
            "title": "Fingerprint short",
            "type": "string",
            "readOnly": true
          },
          "public_key": {
            "title": "Public key",
            "description": "The public key given to repository users.",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          }
        }
      },
      "RepositoryCreateRequest": {
        "required": [
          "name"
        ],
        "type": "object",
        "properties": {
          "broadcast_state": {
            "title": "Broadcast state",
            "description": "Broadcasting status of a repository.",
            "type": "string",
            "enum": [
              "Off",
              "Private",
              "Internal",
              "Public",
              "Open-Source"
            ],
            "default": "Off"
          },
          "content_kind": {
            "title": "Content kind",
            "description": "The repository content kind determines whether this repository contains packages, or provides a distribution of packages from other repositories. You can only select the content kind at repository creation time.",
            "type": "string",
            "enum": [
              "Standard",
              "Distribution",
              "Upstream"
            ],
            "default": "Standard"
          },
          "contextual_auth_realm": {
            "title": "Contextual Authentication Realm?",
            "description": "If checked, missing credentials for this repository where basic authentication is required shall present an enriched value in the 'WWW-Authenticate' header containing the namespace and repository. This can be useful for tooling such as SBT where the authentication realm is used to distinguish and disambiguate credentials.",
            "type": "boolean"
          },
          "copy_own": {
            "title": "Users Can Copy Own Packages",
            "description": "If checked, users can copy any of their own packages that they have uploaded, assuming that they still have write privilege for the repository. This takes precedence over privileges configured in the 'Access Controls' section of the repository, and any inherited from the org.",
            "type": "boolean"
          },
          "copy_packages": {
            "title": "Copy packages",
            "description": "This defines the minimum level of privilege required for a user to copy packages. Unless the package was uploaded by that user, in which the permission may be overridden by the user-specific copy setting.",
            "type": "string",
            "enum": [
              "Admin",
              "Write",
              "Read"
            ],
            "default": "Read"
          },
          "cosign_signing_enabled": {
            "title": "Cosign Signing Enabled?",
            "description": "When enabled, all pushed (or pulled from upstream) OCI packages and artifacts will be signed using cosign with the repository's ECDSA key. This generates a distinct cosign signature artifact per artifact.",
            "type": "boolean"
          },
          "default_privilege": {
            "title": "Default privilege",
            "description": "This defines the default level of privilege that all of your organization members have for this repository. This does not include collaborators, but applies to any member of the org regardless of their own membership role (i.e. it applies to owners, managers and members). Be careful if setting this to admin, because any member will be able to change settings.",
            "type": "string",
            "enum": [
              "Admin",
              "Write",
              "Read",
              "None"
            ],
            "default": "None"
          },
          "delete_own": {
            "title": "Users Can Delete Own Packages",
            "description": "If checked, users can delete any of their own packages that they have uploaded, assuming that they still have write privilege for the repository. This takes precedence over privileges configured in the 'Access Controls' section of the repository, and any inherited from the org.",
            "type": "boolean"
          },
          "delete_packages": {
            "title": "Delete packages",
            "description": "This defines the minimum level of privilege required for a user to delete packages. Unless the package was uploaded by that user, in which the permission may be overridden by the user-specific delete setting.",
            "type": "string",
            "enum": [
              "Admin",
              "Write"
            ],
            "default": "Admin"
          },
          "description": {
            "title": "Description",
            "description": "A description of the repository's purpose/contents.",
            "type": "string"
          },
          "distributes": {
            "description": "The repositories distributed through this repo. Adding repos here is only valid if the content_kind is DISTRIBUTION.",
            "type": "array",
            "items": {
              "description": "The repositories distributed through this repo. Adding repos here is only valid if the content_kind is DISTRIBUTION.",
              "type": "string",
              "format": "slug",
              "pattern": "^[-a-zA-Z0-9_]+$"
            },
            "uniqueItems": true
          },
          "docker_refresh_tokens_enabled": {
            "title": "Docker Auth Refresh Enabled?",
            "description": "If checked, refresh tokens will be issued in addition to access tokens for Docker authentication. This allows unlimited extension of the lifetime of access tokens.",
            "type": "boolean"
          },
          "enforce_eula": {
            "title": "Require EULA acceptance for downloads?",
            "description": "If checked, downloads will explicitly require acceptance of an EULA.",
            "type": "boolean"
          },
          "generic_package_index_enabled": {
            "title": "Serve index for generic packages?",
            "description": "If checked, HTML indexes will be generated that list all available generic packages in the repository.",
            "type": "boolean"
          },
          "index_files": {
            "title": "Index Files?",
            "description": "If checked, files contained in packages will be indexed, which increase the synchronisation time required for packages. Note that it is recommended you keep this enabled unless the synchronisation time is significantly impacted.",
            "type": "boolean"
          },
          "manage_entitlements_privilege": {
            "title": "Manage entitlements privilege",
            "description": "This defines the minimum level of privilege required for a user to manage entitlement tokens with private repositories. Management is the ability to create, alter, enable, disable or delete all tokens without a repository.",
            "type": "string",
            "enum": [
              "Admin",
              "Write",
              "Read"
            ],
            "default": "Admin"
          },
          "move_own": {
            "title": "Users Can Move Own Packages",
            "description": "If checked, users can move any of their own packages that they have uploaded, assuming that they still have write privilege for the repository. This takes precedence over privileges configured in the 'Access Controls' section of the repository, and any inherited from the org.",
            "type": "boolean"
          },
          "move_packages": {
            "title": "Move packages",
            "description": "This defines the minimum level of privilege required for a user to move packages. Unless the package was uploaded by that user, in which the permission may be overridden by the user-specific move setting.",
            "type": "string",
            "enum": [
              "Admin",
              "Write",
              "Read"
            ],
            "default": "Admin"
          },
          "name": {
            "title": "Name",
            "description": "A descriptive name for the repository.",
            "type": "string",
            "pattern": "^\\w[\\w \\-'\\.\\/()]+$",
            "maxLength": 50,
            "minLength": 1
          },
          "nuget_native_signing_enabled": {
            "title": "Nuget Native Signing Enabled?",
            "description": "When enabled, all pushed (or pulled from upstream) nuget packages and artifacts will be signed using the repository's X.509 RSA certificate. Additionally, the nuget RepositorySignature index will list all of the repository's signing certificates including the ones from configured upstreams.",
            "type": "boolean"
          },
          "open_source_license": {
            "title": "Open source license",
            "description": "The SPDX identifier of the open source license.",
            "type": "string",
            "nullable": true
          },
          "open_source_project_url": {
            "title": "Open-Source Project URL",
            "description": "The URL to the Open-Source project, used for validating that the project meets the requirements for Open-Source.",
            "type": "string",
            "format": "uri",
            "maxLength": 200,
            "nullable": true
          },
          "proxy_npmjs": {
            "title": "Proxy Npm Packages?",
            "description": "If checked, Npm packages that are not in the repository when requested by clients will automatically be proxied from the public npmjs.org registry. If there is at least one version for a package, others will not be proxied.",
            "type": "boolean"
          },
          "proxy_pypi": {
            "title": "Proxy Python Packages?",
            "description": "If checked, Python packages that are not in the repository when requested by clients will automatically be proxied from the public pypi.python.org registry. If there is at least one version for a package, others will not be proxied.",
            "type": "boolean"
          },
          "raw_package_index_enabled": {
            "title": "Serve index for raw packages?",
            "description": "If checked, HTML and JSON indexes will be generated that list all available raw packages in the repository.",
            "type": "boolean"
          },
          "raw_package_index_signatures_enabled": {
            "title": "Display generated GPG signatures for the raw package index?",
            "description": "If checked, the HTML and JSON indexes will display raw package GPG signatures alongside the index packages.",
            "type": "boolean"
          },
          "replace_packages": {
            "title": "Replace packages",
            "description": "This defines the minimum level of privilege required for a user to republish packages. Unless the package was uploaded by that user, in which the permission may be overridden by the user-specific republish setting. Please note that the user still requires the privilege to delete packages that will be replaced by the new package; otherwise the republish will fail.",
            "type": "string",
            "enum": [
              "Admin",
              "Write"
            ],
            "default": "Write"
          },
          "replace_packages_by_default": {
            "title": "Replace packages by default",
            "description": "If checked, uploaded packages will overwrite/replace any others with the same attributes (e.g. same version) by default. This only applies if the user has the required privilege for the republishing AND has the required privilege to delete existing packages that they don't own.",
            "type": "boolean"
          },
          "repository_type_str": {
            "title": "Repository type str",
            "description": "The repository type changes how it is accessed and billed. Private repositories are visible only to you or authorized delegates. Public repositories are visible to all Cloudsmith users.",
            "type": "string",
            "enum": [
              "Public",
              "Private",
              "Open-Source"
            ],
            "default": "Public"
          },
          "resync_own": {
            "title": "Users Can Resync Own Packages",
            "description": "If checked, users can resync any of their own packages that they have uploaded, assuming that they still have write privilege for the repository. This takes precedence over privileges configured in the 'Access Controls' section of the repository, and any inherited from the org.",
            "type": "boolean"
          },
          "resync_packages": {
            "title": "Resync packages",
            "description": "This defines the minimum level of privilege required for a user to resync packages. Unless the package was uploaded by that user, in which the permission may be overridden by the user-specific resync setting.",
            "type": "string",
            "enum": [
              "Admin",
              "Write"
            ],
            "default": "Admin"
          },
          "scan_own": {
            "title": "Users Can Scan Own Packages",
            "description": "If checked, users can scan any of their own packages that they have uploaded, assuming that they still have write privilege for the repository. This takes precedence over privileges configured in the 'Access Controls' section of the repository, and any inherited from the org.",
            "type": "boolean"
          },
          "scan_packages": {
            "title": "Scan packages",
            "description": "This defines the minimum level of privilege required for a user to scan packages. Unless the package was uploaded by that user, in which the permission may be overridden by the user-specific scan setting.",
            "type": "string",
            "enum": [
              "Admin",
              "Write",
              "Read"
            ],
            "default": "Read"
          },
          "show_setup_all": {
            "title": "Always show Set Me Up for all formats?",
            "description": "If checked, the Set Me Up help for all formats will always be shown, even if you don't have packages of that type uploaded. Otherwise, help will only be shown for packages that are in the repository. For example, if you have uploaded only NuGet packages, then the Set Me Up help for NuGet packages will be shown only.",
            "type": "boolean"
          },
          "slug": {
            "title": "Slug",
            "description": "The slug identifies the repository in URIs.",
            "type": "string"
          },
          "storage_region": {
            "title": "Storage region",
            "description": "The Cloudsmith region in which package files are stored.",
            "type": "string",
            "default": "default"
          },
          "strict_npm_validation": {
            "title": "Strict Npm Validation?",
            "description": "If checked, npm packages will be validated strictly to ensure the package matches specifcation. You can turn this on if you want to guarantee that the packages will work with npm-cli and other tools correctly.",
            "type": "boolean"
          },
          "tag_pre_releases_as_latest": {
            "title": "Apply Latest Tag for Pre-Release Versions?",
            "description": "If checked, packages pushed with a pre-release component on that version will be marked with the 'latest' tag. Note that if unchecked, a repository containing ONLY pre-release versions, will have no version marked latest which may cause incompatibility with native tools ",
            "type": "boolean"
          },
          "use_debian_labels": {
            "title": "Use Debian Labels?",
            "description": "If checked, a 'Label' field will be present in Debian-based repositories. It will contain a string that identifies the entitlement token used to authenticate the repository, in the form of 'source=t-<identifier>'; or 'source=none' if no token was used. You can use this to help with pinning.",
            "type": "boolean"
          },
          "use_default_cargo_upstream": {
            "title": "Use crates.io as default Cargo upstream?",
            "description": "If checked, dependencies of uploaded Cargo crates which do not set an explicit value for \"registry\" will be assumed to be available from crates.io. If unchecked, dependencies with unspecified \"registry\" values will be assumed to be available in the registry being uploaded to. Uncheck this if you want to ensure that dependencies are only ever installed from Cloudsmith unless explicitly specified as belong to another registry.",
            "type": "boolean"
          },
          "use_entitlements_privilege": {
            "title": "Use entitlements privilege",
            "description": "This defines the minimum level of privilege required for a user to see/use entitlement tokens with private repositories. If a user does not have the permission, they will only be able to download packages using other credentials, such as email/password via basic authentication. Use this if you want to force users to only use their user-based token, which is tied to their access (if removed, they can't use it).",
            "type": "string",
            "enum": [
              "Admin",
              "Write",
              "Read"
            ],
            "default": "Read"
          },
          "use_noarch_packages": {
            "title": "Use/Configure NoArch Packages?",
            "description": "If checked, noarch packages (if supported) are enabled in installations/configurations. A noarch package is one that is not tied to specific system architecture (like i686).",
            "type": "boolean"
          },
          "use_source_packages": {
            "title": "Use/Configure Source Packages?",
            "description": "If checked, source packages (if supported) are enabled in installations/configurations. A source package is one that contains source code rather than built binaries.",
            "type": "boolean"
          },
          "use_vulnerability_scanning": {
            "title": "Use Vulnerability Scanning?",
            "description": "If checked, vulnerability scanning will be enabled for all supported packages within this repository.",
            "type": "boolean"
          },
          "user_entitlements_enabled": {
            "title": "User Entitlements Enabled",
            "description": "If checked, users can use and manage their own user-specific entitlement token for the repository (if private). Otherwise, user-specific entitlements are disabled for all users.",
            "type": "boolean"
          },
          "view_statistics": {
            "title": "View statistics",
            "description": "This defines the minimum level of privilege required for a user to view repository statistics, to include entitlement-based usage, if applicable. If a user does not have the permission, they won't be able to view any statistics, either via the UI, API or CLI.",
            "type": "string",
            "enum": [
              "Admin",
              "Write",
              "Read"
            ],
            "default": "Read"
          }
        }
      },
      "RepositoryCreate": {
        "required": [
          "name"
        ],
        "type": "object",
        "properties": {
          "broadcast_state": {
            "title": "Broadcast state",
            "description": "Broadcasting status of a repository.",
            "type": "string",
            "enum": [
              "Off",
              "Private",
              "Internal",
              "Public",
              "Open-Source"
            ],
            "default": "Off"
          },
          "cdn_url": {
            "title": "Cdn url",
            "description": "Base URL from which packages and other artifacts are downloaded.",
            "type": "string",
            "readOnly": true,
            "nullable": true
          },
          "content_kind": {
            "title": "Content kind",
            "description": "The repository content kind determines whether this repository contains packages, or provides a distribution of packages from other repositories. You can only select the content kind at repository creation time.",
            "type": "string",
            "enum": [
              "Standard",
              "Distribution",
              "Upstream"
            ],
            "default": "Standard"
          },
          "contextual_auth_realm": {
            "title": "Contextual Authentication Realm?",
            "description": "If checked, missing credentials for this repository where basic authentication is required shall present an enriched value in the 'WWW-Authenticate' header containing the namespace and repository. This can be useful for tooling such as SBT where the authentication realm is used to distinguish and disambiguate credentials.",
            "type": "boolean"
          },
          "copy_own": {
            "title": "Users Can Copy Own Packages",
            "description": "If checked, users can copy any of their own packages that they have uploaded, assuming that they still have write privilege for the repository. This takes precedence over privileges configured in the 'Access Controls' section of the repository, and any inherited from the org.",
            "type": "boolean"
          },
          "copy_packages": {
            "title": "Copy packages",
            "description": "This defines the minimum level of privilege required for a user to copy packages. Unless the package was uploaded by that user, in which the permission may be overridden by the user-specific copy setting.",
            "type": "string",
            "enum": [
              "Admin",
              "Write",
              "Read"
            ],
            "default": "Read"
          },
          "cosign_signing_enabled": {
            "title": "Cosign Signing Enabled?",
            "description": "When enabled, all pushed (or pulled from upstream) OCI packages and artifacts will be signed using cosign with the repository's ECDSA key. This generates a distinct cosign signature artifact per artifact.",
            "type": "boolean"
          },
          "created_at": {
            "title": "Created at",
            "type": "string",
            "format": "date-time",
            "readOnly": true
          },
          "default_privilege": {
            "title": "Default privilege",
            "description": "This defines the default level of privilege that all of your organization members have for this repository. This does not include collaborators, but applies to any member of the org regardless of their own membership role (i.e. it applies to owners, managers and members). Be careful if setting this to admin, because any member will be able to change settings.",
            "type": "string",
            "enum": [
              "Admin",
              "Write",
              "Read",
              "None"
            ],
            "default": "None"
          },
          "delete_own": {
            "title": "Users Can Delete Own Packages",
            "description": "If checked, users can delete any of their own packages that they have uploaded, assuming that they still have write privilege for the repository. This takes precedence over privileges configured in the 'Access Controls' section of the repository, and any inherited from the org.",
            "type": "boolean"
          },
          "delete_packages": {
            "title": "Delete packages",
            "description": "This defines the minimum level of privilege required for a user to delete packages. Unless the package was uploaded by that user, in which the permission may be overridden by the user-specific delete setting.",
            "type": "string",
            "enum": [
              "Admin",
              "Write"
            ],
            "default": "Admin"
          },
          "deleted_at": {
            "title": "Deleted at",
            "description": "The datetime the repository was manually deleted at.",
            "type": "string",
            "format": "date-time",
            "readOnly": true,
            "nullable": true
          },
          "description": {
            "title": "Description",
            "description": "A description of the repository's purpose/contents.",
            "type": "string"
          },
          "distributes": {
            "description": "The repositories distributed through this repo. Adding repos here is only valid if the content_kind is DISTRIBUTION.",
            "type": "array",
            "items": {
              "description": "The repositories distributed through this repo. Adding repos here is only valid if the content_kind is DISTRIBUTION.",
              "type": "string",
              "format": "slug",
              "pattern": "^[-a-zA-Z0-9_]+$"
            },
            "uniqueItems": true
          },
          "docker_refresh_tokens_enabled": {
            "title": "Docker Auth Refresh Enabled?",
            "description": "If checked, refresh tokens will be issued in addition to access tokens for Docker authentication. This allows unlimited extension of the lifetime of access tokens.",
            "type": "boolean"
          },
          "ecdsa_keys": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/RepositoryEcdsaKey"
            },
            "readOnly": true
          },
          "enforce_eula": {
            "title": "Require EULA acceptance for downloads?",
            "description": "If checked, downloads will explicitly require acceptance of an EULA.",
            "type": "boolean"
          },
          "generic_package_index_enabled": {
            "title": "Serve index for generic packages?",
            "description": "If checked, HTML indexes will be generated that list all available generic packages in the repository.",
            "type": "boolean"
          },
          "gpg_keys": {
            "type": "array",
            "items": {
              "$ref": "#/components/schemas/RepositoryGpgKey"
            },
            "readOnly": true
          },
          "index_files": {
            "title": "Index Files?",
            "description": "If checked, files contained in packages will be indexed, which increase the synchronisation time required for packages. Note that it is recommended you keep this enabled unless the synchronisation time is significantly impacted.",
            "type": "boolean"
          },
          "is_open_source": {
            "title": "Is open source",
            "type": "boolean",
            "readOnly": true
          },
          "is_private": {
            "title": "Is private",
            "type": "boolean",
            "readOnly": true
          },
          "is_public": {
            "title": "Is public",
            "type": "boolean",
            "readOnly": true
          },
          "manage_entitlements_privilege": {
            "title": "Manage entitlements privilege",
            "description": "This defines the minimum level of privilege required for a user to manage entitlement tokens with private repositories. Management is the ability to create, alter, enable, disable or delete all tokens without a repository.",
            "type": "string",
            "enum": [
              "Admin",
              "Write",
              "Read"
            ],
            "default": "Admin"
          },
          "move_own": {
            "title": "Users Can Move Own Packages",
            "description": "If checked, users can move any of their own packages that they have uploaded, assuming that they still have write privilege for the repository. This takes precedence over privileges configured in the 'Access Controls' section of the repository, and any inherited from the org.",
            "type": "boolean"
          },
          "move_packages": {
            "title": "Move packages",
            "description": "This defines the minimum level of privilege required for a user to move packages. Unless the package was uploaded by that user, in which the permission may be overridden by the user-specific move setting.",
            "type": "string",
            "enum": [
              "Admin",
              "Write",
              "Read"
            ],
            "default": "Admin"
          },
          "name": {
            "title": "Name",
            "description": "A descriptive name for the repository.",
            "type": "string",
            "pattern": "^\\w[\\w \\-'\\.\\/()]+$",
            "maxLength": 50,
            "minLength": 1
          },
          "namespace": {
            "title": "Namespace",
            "description": "Namespace to which this repository belongs.",
            "type": "string",
            "format": "slug",
            "pattern": "^[-a-zA-Z0-9_]+$",
            "readOnly": true
          },
          "namespace_url": {
            "title": "Namespace url",
            "description": "API endpoint where data about this namespace can be retrieved.",
            "type": "string",
            "format": "uri",
            "readOnly": true
          },
          "nuget_native_signing_enabled": {
            "title": "Nuget Native Signing Enabled?",
            "description": "When enabled, all pushed (or pulled from upstream) nuget packages and artifacts will be signed using the repository's X.509 RSA certificate. Additionally, the nuget RepositorySignature index will list all of the repository's signing certificates including the ones from configured upstreams.",
            "type": "boolean"
          },
          "num_downloads": {
            "title": "Num downloads",
            "description": "The number of downloads for packages in the repository.",
            "type": "integer",
            "readOnly": true
          },
          "num_policy_violated_packages": {
            "title": "Num policy violated packages",
            "description": "Number of packages with policy violations in a repository.",
            "type": "integer",
            "readOnly": true
          },
          "num_quarantined_packages": {
            "title": "Num quarantined packages",
            "description": "Number of quarantined packages in a repository.",
            "type": "integer",
            "readOnly": true
          },
          "open_source_license": {
            "title": "Open source license",
            "description": "The SPDX identifier of the open source license.",
            "type": "string",
            "nullable": true
          },
          "open_source_project_url": {
            "title": "Open-Source Project URL",
            "description": "The URL to the Open-Source project, used for validating that the project meets the requirements for Open-Source.",
            "type": "string",
            "format": "uri",
            "maxLength": 200,
            "nullable": true
          },
          "package_count": {
            "title": "Package count",
            "description": "The number of packages in the repository.",
            "type": "integer",
            "readOnly": true
          },
          "package_count_excl_subcomponents": {
            "title": "Package count excl subcomponents",
            "description": "The number of packages in the repository excluding subcomponents.",
            "type": "integer",
            "readOnly": true
          },
          "package_group_count": {
            "title": "Package group count",
            "description": "The number of groups in the repository.",
            "type": "integer",
            "readOnly": true
          },
          "proxy_npmjs": {
            "title": "Proxy Npm Packages?",
            "description": "If checked, Npm packages that are not in the repository when requested by clients will automatically be proxied from the public npmjs.org registry. If there is at least one version for a package, others will not be proxied.",
            "type": "boolean"
          },
          "proxy_pypi": {
            "title": "Proxy Python Packages?",
            "description": "If checked, Python packages that are not in the repository when requested by clients will automatically be proxied from the public pypi.python.org registry. If there is at least one version for a package, others will not be proxied.",
            "type": "boolean"
          },
          "raw_package_index_enabled": {
            "title": "Serve index for raw packages?",
            "description": "If checked, HTML and JSON indexes will be generated that list all available raw packages in the repository.",
            "type": "boolean"
          },
          "raw_package_index_signatures_enabled": {
            "title": "Display generated GPG signatures for the raw package index?",
            "description": "If checked, the HTML and JSON indexes will display raw package GPG signatures alongside the index packages.",
            "type": "boolean"
          },
          "replace_packages": {
            "title": "Replace packages",
            "description": "This defines the minimum level of privilege required for a user to republish packages. Unless the package was uploaded by that user, in which the permission may be overridden by the user-specific republish setting. Please note that the user still requires the privilege to delete packages that will be replaced by the new package; otherwise the republish will fail.",
            "type": "string",
            "enum": [
              "Admin",
              "Write"
            ],
            "default": "Write"
          },
          "replace_packages_by_default": {
            "title": "Replace packages by default",
            "description": "If checked, uploaded packages will overwrite/replace any others with the same attributes (e.g. same version) by default. This only applies if the user has the required privilege for the republishing AND has the required privilege to delete existing packages that they don't own.",
            "type": "boolean"
          },
          "repository_type": {
            "title": "Repository Type",
            "description": "The repository type changes how it is accessed and billed. Private repositories are visible only to you or authorized delegates. Open-Source repositories are always visible to everyone and are restricted by licensing, but are free to use and come with generous bandwidth/storage. You can only select Open-Source at repository creation time.",
            "type": "integer",
            "enum": [
              1,
              2,
              3
            ],
            "readOnly": true
          },
          "repository_type_str": {
            "title": "Repository type str",
            "description": "The repository type changes how it is accessed and billed. Private repositories are visible only to you or authorized delegates. Public repositories are visible to all Cloudsmith users.",
            "type": "string",
            "enum": [
              "Public",
              "Private",
              "Open-Source"
            ],
            "default": "Public"
          },
          "resync_own": {
            "title": "Users Can Resync Own Packages",
            "description": "If checked, users can resync any of their own packages that they have uploaded, assuming that they still have write privilege for the repository. This takes precedence over privileges configured in the 'Access Controls' section of the repository, and any inherited from the org.",
            "type": "boolean"
          },
          "resync_packages": {
            "title": "Resync packages",
            "description": "This defines the minimum level of privilege required for a user to resync packages. Unless the package was uploaded by that user, in which the permission may be overridden by the user-specific resync setting.",
            "type": "string",
            "enum": [
              "Admin",
              "Write"
            ],
            "default": "Admin"
          },
          "scan_own": {
            "title": "Users Can Scan Own Packages",
            "description": "If checked, users can scan any of their own packages that they have uploaded, assuming that they still have write privilege for the repository. This takes precedence over privileges configured in the 'Access Controls' section of the repository, and any inherited from the org.",
            "type": "boolean"
          },
          "scan_packages": {
            "title": "Scan packages",
            "description": "This defines the minimum level of privilege required for a user to scan packages. Unless the package was uploaded by that user, in which the permission may be overridden by the user-specific scan setting.",
            "type": "string",
            "enum": [
              "Admin",
              "Write",
              "Read"
            ],
            "default": "Read"
          },
          "self_html_url": {
            "title": "Self html url",
            "description": "Website URL for this repository.",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          },
          "self_url": {
            "title": "Self url",
            "description": "API endpoint where data about this repository can be retrieved.",
            "type": "string",
            "format": "uri",
            "readOnly": true
          },
          "self_webapp_url": {
            "title": "Self webapp url",
            "description": "Webapp URL for this repository.",
            "type": "string",
            "readOnly": true,
            "minLength": 1
          },
          "show_setup_all": {
            "title": "Always show Set Me Up for all formats?",
            "description": "If checked, the Set Me Up help for all formats will always be shown, even if you don't have packages of that type uploaded. Otherwise, help will only be shown for packages that are in the repository. For example, if you have uploaded only NuGet packages, then the Set Me Up help for NuGet packages will be shown only.",
            "type": "boolean"
          },
          "size": {
            "title": "Size",
            "description": "The calculated size of the repository.",
            "type": "integer",
            "readOnly": true
          },
          "size_str": {
            "title": "Size str",
            "description": "The calculated size of the repository (human readable).",
            "type": "string",
            "readOnly": true
          },
          "slug": {
            "title": "Slug",
            "description": "The slug identifies the repository in URIs.",
            "type": "string"
          },
          "slug_perm": {
            "title": "Slug perm",
            "description": "The slug_perm immutably identifies the repository. It will never change once a repository has been created.",
            "type": "string",
            "format": "slug",
            "pattern": "^[-a-zA-Z0-9_]+$",
            "readOnly": true,
            "minLength": 1
          },
          "storage_region": {
            "title": "Storage region",
            "description": "The Cloudsmith region in which package files are stored.",
            "type": "string",
            "default": "default"
          },
          "strict_npm_validation": {
            "title": "Strict Npm Validation?",
            "description": "If checked, npm packages will be validated strictly to ensure the package matches specifcation. You can turn this on if you want to guarantee that the packages will work with npm-cli and other tools correctly.",
            "type": "boolean"
          },
          "tag_pre_releases_as_latest": {
            "title": "Apply Latest Tag for Pre-Release Versions?",
            "description": "If checked, packages pushed with a pre-release component on that version will be marked with the 'latest' tag. Note that if unchecked, a repository containing ONLY pre-release versions, will have no version marked latest which may cause incompatibility with native tools ",
            "type": "boolean"
          },
          "use_debian_labels": {
            "title": "Use Debian Labels?",
            "description": "If checked, a 'Label' field will be present in Debian-based repositories. It will contain a string that identifies the entitlement token used to authenticate the repository, in the form of 'source=t-<identifier>'; or 'source=none' if no token was used. You can use this to help with pinning.",
            "type": "boolean"
          },
          "use_default_cargo_upstream": {
            "title": "Use crates.io as default Cargo upstream?",
            "description": "If checked, dependencies of uploaded Cargo crates which do not set an explicit value for \"registry\" will be assumed to be available from crates.io. If unchecked, dependencies with unspecified \"registry\" values will be assumed to be available in the registry being uploaded to. Uncheck this if you want to ensure that dependencies are only ever installed from Cloudsmith unless explicitly specified as belong to another registry.",
            "type": "boolean"
          },
          "use_entitlements_privilege": {
            "title": "Use entitlements privilege",
            "description": "This defines the minimum level of privilege required for a user to see/use entitlement tokens with private repositories. If a user does not have the permission, they will only be able to download packages using other credentials, such as email/password via basic authentication. Use this if you want to force users to only use their user-based token, which is tied to their access (if removed, they can't use it).",
            "type": "string",
            "enum": [
              "Admin",
              "Write",
              "Read"
            ],
            "default": "Read"
          },
          "use_noarch_packages": {
            "title": "Use/Configure NoArch Packages?",
            "description": "If checked, noarch packages (if supported) are enabled in installations/configurations. A noarch package is one that is not tied to specific system architecture (like i686).",
            "type": "boolean"
          },
          "use_source_packages": {
            "title": "Use/Configure Source Packages?",
            "description": "If checked, source packages (if supported) are enabled in installations/configurations. A source package is one that contains source code rather than built binaries.",
            "type": "boolean"
          },
          "use_vulnerability_scanning": {
            "title": "Use Vulnerability Scanning?",
            "description": "If checked, vulnerability scanning will be enabled for all supported packages within this repository.",
            "type": "boolean"
          },
          "user_entitlements_enabled": {
            "title": "User Entitlements Enabled",
            "description": "If checked, users can use and manage their own user-specific entitlement token for the repository (if private). Otherwise, user-specific entitlements are disabled for all users.",
            "type": "boolean"
          },
          "view_statistics": {
            "title": "View statistics",
            "description": "This defines the minimum level of privilege required for a user to view repository statistics, to include entitlement-based usage, if applicable. If a user does not have the permission, they won't be able to view any statistics, either via the UI, API or CLI.",
            "type": "string",
            "enum": [
              "Admin",
              "Write",
              "Read"
            ],
            "default": "Read"
          }
        }
      }
    }
  }
}
```