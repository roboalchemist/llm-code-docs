# Source: https://docs.infrahub.app/reference/infrahub-tests.md

# Tests configuration file

The tests configuration file allows you to define multiple tests for Infrahub resources such as Jinja2 Transformations, Python Transformations, checks and GraphQL queries.

The file should be formatted as a YAML file, have a filename prefixed with `test_` like `test_all.yml` and should be stored somewhere in the [repository](/topics/repository.md).

info

See [this topic](/topics/resources-testing-framework.md) for more details on the available repository configuration options

## Version[​](#version "Direct link to Version")

**Key**: `version`<br />**Type**: string<br />**Mandatory**: <!-- -->❌<br />**Default**: `1.0`<br />

## Infrahub Tests[​](#infrahub-tests "Direct link to Infrahub Tests")

**Key**: `infrahub_tests`<br />**Type**: array of tests<br />**Mandatory**: <!-- -->✅<br />

Each test must define a kind of resource to test as well as the name of the resource which must be a valid resource name matching to the repository configuration.

**Key**: `resource`<br />**Type**: string<br />**Mandatory**: <!-- -->✅<br />**Possible value**: `Check` `Jinja2Transform` `PythonTransform` `GraphQLQuery`<br />

**Key**: `resource_name`<br />**Type**: string<br />**Mandatory**: <!-- -->✅<br />

An optional outcome value for the test can be specified.

**Key**: `expect`<br />**Type**: string<br />**Mandatory**: <!-- -->❌<br />**Default**: `PASS`<br />**Possible value**: `PASS` `FAIL`<br />

Each test must then defined a specification, using the `spec` key, which will set properties for the test itself.

**Key**: `spec`<br />**Type**: dictionary<br />**Mandatory**: <!-- -->✅<br />

Depending on the test, the dictionary `spec` may contain the following keys.

note

When a test has an input or an output property, the value of these can be path to JSON (with the `.json` suffix), YAML (with the `.yaml` or `.yml` suffixes) or plain text files.

### Test kind `check-smoke`[​](#test-kind-check-smoke "Direct link to test-kind-check-smoke")

| Spec | Type   | Description                | Mandatory | Default |
| ---- | ------ | -------------------------- | --------- | ------- |
| kind | string | Static value `check-smoke` | ✅        |         |

### Test kind `check-unit-process`[​](#test-kind-check-unit-process "Direct link to test-kind-check-unit-process")

| Spec      | Type   | Description                                                                                                                       | Mandatory | Default    |
| --------- | ------ | --------------------------------------------------------------------------------------------------------------------------------- | --------- | ---------- |
| directory | string | Path to the directory where the input and output files are located                                                                | ❌        |            |
| input     | string | Path to the file with the input data for the test, can be a relative path from the configuration file or from the directory.      | ❌        | input.json |
| output    | string | Path to the file with the expected output for the test, can be a relative path from the configuration file or from the directory. | ❌        |            |
| kind      | string | Static value `check-unit-process`                                                                                                 | ✅        |            |

### Test kind `check-integration`[​](#test-kind-check-integration "Direct link to test-kind-check-integration")

| Spec      | Type                 | Description                                                                                                                       | Mandatory | Default        |
| --------- | -------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------- | -------------- |
| directory | string               | Path to the directory where the input and output files are located                                                                | ❌        |                |
| input     | string               | Path to the file with the input data for the test, can be a relative path from the configuration file or from the directory.      | ❌        | input.json     |
| output    | string               | Path to the file with the expected output for the test, can be a relative path from the configuration file or from the directory. | ❌        |                |
| variables | string or dictionary | Variables and corresponding values to pass to the GraphQL query                                                                   | ❌        | variables.json |
| kind      | string               | Static value `check-integration`                                                                                                  | ✅        |                |

### Test kind `graphql-query-smoke`[​](#test-kind-graphql-query-smoke "Direct link to test-kind-graphql-query-smoke")

| Spec | Type   | Description                                            | Mandatory | Default |
| ---- | ------ | ------------------------------------------------------ | --------- | ------- |
| kind | string | Static value `graphql-query-smoke`                     | ✅        |         |
| path | string | Path to the file in which the GraphQL query is defined | ✅        |         |

### Test kind `graphql-query-integration`[​](#test-kind-graphql-query-integration "Direct link to test-kind-graphql-query-integration")

