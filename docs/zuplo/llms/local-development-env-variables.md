# Source: https://www.zuplo.com/docs/articles/local-development-env-variables.md

# Configuring Environment Variables Locally

For security reasons, your local development doesn't have access to the
environment variables that you have configured on the Zuplo Portal. Instead,
your local Zuplo API Gateway will load environment variables from a .env file.

1. Create a .env file in the root of your project.
2. Follow the following format

:::warning

As the `.env` file could contain sensitive information, it shouldn't be
committed to your version system. Consider adding .env to your .gitignore file.

:::

```txt
KEY1=VALUE1
KEY2=VALUE2
```
