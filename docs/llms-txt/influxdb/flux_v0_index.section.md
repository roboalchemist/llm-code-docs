---
title: Flux documentation
description: Flux is a open source functional data scripting language designed for querying, analyzing, and acting on data.
url: https://docs.influxdata.com/flux/v0/
product: Flux
type: section
pages: 17
estimated_tokens: 71874
child_pages:
  - url: https://docs.influxdata.com/flux/v0/write-data/
    title: Write to data sources
  - url: https://docs.influxdata.com/flux/v0/tags/
    title: Related to "Tags"
  - url: https://docs.influxdata.com/flux/v0/stdlib/
    title: Flux standard library
  - url: https://docs.influxdata.com/flux/v0/spec/
    title: Flux language specification
  - url: https://docs.influxdata.com/flux/v0/release-notes/
    title: Flux release notes
  - url: https://docs.influxdata.com/flux/v0/query-data/
    title: Query data sources
  - url: https://docs.influxdata.com/flux/v0/prometheus/
    title: Work with Prometheus
  - url: https://docs.influxdata.com/flux/v0/mcp-server/
    title: Use the InfluxDB documentation MCP server
  - url: https://docs.influxdata.com/flux/v0/join-data/
    title: Join data
  - url: https://docs.influxdata.com/flux/v0/influxdb-versions/
    title: Flux versions in InfluxDB
  - url: https://docs.influxdata.com/flux/v0/get-started/
    title: Get started with Flux
  - url: https://docs.influxdata.com/flux/v0/future-of-flux/
    title: The future of Flux
  - url: https://docs.influxdata.com/flux/v0/function-types/
    title: Flux function types and categories
  - url: https://docs.influxdata.com/flux/v0/function-type-signatures/
    title: Function type signatures
  - url: https://docs.influxdata.com/flux/v0/define-functions/
    title: Define custom functions
  - url: https://docs.influxdata.com/flux/v0/data-types/
    title: Work with Flux data types
---

# Flux documentation

Flux is an open source functional data scripting language designed for querying, analyzing, and acting on data. Flux supports multiple data source types, including:

-   Time series databases (such as [InfluxDB](/flux/v0/query-data/influxdb/))
-   [Relational SQL databases](/flux/v0/query-data/sql/) (such as [MySQL](/flux/v0/query-data/sql/mysql/) and [PostgreSQL](/flux/v0/query-data/sql/postgresql/))
-   [CSV](/flux/v0/query-data/csv/)

Flux unifies code for querying, processing, writing, and acting on data into a single syntax. The language is designed to be usable, readable, flexible, composable, testable, contributable, and shareable.

[Get started with Flux](/flux/v0/get-started/)


---

## Write to data sources

Write to the following data sources with Flux:

