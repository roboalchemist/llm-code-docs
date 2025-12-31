# Source: https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant.md.txt

# FirebaseAdmin.Auth.Multitenancy.Tenant Class Reference

# FirebaseAdmin.Auth.Multitenancy.Tenant

Represents a tenant in a multi-tenant application.

## Summary

[Multitenancy](https://firebase.google.com/docs/reference/admin/dotnet/namespace/firebase-admin/auth/multitenancy#namespace_firebase_admin_1_1_auth_1_1_multitenancy) support requires Google Cloud Identity Platform (GCIP). To learn more about GCIP, including pricing and features, see the [GCIP documentation](https://cloud.google.com/identity-platform).

Before multitenancy can be used in a Google Cloud Identity Platform project, tenants must be allowed on that project via the Cloud Console UI.

A tenant configuration provides information such as the display name, tenant identifier and email authentication configuration. For OIDC/SAML provider configuration management, [TenantAwareFirebaseAuth](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant-aware-firebase-auth#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenant_aware_firebase_auth) instances should be used instead of a [Tenant](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenant) to retrieve the list of configured IdPs on a tenant. When configuring these providers, note that tenants will inherit whitelisted domains and authenticated redirect URIs of their parent project.

All other settings of a tenant will also be inherited. These will need to be managed from the Cloud Console UI.

|                                                                                                                                                                   ### Public attributes                                                                                                                                                                    ||
|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------------------------------------|
| [DisplayName](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenant_1addf318ccee5b3c02bc9cf1dd1b023f1a)` => this.args.DisplayName`                                | `string` Gets the tenant display name.                                        |
| [EmailLinkSignInEnabled](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenant_1a7d89ca274d8141750655e919d295b2a2)` => this.args.EmailLinkSignInEnabled ?? false` | `bool` Gets a value indicating whether the email link sign-in is enabled.     |
| [PasswordSignUpAllowed](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenant_1a5ac5dcba0a3062f6f6edc7ff712c3d35)` => this.args.PasswordSignUpAllowed ?? false`   | `bool` Gets a value indicating whether the email sign-in provider is enabled. |
| [TenantId](https://firebase.google.com/docs/reference/admin/dotnet/class/firebase-admin/auth/multitenancy/tenant#class_firebase_admin_1_1_auth_1_1_multitenancy_1_1_tenant_1a95cd932d45f3b1ece68dadf08cc9fe44)` => this.ExtractResourceId(this.args.Name)`                  | `string` Gets the tenant identifier.                                          |

## Public attributes

### DisplayName

```text
string DisplayName => this.args.DisplayName
```  
Gets the tenant display name.  

### EmailLinkSignInEnabled

```text
bool EmailLinkSignInEnabled => this.args.EmailLinkSignInEnabled ?? false
```  
Gets a value indicating whether the email link sign-in is enabled.  

### PasswordSignUpAllowed

```text
bool PasswordSignUpAllowed => this.args.PasswordSignUpAllowed ?? false
```  
Gets a value indicating whether the email sign-in provider is enabled.  

### TenantId

```text
string TenantId => this.ExtractResourceId(this.args.Name)
```  
Gets the tenant identifier.