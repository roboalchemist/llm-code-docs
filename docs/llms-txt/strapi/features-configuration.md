# Features configuration

The `config/features.js|ts` file is used to enable feature flags. Currently this file only includes a `future` object used to enable experimental features through **future flags**.

Some incoming Strapi features are not yet ready to be shipped to all users, but Strapi still offers community users the opportunity to provide early feedback on these new features or changes. With these experimental features, developers have the flexibility to choose and integrate new features and changes into their Strapi applications as they become available in the current major version as well as assist us in shaping these new features.

Such experimental features are indicated by a 

  </Tabs>

4. Rebuild the admin panel and restart the server:

  </Tabs>

## Future flags API

Developers can use the following APIs to interact with future flags:

- Features configuration is part of the `config` object and can be read with `strapi.config.get('features')` or with `strapi.features.config`.

- `strapi.features.future` returns the `isEnabled()` that can be used to determine if a future flag is enabled, using the following method: `strapi.features.future.isEnabled('featureName')`.

## Available future flags

| Property name | Related feature | Suggested environment variable name |
| ------------- | --------------- | ---------------------------------- |
| `experimental_firstPublishedAt` | [Draft & Publish](/cms/features/draft-and-publish#recording-the-first-publication-date) | `STRAPI_FUTURE_EXPERIMENTAL_FIRST_PUBLISHED_AT` |