# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/api/user_api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.api.user_api

## Classes

### UserApi

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi(
	api_client=None
)
```

| Parameters        |     |
| ----------------- | --- |
| `api_client=None` | ` ` |

***

**METHODS**

#### accept\_eula

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.accept_eula(
	self,
	accept_eula_request: edgeimpulse_api.models.accept_eula_request.AcceptEulaRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Accept End-User License Agreement

To access some models or tooling, you might need to first accept an End-User License Agreement. The full list of available EULAs are listed via `GetUserResponse`.

| Parameters            |                                                                |
| --------------------- | -------------------------------------------------------------- |
| `self`                | ` `                                                            |
| `accept_eula_request` | `edgeimpulse_api.models.accept_eula_request.AcceptEulaRequest` |
| `**kwargs`            | ` `                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### accept\_terms\_of\_service

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.accept_terms_of_service(
	self,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Accept Terms of Service

Accept Terms of Service.

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |
| `**kwargs` | ` ` |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### activate\_current\_user

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.activate_current_user(
	self,
	activate_user_or_verify_email_request: edgeimpulse_api.models.activate_user_or_verify_email_request.ActivateUserOrVerifyEmailRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Activate current user

Activate the current user account (requires an activation code). This function is only available through a JWT token.

| Parameters                              |                                                                                                 |
| --------------------------------------- | ----------------------------------------------------------------------------------------------- |
| `self`                                  | ` `                                                                                             |
| `activate_user_or_verify_email_request` | `edgeimpulse_api.models.activate_user_or_verify_email_request.ActivateUserOrVerifyEmailRequest` |
| `**kwargs`                              | ` `                                                                                             |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### activate\_user

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.activate_user(
	self,
	user_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='User ID')],
	activate_user_or_verify_email_request: edgeimpulse_api.models.activate_user_or_verify_email_request.ActivateUserOrVerifyEmailRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Activate user

Activate a user account (requires an activation code). This function is only available through a JWT token.

| Parameters                              |                                                                                                             |
| --------------------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `self`                                  | ` `                                                                                                         |
| `user_id`                               | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='User ID')]` |
| `activate_user_or_verify_email_request` | `edgeimpulse_api.models.activate_user_or_verify_email_request.ActivateUserOrVerifyEmailRequest`             |
| `**kwargs`                              | ` `                                                                                                         |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### activate\_user\_by\_third\_party\_activation\_code

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.activate_user_by_third_party_activation_code(
	self,
	activate_user_by_third_party_activation_code_request: edgeimpulse_api.models.activate_user_by_third_party_activation_code_request.ActivateUserByThirdPartyActivationCodeRequest,
	**kwargs
) ‑> edgeimpulse_api.models.get_jwt_response.GetJWTResponse
```

Activate user by third party activation code

Activate a user that was created by a third party. This function is only available through a JWT token.

| Parameters                                             |                                                                                                                             |
| ------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------- |
| `self`                                                 | ` `                                                                                                                         |
| `activate_user_by_third_party_activation_code_request` | `edgeimpulse_api.models.activate_user_by_third_party_activation_code_request.ActivateUserByThirdPartyActivationCodeRequest` |
| `**kwargs`                                             | ` `                                                                                                                         |

| Returns                                                  |
| -------------------------------------------------------- |
| `edgeimpulse_api.models.get_jwt_response.GetJWTResponse` |

#### change\_password\_current\_user

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.change_password_current_user(
	self,
	change_password_request: edgeimpulse_api.models.change_password_request.ChangePasswordRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Change password current user

Change the password for the current user account. This function is only available through a JWT token.

| Parameters                |                                                                        |
| ------------------------- | ---------------------------------------------------------------------- |
| `self`                    | ` `                                                                    |
| `change_password_request` | `edgeimpulse_api.models.change_password_request.ChangePasswordRequest` |
| `**kwargs`                | ` `                                                                    |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### change\_password\_user

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.change_password_user(
	self,
	user_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='User ID')],
	change_password_request: edgeimpulse_api.models.change_password_request.ChangePasswordRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Change password

Change the password for a user account. This function is only available through a JWT token.

| Parameters                |                                                                                                             |
| ------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `self`                    | ` `                                                                                                         |
| `user_id`                 | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='User ID')]` |
| `change_password_request` | `edgeimpulse_api.models.change_password_request.ChangePasswordRequest`                                      |
| `**kwargs`                | ` `                                                                                                         |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### convert\_current\_user

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.convert_current_user(
	self,
	convert_user_request: edgeimpulse_api.models.convert_user_request.ConvertUserRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Convert current evaluation user

Convert current evaluation user account to regular account.

| Parameters             |                                                                  |
| ---------------------- | ---------------------------------------------------------------- |
| `self`                 | ` `                                                              |
| `convert_user_request` | `edgeimpulse_api.models.convert_user_request.ConvertUserRequest` |
| `**kwargs`             | ` `                                                              |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### create\_developer\_profile

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.create_developer_profile(
	self,
	**kwargs
) ‑> edgeimpulse_api.models.create_developer_profile_response.CreateDeveloperProfileResponse
```

Create developer profile

Create a developer profile for the current active user.

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |
| `**kwargs` | ` ` |

| Returns                                                                                   |
| ----------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.create_developer_profile_response.CreateDeveloperProfileResponse` |

#### create\_enterprise\_trial\_user

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.create_enterprise_trial_user(
	self,
	create_enterprise_trial_user_request: Annotated[edgeimpulse_api.models.create_enterprise_trial_user_request.CreateEnterpriseTrialUserRequest, FieldInfo(annotation=NoneType, required=True, description='Trial request')],
	**kwargs
) ‑> edgeimpulse_api.models.create_enterprise_trial_response.CreateEnterpriseTrialResponse
```

Create enterprise trial user

Creates an enterprise trial user and a new trial organization, and redirects the user to the new organization. This API is internal (it requires some signed fields), sign up at [https://studio.edgeimpulse.com/signup](https://studio.edgeimpulse.com/signup) instead.

| Parameters                             |                                                                                                                                                                                       |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`                                 | ` `                                                                                                                                                                                   |
| `create_enterprise_trial_user_request` | `Annotated[edgeimpulse_api.models.create_enterprise_trial_user_request.CreateEnterpriseTrialUserRequest, FieldInfo(annotation=NoneType, required=True, description='Trial request')]` |
| `**kwargs`                             | ` `                                                                                                                                                                                   |

| Returns                                                                                 |
| --------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.create_enterprise_trial_response.CreateEnterpriseTrialResponse` |

#### create\_pro\_tier\_user

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.create_pro_tier_user(
	self,
	create_pro_tier_user_request: edgeimpulse_api.models.create_pro_tier_user_request.CreateProTierUserRequest,
	**kwargs
) ‑> edgeimpulse_api.models.create_user_response.CreateUserResponse
```

Create Professional Tier user

Create a new user for the Professional Plan and a new project. Note that the Professional plan will not be enabled until the payment is successful. This API is internal (it requires some signed fields), sign up at [https://studio.edgeimpulse.com/signup](https://studio.edgeimpulse.com/signup) instead.

| Parameters                     |                                                                                |
| ------------------------------ | ------------------------------------------------------------------------------ |
| `self`                         | ` `                                                                            |
| `create_pro_tier_user_request` | `edgeimpulse_api.models.create_pro_tier_user_request.CreateProTierUserRequest` |
| `**kwargs`                     | ` `                                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.create_user_response.CreateUserResponse` |

#### create\_user

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.create_user(
	self,
	create_user_request: edgeimpulse_api.models.create_user_request.CreateUserRequest,
	**kwargs
) ‑> edgeimpulse_api.models.create_user_response.CreateUserResponse
```

Create user

Create a new user and project. This API is no longer publicly available. Sign up at [https://studio.edgeimpulse.com/signup](https://studio.edgeimpulse.com/signup) instead.

| Parameters            |                                                                |
| --------------------- | -------------------------------------------------------------- |
| `self`                | ` `                                                            |
| `create_user_request` | `edgeimpulse_api.models.create_user_request.CreateUserRequest` |
| `**kwargs`            | ` `                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.create_user_response.CreateUserResponse` |

#### delete\_current\_user

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.delete_current_user(
	self,
	delete_user_request: edgeimpulse_api.models.delete_user_request.DeleteUserRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Delete current user

Delete a user. This function is only available through a JWT token, and can only remove the current user.

| Parameters            |                                                                |
| --------------------- | -------------------------------------------------------------- |
| `self`                | ` `                                                            |
| `delete_user_request` | `edgeimpulse_api.models.delete_user_request.DeleteUserRequest` |
| `**kwargs`            | ` `                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### delete\_photo\_current\_user

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.delete_photo_current_user(
	self,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Delete photo

Delete user profile photo. This function is only available through a JWT token.

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |
| `**kwargs` | ` ` |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### delete\_user

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.delete_user(
	self,
	user_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='User ID')],
	delete_user_request: edgeimpulse_api.models.delete_user_request.DeleteUserRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Delete user

Delete a user. This function is only available through a JWT token, and can only remove the current user.

| Parameters            |                                                                                                             |
| --------------------- | ----------------------------------------------------------------------------------------------------------- |
| `self`                | ` `                                                                                                         |
| `user_id`             | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='User ID')]` |
| `delete_user_request` | `edgeimpulse_api.models.delete_user_request.DeleteUserRequest`                                              |
| `**kwargs`            | ` `                                                                                                         |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### get\_current\_user

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.get_current_user(
	self,
	exclude_projects: Annotated[Annotated[bool, Strict(strict=True)] | None, FieldInfo(annotation=NoneType, required=True, description='If set to "true", the "projects" field is left empty (will be faster if you call this function a lot). Use `getCurrentUserProjects` to get the project list in a separate call.')] = None,
	**kwargs
) ‑> edgeimpulse_api.models.get_user_response.GetUserResponse
```

Get current user

Get information about the current user. This function is only available through a JWT token.

| Parameters         |                                                                                                                                                                                                                                                                                                                |
| ------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `self`             | ` `                                                                                                                                                                                                                                                                                                            |
| `exclude_projects` | `Annotated[Annotated[bool, Strict(strict=True)] \| None, FieldInfo(annotation=NoneType, required=True, description='If set to "true", the "projects" field is left empty (will be faster if you call this function a lot). Use `getCurrentUserProjects` to get the project list in a separate call.')] = None` |
| `**kwargs`         | ` `                                                                                                                                                                                                                                                                                                            |

| Returns                                                    |
| ---------------------------------------------------------- |
| `edgeimpulse_api.models.get_user_response.GetUserResponse` |

#### get\_current\_user\_projects

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.get_current_user_projects(
	self,
	**kwargs
) ‑> edgeimpulse_api.models.get_user_projects_response.GetUserProjectsResponse
```

Get current user projects

Get projects for the current user. This returns all projects regardless of whitelabel. This function is only available through a JWT token.

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |
| `**kwargs` | ` ` |

| Returns                                                                     |
| --------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_user_projects_response.GetUserProjectsResponse` |

#### get\_user

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.get_user(
	self,
	user_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='User ID')],
	**kwargs
) ‑> edgeimpulse_api.models.get_user_response.GetUserResponse
```

Get user

Get information about a user. This function is only available through a JWT token.

| Parameters |                                                                                                             |
| ---------- | ----------------------------------------------------------------------------------------------------------- |
| `self`     | ` `                                                                                                         |
| `user_id`  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='User ID')]` |
| `**kwargs` | ` `                                                                                                         |

| Returns                                                    |
| ---------------------------------------------------------- |
| `edgeimpulse_api.models.get_user_response.GetUserResponse` |

#### get\_user\_by\_third\_party\_activation\_code

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.get_user_by_third_party_activation_code(
	self,
	user_by_third_party_activation_request: edgeimpulse_api.models.user_by_third_party_activation_request.UserByThirdPartyActivationRequest,
	**kwargs
) ‑> edgeimpulse_api.models.get_user_response.GetUserResponse
```

Get user by third party activation code

Get information about a user through an activation code. This function is only available through a JWT token.

| Parameters                               |                                                                                                   |
| ---------------------------------------- | ------------------------------------------------------------------------------------------------- |
| `self`                                   | ` `                                                                                               |
| `user_by_third_party_activation_request` | `edgeimpulse_api.models.user_by_third_party_activation_request.UserByThirdPartyActivationRequest` |
| `**kwargs`                               | ` `                                                                                               |

| Returns                                                    |
| ---------------------------------------------------------- |
| `edgeimpulse_api.models.get_user_response.GetUserResponse` |

#### get\_user\_need\_to\_set\_password

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.get_user_need_to_set_password(
	self,
	username_or_email: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Username or email')],
	**kwargs
) ‑> edgeimpulse_api.models.get_user_need_to_set_password_response.GetUserNeedToSetPasswordResponse
```

Get user registration state

Tells whether a user is registered and whether it needs to set its password.

| Parameters          |                                                                                                                       |
| ------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `self`              | ` `                                                                                                                   |
| `username_or_email` | `Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Username or email')]` |
| `**kwargs`          | ` `                                                                                                                   |

| Returns                                                                                          |
| ------------------------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.get_user_need_to_set_password_response.GetUserNeedToSetPasswordResponse` |

#### list\_emails\_current\_user

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.list_emails_current_user(
	self,
	**kwargs
) ‑> edgeimpulse_api.models.list_email_response.ListEmailResponse
```

List emails

Get a list of all emails sent by Edge Impulse to the current user. This function is only available through a JWT token, and is not available for all users.

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |
| `**kwargs` | ` ` |

| Returns                                                        |
| -------------------------------------------------------------- |
| `edgeimpulse_api.models.list_email_response.ListEmailResponse` |

#### list\_emails\_user

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.list_emails_user(
	self,
	user_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='User ID')],
	**kwargs
) ‑> edgeimpulse_api.models.list_email_response.ListEmailResponse
```

List emails

Get a list of all emails sent by Edge Impulse to a user. This function is only available through a JWT token, and is not available for all users.

| Parameters |                                                                                                             |
| ---------- | ----------------------------------------------------------------------------------------------------------- |
| `self`     | ` `                                                                                                         |
| `user_id`  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='User ID')]` |
| `**kwargs` | ` `                                                                                                         |

