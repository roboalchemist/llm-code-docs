# Source: https://docs.api7.ai/enterprise/getting-started/rbac.md

# Source: https://docs.api7.ai/enterprise/3.2.16.7/getting-started/rbac.md

# Source: https://docs.api7.ai/enterprise/3.2.16.6/getting-started/rbac.md

# Source: https://docs.api7.ai/enterprise/3.2.16.5/getting-started/rbac.md

# Source: https://docs.api7.ai/enterprise/3.2.16.4.1/getting-started/rbac.md

# Source: https://docs.api7.ai/enterprise/3.2.15.2.1/getting-started/rbac.md

# Source: https://docs.api7.ai/enterprise/3.2.14.6/getting-started/rbac.md

# Source: https://docs.api7.ai/enterprise/3.8.x/getting-started/rbac.md

# Source: https://docs.api7.ai/enterprise/3.7.x/getting-started/rbac.md

# Source: https://docs.api7.ai/enterprise/3.6.x/getting-started/rbac.md

# Source: https://docs.api7.ai/enterprise/3.5.x/getting-started/rbac.md

# Source: https://docs.api7.ai/enterprise/3.4.x/getting-started/rbac.md

# Source: https://docs.api7.ai/enterprise/3.3.x/getting-started/rbac.md

# Update User Roles

Role-Based Access Control (RBAC) links permissions to roles instead of directly to users. Users are then assigned these roles, simplifying access management, enhancing efficiency, and reducing errors. This guide will walk you through managing role-based access control using custom role, permission policy, and permission boundary of API7 Enterprise.

## Update a User Role[â](#update-a-user-role "Direct link to Update a User Role")

1. Select **Organization** from the top navigation bar, and then select **Users**.
2. Click **Update Roles** for the target user.
3. Add or remove roles.
4. Click **Update**.

note

To view the permissions for every role, select **Organization** from the top navigation bar and select **Roles**.

Roles and permission policies are combined to control access. Here's an example of isolating access to environments using a custom role and permission policy.

### Define Permission Policies[â](#define-permission-policies "Direct link to Define Permission Policies")

1. Create three gateway groups: `test`, `UAT`, and `production`.

2. Select **Organization** from the top navigation bar, and then select **Permission Policies**.

3. Click **+ Add Policy**.

4. In the **+ Add Permission Policy** dialog box, do the following:

   <!-- -->

   * In the **Name** field, enter `test-gateway-group-full-access`.

   * In the **Policy editor** field, enter the configuration:

     ```
      {
        "statement": [
          {
            "resources": [
              "arn:api7:gateway:gatewaygroup/b6db7341-fc1f-4cee-a318-3e782a163d24"
            ],
            "actions": [
              "<.*>"
            ],
            "effect": "allow"
          },
          {
            "resources": [
              "arn:api7:gateway:gatewaygroup/b6db7341-fc1f-4cee-a318-3e782a163d24/publishedservice/<.*>"
            ],
            "actions": [
              "<.*>"
            ],
            "effect": "allow"
          }
        ]
      } 
     ```

     note

     The resource ID should be consistent with the gateway groups created. Please change it per your use.

   * Click **Add**.

5. Click **+ Add Policy**.

6. In the dialog box, do the following:

   <!-- -->

   * In the **Name** field, enter `uat-gateway-group-full-access`.

   * In the **Policy editor** field, enter the configuration:

     ```
      {
        "statement": [
          {
            "resources": [
              "arn:api7:gateway:gatewaygroup/45a06edc-4a93-4bea-a437-3f153b56254c"
            ],
            "actions": [
              "<.*>"
            ],
            "effect": "allow"
          },
          {
            "resources": [
              "arn:api7:gateway:gatewaygroup/45a06edc-4a93-4bea-a437-3f153b56254c/publishedservice/<.*>"
            ],
            "actions": [
              "<.*>"
            ],
            "effect": "allow"
          }
        ]
      } 
     ```

   * Click **Add**.

7. Click **+ Add Policy**.

8. In the dialog box, do the following:

   <!-- -->

   * In the **Name** field, enter `production-gateway-group-full-access`.

   * In the **Policy editor** field, enter the configuration:

     ```
      {
        "statement": [
          {
            "resources": [
              "arn:api7:gateway:gatewaygroup/edc12ecd-94a5-49b2-b82d-8d1113e6cd86"
            ],
            "actions": [
              "<.*>"
            ],
            "effect": "allow"
          },
          {
            "resources": [
              "arn:api7:gateway:gatewaygroup/edc12ecd-94a5-49b2-b82d-8d1113e6cd86/publishedservice/<.*>"
            ],
            "actions": [
              "<.*>"
            ],
            "effect": "allow"
          }
        ]
      } 
     ```

   * Click **Add**.

### Define Custom Roles[â](#define-custom-roles "Direct link to Define Custom Roles")

1. Select **Organization** from the top navigation bar, and then select **Roles**.

2. Click **+ Add Custom Role**.

3. In the dialog box, do the following:

   <!-- -->

   * In the **Name** field, enter `Development Team Member`.
   * Click **Add**.

4. Create two other roles `Development Team Lead` and `Test Engineer` in the same way.

