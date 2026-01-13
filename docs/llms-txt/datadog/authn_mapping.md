# Source: https://docs.datadoghq.com/account_management/authn_mapping.md

---
title: Federated Authentication to Role Mapping API
description: >-
  Automatically map identity provider groups to Datadog roles using the
  Authentication Mapping API for federated authentication systems.
breadcrumbs: Docs > Account Management > Federated Authentication to Role Mapping API
source_url: https://docs.datadoghq.com/authn_mapping/index.html
---

# Federated Authentication to Role Mapping API

If you are using Federated Authentication mechanisms, this API allows you to automatically map groups of users to roles in Datadog using attributes sent from your Identity Provider. To create and manage Authentication Mappings through the API, users need to use an application key owned by someone with the Access Management permission.

**Note**: If you are a SAML user, Datadog strongly recommends that you transition to using this API.

You can also create and manage mappings in the Datadog UI, on the **Mappings** tab in User Management. See [SAML group mapping](https://docs.datadoghq.com/account_management/saml/mapping) for more information.

## Requests{% #requests %}

All the API endpoints below are using the following host endpoint:

- `https://api.  /api/` for your Datadog region.

### Create a new authentication mapping{% #create-a-new-authentication-mapping %}

Create a new AuthN Mapping from a JSON body. Returns the newly created AuthN Mapping.

| Method | Endpoint path        | Required payload |
| ------ | -------------------- | ---------------- |
| `POST` | `/v2/authn_mappings` | JSON             |

##### ARGUMENTS{% #arguments %}

- **`role["data"]["id"]`** [*required*, no default]: The `ID` of the Role to map to. The Roles API can be used to create and manage Datadog roles, what global permissions they grant, and which users belong to them. **Note**: This attribute should be presented as part of a `role` relationship block in requests. See the example below for more details. When you create a Role, it is assigned an ID. For more information about finding the `ID` for the role you want to map to, see the [Role API documentation](https://docs.datadoghq.com/api/v2/roles/#list-roles).
- **`attributes["attribute_key"]`** [*required*, no default]: The `attribute_key` is the key portion of a key/value pair that represents an attribute sent from your Identity Provider. You can define these for your own use case. For example, `attribute_key` could be `member-of` and the `attribute_value` could be `Development`.
- **`attributes["attribute_value"]`** [*required*, no default]: The `attribute_value` is the value portion of a key/value pair that represents an attribute sent from your Identity Provider. You can define these for your own use case. For example, `attribute_key` could be `member-of` and the `attribute_value` could be `Development`.

{% tab title="Example" %}

```sh
curl -X POST \
    "https://api.<YOUR_DD_SITE>/api/v2/authn_mappings" \
    -H "Content-Type: application/json" \
    -H "DD-API-KEY: <YOUR_DATADOG_API_KEY>" \
    -H "DD-APPLICATION-KEY: <YOUR_DATADOG_APPLICATION_KEY>" \
    -d '{
            "data": {
                "type": "authn_mappings",
                "attributes": {
                    "attribute_key": "member-of",
                    "attribute_value": "Development"
                },
                "relationships": {
                    "role": {
                        "data": {
                            "id": "123e4567-e89b-12d3-a456-426655445555",
                            "type": "roles"
                        }
                    }
                }
            }
        }'
```

- Replace `<YOUR_DATADOG_API_KEY>` and `<YOUR_DATADOG_APPLICATION_KEY>` with the corresponding [API and application keys](https://api.datadoghq.com/account/settings#api) for your organization.
- Replace `<YOUR_DD_SITE>` with

{% /tab %}

{% tab title="Response" %}

```json
{
    "data": {
        "attributes": {
            "created_at": "2019-11-04 17:41:29.015504",
            "modified_at": "2019-11-04 17:41:29.015504",
            "role_uuid": "00000000-0000-0000-0000-000000000000",
            "saml_assertion_attribute_id": 0
        },
        "type": "authn_mappings",
        "id": "123e4567-e89b-12d3-a456-426655440000",
        "relationships": {
            "saml_assertion_attribute": {
                "data": {
                    "id": 0,
                    "type": "saml_assertion_attributes"
                }
            },
            "role": {
                "data": {
                    "id": "123e4567-e89b-12d3-a456-426655440000",
                    "type": "roles"
                }
            }
        }
    },
    "included": [
        {
            "data": {
                "id": "123e4567-e89b-12d3-a456-426655440000",
                "type": "roles",
                "attributes": {
                    "created_at": "2019-11-04 17:41:29.015504",
                    "modified_at": "2019-11-06 17:41:29.015504",
                    "name": "Developer Role"
                },
                "relationships": {
                    "permissions": {
                        "data": [
                            {
                                "id": "123e4567-e89b-12d3-a456-426655441000",
                                "type": "permissions"
                            }
                        ]
                    }
                }
            }
        },
        {
            "data": {
                "id": 6,
                "type": "saml_assertion_attributes",
                "attributes": {
                    "id": 6,
                    "attribute_key": "member-of",
                    "attribute_value": "Development"
                }
            }
        }
    ]
}
```

{% /tab %}

### Get all AuthN mappings{% #get-all-authn-mappings %}

Returns a list of AuthN Mappings

| Method | Endpoint path        | Required payload          |
| ------ | -------------------- | ------------------------- |
| `GET`  | `/v2/authn_mappings` | Optional query parameters |

##### ARGUMENTS{% #arguments-1 %}

- **`sort`** [*optional*, *default*=**created\_at**]: Sort attribute and directionâdefaults to ascending order, `-<attribute>` sorts in descending order. Can also sort on relationship attributes `role.name`, `saml_assertion_attribute.attribute_key`, `saml_assertion_attribute.attribute_value`.
- **`page[number]`** [*optional*, *default*=**0**, *minimum*=**0**]: The page of results to return.
- **`page[size]`** [*optional*, *default*=**10**]: The number of results to return on each page.
- **`filter`** [*optional*, default=none]: Filter by tags as strings. For example, `Billing Users`.

{% tab title="Example" %}

```sh
curl -X GET "https://api.<YOUR_DD_SITE>/api/v2/authn_mappings" \
     -H "DD-API-KEY: <YOUR_DATADOG_API_KEY>" \
     -H "DD-APPLICATION-KEY: <YOUR_DATADOG_APPLICATION_KEY>"
```

- Replace `<YOUR_DATADOG_API_KEY>` and `<YOUR_DATADOG_APPLICATION_KEY>` with the corresponding [API and application keys](https://api.datadoghq.com/account/settings#api) for your organization.
- Replace `<YOUR_DD_SITE>` with

{% /tab %}

{% tab title="Response" %}

```json
{
    "data": [
      {
        "type": "authn_mapping",
        "id": "123e4567-e89b-12d3-a456-426655440000",
        "relationships": {
          "saml_assertion_attribute": {
            "data": {"id": 0, "type": "saml_assertion_attributes"}
          },
          "role": {
            "data": {
              "id": "123e4567-e89b-12d3-a456-426655440000",
              "type": "roles"
            }
          }
        },
        "attributes": {
          "created_at": "2019-11-04 17:41:29.015504",
          "modified_at": "2019-11-04 17:41:29.015504",
          "saml_assertion_attribute_id": 0
        }
      }
    ],
    "included": [
      {
        "data": {
          "id": "123e4567-e89b-12d3-a456-426655440000",
          "type": "roles",
          "attributes": {
            "created_at": "2019-11-04 17:41:29.015504",
            "modified_at": "2019-11-06 17:41:29.015504",
            "name": "Developer Role"
          },
          "relationships": {
            "permissions": {
                "data": [
                  {
                    "id": "123e4567-e89b-12d3-a456-426655440000",
                    "type": "permissions"
                  }
                ]
            }
          }
        }
      },
      {
        "data": {
          "id": 6,
          "type": "saml_assertion_attributes",
          "attributes": {
            "id": 6,
            "attribute_key": "member-of",
            "attribute_value": "Developer"
          }
        }
      }
    ],
    "meta": {
      "page": {
        "total_count": 1,
        "total_filtered_count": 1,
      }
    }
}
```

{% /tab %}

### Get a specific AuthN mapping{% #get-a-specific-authn-mapping %}

Returns a specific AuthN Mapping by UUID.

| Method | Endpoint path                        | Required payload |
| ------ | ------------------------------------ | ---------------- |
| `GET`  | `/authn_mappings/{authn_mapping_id}` | URL parameter    |

##### ARGUMENTS{% #arguments-2 %}

- **`{authn_mapping_id}`** [*required*, no default]: Replace `{authn_mapping_id}` with the ID of the AuthN Mapping you want to view.

{% tab title="Example" %}

```sh
curl -X GET "https://api.<YOUR_DD_SITE>/api/v2/authn_mappings/{authn_mapping_id}" \
     -H "DD-API-KEY: <YOUR_DATADOG_API_KEY>" \
     -H "DD-APPLICATION-KEY: <YOUR_DATADOG_APPLICATION_KEY>"
```

- Replace `<YOUR_DATADOG_API_KEY>` and `<YOUR_DATADOG_APPLICATION_KEY>` with the corresponding [API and application keys](https://api.datadoghq.com/account/settings#api) for your organization.
- Replace `<YOUR_DD_SITE>` with

{% /tab %}

{% tab title="Response" %}

```json
{
    "data": {
        "attributes": {
            "created_at": "2019-11-04 17:41:29.015504",
            "modified_at": "2019-11-04 17:41:29.015504",
            "uuid": "123e4567-e89b-12d3-a456-426655440000",
            "saml_assertion_attribute_id": 0
        },
        "type": "authn_mappings",
        "id": "123e4567-e89b-12d3-a456-426655440000",
        "relationships": {
            "saml_assertion_attribute": {
                "data": {
                    "id": 0,
                    "type": "saml_assertion_attributes"
                }
            },
            "role": {
                "data": {
                    "id": "123e4567-e89b-12d3-a456-426655440000",
                    "type": "roles"
                }
            }
        }
    },
    "included": [
        {
            "data": {
                "id": "123e4567-e89b-12d3-a456-426655440000",
                "type": "roles",
                "attributes": {
                    "created_at": "2019-11-04 17:41:29.015504",
                    "modified_at": "2019-11-06 17:41:29.015504",
                    "uuid": "123e4567-e89b-12d3-a456-426655440000",
                    "name": "Developer Role"
                },
                "relationships": {
                    "permissions": {
                        "data": [
                            {
                                "id": "123e4567-e89b-12d3-a456-426655440000",
                                "type": "permissions"
                            }
                        ]
                    }
                }
            }
        },
        {
            "data": {
                "id": 6,
                "type": "saml_assertion_attributes",
                "attributes": {
                    "id": 6,
                    "attribute_key": "member-of",
                    "attribute_value": "Developer"
                }
            }
        }
    ]
}
```

{% /tab %}

### Update mapping{% #update-mapping %}

Updates the AuthN Mapping `role`, `saml_assertion_attribute_id`, or both from a JSON body. Returns the updated AuthN Mapping.

| Method  | Endpoint path                           | Required payload    |
| ------- | --------------------------------------- | ------------------- |
| `PATCH` | `/v2/authn_mappings/{authn_mapping_id}` | URL parameter, JSON |

##### ARGUMENTS{% #arguments-3 %}

- **`{authn_mapping_id}`** [*required*, no default]: Replace `{authn_mapping_id}` with the ID of the AuthN Mapping you want to update. This is required in both the path of the request and the body of the request.
- **`role["data"]["id"]`** [*optional*, *default*=none]: The `ID` of the Role to map to. The Roles API can be used to create and manage Datadog roles, what global permissions they grant, and which users belong to them. **Note**: This attribute should be presented as part of a `role` relationship block in requests. See the example below for more details. When you create a Role, it is assigned an ID. For more information about finding the `ID` for the role you want to map to, see the [Role API documentation](https://docs.datadoghq.com/api/v2/roles/#list-roles).
- **`attributes["attribute_key"]`** [*optional*, *default*=none]: The `attribute_key` is the key portion of a key/value pair that represents an attribute sent from your Identity Provider. You can define these for your own use case. For example, `attribute_key` could be `member-of` and the `attribute_value` could be `Development`.
- **`attributes["attribute_value"]`** [*optional*, *default*=none]: The `attribute_value` is the value portion of a key/value pair that represents an attribute sent from your Identity Provider. You can define these for your own use case. For example, `attribute_key` could be `member-of` and the `attribute_value` could be `Development`.

{% tab title="Example" %}

```sh
curl -X PATCH \
    "https://api.<YOUR_DD_SITE>/api/v2/authn_mappings/{UUID}" \
    -H "Content-Type: application/json" \
    -H "DD-API-KEY: <YOUR_DATADOG_API_KEY>" \
    -H "DD-APPLICATION-KEY: <YOUR_DATADOG_APPLICATION_KEY>" \
    -d '{
            "data": {
                "type": "authn_mappings",
                "id": "{authn_mapping_id}",
                "attributes": {
                    "attribute_key": "member-of",
                    "attribute_value": "Developer"
                }
                "relationships": {
                "role": {
                    "data": {
                            "id": "123e4567-e89b-12d3-a456-426655440000",
                            "type": "roles"
                        }
                    }
                }
            }
        }'
```

- Replace `<YOUR_DATADOG_API_KEY>` and `<YOUR_DATADOG_APPLICATION_KEY>` with the corresponding [API and application keys](https://api.datadoghq.com/account/settings#api) for your organization.
- Replace `<YOUR_DD_SITE>` with

{% /tab %}

{% tab title="Response" %}

```json
{
    "data": {
        "attributes": {
            "created_at": "2019-11-04 17:41:29.015504",
            "modified_at": "2019-11-04 17:41:29.015504",
            "saml_assertion_attribute_id": 0
        },
        "type": "authn_mappings",
        "id": "123e4567-e89b-12d3-a456-426655440000",
        "relationships": {
            "saml_assertion_attribute": {
                "data": {
                    "id": 0,
                    "type": "saml_assertion_attributes"
                }
            },
            "role": {
                "data": {
                    "id": "123e4567-e89b-12d3-a456-426655440000",
                    "type": "roles"
                }
            }
        }
    },
    "included": [
        {
            "data": {
                "id": "123e4567-e89b-12d3-a456-426655440000",
                "type": "roles",
                "attributes": {
                    "created_at": "2019-11-04 17:41:29.015504",
                    "modified_at": "2019-11-06 17:41:29.015504",
                    "uuid": "123e4567-e89b-12d3-a456-426655440000",
                    "name": "Developer Role"
                },
                "relationships": {
                    "data": [
                        {
                            "id": "123e4567-e89b-12d3-a456-426655440000",
                            "type": "permissions"
                        }
                    ]
                }
            }
        },
        {
            "data": {
                "id": 6,
                "type": "saml_assertion_attributes",
                "attributes": {
                    "id": 6,
                    "attribute_key": "member-of",
                    "attribute_value": "Developer"
                }
            }
        }
    ]
}
```

{% /tab %}

### Delete mapping{% #delete-mapping %}

Deletes a specific AuthN Mapping.

| Method   | Endpoint path                           | Required payload |
| -------- | --------------------------------------- | ---------------- |
| `DELETE` | `/v2/authn_mappings/{authn_mapping_id}` | URL parameter    |

##### ARGUMENTS{% #arguments-4 %}

- **`{authn_mapping_id}`** [*required*, no default]: Replace `{authn_mapping_id}` with the ID of the AuthN Mapping you want to delete.

{% tab title="Example" %}

```sh
curl -X DELETE "https://api.<YOUR_DD_SITE>/api/v2/authn_mappings/{UUID}" \
         -H "Content-Type: application/json" \
         -H "DD-API-KEY: <YOUR_DATADOG_API_KEY>" \
         -H "DD-APPLICATION-KEY: <YOUR_DATADOG_APPLICATION_KEY>"
```

- Replace `<YOUR_DATADOG_API_KEY>` and `<YOUR_DATADOG_APPLICATION_KEY>` with the corresponding [API and application keys](https://api.datadoghq.com/account/settings#api) for your organization.
- Replace `<YOUR_DD_SITE>` with

{% /tab %}

{% tab title="Response" %}

```sh
HTTP/2 204
```

{% /tab %}

### Get AuthN mapping enablement{% #get-authn-mapping-enablement %}

Check whether AuthN Mappings are enabled or disabled.

| Method | Endpoint path         | Required payload |
| ------ | --------------------- | ---------------- |
| `GET`  | `/v1/org_preferences` | None             |

{% tab title="Example" %}

```sh
curl -X GET \
         "https://api.<YOUR_DD_SITE>/api/v1/org_preferences" \
         -H "Content-Type: application/json" \
         -H "DD-API-KEY: <YOUR_DATADOG_API_KEY>" \
         -H "DD-APPLICATION-KEY: <YOUR_DATADOG_APPLICATION_KEY>" \
```

- Replace `<YOUR_DATADOG_API_KEY>` and `<YOUR_DATADOG_APPLICATION_KEY>` with the corresponding [API and application keys](https://api.datadoghq.com/account/settings#api) for your organization.
- Replace `<YOUR_DD_SITE>` with

{% /tab %}

{% tab title="Response" %}

```json
{
  "data": {
    "attributes": {
        "preference_data": "saml_authn_mapping_roles",
        "preference_type": true
    },
    "type": "org_preferences",
    "id": 1,
  },
}
```

{% /tab %}

### Enable or disable all mappings{% #enable-or-disable-all-mappings %}

{% alert level="danger" %}
When mappings are enabled, all users logging in with SAML are stripped of their roles and reassigned roles based on the values in their SAML assertion. It's important to confirm you are receiving the expected SAML assertions in your login before enabling the mapping enforcement.
{% /alert %}

Enables/disables the enforcement of all AuthN Mappings.

| Method | Endpoint path         | Required payload |
| ------ | --------------------- | ---------------- |
| `POST` | `/v1/org_preferences` | JSON             |

##### ARGUMENTS{% #arguments-5 %}

- **`{preference_type}`** [*required*, no default]: Preference to update, required to be "saml_authn_mapping_roles"
- **`{preference_data}`** [*required*, no default]: Data to update preference with, must be true or false: true to enable all mappings, false to disable

{% tab title="Example" %}

```sh
curl -X POST \
    "https://api.<YOUR_DD_SITE>/api/v1/org_preferences" \
    -H "Content-Type: application/json" \
    -H "DD-API-KEY: <YOUR_DATADOG_API_KEY>" \
    -H "DD-APPLICATION-KEY: <YOUR_DATADOG_APPLICATION_KEY>" \
    -d '{
        "data": {
            "type": "org_preferences",
            "attributes": {
                "preference_type": "saml_authn_mapping_roles",
                "preference_data": true
            }
        }
    }'
`
```

- Replace `<YOUR_DATADOG_API_KEY>` and `<YOUR_DATADOG_APPLICATION_KEY>` with the corresponding [API and application keys](https://api.datadoghq.com/account/settings#api) for your organization.
- Replace `<YOUR_DD_SITE>` with

{% /tab %}

{% tab title="Response" %}

```json
{
  "data": {
    "attributes": {
        "preference_type": "saml_authn_mapping_roles",
        "preference_data": true
    },
    "type": "org_preferences",
    "id": 1,
  },
}
```

{% /tab %}

## Further Reading{% #further-reading %}

- [RBAC for Log Management](https://docs.datadoghq.com/account_management/rbac/log_management/)