| Returns                                                        |
| -------------------------------------------------------------- |
| `edgeimpulse_api.models.list_email_response.ListEmailResponse` |

#### list\_enterprise\_trials\_user

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.list_enterprise_trials_user(
	self,
	user_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='User ID')],
	**kwargs
) ‑> edgeimpulse_api.models.list_enterprise_trials_response.ListEnterpriseTrialsResponse
```

Get enterprise trials

Get a list of all enterprise trials for a user. This function is only available through a JWT token.

| Parameters |                                                                                                             |
| ---------- | ----------------------------------------------------------------------------------------------------------- |
| `self`     | ` `                                                                                                         |
| `user_id`  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='User ID')]` |
| `**kwargs` | ` `                                                                                                         |

| Returns                                                                               |
| ------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.list_enterprise_trials_response.ListEnterpriseTrialsResponse` |

#### list\_organization\_buckets\_current\_user

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.list_organization_buckets_current_user(
	self,
	**kwargs
) ‑> edgeimpulse_api.models.list_organization_buckets_user_response.ListOrganizationBucketsUserResponse
```

Get buckets current user

List all organizational storage buckets that the current user has access to. This function is only available through a JWT token.

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |
| `**kwargs` | ` ` |

| Returns                                                                                              |
| ---------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.list_organization_buckets_user_response.ListOrganizationBucketsUserResponse` |

#### list\_organization\_buckets\_user

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.list_organization_buckets_user(
	self,
	user_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='User ID')],
	**kwargs
) ‑> edgeimpulse_api.models.list_organization_buckets_user_response.ListOrganizationBucketsUserResponse
```

