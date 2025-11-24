# Source: https://infisical.com/docs/documentation/platform/secret-versioning.md

# Secret Versioning

> Learn how secret versioning works in Infisical.

Every time a secret change is performed, a new version of the same secret is created.

Such versions can be accessed visually by opening up the [secret sidebar](/documentation/platform/project#drawer) (as seen below) or [retrieved via API](/api-reference/endpoints/secrets/read)
by specifying the `version` query parameter.

<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/secret-versioning-overview.png" alt="secret versioning overview" />
<img src="https://mintlify.s3.us-west-1.amazonaws.com/infisical/images/platform/secret-versioning.png" alt="secret versioning" />

The secret versioning functionality is heavily connected to [Point-in-time Recovery](/documentation/platform/pit-recovery) of secrets in Infisical.

<Note>
  You can copy and paste a secret version value to the "Value" input field "roll
  back" to that secret version. This creates a new secret version at the top of
  the stack. We're releasing the ability to automatically roll back to
  a secret version soon.
</Note>
