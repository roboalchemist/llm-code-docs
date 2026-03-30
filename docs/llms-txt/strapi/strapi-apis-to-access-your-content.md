# Strapi APIs to access your content

Once you've created and configured a Strapi project, created a content structure with the [Content-Type Builder](/cms/features/content-type-builder) and started adding data through the [Content Manager](/cms/features/content-manager), you likely would like to access your content.

From a front-end application, your content can be accessed through Strapi's Content API, which is exposed:

- by default through the [REST API](/cms/api/rest)
- and also through the [GraphQL API](/cms/api/graphql) if you installed the Strapi built-in [GraphQL plugin](/cms/plugins/graphql).

You can also use the [Strapi Client](/cms/api/client) library to interact with the REST API.

REST and GraphQL APIs represent the top-level layers of the Content API exposed to external applications. Strapi also provides 2 lower-level APIs:

- The [Document Service API](/cms/api/document-service), accessible through `strapi.documents`, is the recommended API to interact with your application's database within the [backend server](/cms/customization) or through [plugins](/cms/plugins-development/developing-plugins). The Document Service is the layer that handles **documents**