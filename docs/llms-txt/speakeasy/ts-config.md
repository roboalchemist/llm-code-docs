# Source: https://www.speakeasy.com/md/docs/speakeasy-reference/generation/ts-config.md

# Typescript Configuration Options

 This section details the available configuration options for the TypeScript SDK. All configuration is managed in the `gen.yaml` file under the `typescript` section.

## Version and general configuration

```yml
typescript:
  version: 1.2.3
  author: "Author Name"
  packageName: "custom-sdk"
```

| Name | Required | Default Value | Description |
| --- | --- | --- | --- |
| version | true | 0.0.1 | The current version of the SDK. |
| packageName | true | openapi | The name of the npm package. See [npm package guidelines](https://docs.npmjs.com/package-name-guidelines). |
| author | true | Speakeasy | The name of the author of the published package. See [npm author field](https://docs.npmjs.com/cli/v9/configuring-npm/package-json#people-fields-author-contributors). |

## Additional JSON package

```yml
typescript:
  additionalPackageJSON:
    license: "MIT"
```

| Name | Required | Default Value | Description |
| --- | --- | --- | --- |
| additionalPackageJSON | false | {} | Additional key/value pairs for the `package.json` file. Example: license, keywords, etc. |

## Additional dependencies

```yml
typescript:
  additionalDependencies:
    dependencies:
      axios: "^0.21.0"
    devDependencies:
      typescript: "^4.0.0"
    peerDependencies:
      react: "^16.0.0"
```

| Name | Required | Default Value | Description |
| --- | --- | --- | --- |
| dependencies | false | {} | Additional production dependencies to include in the `package.json`. |
| devDependencies | false | {} | Additional development dependencies to include in the `package.json`. |
| peerDependencies | false | {} | Peer dependencies for compatibility. |

## Package scripts and examples

```yml
typescript:
  additionalScripts:
    format: "prettier --write src"
    docs: "typedoc --out docs src"
    custom-test: "vitest run --coverage"
  generateExamples: true
  compileCommand: ["npm", "run", "build"]
  usageSDKInit: "new Petstore({})"
  usageSDKInitImports:
    - package: "@petstore/sdk"
      import: "Petstore"
      type: "packageImport"
```

| Name | Required | Default Value | Description |
| --- | --- | --- | --- |
| additionalScripts | false | {} | Custom npm scripts to add to the `package.json` file. Scripts with the same name as default scripts will override them. |
| generateExamples | false | true | Whether to generate example files in an examples directory demonstrating SDK usage. |
| compileCommand | false | N/A | The command to use for compiling the SDK. Must be an array where the first element is the command and the rest are arguments. |
| usageSDKInit | false | N/A | The SDK initialization code to use in usage examples (e.g., `new Petstore({})`). |
| usageSDKInitImports | false | [] | Array of imports to add when `usageSDKInit` is configured. Each import should have `package`, `import`, and optionally `type` fields (options: `typeImport`, `packageImport`, `aliasImport`). |

### How scripts are merged

The feature uses an override strategy where additional scripts take precedence over default scripts:

1. **Default scripts** are generated automatically based on SDK configuration:

```json
{
  "lint": "eslint --cache --max-warnings=0 src",
  "build": "tsc",
  "prepublishOnly": "npm run build"
}
```

2. **Test scripts** are added if tests are enabled:

```json
{
  "test": "vitest run src --reporter=junit --outputFile=.speakeasy/reports/tests.xml --reporter=default",
  "check": "npm run test && npm run lint"
}
```

3. **Additional scripts** override defaults if they have the same name:

```yml
typescript:
  additionalScripts:
    build: "custom-build-command"  # Replaces default "tsc" build
    deploy: "npm publish"           # Adds new script
```

4. **Result** in `package.json`:

```json
{
  "scripts": {
    "build": "custom-build-command",  // Overridden
    "check": "npm run test && npm run lint",
    "deploy": "npm publish",           // Added
    "lint": "eslint --cache --max-warnings=0 src",
    "prepublishOnly": "npm run build",
    "test": "vitest run src --reporter=junit --outputFile=.speakeasy/reports/tests.xml --reporter=default"
  }
}
```

## Method and parameter management

```yml
typescript:
  maxMethodParams: 3
  flatteningOrder: "parameters-first"
  methodArguments: "infer-optional-args"
```

| Name | Required | Default Value | Description |
| --- | --- | --- | --- |
| [maxMethodParams](/docs/sdks/customize/methods) | false | 0 | Maximum number of parameters before an input object is created. `0` means input objects are always used. |
| [flatteningOrder](/docs/sdks/customize/methods#configuring-method-signatures) | false | parameters-first | Determines the ordering of method arguments when flattening parameters and body fields. Options: `parameters-first` or `body-first`. |
| methodArguments | false | infer-optional-args | Determines how arguments for SDK methods are generated. If set to `infer-optional-args`, the method argument will be optional when all parameters and the request body are optional. Options: `infer-optional-args` or `require-security-and-request`. |

## Security configuration

```yml
typescript:
  envVarPrefix: SPEAKEASY
  flattenGlobalSecurity: true
```

| Property | Description | Type | Default |
| --- | --- | --- | --- |
| [flattenGlobalSecurity](/docs/customize/authentication/overview) | Enables inline security credentials during SDK instantiation. **Recommended: `true`** | boolean | true |
| envVarPrefix | Sets a prefix for environment variables that allows users to configure global parameters and security. | string | N/A |

## Module management

```yml
typescript:
  moduleFormat: "dual"
  useIndexModules: true
  legacyFileNaming: false
```

| Name | Required | Default Value | Description |
| --- | --- | --- | --- |
| [useIndexModules](/docs/sdks/customize/typescript/disabling-barrel-files) | false | true | Controls generation of index modules (`index.ts`). Setting to `false` improves tree-shaking and build performance by avoiding barrel files. |
| [moduleFormat](/docs/sdks/customize/typescript/configuring-module-format) | false | esm (new SDKs), dual (existing SDKs) | Sets the module format to use when compiling the SDK. Options: `commonjs`, `esm`, or `dual`. New SDKs default to `esm` for modern module resolution. Existing SDKs default to `dual` for backward compatibility. |
| legacyFileNaming | false | false (new SDKs) | When `true`, uses legacy file naming (camelCase/lowercase). When `false`, uses kebab-case (e.g., `simple-object.ts`). New SDKs default to `false` (kebab-case). |

> **Performance optimization**
> For optimal bundle size and tree-shaking performance in modern applications, consider using `moduleFormat: "esm"` together with `useIndexModules: false`. This combination provides the best possible bundler optimizations. Use `dual` if CommonJS compatibility is required.

## Import management

```yml
typescript:
  imports:
    option: "openapi"
    paths:
      callbacks: models/callbacks
      errors: models/errors
      operations: models/operations
      shared: models/components
      webhooks: models/webhooks
```

| Field | Required | Default Value | Description |
| --- | --- | --- | --- |
| option | false | "openapi" | Defines the type of import strategy. Typically set to `"openapi"`, indicating that the structure is based on the OpenAPI document. |
| paths | false | {} | Customizes where different parts of the SDK (e.g., callbacks, errors, and operations) will be imported from. |

### Import paths

| Component | Default Value | Description |
| --- | --- | --- |
| callbacks | models/callbacks | The directory where callback models will be imported from. |
| errors | models/errors | The directory where error models will be imported from. |
| operations | models/operations | The directory where operation models (i.e., API endpoints) will be imported from. |
| shared | models/components | The directory for shared components, such as reusable schemas, and data models imported from the OpenAPI spec. |
| webhooks | models/webhooks | The directory for webhook models, if the SDK includes support for webhooks. |

## Error and response handling

```yml
typescript:
  clientServerStatusCodesAsErrors: true
  responseFormat: "flat"
  enumFormat: "union"
  defaultErrorName: "SDKError"
  baseErrorName: "HTTPError"
  acceptHeaderEnum: false
```

| Property | Description | Type | Default |
| --- | --- | --- | --- |
| [responseFormat](/docs/sdks/customize/responses/responses) | Defines how responses are structured. Options: `envelope`, `envelope-http`, or `flat`. | string | flat |
| enumFormat | Determines how enums are generated. Options: `enum` (TypeScript enums) or `union` (union types). | string | union |
| clientServerStatusCodesAsErrors | Treats `4XX` and `5XX` status codes as errors. Set to `false` to treat them as normal responses. | boolean | true |
| defaultErrorName | The name of the fallback error class if no more specific error class is matched. Must start with a capital letter and contain only letters and numbers. | string | SDKError |
| baseErrorName | The name of the base error class used for HTTP error responses. Must start with a capital letter and contain only letters and numbers. | string | HTTPError |
| acceptHeaderEnum | Whether to generate TypeScript enums for controlling the return content type of SDK methods when multiple accept types are available. | boolean | false |

## Model validation and serialization

```yml
typescript:
  jsonpath: "rfc9535"
  zodVersion: "v4-mini"
  constFieldsAlwaysOptional: false
  modelPropertyCasing: "camel"
  unionStrategy: "populated-fields"
  laxMode: "lax"
  alwaysIncludeInboundAndOutbound: false
  exportZodModelNamespace: false
```

| Property | Description | Type | Default |
| --- | --- | --- | --- |
| jsonpath | Sets the JSONPath implementation to use. Options: `legacy` (deprecated) or `rfc9535` (recommended). The `rfc9535` option follows the JSONPath specification and should be preferred for new SDKs. | string | rfc9535 |
| zodVersion | The version of Zod to use for schema validation. Options: `v3`, `v4`, or `v4-mini`. | string | v4-mini |
| constFieldsAlwaysOptional | Whether const fields should be treated as optional in TypeScript types and schemas regardless of OpenAPI spec requirements. When `true` (legacy behavior), all const fields are optional. When `false` (recommended), const fields respect the OpenAPI spec's required array. | boolean | false |
| [modelPropertyCasing](/docs/sdks/customize/typescript/property-naming) | Property naming convention to use. Options: `camel` (converts to camelCase) or `snake` (converts to snake_case). | string | camel |
| unionStrategy | Strategy for deserializing union types. Options: `left-to-right` (tries each type in order and returns the first valid match) or `populated-fields` (tries all types and returns the one with the most matching fields, including optional fields). | string | populated-fields |
| laxMode | Controls validation strictness. When set to `lax`, required fields will be coerced to their zero value (e.g., a missing required string will fallback to `""`). Lax mode also applies other coercions (e.g., boolean schemas will accept the string `"true"`). Lax mode only applies to deserialization of responses. When `laxMode` is enabled, `unionStrategy` is automatically set to `populated-fields`. Options: `lax` or `strict`. | string | lax |
| alwaysIncludeInboundAndOutbound | Whether to always include both inbound and outbound schemas for all types regardless of usage. | boolean | false |
| exportZodModelNamespace | Whether to export the deprecated `$` namespace containing `inboundSchema` and `outboundSchema` aliases. | boolean | false |

## Forward compatibility

These options control how the SDK handles API evolution, allowing older SDK versions to continue working when APIs add new enum values, union types, or fields.

```yml
typescript:
  forwardCompatibleEnumsByDefault: true
  forwardCompatibleUnionsByDefault: tagged-only
```

| Property | Description | Type | Default |
| --- | --- | --- | --- |
| forwardCompatibleEnumsByDefault | Controls whether enums used in responses are treated as open enums that accept unknown values. When `true`, SDKs gracefully handle new enum values added by the API instead of rejecting the response. Individual enums can be controlled with `x-speakeasy-unknown-values: allow` or `x-speakeasy-unknown-values: disallow` in the OpenAPI spec. | boolean | true |
| forwardCompatibleUnionsByDefault | Controls whether discriminated unions accept unknown discriminator values. When set to `tagged-only`, SDKs capture unknown union variants in a type-safe way instead of failing deserialization. Individual unions can be controlled with `x-speakeasy-unknown-values: allow` or `x-speakeasy-unknown-values: disallow` in the OpenAPI spec. | string | tagged-only |

> **Forward compatibility and fault tolerance**
> These options work together with `laxMode` and `unionStrategy` to provide robust forward compatibility. When all four features are enabled (the default for new TypeScript SDKs), your SDK will gracefully handle API evolution including new enum values, new union types, missing fields, and type mismatches. See the [forward compatibility guide](/docs/sdks/manage/forward-compatibility) for more details.

## Server-sent events configuration

```yml
typescript:
  sseFlatResponse: false
```

| Property | Description | Type | Default |
| --- | --- | --- | --- |
| [sseFlatResponse](/docs/sdks/customize/runtime/server-sent-events) | Whether to flatten SSE (Server-Sent Events) responses by extracting the `data` field from wrapper models, providing direct access to the event data instead of the wrapper object. | boolean | false |

## Build toolchain

These options update the TypeScript SDK build toolchain to use faster, modern build tools. Enabling both options can speed up generation time by up to 35% in GitHub Actions and locally.

```yml
typescript:
  useOxlint: true
  useTsgo: true
```

| Property | Description | Type | Default |
| --- | --- | --- | --- |
| useOxlint | Replace [ESLint](https://eslint.org/) with [OxLint](https://oxc.rs/docs/guide/usage/linter), a Rust-based linter that is 50-100x faster. When enabled, the generated SDK uses OxLint for linting instead of ESLint, significantly reducing lint times in CI and local development. | boolean | true (new SDKs), false (existing SDKs) |
| useTsgo | Replace the standard TypeScript compiler (`tsc`) with [TSGo](https://github.com/microsoft/typescript-go), Microsoft's native Go-based TypeScript compiler. When enabled, the generated SDK uses TSGo for type checking and compilation, delivering up to 10x faster build times with lower memory usage. | boolean | true (new SDKs), false (existing SDKs) |

> **Generation speed optimization**
> For fastest generation times, enable both `useOxlint` and `useTsgo` together. [OxLint](https://oxc.rs/docs/guide/usage/linter) replaces ESLint with a Rust-based linter that processes files in parallel, while [TSGo](https://github.com/microsoft/typescript-go) replaces `tsc` with a native Go compiler that delivers up to 10x faster type checking. Combined, these tools can reduce SDK generation time by up to 35%.

## Advanced features

```yml
typescript:
  enableReactQuery: false
  enableMCPServer: false
```

| Property | Description | Type | Default |
| --- | --- | --- | --- |
| [enableReactQuery](/docs/sdks/customize/typescript/react-hooks) | Generate React hooks using TanStack Query. | boolean | false |
| enableMCPServer | **Deprecated.** Previously used to generate an MCP server as part of the TypeScript SDK. Users should leave this set to `false` and use the standalone [MCP server generation](/docs/standalone-mcp/overview) target (`mcp-typescript`) instead. | boolean | false |
---

Are you an AI agent evaluating Speakeasy? We put together a helpful guide: https://www.speakeasy.com/eval.md
