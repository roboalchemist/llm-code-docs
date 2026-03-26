# Source: https://docs.infrahub.app/schema-library/reference/azure.md

# Azure

This schema extension introduces cloud support for Microsoft Azure.

## Details[​](#details "Direct link to Details")

* **Dependencies:**
  * [base](/schema-library/reference/dcim.md)
* **Attribution:** [Rowan Coleman](https://www.linkedin.com/in/rowan-coleman-6a147156/)

## Nodes[​](#nodes "Direct link to Nodes")

### Location[​](#location "Direct link to Location")

* **Namespace:** Azure
* **Display Labels:** name\_\_value

#### Attributes[​](#attributes "Direct link to Attributes")

| name | description | kind | optional | default\_value | choices |
| ---- | ----------- | ---- | -------- | -------------- | ------- |
| name |             | Text |          |                |         |

### Tenant[​](#tenant "Direct link to Tenant")

* **Namespace:** Azure
* **Display Labels:** name\_\_value, tenant\_id\_\_value

#### Attributes[​](#attributes-1 "Direct link to Attributes")

| name       | description | kind | optional | default\_value | choices |
| ---------- | ----------- | ---- | -------- | -------------- | ------- |
| name       |             | Text |          |                |         |
| tenant\_id |             | Text |          |                |         |

#### Relationships[​](#relationships "Direct link to Relationships")

| name          | peer              | optional | cardinality | kind      |
| ------------- | ----------------- | -------- | ----------- | --------- |
| subscriptions | AzureSubscription |          | many        | Component |

### Subscription[​](#subscription "Direct link to Subscription")

* **Namespace:** Azure
* **Display Labels:** name\_\_value, subscription\_id\_\_value

#### Attributes[​](#attributes-2 "Direct link to Attributes")

| name             | description | kind | optional | default\_value | choices |
| ---------------- | ----------- | ---- | -------- | -------------- | ------- |
| name             |             | Text |          |                |         |
| subscription\_id |             | Text |          |                |         |

#### Relationships[​](#relationships-1 "Direct link to Relationships")

| name           | peer               | optional | cardinality | kind      |
| -------------- | ------------------ | -------- | ----------- | --------- |
| tenant         | AzureTenant        | False    | one         | Parent    |
| resourcegroups | AzureResourceGroup |          | many        | Component |

### ResourceGroup[​](#resourcegroup "Direct link to ResourceGroup")

* **Namespace:** Azure
* **Display Labels:** name\_\_value

#### Attributes[​](#attributes-3 "Direct link to Attributes")

| name | description | kind | optional | default\_value | choices |
| ---- | ----------- | ---- | -------- | -------------- | ------- |
| name |             | Text |          |                |         |

#### Relationships[​](#relationships-2 "Direct link to Relationships")

| name         | peer              | optional | cardinality | kind      |
| ------------ | ----------------- | -------- | ----------- | --------- |
| location     | AzureLocation     |          | one         | Attribute |
| subscription | AzureSubscription | False    | one         | Parent    |

### VirtualNetwork[​](#virtualnetwork "Direct link to VirtualNetwork")

* **Label:** Virtual Networks
* **Namespace:** Azure
* **Display Labels:** name\_\_value
* **Inherit From:** AzureResource

#### Relationships[​](#relationships-3 "Direct link to Relationships")

| name           | peer                      | optional | cardinality | kind      |
| -------------- | ------------------------- | -------- | ----------- | --------- |
| address\_space | BuiltinIPPrefix           |          | many        | Attribute |
| subnets        | AzureVirtualNetworkSubnet |          | many        | Component |

### VirtualNetworkSubnet[​](#virtualnetworksubnet "Direct link to VirtualNetworkSubnet")

* **Label:** Subnets
* **Namespace:** Azure
* **Display Labels:** name\_\_value

#### Attributes[​](#attributes-4 "Direct link to Attributes")

| name | description | kind | optional | default\_value | choices |
| ---- | ----------- | ---- | -------- | -------------- | ------- |
| name |             | Text |          |                |         |

#### Relationships[​](#relationships-4 "Direct link to Relationships")

| name              | peer                | optional | cardinality | kind      |
| ----------------- | ------------------- | -------- | ----------- | --------- |
| virtualnetwork    | AzureVirtualNetwork | False    | one         | Parent    |
| address\_prefixes | BuiltinIPPrefix     |          | many        | Attribute |

## Generics[​](#generics "Direct link to Generics")

### Resource[​](#resource "Direct link to Resource")

* **Label:** Azure
* **Namespace:** Azure

#### Attributes[​](#attributes-5 "Direct link to Attributes")

| name | description | kind | optional | default\_value | choices |
| ---- | ----------- | ---- | -------- | -------------- | ------- |
| name |             | Text |          |                |         |

#### Relationships[​](#relationships-5 "Direct link to Relationships")

| name          | peer               | optional | cardinality | kind      |
| ------------- | ------------------ | -------- | ----------- | --------- |
| location      | AzureLocation      |          | one         | Attribute |
| resourcegroup | AzureResourceGroup | False    | one         | Parent    |

## Code[​](#code "Direct link to Code")

```
version: '1.0'
generics:
- name: Resource
  namespace: Azure
  label: Azure
  include_in_menu: true
  attributes:
  - name: name
    kind: Text
  relationships:
  - name: location
    cardinality: one
    kind: Attribute
    peer: AzureLocation
  - name: resourcegroup
    cardinality: one
    peer: AzureResourceGroup
    kind: Parent
    optional: false
nodes:
- name: Location
  namespace: Azure
  menu_placement: AzureResource
  display_labels:
  - name__value
  attributes:
  - name: name
    kind: Text
- name: Tenant
  namespace: Azure
  menu_placement: AzureResource
  display_labels:
  - name__value
  - tenant_id__value
  attributes:
  - name: name
    kind: Text
  - name: tenant_id
    kind: Text
  relationships:
  - name: subscriptions
    cardinality: many
    peer: AzureSubscription
    kind: Component
- name: Subscription
  namespace: Azure
  menu_placement: AzureResource
  display_labels:
  - name__value
  - subscription_id__value
  attributes:
  - name: name
    kind: Text
  - name: subscription_id
    kind: Text
  relationships:
  - name: tenant
    cardinality: one
    peer: AzureTenant
    kind: Parent
    optional: false
  - name: resourcegroups
    cardinality: many
    peer: AzureResourceGroup
    kind: Component
- name: ResourceGroup
  namespace: Azure
  menu_placement: AzureResource
  display_labels:
  - name__value
  attributes:
  - name: name
    kind: Text
  relationships:
  - name: location
    cardinality: one
    kind: Attribute
    peer: AzureLocation
  - name: subscription
    cardinality: one
    peer: AzureSubscription
    kind: Parent
    optional: false
- name: VirtualNetwork
  label: Virtual Networks
  namespace: Azure
  menu_placement: AzureResource
  display_labels:
  - name__value
  inherit_from:
  - AzureResource
  relationships:
  - name: address_space
    cardinality: many
    kind: Attribute
    peer: BuiltinIPPrefix
  - name: subnets
    cardinality: many
    kind: Component
    peer: AzureVirtualNetworkSubnet
- name: VirtualNetworkSubnet
  label: Subnets
  namespace: Azure
  menu_placement: AzureResource
  include_in_menu: true
  display_labels:
  - name__value
  attributes:
  - name: name
    kind: Text
  relationships:
  - name: virtualnetwork
    cardinality: one
    peer: AzureVirtualNetwork
    kind: Parent
    optional: false
  - name: address_prefixes
    cardinality: many
    kind: Attribute
    peer: BuiltinIPPrefix
```
