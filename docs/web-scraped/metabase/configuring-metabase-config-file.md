# Source: https://www.metabase.com/docs/latest/configuring-metabase/config-file

<div>

1.  [Home](/docs/latest/)
2.  [Configuring Metabase](/docs/latest/configuring-metabase/start)

</div>

<div>

[ v0.57 ![](data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMzIiIGhlaWdodD0iMzIiIHZpZXdib3g9IjAgMCAzMiAzMiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIiBjbGFzcz0iY2hldnJvbiI+CjxwYXRoIG9wYWNpdHk9IjAuOSIgZD0iTTMgOC45NjMzOEwxNiAyMS45NjM0TDI5IDguOTYzMzgiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSI1IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) ]

-   [v0.56](/docs/v0.56)
-   [v0.55](/docs/v0.55)
-   [v0.54](/docs/v0.54)
-   [v0.53](/docs/v0.53)
-   [v0.52](/docs/v0.52)
-   [v0.51](/docs/v0.51)
-   [v0.50](/docs/v0.50)
-   [v0.49](/docs/v0.49)
-   [v0.48](/docs/v0.48)
-   [See more](/docs/all)

[![](data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSIyNCIgaGVpZ2h0PSIyNCIgdmlld2JveD0iMCAwIDI0IDI0IiBmaWxsPSJub25lIj48cGF0aCBzdHJva2U9IiM1MDlFRTMiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlLXdpZHRoPSIxLjUiIGQ9Ik0xNi4yODMgMTIuMjYgMTUuNSAxNWwtLjc4My0yLjc0YTQuMzMzIDQuMzMzIDAgMCAwLTIuOTc1LTIuOTc2TDkgOC41bDIuNzQtLjc4M2E0LjMzMyA0LjMzMyAwIDAgMCAyLjk3Ni0yLjk3NUwxNS41IDJsLjc4MyAyLjc0YTQuMzMzIDQuMzMzIDAgMCAwIDIuOTc1IDIuOTc2TDIyIDguNWwtMi43NC43ODNhNC4zMzQgNC4zMzQgMCAwIDAtMi45NzYgMi45NzVsLS4wMDEuMDAxWk02LjUgMjJsLjU5MS0xLjc3NGEzLjM3NSAzLjM3NSAwIDAgMSAyLjEzNS0yLjEzNUwxMSAxNy41bC0xLjc3NC0uNTkxYTMuMzc1IDMuMzc1IDAgMCAxLTIuMTM1LTIuMTM0TDYuNSAxM2wtLjU5MSAxLjc3NGEzLjM3NSAzLjM3NSAwIDAgMS0yLjEzNCAyLjEzNUwyIDE3LjVsMS43NzUuNTkxYTMuMzc1IDMuMzc1IDAgMCAxIDIuMTM0IDIuMTM0TDYuNSAyMloiPjwvcGF0aD48L3N2Zz4=) What's new](/releases)

</div>

<div>

</div>

# Configuration file

![](data:image/svg+xml;base64,PHN2ZyBjbGFzcyB3aWR0aD0iMjQiIGhlaWdodD0iMjQiIHZpZXdib3g9IjAgMCAyNiAyNiIgZmlsbD0ibm9uZSI+CiAgPHBhdGggZD0iTTEyIDEzVjE1IiBzdHJva2Utd2lkdGg9IjIiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCIgc3Ryb2tlPSIjNTA5RUUzIj48L3BhdGg+CiAgPHBhdGggZD0iTTEyIDEwQzEyLjU1MjMgMTAgMTMgOS41NTIyOCAxMyA5QzEzIDguNDQ3NzIgMTIuNTUyMyA4IDEyIDhDMTEuNDQ3NyA4IDExIDguNDQ3NzIgMTEgOUMxMSA5LjU1MjI4IDExLjQ0NzcgMTAgMTIgMTBaIiBmaWxsPSIjNTA5RUUzIj48L3BhdGg+CiAgPHBhdGggZD0iTTEyIDE5LjI1QzE2LjAwNDEgMTkuMjUgMTkuMjUgMTYuMDA0MSAxOS4yNSAxMkMxOS4yNSA3Ljk5NTk0IDE2LjAwNDEgNC43NSAxMiA0Ljc1QzcuOTk1OTQgNC43NSA0Ljc1IDcuOTk1OTQgNC43NSAxMkM0Ljc1IDE2LjAwNDEgNy45OTU5NCAxOS4yNSAxMiAxOS4yNVoiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiIHN0cm9rZT0iIzUwOUVFMyI+PC9wYXRoPgo8L3N2Zz4=)

Loading from a configuration file is only available on [Pro](/product/pro) and [Enterprise](/product/enterprise) plans (only on self-hosted plans).

On self-hosted [Pro](/product/pro) and [Enterprise](/product/enterprise) plans, Metabase supports initialization on launch from a config file named `config.yml`. The config file should be located at:

-   The current directory (the directory where the running Metabase JAR is located).
-   The path specified by the `MB_CONFIG_FILE_PATH` [environment variable](./environment-variables).

The settings in the config file work the same as if you'd set the settings in the Admin Settings in your Metabase. Settings defined in this configuration file will update any existing settings. If, for example, a database already exists (that is, you'd already added it via the initial set up or **Admin settings** \> **Databases**, Metabase will update the database entry based on the data in the config file). Which means: if you define a setting in the config file, and then later change that setting in your Metabase application, keep in mind that the config file will overwrite that change whenever Metabase restarts. Let's reiterate that in a blockquote:

