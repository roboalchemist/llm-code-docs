# Source: https://docs.getdbt.com/reference/global-configs/about-global-configs.md

# About flags (global configs)

In dbt, "flags" (also called "global configs") are configurations for fine-tuning *how* dbt runs your project. They differ from [resource-specific configs](https://docs.getdbt.com/reference/configs-and-properties.md) that tell dbt about *what* to run.

Flags control things like the visual output of logs, whether to treat specific warning messages as errors, or whether to "fail fast" after encountering the first error. Flags are "global" configs because they are available for all dbt commands and they can be set in multiple places.

There is a significant overlap between dbt's flags and dbt's command line options, but there are differences:

* Certain flags can only be set in [`dbt_project.yml`](https://docs.getdbt.com/reference/dbt_project.yml.md) and cannot be overridden for specific invocations via CLI options.
* If a CLI option is supported by specific commands, rather than supported by all commands ("global"), it is generally not considered to be a "flag".

### Setting flags[​](#setting-flags "Direct link to Setting flags")

<!-- -->

There are multiple ways of setting flags, which depend on the use case:

* **[Project-level `flags` in `dbt_project.yml`](https://docs.getdbt.com/reference/global-configs/project-flags.md):** Define version-controlled defaults for everyone running this project. Also, opt in or opt out of [behavior changes](https://docs.getdbt.com/reference/global-configs/behavior-changes.md) to manage your migration off legacy functionality.
* **[Environment variables](https://docs.getdbt.com/reference/global-configs/environment-variable-configs.md):** Define different behavior in different runtime environments (development vs. production vs. [continuous integration](https://docs.getdbt.com/docs/deploy/continuous-integration.md), or different behavior for different users in development (based on personal preferences).
* **[CLI options](https://docs.getdbt.com/reference/global-configs/command-line-options.md):** Define behavior specific to *this invocation*. Supported for all dbt commands.

The most specific setting "wins." If you set the same flag in all three places, the CLI option will take precedence, followed by the environment variable, and finally, the value in `dbt_project.yml`. If you set the flag in none of those places, it will use the default value defined within dbt.

Most flags can be set in all three places:

```yaml
# dbt_project.yml
flags:
  # set default for running this project -- anywhere, anytime, by anyone
  fail_fast: true
```

```bash
# set this environment variable to 'True' (bash syntax)
export DBT_FAIL_FAST=1
dbt run
```

```bash
dbt run --fail-fast # set to True for this specific invocation
dbt run --no-fail-fast # set to False
```

There are two categories of exceptions:

1. **Flags setting file paths:** Flags for file paths that are relevant to runtime execution (for example, `--log-path` or `--state`) cannot be set in `dbt_project.yml`. To override defaults, pass CLI options or set environment variables (`DBT_LOG_PATH`, `DBT_STATE`). Flags that tell dbt where to find project resources (for example, `model-paths`) are set in `dbt_project.yml`, but as a top-level key, outside the `flags` dictionary; these configs are expected to be fully static and never vary based on the command or execution environment.
2. **Opt-in flags:** Flags opting in or out of [behavior changes](https://docs.getdbt.com/reference/global-configs/behavior-changes.md) can *only* be defined in `dbt_project.yml`. These are intended to be set in version control and migrated via pull/merge request. Their values should not diverge indefinitely across invocations, environments, or users.

### Accessing flags[​](#accessing-flags "Direct link to Accessing flags")

Custom user-defined logic, written in Jinja, can check the values of flags using [the `flags` context variable](https://docs.getdbt.com/reference/dbt-jinja-functions/flags.md).

```yaml
# dbt_project.yml

on-run-start:
  - '{{ log("I will stop at the first sign of trouble", info = true) if flags.FAIL_FAST }}'
```

## Available flags[​](#available-flags "Direct link to Available flags")

Because the values of `flags` can differ across invocations, we strongly advise against using `flags` as an input to configurations or dependencies (`ref` + `source`) that dbt resolves [during parsing](https://docs.getdbt.com/reference/parsing.md#known-limitations).

### Common flag examples[​](#common-flag-examples "Direct link to Common flag examples")

Use the `--target` flag to specify which target (environment) to use when running dbt commands. For example:

```bash
dbt run --target dev
dbt run --target prod
dbt build --target staging
```

The `--target` flag allows you to run the same dbt project against different environments without modifying your configuration files. Define the target in your `profiles.yml` file. Learn more about [connection profiles and targets](https://docs.getdbt.com/docs/local/profiles.yml.md#understanding-targets-in-profiles).

|   |
| - |

| Flag name                                                                                                                                         | Type     | Default                           | Supported in project?   | Environment variable                                   | CLI options                                                                                       | Supported in dbt CLI? |
| ------------------------------------------------------------------------------------------------------------------------------------------------- | -------- | --------------------------------- | ----------------------- | ------------------------------------------------------ | ------------------------------------------------------------------------------------------------- | --------------------- |
| [cache\_selected\_only](https://docs.getdbt.com/reference/global-configs/cache.md)                                                                | boolean  | False                             | ✅                      | `DBT_CACHE_SELECTED_ONLY`                              | `--cache-selected-only`, `--no-cache-selected-only`                                               | ✅                    |
| [clean\_project\_files\_only](https://docs.getdbt.com/reference/commands/clean.md#--clean-project-files-only)                                     | boolean  | True                              | ❌                      | `DBT_CLEAN_PROJECT_FILES_ONLY`                         | `--clean-project-files-only, --no-clean-project-files-only`                                       | ❌                    |
| [debug](https://docs.getdbt.com/reference/global-configs/logs.md#debug-level-logging)                                                             | boolean  | False                             | ✅                      | `DBT_DEBUG`                                            | `--debug`, `--no-debug`                                                                           | ✅                    |
| [defer](https://docs.getdbt.com/reference/node-selection/defer.md)                                                                                | boolean  | False                             | ❌                      | `DBT_DEFER`                                            | `--defer`, `--no-defer`                                                                           | ✅ (default)          |
| [defer\_state](https://docs.getdbt.com/reference/node-selection/defer.md)                                                                         | path     | None                              | ❌                      | `DBT_DEFER_STATE`                                      | `--defer-state`                                                                                   | ❌                    |
| [favor\_state](https://docs.getdbt.com/reference/node-selection/defer.md#favor-state)                                                             | boolean  | False                             | ❌                      | `DBT_FAVOR_STATE`                                      | `--favor-state`, `--no-favor-state`                                                               | ✅                    |
| [empty](https://docs.getdbt.com/docs/build/empty-flag.md)                                                                                         | boolean  | False                             | ❌                      | `DBT_EMPTY`                                            | `--empty`, `--no-empty`                                                                           | ✅                    |
| [event\_time\_start](https://docs.getdbt.com/reference/dbt-jinja-functions/model.md#batch-properties-for-microbatch-models)                       | datetime | None                              | ❌                      | `DBT_EVENT_TIME_START`                                 | `--event-time-start`                                                                              | ✅                    |
| [event\_time\_end](https://docs.getdbt.com/reference/dbt-jinja-functions/model.md#batch-properties-for-microbatch-models)                         | datetime | None                              | ❌                      | `DBT_EVENT_TIME_END`                                   | `--event-time-end`                                                                                | ✅                    |
| [fail\_fast](https://docs.getdbt.com/reference/global-configs/failing-fast.md)                                                                    | boolean  | False                             | ✅                      | `DBT_FAIL_FAST`                                        | `--fail-fast`, `-x`, `--no-fail-fast`                                                             | ✅                    |
| [full\_refresh](https://docs.getdbt.com/reference/resource-configs/full_refresh.md)                                                               | boolean  | False                             | ✅ (as resource config) | `DBT_FULL_REFRESH`                                     | `--full-refresh`, `--no-full-refresh`                                                             | ✅                    |
| [indirect\_selection](https://docs.getdbt.com/reference/node-selection/test-selection-examples.md#syntax-examples)                                | enum     | eager                             | ✅                      | `DBT_INDIRECT_SELECTION`                               | `--indirect-selection`                                                                            | ❌                    |
| [introspect](https://docs.getdbt.com/reference/commands/compile.md#introspective-queries)                                                         | boolean  | True                              | ❌                      | `DBT_INTROSPECT`                                       | `--introspect`, `--no-introspect`                                                                 | ❌                    |
| [log\_cache\_events](https://docs.getdbt.com/reference/global-configs/logs.md#logging-relational-cache-events)                                    | boolean  | False                             | ❌                      | `DBT_LOG_CACHE_EVENTS`                                 | `--log-cache-events`, `--no-log-cache-events`                                                     | ❌                    |
| [log\_format\_file](https://docs.getdbt.com/reference/global-configs/logs.md#log-formatting)                                                      | enum     | default (text)                    | ✅                      | `DBT_LOG_FORMAT_FILE`                                  | `--log-format-file`                                                                               | ❌                    |
| [log\_format](https://docs.getdbt.com/reference/global-configs/logs.md#log-formatting)                                                            | enum     | default (text)                    | ✅                      | `DBT_LOG_FORMAT`                                       | `--log-format`                                                                                    | ❌                    |
| [log\_level\_file](https://docs.getdbt.com/reference/global-configs/logs.md#log-level)                                                            | enum     | debug                             | ✅                      | `DBT_LOG_LEVEL_FILE`                                   | `--log-level-file`                                                                                | ❌                    |
| [log\_level](https://docs.getdbt.com/reference/global-configs/logs.md#log-level)                                                                  | enum     | info                              | ✅                      | `DBT_LOG_LEVEL`                                        | `--log-level`                                                                                     | ❌                    |
| [log\_path](https://docs.getdbt.com/reference/global-configs/logs.md)                                                                             | path     | None (uses `logs/`)               | ❌                      | `DBT_LOG_PATH`                                         | `--log-path`                                                                                      | ❌                    |
| [partial\_parse](https://docs.getdbt.com/reference/global-configs/parsing.md#partial-parsing)                                                     | boolean  | True                              | ✅                      | `DBT_PARTIAL_PARSE`                                    | `--partial-parse`, `--no-partial-parse`                                                           | ✅                    |
| [populate\_cache](https://docs.getdbt.com/reference/global-configs/cache.md)                                                                      | boolean  | True                              | ✅                      | `DBT_POPULATE_CACHE`                                   | `--populate-cache`, `--no-populate-cache`                                                         | ✅                    |
| [print](https://docs.getdbt.com/reference/global-configs/print-output.md#suppress-print-messages-in-stdout)                                       | boolean  | True                              | ❌                      | `DBT_PRINT`                                            | `--print`, `--no-print`                                                                           | ❌                    |
| [printer\_width](https://docs.getdbt.com/reference/global-configs/print-output.md#printer-width)                                                  | int      | 80                                | ✅                      | `DBT_PRINTER_WIDTH`                                    | `--printer-width`                                                                                 | ❌                    |
| [profile](https://docs.getdbt.com/docs/local/profiles.yml.md#about-profiles)                                                                      | string   | None                              | ✅ (as top-level key)   | `DBT_PROFILE`                                          | [`--profile`](https://docs.getdbt.com/docs/local/profiles.yml.md#overriding-profiles-and-targets) | ❌                    |
| [profiles\_dir](https://docs.getdbt.com/docs/local/profiles.yml.md#about-profiles)                                                                | path     | None (current dir, then HOME dir) | ❌                      | `DBT_PROFILES_DIR`                                     | `--profiles-dir`                                                                                  | ❌                    |
| [project\_dir](https://docs.getdbt.com/reference/dbt_project.yml.md)                                                                              | path     |                                   | ❌                      | `DBT_PROJECT_DIR`                                      | `--project-dir`                                                                                   | ❌                    |
| [quiet](https://docs.getdbt.com/reference/global-configs/logs.md#suppress-non-error-logs-in-output)                                               | boolean  | False                             | ❌                      | `DBT_QUIET`                                            | `--quiet`                                                                                         | ✅                    |
| [resource-type](https://docs.getdbt.com/reference/global-configs/resource-type.md) (v1.8+)                                                        | string   | None                              | ❌                      | `DBT_RESOURCE_TYPES`<br />`DBT_EXCLUDE_RESOURCE_TYPES` | `--resource-type`<br />`--exclude-resource-type`                                                  | ✅                    |
| [sample](https://docs.getdbt.com/docs/build/sample-flag.md)                                                                                       | string   | None                              | ❌                      | `DBT_SAMPLE`                                           | `--sample`                                                                                        | ✅                    |
| [send\_anonymous\_usage\_stats](https://docs.getdbt.com/reference/global-configs/usage-stats.md)                                                  | boolean  | True                              | ✅                      | `DBT_SEND_ANONYMOUS_USAGE_STATS`                       | `--send-anonymous-usage-stats`, `--no-send-anonymous-usage-stats`                                 | ❌                    |
| [source\_freshness\_run\_project\_hooks](https://docs.getdbt.com/reference/global-configs/behavior-changes.md#source_freshness_run_project_hooks) | boolean  | True                              | ✅                      | ❌                                                     | ❌                                                                                                | ❌                    |
| [state](https://docs.getdbt.com/reference/node-selection/defer.md)                                                                                | path     | none                              | ❌                      | `DBT_STATE`, `DBT_DEFER_STATE`                         | `--state`, `--defer-state`                                                                        | ❌                    |
| [static\_parser](https://docs.getdbt.com/reference/global-configs/parsing.md#static-parser)                                                       | boolean  | True                              | ✅                      | `DBT_STATIC_PARSER`                                    | `--static-parser`, `--no-static-parser`                                                           | ❌                    |
| [store\_failures](https://docs.getdbt.com/reference/resource-configs/store_failures.md)                                                           | boolean  | False                             | ✅ (as resource config) | `DBT_STORE_FAILURES`                                   | `--store-failures`, `--no-store-failures`                                                         | ✅                    |
| [target\_path](https://docs.getdbt.com/reference/global-configs/json-artifacts.md)                                                                | path     | None (uses `target/`)             | ❌                      | `DBT_TARGET_PATH`                                      | `--target-path`                                                                                   | ❌                    |
| [target](https://docs.getdbt.com/docs/local/profiles.yml.md#about-profiles)                                                                       | string   | None                              | ❌                      | `DBT_TARGET`                                           | [`--target`](https://docs.getdbt.com/docs/local/profiles.yml.md#overriding-profiles-and-targets)  | ❌                    |
| [use\_colors\_file](https://docs.getdbt.com/reference/global-configs/logs.md#color)                                                               | boolean  | True                              | ✅                      | `DBT_USE_COLORS_FILE`                                  | `--use-colors-file`, `--no-use-colors-file`                                                       | ❌                    |
| [use\_colors](https://docs.getdbt.com/reference/global-configs/print-output.md#print-color)                                                       | boolean  | True                              | ✅                      | `DBT_USE_COLORS`                                       | `--use-colors`, `--no-use-colors`                                                                 | ❌                    |
| [use\_experimental\_parser](https://docs.getdbt.com/reference/global-configs/parsing.md#experimental-parser)                                      | boolean  | False                             | ✅                      | `DBT_USE_EXPERIMENTAL_PARSER`                          | `--use-experimental-parser`, `--no-use-experimental-parser`                                       | ❌                    |
| [version\_check](https://docs.getdbt.com/reference/global-configs/version-compatibility.md)                                                       | boolean  | varies                            | ✅                      | `DBT_VERSION_CHECK`                                    | `--version-check`, `--no-version-check`                                                           | ❌                    |
| [warn\_error\_options](https://docs.getdbt.com/reference/global-configs/warnings.md)                                                              | dict     |                                   | ✅                      | `DBT_WARN_ERROR_OPTIONS`                               | `--warn-error-options`                                                                            | ✅                    |
| [warn\_error](https://docs.getdbt.com/reference/global-configs/warnings.md)                                                                       | boolean  | False                             | ✅                      | `DBT_WARN_ERROR`                                       | `--warn-error`                                                                                    | ✅                    |
| [write\_json](https://docs.getdbt.com/reference/global-configs/json-artifacts.md)                                                                 | boolean  | True                              | ✅                      | `DBT_WRITE_JSON`                                       | `--write-json`, `--no-write-json`                                                                 | ✅                    |

Search table...

|                  |   |   |   |   |
| ---------------- | - | - | - | - |
| Loading table... |   |   |   |   |

Search table...

|                  |   |   |   |   |
| ---------------- | - | - | - | - |
| Loading table... |   |   |   |   |