Get buckets

List all organizational storage buckets that a user has access to. This function is only available through a JWT token.

| Parameters |                                                                                                             |
| ---------- | ----------------------------------------------------------------------------------------------------------- |
| `self`     | ` `                                                                                                         |
| `user_id`  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='User ID')]` |
| `**kwargs` | ` `                                                                                                         |

| Returns                                                                                              |
| ---------------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.list_organization_buckets_user_response.ListOrganizationBucketsUserResponse` |

#### list\_organizations\_current\_user

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.list_organizations_current_user(
	self,
	**kwargs
) ‑> edgeimpulse_api.models.list_organizations_response.ListOrganizationsResponse
```

Get organizations

List all organizations that the current user is a member of. This function is only available through a JWT token.

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |
| `**kwargs` | ` ` |

| Returns                                                                        |
| ------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.list_organizations_response.ListOrganizationsResponse` |

#### list\_organizations\_user

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.list_organizations_user(
	self,
	user_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='User ID')],
	**kwargs
) ‑> edgeimpulse_api.models.list_organizations_response.ListOrganizationsResponse
```

Get organizations

List all organizations for a user. This function is only available through a JWT token.

| Parameters |                                                                                                             |
| ---------- | ----------------------------------------------------------------------------------------------------------- |
| `self`     | ` `                                                                                                         |
| `user_id`  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='User ID')]` |
| `**kwargs` | ` `                                                                                                         |