> **Whenever Metabase restarts and loads your config file, the settings in the config file will *overwrite* any changes to those settings made in the Metabase UI.**

The config file settings are NOT treated as a hardcoded source of truth (like [environment variables](./environment-variables) are). Settings set by environment variables cannot be changed, even in the Admin settings in the application itself.

## Example config template

See [Config template](./config-template).

## Config setup

The config file is split up into sections: `version` and `config.` Under `config`, you can specify:

-   [Users](#users)
-   [Databases](#databases)
-   [Settings](#settings)

Like so:

``` highlight
version: 1
config:
  settings:
    - ...
  users:
    - ...
  databases:
    - ...
```

The config file must also include a `version` key, which is just a convenience field for you to help you keep track of your config file versions.

## Users

The first user created in a Metabase instance is an Admin. The first user listed in the config file may be designated an admin, but not necessarily. If someone has already spun up and logged into that Metabase for the first time, Metabase will make that first user an admin. Additionally, you can specify a user account as an admin by using the `is_superuser: true` key.

In the following example, assuming that the Metabase hasn't already been set up (which creates the first user) both users `first@example.com` and `admin@example.com` will be admins: `first@example.com` because it's the first user account on the list, and `admin@example.com` because that user has the `is_superuser` flag set to true.

``` highlight
version: 1
config:
  users:
    - first_name: First
      last_name: Person
      password: metabot1
      email: first@example.com
    - first_name: Normal
      last_name: Person
      password: metabot1
      email: normal@example.com
    - first_name: Admin
      last_name: Person
      password: metabot1
      is_superuser: true
      email: admin@example.com
```

If the Metabase has already been set up, then `first@example.com` will be loaded as a normal user.

## Databases

On a new Metabase, the example below sets up an admin user account and one database connection.

``` highlight
version: 1
config:
  users:
    - first_name: Cam
      last_name: Era
      password: 2cans3cans4cans
      email: cam@example.com
  databases:
    - name: test-data (Postgres)
      engine: postgres
      details:
        host: localhost
        port: 5432
        user: dbuser
        password: "}"
        dbname: test-data
```

To determine which keys you can specify for a database, check out the fields available in Metabase itself for the database that you want to add.

### Setting up uploads on a database

You can also configure [uploads](../databases/uploads) in the config file with the following settings:

-   `uploads_enabled`: Boolean
-   `uploads_schema_name`: String
-   `uploads_table_prefix`: String

Here's an example:

``` highlight
version: 1
config:
  users:
    - first_name: Cam
      last_name: Era
      password: 2cans3cans4cans
      email: cam@example.com
  databases:
    - name: test-data (Postgres)
      engine: postgres
      details:
        host: localhost
        port: 5432
        user: dbuser
        password: "}"
        dbname: test-data
      uploads_enabled: true
      uploads_schema_name: uploads
      uploads_table_prefix: uploads_
```

See [Uploads](../databases/uploads).

## API keys

You can use the config file to create API keys, which is useful for automated deployments and keeping API keys stable across environments.

You can add API keys like so:

``` highlight
version: 1
config:
  users:
    - first_name: Cam
      last_name: Era
      password: 2cans3cans4cans
      email: cam@example.com
  api-keys:
    - name: "Admin API key"
      group: admin
      creator: cam@example.com
      key: mb_firsttestapikey
    - name: "All Users API key"
      group: all-users
      creator: cam@example.com
      key: mb_secondtestapikey
```

You can also use an environment variable to supply an API key, like so:

``` highlight
api-keys:
  - name: "ENV API Key"
    key: "}"
    creator: "admin@example.com"
    group: "admin"
```

See below for more on [environment variables in the config file](#referring-to-environment-variables-in-the-configyml).

API keys that you create (the value of the `key`) must have the format `mb_` followed by a [Base64](https://en.wikipedia.org/wiki/Base64) string (if you're wearing formal attire, you'd say a *tetrasexagesimal* string). So, `mb_` followed by letters and numbers, minimum: 12 characters, maximum: 254 characters. Concretely, the API key you create must satisfy the following regular expression: `mb_[A-Za-z0-9+/=]+`.

You can generate a handsome API key using the `openssl rand` command:

``` highlight
echo "mb_$(openssl rand -base64 32)"
```

Which would generate something like:

``` highlight
mb_aDqk1Tc4ZotWb2TyjHY71glALKlB+g75dLgmSufWGLc=
```

Some other things to note about API keys in the config file:

-   The `creator` of an API key must be an admin. This means either a) your Metabase must already have at least one admin account, or b) you need to add an admin account in the `users` section of the config file.
-   The keys themselves can be assigned to one of two groups: `admin` or `all-users`. The config file restricts `group` assignment to these groups because they're the only ones that Metabase *always* initializes.
-   The permissions for the key correspond to the permissions granted to its `group` (not its `creator`).
-   If Metabase finds an existing API key with the same *name* as a key in the config file, it will preserve the existing key (i.e., it won't overwrite the existing key with the key in the config file). For example, if you initially set up an API key, then later regenerate the key in the Metabase user interface, loading Metabase with the config file won't overwrite that regenerated key (which means the `key` in the config file will no longer work).
-   If you *do* want to overwrite the existing key from the config file, you'll need to first [delete the existing key](../people-and-groups/api-keys#deleting-api-keys). If you want to keep both keys, you'll need to rename the key in the config file.

> The config file also contains an [`api-key`](./environment-variables#mb_api_key) key in the `settings` section of the config file. This setting *doesn't* create API keys; it's used for string-matching in the header for authenticating requests to the `/notify` endpoint.

## Referring to environment variables in the `config.yml` 

As shown in the examples above, environment variables can be specified with template tags like so:

``` highlight
setting: "}"
```

Note the quote marks wrapping the template `"}"`; if you don't include the quotes, the YAML parser won't know it's a string template for Metabase to expand, and Metabase won't know to swap in the env var's value.

Metabase doesn't support recursive expansion, so if one of your environment variables references *another* environment variable, you're going to have a bad time.

## Values with special characters in the `config.yml` 

If a value contains double braces (`}}` or `), you must use triple braces to tell the config parser to use the literal value. For example, if your password was `MetaPa$$123, you'd need to wrap the value in triple braces, like so:

``` highlight
password: "}}"
```

Note the quote marks in `"}}"`.

## Disable initial database sync

When loading a data model from a serialized export, you want to disable the scheduler so that the Metabase doesn't try to sync.

To disable the initial database sync, you can add `config-from-file-sync-database` to the `settings` list and set the value to `false`. The setting `config-from-file-sync-database` must come *before* the databases list, like so:

``` highlight
version: 1
config:
  settings:
    config-from-file-sync-databases: false
  databases:
    - name: my-database
      engine: postgres
      details: ...
```

## Settings

In this config file, you can specify *any* Admin setting.

In general, the settings you can set in the `settings` section of this config file map to the [environment variables](./environment-variables), so check them out to see which settings you can use in your config file. The actual key that you include in the config file differs slightly from the format used for environment variables. For environment variables, the form is in screaming snake case, prefixed by an `MB`:

``` txt
MB_NAME_OF_VARIABLE
```

Whereas in the config file, you'd translate that to:

``` txt
name-of-variable
```

So for example, if you wanted to specify the `MB_EMAIL_FROM_NAME` in the `config.yml` file:

``` highlight
version: 1
config:
  settings:
    config-from-file-sync-databases: false
    email-from-name: Stampy von Mails-a-lot
  databases:
    - name: my-database
      engine: h2
      details: ...
```

But you can set any of the Admin settings with the config file (for a list of settings, check out the [config file template](./config-template)). You can also browse the list of [environment variable](./environment-variables) to see what you can configure (though note that not all environment variables can be set via the config file.)

## Loading a new Metabase from a config file

Since loading from a config file is a Pro/Enterprise feature: for new installations, you'll need to supply Metabase with a token using the `MB_PREMIUM_EMBEDDING_TOKEN` environment variable.

``` highlight
MB_PREMIUM_EMBEDDING_TOKEN="[your token]" java --add-opens java.base/java.nio=ALL-UNNAMED -jar metabase.jar
```

## Further reading

-   [Config file template](./config-template)
-   [Environment variables](./environment-variables)

<div>

Read docs for other [versions of Metabase](/docs/all).

</div>

###### Was this helpful?

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0ibWUtMSIgd2lkdGg9IjE4IiBoZWlnaHQ9IjE4IiB2aWV3Ym94PSIwIDAgMjQgMjQiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CiAgICA8cGF0aCBkPSJNMTAuNjY2NyA3LjMzMzMzSDE0LjYzNjdDMTQuOTIwNyA3LjMzMzM0IDE1LjIwMDEgNy40MDU5NSAxNS40NDgyIDcuNTQ0MjdDMTUuNjk2MyA3LjY4MjU5IDE1LjkwNDkgNy44ODIwMiAxNi4wNTQzIDguMTIzNjRDMTYuMjAzNiA4LjM2NTI1IDE2LjI4ODggOC42NDEwNCAxNi4zMDE2IDguOTI0OEMxNi4zMTQ0IDkuMjA4NTcgMTYuMjU0NSA5LjQ5MDkgMTYuMTI3NSA5Ljc0NUwxMy4yMTA4IDE1LjU3ODNDMTMuMDcyNCAxNS44NTU0IDEyLjg1OTUgMTYuMDg4NCAxMi41OTYgMTYuMjUxMkMxMi4zMzI1IDE2LjQxNCAxMi4wMjg5IDE2LjUwMDEgMTEuNzE5MiAxNi41SDguMzcxNjdDOC4yMzU4MyAxNi41IDguMSAxNi40ODMzIDcuOTY3NSAxNi40NUw0LjgzMzMzIDE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzVjMuMTY2NjdDMTAuNjY2NyAyLjcyNDY0IDEwLjQ5MTEgMi4zMDA3MiAxMC4xNzg1IDEuOTg4MTZDOS44NjU5NSAxLjY3NTU5IDkuNDQyMDMgMS41IDkgMS41SDguOTIwODNDOC41MDQxNyAxLjUgOC4xNjY2NyAxLjgzNzUgOC4xNjY2NyAyLjI1NDE3QzguMTY2NjcgMi44NDkxNyA3Ljk5MDgzIDMuNDMwODMgNy42NiAzLjkyNTgzTDQuODMzMzMgOC4xNjY2N1YxNS42NjY3TTEwLjY2NjcgNy4zMzMzM0g5TTQuODMzMzMgMTUuNjY2N0gzLjE2NjY3QzIuNzI0NjQgMTUuNjY2NyAyLjMwMDcyIDE1LjQ5MTEgMS45ODgxNiAxNS4xNzg1QzEuNjc1NTkgMTQuODY2IDEuNSAxNC40NDIgMS41IDE0VjlDMS41IDguNTU3OTcgMS42NzU1OSA4LjEzNDA1IDEuOTg4MTYgNy44MjE0OUMyLjMwMDcyIDcuNTA4OTMgMi43MjQ2NCA3LjMzMzMzIDMuMTY2NjcgNy4zMzMzM0g1LjI1IiBzdHJva2U9IiM1MDllZTMiIHN0cm9rZS13aWR0aD0iMS41IiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiPjwvcGF0aD4KPC9zdmc+) Yes

![](data:image/svg+xml;base64,PHN2ZyBpZCBjbGFzcz0icm90YXRlLTE4MCBtZS0xIiB3aWR0aD0iMTgiIGhlaWdodD0iMTgiIHZpZXdib3g9IjAgMCAyNCAyNCIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KICAgIDxwYXRoIGQ9Ik0xMC42NjY3IDcuMzMzMzNIMTQuNjM2N0MxNC45MjA3IDcuMzMzMzQgMTUuMjAwMSA3LjQwNTk1IDE1LjQ0ODIgNy41NDQyN0MxNS42OTYzIDcuNjgyNTkgMTUuOTA0OSA3Ljg4MjAyIDE2LjA1NDMgOC4xMjM2NEMxNi4yMDM2IDguMzY1MjUgMTYuMjg4OCA4LjY0MTA0IDE2LjMwMTYgOC45MjQ4QzE2LjMxNDQgOS4yMDg1NyAxNi4yNTQ1IDkuNDkwOSAxNi4xMjc1IDkuNzQ1TDEzLjIxMDggMTUuNTc4M0MxMy4wNzI0IDE1Ljg1NTQgMTIuODU5NSAxNi4wODg0IDEyLjU5NiAxNi4yNTEyQzEyLjMzMjUgMTYuNDE0IDEyLjAyODkgMTYuNTAwMSAxMS43MTkyIDE2LjVIOC4zNzE2N0M4LjIzNTgzIDE2LjUgOC4xIDE2LjQ4MzMgNy45Njc1IDE2LjQ1TDQuODMzMzMgMTUuNjY2N00xMC42NjY3IDcuMzMzMzNWMy4xNjY2N0MxMC42NjY3IDIuNzI0NjQgMTAuNDkxMSAyLjMwMDcyIDEwLjE3ODUgMS45ODgxNkM5Ljg2NTk1IDEuNjc1NTkgOS40NDIwMyAxLjUgOSAxLjVIOC45MjA4M0M4LjUwNDE3IDEuNSA4LjE2NjY3IDEuODM3NSA4LjE2NjY3IDIuMjU0MTdDOC4xNjY2NyAyLjg0OTE3IDcuOTkwODMgMy40MzA4MyA3LjY2IDMuOTI1ODNMNC44MzMzMyA4LjE2NjY3VjE1LjY2NjdNMTAuNjY2NyA3LjMzMzMzSDlNNC44MzMzMyAxNS42NjY3SDMuMTY2NjdDMi43MjQ2NCAxNS42NjY3IDIuMzAwNzIgMTUuNDkxMSAxLjk4ODE2IDE1LjE3ODVDMS42NzU1OSAxNC44NjYgMS41IDE0LjQ0MiAxLjUgMTRWOUMxLjUgOC41NTc5NyAxLjY3NTU5IDguMTM0MDUgMS45ODgxNiA3LjgyMTQ5QzIuMzAwNzIgNy41MDg5MyAyLjcyNDY0IDcuMzMzMzMgMy4xNjY2NyA3LjMzMzMzSDUuMjUiIHN0cm9rZT0iIzUwOWVlMyIgc3Ryb2tlLXdpZHRoPSIxLjUiIHN0cm9rZS1saW5lY2FwPSJyb3VuZCIgc3Ryb2tlLWxpbmVqb2luPSJyb3VuZCI+PC9wYXRoPgo8L3N2Zz4=) No

Send

###### Thanks for your feedback! 

[ Want to improve these docs? [Propose a change.](https://github.com/metabase/metabase/blob/master/docs/configuring-metabase/config-file.md) ]