### Assign Roles with Controlled Access[â](#assign-roles-with-controlled-access "Direct link to Assign Roles with Controlled Access")

1. Click `Development Team Member` and enter the role page.

2. Click **+ Attach Policy**.

3. In the dialog box, do the following:

   <!-- -->

   * In the **Permission Policies** field, select `test-gateway-group-full-access`.
   * Click **Submit**. This allows them to make changes solely in the test environment.

4. Assign `test-gateway-group-full-access` and `uat-gateway-group-full-access` policies to `Development Team Lead`. This enables them to work in both test and UAT environments, potentially including the ability to synchronize stable configurations from test to UAT.

5. Assign `uat-gateway-group-full-access` and `production-gateway-group-full-access` policies to `Test Engineer`. This restricts their access to UAT and Production environments, focusing on new API testing and publishing tasks.

### Validate[â](#validate "Direct link to Validate")

1. Log in to API7 Enterprise using an account with the `Development Team Member` role and can only have access to the `Test` gateway group.
2. Log in to API7 Enterprise using an account with the `Development Team Lead` role and can only have access to the `Test` and `UAT` gateway groups.
3. Log in to API7 Enterprise using an account with the `Test Engineer` role and can only have access to the `UAT` and `Production` gateway groups.

## Set Role Mapping (SSO Required)[â](#set-role-mapping-sso-required "Direct link to Set Role Mapping (SSO Required)")

Users who meet the defined key-value mapping rules will be automatically assigned the corresponding roles upon login. See [Set Role Mapping](https://docs.api7.ai/enterprise/3.3.x/best-practices/sso.md#set-role-mapping) for details.

note

Role mapping takes precedence over manual role assignments. Any manual adjustments to a user's roles will be overwritten upon the next user login when role mapping is active.

## Set User Permission Boundary[â](#set-user-permission-boundary "Direct link to Set User Permission Boundary")

A user's effective permissions are determined by the intersection of their assigned roles and their permission boundary. This means a user's action is permitted only when:

* Allowed by at least one assigned role.
* Allowed by at least one permission boundary (if present).
* Not denied by any assigned role or permission boundary.

Here is an example of restricting access to licenses using permission boundaries. Below is an interactive demo that provides a hands-on introduction.

### Create Permission Policy and Set Permission Boundary[â](#create-permission-policy-and-set-permission-boundary "Direct link to Create Permission Policy and Set Permission Boundary")

1. Select **Organization** from the top navigation bar, and then select **Permission Policies**.

2. Click **+ Add Policy**.

3. In the dialog box, do the following:

   <!-- -->

   * In the **Name** field, enter `no-access-to-license`.

   * In the **Policy editor** field, enter the configuration:

     ```
      {
        "statement": [
          {
            "resources": [
              "arn:api7:iam:organization/*"
            ],
            "actions": [
              "iam:UpdateLicense"
            ],
            "effect": "deny"
          },
          {
            "resources": [
              "<.*>"
            ],
            "actions": [
              "<.*>"
            ],
            "effect": "allow"
          }
        ]
      }
     ```

     note

     This policy allows access to all the resources except the license.

   * Click **Add**.

4. Select **Organization** from the top navigation bar, and then select **Users**.

5. Click **+ Invite User**.

6. In the dialog box, do the following:

   <!-- -->

   * In the **Username** field, enter `Tom`.
   * Set a one-time password for Tom.
   * In the **Permission Boundary** field, select `no-access-to-license`.
   * Click **Invite**.

7. Click **Update Roles**.

8. In the dialog box, do the following:

   <!-- -->

   * In the **Roles** field, select `Super Admin`.
   * Click **Update**.

### Validate[â](#validate-1 "Direct link to Validate")

1. Log in to API7 Enterprise using Tom's account.
2. Select **Organization** from the top navigation bar, and then select **License**.
3. Click the editing logo on the license page, and can see the following note, showing that access is denied: **Permission denied. Your role does not allow this action. Please contact your administrator if you need additional access.**

## Set Permission Boundary Mapping (SSO Required)[â](#set-permission-boundary-mapping-sso-required "Direct link to Set Permission Boundary Mapping (SSO Required)")

Users who meet the defined key-value mapping rules will be automatically assigned the corresponding permission boundary upon login. See [Set Permission Boundary Mapping](https://docs.api7.ai/enterprise/3.3.x/best-practices/sso.md#set-permission-boundary-mapping) for details.

note

Permission boundary mapping takes precedence over manual permission boundary modification. Any manual adjustments to a user's permission boundaries will be overwritten upon the next user login when permission boundary mapping is active.

## Additional Resources[â](#additional-resources "Direct link to Additional Resources")

* Key Concepts
  <!-- -->
  * [Roles and Permission Policies](https://docs.api7.ai/enterprise/3.3.x/key-concepts/roles-and-permission-policies.md)
* Getting Started
  <!-- -->
  * [Create Custom Role](https://docs.api7.ai/enterprise/3.3.x/getting-started/create-custom-role.md)
* Best Practices
  <!-- -->
  * [Log in to API7 Dashboard with SSO](https://docs.api7.ai/enterprise/3.3.x/best-practices/sso.md)
