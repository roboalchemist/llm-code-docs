# Source: https://relay.dev/docs/getting-started/compiler-config/

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Get Started]
-   [Compiler Configuration]

[Version: v20.1.0]

On this page

<div>

# Compiler Configuration

</div>

## Compiler Config Options[​](#compiler-config-options "Direct link to Compiler Config Options") 

For information about where the Relay compiler looks for its config file, or a minimal config, see the [Relay Compiler](/docs/guides/compiler/#Configuration) page.

If you need more advanced options of the Relay Compiler Config, the exhaustive full schema can be found below. The shape of the Relay Compiler Config is given as `ConfigFile`. Note that while the shapes are documented in pseudo TypeScript, the compiler is parsing them in Rust so some subtle differences may exist.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6Ij48L3BhdGg+PC9zdmc+)]tip

Install the [Relay VSCode extension](/docs/editor-support/) to get autocomplete, hover tips, and type checking for the options in your Relay config.

<div>

## Config File 

Relay\'s configuration file. Supports a single project config for simple use cases and a multi-project config for cases where multiple projects live in the same repository. In general, start with the SingleProjectConfigFile.

<div>

type ConfigFile =

// Base case configuration (mostly of OSS) where the project have single schema, and single source directory

\| [[SingleProjectConfigFile](#SingleProjectConfigFile)]

// Relay can support multiple projects with multiple schemas and different options (output, typegen, etc\...). This MultiProjectConfigFile is responsible for configuring these type of projects (complex)

\| [[MultiProjectConfigFile](#MultiProjectConfigFile)]

</div>

</div>

<div>

## Config File Project 

<div>

type ConfigFileProject = 

</div>

// Name of the command that runs the relay compiler. This will be added at the top of generated code to let readers know how to regenerate the file.

<div>

codegenCommand?: [string \| null]

</div>

// A map from GraphQL error name to import path, example: 

<div>

customErrorType?: [[CustomTypeImport](#CustomTypeImport) \| null]

</div>

// A map from GraphQL scalar types to a custom JS type, example:   }

<div>

customScalarTypes?: [[]][ = ]

</div>

// Threshold for diagnostics to be critical to the compiler\'s execution. All diagnostic with severities at and below this level will cause the compiler to fatally exit.

<div>

diagnosticReportConfig?: [[DiagnosticReportConfig](#DiagnosticReportConfig)][ = 

criticalLevel: \"error\",

}

</div>

// This option enables opting out of emitting es modules artifacts. When set to false, Relay will emit CommonJS modules.

<div>

eagerEsModules?: [boolean][ = true]

</div>

// When set, enum values are imported from a module with this suffix. For example, an enum Foo and this property set to \".test\" would be imported from \"Foo.test\". Note: an empty string is allowed and different from not setting the value, in the example above it would just import from \"Foo\".

<div>

enumModuleSuffix?: [string \| null]

</div>

// Some projects may need to exclude files with certain extensions.

<div>

excludesExtensions?: [array \| null]

</div>

// A placeholder for allowing extra information in the config file

<div>

extra?: [any]

</div>

// Some projects may need to generate extra artifacts. For those, we may need to provide an additional directory to put them. By default the will use \`output\` \*if available

<div>

extraArtifactsOutput?: [string \| null]

</div>

// Enable and disable experimental or legacy behaviors. WARNING! These are not stable and may change at any time.

<div>

featureFlags?: [[FeatureFlags](#FeatureFlags) \| null]

</div>

// Import/export style to use in generated JavaScript modules.

<div>

jsModuleFormat?: [[JsModuleFormat](#JsModuleFormat)][ = \"commonjs\"]

</div>

// The desired output language, \"flow\" or \"typescript\".

<div>

language?: [[\"javascript\"] \| [\"typescript\"] \| [\"flow\"]]

</div>

// Configuration for the \@module GraphQL directive.

<div>

moduleImportConfig?: [[ModuleImportConfig](#ModuleImportConfig)][ = 

dynamicModuleProvider: null,

operationModuleProvider: null,

surface: null,

}

</div>

// This option controls whether or not a catch-all entry is added to enum type definitions for values that may be added in the future. Enabling this means you will have to update your application whenever the GraphQL server schema adds new enum values to prevent it from breaking.

<div>

noFutureProofEnums?: [boolean]

</div>

// When set, generated input types will have the listed fields optional even if the schema defines them as required.

<div>

optionalInputFields?: [string\[\]][ = \[\]]

</div>

// A project without an output directory will put the generated files in a \_\_generated\_\_ directory next to the input file. All files in these directories should be generated by the Relay compiler, so that the compiler can cleanup extra files.

<div>

output?: [string \| null]

</div>

// If this option is set, the compiler will persist queries using this config.

<div>

persist?: [[PersistConfig](#PersistConfig) \| null]

</div>

// Whether to treat all JS module names as relative to \'./\' (true) or not. default: true

<div>

relativizeJsModulePaths?: [boolean][ = true]

</div>

// Require all GraphQL scalar types mapping to be defined, will throw if a GraphQL scalar type doesn\'t have a JS type

<div>

requireCustomScalarTypes?: [boolean]

</div>

// Indicates the type to import and use as the context for Relay Resolvers.

<div>

resolverContextType?: [[ResolverContextTypeInput](#ResolverContextTypeInput) \| null]

</div>

<div>

resolversSchemaModule?: [[ResolversSchemaModuleConfig](#ResolversSchemaModuleConfig) \| null]

</div>

// A generic rollout state for larger codegen changes. The default is to pass, otherwise it should be a number between 0 and 100 as a percentage.

<div>

rollout?: [[integer] \| [null]]

</div>

// Path to the schema.graphql or a directory containing a schema broken up in multiple \*.graphql files. Exactly 1 of these options needs to be defined.

<div>

schema?: [string \| null]

</div>

// Extra configuration for the GraphQL schema itself.

<div>

schemaConfig?: [[SchemaConfig](#SchemaConfig)][ = 

connectionInterface: ,

deferStreamInterface: ,

enableTokenField: false,

nodeInterfaceIdField: \"id\",

nodeInterfaceIdVariableName: \"id\",

nonNodeIdFields: null,

unselectableDirectiveName: \"unselectable\",

}

</div>

<div>

schemaDir?: [string \| null]

</div>

// Directory containing \*.graphql files with schema extensions.

<div>

schemaExtensions?: [string\[\]][ = \[\]]

</div>

// Schema name, if differs from project name. If schema name is unset, the project name will be used as schema name.

<div>

schemaName?: [string \| null]

</div>

// If \`output\` is provided and \`shard_output\` is \`true\`, shard the files by putting them under \`/\`

<div>

shardOutput?: [boolean]

</div>

// Regex to match and strip parts of the \`source_relative_path\`

<div>

shardStripRegex?: [string \| null]

</div>

// Optional regex to restrict \@relay_test_operation to directories matching this regex. Defaults to no limitations.

<div>

testPathRegex?: [string \| null]

</div>

// Keep the previous compiler behavior by outputting an union of the raw type and null, and not the \*\*correct\*\* behavior of an union with the raw type, null and undefined.

<div>

typescriptExcludeUndefinedFromNullableUnion?: [boolean]

</div>

// Whether to use the \`import type\` syntax introduced in Typescript version 3.8. This will prevent warnings from \`importsNotUsedAsValues\`.

<div>

useImportTypeSyntax?: [boolean]

</div>

// Generates a \`// \@relayVariables name1 name2\` header in generated operation files

<div>

variableNamesComment?: [boolean]

</div>

</div>

}

</div>

</div>

<div>

## Connection Interface 

Configuration where Relay should expect some fields in the schema.

<div>

type ConnectionInterface = 

</div>

<div>

edges?: [string]

</div>

<div>

endCursor?: [string]

</div>

<div>

hasNextPage?: [string]

</div>

<div>

hasPreviousPage?: [string]

</div>

<div>

node?: [string]

</div>

<div>

pageInfo?: [string]

</div>

<div>

startCursor?: [string]

</div>

</div>

}

</div>

</div>

<div>

## Custom Type 

Defines a custom GraphQL descrbing a custom scalar.

<div>

type CustomType =

// A string representing the name of a custom type. e.g. \"string\" or \"number\"

\| [string]

// A module which defines the custom type. e.g. 

\| [[CustomTypeImport](#CustomTypeImport)]

</div>

</div>

<div>

## Custom Type Import 

Defines a module path and export name of the Flow or TypeScript type descrbing a GraphQL custom scalar.

<div>

type CustomTypeImport = 

</div>

// The path to the module relative to the project root

<div>

path?: [string]

</div>

</div>

}

</div>

</div>

<div>

## Defer Stream Interface 

Configuration where Relay should expect some fields in the schema.

<div>

type DeferStreamInterface = 

</div>

<div>

ifArg?: [string]

</div>

<div>

initialCountArg?: [string]

</div>

<div>

labelArg?: [string]

</div>

<div>

streamName?: [string]

</div>

<div>

useCustomizedBatchArg?: [string]

</div>

</div>

}

</div>

</div>

<div>

## Deserializable Project Set 

<div>

type DeserializableProjectSet =

\| [[ProjectName](#ProjectName)]

\| [[ProjectName](#ProjectName)\[\]]

</div>

</div>

<div>

## Diagnostic Level 

Levels for reporting errors in the compiler.

<div>

type DiagnosticLevel =

// Report only errors

\| [\"error\"]

// Report diagnostics up to warnings

\| [\"warning\"]

// Report diagnostics up to informational diagnostics

\| [\"info\"]

// Report diagnostics up to hints

\| [\"hint\"]

</div>

</div>

<div>

## Diagnostic Report Config 

Configuration for all diagnostic reporting in the compiler

<div>

type DiagnosticReportConfig = 

</div>

</div>

}

</div>

</div>

<div>

## Feature Flag 

<div>

type FeatureFlag =

// Fully disabled: developers may not use this feature

\| [

kind: \"disabled\"

}

// Fully enabled: developers may use this feature

\| [

kind: \"enabled\"

}

// Partially enabled: developers may only use this feature on the listed items (fragments, fields, types).

\| [

allowlist: string\[\]

kind: \"limited\"

}

// Partially enabled: used for gradual rollout of the feature

\| [

kind: \"rollout\"

rollout: [integer] \| [null]

}

// Partially enabled: used for gradual rollout of the feature

\| [

kind: \"rolloutrange\"

rollout: [RolloutRange](#RolloutRange)

}

</div>

</div>

<div>

## Feature Flags 

<div>

type FeatureFlags = [ = 

kind: \"disabled\",

}

</div>

// \@outputType resolvers are a discontinued experimental feature. This flag allows users to allowlist old uses of this feature while they work to remove them. Weak types (types without an \`id\` field) returned by a Relay Resolver should be limited to types defined using \`@RelayResolver\` with \`@weak\`. If using the \"limited\" feature flag variant, users can allowlist a specific list of field names. https://relay.dev/docs/next/guides/relay-resolvers/defining-types/#defining-a-weak-type

<div>

allow_output_type_resolvers?: [[FeatureFlag](#FeatureFlag)][ = 

kind: \"disabled\",

}

</div>

// \@required with an action of THROW is read-time feature that is not compatible with our mutation APIs. We are in the process of removing any existing examples, but this flag is part of a process of removing any existing examples.

<div>

allow_required_in_mutation_response?: [[FeatureFlag](#FeatureFlag)][ = 

kind: \"disabled\",

}

</div>

// Allow non-nullable return types from resolvers.

<div>

allow_resolver_non_nullable_return_type?: [[FeatureFlag](#FeatureFlag)][ = 

kind: \"disabled\",

}

</div>

// Relay Resolvers are a read-time feature that are not actually handled in our mutation APIs. We are in the process of removing any existing examples, but this flag is part of a process of removing any existing examples.

<div>

allow_resolvers_in_mutation_response?: [[FeatureFlag](#FeatureFlag)][ = 

kind: \"disabled\",

}

</div>

// Print queries in compact form

<div>

compact_query_text?: [[FeatureFlag](#FeatureFlag)][ = 

kind: \"disabled\",

}

</div>

// Skip the optimization which extracts common JavaScript structures in generated artifacts into numbered variables and uses them by reference in each position in which they occur. This optimization can make it hard to follow changes to generated code, so being able to disable it can be helpful for debugging. To disable deduping for just one fragment or operation\'s generated artifacts: \`\`\`json \"disable_deduping_common_structures_in_artifacts\":  } \`\`\`

<div>

disable_deduping_common_structures_in_artifacts?: [[FeatureFlag](#FeatureFlag)][ = 

kind: \"disabled\",

}

</div>

// Disable validation of the \`edgeTypeName\` argument on \`@prependNode\` and \`@appendNode\`.

<div>

disable_edge_type_name_validation_on_declerative_connection_directives?: [[FeatureFlag](#FeatureFlag)][ = 

kind: \"disabled\",

}

</div>

// Disable full GraphQL argument type validation. Historically, we only applied argument type validation to the query that was actually going to be persisted and sent to the server. This meant that we didn\'t typecheck arguments passed to Relay Resolvers or Client Schema Extensions. We also permitted an escape hatch of \`uncheckedArguments_DEPRECATED\` for defining fragment arguments which were not typechecked. We no-longer support \`uncheckedArguments_DEPRECATED\`, and we typecheck both client and server arguments. This flag allows you to opt out of this new behavior to enable gradual adoption of the new validations. This flag will be removed in a future version of Relay.

<div>

disable_full_argument_type_validation?: [[FeatureFlag](#FeatureFlag)][ = 

kind: \"disabled\",

}

</div>

// Mirror of \`enable_resolver_normalization_ast\` excludes resolver metadata from reader ast

<div>

disable_resolver_reader_ast?: [boolean]

</div>

// Disable validating the composite schema (server, client schema extensions, Relay Resolvers) after its built.

<div>

disable_schema_validation?: [boolean]

</div>

// Disallow \@required action THROW on semantically nullable fields. When enabled, this will prevent the use of THROW action on fields that are semantically nullable (e.g., fields that can legitimately be null in normal operation).

<div>

disallow_required_action_throw_on_semantically_nullable_fields?: [[FeatureFlag](#FeatureFlag)][ = 

kind: \"disabled\",

}

</div>

<div>

enable_3d_branch_arg_generation?: [boolean]

</div>

// Allow per-query opt in to normalization AST for Resolvers with exec_time_resolvers directive. In contrast to enable_resolver_normalization_ast, if this is true, a normalization AST can be generated for a query using the \@exec_time_resolvers directive

<div>

enable_exec_time_resolvers_directive?: [boolean]

</div>

// Add support for parsing and transforming variable definitions on fragment definitions and arguments on fragment spreads.

<div>

enable_fragment_argument_transform?: [boolean]

</div>

// Allow relay resolvers to extend the Mutation type

<div>

enable_relay_resolver_mutations?: [boolean]

</div>

// Fully build the normalization AST for Resolvers

<div>

enable_resolver_normalization_ast?: [boolean]

</div>

// Perform strict validations when custom scalar types are used

<div>

enable_strict_custom_scalars?: [boolean]

</div>

// Enforce that you must add \`@alias\` to a fragment if it may not match, due to type mismatch or \`@skip\`/\`@include\`

<div>

enforce_fragment_alias_where_ambiguous?: [[FeatureFlag](#FeatureFlag)][ = 

kind: \"enabled\",

}

</div>

// The \`path\` field in \`@required\` Reader AST nodes is no longer used. But removing them in one diff is too large of a change to ship at once. This flag will allow us to use the rollout FeatureFlag to remove them across a number of diffs.

<div>

legacy_include_path_in_required_reader_nodes?: [[FeatureFlag](#FeatureFlag)][ = 

kind: \"disabled\",

}

</div>

// For now, this also disallows fragments with variable definitions This also makes \@module to opt in using \@no_inline internally NOTE that the presence of a fragment in this list only controls whether a fragment is \*allowed\* to use \@no_inline: whether the fragment is inlined or not depends on whether it actually uses that directive.

<div>

no_inline?: [[FeatureFlag](#FeatureFlag)][ = 

kind: \"disabled\",

}

</div>

// Skip generating resolver type assertions for resolvers which have been derived from TS/Flow types.

<div>

omit_resolver_type_assertions_for_confirmed_types?: [[FeatureFlag](#FeatureFlag)][ = 

kind: \"disabled\",

}

</div>

// Feature flag to prefer \`fetch_MyType()\` generatior over \`node()\` query generator in \@refetchable transform

<div>

prefer_fetchable_in_refetch_queries?: [boolean]

</div>

// Use ReadonlyArray\<T\> instead of \$ReadOnlyArray\<T\> for Flow typegen. This enables gradual rollout of the new array type across files.

<div>

readonly_array_for_flow?: [[FeatureFlag](#FeatureFlag)][ = 

kind: \"disabled\",

}

</div>

// Enable returning interfaces from Relay Resolvers without \@outputType

<div>

relay_resolver_enable_interface_output_type?: [[FeatureFlag](#FeatureFlag)][ = 

kind: \"disabled\",

}

</div>

<div>

skip_printing_nulls?: [[FeatureFlag](#FeatureFlag)][ = 

kind: \"disabled\",

}

</div>

// Enable generation of text artifacts used to generate full query strings later.

<div>

text_artifacts?: [[FeatureFlag](#FeatureFlag)][ = 

kind: \"disabled\",

}

</div>

// Generate the \`moduleImports\` field in the Reader AST.

<div>

use_reader_module_imports?: [[FeatureFlag](#FeatureFlag)][ = 

kind: \"disabled\",

}

</div>

</div>

}

</div>

</div>

<div>

## Js Module Format 

Formatting style for generated files.

<div>

type JsModuleFormat =

// Common JS style, e.g. \`require(\'../path/MyModule\')\`

\| [\"commonjs\"]

// Facebook style, e.g. \`require(\'MyModule\')\`

\| [\"haste\"]

</div>

</div>

<div>

## Local Persist Config 

Configuration for local persistence of GraphQL documents. This struct contains settings that control how GraphQL documents are persisted locally.

<div>

type LocalPersistConfig =  \| [\"SHA1\"] \| [\"SHA256\"]][ = \"MD5\"]

</div>

// The file path where the persisted documents will be written.

<div>

file?: [string]

</div>

// Whether to include the query text in the persisted document.

<div>

include_query_text?: [boolean]

</div>

</div>

}

</div>

</div>

<div>

## Module Import Config 

Configuration for \@module.

<div>

type ModuleImportConfig = 

</div>

// Defines the custom import statement to be generated for the \`operationModuleProvider\` function on the \`NormalizationModuleImport\` node in ASTs. Used in exec time client 3D.

<div>

operationModuleProvider?: [[ModuleProvider](#ModuleProvider) \| null]

</div>

// Defines the surface upon which \@module is enabled.

<div>

surface?: [[\"resolvers\"] \| [\"all\"] \| null]

</div>

</div>

}

</div>

</div>

<div>

## Module Provider 

<div>

type ModuleProvider =

// Generates a module provider using JSResource

\| [

mode: \"JSResource\"

}

// Generates a custom JS import, Use \`\<\$module\>\` as the placeholder for the actual module. e.g. \`\"() =\> import(\'\<\$module\>\')\"\`

\| [

mode: \"Custom\"

statement: string

}

</div>

</div>

<div>

## Multi Project Config File 

Schema of the compiler configuration JSON file.

<div>

type MultiProjectConfigFile = 

</div>

<div>

codegenCommand?: [string \| null]

</div>

// Glob patterns that should not be part of the sources even if they are in the source set directories.

<div>

excludes?: [string\[\]][ = \[\"\*\*/node_modules/\*\*\", \"\*\*/\_\_mocks\_\_/\*\*\", \"\*\*/\_\_generated\_\_/\*\*\"\]]

</div>

// Enable and disable experimental or legacy behaviors. WARNING! These are not stable and may change at any time.

<div>

featureFlags?: [[FeatureFlags](#FeatureFlags)][ = 

actor_change_support: ,

allow_output_type_resolvers: ,

allow_required_in_mutation_response: ,

allow_resolver_non_nullable_return_type: ,

allow_resolvers_in_mutation_response: ,

compact_query_text: ,

disable_deduping_common_structures_in_artifacts: ,

disable_edge_type_name_validation_on_declerative_connection_directives: ,

disable_full_argument_type_validation: ,

disable_resolver_reader_ast: false,

disable_schema_validation: false,

disallow_required_action_throw_on_semantically_nullable_fields: ,

enable_3d_branch_arg_generation: false,

enable_exec_time_resolvers_directive: false,

enable_fragment_argument_transform: false,

enable_relay_resolver_mutations: false,

enable_resolver_normalization_ast: false,

enable_strict_custom_scalars: false,

enforce_fragment_alias_where_ambiguous: ,

legacy_include_path_in_required_reader_nodes: ,

no_inline: ,

omit_resolver_type_assertions_for_confirmed_types: ,

prefer_fetchable_in_refetch_queries: false,

readonly_array_for_flow: ,

relay_resolver_enable_interface_output_type: ,

skip_printing_nulls: ,

text_artifacts: ,

use_reader_module_imports: ,

}

</div>

// Similar to sources but not affected by excludes.

<div>

generatedSources?: [[]][ = ]

</div>

<div>

header?: [string\[\]][ = \[\]]

</div>

// Then name of the global \_\_DEV\_\_ variable to use in generated artifacts

<div>

isDevVariableName?: [string \| null]

</div>

// Optional name for this config, might be used for logging or custom extra artifact generator code.

<div>

name?: [string \| null]

</div>

// Opt out of source control checks/integration.

<div>

noSourceControl?: [boolean \| null]

</div>

// Configuration of projects to compile.

<div>

projects?: [[]]

</div>

// Root directory relative to the config file. Defaults to the directory where the config is located.

<div>

root?: [string \| null]

</div>

// Watchman saved state config.

<div>

savedStateConfig?: [[ScmAwareClockData](#ScmAwareClockData) \| null]

</div>

// A mapping from directory paths (relative to the root) to a source set. If a path is a subdirectory of another path, the more specific path wins.

<div>

sources?: [[]]

</div>

</div>

}

</div>

</div>

<div>

## Non Node Id Fields Config 

Configuration of Relay\'s validation for \`id\` fields outside of the \`Node\` interface.

<div>

type NonNodeIdFieldsConfig = ]][ = ]

</div>

</div>

}

</div>

</div>

<div>

## Persist Config 

Configuration for how the Relay Compiler should persist GraphQL queries.

<div>

type PersistConfig =

// This variant represents a remote persistence configuration, where GraphQL queries are sent to a remote endpoint for persistence.

\| [[RemotePersistConfig](#RemotePersistConfig)]

// This variant represents a local persistence configuration, where GraphQL queries are persisted to a local JSON file. When this variant is used, the compiler will attempt to read the local file as a hash map, add new queries to the map, and then serialize and write the resulting map to the configured path.

\| [[LocalPersistConfig](#LocalPersistConfig)]

</div>

</div>

<div>

## Project Name 

Represents the name of a project in the Relay configuration.

<div>

type ProjectName =

// No project name is specified.

\| [null]

// A project name. This should match one the keys in the \`projects\` map in the Relay compiler config.

\| [string]

</div>

</div>

<div>

## Project Set 

Set of project names.

<div>

type ProjectSet =

\| [[ProjectName](#ProjectName)]

\| [[ProjectName](#ProjectName)\[\]]

</div>

</div>

<div>

## Remote Persist Config 

Configuration for remote persistence of GraphQL documents.

<div>

type RemotePersistConfig = 

</div>

// Additional headers to include in the POST request.

<div>

headers?: [[]][ = ]

</div>

// Whether to include the query text in the persisted document.

<div>

includeQueryText?: [boolean]

</div>

// Additional parameters to include in the POST request. The main document will be in a POST parameter \`text\`. This map can contain additional parameters to send.

<div>

params?: [[]][ = ]

</div>

// URL that the document should be persisted to via a POST request.

<div>

url?: [string]

</div>

</div>

}

</div>

</div>

<div>

## Resolver Context Type Input 

Describes the type to import and use as the context for Relay Resolvers.

<div>

type ResolverContextTypeInput =

// The type imported using a relative path

\| [[ResolverContextTypeInputPath](#ResolverContextTypeInputPath)]

// The type imported using a named package

\| [[ResolverContextTypeInputPackage](#ResolverContextTypeInputPackage)]

</div>

</div>

<div>

## Resolver Context Type Input Package 

Specifies how Relay can import the Resolver context type from a named package

<div>

type ResolverContextTypeInputPackage = 

</div>

// The name of the package

<div>

package?: [string]

</div>

</div>

}

</div>

</div>

<div>

## Resolver Context Type Input Path 

Specifies how Relay can import the Resolver context type from a path

<div>

type ResolverContextTypeInputPath = 

</div>

// The path to the module relative to the project root

<div>

path?: [string]

</div>

</div>

}

</div>

</div>

<div>

## Resolvers Schema Module Config 

Configuration for resolvers_schema_module generation

<div>

type ResolversSchemaModuleConfig = 

</div>

<div>

path?: [string]

</div>

</div>

}

</div>

</div>

<div>

## Rollout Range 

A utility to enable gradual rollout of large codegen changes. Allows you to specify a range of percentages to rollout.

<div>

type RolloutRange = 

</div>

<div>

start?: [number]

</div>

</div>

}

</div>

</div>

<div>

## Saved State Clock Data 

Holds extended clock data that includes source control aware query metadata. \<https://facebook.github.io/watchman/docs/scm-query.html\>

<div>

type SavedStateClockData = 

</div>

<div>

config?: [true]

</div>

<div>

storage?: [string \| null]

</div>

</div>

}

</div>

</div>

<div>

## Schema Config 

<div>

type SchemaConfig = [ = 

cursor: \"cursor\",

edges: \"edges\",

endCursor: \"endCursor\",

hasNextPage: \"hasNextPage\",

hasPreviousPage: \"hasPreviousPage\",

node: \"node\",

pageInfo: \"pageInfo\",

startCursor: \"startCursor\",

}

</div>

<div>

deferStreamInterface?: [[DeferStreamInterface](#DeferStreamInterface)][ = 

deferName: \"defer\",

ifArg: \"if\",

initialCountArg: \"initialCount\",

labelArg: \"label\",

streamName: \"stream\",

useCustomizedBatchArg: \"useCustomizedBatch\",

}

</div>

// If we should select \_\_token field on fetchable types

<div>

enableTokenField?: [boolean]

</div>

// The name of the \`id\` field that exists on the \`Node\` interface.

<div>

nodeInterfaceIdField?: [string][ = \"id\"]

</div>

// The name of the variable expected by the \`node\` query.

<div>

nodeInterfaceIdVariableName?: [string][ = \"id\"]

</div>

<div>

nonNodeIdFields?: [[NonNodeIdFieldsConfig](#NonNodeIdFieldsConfig) \| null]

</div>

// The name of the directive indicating fields that cannot be selected

<div>

unselectableDirectiveName?: [string][ = \"unselectable\"]

</div>

</div>

}

</div>

</div>

<div>

## Scm Aware Clock Data 

Holds extended clock data that includes source control aware query metadata. \<https://facebook.github.io/watchman/docs/scm-query.html\>

<div>

type ScmAwareClockData = 

</div>

<div>

mergebase-with?: [string \| null]

</div>

<div>

saved-state?: [[SavedStateClockData](#SavedStateClockData) \| null]

</div>

</div>

}

</div>

</div>

<div>

## Single Project Config File 

<div>

type SingleProjectConfigFile = 

</div>

// A specific directory to output all artifacts to. When enabling this the babel plugin needs \`artifactDirectory\` set as well.

<div>

artifactDirectory?: [string \| null]

</div>

// Name of the command that runs the relay compiler. This will be added at the top of generated code to let readers know how to regenerate the file.

<div>

codegenCommand?: [string \| null]

</div>

// A map from GraphQL error name to import path, example: 

<div>

customErrorType?: [[CustomTypeImport](#CustomTypeImport) \| null]

</div>

// A map from GraphQL scalar types to a custom JS type, example:   }

<div>

customScalarTypes?: [[]][ = ]

</div>

// This option enables opting out of emitting es modules artifacts. When set to false, Relay will emit CommonJS modules.

<div>

eagerEsModules?: [boolean][ = true]

</div>

// When set, enum values are imported from a module with this suffix. For example, an enum Foo and this property set to \".test\" would be imported from \"Foo.test\". Note: an empty string is allowed and different from not setting the value, in the example above it would just import from \"Foo\".

<div>

enumModuleSuffix?: [string \| null]

</div>

// Directories to ignore under src default: \[\'\*\*/node_modules/\*\*\', \'\*\*/\_\_mocks\_\_/\*\*\', \'\*\*/\_\_generated\_\_/\*\*\'\],

<div>

excludes?: [string\[\]][ = \[\"\*\*/node_modules/\*\*\", \"\*\*/\_\_mocks\_\_/\*\*\", \"\*\*/\_\_generated\_\_/\*\*\"\]]

</div>

// A placeholder for allowing extra information in the config file

<div>

extra?: [any]

</div>

// Enable and disable experimental or legacy behaviors. WARNING! These are not stable and may change at any time.

<div>

featureFlags?: [[FeatureFlags](#FeatureFlags) \| null]

</div>

// We may generate some content in the artifacts that\'s stripped in production if \_\_DEV\_\_ variable is set This config option is here to define the name of that special variable

<div>

isDevVariableName?: [string \| null]

</div>

// Import/export style to use in generated JavaScript modules.

<div>

jsModuleFormat?: [[JsModuleFormat](#JsModuleFormat)][ = \"commonjs\"]

</div>

// The desired output language, \"flow\" or \"typescript\".

<div>

language?: [[\"javascript\"] \| [\"typescript\"] \| [\"flow\"]]

</div>

// Configuration for \@module

<div>

moduleImportConfig?: [[ModuleImportConfig](#ModuleImportConfig)][ = 

dynamicModuleProvider: null,

operationModuleProvider: null,

surface: null,

}

</div>

// This option controls whether or not a catch-all entry is added to enum type definitions for values that may be added in the future. Enabling this means you will have to update your application whenever the GraphQL server schema adds new enum values to prevent it from breaking.

<div>

noFutureProofEnums?: [boolean]

</div>

// Opt out of source control checks/integration.

<div>

noSourceControl?: [boolean \| null]

</div>

// When set, generated input types will have the listed fields optional even if the schema defines them as required.

<div>

optionalInputFields?: [string\[\]][ = \[\]]

</div>

// Query Persist Configuration It contains URL and addition parameters that will be included with the request (think API_KEY, APP_ID, etc\...)

<div>

persistConfig?: [[PersistConfig](#PersistConfig) \| null]

</div>

// Whether to treat all JS module names as relative to \'./\' (true) or not. default: true

<div>

relativizeJsModulePaths?: [boolean][ = true]

</div>

// Require all GraphQL scalar types mapping to be defined, will throw if a GraphQL scalar type doesn\'t have a JS type

<div>

requireCustomScalarTypes?: [boolean]

</div>

// Indicates the type to import and use as the context for Relay Resolvers.

<div>

resolverContextType?: [[ResolverContextTypeInput](#ResolverContextTypeInput) \| null]

</div>

<div>

resolversSchemaModule?: [[ResolversSchemaModuleConfig](#ResolversSchemaModuleConfig) \| null]

</div>

// Path to schema.graphql

<div>

schema?: [string]

</div>

// Extra configuration for the GraphQL schema itself.

<div>

schemaConfig?: [[SchemaConfig](#SchemaConfig)][ = 

connectionInterface: ,

deferStreamInterface: ,

enableTokenField: false,

nodeInterfaceIdField: \"id\",

nodeInterfaceIdVariableName: \"id\",

nonNodeIdFields: null,

unselectableDirectiveName: \"unselectable\",

}

</div>

// List of directories with schema extensions.

<div>

schemaExtensions?: [string\[\]][ = \[\]]

</div>

// Root directory of application code

<div>

src?: [string]

</div>

// Keep the previous compiler behavior by outputting an union of the raw type and null, and not the \*\*correct\*\* behavior of an union with the raw type, null and undefined.

<div>

typescriptExcludeUndefinedFromNullableUnion?: [boolean]

</div>

// Whether to use the \`import type\` syntax introduced in Typescript version 3.8. This will prevent warnings from \`importsNotUsedAsValues\`.

<div>

useImportTypeSyntax?: [boolean]

</div>

</div>

}

</div>

</div>

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit this page](https://github.com/facebook/relay/tree/main/website/versioned_docs/version-v20.1.0/getting-started/compiler-config.md)