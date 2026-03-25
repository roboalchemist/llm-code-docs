# Source: https://docs.edgeimpulse.com/tools/libraries/api-bindings/studio/python/edgeimpulse_api/api/login_api.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.edgeimpulse.com/llms.txt
> Use this file to discover all available pages before exploring further.

# edgeimpulse_api.api.login_api

## Classes

### LoginApi

```python  theme={"system"}
edgeimpulse_api.api.login_api.LoginApi(
	api_client=None
)
```

| Parameters        |     |
| ----------------- | --- |
| `api_client=None` | ` ` |

***

**METHODS**

#### get\_sso\_domain\_id\_ps

```python  theme={"system"}
edgeimpulse_api.api.login_api.LoginApi.get_sso_domain_id_ps(
	self,
	username_or_email: Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Username or email')],
	**kwargs
) ‑> edgeimpulse_api.models.get_sso_domain_id_ps_response.GetSSODomainIdPsResponse
```

Get SSO settings for a user or email domain

Get the list of identity providers enabled for a user or a given email domain.

| Parameters          |                                                                                                                       |
| ------------------- | --------------------------------------------------------------------------------------------------------------------- |
| `self`              | ` `                                                                                                                   |
| `username_or_email` | `Annotated[str, Strict(strict=True), FieldInfo(annotation=NoneType, required=True, description='Username or email')]` |
| `**kwargs`          | ` `                                                                                                                   |

| Returns                                                                         |
| ------------------------------------------------------------------------------- |
| `edgeimpulse_api.models.get_sso_domain_id_ps_response.GetSSODomainIdPsResponse` |

#### login

```python  theme={"system"}
edgeimpulse_api.api.login_api.LoginApi.login(
	self,
	get_jwt_request: edgeimpulse_api.models.get_jwt_request.GetJWTRequest,
	**kwargs
) ‑> edgeimpulse_api.models.get_jwt_response.GetJWTResponse
```

Get JWT token

Get a JWT token to authenticate with the API.

| Parameters        |                                                        |
| ----------------- | ------------------------------------------------------ |
| `self`            | ` `                                                    |
| `get_jwt_request` | `edgeimpulse_api.models.get_jwt_request.GetJWTRequest` |
| `**kwargs`        | ` `                                                    |

| Returns                                                  |
| -------------------------------------------------------- |
| `edgeimpulse_api.models.get_jwt_response.GetJWTResponse` |


Built with [Mintlify](https://mintlify.com).