| Spec      | Type                 | Description                                                                                                                       | Mandatory | Default        |
| --------- | -------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------- | -------------- |
| directory | string               | Path to the directory where the input and output files are located                                                                | ❌        |                |
| input     | string               | Path to the file with the input data for the test, can be a relative path from the configuration file or from the directory.      | ❌        | input.json     |
| output    | string               | Path to the file with the expected output for the test, can be a relative path from the configuration file or from the directory. | ❌        |                |
| variables | string or dictionary | Variables and corresponding values to pass to the GraphQL query                                                                   | ❌        | variables.json |
| kind      | string               | Static value `graphql-query-integration`                                                                                          | ✅        |                |
| query     | string               | Name of a pre-defined GraphQL query to execute                                                                                    | ✅        |                |

### Test kind `jinja2-transform-smoke`[​](#test-kind-jinja2-transform-smoke "Direct link to test-kind-jinja2-transform-smoke")

| Spec | Type   | Description                           | Mandatory | Default |
| ---- | ------ | ------------------------------------- | --------- | ------- |
| kind | string | Static value `jinja2-transform-smoke` | ✅        |         |

### Test kind `jinja2-transform-unit-render`[​](#test-kind-jinja2-transform-unit-render "Direct link to test-kind-jinja2-transform-unit-render")

| Spec      | Type   | Description                                                                                                                       | Mandatory | Default    |
| --------- | ------ | --------------------------------------------------------------------------------------------------------------------------------- | --------- | ---------- |
| directory | string | Path to the directory where the input and output files are located                                                                | ❌        |            |
| input     | string | Path to the file with the input data for the test, can be a relative path from the configuration file or from the directory.      | ❌        | input.json |
| output    | string | Path to the file with the expected output for the test, can be a relative path from the configuration file or from the directory. | ❌        |            |
| kind      | string | Static value `jinja2-transform-unit-render`                                                                                       | ✅        |            |

### Test kind `jinja2-transform-integration`[​](#test-kind-jinja2-transform-integration "Direct link to test-kind-jinja2-transform-integration")

| Spec      | Type   | Description                                                                                                                       | Mandatory | Default        |
| --------- | ------ | --------------------------------------------------------------------------------------------------------------------------------- | --------- | -------------- |
| directory | string | Path to the directory where the input and output files are located                                                                | ❌        |                |
| input     | string | Path to the file with the input data for the test, can be a relative path from the configuration file or from the directory.      | ❌        | input.json     |
| output    | string | Path to the file with the expected output for the test, can be a relative path from the configuration file or from the directory. | ❌        |                |
| variables |        | Variables and corresponding values to pass to the GraphQL query                                                                   | ❌        | variables.json |
| kind      | string | Static value `jinja2-transform-integration`                                                                                       | ✅        |                |

### Test kind `python-transform-smoke`[​](#test-kind-python-transform-smoke "Direct link to test-kind-python-transform-smoke")

| Spec | Type   | Description                           | Mandatory | Default |
| ---- | ------ | ------------------------------------- | --------- | ------- |
| kind | string | Static value `python-transform-smoke` | ✅        |         |

### Test kind `python-transform-unit-process`[​](#test-kind-python-transform-unit-process "Direct link to test-kind-python-transform-unit-process")

| Spec      | Type   | Description                                                                                                                       | Mandatory | Default    |
| --------- | ------ | --------------------------------------------------------------------------------------------------------------------------------- | --------- | ---------- |
| directory | string | Path to the directory where the input and output files are located                                                                | ❌        |            |
| input     | string | Path to the file with the input data for the test, can be a relative path from the configuration file or from the directory.      | ❌        | input.json |
| output    | string | Path to the file with the expected output for the test, can be a relative path from the configuration file or from the directory. | ❌        |            |
| kind      | string | Static value `python-transform-unit-process`                                                                                      | ✅        |            |

### Test kind `python-transform-integration`[​](#test-kind-python-transform-integration "Direct link to test-kind-python-transform-integration")

| Spec      | Type                 | Description                                                                                                                       | Mandatory | Default        |
| --------- | -------------------- | --------------------------------------------------------------------------------------------------------------------------------- | --------- | -------------- |
| directory | string               | Path to the directory where the input and output files are located                                                                | ❌        |                |
| input     | string               | Path to the file with the input data for the test, can be a relative path from the configuration file or from the directory.      | ❌        | input.json     |
| output    | string               | Path to the file with the expected output for the test, can be a relative path from the configuration file or from the directory. | ❌        |                |
| variables | string or dictionary | Variables and corresponding values to pass to the GraphQL query                                                                   | ❌        | variables.json |
| kind      | string               | Static value `python-transform-unit-process`                                                                                      | ✅        |                |
