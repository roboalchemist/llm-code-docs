# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.auth.md.txt

# Auth class

Auth service bound to the provided app. An Auth instance can have multiple tenants.

**Signature:**  

    export declare class Auth extends BaseAuth 

**Extends:** [BaseAuth](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.baseauth.md#baseauth_class)

## Properties

|                                             Property                                             | Modifiers | Type |                     Description                     |
|--------------------------------------------------------------------------------------------------|-----------|------|-----------------------------------------------------|
| [app](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.auth.md#authapp) |           | App  | Returns the app associated with this Auth instance. |

## Methods

|                                                                Method                                                                | Modifiers |                                   Description                                    |
|--------------------------------------------------------------------------------------------------------------------------------------|-----------|----------------------------------------------------------------------------------|
| [projectConfigManager()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.auth.md#authprojectconfigmanager) |           | Returns the project config manager instance associated with the current project. |
| [tenantManager()](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.auth.md#authtenantmanager)               |           | Returns the tenant manager instance associated with the current project.         |

## Auth.app

Returns the app associated with this Auth instance.

**Signature:**  

    get app(): App;

## Auth.projectConfigManager()

Returns the project config manager instance associated with the current project.

**Signature:**  

    projectConfigManager(): ProjectConfigManager;

**Returns:**

[ProjectConfigManager](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.projectconfigmanager.md#projectconfigmanager_class)

The project config manager instance associated with the current project.

## Auth.tenantManager()

Returns the tenant manager instance associated with the current project.

**Signature:**  

    tenantManager(): TenantManager;

**Returns:**

[TenantManager](https://firebase.google.com/docs/reference/admin/node/firebase-admin.auth.tenantmanager.md#tenantmanager_class)

The tenant manager instance associated with the current project.