| Returns                                                                        |
| ------------------------------------------------------------------------------ |
| `edgeimpulse_api.models.list_organizations_response.ListOrganizationsResponse` |

#### request\_activation\_code\_current\_user

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.request_activation_code_current_user(
	self,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Request activation code

Request a new activation code for the current user. This function is only available through a JWT token.

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |
| `**kwargs` | ` ` |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### request\_activation\_code\_user

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.request_activation_code_user(
	self,
	user_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='User ID')],
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Request activation code

Request a new activation code. This function is only available through a JWT token.

| Parameters |                                                                                                             |
| ---------- | ----------------------------------------------------------------------------------------------------------- |
| `self`     | ` `                                                                                                         |
| `user_id`  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='User ID')]` |
| `**kwargs` | ` `                                                                                                         |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### request\_reset\_password

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.request_reset_password(
	self,
	request_reset_password_request: edgeimpulse_api.models.request_reset_password_request.RequestResetPasswordRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Request reset password

Request a password reset link for a user.

| Parameters                       |                                                                                     |
| -------------------------------- | ----------------------------------------------------------------------------------- |
| `self`                           | ` `                                                                                 |
| `request_reset_password_request` | `edgeimpulse_api.models.request_reset_password_request.RequestResetPasswordRequest` |
| `**kwargs`                       | ` `                                                                                 |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### reset\_password

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.reset_password(
	self,
	reset_password_request: edgeimpulse_api.models.reset_password_request.ResetPasswordRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Reset password

Reset the password for a user.

| Parameters               |                                                                      |
| ------------------------ | -------------------------------------------------------------------- |
| `self`                   | ` `                                                                  |
| `reset_password_request` | `edgeimpulse_api.models.reset_password_request.ResetPasswordRequest` |
| `**kwargs`               | ` `                                                                  |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### send\_user\_feedback

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.send_user_feedback(
	self,
	user_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='User ID')],
	send_user_feedback_request: edgeimpulse_api.models.send_user_feedback_request.SendUserFeedbackRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Send feedback

Send feedback to Edge Impulse or get in touch with sales.

| Parameters                   |                                                                                                             |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `self`                       | ` `                                                                                                         |
| `user_id`                    | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='User ID')]` |
| `send_user_feedback_request` | `edgeimpulse_api.models.send_user_feedback_request.SendUserFeedbackRequest`                                 |
| `**kwargs`                   | ` `                                                                                                         |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### send\_user\_upgrade\_request

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.send_user_upgrade_request(
	self,
	user_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='User ID')],
	enterprise_upgrade_or_trial_extension_request: edgeimpulse_api.models.enterprise_upgrade_or_trial_extension_request.EnterpriseUpgradeOrTrialExtensionRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Send upgrade request

