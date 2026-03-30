# Step-by-step guide to upgrade to Strapi 5

The latest major version of Strapi is Strapi 5.

The present page is meant to be used as step-by-step instructions for upgrading your Strapi v4 application to Strapi 5.

:::prerequisites
Your Strapi v4 application is already running on the latest v4 minor and patch version. If it's not, run the [upgrade tool](/cms/upgrade-tool) with the `minor` command to reach it: `npx @strapi/upgrade minor`.
:::

## Step 1: Get ready to upgrade

Before getting into the upgrade process itself, take the following precautions:

1. **Backup your database**:
    * If you are using SQLite with the default configuration (the default database provided with Strapi), your database file is named `data.db` and is located in the `.tmp/` folder at the root of your Strapi application.
    * If you are using another type of database, please refer to their official documentation (see  and ).
    * If your project is hosted on Strapi Cloud, you can manually [create a backup](/cloud/projects/settings#creating-a-manual-backup).
2. **Backup your code**:
    * If your code is versioned with git, create a new dedicated branch to run the migration.
    * If your code is _not_ versioned with git, create a backup of your working Strapi v4 code and store it in a safe place.
3. **Ensure the plugins you are using are compatible with Strapi 5**.

  To do so, list the plugins you are using, then check compatibility for each of them by reading their dedicated documentation on the  website.

## Step 2: Run automated migrations

Strapi provides a tool to automate some parts of the upgrade to Strapi 5: the [upgrade tool](/cms/upgrade-tool).

1. **Run the upgrade tool**.  

  ```sh
  npx @strapi/upgrade major
  ```

  The command will execute the update and installation of the dependencies of Strapi 5, and run the codemods to handle some of the breaking changes that come with Strapi 5.

  The codemods will handle the following changes:

  | Codemod name and GitHub code link | Description |
  |-----------------------------------|-------------|
  |  | Comment out lifecycles files in favor of [Document Service Middlewares](/cms/migration/v4-to-v5/breaking-changes/lifecycle-hooks-document-service) | 
  |  | Remove the i18n plugin dependency as i18n is now integrated into the core of Strapi |
  |   | Upgrade the react and react-dom dependencies | 
  |   | Upgrade the react-router-dom dependency |
  |   | Upgrade the styled-components dependency |
  |   | Partly handle migrations from `@strapi/helper-plugin` |
  |             | Partly handle the migration from the Entity Service API to the new Document Service API |
  |             | Wrap the `accessKeyId` and `secretAccessKey` properties inside a `credentials` object for users using the `aws-s3` provider | 
  |                                                                     | Update the sqlite dependency to better-sqlite3 | 
  |                           | Transform `@strapi/strapi` imports to use the new public interface | 
  |                 | Replace string dot format for config get/set/has with uid format for 'plugin' and 'api' namespace where possible | 
  |                             | Update utils to use the new public interface | 

:::tip
If you develop Strapi plugins, other codemods handle some aspects of the helper-plugin deprecation. See the [related breaking change](/cms/migration/v4-to-v5/breaking-changes/helper-plugin-deprecated) for more information.
:::

2. Go over the changes made by the upgrade tool to **check if you have to manually complete some code updates**:

  Look for `__TODO__` automatically added to your code by the codemods. Some of them might have been added while migrating from the Entity Service API to the new Document Service API introduced in Strapi 5.
  
  :::info Document Service API
  Additional information about the Document Service API can be found in the [breaking change entry description](/cms/migration/v4-to-v5/breaking-changes/entity-service-deprecated), the [specific migration guide](/cms/migration/v4-to-v5/additional-resources/from-entity-service-to-document-service), and the [API reference](/cms/api/document-service).
  :::

## Step 3: Check and handle manual upgrades

The following main changes might affect your Strapi application and require you to do some manual actions.

For each of them, read the indicated breaking change entry and check if some manual actions are still required after the upgrade tool has run:

1. **Database migration**:
    1. MySQL v5 is not supported 👉 see [breaking change](/cms/migration/v4-to-v5/breaking-changes/mysql5-unsupported)
    2. Only better-sqlite3 is supported 👉 see [breaking change](/cms/migration/v4-to-v5/breaking-changes/only-better-sqlite3-for-sqlite)
    3. Only mysql2 is supported 👉 see [breaking change](/cms/migration/v4-to-v5/breaking-changes/only-mysql2-package-for-mysql)
    4. Lifecycle hooks are triggered differently 👉 see [breaking change](/cms/migration/v4-to-v5/breaking-changes/lifecycle-hooks-document-service)
2. **Configuration**:
    1. Some environment variables are handled by the server configuration 👉 see [breaking change](/cms/migration/v4-to-v5/breaking-changes/removed-support-for-some-env-options)
    2. Custom configuration must meet specific requirements 👉 see [breaking change](/cms/migration/v4-to-v5/breaking-changes/strict-requirements-config-files)
3. **Admin panel customization**:
    * The helper-plugin has been removed 👉 see [migration reference](/cms/migration/v4-to-v5/additional-resources/helper-plugin)

👉 Finally, go over the rest of the [breaking changes database](/cms/migration/v4-to-v5/breaking-changes) for any edge case you might be concerned about.

## Step 4: Migrate the API consuming side

Strapi 5 has updated both the REST and GraphQL APIs.

Follow the steps below and leverage retro-compatibility headers and guided migration resources to gradually update your code for Strapi 5.

### Migrate REST API calls

1. Enable the compatibility header everywhere you still expect `attributes`, by adding `Strapi-Response-Format: v4` to REST calls in HTTP clients, SDKs, and middleware (see the [breaking change entry](/cms/migration/v4-to-v5/breaking-changes/new-response-format#migration) for concrete examples).
2. While the header is on, audit existing payloads. Capture representative responses (including populated relations, components, and media) so you can verify that legacy consumers keep working during the transition.
3. Update and test each client by:
    - removing `data.attributes` access,
    - switching to the flattened payload,
    - and adopting [`documentId`](/cms/migration/v4-to-v5/breaking-changes/use-document-id) wherever the REST API was previously returning numeric `id` only.
4. Disable the compatibility header per endpoint or consumer: once tests pass for a given client, remove `Strapi-Response-Format: v4` from its requests. Repeat until no consumer depends on the legacy wrapper.

### Migrate GraphQL API calls

1. Enable the compatibility header by setting `v4CompatibilityMode` to `true` in the `graphql` plugin configuration, so clients can continue to rely on `data.attributes` while you refactor them.
2. Follow each step of the [breaking change entry for GraphQL](/cms/migration/v4-to-v5/breaking-changes/graphql-api-updated). This will guide you to swap `id` for `documentId`, adopt `_connection` queries, remove `attributes`, and finally switch to `nodes/pageInfo`.
3. Test Relay and non-Relay queries by confirming that pagination metadata still matches expectations when you remove `_connection` and `data` for clients that do not need Relay semantics.
4. Disable the `v4CompatibilityMode` compatibility header: after every query and mutation works with the flattened schema, set the header to `false` so the server emits the Strapi 5 format by default.