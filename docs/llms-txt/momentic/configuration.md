# Source: https://momentic.ai/docs/cli/configuration.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Configuring momentic.config.yaml

Configure the behavior of `momentic` by using a `momentic.config.yaml` file in
your project root directory. Each configuration file represents a **project**.

Paths are relative to the location of `momentic.config.yaml` or absolute paths.
Globs are relative to the location of `momentic.config.yaml`.

## Global options

### `name`

```yaml momentic.config.yaml theme={null}
name: my-project-name
```

The name of your project. This is used in reports and other places to identify
your project.

### `include`

```yaml momentic.config.yaml theme={null}
include:
  - "**/*.test.yaml"
  - "**/*.module.yaml"
```

A list of globs for test and module files to include.

Momentic will automatically include all files that match these globs when
starting the Momentic Local App or running tests.

### `exclude`

```yaml momentic.config.yaml theme={null}
exclude:
  - "out/**/*"
```

A list of globs for files to exclude.

Folders such as `node_modules`, `.git`, and `.venv` are always excluded.

The default directory Momentic will write to when creating a new module.

### `goldenFileDir`

```yaml momentic.config.yaml theme={null}
goldenFileDir: golden/visual-diff
```

The default directory Momentic will write to storing golden files for
[Visual diff](/steps/visual-diff).

### `reporterDir`

```yaml momentic.config.yaml theme={null}
reporterDir: reports
```

The default directory for storing test reports when using reporters.

### `retries`

```yaml momentic.config.yaml theme={null}
retries: 2
```

The number of times to retry a test if it fails. This is useful for flaky tests
that may fail due to network issues or other transient problems. This will
override the `retries` option set on the test.

### `parallel`

```yaml momentic.config.yaml theme={null}
parallel: 1
```

Default: `1`

The number of tests to run in parallel. This is useful for speeding up test
execution, especially for large test suites. Set to `1` to run tests
sequentially.

### gitMainBranch

```yaml momentic.config.yaml theme={null}
gitMainBranch: main
```