Send an upgrade to Enterprise request to Edge Impulse.

| Parameters                                      |                                                                                                                 |
| ----------------------------------------------- | --------------------------------------------------------------------------------------------------------------- |
| `self`                                          | ` `                                                                                                             |
| `user_id`                                       | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='User ID')]`     |
| `enterprise_upgrade_or_trial_extension_request` | `edgeimpulse_api.models.enterprise_upgrade_or_trial_extension_request.EnterpriseUpgradeOrTrialExtensionRequest` |
| `**kwargs`                                      | ` `                                                                                                             |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### set\_user\_password

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.set_user_password(
	self,
	user_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='User ID')],
	set_user_password_request: edgeimpulse_api.models.set_user_password_request.SetUserPasswordRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Set password for SSO user

Set the password for a new SSO user. This function is only available through an SSO access token.

| Parameters                  |                                                                                                             |
| --------------------------- | ----------------------------------------------------------------------------------------------------------- |
| `self`                      | ` `                                                                                                         |
| `user_id`                   | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='User ID')]` |
| `set_user_password_request` | `edgeimpulse_api.models.set_user_password_request.SetUserPasswordRequest`                                   |
| `**kwargs`                  | ` `                                                                                                         |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### start\_enterprise\_trial

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.start_enterprise_trial(
	self,
	start_enterprise_trial_request: edgeimpulse_api.models.start_enterprise_trial_request.StartEnterpriseTrialRequest,
	**kwargs
) ‑> edgeimpulse_api.models.create_enterprise_trial_response.CreateEnterpriseTrialResponse
```

Start enterprise trial

Create an enterprise trial for the current user. Users can only go through a trial once.

| Parameters                       |                                                                                     |
| -------------------------------- | ----------------------------------------------------------------------------------- |
| `self`                           | ` `                                                                                 |
| `start_enterprise_trial_request` | `edgeimpulse_api.models.start_enterprise_trial_request.StartEnterpriseTrialRequest` |
| `**kwargs`                       | ` `                                                                                 |

| Returns                                                                                 |
| --------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.create_enterprise_trial_response.CreateEnterpriseTrialResponse` |

