# Source: https://developers.cash.app/cash-app-pay-partner-api/guides/technical-guides/api-fundamentals/requests/api-versioning.mdx

***

## stoplight-id: c7540c9ac61d4

# API Versioning

## API Versions

### Customer Request API

Current Version: **`v1`**

**API Versions:**

* **`v1`**
  * Status: Active; under continued development
  * Support Window (subject to change): January 1st, 2022 - March 1st, 2027
  * Accepting new developers

### Network API

Current Version: **`v1`**

**API Versions:**

* **`v1`**
  * Status: Active; under continued development
  * Support Window (subject to change): January 1st, 2022 - March 1st, 2027
  * Accepting new developers

* **`v0`**
  * Status: Deprecated
  * Support Window: August 1st, 2020 - December 31st, 2022
  * Not accepting new developers

### Management API

Current Version: **`v1`**

**API Versions:**

* **`v1`**
  * Status: Active; under continued development
  * Support Window (subject to change): January 1st, 2022 - March 1st, 2027
  * Accepting new developers

***

## Version Statuses

API Versions can be in one of 5 statuses:

* **Active**: The API is actively serving traffic and receiving new features from patch updates
* **In development**: The API is currently being built and is not available for public use
* **Maintenance**: The API is actively serving traffic, but is no longer receiving new features
* **Deprecated**: The API is within a year of being retired, and should no longer be adopted by new integrations. Existing integrations should plan to migrate to a newer API version.
* **Retired**: The API is no longer serving traffic.

Support window refers to the period in which the API will serve traffic.

## How to select an API version

The Cash App Pay API uses **path-based versioning**. Every API call is required to specify a version, which can be done by providing it in the URL path  after the name of the API suite you're calling:

**Network API**

```
Format: https://api.cash.app/network/v<Major.Minor>
Example: https://api.cash.app/network/v1
```

**Customer Request API**

```
Format: https://api.cash.app/customer-request/v<Major.Minor>
Example: https://api.cash.app/customer-request/v1
```

Each API suite is versioned independently.

## Types of changes between versions

There are 3 types of changes Cash App Pay makes to the API, some of which are versioned:

* Major (breaking) changes
* Minor changes
* Patches

### Major Version Changes

Major versions introduce new features or functionality in a non-backwards-compatible way, and / or remove existing functionality. They require modifying business logic in the integration to adopt.

Examples of changes in major version updates:

* Removing an endpoint
* Removing a field from a request or response
* Making a response field optional that was previously required
* Removing a country code from the list of supported countries

### Minor Version Changes

Minor versions introduce new features or functionality that are generally backwards-compatible, but may require modifying a small amount of business logic in the integration.

Examples of changes in minor version updates:

* Adding a new country code to the list of supported countries
* Adding a new state to a resource with a state machine (for example, a new payment state)

### Patches

Patches introduce new features or functionality that are guaranteed to be 100% backwards-compatible with existing integrations. Patches are **non-versioned**, and will routinely be applied by the Cash App Pay engineering team.

Examples of patches:

* Adding a new "notes" field to payments that allows an API client to add details about a payment that are shown in the Cash App mobile application
* Adding a new endpoint for listing customer requests
