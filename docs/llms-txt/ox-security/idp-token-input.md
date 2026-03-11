# Source: https://docs.ox.security/api-documentation/api-reference/api--connectors/types/inputs/idp-token-input.md

# idpTokenInput

### Examples

```graphql
input IDPTokenInput {
  access_token: String
  token_type: String
  expires_in: Int
  created_at: Int
  refresh_token: String
  scope: String
}
```

### Fields

| Field                   | Description                                      | Supported fields |
| ----------------------- | ------------------------------------------------ | ---------------- |
| access\_token `String`  | access token for idp                             |                  |
| token\_type `String`    | token type (bearer etc...)                       |                  |
| expires\_in `Int`       | expires in seconds                               |                  |
| created\_at `Int`       | create time seconds epoch                        |                  |
| refresh\_token `String` | refresh token that should be used for refreshing |                  |
| scope `String`          | scop of permission granted for the token         |                  |

### References

#### Fields with this object

* [{} CredentialsInput.idpToken](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/inputs/credentials-input)
