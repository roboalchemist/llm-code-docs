# Source: https://docs.snowflake.com/en/sql-reference/functions/system_begin_debug_application.md

Categories:
:   [System functions](../functions-system.md) (System Control)

# SYSTEM$BEGIN_DEBUG_APPLICATION

Enables [session debug mode](../../developer-guide/native-apps/installing-testing-application.md) for a Snowflake Native App.

## Syntax

```sqlsyntax
SYSTEM$BEGIN_DEBUG_APPLICATION( '<app_name>' [ , <execution_mode>] )
```

## Arguments

`'app_name'`
:   The name of the app on which session debug mode is being enabled.

`execution_mode =`
:   The behavior of commands run during session debug mode. Possible values are:

    * `'AS_APPLICATION'` (DEFAULT)

      All statements are executed as using the same privileges as the app. This mimics the
      behavior of the app in the consumer account.
    * `'AS_SETUP_SCRIPT'`

      All statements are executed using the same privileges as the setup script of the app. This
      allows providers to test the setup script using session debug mode.

## Usage notes

* Providers can use this function to enable session debug mode on an app created using development mode.
  This allows providers to test the behavior of the app and setup script.

## Examples

The following example shows how to set the execution mode to `AS_APPLICATION`:

```sqlexample
SELECT SYSTEM$BEGIN_DEBUG_APPLICATION( 'hello_snowflake_app', execution_mode ='AS_APPLICATION')
```

The following example show how to set the execution mode to `AS_SETUP_SCRIPT`:

```sqlexample
SELECT SYSTEM$BEGIN_DEBUG_APPLICATION( 'hello_snowflake_app', execution_mode = 'AS_SETUP_SCRIPT')
```
