# Source: https://doc.keepnetlabs.com/next-generation-product/getting-started/2.-add-target-users/add-users-via-scim/scim-setup-in-onelogin.md

# SCIM Setup in Onelogin

The document show step by step how to synchronize users' information from the Onelogin identity provider to the platform.

## **Onelogin Configuration**

1. Please log in to[ https://www.onelogin.com/](https://www.onelogin.com/) as an admin user.
2. Click on **Applications** and click **Add App** on the top of the screen.
3. Search **‘SCIM Provisioner with SAML (SCIM v2 Enterprise)'** and click on the **Add** button.
4. Enter a name for the application like **My SCIM Integration** and click on the **Save** button.
5. Once you have successfully created the application, enter the application details and go to the **Configuration** menu and enable the **API Connection.**
   1. **Tenant URL:** <https://scim-api.keepnetlabs.com/scim>
   2. **SCIM JSON Template:** Please fill up this field with the following code.
   3. {\
      "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {\
      "department": "{$parameters.department}",\
      "manager": {\
      "managerId": "{$parameters.external\_manager\_id}",\
      "displayName": "{$user.manager\_firstname} {$user.manager\_lastname}"\
      }\
      },\
      \
      "active": "{$user.active}",\
      "emails": \[\
      {\
      "value": "{$user.email}",\
      "type": "work",\
      "primary": true\
      }\
      ],\
      "meta": {\
      "resourceType": "User"\
      },\
      "name": {\
      "familyName": "{$user.lastname}",\
      "givenName": "{$user.firstname}",\
      "formatted": "{$user.display\_name}"\
      },\
      "userName": "{$parameters.scimusername}",\
      "id": null,\
      "schemas": \[\
      "urn:ietf:params:scim:schemas:core:2.0:User"\
      ]\
      }
   4. **SCIM Bearer Token:** Enter the token which was created on the platform.
   5. Click on the **Save** button the proceed.
6. Go to the **Provisioning menu** and enable the following options under the **Workflow title**.
   1. Enable Provisioning.
   2. Create User
   3. Delete User
   4. Update User

OneLogin configuration has been successfully finished. You can proceed with the following step.

## **Synchronization Users or Groups**

You can find how to synchronize users or groups from [here](https://developers.onelogin.com/scim/create-app) under the **‘Provisioning Users into Groups’** title.

✅ **You have now added your first Target Users. Now you need to** [**ensure they are able to receive emails from Keepnet**](https://github.com/ucarozan/keepnet-docs/blob/main/next-generation-product/getting-started/3.-email-deliverability) **successfully ➡️**
