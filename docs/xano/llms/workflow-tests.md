# Source: https://docs.xano.com/xano-cli/workflow-tests.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Testing

> Run unit tests and workflow tests from the CLI

export const BrowserFrame = props => {
  const {url = "xano.run", maxWidth = 820, className = "", lightSrc, darkSrc, alt = "", children} = props || ({});
  const style = typeof maxWidth === "number" ? {
    maxWidth: `${maxWidth}px`,
    margin: "16px 0"
  } : {
    maxWidth,
    margin: "16px 0"
  };
  const hasSwapImages = Boolean(lightSrc && darkSrc);
  return <div className={`browser-frame ${className}`.trim()} style={style}>
      <div className="browser-frame__top">
        <div className="browser-frame__controls" aria-hidden="true">
          <span className="browser-frame__dot browser-frame__dot--red" />
          <span className="browser-frame__dot browser-frame__dot--yellow" />
          <span className="browser-frame__dot browser-frame__dot--green" />
        </div>
        <div className="browser-frame__address">{url}</div>
      </div>

      <div className="browser-frame__body">
        {hasSwapImages ? <>
            <img className="browser-frame__img--light" src={lightSrc} alt={alt} />
            <img className="browser-frame__img--dark" src={darkSrc} alt={alt} />
          </> : children}
      </div>
    </div>;
};

The CLI provides commands for running both unit tests and workflow tests, letting you validate your backend logic directly from the terminal.

<Note>
  Test commands require a workspace ID, either from your profile or via the `-w` flag.
</Note>

## Unit Tests

Unit tests validate individual functions and logic blocks.

### List Unit Tests

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano unit_test list
  ```
</BrowserFrame>

Filter by branch or object type:

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano unit_test list --branch dev --obj-type function
  ```
</BrowserFrame>

### Run a Unit Test

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano unit_test run UNIT_TEST_ID
  ```
</BrowserFrame>

### Run All Unit Tests

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano unit_test run_all
  ```
</BrowserFrame>

Filter by branch or object type:

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano unit_test run_all --branch dev --obj-type function
  ```
</BrowserFrame>

***

## Workflow Tests

Workflow tests validate end-to-end backend logic by running test suites.

### List Tests

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano workflow_test list
  ```
</BrowserFrame>

Filter by branch with `-b`:

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano workflow_test list -b dev
  ```
</BrowserFrame>

Use `-o json` for the full JSON response.

### Get Test Details

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano workflow_test get TEST_ID
  ```
</BrowserFrame>

| Flag              | Description                                                   |
| ----------------- | ------------------------------------------------------------- |
| `--include-draft` | Include the draft version of the test                         |
| `-o`              | Output format: `summary`, `json`, or `xs` (XanoScript source) |

### Run a Test

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano workflow_test run TEST_ID
  ```
</BrowserFrame>

### Run All Tests

Run every workflow test in the workspace:

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano workflow_test run_all
  ```
</BrowserFrame>

Filter by branch with `-b`:

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano workflow_test run_all -b dev
  ```
</BrowserFrame>

### Delete a Test

<BrowserFrame url="Terminal">
  ```bash  theme={null}
  xano workflow_test delete TEST_ID
  ```
</BrowserFrame>

Add `-f` to skip the confirmation prompt.


Built with [Mintlify](https://mintlify.com).