#### update\_current\_user

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.update_current_user(
	self,
	update_user_request: edgeimpulse_api.models.update_user_request.UpdateUserRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Update current user

Update user properties such as name. This function is only available through a JWT token.

| Parameters            |                                                                |
| --------------------- | -------------------------------------------------------------- |
| `self`                | ` `                                                            |
| `update_user_request` | `edgeimpulse_api.models.update_user_request.UpdateUserRequest` |
| `**kwargs`            | ` `                                                            |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### update\_user

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.update_user(
	self,
	user_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='User ID')],
	update_user_request: edgeimpulse_api.models.update_user_request.UpdateUserRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Update user

Update user properties such as name. This function is only available through a JWT token.

| Parameters            |                                                                                                             |
| --------------------- | ----------------------------------------------------------------------------------------------------------- |
| `self`                | ` `                                                                                                         |
| `user_id`             | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='User ID')]` |
| `update_user_request` | `edgeimpulse_api.models.update_user_request.UpdateUserRequest`                                              |
| `**kwargs`            | ` `                                                                                                         |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### upload\_photo\_current\_user

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.upload_photo_current_user(
	self,
	photo: Annotated[str, Strict(strict=True)],
	**kwargs
) ‑> edgeimpulse_api.models.upload_user_photo_response.UploadUserPhotoResponse
```