The name of the main branch in your repository. When running tests on a brand
new branch, Momentic will seed the cache entries from the nearest commit on the
main branch. Additionally, when running Momentic in non-CI environments, the
main branch is excluded from cache saving. Please see
[cache saving eligibility](/step-cache#cache-saving-eligibility) for more
information.

### gitProtectedBranches

```yaml momentic.config.yaml theme={null}
gitProtectedBranches:
  - staging
```

A list of branches that by default are considered ineligible for cache saving
when running tests in a non-CI environment. This prevents accidental cache
overwriting on shared branches. Please see
[cache saving eligibility](/step-cache#cache-saving-eligibility) for more
information.

### recordVideo

```yaml momentic.config.yaml theme={null}
recordVideo: true
```

Whether to record videos of test runs. Enabling this option will increase the
size of results. Once results are uploaded, the videos can be viewed in the run
viewer. In order to use this option, ffmpeg must be installed on the machine.
This can be done using the `momentic install-browsers ffmpeg` command.

### displayRoot

```yaml momentic.config.yaml theme={null}
displayRoot: src/tests
```

A relative path from the project root to use as the Repository root in the
Momentic Local App. This allows you to focus the repository view on a specific
subdirectory. If not specified, the repository view shows the entire project
root. This setting is display only and does not affect test execution or file
resolution.

## Defining environments

### `environments`

Each object in the `environments` list defines a different environment for
running tests. Each environment defines a set of key-value pairs which are
available to tests as [variables](/variables).

In the example below, we've defined three environments: `dev`, `staging`, and
`production`.

```yaml momentic.config.yaml theme={null}
environments:
  - name: dev
    baseUrl: https://dev.example.com
    envVariables:
      USERNAME: devUser
      PASSWORD: devPassword
  - name: staging
    baseUrl: https://staging.example.com
    envVariables:
      USERNAME: stagingUser
      PASSWORD: stagingPassword
  - name: production
    baseUrl: https://www.example.com
    envVariables:
      USERNAME: prodUser
      PASSWORD: prodPassword
```

## Environment options

### `name`

```yaml momentic.config.yaml theme={null}
environments:
  - name: dev
```

The name of the environment. This is used to identify the environment when
running tests. It is also available as `env.ENV_NAME` in tests.

### `baseUrl`

```yaml momentic.config.yaml theme={null}
environments:
  - name: dev
    baseUrl: https://dev.example.com
```

The starting URL for the environment. This is used as the base URL for all tests
using this environment. It is also available as `env.BASE_URL` in tests.

### `envVariables`

```yaml momentic.config.yaml theme={null}
environments:
  - name: dev
    baseUrl: https://dev.example.com
    envVariables:
      USERNAME: devUser
      PASSWORD: devPassword
      API_KEY: ${VAR_FROM_SHELL:-default_value}
```

A list of key-value pairs that define environment variables for the environment.
These variables are available to tests as `env.VARIABLE_NAME`. They can be used
to store sensitive information like API keys or credentials.

[Interpolation](https://dotenvx.com/docs/env-file#interpolation) is supported,
so you can reference shell variables. You cannot reference other variables
defined in the same environment.

#### `inheritFromShell`

```yaml momentic.config.yaml theme={null}
environments:
  - name: dev
    baseUrl: https://dev.example.com
    inheritFromShell: true
    envVariables:
      USERNAME: devUser
      PASSWORD: devPassword
```

Default: `false`

Include all values from the enclosing shell as environment variables at runtime.

#### `envFile`

```yaml momentic.config.yaml theme={null}
environments:
  - name: dev
    baseUrl: https://dev.example.com
    envFile: .dev.env
    envVariables:
      USERNAME: devUser
      PASSWORD: devPassword
```

The path to a file containing environment variables. This file should be in the
format of a `.env` file, with each line containing a key-value pair. Momentic
will load these variables and make them available to tests as
`env.VARIABLE_NAME`.

#### JSON file

```yaml momentic.config.yaml theme={null}
environments:
  - name: dev
    baseUrl: https://dev.example.com
    envVariables:
      VAR_FROM_FILE:
        fromFile: package.json
        json: true
```

You can also load environment variables from a JSON file. The `fromFile` option
specifies the path to the file, and the `json` option indicates that the file is
in JSON format. The variables will be available as `env.VAR_FROM_FILE`.

#### `browser.proxy`

```yaml momentic.config.yaml theme={null}
environments:
  - name: dev
    browser:
      proxy:
        server: http://proxy.internal.example.com:3128
        username: my-proxy-user
        password: my-proxy-password
```

Configure an HTTP proxy for a specific environment. The `server` field must
include the protocol (`http://` or `https://`), host, and port. Optionally set
`username` and `password` when the proxy requires authentication.

## Browser options

### `browser`

Configure default browser settings for all tests in the project. Individual
tests can override these settings.

```yaml momentic.config.yaml theme={null}
browser: {}
```

#### `defaultBrowserType`

```yaml momentic.config.yaml theme={null}
browser:
  defaultBrowserType: Chromium
```

Set the default browser type for all tests in the project. When creating a test,
you can choose to use this default or select a specific browser type.

Valid options:

* `Chromium`: A lightweight, open-source browser that supports only a basic
  feature set. This is the default browser used by automation frameworks such as
  Playwright and Cypress.
* `Google Chrome`: An experimental, full-fledged Google Chrome build supporting
  advanced features such as Chrome extensions, PDF rendering, and WebGL.
* `Chrome for Testing`: A headless-only version of Google Chrome with a separate
  rendering engine specifically optimized for testing and automation.

Individual tests can override this setting by specifying a different browser
type.

#### `pageLoadTimeoutMs`

```yaml momentic.config.yaml theme={null}
browser:
  pageLoadTimeoutMs: 20000
```

Default: `8000`

How long to wait for a page to load before timing out, in milliseconds. This
includes new tabs and navigation events.

#### `smartWaitingTimeoutMs`

```yaml momentic.config.yaml theme={null}
browser:
  smartWaitingTimeoutMs: 10000
```

Default: `5000`

Configure the maximum timeout for [smart waiting](/auto-heal#smart-waiting), in
milliseconds. This controls how long Momentic will wait for the page to
stabilize before proceeding from one step to the next.

#### `localChromeExtensionPaths`

```yaml momentic.config.yaml theme={null}
browser:
  localChromeExtensionPaths:
    - /tmp/eimadpbcbfnmbkopoojfekhnkhdbieeh
    - /tmp/bcjindcccaagfpapjjmafapmmgkkhgoa
```

An list of paths to unpacked Chrome extensions. These extensions will be loaded
onto the browser before the test begins.

#### `extraHeaders`

```yaml momentic.config.yaml theme={null}
browser:
  extraHeaders:
    Authorization: Bearer my-secret-token
    X-Custom-Header: CustomValue
```

Extra HTTP headers to include in all requests made by the browser. This can be
useful for authentication or other custom headers that your application
requires.

#### `initialLocalStorage`

```yaml momentic.config.yaml theme={null}
browser:
  initialLocalStorage:
    https://momentic.ai:
      momenticTestKey1: momenticTestValue1
      momenticTestKey2: momenticTestValue2
```

Initial state to set in local storage, specified as key-value pairs per origin.
The specified origin must be the full origin (scheme + host + optional port).
This can be useful for authentication or settings that use local storage (such
as feature flag overrides).

#### `userAgent`

```yaml momentic.config.yaml theme={null}
browser:
  userAgent:
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML,
    like Gecko) Chrome/138.0.0.0 Safari/537.36"
```

Default:
`Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/136.0.7103.25 Safari/537.36`

The user agent string to use for all requests made by the browser.

#### `disableGpu`

```yaml momentic.config.yaml theme={null}
browser:
  disableGpu: true
```

Default: `false`

Whether to disable intensive graphical operations, such as WebGL and
rasterization with hardware acceleration. Disabling can significantly increase
performance, however some graphics libraries may require it.

#### `disableZygote`

```yaml momentic.config.yaml theme={null}
browser:
  disableZygote: true
```

Default: `false`

Whether to disable Chrome's zygote process. This can reduce process overhead in
some environments, but may impact compatibility with certain browser features.

#### `disableBrowserMonitoring`

```yaml momentic.config.yaml theme={null}
browser:
  disableBrowserMonitoring: true
```

Default: `false`

Whether to disable Momentic's default recording of console logs and network
requests. This data populates the Console and Network tabs in the run viewer and
test editor. Disabling this extra data capturing can improve performance on
sites with a large volume of logs or requests.

#### `disableConsoleLogs`

```yaml momentic.config.yaml theme={null}
browser:
  disableConsoleLogs: true
```

Default: `false`

Whether to disable console log recording during test runs. This setting can
provide a small performance improvement on sites with a large volume of console
logs.

#### `disableNetworkLogs`

```yaml momentic.config.yaml theme={null}
browser:
  disableNetworkLogs: true
```

Default: `false`

Whether to disable network request recording during test runs. This setting can
provide a small performance improvement on sites with a large volume of network
requests.

#### `grantedPermissions`

```yaml momentic.config.yaml theme={null}
browser:
  grantedPermissions:
    - clipboard-read
    - clipboard-write
    - microphone
    - camera
    - geolocation
```

Default: `undefined`

A list of browser permissions to automatically grant during test execution. If
not set, all permissions are granted.

#### `autoExpandIframes`

```yaml momentic.config.yaml theme={null}
browser:
  autoExpandIframes: true
```

Default: `false`

Automatically expand iframes. This allows Momentic to interact with elements
inside iframes without needing to configure the **Act within iframe** option.

#### `autoFollowNewTabs`

<Warning>
  This option is deprecated and will be removed in the future. Waiting for new
  tabs to open is inherently racy, as client-side JavaScript may not open the
  tab before Momentic continues onto the next step. Please use [Switch
  Tab](/steps/switch-tab) steps to explicitly switch to new tabs instead.
</Warning>

```yaml momentic.config.yaml theme={null}
browser:
  autoFollowNewTabs: true
```

Default: `false`

Automatically switch to new tabs that are opened during test execution.

#### `allowPartialAccessibilityTree`

```yaml momentic.config.yaml theme={null}
browser:
  allowPartialAccessibilityTree: true
```

Default: `false`

Momentic uses the accessibility tree as context for several AI agents. However,
some sites can fail to load the complete accessibility tree due to third-party
iframes, embedded videos, or misconfigured script tags. Enable this setting to
allow using partial sections of the accessibility tree.

#### `ignoreHttpsErrors`

```yaml momentic.config.yaml theme={null}
browser:
  ignoreHttpsErrors: true
```

Default: `false`

Ignore HTTPS errors, such as self-signed certificates and certificate errors.
Useful for testing internal or development environments that use self-signed
certificates.

#### `showZeroOpacityElements`

<Warning>
  We strongly recommend using [hover](/steps/hover) steps to reveal hidden
  elements before interacting with them.
</Warning>

```yaml momentic.config.yaml theme={null}
browser:
  showZeroOpacityElements: false | true | inputs-only
```

Default: `true`

When set to false, filter out elements with zero opacity from the page context
that is passed to Momentic's locator AI agent. In addition, prevent interactive
steps from targeting elements that have opacity 0. This improves AI performance
and more closely mimics the behavior of a human user.

This option never affects element check steps, which are commonly used to locate
and verify hidden elements.

When this option is set to `false`, users may need to add hover or scroll steps
to reveal hidden elements before interacting with them.

When this option is set to `inputs-only`, `<input>` elements that are zero
opacity are still shown. This is useful for sites that use UI frameworks that
rely on hidden inputs for styling reasons.

#### `ignoreHrefForCaching`

```yaml momentic.config.yaml theme={null}
browser:
  ignoreHrefForCaching: true
```

Default: `false`

Ignore the `href` attribute when determining whether cache entries can be reused
for anchor elements. This can greatly improve speed for sites that use
auto-generated or dynamic links. `href` attributes are only ignored if the
anchor element has some text content (either as a direct child or in some nested
element).

#### `disableSecondaryCacheResolution`

```yaml momentic.config.yaml theme={null}
browser:
  disableSecondaryCacheResolution: true
```

Default: `false`

Disable secondary cache resolution methods, which include using HTML l-dist and
template matching. These methods are less accurate and may cause instances where
step caches resolve to the wrong element, but can improve test speed.

#### `hybridSelectorMode`

<Warning>
  Hybrid selectors are in beta and subject to be deprecated in the future.
</Warning>

Hybrid selectors combine multiple different pieces of information from the HTML
to reliably identify an element, including it's text content, classes,
attributes, parent hierarchy, and more. Hybrid selectors can even pierce shadow
DOM roots, unlike traditional selectors.

Hybrid selectors place a greater emphasis on text content compared to CSS
selectors. As such, if you desire behavior where a specific child in the
hierarchy is always chosen, we recommend using nth keywords and turning on
`Disable cache` to ensure the correct element is always targeted.

```yaml momentic.config.yaml theme={null}
browser:
  hybridSelectorMode: prefer
```

Default: `off`

Options:

* `off`: Disable hybrid selectors altogether. Equivalent to omitting this field
  entirely.
* `test`: Enable hybrid selectors for element resolution, and report mismatches
  to Momentic.
* `prefer`: Enable hybrid selectors for element resolution and prefer using them
  over traditional selectors. If no elements are discovered using hybrid
  selectors, falls back to CSS selectors.
* `always`: Enable hybrid selectors and never use traditional CSS selectors. If
  no elements are discovered using hybrid selectors, falls back to AI.

#### `globalLocatorRedirect`

```yaml momentic.config.yaml theme={null}
browser:
  globalLocatorRedirect: false | true | always
```

Default: `always`

For backwards compatibility reasons, when this setting is set to `true`, it will
only be enabled for CLICK steps. When set to `always` it will apply to all
steps.

During interactive steps, use Momentic's custom algorithm for determining the
"top-most" element that should be interacted with. Sometimes, functional HTML
elements can be covered by other presentational HTML elements. For example, many
UI frameworks employ hidden inputs that are covered by styled `<div>` or
`<label>` elements that users actually interact with when clicking. While other
frameworks such as Playwright
[throw errors](https://playwright.dev/docs/actionability#receives-events) or
require users to explicitly bypass stability checks in this case, Momentic's
algorithm can determine the top-most element that still intersects with the
original bounding box and interact with that element instead.

For customers who desire more manual control over how to handle cases where an
element is covered by another element, you can opt out of this feature. The
"Disable stability checks" option on interactive steps can also be used to force
interactions with covered elements, similar to Playwright's
[force](https://playwright.dev/docs/actionability#forcing-actions) setting.

#### `forceClickForMissingRedirectElement`

```yaml momentic.config.yaml theme={null}
browser:
  forceClickForMissingRedirectElement: true
```

Default: `false`

When `globalLocatorRedirect` is enabled but it cannot find a valid element to
redirect to, force click the originally targeted element instead of failing due
to actionability checks.

#### `visualActions`

```yaml momentic.config.yaml theme={null}
browser:
  visualActions: true
```

Default: `false`

Use a heuristic to determine x, y coordinates of the element and use them to
perform actions like clicking, hovering, or typing.

#### `importantAttributes`

```yaml momentic.config.yaml theme={null}
browser:
  importantAttributes:
    - data-topic-id
```

Specify additional HTML attributes that should never be pruned from the context
passed to AI agents. Common testing attributes such as `data-test-id` and
`aria-label` are automatically considered important. Values may contain a single
`*` at the end to indicate a prefix match, such as `data-test-*`.

#### `importantClasses`

```yaml momentic.config.yaml theme={null}
browser:
  importantClasses:
    - list-controls
```

Specify important CSS class names. An element with an important class name will
never be pruned from the context passed to AI agents. Values may contain a
single `*` at the end to indicate a prefix match, such as `home-page-*`.

#### `disableFullStory`

```yaml momentic.config.yaml theme={null}
browser:
  disableFullStory: true
```

Prevent all FullStory scripts from mounting during test execution. FullStory is
known to impact page performance and cause page crashes during test automation
due to the high volumes of nodes scanned and mutated.

## AI options

### `ai`

Configure AI features for the project.

```yaml momentic.config.yaml theme={null}
ai: {}
```

#### `agentConfig`

```yaml momentic.config.yaml theme={null}
ai:
  agentConfig:
    locator: v3
    assertion: v3
    visual-assertion: v3
    text-extraction: v3
```

Choose which version of prompts and AI models to use for certain AI tasks.
Please see [AI configuration](/ai-config) for available options.

#### `failureRecovery`

<Warning>
  Failure recovery is in beta and subject to be deprecated in the future.
</Warning>

```yaml momentic.config.yaml theme={null}
ai:
  failureRecovery: true
```

Default: `false`

Enable [Failure recovery](/failure-recovery) to automatically recover from
certain test failures by proposing and executing step changes.

#### `aiFailureAnalysis`

```yaml momentic.config.yaml theme={null}
ai:
  aiFailureAnalysis: true
```

Default `false`

Enable AI failure analysis for failed test runs. When a run fails, Momentic
analyzes the error to classify a likely root cause, summarize previous steps,
and generate an error summary. The analysis appears in the Run Viewer under the
"AI failure analysis" tab.

#### `aiPageFiltering`

```yaml momentic.config.yaml theme={null}
ai:
  aiPageFiltering: true
```

Default: `false`

Enables page chunking and filtering if the page is too large. This allows
Momentic to handle large pages more efficiently by breaking them into smaller
chunks and filtering out unnecessary content.

#### `useMemory`

```yaml momentic.config.yaml theme={null}
ai:
  useMemory: true
```

Default: `false` for browser tests / `true` for mobile tests

Allow AI agents to use data from past test runs to ensure consistency and
accuracy when locating elements and evaluating assertions. Read more about
memory [here](/memory). This option sets the organization-wide default for
memory, but can still be overridden on a per-test basis.

## Advanced options

### `advanced`

Configure advanced settings for the project.

```yaml momentic.config.yaml theme={null}
advanced: {}
```

#### `fakerConstantSeed`

```yaml momentic.config.yaml theme={null}
advanced:
  fakerConstantSeed: true
```

Default: `false`

Use a constant seed for the Faker library to ensure that random data generated
by Faker is consistent across test runs. This can be useful for debugging and
ensuring that tests are reproducible.

#### `isolateCachesByEnvironment`

```yaml momentic.config.yaml theme={null}
advanced:
  isolateCachesByEnvironment: true
```

Default: `false`

Store separate step cache entries for each environment. By default, step caches
are shared across all environments. This works well when it can be assumed that
selectors that work in one environment will also work in another. However, in
cases where there are significant differences between environments (such as
different DOM structures or randomized element IDs), sharing caches will cause
frequent cache misses and slower test runs.

## Mobile options

The following sections only apply to mobile test runs.

### Emulator

Configure options for mobile emulators spun up by Momentic.

#### `region`

```yaml momentic.config.yaml theme={null}
emulator:
  region: us-west1
```

Default: when unset, Momentic chooses the region closest to the user's source IP
address.

Choose the region where the emulator will be spun up, which may affect
application behavior and latency. Currently, the supported options are
`us-west1` and `eu-north1`.

#### `autoGrantPermissions`

```yaml momentic.config.yaml theme={null}
emulator:
  autoGrantPermissions: true
```

Default: `false`

Automatically grant permissions to the app under test. This bypasses most
permission confirmation dialogs.

#### `disableMomenticAccessibilityTree`

```yaml momentic.config.yaml theme={null}
emulator:
  disableMomenticAccessibilityTree: true
```

Default: `false`

When interacting with webviews, Momentic uses a custom implementation of the
accessibility tree that includes more elements by default. This flag disables
that behavior, using the native Android accessibility tree implementation
instead. Enabling this setting may speed up webview interactions by 1-2 seconds,
but may cause interactions with elements within webviews to fail, especially
those outside of the current viewport.


Built with [Mintlify](https://mintlify.com).