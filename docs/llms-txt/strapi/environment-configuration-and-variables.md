# Environment configuration and variables

Strapi provides specific environment variable names. Defining them in an environment file (e.g., `.env`) will make these variables and their values available in your code.

:::tip
An `env()` utility can be used to [retrieve the value of environment variables](/cms/configurations/guides/access-cast-environment-variables#accessing-environment-variables) and [cast variables to different types](/cms/configurations/guides/access-cast-environment-variables).
:::

Additionally, specific [configurations for different environments](#environment-configurations) can be created.

## Strapi's environment variables {#strapi}

Strapi provides the following environment variables:

 Setting                                                    | Description                                                                                                                                                                                                                                                                   | Type      | Default value   |
|------------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|-----------------|
| `STRAPI_TELEMETRY_DISABLED`                                | Don't send telemetry usage data to Strapi                                                                                                                                                                                                                                     | `Boolean` | `false`         |
| `STRAPI_LICENSE`                                           | The license key to activate the Enterprise Edition                                                                                                                                                                                                                            | `String`  | `undefined`     |
| `NODE_ENV` | Type of environment where the application is running.<br/><br/>`production` enables specific behaviors (see 

</Tabs>

With these configuration files the server will start on various ports depending on the environment variables passed:

```bash
yarn start                                   # uses host 127.0.0.1
NODE_ENV=production yarn start               # uses host defined in .env. If not defined, uses 0.0.0.0
HOST=10.0.0.1 NODE_ENV=production yarn start # uses host 10.0.0.1
```

<br/>

To learn deeper about how to use environment variables in your code, please refer to the following guide: