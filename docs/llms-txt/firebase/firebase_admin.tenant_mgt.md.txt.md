# Source: https://firebase.google.com/docs/reference/admin/python/firebase_admin.tenant_mgt.md.txt

# firebase_admin.tenant_mgt module

Firebase tenant management module.

This module contains functions for creating and configuring authentication tenants within a
Google Cloud Identity Platform (GCIP) instance.

## Exceptions

| ### TenantIdMismatchError exception firebase_admin.tenant_mgt.TenantIdMismatchError(*message* ) |
|---|
| Bases: [`InvalidArgumentError`](https://firebase.google.com/docs/reference/admin/python/firebase_admin.exceptions#firebase_admin.exceptions.InvalidArgumentError "firebase_admin.exceptions.InvalidArgumentError") Missing or invalid tenant ID field in the given JWT. |

| ### TenantNotFoundError exception firebase_admin.tenant_mgt.TenantNotFoundError(*message* , *cause=None* , *http_response=None* ) |
|---|
| Bases: [`NotFoundError`](https://firebase.google.com/docs/reference/admin/python/firebase_admin.exceptions#firebase_admin.exceptions.NotFoundError "firebase_admin.exceptions.NotFoundError") No tenant found for the specified identifier. default_message = 'No tenant found for the given identifier' : |

## Classes

| ### ListTenantsPage class firebase_admin.tenant_mgt.ListTenantsPage(*download* , *page_token* , *max_results* ) |
|---|
| Bases: `object` Represents a page of tenants fetched from a Firebase project. Provides methods for traversing tenants included in this page, as well as retrieving subsequent pages of tenants. The iterator returned by `iterate_all()` can be used to iterate through all tenants in the Firebase project starting from this page. get_next_page() :   Retrieves the next page of tenants, if available. Returns: :   Next page of tenants, or None if this is the last page. Return type: :   [ListTenantsPage](https://firebase.google.com/docs/reference/admin/python/firebase_admin.tenant_mgt#firebase_admin.tenant_mgt.ListTenantsPage "firebase_admin.tenant_mgt.ListTenantsPage") iterate_all() :   Retrieves an iterator for tenants. Returned iterator will iterate through all the tenants in the Firebase project starting from this page. The iterator will never buffer more than one page of tenants in memory at a time. Returns: :   An iterator of Tenant instances. Return type: :   iterator | property has_next_page | |---| | A boolean indicating whether more pages are available. | | property next_page_token | |---| | Page token string for the next page (empty string indicates no more pages). | | property tenants | |---| | A list of `ExportedUserRecord` instances available in this page. | |

| ### Tenant class firebase_admin.tenant_mgt.Tenant(*data* ) |
|---|
| Bases: `object` Represents a tenant in a multi-tenant application. Multi-tenancy support requires Google Cloud Identity Platform (GCIP). To learn more about GCIP including pricing and features, see <https://cloud.google.com/identity-platform>. Before multi-tenancy can be used in a Google Cloud Identity Platform project, tenants must be enabled in that project via the Cloud Console UI. A Tenant instance provides information such as the display name, tenant identifier and email authentication configuration. | property allow_password_sign_up | |---| |   | | property display_name | |---| |   | | property enable_email_link_sign_in | |---| |   | | property tenant_id | |---| |   | |

## Functions

| ### auth_for_tenant firebase_admin.tenant_mgt.auth_for_tenant(*tenant_id* , *app=None* ) |
|---|
| Gets an Auth Client instance scoped to the given tenant ID. Parameters: : - **tenant_id** -- A tenant ID string. - **app** -- An App instance (optional). Returns: :   An `auth.Client` object. Return type: :   [auth.Client](https://firebase.google.com/docs/reference/admin/python/firebase_admin.auth#firebase_admin.auth.Client "firebase_admin.auth.Client") Raises: :   **ValueError** -- If the tenant ID is None, empty or not a string. |

| ### create_tenant firebase_admin.tenant_mgt.create_tenant(*display_name* , *allow_password_sign_up=None* , *enable_email_link_sign_in=None* , *app=None* ) |
|---|
| Creates a new tenant from the given options. Parameters: : - **display_name** -- Display name string for the new tenant. Must begin with a letter and contain only letters, digits and hyphens. Length must be between 4 and 20. - **allow_password_sign_up** -- A boolean indicating whether to enable or disable the email sign-in provider (optional). - **enable_email_link_sign_in** -- A boolean indicating whether to enable or disable email link sign-in (optional). Disabling this makes the password required for email sign-in. - **app** -- An App instance (optional). Returns: :   A tenant object. Return type: :   [Tenant](https://firebase.google.com/docs/reference/admin/python/firebase_admin.tenant_mgt#firebase_admin.tenant_mgt.Tenant "firebase_admin.tenant_mgt.Tenant") Raises: : - **ValueError** -- If any of the given arguments are invalid. - [**FirebaseError**](https://firebase.google.com/docs/reference/admin/python/firebase_admin.exceptions#firebase_admin.exceptions.FirebaseError "firebase_admin.exceptions.FirebaseError") -- If an error occurs while creating the tenant. |

| ### delete_tenant firebase_admin.tenant_mgt.delete_tenant(*tenant_id* , *app=None* ) |
|---|
| Deletes the tenant corresponding to the given `tenant_id`. Parameters: : - **tenant_id** -- A tenant ID string. - **app** -- An App instance (optional). Raises: : - **ValueError** -- If the tenant ID is None, empty or not a string. - [**TenantNotFoundError**](https://firebase.google.com/docs/reference/admin/python/firebase_admin.tenant_mgt#firebase_admin.tenant_mgt.TenantNotFoundError "firebase_admin.tenant_mgt.TenantNotFoundError") -- If no tenant exists by the given ID. - [**FirebaseError**](https://firebase.google.com/docs/reference/admin/python/firebase_admin.exceptions#firebase_admin.exceptions.FirebaseError "firebase_admin.exceptions.FirebaseError") -- If an error occurs while retrieving the tenant. |

| ### get_tenant firebase_admin.tenant_mgt.get_tenant(*tenant_id* , *app=None* ) |
|---|
| Gets the tenant corresponding to the given `tenant_id`. Parameters: : - **tenant_id** -- A tenant ID string. - **app** -- An App instance (optional). Returns: :   A tenant object. Return type: :   [Tenant](https://firebase.google.com/docs/reference/admin/python/firebase_admin.tenant_mgt#firebase_admin.tenant_mgt.Tenant "firebase_admin.tenant_mgt.Tenant") Raises: : - **ValueError** -- If the tenant ID is None, empty or not a string. - [**TenantNotFoundError**](https://firebase.google.com/docs/reference/admin/python/firebase_admin.tenant_mgt#firebase_admin.tenant_mgt.TenantNotFoundError "firebase_admin.tenant_mgt.TenantNotFoundError") -- If no tenant exists by the given ID. - [**FirebaseError**](https://firebase.google.com/docs/reference/admin/python/firebase_admin.exceptions#firebase_admin.exceptions.FirebaseError "firebase_admin.exceptions.FirebaseError") -- If an error occurs while retrieving the tenant. |

| ### list_tenants firebase_admin.tenant_mgt.list_tenants(*page_token=None* , *max_results=100* , *app=None* ) |
|---|
| Retrieves a page of tenants from a Firebase project. The `page_token` argument governs the starting point of the page. The `max_results` argument governs the maximum number of tenants that may be included in the returned page. This function never returns None. If there are no user accounts in the Firebase project, this returns an empty page. Parameters: : - **page_token** -- A non-empty page token string, which indicates the starting point of the page (optional). Defaults to `None`, which will retrieve the first page of users. - **max_results** -- A positive integer indicating the maximum number of users to include in the returned page (optional). Defaults to 100, which is also the maximum number allowed. - **app** -- An App instance (optional). Returns: :   A page of tenants. Return type: :   [ListTenantsPage](https://firebase.google.com/docs/reference/admin/python/firebase_admin.tenant_mgt#firebase_admin.tenant_mgt.ListTenantsPage "firebase_admin.tenant_mgt.ListTenantsPage") Raises: : - **ValueError** -- If `max_results` or `page_token` are invalid. - [**FirebaseError**](https://firebase.google.com/docs/reference/admin/python/firebase_admin.exceptions#firebase_admin.exceptions.FirebaseError "firebase_admin.exceptions.FirebaseError") -- If an error occurs while retrieving the user accounts. |

| ### update_tenant firebase_admin.tenant_mgt.update_tenant(*tenant_id* , *display_name=None* , *allow_password_sign_up=None* , *enable_email_link_sign_in=None* , *app=None* ) |
|---|
| Updates an existing tenant with the given options. Parameters: : - **tenant_id** -- ID of the tenant to update. - **display_name** -- Updated display name string for the tenant (optional). - **allow_password_sign_up** -- A boolean indicating whether to enable or disable the email sign-in provider. - **enable_email_link_sign_in** -- A boolean indicating whether to enable or disable email link sign-in. Disabling this makes the password required for email sign-in. - **app** -- An App instance (optional). Returns: :   The updated tenant object. Return type: :   [Tenant](https://firebase.google.com/docs/reference/admin/python/firebase_admin.tenant_mgt#firebase_admin.tenant_mgt.Tenant "firebase_admin.tenant_mgt.Tenant") Raises: : - **ValueError** -- If any of the given arguments are invalid. - [**TenantNotFoundError**](https://firebase.google.com/docs/reference/admin/python/firebase_admin.tenant_mgt#firebase_admin.tenant_mgt.TenantNotFoundError "firebase_admin.tenant_mgt.TenantNotFoundError") -- If no tenant exists by the given ID. - [**FirebaseError**](https://firebase.google.com/docs/reference/admin/python/firebase_admin.exceptions#firebase_admin.exceptions.FirebaseError "firebase_admin.exceptions.FirebaseError") -- If an error occurs while creating the tenant. |