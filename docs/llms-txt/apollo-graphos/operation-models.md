# Source: https://www.apollographql.com/docs/ios/project-configuration/operation-models.md

# Operation Models Configuration

Operation models are generated for each of the GraphQL definitions defined in your project. These models are used to execute operations using the `ApolloClient` and include response models for accessing the data returned by these operations.

The way you want to structure your project to use these operation models is important in determining where they should be located in your project. You can configure this using the [`output.operations`](https://www.apollographql.com/docs/ios/code-generation/codegen-configuration#operations) property in your codegen configuration.

In this section, we will consider the options for how you may use the generated operation models and answer the question:

**Where should your generated operation models be located?**

Generally, you'll decide between two approaches: [confined models](https://www.apollographql.com/docs/ios/project-configuration/operation-models.md#confined-models) or [shared models](https://www.apollographql.com/docs/ios/project-configuration/operation-models.md#shared-models).

Wherever your operation models are located, it is required that they have access to your schema types and the `ApolloAPI` target to compile successfully.

## Confined models

If you want to organize your generated models by specific feature areas or modules, use the [`OperationsFileOutput.relative(subpath: String?)`](https://www.apollographql.com/docs/ios/code-generation/codegen-configuration#relative-operations-output) value for the [`output.operations`](https://www.apollographql.com/docs/ios/code-generation/codegen-configuration#operations) property. The code generation engine now generates your operation models relative to the `.graphql` files that define them.

This option gives you the most flexibility and control over your operation models. You can generate them anywhere in your project structure by organizing your `.graphql` operation definitions.

With relative paths, you can:

* Co-locate models alongside the feature code using them
* Include models in different modules across your project
* Organize models based on feature area
* Or use any other structure your project needs

When including your operation models in a **multi-module project configuration**, ensure that any modules that include your operation models link to **both** your [schema types module](https://www.apollographql.com/docs/ios/project-configuration/schema-types) and the [`ApolloAPI` library](https://www.apollographql.com/docs/ios/project-configuration/sdk-components/#apolloapi).

### Sharing fragments across modules

When working in a **multi-module project configuration** with confined operation models, you may want to share fragment models across operations (or other fragments) in multiple modules in your project. This can be accomplished using the [`@import(module: String!)` client directive](https://www.apollographql.com/docs/ios/client-directives#importmodule-string).

This directive can be applied to any GraphQL definition in it's `.graphql` file, which adds an `import` statement for the given module name to the top of definition's generated Swift file.

Using [`.relative(subpath:)`](https://www.apollographql.com/docs/ios/code-generation/codegen-configuration#relative-operations-output) operations, you can place your shared fragment into a module that can be shared between the dependent definitions. Make sure the modules containing your dependent definitions are linked to the module containing your fragment. Then, you can use the [`@import(module: String!)` client directive](https://www.apollographql.com/docs/ios/client-directives#importmodule-string) to import that module in your generated operation model file.

## Shared models

You can also share your generated operation models across modules in your project. You can do this by including them within the shared schema types module or by manually including them in another shared module.

### Bundling within a shared schema type module

For most small projects, including your operation models within the shared schema type module is the most straightforward way to share them. With this structure, your operation models are in a sub-folder of the schema types module directory.

You can do this using the [`.inSchemaModule`](https://www.apollographql.com/docs/ios/code-generation/codegen-configuration#operations-in-the-schema-module) option for the [`output.operations`](https://www.apollographql.com/docs/ios/code-generation/codegen-configuration#operations) property:

* *If you have a schema module*, the codegen engine includes your operations in that module, which you can then import into your project's other modules.
* *If you are embedding your schema in another target*, the codegen engine includes your operations in the generated schema namespace in your application target.

## Absolute path

You can also generate your operation models into a single directory using the [`.absolute(path:)`](https://www.apollographql.com/docs/ios/code-generation/codegen-configuration#absolute-operations-output) option. Then, you can manually include this directory in your project however you see fit.

If you choose to generate the operation models to an absolute path, you are responsible for linking the generated files to the rest of your project. You must ensure that any targets included by your operation models link to both your schema types module and the `ApolloAPI` library.