-   [InfluxDB](#influxdb)
-   [SQL databases](#sql-databases)

### [InfluxDB](/flux/v0/write-data/influxdb/)

Use [`to()`](/flux/v0/stdlib/influxdata/influxdb/to/) or [`experimental.to()`](/flux/v0/stdlib/experimental/to/) to write data to InfluxDB using Flux.

```js
data
    |> to(bucket: "example-bucket")
```

[Read more](/flux/v0/write-data/influxdb/)

### [SQL databases](/flux/v0/write-data/sql/)

Use [`sql.to()`](/flux/v0/stdlib/sql/to/) to write data to SQL databases with Flux.

```js
import "sql"

sql.to(
    driverName: "postgres",
    dataSourceName: "postgresql://user:password@localhost",
    table: "ExampleTable",
    batchSize: 10000,
)
```

[Read more](/flux/v0/write-data/sql/)


---

## Related to "Tags"

### [Aggregates](/flux/v0/tags/aggregates/)

### [Array](/flux/v0/tags/array/)

### [Basic Types](/flux/v0/tags/basic-types/)

### [Bitwise](/flux/v0/tags/bitwise/)

### [Composite Types](/flux/v0/tags/composite-types/)

### [Csv](/flux/v0/tags/csv/)

### [Data Types](/flux/v0/tags/data-types/)

### [Date/Time](/flux/v0/tags/date/time/)

### [Dynamic Queries](/flux/v0/tags/dynamic-queries/)

### [Dynamic Types](/flux/v0/tags/dynamic-types/)

### [Events](/flux/v0/tags/events/)

### [Filters](/flux/v0/tags/filters/)

### [Flux](/flux/v0/tags/flux/)

### [Functions](/flux/v0/tags/functions/)

### [Generate](/flux/v0/tags/generate/)

### [Geotemporal](/flux/v0/tags/geotemporal/)

### [Http](/flux/v0/tags/http/)

### [Inputs](/flux/v0/tags/inputs/)

### [Json](/flux/v0/tags/json/)

### [Kafka](/flux/v0/tags/kafka/)

### [Location](/flux/v0/tags/location/)

### [Metadata](/flux/v0/tags/metadata/)

### [Mqtt](/flux/v0/tags/mqtt/)

### [Notification Endpoints](/flux/v0/tags/notification-endpoints/)

### [Numeric Types](/flux/v0/tags/numeric-types/)

### [Operators](/flux/v0/tags/operators/)

### [Optimize](/flux/v0/tags/optimize/)

### [Outputs](/flux/v0/tags/outputs/)

### [Package](/flux/v0/tags/package/)

### [Prometheus](/flux/v0/tags/prometheus/)

### [Regexp Types](/flux/v0/tags/regexp-types/)

### [Sample Data](/flux/v0/tags/sample-data/)

### [Secrets](/flux/v0/tags/secrets/)

### [Security](/flux/v0/tags/security/)

### [Selectors](/flux/v0/tags/selectors/)

### [Single Notification](/flux/v0/tags/single-notification/)

### [Sql](/flux/v0/tags/sql/)

### [Table](/flux/v0/tags/table/)

### [Tables](/flux/v0/tags/tables/)

### [Tests](/flux/v0/tags/tests/)

### [Transformations](/flux/v0/tags/transformations/)

### [Transformtions](/flux/v0/tags/transformtions/)

### [Type-Conversions](/flux/v0/tags/type-conversions/)

### [Types](/flux/v0/tags/types/)


---

## Flux standard library

The Flux standard library includes built-in functions and importable packages that retrieve, transform, process, and output data.

### [Complete list of Flux functions](/flux/v0/stdlib/all-functions/)

View the full library of documented Flux functions.

### [universe package](/flux/v0/stdlib/universe/)

The `universe` package provides options and primitive functions that are loaded into the Flux runtime by default and do not require an import statement.

### [array package](/flux/v0/stdlib/array/)

The `array` package provides functions for manipulating array and building tables from arrays.

### [bitwise package](/flux/v0/stdlib/bitwise/)

The `bitwise` package provides functions for performing bitwise operations on integers.

### [contrib package](/flux/v0/stdlib/contrib/)

The `contrib` package contains packages and functions contributed and maintained by members of the Flux and InfluxDB communities.

### [csv package](/flux/v0/stdlib/csv/)

The `csv` package provides tools for working with data in annotated CSV format.

### [date package](/flux/v0/stdlib/date/)

The `date` package provides date and time constants and functions.

### [dict package](/flux/v0/stdlib/dict/)

The `dict` package provides functions for interacting with dictionary types.

### [experimental package](/flux/v0/stdlib/experimental/)

The `experimental` package includes experimental functions and packages.

### [generate package](/flux/v0/stdlib/generate/)

The `generate` package provides functions for generating data.

### [http package](/flux/v0/stdlib/http/)

The `http` package provides functions for transferring data using the HTTP protocol.

### [influxdata package](/flux/v0/stdlib/influxdata/)

The `influxdata` package contains packages and functions that integrate with InfluxData products.

### [internal package](/flux/v0/stdlib/internal/)

The `internal` package contains packages and functions used internally by Flux.

### [interpolate package](/flux/v0/stdlib/interpolate/)

The `interpolate` package provides functions that insert rows for missing data at regular intervals and estimate values using different interpolation methods.

### [join package](/flux/v0/stdlib/join/)

The `join` package provides functions that join two table streams together.

### [json package](/flux/v0/stdlib/json/)

The `json` package provides tools for working with JSON.

### [kafka package](/flux/v0/stdlib/kafka/)

The `kafka` package provides tools for working with [Apache Kafka](https://kafka.apache.org/).

### [math package](/flux/v0/stdlib/math/)

The `math` package provides basic constants and mathematical functions.

### [pagerduty package](/flux/v0/stdlib/pagerduty/)

The `pagerduty` package provides functions for sending data to PagerDuty.

### [planner package](/flux/v0/stdlib/planner/)

The `planner` package provides an API for interacting with the Flux engine planner.

### [profiler package](/flux/v0/stdlib/profiler/)

The `profiler` package provides performance profiling tools for Flux queries and operations.

### [pushbullet package](/flux/v0/stdlib/pushbullet/)

The `pushbullet` package provides functions for sending data to Pushbullet.

### [regexp package](/flux/v0/stdlib/regexp/)

The `regexp` package provides tools for working with regular expressions.

### [runtime package](/flux/v0/stdlib/runtime/)

The `runtime` package provides information about the current Flux runtime.

### [sampledata package](/flux/v0/stdlib/sampledata/)

The `sampledata` package provides functions that return basic sample datasets.

### [slack package](/flux/v0/stdlib/slack/)

The `slack` package provides functions for sending messages to [Slack](https://slack.com/).

### [socket package](/flux/v0/stdlib/socket/)

The `socket` package provides tools for returning data from socket connections.

### [sql package](/flux/v0/stdlib/sql/)

The `sql` package provides tools for working with data in SQL databases.

### [strings package](/flux/v0/stdlib/strings/)

The `strings` package provides functions to operate on UTF-8 encoded strings.

### [system package](/flux/v0/stdlib/system/)

The `system` package provides functions for reading values from the system.

### [testing package](/flux/v0/stdlib/testing/)

The `testing` package provides functions for testing Flux operations.

### [timezone package](/flux/v0/stdlib/timezone/)

The `timezone` package defines functions for setting timezones on the location option in package universe.

### [types package](/flux/v0/stdlib/types/)

The `types` package provides functions for working with Flux’s types.

[flux](/flux/v0/tags/flux/) [functions](/flux/v0/tags/functions/) [package](/flux/v0/tags/package/)


---

## Flux language specification

The following documents specify the Flux language and query execution.

### [Notation](/flux/v0/spec/notation/)

Notation principles for the Flux functional data scripting language.

### [Representation](/flux/v0/spec/representation/)

Source code is encoded in UTF-8. The text need not be canonicalized.

### [Lexical elements](/flux/v0/spec/lexical-elements/)

Descriptions of Flux comments, tokens, identifiers, keywords, and other lexical elements.

### [Variables](/flux/v0/spec/variables/)

Flux variables hold values. A variable can only hold values defined by its type.

### [Options](/flux/v0/spec/options/)

A Flux option represents a storage location for any value of a specified type. Options are mutable. An option can hold different values during its lifetime.

### [Types](/flux/v0/spec/types/)

A type defines the set of values and operations on those values. Types are never explicitly declared as part of the syntax. Types are always inferred from the usage of the value.

### [Blocks](/flux/v0/spec/blocks/)

A block is a possibly empty sequence of statements within matching braces ({}).

### [Assignment and scope](/flux/v0/spec/assignment-scope/)

An assignment binds an identifier to a variable, option, or function. Every identifier in a program must be assigned.

### [Expressions](/flux/v0/spec/expressions/)

An expression specifies the computation of a value by applying the operators and functions to operands.

### [Operators](/flux/v0/spec/operators/)

Flux supports many types of operators including arithmetic operators, comparison operators, function operators, and others.

### [Packages](/flux/v0/spec/packages/)

Flux source is organized into packages. A package consists of one or more source files. Each source file is parsed individually and composed into a single package.

### [Attributes](/flux/v0/spec/attributes/)

Attributes define a set of properties on source code elements.

### [Statements](/flux/v0/spec/statements/)

Statements control execution in the Flux functional data scripting language.

### [Side effects](/flux/v0/spec/side-effects/)

A summary of side effects in the Flux functional data scripting language.

### [System built-ins](/flux/v0/spec/system-built-ins/)

When a built-in value is not expressible in Flux, its value may be defined by the hosting environment. All such values must have a corresponding builtin statement to declare the existence and type of the built-in value.

### [Data model](/flux/v0/spec/data-model/)

Flux employs a basic data model built from basic data types. The data model consists of tables, records, columns and streams.

[Notation](/flux/v0/spec/notation/)

[flux](/flux/v0/tags/flux/)


---

## Flux release notes

## v0.195.1

-   *Internal code cleanup.*

## v0.195.0

### Features

-   Return to internal string references.
-   Allocate memory for string content.

### Bug fixes

-   Join paths correctly in the `influxdb` source.
-   Optimize string arrays.

### Dependency updates

-   Update `github.com/benbjohnson/immutable`.
-   Update `github.com/SAP/go-hdb`.
-   Build on Rust 1.78.

## v0.194.5

### Bug fixes

-   Resolve build error on Rust 1.72.0+.

## v0.194.4

-   *Internal code cleanup.*

## v0.194.3

-   *Internal code cleanup.*

## v0.194.3

### Bug fixes

-   Make [`histogramQuantile()`](/flux/v0/stdlib/universe/histogramquantile/) correctly handle cases of zero samples.

## v0.194.1

### Bug fixes

-   Make C foreign function interface (FFI) more robust when checking for valid input.

## v0.194.0

### Features

-   Add microsecond and nanosecond support to [`iox.sqlInterval()`](/flux/v0/stdlib/experimental/iox/sqlinterval/).

### Bug fixes

-   Fix panic caused by chunking outer joins.
-   Remove 64bit reference counter misalignments.

## v0.193.0

### Features

-   Add `onNonmonotonic` parameter to [`histogramQuantile()`](/flux/v0/stdlib/universe/histogramquantile/) to define behavior when bin counts are not monotonically increasing.
-   Add the following functions to the `contrib/qxip/hash` package:
    -   [`hash.sha1()`](/flux/v0/stdlib/contrib/qxip/hash/sha1/)
    -   [`hash.md5()`](/flux/v0/stdlib/contrib/qxip/hash/md5/)
    -   [`hash.b64()`](/flux/v0/stdlib/contrib/qxip/hash/b64/)
    -   [`hash.hmac()`](/flux/v0/stdlib/contrib/qxip/hash/hmac/)

### Bug fixes

-   Convert platform-dependent path separators to slashes.
-   `use-after-free` in optimized String array.

## v0.192.0

### Breaking changes

-   Update iox.sql to detect midstream errors.

### Features

-   Add [`geo.totalDistance()`](/flux/v0/stdlib/experimental/geo/totaldistance/) to aggregate total distance of consecutive points.
-   Add [`iox.sqlInterval()`](/flux/v0/stdlib/experimental/iox/sqlinterval/) to convert Flux durations to SQL interval strings.
-   Add the [`contrib/qxip/hash`](/flux/v0/stdlib/contrib/qxip/hash/) package which includes hashing functions.
-   Add the [`contrib/qxip/logql`](/flux/v0/stdlib/contrib/qxip/logql/) package which provides functions for working with [Grafana Loki](https://grafana.com/oss/loki/) and [LogQL](https://grafana.com/docs/loki/latest/logql/).
-   Add [`contrib/qxip/clickhouse`](/flux/v0/stdlib/contrib/qxip/clickhouse/) package which provides functions for querying data from [Clickhouse](https://clickhouse.com/).

## v0.191.0

### Features

-   Associate registry attributes to import statements.

## v0.190.0

### Features

-   Add download headers within the CSV dialect.

## v0.189.0

### Features

-   Add `PartialOrd` and `Ord` to `ast::Position`.
-   Detect undesirable patterns so we can remove them later.

### Bug fixes

-   Update attribute syntax to require following element.
-   Add `salsaDatabase` to list of feature passed to Rust.
-   `testing.ShouldError` should error when no error occurs.
-   Restore termination defaults for `holtWinters` to improve performance.
-   Use salsa db when generating documentation.

## v0.188.1

### Bug fixes

-   Correctly handle join operations with large input that exceed the buffer size.

## v0.188.0

### Features

-   Compile the standard library incrementally.
-   Add attribute parsing to the parser.

### Bug fixes

-   Allow functions receiving dynamic arguments to do member expressions.

## v0.187.0

### Features

-   Add [`types.isNumeric()`](/flux/v0/stdlib/types/isnumeric/) to test for numeric values.
-   Recommend valid arguments in extra argument errors.
-   Add dynamic type support to standard type conversion functions.

### Bug fixes

-   When using `experimental.unpivot()`, don’t add the `_field` column to the group key by default.
-   Fix compilation error when using Rust 1.64.

## v0.186.0

### Features

-   Add [`dynamic.isType()` function](/flux/v0/stdlib/experimental/dynamic/istype/).
-   Add [`dynamic.asArray()` function](/flux/v0/stdlib/experimental/dynamic/asarray/).
-   Add JSON functions that work with dynamic values:
    -   [`dynamic.jsonParse()`](/flux/v0/stdlib/experimental/dynamic/jsonparse/)
    -   [`dynamic.jsonEncode()`](/flux/v0/stdlib/experimental/dynamic/jsonencode/)
-   Add runtime support for member expressions and remove index support for dynamic values.
-   Add [`iox.sql()` function](/flux/v0/stdlib/experimental/iox/sql/).

### Bug fixes

-   Update the `toUInt()` test to use the correct conversion behavior.
-   Prevent the Flux formatter from losing precision on float values.

## v0.185.0

### Features

-   Add dynamic type.
-   Add dynamic wrapper function.
-   Enable codespan formatting for errors via feature flags.

### Bug fixes

-   Pass context in the `Run` source helper.
-   Handle null vector inputs for `_vecFloat`.
-   Remove broken `contrib` packages:
    -   contrib/jsternberg/aggregate
    -   contrib/jsternberg/math

## v0.184.2

### Bug fixes

-   Remove the `stacker` dependency.
-   Skip strict *null* logical evaluator.

## v0.184.1

-   *Internal code cleanup.*

## v0.184.0

### Breaking changes

-   Update logical *null* handling and align all logical operator implementations (vectorized, row-based, as well as “in the interpreter”) to be consistent and representative of the Flux SPEC.

### Features

-   Add array type conversion functions to the [experimental `array` package](/flux/v0/stdlib/experimental/array/).

### Bug fixes

-   Update SPEC and fix some inconsistencies.
-   Update `sort limit` to skips chunks with no rows.
-   Don’t report an error about testcases in the LSP.
-   Prevent the metadata map from being concurrently mutated.
-   Don’t stackoverflow on deeply nested expressions.

## v0.183.0

### Features

-   Add support for piped-forward arrays to [`array.from()`](/flux/v0/stdlib/array/from/).
-   Add parameter to [`experimental.unpivot()`](/flux/v0/stdlib/experimental/unpivot/) for non-field and non-group-key columns.
-   Add a syntax for describing label literals.
-   Don’t display nulls as 0 in the output of `experimental.diff()`.

### Bug fixes

-   Fix duplicate definitions and update issue links in the Flux SPEC.
-   Don’t include opening parentheses in invalid call expressions.
-   Improve error message when joining with an empty table.

## v0.182.0

### Features

-   Display yields in `fluxtest`.
-   Allow [`experimental.unpivot()`](/flux/v0/stdlib/experimental/unpivot/) to work when the `_time` column is missing.
-   Add utility to the `function` package to register a source or transformation.
-   Add Rust binary to sit on top of “headless” REPL backend.

### Bug fixes

-   Correct type for `fillValueTime`.
-   Correct panic in vectorized division by zero.
-   Correct inconsistent runtime typing for `logicalVectorEvaluator`.
-   Don’t treat errors in SQL syntax as internal.
-   Improve error handling when missing a property on member expressions.
-   Preserve values of non-string group keys in `experimental.diff()`.

## v0.181.0

### Features

-   Add “headless” JSON-RPC based REPL.
-   Support vectorized unary operators.
-   Add [`experimental/polyline` package](/flux/v0/stdlib/experimental/polyline) for downsampling data.
-   Update function library to have its own arguments struct.

### Bug fixes

-   Update import path for the `Spec` package in the “headless” REPL.
-   Update conditional vectorization to handle bad values for `test`, `consequent`, or `alternate`.

## v0.180.1

-   *Internal code cleanup.*

## v0.180.0

### Features

-   Rewrite calls to `float()` as `_vectorizedFloat()`.
-   Reduce the Flux formatter default line length to 100 characters.

### Bug fixes

-   Fix logic bug in planner helper method.
-   Don’t include null columns when unpivoting.
-   Don’t error when formatting boolean literals.
-   Sort columns when printing group keys.

## v0.179.0

### Features

-   Add a `Stringify` utility function for `table.Chunk`.
-   Add support for vectorized binary equality operations.
-   Update `testing.diff()` to use `experimental.diff()` permanently.
-   Add vectorized `float()` builtin function.
-   Enhance `fluxtest` to use package name with `test` and `skip` flags.
-   Allow any kind of AST fragment to be formatted.
-   Accept Flux feature flags to the test command.

### Bug fixes

-   Update `testing.shouldError()` to use regular expression matching instead of string matching.
-   Temporarily remove duplicates test to avoid conflicts downstream.
-   Update `buildinfo` documnentation comments to match latest `go fmt`.
-   Fix aggregate window rules that left query plans in a bad state.
-   Include filename when printing the AST location.

## v0.178.0

### Features

-   Support `apiKey` parameter in [`zenoss.event()`](/flux/v0/stdlib/contrib/bonitoo-io/zenoss/event/) and [`zenoss.endpoint()`](/flux/v0/stdlib/contrib/bonitoo-io/zenoss/endpoint/).
-   Remove `vectorizedConst` feature flag.

### Bug fixes

-   Deprecate `date/boundaries` package in favor of [`experimental/date/boundaries`](/flux/v0/stdlib/experimental/date/boundaries/).
-   Update pattern matching to specify successor counts.
-   Restore integer return value for [`pagerduty.sendEvent()`](/flux/v0/stdlib/pagerduty/sendevent/).

## v0.177.1

### Bug fixes

-   Update `strings.substring()` to check bounds using rune array instead of string length.

## v0.177.0

### Features

-   Support conditional expressions in vectorized `map()`.
-   Compute minimum required dispatcher concurrency from the plan graph.
-   Add a query planner rule to remove redundant sort nodes.

### Bug fixes

-   Guard message processing with mutexes.
-   Update Flux REPL to use unique planner node IDs.

## v0.176.0

### Features

-   Promote various feature-flagged features and optimizations to be used by default.

### Bug fixes

-   Support the [`location` option](/flux/v0/stdlib/internal/location/#options) in the [`boundaries` package](/flux/v0/stdlib/date/boundaries/).
-   Pass epsilon value from Go tests to the Flux test framework.
-   Ignore unknown messages rather than erroring.

## v0.175.0

### Features

-   Update [`testing.diff()`](/flux/v0/stdlib/testing/diff/) to use [`experimental.diff()`](/flux/v0/stdlib/experimental/diff/) as its base.
-   Add a new diff implementation to the [experimental package](/flux/v0/stdlib/experimental/).
-   Generalize attributes in the query planner.
-   Add support for constants and literals in vectorized `map()`.
-   Optimize the Holt Winters implementation by using the [gonum Nelder-Mead optimization](https://github.com/gonum/gonum/blob/master/optimize/neldermead.go).

### Bug fixes

-   When joining data, provide a default schema for unmatched group keys.
-   Update the join package to be resilient to schema changes.

## v0.174.1

### Bug fixes

-   Update [`aggregateWindow()`](/flux/v0/stdlib/universe/aggregatewindow/) to correctly handle null values when using `sum` or `mean`.
-   Update [`to()`](/flux/v0/stdlib/influxdata/influxdb/to/) and [`wideTo()`](/flux/v0/stdlib/influxdata/influxdb/wideto/) to skip empty tag values.

## v0.174.0

### Features

-   Add coloring highlights to test outputs.
-   Promote [`experimental.to()`](/flux/v0/stdlib/experimental/to/) to [`influxdata.influxdb.wideTo()`](/flux/v0/stdlib/influxdata/influxdb/wideto/).
-   Allow physical plan [`attributes`](https://github.com/influxdata/flux/blob/master/plan/attributes.go) to contribute to [`formatter`](https://github.com/influxdata/flux/blob/master/plan/format.go) details.
-   Add tagging support to Flux tests.
-   Add new function [`experimental.catch()`](/flux/v0/stdlib/experimental/catch/).
-   Add new function [`testing.shouldError()`](/flux/v0/stdlib/testing/shoulderror/).

### Bug fixes

-   Update `httpWriter` struct to skip invalid floats.
-   Update [`join()`](/flux/v0/stdlib/join/) to validate group keys.
-   Fix unit tests for [`covariance()`](/flux/v0/stdlib/universe/covariance/).
-   Update all Flux packages to additionally live as Go packages.

## v0.173.0

### Breaking changes

-   Format scripts with a trailing newline by default when running the formatter.

### Features

-   Deprecate [`experimental.http.get`](/flux/v0/stdlib/experimental/http/get/).
-   Deprecate [`experimental.csv.from()`](/flux/v0/stdlib/experimental/csv/from/).
-   Promote the following functions from `experimental.array` into the [`array`](/flux/v0/stdlib/array) package:
    -   [`array.concat()`](/flux/v0/stdlib/array/concat/)
    -   [`array.filter()`](/flux/v0/stdlib/array/filter/)
    -   [`array.map()`](/flux/v0/stdlib/array/map/)
-   Promote the following functions from `experimental.http.requests` into the [`http.requests`](/flux/v0/stdlib/http/requests/) package:
    -   [`http.requests.do()`](/flux/v0/stdlib/http/requests/do/)
    -   [`http.requests.get()`](/flux/v0/stdlib/http/requests/get/)
    -   [`http.requests.peek()`](/flux/v0/stdlib/http/requests/peek/)
    -   [`http.requests.post()`](/flux/v0/stdlib/http/requests/post/)
-   Promote `experimental.bitwise` into the [`bitwise`](/flux/v0/stdlib/bitwise/) package.
-   Remove all `Test` statements. New statements are written with `TestCase`.
-   Format scripts with a trailing newline by default when running the formatter.

### Bug fixes

-   Return an error if the user modifies group key while using [`join`](/flux/v0/stdlib/join/)

## v0.172.0

### Features

-   Add multiple new join functions to the [`join`](/flux/v0/stdlib/join/) package such as [`join.full()`](/flux/v0/stdlib/join/full/).
-   Add [`initialZero`](/flux/v0/stdlib/universe/derivative/#initialzero) parameter to the derivative function.
-   Allow features to enable builtin statements.
-   Provide the comments for each `Symbol` from `PackageExports`.
-   Suggestions now start off by default and added a new flag.
-   Add builtin function [`time`](/flux/v0/stdlib/date/time/) to the `date` package to convert any timeable into datetime.
-   Allow vector types to be specified in Flux source.

### Bug fixes

-   Replace extra boolean parameter for suggestions with Flux REPL options.
-   Remove [`testing.load()`](/flux/v0/stdlib/testing/load/) from [`testutil.yield()`](/flux/v0/stdlib/internal/testutil/yield/).
-   Fix a bug in how sort nodes are created for a new join.
-   Removed extra indentation for test cases.
-   Retain the package for identifier referencing the prelude.
-   Only return an error in tests if an assertion fails.
-   Fix [`findColumn()`](/flux/v0/stdlib/universe/findcolumn/) to handle multi-buffer tables.
-   Point to the function being piped to on argument mismatches.
-   Visit successors before continuing DFS on node.

## v0.171.0

### Breaking changes

-   Remove `testing.loadStorage()`.

### Features

-   Add `FromStr` to allow the Flux LSP (language server protocol) CLI to run with optional Flux features.
-   Add method to parallelize aggregate transformations.
-   Report unused symbols.
-   Add `From` implementations for `Node/NodeMut`.

### Bug fixes

-   Pass a seed to the tables generator.
-   Ensure buffers are retained when copying a buffered table.
-   Return an error when using a label variable without the Label constraint.

## v0.170.1

### Bug fixes

-   Require an earlier minimum version of `lsp-types`.

## v0.170.0

### Features

-   Add a `pretty.rs`\-based MonoType formatter.

### Bug fixes

-   Update vectorized `map()` to properly handle shadowed columns.

## v0.169.0

### Features

-   Add a `_status` tag to PagerDuty records.
-   Refactor the operator profile to be in the query statistics.

### Bug fixes

-   Ensure that constraints are checked and propagated fully.
-   Fix math for integral with a single value.
-   Add `json` tags for the transport profiles in statistics.
-   Initialize `Metadata` in Flux statistics.
-   Return a more helpful error message when an HTTP response body exceeds 100MB.
-   Correct several issues found during the implementation of polymorphic labels.

## v0.168.0

### Features

-   Enable [`movingAverage()`](/flux/v0/stdlib/universe/movingaverage/) and [`cumulativeSum()`](/flux/v0/stdlib/universe/cumulativesum/) optimizations by default.
-   Vectorize logical operations in [`map()`](/flux/v0/stdlib/universe/map/).
-   Add a planner rule that expands logical join nodes.
-   Added timezone support to [`hourSelection()`](/flux/v0/stdlib/universe/hourselection/).

### Bug fixes

-   Attach type when constructing logical expressions.
-   Fix panic with half-diamond logical plan.

## v0.167.0

### Features

-   Allow default types to be specified for default arguments.
-   Add [`date.scale()`](/flux/v0/stdlib/date/scale/) to allow for dynamic duration changes.
-   Expose aggregate window spec fields for use by the query planner.
-   Add [`experimental.preview()`](/flux/v0/stdlib/experimental/preview/).

### Bug fixes

-   Update `date.add()` and `date.sub()` to work correctly with timezones enabled.
-   Fix failing continuous integration tests.
-   Update `hourSelection()` to support overnight time ranges.
-   Fix logic error in aggregate window planner rule preserve the rule if `table.fill` is present.
-   Use `MultiplicativeOperator` in `MultiplicativeExpression`.

## v0.166.0

### Features

-   Add InfluxData semantic commit and pull request title validator.
-   Add an `Expr` node to the visitor API.
-   Add label polymorphism.
-   Vectorize remaining arithmetic operators.

### Bug fixes

-   Remove `JoinOpSpec.TableNames` in favor of `JoinOpSpec.params` to stay consistent inside `tableFind()`.
-   Fix `SortLimit` for empty input group.

## v0.165.0

### Features

-   Add support for options in the `testcase` extension.
-   Vectorize addition operations in `map()`.
-   Add location support to `date.truncate()`.
-   Accept string literals in properties of a record type.
-   Add trace option to the `flux` CLI.
-   Add `EquiJoinPredicateRule`.

### Bug fixes

-   Update `map()` test case to include a range.
-   Don’t set `BaseLocation.file` to `Some("")`.
-   Fix `strings.joinStr` panic when it receives a null value.
-   Remove 64bit misalignment.
-   Fix memory releases and add checked allocator to the end of tests.

## v0.164.1

### Bug fixes

-   Remove an extraneous `go generate` statement.

## v0.164.0

### Features

-   Allow Go to pass compilation options to Rust.

### Bug fixes

-   Do not assume integers are 64bit integers.
-   Update `prometheus.scrape` type signature to correctly return a stream.

## v0.163.0

### Features

-   Report skipped tests.

### Bug fixes

-   Update transformation transport adapter to always invoke `finish`.
-   Add support for “soft paragraphs” (paragraphs that contain single newline characters) in inline Flux documentation.

## v0.162.0

### Features

-   Add [OpenTracing spans](https://opentracing.io/docs/overview/spans/) to the Flux runtime.
-   Add the `cffi` feature to reduce WASM binary size.
-   Replace the main `flux` CLI with a new `flux` CLI that starts a Flux REPL by default or executes a Flux script via stdin.
-   Track freed memory with `SetFinalizer`.
-   Move [`addDuration()`](/flux/v0/stdlib/date/add/) and [`subDuration()`](/flux/v0/stdlib/date/sub/) from the `experimental` package to the `date` package.

### Bug fixes

-   Improve error messages for column conflicts in pivot operations.
-   Create OpenTracing spans for transformations using the proper context.
-   Add errors to OpenTracing spans created for transformations.
-   Restore required features hidden behind the `cffi` feature.

## v0.161.0

### Features

-   Re-enable the dialer pool and update dependency injection.

### Bug fixes

-   Check length boundary for lower bound of [`strings.substring()`](/flux/v0/stdlib/strings/substring/).

## v0.160.0

### Features

-   Remove the `concurrencyLimit` feature flag and keep it in the dependencies.
-   Add MQTT Docker integration test.
-   Enable dialer pool.
-   Add an IOx-specific unpivot function to the `internal` package.

### Bug fixes

-   Update [`join()`](/flux/v0/stdlib/universe/join/) to properly handle divergent schemas.
-   Fix line endings in the `testcase` format to prevent unnecessarily nesting the body of a test case.
-   Make [`strings.substring()`](/flux/v0/stdlib/strings/substring/) check bounds correctly.
-   Fix duration and integer literal scanning.
-   Make `testcase` a semantic check instead of an error.
-   Skip parallel merge when selecting the result name based on side effects.
-   Add metadata headers to inline documentation.

## v0.159.0

### Features

-   Added a `finish` state to parallel-merge and always protect with a mutex lock.

### Bug fixes

-   Use a fork of the `gosnowflake` library to prevent file transfers.
-   When encoding Flux types as JSON, encode dictionary types as JSON objects.
-   Upgrade Apache Arrow to v7.

## v0.158.0

### Features

-   Add inline documentation to the `universe` package.
-   Factor parallel execution into the concurrency quota calculation.

### Bug fixes

-   Add parallel merges with no successors to the results set.
-   Correctly use range in an updated `map()` test.

## v0.157.0

### Features

-   Update `fill()` to use narrow transformation.
-   Add an attribute-based instantiation of parallel execution nodes.
-   Expose the `Record::fields` iterator.
-   Allow the `estimate_tdigest` method in `quantile()` to process any numeric value.
-   Optimize `aggregateWindow()` for specific aggregate transformations.

### Bug fixes

-   Update vectorized `map()` to handle missing columns.
-   Remove duplicate line in `Makefile`.
-   Fix `cargo doc` build errors.
-   Reclassify CSV-decoding errors as user errors.
-   Update `iox.from()` and `generate.from()` to use proper stream annotation.

## v0.156.0

### Features

-   Add second pass to physical planner for parallelization rules.
-   Separate streams from arrays in the type system.
-   Add function to internal/debug to check feature flag values.
-   Allow feature flags to record metrics if configured.
-   Add extra verbose level to dump AST of test.
-   Explain what `[A], [A:B]` etc means in errors.

### Bug fixes

-   Make `buckets()` function return a stream.
-   Remove unnecessary `TableObject` guards.
-   Copy `TagColumns` in `to()` that may get modified into the transformation.
-   Update tests to use explicit yields.

## v0.155.1

### Bug fixes

-   Update tests to use an explicit yield.

## v0.155.0

### Features

-   Add new [experimental array functions](/flux/v0/stdlib/experimental/array/) for operating on arrays.

### Bug fixes

-   Add `stop` parameter to [InfluxDB schema functions](/flux/v0/stdlib/influxdata/influxdb/schema/).
-   Remove `os.Exit` calls and allow `defer executor.Close` to run.
-   Properly handle time zone transitions when there is no daylight savings time in the specified time zone.

## v0.154.0

### Features

-   Add [`requests.peek()`](/flux/v0/stdlib/experimental/http/requests/peek/) to return HTTP response data in a table.
-   Add [`display()`](/flux/v0/stdlib/universe/display/) to represent any value as a string.
-   Create a version of `map()` that is columnar and supports vectorization.
-   Support vectorized functions.

### Bug fixes

-   Add time vector to the `values` package.
-   Set the correct type for vectorized functions.

## v0.153.0

### Features

-   Connect language server protocol (LSP) features through the Flux crate.
-   Add conversion from `flux.Bounds` to `plan/execute.Bounds`.
-   Re-index all bound variables to start from 0.

### Bug fixes

-   Int feature flags work properly when returned as floats.

## v0.152.0

### Features

-   Add the [`experimental/http/requests` package](/flux/v0/stdlib/experimental/http/requests/) to support generic HTTP requests.
-   Add [`experimental/iox` package](/flux/v0/stdlib/experimental/iox/) and a placeholder for the `iox.from()` function.
-   Add dependency hooks to the dependency subsystem.
-   Remove unneeded feature flags.

### Bug fixes

-   Revert update to the dependencies package.
-   Return false if contains gets invalid value.

## v0.151.1

### Features

-   Update to Rust 1.58.1.

## v0.151.0

### Features

-   Expose `MonoType::parameter` and `MonoType::field`.

### Bug fixes

-   Support writing unsigned integers with the `http` provider.

## v0.150.1

### Bug fixes

-   Remove duplicate `die` builtin in the `universe` package.

## v0.150.0

### Features

-   Update inline documentation in the following packages:
    -   date
    -   experimental
    -   testing
    -   timezone
    -   types

### Bug fixes

-   Make iterating the hashmap deterministic.
-   Quote SQL identifiers to mitigate the risk of SQL injection.

## v0.149.0

### Features

-   Add `Get` methods to `metadata`.
-   Optimized `sort |> limit` operations.
-   Add [`location` option](/flux/v0/stdlib/universe/#location) support to the `date` package.
-   Use reference equality for `Symbol`.
-   Add inline documentation to the following packages:
    -   socket
    -   sql
    -   strings

### Bug fixes

-   Do not attempt IP validation for BigQuery data source names (DSNs).

## v0.148.0

### Features

-   Report multiple errors from a single `unify` call.
-   Update [`to`](/flux/v0/stdlib/influxdata/influxdb/to/) transformation to use narrow transformation.
-   Provide specific error information on function calls.
-   Allow errors to be formatted via `codespan`.
-   Add an `internal/debug.opaque` function.
-   Provide which package exported a symbol.
-   Add timeable support to [`experimental.addDuration()`](/flux/v0/stdlib/experimental/addduration/) and [`experimental.subDuration()`](/flux/v0/stdlib/experimental/subduration/).
-   Add inline documentation to the following packages:
    -   interpolate
    -   json
    -   kafka
    -   math
    -   regexp
    -   runtime
    -   sampledata
    -   slack
    -   system
    -   pagerduty
    -   profiler
    -   pushbullet

### Bug fixes

-   Classify IP validation failures as `Invalid`.
-   Relocate the mutex in the optimized union to avoid a data race.
-   Split the entire pipe chain into multiple lines (if necessary).

## v0.147.0

### Features

-   Optimize [`union()` transformation](/flux/v0/stdlib/universe/union/).
-   Optimize [`timeShift()` transformation](/flux/v0/stdlib/universe/timeshift/).
-   Add inline documentation to the following packages:
    -   experimental/prometheus
    -   experimental/query
    -   experimental/record
    -   experimental/table
    -   experimental/usage

### Bug fixes

-   Add mutex to the optimized `union` transformation.
-   Ensure arrays are not table streams before calling `Len()`.
-   Disable flakey `geo.filterRows` tests.

## v0.146.0

### Features

-   Update `pkg-config` to support `aarch64-apple-darwin`.
-   Add inline documentation to the following packages:
    -   experimental/geo
    -   experimental/http
    -   experimental/influxdb
    -   experimental/json
    -   experimental/mqtt
    -   experimental/oee

### Bug fixes

-   Update the default `epsilon` parameter for `testing.diff` to `0.000001`.
-   Fix unsigned integer conversion tests to correctly use an defined conversion.

## v0.145.0

### Features

-   Add inline documentation to the following packages:
    -   experimental/aggregate
    -   experimental/array
    -   experimental/bigtable
    -   experimental/bitwise
    -   experimental/csv

### Bug fixes

-   Return an error from join operations if a column is not found in the schema.

## v0.144.0

### Features

-   Add location and message methods to `semantic::Error`.
-   Return multiple errors from conversions.
-   Add a vectorized field to semantic graph, `FunctionExpr`.

### Bug fixes

-   Set `GOPATH` in `Dockerfile_build`.

## v0.143.1

### Bug fixes

-   Add targets to `rust-toolchain`.

## v0.143.0

### Breaking changes

-   Add new parameters to [`difference()`](/flux/v0/stdlib/universe/difference/) to ensure [`increase()`](/flux/v0/stdlib/universe/increase/) returns more accurate results on counter reset.

### Features

-   Don’t introduce constraints for default arguments.
-   Make error messages more consistent.
-   Use new versions of `sort()` and `derivative()` by default.
-   Add inline documentation to the following packages:
    -   contrib/anaisdg/anomalydetection
    -   contrib/anaisdg/statsmodels
    -   contrib/bonitoo-io/victorops
    -   contrib/bonitoo-io/zenoss
    -   contrib/jsternberg/influxdb
    -   contrib/rhajek/bigpanda
    -   contrib/sranka/telegram
    -   experimental

### Bug fixes

-   Validate examples in inline documentation as part of CI linting process.
-   Correctly handle trailing dollar signs in string expression.
-   Improve `fluxdoc` error messages.
-   Fix panic when `length()` is given a stream of tables.
-   Fix panic when `json.encode()` is given a stream of tables.

## v0.142.0

### Features

-   Default to erroring dependencies

### Bug fixes

-   Fix Queryd panic when using the `experimental/geo` package.

## v0.141.0

### Features

-   Add `is_type` to query the runtime type.
-   Add ability to read options from the `Context`.
-   Ignore documentation for values prefixed with an underscore (`_`).
-   Add inline documentation to the following packages:
    -   contrib/RohanSreerama5/naiveBayesClassifier
    -   contrib/bonitoo-io/alerta
    -   contrib/bonitoo-io/hex
    -   contrib/bonitoo-io/servicenow
    -   contrib/bonitoo-io/tickscript
    -   contrib/chobbs/discord
    -   contrib/jsternberg/rows/
    -   contrib/sranka/opsgenie
    -   contrib/sranka/sensu/
    -   contrib/sranka/teams
    -   contrib/sranka/webexteams
    -   contrib/tomhollingworth/events
    -   generate
    -   http
    -   influxdata/influxdb
    -   influxdata/influxdb/monitor
    -   influxdata/influxdb/sample
    -   influxdata/influxdb/schema
    -   influxdata/influxdb/secrets
    -   influxdata/influxdb/tasks
    -   influxdata/influxdb/v1

### Bug fixes

-   Propagate the element type through array constructors.
-   Catch unsupported input types in aggregate transformations.
-   Support pipe parameters (`<-`) in `fluxdoc`.
-   Fix documentation errors when running `cargo doc`.
-   Reduce the amount of extra parse errors.

## v0.140.0

### Features

-   Support reporting unlimited diagnostics.
-   Support type inference running on invalid ASTs.
-   Add erroring versions for each dependency.
-   Report multiple errors from type inference.
-   Add `fluxdoc` formatting documentation.
-   Add inline documentation to the following packages:
    -   array
    -   csv
    -   dict

### Bug fixes

-   Handle errors when executing inline examples.
-   Convert fixed array to slice.
-   Compare sorted join keys.
-   Make multiline-formatting consistent.
-   Fix invalid syntax formatting.
-   Improve error checking for null and invalid types.

## v0.139.0

### Features

-   Continue type inference through errors at runtime.

### Bug fixes

-   Revert `runtime.now()` and related updates.

## v0.138.0

### Features

-   Create a BigTable dependency to let Flux mimic or control BigTable API usage.
-   Report multiple type inference errors.
-   Add [bitwise operations](/flux/v0/stdlib/experimental/bitwise/).

### Bug fixes

-   Update [`fill()`](/flux/v0/stdlib/universe/fill/) to return tables unchanged when using `usePrevious` to fill a non-existent column.
-   Add `runtime.now()` to return the same time throughout a script execution.

## v0.137.0

### Features

-   Add support for [Vertica](https://www.vertica.com/) to the [`sql` package](/flux/v0/stdlib/sql/).

### Bug fixes

-   Correctly handle HTTP errors from the InfluxDB writer.

## v0.136.0

### Features

-   Enable executable examples to documentation generated by `fluxdoc`.
-   Enforces IP validation and timeouts when using `mqtt`.
-   Add an alternate `flux` CLI that starts the REPL if no argument is given.
-   Update lint formatting.
-   Add [`contrib/bonitoo-io/servicenow` package](/flux/v0/stdlib/contrib/bonitoo-io/servicenow/) and support for [ServiceNow](https://servicenow.com/) events.
-   Add `component` and `customDetails` parameters to [`pagerduty.sendEvent()`](/flux/v0/stdlib/pagerduty/sendevent/).
-   Update the `fluxdoc` parser to capture more data.
-   Create a formatter for semantic graph.

### Bug fixes

-   Add `contrib/bonitoo-io/servicenow` to the list of `fluxdoc` exceptions.
-   Disable write retries for the InfluxDB `http` provider.

## v0.135.1

### Features

-   Add a disposable interface for transformations.

### Bug fixes

-   Improve error message when regrouping is required in `map()`.

## v0.134.0

### Features

-   Add short mode to `fluxdoc dump` command.
-   Add Analyzer API to `libflux`.
-   Add [`timezone` package](/flux/v0/stdlib/timezone/) with fixed offset location.
-   Add [`record.get()` function](/flux/v0/stdlib/experimental/record/get/) to dynamically retrieve record properties.
-   Embed the compiled standard library instead of compiling at runtime.

### Bug fixes

-   Create new annotations when group key columns change.
-   Update [`prometheus.histogramQuantile()`](/flux/v0/stdlib/experimental/prometheus/histogramquantile/) to support multiple histograms and metric format versions.

## v0.133.0

### Features

-   Expose location functionality to [`window()`](/flux/v0/stdlib/universe/window/), [`aggregateWindow()`](/flux/v0/stdlib/universe/aggregatewindow/), and [`experimental.window()`](/flux/v0/stdlib/experimental/window/).
-   Add location functionality to the `interval` package.
-   Add methods to convert time values to and from local clock time.
-   Add [`mqtt.publish()` function](/flux/v0/stdlib/experimental/mqtt/publish/).
-   Add [`retain` parameter](/flux/v0/stdlib/experimental/mqtt/to/#retain) to [`mqtt.to`](/flux/v0/stdlib/experimental/mqtt/to/).

### Bug fixes

-   Add `range()` before `window()` to set query time bounds in tests.
-   Use a new `Fresher` instance for each package.

## v0.132.0

### Features

-   Copy location-related code from the Go `time` package.
-   Create a `Vector` monotype.
-   Refactor and optimize [`derivative()` transformation](/flux/v0/stdlib/universe/derivative/).
-   Add new [InfluxDB sample datasets](/flux/v0/stdlib/influxdata/influxdb/sample/data/#available-influxdb-sample-datasets) and [`sample.alignToNow()`](/flux/v0/stdlib/influxdata/influxdb/sample/aligntonow/).
-   Allow query concurrency to be set to the number of nodes in the graph.

### Bug fixes

-   Update null check with clear error message.
-   Report errors from function parameters.
-   Propagate all inferred properties to a function argument.
-   Fix `Staticcheck` linter in `executetest`.
-   Reformat non-formatted Flux files.
-   Make builds reproducible by ordering package members in the `doc` package.
-   Prevent the optimized `derivative()` from attempt to replicate a non-existent bug.
-   Update [`events.duration()`](/flux/v0/stdlib/contrib/tomhollingworth/events/duration/) to properly handle multiple buffers.

## v0.131.0

### Features

-   Update `group` to use new `GroupTransformation` interface.
-   Add [`experimental/record` package](/flux/v0/stdlib/experimental/record/).
-   Embed compiled Flux standard library instead of compiling at runtime.
-   Add [`contrib/bonitoo-io/hex` package](/flux/v0/stdlib/contrib/bonitoo-io/hex/) to work with hexadecimal string values.

### Bug fixes

-   Disallow setting [`allowAllFiles` parameter](https://github.com/go-sql-driver/mysql#allowallfiles) in [MySQL DSNs](/flux/v0/query-data/sql/mysql/#mysql-data-source-name).
-   Downgrade [Snowflake](/flux/v0/query-data/sql/snowflake/) version.
-   Add *null* support to optimized `repeat` function.

## v0.130.0

### Features

-   Add narrow state transformation transport.

## v0.129.0

### Features

-   Make `flux-dump-docs` use a nested documentation structure.

### Bug fixes

-   Add `boolean` package to prelude.
-   Delete obsolete Go formatter code.
-   Fix `unknown type` panic when using `difference()`.

## v0.128.0

### Features

-   Add [`sampledata` package](/flux/v0/stdlib/sampledata/) with basic sample datasets.
-   Add `GroupTransformation` transport.

## v0.127.3

### Bug fixes

-   Add `FormatDuration` method that can be exported in other repositories.

## v0.127.2

### Bug fixes

-   Remove `flux wasm` crate and moved it to `lsp`.
-   Delete obsolete packages.
-   Add `_time` to status sorting.
-   Fix panic with `unknown type invalid` in `reduce()` function.

## v0.127.1

### Bug fixes

-   `limit()` correctly resets the offset after processing a partial buffer.

## v0.127.0

### Features

-   Create an executable to retrieve all `stdlib` documentation and updated WASM functions.
-   Implement `transport` in aggregate transformations.
-   Add documentation site links and fix `flux_types` issue.

### Bug fixes

-   `fill()` function fails when the specified fill column doesn’t exist.
-   Add `link` parameter to function structs.

## v0.126.0

### Features

-   Update `filter()` to use narrow transformation.

### Bug fixes

-   Return JSON for WASM.
-   Check both dynamic types and static values in `strings` package.
-   Check both dynamic types and static values in `regexp` package.
-   Change `die` error code to invalid.

## v0.125.0

### Features

-   Add feature flag library as an internal package.
-   Add narrow transformation transport.
-   Add transport-aware dataset.
-   Simplify the transport interface and add a transformation adapter.
-   Add [`contrib/sranka/webexteams` package](/flux/v0/stdlib/contrib/sranka/webexteams/).
-   Add optimized repeat function for arrow arrays.
-   Add two additional internal message types.

### Bug fixes

-   Update transformation adapter to return an error when receiving a flush key for a table that is not present.
-   Fix pivot operations when no data is left to operate on.
-   Update `join()` to produce columns of equivalent length when combining mismatched schemas.

## v0.124.0

### Features

-   Update the string array builder to support constant data.
-   Expand message interface with message lifetime controls.
-   Create internal Flux array package.

### Bug fixes

-   Register `sortedPivot` and update `sortedPivot` kind.
-   Derive `Copy` on `ast::Position`.
-   Update `to()` function to properly close the writer on error.
-   Update `libflux` include paths to use `pkg-config`.
-   Properly copy record types with no `extends` parameter.

## v0.123.0

### Breaking changes

-   Remove the `sleep()` function.

### Features

-   Optimize [`pivot()` transformation](/flux/v0/stdlib/universe/pivot/).
-   Add [InfluxDB sample data package](/flux/v0/stdlib/influxdata/influxdb/sample/).
-   Use `table.fill()` when `aggregateWindow(createEmpty: true)` is used.

## v0.122.0

### Features

-   Add `--skip` flag to the `flux test` command to skip specific tests.

## v0.121.0

### Features

-   Update [`experimental.to()`](/flux/v0/stdlib/experimental/to/) to use the Flux `influxdb` provider.

## v0.120.1

-   *Add inline Flux function documentation.*

## v0.120.0

### Features

-   Bootstrap documentation methods.

### Bug fixes

-   Reverse [`math.atan2()`](/flux/v0/stdlib/math/atan2/) parameters.
-   Fix documentation headers in `stdlib`.
-   Distinct `testcase` should not use `testing.load()`.
-   `movingAverage()` creates columns with the same length when `n` is the size of the input.
-   Allow work queue to be resized when work exceeds queue length.
-   `distinct()` appends null values without creating invalid tables.

## v0.119.1

-   *Add inline Flux function documentation.*

## v0.118.1

-   *Internal code cleanup.*

## v0.118.0

### Features

-   Add `exclude` parameter to `pagerduty.dedupKey()`.

### Bug fixes

-   Ensure PagerDuty tests include a `_value` column.
-   Add length check to CSV annotation parsing.
-   Change `FunctionLiteral` precedence to preserve parentheses.

## v0.117.3

-   *Internal code cleanup.*

## v0.117.2

### Bug fixes

-   Remove `tabstop` processing from formatter.
-   Support dividing IEEE float values by zero.
-   Fix multiline collapse when formatting function parameters.
-   Reclassify `map type` error as `user` error.
-   Fix acceptance tests to catch different timestamps.

## v0.117.1

### Bug fixes

-   Update `group_no_agg_table` acceptance test to run in a consistent order.
-   Remove `xcc.sh` release dependency.
-   Fix `staticcheck` linter failures.
-   Replace erroneous line deletions.

## v0.117.0

### Features

-   [`to()`](/flux/v0/stdlib/influxdata/influxdb/to/) function writes to a remote InfluxDB instance.

### Bug fixes

-   Fix unexpected behavior caused by going over the Go/Rust boundary multiple times using JSON serialization.
-   Update `Assert_eq!` output.
-   Update `comrak` dependency.
-   Set `CARGO_HOME` after removing privileges.
-   Log uneven columns found when processing tables.
-   Audit and clean up the Docker build image.
-   Switch default InfluxDB port from `9999` to `8086`.
-   Add tests for window offset behavior.
-   Update formatting for conditional expressions.
-   Fix string interpolation for basic types.

## v0.116.0

### Features

-   Add Jaeger tracing information to profile metadata.
-   Add `flux fmt` step to the continuous integration pipeline.
-   Update the `window` implementation to use `interval.Window`.
-   Add [`today()` function](/flux/v0/stdlib/universe/today/).

### Bug fixes

-   Remove deadlock when an error occurs while the dispatcher is stopping.
-   Prevent errors caused by the the auto-formatter removing brackets around `if` expressions.
-   Auto-format remaining Flux files.

## v0.115.0

### Features

-   Add [Alerta notifications support](/flux/v0/stdlib/contrib/bonitoo-io/alerta/).
-   Add [`table.fill()` function](/flux/v0/stdlib/experimental/table/fill/) to fill empty tables with a single row.
-   Add string formatting to `dict` type.

### Bug fixes

-   Refactor semantic printing of types.
-   Do not remove escape characters when auto-formatting.
-   Add `0.0.0.0` to URL validator.
-   Add new display API for values.
-   Auto-format Flux files in `stdlib/testing`.

## v0.114.1

### Bug fixes

-   Upgrade `mssqldb` dependency for Go 1.16.
-   Format Flux files in `stdlib`.

## v0.114.0

### Features

-   Add `debug.slurp()` and `debug.sink()`.
-   Add [`experimental/influxdb`](/flux/v0/stdlib/experimental/influxdb/) and [`experimental/usage`](/flux/v0/stdlib/experimental/usage/) packages.
-   Add `fmt` subcommand to the `flux` CLI to apply formatting to Flux files.

### Bug fixes

-   Format Flux files in `stdlib` and `stdlib/testing`.
-   Update the macOS SDK for Go 1.16.
-   Revert check for uneven columns.
-   Wait for the dispatcher to finish before finishing query.
-   Remove `codecov` job.

## v0.113.0

### Features

-   Add ported table test.
-   Create `astutil` package for AST utilities such as formatting.

### Bug fixes

-   Update expected output for acceptance test `group_no_agg_table`.

## v0.112.1

### Bug fixes

-   Add `Comment` fields to Go AST structs to preserve comments in the AST.

## v0.112.0

### Features

-   Add [`testing.load`](/flux/v0/stdlib/testing/load/) for using raw tables in tests.
-   Add remaining experimental built-in types without column parameters.
-   Add [OEE (overall equipment effectiveness) package](/flux/v0/stdlib/experimental/oee/).

### Bug fixes

-   Use new crate name in `buildinfo`.
-   Add bounded time ranges to fix test cases.
-   Move `derive` helper attribute after `derive` macro.

## v0.111.0

### Features

-   Use `FnvHasher` for hash maps.
-   Add [`tickscript` package](/flux/v0/stdlib/contrib/bonitoo-io/tickscript/).

### Bug fixes

-   When finding the parent directory’s root, skip the current directory.
-   Fix `if else` statement in `aggregate.window()`.

## v0.109.1

### Bug fixes

-   Perform testing checks as part of query `done`.
-   Delimited multi-result encoder properly releases results before checking for errors.

## v0.109.0

### Features

-   Add support for null values in string interpolation.
-   Add support for all basic datatypes in string interpolation.
-   Add support for parsing CSV files without annotations.
-   Support formatting the AST from `libflux`.

### Bug fixes

-   Add error handling for wrong number of fields for raw CSV.
-   Change Rust version to be updated manually.

## v0.108.1

-   *Internal code cleanup.*

## v0.108.0

### Features

-   Add [BigPanda notification support](/flux/v0/stdlib/contrib/rhajek/bigpanda/).
-   Add [Zenoss notifications support](/flux/v0/stdlib/contrib/bonitoo-io/zenoss/).
-   Add [VictorOps notifications support](/flux/v0/stdlib/contrib/bonitoo-io/victorops/).

### Bug fixes

-   Classify “Option not found error” as internal.
-   Remove `as_user` parameter from `slack.message` payload.

## v0.107.0

### Features

-   Add new [`experimental.kaufmansAMA()` function](/flux/v0/stdlib/experimental/kaufmansama/) signature.
-   Add new [experimental aggregate function](/flux/v0/stdlib/experimental/#experimental-functions) signatures.
-   Add `extends` capability to `testcase` block to extend tests using a relative path to another file.

### Bug fixes

-   Update CSV package to handle large files.
-   Add tests and fix the `NoHeader` configuration for the `csv` decoder.
-   Remove `interval` package and documentation.
-   Disable line wrap linter.
-   Fix typo in comment.

## v0.106.0

### Features

-   Add new [experimental `integral()` function](/flux/v0/stdlib/experimental/integral/) signature.
-   Add new [experimental `window()` function](/flux/v0/stdlib/experimental/window/) signature.

# Bug fixes

-   Switch from `HashMap` to `BTreeMap` in the conversion functions from AST to semantic.
-   Track and reduce memory used by `tdigest`.
-   Detect and break infinite loops while parsing arrays.

## v0.105.0

### Features

-   Add `interval` package to `window` transformation.

## v0.104.0

### Features

-   Reintroduce `IsZero` method on time windows.

### Bug fixes

-   Break parse loop when invalid array item is found.

## v0.103.0

### Features

-   Add `testing/expect` package for test expectations.

### Bug fixes

-   Change the default test discovery path from `./stdlib` to `.`.

## v0.102.0

### Features

-   Add `fluxdoc` command to generate JSON and HTML from Flux source code.
-   Improve performance of random access group lookup by utilizing `xxhash`.
-   Improve performance for accessing data within a `Value`.

### Bug fixes

-   Clean up `interval` package.

## v0.101.0

### Features

-   Validate IP addresses from the dialer `Control` function.
-   Expose `test` command to be used by external libraries.

## v0.100.0

### Features

-   Add ability to execute tests from `.tar` and `.zip` archives.

### Bug fixes

-   Fix endpoint examples in source code.

## v0.99.0

### Features

-   Evaluate [dictionary literals](/flux/v0/spec/expressions/#dictionary-literals).
-   Infer the type of dictionary literals.
-   Parse and format dictionary literals.
-   Add a pure Flux test runner.

### Bug fixes

-   Ensure `csv.from()` only returns one result.
-   Change `extern` parsing code to return a more descriptive error message.
-   Do not allow containers within a record to be null.
-   Retrieve `now` option before running a Flux script.
-   Fix misspellings in the [Flux README](https://github.com/influxdata/flux/blob/master/README.md).

## v0.98.0

### Features

-   Transform `testcase` AST into pure flux.
-   Added Rust scanner.

### Bug fixes

-   Substring method now works on more indices.
-   Fix typos in `Dockerfile_build`.

## v0.97.0

### Features

-   Add dict package for interacting with dictionaries.
-   Added Ragel 7 to the Dockerfiles.
-   Add support for `testcase` statement.
-   Add Dictionary type syntax.
-   Add Dictionary type unification rule.

## v0.96.0

### Features

-   Create a Dictionary type interface and implementation.
-   Add Dictionary type (dict) to the semantic flatbuffers.

## v0.95.0

### Features

-   Use `tabwriter` to vertically align tab stops.

### Bug fixes

-   Format types in error messages according to Flux grammar.

## v0.94.0

### Features

-   Add “everything” Rust benchmark.

### Bug fixes

-   Add multiline support to the Flux formatter.
-   Format types using letters instead of numbers.

## v0.93.0

### Features

-   Ensure query plan nodes have unique IDs.

## v0.92.0

### Features

-   Add `fluxinit` package as an alternative to importing `builtin`.
-   Add [series `cardinality()` function](/flux/v0/stdlib/influxdata/influxdb/cardinality/) to InfluxDB package.

### Bug fixes

-   Do not panic when the value column for `pivot()` does not exist.
-   Properly truncate timestamps to beginning of window bounds.
-   Updates operator precedence in formatter.
-   Do not panic when a string expression evaluates to *null*.
-   Add support for multiline conditional logic.

## v0.91.0

### Features

-   Aggregate results for `operator` profiler.
-   Add contributed [`events` package](/flux/v0/stdlib/contrib/tomhollingworth/events/).
-   Use `tableFind` and related functions with profiler results.
-   Add duration support to [`orTime` parameter](/flux/v0/stdlib/influxdata/influxdb/tasks/lastsuccess/#ortime) of `lastSuccess()`.

### Bug fixes

-   Configure the profiler even if `operator` profiler is not enabled.
-   Update formatter to handle newline characters in `write_string`.
-   Make formatter use spaces instead of tabs.
-   Update formatter double spacing rules.
-   Add support for multiline type expressions.
-   Update `influxdata/influxdb/tasks` package with new location of `execute` dependencies.
-   Improve multiline and parentheses support in formatter.

## v0.90.0

### Features

-   Add [Sensu package](/flux/v0/stdlib/contrib/sranka/sensu).

### Bug fixes

-   Verify dependencies in `Dockerfile_build`.
-   Fix panic in `experimental.join`.

## v0.89.0

### Features

-   Add support for SAP HANA databases.
-   Add support for comments preceding `builtin` statements in code formatting.

## v0.88.0

### Features

-   Move functions from `v1` package to `schema` package.

### Bug fixes

-   Fix field type error in test.
-   Update buildinfo script to handle new and deleted files.
-   Sets default quantile method when not specified.
-   Improve security of Dockerfile for build scripts.

## v0.87.1

### Bug fixes

-   Fetch ragel dependency over HTTPS.
-   Ensure `ast.TextPart` is properly escaped when formatting.
-   Elapsed with multiple buffers per table.

## v0.87.0

### Features

-   Linear interpolation.
-   Type signature for linear interpolate function.

### Bug fixes

-   Fix compiler type inference with extended records.
-   Colm Flux grammar updates: keywords, string interpolation, and UTF-8 IDs.
-   Exponent operator have higher precedence.

## v0.86.0

### Features

-   Add operator profiler.
-   Add duration conversion.
-   Add naive bayes classification.

### Bug fixes

-   Reset pointer after scanning invalid Unicode.
-   Catch references to non-existent columns.
-   Propagate span context to `source.Run`.

## v0.85.0

### Features

-   Add `Aggregate.window` for an alternative windowing aggregate.

### Bug fixes

-   Remove months parameter.

## v0.84.0

### Breaking changes

-   Remove time-column parameters from `range()` function and update type signature.

### Features

-   Add [Opsgenie package](/flux/v0/stdlib/contrib/sranka/opsgenie/).
-   Implement [`lastSuccess()`](/flux/v0/stdlib/influxdata/influxdb/tasks/lastsuccess/) in the `tasks` package.
-   Support duration values in `aggregateWindow`.
-   Update Apache Arrow to 1.0.1.

### Bug fixes

-   Ensure meta columns are never part of group key.

## v0.83.1

### Bug fixes

-   Single value integral interpolation.

## v0.83.0

### Features

-   Improve window errors.
-   Add [BigQuery](https://cloud.google.com/bigquery) support to [`sql` package](/flux/v0/stdlib/sql/).
-   Add `TypeExpression` to `BuiltinStmt` and fix tests.
-   Add time-weighted average ([`timeWeightedAvg()` function](/flux/v0/stdlib/universe/timeweightedavg/)).
-   Update [`integral()`](/flux/v0/stdlib/universe/integral/) with linear interpolation.
-   Make experimental tracing an attribute of the context.

### Bug fixes

-   Update builtin statement for `integral()`.
-   Add Rust JSON tests.
-   CSV no longer deadlocks when next transformation does not consume table.

## v0.82.2

### Features

-   Add [`tasks.lastSuccess` function](/flux/v0/stdlib/influxdata/influxdb/tasks/lastsuccess/) to retrieve the time of the last successful run of an InfluxDB task.

## v0.82.1

-   *Internal code cleanup.*

## v0.82.0

### Features

-   Add the [`profiler` package](/flux/v0/stdlib/profiler/).
-   Add a documentation URL field to Flux errors.
-   Check InfluxDB schema compatibility.

### Bug fixes

-   Panic when a map object property contains an invalid type.

## v0.81.0

### Features

-   Delete old parser.
-   Add function to indicate duplicate option assignments.

### Bug fixes

-   Calculate distinct key values.
-   Handle pipe arguments inside of compiler.

## v0.80.0

### Features

-   Add `nulls` parameter to `gen.tables()`.

### Bug fixes

-   Revert the timeable constraint for integer.
-   Make socket/sql URL test robust.

## v0.79.0

### Features

-   Add `array.from()` function to convert Flux values into a table.

### Bug fixes

-   Add bounds to Geo package end-to-end tests.

## v0.78.0

### Breaking changes

-   Removed `correlationKey` parameter from `geo.toRows` and `geo.shapeData`.

### Features

-   Add functions to convert semantic monotype to AST type.
-   Add BigQuery support.
-   Rust flatbuffer serialization for `MonoType` and `TypeExpression`.
-   Extend with Geo package with GIS functions and [unit support](/flux/v0/stdlib/experimental/geo/#distance-units).

### Bug fixes

-   String interpolation in arrays.

## v0.77.1

### Bug fixes

-   Write tests and fix issues with `rows.map`.

## v0.77.0

### Features

-   Add a faster `map()` function *(user-contributed `/contrib/jsternberg/rows` package)*.
-   Add an [`influxdb.select()` function](/flux/v0/stdlib/contrib/jsternberg/influxdb/select/) *(user-contributed)*.
-   Flatbuffer deserialization for type expression AST nodes.
-   Flatbuffer types for monotype and type expression AST nodes.
-   Go AST nodes for type expression syntax.
-   Get all options and properties.
-   Add `parse_function` in `parser/mod.rs`.
-   Add an alternative aggregate package to user-contributed packages.

### Bug fixes

-   Fix string interpolation in arrays.

## v0.76.1

### Bug fixes

-   Fix data race in metadata.

## v0.76.0

### Features

-   Add query plan to query metadata.

## v0.75.0

### Features

-   Update `parse_record` to return `MonoType` for consistent results from functions used by `parse_monotype`.
-   Internal command utility for comparing CSV tables.
-   Update `mod.rs` with `parse_record`.
-   Add planner tests for window min and max.
-   CRUD options and properties.
-   Update `mod.rs` with `parse_constraints`.
-   Update `mod.rs` with `ArrayType` and add `Array` to the `Monotype` enumeration.

### Bug fixes

-   Statuses are always sorted by source timestamp.
-   Multiple `do` calls will fail with an empty table.

## v0.74.0

### Features

-   Add `discord.endpoint()` function.
-   Enhance the static table API.
-   Update `mod.rs` with `parse_type_expression` and other supporting functions.
-   Expose static table package and table diff functions.
-   `Find_var_type()` API.
-   Add `stringify` method for a table and a diff utility.
-   Added range to end-to-end tests.
-   Add types grammar to SPEC.

### Bug fixes

-   Normalize Monotype.

## v0.73.0

### Features

-   Add parameter for applying substitution to top-level environment.
-   Add MergeFilterRule to `universe.filter`

### Bug fixes

-   Use query strings instead of AST for remote InfluxDB queries. This lets you query remote InfluxDB instances in the Flux REPL.

## v0.72.1

### Bug fixes

-   Correctly classify “duplicate yield” error.

## v0.72.0

### Features

-   Update `from()` to use `Timeable`.

### Bug fixes

-   Fix appending an array of booleans with null values.
-   Pass the context to the planner when using the table object compiler.
-   Add `diff` output to release script on error.
-   Appending empty tables to a buffered builder normalizes the schema.
-   Remove `bad_sqlite_path1` test.
-   Classify spec build errors as user errors.
-   Verify index expression bounds in evaluation.
-   Substitute array element types correctly.

## v0.71.1

### Bug fixes

-   Add a check to ensure `every` is non-negative.

## v0.71.0

### Features

-   Apply `Timeable` constraint to integer type to support integer values in time-related function parameters.
-   Implement schema mutation functions without performing any copies.
-   Add [`http.pathEscape()` function](/flux/v0/stdlib/http/pathescape/).

## v0.70.0

### Features

-   Update all `date` functions to accept time and duration types.
-   Add [Microsoft Teams package](/flux/v0/stdlib/contrib/sranka/teams/).
-   Evaluate and store `now` in execution dependencies for `tableFind()`.
-   Add `Timeable` constraint for time and duration types.
-   Add [SQL Server support](/flux/v0/stdlib/sql/from/#query-a-sql-server-database) to `sql` package.
-   Add [Telegram package](/flux/v0/stdlib/contrib/sranka/telegram/).
-   Add [Amazon Athena support](/flux/v0/stdlib/sql/from/#query-an-amazon-athena-database) to `sql` package.
-   Add support for macOS builds.

### Bug fixes

-   Move semantic analysis to the finalize step.
-   Fix check for stream equality.
-   Fix the compiler’s return type when `with` operator is used.
-   Include `stdlib` Flux dependencies from the Flux `build.rs`.
-   Include a hash of the sources for `libflux`.
-   Flux test for [experimental `json.parse()`](/flux/v0/stdlib/experimental/json/parse/).
-   Reorder `go generate` call to `libflux` in `stdlib`.

## v0.69.2

### Bug fixes

-   Include a hash of sources for `libflux`.

## v0.69.1

### Bug fixes

-   Fix experimental `json.parse()` test.

## v0.69.0

### Features

-   Add [Discord package](/flux/v0/stdlib/contrib/chobbs/discord/) *(contributed by [@chobbs](https://github.com/chobbs))*.
-   Add [`json.parse()` function](/flux/v0/stdlib/experimental/json/parse/).

### Bug fixes

-   Adjust error handling in Flux `date` package.

## v0.68.0

This version of Flux introduces an updated type inference system that improves performance, error messaging, and usability of the [Flux Language Server Protocol (LSP)](https://github.com/influxdata/flux-lsp).

### Breaking Changes

-   Change signature of `group()` function.

### Features

-   Add [`fieldKeys()`](/flux/v0/stdlib/influxdata/influxdb/v1/fieldkeys/) and [`measurementFieldKeys()`](/flux/v0/stdlib/influxdata/influxdb/v1/measurementfieldkeys/) to v1 package.
-   Add a context to `plantest.RuleTestCase`.
-   Add Snowflake support to SQL package.
-   Add [`experimental.chain()`](/flux/v0/stdlib/experimental/chain/) function.
-   Add semantic nodes for bad statement and bad expression.
-   Add [`findColumn()`](/flux/v0/stdlib/universe/findcolumn/) and [`findRecord()`](/flux/v0/stdlib/universe/findrecord/) functions.
-   Return `false` if `contains()` is called with an empty set.
-   Various performance optimizations.
-   Add a dynamically linked Valgrind test.
-   Add location information to type error messages.
-   Add all Linux cross-compilation tools to release Docker image.
-   Support remote `buckets()` and `v1.databases()` calls.
-   Add support for static linking.
-   Add `influxdb` source.
-   Add support for `pkg-config`.
-   Transform semantic nodes back to AST nodes.
-   Handle multi-file packages.
-   Make `Eval()` and `EvalAST()` use libflux for parsing and analysis.
-   Add `lookuptype` function for stdlib builtins.

### Bug Fixes

-   Re-enable Clippy linter rule match single binding.
-   Fix bug in object equal method.
-   Add builtin formatting.
-   Implement `TimeBounds` for `influxdb.fromRemote`.
-   Inject the URL validator into `NewDefaultClient`.
-   Fix race condition in the `filter()` function.
-   Validate HTTP redirects against private IPs.
-   Hide DNS information in HTTP.
-   Fix concurrent map write in `filter()` transformation.
-   Copy all fields of `WindowProcedureSpec` in `Copy()`.
-   Run `go generate` on libflux when `go generate` is run on stdlib.
-   Fix panic when `map()` overwrites group column.
-   Support execution contexts in the REPL.
-   Apply substitution fully when compiling lambda.
-   Planner rewrite rules take a context.
-   Fix panics when functions operate on null values.
-   Fix logic for merging packages with no package clause.
-   Compute function’s return type after substitution.
-   Resolve member expressions.
-   Improve error message descriptions.
-   Check types of parts when evaluating `StringExpression`.
-   Bind appropriate interpreter when evaluating functions.
-   Tweak Rust JSON serialization and add tests.
-   Pivot sends update watermark and processing time exactly once.
-   Calculate diff’s watermark using both predecessors.
-   Add length check to avoid allocs checking for JSON `null`.
-   Make compilers robust to `null` keyword in `extern` field.
-   Address issues in `RemoveTrivialFilterRule`.
-   Bind appropriate interpreter when evaluating functions.
-   Convert `HashMap` in semantic package to `BTreeMap`.
-   Use static linking when creating the Valgrind test.
-   Update `flatbuffers` dependency.
-   Fix JSON serialization of Rust AST.
-   Remove unused environment variables.
-   Make `merge_packages` allow no package clauses.
-   Do not call `CheckKind` when evaluating logical expressions.
-   Force the Go libflux wrapper to rebuild using `go generate`.
-   Adjust `test-bench` config for Circle CI.
-   Fix Valgrind test code.
-   Let Rust parser parse with file name.
-   Remove Algorithm-W to-do list.
-   `JoinStr` returns a string, not an empty record.
-   Only add visible properties to output of `map()`.
-   Serialize the correct sign duration literal.
-   Remove code in semantic package that depends on Rust/Cgo code.
-   Remove `component` field from API.
-   Remove unused notification rule fields from Slack and PagerDuty APIs.
-   Array builders accept array types as input.
-   Enable `map()` tests with null values.
-   Remove tests for marshalling semantic graph.
-   Run `make generate` to generate stdlib.
-   Fix type error in benchmark test.
-   Update `TableObject` test.
-   Do not call `LocalRange` on nil scope.
-   Type assertion error in `length()` tests.
-   Update type inference test case with test for `union()`.
-   Make non-test CI steps pass.
-   Fix semantic check for option reassignment.
-   Type inference tests for binary comparison operators.
-   Fix typo in builtins.
-   Update `holtWinters()` to make `seasonality` optional.
-   Fix type errors in tests.
-   Remove default value from notify data.
-   Allow options to be set in scope.
-   Replace `ScopeComparer` with `ScopeTransformer`.
-   Use `LocalRange` in compile tests.
-   Add missing parameter to type of `to()`.
-   Get `TableObject` test case to compile.
-   Fix typo in test case.
-   Update `TableObjects` to type `Array`.
-   Use array type method correctly.
-   Update schema mutators.
-   Return proper types for type conversion functions.
-   Enable complete package to compile and pass tests.
-   Make stdlib compile.
-   Expect monotypes for function values.
-   Require successful lookup of stdlib builtins or panic.
-   Optimize lookup function using hashmap.
-   Include function type when deserializing function expressions.

## v0.67.0

### Features

-   Planner Pattern interface supplies a set of ProcedureKind as root.
-   Initial prototype of a table-based Flux.
-   Evaluate and store “now” in execution dependencies for `tableFind()` to use.
-   Static analysis tool for listing entry points to Flux.
-   Pass context to rewrite rules in the planner.

### Bug fixes

-   Pivot sends update watermark and processing time exactly once.
-   `system.time()` checks context for override.
-   Add bounds to alignTime tests.

## v0.66.1

### Bug fixes

-   Add bounds to `alignTime()` tests.

## v0.66.0

### Features

-   Add [`epsilon` parameter](/flux/v0/stdlib/testing/diff/#epsilon) to `testing.diff()`.
-   Add [`experimental.alignTime()` function](/flux/v0/stdlib/experimental/aligntime/).
-   Add random access group lookup.
-   Add [Pushbullet package](/flux/v0/stdlib/pushbullet/).
-   Add a helper for testing `execute.Source`.

### Bug fixes

-   Use RandomAccessGroupLookup in `testing.diff()`.
-   Address deleted state `GroupLookup`.
-   Add test case for errors when AST is bad.
-   Reduce memory usage during CI testing.

## v0.65.0

### Features

-   Add [`experimental.join()`](/flux/v0/stdlib/experimental/join/) function.
-   Store comments in the AST and preserve on format.
-   Add [`shapeData()`](/flux/v0/stdlib/experimental/geo/shapedata/) function to Geo package.
-   Expose format to Wasm users.

### Bug fixes

-   Reimplement `stateChanges()` function.
-   Remove the `set -x` in the xcc script.
-   Publishes Flux as a public npm package.
-   Pivot message passing.

## v0.64.0

### Features

-   Hand-transpile `elapsed()` aggregate.
-   Hand-transpile `cumulative_sum()`.
-   Experimental `csv` package.

### Bug fixes

-   Add response reader as dependency to tune response size.
-   Handle unfinished option statement without panic.
-   Simplify libflux C API and resolve memory leaks.
-   Don’t construct a `compiler.compilerScope` with a nil `value.Scope` as base.
-   Influxql-decode to handle the case without tag set.

## v0.63.0

### Features

-   Experimental `geo` package.
-   Initial grammar for Flux and a partial grammar for InfluxQL.

## v0.62.0

### Features

-   InfluxQL decode and series aggregation tests.

### Bug fixes

-   Properly categorize parse errors as “invalid”.
-   Fail gracefully when `tableFind` does not have an execution context.

## v0.61.0

### Features

-   Add experimental aggregate package with `rate()` function.

### Bug fixes

-   Deserialize the default vector if array elements are null.
-   Allow array and row types to be equatable.

## v0.60.0

### Features

-   Add experimental `query` package.
-   Create a Docker environment for Flux releases.
-   Validate there are no free type variables in prelude/stdlib build.
-   Add formatter library.

### Bug fixes

-   `derivative()` works properly across multiple buffers.
-   Fix free type variable found in `tripleExponentialDerivative()`.
-   Update type of `window()` function.
-   Freshen row types using deterministic property order.
-   Libflux JSON deserialization uses type properly.
-   Expose the builtin polytypes when analyzing a `stdlib` package.
-   Deserialize call expressions when arguments are missing.
-   Handled malformed data as well as EOF.
-   Allow unsigned integers to be subtractable.
-   Link both `libflux` and `liblibstd` for flux-config.
-   Link `libstd` into the `lib` directory instead of `libflux`.
-   Flux-config correctly copies `stdlib` when using a module.
-   Add 169.254/16 range to URL validator.
-   Update `uuid` library to improve security.
-   Handle invalid string literals.
-   Remove ’tags’ line from local tags.

## v0.59.6

### Bug fixes

-   `derivative()` works properly across multiple buffers.

## v0.59.5

### Bug fixes

-   Revert window optimizations to fix regression in output row sorting.

## v0.59.4

### Bug fixes

-   Remove `tags` line from local tags.
-   Handle malformed data as well as EOF.

## v0.59.3

### Bug fixes

-   Link both `libflux` and `libstd` for flux-config.

## v0.59.2

### Bug fixes

-   Link `libstd` into the lib directory instead of `libflux`.

## v0.59.1

### Bug fixes

-   Flux-config correctly copies `stdlib` when using a module.
-   UUID security.

## v0.59.0

### Features

-   Add Go/Rust API for getting semantic graph.
-   Optimize `limit()` transformation.
-   Optimize `group()` transformation.

### Bug fixes

-   AST json serialization glitches.
-   Better messaging for malformed CSV.
-   Skip stdlib symlink was removed erroneously.
-   Ensure stdlib directory is created.
-   Correctly skip the stdlib symlink in libflux.
-   Ensure that stdlib is present when building with flux-config.

## v0.58.4

### Bug fixes

-   Skip stdlib symlink was removed erroneously.

## v0.58.3

### Bug fixes

-   Ensure stdlib directory is created.

## v0.58.2

### Bug fixes

-   Correctly skip the stdlib symlink in libflux.

## v0.58.1

### Bug fixes

-   Ensure that stdlib is present when building with flux-config.

## v0.58.0

### Features

-   Serialize semantic graph flatbuffers.
-   Implement `onEmpty` parameter for `filter()`.
-   Serialize Flux standard library types as part of build process.
-   Add type declarations for universe.
-   Methods for type checking package dependencies.
-   Add type declarations for strings.

### Bug fixes

-   Expose tracing flag.
-   Update `count` builtin type.
-   Update `experimental.set` builtin type.
-   Update the type of `influxdb.to` to be a passthrough.
-   Update `fill` builtin type.
-   Remove redundant clones found by a new version of Clippy.
-   Fix durations in Rust semantic graph.
-   Removes unnecessary rc clone in semantic serializer.
-   Do not stall forever in flux-config when an error happens with verbose.
-   Update function block return statements to produce a stmt and not an expression.
-   Fix token location for `scan_with_regex`.
-   Cache environment variable for performance.
-   Fix a couple errors in builtin types.
-   Annotate variable assignment with polytype (not monotype).

## v0.57.0

### Features

-   Categorize more Flux errors with codes.
-   Teach flux-config how to download the sources when using vendor.
-   Opentracing in query execution runtime.
-   Reduce memory allocations for operations in values.
-   Translate FlatBuffers semantic graph to Go.
-   Add types for some universe builtins.
-   Add type declarations for builtins.
-   Add Numeric and Row kind constraints.

### Bug fixes

-   Enable strict mode by default.

## v0.56.0

### Features

-   Crate for typing Flux standard library.
-   Serialize type environment.
-   Improve filter performance when filtering on values.
-   Update usage duration test to exclude queue and requeue time.
-   Add types for some built-ins.
-   Add `timeout` parameter to experimental `http.get()`.

### Bug fixes

-   Properly use a fake version with `flux-config` when no version is present.
-   Address Clippy lints.
-   Add bytes monotype to Rust semantic module.
-   Allow underscores (`_`) in type expressions.

## v0.55.1

### Bug fixes

-   Fix e2e usage test so that their queries are properly pushed down.

## v0.55.0

### Breaking changes

-   Expand the interface for `BufferedTable`.

### Features

-   Expose optimized `pivot()` function.
-   Create utility program for building `libflux`.
-   Create a tool that measures performance of calling Rust from Go.
-   Inject types in the semantic graph.
-   MonoType and PolyType flatbuffer encodings.
-   MonoType and PolyType flatbuffer schemas.
-   Update Rust flatbuffers to more closely match Rust semantic graph.
-   Flatbuffers AST to Go AST.
-   Port immutable walk and fix mutable walk.
-   Define the flatbuffers schema for semantic graph.
-   Infer imported package types.
-   Unify and infer function types.
-   Add support for safely converting bytes to strings.
-   Add sqlite3 support.
-   Add internal table utility for streaming tables.

### Bug fixes

-   Update semantic graph FlatBuffers schema for identifiers.
-   Ignore order when comparing record types.
-   Operands for `<=` and `>=` are comparable AND equatable.
-   Constrain unary expressions to be same type as operand.

## v0.54.0

### Features

-   Expose function to analyze from string.
-   Added semantic expression constraints to libflux.
-   Custom `PartialEq` for polytypes.
-   Extensible record unification.
-   `Semantic.Walk`.

### Bug fixes

-   Do not constrain type variables with empty kinds.
-   Update usage tests to filter on `_field`.
-   Record labels are scoped and fields are ordered.
-   Parse row variables.
-   Update make release to confirm remote and local are in sync.
-   Make `walk_rc` public.

## v0.53.0

### Breaking changes

-   Interpret months as part of the semantic duration.

### Features

-   Macros for type inference tests.
-   Let-polymorphism with test example.
-   Generalization, instantiation, and constraint solving.
-   Type environment.
-   Convert Rust AST to FlatBuffers format.
-   Allow lexing and parsing of string polytypes according to polytype grammar rules.
-   Add month support when adding durations to a time value.
-   Interpret months as part of the semantic duration.

### Bug fixes

-   Type variable constraints.
-   Apply sub to both sides of constraint before unifying.
-   Instantiate quantified vars, not free vars.

## v0.52.0

### Features

-   `Visitor` uses `Rc` for nodes.
-   Add `EvalOptions`.

### Bug fixes

-   Correctly lex `µs`.

## v0.51.0

### Breaking changes

-   Update the Flux SPEC to remove duration addition and subtraction.
-   Turn duration value into a vector.

### Features

-   Implementations for type substitutions and constraints.
-   Add semantic analysis.
-   Updated the duration value to include months and negative flag.
-   Create a flatbuffers schema for AST.
-   Add initial C binding for parsing an AST.
-   Create a tool for updating `.flux` tests in-place.
-   Add walk implementation.
-   Turn duration value into a vector.
-   Define initial Flux data types.

### Bug fixes

-   Update libflux parser to match the Go parser.
-   Allow data collected by `prometheus.scrape()` to be used by `histogramQuantile()`.
-   Remove mock allocator.
-   Validate URL for `sql.from()`, `sql.to()`, and `socket.from()`.

## v0.50.2

### Bug fixes

-   Make `keep()` and `drop()` throw an error if merging tables with different schemas.

## v0.50.1

### Bug fixes

-   Add annotated errors to the execute package where it affects normal usage.
-   Reorder variables in the allocator for atomic operations.

## v0.50.0

### Features

-   Add `experimental/prometheus` package.
-   Add a memory manager to the memory allocator.
-   Add an internal function for generating data.
-   Switch to using discarding mode for transformations.
-   Group key join on `_time`.

### Bug fixes

-   Require `data` parameter in `monitor.check()`.
-   Return the EOF error when reading metadata.
-   Re-add missing import.
-   Fix broken links in SPEC.
-   Return error from cache.
-   Update the `universe` package to use flux errors throughout.
-   Parse escape characters in string interpolation expressions.
-   Improve CSV error message for serialized Flux error.
-   Have the interpreter return annotated Flux errors.

## v0.49.0

### Features

-   Optimize `filter()` to pass through tables when possible.
-   Additional arrow builder utilities.
-   Add a `benchmark()` function to the testing package.
-   Add an arrow backed version of the table buffer.

### Bug fixes

-   Fix `sql.from()` connection leak.
-   Fix some of the memory leaks within the standard library.
-   Fix `mqtt.to()` topic parameter.

## v0.48.0

### Breaking changes

-   Convert the Flux memory allocator into an arrow allocator.

### Features

-   New dependency injection framework.
-   Add planner options to Flux language.
-   Make Flux `internal/promql/quantile` behavior match PromQL `quantile` aggregate.

### Bug fixes

-   Passing context to WalkIR.
-   Make `join()` reject input tables lacking `on` columns.

## v0.47.1

### Bug fixes

-   Pass dependencies to WalkIR

## v0.47.0

### Bug fixes

-   Introduce ParenExpression.
-   Make fmt runs cargo fmt on Rust directories.
-   Update `Hex.Dump` to `hex.EncodeToString`.
-   Integrate the Promql transpiler into Flux.

## v0.46.2

### Bug fixes

-   Make `to` use URL validator.
-   Add filesystem to default test dependencies.

## v0.46.1

### Bug fixes

-   Add a filesystem service.
-   Do a pointer comparison for table objects instead of a deep compare.

## v0.46.0

### Features

-   Replace EnvironmentSecretService with EmptySecret….
-   Source location for rust parser.

### Bug fixes

-   Push error for bad string expression.
-   Remove `token` parameter from `pagerduty.endpoint`.

## v0.45.2

### Bug fixes

-   Push the tag before running goreleaser.
-   Additional opentracing spans for debugging query flow.

## v0.45.1

### Bug fixes

-   Ensure `http.post` respects the context.

## v0.45.0

### Features

-   Added Google Bigtable `from()`.

### Bug fixes

-   Add `pagerduty.severityFromLevel()` helper function.
-   Sleep function now gets canceled when the context is canceled.
-   Categorize the undefined identifier as an invalid status code.
-   Panic from `CheckKind` in `memberEvaluator`.

## v0.44.0

### Features

-   Add `http.basicAuth` function.
-   Add measurement filters to `monitor.from` and `monitor.logs`.

### Bug fixes

-   changed the default HTTP client to be more robust.

## v0.43.0

### Features

-   PagerDuty endpoint for alerts and notifications.

## v0.42.0

### Features

-   Add `stateChanges` function.

### Bug fixes

-   Race condition in looking up types in `map`.
-   Support bool equality expressions.
-   Calculating a type variable’s free type variables.
-   Do not generate fresh type variables for member expressions.
-   Array instantiation.

## v0.41.0

### Features

-   Add ability to validate URLs before making `http.post` requests.
-   Evaluate string interpolation.
-   Implement the `secrets.get` function.
-   Added secret service interface.
-   Add secrets package that will construct a secret object.
-   Added a SecretService interface and a new dependencies package and a basic test of functionality.
-   Add Slack endpoint.

### Bug fixes

-   Make `reset()` check for non-nil data before calling `Release()`.
-   Add test case for `notify` function.
-   Add missing math import to test case.
-   Make packages aware of options.
-   Resolved `holtWinters` panic.
-   Use non-pointer receiver for `interpreter.function`.

## v0.40.2

### Bug fixes

-   Resolved `holtWinters()` panic.

## v0.40.1

### Bug fixes

-   Use non-pointer receiver for `interpreter.function`.

## v0.40.0

### Breaking changes

-   Update compiler package to use true scope.
-   Add `http` and `json` to prelude.

### Features

-   Add `alerts.check()` function.
-   Add `alerts.notify` function.
-   Add `kaufmansER()` and `kaufmansAMA()` functions.
-   Add `experimental.to()` function.
-   Add `experimental.set()` function to update entire object.
-   Add `experimental.objectKeys()` function.
-   Add `tripleExponentialDerivative()` function.
-   Add `json.encode()` function.
-   Add `mqtt.to()` function.
-   Add Bytes type.
-   Update compiler package to use true scope.
-   Add http endpoint.
-   Add post method implementation.
-   String interpolation.

### Bug fixes

-   Avoid wrapping table errors in the CSV encoder.
-   Remove irrelevant TODOs.
-   `mode()` now properly considers nulls when calculating the mode.
-   Add `http` and `json` to prelude.
-   Rename all Flux test files to use `_test.flux`.

## v0.39.0

In Flux 0.39.0, `holtWinters()` can cause the query engine to panic. **Flux 0.40.2 resolves this panic.**

### Breaking changes

-   Implement the scanning components for string expressions.

### Features

-   Add `tail()` function.
-   Add framework for `http.post()` function.
-   Implement `deadman()` function.
-   Time arithmetic functions.
-   Alerts package.
-   Add an experimental `group()` function with mode `extend`.
-   Implement the scanning components for string expressions.
-   Add `chandeMomentumOscillator()` function.
-   Add `hourSelection()` function.
-   Add `date.year()` function

### Bug fixes

-   Update object to use Invalid type instead of nil monotypes.
-   Make it so the alerts package can be defined in pure Flux.
-   Close connection after `sql.to()`.

## v0.38.0

### Features

-   Update selectors to operate on time columns.
-   Add `relativeStrengthIndex()` transformation.
-   Add double and triple exponential average transformations (`doubleEMA()` and `tripleEMA()`).
-   Add `holtWinters()` transformation.
-   Add `keepFirst` parameter to `difference()`.
-   DatePart equivalent functions.
-   Add runtime package.
-   Add and subtract duration literal arithmetic.
-   Allow `keep()` to run regardless of nonexistent columns. If all columns given are nonexistent, `keep()` returns an empty table.
-   Scanner returns positioning.

### Bug fixes

-   Function resolver now keeps track of local assignments that may be evaluated at runtime.
-   Fixed InfluxDB test errors.
-   Add range to tests to pass in InfluxDB.
-   Allow converting a duration to a duration.
-   Catch integer overflow and underflow for literals.

## v0.37.2

-   *General cleanup of internal code.*

## v0.37.1

### Bug fixes

-   Fixed InfluxDB test errors.
-   Add range to tests to pass in InfluxDB.

## v0.37.0

### Features

-   Add PromQL to Flux transpiler and Flux helper functions.
-   Add mutable arrow array builders.
-   Created date package.
-   Return query and result errors in the multi result encoder.
-   Add `exponentialMovingAverage()`.
-   Add full draft of Rust parser.
-   Implement more production rules.
-   AST marshalling.
-   Parse statements.
-   Parse integer and float literals.
-   Add initial Rust implementation of parser.

## v0.36.2

### Bug fixes

-   Add helper methods for comparing entire result sets.
-   Map will not panic when a record is `null`.

## v0.36.1

### Bug fixes

-   Add `range` call to some end-to-end tests.
-   Fix implementation of `strings.replaceAll`.

## v0.36.0

### Features

-   Updated `movingAverage()` and added `timedMovingAverage`.
-   `elapsed()` function.
-   `mode()` function.
-   `sleep()` function.
-   Modify error usage in places to use the new enriched errors.
-   Enriched error interface.
-   End-to-end tests that show how to mimic pandas functionality.
-   End-to-end tests for string functions.

### Bug fixes

-   Fix `difference()` so that it returns an error instead of panicking when given a `_time` column.
-   Added end-to-end tests for type conversion functions.
-   Make `map()` error if return type is not an object.
-   Fixed miscounted allocations in the `ColListTableBuilder`.
-   Support formatting `with`.

### Breaking changes

-   Updated `movingAverage()` to `timedMovingAverage` and added new `movingAverage()` implementation.

## v0.35.1

### Bug fixes

-   Re-add `mergeKey` parameter to `map()` in deprecated state.

## v0.35.0

### Breaking changes

-   Remove `mergeKey` parameter from the `map()` function.

### Features

-   Add `sql.to()` function.
-   Add `movingAverage()` function.
-   Add `strlen()` and `substring()` functions to the `strings` package.

### Bug fixes

-   Remove `mergeKey` parameter from the `map()` function.
-   Parse float types with PostgreSQL.

## v0.34.2

### Bug fixes

-   Parse float types with PostgreSQL.

## v0.34.1

### Features

-   Add custom PostgreSQL type support.
-   Added MySQL type support.
-   Nulls work in table and row functions.

### Bug fixes

-   Fixed boolean literal type conversion problem and added tests.
-   Diff should track memory allocations when it copies the table.
-   Copy table will report if it is empty correctly.

## v0.33.2

### Bug fixes

-   Use `strings.Replace` instead of `strings.ReplaceAll` for compatibility.

## v0.33.1

### Bug fixes

-   Copy table will report if it is empty correctly.

## v0.33.0

### Breaking changes

-   Implement nulls in the compiler runtime.

### Features

-   Add Go `regexp` functions to Flux.
-   Add the exists operator to the compiler runtime.
-   Implement nulls in the compiler runtime.
-   Add nullable kind.
-   Support “with” syntax for objects in row functions.
-   Port several string functions from go `strings` library to Flux.
-   Add exists unary operator.

### Bug fixes

-   Add range to map\_extension\_with.flux.
-   Row function resets records map with each call to prepare.
-   Fix `joinStr`, including adding an EndToEnd Test.
-   Fix `string_trimLeft` and `string_trimRight` so that they pass in InfluxDB.
-   Add length check for empty tables in fill.

## v0.32.1

### Bug fixes

-   Identify memory limit exceeded errors in dispatcher.

## v0.32.0

### Breaking changes

-   Remove the control package.

### Bug fixes

-   Changelog generator now handles merge commits better.
-   Return count of errors when checking AST.

## v0.31.1

### Bug fixes

-   Do not call done after calling the function.

## v0.31.0

### Breaking changes

-   Copy the table when a table is used multiple times.

### Features

-   Support for dynamic queries.

### Bug fixes

-   Copy the table when a table is used multiple times.

## v0.30.0

### Features

-   Support for dynamic queries.

## v0.29.0

### Breaking changes

-   Make `on` a required parameter to `join()`.

### Features

-   Add stream table index functions ( [`tableFind()`](/flux/v0/stdlib/universe/tablefind/), [`getRecord()`](/flux/v0/stdlib/universe/getrecord/), [`getColumn()`](/flux/v0/stdlib/universe/getcolumn/) ).
-   Construct invalid binary expressions when given multiple expressions.

### Bug fixes

-   Properly use RefCount to reference count tables.
-   Remove the race condition within the `(*Query).Done` method.
-   Fix table functions test.
-   Add `column` parameter to `median()`.
-   Modify `median` to work with `aggregateWindow()`.
-   `pivot()` now uses the correct column type when filling nulls.
-   Add error handling for property list.
-   Return the error from the context in the executor.

## v0.28.3

### Bug fixes

-   Fix request results labels to count runtime errors.
-   An error when joining could result in two calls to finish.

## v0.28.2

### Bug fixes

-   Preallocate data when constructing a new string array.

## v0.28.1

### Bug fixes

-   Make executor respect memory limit from caller.

## v0.28.0

### Features

-   Allow choosing sample/population mode in `stddev()`.

### Bug fixes

-   Fix `reduce()` so it resets the reduce value to the neutral element value for each new group key and reports an error when two reducers write to the same destination group key.

## v0.27.0

### Features

-   Add `trimSuffix` and `trimPrefix` functions to the strings package.
-   Add support for conditional expressions to compiler.
-   Add conditional expression handling to interpreter.

### Bug fixes

-   Enforce memory and concurrency limits in controller.
-   Format conditional expression.
-   `tagKeys` should include a call to `distinct`.

## v0.26.0

### Breaking changes

-   Aggregates now accept only a `column` parameter. `columns` not used.

### Features

-   Add handling for conditional expressions to type inference.
-   Add `if`/`then`/`else` syntax to Flux parser.
-   Added a WalkIR function that external programs can use to traverse an opSpec structure.
-   Add planner options to compile options.
-   Add example on how to use Flux as a library.
-   `duplicate()` will now overwrite a column if the as label already exists.

#### Bug fixes

-   Format right child with good parentheses.
-   Make staticcheck pass.
-   Rename `json` tag so go vet passes.
-   The controller pump could reference a nil pointer.
-   Create a DependenciesAwareProgram so controller can assign dependencies.
-   Make `Program.Start` start execution synchronously.
-   Read the metadata channel in a separate goroutine.
-   Remove dead code in controller so `staticcheck` passes.
-   Allow Flux unit tests to pass.
-   Require a Github token to perform a release.
-   Change example name to make go vet pass.
-   Make `csv.from` return decode error.

## v0.25.0

### Breaking changes

-   Fix logical operators (`and`, `or`) precedence.

### Bug fixes

-   Omit space between unary operator and operand.
-   Format AST preserving operator precedence.

## v0.24.0

### Breaking changes

-   Rename `percentile()` function to `quantile()`.

### Bug fixes

-   Handle when a non-call expression is parsed as the pipe destination.
-   Add error message to Compile methods for empty Spec.

## v0.23.0

### Breaking changes

-   Remove unused statistics from the struct.

### Features

-   Define comparison operators between time types.
-   Parse signed duration.
-   Added `reduce()` function and supporting go API for implementation.
-   Fix for recognizing locally scoped objects and arrays in a row function.

### Bug fixes

-   Columns in percentile signature and more strict param checking.
-   Report the error received when parsing a bad regex literal.
-   Remove unused statistics from the struct.

## v0.22.0

### Features

-   Added a math package and ported all 64 bit go math library functions.

### Bug fixes

-   Make read-like access patterns for objects thread-safe.

## v0.21.4

### Bug fixes

-   Test union.flux correctly uses sort.
-   Pivot orders rowKey and columnKey by the input parameters, rather than the table column order.
-   Deterministic sorting of input tables in join.
-   Group key comparison works regardless of column ordering.

## v0.21.3

### Bug fixes

-   Fix test to pass in InfluxDB.
-   Write table and result name in each row of CSV output.
-   Make time() function accept any format that parser accepts.
-   Return errors when evaluating functions.
-   Prevent a deadlock in the array expression parser.

## v0.21.2

### Bug fixes

-   Add AST compiler to mappings.

## v0.21.1

### Bug fixes

-   Make ASTCompiler marshalable.
-   Fix a controller test to be less flaky.
-   `from()` must send deep table copies to its downstream transformations.

## v0.21.0

### Breaking changes

-   Support attaching arbitrary query metadata from the executor.

### Features

-   Support attaching arbitrary query metadata from the executor.
-   Socket source.

### Bug fixes

-   Add locks to make diff threadsafe.

## v0.20.0

### Features

-   AST match.
-   Generate ASTs from Flux test files for external consumption.
-   Add compile subcommand that compiles Flux to spec.

### Bug fixes

-   Change loadStorage and loadMem to be options so that they are modifiable.
-   Generate skipped tests; skip in test driver.

## v0.19.0

### Breaking changes

-   Make `window()` parameters match SPEC.
-   Split FromProcedureSpec into logical and physical specs.

### Features

-   Add `contains()` function to check for membership in lists.
-   `test` keyword.

### Bug fixes

-   Raw query test case.

## v0.18.0

### Features

-   Add strings package with functions to trim/change string case.
-   Make duration conversion public.
-   Add assertEmpty method and use it with testing.test.
-   Expose literal parsers used within the parser.
-   Add testing.diff function.
-   Execute command.

### Bug fixes

-   Refactor the controller to remove data races.
-   Member expressions using a string literal use the incorrect end bracket.
-   Skip lambda evaluation when referencing nulls.
-   Options editor should use ast.Expression.
-   Fix decoder bug where a default table ID is given when none is required.
-   Add close to SourceIterator.

## v0.17.0

### Features

-   Checks for option dependencies.
-   Add query success and error metrics.
-   Track nested blocks in the parser.
-   Update `aggregateWindow()` to include `createEmpty` as parameter to allow for null results.
-   Add query function count metrics.

### Bug fixes

-   Multiplicative operators are above additive operators in precedence.
-   Fix panic when copying lambda.
-   Only print a package’s public exports.
-   Cannot access imports of imports.
-   Check for schema collision when appending columns to a table.
-   Process test helper had bad logic to check for errors.
-   Handle rune errors correctly when decoding an illegal token.

## v0.16.1

### Bug fixes

-   Copy packages for importer copy.

## v0.16.0

### Features

-   Adds various v1 meta queries helper functions

### Bug fixes

-   Fixes various UX issues.
-   Object polytype.
-   Fix edge case panic in `assertEquals`.
-   Check for equality in time columns correctly.
-   Fix bug where `assertEquals` did not check tables without a match in both streams.
-   Clear return for each REPL command.

## v0.15.0

### Features

-   Add rule to remove filter true nodes.
-   Checks for variable reassignment and option declarations below package block.

### Bug fixes

-   Move a test file into the testing/testdata folder.

## v0.14.0

### Breaking changes

-   Implement and require builtin statements.
-   Fix keys to output group key.
-   Organizes builtin code into Flux packages.
-   Change flux command to be a REPL.

### Features

-   Implement and require builtin statements.
-   Added a new utility library for generating test data.
-   `columns()` function.
-   Add fill function to set a default value for null values in a column.
-   Organizes built-in code into Flux packages.
-   Change flux command to be a REPL.
-   Refactored the table builder interfaces to support null value creation.
-   Aggregates process empty/all-null tables by creating a null row.
-   Show nulls in REPL as empty string.
-   Add ability to define built-in packages.
-   Treat omitted values with no defaults as nil in CSV.
-   Build arrow columns with null values.
-   Converting limit to use arrow arrays.
-   TableBuilder interface and ColListTableBuilder implementation support creation of nil values.

### Bug fixes

-   Count nulls in the count aggregate.
-   Fix keys to output group key.
-   Adding test for type mismatch in group.
-   Nest extern blocks for each level in scope.
-   Memory leak in limit when slicing.
-   Prettier formatting for package.
-   Change Package.Path to be json omitempty.

## v0.13.0

### Breaking changes

-   Add File and Package nodes to the AST.

### Features

-   Embed errors into the ast from the parser.
-   Add no-points optimization for `from() |> keys()`.
-   Add File and Package nodes to the AST.
-   Add a function for checking for errors within the AST.

### Bug fixes

-   Remove unneeded use of memory allocator.
-   Allow the memory allocator to be nil for arrow arrays.
-   Fix several bugs in copy methods add tests.
-   Fix a flaky test in the controller shutdown.

## v0.12.0

### Features

-   Slice utils.
-   Parse string literal object keys.
-   Add tests for multi-line and escaped strings.
-   Arrow helper method.
-   Converting all aggregates to use arrow arrays.

### Bug fixes

-   Embed plan.DefaultCost in input and output functions.
-   Side effect statements are now copied between related interpreter scopes.

## v0.11.0

### Features

-   Add utility methods for converting a slice into an arrow array buffer.

### Bug fixes

-   Do not panic with unbalanced parenthesis.
-   Respect positive timeout for toHTTP.

## v0.10.0

### Breaking changes

-   Change “label” to “column” for state tracking functions.

### Features

-   Plan validation.
-   Testing framework no longer checks output.
-   Integrate arrow arrays into the table builder.
-   Support packages and imports.

### Bug fixes

-   Cancel all queries after timeout elapses.
-   `makefile` for generating the scanner after clean was incorrect.

## v0.9.0

### Features

-   Option Editor.

### Bug fixes

-   Return the source attribute in the location correctly.

## v0.8.0

### Features

-   Rule to chain group operations.
-   Add package and import support to the semantic graph.
-   Add `assertEquals` function to transformations.
-   Parse import and package statements
-   Walk pattern for AST.
-   AST formatting.
-   Switch over to the new parser.

### Bug fixes

-   Make controller return planner failures.
-   Collision between external and fresh type vars.
-   fmt for import and package.
-   Add import/package nodes to ast.Walk.
-   Improve panic message when the wrong column type is used.
-   Check nil results when computing stats.
-   Suppress group push down for \_time and \_value.
-   Terminal output functions must produce results.
-   Fix race in interpreter.doCall.
-   Fix ast.Walk for Assignment rename.
-   Improve error message for missing object properties.
-   Add unary logical expression to the parser.
-   Variable declarator node needs to duplicate the location information.

## v0.7.4

### Bug Fixes

-   Add missing comparison operators.

## v0.7.3

### Bug Fixes

-   Fix the ident statement to use expression suffix.


---

## Query data sources

Query the following data sources with Flux:

-   [InfluxDB](#influxdb)
-   [SQL databases](#sql-databases)
-   [CSV](#csv)
-   [Google Cloud Bigtable](#google-cloud-bigtable)

### [InfluxDB](/flux/v0/query-data/influxdb/)

Use [`from()`](/flux/v0/stdlib/influxdata/influxdb/from/) and [`range`](/flux/v0/stdlib/universe/range/) to query data from InfluxDB using Flux.

```js
from(bucket: "example-bucket")
  |> range(start: -1h)
```

[Read more](/flux/v0/query-data/influxdb/)

### [SQL databases](/flux/v0/query-data/sql/)

Use [`sql.from()`](/flux/v0/stdlib/sql/from/) to query SQL databases with Flux.

```js
import "sql"

sql.from(
    driverName: "postgres",
    dataSourceName: "postgresql://user:password@localhost",
    query:"SELECT * FROM TestTable",
)
```

[Read more](/flux/v0/query-data/sql/)

### [CSV](/flux/v0/query-data/csv/)

Use [`csv.from()`](/flux/v0/stdlib/csv/from/) and [experimental `csv.from()`](/flux/v0/stdlib/experimental/csv/from/) to query CSV data with Flux. Query a CSV string, CSV file, or CSV data from a URL.

```js
import "csv"

csvData =
    "
#group,false,false,true,true,true,false,false
#datatype,string,long,string,string,string,long,double
#default,_result,,,,,,
,result,table,dataset,metric,sensorID,timestamp,value
,,0,air-sensors,humidity,TLM0100,1627049400000000000,34.79
,,0,air-sensors,humidity,TLM0100,1627049700000000000,34.65
,,1,air-sensors,humidity,TLM0200,1627049400000000000,35.64
,,1,air-sensors,humidity,TLM0200,1627049700000000000,35.67
"

csv.from(csv: csvData)
```

[Read more](/flux/v0/query-data/csv/)

### [Google Cloud Bigtable](/flux/v0/query-data/bigtable/)

Use [`bigtable.from`](/flux/v0/stdlib/experimental/bigtable/from) to query [Google Cloud Bigtable](https://cloud.google.com/bigtable/) with Flux.

```js
import "experimental/bigtable"

bigtable.from(url: "http://example.com/metrics")
```

[Read more](/flux/v0/query-data/bigtable/)


---

## Work with Prometheus

[Prometheus](https://prometheus.io/) is an open-source toolkit designed to build simple and robust monitoring and alerting systems. Flux provides tools for scraping raw [Prometheus-formatted metrics](https://prometheus.io/docs/concepts/data_model/) from an HTTP-accessible endpoint, writing them to InfluxDB, then processing those raw metrics for visualization in InfluxDB dashboards.

### [Scrape Prometheus metrics](/flux/v0/prometheus/scrape-prometheus/)

Use the Flux [`prometheus.scrape`](/flux/v0/stdlib/experimental/prometheus/scrape/) function to scrape Prometheus-formatted metrics from an HTTP-accessible endpoint.

### [Work with Prometheus metric types](/flux/v0/prometheus/metric-types/)

Learn how to use Flux to work with Prometheus’ four main metric types (counter, gauge, histogram, and summary) and process them for visualizations in InfluxDB dashboards.

[prometheus](/flux/v0/tags/prometheus/)


---

## Use the InfluxDB documentation MCP server

The **InfluxDB documentation MCP server** lets AI tools and agents search InfluxDB documentation directly from your development environment. Use it to find answers, code examples, and configuration details without leaving your IDE.

## Why use the documentation MCP server?

When you connect the documentation MCP server to your AI coding assistant, the assistant can search InfluxDB documentation to answer your questions with accurate, up-to-date information. Instead of switching to a browser or guessing at syntax, you can ask questions in your IDE and get responses grounded in official documentation.

**Common use cases:**

-   Get help writing queries, client library code, or CLI commands
-   Look up configuration options and environment variables
-   Find code examples for specific tasks
-   Troubleshoot errors with documentation-backed answers

## Install the documentation MCP server

The documentation MCP server is a hosted service—you don’t need to install or run anything locally. Add the server URL to your AI assistant’s MCP configuration.

On first use, you’ll be prompted to sign in with Google. This authentication is used only for rate limiting—no personal data is collected.

**MCP server URL:**

```text
https://influxdb-docs.mcp.kapa.ai
```

The server uses SSE (Server-Sent Events) transport.

### Configure your AI assistant to use the documentation MCP server

The following instructions show how to configure popular AI assistants to use the InfluxDB documentation MCP server.

<!-- Tabbed content: Select one of the following options -->

**Claude Desktop:**

In **Claude Desktop**, go to **Settings** > **Developer** and edit your configuration. Add the following JSON configuration:

```json
{
  "mcpServers": {
    "influxdb-docs": {
      "url": "https://influxdb-docs.mcp.kapa.ai"
    }
  }
}
```

Save the file and restart Claude Desktop for the changes to take effect.

**ChatGPT Desktop:**

In **ChatGPT Desktop**, go to **Settings** > **Integrations** > **Enable MCP** and add a new server. Add the following JSON configuration:

```json
{
  "mcpServers": {
    "influxdb-docs": {
      "url": "https://influxdb-docs.mcp.kapa.ai",
      "transport": "sse"
    }
  }
}
```

Save the configuration and restart ChatGPT Desktop.

**GitHub Copilot (VS Code):**

In **VS Code**, configure GitHub Copilot to use the MCP server:

1. Create or edit `.vscode/mcp.json` in your workspace or project directory
2. Add the following configuration:

```json
{
  "servers": {
    "influxdb-docs": {
      "type": "http",
      "url": "https://influxdb-docs.mcp.kapa.ai"
    }
  }
}
```

3. Restart or reload VS Code
4. Open the Command Palette (`Ctrl+Shift+P` or `Cmd+Shift+P`)
5. Run **MCP: List Servers** to verify the server is registered

The InfluxDB documentation MCP server will now be available through GitHub Copilot Chat.

**Cursor:**

In **Cursor**, add the MCP server configuration to your MCP settings file.

1. Open **Settings** and navigate to **MCP Servers**
2. Click **Add MCP Server** or edit the configuration file directly
3. Add the following configuration to `.cursor/mcp.json` (project-level) or `~/.cursor/mcp.json` (global):

```json
{
  "mcpServers": {
    "influxdb-docs": {
      "url": "https://influxdb-docs.mcp.kapa.ai",
      "transport": "streamableHttp"
    }
  }
}
```

Save the file and restart Cursor.

**OpenCode:**

In **OpenCode**, configure the MCP server in your configuration file:

1. Create or edit `opencode.json` (or `opencode.jsonc`) in your workspace
2. Add the following configuration:

```json
{
  "$schema": "https://opencode.ai/config.json",
  "mcp": {
    "influxdb-docs": {
      "type": "remote",
      "url": "https://influxdb-docs.mcp.kapa.ai",
      "enabled": true
    }
  }
}
```

3. Start OpenCode and use the `/init` command to verify the MCP server is accessible

The InfluxDB documentation search tools will be available in your OpenCode sessions.

<!-- End tabbed content -->

## Authentication and rate limits

When you connect to the documentation MCP server for the first time, a Google sign-in window opens to complete an OAuth/OpenID Connect login.

The hosted MCP server:

-   Requests only the `openid` scope from Google
-   Receives an ID token (JWT) containing a stable, opaque user ID
-   Does not request `email` or `profile` scopes—your name, email address, and other personal data are not collected

The anonymous Google ID enforces per-user rate limits to prevent abuse:

-   **40 requests** per user per hour
-   **200 requests** per user per day

On Google’s consent screen, this appears as “Associate you with your personal info on Google.” This is Google’s generic wording for the `openid` scope—it means the app can recognize that the same Google account is signing in again. It does not grant access to your email, name, contacts, or other data.

## Search documentation with the MCP tool

The documentation MCP server exposes a semantic search tool:

```text
search_influxdb_knowledge_sources
```

This tool lets AI agents perform semantic retrieval over InfluxDB documentation and related knowledge sources.

**What the tool does:**

-   Searches all InfluxDB documentation for a given query
-   Returns the most relevant chunks in descending order of relevance
-   Each chunk is a self-contained snippet from a single documentation page

**Response format:**

Each result includes:

-   `source_url`: URL of the original documentation page
-   `content`: The chunk content in Markdown

![MCP tool search results showing InfluxDB documentation](/img/influxdb3/core-mcp-influxdb3-plugin.png)

## Use the documentation MCP server

After you install the documentation MCP server, your AI assistant can search InfluxDB documentation to help you with tasks. Ask questions naturally—the assistant uses the MCP server to find relevant documentation and provide accurate answers.

### Example prompts

> “How do I write data to InfluxDB using Python?”
> 
> “What’s the syntax for a SQL query with a WHERE clause in InfluxDB?”
> 
> “Show me how to configure Telegraf to collect CPU metrics.”
> 
> “What environment variables does the InfluxDB CLI use?”
> 
> “How do I create a database token with read-only permissions?”


---

## Join data

Use the Flux [`join` package](/flux/v0/stdlib/join/) to join two data sets based on common values. Learn how join two data sets using the following join methods:

[

**Inner join**

](#perform-an-inner-join)

[

**Left outer join**

](#perform-a-left-outer-join)

[

**Right outer join**

](#perform-a-right-outer-join)

[

**Full outer join**

](#perform-a-full-outer-join)

#### When to use the join package

We recommend using the `join` package to join streams that have mostly different schemas or that come from two separate data sources. If you’re joining data from the same data source with the same schema, using [`union()`](/flux/v0/stdlib/universe/union/) and [`pivot()`](/flux/v0/stdlib/universe/pivot/) to combine the data will likely be more performant.

For more information, see [When to use union and pivot instead of join functions](/influxdb/v2/query-data/flux/join/#when-to-use-union-and-pivot-instead-of-join-functions).

-   [How join functions work](#how-join-functions-work)
    -   [Input streams](#input-streams)
    -   [Join predicate function (on)](#join-predicate-function-on)
    -   [Join output function (as)](#join-output-function-as)
-   [Perform join operations](#perform-join-operations)
    -   [Perform an inner join](#perform-an-inner-join)
    -   [Perform a left outer join](#perform-a-left-outer-join)
    -   [Perform a right outer join](#perform-a-right-outer-join)
    -   [Perform a full outer join](#perform-a-full-outer-join)
    -   [Join on time](#join-on-time)
-   [Troubleshoot join operations](#troubleshoot-join-operations)

## How join functions work

`join` functions join *two* streams of tables together based on common values in each input stream.

-   [Input streams](#input-streams)
-   [Join predicate function (on)](#join-predicate-function-on)
-   [Join output function (as)](#join-output-function-as)

### Input streams

Each input stream is assigned to the `left` or `right` parameter. Input streams can be defined from any valid data source. For more information, see:

-   [Query data sources](/flux/v0/query-data/)
-   Define ad hoc tables with [`array.from()`](/flux/v0/stdlib/array/from/)

#### Data requirements

To join data, each input stream must have the following:

-   **One or more columns with common values to join on**.  
    Columns do not need identical labels, but they do need to have comparable values.
    
-   **Identical [group keys](/flux/v0/get-started/data-model/#group-key)**.  
    Functions in the `join` package use group keys to quickly determine what tables from each input stream should be paired and evaluated for the join operation.  
    *Both input streams should have the same group key.* If they don’t, your join operation may not find any matching tables and will return unexpected output. If the group keys of your input streams are not identical, use [`group()`](/flux/v0/stdlib/universe/group/) to regroup each input stream before joining them together.
    
    Only tables with the same [group key instance](/flux/v0/get-started/data-model/#example-group-key-instances) are joined.
    

### Join predicate function (on)

`join` package functions require the `on` parameter to compare values from each input stream (represented by `l` (left) and `r` (right)) and returns `true` or `false`. Rows that return `true` are joined. This parameter is a [predicate function](/flux/v0/get-started/syntax-basics/#predicate-functions).

```js
(l, r) => l.column == r.column
```

### Join output function (as)

`join` package functions *(except [`join.time()`](/flux/v0/stdlib/join/time/))* require the `as` parameter to define the output schema of the join. The `as` parameter returns a new record using values from joined rows–left (`l`) and right (`r`).

```js
(l, r) => ({l with name: r.name, location: r.location})
```

#### Do not modify group key columns

Do not modify group key columns. The `as` function must return the same group key as both input streams to successfully perform a join.

## Perform join operations

The `join` package supports the following join types and special use cases:

-   [Perform an inner join](#perform-an-inner-join)
-   [Perform a left outer join](#perform-a-left-outer-join)
-   [Perform a right outer join](#perform-a-right-outer-join)
-   [Perform a full outer join](#perform-a-full-outer-join)
-   [Join on time](#join-on-time)

### [Perform an inner join](/flux/v0/join-data/inner/)

Use [`join.inner()`](/flux/v0/stdlib/join/inner/) to perform an inner join of two streams of data. Inner joins drop any rows from both input streams that do not have a matching row in the other stream.

```js
import "join"

left = from(bucket: "example-bucket-1") |> //...
right = from(bucket: "example-bucket-2") |> //...

join.inner(
    left: left,
    right: right,
    on: (l, r) => l.column == r.column,
    as: (l, r) => ({l with name: r.name, location: r.location}),
)
```

[Read more](/flux/v0/join-data/inner/)

### [Perform a left outer join](/flux/v0/join-data/left-outer/)

Use [`join.left()`](/flux/v0/stdlib/join/left/) to perform an outer left join of two streams of data. Left joins output a row for each row in the **left** data stream with data matching from the **right** data stream. If there is no matching data in the **right** data stream, non-group-key columns with values from the **right** data stream are *null*.

```js
import "join"

left = from(bucket: "example-bucket-1") |> //...
right = from(bucket: "example-bucket-2") |> //...

join.left(
    left: left,
    right: right,
    on: (l, r) => l.column == r.column,
    as: (l, r) => ({l with name: r.name, location: r.location}),
)
```

[Read more](/flux/v0/join-data/left-outer/)

### [Perform a right outer join](/flux/v0/join-data/right-outer/)

Use [`join.right()`](/flux/v0/stdlib/join/right/) to perform an right outer join of two streams of data. Right joins output a row for each row in the **right** data stream with data matching from the **left** data stream. If there is no matching data in the **left** data stream, non-group-key columns with values from the **left** data stream are *null*.

```js
import "join"

left = from(bucket: "example-bucket-1") |> //...
right = from(bucket: "example-bucket-2") |> //...

join.right(
    left: left,
    right: right,
    on: (l, r) => l.column == r.column,
    as: (l, r) => ({r with name: l.name, location: l.location}),
)
```

[Read more](/flux/v0/join-data/right-outer/)

### [Perform a full outer join](/flux/v0/join-data/full-outer/)

Use [`join.full()`](/flux/v0/stdlib/join/full/) to perform an full outer join of two streams of data. Full outer joins output a row for all rows in both the **left** and **right** input streams and join rows that match according to the `on` predicate.

```js
import "join"

left = from(bucket: "example-bucket-1") |> //...
right = from(bucket: "example-bucket-2") |> //...

join.full(
    left: left,
    right: right,
    on: (l, r) => l.id== r.id,
    as: (l, r) => {
        id = if exists l.id then l.id else r.id
        
        return {name: l.name, location: r.location, id: id}
    },
)
```

[Read more](/flux/v0/join-data/full-outer/)

### [Join on time](/flux/v0/join-data/time/)

Use [`join.time()`](/flux/v0/stdlib/join/time/) to join two streams of data based on time values in the `_time` column. This type of join operation is common when joining two streams of [time series data](/influxdb/v2/reference/glossary/#time-series-data).

```js
import "join"

left = from(bucket: "example-bucket-1") |> //...
right = from(bucket: "example-bucket-2") |> //...

join.time(
    left: left,
    right: right,
    as: (l, r) => ({l with field1: l._value, field2: r._value_}),
)
```

[Read more](/flux/v0/join-data/time/)

## Troubleshoot join operations

For information about unexpected behaviors and errors when using the `join` package, see [Troubleshoot join operations](/flux/v0/join-data/troubleshoot-joins/).

#### Related

-   [join package](/flux/v0/stdlib/join/)
-   [join.inner() function](/flux/v0/stdlib/join/inner/)
-   [join.left() function](/flux/v0/stdlib/join/left/)
-   [join.right() function](/flux/v0/stdlib/join/right/)
-   [join.full() function](/flux/v0/stdlib/join/full/)
-   [join.time() function](/flux/v0/stdlib/join/time/)


---

## Flux versions in InfluxDB

View which versions of Flux are packaged with each version of InfluxDB.

-   [InfluxDB Cloud](#influxdb-cloud)
-   [InfluxDB Open Source (OSS)](#influxdb-open-source-oss)
-   [InfluxDB Enterprise](#influxdb-enterprise)

### InfluxDB Cloud

| InfluxDB version | Flux version |
| --- | --- |
| InfluxDB Cloud | 0.194.3 |

### InfluxDB Open Source (OSS)

| InfluxDB OSS version | Flux version |
| --- | --- |
| InfluxDB 1.11 | 0.196.1 |
| InfluxDB 1.7 | 0.50.2 |
| InfluxDB 1.8 | 0.65.1 |
| InfluxDB 2.0 | 0.131.0 |
| InfluxDB 2.1 | 0.139.0 |
| InfluxDB 2.2 | 0.162.0 |
| InfluxDB 2.3 | 0.171.0 |
| InfluxDB 2.4 | 0.179.0 |
| InfluxDB 2.5 | 0.188.1 |
| InfluxDB 2.6 | 0.191.0 |
| InfluxDB 2.7 | 0.196.1 |
| InfluxDB nightly | 0.197.0 |

### InfluxDB Enterprise

| InfluxDB Enterprise version | Flux version |
| --- | --- |
| InfluxDB Enterprise 1.7 | 0.50.2 |
| InfluxDB Enterprise 1.8 | 0.65.1 |
| InfluxDB Enterprise 1.9 | 0.161.0 |
| InfluxDB Enterprise 1.10 | 0.196.1 |
| InfluxDB Enterprise 1.11 | 0.196.1 |


---

## Get started with Flux

Flux is a **functional data scripting** language designed to unify querying, processing, analyzing, and acting on data into a single syntax.

## Flux overview

To understand how Flux works conceptually, consider the process of treating water. Water is pulled from a source, limited by demand, piped through a series of stations to modify (remove sediment, purify, and so on), and delivered in a consumable state.

## Basic Flux query

Like treating water, a Flux query does the following:

1. Retrieves a specified amount of data from a source.
2. Filters data based on time or column values.
3. Processes and shapes data into expected results.
4. Returns the result.

To see how to retrieve data from a source, select the data source: InfluxDB, CSV, or PostgreSQL.

<!-- Tabbed content: Select one of the following options -->

**InfluxDB:**

```js
from(bucket: "example-bucket")
    |> range(start: -1d)
    |> filter(fn: (r) => r._measurement == "example-measurement")
    |> mean()
    |> yield(name: "_results")
```

**CSV:**

```js
import "csv"

csv.from(file: "path/to/example/data.csv")
    |> range(start: -1d)
    |> filter(fn: (r) => r._measurement == "example-measurement")
    |> mean()
    |> yield(name: "_results")
```

**PostgreSQL:**

```js
import "sql"

sql.from(
    driverName: "postgres",
    dataSourceName: "postgresql://user:password@localhost",
    query: "SELECT * FROM TestTable",
)
    |> filter(fn: (r) => r.UserID == "123ABC456DEF")
    |> mean(column: "purchase_total")
    |> yield(name: "_results")
```

<!-- End tabbed content -->

Each example includes the following functions (in the order listed):

-   [`from()`](/flux/v0/stdlib/influxdata/influxdb/from/) to retrieve data from the data source.
-   [Pipe-forward operator (`|>`)](/flux/v0/get-started/syntax-basics/#pipe-forward-operator) to send the output of each function to the next function as input.
-   [`range()`](/flux/v0/stdlib/universe/range/), [`filter()`](/flux/v0/stdlib/universe/filter/), or both to filter data based on column values.
-   [`mean()`](/flux/v0/stdlib/universe/mean/) to calculate the average of values returned from the data source.
-   [`yield()`](/flux/v0/stdlib/universe/yield/) to yield results to the user.

*For detailed information about basic Flux queries, see [Flux query basics](/flux/v0/get-started/query-basics/).*

[Flux data model](/flux/v0/get-started/data-model/)

#### Related


---

## The future of Flux

Flux is in maintenance mode and is not supported in InfluxDB 3 due to the broad demand for native SQL and the continued growth and adoption of InfluxQL.

InfluxData continues to support Flux for InfluxDB 1.x and 2.x, and you can continue using it without changing your code. If interested in transitioning to InfluxDB 3 and you want to future-proof your code, we suggest using InfluxQL.

As we developed InfluxDB 3, our top priority was improving performance at the database layer: faster ingestion, better compression, enhanced querying, and more scalability. However, this meant we couldn’t bring everything forward from v2. As InfluxDB 3 is a ground-up rewrite of the database in a new language (from Go to Rust), we couldn’t bring Flux forward to v3.

-   [What do you mean by Flux is in maintenance mode?](#what-do-you-mean-by-flux-is-in-maintenance-mode)
-   [Is Flux going to End-of-Life?](#is-flux-going-to-end-of-life)
-   [What alternatives do you have for Flux Tasks?](#what-alternatives-do-you-have-for-flux-tasks)

## What do you mean by Flux is in maintenance mode?

We still support Flux, but are not actively developing any new Flux features. We will continue to provide security patches and will address any critical defects through the maintenance period. Our focus is our latest database engine, InfluxDB 3, and its associated products.

## Is Flux going to End-of-Life?

No, we will continue to support Flux for the foreseeable future. We will continue to support our customers who have invested in Flux and have built apps that use it. You can continue using Flux, but if you want to future-proof your code, we recommend using InfluxQL or SQL.

## What alternatives do you have for Flux tasks?

If moving to InfluxDB 3, you can’t bring Flux tasks because InfluxDB 3 doesn’t support Flux natively. When you move to v3, you will need to rewrite your tasks using whatever technologies your team prefers. However, if you’re using tasks for downsampling specifically, the storage performance in v3 is much better so you may no longer need tasks for this functionality.


---

## Flux function types and categories

Flux functions share a set of behaviors or traits that define how the function works. This types and categories lists below are not all-inclusive, but covers distinct and important function behaviors.

-   [Function types](#function-types)
-   [Function categories](#function-categories)

The icon indicates the function is experimental.

## Function types

-   [Inputs](#inputs)
-   [Outputs](#outputs)
-   [Transformations](#transformations)
    -   [Aggregates](#aggregates)
    -   [Selectors](#selectors)
-   [Dynamic queries](#dynamic-queries)

### Inputs

Flux input functions return data from data sources. The following input functions are available:

-   [array.from()](/flux/v0/stdlib/array/from/)
-   [bigtable.from()](/flux/v0/stdlib/experimental/bigtable/from/)
-   [clickhouse.query()](/flux/v0/stdlib/contrib/qxip/clickhouse/query/)
-   [csv.from()](/flux/v0/stdlib/csv/from/)
-   [from()](/flux/v0/stdlib/influxdata/influxdb/from/)
-   [from()](/flux/v0/stdlib/contrib/jsternberg/influxdb/from/)
-   [generate.from()](/flux/v0/stdlib/generate/from/)
-   [http.get()](/flux/v0/stdlib/experimental/http/get/) *– (deprecated)*
-   [influxdb.select()](/flux/v0/stdlib/contrib/jsternberg/influxdb/select/)
-   [iox.from()](/flux/v0/stdlib/experimental/iox/from/)
-   [iox.sql()](/flux/v0/stdlib/experimental/iox/sql/)
-   [logql.query\_range()](/flux/v0/stdlib/contrib/qxip/logql/query_range/)
-   [monitor.logs()](/flux/v0/stdlib/influxdata/influxdb/monitor/logs/)
-   [prometheus.scrape()](/flux/v0/stdlib/experimental/prometheus/scrape/)
-   [query.inBucket()](/flux/v0/stdlib/experimental/query/inbucket/)
-   [requests.do()](/flux/v0/stdlib/http/requests/do/)
-   [requests.do()](/flux/v0/stdlib/experimental/http/requests/do/) *– (deprecated)*
-   [requests.get()](/flux/v0/stdlib/http/requests/get/)
-   [requests.get()](/flux/v0/stdlib/experimental/http/requests/get/) *– (deprecated)*
-   [requests.post()](/flux/v0/stdlib/http/requests/post/)
-   [requests.post()](/flux/v0/stdlib/experimental/http/requests/post/) *– (deprecated)*
-   [socket.from()](/flux/v0/stdlib/socket/from/)
-   [usage.from()](/flux/v0/stdlib/experimental/usage/from/)
-   [v1.json()](/flux/v0/stdlib/influxdata/influxdb/v1/json/)

### Outputs

Flux output functions yield results or send data to a specified output destination. The following output functions are are available:

-   [experimental.to()](/flux/v0/stdlib/experimental/to/) *– (deprecated)*
-   [influxdb.wideTo()](/flux/v0/stdlib/influxdata/influxdb/wideto/)
-   [kafka.to()](/flux/v0/stdlib/kafka/to/)
-   [mqtt.to()](/flux/v0/stdlib/experimental/mqtt/to/)
-   [tickscript.alert()](/flux/v0/stdlib/contrib/bonitoo-io/tickscript/alert/)
-   [to()](/flux/v0/stdlib/influxdata/influxdb/to/)
-   [yield()](/flux/v0/stdlib/universe/yield/)

### Transformations

Flux transformations take a [stream of tables](/flux/v0/get-started/data-model/#stream-of-tables) as input, transform the data in some way, and output a stream of tables. Transformations cover a broad range of functions, but the following categorizations highlight important behaviors associated with specific transformation functions.

-   [Aggregates](#aggregates)
-   [Selectors](#selectors)

##### aggregateWindow helper function

The [`aggregateWindow()` function](/flux/v0/stdlib/universe/aggregatewindow) windows or groups data by time and applies an aggregate or selector function to input tables. **All aggregate and selector functions** work with `aggregateWindow()`.

#### Aggregates

Flux aggregate functions are [transformations](#transformations) aggregate values from input tables in some way. Output tables contain a single row with the aggregated value. Aggregate transformations output a table for every input table they receive.

Each output table from an aggregate function will:

-   Contain a single record.
-   Have the same [group key](/flux/v0/get-started/data-model/#group-key) as the input table.
-   Contain the an aggregated column. The column label will be the same as the input table. The column data type depends on the specific aggregate operation. The value of the column will be `null` if the input table is empty or the input column has only `null` values.
-   Drop all columns that are:
    -   not in the group key
    -   not the aggregated column

**The following aggregate functions are available:**

-   [aggregate.rate()](/flux/v0/stdlib/experimental/aggregate/rate/)
-   [aggregateWindow()](/flux/v0/stdlib/universe/aggregatewindow/)
-   [count()](/flux/v0/stdlib/universe/count/)
-   [cov()](/flux/v0/stdlib/universe/cov/)
-   [covariance()](/flux/v0/stdlib/universe/covariance/)
-   [experimental.count()](/flux/v0/stdlib/experimental/count/)
-   [experimental.histogramQuantile()](/flux/v0/stdlib/experimental/histogramquantile/)
-   [experimental.integral()](/flux/v0/stdlib/experimental/integral/)
-   [experimental.mean()](/flux/v0/stdlib/experimental/mean/)
-   [experimental.mode()](/flux/v0/stdlib/experimental/mode/)
-   [experimental.quantile()](/flux/v0/stdlib/experimental/quantile/)
-   [experimental.skew()](/flux/v0/stdlib/experimental/skew/)
-   [experimental.spread()](/flux/v0/stdlib/experimental/spread/)
-   [experimental.stddev()](/flux/v0/stdlib/experimental/stddev/)
-   [experimental.sum()](/flux/v0/stdlib/experimental/sum/)
-   [geo.ST\_LineString()](/flux/v0/stdlib/experimental/geo/st_linestring/)
-   [geo.totalDistance()](/flux/v0/stdlib/experimental/geo/totaldistance/)
-   [integral()](/flux/v0/stdlib/universe/integral/)
-   [mean()](/flux/v0/stdlib/universe/mean/)
-   [median()](/flux/v0/stdlib/universe/median/)
-   [mode()](/flux/v0/stdlib/universe/mode/)
-   [pearsonr()](/flux/v0/stdlib/universe/pearsonr/)
-   [prometheus.histogramQuantile()](/flux/v0/stdlib/experimental/prometheus/histogramquantile/)
-   [quantile()](/flux/v0/stdlib/universe/quantile/)
-   [reduce()](/flux/v0/stdlib/universe/reduce/)
-   [skew()](/flux/v0/stdlib/universe/skew/)
-   [spread()](/flux/v0/stdlib/universe/spread/)
-   [stddev()](/flux/v0/stdlib/universe/stddev/)
-   [sum()](/flux/v0/stdlib/universe/sum/)
-   [timeWeightedAvg()](/flux/v0/stdlib/universe/timeweightedavg/)

##### Aggregate selectors

The following functions are both aggregates and selectors. Each returns `n` values after performing an aggregate operation. They are categorized as [selector functions](#selectors) in this documentation:

-   [highestAverage()](/flux/v0/stdlib/universe/highestaverage)
-   [highestCurrent()](/flux/v0/stdlib/universe/highestcurrent)
-   [highestMax()](/flux/v0/stdlib/universe/highestmax)
-   [lowestAverage()](/flux/v0/stdlib/universe/lowestaverage)
-   [lowestCurrent()](/flux/v0/stdlib/universe/lowestcurrent)
-   [lowestMin()](/flux/v0/stdlib/universe/lowestmin)

#### Selectors

Flux selector functions are [transformations](#transformations) that return one or more record per input table.

Each output table from a selector function will:

-   Contain one or more unmodified records.
-   Have the same [group key](/flux/v0/get-started/data-model/#group-key) as the input table.

**The following selector functions are available:**

-   [aggregateWindow()](/flux/v0/stdlib/universe/aggregatewindow/)
-   [bottom()](/flux/v0/stdlib/universe/bottom/)
-   [distinct()](/flux/v0/stdlib/universe/distinct/)
-   [experimental.distinct()](/flux/v0/stdlib/experimental/distinct/)
-   [experimental.first()](/flux/v0/stdlib/experimental/first/)
-   [experimental.last()](/flux/v0/stdlib/experimental/last/)
-   [experimental.max()](/flux/v0/stdlib/experimental/max/)
-   [experimental.min()](/flux/v0/stdlib/experimental/min/)
-   [experimental.quantile()](/flux/v0/stdlib/experimental/quantile/)
-   [experimental.unique()](/flux/v0/stdlib/experimental/unique/)
-   [first()](/flux/v0/stdlib/universe/first/)
-   [highestAverage()](/flux/v0/stdlib/universe/highestaverage/)
-   [highestCurrent()](/flux/v0/stdlib/universe/highestcurrent/)
-   [highestMax()](/flux/v0/stdlib/universe/highestmax/)
-   [last()](/flux/v0/stdlib/universe/last/)
-   [limit()](/flux/v0/stdlib/universe/limit/)
-   [lowestAverage()](/flux/v0/stdlib/universe/lowestaverage/)
-   [lowestCurrent()](/flux/v0/stdlib/universe/lowestcurrent/)
-   [lowestMin()](/flux/v0/stdlib/universe/lowestmin/)
-   [max()](/flux/v0/stdlib/universe/max/)
-   [median()](/flux/v0/stdlib/universe/median/)
-   [min()](/flux/v0/stdlib/universe/min/)
-   [quantile()](/flux/v0/stdlib/universe/quantile/)
-   [sample()](/flux/v0/stdlib/universe/sample/)
-   [top()](/flux/v0/stdlib/universe/top/)
-   [unique()](/flux/v0/stdlib/universe/unique/)

##### Selectors and aggregates

The following functions can be used as both selectors or aggregates, but they are categorized as [aggregate functions](#aggregates) in this documentation:

-   [median()](/flux/v0/stdlib/universe/median)
-   [quantile()](/flux/v0/stdlib/universe/quantile)

### Dynamic queries

Flux dynamic query functions extract a table from a stream of tables and access its columns and records. For recommended usage, see [Extract scalar values](/influxdb/cloud/query-data/flux/scalar-values/).

-   [findColumn()](/flux/v0/stdlib/universe/findcolumn/)
-   [findRecord()](/flux/v0/stdlib/universe/findrecord/)
-   [getColumn()](/flux/v0/stdlib/universe/getcolumn/)
-   [getRecord()](/flux/v0/stdlib/universe/getrecord/)
-   [tableFind()](/flux/v0/stdlib/universe/tablefind/)

## Function categories

The following categories represent high-level function behaviors.

-   [Filters](#filters)
-   [Type conversions](#type-conversions)
-   [Tests](#tests)
-   [Date/time](#datetime)
-   [Metadata](#metadata)
-   [Notification endpoints](#notification-endpoints)
-   [Geotemporal](#geotemporal)

### Filters

Filter functions iterate over and evaluate each input row to see if it matches specified conditions. Rows that do not match the specified conditions are dropped from the output. The following filter functions are available:

-   [filter()](/flux/v0/stdlib/universe/filter/)
-   [geo.filterRows()](/flux/v0/stdlib/experimental/geo/filterrows/)
-   [geo.gridFilter()](/flux/v0/stdlib/experimental/geo/gridfilter/)
-   [geo.strictFilter()](/flux/v0/stdlib/experimental/geo/strictfilter/)
-   [hourSelection()](/flux/v0/stdlib/universe/hourselection/)
-   [query.filterFields()](/flux/v0/stdlib/experimental/query/filterfields/)
-   [query.filterMeasurement()](/flux/v0/stdlib/experimental/query/filtermeasurement/)
-   [query.fromRange()](/flux/v0/stdlib/experimental/query/fromrange/)
-   [range()](/flux/v0/stdlib/universe/range/)

### Type conversions

Flux type conversion functions convert scalar values or columns to a specific data type. The following type conversion functions are available:

-   [array.toBool()](/flux/v0/stdlib/experimental/array/tobool/)
-   [array.toDuration()](/flux/v0/stdlib/experimental/array/toduration/)
-   [array.toFloat()](/flux/v0/stdlib/experimental/array/tofloat/)
-   [array.toInt()](/flux/v0/stdlib/experimental/array/toint/)
-   [array.toString()](/flux/v0/stdlib/experimental/array/tostring/)
-   [array.toTime()](/flux/v0/stdlib/experimental/array/totime/)
-   [array.toUInt()](/flux/v0/stdlib/experimental/array/touint/)
-   [bool()](/flux/v0/stdlib/universe/bool/)
-   [bytes()](/flux/v0/stdlib/universe/bytes/)
-   [duration()](/flux/v0/stdlib/universe/duration/)
-   [dynamic.asArray()](/flux/v0/stdlib/experimental/dynamic/asarray/)
-   [dynamic.dynamic()](/flux/v0/stdlib/experimental/dynamic/dynamic/)
-   [dynamic.jsonEncode()](/flux/v0/stdlib/experimental/dynamic/jsonencode/)
-   [dynamic.jsonParse()](/flux/v0/stdlib/experimental/dynamic/jsonparse/)
-   [float()](/flux/v0/stdlib/universe/float/)
-   [int()](/flux/v0/stdlib/universe/int/)
-   [iox.sqlInterval()](/flux/v0/stdlib/experimental/iox/sqlinterval/)
-   [json.encode()](/flux/v0/stdlib/json/encode/)
-   [json.parse()](/flux/v0/stdlib/experimental/json/parse/)
-   [regexp.compile()](/flux/v0/stdlib/regexp/compile/)
-   [string()](/flux/v0/stdlib/universe/string/)
-   [time()](/flux/v0/stdlib/universe/time/)
-   [toBool()](/flux/v0/stdlib/universe/tobool/)
-   [toFloat()](/flux/v0/stdlib/universe/tofloat/)
-   [toInt()](/flux/v0/stdlib/universe/toint/)
-   [toString()](/flux/v0/stdlib/universe/tostring/)
-   [toTime()](/flux/v0/stdlib/universe/totime/)
-   [toUInt()](/flux/v0/stdlib/universe/touint/)
-   [uint()](/flux/v0/stdlib/universe/uint/)

### Tests

Flux testing functions test various aspects of data. Tests return either `true` or `false`, a transformed stream of tables, or, upon failure, an error. The following testing functions are available:

-   [dynamic.isType()](/flux/v0/stdlib/experimental/dynamic/istype/)
-   [testing.assertEmpty()](/flux/v0/stdlib/testing/assertempty/)
-   [testing.assertEquals()](/flux/v0/stdlib/testing/assertequals/)
-   [testing.assertEqualValues()](/flux/v0/stdlib/testing/assertequalvalues/)
-   [testing.assertMatches()](/flux/v0/stdlib/internal/testing/assertmatches/)
-   [testing.diff()](/flux/v0/stdlib/testing/diff/)
-   [testing.shouldError()](/flux/v0/stdlib/testing/shoulderror/)
-   [testing.shouldErrorWithCode()](/flux/v0/stdlib/internal/testing/shoulderrorwithcode/)
-   [types.isNumeric()](/flux/v0/stdlib/types/isnumeric/)
-   [types.isType()](/flux/v0/stdlib/types/istype/)

### Date/time

Flux date/time functions return or operate on [time](/flux/v0/data-types/basic/time/) or [duration](/flux/v0/spec/types/#duration-types) values. The following data/time functions are available:

-   [boundaries.friday()](/flux/v0/stdlib/date/boundaries/friday/) *– (deprecated)*
-   [boundaries.friday()](/flux/v0/stdlib/experimental/date/boundaries/friday/)
-   [boundaries.monday()](/flux/v0/stdlib/date/boundaries/monday/) *– (deprecated)*
-   [boundaries.monday()](/flux/v0/stdlib/experimental/date/boundaries/monday/)
-   [boundaries.month()](/flux/v0/stdlib/date/boundaries/month/) *– (deprecated)*
-   [boundaries.month()](/flux/v0/stdlib/experimental/date/boundaries/month/)
-   [boundaries.saturday()](/flux/v0/stdlib/date/boundaries/saturday/) *– (deprecated)*
-   [boundaries.saturday()](/flux/v0/stdlib/experimental/date/boundaries/saturday/)
-   [boundaries.sunday()](/flux/v0/stdlib/date/boundaries/sunday/) *– (deprecated)*
-   [boundaries.sunday()](/flux/v0/stdlib/experimental/date/boundaries/sunday/)
-   [boundaries.thursday()](/flux/v0/stdlib/date/boundaries/thursday/) *– (deprecated)*
-   [boundaries.thursday()](/flux/v0/stdlib/experimental/date/boundaries/thursday/)
-   [boundaries.tuesday()](/flux/v0/stdlib/date/boundaries/tuesday/) *– (deprecated)*
-   [boundaries.tuesday()](/flux/v0/stdlib/experimental/date/boundaries/tuesday/)
-   [boundaries.wednesday()](/flux/v0/stdlib/date/boundaries/wednesday/) *– (deprecated)*
-   [boundaries.wednesday()](/flux/v0/stdlib/experimental/date/boundaries/wednesday/)
-   [boundaries.week()](/flux/v0/stdlib/date/boundaries/week/) *– (deprecated)*
-   [boundaries.week()](/flux/v0/stdlib/experimental/date/boundaries/week/)
-   [boundaries.yesterday()](/flux/v0/stdlib/date/boundaries/yesterday/) *– (deprecated)*
-   [boundaries.yesterday()](/flux/v0/stdlib/experimental/date/boundaries/yesterday/)
-   [date.add()](/flux/v0/stdlib/date/add/)
-   [date.hour()](/flux/v0/stdlib/date/hour/)
-   [date.microsecond()](/flux/v0/stdlib/date/microsecond/)
-   [date.millisecond()](/flux/v0/stdlib/date/millisecond/)
-   [date.minute()](/flux/v0/stdlib/date/minute/)
-   [date.month()](/flux/v0/stdlib/date/month/)
-   [date.monthDay()](/flux/v0/stdlib/date/monthday/)
-   [date.nanosecond()](/flux/v0/stdlib/date/nanosecond/)
-   [date.quarter()](/flux/v0/stdlib/date/quarter/)
-   [date.scale()](/flux/v0/stdlib/date/scale/)
-   [date.second()](/flux/v0/stdlib/date/second/)
-   [date.sub()](/flux/v0/stdlib/date/sub/)
-   [date.time()](/flux/v0/stdlib/date/time/)
-   [date.truncate()](/flux/v0/stdlib/date/truncate/)
-   [date.week()](/flux/v0/stdlib/date/week/)
-   [date.weekDay()](/flux/v0/stdlib/date/weekday/)
-   [date.year()](/flux/v0/stdlib/date/year/)
-   [date.yearDay()](/flux/v0/stdlib/date/yearday/)
-   [experimental.addDuration()](/flux/v0/stdlib/experimental/addduration/) *– (deprecated)*
-   [experimental.alignTime()](/flux/v0/stdlib/experimental/aligntime/)
-   [experimental.subDuration()](/flux/v0/stdlib/experimental/subduration/) *– (deprecated)*
-   [experimental.window()](/flux/v0/stdlib/experimental/window/)
-   [hourSelection()](/flux/v0/stdlib/universe/hourselection/)
-   [now()](/flux/v0/stdlib/universe/now/)
-   [system.time()](/flux/v0/stdlib/system/time/)
-   [timeShift()](/flux/v0/stdlib/universe/timeshift/)
-   [timezone.fixed()](/flux/v0/stdlib/timezone/fixed/)
-   [timezone.location()](/flux/v0/stdlib/timezone/location/)
-   [today()](/flux/v0/stdlib/universe/today/)
-   [truncateTimeColumn()](/flux/v0/stdlib/universe/truncatetimecolumn/)

### Metadata

Flux metadata functions return metadata from the input stream or from an underlying data source. The following metadata functions are available:

-   [buckets()](/flux/v0/stdlib/influxdata/influxdb/buckets/)
-   [influxdb.cardinality()](/flux/v0/stdlib/influxdata/influxdb/cardinality/)
-   [schema.fieldKeys()](/flux/v0/stdlib/influxdata/influxdb/schema/fieldkeys/)
-   [schema.measurementFieldKeys()](/flux/v0/stdlib/influxdata/influxdb/schema/measurementfieldkeys/)
-   [schema.measurements()](/flux/v0/stdlib/influxdata/influxdb/schema/measurements/)
-   [schema.measurementTagKeys()](/flux/v0/stdlib/influxdata/influxdb/schema/measurementtagkeys/)
-   [schema.measurementTagValues()](/flux/v0/stdlib/influxdata/influxdb/schema/measurementtagvalues/)
-   [schema.tagKeys()](/flux/v0/stdlib/influxdata/influxdb/schema/tagkeys/)
-   [schema.tagValues()](/flux/v0/stdlib/influxdata/influxdb/schema/tagvalues/)
-   [v1.databases()](/flux/v0/stdlib/influxdata/influxdb/v1/databases/)
-   [v1.fieldKeys()](/flux/v0/stdlib/influxdata/influxdb/v1/fieldkeys/) *– (deprecated)*
-   [v1.measurementFieldKeys()](/flux/v0/stdlib/influxdata/influxdb/v1/measurementfieldkeys/) *– (deprecated)*
-   [v1.measurements()](/flux/v0/stdlib/influxdata/influxdb/v1/measurements/) *– (deprecated)*
-   [v1.measurementTagKeys()](/flux/v0/stdlib/influxdata/influxdb/v1/measurementtagkeys/) *– (deprecated)*
-   [v1.measurementTagValues()](/flux/v0/stdlib/influxdata/influxdb/v1/measurementtagvalues/) *– (deprecated)*
-   [v1.tagKeys()](/flux/v0/stdlib/influxdata/influxdb/v1/tagkeys/) *– (deprecated)*
-   [v1.tagValues()](/flux/v0/stdlib/influxdata/influxdb/v1/tagvalues/) *– (deprecated)*

### Notification endpoints

Flux notification endpoint functions send notifications to external endpoints or services. The following notification endpoint functions are available:

-   [alerta.endpoint()](/flux/v0/stdlib/contrib/bonitoo-io/alerta/endpoint/)
-   [bigpanda.endpoint()](/flux/v0/stdlib/contrib/rhajek/bigpanda/endpoint/)
-   [discord.endpoint()](/flux/v0/stdlib/contrib/chobbs/discord/endpoint/)
-   [http.endpoint()](/flux/v0/stdlib/http/endpoint/)
-   [opsgenie.endpoint()](/flux/v0/stdlib/contrib/sranka/opsgenie/endpoint/)
-   [pagerduty.endpoint()](/flux/v0/stdlib/pagerduty/endpoint/)
-   [pushbullet.endpoint()](/flux/v0/stdlib/pushbullet/endpoint/)
-   [sensu.endpoint()](/flux/v0/stdlib/contrib/sranka/sensu/endpoint/)
-   [servicenow.endpoint()](/flux/v0/stdlib/contrib/bonitoo-io/servicenow/endpoint/)
-   [slack.endpoint()](/flux/v0/stdlib/slack/endpoint/)
-   [teams.endpoint()](/flux/v0/stdlib/contrib/sranka/teams/endpoint/)
-   [telegram.endpoint()](/flux/v0/stdlib/contrib/sranka/telegram/endpoint/)
-   [victorops.endpoint()](/flux/v0/stdlib/contrib/bonitoo-io/victorops/endpoint/)
-   [webexteams.endpoint()](/flux/v0/stdlib/contrib/sranka/webexteams/endpoint/)
-   [zenoss.endpoint()](/flux/v0/stdlib/contrib/bonitoo-io/zenoss/endpoint/)

### Geotemporal

Flux geotemporal functions are designed to work with geotemporal data (geographic location over time). The following geotemporal functions are available:

-   [geo.asTracks()](/flux/v0/stdlib/experimental/geo/astracks/)
-   [geo.filterRows()](/flux/v0/stdlib/experimental/geo/filterrows/)
-   [geo.getGrid()](/flux/v0/stdlib/experimental/geo/getgrid/)
-   [geo.getLevel()](/flux/v0/stdlib/experimental/geo/getlevel/)
-   [geo.gridFilter()](/flux/v0/stdlib/experimental/geo/gridfilter/)
-   [geo.groupByArea()](/flux/v0/stdlib/experimental/geo/groupbyarea/)
-   [geo.s2CellIDToken()](/flux/v0/stdlib/experimental/geo/s2cellidtoken/)
-   [geo.s2CellLatLon()](/flux/v0/stdlib/experimental/geo/s2celllatlon/)
-   [geo.shapeData()](/flux/v0/stdlib/experimental/geo/shapedata/)
-   [geo.ST\_Contains()](/flux/v0/stdlib/experimental/geo/st_contains/)
-   [geo.ST\_Distance()](/flux/v0/stdlib/experimental/geo/st_distance/)
-   [geo.ST\_DWithin()](/flux/v0/stdlib/experimental/geo/st_dwithin/)
-   [geo.ST\_Intersects()](/flux/v0/stdlib/experimental/geo/st_intersects/)
-   [geo.ST\_Length()](/flux/v0/stdlib/experimental/geo/st_length/)
-   [geo.ST\_LineString()](/flux/v0/stdlib/experimental/geo/st_linestring/)
-   [geo.stContains()](/flux/v0/stdlib/experimental/geo/stcontains/)
-   [geo.stDistance()](/flux/v0/stdlib/experimental/geo/stdistance/)
-   [geo.stLength()](/flux/v0/stdlib/experimental/geo/stlength/)
-   [geo.strictFilter()](/flux/v0/stdlib/experimental/geo/strictfilter/)
-   [geo.toRows()](/flux/v0/stdlib/experimental/geo/torows/)
-   [geo.totalDistance()](/flux/v0/stdlib/experimental/geo/totaldistance/)

#### Related

-   [Flux standard library](/flux/v0/stdlib/)


---

## Function type signatures

A **function type signature** describes a function’s input parameters and types, and the function’s output type. Use type signatures to identify data types expected by function parameters and to understand a function’s expected output.

-   [Function type signature structure](#function-type-signature-structure)
    -   [Parameter notation](#parameter-notation)
-   [Type variables](#type-variables)
-   [Type notation](#type-notation)
    -   [Stream types](#stream-types)
    -   [Basic types](#basic-types)
    -   [Composite types](#composite-types)
-   [Type constraints](#type-constraints)
-   [Example function type signatures](#example-function-type-signatures)

## Function type signature structure

```js
(parameter: type) => output-type
```

### Parameter notation

Parameter notation indicates specific behaviors of function parameters.

```js
?  // Optional parameter
<- // Pipe receive – indicates the parameter that, by default, represents
   // the piped-forward value

```

## Type variables

Flux type signatures use **type variables** to represent unique types in the signature. A type variable is [polymorphic](/flux/v0/spec/types/#polymorphism), meaning it can be one of many types, and may be constrained by [type constraints](#type-constraints).

Type variables use the following identifier patterns:

```js
A
B
C
t11
// etc.

```

## Type notation

-   [Stream types](#stream-types)
-   [Basic types](#basic-types)
-   [Composite types](#composite-types)

### Stream types

Type signatures identify stream types ([streams of tables](/flux/v0/get-started/data-model/#stream-of-tables)) using the `stream[A]` syntax where `A` is a unique [type variable](#type-variables). Stream types may included specific column names and column types.

```js
// Stream of tables
stream[A]

// Stream of tables with specific columns, but inferred column types.
stream[{col1: A, col2: B}]

// Stream of tables additional or required "count" column with an
// explicit integer type.
stream[{A with count: int}]
```

### Basic types

Type signatures identify [basic types](/flux/v0/data-types/basic/) with the following type identifiers:

```js
bool     // boolean type
bytes    // bytes type
duration // duration type
float    // float type
int      // integer type
regexp   // regular expression type
string   // string type
time     // time type
uint     // unsigned integer type

```

### Composite types

Type signatures identify Flux [composite types](/flux/v0/data-types/composite/) with the following syntaxes:

```js
[A]             // array type
[B: A]          // dictionary type
(param: A) => B // function type
{_value: int}   // record type

```

## Type constraints

Some function parameters are “polymorphic” and can support multiple data types. Polymorphic parameters are bound by **type constraints**, which define what types can be used. Type signatures indicate type constraints for specific values using the `where A: Constraint` syntax.

For example, the following type signature describes a function that takes a single parameter, `v` and returns and integer. `v` can be any type that satisfies the Timeable constraint (duration or time).

```js
(v: A) => int where A: Timeable
```

For more information about the different type constraints and the types each supports, see [Type constraints](/flux/v0/spec/types/#type-constraints).

## Example function type signatures

-   [Function without parameters](#function-without-parameters)
-   [Function with parameters](#function-with-parameters)
-   [Pass-through transformation](#pass-through-transformation)
-   [Basic transformation](#basic-transformation)
-   [Transformation that adds a column with an explicit type](#transformation-that-adds-a-column-with-an-explicit-type)

#### Function without parameters

The following type signature describes a function that:

-   Has no parameters
-   Returns a time value

```js
() => time
```

#### Function with parameters

The following type signature describes a function that:

-   Has two parameters of type `A`:
    -   multiplier *(Optional)*
    -   v (Required)
-   Returns a value the same type as the two input parameters

```js
(?multiplier: A, v: A) => A
```

#### Pass-through transformation

The following type signature describes a [transformation](/flux/v0/function-types/#transformations) that:

-   Takes a stream of tables of type `A` as piped-forward input
-   Returns the input stream of tables with an unmodified type

```js
(<-tables: stream[A]) => stream[A]
```

#### Basic transformation

The following type signature describes a [transformation](/flux/v0/function-types/#transformations) that:

-   Takes a stream of tables of type `A` as piped-forward input
-   Has an `fn` parameter with a function type
    -   `fn` uses type `A` as input and returns type `B`
-   Returns a new, modified stream of tables of type `B`

```js
(<-tables: stream[A], fn: (r: A) => B,) => stream[B]
```

#### Transformation that adds a column with an explicit type

The following type signature describes a [transformation](/flux/v0/function-types/#transformations) that:

-   Takes a stream of tables of type `A` as piped-forward input
-   Has a required **tag** parameter of type `B`
    -   The `B` type is constrained by the Stringable constraint
-   Returns a new, modified stream of tables of type `A` that includes a **tag** column with string values

```js
(<-tables: stream[A], tag: B) => stream[{A with tag: string}] where B: Stringable
```

#### Related

-   [Work with Flux data types](/flux/v0/data-types/)
-   [Type constraints](/flux/v0/spec/types/#type-constraints)


---

## Define custom functions

Flux’s functional syntax lets you define custom functions. Learn the basics of creating your own functions.

###### On this page:

-   [Function definition syntax](#function-definition-syntax)
-   [Custom function examples](#custom-function-examples)
-   [Create a custom transformation](#create-a-custom-transformation)
    -   [Custom transformation examples](#custom-transformation-examples)
-   [Define functions with scoped variables](#define-functions-with-scoped-variables)
    -   [Example functions with scoped variables](#example-functions-with-scoped-variables)

## Function definition syntax

The basic syntax for defining functions in Flux is as follows:

```js
// Basic function definition syntax
functionName = (functionParameters) => functionBody
```

-   **functionName**: Name to use to execute the function.
-   **functionParameters**: Comma-separated list of parameters passed into the function.
-   **functionBody**: Operations on function parameters.

### Define parameter defaults

Use the `=` assignment operator to assign a default value to function parameters in your function definition:

```js
functionName = (param1=defaultVal1, param2=defaultVal2) => functionBody
```

Defaults are overridden by explicitly defining the parameter in the function call. Parameters without default values are considered **required parameters**.

## Custom function examples

[](#square-a-number)

Square a number

```js
square = (n) => n * n

square(n:3)
// Returns 9

```

[](#multiple-two-values)

Multiple two values

```js
multiply = (x, y) => x * y

multiply(x: 2, y: 15)
// Returns 30

```

[](#calculate-n-to-the-p-power-with-default-parameters)

Calculate n to the p power (with default parameters)

```js
pow = (n, p=10) => n ^ p

pow(n: 2)
// Returns 1024

```

## Create a custom transformation

A [transformation](/flux/v0/function-types/#transformations) is a function that takes a [stream of tables](/flux/v0/get-started/data-model/#stream-of-tables) as input, operates on the input, and then outputs a new stream of tables.

The [pipe-forward operator](/flux/v0/get-started/syntax-basics/#pipe-forward-operator) (`|>`) pipes data from the previous identifier or function forward into a transformation. To use piped-forward data, assign a function parameter to the [pipe-receive operator](/flux/v0/spec/operators/#function-operators) (`<-`).

In the following example, the function `x()` receives piped-forwarded data and assigns it to the `t` parameter. In the function body, `t` is piped forward into other operations to generate output.

```js
x = (t=<-) => t |> //...

```

### Custom transformation examples

[](#multiply-values-by-x)

Multiply values by x

#### Multiply values by x

The following example defines a `multByX` function that multiplies the `_value` column of each input row by the `x` parameter. The example uses the [`map()` function](/flux/v0/stdlib/universe/map/) to iterate over each row, modify the `_value`, and then return the updated row.

##### Function definition

```js
multByX = (tables=<-, x) =>
    tables
        |> map(fn: (r) => ({r with _value: r._value * x}))
```

##### Example usage

```js
data
    |> multByX(x: 2.0)
```

###### Given the following input data:

| srcID | _field | _value |
| --- | --- | --- |
| t1a | foo | 1.2 |
| t1a | foo | 3.4 |
| t1a | foo | 5.6 |

| srcID | _field | _value |
| --- | --- | --- |
| t2b | foo | 0.8 |
| t2b | foo | 1.9 |
| t2b | foo | 2.7 |

###### The example above returns:

| srcID | _field | _value |
| --- | --- | --- |
| t1a | foo | 2.4 |
| t1a | foo | 6.8 |
| t1a | foo | 11.2 |

| srcID | _field | _value |
| --- | --- | --- |
| t2b | foo | 1.6 |
| t2b | foo | 3.8 |
| t2b | foo | 5.4 |

[](#calculate-speed)

Calculate speed

#### Calculate speed

The following example defines a `speed` function that calculates speed using an `elapsed` and `distance` column in input tables. The example uses the [`map()` function](/flux/v0/stdlib/universe/map/) to iterate over each row, calculate the speed per specified unit of distance, and then return the updated row with a new `speed` column.

##### Function definition

```js
speed = (tables=<-, unit="m") =>
    tables
        |> map(
            fn: (r) => {
                elapsedHours = float(v: int(v: duration(v: r.elapsed))) / float(v: int(v: 1h))
                distance = float(v: r.distance)
                speed = distance / elapsedHours

                return {r with speed: "${speed} ${unit}ph"}
            },
        )
```

##### Example usage

```js
data
    |> speed()
```

##### Given the following input data:

| id | elapsed | distance |
| --- | --- | --- |
| t1 | 1h15m | 101 |
| t2 | 1h32m | 138 |
| t3 | 56m | 112 |

##### The example above returns:

| id | elapsed | distance | speed |
| --- | --- | --- | --- |
| t1 | 1h15m | 101 | 88.8 mph |
| t2 | 1h32m | 138 | 90 mph |
| t3 | 56m | 112 | 120 mph |

## Define functions with scoped variables

To create custom functions with variables scoped to the function,

1. Enclose your [function body](#function-definition-syntax) in a [block (`{}`)](/flux/v0/spec/blocks/).
2. Use a `return` statement to return a specific variable.

```js
functionName = (param) => {
    exampleVar = "foo"

    return exampleVar
}
```

### Example functions with scoped variables

[](#return-an-alert-level-based-on-a-value)

Return an alert level based on a value

#### Return an alert level based on a value

The following function uses conditional logic to return an alert level based on a numeric input value:

```js
alertLevel = (v) => {
    level =
        if float(v: v) >= 90.0 then
            "crit"
        else if float(v: v) >= 80.0 then
            "warn"
        else if float(v: v) >= 65.0 then
            "info"
        else
            "ok"

    return level
}

alertLevel(v: 87.3)
// Returns "warn"

```

[](#convert-a-hex-color-code-to-a-name)

Convert a HEX color code to a name

#### Convert a HEX color code to a name

The following function converts a hexadecimal (HEX) color code to the equivalent HTML color name. The functions uses the [Flux dictionary package](/flux/v0/stdlib/dict/) to create a dictionary of HEX codes and their corresponding names.

```js
import "dict"

hexName = (hex) => {
    hexNames =
        dict.fromList(
            pairs: [
                {key: "#00ffff", value: "Aqua"},
                {key: "#000000", value: "Black"},
                {key: "#0000ff", value: "Blue"},
                {key: "#ff00ff", value: "Fuchsia"},
                {key: "#808080", value: "Gray"},
                {key: "#008000", value: "Green"},
                {key: "#00ff00", value: "Lime"},
                {key: "#800000", value: "Maroon"},
                {key: "#000080", value: "Navy"},
                {key: "#808000", value: "Olive"},
                {key: "#800080", value: "Purple"},
                {key: "#ff0000", value: "Red"},
                {key: "#c0c0c0", value: "Silver"},
                {key: "#008080", value: "Teal"},
                {key: "#ffffff", value: "White"},
                {key: "#ffff00", value: "Yellow"},
            ],
        )
    name = dict.get(dict: hexNames, key: hex, default: "No known name")

    return name
}

hexName(hex: "#000000")
// Returns "Black"

hexName(hex: "#8b8b8b")
// Returns "No known name"

```

#### Related

-   [Work with functions](/flux/v0/data-types/composite/function/)


---

## Work with Flux data types

A Flux **data type** defines the set of possible values and operations. Flux is **statically typed**, meaning data types are never explicitly declared as part of the Flux syntax (except as part of a [builtin statement](/flux/v0/spec/system-built-ins/)) and types are inferred from how a variable is used.

Flux data types are organized into the following:

## [Basic types](/flux/v0/data-types/basic/)

All Flux data types are constructed from **basic types**: boolean, bytes, duration, string, time, float, integer, uintegers, and null.

## [Composite types](/flux/v0/data-types/composite/)

Flux **composite types** are types constructed from basic types. Flux supports the following composite types: record, array, dictionary, function.

## [Dynamic types](/flux/v0/data-types/dynamic/)

A **dynamic** type is a wrapper for data whose type is not known until runtime. Dynamic types help when working with data from external sources (like JSON) that support types that do not have an equivalent Flux type.

