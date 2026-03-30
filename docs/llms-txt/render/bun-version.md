# Source: https://render.com/docs/bun-version.md

# Setting your Bun Version


| Current default Bun version |
| --- |
| *`1.3.4`* Services created before *2025-12-08* have a different default version. [See below.](#history-of-default-bun-versions) |

> *To include Bun in your service's environment, you must do _at least one_ of the following:*
>
> - Set your service's Bun version using one of the methods below.
> - Include a `bun.lock` or `bun.lockb` file in your service's root directory.
>
> Otherwise, your service's environment will _not_ include Bun.

*Set your service's Bun version in any of the following ways* (in descending order of precedence):

1. Set the `BUN_VERSION` environment variable for your service in the [Render Dashboard](https://dashboard.render.com):

   [image: Setting the BUN_VERSION environment variable]

2. Add a file named `.bun-version` to the root of your repo. This file contains a single line with the version to use:

   ```:.bun-version
   1.3.10
   ```

You can specify either a semantic version number (such as `1.3.4`) or use `latest` to always use the most recent version of Bun with every deploy.

## History of default Bun versions

If you don't set a Bun version for your service, Render's default version depends on when you originally created the service:

| Service Creation Date | Default Bun Version |
|---|---|
| 2025-12-08 and later | `1.3.4` |
| 2025-08-18 | `1.2.20` |
| Before 2025-08-18 | `1.1.0` |
