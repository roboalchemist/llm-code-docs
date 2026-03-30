# Source: https://buildkite.com/docs/test-engine/test-collection/importing-json.md

# Importing JSON

If a test collector is not available for your test framework, you can upload tests results directly to the Test Engine API or [write your own test collector](/docs/test-engine/test-collection/your-own-collectors).
You can upload JSON-formatted test results (described in this page) or [JUnit XML](/docs/test-engine/test-collection/importing-junit-xml).

## How to import JSON in Buildkite

It's possible to import JSON (or [JUnit](/docs/test-engine/test-collection/importing-junit-xml#how-to-import-junit-xml-in-buildkite) files) to Buildkite Test Engine with or without the help of a plugin.

### Using a plugin

To import [JSON-formatted test results](#json-test-results-data-reference) to Test Engine using [Test Collector plugin](https://github.com/buildkite-plugins/test-collector-buildkite-plugin) from a build step:

```yml
steps:
  - label: "🔨 Test"
    command: "make test"
    plugins:
      - test-collector#v1.0.0:
          files: "test-data-*.json"
          format: "json"
```

{: codeblock-file="pipeline.yml"}

See more configuration information in the [Test Collector plugin README](https://github.com/buildkite-plugins/test-collector-buildkite-plugin).

Using the plugin is the recommended way as it allows for a better debugging process in case of an issue.

### Without a plugin

If for some reason you cannot or do not want to use the [Test Collector plugin](https://github.com/buildkite-plugins/test-collector-buildkite-plugin), or if you are looking to implement your own integration, another approach is possible.

To import [JSON-formatted test results](#json-test-results-data-reference) in Buildkite, make a `POST` request to `https://analytics-api.buildkite.com/v1/uploads` with a `multipart/form-data`.

For example, to import the contents of a [JSON-formatted test results](#json-test-results-data-reference) (`test-results.json`):

1. Securely [set the Test Engine token environment variable](/docs/pipelines/security/secrets/managing) (`BUILDKITE_ANALYTICS_TOKEN`).

2. Run the following `curl` command:

    ```sh
    curl \
      -X POST \
      -H "Authorization: Token token=\"$BUILDKITE_ANALYTICS_TOKEN\"" \
      -F "data=@test-results.json" \
      -F "format=json" \
      -F "run_env[CI]=buildkite" \
      -F "run_env[key]=$BUILDKITE_BUILD_ID" \
      -F "run_env[url]=$BUILDKITE_BUILD_URL" \
      -F "run_env[branch]=$BUILDKITE_BRANCH" \
      -F "run_env[commit_sha]=$BUILDKITE_COMMIT" \
      -F "run_env[number]=$BUILDKITE_BUILD_NUMBER" \
      -F "run_env[job_id]=$BUILDKITE_JOB_ID" \
      -F "run_env[message]=$BUILDKITE_MESSAGE" \
      https://analytics-api.buildkite.com/v1/uploads
    ```

To learn more about passing through environment variables to `run_env`-prefixed fields, see the [Buildkite](/docs/test-engine/test-collection/ci-environments#buildkite) or [Other CI providers](/docs/test-engine/test-collection/ci-environments#other-ci-providers) (including manually) on the [CI environments](/docs/test-engine/test-collection/ci-environments) page.

A single file can have a maximum of 5000 test results, and if that limit is exceeded then the upload request will fail. To upload more than 5000 test results for a single run upload multiple smaller files with the same `run_env[key]`.

#### Upload level custom tags

You can configure custom tags on upload level, they will be applied server-side to every execution therein.
This is an efficient way to tag every execution with values that don't vary within one configuration, e.g. cloud environment details, language/framework versions.

```sh
curl \
  -X POST \
  ... \
  -F "tags[team]=frontend" \
  -F "tags[feature]=alchemy" \
  https://analytics-api.buildkite.com/v1/uploads
```

Upload-level tags may be overwritten by execution-level tags, check [Execution level custom tags](/docs/test-engine/test-collection/importing-json#json-test-results-data-reference-execution-level-custom-tags).

## How to import JSON in CircleCI

To import [JSON-formatted test results](#json-test-results-data-reference), make a `POST` request to `https://analytics-api.buildkite.com/v1/uploads` with a `multipart/form-data` body, including as many of the following fields as possible in the request body:

For example, to import the contents of a `test-results.json` file in a CircleCI pipeline:

1. Securely [set the Test Engine token environment variable](/docs/pipelines/security/secrets/managing) (`BUILDKITE_ANALYTICS_TOKEN`).

2. Run the following `curl` command:

    ```sh
    curl \
    -X POST \
    -H "Authorization: Token token=\"$BUILDKITE_ANALYTICS_TOKEN\"" \
    -F "data=@test-results.json" \
    -F "format=json" \
    -F "run_env[CI]=circleci" \
    -F "run_env[key]=$CIRCLE_WORKFLOW_ID-$CIRCLE_BUILD_NUM" \
    -F "run_env[number]=$CIRCLE_BUILD_NUM" \
    -F "run_env[branch]=$CIRCLE_BRANCH" \
    -F "run_env[commit_sha]=$CIRCLE_SHA1" \
    -F "run_env[url]=$CIRCLE_BUILD_URL" \
    https://analytics-api.buildkite.com/v1/uploads
    ```

To learn more about passing through environment variables to `run_env`-prefixed fields, see [CI environments > CircleCI](/docs/test-engine/test-collection/ci-environments#circleci) page section.

A single file can have a maximum of 5000 test results, and if that limit is exceeded then the upload request will fail. To upload more than 5000 test results for a single run upload multiple smaller files with the same `run_env[key]`.

## How to import JSON in GitHub Actions

To import [JSON-formatted test results](#json-test-results-data-reference), make a `POST` request to `https://analytics-api.buildkite.com/v1/uploads` with a `multipart/form-data` body, including as many of the following fields as possible in the request body:

For example, to import the contents of a `test-results.json` file in a GitHub Actions pipeline run:

1. Securely [set the Test Engine token environment variable](/docs/pipelines/security/secrets/managing) (`BUILDKITE_ANALYTICS_TOKEN`).

2. Run the following `curl` command:

    ```sh
    curl \
    -X POST \
    -H "Authorization: Token token=\"$BUILDKITE_ANALYTICS_TOKEN\"" \
    -F "data=@test-results.json" \
    -F "format=json" \
    -F "run_env[CI]=github_actions" \
    -F "run_env[key]=$GITHUB_ACTION-$GITHUB_RUN_NUMBER-$GITHUB_RUN_ATTEMPT" \
    -F "run_env[number]=$GITHUB_RUN_NUMBER" \
    -F "run_env[branch]=$GITHUB_REF" \
    -F "run_env[commit_sha]=$GITHUB_SHA" \
    -F "run_env[url]=https://github.com/$GITHUB_REPOSITORY/actions/runs/$GITHUB_RUN_ID" \
    https://analytics-api.buildkite.com/v1/uploads
    ```

To learn more about passing through environment variables to `run_env`-prefixed fields, see [CI environments > GitHub Actions](/docs/test-engine/test-collection/ci-environments#github-actions) page section.

A single file can have a maximum of 5000 test results, and if that limit is exceeded then the upload request will fail. To upload more than 5000 test results for a single run upload multiple smaller files with the same `run_env[key]`.

## JSON test results data reference

JSON test results data is made up of an array of one or more "test result" objects.
A test result object contains an overall result and metadata.
It also contains a `history` object, which is a summary of the duration of the test run.
Within the history object, detailed `span` objects record the highest resolution details of the test run.

Schematically, the JSON test results data is like this:

- [Test results](#json-test-results-data-reference-test-result-objects)
  - [History](#json-test-results-data-reference-history-objects)
    - [Spans](#json-test-results-data-reference-span-objects)
      - [Detail](#json-test-results-data-reference-detail-objects)

Or in a simplified code view:

```js
[
  {
    /* Test result object */
    "history": {
      /* history object */
      "children": [
        /* span objects */
      ]
    }
  },
  { /* Test result object */ },
]
```

### Test result objects

A test result represents a single test run.

<table class="responsive-table">
  <thead>
    <tr>
      <th>Key</th>
      <th>Type</th>
      <th>Description</th>
      <th>Examples</th>
    </tr>
  </thead>
  <tbody>
          <tr>
        <td><code>id</code> (required)</td>
        <td>UUIDv4 string </td>
        <td>
          <p>A unique identifier for this test result. If a test execution with this UUID already exists in the Test Engine database, this result is ignored.</p>

        </td>
        <td>
          <code><p>1b70486f-ca5f-4e6d-beb8-6347b2e49278</p>
</code>
        </td>
      </tr>
          <tr>
        <td><code>scope</code> </td>
        <td>string </td>
        <td>
          <p>A group or topic for the test</p>

        </td>
        <td>
          <code><p>Student.isEnrolled()</p>
</code>
        </td>
      </tr>
          <tr>
        <td><code>name</code> (required)</td>
        <td>string </td>
        <td>
          <p>A name or description for the test</p>

        </td>
        <td>
          <code><p>Manager.isEnrolled() returns_boolean</p>
</code>
        </td>
      </tr>
          <tr>
        <td><code>location</code> </td>
        <td>string </td>
        <td>
          <p>The file and line number where the test originates, separated by a colon (<code>:</code>)</p>

        </td>
        <td>
          <code><p>./tests/Manager/isEnrolled.js:32</p>
</code>
        </td>
      </tr>
          <tr>
        <td><code>file_name</code> </td>
        <td>string </td>
        <td>
          <p>The file where the test originates</p>

        </td>
        <td>
          <code><p>./tests/Manager/isEnrolled.js</p>
</code>
        </td>
      </tr>
          <tr>
        <td><code>result</code> </td>
        <td>string (<code>passed</code>, <code>failed</code>, <code>skipped</code> or <code>unknown</code>)</td>
        <td>
          <p>The outcome of the test</p>

        </td>
        <td>
          <code><p>failed</p>
</code>
        </td>
      </tr>
          <tr>
        <td><code>failure_reason</code> </td>
        <td>string </td>
        <td>
          <p>If applicable, a short summary of why the test failed</p>

        </td>
        <td>
          <code><p>Expected Boolean, got Object</p>
</code>
        </td>
      </tr>
          <tr>
        <td><code>failure_expanded</code> </td>
        <td>array of hashes </td>
        <td>
          <p>A more detailed explanation of why the test failed</p>

        </td>
        <td>
          
        </td>
      </tr>
          <tr>
        <td><code>history</code> (required)</td>
        <td>history object </td>
        <td>
          <p>Read <a href="/docs/test-analytics/importing-json#json-test-results-data-reference-history-objects">History objects</a></p>

        </td>
        <td>
          
        </td>
      </tr>
          <tr>
        <td><code>tags</code> </td>
        <td>Key-value hash </td>
        <td>
          <p>Read <a href="/docs/test-analytics/importing-json#json-test-results-data-reference-execution-level-custom-tags">Execution level custom tags</a></p>

        </td>
        <td>
          <code><p>{ "team": "foobar", "feature": "frontend" }</p>
</code>
        </td>
      </tr>
      </tbody>
</table>

**Example:**

```js
{
  "id": "95f7e024-9e0a-450f-bc64-9edb62d43fa9",
  "scope": "Analytics::Upload associations",
  "name": "fails",
  "location": "./spec/models/analytics/upload_spec.rb:24",
  "file_name": "./spec/models/analytics/upload_spec.rb",
  "result": "failed",
  "failure_reason": "Failure/Error: expect(true).to eq false",
  "failure_expanded": [
    /* failure_expanded object */
  ],
  "history": {
    /* history object */
  }
}
```

### Failure expanded objects

A failure expanded array contains extra details about the failed test.

<table class="responsive-table">
  <thead>
    <tr>
      <th>Key</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
          <tr>
        <td><code>expanded</code> (required)</td>
        <td>array </td>
        <td>
          <p>An array of strings describing the failure</p>

        </td>
      </tr>
          <tr>
        <td><code>backtrace</code> (required)</td>
        <td>array </td>
        <td>
          <p>An array of strings documenting the backtrace of the failed test</p>

        </td>
      </tr>
      </tbody>
</table>

**Example:**

```js
{
  "expanded": [
    "  expected: false",
    "       got: true",
    "",
    "  (compared using ==)",
    "",
    "  Diff:",
    "  @@ -1 +1 @@",
    "  -false","  +true"
  ],
  "backtrace": [
    "./spec/models/analytics/upload_spec.rb:25:in `block (3 levels) in <top (required)>'","./spec/support/log.rb:17:in `run'",
    "./spec/support/log.rb:66:in `block (2 levels) in <top (required)>'",
    "./spec/support/database.rb:19:in `block (2 levels) in <top (required)>'",
    "/Users/abc/Documents/rspec-buildkite-analytics/lib/rspec/buildkite/analytics/uploader.rb:153:in `block (2 levels) in configure'",
    "-e:1:in `<main>'"
  ]
}
```

### History objects

A history object represents the overall duration of the test run and contains detailed span data, more finely recording the test run.

<table class="responsive-table">
  <thead>
    <tr>
      <th>Key</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
          <tr>
        <td><code>start_at</code> (required)</td>
        <td>number </td>
        <td>
          <p>A monotonically increasing number</p>

        </td>
      </tr>
          <tr>
        <td><code>end_at</code> </td>
        <td>number </td>
        <td>
          <p>A monotonically increasing number</p>

        </td>
      </tr>
          <tr>
        <td><code>duration</code> (required)</td>
        <td>number </td>
        <td>
          <p>How long the test took to run. This value is seconds stored as a float.</p>

        </td>
      </tr>
          <tr>
        <td><code>children</code> </td>
        <td>array of span objects </td>
        <td>
          <p>Read <a href="/docs/test-analytics/importing-json#json-test-results-data-reference-span-objects">Span objects</a></p>

        </td>
      </tr>
      </tbody>
</table>

**Example:**

```js
{
  "start_at": 347611.724809,
  "end_at": 347612.451041,
  "duration": 0.726232000044547,
  "children": [
    /* span objects */
  ]
}
```

### Execution level custom tags

You can add arbitrary tags to your test executions to enable custom grouping and filtering of test metrics.

**Example:**

```json
{
  "team": "frontend",
  "feature": "a-great-feature"
}
```

### Span objects

Span objects represent the finest duration resolution of a test run.
It represents, for example, the duration of an individual database query within a test.

<table class="responsive-table">
  <thead>
    <tr>
      <th>Key</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
          <tr>
        <td><code>section</code> (required)</td>
        <td>string (<code>http</code>, <code>sql</code>, <code>sleep</code> or <code>annotation</code>)</td>
        <td>
          <p>A section category for this span</p>

        </td>
      </tr>
          <tr>
        <td><code>start_at</code> </td>
        <td>number </td>
        <td>
          <p>A monotonically increasing number</p>

        </td>
      </tr>
          <tr>
        <td><code>end_at</code> </td>
        <td>number </td>
        <td>
          <p>A monotonically increasing number</p>

        </td>
      </tr>
          <tr>
        <td><code>duration</code> (required)</td>
        <td>number </td>
        <td>
          <p>How long the span took to run. This value is seconds stored as a float.</p>

        </td>
      </tr>
          <tr>
        <td><code>detail</code> </td>
        <td> </td>
        <td>
          <p>A detail object containing further details on the span. Required when <code>section</code> is <code>http</code>, <code>sql</code>, or <code>annotation</code>.
Read <a href="/docs/test-analytics/importing-json#json-test-results-data-reference-detail-objects">Detail objects</a></p>

        </td>
      </tr>
      </tbody>
</table>

**Example:**

```js
{
  "section": "sql",
  "start_at": 347611.734956,
  "end_at": 347611.735647,
  "duration": 0.0006910000229254365
  "detail": {
    ...
  }
}
```

### Detail objects

Detail objects contains additional information about the span.

<table class="responsive-table">
  <thead>
    <tr>
      <th>Key</th>
      <th>Type</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
          <tr>
        <td><code>method</code> </td>
        <td>string (<code>GET</code>, <code>POST</code>, <code>PUT</code>, <code>DELETE</code>, <code>PATCH</code>, <code>HEAD</code>, <code>CONNECT</code>, <code>OPTIONS</code> or <code>TRACE</code>)</td>
        <td>
          <p>A HTTP request method (required if parent span has a <code>section</code> of <code>http</code>)</p>

        </td>
      </tr>
          <tr>
        <td><code>url</code> </td>
        <td>string </td>
        <td>
          <p>The URL requested (required if parent span has a <code>section</code> of <code>http</code>)</p>

        </td>
      </tr>
          <tr>
        <td><code>lib</code> </td>
        <td>string </td>
        <td>
          <p>The library used to make the HTTP request (required if parent span has a <code>section</code> of <code>http</code>)</p>

        </td>
      </tr>
          <tr>
        <td><code>query</code> </td>
        <td>string </td>
        <td>
          <p>The SQL query (required if parent span has a <code>section</code> of <code>sql</code>)</p>

        </td>
      </tr>
          <tr>
        <td><code>content</code> </td>
        <td>string </td>
        <td>
          <p>The annotation content (required if parent span has a <code>section</code> of <code>annotation</code>)</p>

        </td>
      </tr>
      </tbody>
</table>

**HTTP Example:**

```js
{
  "detail": {
    method: "POST",
    url: "https://example.com",
    lib: "curl"
  }
}
```

**SQL Example:**

```js
{
  "detail": {
    query: "SELECT * FROM ..."
  }
}
```

**Annotation Example:**

```js
{
  "detail": {
    content: "Visting Login"
  }
}
```

### Test result format

The following JSON code block shows an example of how your JSON test results should be formatted, so that these results can be successfully uploaded to Test Engine.

```json
[
  {
    "id": "95f7e024-9e0a-450f-bc64-9edb62d43fa10",
    "scope": "Analytics::Upload associations",
    "name": "fails",
    "location": "./spec/models/analytics/upload_spec.rb:24",
    "file_name": "./spec/models/analytics/upload_spec.rb",
    "result": "failed",
    "failure_reason": "Failure/Error: expect(true).to eq false",
    "failure_expanded": [],
    "history": {
      "start_at": 347611.724809,
      "end_at": 347612.451041,
      "duration": 0.726232000044547,
      "children": [
        {
          "section": "http",
          "start_at": 347611.734956,
          "end_at": 347611.735647,
          "duration": 0.0006910000229254365,
          "detail": {
            "method": "POST",
            "url": "https://example.com",
            "lib": "curl"
          }
        }
      ]
    }
  },
  {
    "id": "56f6e013-8e9a-340f-bc53-8edb51d32fa09",
    "scope": "Analytics::Upload associations",
    "name": "passes",
    "location": "./spec/models/analytics/upload_spec.rb:56",
    "file_name": "./spec/models/analytics/upload_spec.rb",
    "result": "passed",
    "history": {
      "start_at": 347611.724809,
      "end_at": 347612.451041,
      "duration": 0.726232000044547,
      "children": [
        {
          "section": "http",
          "start_at": 347611.734956,
          "end_at": 347611.735647,
          "duration": 0.0006910000229254365,
          "detail": {
            "method": "GET",
            "url": "https://example.com",
            "lib": "curl"
          }
        }
      ]
    }
  }
]
```
