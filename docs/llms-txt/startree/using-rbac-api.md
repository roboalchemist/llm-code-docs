# Source: https://docs.startree.ai/corecapabilities/security/using-rbac-api.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://docs.startree.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Using the StarTree Role-Based Access Control (RBAC) API

> Configure using the RBAC Manager API. RBAC allows you to define granular permissions for users, groups, and service tokens.

## Prerequisites

* You need an Authorization Bearer token to invoke these APIs. See
  [Generating an API Token](./manage-api-tokens#generating-an-api-token).
* Once RBAC is enabled, all access is governed by the roles and  policies you set up. Ensure you assign appropriate admin privileges if needed.

## Core RBAC Setup Process

Setting up RBAC generally involves these four steps:

1. **Create a Policy:** Define *what* actions are allowed or denied on *which* resources.
2. **Create a Role:** Create a role entity that will group permissions.
3. **Attach Policy to Role:** Link the policy (permissions) to the role.
4. **Assign Role to Subject:** Grant the role (and its associated permissions) to users, groups, domains, or service tokens.

Once these steps are completed, access control will be enforced based on your configuration.

## Listing and Viewing Policies

Before creating a new policy, it's often helpful to see which policies already exist in your environment.

1. Start by [retrieving the list of policies](#listing-all-policies) using the `GET /api/v1/rbac-manager/policies` endpoint.
2. For any policy that you want to examine in more detail, [get the policy definition](#viewing-a-specific-policy) using the `GET /api/v1/rbac-manager/policies/{policySrn}` API.

You can then decide whether to [update an existing policy](#updating-a-policy) or [create a new policy](#creating-a-policy).

## Working with Policies

This section covers how to list, view, create, update, and delete policies.

### Listing All Policies

To get a list of all defined policies, use the following API endpoint:

**API Endpoint:**

```
GET /api/v1/rbac-manager/policies
```

**Example CURL Command:**

```bash  theme={null}
curl --location --request GET 'https://rbac-manager.<Your-URL>.startree.cloud/api/v1/rbac-manager/policies' \
--header 'Authorization: Bearer <Token>'
```

**Response:**
A list of policy summaries, each including the policy's name and its SRN (StarTree Resource Name).

### Viewing a Specific Policy

To view the full details of a single policy, including its description and the policy document JSON, use this endpoint:

**API Endpoint:**

```
GET /api/v1/rbac-manager/policies/{policySrn}
```

**Example CURL Command:**

```bash  theme={null}
curl --location --request GET 'https://rbac-manager.<Your-URL>.startree.cloud/api/v1/rbac-manager/policies/srn2:policy%23<Policy-Name>' \
--header 'Authorization: Bearer <Token>'
```

> *`Replace <Policy-Name> with the name part of the policy's SRN`*

**Response:**
The complete details for the specified policy, including its name, description, the policy document JSON, creation timestamp, and last update timestamp.

### Creating a Policy

Use this endpoint to create a policy:

**API Endpoint:**

```
POST /api/v1/rbac-manager/policies
```

**Example CURL Command:**

```bash  theme={null}
curl --location --request POST 'https://rbac-manager.<Your-URL>.startree.cloud/api/v1/rbac-manager/policies' \
--header 'Authorization: Bearer <Token>' \
--header 'Content-Type: application/json' \
--data '{
  "name": "my-read-only-policy",
  "description": "Policy allowing query on myTable",
  "policyDocumentJson": "{
    \"version\": \"v1\",
    \"statements\": [
      {
        \"effect\": \"allow\",
        \"actions\": [\"query\"],
        \"resources\": [\"srn2:cluster#*:table#myTable\"]
      }
    ]
  }"
}'
```

**Policy Document:** This JSON defines the permissions. It contains statements with effect (allow/deny), actions (e.g., "query", "\*"), and resources (e.g., "srn2:cluster#\*", "srn2:cluster#\*:table#myTable").

See the [custom policies documentation](/corecapabilities/security/custom-policies) for syntax details, examples, and additional information.

### Updating a Policy

Use this endpoint to update an existing policy:

**API Endpoint:**

```
PUT /api/v1/rbac-manager/policies/{policySrn}
```

**Example CURL Command:**

```bash  theme={null}
curl --location --request PUT 'https://rbac-manager.<Your-URL>.startree.cloud/api/v1/rbac-manager/policies/srn2:policy%23<Policy-Name>' \
--header 'Authorization: Bearer <Token>' \
--header 'Content-Type: application/json' \
--data '{
  "description": "Updated policy description",
  "policyDocumentJson": "{
    \"version\": \"v1\",
    \"statements\": [
      {
        \"effect\": \"allow\",
        \"actions\": [\"query\", \"read\"],
        \"resources\": [\"srn2:cluster#*:table#myTable\"]
      }
    ]
  }"
}'
```

### Deleting a Policy

Use this endpoint to delete a policy:

**API Endpoint:**

```
DELETE /api/v1/rbac-manager/policies/{policySrn}
```

**Example CURL Command:**

```bash  theme={null}
curl --location --request DELETE 'https://rbac-manager.<Your-URL>.startree.cloud/api/v1/rbac-manager/policies/srn2:policy%23<Policy-Name>' \
--header 'Authorization: Bearer <Token>'
```

<Note>
  A policy cannot be deleted if it is associated with a role.
</Note>

## Working with Roles

This section covers how to create, list, view, and delete roles.

### Creating a Role

Use this endpoint to create a role:

**API Endpoint:**

```
POST /api/v1/rbac-manager/roles
```

**Example CURL Command:**

```bash  theme={null}
curl --location --request POST 'https://rbac-manager.<Your-URL>.startree.cloud/api/v1/rbac-manager/roles' \
--header 'Authorization: Bearer <Token>' \
--header 'Content-Type: application/json' \
--data '{
  "name": "table-reader-role",
  "description": "Provides read-only access to specific tables."
}'
```

### Listing All Roles

Use this endpoint to list all roles:

**API Endpoint:**

```
GET /api/v1/rbac-manager/roles
```

**Example CURL Command:**

```bash  theme={null}
curl --location --request GET 'https://rbac-manager.<Your-URL>.startree.cloud/api/v1/rbac-manager/roles' \
--header 'Authorization: Bearer <Token>'
```

### Getting Role Details

Use this endpoint to get details for a specific role:

**API Endpoint:**

```
GET /api/v1/rbac-manager/roles/{roleSrn}
```

**Example CURL Command:**

```bash  theme={null}
curl --location --request GET 'https://rbac-manager.<Your-URL>.startree.cloud/api/v1/rbac-manager/roles/srn2:role%23<Role-Name>' \
--header 'Authorization: Bearer <Token>'
```

### Deleting a Role

Use this endpoint to delete a role:

**API Endpoint:**

```
DELETE /api/v1/rbac-manager/roles/{roleSrn}
```

**Example CURL Command:**

```bash  theme={null}
curl --location --request DELETE 'https://rbac-manager.<Your-URL>.startree.cloud/api/v1/rbac-manager/roles/srn2:role%23<Role-Name>' \
--header 'Authorization: Bearer <Token>'
```

<Note>
  A role cannot be deleted if any subjects are currently assigned to it.
</Note>

## Attaching Policies to Roles

This section covers how to attach policies to roles, list attached policies, and detach policies.

### Attach a Policy to a Role

Use this endpoint to link a policy to a role:

**API Endpoint:**

```
POST /api/v1/rbac-manager/roles/{roleSrn}/attach-policy
```

**Example CURL Command:**

```bash  theme={null}
curl --location --request POST 'https://rbac-manager.<Your-URL>.startree.cloud/api/v1/rbac-manager/roles/srn2:role%23table-reader-role/attach-policy' \
--header 'Authorization: Bearer <Token>' \
--header 'Content-Type: application/json' \
--data '{
  "policySrn": "srn2:policy#my-read-only-policy"
}'
```

You can attach multiple policies to a single role by calling this API multiple times.

### List Policies Attached to a Role

Use this endpoint to list all policies attached to a role:

**API Endpoint:**

```
GET /api/v1/rbac-manager/roles/{roleSrn}/policies
```

**Example CURL Command:**

```bash  theme={null}
curl --location --request GET 'https://rbac-manager.<Your-URL>.startree.cloud/api/v1/rbac-manager/roles/srn2:role%23<Role-Name>/policies' \
--header 'Authorization: Bearer <Token>'
```

### Detach a Policy from a Role

Use this endpoint to detach a policy from a role:

**API Endpoint:**

```
POST /api/v1/rbac-manager/roles/{roleSrn}/detach-policy
```

**Example CURL Command:**

```bash  theme={null}
curl --location --request POST 'https://rbac-manager.<Your-URL>.startree.cloud/api/v1/rbac-manager/roles/srn2:role%23<Role-Name>/detach-policy' \
--header 'Authorization: Bearer <Token>' \
--header 'Content-Type: application/json' \
--data '{
  "policySrn": "srn2:policy#<Policy-Name>"
}'
```

## Role Assignments

This section covers how to assign roles to subjects, list assignments, and delete assignments.

### Assign a Role to a Subject

Use this endpoint to grant a role to a subject:

**API Endpoint:**

```
POST /api/v1/rbac-manager/roles/{roleSrn}/create-assignment
```

**Subject Types:**

* **user-email**: An individual user's email address (e.g., "[john.doe@acme.com](mailto:john.doe@acme.com)")
* **group**: The name of a group managed in your Identity Provider (IDP) (e.g., "data-analysts")
* **domain**: An email domain (e.g., "acme.com")
* **service-token**: A service token identified by its accessKey, which is the 16 character string between `st-` and the following `-` (dash)

**Example Request (assigning to a user):**

```bash  theme={null}
curl --location --request POST 'https://rbac-manager.<Your-URL>.startree.cloud/api/v1/rbac-manager/roles/srn2:role%23table-reader-role/create-assignment' \
--header 'Authorization: Bearer <Token>' \
--header 'Content-Type: application/json' \
--data '{
  "subject": "<User-Email>",
  "subjectType": "user-email"
}'
```

**Example Request (assigning to a group):**

```bash  theme={null}
curl --location --request POST 'https://rbac-manager.<Your-URL>.startree.cloud/api/v1/rbac-manager/roles/srn2:role%23<Role-Name>/create-assignment' \
--header 'Authorization: Bearer <Token>' \
--header 'Content-Type: application/json' \
--data '{
  "subject": "<Group-Name-from-IDP>",
  "subjectType": "group"
}'
```

**Example Request (assigning to a domain):**

```bash  theme={null}
curl --location --request POST 'https://rbac-manager.<Your-URL>.startree.cloud/api/v1/rbac-manager/roles/srn2:role%23<Role-Name>/create-assignment' \
--header 'Authorization: Bearer <Token>' \
--header 'Content-Type: application/json' \
--data '{
  "subject": "<Domain-Name>",
  "subjectType": "domain"
}'
```

**Example Request (assigning to a service token):**

```bash  theme={null}
curl --location --request POST 'https://rbac-manager.<Your-URL>.startree.cloud/api/v1/rbac-manager/roles/srn2:role%23<Role-Name>/create-assignment' \
--header 'Authorization: Bearer <Token>' \
--header 'Content-Type: application/json' \
--data '{
  "subject": "<AccessKey-from-Token>",
  "subjectType": "service-token"
}'
```

### List Role Assignments

Use this endpoint to list all assignments for a role:

**API Endpoint:**

```
GET /api/v1/rbac-manager/roles/{roleSrn}/assignments
```

**Example CURL Command:**

```bash  theme={null}
curl --location --request GET 'https://rbac-manager.<Your-URL>.startree.cloud/api/v1/rbac-manager/roles/srn2:role%23<Role-Name>/assignments' \
--header 'Authorization: Bearer <Token>'
```

### Delete a Role Assignment

Use this endpoint to delete a role assignment:

**API Endpoint:**

```
POST /api/v1/rbac-manager/roles/{roleSrn}/delete-assignment
```

**Example CURL Command:**

```bash  theme={null}
curl --location --request POST 'https://rbac-manager.<Your-URL>.startree.cloud/api/v1/rbac-manager/roles/srn2:role%23<Role-Name>/delete-assignment' \
--header 'Authorization: Bearer <Token>' \
--header 'Content-Type: application/json' \
--data '{
  "subject": "joe@someorg.com",
  "subjectType": "user-email"
}'
```

## Service Tokens

Service tokens act as bearer tokens for programmatic access to StarTree services (like Pinot). They consist of an access key and a secret key, formatted as st-\<accesskey>-\<secretkey>.

### Creating and Using Service Tokens

1. **Create Token:** Use the following API endpoint:

   **API Endpoint:**

   ```
   POST /api/v1/rbac-manager/service-tokens
   ```

   **Example CURL Command:**

   ```bash  theme={null}
   curl --location --request POST 'https://rbac-manager.<Your-URL>.startree.cloud/api/v1/rbac-manager/service-tokens' \
   --header 'Authorization: Bearer <Token>' \
   --header 'Content-Type: application/json' \
   --data '{
     "description": "<Description>"
   }'
   ```

   The response contains the accessKey, secretKey, and the full bearerToken.

<Warning>
  Securely save the bearerToken and secretKey immediately; the secret key cannot be retrieved again. The accessKey is used as the identifier.
</Warning>

1. **Assign Role:** Use the create-assignment endpoint (detailed in the [Assign a Role to a Subject](#assign-a-role-to-a-subject) section) with subjectType: "service-token" and the token's accessKey as the subject. A token is unusable until assigned to a role.
2. **Use Token:** Use the full bearerToken (e.g., st-accesskey-secretkey) in the Authorization: Bearer \<token> header for API calls.

### Managing Service Tokens

* **Describe:**

  **API Endpoint:**

  ```
  GET /api/v1/rbac-manager/service-tokens/{tokenSrn}
  ```

  (using the SRN which includes the access key)
* **Revoke/Delete:**

  **API Endpoint:**

  ```
  DELETE /api/v1/rbac-manager/service-tokens/{tokenSrn}
  ```

  You can also temporarily disable a token by detaching all its roles.

Built with [Mintlify](https://mintlify.com).
