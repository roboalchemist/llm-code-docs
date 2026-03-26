# Source: https://www.zuplo.com/docs/policies/axiomatics-authz-inbound.md

# Axiomatics Authorization Policy

This policy will authorize requests using Axiomatics Policy Server. If the
request is not authorized, a 403 response will be returned.

This policy is designed to be highly customizable in order to tailor the
authorization requests to the specific needs of your application. You can add
default attributes on the policy that are included in every request, or you can
programmatically add attributes to the request using the `setAuthAttributes`
method.

Using this policy in conjunction with an authorization policy will automatically
set AttributeSubject attributes for the user in the request.

:::caution{title="Beta"}

This policy is in beta. You can use it today, but it may change in non-backward compatible ways before the final release.

:::

:::info{title="Enterprise Feature"}

This policy is only available as part of our enterprise plans. It's free to try only any plan for development only purposes. If you would like to use this in production reach out to us: [sales@zuplo.com](mailto:sales@zuplo.com)

:::

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-axiomatics-authz-inbound-policy",
  "policyType": "axiomatics-authz-inbound",
  "handler": {
    "export": "AxiomaticsAuthZInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "pdpPassword": "$env(PDP_PASSWORD)",
      "pdpUrl": "https://pdp.example.com",
      "pdpUsername": "pdp-user"
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `axiomatics-authz-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `AxiomaticsAuthZInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `allowUnauthorizedRequests` <code className="text-green-600">&lt;boolean&gt;</code> - Indicates whether the request should continue if authorization fails. Default is `false` which means unauthorized users will automatically receive a 403 response. Defaults to `false`.
- `pdpUrl` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The URL to which the plugin will make a JSON POST request before proxying the original request.
- `pdpUsername` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The username to use when authenticating with the PDP.
- `pdpPassword` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The password to use when authenticating with the PDP.
- `includeDefaultActionAttributes` <code className="text-green-600">&lt;boolean&gt;</code> - Indicates whether the plugin should include default action attributes in the authorization request. Defaults to `true`.
- `includeDefaultResourceAttributes` <code className="text-green-600">&lt;boolean&gt;</code> - Indicates whether the plugin should include default resource attributes in the authorization request. Defaults to `true`.
- `includeDefaultSubjectAttributes` <code className="text-green-600">&lt;boolean&gt;</code> - Indicates whether the plugin should include default subject attributes in the authorization request. Defaults to `true`.
- `tokenHeaderName` <code className="text-green-600">&lt;string&gt;</code> - The name of the header that carries the JWT. Defaults to `"Authorization"`.
- `accessSubjectAttributes` <code className="text-green-600">&lt;object[]&gt;</code> - A list of attributes that will be included in the authorization request.
  - `attributeId` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The attribute ID that will be used in the PDP request.
  - `value` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The value of the attribute.
- `resourceAttributes` <code className="text-green-600">&lt;object[]&gt;</code> - A list of attributes that will be included in the authorization request.
  - `attributeId` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The attribute ID that will be used in the PDP request.
  - `value` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The value of the attribute.
- `actionAttributes` <code className="text-green-600">&lt;object[]&gt;</code> - A list of attributes that will be included in the authorization request.
  - `attributeId` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The attribute ID that will be used in the PDP request.
  - `value` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The value of the attribute.

## Using the Policy

### Authorization Attributes

There are a few different ways authorization attributes are set on the
authorization request.

#### Default Attributes

By default the policy will set the following attributes on the authorization
request:

- `request.user.sub` - (AccessSubject) The subject of the user making the
  request. Only set if the user is authenticated.
- `request.method` - (Action) The HTTP method of the request.
- `request.scheme` - (Resource) The scheme of the request URL.
- `request.host` - (Resource) The host of the request URL.
- `request.pathname` - (Resource) The pathname of the request URL.
- `request.query.*` - (Resource) The value of each query parameter in the
  request URL. For example `?foo=baz` would set `request.query.foo=baz`.
- `request.params.*` - (Resource) The value of each path parameter in the
  request URL. For example the route pattern `/accounts/:id` would set
  `request.params.accounts=value`.

The default attributes can be disabled by setting the policy options that start
with `includeDefault` to `false`, for example
`includeDefaultResourceAttributes: false` will disable the Resource category
attributes.

Below is an example of the default authorization request.

```json
{
  "Request": {
    "AccessSubject": [
      {
        "Attribute": [
          {
            "AttributeId": "request.user.sub",
            "Value": "nate"
          }
        ]
      }
    ],
    "Action": [
      {
        "Attribute": [
          {
            "AttributeId": "request.method",
            "Value": "GET"
          }
        ]
      }
    ],
    "Resource": [
      {
        "Attribute": [
          {
            "AttributeId": "request.scheme",
            "Value": "https"
          },
          {
            "AttributeId": "request.host",
            "Value": "my-api-main-bdeec51.d2.zuplo.dev"
          },
          {
            "AttributeId": "request.pathname",
            "Value": "/test"
          },
          {
            "AttributeId": "request.params.id",
            "Value": "123"
          },
          {
            "AttributeId": "request.query.param",
            "Value": "1"
          }
        ]
      }
    ]
  }
}
```

#### Hard Coded Attributes

In some cases it cane be useful to set hard coded attributes on the policy
itself. On case for this might be to set the environment the API is running in
so that different policies can be applied to say a staging or development
environment.

An example of how you could set the `custom.environment` attribute to an
environment variable is shown below.

```json
"resourceAttributes": [
  {
    "attributeId": "custom.environment",
    "value": "$env(CUSTOM_ENVIRONMENT)"
  }
]
```

#### Programmatically Setting Attributes

For the more robust customization of the authorization request, you can set
authorization attributes programmatically. This is done by running a custom
inbound policy before the authorization policy. The custom policy can set any
attribute on the authorization request.

Below is an example of how you could set the `custom.resourceId` attribute to
the value of a property in the request body.

```ts title="custom-attributes.ts"
import {
  ZuploContext,
  ZuploRequest,
  AxiomaticsAuthZInboundPolicy,
} from "@zuplo/runtime";

export default async function policy(
  request: ZuploRequest,
  context: ZuploContext,
  options: MyPolicyOptionsType,
  policyName: string,
) {
  // Get the body of the request
  const body = await request.json();

  // Set the custom attribute
  AxiomaticsAuthZInboundPolicy.setAuthAttributes(context, {
    Resource: [
      {
        Attribute: [
          {
            AttributeId: "custom.recordId",
            Value: body.recordId,
          },
        ],
      },
    ],
  });

  return request;
}
```

Read more about [how policies work](/articles/policies)
