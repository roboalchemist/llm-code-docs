# Source: https://www.speakeasy.com/md/docs/speakeasy-reference/generation/go-config.md

# Go configuration options

This section details the available configuration options for the Go SDK. All configuration is managed in the `gen.yaml` file under the `go` section.

## Version and general configuration

```yml
go:
  version: 1.2.3
  modulePath: "github.com/my-company/company-go-sdk"
  sdkPackageName: "company"
```

| Name | Required | Default Value | Description |
| --- | --- | --- | --- |
| version | true | 0.0.1 | The current version of the SDK. |
| modulePath | true | github.com/my-company/company-go-sdk | Root module path. Use sdkPackageName to configure the package clause for the root module package. [Go Module Path documentation](https://go.dev/ref/mod#module-path). |
| sdkPackageName | true | company | Root module package name written in the package clause. Determines the package naming in consuming code if the modulePath does not end with a valid identifier. [Go Packages documentation](https://go.dev/ref/spec#Packages). |
| packageName | false |  | Legacy combined root module path and SDK package naming. Use sdkPackageAlias to update SDK package import aliases in documentation while preserving major version compatibility, otherwise migrate to modulePath and sdkPackageName. [Go Module Path documentation](https://go.dev/ref/mod#module-path). |
| sdkPackageAlias | false | openapi | Root module package import alias for documentation. Use this to preserve compatibility if the SDK has already had a stable major version release with modulePath, packageName, or sdkPackageName, as the package clause determines package naming in consuming code if the import path does not end in a valid identifier. [Go Packages documentation](https://go.dev/ref/spec#Packages). |

## Additional dependencies

```yml
go:
  additionalDependencies:
    axios: "0.21.0"
```

| Name | Required | Default Value | Description |
| --- | --- | --- | --- |
| additionalDependencies | false | {} | Add additional dependencies to include in the generated `go.mod`. |

## Retractions

You can use retractions to mark specific versions of your Go module as unsuitable for use. Each retraction requires a version and can optionally include a comment explaining why the version was retracted.

```yml
go:
  retractions:
    - version: v1.0.0
      comment: Published accidentally
    - version: v1.0.1
```

| Name | Required | Default Value | Description |
| --- | --- | --- | --- |
| version | true |  | The version to retract. Must be a valid semantic version. |
| comment | false |  | Optional comment explaining why the version was retracted. |

## Method and parameter management

```yml
go
  maxMethodParams: 4
  methodArguments: "require-security-and-request"
```

| Name | Required | Default Value | Description |
| --- | --- | --- | --- |
| [maxMethodParams](/docs/customize/methods) | false | 4 | The maximum number of parameters a method can have before the resulting SDK endpoint is no longer "flattened" and an input object is created. `0` will use input objects always. Must match the regex pattern `/^\d+$/`. |
| methodArguments | false | require-security-and-request | Determines how arguments for SDK methods are generated. Options: `"infer-optional-args"` or `"require-security-and-request"`. |

## Security configuration

```yml
go
  envVarPrefix: SPEAKEASY
  flattenGlobalSecurity: true
```

| Name | Required | Default Value | Description |
| --- | --- | --- | --- |
| clientServerStatusCodesAsErrors | false | true | Whether to treat `4xx` and `5xx` status codes as errors. |
| [flattenGlobalSecurity](/docs/customize/authentication/overview) | false | newSDK | Flatten the global security configuration if there is only a single option in the spec. |

## Import management

```yml
go
  imports:
    paths:
      callbacks: models/callbacks
      errors: models/errors
      operations: models/operations
      shared: models/components
      webhooks: models/webhooks
```

| Path | Default Value | Description |
| --- | --- | --- |
| shared | models/components | The directory for shared components, such as reusable schemas, and data models. |
| operations | models/operations | The directory where operation models (i.e., API endpoints) will be imported from. |
| errors | models/sdkerrors | The directory where error models will be imported from. |
| callbacks | models/callbacks | The directory where callback models will be imported from. |
| webhooks | models/webhooks | The directory where webhook models will be imported from. |

## Error and response handling

```yml
go:
  responseFormat: "envelope-http"
```

| Name | Required | Default Value | Description |
| --- | --- | --- | --- |
| [responseFormat](/docs/customize/responses/responses) | false | envelope-http | Determines the shape of the response envelope that is returned from SDK methods. Must be `envelope-http`, `envelope`, or `flat` only. |

## Nullable and optional field handling

```yml
go:
  nullableOptionalWrapper: true
```

| Name | Required | Default Value | Description |
| --- | --- | --- | --- |
| nullableOptionalWrapper | false | newSDK | When enabled, fields that are both optional and nullable in the source schema are generated using a wrapper type with explicit presence semantics: `optionalnullable.OptionalNullable[T]`. Defaults to `true` for new Go SDKs and `false` for existing SDKs to avoid breaking changes. |

### When it applies

The wrapper is generated only for fields that are:

- Optional (the property is not listed in the parent schema's `required` array)
- Nullable (the property `type` includes `"null"` in OpenAPI 3.1)

For example, the following JSON Schema (OpenAPI 3.1) defines an optional, nullable `nickname`:

```yaml
type: object
required:
  - id
properties:
  id:
    type: string
  nickname:
    type:
      - string
      - "null"
```

### Generated code

With `nullableOptionalWrapper: true`, the corresponding Go model uses a wrapper type:

```go
type Pet struct {
    ID       string                                    `json:"id"`
    Nickname optionalnullable.OptionalNullable[string] `json:"nickname,omitempty"`
}
```

Without the wrapper (when disabled for existing SDKs), the same field may be generated as a pointer type.

### Using the wrapper

Set values using helper constructors on `OptionalNullable` and retrieve values via `Get()`, which returns `(*T, bool)` — `ok` indicates presence, and a `nil` pointer indicates an explicit null value:

```go
// Set a present, non-null value
pet := shared.Pet{}
nickname := "Finn"
pet.Nickname = optionalnullable.From(&nickname)

// Read a value
if val, ok := pet.Nickname.Get(); ok {
    if val == nil {
        fmt.Println("nickname is explicitly null")
    } else {
        fmt.Println("nickname:", *val)
    }
} else {
    fmt.Println("nickname not set")
}
```

Enabling this flag changes the generated field type and how values are set and read. This is a breaking change for existing SDKs and requires migrating code that accessed those fields directly or through pointer checks to use `optionalnullable.From(...)` and `.Get()`.
---

Are you an AI agent evaluating Speakeasy? We put together a helpful guide: https://www.speakeasy.com/eval.md
