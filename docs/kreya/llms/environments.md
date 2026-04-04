# Source: https://kreya.app/docs/environments.md

# Environments

Environments are a core feature of Kreya. They simplify your Kreya experience. You can add, edit and delete environments via Project → Environments.

## Environment data[​](#environment-data "Direct link to Environment data")

Store environment-specific values in here. The environment data must be valid JSON and the keys should only consist of letters, numbers and underscores. Comments are allowed too, both `//` and `/**/` style comments work.

### User specific data[​](#user-specific-data "Direct link to User specific data")

In some cases, you may not want to store environment values inside the Kreya project. Examples include passwords, other user-specific authentication values or simply secret keys that should not be synced in plain text over the Internet.

Note that this user specific data is still stored in plain text, only outside of the Kreya project (in your appdata-folder).

User specific environment values take precedence over "normal" environment values.

### Process / System environment variables[​](#process--system-environment-variables "Direct link to Process / System environment variables")

Kreya automatically imports system environment variables prefixed with `KREYA_ENV_` into the active Kreya environment. The `KREYA_ENV_` prefix is stripped. Additionally `.` and `__` (double underscore) split the values into objects. These variables take precedence over "normal" and user specific environment values. System environment variables are especially useful in CI/CD systems or for secrets.

Example:

```
KREYA_ENV_FruitApi__ApiKey='FruitApiSecretKey'
KREYA_ENV_CarApi__ApiKey='CarApiSecretKey'
```

will be imported as

```
{
  "FruitApi": { "ApiKey": "FruitApiSecretKey" },
  "CarApi": { "ApiKey": "CarApiSecretKey" }
}
```

## Changing the active environment[​](#changing-the-active-environment "Direct link to Changing the active environment")

You can view and change the active environment in the upper-left corner.

![Changing the active environment](/assets/ideal-img/set-active-environment.5661b45.400.png)

## Using environment values[​](#using-environment-values "Direct link to Using environment values")

See the [Templating](/docs/templating.md) section.