Upload photo

Upload a photo for the current user. This function is only available through a JWT token.

| Parameters |                                       |
| ---------- | ------------------------------------- |
| `self`     | ` `                                   |
| `photo`    | `Annotated[str, Strict(strict=True)]` |
| `**kwargs` | ` `                                   |

| Returns                                                                     |
| --------------------------------------------------------------------------- |
| `edgeimpulse_api.models.upload_user_photo_response.UploadUserPhotoResponse` |

#### upload\_photo\_user

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.upload_photo_user(
	self,
	user_id: Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='User ID')],
	photo: Annotated[str, Strict(strict=True)],
	**kwargs
) ‑> edgeimpulse_api.models.upload_user_photo_response.UploadUserPhotoResponse
```

Upload photo

Upload a photo for a user. This function is only available through a JWT token, and is not available for all users.

| Parameters |                                                                                                             |
| ---------- | ----------------------------------------------------------------------------------------------------------- |
| `self`     | ` `                                                                                                         |
| `user_id`  | `Annotated[int, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='User ID')]` |
| `photo`    | `Annotated[str, Strict(strict=True)]`                                                                       |
| `**kwargs` | ` `                                                                                                         |

| Returns                                                                     |
| --------------------------------------------------------------------------- |
| `edgeimpulse_api.models.upload_user_photo_response.UploadUserPhotoResponse` |

#### user\_cancel\_subscription

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.user_cancel_subscription(
	self,
	downgrade_subscription_request: edgeimpulse_api.models.downgrade_subscription_request.DowngradeSubscriptionRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Cancel subscription

Cancel the current subscription.

| Parameters                       |                                                                                      |
| -------------------------------- | ------------------------------------------------------------------------------------ |
| `self`                           | ` `                                                                                  |
| `downgrade_subscription_request` | `edgeimpulse_api.models.downgrade_subscription_request.DowngradeSubscriptionRequest` |
| `**kwargs`                       | ` `                                                                                  |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### user\_delete\_totp\_mfa\_key

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.user_delete_totp_mfa_key(
	self,
	user_delete_totp_mfa_key_request: edgeimpulse_api.models.user_delete_totp_mfa_key_request.UserDeleteTotpMfaKeyRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Remove TOTP MFA key

Disable MFA on this account using an TOTP token.

| Parameters                         |                                                                                       |
| ---------------------------------- | ------------------------------------------------------------------------------------- |
| `self`                             | ` `                                                                                   |
| `user_delete_totp_mfa_key_request` | `edgeimpulse_api.models.user_delete_totp_mfa_key_request.UserDeleteTotpMfaKeyRequest` |
| `**kwargs`                         | ` `                                                                                   |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### user\_dismiss\_notification

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.user_dismiss_notification(
	self,
	user_dismiss_notification_request: edgeimpulse_api.models.user_dismiss_notification_request.UserDismissNotificationRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Dismiss a notification

Dismiss a notification

| Parameters                          |                                                                                           |
| ----------------------------------- | ----------------------------------------------------------------------------------------- |
| `self`                              | ` `                                                                                       |
| `user_dismiss_notification_request` | `edgeimpulse_api.models.user_dismiss_notification_request.UserDismissNotificationRequest` |
| `**kwargs`                          | ` `                                                                                       |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### user\_generate\_new\_totp\_mfa\_key

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.user_generate_new_totp_mfa_key(
	self,
	**kwargs
) ‑> edgeimpulse_api.models.user_generate_new_mfa_key_response.UserGenerateNewMfaKeyResponse
```

Generate a new TOTP MFA key

