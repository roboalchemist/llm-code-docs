# Source: https://www.apollographql.com/docs/rover/commands/config.md

# Rover config Commands

Rover enables you to create multiple *configuration profiles*, each of which corresponds to a different GraphOS identity. Each configuration profile has an associated [API key](https://www.apollographql.com/docs/graphos/api-keys), which determines its permissions. You manage your configuration profiles with the `rover config` set of commands.

## Displaying configuration profiles

### `config list`

The `config list` command lists all of your stored configuration profiles:

```text
rover config list

Profiles:

default
sso
```

### `config whoami`

The `config whoami` command displays the details of your current active configuration profile:

```text
rover config whoami

Checking identity of your API key against the registry.
Key Type: USER
User ID: gh.StephenBarlow
Origin: --profile default
API Key: user************************************abcd
```

## Creating configuration profiles

### `config auth`

You create a new configuration profile with the `config auth` command:

```text
rover config auth

Go to https://go.apollo.dev/r/auth and create a new Personal API Key.
Copy the key and paste it into the prompt below.
>
```

By default, your configuration profile is saved with the name `default`. You can specify a different name with the `--profile` option:

```text
rover config auth --profile sso
```

## Deleting configuration profiles

### `config delete`

The `config delete` command deletes a single configuration profile, specified by its name:

```text
rover config delete sso

Successfully deleted profile "sso"
```

### `config clear`

The `config clear` command deletes all of your stored configuration profiles:

```text
rover config clear

Successfully cleared all configuration.
```
