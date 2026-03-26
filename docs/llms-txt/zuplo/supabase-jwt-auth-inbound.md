# Source: https://www.zuplo.com/docs/policies/supabase-jwt-auth-inbound.md

# Supabase JWT Auth Policy

The Supabase JWT Authentication policy allows you to authenticate incoming
requests using a token created by [supabase.com](https://supabase.com).

When configured, you can have Zuplo check incoming requests for a JWT token and
automatically populate the `ZuploRequest`'s `user` property with a user object.

This `user` object will have a `sub` property - taking the `sub` id from the JWT
token. It will also have a `data` property populated by other data returned in
the JWT token - including all your claims, `user_metadata` and `app_metadata`.

You can also require specific claims to have specific values to allow
authentication to complete, providing a layer of authorization.

## Configuration

The configuration shows how to configure the policy in the 'policies.json' document.

```json title="config/policies.json"
{
  "name": "my-supabase-jwt-auth-inbound-policy",
  "policyType": "supabase-jwt-auth-inbound",
  "handler": {
    "export": "SupabaseJwtInboundPolicy",
    "module": "$import(@zuplo/runtime)",
    "options": {
      "allowUnauthenticatedRequests": false,
      "oAuthResourceMetadataEnabled": false,
      "requiredClaims": {
        "claim_1": ["valid_value_1", "valid_value_2"]
      },
      "secret": "$env(SUPABASE_JWT_SECRET)"
    }
  }
}
```

### Policy Configuration

- `name` <code className="text-green-600">&lt;string&gt;</code> - The name of your policy instance. This is used as a reference in your routes.
- `policyType` <code className="text-green-600">&lt;string&gt;</code> - The identifier of the policy. This is used by the Zuplo UI. Value should be `supabase-jwt-auth-inbound`.
- `handler.export` <code className="text-green-600">&lt;string&gt;</code> - The name of the exported type. Value should be `SupabaseJwtInboundPolicy`.
- `handler.module` <code className="text-green-600">&lt;string&gt;</code> - The module containing the policy. Value should be `$import(@zuplo/runtime)`.
- `handler.options` <code className="text-green-600">&lt;object&gt;</code> - The options for this policy. [See Policy Options](#policy-options) below.

### Policy Options

The options for this policy are specified below. All properties are optional unless specifically marked as required.

- `secret` **(required)** <code className="text-green-600">&lt;string&gt;</code> - The key used to verify the signature of the JWT token.
- `allowUnauthenticatedRequests` <code className="text-green-600">&lt;boolean&gt;</code> - Indicates whether the request should continue if authentication fails. Default is `false` which means unauthenticated users will automatically receive a 401 response. Defaults to `false`.
- `requiredClaims` <code className="text-green-600">&lt;object&gt;</code> - Any claims that must be present for authentication to succeed - multiple valid values can be specified for each claim.
- `oAuthResourceMetadataEnabled` <code className="text-green-600">&lt;boolean&gt;</code> - Flag that determines whether OAuth protected resource metadata is enabled. Defaults to `false`.

## Using the Policy

## Authorization

You can also require certain claims to be valid by specifying this in the
options. For example, if you require the claim `user_role` to be either `admin`
or `supa_user`, you would configure the policy as follows:

```json
{
  "export": "SupabaseJwtInboundPolicy",
  "module": "$import(@zuplo/runtime)",
  "options": {
    "secret": "$env(SUPABASE_JWT_SECRET)",
    "allowUnauthenticatedRequests": false,
    "requiredClaims": {
      "user_role": ["admin", "supa_user"]
    }
  }
}
```

## OAuth 2.0 Protected Resource Metadata

The Supabase JWT Auth policy supports OAuth protected resource metadata
discovery. To enable this feature, set the `oAuthResourceMetadataEnabled` option
to `true` and add the
[`OAuthProtectedResourcePlugin` to `modules/zuplo.runtime.ts`](/docs/programmable-api/oauth-protected-resource-plugin).
When configured, this enables OAuth clients to find metadata information about
how to interact with your OAuth 2.0 protected resources according to
[`RFC 9728`](https://datatracker.ietf.org/doc/html/rfc9728).

Read more about [how policies work](/articles/policies)
