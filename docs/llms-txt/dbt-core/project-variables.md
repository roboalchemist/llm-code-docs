# Source: https://docs.getdbt.com/docs/build/project-variables.md

# Project variables

dbt provides a mechanism called [variables](https://docs.getdbt.com/reference/dbt-jinja-functions/var.md) to provide data to models for compilation. Variables allow you to define configurable values for your project instead of hardcoding them in SQL.

<!-- -->

<!-- -->

You might use variables to [configure timezones](https://github.com/dbt-labs/snowplow/blob/0.3.9/dbt_project.yml#L22), set reporting date ranges, [avoid hardcoding table names](https://github.com/dbt-labs/quickbooks/blob/v0.1.0/dbt_project.yml#L23), or otherwise control how models are compiled.

To use a variable in a model, hook, or macro, use the `{{ var('...') }}` function. The `var()` function retrieves the value defined in your project or passed using `--vars`. For more information, see [About var function](https://docs.getdbt.com/reference/dbt-jinja-functions/var.md).

Note, refer to [YAML tips](https://docs.getdbt.com/docs/build/dbt-tips.md#yaml-tips) for more YAML information.

<!-- -->

### Defining variables in `dbt_project.yml`[​](#defining-variables-in-dbt_projectyml "Direct link to defining-variables-in-dbt_projectyml")

info

Jinja is not supported within the `vars` config, and all values will be interpreted literally.

To define variables in a dbt project, add a `vars` config to your `dbt_project.yml` file. These `vars` can be scoped globally, or to a specific package imported in your project.

dbt\_project.yml

```yaml
name: my_dbt_project
version: 1.0.0

config-version: 2

vars:
  # The `start_date` variable will be accessible in all resources
  start_date: '2016-06-01'

  # The `platforms` variable is only accessible to resources in the my_dbt_project project
  my_dbt_project:
    platforms: ['web', 'mobile']

  # The `app_ids` variable is only accessible to resources in the snowplow package
  snowplow:
    app_ids: ['marketing', 'app', 'landing-page']

models:
    ...
```

<!-- -->

### Defining variables on the command line[​](#defining-variables-on-the-command-line "Direct link to Defining variables on the command line")

<!-- -->

The `dbt_project.yml` file is a great place to define variables that rarely change.

When you need to override a variable for a specific run, use the `--vars` command line option. For example, when you want to test with a different date range, run models with environment-specific settings, or adjust behavior dynamically.

Use `--vars` to pass one or more variables to a dbt command. Provide the argument as a YAML dictionary string.

For example:

```text
$ dbt run --vars '{"event_type": "signup"}'
```

Inside a model or macro, access the value using the `var()` function:

```text
select '{{ var("event_type") }}' as event_type
```

When you pass variables using `--vars`, you can access them anywhere you use the `var()` function in your project.

You can pass multiple variables at once:

```text
$ dbt run --vars '{event_type: signup, region: us}'
```

If only one variable is being set, the brackets are optional:

```text
$ dbt run --vars 'event_type: signup'
```

The `--vars` argument accepts a YAML dictionary as a string on the command line. YAML is convenient because it does not require strict quoting as with JSON.

Both of the following are valid and equivalent:

```text
$ dbt run --vars '{"key": "value", "date": 20180101}'
$ dbt run --vars '{key: value, date: 20180101}'
```

Variables defined using `--var`, override values defined in `dbt_project.yml`. This makes `--vars` useful for temporarily overriding configuration without changing your committed project files. For the complete order of precedence (including package-scoped variables and default values defined in `var()`), see [Variable precedence](https://docs.getdbt.com/docs/build/project-variables.md#variable-precedence).

You can find more information on defining dictionaries with YAML [here](https://github.com/Animosity/CraftIRC/wiki/Complete-idiot%27s-introduction-to-yaml).

### Variable precedence[​](#variable-precedence "Direct link to Variable precedence")

<!-- -->

<!-- -->

If dbt is unable to find a definition for a variable after checking all possible variable declaration places, then a compilation error will be raised.

**Note:** Variable scope is based on the node ultimately using that variable. Imagine the case where a model defined in the root project is calling a macro defined in an installed package. That macro, in turn, uses the value of a variable. The variable will be resolved based on the *root project's* scope, rather than the package's scope.

### Questions from the Community[​](#questions-from-the-community "Direct link to Questions from the Community")

![Loading](/img/loader-icon.svg)[Ask the Community](https://discourse.getdbt.com/new-topic?category=help\&tags=variables "Ask the Community")

## Was this page helpful?

YesNo

[Privacy policy](https://www.getdbt.com/cloud/privacy-policy)[Create a GitHub issue](https://github.com/dbt-labs/docs.getdbt.com/issues)

This site is protected by reCAPTCHA and the Google [Privacy Policy](https://policies.google.com/privacy) and [Terms of Service](https://policies.google.com/terms) apply.
