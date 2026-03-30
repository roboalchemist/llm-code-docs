# Source: https://www.apollographql.com/docs/graphos/connectors/tooling/cli-tools.md

# CLI Tools for Connectors

## Available tools

* [`rover connector test`](https://www.apollographql.com/docs/graphos/connectors/tooling/cli-tools.md#rover-connector-test): Unit testing framework for connectors
* [`rover connector list`](https://www.apollographql.com/docs/graphos/connectors/tooling/cli-tools.md#rover-connector-list): List the connectors in a graph with identifiers to use in `test` and `run`
* [`rover connector run`](https://www.apollographql.com/docs/graphos/connectors/tooling/cli-tools.md#rover-connector-run): Run a single connector and inspect its input and output
* [`rover connector analyze`](https://www.apollographql.com/docs/graphos/connectors/tooling/cli-tools.md#rover-connector-analyze): Captures snapshots of request and response data from calling live services
* [`rover connector generate`](https://www.apollographql.com/docs/graphos/connectors/tooling/cli-tools.md#rover-connector-generate): Generate a schema from a collection of analysis snapshots

## `rover connector test`

[Learn more about testing Connectors](https://www.apollographql.com/docs/graphos/connectors/testing).

```log
Usage: rover connector test [OPTIONS]

Options:
  -f, --file <FILE>
          Defines a single test suite file source If no directory is passed. It will execute all test cases in that file. If this flag is not present it will default to `--directory tests/` and self discover any files in `./tests/**/*.connector.yaml`

  -q, --quiet
          Hides test progression. Defaults to 'false'

  -d, --directory <DIRECTORY>
          Defines a test suite directory, will look for any file ending in `.connector.yml`. If no directory and no file is passed, it will default to `--directory tests/` and self discover any files in `./tests/**/*.connector.yaml`

  -v, --verbose
          Enable verbose logging. Defaults to 'false'

          NOTE: Overrides the --log-level flag

  -l, --log-level <LEVEL>
          Sets the log-level of the CLI. Defaults to 'INFO'

      --no-fail-fast
          Avoids failure on asserting error. Failures and errors encountered will be reported at the end of the execution. Recommended flag for CI environments

      --schema <SCHEMA_PATH>
          Schema file to override `config.schema` (or missing fields) for all test suites executed

  -o, --output <OUTPUT>
          JUnit XML Report output location

  -h, --help
          Print help (see a summary with '-h')
```

## `rover connector list`

This command lists all Connectors in a GraphQL schema file. If `supergraph.yml` contains only one subgraph, the schema is automatically detected. Otherwise, use the `--schema` flag to specify the GraphQL schema file to list all Connectors from.

## `rover connector run`

This command executes a Connector against a live service.

To run a Connector, specify the following parameters:

* `--path`: the path to the GraphQL schema file
* `--connector-id`: the specific Connector to run within that schema. See [Connector IDs](https://www.apollographql.com/docs/graphos/connectors/tooling/cli-tools.md#connector-ids) for more information.
* `--variables`: any Connector variables, expressed as a JSON object, to use when calling the Connector. For a list of available variables, see the [Variable reference documentation](https://www.apollographql.com/docs/graphos/connectors/mapping/variables).

```shell
rover connector run \
--path build/connectors/output.graphql \
--connector-id Query.users_by_id \
--variables '{"$args": {"users": "1"}}'
```

This returns a response like the following:

```json
{
  "request": {
    "method": "GET",
    "uri": "http://localhost:5050/users/1",
    "headers": {},
    "problems": []
  },
  "response": {
    "body": {
      "greeting": "hi",
      "id": "1",
      "theme": "purple",
      "username": "Bob"
    },
    "status": 200,
    "headers": {
      "server": "Werkzeug/3.1.3 Python/3.9.6",
      "date": "Fri, 12 Sep 2025 14:23:10 GMT",
      "content-type": "application/json",
      "content-length": "61",
      "connection": "close"
    },
    "problems": [],
    "mapped_data": {
      "greetingSize": 2,
      "id": "1",
      "theme": "purple",
      "username": "Bob"
    }
  }
}

```

Rover outputs a pretty-printed version of the preceding JSON output, but all of the data is the same.

### Connector IDs

A Connector can optionally specify an ID in the `@connect` directive:

```graphql
@connect(id: "MyNiceId", ...)
```

If a custom `id` isn't specified in the `@connect` directive, use the Connector's coordinates.

Coordinates follow the pattern `ParentType.field`. If you have more than one Connector on a type or field, you can use the `[index]` suffix to differentiate Connectors. For example, `Product.reviews`, without an index, refers to the first Connector on the `Product.reviews` field, and `Product.reviews[2]` refers to the third Connector on the same field.

## `rover connector analyze`

This tool only supports macOS.

This tool depends on libssl which is not configured by default on non-macOS platforms.

This command captures snapshots of requests and responses for one or more APIs. You can use these analysis snapshots to define tests with the testing framework or to generate a GraphQL schema.

This command includes the `interactive`, `curl`, and `clean` commands.

### `interactive` command

This command analyzes calls made from your terminal. This includes running a `curl` command against an endpoint, running Python or Java code, or running any shell command.

When you run `rover connector analyze interactive`, the command starts an interactive shell. Run `curl` commands within that interactive shell to collect analysis snapshots.

When you're done collecting data, type `exit` to exit the process.

Interactive analysis ignores calls from clients that don't honor the `HTTP_PROXY` or `GLOBAL_PROXY` environment variables.

### `curl` command

This command captures data from a single request/response using the `curl` command. The `curl` command mimics the `curl` utility flags and inputs, so you can copy and paste an existing `curl` command into the command line.

This command generates an `analysis` directory with snapshots for the request and response.

```log
rover connector analyze curl [OPTIONS] <URL>

Arguments:
  <URL>
          Sets the endpoint to call

Options:
  -H, --headers <HEADERS>...
          Headers to include in request

  -q, --quiet
          Hides test progression. Defaults to 'false'

  -v, --verbose
          Enable verbose logging. Defaults to 'false'.

          NOTE: Overrides the --log-level flag

  -X, --method <REQUEST>
          Request method to use for call

  -l, --log-level <LEVEL>
          Sets the log-level of the CLI. Defaults to 'Warn'

  -t, --timeout <CONNECT_TIMEOUT>
          Connection timeout in seconds

  -d, --data <DATA>
          Add JSON data to the request

  -a, --analysis-dir <ANALYSIS_DIR>
          Set analysis directory to save data to

  -h, --help
          Print help (see a summary with '-h')
```

```sh
$ rover connector analyze curl -X GET 'https://httpbin.org/json?name=Your-Name' -H 'accept: application/json' -H 'x-user: 123'
```

The command generates the following files:

#### `analysis/<id>_request.http`

```http
GET https://httpbin.org/json?name=Julia
accept: application/json
x-user: 123
```

#### `analysis/<id>_response.json`

```json
{
  "status": 200,
  "headers": [
    [
      "x-user-id",
      "ca42b19d-9068-4818-bb19-174fcf6e2e2f"
    ]
  ]
}
```

Only non-standard headers (`x-<HEADER_NAME>`) are stored in the response file.

#### `analysis/<id>_body.json`

```json
{
  "slideshow": {
    "author": "Yours Truly", 
    "date": "date of publication", 
    "slides": [
      {
        "title": "Wake up to WonderWidgets!", 
        "type": "all"
      }, 
      {
        "items": [
          "Why <em>WonderWidgets</em> are great", 
          "Who <em>buys</em> WonderWidgets"
        ], 
        "title": "Overview", 
        "type": "all"
      }
    ], 
    "title": "Sample Slide Show"
  }
}
```

### `clean` command

This command removes the `analysis/` directory and its contents.

## `rover connector generate`

This tool only supports macOS.

This tool depends on libssl which is not configured by default on non-macOS platforms.

This command generates a GraphQL schema from analysis data.

You need [existing analysis data](https://www.apollographql.com/docs/graphos/connectors/tooling/cli-tools.md#rover-connector-analyze) to run this command.

By default, this command loads data from `./analysis` and generates a schema at `./build/connectors/output.graphql`.

You can customize the output directory, filenames, and where to load analysis snapshots using CLI options.

```log
Usage: rover connector generate [OPTIONS]
Options:
  -n, --name <NAME>
           Sets the name of the generated file (the generated file will be named `<name>.graphql`).
          
          Defaults to `output`
  -q, --quiet
          Hides test progression. Defaults to 'false'
  -a, --analysis-dir <ANALYSIS_DIR>
          Set analysis directory to load data from.
          
          Defaults to `./analysis/`
  -v, --verbose
          Enable verbose logging. Defaults to 'false'.
          
          NOTE: Overrides log-level
  -l, --log-level <LEVEL>
          Sets the log-level of the CLI. Defaults to 'Warn'
          
  -o, --output-dir <OUTPUT_DIR>
          Set a custom directory to generate output files to.
          
          Defaults to `build/connectors/`.
  -h, --help
          Print help (see a summary with '-h')
```

* Queries come from `GET` requests without a `body` and with only ID path arguments and/or query parameters.
* Mutations come from other HTTP methods, such as `POST` and `PUT`.

The generated schema might need manual adjustments depending on your API patterns or desired field structure. Use the [`run` command](https://www.apollographql.com/docs/graphos/connectors/tooling/cli-tools.md#rover-connector-run) to test and refine the generated schemas.