Creates a new MFA key, only allowed if the user has no MFA configured. TOTP tokens use SHA-1 algorithm.

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |
| `**kwargs` | ` ` |

| Returns                                                                                   |
| ----------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.user_generate_new_mfa_key_response.UserGenerateNewMfaKeyResponse` |

#### user\_get\_subscription\_metrics

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.user_get_subscription_metrics(
	self,
	**kwargs
) ‑> edgeimpulse_api.models.user_subscription_metrics_response.UserSubscriptionMetricsResponse
```

Get user billable compute metrics

Get billable compute metrics for a user. This function is only available to users with an active subscription.

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |
| `**kwargs` | ` ` |

| Returns                                                                                     |
| ------------------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.user_subscription_metrics_response.UserSubscriptionMetricsResponse` |

#### user\_set\_totp\_mfa\_key

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.user_set_totp_mfa_key(
	self,
	user_set_totp_mfa_key_request: edgeimpulse_api.models.user_set_totp_mfa_key_request.UserSetTotpMfaKeyRequest,
	**kwargs
) ‑> edgeimpulse_api.models.user_set_totp_mfa_key_response.UserSetTotpMfaKeyResponse
```

Set TOTP MFA key

Enable MFA on this account using an TOTP token. First create a new key via `userGenerateNewTotpMfaKey`.

| Parameters                      |                                                                                 |
| ------------------------------- | ------------------------------------------------------------------------------- |
| `self`                          | ` `                                                                             |
| `user_set_totp_mfa_key_request` | `edgeimpulse_api.models.user_set_totp_mfa_key_request.UserSetTotpMfaKeyRequest` |
| `**kwargs`                      | ` `                                                                             |

| Returns                                                                           |
| --------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.user_set_totp_mfa_key_response.UserSetTotpMfaKeyResponse` |

#### user\_undo\_cancel\_subscription

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.user_undo_cancel_subscription(
	self,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Undo subscription cancellation

Stop a pending cancellation. If you schedule a subscription to be canceled, and the subscription hasn't yet reached the end of the billing period, you can stop the cancellation. After a subscription has been canceled, you can't reactivate it.

| Parameters |     |
| ---------- | --- |
| `self`     | ` ` |
| `**kwargs` | ` ` |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |

#### user\_upgrade\_subscription

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.user_upgrade_subscription(
	self,
	upgrade_subscription_request: edgeimpulse_api.models.upgrade_subscription_request.UpgradeSubscriptionRequest,
	**kwargs
) ‑> None
```

Upgrade subscription

Upgrade the current subscription.

| Parameters                     |                                                                                  |
| ------------------------------ | -------------------------------------------------------------------------------- |
| `self`                         | ` `                                                                              |
| `upgrade_subscription_request` | `edgeimpulse_api.models.upgrade_subscription_request.UpgradeSubscriptionRequest` |
| `**kwargs`                     | ` `                                                                              |

| Returns |
| ------- |
| `None`  |

#### verify\_reset\_password

```python  theme={"system"}
edgeimpulse_api.api.user_api.UserApi.verify_reset_password(
	self,
	verify_reset_password_request: edgeimpulse_api.models.verify_reset_password_request.VerifyResetPasswordRequest,
	**kwargs
) ‑> edgeimpulse_api.models.generic_api_response.GenericApiResponse
```

Verify reset password code

Verify whether the reset password code for the user is valid.

| Parameters                      |                                                                                   |
| ------------------------------- | --------------------------------------------------------------------------------- |
| `self`                          | ` `                                                                               |
| `verify_reset_password_request` | `edgeimpulse_api.models.verify_reset_password_request.VerifyResetPasswordRequest` |
| `**kwargs`                      | ` `                                                                               |

| Returns                                                          |
| ---------------------------------------------------------------- |
| `edgeimpulse_api.models.generic_api_response.GenericApiResponse` |


Built with [Mintlify](https://mintlify.com).