# Momentic Documentation

Source: https://docs.momentic.ai/llms-full.txt

---

# AI configuration
Source: https://momentic.ai/docs/ai-config

Customize AI behavior in your tests

Momentic uses a variety of agents, each specialized for a specific task within
end-to-end testing. Currently, the following agents can be configured by users:

| Name                                  | Description                                                                                                                                                                                                                                                                                          |
| ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Locator (`locator`)                   | Locates elements on the page based on a natural language description. This agent is used for all interactive commands that target elements, such as [Click](/steps/click) and [Type](/steps/type) steps. This agent is also used to resolve elements in [Element check](/steps/element-check) steps. |
| Assertion (`assertion`)               | Evaluates the truthiness of natural language statements based on an instantaneous snapshot of the page. This agent is used to power [AI check](/steps/ai-check) steps.                                                                                                                               |
| Visual Assertion (`visual-assertion`) | Evaluates the truthiness of natural language statements purely based on a screenshot of the current viewport.                                                                                                                                                                                        |
| Text Extraction (`text-extraction`)   | Extracts text from the page based on a natural language description. This agent powers [AI extract](/steps/ai-extract) steps.                                                                                                                                                                        |

Momentic exposes the ability to choose the versions of these agents so that
users can upgrade at their own cadence and test upgrades before applying them.

## Locator

### v1

* Uses older 2024 models.
* Interprets the user's criteria more leniently and will attempt to find a
  candidate element that fulfills the same function as what the user describes.

### v2

* Uses early 2025 models.
* Places a strong emphasis on respecting relative positioning criteria (e.g.
  "the link in the header", "the X icon in the modal"), and will fail if it
  cannot find the reference element.
* Strongly respects single-quoted text (e.g. "the 'Submit' button") and will
  reject candidate elements that do not contain that exact text.

### v3 (recommended)

* Recommended configuration for new organizations.
* Uses the latest 2025 models.
* Generates smarter caches:
  * Element attributes: if a prompt specifically refers to certain attributes
    such as text content or position, those will be stored and required to
    remain the same across runs.
  * Relative elements: if a prompt refers to other elements on the page, those
    will also be included in the cache to ensure that any meaningful changes
    result in the cache busting.
* Writes better explanations of its reasoning for choosing elements.

## Assertion

### v1

* Uses older 2024 models.
* Interprets assertion criteria more leniently and will attempt to evaluate
  whether or not an assertion is "overall true" or "overall false".

### v2

* Uses early 2025 models.
* Displays superior understanding of sorted order, visual positioning, and
  relative positioning criteria (e.g. "The button in the modal is enabled").
* Strongly respects single-quoted text (e.g. "element with title='hello world'")
  and will fail the assertion if there is no element that contains that provided
  text.

### v3 (recommended)

* Recommended configuration for new organizations.
* Uses the latest 2025 models.

## Visual Assertion

### v1

* Uses older 2024 models.
* Faster, returning results in an average of 3 seconds.
* More lenient when evaluating user criteria against the page state,
  specifically for assertions about color.

### v2

* Uses early 2025 models.
* Slower than V1 but perceives small visual details more accurately.
* Far stronger on logical reasoning, negated assertions, and assertions about
  elements in containers.
* Strongly respects the term "exactly" and single quotes around text terms. Will
  fail the assertion if it not unambiguously true when these modifiers are
  provided.

### v3 (recommended)

* Recommended configuration for new organizations.
* Uses the latest 2025 models.

## Text Extraction

### v1

* Uses older 2024 models.

### v2

* Uses early 2025 models.
* Adheres to the provided JSON schema more consistently and will throw an error
  if the extracted data does not conform to the schema.
* Tuned to understand the `pattern` JSON schema option specifically.

### v3 (recommended)

* Recommended configuration for new organizations.
* Uses the latest 2025 models.
* Improved ability to handle complex JSON schemas, including nested objects and
  arrays.
* Better at following user instructions for processing or transforming data
  before returning it.


# Auto-healing
Source: https://momentic.ai/docs/auto-heal

Learn how Momentic makes tests reliable by automatically adjusting to changes in your app

## Natural language locators

During test execution, Momentic uses both traditional and AI-enhanced techniques
to determine whether the original element you targeted still exists on the page.

If the original element is not present, Momentic will attempt to locate a
replacement element on the page that still matches your original description.

If a reasonable result is found and the rest of the test passes, the new target
will be [cached](/step-cache) automatically.

## Smart waiting

Momentic intelligently waits for the page to stabilize before performing each
action. Smart waiting is designed to remove the need for users to add explicit
[Wait](/steps/wait) steps, which is a common source of flakiness.

While smart waiting, Momentic will periodically check if performing the next
step is possible. For example, while waiting for the page to stabilize for a
[Click](/steps/click) step, Momentic will periodically check if the element to
be clicked is present on the page and proceed if so.

The smart waiting timeout is set to 3 seconds by default and is configurable for
each test.

Inputs to smart waiting:

* Navigation events
* `load` events
* Page screenshots
* DOM changes (nodes added, removed, or updated)
* Same-origin requests


# Browsers
Source: https://momentic.ai/docs/browsers

Supported browser types

## Chromium

Chromium is the default browser option for Momentic. It is a fast and
lightweight browser optimized for testing needs. However, it does not support
all the features of Google Chrome such as video playback. Chromium is known to
be unstable when used to automate sites with graphics-heavy scripts.

## Google Chrome

Google Chrome is a full-fledged browser that offers the broadest feature
support, including H.264 video playback, media streaming, WebGL, and more. It
may consume more resources than Chromium and execute tests more slowly.

## Chrome for Testing

[Chrome for Testing](https://developer.chrome.com/blog/chrome-for-testing/) is a
browser version newly released in 2025, maintained by Google specifically for
testing purposes.

## Browser behavior

To ensure consistent test results, Momentic overrides certain browser behaviors.

| Setting                   | Value                                                                                                               |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| User agent                | Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.31 Safari/537.36 |
| Location                  | 37.7749 by -122.4194 (San Francisco)                                                                                |
| Video auto-play           | Disabled                                                                                                            |
| Chrome browser onboarding | Disabled                                                                                                            |
| Desktop notifications     | Disabled                                                                                                            |


# Product updates
Source: https://momentic.ai/docs/changelog

New updates and improvements

<Update label="Feb 2026">
  ## Features

  ### Web

  * AI settings used during a test run are now surfaced in the Run Viewer for
    easier debugging.
  * Runs that passed thanks to [Failure Recovery](/failure-recovery) now display
    recovery details and a "Recovered" badge in the Run Viewer.
  * A "Recovered" filter is available on the Runs table to quickly find recovered
    runs.
  * Updated [Failure Recovery](/failure-recovery) UI with clearer presentation of
    recovery details and suggested steps.
  * Failure Recovery now handles a wider range of scenarios, including failures
    within modules and longer action sequences.
  * Filters on the Runs, Run Groups, and Analytics pages now support multi-select.
  * Added a date range picker, CLI version filter, to the Runs and Run Groups
    page.
  * Added a search bar to the Quarantine page to filter by test name.
  * Added a directory filter option for Quarantine rules.
  * Video player now supports speed controls and smoother playback.
  * Network tab dropdowns in the Run Viewer now support multi-select.
  * Test retries are now optional per-test and fall back to the organization's
    Momentic config if not set.
  * Run a single step within a Conditional without triggering the assertion.
  * Assertion V4 model rolled out with improved accuracy.
  * [Page Check](/steps/page-check) assertions are now scoped to the document
    body, reducing false positives from non-visible page content.

  ### MCP / Copilot

  * Granular MCP tools — individual tools for each step type instead of a single
    monolithic tool, with skill files for guided workflows.
  * New parameter for outputting test results to files.
  * Consolidated test and environment listing into a single MCP tool.
  * Added `resetSession` parameter to `momentic_run_step` for in-place session
    restart.
  * Added request listener, request recording, and mock route step types for AI
    agents.
  * Added custom headers and device pixel ratio support to MCP server.
  * `momentic mcp` command now accepts an argument to override headful/headless
    browser mode.
  * Caching now supported in Copilot for faster repeat interactions.

  ## Bug fixes

  * Fixed an error when opening the Settings > AI page.
  * Fixed an issue where runs that passed via Failure Recovery were not displaying
    the recovery badge.
  * Ensured failed Conditional child steps are properly skipped when using "Run
    To."
  * Fixed video timeline scrubber sync issues on short runs.
  * Fixed the AI configs page failing to load due to a type error.
  * Test details panel now correctly updates the title when switching between
    tests.
</Update>

<Update label="Jan 2026">
  ## Features

  ### Web

  * Added a global organization-level setting for default browser type (Chrome,
    Chromium, or Chrome for Testing) in
    [Settings](https://app.momentic.ai/settings/browser). Individual tests can use
    "default" to inherit this setting.
  * Cloud customers can now pin specific sub-agent versions in
    [AI Settings](https://app.momentic.ai/settings/ai) for consistent AI
    performance across CLI releases.
  * Added a Video Player to the Run Viewer to watch recorded test run videos
    directly in the browser.
  * Filter the Analytics page by individual test for more targeted insights.
  * Conditional steps now support Javascript as an assertion, enabling
    programmatic branching logic in tests.
  * Memory now supports Conditional steps, ensuring assertion memory is saved and
    resolved for conditional blocks.
  * Undo/Redo is now supported in the editor.

  ### Mobile

  * Failure Recovery now available for mobile tests.
  * Rotate Orientation step added for mobile tests.
  * Error messages and details are now shown for failed mobile test runs.
  * Undo/Redo now supported in the mobile editor.
  * iOS support: AI Check, AI Tap, WebView support, and iOS-specific agents
    launched.

  ## Bug fixes

  * Fixed the Save button remaining enabled after saving changes, which also
    prevented the Reset button from working.
  * Conditional steps no longer throw errors when used inside modules.
  * Cached modules now work reliably — auth state is no longer incorrectly
    restored when an invalidation rule is configured.
  * Modules can no longer be incorrectly added inside other modules via the step
    chooser.
  * Fixed a full-page error triggered by clicking a single day on the Usage page.
  * Saving a new module parameter option no longer returns an error.
  * Resolved a server components error on the Usage page affecting certain
    accounts.
  * Fixed editor performance issues and excessive battery drain during prolonged
    usage of the Cloud app.
  * AI CHECK and AI EXTRACT steps are now significantly faster.
</Update>

<Update label="Dec 2025">
  ## Features

  ### Web

  * Runs that passed thanks to Failure Recovery are now visually indicated in the
    Runs page.
  * The Run Viewer now auto-focuses and scrolls to the first failed step when
    opening a test result.
  * Navigate between steps in the Run Viewer using arrow keys.
  * Added `disableConsoleLogs` and `disableNetworkLogs` browser settings to
    control log collection during Cloud runs, reducing CPU usage.

  ### Mobile

  * Screen Check step now available for mobile tests.
  * Added Uninstall App step type.
  * Step retries now supported for mobile tests.
  * Element Check step now available for mobile tests.
  * Drag and Drop step now supported in mobile tests.
  * Memory is now supported for mobile tests.

  ## Bug fixes

  * Massive console logs no longer cause high CPU usage and crashes in Cloud runs.
  * Modules in the Run Viewer can now be collapsed again after expanding.
  * Fixed elements bleeding through the Run Viewer details panel.
  * Editing an assertion in a Conditional step no longer causes child steps to
    disappear.
  * Conditional steps now save correctly inside modules.
  * Fixed cached action slowness for certain customer accounts.
</Update>

<Update label="Nov 2025">
  ## Features

  * Released
    [V3 AI models for locator, assertions, and visual assertions](ai-config).
    Enable them today in your Settings page or in your project YAML.
  * With V3 locator models enabled, Momentic will now cache contextual elements in
    addition to the targeted element.
  * Videos of test runs can now be captured in Momentic. You can enable this via
    the `--record-video` flag or in your project YAML with `recordVideo: true`.
  * Added Conditional step to support if statements. Write an AI CHECK assertion
    and if it is true, perform steps you nest within the step.
  * MCP/Copilot can now reference and use modules.
  * Updated to latest version of Playwright.
  * Test caches now merge back into `main` when using GitHub or GitLab
    integrations.
  * Quarantined test notifications can be routed to a specific Slack channel.
  * AI ACTION now supports Drag and Drop steps.
  * Added `disableFullStory` configuration option. FullStory can negatively impact
    page performance and may cause crashes during test automation due to extensive
    DOM mutation tracking.
  * `momentic quarantine list` command added to print tests that are quarantined.

  ## Bug fixes

  * Smart Waiting improved to handle element location stability when cache cannot
    be used.
  * Updated all libraries with security vulnerabilities in Momentic CLI.
  * AI now considers alternative elements if the original target is ineligible.
  * AI ACTION steps no longer attempt to interact with ineligible elements.
  * Improved V3 element locator agent accuracy and reduced false positives.
  * Removed conflict resolution dialog between editor and disk state; simplified
    auto-save behavior.
  * Fixed visual bug preventing AI ACTION steps from adding Child steps correctly.
  * Improved load times for Quarantine rules.
  * Responses from recorded or mocked network calls are no longer redacted due to
    memory limits.
  * Error messages now correctly reference a step’s position within a test.
  * Fixed incorrect detection of element changes between cache resolution and
    interaction.
  * Reduced memory usage associated with storing network requests
  * Resolved visual bug where Copilot could significantly extend page height.
</Update>

<Update label="Oct 2025">
  ## Features

  * Tests that are Quarantined are now labeled as such in the Analytics page.
  * Type steps now support using relative positioning when interacting with an
    element.
  * V3 models for assertions, visual assertions, and locators are now in beta and
    can be enabled in Settings.
  * More verbose logs for long-running scripts are now shown in the Console tab.
  * Added a column in the Quarantine table for the last date the test was run.
  * Icon elements using the `<i>` tag are now visible in the a11y tree.

  ## Bug fixes

  * Fixed a bug that caused caches to reset to the original cache after Element
    Check steps executed.
  * Resolved an issue where focusing the Cloud app caused unexpected behavior.
  * Resetting a test while it is saving now shows a toast notification instead of
    quietly failing.
  * Test results with many steps are no longer truncated.
  * Locator no longer picks elements based on momentic-id if removed and added
    back into the DOM.
  * Scrolling now works as expected for XML viewers.
  * Larger pages are now pruned more efficiently to prevent delays caused by
    excessive RAM usage.
  * Sorting tests in the Quarantine table now works as expected.
</Update>

<Update label="Sept 2025">
  ## Features

  ### MCP Server

  * Leverage AI models to interact with your local Momentic tests via the desktop
    server.
  * Create and modify your tests without leaving your IDE.
  * Get started using MCP [here](model-context-protocol).

  ### Mobile App

  * Create and run tests written in natural language for Android.
  * Upload your APK and collaborate with your team on testing your mobile app.
  * Check out our [documentation](model-context-protocol) and get started today!

  ### Additional features

  * Support for network [request mocking](request-mocking) for testing your
    frontend without running a backend, overwriting feature flag configurations,
    or testing error states.
  * Revamped Network tab for easier readability and navigation.
  * Tests that are removed from Quarantine no longer reenter Quarantine if they
    fail and must meet the threshold set in the Quarantine rules.

  ## Bug fixes

  * Resolved issue where filtering network logs would show unassociated logs.
  * Longer lists of variables in the Context tab are no longer truncated.
  * AI Extract now supports all valid JSON schemas.
</Update>

<Update label="Aug 2025">
  ## Features

  ### Mobile Support

  * Beta testing for Android [Mobile Support](https://momentic.ai/blog/mobile) is
    now open. [Sign up here](https://momentic.ai/sales)!
  * Author once in natural language and run across iOS (release date TBA) and
    Android. Instant feedback, stable tests, quality that you can trust.

  ### Copilot + MCP

  * [Copilot + MCP](https://momentic.ai/blog/copilot-mcp) now available in the
    Momentic local application.
  * Momentic Copilot with MCP brings natural-language test creation and execution
    directly into your local development workflow.

  ### Failure Recovery

  * [Failure recovery](failure-recovery) enables Momentic to auto-correct and
    retry tests when transient UI or network glitches occur, ensuring only true
    regressions reach your team.
  * Failure recovery can be enabled via your account's
    [Settings](https://app.momentic.ai/settings/ai) or at the per-test level.

  ### Suggestions & GitHub App

  * [Test Suggestions and GitHub](https://momentic.ai/blog/suggestions) app now
    available.
  * Momentic can now review your pull requests, surface relevant test execution
    context, and suggest precise edits you can apply with one click.
  * You can integrate your GitHub account with Momentic today in your account's
    [Settings](https://app.momentic.ai/settings/integrations).

  ### Additional features

  * Rules can now be set to automate test Quarantine in your account
    [Settings](https://app.momentic.ai/settings/quarantine-rules).
  * The GitHub integration can now post status messages directly on associated
    pull requests.
  * Steps can now be edited while a test is running in the Editor.
  * Retries can now be set at the step level.
  * Element Checks can now assert against computed styles.
  * Teardown steps that fail will now fail the entire test.
  * Native Slack app now available. Enable it in your account's
    [Integration](https://app.momentic.ai/settings/integrations) page.
  * [Memory](memory) is now out of beta and available to all Momentic users.
  * AI Extract steps now validate schema before execution with the v2 schema.
  * Default user-agent now appends `Momentic/1.0 (+https://momentic.ai)` as a
    suffix to support anti-botting and Vercel automation, without affecting normal
    application behavior.

  ## Bug fixes

  * Fixed UI bug in the Usage page impacting customers with annual plans.
  * `momentic list` no longer truncates test names.
  * Fixed UI slowness when opening a test in the Repository view.
  * Values of variables in the GraphQL Request step no longer converts to a
    string.
  * AI model configurations in Settings now correctly shows the models in use.
  * Search results in the network viewer now shows only what is passed in the
    search input.
  * AI Action steps now show Before/After screenshots in the Run Viewer.
</Update>

<Update label="July 2025">
  ## Features

  * Added AI Settings to select the AI agent version for locators, assertions,
    visual assertions, and text extraction.
  * Added Browser Settings to toggle Visual Click, zero-opacity elements, and
    Global Locator Redirect.
  * Introduced [Memory (beta)](/memory) to leverage traces from past test runs for
    improved AI consistency and reliability.
  * Tests can now be [Quarantined](/quarantine) to prevent them from failing
    pipelines, either manually or through automated rules.
  * Runs now display additional metadata.
  * Added the ability to duplicate modules.
  * Module parameters now support persistent options for inputs.
  * Rows in Runs and Repository can be opened in a new tab using CMD/CTRL + Click.
  * Element Check now supports assertions on tag names, computed styles, and focus
    state.
  * Added more filters to the Run, Run Groups, and Analytics pages.
  * Updated the Network Viewer UI to show intercepted data.

  ## Bug fixes

  * Test descriptions now correctly update in the side panel when opening tests in
    the Repository.
  * Resolved an issue preventing API key creation.
  * Folders in different directories can now share the same name.
  * Fixed an issue where values in the GraphQL Request step were being converted
    to strings.
  * Screenshots now save correctly in all Runs.
  * Runs and Run Group results load much faster.
  * Moved the interaction mode warning outside the browser preview.
  * Fixed a UI crash when interacting with the Network Viewer.
</Update>

<Update label="June 2025">
  ## Features

  * Support for setup and teardown steps.
  * Hybrid selector mode for locators.
  * New sidebar for the local app that shows all folders.
  * New step to set headers
  * New `momentic list` command for easier integration with CircleCI.
  * Skipped tests are included in JUnit XML reports.
  * New keydown and keyup steps.
  * New step to wait for requests.
  * New module search experience with multiple tabs.
  * Clearer separation of global and local module configurations.
  * Be able to copy environment variable paths and values.
  * Table rows are now links.
  * You can now view initial navigation in the test trace.
  * Page and element check builder now supports syntax highlighting.
  * Labels are included in Junit XML reports.
  * Be able to duplicate modules in the local app.

  ## Bug fixes

  * `momentic import` now supports importing a much larger volume of tests.
  * Fix handling of zero opacity elements.
  * Opening a test link directly in the local app no longer show's an empty page.
  * Ungrouping a module no longer causes duplicate id errors.
  * Drastically improved local app performance and navigation speed.
  * Search query is now debounced.
  * Screenshots in test traces now display with the correct dimensions.
  * Create and edit suite now paginates tests properly.
  * Test options dialog now scrolls.
  * Fixed option parsing for the CLI.
</Update>

<Update label="May 2025">
  ## Momentic 2.0

  We're excited to introduce Momentic 2.0 - a major update with performance
  improvements, new features, and expanded configuration.

  * Test results are now saved locally by default.
  * Caching is now isolated per branch to prevent cross-branch cache
    contamination.
  * Project configuration now supports feature flags, protected branches, new AI
    settings, and more browser controls.
  * Chromium has been updated to the latest version, and Chrome for Testing is now
    supported.
  * Read our [v2.x migration guide](/cli/migrate-v2) for details on how to
    transition.

  ## Features

  * Steps now appear in the module overview panel for easier inspection.
  * Time zone and geolocation can be configured in test options to simulate
    various regions.
  * Option to ignore href attributes in anchor tags.
  * Option to invalidate cache when an element's bounding box changes.
  * Local app search now includes all tests and modules within nested directories
    and subdirectories.

  ## Bug fixes

  * Improved handling of long page content to prevent selector errors on pages
    with a lot of HTML.
  * Credits in the billing view now properly reflect additions and rollovers.
  * Improved locators to distinguish between nearly identical elements.
  * Tests now honor the configured retry count when screenshots fail to capture.
  * Dropdowns with a large number of options are now scrollable.
</Update>

<Update label="April 2025">
  ## Features

  * Improved accuracy of recording on lengthy sites.
  * [Switch tab](/steps/switch-tab) now accepts template strings.
  * Download HTML and Download A11y tree in the debug pane of the test editor.
  * New CLI option to ignore autogenerated `href` attributes.
  * Tests can now be duplicated directly from the app.

  ## Bug fixes

  * React components that change classes no longer bust the cache.
  * [Failure recovery](/failure-recovery) no longer removes
    [Element Check](/steps/element-check) if they fail during a test.
  * Resolved an issue where scrolling in the browser preview or during
    [Scroll](/steps/scroll) steps did not match real-world behavior.
  * Fixed an issue that would sometimes cause the usage breakdown graph in Billing
    to not populate.
  * Changing the name of a module locally now updates the file name to match.
  * Addressed a compatibility issue where
    [PostHog introduced a breaking change](https://github.com/PostHog/posthog-js-lite/issues/491)
    affecting users with Node.js versions 20.19.0 or older. Pinned and
    shrinkwrapped PostHog to version 4.15.0 to prevent future failures.
</Update>

<Update label="March 2025">
  ## Features

  * You can now upload files directly in Momentic. Use the
    [File Upload](/steps/file-upload) step to upload files to your application
    during tests.
  * New search for modules in the editor.
  * Updated the repository's tree structure to support arbitrary folder nesting,
    making it easier to organize your tests and modules.

  ## Bug fixes

  * Uploading files larger than 5MB no longer causes a full-page error.
  * [Element check](/steps/element-check) now supports empty strings.
  * Assertions no longer cause elements to scroll into view.
  * Tests will no longer auto-save if validation errors are present.
  * Negative assertion results are no longer cached, ensuring accuracy.
  * Resolved navigation errors between multiple run attempts.
  * Local YAML test files will remain unchanged unless explicitly modified.
</Update>

<Update label="February 2025">
  ## Features

  * [AI action](/steps/ai-action) has improved reasoning and self-healing
    capabilities.
  * Test runs with multiple attempts now allow viewing results for all attempts.
  * Momentic now displays Git information for CLI-executed tests.

  ## Bug fixes

  * Momentic now correctly sets MIME types for uploaded files.
  * Fixed incorrect labeling of tests running on main branches as `HEAD`.
  * Suite-level environments now correctly override individual test environments.
  * Addressed an issue preventing removal or modification of scheduled tests.
  * `npx momentic queue test` no longer queues disabled tests.

  ## Data retention policy updates

  * Screenshots and stop-level details will be kept for 3 months.
  * Run metadata will be kept for 6 months.
  * Analytics will be available indefinitely.
</Update>

<Update label="January 2025">
  ## Features

  * Analytics loads much faster and provides helpful insights to identify failing
    or flaky tests tests.
  * You can now view suite analytics, which aggregates analytics for all tests in
    a suite.
  * You can now view historical credit usage for suites and tests.
  * There are now steps in the editor for copy and pasting to and from the
    clipboard.
  * The editor now has a refresh button to refresh the page.
  * New buttons in the editor to move a step to the top or bottom of the test.
  * Suites now support setup and teardown.

  ## Bug fixes

  * Enabled `--headless=new` on Chromium
  * [AI action](/steps/ai-action) now supports interpolated variables.
  * Creating a new test when viewing a folder now adds it to that folder.
  * Selecting more than 40 tests per page when creating suites no longer breaks
    the dialog.
  * Test export now exports labels.
  * Duplicated tests are now created in the same folder as the original.
  * Accepting email invites no longer fails with 500 errors.
</Update>

<Update label="December 2024">
  ## Failure recovery (beta)

  * Review proposed steps in the run viewer and apply them directly to tests
    stored on Cloud or your local machine through a CLI command.
  * Can be enabled on a per-test basis or globally in organization settings.

  ## Test and suite cancellation

  * Tests and suites running on Momentic Cloud can now be cancelled through the
    UI.

  ## Usage statistics

  * You can now view usage statistics for your organization in
    [settings](https://app.momentic.ai/settings/usage).

  ## AI improvements

  * We have developed a new v1 AI agents for locating elements and evaluating
    assertions that perform 17% better on our benchmarks.
  * These agents should return more detailed thoughts and reasoning steps.
  * We back-tested these agents extensively and followed a gradual rollout process
    in the last few weeks. v1 agents are now the default for all organizations.

  ## Bug fixes

  * Fix a bug where the [Page check](/steps/page-check) assertions would fail
    because fetching the HTML took too long.
  * Improve the exponential backoff algorithm for [Page check](/steps/page-check)
    assertions, which sometimes led to lengthy pauses.
  * Improve execution logic when running an individual step within a module; if
    all sub-steps of a module have been ran individually, the module as a whole is
    marked as complete now.
  * Fix the logic for the "run to end" button when running a cached module.
  * Reduce memory and CPU usage caused by streaming browser screenshots.
  * Bump the max number of tokens that can be generated by AI agents for
    [AI check](/steps/ai-check) steps.
  * Create a randomized test ID when importing a new test via ZIP file into the
    cloud app.
  * Restore the feature of test auto-saving on load in the editor.
  * Fix rare cases of the Chrome browser hanging indefinitely due to an underlying
    Chromium bug.
</Update>

<Update label="November 2024">
  ## New test tree view

  * Click on a test in the tree view to view detailed information about the test.
    Including the steps, estimated credits, and included modules.
  * Duplicate a test with a new name.
  * Manually run tests against different environments.
  * Delete a test directly from the tree view.
  * Manage labels and suites directly from the test view.
  * Schedule tests directly from the test view.
  * Configure and customize notifications that you receive from Momentic. You can
    use variables and test data to make it more informative.

  ## Step updates

  * [Wait for URL](/steps/wait-for-url) now supports case insensitive matching and
    negative matching.
  * [AI check](/steps/ai-check) now support vision-only mode that is tuned for
    visual checks.
  * A module can now be treated as a auth module. This will automatically save and
    restore the state of the module. Turn on "Treat as auth module" to enable this
    feature.
  * You can now use XY coordinates to target elements. This is useful when you
    want to click on a specific part of the screen.
  * Pressing keys now supports a delay between each key press. This is useful when
    you want to simulate typing.
  * Empty string is a valid value for the [Type](/steps/type) step.

  ## Debug data

  You can now see the HTML as well as the a11y tree in the editor and the test
  results. This will help you debug issues with your tests. We've also made
  updates to the console log and network logs viewers.

  ## Suites

  You can now set a default environment for a suite. This will be used when
  running tests in the suite.

  ## Reporting

  The CLI now supports outputting JUnit XML reports for test runs. You can use
  this to integrate with your CI/CD pipeline.

  ## Knowledge base

  We now have a dedicated knowledge base for customers to share detailed guides
  and tutorials. You can access it [here](https://support.momentic.ai) if you're a
  current customer.

  ## Performance

  We've written an in-depth guide on Momentic's performance characteristics. Check
  it out [here](/performance).

  ## Bug fixes

  * Fixed a race condition when updating results.
  * Locator redirection now works in shadow roots.
  * Fixed concurrency issues with the Chromium browser in the CLI.
  * Include IndexDB in saved and restored auth state.
  * Updated mirror for stable channel Chrome.
  * Improved table serialization.
  * Updated [File upload](/steps/file-upload) URL validation.
  * Retry failed email requests.
  * Fixed drag and drop.
  * Scroll now wait for the scroll to complete.
  * Updated the create suite dialogs to support >35 tests at a time.
  * Don't throw an error if a click times out after completion.
  * Make sure ungrouped steps have new ids.
  * Support Node 18 in the CLI.
  * Search will now preserve folders when searching.
</Update>


# CircleCI
Source: https://momentic.ai/docs/ci/circleci



The following example shows how to use Momentic with
[CircleCI](https://circleci.com/).

For more usage examples, see the
[momentic-ai/examples](https://github.com/momentic-ai/examples) repository.

For a given root `package.json`:

```json package.json theme={null}
{
  "name": "my-momentic-repo",
  "scripts": {},
  "devDependencies": {
    "momentic": "latest"
  }
}
```

Create a file called `.circleci/config.yml` in your repository with the
following contents:

```yaml config.yml theme={null}
version: 2.1
orbs:
  node: circleci/node@5.0.2
workflows:
  test:
    jobs:
      - test
jobs:
  test:
    docker:
      - image: cimg/node:lts
    steps:
      - checkout
      - node/install-packages

      - run:
          name: Install browsers
          command: npx momentic install-browsers --all

      - run:
          name: Run Momentic tests
          command: npx momentic run
          when: always

      - run:
          name: Upload results
          command: npx momentic results upload test-results
          when: always
```

## Authentication

To run any commands, you must authenticate with Momentic. You can do this by
setting the `MOMENTIC_API_KEY` environment variable in your CircleCI project
settings.

1. Create an API key in
   [Momentic Cloud](https://app.momentic.ai/settings/api-keys).

<Frame>
  <img />
</Frame>

Copy the value to a safe place. You'll need it in a moment.

2. Go to your CircleCI project settings and click on the **Environment
   Variables** tab. Create a new secret called `MOMENTIC_API_KEY` and enter the
   value of your API key.

<Frame>
  <img />
</Frame>

<Frame>
  <img />
</Frame>

3. CircleCI automatically loads environment variables stored in project settings
   into the CI environment. No modifications are necessary for the CI file.

## Sharding

If you have a large test suite, you can use sharding to run tests in parallel.
This can significantly speed up your CI runs.

To shard the test suite, pass the `--shard-index` and `--shard-count` options to
the `momentic run` command. The `shard-index` is the index of the current shard
(starting from 1), and `shard-count` is the total number of shards.

In order to collect test results inside a single run group in Momentic cloud,
you need to add a separate step after all tests complete to merge and upload
results.

```yaml config.yml theme={null}
version: 2.1
orbs:
  node: circleci/node@5.0.2

jobs:
  run-tests:
    parallelism: 2
    executor: node/default
    steps:
      - checkout
      - node/install-packages

      - run:
          name: Install browsers
          command: npx momentic install-browsers --all

      - run:
          name: Run tests
          command: |
            npx momentic run \
              --output-dir test-results/shard-${CIRCLE_NODE_INDEX} \
              --shard-index $(($CIRCLE_NODE_INDEX+1)) \
              --shard-count ${CIRCLE_NODE_TOTAL}

      - store_artifacts:
          when: always
          path: ./test-results

      - persist_to_workspace:
          when: always
          root: .
          paths:
            - test-results

  upload-results:
    executor: node/default
    steps:
      - checkout
      - node/install-packages

      - attach_workspace:
          at: .

      - run:
          name: Merge test results
          command: npx momentic results merge --output-dir test-results/merged test-results

      - run:
          name: Upload test results
          command: npx momentic results upload test-results/merged

workflows:
  test:
    jobs:
      - run-tests
      - upload-results:
          requires:
            - run-tests:
              - success
              - failed
```


# Custom setups
Source: https://momentic.ai/docs/ci/custom-setups



The following guide contains useful information for using Momentic in custom CI
setups.

## Best practices

Most CI providers set the `CI` environment variable to `true` by default. This
allows Momentic to automatically detect when tests are being run in CI. In
custom setups, this isn't always the case.

We recommend setting the environment variable `CI=true` to enable all CI-related
features by default and more closely mimic standard CI environments.

## Saving caches

By default, Momentic CLI does not save caches for test runs on the configured
git main branch. This is to prevent developers from accidentally polluting those
caches when building tests locally.

In standard CI setups like GitHub Actions, GitLab CI, and Travis CI, Momentic
can automatically infer that tests are being run in a CI environments and
override this behavior to save caches. However, in custom CI setups, you need to
pass the --save-cache flag to the run command in order to enable cache saving.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --save-cache [options] [tests...]
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --save-cache [options] [tests...]
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --save-cache [options] [tests...]
  ```
</CodeGroup>

<Tip>
  We recommend always saving caches during CI runs in order to ensure optimal
  performance and consistency.
</Tip>

You can read more about caching in Momentic in the [docs](/step-cache).

## Git metadata

Momentic collects git metadata during test runs in order to power several
features:

* Cache isolation
* Test run traceability
* GitHub status messages

And more.

In order to collect this data, Momentic relies on either the git CLI tool or
special handling for specific CI providers. Some custom CI setups may not have
git installed or might have incomplete information.

In order to provide the metadata manually, you can set any combination of the
following environment variables. All of these are optional, but providing more
information will lead to better results.

<Tip>
  In order to get the best caching performance possible, we recommend providing
  at least `GIT_BRANCH_NAME`, `GIT_COMMIT_SHA`, `GIT_COMMIT_TIMESTAMP`,
  `LAST_COMMIT_ON_MAIN_SHA`, `LAST_COMMIT_ON_MAIN_TIMESTAMP`, and if possible
  `MERGED_GIT_BRANCH_NAME`.
</Tip>

* `MOMENTIC_GIT_OVERRIDE=true`: must be set to enable git metadata overrides
* `GIT_COMMIT_SHA`: the full commit SHA
* `GIT_COMMIT_SHA_SHORT`: the short commit SHA (if not provided, this will be
  derived from the full SHA)
* `GIT_COMMIT_TIMESTAMP`: the current commit timestamp in ISO 8601 format
* `GIT_BRANCH_NAME`: the current branch name
* `GIT_ORIGIN_URL`: the git origin URL
* `GIT_COMMIT_AUTHOR_NAME`: the commit author's name
* `GIT_COMMIT_MESSAGE`: the commit message
* `LAST_COMMIT_ON_MAIN_SHA`: the full commit SHA of the last commit on main.
  When using git, this is the output of running `git merge-base main HEAD`. On
  main, this is the current commit SHA.
* `LAST_COMMIT_ON_MAIN_TIMESTAMP`: the commit timestamp of
  `LAST_COMMIT_ON_MAIN_SHA` in ISO 8601 format.
* `MERGED_GIT_BRANCH_NAME`: when on main, the name of the branch that was merged
  to create the current commit. This is usually derived from pull/merge requests
  using our GitHub/GitLab integrations.
* `GITHUB_REPOSITORY`: the GitHub repository name in the format `owner/repo` (if
  applicable)
* `GITLAB_PROJECT_PATH`: the GitLab project path in the format
  `group/subgroup/repo` (if applicable)
* `GIT_USERNAME`: the username of the current git user (if applicable)
* `GIT_EMAIL`: the email of the current git user (if applicable)
* `GIT_NAME`: the name of the current git user (if applicable)


# GitHub Actions
Source: https://momentic.ai/docs/ci/github-actions



The following example shows how to use Momentic with
[GitHub Actions](https://github.com/features/actions).

For more usage examples, see the
[momentic-ai/examples](https://github.com/momentic-ai/examples) repository.

For a given root `package.json`:

```json package.json theme={null}
{
  "name": "my-momentic-repo",
  "scripts": {},
  "devDependencies": {
    "momentic": "latest"
  }
}
```

Create a file called `.github/workflows/ci.yml` in your repository with the
following contents:

```yaml ci.yml theme={null}
name: CI

on:
  push:
    branches: ["main"]
  pull_request:
    types: [opened, synchronize]

jobs:
  build:
    name: Test
    timeout-minutes: 15
    runs-on: ubuntu-latest

    steps:
      - name: Check out code
        uses: actions/checkout@v4
        with:
          fetch-depth: 2

      - name: Setup Node.js environment
        uses: actions/setup-node@v4
        with:
          node-version: 20.19.0
          cache: "npm"

      - name: Install dependencies
        run: npm install

      - name: Install browsers
        run: npx momentic install-browsers --all

      - name: Test
        run: npx momentic run

      - name: Upload results
        if: always()
        run: npx momentic results upload test-results
```

## Authentication

To run any commands, you must authenticate with Momentic. You can do this by
adding the `MOMENTIC_API_KEY` environment variable to your GitHub Actions
workflow.

1. Create an API key in
   [Momentic Cloud](https://app.momentic.ai/settings/api-keys).

<Frame>
  <img />
</Frame>

Copy the value to a safe place. You'll need it in a moment.

2. Go to your GitHub repository settings and click on the **Secrets** and then
   **Actions** tab. Create a new secret called `MOMENTIC_API_KEY` and enter the
   value of your API key.

<Frame>
  <img />
</Frame>

<Frame>
  <img />
</Frame>

3. At the top of your GitHub Actions workflow, provide the following environment
   variables to jobs that use `momentic`:

```yaml ci.yml {8-10} theme={null}
# ...

jobs:
  build:
    name: Build and Test
    timeout-minutes: 15
    runs-on: ubuntu-latest
    # To authenticate, set the following environment variables.
    env:
      MOMENTIC_API_KEY: ${{ secrets.MOMENTIC_API_KEY }}

    steps:
      - name: Check out code
        uses: actions/checkout@v4
        with:
          fetch-depth: 2
    # ...
```

## Sharding

If you have a large test suite, you can use sharding to run tests in parallel.
This can significantly speed up your CI runs.

To shard the test suite, pass the `--shard-index` and `--shard-count` options to
the `momentic run` command. The `shard-index` is the index of the current shard
(starting from 1), and `shard-count` is the total number of shards.

In order to collect test results inside a single run group in Momentic cloud,
you need to add a separate step after all tests complete to merge and upload
results.

```yaml ci.yml theme={null}
name: CI

on:
  push:
    branches: ["main"]
  pull_request:
    types: [opened, synchronize]

jobs:
  run-tests:
    name: Run tests
    runs-on: ubuntu-latest
    strategy:
      fail-fast: false
      matrix:
        shardIndex: [1, 2]
        shardTotal: [2]
    steps:
      - name: Check out code
        uses: actions/checkout@v4
        with:
          fetch-depth: 2

      - name: Setup Node.js environment
        uses: actions/setup-node@v4
        with:
          node-version: 20.19.0
          cache: "npm"

      - name: Install dependencies
        run: npm install

      - name: Install browsers
        run: npx momentic install-browsers --all

      - name: Test
        run: |
          npx momentic run \
            --output-dir test-results/shard-${{ matrix.shardIndex }} \
            --shard-index ${{ matrix.shardIndex }} \
            --shard-count ${{ matrix.shardTotal }}

      - name: Save test results artifact
        uses: actions/upload-artifact@v4
        if: always()
        with:
          name: test-results-${{ matrix.shardIndex }}
          path: ./test-results
          retention-days: 1

  upload-results:
    name: Merge and upload test results
    runs-on: ubuntu-latest
    if: always()
    timeout-minutes: 5
    needs:
      - run-tests

    steps:
      - name: Check out code
        uses: actions/checkout@v4
        with:
          fetch-depth: 2

      - name: Setup Node.js environment
        uses: actions/setup-node@v4
        with:
          node-version: 20.19.0
          cache: "npm"

      - name: Install dependencies
        run: npm install

      - name: Download all test results artifacts
        uses: actions/download-artifact@v4
        with:
          path: ./test-results
          pattern: test-results-*
          merge-multiple: true

      - name: Merge test results
        run: npx momentic results merge --output-dir test-results/merged test-results

      - name: Upload test results to Momentic
        run: npx momentic results upload test-results/merged
```


# GitLab CI
Source: https://momentic.ai/docs/ci/gitlab-ci



The following example shows how to use Momentic with
[GitLab CI](https://docs.gitlab.com/runner/).

For more usage examples, see the
[momentic-ai/examples](https://github.com/momentic-ai/examples) repository.

For a given root `package.json`:

```json package.json theme={null}
{
  "name": "my-momentic-repo",
  "scripts": {},
  "devDependencies": {
    "momentic": "latest"
  }
}
```

Create a file called `gitlab-ci.yml` in your repository with the following
contents:

```yaml gitlab-ci.yml theme={null}
image: node:latest
stages:
  - build
build:
  stage: build
  script:
    - npm install
    - npx momentic install-browsers --all
    - npx momentic run
  after_script:
    - npx momentic results upload test-results
```

## Authentication

To run any commands, you must authenticate with Momentic. You can do this by
adding the `MOMENTIC_API_KEY` environment variable to your GitLab CI workflow.

1. Create an API key in
   [Momentic Cloud](https://app.momentic.ai/settings/api-keys).

<Frame>
  <img />
</Frame>

Copy the value to a safe place. You'll need it in a moment.

2. Go to your GitLab repository settings and click on the **Settings** and then
   **CI/CD** tab. Create a new variable called `MOMENTIC_API_KEY` and enter the
   value of your API key.

<Frame>
  <img />
</Frame>

<Frame>
  <img />
</Frame>

3. GitLab CI automatically loads environment variables stored in project
   settings into the CI environment. No modifications are necessary for the CI
   file.

## Sharding

If you have a large test suite, you can use sharding to run tests in parallel.
This can significantly speed up your CI runs.

To shard the test suite, pass the `--shard-index` and `--shard-count` options to
the `momentic run` command. The `shard-index` is the index of the current shard
(starting from 1), and `shard-count` is the total number of shards.

In order to collect test results inside a single run group in Momentic cloud,
you need to add a separate step after all tests complete to merge and upload
results.

```yaml gitlab-ci.yml theme={null}
image: node:latest
stages:
  - test
  - merge-results

test:
  stage: test
  script:
    - npm install
    - npx momentic install-browsers --all
    - npx momentic run --shard-index=$CI_NODE_INDEX --shard-count=$CI_NODE_TOTAL --output-dir test-results/shard-$CI_NODE_INDEX
  parallel: 2
  artifacts:
    paths:
      - test-results
    expire_in: 12 hours
    when: always

merge-results:
  stage: merge-results
  when: always
  dependencies:
    - test
  script:
    - npm install
    - npx momentic results merge --output-dir test-results/merged test-results
    - npx momentic results upload test-results/merged
```


# Jenkins
Source: https://momentic.ai/docs/ci/jenkins



The following example shows how to use Momentic with
[Jenkins](https://www.jenkins.io/).

For more usage examples, see the
[momentic-ai/examples](https://github.com/momentic-ai/examples) repository.

For a given root `package.json`:

```json package.json theme={null}
{
  "name": "my-momentic-repo",
  "scripts": {},
  "devDependencies": {
    "momentic": "latest"
  }
}
```

Create a file called `Jenkinsfile` in your repository with the following
contents:

```java Jenkinsfile theme={null}
pipeline {
    agent any

    tools {
        nodejs 'NodeJS 20'
    }

    stages {
        stage('Checkout Code') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'npm ci'
            }
        }

        stage('Install Browsers for Momentic') {
            steps {
                sh 'npx momentic install-browsers --all'
            }
        }

        stage('Run Momentic Tests and Upload Results') {
            steps {
                sh 'npx momentic run'
            }
            post {
                always {
                    sh 'npx momentic results upload test-results'
                }
            }
        }
    }
}
```

## Authentication

To run any commands, you must authenticate with Momentic. You can do this by
adding the `momentic-api-key` credential to your Jenkins instance.

1. Create an API key in
   [Momentic Cloud](https://app.momentic.ai/settings/api-keys).

<Frame>
  <img />
</Frame>

Copy the value to a safe place. You'll need it in a moment.

2. Add a new global credential to your Jenkins controller.

<Frame>
  <img />
</Frame>

3. At the top of your `Jenkinsfile`, provide the following environment variables
   to the pipeline:

```java Jenkinsfile {4-7} theme={null}
pipeline {
    agent any

    // To authenticate, set the following environment variables.
    environment {
        MOMENTIC_API_KEY = credentials('momentic-api-key')
    }

    // ...
}
```


# Travis CI
Source: https://momentic.ai/docs/ci/travis-ci



The following example shows how to use Momentic with
[Travis CI](https://docs.travis-ci.com/).

For more usage examples, see the
[momentic-ai/examples](https://github.com/momentic-ai/examples) repository.

For a given root `package.json`:

```json package.json theme={null}
{
  "name": "my-momentic-repo",
  "scripts": {},
  "devDependencies": {
    "momentic": "latest"
  }
}
```

Create a file called `.travis.yml` in your repository with the following
contents:

```yaml .travis.yml theme={null}
language: node_js
node_js:
  - lts/*
install:
  - npm install
script:
  - npx momentic run
after_script:
  - npx momentic results upload test-results
```

## Authentication

To run any commands, you must authenticate with Momentic. You can do this by
adding the `MOMENTIC_API_KEY` environment variable to your Travis CI workflow.

1. Create an API key in
   [Momentic Cloud](https://app.momentic.ai/settings/api-keys).

<Frame>
  <img />
</Frame>

Copy the value to a safe place. You'll need it in a moment.

2. Go to your Travis repository settings and scroll down to the Environment
   Variables section. Create a new variable called `MOMENTIC_API_KEY` and enter
   the value of your API key.

<Frame>
  <img />
</Frame>

3. Travis CI automatically loads environment variables stored in project
   settings into the CI environment. No modifications are necessary for the CI
   file.


# app
Source: https://momentic.ai/docs/cli/commands/app



Start the Momentic app.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic app [options]
  ```

  ```bash yarn theme={null}
  yarn dlx momentic app [options]
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic app [options]
  ```
</CodeGroup>

## Options

### `-c, --config <config>`

Path to the Momentic configuration file. If not specified, it defaults to
`momentic.config.yaml` in the current directory.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic app --config path/to/momentic.config.yaml
  ```

  ```bash yarn theme={null}
  yarn dlx momentic app --config path/to/momentic.config.yaml
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic app --config path/to/momentic.config.yaml
  ```
</CodeGroup>

### `--disable-cache`

Disable caching entirely. This will cause all steps to run without cached data,
and not save caches after runs. This can result in slower test execution, but
ensures that all steps are run fresh without stored data.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic app --disable-cache
  ```

  ```bash yarn theme={null}
  yarn dlx momentic app --disable-cache
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic app --disable-cache
  ```
</CodeGroup>

### `--save-cache`

Always save updated step caches after successful test runs, even on the main Git
branch and protected Git branches. Please see the
[cache saving eligibility](/step-cache#cache-saving-eligibility) documentation
for more information.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic app --save-cache
  ```

  ```bash yarn theme={null}
  yarn dlx momentic app --save-cache
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic app --save-cache
  ```
</CodeGroup>


# apply
Source: https://momentic.ai/docs/cli/commands/apply



## `patch`

Apply patch changes to your Momentic tests.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic apply patch [options]
  ```

  ```bash yarn theme={null}
  yarn dlx momentic apply patch [options]
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic apply patch [options]
  ```
</CodeGroup>

### Options

### `-c, --config <config>`

Path to the Momentic configuration file. If not specified, it defaults to
`momentic.config.yaml` in the current directory.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic apply patch --config path/to/momentic.config.yaml
  ```

  ```bash yarn theme={null}
  yarn dlx momentic apply patch --config path/to/momentic.config.yaml
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic apply patch --config path/to/momentic.config.yaml
  ```
</CodeGroup>

### `-f, --filter <filter>`

Only applicable when using [Workspaces](/cli/workspace). Loads the project with
the specified name.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic apply patch --filter workspace-name
  ```

  ```bash yarn theme={null}
  yarn dlx momentic apply patch --filter workspace-name
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic apply patch --filter workspace-name
  ```
</CodeGroup>

#### `--from <from>`

The identifier of the patch to apply. It consists of three random words
separated by dashes, like `potato-apple-cherry`.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic apply patch --from potato-apple-cherry
  ```

  ```bash yarn theme={null}
  yarn dlx momentic apply patch --from potato-apple-cherry
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic apply patch --from potato-apple-cherry
  ```
</CodeGroup>

#### `--to <to>`

The test name to apply the patch to.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic apply patch --from potato-apple-cherry --to example-test
  ```

  ```bash yarn theme={null}
  yarn dlx momentic apply patch --from potato-apple-cherry --to example-test
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic apply patch --from potato-apple-cherry --to example-test
  ```
</CodeGroup>


# check
Source: https://momentic.ai/docs/cli/commands/check



## `duplicate-ids`

Ensure that there are no duplicate step and command IDs in your tests and
modules. This is important for maintaining the integrity of your caches and
avoiding conflicts during execution.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic check duplicate-ids
  ```

  ```bash yarn theme={null}
  yarn dlx momentic check duplicate-ids
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic check duplicate-ids
  ```
</CodeGroup>

### Options

#### `--fix`

Apply fixes to the duplicate IDs found. This will automatically rename the
duplicate IDs to ensure uniqueness.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic check duplicate-ids --fix
  ```

  ```bash yarn theme={null}
  yarn dlx momentic check duplicate-ids --fix
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic check duplicate-ids --fix
  ```
</CodeGroup>

## `duplicate-names`

Check for duplicate names in your tests and modules. This helps to prevent
confusion and ensures that each test and module are uniquely identified.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic check duplicate-names
  ```

  ```bash yarn theme={null}
  yarn dlx momentic check duplicate-names
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic check duplicate-names
  ```
</CodeGroup>

## `config`

Check your `momentic.config.yaml` for errors.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic check config
  ```

  ```bash yarn theme={null}
  yarn dlx momentic check config
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic check config
  ```
</CodeGroup>

### Options

#### `-c, --config <config>`

Path to the Momentic configuration file. If not specified, it defaults to
`momentic.config.yaml` in the current directory.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic check config --config path/to/momentic.config.yaml
  ```

  ```bash yarn theme={null}
  yarn dlx momentic check config --config path/to/momentic.config.yaml
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic check config --config path/to/momentic.config.yaml
  ```
</CodeGroup>


# import
Source: https://momentic.ai/docs/cli/commands/import



Import all tests, modules, and environments configured on Momentic Cloud to your
local environment.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic import
  ```

  ```bash yarn theme={null}
  yarn dlx momentic import
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic import
  ```
</CodeGroup>

To import a single test and the modules it uses into your local environment,
pass the test path from Momentic Cloud to the import command.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic import <test-path>
  ```

  ```bash yarn theme={null}
  yarn dlx momentic import <test-path>
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic import <test-path>
  ```
</CodeGroup>


# init
Source: https://momentic.ai/docs/cli/commands/init



Initialize a new Momentic project and create a
[configuration file](/cli/configuration).

<CodeGroup>
  ```bash npm theme={null}
  npx momentic init
  ```

  ```bash yarn theme={null}
  yarn dlx momentic init
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic init
  ```
</CodeGroup>


# install-browsers
Source: https://momentic.ai/docs/cli/commands/install-browsers



Install browsers for your Momentic tests. Here are the
[supported browsers](/browsers).

<CodeGroup>
  ```bash npm theme={null}
  npx momentic install-browsers [options] [browsers...]
  ```

  ```bash yarn theme={null}
  yarn dlx momentic install-browsers [options] [browsers...]
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic install-browsers [options] [browsers...]
  ```
</CodeGroup>

* **\[browsers...]**: The browsers to install. You can specify multiple browsers
  separated by spaces. Available browsers are `chromium`, `chrome`, and
  `chrome-for-testing`. You can review the differences between each browser
  [here](/browsers).

## Options

### `--force`

Force the installation of the specified browsers, even if they are already
installed.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic install-browsers chromium --force
  ```

  ```bash yarn theme={null}
  yarn dlx momentic install-browsers chromium --force
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic install-browsers chromium --force
  ```
</CodeGroup>

### `--all`

Install all supported browsers. This is equivalent to specifying `chromium`,
`chrome`, and `chrome-for-testing`.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic install-browsers --all
  ```

  ```bash yarn theme={null}
  yarn dlx momentic install-browsers --all
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic install-browsers --all
  ```
</CodeGroup>


# install-skills
Source: https://momentic.ai/docs/cli/commands/install-skills



Install the Momentic skill so coding assistants get explicit instructions for
using momentic MCP. Without it, agents are more likely to make malformed tool
calls.

Run this after configuring the MCP server. For full setup, see
[MCP](/model-context-protocol).

<CodeGroup>
  ```bash npm theme={null}
  npx momentic install-skills [options] [installPath]
  ```

  ```bash yarn theme={null}
  yarn dlx momentic install-skills [options] [installPath]
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic install-skills [options] [installPath]
  ```
</CodeGroup>

* **\[installPath]**: Optional target directory. **Mutually exclusive with all
  agent flags.** Either provide a path to install to a custom directory, or use
  one agent flag below, never both.

## Options

Use exactly one of these: either a custom `[installPath]` or one of the agent
flags below.

### `--cursor`

Install into Cursor's default skill directory:
`~/.cursor/skills/momentic-test/SKILL.md`

<CodeGroup>
  ```bash npm theme={null}
  npx momentic install-skills --cursor
  ```

  ```bash yarn theme={null}
  yarn dlx momentic install-skills --cursor
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic install-skills --cursor
  ```
</CodeGroup>

### `--claude-code`

Install into Claude Code's default skill directory:
`~/.claude/skills/momentic-test/SKILL.md`

<CodeGroup>
  ```bash npm theme={null}
  npx momentic install-skills --claude-code
  ```

  ```bash yarn theme={null}
  yarn dlx momentic install-skills --claude-code
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic install-skills --claude-code
  ```
</CodeGroup>

### `--codex`

Install into Codex's default skill directory:
`~/.agents/skills/momentic-test/SKILL.md`

<CodeGroup>
  ```bash npm theme={null}
  npx momentic install-skills --codex
  ```

  ```bash yarn theme={null}
  yarn dlx momentic install-skills --codex
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic install-skills --codex
  ```
</CodeGroup>

### `--opencode`

Install into OpenCode's default skill directory:
`~/.config/opencode/skills/momentic-test/SKILL.md`

<CodeGroup>
  ```bash npm theme={null}
  npx momentic install-skills --opencode
  ```

  ```bash yarn theme={null}
  yarn dlx momentic install-skills --opencode
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic install-skills --opencode
  ```
</CodeGroup>

### `--copilot`

Install into Copilot (VS Code)'s default skill directory:
`~/.copilot/skills/momentic-test/SKILL.md`

<CodeGroup>
  ```bash npm theme={null}
  npx momentic install-skills --copilot
  ```

  ```bash yarn theme={null}
  yarn dlx momentic install-skills --copilot
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic install-skills --copilot
  ```
</CodeGroup>

### Custom path

Install into a custom directory. The command creates `SKILL.md` in the given
path.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic install-skills ~/my/custom/skills/momentic-test
  ```

  ```bash yarn theme={null}
  yarn dlx momentic install-skills ~/my/custom/skills/momentic-test
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic install-skills ~/my/custom/skills/momentic-test
  ```
</CodeGroup>


# list
Source: https://momentic.ai/docs/cli/commands/list



<Info>**Prerequisites**: These tests must exist locally as YAML files.</Info>

List tests in the current project.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic list [options] [tests...]
  ```

  ```bash yarn theme={null}
  yarn dlx momentic list [options] [tests...]
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic list [options] [tests...]
  ```
</CodeGroup>

* **\[tests...]**: The tests to list. If not specified, selects all tests in the
  current project. You can specify multiple tests separated by spaces, test
  paths, or folder paths. You can also pass substrings to match test names.

## Options

### `-c, --config <config>`

Path to the Momentic configuration file. If not specified, it defaults to
`momentic.config.yaml` in the current directory.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic list --config path/to/momentic.config.yaml
  ```

  ```bash yarn theme={null}
  yarn dlx momentic list --config path/to/momentic.config.yaml
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic list --config path/to/momentic.config.yaml
  ```
</CodeGroup>

### `-f, --filter <filter>`

Only applicable when using [Workspaces](/cli/workspace). Loads the project with
the specified name.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic list --filter workspace-name
  ```

  ```bash yarn theme={null}
  yarn dlx momentic list --filter workspace-name
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic list --filter workspace-name
  ```
</CodeGroup>

### `--labels <labels...>`

Run tests with the specified labels. This allows you to filter tests based on
assigned labels.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic list --labels smoke regression
  ```

  ```bash yarn theme={null}
  yarn dlx momentic list --labels smoke regression
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic list --labels smoke regression
  ```
</CodeGroup>

### `--include <includePatterns...>`

Only include tests that match the provided regex patterns. Multiple patterns can
be provided. The patterns will be matched against the test file paths and the
pattern only needs to match a part of the path for the test to be included.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic list --include "billing*"
  ```

  ```bash yarn theme={null}
  yarn dlx momentic list --include "billing*"
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic list --include "billing*"
  ```
</CodeGroup>

### `--exclude <excludePatterns...>`

The opposite of `--include`: a test that matches any of the provided regex
patterns will be excluded from running.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic list --exclude "billing*"
  ```

  ```bash yarn theme={null}
  yarn dlx momentic list --exclude "billing*"
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic list --exclude "billing*"
  ```
</CodeGroup>


# mcp
Source: https://momentic.ai/docs/cli/commands/mcp



Start the MCP (Model Context Protocol) server over stdio so coding assistants
can create, edit, and run Momentic tests. For full setup instructions see
[MCP](/model-context-protocol).

All options below can be passed as flags or, where noted, set via environment
variables. CLI flags override environment variables.

```bash theme={null}
npx momentic mcp [options]
```

## Options

| Setting                         | Flag                                       | Environment variable                    | Description                                                                                                                          |
| ------------------------------- | ------------------------------------------ | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Momentic API key                | `--api-key <key>`                          | `MOMENTIC_API_KEY`                      | Authenticates the MCP server with Momentic APIs.                                                                                     |
| Config file path                | `-c`, `--config <path>`                    | —                                       | Points to the `momentic.config.yaml` file used to load project tests, modules, and environments.                                     |
| Headful browser (default: true) | `--headful-browser [true or false]`        | `MOMENTIC_HEADFUL_BROWSER`              | Sets whether browser sessions launch with a visible UI (`true`) or in headless mode (`false`).                                       |
| Device pixel ratio              | `--pixel-ratio <n>`                        | —                                       | Overrides viewport DPR used for browser rendering. Defaults to `2` on macOS Retina and `1` on other setups.                          |
| Session idle timeout            | `--session-idle-timeout-minutes <minutes>` | `MOMENTIC_SESSION_IDLE_TIMEOUT_MINUTES` | Idle timeout for MCP sessions in minutes. Sessions inactive for this duration are terminated automatically. Defaults to `5` minutes. |

### `--api-key <key>`

Momentic API key.

```bash theme={null}
npx momentic mcp --api-key your-api-key
```

### `-c, --config <path>`

Path to the `momentic.config.yaml` file. Required when run from an MCP client;
use an absolute path so the server can resolve it correctly.

```bash theme={null}
npx momentic mcp --config /absolute/path/to/momentic.config.yaml
```

### `--headful-browser [true|false]`

Whether to launch MCP session browsers with a visible UI (`true`) or in headless
mode (`false`). Defaults to `true`.

```bash theme={null}
npx momentic mcp --headful-browser false
```

### `--pixel-ratio <n>`

Device pixel ratio for browser rendering. Defaults to `2` on macOS Retina and
`1` elsewhere.

```bash theme={null}
npx momentic mcp --pixel-ratio 2
```

### `--session-idle-timeout-minutes <minutes>`

Session idle timeout in minutes. MCP sessions that remain idle for this duration
are automatically terminated. Defaults to `5` minutes. Can also be set via the
`MOMENTIC_SESSION_IDLE_TIMEOUT_MINUTES` environment variable.

```bash theme={null}
npx momentic mcp --session-idle-timeout-minutes 5
```


# quarantine
Source: https://momentic.ai/docs/cli/commands/quarantine



Quarantine and unquarantine tests

## `add`

Quarantine a test so that it is skipped in all pipelines.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic quarantine add [options] <test>
  ```

  ```bash yarn theme={null}
  yarn dlx momentic quarantine add [options] <test>
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic quarantine add [options] <test>
  ```
</CodeGroup>

* **\<test>**: The test to quarantine. If not specified, you will be prompted
  to select one interactively.

### Options

#### `--reason <reason>`

The reason for quarantining the test. This will be displayed in the Momentic
Cloud UI to help with debugging.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic quarantine add --reason <reason> <test>
  ```

  ```bash yarn theme={null}
  yarn dlx momentic quarantine add --reason <reason> <test>
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic quarantine add --reason <reason> <test>
  ```
</CodeGroup>

## `list`

List quarantined tests.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic quarantine list
  ```

  ```bash yarn theme={null}
  yarn dlx momentic quarantine list
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic quarantine list
  ```
</CodeGroup>

## `remove`

Unquarantine a test so that it is no longer skipped in pipelines.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic quarantine remove [options] <test>
  ```

  ```bash yarn theme={null}
  yarn dlx momentic quarantine remove [options] <test>
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic quarantine remove [options] <test>
  ```
</CodeGroup>

* **\<test>**: The test to unquarantine. If not specified, you will be prompted
  to select one interactively.

### Options

#### `--reason <reason>`

The reason for unquarantining the test. This is optional, but can be useful for
record-keeping purposes.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic quarantine remove --reason <reason> <test>
  ```

  ```bash yarn theme={null}
  yarn dlx momentic quarantine remove --reason <reason> <test>
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic quarantine remove --reason <reason> <test>
  ```
</CodeGroup>


# queue
Source: https://momentic.ai/docs/cli/commands/queue



<Info>
  **Prerequisites**: These tests and suites must exist in Momentic Cloud.
</Info>

Queue tests and suites to run in Cloud on Momentic infrastructure.

## `tests`

<CodeGroup>
  ```bash npm theme={null}
  npx momentic queue tests [options] <tests...>
  ```

  ```bash yarn theme={null}
  yarn dlx momentic queue tests [options] <tests...>
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic queue tests [options] <tests...>
  ```
</CodeGroup>

* **\<tests...>**: The names of the tests to run. You can specify multiple
  tests separated by spaces.

### Options

#### `--custom-headers <customHeaders...>`

Custom headers to include in the test run. You can specify multiple headers by
separating them with spaces.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic queue tests --custom-headers TEST=true OTHER_HEADER=true
  ```

  ```bash yarn theme={null}
  yarn dlx momentic queue tests --custom-headers TEST=true OTHER_HEADER=true
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic queue tests --custom-headers TEST=true OTHER_HEADER=true
  ```
</CodeGroup>

#### `--input-csv <inputCsv>`

Path to a CSV file containing input data for the tests. Each row in the CSV file
will be used as input for a separate test run.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic queue tests --input-csv path/to/input.csv
  ```

  ```bash yarn theme={null}
  yarn dlx momentic queue tests --input-csv path/to/input.csv
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic queue tests --input-csv path/to/input.csv
  ```
</CodeGroup>

#### `--env <env>`

<Info>
  The base URL set on the test will always take precedence over the environment.
  If you want to override the base URL set on the test, use the `--url-override`
  option.
</Info>

The environment to run the test in. This will override any environment specified
by the test.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic queue tests --env env-name
  ```

  ```bash yarn theme={null}
  yarn dlx momentic queue tests --env env-name
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic queue tests --env env-name
  ```
</CodeGroup>

#### `--url-override <urlOverride>`

The URL to override the base URL set on the test or the environment. This is
useful if you want to run the test against a different URL than the one
specified in the test or environment.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic queue tests --url-override https://example.com
  ```

  ```bash yarn theme={null}
  yarn dlx momentic queue tests --url-override https://example.com
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic queue tests --url-override https://example.com
  ```
</CodeGroup>

#### `-w, --wait`

Wait for the test run to complete before exiting.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic queue tests --wait
  ```

  ```bash yarn theme={null}
  yarn dlx momentic queue tests --wait
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic queue tests --wait
  ```
</CodeGroup>

#### `--wait-timeout <waitTimeout>`

Default: `1800`

The maximum time to wait for the test run to complete, in seconds. Must be used
with the `--wait` option. If the test run does not complete within this time,
the command will exit with an error.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic queue tests --wait --wait-timeout 600
  ```

  ```bash yarn theme={null}
  yarn dlx momentic queue tests --wait --wait-timeout 600
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic queue tests --wait --wait-timeout 600
  ```
</CodeGroup>

## `suites`

<CodeGroup>
  ```bash npm theme={null}
  npx momentic queue suites [options] <suites...>
  ```

  ```bash yarn theme={null}
  yarn dlx momentic queue suites [options] <suites...>
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic queue suites [options] <suites...>
  ```
</CodeGroup>

* **\<suites...>**: The names of the suites to run. You can specify multiple
  suites separated by spaces.

### Options

#### `--custom-headers <customHeaders...>`

Custom headers to include in the suite run. You can specify multiple headers by
separating them with spaces.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic queue suites --custom-headers TEST=true OTHER_HEADER=true
  ```

  ```bash yarn theme={null}
  yarn dlx momentic queue suites --custom-headers TEST=true OTHER_HEADER=true
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic queue suites --custom-headers TEST=true OTHER_HEADER=true
  ```
</CodeGroup>

#### `--env <env>`

<Info>
  The base URL set on the test will always take precedence over the environment.
  If you want to override the base URL set on the test, use the `--url-override`
  option.
</Info>

The environment to run the suite in. This will override any environment
specified by the suite.

```bash theme={null}
momentic queue suites --env env-name
```

#### `--url-override <urlOverride>`

The URL to override the base URL set on the test or the environment. This is
useful if you want to run the test against a different URL than the one
specified in the test or environment.

```bash theme={null}
momentic queue suites --url-override https://example.com
```

#### `-w, --wait`

Wait for the suite run to complete before exiting.

```bash theme={null}
momentic queue suites --wait
```

#### `--wait-timeout <waitTimeout>`

Default: `1800`

The maximum time to wait for the suite run to complete, in seconds. Must be used
with the `--wait` option. If the test run does not complete within this time,
the command will exit with an error.

```bash theme={null}
momentic queue suites --wait --wait-timeout 600
```


# results
Source: https://momentic.ai/docs/cli/commands/results



Manage, view, and upload test results.

## `upload`

Upload test results to Momentic Cloud.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic results upload <folder>
  ```

  ```bash yarn theme={null}
  yarn dlx momentic results upload <folder>
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic results upload <folder>
  ```
</CodeGroup>

* **\<folder>**: The path to the folder containing test results generated by a
  `momentic run` invocation or by the `momentic results merge` command.
  `momentic run` [saves local results](/cli/commands/run#output-dir-\<outputdir>)
  to the folder specified by the `--output-dir` option, which defaults to
  `test-results`.

## `merge`

<CodeGroup>
  ```bash npm theme={null}
  npx momentic results merge [options] <parent folder>
  ```

  ```bash yarn theme={null}
  yarn dlx momentic results merge [options] <parent folder>
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic results merge [options] <parent folder>
  ```
</CodeGroup>

* **\<parent folder>**: The parent folder for the results to merge. This folder
  must contain only valid Momentic test outputs. For example, if you pass
  `--output-dir test-results/results-1` to thee `run` command, your parent
  folder is `test-results`.

### Options

#### `--output-dir <outputDir>`

The directory to output the merged results to. The folder will be overwritten if
it already exists on disk.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic results merge --output-dir merged-output test-results/invocation1 test-results/invocation2
  ```

  ```bash yarn theme={null}
  yarn dlx momentic results merge --output-dir merged-output test-results/invocation1 test-results/invocation2
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic results merge --output-dir merged-output test-results/invocation1 test-results/invocation2
  ```
</CodeGroup>

## `view`

Launch the run viewer to inspect test results locally. Starts a local server,
opens it in your browser, and opens the specified run in the run viewer UI.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic results view <results> [runId]
  ```

  ```bash yarn theme={null}
  yarn dlx momentic results view <results> [runId]
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic results view <results> [runId]
  ```
</CodeGroup>

* **\<results>**: Path to the folder containing a `runs/` subfolder with test
  results. Defaults to `test-results`. `momentic run`
  [saves local results](/cli/commands/run#output-dir-\<outputdir>) to the folder
  specified by the `--output-dir` option.
* **\[runId]**: The run ID to open, correlates to a zip file in the `runs/`
  subfolder of your results directory. For example, for
  `runs/eed92602-7355-43dc-8d79-1c43029bec26.zip` use runId
  `eed92602-7355-43dc-8d79-1c43029bec26`. If not provided, the run viewer opens
  to a table with all runs in the run group within the results directory.

### Options

#### `--port <port>`

Port for the run viewer server. Defaults to `58889`.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic results view --port 59999 my-results eed92602-7355-43dc-8d79-1c43029bec26
  ```

  ```bash yarn theme={null}
  yarn dlx momentic results view --port 59999 my-results eed92602-7355-43dc-8d79-1c43029bec26
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic results view --port 59999 my-results seed92602-7355-43dc-8d79-1c43029bec26
  ```
</CodeGroup>


# run
Source: https://momentic.ai/docs/cli/commands/run



<Info>**Prerequisites**: These tests must exist locally as YAML files.</Info>

Run Momentic tests in the current project.

By default, tests will output results to a local directory. You can then upload
results to Momentic Cloud using the `momentic results upload`
[command](/cli/commands/results).

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run [options] [tests...]
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run [options] [tests...]
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run [options] [tests...]
  ```
</CodeGroup>

* **\[tests...]**: The tests to run. If not specified, selects all tests in the
  current project. You can specify multiple tests separated by spaces, test
  paths, or folder paths. You can also pass substrings to match test names.

## Options

### `-c, --config <config>`

Path to the Momentic configuration file. If not specified, it defaults to
`momentic.config.yaml` in the current directory.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --config path/to/momentic.config.yaml
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --config path/to/momentic.config.yaml
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --config path/to/momentic.config.yaml
  ```
</CodeGroup>

### `--disable-cache`

Disable caching entirely. This will cause all steps to run without cached data,
and not save caches after runs. This can result in slower test execution, but
ensures that all steps are run fresh without stored data.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --disable-cache
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --disable-cache
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --disable-cache
  ```
</CodeGroup>

### `-f, --filter <filter>`

Only applicable when using [Workspaces](/cli/workspace). Loads the project with
the specified name.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --filter workspace-name
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --filter workspace-name
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --filter workspace-name
  ```
</CodeGroup>

### `--custom-headers <customHeaders...>`

Custom headers to include in the test run. You can specify multiple headers by
separating them with spaces.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --custom-headers TEST=true OTHER_HEADER=true
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --custom-headers TEST=true OTHER_HEADER=true
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --custom-headers TEST=true OTHER_HEADER=true
  ```
</CodeGroup>

### `--input-csv <inputCsv>`

Path to a CSV file containing input data for the tests. Each row in the CSV file
will be used as input for a separate test run.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --input-csv path/to/input.csv
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --input-csv path/to/input.csv
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --input-csv path/to/input.csv
  ```
</CodeGroup>

### `--env <env>`

<Info>
  The base URL set on the test will always take precedence over the environment.
  If you want to override the base URL set on the test, use the `--url-override`
  option.
</Info>

The environment to run the test in. This will override any environment specified
by the test.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --env env-name
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --env env-name
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --env env-name
  ```
</CodeGroup>

### `--name <suiteName>`

A name to assign to the test suite. This will be the suite name in generated
reports and will also be displayed in Momentic Cloud if results are uploaded.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --name my-test-suite
  ```

  ```bash yarn theme={null}
  npx momentic run --name my-test-suite
  ```

  ```bash pnpm theme={null}
  npx momentic run --name my-test-suite
  ```
</CodeGroup>

### `--url-override <urlOverride>`

The URL to override the base URL set on the test or the environment. This is
useful if you want to run the test against a different URL than the one
specified in the test or environment.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --url-override https://example.com
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --url-override https://example.com
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --url-override https://example.com
  ```
</CodeGroup>

### `--save-cache`

Always save updated step caches after successful test runs, even on the main Git
branch and protected Git branches. Please see the
[cache saving eligibility](/step-cache#cache-saving-eligibility) documentation
for more information.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --save-cache
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --save-cache
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --save-cache
  ```
</CodeGroup>

### `--regenerate-cache`

Run the test without using any existing caches. Running with this option will
still save step caches at the end of the run. This can be useful for updating
caches after changing a configuration option.

Warning: using this option will cause all steps to run without any cached data,
resulting in significantly longer execution times. This option should not be
used on an ongoing basis.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --regenerate-cache
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --regenerate-cache
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --regenerate-cache
  ```
</CodeGroup>

### `--start <start>`

A command to run before starting the test. This can be used to start a local
server or any other command that needs to be run before the test starts.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --start "npm run start"
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --start "yarn start"
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --start "pnpm start"
  ```
</CodeGroup>

### `--upload-results`

Upload test results to Momentic cloud after the test run. This is the same as
running `momentic results upload <outputDir>` after the test run, where
`<outputDir>` is the directory specified by the `--output-dir` option or
`./test-results` if not specified.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --upload-results
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --upload-results
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --upload-results
  ```
</CodeGroup>

### `--wait-on <waitOn>`

The resource to wait for before starting the test. This can be a URL, a file, or
any other resource that can be waited on. This is useful for ensuring that the
resource is available before starting the test.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --wait-on http://localhost:3000
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --wait-on http://localhost:3000
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --wait-on http://localhost:3000
  ```
</CodeGroup>

### `--wait-on-proxy <waitOnProxy>`

HTTP proxy to use when polling the `--wait-on` resource. Provide the full proxy
URL, including protocol, optional credentials, host, and port.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --wait-on http://localhost:3000 --wait-on-proxy https://user:pass@proxy.example.com:8080
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --wait-on http://localhost:3000 --wait-on-proxy https://user:pass@proxy.example.com:8080
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --wait-on http://localhost:3000 --wait-on-proxy https://user:pass@proxy.example.com:8080
  ```
</CodeGroup>

### `--wait-on-timeout <waitOnTimeout>`

The timeout for the `--wait-on` option. If the resource is not available within
this time, the test will fail.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --wait-on http://localhost:3000 --wait-on-timeout 30000
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --wait-on http://localhost:3000 --wait-on-timeout 30000
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --wait-on http://localhost:3000 --wait-on-timeout 30000
  ```
</CodeGroup>

### `--retries <retries>`

The number of times to retry a test if it fails.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --retries 3
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --retries 3
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --retries 3
  ```
</CodeGroup>

### `-p, --parallel <parallel>`

The number of tests to run in parallel. This can be useful for speeding up test
execution, especially for large test suites. Each test will start its own
browser instance.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --parallel 5
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --parallel 5
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --parallel 5
  ```
</CodeGroup>

### `--timeout-minutes <timeoutMinutes>`

Maximum number of minutes to run tests before stopping. When the timeout is
reached, any currently running tests will be stopped, results will be written to
disk, and a summary will be printed. The process will exit with code 1. This is
useful for CI pipelines where you want to enforce a maximum execution time.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --timeout-minutes 30
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --timeout-minutes 30
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --timeout-minutes 30
  ```
</CodeGroup>

### `--labels <labels...>`

Run tests with the specified labels. This allows you to filter tests based on
assigned labels.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --labels smoke regression
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --labels smoke regression
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --labels smoke regression
  ```
</CodeGroup>

### `--update-golden-files`

Update the golden files for [Visual diff](/steps/visual-diff).

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --update-golden-files
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --update-golden-files
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --update-golden-files
  ```
</CodeGroup>

### `--reporter <reporter>`

Specify the reporter to use for the output.

Options:

* `junit`
* `allure-json`
* `playwright-json`
* `buildkite-json`

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --reporter junit
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --reporter junit
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --reporter junit
  ```
</CodeGroup>

### `--reporter-dir <reporterDir>`

Specify the directory where the reporter output will be saved. If not specified,
it defaults to `./reports`.

Reporter filenames are based on the suite name. For example, `junit` writes
`{suiteName}.xml` and `buildkite-json` writes `{suiteName}.buildkite.json`.

The suite name comes from `--name` when provided. Otherwise, Momentic uses the
detected project's `name` from `momentic.config.yaml`.

For `buildkite-json`, `scope` comes from the suite name and `name` comes from
the individual test name.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --reporter-dir ./reports
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --reporter-dir ./reports
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --reporter-dir ./reports
  ```
</CodeGroup>

### `--output-dir <outputDir>`

Directory to store run artifacts such as screenshots, results, and logs. This
directory will be cleared at the start of execution. If not specified, it
defaults to `./test-results`.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --output-dir ./output
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --output-dir ./output
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --output-dir ./output
  ```
</CodeGroup>

### `--shard-index <shardIndex>`

The index of the shard to run. This is used in conjunction with `--shard-count`
to determine which tests to run in this shard. This is useful for running tests
in parallel across multiple machines or processes. The index starts at 1.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --shard-index 1 --shard-count 3
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --shard-index 1 --shard-count 3
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --shard-index 1 --shard-count 3
  ```
</CodeGroup>

### `--shard-count <shardCount>`

The total number of shards to run. This is used in conjunction with
`--shard-index` to determine which tests to run in this shard. For example, if
you have 3 shards and you set `--shard-index` to 1, only the tests that belong
to the first shard will be executed.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --shard-index 1 --shard-count 3
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --shard-index 1 --shard-count 3
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --shard-index 1 --shard-count 3
  ```
</CodeGroup>

### `--include <includePatterns...>`

Only include tests that match the provided regex patterns. Multiple patterns can
be provided. The patterns will be matched against the test file paths and the
pattern only needs to match a part of the path for the test to be included.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --include "billing*"
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --include "billing*"
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --include "billing*"
  ```
</CodeGroup>

### `--exclude <excludePatterns...>`

The opposite of `--include`: a test that matches any of the provided regex
patterns will be excluded from running.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --exclude "billing*"
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --exclude "billing*"
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --exclude "billing*"
  ```
</CodeGroup>

### `--skip-quarantined`

Skip quarantined tests entirely. By default, quarantined tests will run, but
their statuses won't impact pipeline success or the exit code of the process.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --skip-quarantined
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --skip-quarantined
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --skip-quarantined
  ```
</CodeGroup>

### `--only-quarantined`

Run only quarantined tests. Only quarantined tests will be executed and their
statuses will impact the pipeline success and the exit code of the process.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --only-quarantined
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --only-quarantined
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --only-quarantined
  ```
</CodeGroup>

### `--ignore-quarantine`

Run all tests and apply their statuses to the pipeline success and exit code.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --ignore-quarantine
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --ignore-quarantine
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --ignore-quarantine
  ```
</CodeGroup>

### `--record-video`

Record videos of test runs. Enabling this option will increase the size of
results. Once results are uploaded, the videos can be viewed in the run viewer.
In order to use this flag, ffmpeg must be installed on the machine. This can be
done using the `momentic install-browsers ffmpeg` command.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --record-video
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --record-video
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --record-video
  ```
</CodeGroup>


# Configuring momentic.config.yaml
Source: https://momentic.ai/docs/cli/configuration



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


# File glob specification
Source: https://momentic.ai/docs/cli/globs



File globs are used for configuring which files to include or exclude in various
contexts, allowing you to specifically define the files you want `momentic` to
include.

## Glob patterns

| Pattern     | Description                                                                                          |
| ----------- | ---------------------------------------------------------------------------------------------------- |
| `*`         | Match all files in the directory                                                                     |
| `**`        | Recursively match all files and sub-directories                                                      |
| `some-dir/` | Match the `some-dir` directory and its contents                                                      |
| `some-dir`  | Match a file named `some-dir` or a `some-dir` directory and its contents                             |
| `some-dir*` | Match files and directories that start with `some-dir`, including contents when matching a directory |
| `*.js`      | Match all `.js` files in the directory                                                               |
| `!`         | Negate the whole glob (automatically applies `/**` to the end of the defined glob)                   |

## Examples

| Pattern            | Description                                                                                       |
| ------------------ | ------------------------------------------------------------------------------------------------- |
| `dist/**`          | Match all files in the `dist` directory, its contents, and all sub-directories                    |
| `dist/`            | Match the `dist` directory and its contents                                                       |
| `dist`             | Match a file named `dist` or a `dist` directory, its contents, and all sub-directories            |
| `dist/some-dir/**` | Match all files in the `dist/some-dir` directory and all sub-directories in the current directory |
| `!dist`            | Ignore the `dist` directory and all of its contents                                               |
| `dist*`            | Match files and directories that start with `dist`                                                |
| `dist/*.js`        | Match all `.js` files in the `dist` directory                                                     |
| `!dist/*.js`       | Ignore all `.js` files in the `dist` directory                                                    |
| `dist/**/*.js`     | Recursively match all `.js` files in the `dist` directory and its sub-directories                 |
| `../scripts/**`    | Up one directory, match all files and sub-directories in the `scripts` directory                  |


# Migrating to v2.x
Source: https://momentic.ai/docs/cli/migrate-v2



## Update Momentic version

<Info>
  Make sure `momentic` is installed as a devDependency in the root of your
  repository.
</Info>

<CodeGroup>
  ```bash npm theme={null}
  npm update momentic
  ```

  ```bash yarn theme={null}
  yarn upgrade momentic
  ```

  ```bash pnpm theme={null}
  pnpm update momentic
  ```
</CodeGroup>

Update CI scripts, `package.json`, Makefiles, and any other files in your
codebase that reference `momentic` to the latest `2.x` version.

## Run the migration wizard

This command will update your `momentic.config.yaml` to include feature flags,
Git branch configuration, and AI agent settings.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic migrate v1-v2
  ```

  ```bash yarn theme={null}
  yarn dlx momentic migrate v1-v2
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic migrate v1-v2
  ```
</CodeGroup>

## Run checks for duplicate IDs

Momentic will fail if it detects duplicate command or step IDs. Duplicate IDs
are caused by manually modifying tests outside of the Momentic editor, and can
lead to test flakiness.

To check whether your existing repository has duplicate IDs, run the following
command. Problems can be automatically fixed by adding the `--fix` flag.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic check duplicate-ids
  ```

  ```bash yarn theme={null}
  yarn dlx momentic check duplicate-ids
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic check duplicate-ids
  ```
</CodeGroup>

## Update CI scripts to install browsers

In Momentic 2.0, browsers must be explicitly installed.

If your CI scripts do not already invoke the `install-browsers` command, add
this command before any tests are executed.

You can determine which browsers to install by searching your codebase for the
`browserType` string. See the [install-browsers](/cli/commands/install-browsers)
command for more information.

## Update CI scripts to upload results

`momentic run` now saves all test results to a local directory called
`test-results` by default.

For the results to be available on Momentic Cloud, add a step to run the
`momentic results upload <folder>` command, supplying the path to the directory
containing the local test results.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic results upload test-results
  ```

  ```bash yarn theme={null}
  yarn dlx momentic results upload test-results
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic results upload test-results
  ```
</CodeGroup>

See the [results](/cli/commands/results) command for more information and
details on merging results for sharding setups.

## Update deprecated commands and flags

* The `--report` and `--no-report` flags are no longer supported.
* Using `CI=true` to upload results is no longer necessary and can be removed
  from CI scripts.
* `momentic import-from-cloud` is deprecated and replaced with
  `momentic import`.
* `momentic check-config` is deprecated and replaced with
  `momentic check config`.

## Update tests relying on automatic tab switching

<Tip>
  Use [Switch Tab](/steps/switch-tab) steps instead of relying on automatic tab
  switching.
</Tip>

In Momentic 2.0, switching to newly opened tabs no longer occurs automatically,
as this behavior is inherently racy and flaky.

If you want to continue using automatic tab switching, you can enable it by
adding the following to your `momentic.config.yaml` file:

```yaml momentic.config.yaml theme={null}
browser:
  autoFollowNewTabs: true
```


# Workspaces
Source: https://momentic.ai/docs/cli/workspace



For organizations with multiple teams, you can initialize a separate Momentic
project for each team to isolate tests, environments, and settings. A group of
projects is known as a **workspace**. Each Git repository should have at most
one workspace.

## Creating a workspace

Create a `momentic.workspace.yaml` file in the location where you want users to
start the app. For most organizations, this should be the root of your Git
repository.

### `projects`

The workspace file currently supports a single `projects` key, which is an list
of paths where Momentic should look for projects:

```yaml theme={null}
projects:
  - project-a
  - folder/*
  - apps/**/*
```


# Cloud vs. CLI
Source: https://momentic.ai/docs/cloud-vs-cli

Compare Momentic's Cloud and CLI offerings to find the best fit for your team

Momentic offers two primary ways to build and run tests:
[Cloud](/quickstart/cloud) and [CLI](/quickstart/cli). Each has its own
strengths and is suited for different use cases.

## Comparison

Cloud is ideal for teams that want to get started quickly without worrying about
infrastructure. It allows you to build and run tests directly in your browser,
making it easy to monitor public-facing applications.

If you want to
[shift left](https://github.com/resources/articles/security/what-is-shift-left-testing)
and run tests as part of your development process, the CLI is the best choice.
It allows you to run tests locally, store them in version control, and integrate
them into your CI/CD pipelines seamlessly.

| Features                   | Cloud                                                | CLI                                         |
| -------------------------- | ---------------------------------------------------- | ------------------------------------------- |
| Version control            | No                                                   | Store tests in GitHub and other SCM systems |
| CI/CD integration          | Yes                                                  | Yes                                         |
| Public deployment testing  | Yes                                                  | Yes                                         |
| Private deployment testing | Yes with IP whitelist                                | Yes                                         |
| Local testing              | Yes with tunnel                                      | Yes                                         |
| Scheduled runs             | Yes                                                  | Orchestrate with CI/CD                      |
| Infrastructure             | Provisioned and managed by Momentic                  | Self-hosted or managed by your team         |
| Analytics                  | Yes                                                  | Yes                                         |
| Custom reporting           | No                                                   | JSON, JUnit, and Allure reports             |
| Notifications              | Slack, PagerDuty, Opsgenie, any webhook-based system | Orchestrate with CI/CD                      |

## Next steps

<Card title="CLI" icon="terminal" href="/quickstart/cli">
  For teams looking to store tests in source code management (SCM) and integrate
  into CI/CD
</Card>

<Card title="Cloud" icon="cloud" href="/quickstart/cloud">
  For teams looking to get started quickly and run tests without worrying about
  infrastructure
</Card>


# Browser preview
Source: https://momentic.ai/docs/editor/browser-preview

Interactive browser for instant feedback

The browser preview is an interactive browser that allows you to see the results
of your test definition in real-time. It provides instant feedback on how your
test will behave when executed.

You can also preview the mouse x, y coordinates, which is useful for debugging
steps using coordinates.

<Frame>
  <img />
</Frame>

## Browser actions

* **Refresh**: Reload the current page.
* **Reset**: Reset the browser to its initial state, clearing any cookies, local
  storage, or session data.
* **Switch tab**: Switch between different tabs in the browser.


# Developer tools
Source: https://momentic.ai/docs/editor/developer-tools

Tools to help you develop and debug your tests

The developer tools provide additional functionality to help you develop and
debug your tests.

<Frame>
  <img />
</Frame>

## Panes

* **Context**: The available data in the test. This includes variables from the
  environment as well as any data you have defined in the test.
* **Console**: View console logs and errors from the browser.
* **Network**: View network requests made by the browser during the test run.
* **Accessibility**: View the accessibility tree of the current page.
* **HTML**: View the HTML of the current page.


# Test definition
Source: https://momentic.ai/docs/editor/test-definition

How to tell Momentic what to do

The test definition is the core of your Momentic test. It describes what actions
to perform, what elements to interact with, and how to verify the results. You
can write the test definition in natural language, and Momentic will convert it
into browser interactions at runtime.

<Frame>
  <img />
</Frame>

## Test actions

There is a toolbar at the top of the editor that provides various actions to
manage your test definition.

<Frame>
  <img />
</Frame>

Here are the available actions:

* **Add new step**: Create a new step in your test definition.
* **Record**: Start recording a new test definition. This will open the browser
  in recording mode, allowing you to interact with the app and automatically
  generate steps based on your actions.
* **Create module**: Create a reusable module from selection of steps. This
  allows you to share logic across multiple tests.
* **Run from start**: Execute the test definition from the beginning. This will
  reset the browser and run all steps in order.

## Step actions

If you hover over each step, you will see action buttons that allow you to
execute, edit, delete, or move the step.

<Frame>
  <img />
</Frame>

Here are the available actions (from left to right):

* **Run**: Execute the step immediately.
* **Run to**: Execute the step and all previous steps.
* **Run from**: Execute the step and all subsequent steps.
* **Edit**: Modify the step's content.
* **Duplicate**: Create a copy of the step.
* **Move up**: Move the step one position up in the list.
* **Move to top**: Move the step to the top of the list.
* **Move down**: Move the step one position down in the list.
* **Move to bottom**: Move the step to the bottom of the list.
* **Add before**: Insert a new step before the current one.
* **Add after**: Insert a new step after the current one.
* **Delete**: Remove the step from the test definition.

## Editing steps

You can edit a step by clicking on the **Edit** button. This will open a text
editor where you can modify the step's content. Hover over labels to see
tooltips with more information about each option.

<Frame>
  <img />
</Frame>

## Keyboard shortcuts

<Info>All `Cmd` keys can be replaced with `Ctrl` on Windows.</Info>

| Shortcut                       | Action                         |
| ------------------------------ | ------------------------------ |
| <kbd>Cmd + Enter</kbd>         | Save the currents step         |
| <kbd>Cmd + Shift + Enter</kbd> | Save and run the currents step |
| <kbd>Esc</kbd>                 | Discard edits                  |


# Email
Source: https://momentic.ai/docs/email



<Info>
  **Prerequisites**: An email address must be provisioned by Momentic.
</Info>

Momentic supports sending and receiving emails to and from allocated
`@usemomentic.com` or `@gomomentic.com` addresses.

Email functionality is surfaced through the [JavaScript](/steps/javascript)
step. Within Momentic's JavaScript sandbox, your code can access the `email`
object. This object contains the following utility functions:

## Sending emails

The `send` utility function allows you to send an email to an inbox. The inbox
provided in the `from` argument must be issued by Momentic.

<Tabs>
  <Tab title="Function signature">
    ```ts theme={null}
      async function send(params: {
        subject: string;
        body: string;
        to: string;
        from: string;
      }): Promise<void>;
    ```
  </Tab>

  <Tab title="Example">
    ```ts theme={null}
      await email.send({
        subject: "Hello",
        body: "Hello world!",
        to: "momentic+test@gomomentic.com",
        from: "momentic"
      });
    ```
  </Tab>
</Tabs>

## Fetching the latest email

<Info>
  Make sure the function timeout is shorter than the JavaScript lambda timeout.
  The default timeout for both is 10 seconds.
</Info>

The `fetchLatest` utility function retrieves the most recent email received.
Optionally, you can filter for emails sent after a particular date. This can be
useful for ensuring that you are not reading stale emails that were received
before the test began.

This function will automatically retry until a matching email is found or the
timeout is exhausted. If no email is received within the timeout, an error is
thrown.

If an email is received, the text content of the email will be available in the
`text` field of the result. When `trimWhitespace` is true, which is the default
behavior, adjacent whitespace characters will be combined to make the text
easier to read and parse in future steps. If the email contains HTML content,
the raw HTML will be provided in the `html` field.

<Tabs>
  <Tab title="Function signature">
    ```ts theme={null}
    async function fetchLatest(params: {
      inbox: string, // inbox name allocated by momentic
      afterDate?: Date,
      timeout?: number,
      trimWhitespace: boolean = true,
    }): Promise<Email>;

    type Email = {
      subject: string; // subject line
      from: string; // sender's name and email
      fromEmail: string; // sender's email address
      to: string; // recipient's name and email address (the email address allocated to your organization)
      time: number; // unix timestamp for when the email was received
      secondsAgo: number; // how many seconds ago the email was received
      size: number | undefined; // size of the email in bytes

      text: string; // the text content of the email. if trimWhitespace is true, adjacent whitespace characters will be combined
      html: string | undefined; // if the email has HTML content, this field will contain the raw HTML
    };
    ```
  </Tab>

  <Tab title="Example">
    ```ts theme={null}
    const msg = await email.fetchLatest({
      inbox: "jeff+test",
      afterDate: new Date(),
      timeout: 20_000,
    });

    return msg.text;
    ```
  </Tab>
</Tabs>

## Fetching all emails

The `fetchAll` utility function retrieves all recently received emails. You can
filter for emails received after a certain date and set a limit on the number of
emails returned. By default, these parameters are set to 15 minutes ago and 3
emails; the maximum allowed values are 24 hours and 10 emails.

This function runs instantaneously and does not retry or poll until an email
exists. As such, it is the responsibility of the caller to ensure that the email
they are interested in is already delivered by the time this function is
invoked. If no emails exist in the inbox, the function will throw an error.

<Tabs>
  <Tab title="Function signature">
    ```ts theme={null}
    async function fetchAll(params: {
      inbox: string, // inbox name allocated by momentic
      afterDate?: Date,
      limit?: number,
      trimWhitespace: boolean = true,
    }): Promise<Email[]>;
    ```
  </Tab>

  <Tab title="Example">
    ```ts theme={null}
    const msgs = await email.fetchAll({
      inbox: "jeff+test",
      afterDate: new Date(Date.now() - 60 * 1000),
      limit: 5,
    });

    return msgs.filter((msg) => msg.text.includes("verification code"))
    ```
  </Tab>
</Tabs>

## Creating isolated inboxes

Once you are allocated unique username from Momentic, you can create unlimited,
isolated inboxes accessible from your organization by appending a suffix to the
username. For example, if your unique username is `momentic`, you can also send
emails to `momentic+test@usemomentic.com` and fetch results using the
`momentic+test` inbox name.

We recommend using this strategy with a randomized suffix such as `Date.now()`
when running multiple tests in parallel that require email access to prevent
race conditions.


# Authentication
Source: https://momentic.ai/docs/environment/authentication



<Warning>
  Avoid using Momentic tests to log in using SSO. Providers like Google,
  Facebook, and GitHub often have security measures that block automated
  browsers.
</Warning>

## Username and password

Username and password authentication is the easiest and most straightforward
method for authenticating users in your tests.

## Email magic link

<Info>
  **Prerequisites**: An email address must be provisioned by Momentic.
</Info>

Add a [JavaScript](/steps/javascript) step with the following content:

```javascript theme={null}
// fetch the latest email from the inbox
const msg = await email.fetchLatest({
  inbox: "<YOUR USERNAME HERE>",
});

// extract the magic link using regex
const link = msg.text.match(/https?:\/\/[^\s]+/)[0];

return link;
```

Use the **Save to environment variable** option to save the link to an
environment variable, e.g., `MAGIC_LINK`.

Then, use the [Navigate](/steps/navigate) step with content
`{{ env.MAGIC_LINK }}` to navigate to the magic link and complete the login
process.

## Email One-Time Password (OTP)

<Info>
  **Prerequisites**: An email address must be provisioned by Momentic.
</Info>

Add a [JavaScript](/steps/javascript) step with the following content:

```javascript theme={null}
// fetch the latest email from the inbox
const msg = await email.fetchLatest({
  inbox: "<YOUR USERNAME HERE>",
});

// extract the code using regex
const code = msg.text.match(/\b\d{6}\b/);

return code;
```

Use the **Save to environment variable** option to save the link to an
environment variable, e.g., `OTP_CODE`.

Then, use the [Type](/steps/type) step with content `{{ env.OTP_CODE }}` to
input the OTP code and complete the login process.

## SMS One-Time Password (OTP)

<Info>**Prerequisites**: A SMS number must be provisioned by Momentic.</Info>

Add a [JavaScript](/steps/javascript) step with the following content:

```javascript theme={null}
// fetch the latest message from the inbox
const msg = await sms.fetchLatest({
  to: "<YOUR SMS NUMBER HERE>",
});

// extract the code using regex
const code = msg.body.match(/\b\d{6}\b/);

return code;
```

Use the **Save to environment variable** option to save the link to an
environment variable, e.g., `OTP_CODE`.

Then, use the [Type](/steps/type) step with content `{{ env.OTP_CODE }}` to
input the OTP code and complete the login process.

## Vercel Deployment Projection

Follow the instructions
[here](https://vercel.com/docs/deployment-protection/methods-to-bypass-deployment-protection/protection-bypass-automation)
for Playwright. You can configure headers in test options.

## IP whitelist

For teams that use Momentic Cloud, you can whitelist Momentic's fixed egress IP:
`34.106.239.183`


# Requirements
Source: https://momentic.ai/docs/environment/requirements



In order to automate hundreds or thousands of end-to-end tests, and run them
concurrently, we need a testing environment that meets certain requirements.

## Resource class

For the best performance, we recommend using a resource class with **at least 2
vCPUs and 4 GB of RAM per browser instance** (these are the minimum
specifications needed for Chromium).

## Stability

Applications on the environment do not have frequent restarts or resource
consumption issues; and there is some form of change control to prevent
unexpected deployments.

## Concurrent user capacity

We run each of your tests in a separate worker, each of which acts as an
individual user. The test environment (and dependent databases, email servers,
etc.) must have the resources to support as many concurrent users as you have
tests.

## Configured for automated testing

Applications in the environment need to be configured so that the tests can
pass. For example:

* If the application has feature flags, the flags are set so that tests can
  pass.
* There is at least one user account created for Momentic, and the ability to
  programmatically add more as needed to run tests concurrently.
* Sub-one minute email and SMS delivery.


# Failure analysis
Source: https://momentic.ai/docs/failure-analysis



Momentic automatically analyzes failed runs to highlight the most likely root
cause and provide a brief narrative of what went wrong. It uses visual context
(screenshots) and page state to quickly surface issues so you can triage faster,
with less guesswork.

## What it analyzes

When a run fails, Momentic reviews a playback of your recent steps and compares
the state before and after key actions. It analyzes your run data including:

* **Screenshots before and after a step** to spot overlays, misaligned elements,
  or unexpected UI changes
* **Page state and current URL** to understand what the app was showing at each
  moment
* **Step descriptions and actions taken** to understand what the test was
  attempting to do
* **Element targeting details** to catch hidden/disabled elements or mismatched
  selectors
* **Error message and stack** as helpful context for understanding the failure

The analysis reasons through the test execution, exploring how different factors
might have contributed to the failure. It considers possibilities like an
assertion failing because a modal overlapped a button, or navigation leaving the
page in an unexpected state. It focuses on providing insights, possible fixes
ranging from tests not using random values causing concurrency errors to tests
using an irrelevant module, and gives a likely root cause of the test failure.

## What you'll see

### Web app (Run Viewer)

In the run viewer, failure analysis appears in a dedicated "AI failure analysis"
tab alongside the failed step and includes:

* **Error summary** - A concise overview of what went wrong
* **Root cause analysis** - A detailed explanation of the underlying issue, how
  the test failed, and potential fixes
* **Error details** - The actual error message and stack trace
* **Summary of previous steps** - Context about what happened before the failure

### CLI output

When running tests locally with failure analysis enabled
(`aiFailureAnalysis: true`), the CLI provides:

* **Root cause analysis** - A focused, detailed explanation of the failure (the
  RCA) when available
* **Error type** - The classified reason for the failure
* **Fallback description** - Basic error description when root cause analysis
  isn't available

The CLI output focuses on actionable insights to help you understand and fix
issues quickly during development. Root cause analysis appears only when the AI
can provide it - otherwise it falls back to the standard error type and
description.

## Configuration

* **Cloud runs**: Toggle failure analysis on the workspace **AI settings** page.
  You can enable/disable it at any time.
* **CLI runs**: Control via your yaml for
  [CLI configuration](/cli/configuration) (look for the `ai.aiFailureAnalysis`
  option).


# Failure recovery (Beta)
Source: https://momentic.ai/docs/failure-recovery



<Warning>
  Failure recovery is in beta and subject to change or be deprecated in the
  future.
</Warning>

Momentic can automatically attempt to recover from certain transient test
failures, such as slow page loads, temporary modals, and UI race conditions.

<Info>
  Failure recovery is best effort. It reduces noise from temporary conditions,
  but it is not guaranteed to recover every run. Recovery behavior can change
  over time.
</Info>

## Recovery behavior

When an eligible test fails, Momentic analyzes the failure and classifies it as
recoverable or not recoverable.

* **Recoverable**: transient, explainable conditions where the failed step can
  likely succeed after restoring the page to a good state.
* **Not recoverable**: legitimate failures, infrastructure issues, or ambiguous
  cases where retrying could hide a real problem.

For recoverable failures, Momentic generates and executes recovery steps, then
automatically retries the failed step. If the retry succeeds, the test
continues. If not, the run is marked failed.

<Info>
  Failure recovery adds runtime latency. The initial diagnosis ranges from 5-20
  seconds. Recovery steps are also generated dynamically, which can add up to 10
  seconds per newly generated step (plus normal step execution time).
</Info>

Recovery activity is visible in the run viewer and CLI output. In the run
viewer, you can filter tests by recovery status to quickly find recovered runs.

## Configuration

Failure recovery can be enabled or disabled per test in test options. You can
also set defaults in your organization's [CLI configuration](/cli/configuration)
for local executions or on the
[AI settings page](https://app.momentic.ai/settings/ai) for Cloud runs.

Failure recovery uses your test description to preserve test intent. You can
also use test options to describe custom scenarios that should or should not be
treated as recoverable.

## Limitations

A single test run is eligible for failure recovery up to 3 times. Only primitive
steps can be recovered: steps that contain other steps such as modules and AI
actions are not eligible.

Only tests running in CI (detected through the `CI` environment variable) are
eligible for failure recovery. Interactive editor sessions never trigger failure
recovery.

In addition, the following scenarios are not eligible for failure recovery:

* **Infrastructure issues**: Momentic will not recover from infrastructure
  issues such as network timeouts, server errors, full-page errors, or 500
  response codes. We recommend you configure retries on your test or configure
  your CI to wait until fixtures are ready before invoking Momentic.
* **Legitimate failures**: if all steps were executed correctly and the test
  fails due to a legitimate error, failure recovery will not be triggered. This
  includes permanent user behavior and flow changes where the test is now out of
  sync with the application and needs to be updated.
* **Configuration errors**: Momentic will not attempt to salvage tests that have
  incorrect step options or nonsensical action sequences.

## Examples

Recoverable examples:

* A cookie consent modal temporarily blocks the intended click target.
* A page transition is still in progress when an assertion runs.
* A stale cached target causes a mis-click, and retrying with fresh targeting
  can recover.

Not recoverable examples:

* Login now requires a new permanent **Continue** step after entering username.
* The app returns a full-page 500 error after form submission.
* A network timeout or backend outage prevents required data from loading.
* The browser/page process crashes during the run.
* A CAPTCHA or anti-bot challenge blocks further progress.
* A required action is blocked by account plan limits or missing permissions.

## Usage guidance

If a test is recovered frequently, treat it as unstable test behavior, not a
successful long-term state.

* Do not rely on failure recovery as the only reason a test passes.
* Fix the test or app behavior to remove recurring recovery conditions.
* Quarantine persistently flaky tests until they are corrected (see
  [quarantine](/quarantine)).
* Use run viewer recovery-status filters to monitor and triage recurring
  recoveries.


# Files
Source: https://momentic.ai/docs/files



## File upload

<Warning>
  The [File upload](/steps/file-upload) step registers an event listener to
  automatically upload a file when the native file picker dialog is opened. This
  step must be executed **before** the file picker dialog is opened, otherwise
  it will not work.
</Warning>

<Frame>
  <img />
</Frame>

### Cloud-hosted files

You can upload files to Momentic that are private and not accessible to the
public.

Select **Files** on the left sidebar and click on the **Upload file** button in
the top-right corner. You can upload any file type, including images, documents,
and more.

<Frame>
  <img />
</Frame>

### Public files

<Info>
  Make sure the URL you provide is a direct link to the file. For example, if
  you want to upload an image, the URL should end with `.jpg`, `.png`, or
  another image file extension. If the URL does not point directly to a file,
  Momentic will not be able to access it.
</Info>

You can upload any files that has a publicly accessible URL. For example, this
is a URL for a `README.md` file of a public repository on GitHub:

[https://raw.githubusercontent.com/momentic-ai/momentic/main/README.md](https://raw.githubusercontent.com/momentic-ai/momentic/main/README.md)

### Local files

If you're using the Momentic CLI, you can also upload files from your local
machine.

Local files can be referenced by path. The path must be absolute or relative the
the root `momentic.config.yaml`.

## File download

You can download a file in a Momentic test by using a [Click](/steps/click) step
and configuring the **Wait for download** option. This will wait for the file to
be downloaded before proceeding to the next step. The default download timeout
is 10 seconds.

<Frame>
  <img />
</Frame>

Current limitations:

* Only one file can be downloaded per step.
* The maximum supported size is 50mb.
* Direct file manipulation (e.g., checking file names or formats) is not
  supported.


# Generating text
Source: https://momentic.ai/docs/generating-text



AI text generation is currently surfaced through the
[JavaScript](/steps/javascript) step. Within Momentic's JavaScript sandbox, your
code can access a special `ai` object. This object contains the following
utility function:

### Generating text

The `generate` utility function allows you to prompt an LLM to generate text.
The `input` is a string which the LLM will use as the prompt.

<Tabs>
  <Tab title="Function signature">
    ```ts theme={null}
    async function generate(input: string): Promise<string>
    ```
  </Tab>

  <Tab title="Example">
    ```ts theme={null}
    const otpCodeSms = "Your verification code is 543890"
    return await ai.generate(`Extract the OTP code and only the OTP code from the following: ${otpCodeSms}`)
    ```
  </Tab>
</Tabs>


# Global locator redirect
Source: https://momentic.ai/docs/global-locator-redirect

Global locator redirect is a feature that Momentic uses to link accessible elements to their visible, actionable counterparts.

## Why we built global locator redirect

Many sites use a combination of semantically correct html tags (e.g.
`<input type=”checkbox”>`) combined with other elements to create components
that both look good and are accessible. Usually, what this looks like in
practice is an invisible input element covered by elements that are styled to
look like something (for example, a checkbox).

This can cause problems when using Momentic because the AI chooses elements from
the accessibility tree (i.e. the input), but we interact with the page as a
regular user would (i.e. clicking on the button). Often, the outcome is that the
element that the AI chose fails stability checks (is not visible, has no
bounding box, or is covered by another element), causing test failures. Because
of this, we need a way to get from the accessible element that the AI chose to
an element on the page that playwright can actually interact with.

## How global locator redirect works

Global locator redirect works by hit testing points where the original element
is located. At each point, we determine the topmost element that is visible and
can be interacted with. If the original element is ever visible, we continue to
target that element. If the original element is never visible, we choose the
most common overlapping element that is also similar to the original. We
determine similarity by verifying that the elements are nearby in the DOM and
their bounding boxes are similar. This prevents us from redirecting to
overlapping elements that are obviously completely unrelated to the original.

## Configuration options

Currently, global locator redirect has three configuration options:

1. Always: global locator redirect is used for all interactive steps that target
   elements (click, type, etc.). For CLI users, this is the same as setting
   `globalLocatorRedirect` to `always` in `momentic.config.yaml`.

2. Click only: this option exists for backwards-compatibility reasons. When
   enabled, global locator redirect applies only to click steps. For CLI users,
   this is the same as setting `globalLocatorRedirect` to `true` in
   `momentic.config.yaml`.

3. Never: global locator redirect is never used. For CLI users, this is the same
   as setting `globalLocatorRedirect` to `false` in `momentic.config.yaml`.

By default, global locator redirect is always enabled.


# Welcome to Momentic
Source: https://momentic.ai/docs/index

Get started with Momentic and learn how to write tests

Momentic is a AI-powered platform for software testing. It allows you to write
reliable end-to-end tests for web apps in a simple and intuitive way using
natural language.

<Frame>
  <img />
</Frame>

## Getting started

If you're new to Momentic, you can get started using the guides below.

<CardGroup>
  <Card title="Momentic CLI" icon="rocket" href="/quickstart/cli">
    Run your first test and integrate it into your repository in minutes using
    the CLI
  </Card>

  <Card title="Momentic Cloud" icon="terminal" href="/quickstart/cloud">
    Run your first test in minutes using Cloud without local development tools
  </Card>
</CardGroup>

## Prompting 101

Learn how to describe your tests in natural language.

<CardGroup>
  <Card title="Finding elements" icon="magnifying-glass" href="/prompting/finding-elements">
    Describe the elements you want to interact with instead of using CSS
    selectors or XPath
  </Card>

  <Card title="Writing assertions" icon="check" href="/prompting/writing-assertions">
    Describe the expected behavior of your app using multi-modal AI
  </Card>
</CardGroup>


# JavaScript
Source: https://momentic.ai/docs/javascript



Momentic tests can run arbitrary JavaScript code to craft complex logic and
achieve dynamic behavior within steps.

### JavaScript step

The [JavaScript](/steps/javascript) steps allows you to execute JavaScript code.
Asynchronous code using `async` and `await` is supported.

The output of the step is set to the final return value. This value must be
[serializable](https://en.wikipedia.org/wiki/Serialization) (e.g. you cannot
return a `class` or a `function`).

### `{{ }}` expressions

<Warning>
  Do not use `{{}}` expressions within JavaScript steps. There is no need to do
  so since any variables and functions can be referenced directly.
</Warning>

String input fields in every step step can contain JavaScript expressions inside
curly brackets. At test runtime, these expressions are evaluated and the
templated value is used instead.

For example, the value of a [Type](/steps/type) step can be set to
`{{ env.USERNAME }}@gmail.com`, which might evaluate to something like
`johndoe@gmail.com`.

You should not include a `return` statement in these expressions.

## Execution context

By default, all code executes in an isolated Node.js sandbox. This ensures that
one test's code cannot access other users' data, modify the test environment, or
consume excessive resources.

You can also execute the code in the current page's JavaScript context by turn
on the **Execute in browser** option. You will have access to globals like
`window`, `document`, and other browser APIs. This is useful for interacting
with the page directly, such as manipulating the DOM or accessing
browser-specific features.

## Globals

<Info>
  These globals are **only available** in the Node.js sandbox environment.
</Info>

In addition to the Node.js built-in libraries, Momentic provides several
third-party packages, special utility functions, and global constants to
accelerate the testing experience.

### Third-party packages

* `axios`: For making HTTP/HTTPS requests. Please see the official
  [documentation](https://axios-http.com/docs/intro) for usage and examples.
* `assert`: For executing assertions based on variables and constants. Please
  see the official [Node.js documentation](https://nodejs.org/api/assert.html)
  for usage and examples.
* `faker`: For generating mock data. Please see the official
  [documentation](https://fakerjs.dev/api/) for usage and examples.
* `moment`: For creating and manipulating `Date` objects. Please see the
  official [documentation](https://momentjs.com/docs/) for usage and examples.
* `createAppAuth`: For authenticating with the GitHub API as a GitHub app.
  Please see the official
  [documentation](https://github.com/octokit/auth-app.js/?tab=readme-ov-file#createappauthoptions-or-new-octokit-auth-)
  for usage and examples.
* `Octokit`: For interacting with the GitHub API. Using this function may incur
  additional runtime. Please see the official
  [documentation](https://github.com/octokit/octokit.js)
* `pg`: For interacting with PostgreSQL databases. Please see the official
  [documentation](https://node-postgres.com/features/connecting) for usage and
  examples.

### Special utility functions

* `setVariable`: For setting a variable in the test context. Read more in
  [Variables](/variables).
* `sms`: For sending and receiving SMS messages. Read more in [SMS](/sms).
* `email`: For sending and receiving email messages. Read more in
  [Email](/email).
* `ai`: For interacting with an LLM to generate text. Read more in
  [Generating text](/generating-text).
* `extractCookiesFromResponse`: For extracting cookies from a
  [Response](https://developer.mozilla.org/en-US/docs/Web/API/Response) object,
  which is the type returned from `fetch` and `axios` calls. The cookies are
  returned in a format compatible with Playwright as well as the
  [Load auth state](/steps/load-auth-state) step.

  ```javascript theme={null}
    type CookieSetting = {
      name: string;
      value: string;
      domain: string;
      path: string;
      expires: number;
      httpOnly: boolean;
      secure: boolean;
      sameSite: "Strict" | "Lax" | "None";
    };

    async function extractCookiesFromResponse(
      response: Response,
    ): Promise<CookieSetting[]>;
  ```


# Memory
Source: https://momentic.ai/docs/memory



Momentic can use traces from past test runs to improve AI consistency and
reliability.

## How memory works

Natural language phrases can often be interpreted in different ways. For
example, does the description "the selected tab" refer to "the currently
selected tab", or does it mean "the tab with the text 'Selected'"? What if both
options exist on the page?

In order to eliminate flakiness, it is imperative that AI chooses a single
interpretation for each query across different test runs. To achieve this,
Momentic stores AI completions from successful test runs and supplies those
traces back to the AI agent when generating new completions.

By using past runs' decisions and logical reasoning processes as context, we can
ensure Momentic's AI agents are making consistent decisions.

## When memory is used

Memory is used whenever a step uses AI to locate an element or evaluate an
assertion. This includes interactive steps like `CLICK` as well as assertions
like `AI CHECK` and `ELEMENT CHECK`.

Memory is considered a type of caching and will not be applied if caching is
explicitly disabled for a specific step or at the test level.

## Storage and expiration

Memory is:

* Securely stored on Momentic Cloud.
* Isolated per organization and only accessible during authenticated test runs.
* Automatically expired after 30 days of inactivity.
* Supported by our locator and assertion agents currently.

Momentic automatically chooses the most relevant traces to keep in memory,
preventing memory size from growing indefinitely.

## Failed steps and memory

If enabled, memory is updated whenever a step executes and uses AI. Even if the
test ultimately fails, Momentic still stores a memory entry for that step. This
behavior helps tests fail consistently when there are legitimate errors.

## Enabling memory

Memory can always be controlled on a per-test basis through the test's AI
options in the test editor.

The default setting for memory can be controlled through the organization-level
AI settings on Momentic Cloud, and through the project
[configuration file](/cli/configuration#usememory) when using the CLI.


# app
Source: https://momentic.ai/docs/mobile-cli/commands/app



Start the Momentic app.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic-mobile app
  ```

  ```bash yarn theme={null}
  yarn dlx momentic-mobile app
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic-mobile app
  ```
</CodeGroup>

## Options

### `-c, --config <config>`

Path to the Momentic configuration file. If not specified, it defaults to
`momentic.config.yaml` in the current directory.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic-mobile app --config path/to/momentic.config.yaml
  ```

  ```bash yarn theme={null}
  yarn dlx momentic-mobile app --config path/to/momentic.config.yaml
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic-mobile app --config path/to/momentic.config.yaml
  ```
</CodeGroup>


# assets
Source: https://momentic.ai/docs/mobile-cli/commands/assets



Manage and upload assets.

## `upload`

Upload an APK asset to Momentic Cloud. After upload, this asset can be used in
both the interactive editor and in test runs.

The file provided must exist on disk and be an Android APK (`.apk`).

<CodeGroup>
  ```bash npm theme={null}
  npx momentic-mobile assets upload <file> --channel <channel> [--tag <tag>]
  ```

  ```bash yarn theme={null}
  yarn dlx momentic-mobile assets upload <file> --channel <channel> [--tag <tag>]
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic-mobile assets upload <file> --channel <channel> [--tag <tag>]
  ```
</CodeGroup>

### Options

#### `--channel <channel>`

Release channel for the asset, such as `staging` or `dev`. This name affects how
the APK will be referenced by tests. Channels cannot be renamed after creation.

#### `--tag <tag>`

Version label within the channel. This could be a semantic version like `0.0.1`
or a floating tag like `latest`. If omitted, defaults to `latest`.

## `download`

Download a mobile asset (APK) from Momentic Cloud to the local machine.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic-mobile assets download [path] --channel <channel> --tag <tag>
  ```

  ```bash yarn theme={null}
  yarn dlx momentic-mobile assets download [path] --channel <channel> --tag <tag>
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic-mobile assets download [path] --channel <channel> --tag <tag>
  ```
</CodeGroup>

### Arguments

#### `[path]`

Optional path to download the asset to. Can be a directory or a file path. If
omitted, defaults to the current working directory. If a directory is provided,
the file will be named `<channel>-<tag>.apk`.

### Options

#### `--channel <channel>`

**Required**. Release channel for the asset to download.

#### `--tag <tag>`

**Required**. Version label within the channel to download.


# init
Source: https://momentic.ai/docs/mobile-cli/commands/init



Initialize a new Momentic project and create a
[configuration file](/cli/configuration).

<CodeGroup>
  ```bash npm theme={null}
  npx momentic-mobile init
  ```

  ```bash yarn theme={null}
  yarn dlx momentic-mobile init
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic-mobile init
  ```
</CodeGroup>


# install-browsers
Source: https://momentic.ai/docs/mobile-cli/commands/install-browsers



Install the Chromium browser to automate webviews on Android.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic-mobile install-browsers chromium
  ```

  ```bash yarn theme={null}
  yarn dlx momentic-mobile install-browsers chromium
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic-mobile install-browsers chromium
  ```
</CodeGroup>


# install-skills
Source: https://momentic.ai/docs/mobile-cli/commands/install-skills



Install the Momentic skill so coding assistants get explicit instructions for
using momentic MCP. Without it, agents are more likely to make malformed tool
calls.

Run this after configuring the MCP server. For full setup, see
[MCP](/mobile-cli/model-context-protocol).

<CodeGroup>
  ```bash npm theme={null}
  npx momentic-mobile install-skills [options] [installPath]
  ```

  ```bash yarn theme={null}
  yarn dlx momentic-mobile install-skills [options] [installPath]
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic-mobile install-skills [options] [installPath]
  ```
</CodeGroup>

* **\[installPath]**: Optional target directory. **Mutually exclusive with all
  agent flags.** Either provide a path to install to a custom directory, or use
  one agent flag below, never both.

## Options

Use exactly one of these: either a custom `[installPath]` or one of the agent
flags below.

### `--cursor`

Install into Cursor's default skill directory:
`~/.cursor/skills/momentic-test/SKILL.md`

<CodeGroup>
  ```bash npm theme={null}
  npx momentic-mobile install-skills --cursor
  ```

  ```bash yarn theme={null}
  yarn dlx momentic-mobile install-skills --cursor
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic-mobile install-skills --cursor
  ```
</CodeGroup>

### `--claude-code`

Install into Claude Code's default skill directory:
`~/.claude/skills/momentic-test/SKILL.md`

<CodeGroup>
  ```bash npm theme={null}
  npx momentic-mobile install-skills --claude-code
  ```

  ```bash yarn theme={null}
  yarn dlx momentic-mobile install-skills --claude-code
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic-mobile install-skills --claude-code
  ```
</CodeGroup>

### `--codex`

Install into Codex's default skill directory:
`~/.agents/skills/momentic-test/SKILL.md`

<CodeGroup>
  ```bash npm theme={null}
  npx momentic-mobile install-skills --codex
  ```

  ```bash yarn theme={null}
  yarn dlx momentic-mobile install-skills --codex
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic-mobile install-skills --codex
  ```
</CodeGroup>

### `--opencode`

Install into OpenCode's default skill directory:
`~/.config/opencode/skills/momentic-test/SKILL.md`

<CodeGroup>
  ```bash npm theme={null}
  npx momentic-mobile install-skills --opencode
  ```

  ```bash yarn theme={null}
  yarn dlx momentic-mobile install-skills --opencode
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic-mobile install-skills --opencode
  ```
</CodeGroup>

### `--copilot`

Install into Copilot (VS Code)'s default skill directory:
`~/.copilot/skills/momentic-test/SKILL.md`

<CodeGroup>
  ```bash npm theme={null}
  npx momentic-mobile install-skills --copilot
  ```

  ```bash yarn theme={null}
  yarn dlx momentic-mobile install-skills --copilot
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic-mobile install-skills --copilot
  ```
</CodeGroup>

### Custom path

Install into a custom directory. The command creates `SKILL.md` in the given
path.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic-mobile install-skills ~/my/custom/skills/momentic-test
  ```

  ```bash yarn theme={null}
  yarn dlx momentic-mobile install-skills ~/my/custom/skills/momentic-test
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic-mobile install-skills ~/my/custom/skills/momentic-test
  ```
</CodeGroup>


# list
Source: https://momentic.ai/docs/mobile-cli/commands/list



<Info>**Prerequisites**: These tests must exist locally as YAML files.</Info>

List tests in the current project.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic-mobile list [options] [tests...]
  ```

  ```bash yarn theme={null}
  yarn dlx momentic-mobile list [options] [tests...]
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic-mobile list [options] [tests...]
  ```
</CodeGroup>

* **\[tests...]**: The tests to list. If not specified, selects all tests in the
  current project. You can specify multiple tests separated by spaces, test
  paths, or folder paths. You can also pass substrings to match test names.

## Options

### `-c, --config <config>`

Path to the Momentic configuration file. If not specified, it defaults to
`momentic.config.yaml` in the current directory.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic-mobile list --config path/to/momentic.config.yaml
  ```

  ```bash yarn theme={null}
  yarn dlx momentic-mobile list --config path/to/momentic.config.yaml
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic-mobile list --config path/to/momentic.config.yaml
  ```
</CodeGroup>

### `-f, --filter <filter>`

Only applicable when using [Workspaces](/cli/workspace). Loads the project with
the specified name.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic-mobile list --filter workspace-name
  ```

  ```bash yarn theme={null}
  yarn dlx momentic-mobile list --filter workspace-name
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic-mobile list --filter workspace-name
  ```
</CodeGroup>

### `--include <includePatterns...>`

Only include tests that match the provided regex patterns. Multiple patterns can
be provided. The patterns will be matched against the test file paths and the
pattern only needs to match a part of the path for the test to be included.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic-mobile list --include "billing*"
  ```

  ```bash yarn theme={null}
  yarn dlx momentic-mobile list --include "billing*"
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic-mobile list --include "billing*"
  ```
</CodeGroup>

### `--exclude <excludePatterns...>`

The opposite of `--include`: a test that matches any of the provided regex
patterns will be excluded from running.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic-mobile list --exclude "billing*"
  ```

  ```bash yarn theme={null}
  yarn dlx momentic-mobile list --exclude "billing*"
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic-mobile list --exclude "billing*"
  ```
</CodeGroup>


# mcp
Source: https://momentic.ai/docs/mobile-cli/commands/mcp



Start the MCP (Model Context Protocol) server over stdio so coding assistants
can create, edit, and run Momentic tests. For full setup instructions see
[MCP](/mobile-cli/model-context-protocol).

<Info>
  **Emulators**: Remote emulators cannot be shown headfully with the current
  MCP. Local emulators must run headful (visible UI).
</Info>

All options below can be passed as flags or, where noted, set via environment
variables. CLI flags override environment variables.

```bash theme={null}
npx momentic-mobile mcp [options]
```

## Options

| Setting              | Flag                                       | Environment variable                    | Description                                                                                                                          |
| -------------------- | ------------------------------------------ | --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------ |
| Momentic API key     | `--api-key <key>`                          | `MOMENTIC_API_KEY`                      | Authenticates the MCP server with Momentic APIs.                                                                                     |
| Config file path     | `-c`, `--config <path>`                    | —                                       | Points to the `momentic.config.yaml` file used to load project tests, modules, and environments.                                     |
| Android SDK root     | `--android-home <path>`                    | `ANDROID_HOME`                          | Sets `ANDROID_HOME` for the current MCP process.                                                                                     |
| Java home            | `--java-home <path>`                       | `JAVA_HOME`                             | Sets `JAVA_HOME` for the current MCP process.                                                                                        |
| Session idle timeout | `--session-idle-timeout-minutes <minutes>` | `MOMENTIC_SESSION_IDLE_TIMEOUT_MINUTES` | Idle timeout for MCP sessions in minutes. Sessions inactive for this duration are terminated automatically. Defaults to `5` minutes. |

### `--api-key <key>`

Momentic API key.

```bash theme={null}
npx momentic-mobile mcp --api-key your-api-key
```

### `-c, --config <path>`

Path to the `momentic.config.yaml` file. Required when run from an MCP client;
use an absolute path so the server can resolve it correctly.

```bash theme={null}
npx momentic-mobile mcp --config /absolute/path/to/momentic.config.yaml
```

If your MCP client does not inherit your shell environment, include the Android
SDK and JDK paths directly:

```bash theme={null}
npx momentic-mobile mcp --config /absolute/path/to/momentic.config.yaml --android-home /absolute/path/to/Android/sdk --java-home /absolute/path/to/java-home
```

### `--session-idle-timeout-minutes <minutes>`

Session idle timeout in minutes. MCP sessions that remain idle for this duration
are automatically terminated. Defaults to `5` minutes. Can also be set via the
`MOMENTIC_SESSION_IDLE_TIMEOUT_MINUTES` environment variable.

```bash theme={null}
npx momentic-mobile mcp --session-idle-timeout-minutes 5
```

### `--android-home <path>`

Path to the Android SDK root. This sets `ANDROID_HOME` for the current MCP
process.

### `--java-home <path>`

Path to the Java home directory. This sets `JAVA_HOME` for the current MCP
process.


# results
Source: https://momentic.ai/docs/mobile-cli/commands/results



Manage, view, and upload test results.

## `upload`

Upload test results to Momentic Cloud.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic-mobile results upload <folder>
  ```

  ```bash yarn theme={null}
  yarn dlx momentic-mobile results upload <folder>
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic-mobile results upload <folder>
  ```
</CodeGroup>

* **\<folder>**: The path to the folder containing test results generated by a
  `momentic-mobile run` invocation or by the `momentic-mobile results merge`
  command. `momentic-mobile run`
  [saves local results](/mobile-cli/commands/run#output-dir-\<outputdir>) to the
  folder specified by the `--output-dir` option, which defaults to
  `test-results`.

## `view`

Launch the run viewer to inspect test results locally. Starts a local server,
opens it in your browser, and opens the specified run in the run viewer UI.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic-mobile results view <results> [runId]
  ```

  ```bash yarn theme={null}
  yarn dlx momentic-mobile results view <results> [runId]
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic-mobile results view <results> [runId]
  ```
</CodeGroup>

* **\<results>**: Path to the folder containing a `runs/` subfolder with test
  results. Defaults to `test-results`. `momentic run`
  [saves local results](/cli/commands/run#output-dir-\<outputdir>) to the folder
  specified by the `--output-dir` option.
* **\[runId]**: The run ID to open, correlates to a zip file in the `runs/`
  subfolder of your results directory. For example, for
  `runs/eed92602-7355-43dc-8d79-1c43029bec26.zip` use runId
  `eed92602-7355-43dc-8d79-1c43029bec26`. If not provided, the run viewer opens
  to a table with all runs in the run group within the results directory.

### Options

#### `--port <port>`

Port for the run viewer server. Defaults to `58889`.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic-mobile results view --port 59999 my-results eed92602-7355-43dc-8d79-1c43029bec26
  ```

  ```bash yarn theme={null}
  yarn dlx momentic-mobile results view --port 59999 my-results eed92602-7355-43dc-8d79-1c43029bec26
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic-mobile results view --port 59999 my-results eed92602-7355-43dc-8d79-1c43029bec26
  ```
</CodeGroup>


# run
Source: https://momentic.ai/docs/mobile-cli/commands/run



<Info>**Prerequisites**: These tests must exist locally as YAML files.</Info>

Run Momentic mobile tests in the current project.

By default, tests will output results to a local directory. You can then upload
them to Momentic Cloud using the `momentic-mobile results upload`
[command](/mobile-cli/commands/results).

<CodeGroup>
  ```bash npm theme={null}
  npx momentic-mobile run [options] [tests...]
  ```

  ```bash yarn theme={null}
  yarn dlx momentic-mobile run [options] [tests...]
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic-mobile run [options] [tests...]
  ```
</CodeGroup>

* **\[tests...]**: The tests to run. If not specified, selects all tests in the
  current project. You can specify multiple tests separated by spaces, test
  paths, or folder paths. You can also pass substrings to match test names.

## Options

### `-c, --config <config>`

Path to the Momentic configuration file. Defaults to `momentic.config.yaml` in
the current directory.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic-mobile run --config path/to/momentic.config.yaml
  ```

  ```bash yarn theme={null}
  yarn dlx momentic-mobile run --config path/to/momentic.config.yaml
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic-mobile run --config path/to/momentic.config.yaml
  ```
</CodeGroup>

### `-y, --yes`

Skip all confirmation prompts (defaults to true in CI).

<CodeGroup>
  ```bash npm theme={null}
  npx momentic-mobile run --yes
  ```

  ```bash yarn theme={null}
  yarn dlx momentic-mobile run --yes
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic-mobile run --yes
  ```
</CodeGroup>

### `-p, --parallel <parallel>`

Number of tests to run in parallel. Defaults to `1`.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic-mobile run --parallel 3
  ```

  ```bash yarn theme={null}
  yarn dlx momentic-mobile run --parallel 3
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic-mobile run --parallel 3
  ```
</CodeGroup>

### `--shard-count <shardCount>`

Total number of shards to split the selected tests into. Defaults to `1` (no
sharding).

<CodeGroup>
  ```bash npm theme={null}
  npx momentic-mobile run --shard-count 2
  ```

  ```bash yarn theme={null}
  yarn dlx momentic-mobile run --shard-count 2
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic-mobile run --shard-count 2
  ```
</CodeGroup>

### `--shard-index <shardIndex>`

Which shard to run (1-indexed). Defaults to `1`.

This must be less than or equal to `--shard-count`. To run all tests across 2 CI
workers, run shard 1 on one worker and shard 2 on another:

<CodeGroup>
  ```bash npm theme={null}
  npx momentic-mobile run --shard-index 1 --shard-count 2
  ```

  ```bash yarn theme={null}
  yarn dlx momentic-mobile run --shard-index 1 --shard-count 2
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic-mobile run --shard-index 1 --shard-count 2
  ```
</CodeGroup>

### `--include <includePatterns...>`

Only include tests that match the provided regex patterns. Multiple patterns can
be provided. The patterns will be matched against the test file paths and the
pattern only needs to match a part of the path for the test to be included.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --include "billing*"
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --include "billing*"
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --include "billing*"
  ```
</CodeGroup>

### `--exclude <excludePatterns...>`

The opposite of `--include`: a test that matches any of the provided regex
patterns will be excluded from running.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --exclude "billing*"
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --exclude "billing*"
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --exclude "billing*"
  ```
</CodeGroup>

### `--log-level <logLevel>`

Set logging verbosity. One of: `error`, `warn`, `info`, `debug`.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic-mobile run --log-level debug
  ```

  ```bash yarn theme={null}
  yarn dlx momentic-mobile run --log-level debug
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic-mobile run --log-level debug
  ```
</CodeGroup>

### `--output-dir <outputDir>`

Directory to store run artifacts (screenshots, logs, results). Defaults to the
project’s `outputDir` or `./test-results`. The directory is cleared at the start
of a run.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic-mobile run --output-dir ./mobile-results
  ```

  ```bash yarn theme={null}
  yarn dlx momentic-mobile run --output-dir ./mobile-results
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic-mobile run --output-dir ./mobile-results
  ```
</CodeGroup>

### `--upload-results`

Automatically upload test results to Momentic Cloud after the run (equivalent to
running `momentic-mobile results upload <outputDir>` after completion).

<CodeGroup>
  ```bash npm theme={null}
  npx momentic-mobile run --upload-results
  ```

  ```bash yarn theme={null}
  yarn dlx momentic-mobile run --upload-results
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic-mobile run --upload-results
  ```
</CodeGroup>

### `--channel <channel>`

Override the default release channel for APK selection during this run (e.g.,
`staging`, `dev`). If omitted and no default channel is configured on the test,
Momentic will not install an APK on emulator initialization.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic-mobile run --channel dev
  ```

  ```bash yarn theme={null}
  yarn dlx momentic-mobile run --channel dev
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic-mobile run --channel dev
  ```
</CodeGroup>

### `--tag <tag>`

Override the version tag within the selected channel for APK selection. If
omitted, each test uses the default tag configured, or the latest uploaded APK
in the channel if no default exists.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic-mobile run --channel staging --tag 0.0.1
  ```

  ```bash yarn theme={null}
  yarn dlx momentic-mobile run --channel staging --tag 0.0.1
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic-mobile run --channel staging --tag 0.0.1
  ```
</CodeGroup>

### `--env <env>`

Override the default environment for all tests during this run. The environment
name should exist in your Momentic project configuration. This option takes
precedence over the default environment configured on the test level.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic-mobile run --env staging my-test
  ```

  ```bash yarn theme={null}
  yarn dlx momentic-mobile run --env staging my-test
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic-mobile run --env staging my-test
  ```
</CodeGroup>

### `--name <suiteName>`

A name to assign to the test suite. This will be the suite name in generated
reports and will also be displayed in Momentic Cloud if results are uploaded.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --name my-test-suite
  ```

  ```bash yarn theme={null}
  npx momentic run --name my-test-suite
  ```

  ```bash pnpm theme={null}
  npx momentic run --name my-test-suite
  ```
</CodeGroup>

### `--timeout-minutes <timeoutMinutes>`

Maximum number of minutes to run tests before stopping. When the timeout is
reached, tests will stop and current results will be printed.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic-mobile run --timeout-minutes 30
  ```

  ```bash yarn theme={null}
  yarn dlx momentic-mobile run --timeout-minutes 30
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic-mobile run --timeout-minutes 30
  ```
</CodeGroup>

### `--labels <labels...>`

Run tests with the specified labels. This allows you to filter tests based on
assigned labels.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --labels smoke regression
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --labels smoke regression
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --labels smoke regression
  ```
</CodeGroup>

### `--reporter <reporter>`

Specify the reporter to use for the output.

Options:

* `junit`
* `buildkite-json`

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --reporter junit
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --reporter junit
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --reporter junit
  ```
</CodeGroup>

### `--reporter-dir <reporterDir>`

Specify the directory where the reporter output will be saved. If not specified,
it defaults to `./reports`.

Reporter filenames are based on the suite name. For example, `junit` writes
`{suiteName}.xml` and `buildkite-json` writes `{suiteName}.buildkite.json`.

The suite name comes from `--name` when provided. Otherwise, Momentic uses the
detected project's configured name.

For `buildkite-json`, `scope` comes from the suite name and `name` comes from
the individual test name.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --reporter-dir ./reports
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --reporter-dir ./reports
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --reporter-dir ./reports
  ```
</CodeGroup>

### `--local-avd-id`

Force tests to use a specific local Android Virtual Device (AVD). Overrides all
other configuration at the test and environment level.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic-mobile run --local-avd-id Pixel_10_API_35
  ```

  ```bash yarn theme={null}
  yarn dlx momentic-mobile run --local-avd-id Pixel_10_API_35
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic-mobile run --local-avd-id Pixel_10_API_35
  ```
</CodeGroup>

### `--local-apk-path`

When used together with `local-avd-id`, override the APK that will be installed
on emulator initialization. This takes precedence over all other configuration
at the test and environment level.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic-mobile run --local-avd-id Pixel_10_API_35 --local-apk-path build/debug.apk
  ```

  ```bash yarn theme={null}
  yarn dlx momentic-mobile run --local-avd-id Pixel_10_API_35 --local-apk-path build/debug.apk
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic-mobile run --local-avd-id Pixel_10_API_35 --local-apk-path build/debug.apk
  ```
</CodeGroup>


# Emulators
Source: https://momentic.ai/docs/mobile-cli/emulators

Learn about the different emulator options offered by Momentic.

Momentic offers two options for automating Android apps.

**Remote** emulators are hosted through a third-party provider and offer a
scalable fleet of instances that boot within seconds. Simply upload the APK you
wish to test, and we'll take care of the rest.

**Local** emulators use your local Android Studio installation to create an
emulator that runs on your own machine. In this setup, you'll have to specify an
[Android Virtual Device](https://developer.android.com/studio/run/managing-avds)
(AVD) and APK file that already exist locally.

## Choosing a platform

We recommend that teams use either remote or local emulators for all tests, and
avoid mixing the two.

The platform can be chosen when creating or editing a test through the Region
dropdown menu. Choosing the `Local` region activates the local emulator mode;
selecting any other region activates the remote emulator mode.

## Remote emulators

When using remote emulators, Momentic provides fresh Android instances on-demand
when launching the local app or executing a mobile test. Average provisioning
time is under 1 second.

### Configuration

#### APK

APK installation for remote emulators is managed through **channels** and
**tags**. APKs can be uploaded through the Momentic Mobile app in the Assets
page, or via the `momentic-mobile assets upload`
[command](/mobile-cli/commands/assets).

<Warning>
  If the uploaded APK contains Android `WebView` content that you want to
  automate, enable WebView debugging with
  `WebView.setWebContentsDebuggingEnabled(true)` so Momentic can attach to the
  WebView.
</Warning>

Channels are generally distinct release environments, such as `dev`, `staging`,
and `production`. You can also use channels to separate different apps, such as
`production-trading` and `production-banking`.

Tags are versions within a particular channel. We recommend that teams use
[semver](https://semver.org/) tags, such as `0.0.1` and `1.2.0`, or some other
identifier that can be easily tied to code changes.

When creating or editing a test that uses remote emulators, you will be prompted
to choose a channel and tag.

#### Region

The Region property on each test's settings defines where your emulator will be
created. If unset, the closest region to your IP address will be chosen.

Currently, Momentic's emulator provider supports two regions: US West and EU
North. If you are located far away from both regions, we highly recommend using
local emulators instead for improved latency.

#### Android version

Currently, Android 14 and 15 are supported. This setting can be configured in
each test's options.

## Local emulators

### Configuration

When using local emulators, users are responsible for building, storing, and
sharing AVDs that have the desired settings, including the Android version, Play
Store version, and device size. Users then provide this AVD ID to Momentic.

To install an APK, there are several options:

1. **Install APK step**: Given an APK path that is accessible on disk, you can
   use a preset `Install APK` step at any point in a test.
2. **Test-level APK path setting**: An APK path can be specified in each test's
   settings. This APK will be automatically installed on emulator start.
3. **Inherit APK settings from the environment**: see the section
   [below](#environment-based-settings) on how to read configuration from
   environment variables.

### Environment-based settings

Some teams may not share APKs or AVDs during development. In this case, it can
be cumbersome to constantly change the AVD ID or APK path at the test level.

Configuring these settings at the environment level instead solves this problem.
Specifically, rather than setting AVD ID or APK path at the test level, users
can define the `LOCAL_AVD_ID` and `LOCAL_APK_PATH` keys in an environment. Then,
users can leverage Momentic's ability to interpolate environment variables using
the shell to achieve dynamic behavior on each developer's machine.

For example, the environment below will first read the `LOCAL_AVD_ID` from the
`MOMENTIC_AVD_ID` env var from the surrounding shell, and default to
`Pixel_9_API_35` if this env var is unset. Similarly, the local APK path will
first be read from the `MOMENTIC_APK_PATH` env var.

```yaml momentic.config.yaml theme={null}
environments:
  - name: local
    envVariables:
      LOCAL_AVD_ID: ${MOMENTIC_AVD_ID:-Pixel_9_API_35}
      LOCAL_APK_PATH: ${MOMENTIC_APK_PATH:-../../data/android-test-apks/drag-drop-native/app-debug.apk}
```

Each developer then can set their own `MOMENTIC_AVD_ID` and `MOMENTIC_APK_PATH`
in a `.env` file or in their `~/.zshrc`, avoiding the need to commit these
configuration changes to source control.

Note that environment-based configuration is only active if the test is set to
run in that environment. In addition, there cannot be any overrides at the test
level.

### Overrides in CI

When executing tests in CI, Momentic's [run](/mobile-cli/commands/run) command
supports the `--local-avd-id` and `--local-apk-path` flags to make overriding
local emulator configuration easy. These flags take precedence over all other
configuration.


# MCP
Source: https://momentic.ai/docs/mobile-cli/model-context-protocol



<Warning>Requires Momentic mobile CLI version 0.55.1 or greater.</Warning>

<Info>Currently only one emulator can run at a time.</Info>

Momentic's MCP server exposes tools so agents can:

* Browse tests, modules, and environments
* Edit tests and modules via tool calls (not direct YAML edits)
* Create tests from natural language
* Run sessions with a live emulator

## Prerequisites

* **Momentic-mobile CLI installed**: MCP is local only and requires the
  [Momentic-mobile CLI](/mobile-cli/setup) on your machine.
* **Project setup complete**: Finish CLI setup and ensure your project includes
  a valid `momentic.config.yaml`.

## Step 1: Set up your MCP client

<Tip>
  The MCP shell command must have access to `MOMENTIC_API_KEY`, `JAVA_HOME`, and
  `ANDROID_HOME` directly in the MCP command. You can provide it through the MCP
  server `env` block or pass the `--api-key`, `--java-home`, and `--android-home`
  flags directly to `momentic-mobile mcp`. Most MCP servers do *not* inherit your
  usual shell environment variables.
</Tip>

All configurations below use an absolute path to `momentic.config.yaml`. Replace
it with your project's actual path. For additional options, see the
[mcp command](/mobile-cli/commands/mcp).

<Tabs>
  <Tab title="Cursor">
    **Setup Steps**:

    1. Open Cursor's command palette (usually Cmd+Shift+P on Mac OS).
    2. Search for and select the "View: Open MCP Settings" command.
    3. Click "Add a new Custom MCP server".
    4. Add a block in the JSON file for "momentic-mobile" based on the code sample below. Replace the path with your true `momentic.config.yaml` location.
    5. Restart Cursor.

    ```json theme={null}
    {
      "mcpServers": {
        "momentic-mobile": {
          "type": "stdio",
          "command": "npx",
          "args": [
            "momentic-mobile",
            "mcp",
            "--config",
            "/absolute/path/to/momentic.config.yaml",
            "--android-home",
            "/absolute/path/to/Android/sdk",
            "--java-home",
            "/absolute/path/to/java-home"
          ]
        }
      }
    }
    ```

    <Accordion title="Full configuration example (all options)">
      These settings are optional.

      ```json theme={null}
      {
        "mcpServers": {
          "momentic-mobile": {
            "type": "stdio",
            "command": "npx",
            "args": [
              "momentic-mobile",
              "mcp",
              "--config",
              "/absolute/path/to/momentic.config.yaml",
              "--android-home",
              "/absolute/path/to/Android/sdk",
              "--java-home",
              "/absolute/path/to/java-home",
              "--session-idle-timeout-minutes",
              "5"
            ],
            "env": {
              "MOMENTIC_API_KEY": "your-api-key",
              "ANDROID_HOME": "/absolute/path/to/Android/sdk",
              "JAVA_HOME": "/absolute/path/to/java-home"
            }
          }
        }
      }
      ```
    </Accordion>
  </Tab>

  <Tab title="VS Code (GitHub Copilot)">
    **Setup Steps**:

    1. Open the Command Palette (Shift+Command+P on macOS, Shift+Ctrl+P on
       Windows/Linux).
    2. Type and select **MCP: Add Server**.
    3. Choose the **Command (stdio)** option.
    4. Add the **`momentic-mobile`** MCP server using the configuration below
       (replace the config path with your project's `momentic.config.yaml`):

    ```json theme={null}
    {
      "mcpServers": {
        "momentic-mobile": {
          "type": "stdio",
          "command": "npx",
          "args": [
            "momentic-mobile",
            "mcp",
            "--config",
            "/absolute/path/to/momentic.config.yaml",
            "--android-home",
            "/absolute/path/to/Android/sdk",
            "--java-home",
            "/absolute/path/to/java-home"
          ]
        }
      }
    }
    ```

    <Accordion title="Full configuration example (all options)">
      These settings are optional.

      ```json theme={null}
      {
        "mcpServers": {
          "momentic-mobile": {
            "type": "stdio",
            "command": "npx",
            "args": [
              "momentic-mobile",
              "mcp",
              "--config",
              "/absolute/path/to/momentic.config.yaml",
              "--android-home",
              "/absolute/path/to/Android/sdk",
              "--java-home",
              "/absolute/path/to/java-home",
              "--session-idle-timeout-minutes",
              "5"
            ],
            "env": {
              "MOMENTIC_API_KEY": "your-api-key"
            }
          }
        }
      }
      ```
    </Accordion>

    5. Name the server when prompted (e.g., "momentic-mobile").
    6. Open Extensions and confirm the MCP server connects and detects the tools.
    7. Allow all tools from Momentic.

    GitHub Copilot may require your organization to allow MCP server usage. VS Code may only allow MCP usage in agent mode.
  </Tab>

  <Tab title="Claude Code">
    **Setup Steps**:

    1. Open your terminal and navigate to your project directory.
    2. Run the command below. Replace the config path with your
       project's `momentic.config.yaml`. To add optional settings (API key,
       session idle timeout), see the [mcp command](/mobile-cli/commands/mcp).

    ```bash theme={null}
    claude mcp add --transport stdio momentic-mobile -- npx momentic-mobile mcp --config /absolute/path/to/momentic.config.yaml
    ```

    3. Verify the server is configured: `claude mcp list`.
    4. Restart Claude Code if it was already running.

    **Note:** All options (e.g. `--transport stdio`, `--env`) must come before the
    server name. The `--` separates the server name from the command and its
    arguments.

    **Windows:** On native Windows (not WSL), wrap `npx` with `cmd /c`:
    `claude mcp add --transport stdio momentic-mobile -- cmd /c npx momentic-mobile mcp --config C:\path\to\momentic.config.yaml`

    Need help configuring advanced Claude flags (for example `--env`,
    `--scope`, or auth options)? See [Claude Code MCP server
    setup](https://code.claude.com/docs/en/mcp#option-3-add-a-local-stdio-server).
  </Tab>

  <Tab title="Codex">
    **Setup Steps**:

    1. Open your terminal in your project directory (or ensure the config path is
       absolute).
    2. Run the command below. Replace the config path with your
       project's `momentic.config.yaml`. To add optional settings (API key,
       session idle timeout), see the [mcp command](/mobile-cli/commands/mcp).
    3. Codex saves this configuration to `~/.codex/config.toml`. You can always edit your MCP configuration through this file.
    4. Restart Codex. Open a new chat and type `/mcp` to confirm that the Momentic mobile MCP server is active.

    ```bash theme={null}
    codex mcp add momentic-mobile -- npx momentic-mobile mcp --config /absolute/path/to/momentic.config.yaml --api-key your-api-key --android-home /absolute/path/to/Android/sdk --java-home /absolute/path/to/java-home
    ```

    3. For advanced configuration, edit `~/.codex/config.toml` (or
       project-scoped `.codex/config.toml` in trusted projects).
    4. Verify MCP servers from Codex by running `/mcp` in the Codex TUI.
    5. If tools don’t appear, restart Codex.

    Refer to the [Codex docs](https://developers.openai.com/codex/mcp/) for help configuring advanced Codex MCP options such as environment variables and timeouts.
  </Tab>

  <Tab title="OpenCode">
    **Setup Steps**:

    1. Edit `opencode.json` or `opencode.jsonc` in your project root or global
       config (`~/.config/opencode/`). See [OpenCode MCP
       docs](https://opencode.ai/docs/mcp-servers/).
    2. Add the Momentic mobile MCP server under the `mcp` key. Replace the config path with your project's `momentic.config.yaml`.
    3. Start OpenCode.

    ```json theme={null}
    {
      "mcp": {
        "momentic-mobile": {
          "type": "local",
          "command": [
            "npx",
            "momentic-mobile",
            "mcp",
            "--config",
            "/absolute/path/to/momentic.config.yaml",
            "--android-home",
            "/absolute/path/to/Android/sdk",
            "--java-home",
            "/absolute/path/to/java-home"
          ],
          "enabled": true
        }
      }
    }
    ```

    <Accordion title="Full configuration example (all options)">
      These settings are optional.

      ```json theme={null}
      {
        "mcp": {
          "momentic-mobile": {
            "type": "local",
            "command": [
              "npx",
              "momentic-mobile",
              "mcp",
              "--config",
              "/absolute/path/to/momentic.config.yaml",
              "--android-home",
              "/absolute/path/to/Android/sdk",
              "--java-home",
              "/absolute/path/to/java-home",
              "--session-idle-timeout-minutes",
              "5"
            ],
            "enabled": true,
            "environment": {
              "MOMENTIC_API_KEY": "your-api-key"
            }
          }
        }
      }
      ```
    </Accordion>
  </Tab>
</Tabs>

## Step 2: Install the Momentic skill

The Momentic skill gives your assistant explicit operating guidance for Momentic
workflows: it teaches the model how to build reliable tests, construct test
steps correctly, reuse modules in your workspace, and more.

Without a skill, coding agents are far more likely to make malformed tool calls
and waste time on unnecessary actions.

<Card>
  <Tabs>
    <Tab title="Cursor">
      [Global skill directory](https://cursor.com/docs/context/skills):
      `~/.cursor/skills/momentic-test/SKILL.md`

      Cursor respected directories:

      * `~/.cursor/skills/<name>/SKILL.md`
      * `~/.claude/skills/<name>/SKILL.md`
      * `~/.codex/skills/<name>/SKILL.md`

      ```bash theme={null}
      npx momentic-mobile install-skills --cursor
      ```
    </Tab>

    <Tab title="Claude Code">
      [Global skill directory](https://code.claude.com/docs/en/skills):
      `~/.claude/skills/momentic-test/SKILL.md`

      Claude Code respected directories:

      * `~/.claude/skills/<name>/SKILL.md`

      ```bash theme={null}
      npx momentic-mobile install-skills --claude-code
      ```
    </Tab>

    <Tab title="Codex">
      [Global skill directory](https://developers.openai.com/codex/skills):
      `~/.agents/skills/momentic-test/SKILL.md`

      Codex respected directories:

      * `~/.agents/skills/<name>/SKILL.md`

      ```bash theme={null}
      npx momentic-mobile install-skills --codex
      ```
    </Tab>

    <Tab title="OpenCode">
      [Global skill directory](https://opencode.ai/docs/skills/):
      `~/.config/opencode/skills/momentic-test/SKILL.md`

      OpenCode respected directories:

      * `~/.config/opencode/skills/<name>/SKILL.md`
      * `~/.claude/skills/<name>/SKILL.md`
      * `~/.agents/skills/<name>/SKILL.md`

      ```bash theme={null}
      npx momentic-mobile install-skills --opencode
      ```
    </Tab>

    <Tab title="Copilot (VS Code)">
      [Global skill directory](https://code.visualstudio.com/docs/copilot/customization/agent-skills):
      `~/.copilot/skills/momentic-test/SKILL.md`

      Copilot respected directories:

      * `~/.copilot/skills/<name>/SKILL.md`
      * `~/.claude/skills/<name>/SKILL.md`
      * `~/.agents/skills/<name>/SKILL.md`

      ```bash theme={null}
      npx momentic-mobile install-skills --copilot
      ```
    </Tab>

    <Tab title="Custom path">
      ```bash theme={null}
      npx momentic-mobile install-skills ~/my/custom/skills/momentic-test
      ```
    </Tab>
  </Tabs>
</Card>

## Step 3: Add an agent rule

Agent rules are stronger, global rulesets that agents are trained to strongly
respect. They are usually stored in an `AGENTS.md` file at the root of your
codebase. Some agents also support rules in their own custom directory (e.g.
`.cursor/rules`).

We recommend adding one of the following lines to your rules to prevent agents
from bypassing Momentic's MCP tools completely and directly editing your test or
module YAML files. Direct edits will likely lead to parsing and caching errors.

```bash theme={null}
Never directly edit Momentic test (`*.test.yaml`) or module YAMLs (`*.module.yaml`). Only use the Momentic MCP tools to edit Momentic YAMLs. If they are unavailable tell the user you are unable to edit the YAML files.
```

## Step 4: Verify installation

The MCP server should now show up in a status page within your coding agent.
CLI-based tools usually provide a command like `/mcp` to view all installed MCP
servers.

Start a new chat and ask the agent what MCP servers and tools are available. It
should list tools whose names start with `momentic_`, such as
`momentic_get_artifacts`. If tools don’t appear, restart the IDE completely.

You're now ready to use Momentic's MCP! Select the Momentic skill and then
insert your desired goal.

## Usage

1. **Model selection**: Choose the latest frontier models for the best
   performance. As of version `0.55.1`, Momentic has benchmarked MCP performance
   on `GPT5.4`. If current agent performance is acceptable, `Medium` reasoning
   can improve speed by about 20%.
2. **Invoke Momentic's skill**: Explicitly invoke the skill in your assistant
   (e.g. in Codex, type `/momentic` and choose the autocompleted skill).
3. **Prompting**: Specific instructions generally lead to better outcomes. For
   exploratory testing, we recommend specifying a step limit so that the agent
   knows when to stop.
4. **Session management**: Allow sessions to clean up properly. You should
   notice the model calling the `momentic_session_terminate` tool, which will
   shut down the emulator session. Repeatedly stopping your coding agent may
   leak emulator resources and slow down your machine.

## Configurable settings

For all available flags and environment variables, see the
[mcp command reference](/mobile-cli/commands/mcp).


# Setup
Source: https://momentic.ai/docs/mobile-cli/setup

This guide will walk you through building your first mobile test locally and integrating into CI/CD

## Prerequisites

<Info>
  If you already have these installed, skip to the verification steps below.
</Info>

The Momentic CLI requires the following tools:

* Node.js: version 20.19.0 or later
* Java JDK: version 24 recommended
* Android Studio: latest stable version, including platform tools.
  * `ANDROID_HOME` must be set in your shell to your SDK install folder.

### Install Node.js

Download [Node.js 20.19.0 or later](https://nodejs.org/en/download). To verify
your installation:

```bash theme={null}
node -v  # v20.19.0 or later
```

### Install Java

Download [JDK version 24](https://www.oracle.com/java/technologies/downloads/)
from Oracle.

To verify your installation:

```bash theme={null}
java --version  # should show JDK 24
```

<Info>
  If `java --version` is not found, re-open your terminal or ensure
  `JAVA_HOME/bin` is in your PATH.
</Info>

### Install Android Studio (+ SDK + Platform Tools)

Download [Android Studio](https://developer.android.com/studio) and complete the
first-run setup wizard. If prompted, ensure you include the following tools:

* Android SDK Platform-Tools (ADB)
* Android Emulator

### Set ANDROID\_HOME

Set the `ANDROID_HOME` environment variable in your shell. This should point to
the root of your Android SDK installation.

Typical installation locations are listed below:

* macOS: `/Users/<username>/Library/Android/sdk`
* Windows: `C:\\Users\\<username>\\AppData\\Local\\Android\\Sdk`
* Linux: `/home/<username>/Android/Sdk`

<Tabs>
  <Tab title="macOS (zsh)">
    ```bash theme={null}
    echo 'export ANDROID_HOME="$HOME/Library/Android/sdk"' >> ~/.zshrc
    echo 'export PATH="$ANDROID_HOME/platform-tools:$ANDROID_HOME/emulator:$PATH"' >> ~/.zshrc
    source ~/.zshrc
    ```
  </Tab>

  <Tab title="Linux (bash/zsh)">
    Adjust the path if your SDK is elsewhere:

    ```bash theme={null}
    echo 'export ANDROID_HOME="$HOME/Android/Sdk"' >> ~/.bashrc
    echo 'export PATH="$ANDROID_HOME/platform-tools:$ANDROID_HOME/emulator:$PATH"' >> ~/.bashrc
    source ~/.bashrc
    ```
  </Tab>

  <Tab title="Windows">
    Follow the official guidance to set `ANDROID_HOME`:
    [https://developer.android.com/tools/variables](https://developer.android.com/tools/variables)
  </Tab>
</Tabs>

### Verify your setup

Run the following commands; all should succeed without errors:

```bash theme={null}
node -v                # expect v20.19.0 or later
java --version         # expect JDK 24
echo $ANDROID_HOME     # prints your SDK path
```

If any check fails:

* Re-open your terminal or source your profile after editing it.
* Ensure Platform-Tools are installed via Android Studio’s SDK Manager.
* Confirm `ANDROID_HOME` matches your actual SDK path.
* On Windows, ensure environment variables are set in System Properties and
  restart your shell.

## Installation

### Get your API key

To get started, log in to
[Momentic Cloud](https://app.momentic.ai/settings/api-keys) and generate an API
key.

<Frame>
  <img />
</Frame>

You can export the API key in your shell configuration file (usually `.bashrc`
or `.zshrc`) like so:

```bash theme={null}
export MOMENTIC_API_KEY=your-api-key
```

### Install the CLI

Before proceeding, ensure a `package.json` file already exists in your project.
If you don’t, run `npm init`, `yarn init`, or `pnpm init` to create the file
beforehand.

Install the [momentic-mobile](https://www.npmjs.com/package/momentic-mobile) CLI
by running the following command in your terminal:

<CodeGroup>
  ```bash npm theme={null}
  npm install momentic-mobile --save-dev
  ```

  ```bash yarn theme={null}
  yarn add momentic-mobile --dev --ignore-workspace-root-check
  ```

  ```bash pnpm theme={null}
  pnpm add momentic-mobile --save-dev --ignore-workspace-root-check
  ```
</CodeGroup>

## Start building locally

### Install Chromium

To automate webviews, Momentic uses a headless browser. You can install it using
the following command:

<CodeGroup>
  ```bash npm theme={null}
  npx momentic-mobile install-browsers chromium
  ```

  ```bash yarn theme={null}
  yarn dlx momentic-mobile install-browsers chromium
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic-mobile install-browsers chromium
  ```
</CodeGroup>

### Enable Android WebView debugging in your app

If your app renders content inside an Android `WebView`, enable WebView
debugging so Momentic can attach and interact with elements inside the webview.

Add the following in your app startup code before the relevant `WebView` is
used:

```java theme={null}
WebView.setWebContentsDebuggingEnabled(true);
```

<Warning>
  If this is not enabled, Momentic cannot attach to the WebView. Interactions
  against elements inside that WebView may fail with `InternalWebAgentError: No
      browser controller is attached to the requested webview.`
</Warning>

### Initialize a new project

<Info>
  If you already have a `momentic.config.yaml` file for browser testing, you can
  skip this step and reuse the same project.
</Info>

Create a new Momentic project by running the following command in your terminal:

<CodeGroup>
  ```bash npm theme={null}
  npx momentic-mobile init
  ```

  ```bash yarn theme={null}
  yarn dlx momentic-mobile init
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic-mobile init
  ```
</CodeGroup>

## Start the local app

Start the local app UI by running the following command in your terminal:

<CodeGroup>
  ```bash npm theme={null}
  npx momentic-mobile app
  ```

  ```bash yarn theme={null}
  yarn dlx momentic-mobile app
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic-mobile app
  ```
</CodeGroup>


# MCP
Source: https://momentic.ai/docs/model-context-protocol



<Warning>Requires Momentic CLI version 2.54.0 or greater.</Warning>

Momentic's MCP server exposes tools so agents can:

* Browse tests, modules, and environments
* Edit tests and modules via tool calls (not direct YAML edits)
* Create tests from natural language
* Run sessions with a live browser

## Prerequisites

* **Momentic CLI installed**: MCP is local only and requires the
  [Momentic CLI](/quickstart/cli) on your machine.
* **Project setup complete**: Finish CLI setup and ensure your project includes
  a valid `momentic.config.yaml`.

## Step 1: Set up your MCP client

<Tip>
  The MCP shell command must have access to `MOMENTIC_API_KEY`. You can provide it
  through the MCP server `env` block or pass the `--api-key` flag directly to
  `momentic mcp`. Most MCP servers do *not* inherit your usual shell environment
  variables.
</Tip>

All configurations below use an absolute path to `momentic.config.yaml`. Replace
it with your project's actual path. For additional options, see the
[mcp command](/cli/commands/mcp).

<Tabs>
  <Tab title="Cursor">
    **Setup Steps**:

    1. Open Cursor's command palette (usually Cmd+Shift+P on Mac OS).
    2. Search for and select the "View: Open MCP Settings" command.
    3. Click "Add a new Custom MCP server".
    4. Add a block in the JSON file for "momentic" based on the code sample below. Replace the path with your true `momentic.config.yaml` location.
    5. Restart Cursor.

    ```json theme={null}
    {
      "mcpServers": {
        "momentic": {
          "type": "stdio",
          "command": "npx",
          "args": ["momentic", "mcp", "--config", "/absolute/path/to/momentic.config.yaml"]
        }
      }
    }
    ```

    <Accordion title="Full configuration example (all options)">
      These settings are optional.

      ```json theme={null}
      {
        "mcpServers": {
          "momentic": {
            "type": "stdio",
            "command": "npx",
            "args": [
              "momentic",
              "mcp",
              "--config",
              "/absolute/path/to/momentic.config.yaml",
              "--headful-browser",
              "false",
              "--pixel-ratio",
              "2",
              "--session-idle-timeout-minutes",
              "5"
            ],
            "env": {
              "MOMENTIC_API_KEY": "your-api-key"
            }
          }
        }
      }
      ```
    </Accordion>
  </Tab>

  <Tab title="VS Code (GitHub Copilot)">
    **Setup Steps**:

    1. Open the Command Palette (Shift+Command+P on macOS, Shift+Ctrl+P on
       Windows/Linux).
    2. Type and select **MCP: Add Server**.
    3. Choose the **Command (stdio)** option.
    4. Add the Momentic MCP server using the configuration below (replace
       the config path with your project's `momentic.config.yaml`):

    ```json theme={null}
    {
      "mcpServers": {
        "momentic": {
          "type": "stdio",
          "command": "npx",
          "args": ["momentic", "mcp", "--config", "/absolute/path/to/momentic.config.yaml"]
        }
      }
    }
    ```

    <Accordion title="Full configuration example (all options)">
      These settings are optional.

      ```json theme={null}
      {
        "mcpServers": {
          "momentic": {
            "type": "stdio",
            "command": "npx",
            "args": [
              "momentic",
              "mcp",
              "--config",
              "/absolute/path/to/momentic.config.yaml",
              "--headful-browser",
              "false",
              "--pixel-ratio",
              "2",
              "--session-idle-timeout-minutes",
              "5"
            ],
            "env": {
              "MOMENTIC_API_KEY": "your-api-key"
            }
          }
        }
      }
      ```
    </Accordion>

    5. Name the server when prompted (e.g., "momentic").
    6. Open Extensions and confirm the MCP server connects and detects the tools.
    7. Allow all tools from Momentic.

    GitHub Copilot may require your organization to allow MCP server usage. VS Code may only allow MCP usage in agent mode.
  </Tab>

  <Tab title="Claude Code">
    **Setup Steps**:

    1. Open your terminal and navigate to your project directory.
    2. Run the command below. Replace the config path with your
       project's `momentic.config.yaml`. To add optional settings (API key,
       headful browser, pixel ratio), see the [mcp command](/cli/commands/mcp).

    ```bash theme={null}
    claude mcp add --transport stdio momentic -- npx momentic mcp --config /absolute/path/to/momentic.config.yaml
    ```

    3. Verify the server is configured: `claude mcp list`.
    4. Restart Claude Code if it was already running.

    **Note:** All options (e.g. `--transport stdio`, `--env`) must come before the
    server name. The `--` separates the server name from the command and its
    arguments.

    **Windows:** On native Windows (not WSL), wrap `npx` with `cmd /c`:
    `claude mcp add --transport stdio momentic -- cmd /c npx momentic mcp --config C:\path\to\momentic.config.yaml`

    Need help configuring advanced Claude flags (for example `--env`,
    `--scope`, or auth options)? See [Claude Code MCP server
    setup](https://code.claude.com/docs/en/mcp#option-3-add-a-local-stdio-server).
  </Tab>

  <Tab title="Codex">
    **Setup Steps**:

    1. Open your terminal in your project directory (or ensure the config path is
       absolute).
    2. Run the command below. Replace the config path with your
       project's `momentic.config.yaml`. To add optional settings (API key,
       headful browser, pixel ratio), see the [mcp command](/cli/commands/mcp).
    3. Codex saves this configuration to `~/.codex/config.toml`. You can always edit your MCP configuration through this file.
    4. Restart Codex. Open a new chat and type `/mcp` to confirm that the Momentic MCP is active.

    ```bash theme={null}
    codex mcp add momentic -- npx momentic mcp --config /absolute/path/to/momentic.config.yaml
    ```

    3. For advanced configuration, edit `~/.codex/config.toml` (or
       project-scoped `.codex/config.toml` in trusted projects).
    4. Verify MCP servers from Codex by running `/mcp` in the Codex TUI.
    5. If tools don’t appear, restart Codex.

    Refer to the [Codex docs](https://developers.openai.com/codex/mcp/) for help configuring advanced Codex MCP options such as environment variables and timeouts.
  </Tab>

  <Tab title="OpenCode">
    **Setup Steps**:

    1. Edit `opencode.json` or `opencode.jsonc` in your project root or global
       config (`~/.config/opencode/`). See [OpenCode MCP
       docs](https://opencode.ai/docs/mcp-servers/).
    2. Add the Momentic MCP server under the `mcp` key. Replace the config path
       with your project's `momentic.config.yaml`.
    3. Start OpenCode.

    ```json theme={null}
    {
      "mcp": {
        "momentic": {
          "type": "local",
          "command": ["npx", "momentic", "mcp", "--config", "/absolute/path/to/momentic.config.yaml"],
          "enabled": true
        }
      }
    }
    ```

    <Accordion title="Full configuration example (all options)">
      These settings are optional.

      ```json theme={null}
      {
        "mcp": {
          "momentic": {
            "type": "local",
            "command": [
              "npx",
              "momentic",
              "mcp",
              "--config",
              "/absolute/path/to/momentic.config.yaml",
              "--headful-browser",
              "false",
              "--pixel-ratio",
              "2",
              "--session-idle-timeout-minutes",
              "5"
            ],
            "enabled": true,
            "environment": {
              "MOMENTIC_API_KEY": "your-api-key"
            }
          }
        }
      }
      ```
    </Accordion>
  </Tab>
</Tabs>

## Step 2: Install the Momentic skill

The Momentic skill gives your assistant explicit operating guidance for Momentic
workflows: it teaches the model how to build reliable tests, construct test
steps correctly, reuse modules in your workspace, and more.

Without a skill, coding agents are far more likely to make malformed tool calls
and waste time on unnecessary actions.

<Card>
  <Tabs>
    <Tab title="Cursor">
      [Global skill directory](https://cursor.com/docs/context/skills):
      `~/.cursor/skills/momentic-test/SKILL.md`

      Cursor respected directories:

      * `~/.cursor/skills/<name>/SKILL.md`
      * `~/.claude/skills/<name>/SKILL.md`
      * `~/.codex/skills/<name>/SKILL.md`

      ```bash theme={null}
      npx momentic install-skills --cursor
      ```
    </Tab>

    <Tab title="Claude Code">
      [Global skill directory](https://code.claude.com/docs/en/skills):
      `~/.claude/skills/momentic-test/SKILL.md`

      Claude Code respected directories:

      * `~/.claude/skills/<name>/SKILL.md`

      ```bash theme={null}
      npx momentic install-skills --claude-code
      ```
    </Tab>

    <Tab title="Codex">
      [Global skill directory](https://developers.openai.com/codex/skills):
      `~/.agents/skills/momentic-test/SKILL.md`

      Codex respected directories:

      * `~/.agents/skills/<name>/SKILL.md`

      ```bash theme={null}
      npx momentic install-skills --codex
      ```
    </Tab>

    <Tab title="OpenCode">
      [Global skill directory](https://opencode.ai/docs/skills/):
      `~/.config/opencode/skills/momentic-test/SKILL.md`

      OpenCode respected directories:

      * `~/.config/opencode/skills/<name>/SKILL.md`
      * `~/.claude/skills/<name>/SKILL.md`
      * `~/.agents/skills/<name>/SKILL.md`

      ```bash theme={null}
      npx momentic install-skills --opencode
      ```
    </Tab>

    <Tab title="Copilot (VS Code)">
      [Global skill directory](https://code.visualstudio.com/docs/copilot/customization/agent-skills):
      `~/.copilot/skills/momentic-test/SKILL.md`

      Copilot respected directories:

      * `~/.copilot/skills/<name>/SKILL.md`
      * `~/.claude/skills/<name>/SKILL.md`
      * `~/.agents/skills/<name>/SKILL.md`

      ```bash theme={null}
      npx momentic install-skills --copilot
      ```
    </Tab>

    <Tab title="Custom path">
      ```bash theme={null}
      npx momentic install-skills ~/my/custom/skills/momentic-test
      ```
    </Tab>
  </Tabs>
</Card>

## Step 3: Add an agent rule

Agent rules are stronger, global rulesets that agents are trained to strongly
respect. They are usually stored in an `AGENTS.md` file at the root of your
codebase. Some agents also support rules in their own custom directory (e.g.
`.cursor/rules`).

We recommend adding one of the following lines to your rules to prevent agents
from bypassing Momentic's MCP tools completely and directly editing your test or
module YAML files. Direct edits will likely lead to parsing and caching errors.

```bash theme={null}
Never directly edit Momentic test (`*.test.yaml`) or module YAMLs (`*.module.yaml`). Only use the Momentic MCP tools to edit Momentic YAMLs. If they are unavailable tell the user you are unable to edit the YAML files.
```

## Step 4: Verify installation

The MCP server should now show up in a status page within your coding agent.
CLI-based tools usually provide a command like `/mcp` to view all installed MCP
servers.

Start a new chat and ask the agent what MCP servers and tools are available. It
should list `momentic_` tools such as `momentic_get_artifacts`. If tools don’t
appear, restart the IDE completely.

You're now ready to use Momentic's MCP! Select the Momentic skill and then
insert your desired goal.

## Usage

1. **Model selection**: Choose the latest frontier models for the best
   performance. As of version `2.53.0`, Momentic has benchmarked MCP performance
   on `GPT5.3 Codex (High)` and `Opus 4.6 (High)`. If current agent performance
   is acceptable, `Medium` reasoning can improve speed by about 20%.
2. **Invoke Momentic's skill**: Explicitly invoke the skill in your assistant
   (e.g. in Codex, type `/momentic` and choose the autocompleted skill).
3. **Prompting**: Specific instructions generally lead to better outcomes. For
   exploratory testing, we recommend specifying a step limit so that the agent
   knows when to stop.
4. **Session management**: Allow sessions to clean up properly. You should
   notice the model calling the `momentic_session_terminate` tool, which will
   close the browser instance. Repeatedly stopping your coding agent may leak
   browser resources and slow down your machine.

<Accordion title="Full Chat Stream Example: Creating and Editing a YC Website Test">
  **User Request:**

  ```
  create a new test called demo test for the yc website

  Then once you create that test load its full data, use this to then edit the test

  click on the companies tab
  choose a major name brand company and click on their profile
  check that the team size is visible
  click on the jobs tab
  assert that the blurb about what the company does is no longer visible
  ```

  **AI Response:**

  I'll help you create a new test for the YC website and then edit it according to
  your specifications. Let me start by creating the test and then loading its data
  to edit it.

  *Creates TODO list:*

  * Create a new test called demo test for the YC website \[in\_progress]
  * Edit the test to implement the specified flow \[pending]

  <Accordion title="momentic_test_create">
    **Parameters:**

    ```yaml theme={null}
    name: "demo-test"
    baseUrl: "https://www.ycombinator.com"
    description: "Test for YC website - companies tab navigation and job page verification"
    ```

    **Result:** Successfully created test with ID
    391f065b-48f3-4548-ab15-079543fa69e0
  </Accordion>

  <Accordion title="momentic_test_edit">
    **Parameters:**

    ```yaml theme={null}
    id: "391f065b-48f3-4548-ab15-079543fa69e0"
    message: |
      Add test steps to:
      1. Navigate to the YC website
      2. Click on the 'Companies' tab
      3. Find and click on a major brand company like DoorDash or Coinbase
      4. Verify that the team size is visible on the company profile
      5. Click on the 'Jobs' tab
      6. Assert that the company description blurb is no longer visible on the jobs page
    ```

    **Result:** Test successfully updated with 7 automated steps:

    1. Navigate to [https://www.ycombinator.com](https://www.ycombinator.com)
    2. Click on "Companies" tab in navigation
    3. Verify companies list is displayed
    4. Click on DoorDash company profile
    5. Assert team size (8600) is visible
    6. Click on "Jobs" tab
    7. Assert detailed company description is not visible on jobs page
  </Accordion>

  **Final Result:** ✅ Created "demo-test" for YC website ✅ Implemented complete
  user flow with proper assertions ✅ Test validates team size visibility and
  content changes between tabs ✅ Ready to execute with 7 comprehensive test steps

  The AI successfully:

  * Created a new test with appropriate configuration
  * Loaded and analyzed the test structure
  * Converted natural language requirements into specific test steps
  * Chose DoorDash as the major brand company example
  * Added proper assertions for team size visibility and content validation
  * Generated executable test steps ready for automation
</Accordion>

## Configurable settings

For all available flags and environment variables, see the
[mcp command reference](/cli/commands/mcp).

## Alternative protocol: Streamable HTTP

<Warning>
  Streamable HTTP is deprecated and may be removed in a future release. We
  highly recommend migrating to the Stdio transport.
</Warning>

If you prefer to connect via the Momentic desktop app instead of the Stdio CLI,
you can use Streamable HTTP. This requires the Momentic app to be running before
connecting.

**Streamable HTTP Transport** (available in Momentic >= 2.17.2):

```
POST/GET/DELETE /api/mcp/
Header: mcp-session-id: <session-id>
url: http://localhost:58888/api/mcp
```

### IDE configuration

<Tabs>
  <Tab title="Cursor">
    ```json theme={null}
    {
      "mcpServers": {
        "momentic": {
          "url": "http://localhost:58888/api/mcp"
        }
      }
    }
    ```

    Make sure you have [started the local app](/cli/commands/app) before connecting. If tools don't appear, restart both the IDE and the Momentic desktop server.
  </Tab>

  <Tab title="Windsurf">
    ```json theme={null}
    {
      "mcpServers": {
        "momentic": {
          "serverUrl": "http://localhost:58888/api/mcp"
        }
      }
    }
    ```

    Make sure you have started the Momentic app before connecting. If tools don't appear, restart both the IDE and the Momentic desktop server.
  </Tab>

  <Tab title="VS Code (GitHub Copilot)">
    Use the command palette flow and select the URL transport. Enter
    `http://localhost:58888/api/mcp` when prompted.
  </Tab>
</Tabs>


# Modules
Source: https://momentic.ai/docs/modules



<Warning>
  Editing a module will update all tests that use it. This allows you to
  maintain a single source of truth for your test logic, making it easier to
  manage and update.
</Warning>

Modules are reusable steps that can be shared across multiple tests. This is
particularly useful for complex workflows or when you need to perform the same
actions in different tests.

## Parameters

Parameters allow you to pass different values to the module when you use it in a
test. This way, you can use the same module with different inputs without
duplicating steps.

Parameter keys are strings and parameter values are any valid JavaScript value,
including strings, numbers, booleans, and objects.

<Frame>
  <img />
</Frame>

## Caching

By default, modules are not cached, meaning they will always execute. However,
you can enable caching to speed up test execution by skipping steps that have
already been completed.

The return value of the module will be cached, allowing you to use it in
subsequent steps. The return value of a module is the return value of the last
step.

Make sure to configure the cache key and expiry.

<Frame>
  <img />
</Frame>

### Authentication

<Info>
  Make sure the authenticated session expiry time is longer than the cache
  expiry time. If the session expires, the module will need to be re-executed.
</Info>

<Info>
  Make sure the last step of the module is validating the authentication state
  (e.g. by checking if the user is logged in or if a specific element is
  present). This ensures that the module is only cached when the authentication
  state is valid.
</Info>

If your module is performing authentication logic, you can enable the **Treat as
auth module** option. This will automatically save and restore the
authentication state between test runs, allowing you to reuse the same
authentication session without having to log in again.

Values stored:

* [Cookies](https://playwright.dev/docs/api/class-browsercontext#browser-context-cookies)
* `localStorage`
* [IndexedDB](https://developer.mozilla.org/en-US/docs/Web/API/IndexedDB_API)


# Performance
Source: https://momentic.ai/docs/performance

Momentic's performance characteristics and benchmarks

## Execution speed

The runtime of a Momentic test largely depends on how it is crafted and the
state of the system under test.

A Momentic test that only attempts to achieve feature parity with a traditional
testing tool such as Playwright or Cypress will run at approximately the same
speed. Due to [intelligent caching](/step-cache), over 99% of steps that run on
the Momentic platform execute in under 500ms:

| Preset action                      | Average runtime |
| ---------------------------------- | --------------- |
| Click                              | 250ms           |
| Type                               | 340ms           |
| Choosing from a `<select>` element | 275ms           |
| Pressing a key                     | \<5ms           |
| Scroll                             | \<5ms           |
| Page check attempt                 | 220ms           |
| Element check attempt              | 210ms           |
| Visual diff                        | 620ms           |

However, any enhanced steps that require AI completions can incur greater
runtime costs. These steps provide outsized value, power, and flexibility to
developers at the cost of duration. The approximate **first-time** execution
speed of each AI-enhanced action supported by Momentic is listed below. In many
cases, Momentic [caches](/step-cache) AI results to reduce subsequent runtime.

| AI-enhanced action                          | First-time runtime range |
| ------------------------------------------- | ------------------------ |
| Locating an element                         | 4-8 seconds              |
| Evaluating an assertion once                | 5-8 seconds              |
| Extracting data from the page               | 5-8 seconds              |
| Generating a single command in an AI action | 6-12 seconds             |
| Classifying a test failure                  | 20-30 seconds            |
| Auto-healing a section                      | 30+ seconds              |

## Benchmarks

### Overview

We have published a basic benchmark comparing Momentic against Playwright in
this publicly accessible test automation
[environment](https://practicetestautomation.com/practice-test-login/).

The results illustrate that cached Momentic steps are **only 52ms slower** on
average than comparable Playwright functions. Non-cached steps that require AI
to execute run on average **6354ms** slower. Over 99% of all steps executed on
the Momentic platform are cached.

Note that this benchmark does not exhaustively test all Momentic step types,
many of which do not have analogs in Playwright, Cypress, or any traditional
tooling (e.g. [AI check](/steps/ai-check), [Visual diff](/steps/visual-diff)).

### Method

We built a Momentic test that logs into the practice automation site, as well as
an equivalent Playwright script that performs the same sequence of actions. We
obtained three different sets of measurements:

* The "Steps only" category only measures the time spent executing steps in both
  software.
* The "End-to-end" category includes Momentic's fixed bootstrap (e.g. API key
  check) and test result upload times. For Playwright, the end-to-end time
  includes CLI initialization time but does not involve any upload of data.
* The "First-run" category ran with caching explicitly disabled and thus
  includes the runtime of 4 fresh AI completions.

All measurements were completed on a M3 Max Macbook Pro with 36GB RAM running
Mac OS Sonoma.

### Results

All values are P50 milliseconds measured over 10 independent samples.

|                      | Playwright | Momentic |
| -------------------- | ---------- | -------- |
| Steps only           | 961ms      | 1173ms   |
| End-to-end           | 1870ms     | 3998ms   |
| First-run steps only | N/A        | 26379ms  |

The source used for this benchmark is provided below:

<CodeGroup>
  ```yaml benchmark.test.yaml theme={null}
  fileType: momentic/test
  id: 48f763e2-3ace-4ac8-ba7d-36f3bf0496a2
  name: Log in practice test automation
  baseUrl: https://practicetestautomation.com/practice-test-login/
  schemaVersion: 1.0.13
  advanced:
    disableAICaching: false
  retries: 1
  envs: []
  steps:
    - id: c0f25128-3dfe-4b79-9353-5d11eca5a15b
      type: PRESET_ACTION
      command:
        id: 72e7f915-1262-4558-9d60-4a7805fb00c7
        useSelector: false
        useXY: false
        force: false
        disableCache: false
        clearContent: true
        pressEnter: false
        type: TYPE
        target:
          type: description
          elementDescriptor: the username input
        value: student
    - id: 
      type: PRESET_ACTION
      command:
        id: 243fc113-511f-4f25-bdea-c68af30bd077
        useSelector: false
        useXY: false
        force: false
        disableCache: false
        clearContent: true
        pressEnter: false
        type: TYPE
        target:
          type: description
          elementDescriptor: the password input
        value: Password123
    - id: b46c7d74-b549-4921-9b94-d3a48c4d24ff
      type: PRESET_ACTION
      command:
        id: 52153871-0237-4847-8b33-86a7bf709246
        useSelector: false
        useXY: false
        force: false
        disableCache: false
        type: CLICK
        target:
          type: description
          elementDescriptor: the submit button
        doubleClick: false
        rightClick: false
    - id: 4f2d060e-716e-4b26-b821-6d1d170fbccb
      type: PRESET_ACTION
      command:
        id: 21003652-329b-4f13-8891-21a31cd40aa6
        type: PAGE_CHECK
        assertion:
          type: CONTENT
          value: Logged In
  ```

  ```javascript benchmark.spec.js theme={null}
  import { chromium } from "playwright";

  async function main() {
    console.log("starting steps", Date.now());
    const browser = await chromium.launch({
      headless: true,
    });
    const context = await browser.newContext();
    const page = await context.newPage();
    await page.goto("https://practicetestautomation.com/practice-test-login/");
    await page.locator("#username").fill("student");
    await page.locator("#password").fill("Password123");
    await page.locator("#submit").click();
    await page.getByText("Logged In Successfully").waitFor({ state: "visible" });
    console.log("done", Date.now());
    process.exit(0);
  }

  void main();
  ```
</CodeGroup>


# Finding elements
Source: https://momentic.ai/docs/prompting/finding-elements

Guide to targeting elements reliably with Momentic's AI

Momentic's AI is trained to understand HTML, the accessibility tree, and
screenshots. Use a combination of these three modalities to describe the
elements you want to interact with.

## Accessibility attributes

<Tip>
  Leveraging accessibility attributes such as `aria-roles`, `aria-labels`, and
  alt text is an existing [best practice](https://playwright.dev/docs/locators)
  in testing. If your app is not accessible, we recommend adding these
  attributes to improve UX and comply with [ADA
  standards](https://www.uschamber.com/co/run/technology/ada-website-accessibility-compliance).
</Tip>

The accessibility tree is how screen readers and other assistive technologies
navigate web pages. As such, the best descriptions reference elements using
their accessibility attributes.

We recommend mentioning the desired element's
[accessibility role](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA/Roles)
in the description, such as "the submit **button**", "the homepage **link**",
"the password **input**", "the 'People' **tab**", or "the **combobox** for
selecting a month".

If you are unsure what attributes to use, you can use
[Chrome Dev Tools](https://developer.chrome.com/blog/full-accessibility-tree#full_accessibility_tree_in_devtools)
to find out.

<Frame>
  <img />
</Frame>

## HTML content and attributes

If the desired element contains text content, you can also include a subset or
summary of the text in your description. For example, the "the **'Welcome'**
header" or "the text area containing **'Lorem Ipsum'**".

Momentic's AI also looks at certain high-signal HTML attributes. Values that are
flagged as auto-generated, sensitive, or lengthy are ignored.

<Accordion title="Included HTML attributes">
  ```
  id
  value
  type
  class
  height
  width
  target
  title
  href
  src
  alt
  role
  headers
  scope
  checked
  required
  action

  min
  max
  minlength
  maxlength
  multiple
  pattern
  placeholder
  accept
  contenteditable

  data-value
  data-testid
  data-cy
  data-test-id
  data-test
  data-role
  data-type
  data-key
  data-action
  data-hidden

  data-handleid
  data-handlepos

  data-col-index
  data-row-index
  data-row
  data-col
  ```
</Accordion>

## Typos

Momentic's agents are tuned for helpfulness and will tolerate minor spelling,
casing, and punctuation mismatches. For example, our agent will allow you to a
describe an element like `<button>Sign in</button>` as "the logging in button",
"the sign on button", or even "the signin button".

If you would like to ensure an exact match, you can wrap the desired content in
single quotes and explicitly prompt the agent to disallow any differences in the
element description. For example, "the 'Sign in' button. don't allow any typos".
Alternatively, you can use an [Element Check step](/steps/element-check) to
deterministically validate requirements for the element.

If single quotes are not provided, Momentic's AI will try to use the context
available on the page, as well as past executions, to infer the correct element.

## Visual information

<Warning>
  Momentic's AI can access HTML and a11y tree for the **entire page**, not just
  the current visible viewport. However, it can only access visual information
  from the current visible viewport as it relies on a screenshot of the page.
</Warning>

Momentic's AI is trained to understand visual information like colors, shapes,
sizes, and positions. For example, you can say "the **red** 'Cancel' button",
"the **thumbs up** icon", or "the **hamburger menu** beside the logo".

Due to image quality constraints, we recommend against relying on visual
information alone to identify elements smaller than 12x12 pixels. Vision-based
descriptions are also less reliable when the element is embedded among many
visually similar elements (e.g. a toolbar full of small icons).

## Positional cues

Wen there are multiple instances of the same element (e.g. a data table or
list), you will need to disambiguate which instance you want to interact with.

### Absolute locations

You can provide absolute cues such as "...**at the top** of the page" or
"...**in the bottom right corner**".

### Relative locations

You can provide relative cues such as "...**below** the 'Introduction' header"
or "...**beside** the 'Back' button".

Use the **inside** keyword to specify the parent element of another element. For
example, "the 'Submit' button **inside** the user dialog".

Use the **closest** keyword to specify the closest element to another element.
For example, "the **closest** 'Submit' button to the 'Username' input".

### Ordering

<Warning>
  Since the order of elements on the page can change, make sure to turn off
  [caching](/step-cache). This will ensure Momentic's AI will always target the
  correct element
</Warning>

Use the **nth** keyword to specify the position of an element in a list. For
example, "the **second** 'Submit' button".

## Dynamic elements

<Warning>
  Since the target element will change every time, make sure to turn off
  [caching](/step-cache). This will ensure Momentic's AI will always target the
  correct element
</Warning>

You can target random and dynamic elements with natural language descriptions.
For example, "a **random** card" or "**today's** date in the calendar"

## Examples

<Frame>
  <img />
</Frame>

Putting it all together, here are some examples of how to describe the labelled
elements in the screenshot above:

1. "the avatar picture on the top left corner"
2. "the home link in the sidebar"
3. "the 'Amount' filter menu"
4. "the notification bell icon to the right of the green button"
5. "the third outgoing transaction card in the list"

## Troubleshooting

* **Dynamic elements**: If you use **nth** or dynamic elements in a description,
  make sure to turn off [caching](/step-cache). This will ensure Momentic's AI
  will always target the correct element.
* **Hidden elements**: Momentic's AI will ignore elements that are explicitly
  marked as `aria-hidden` (or are part of sub-trees that are hidden), not
  attached to the DOM, or have no bounding box.
* **Multiple matches**: If Momentic's AI finds multiple elements that match your
  description, it will select the first one in the DOM order. If you want to
  target a specific instance, use positional cues like **nth**, **closest**, or
  **inside**.


# Writing assertions
Source: https://momentic.ai/docs/prompting/writing-assertions

Guide to asserting on complex application state with Momentic's AI

Momentic's AI is trained to understand HTML, the accessibility tree, and
screenshots. Use a combination of these three modalities to verify assertions.
Read more [here](/prompting/writing-assertions).

## Best practices

* **Keep assertions short and specific**. Break down complex assertions into
  smaller, manageable parts. This helps the AI understand your intentions. We
  recommend using no more than 20 words.
* **Provide useful context**. To avoid misinterpretations, include information
  such as a specific part of the page the AI should focus on or the element you
  are looking for. Explain any non-standard terminology.
* **Avoid ambiguity and subjectivity**: Minimize "grey area" when formulating
  your assertion - the answer to your assertion should be clearly true or false
  given the page state. If your assertion is highly nuanced, explicitly state
  the criteria you want the AI to use. For example, you can say "the textbox
  contains the exact value 'heading1'" rather than "textbox has heading".

## Examples

Here are some good examples of how to write assertions using
[AI check](/steps/ai-check):

| Category                          | Example                                                      |
| --------------------------------- | ------------------------------------------------------------ |
| Presence (or absence) of text     | A congratulations message is shown in the modal              |
| Presence (or absence) of elements | The page shows 3 search results                              |
| Logical statements                | The publish date of this article is more than 30 days ago    |
| Page state                        | There is no error message present on the page                |
| Color                             | The buy button is blue                                       |
| Layout                            | The 'XL' button is the largest button in the submission form |
| Images & video                    | There is a LinkedIn icon on the page                         |

Here are some poorly crafted assertions that are likely to be flaky,
misunderstood, or incorrect:

| Category                               | Bad example                                                                              | Alternative                                                                  |
| -------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| Malformed assertion                    | Search results                                                                           | There are search results displayed on the main body                          |
| Ambiguous assertion                    | The order of the results is correct                                                      | The search results are sorted by date                                        |
| Multiple focuses in a single assertion | The logo is blue, the page shows 4 results, and the last result is more than 30 days old | Split into 3 separate assertions                                             |
| Assertion contains an action           | Wait for the results to appear                                                           | Use a wait step if necessary, and then assert that the results have appeared |
| Assertion about imperceivable details  | The color of line divider is #ff5733                                                     | The color of the divider looks red                                           |
| Subjective assertion                   | The page looks well designed                                                             | No text in the table overflows its cell                                      |
| Assertion depends on changes over time | The video plays a 10-second advertisement for an insurance product                       | N/A                                                                          |

## Pre-trained behavior

The assertion agent is pre-trained to follow specific thought patterns to ensure
AI safety, testing consistency, and ease of interaction. Momentic has carefully
tuned the following behaviors.

### Typos

The agent is trained to tolerate and auto-heal minor typos. For example, if you
write "the username is `john@@gmail.com`" but the actual username is
`john@gmail.com`, the AI will pass the assertion since the test author likely
typed an extra `@`.

If your test genuinely relies such on a small difference, explicitly instruct
the agent to *not* to allow any changes and place the desired text in single
quotes. For example, "the username is exactly 'john@@gmail.com'. do not allow
any typos or casing differences".

If you are auto-generating test data, we recommend creating long, distinct
values using JavaScript functions like `crypto.randomUUID()` or
`faker.word.words(3)` so that assertions are unambiguous. Singular words like
`faker.animal.type()` are especially prone to collision.

### Visual criteria

Visual criteria is always verified using the screenshot. The assertion agent is
not allowed to infer the visual state using HTML attributes or CSS properties.
If a described element is not visible in the screenshot (e.g. because it is
hidden, covered, or out of the current viewport), the assertion will be
evaluated as false. Examples of visual criteria include color, size, position,
and shape.

### Vacuously true statements are disallowed

Momentic's agent will fail any assertion that is vacuously true. For example,
suppose the test asserts that the "submit button is not blue" but there is no
submit button on the page at all. Even though this statement is technically
true, the original test author likely intended a button to be present and so
Momentic errs on the side of caution and fails the assertion in this case.

The same line of reasoning applies to dependent elements. For example, if a test
asserts that "the X icon in the modal is active" but there is no modal present
at all, the assertion will be evaluated as false.

### Counts are evaluated exactly

If the assertion states that a certain number of objects are present, the agent
will evaluate the assertion as false if the actual number of objects does not
exactly match the expected number. This includes the case where the actual count
is greater than the expected count.

For example, if the assertion states that "the page shows 3 search results",
Momentic will fail the assertion if there are zero, two, or four search results
on the page.

#### Limited real-world knowledge

Our agent does not have access to up-to-date real-world knowledge such as the
news or the current date. In addition, the agent is also trained to focus on the
current page state. You can pass the agent dynamic context using `{{}}`
[expressions](/javascript#expressions), but we recommend using a
[JavaScript](/steps/javascript) step to evaluate assertions that do not depend
on the page state (e.g. mathematical calculations).

## Data visualizations

You can also assert on SVG or canvas-based data visualizations rendered by
libraries such as [D3](https://d3js.org/),
[Hicharts](https://www.highcharts.com/), [Recharts](https://recharts.org/en-US),
and more.

To improve accuracy, use the following guidelines:

* Maximize or expand your graph so that it takes up a majority of the screen. If
  your charting library does not have this functionality, you can try setting
  `document.body.style.zoom` manually using [JavaScript](/javascript).
* Provide clear labels and units for all axes. Include grid lines when possible.
* For interactive visualizations, use [Click](/steps/click) or
  [Hover](/steps/hover) steps to show tooltips and labels before making
  assertions.

## Troubleshooting

* **Assertions with actions**: The assertion agent cannot execute actions (e.g.,
  "expand the dropdown", "wait for the page to load") and will not be able to
  understand such queries. Instead, split the action and assertion into separate
  steps.
* **Assertions over time**: The AI does not support assertions that evaluate
  changes over time (e.g., "after 5 seconds, a popup appears", "the table has
  shifted upwards"). Instead, use a [Wait](/steps/wait) step to pause the test
  and then check for the expected post-condition.
* **Assertions on small visual details**: Due to resolution downscaling
  performed by AI providers, the AI may not be able to perceive small visual
  details such as exact hex codes, colors of indicator dots, colors of thin font
  faces, and shapes of SVGs smaller than 12px. We recommend keeping assertions
  general enough to avoid these edge cases.
* **Complex math**: The AI may struggle with complex mathematical calculations
  (e.g., "the average slope of the graph is 31.4"). Instead, simplify the
  assertion to a more straightforward comparison (e.g., "the graph shows an
  upward trend").
* **Complex conditionals**: The AI may not handle complex conditional logic well
  (e.g., "if the user is logged in, check that their profile photo is visible;
  otherwise, check that there is a Google icon on the page"). Instead, break it
  down into simpler assertions that do not rely on conditional logic.


# Quarantine
Source: https://momentic.ai/docs/quarantine



If a test or feature is flaky or unstable, you can quarantine it to prevent it
from failing pipelines. This allows pipelines to continue running without being
affected.

Once a test is quarantined, it will be skipped in all environments, and across
all branches, until it is unquarantined.

## How to quarantine a test

### CLI

You can quarantine and unquarantine tests using the
[quarantine](/cli/commands/quarantine) command in the Momentic CLI.

<CodeGroup>
  ```bash npm theme={null}
  npx momentic quarantine add <test> --reason <reason>
  ```

  ```bash yarn theme={null}
  yarn dlx momentic quarantine add <test> --reason <reason>
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic quarantine add <test> --reason <reason>
  ```
</CodeGroup>

### Cloud

Select **Quarantine** on the left sidebar, and click the **Quarantine test**
button in the top right corner.

<Frame>
  <img />
</Frame>

To unquarantine a test, navigate to the same page, hover over the test to
unquarantine, and select the **Unquarantine** option in the dropdown menu.

<Frame>
  <img />
</Frame>

You can also quarantine a test directly from the run viewer, by clicking on the
**Quarantine test** button in the top right corner of the page.

<Frame>
  <img />
</Frame>

## Quarantine rules

Quarantine rules are a way to define thresholds past which tests are
automatically quarantined or unquarantined. This allows you to easily keep your
test suite running smoothly without taking manual action.

<Frame>
  <img />
</Frame>

### Rule

The rule defines both the action to be taken, as well as when to take it. You
can configure:

* Whether to quarantine or unquarantine the test.
* Which metric to use (options include pass rate, number of failures, and flake
  rate).
* What threshold triggers the action.
* What period to evaluate the metric over.

<Frame>
  <img />
</Frame>

### Filtering

In order to create more granular rules, you can configure additional filters so
that the rule only applies to certain tests and runs:

* Only apply to tests in a specific repository.
* Only include runs on a particular branch. This is useful for quarantining
  tests that fail too often on main.
* Only include tests with particular labels. This is useful if you have stricter
  rules for particular suites.

<Frame>
  <img />
</Frame>


# CLI
Source: https://momentic.ai/docs/quickstart/cli

This quickstart guide will walk you building your first test locally and integrating into CI/CD

<Info>
  **Prerequisite**: Please install [Node.js](https://nodejs.org/en) (version
  20.19.0 or higher) before proceeding.
</Info>

Before you begin, you must already have a `package.json` file. If you don’t,
make sure to run `npm init` or `yarn init` to create the file beforehand.

## Get your API key

To get started, log in to
[Momentic Cloud](https://app.momentic.ai/settings/api-keys) and generate an API
key.

<Frame>
  <img />
</Frame>

You can export the API key in your shell configuration file (usually `.bashrc`
or `.zshrc`) like so:

```bash theme={null}
export MOMENTIC_API_KEY=your-api-key
```

## Install the Momentic CLI

Install the CLI, [momentic](https://www.npmjs.com/package/momentic), by running
the following command in your terminal:

<CodeGroup>
  ```bash npm theme={null}
  npm install momentic --save-dev
  ```

  ```bash yarn theme={null}
  yarn add momentic --dev --ignore-workspace-root-check
  ```

  ```bash pnpm theme={null}
  pnpm add momentic --save-dev --ignore-workspace-root-check
  ```
</CodeGroup>

## Install browsers

Momentic relies on [headless browsers](/browsers) that must be installed. To
install all available browsers:

<CodeGroup>
  ```bash npm theme={null}
  npx momentic install-browsers --all
  ```

  ```bash yarn theme={null}
  yarn dlx momentic install-browsers --all
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic install-browsers --all
  ```
</CodeGroup>

## Initialize a new project

To create a new Momentic project, run the following command in your terminal:

<CodeGroup>
  ```bash npm theme={null}
  npx momentic init
  ```

  ```bash yarn theme={null}
  yarn dlx momentic init
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic init
  ```
</CodeGroup>

## Start the Momentic Local App

Start the Local App by running the following command in your terminal:

<CodeGroup>
  ```bash npm theme={null}
  npx momentic app
  ```

  ```bash yarn theme={null}
  yarn dlx momentic app
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic app
  ```
</CodeGroup>

It will open a new browser window with the Momentic Local App, where you can
manage your tests, view results, and more.

<Frame>
  <img />
</Frame>

## Create a test

Click on the **Create test** button in the top-right corner.

<Frame>
  <img />
</Frame>

Enter these details:

* **Name**: `example-test`
* **Base URL**: `https://practicetestautomation.com/practice-test-login/` (a
  demo site for testing)

This will open the Momentic Editor, where you can add instructions in natural
language. Click **Run from start** to execute the test live.

<Frame>
  <img />
</Frame>

This will create a new file in your project directory called
`example-test.test.yaml`. Changes are saved automatically, so you don't need to
worry about losing your work.

## Run the test

You can run the test you just created by running the following command in your
terminal:

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run example-test
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run example-test
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run example-test
  ```
</CodeGroup>

## Next steps

Congratulations! You have successfully built and ran your first test with
Momentic. Here are suggested next steps:

<Card title="Set up GitHub Actions" icon="github" href="/ci/github-actions">
  Integrate Momentic tests into your GitHub Actions workflows
</Card>

<Card title="Variables" icon="square-root-variable" href="/variables">
  Learn how to use variables to make your tests more dynamic and reusable
</Card>


# Cloud
Source: https://momentic.ai/docs/quickstart/cloud

This quickstart guide will walk you through building and running your first test on Momentic Cloud

## Log in

1. [Log in](https://app.momentic.ai) to your account
2. Select **Repository** on the left sidebar

<Frame>
  <img />
</Frame>

## Create a test

Click on the **Create test** button in the top-right corner.

<Frame>
  <img />
</Frame>

Enter these details:

* **Name**: `example-test`
* **Base URL**: `https://practicetestautomation.com/practice-test-login/` (a
  demo site for testing)

This will open the Momentic Editor, where you can add instructions in natural
language. Click **Run from start** to execute the test live.

<Frame>
  <img />
</Frame>

Changes are saved automatically, so you don't need to worry about losing your
work.

## Run the test

You can run any tests you create by clicking on the **Run** button in the panel.

<Frame>
  <img />
</Frame>

You can also schedule tests to run automatically at specific times or intervals
using a [cron expression](https://crontab.guru/). To do this, click on the
**Schedule test** button in the panel and input the desired schedule.

## Next steps

Congratulations! You have successfully built and ran your first test with
Momentic. Here are suggested next steps:

<Card title="CLI" icon="terminal" href="/quickstart/cli">
  Install the Momentic CLI to build and run tests locally
</Card>

<Card title="Variables" icon="square-root-variable" href="/variables">
  Learn how to use variables to make your tests more dynamic and reusable
</Card>


# Request mocking
Source: https://momentic.ai/docs/request-mocking



Mocking network requests can be useful for a variety of use-cases, such as
testing your frontend without running a backend, overwriting feature flag
configurations, or testing error states.

## Mocking a route

In this example, we'll capture requests to our `/todos` endpoint, and return
fake data instead of hitting the production API server.

First, we'll create a new [mock route](./steps/mock-route) step, and set the URL
matcher to a regex that will capture requests to `GET /todos`.

<Frame>
  <img />
</Frame>

Then, we define a response generator to create fake data.

```javascript theme={null}
const url = new URL(mock.request.url)

const fakeTodo = {
    id: url.searchParams.get("id"),
    name: "My todo item",
    done: false,
    description: "An item that I need to do",
}

return new Response(
    JSON.stringify([fakeTodo]),
    {
        status: 200,
        headers: {
            "content-type": "application/json"
        }
    }
)
```

## Modifying the original response from the server

Sometimes, it's easier to simply modify the original response from the server,
for example, in order to set a specific feature flag.

In order complete the initial request and pass the response to the mock
generator, you must first enable the "fetch real response" option. This will
allow us to access the response at `mock.response` inside our JavaScript code.

<Frame>
  <img />
</Frame>

Now we can configure our mock to intercept feature flag requests.

<Frame>
  <img />
</Frame>

And define a response to overwrite one of the values.

```javascript theme={null}
const originalJson = await mock.response.json()

return new Response(
  JSON.stringify({
    ...originalJson,
    flags: {
        ...originalJson.flags,
        momentic_test: true,
    }
  }),
  {
    status: mock.response.status,
    headers: mock.response.headers
  }
)
```

## Removing a mock

There are two ways to reference a mock in later steps:

1. By configuring a key in the [mock route](./steps/mock-route) step.
2. If no key is provided, a random one will be generated. You can still
   reference it later by saving the output of the step to an environment
   variable. The output of the [mock route](./steps/mock-route) step will have a
   `key` field containing the random string.

You can use a [remove route mock](./steps/remove-mock-route) step to remove a
mock by key, or remove all mocks if you omit the key.

## Updating a mock

You can update a mock by registering a different handler with the same key using
another [mock route](./steps/mock-route) step. Registering a mock with the same
URL matcher but a different key is not sufficient to replace the existing mock.

## Debugging mocked routes

Because network requests are handled asynchronously in a separate process, it
can be hard to investigate when something goes wrong.

If a response generator throws an error while handling a request, Momentic will
still respond to the request with a 500 server error status code, and the error
message in the body of the response. This makes it easy to figure out what's
going on either in your app's UI, or using the network logs.

<Frame>
  <img />
</Frame>


# Privacy & security
Source: https://momentic.ai/docs/security

Guide to Momentic's data handling and security practices

Momentic is SOC 2 Type 2 certified. We have built Momentic from the ground up to
give you the peace of mind that your data is private and secure.

## Quick links

<Card title="Privacy Policy" icon="user-shield" href="https://momentic.ai/legal/privacy">
  Read our comprehensive privacy policy to understand how we handle your data
</Card>

<Card title="Trust Center" icon="shield" href="https://app.vanta.com/momentic/trust/cf4grito2o2n5arv16n1bz">
  View our Trust Center to learn more about our security practices and to access
  our SOC2 certification. security reports and annual penetration testing
  reports.
</Card>

## Sub-processors

We work with companies and tools to store, analyze, and transmit data on behalf
of our users. These companies have been vetted for best-in-class security
practices.

| Sub-processor         | Purpose            |
| --------------------- | ------------------ |
| PostHog               | Product analytics  |
| DataDog               | Analytics          |
| Google Cloud Platform | Cloud hosting      |
| Superhuman            | Email              |
| Pylon                 | Support            |
| Slack                 | Internal processes |
| Notion                | Internal processes |
| Google Workspace      | Internal processes |
| GitHub                | Source code        |
| Linear                | Issue tracking     |
| Sentry                | Error monitoring   |
| Stripe                | Billing            |
| Orb                   | Billing            |
| Anthropic             | AI                 |
| OpenAI                | AI                 |
| Microsoft Azure       | AI                 |
| WorkOS                | Authentication     |


# SMS
Source: https://momentic.ai/docs/sms



<Info>**Prerequisites**: A SMS number must be provisioned by Momentic.</Info>

SMS functionality is surfaced through the [JavaScript](/steps/javascript) step.
Within Momentic's JavaScript sandbox, your code can access the `sms` object.
This object contains the following utility functions:

### Sending SMS

The `send` utility function allows you to send an SMS message to a phone number.
The phone number provided in the `from` argument must be issued by Momentic.

<Tabs>
  <Tab title="Function signature">
    ```ts theme={null}
    async function send(params: {
      body: string;
      to: string;
      from: string;
    }): Promise<void>;
    ```
  </Tab>

  <Tab title="Example">
    ```ts theme={null}
    await sms.send({
      body: "Hello world!",
      to: "+14151234567",
      from: "+14159876543"
    });
    ```
  </Tab>
</Tabs>

### Fetching the latest SMS message

<Info>
  Make sure the function timeout is shorter than the JavaScript lambda timeout.
  The default timeout for both is 10 seconds.
</Info>

The `fetchLatest` utility function retrieves the most recent SMS message sent to
your phone number. You can filter messages based on the sender as well as the
receipt date. This function will automatically retry until a matching message is
found or the timeout is exhausted.

If multiple new SMS messages are received, only the most recently received
message will be returned. To avoid race conditions, we recommend structuring
your tests so that only a single SMS flow is active at any given time for each
phone number allocated.

If you do not filter by receipt date, `fetchLatest` can return messages that
were received before your test started (i.e. data generated from previous test
runs).

`fetchLatest` will throw an error if no matching SMS message is received within
the timeout.

<Tabs>
  <Tab title="Function signature">
    ```ts theme={null}
    async function fetchLatest(params: {
      to: string;
      from?: string;
      beforeDate?: Date;
      afterDate?: Date;
      timeout?: number; // milliseconds
    }): Promise<{ body: string }>;
    ```
  </Tab>

  <Tab title="Example">
    ```ts theme={null}
    const { body } = await sms.fetchLatest({
      to: "+14151234567",
      from: "+14159876543"
      afterDate: new Date(), // only fetch messages received after this call starts
      timeout: 30000, // 30 seconds
    });
    // use regex to extract link from message body
    const link = body.match(/https?:\/\/[^\s]+/)[0];
    return link;
    ```
  </Tab>
</Tabs>


# Step caching
Source: https://momentic.ai/docs/step-cache

How Momentic uses caching to improve test performance

This page describes the behavior of step caches. For more information about
module caching or persisting auth state, see
[the module docs](/modules#caching).

Momentic improves test performance by caching element data. Most steps run in
milliseconds by avoiding repeated AI lookups, while still maintaining accuracy.

## How caching works

Caching is automatically applied to most interactive steps such as
[Click](/steps/click) and [Type](/steps/type). When these steps are executed,
Momentic stores contextual information about the targeted element, including:

* CSS selectors and HTML attributes.
* Accessibility roles and metadata.
* Screenshots and visual cues.
* Element location and dimensions.

This allows Momentic to reuse known element data across test runs instead of
re-identifying it every time.

Momentic will bust the existing cache if the target element changes
significantly or if the templated description is different than what was cached.

Caches are only ever saved on successful test runs. Additionally, the test run
must be **eligible** for cache saving (see below).

## Cache saving eligibility

<Info>A test run is always eligible if the `--save-cache` flag is passed.</Info>

* If the test is running in a CI environment, the test is eligible for cache
  saving. This is defined by the environment variable `CI` being set to `true`.
* If the test is not running in a CI environment, caches are saved when running
  on a branch **not configured** as a main branch or protected branch. These
  branches are specified in the
  [project configuration](/cli/configuration#gitmainbranch).

## Where caching is never applied

* Steps like [AI check](/steps/ai-check) or [AI extract](/steps/ai-extract)
  which rely on dynamic evaluation.
* Steps with variables that have continuously changing values (e.g.
  `CLICK the {{ Date.now() }} timer`).

## Disabling cache

<Warning>
  Disabling cache may drastically increase test duration and non-determinism.
</Warning>

You can disable caching globally by passing the `--disable-cache` flag when
running tests:

<CodeGroup>
  ```bash npm theme={null}
  npx momentic run --disable-cache
  ```

  ```bash yarn theme={null}
  yarn dlx momentic run --disable-cache
  ```

  ```bash pnpm theme={null}
  pnpm dlx momentic run --disable-cache
  ```
</CodeGroup>

You can disable caching on a per-step basis in the step options. This is useful
when the target element is dynamic and changes between test runs (e.g., "last
item in list")

## How cache keys are generated

Cache keys are based on:

* The step's unique ID.
* IDs of any parent modules.
* The resolved element description.
* Dynamic template values (e.g., `{{ env.USERNAME }}`).

If any of these inputs change, the cache is invalidated and regenerated.

## Storage and expiration

Cache is:

* Securely stored on Momentic Cloud.
* Isolated per organization and only accessible during authenticated test runs.
* Automatically expired after 90 days of inactivity.

## Failed steps and caching

Cache is only created when a step **successfully** executes. Failed steps do not
generate or store cache entries.

## Git-based caching

In order to ensure that tests continue to run smoothly while engineers are
making changes concurrently, caches are isolated by git branch when possible:

* For the main branch (configured in `momentic.config.yaml`), caches are stored
  for each commit. This allows new branches to seed their caches from main.
* For non-main branches, only the latest caches are stored.
* When a new branch is created based off of main, its caches will be seeded with
  the latest values before the merge base commit.
* When a feature branch is merged into the main branch, the caches from the
  merged branch and the previous commit on main are combined it order to ensure
  consistency with both previous runs on the main branch as well as checks that
  passed in that branch's CI.


# AI action (beta)
Source: https://momentic.ai/docs/steps/ai-action

Use AI to generate steps

<Warning>
  AI action is in beta and subject to be deprecated in the future.
</Warning>

<Info>AI action is currently limited to a maximum of 15 steps.</Info>

AI actions are special steps that expand into a series of sub-steps based on a
goal you provide. The sub-steps are automatically generated by our AI agent.

AI actions are useful for the following use cases:

* Completing forms, including login pages and submissions
* Measuring the accessibility and ease-of-use of your site

AI actions should **not** be used to execute single interactions on your page -
please use our other steps like [Click](/steps/click) or [Type](/steps/type)
instead, which are far simpler and execute more deterministically.

## Inputs

<ResponseField name="Goal" type="string">
  High-level goal that you want the AI to achieve. The prompt should include any
  variables required to complete the task, such as credentials ("login using
  mypassword"), descriptors ("add a 128GB iPad to my cart"), and option choices
  ("decline all add-ons and checkout").
</ResponseField>


# AI check
Source: https://momentic.ai/docs/steps/ai-check

Use AI to check if a condition is true

AI checks are assertions on steroids. You can specify a condition in natural
language that can be as specific as "the button on the top left corner of the
page is blue" or as broad as "there is no error page".

## Inputs

<ResponseField name="Assertion" type="string">
  The condition you want to assert. The assertion should be written in plain
  English and can be as specific or as broad as you like.
</ResponseField>

## Configs

<ResponseField name="AI context mode" type="string">
  Choose between a general-purpose AI model that can understand both HTML &
  screenshots, or an advanced vision-only model optimized for visual attributes.
</ResponseField>

<ResponseField name="Timeout" type="number">
  The maximum number of seconds to wait for the assertion to be true. If it
  becomes true at any point during that window, the step passes. The step may
  continue running for a bit longer due to the latency of the final check, which
  starts when the timeout is reached. If unset, defaults to the smart waiting
  timeout, which is usually 5s.
</ResponseField>


# AI extract
Source: https://momentic.ai/docs/steps/ai-extract

Use AI to get data from the page

The AI extract step allows you to pull textual information from the page in a
structured format. You can then reference that information in later steps using
variables.

If you would like our AI to interpret the page results instead of simply
returning data that already exists on the page, you should explicitly instruct
the AI to do so by using the keywords "interpret and then \[…]" or "analyze"

## Inputs

<ResponseField name="Description" type="string">
  A description of the data you'd like to extract. You should try to include a
  location or section of the page that the data should be extracted from. For
  example, "the pricing data in dollars from the plans table".
</ResponseField>

<ResponseField name="Schema" type="object">
  An optional JSON schema for the format the data should be returned in. The
  schema should follow the [official JSON schema
  specification](https://json-schema.org/learn/getting-started-step-by-step#introduction-to-json-schema).
</ResponseField>

## Configs

<ResponseField name="Save to environment variable" type="string">
  Store the output of this step into the environment at the given key. This
  configuration only applies for steps that output data.
</ResponseField>


# Await listener
Source: https://momentic.ai/docs/steps/await-listener

Wait for an event listener to resolve

Wait for an event listener to resolve. This is useful when you have registered a
listener for a specific event (like a network request) and want to wait for that
event to complete before proceeding with the next steps. If the listener does
not resolve within the specified timeout, this step will fail.

## Inputs

<ResponseField name="Listener key" type="string">
  The unique key of the listener you want to wait for. This key should match the
  one used in the [register request
  listener](../steps/register-request-listener) step.
</ResponseField>

## Configs

<ResponseField name="Timeout" type="string">
  The maximum time to wait for the listener to resolve, in seconds. If the
  listener does not resolve within this time, the step will fail. Default is 10
  seconds.
</ResponseField>

<ResponseField name="Save to an environment variable" type="string">
  The name of the environment variable where the result of the listener will be
  saved. This is useful if you need to use a [javascript
  step](/steps/javascript) to validate the response.
</ResponseField>


# Click
Source: https://momentic.ai/docs/steps/click

Clicking on an element on the page

## Inputs

<ResponseField name="Description" type="string">
  Description of the element you want to interact with.
</ResponseField>

## Configs

<ResponseField name="Double click" type="boolean">
  Double click on the element.
</ResponseField>

<ResponseField name="Right click" type="boolean">
  Right click on the element.
</ResponseField>

<ResponseField name="Wait for download" type="boolean">
  Wait for the click to initiate a download and for the download to complete. A
  handle to the downloaded file will be returned in the step output. Files
  should not exceed 10MB.
</ResponseField>

<ResponseField name="Download timeout" type="number">
  Number of milliseconds to wait for a download. Defaults to 30000ms if unset.
</ResponseField>

<ResponseField name="Click delay ms" type="number">
  Number of milliseconds between each
  [mousedown](https://developer.mozilla.org/en-US/docs/Web/API/Element/mousedown_event)
  and
  [mouseup](https://developer.mozilla.org/en-US/docs/Web/API/Element/mouseup_event)
  event. Useful for UI handlers that require long presses or only listen to
  mousedown events.
</ResponseField>

<ResponseField name="Relative position" type="boolean">
  Specify where the click should occur relative to the top-left corner of the
  element.
</ResponseField>

<ResponseField name="Disable stability checks" type="boolean">
  Do not wait for the element to be visible, stable and actionable before
  interacting. Useful for elements that are constantly animating or partially
  obscured.
</ResponseField>

<ResponseField name="Use CSS selector" type="boolean">
  Treat the element description as a CSS selector. This is not recommended for
  maintainability reasons but can be useful for dynamic pages.
</ResponseField>

<ResponseField name="Disable caching" type="boolean">
  Disable [caching](/step-cache) for this step. Useful for elements that should
  always be located dynamically, such as table rows, search results, or graph
  nodes that may be re-ordered.
</ResponseField>

<ResponseField name="Act within iframe" type="string">
  Specify an exact URL or a regex to match the URL of the iframe in which the element is located.
  The provided matcher must match exactly one iframe element on the page. To provide a custom regex, use the `/<regex-here>/` format.
</ResponseField>


# Conditional
Source: https://momentic.ai/docs/steps/conditional

Execute an "if statement" and perform steps if true

This step evaluates a condition and runs child steps when it passes. You can
choose an AI Assertion, JavaScript condition, or Page Check. To add child steps,
hover over the Conditional step and in the action bar, click Add Child.

If the condition is false, the Conditional step will be marked as having passed,
skip nested steps, and continue with the test.

## Inputs

<ResponseField name="Conditional type" type="dropdown">
  The type of condition to check.
</ResponseField>

<Tabs>
  <Tab title="AI Assertion">
    <ResponseField name="Assertion" type="string">
      Describe the condition in plain English. The assertion can be as specific
      or as broad as you like.
    </ResponseField>
  </Tab>

  <Tab title="JavaScript">
    <ResponseField name="JavaScript" type="string">
      Write code that returns a truthy or falsy value. Truthy executes the
      block, falsy skips it. Errors fail the Conditional step.
    </ResponseField>
  </Tab>

  <Tab title="Page Check">
    <ResponseField name="Page check" type="string">
      Define the page content assertion. If the check fails, the block is
      skipped and the Conditional step still passes. Errors fail the Conditional
      step.
    </ResponseField>
  </Tab>
</Tabs>

## Configs

<ResponseField name="Disable caching" type="boolean">
  Disable [caching](/step-cache) for this step. Useful for elements that should
  always be located dynamically, such as table rows, search results, or graph
  nodes that may be re-ordered.
</ResponseField>

<ResponseField name="Timeout" type="number">
  Max number of seconds for the action to finish.
</ResponseField>

<ResponseField name="AI context mode" type="string">
  Choose between a general-purpose AI model that can understand both HTML &
  screenshots, or an advanced vision-only model optimized for visual attributes.
</ResponseField>

<SaveToEnv />


# Cookie
Source: https://momentic.ai/docs/steps/cookie

Setting a cookie in the browser

Set a cookie that will persist throughout the browser session.

## Inputs

<ResponseField name="Cookie" type="string">
  Cookie in the
  [Set-Cookie](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Set-Cookie)
  format. Options can be specified through key-value pairs separated by a
  semicolon (e.g. `id=1; domain=google.com; secure`).
</ResponseField>


# Copy
Source: https://momentic.ai/docs/steps/copy

Copy text to the clipboard

Copy the specified value to the clipboard.

## Inputs

<ResponseField name="Value" type="string">
  The text you want to copy to the clipboard.
</ResponseField>


# Drag and drop
Source: https://momentic.ai/docs/steps/drag-and-drop

Drag and drop elements across the page

This step allows you to drag an element from one location to another on the
page.

## Inputs

<ResponseField name="Element to drag" type="string">
  Description of the element where you are initiating drag.
</ResponseField>

<ResponseField name="Drag destination element" type="string">
  Description of the element where you are dropping the dragged element.
</ResponseField>

## Configs

<ResponseField name="Hover duration" type="number">
  Number of seconds to wait before dropping the element. This can be useful for
  ensuring that mouse and hover events are triggered before the drop completes.
</ResponseField>

<ResponseField name="Drag segments" type="number">
  Number of intermediate segments to use when dragging the mouse. Increasing
  this value sends more incremental move events, creating a smoother drag.
  Defaults to 5 segments if unset.
</ResponseField>

<ResponseField name="Disable stability checks" type="boolean">
  Do not wait for the element to be visible, stable and actionable before
  interacting. Useful for elements that are constantly animating or partially
  obscured.
</ResponseField>

<ResponseField name="Use CSS selector" type="boolean">
  Treat the element description as a CSS selector. This is not recommended for
  maintainability reasons but can be useful for dynamic pages.
</ResponseField>

<ResponseField name="Disable caching" type="boolean">
  Disable [caching](/step-cache) for this step. Useful for elements that should
  always be located dynamically, such as table rows, search results, or graph
  nodes that may be re-ordered.
</ResponseField>

<ResponseField name="Act within iframe" type="string">
  Specify an exact URL or a regex to match the URL of the iframe in which the element is located.
  The provided matcher must match exactly one iframe element on the page. To provide a custom regex, use the `/<regex-here>/` format.
</ResponseField>


# Element check
Source: https://momentic.ai/docs/steps/element-check

Assert on a specific element

This step asserts on a specific element's content, attributes, or state.

When a usable cached target exists, `ELEMENT_CHECK` retries with cache-only
resolution during the timeout window. If those retries still fail, it performs
one final AI locate attempt after the timeout window elapses.

Assertion types:

* **Content**: Verify the text content of an element.
* **Attribute**: Verify the value of an attribute on an element.
* **State**:Verify the state of an element, such as whether it is visible or
  enabled.

## Inputs

<ResponseField name="Description" type="string">
  Description of the element you want to assert on.
</ResponseField>

## Configs

<ResponseField name="Timeout" type="number">
  The maximum number of seconds to wait for the check to be true. If it becomes
  true at any point during that window, the step passes. The step may continue
  running for a bit longer due to the latency of the final check, which starts
  when the timeout is reached.
</ResponseField>

<ResponseField name="Disable stability checks" type="boolean">
  Do not wait for the element to be visible, stable and actionable before
  interacting. Useful for elements that are constantly animating or partially
  obscured.
</ResponseField>

<ResponseField name="Use CSS selector" type="boolean">
  Treat the element description as a CSS selector. This is not recommended for
  maintainability reasons but can be useful for dynamic pages.
</ResponseField>

<ResponseField name="Disable caching" type="boolean">
  Disable [caching](/step-cache) for this step. Useful for elements that should
  always be located dynamically, such as table rows, search results, or graph
  nodes that may be re-ordered.
</ResponseField>

<ResponseField name="Act within iframe" type="string">
  Specify an exact URL or a regex to match the URL of the iframe in which the element is located.
  The provided matcher must match exactly one iframe element on the page. To provide a custom regex, use the `/<regex-here>/` format.
</ResponseField>


# File upload
Source: https://momentic.ai/docs/steps/file-upload

Upload a file to a file input element

This step allows you to upload a file to a file input element on the page. You
must execute this step before opening the native file picker dialog.

For security reasons, certain file extensions are not allowed:

* Executable files: `.exe`, `.app`, `.bat`, `.cmd`, `.msi`
* Scripts: `.sh`, `.py`, `.js`, `.php`, `.asp`
* Mobile apps: `.apk`
* Java archives: `.jar`


# Get recorded requests
Source: https://momentic.ai/docs/steps/get-recorded-requests

Retrieve recorded requests

Retrieve recorded requests from a given recorder key. This step must be used
after the [record requests](../steps/record-requests) step to access the
captured requests and their responses.

## Inputs

<ResponseField name="Recorder key" type="string">
  The unique key of the recorded requests you want to retrieve. This key should
  match the one used in the [record requests](../steps/record-requests) step.
</ResponseField>

## Configs

<ResponseField name="Save to environment variable" type="string">
  Store the output of this step into the environment at the given key. This
  configuration only applies for steps that output data.
</ResponseField>

## Outputs

<ResponseField name="Requests" type="Array">
  <Expandable title="properties">
    <ResponseField name="request" type="Request object">
      <Expandable title="properties">
        <ResponseField name="url" type="string">
          The URL of the request that matched the pattern.
        </ResponseField>

        <ResponseField name="method" type="string">
          The HTTP method of the request (e.g., GET, POST).
        </ResponseField>

        <ResponseField name="headers" type="object">
          A key-value object containing the request headers.
        </ResponseField>

        <ResponseField name="json" type="object">
          The JSON body of the request. This will be undefined if the content-type is not JSON.
        </ResponseField>

        <ResponseField name="text" type="string">
          The raw body of the request. This will be undefined if the content-type is not text.
        </ResponseField>
      </Expandable>
    </ResponseField>

    <ResponseField name="response" type="Response object">
      <Expandable title="properties">
        <ResponseField name="status" type="number">
          The HTTP status code of the response.
        </ResponseField>

        <ResponseField name="headers" type="object">
          A key-value object containing the response headers.
        </ResponseField>

        <ResponseField name="json" type="object">
          The JSON body of the response. This will be undefined if the content-type is not JSON.
        </ResponseField>

        <ResponseField name="text" type="string">
          The raw body of the response. This will be undefined if the content-type is not text.
        </ResponseField>
      </Expandable>
    </ResponseField>
  </Expandable>
</ResponseField>


# Hover
Source: https://momentic.ai/docs/steps/hover

Hover over an element on the page

## Inputs

<ResponseField name="Description" type="string">
  Description of the element you want to interact with.
</ResponseField>

## Configs

<ElementConfigs />


# JavaScript
Source: https://momentic.ai/docs/steps/javascript

Execute arbitrary JavaScript in a Node.js sandbox or in the browser

This step allows you to execute arbitrary JavaScript code in a Node.js sandbox
or in the running browser.

Please see the [JavaScript](/javascript) for more details on the global
libraries and utility functions available to you in JavaScript.

## Inputs

<ResponseField name="Javascript" type="string">
  The JavaScript code you want to execute. This can be any valid JavaScript
  code.
</ResponseField>

## Configs

<ResponseField name="Timeout" type="number">
  Max number of seconds for the action to finish. Maximum is 60 seconds.
</ResponseField>

<ResponseField name="Execute in browser" type="boolean">
  Execute script in the current browser instead of a Node.js context.
</ResponseField>

<ResponseField name="Save to environment variable" type="string">
  Store the output of this step into the environment at the given key. This
  configuration only applies for steps that output data.
</ResponseField>


# Key down
Source: https://momentic.ai/docs/steps/key-down

Hold down a combination of keys on the keyboard

Hold down the specified keys using the keyboard. This is useful for testing
behaviors like Shift+Click.

For all available key combinations that can be used, see the
[Key values](https://developer.mozilla.org/en-US/docs/Web/API/UI_Events/Keyboard_event_key_values)
guide.

## Inputs

<ResponseField name="Key" type="string">
  Use `+` to combine keys, e.g. `Control+Shift+T`. Here is a list of valid key
  values.
</ResponseField>

## Configs

<ResponseField name="Convert platform-specific keys" type="boolean">
  Automatically convert known keyboard combinations based on the current
  operating system. For example, `Meta+V` is converted to `Ctrl+V` when the test
  is executed in a Linux environment.
</ResponseField>


# Key up
Source: https://momentic.ai/docs/steps/key-up

Release a combination of keys on the keyboard

Release the specified keys using the keyboard. This is the opposite of the
[`Key down`](./key-down) step, which simulates pressing keys down.

For all available key combinations that can be used, see the
[Key values](https://developer.mozilla.org/en-US/docs/Web/API/UI_Events/Keyboard_event_key_values)
guide.

## Inputs

<ResponseField name="Key" type="string">
  Use `+` to combine keys, e.g. `Control+Shift+T`. Here is a list of valid key
  values.
</ResponseField>

## Configs

<ResponseField name="Convert platform-specific keys" type="boolean">
  Automatically convert known keyboard combinations based on the current
  operating system. For example, `Meta+V` is converted to `Ctrl+V` when the test
  is executed in a Linux environment.
</ResponseField>


# Load auth state
Source: https://momentic.ai/docs/steps/load-auth-state

Load session data in JSON form into the current browser context

Load or clear session state using a JSON snapshot including cookies,
`localstorage`, and IndexDB entries.

## Inputs

<ResponseField name="Authentication state function" type="string">
  JavaScript code returning an object containing cookies and local storage to
  load into the session. The object should be in the same format returned by the
  [Save auth state](/steps/save-auth-state) step. Leave the function blank or
  return an empty object to clear the current session state instead.
</ResponseField>


# Local storage
Source: https://momentic.ai/docs/steps/local-storage

Setting a value in local storage

Set a local storage value that will persist throughout the browser session.

## Inputs

<ResponseField name="Key" type="string">
  Key to set in local storage.
</ResponseField>

<ResponseField name="Value" type="string">
  Value to set in local storage.
</ResponseField>


# Mock route
Source: https://momentic.ai/docs/steps/mock-route

Intercept network requests and mock their responses

For more information about using this step, see our guide on
[request mocking](../request-mocking).

## Inputs

<ResponseField name="URL Matcher" type="object">
  <Expandable>
    <Tabs>
      <Tab title="Substring">
        <ResponseField name="url" type="string">
          The substring to look for
        </ResponseField>
      </Tab>

      <Tab title="Glob">
        <ResponseField name="glob" type="string">
          The glob pattern to match against
        </ResponseField>
      </Tab>

      <Tab title="Regex">
        <ResponseField name="regex" type="string">
          The regex pattern to match against
        </ResponseField>
      </Tab>

      <Tab title="Domain">
        <ResponseField name="domain" type="string">
          The domain to match against. If matching a subdomain, the exact subdomain is required.
        </ResponseField>
      </Tab>
    </Tabs>
  </Expandable>
</ResponseField>

<ResponseField name="HTTP Method" type="POST | GET | DELETE | PUT | PATCH | OPTIONS">
  Only match requests that have this HTTP Method
</ResponseField>

<ResponseField name="Response" type="string">
  Javascript code used to generate a response for the intercepted requests. This code must return a Javascript `Response` object. This
  code behaves similarly to Momentic's standard javascript step with a couple of
  exceptions:

  * Environment variables can be read at `env.<VARIABLE_NAME>`, however, they cannot be updated using `setVariable`. This is to prevent potential race conditions.
  * The request itself is accessible at `mock.request`. It is a standard Javascript [request object](https://developer.mozilla.org/en-US/docs/Web/API/Request).
  * If the 'fetch real response' config is enabled, the original response is accessible at `mock.response`. It is a standard Javascript [response object](https://developer.mozilla.org/en-US/docs/Web/API/Response).
</ResponseField>

## Configs

<ResponseField name="Fetch real response" type="boolean">
  Complete the original request, and pass its response into the generator as
  `mock.response`. Enabling this option is helpful if you want to modify the
  original response rather than fully replacing it. You should not enable this
  option if the request will fail (for example if the host is inaccessible), as
  it will cause the mock to fail.
</ResponseField>

<ResponseField name="Key" type="string">
  A key that can be used to reference the mock later. This should be set if you
  want to remove the mock later in the test. If not set, a random key will be
  generated.
</ResponseField>

<ResponseField name="Save to environment variable" type="string">
  Store the output of this step into the environment at the given key. This
  configuration only applies for steps that output data.
</ResponseField>


# Navigate
Source: https://momentic.ai/docs/steps/navigate

Navigate to a specified URL

Navigate to the specified URL.

## Inputs

<ResponseField name="Url" type="url">
  URL to navigate to.
</ResponseField>


# New tab
Source: https://momentic.ai/docs/steps/new-tab

Open a new tab

Create and switch to a new tab in the browser.

## Inputs

<ResponseField name="Url to open" type="url">
  URL to open as a new tab. Fully qualified URLs are supported as well as URLs
  relative to the BASE\_URL.
</ResponseField>


# Page check
Source: https://momentic.ai/docs/steps/page-check

Assert on page content

Assert on the active page using HTML content substring.

<ResponseField name="Timeout" type="number">
  The maximum number of seconds to wait for the assertion to be true. If it
  becomes true at any point during that window, the step passes. The step may
  continue running for a bit longer due to the latency of the final check, which
  starts when the timeout is reached.
</ResponseField>


# Paste
Source: https://momentic.ai/docs/steps/paste

Paste text from the browser clipboard

Paste the clipboard contents.


# Press
Source: https://momentic.ai/docs/steps/press

Press a combination of keys on the keyboard

Press the specified keys using the keyboard.

For all available key combinations that can be used, see the
[Key values](https://developer.mozilla.org/en-US/docs/Web/API/UI_Events/Keyboard_event_key_values)
guide.

## Inputs

<ResponseField name="Value" type="string">
  Use `+` to combine keys, e.g. `Control+Shift+T`. Here is a list of valid key
  values.
</ResponseField>

## Configs

<ResponseField name="Convert platform-specific keys" type="boolean">
  Automatically convert known keyboard combinations based on the current
  operating system. For example, `Meta+V` is converted to `Ctrl+V` when the test
  is executed in a Linux environment.
</ResponseField>

<ResponseField name="Repeat" type="number">
  Number of times to issue the key sequence.
</ResponseField>

<ResponseField name="Delay ms" type="number">
  Milliseconds to wait after each key sequence. This is only applicable if the
  `repeat` config is set to a value greater than 1.
</ResponseField>


# Record requests
Source: https://momentic.ai/docs/steps/record-requests

Record requests matching a specific URL pattern

Start recording requests that match a specific URL pattern. This is useful for
capturing API calls or other network requests made by the application during
testing. The recorded requests can later be retrieved using the
[get recorded requests](./get-recorded-requests) step.

Only requests made after this step is executed will be recorded. If an action
triggers the request, make sure to add this step before the action in your test.

## Inputs

<ResponseField name="URL Matcher" type="object">
  <Expandable>
    <Tabs>
      <Tab title="Substring">
        <ResponseField name="url" type="string">
          The substring to look for
        </ResponseField>
      </Tab>

      <Tab title="Glob">
        <ResponseField name="glob" type="string">
          The glob pattern to match against
        </ResponseField>
      </Tab>

      <Tab title="Regex">
        <ResponseField name="regex" type="string">
          The regex pattern to match against
        </ResponseField>
      </Tab>

      <Tab title="Domain">
        <ResponseField name="domain" type="string">
          The domain to match against. If matching a subdomain, the exact subdomain is required.
        </ResponseField>
      </Tab>
    </Tabs>
  </Expandable>
</ResponseField>

<ResponseField name="HTTP Method" type="POST | GET | DELETE | PUT | PATCH | OPTIONS">
  Only match requests that have this HTTP Method
</ResponseField>

<ResponseField name="Key" type="string">
  A unique key to identify the recorder. This key can be used in the [get
  recorded requests](./get-recorded-requests) step to wait for the request to
  complete.
</ResponseField>


# Refresh
Source: https://momentic.ai/docs/steps/refresh

Refresh the current page



# Register request listener
Source: https://momentic.ai/docs/steps/register-request-listener

Register a listener for requests that match a specific URL pattern

Starts listening for requests that match a specific URL pattern. When awaited
using an [await listener](../steps/await-listener) step, it will return the
first request matching the pattern, if any.

You should register your listener before the request is made. If an action
triggers the request, make sure to add this step before the action in your test.

## Inputs

<ResponseField name="URL Matcher" type="object">
  <Expandable>
    <Tabs>
      <Tab title="Substring">
        <ResponseField name="url" type="string">
          The substring to look for
        </ResponseField>
      </Tab>

      <Tab title="Glob">
        <ResponseField name="glob" type="string">
          The glob pattern to match against
        </ResponseField>
      </Tab>

      <Tab title="Regex">
        <ResponseField name="regex" type="string">
          The regex pattern to match against
        </ResponseField>
      </Tab>

      <Tab title="Domain">
        <ResponseField name="domain" type="string">
          The domain to match against. If matching a subdomain, the exact subdomain is required.
        </ResponseField>
      </Tab>
    </Tabs>
  </Expandable>
</ResponseField>

<ResponseField name="HTTP Method" type="POST | GET | DELETE | PUT | PATCH | OPTIONS">
  Only match requests that have this HTTP Method
</ResponseField>

<ResponseField name="Listener key" type="string">
  A unique key to identify the listener. This key can be used in the [await
  listener](../steps/await-listener) step to wait for the request to complete.
</ResponseField>

## Outputs

The following outputs will be returned once the listener resolves in an
[await listener](../steps/await-listener) step:

<ResponseField name="request" type="Request object">
  <Expandable title="properties">
    <ResponseField name="url" type="string">
      The URL of the request that matched the pattern.
    </ResponseField>

    <ResponseField name="method" type="string">
      The HTTP method of the request (e.g., GET, POST).
    </ResponseField>

    <ResponseField name="headers" type="object">
      A key-value object containing the request headers.
    </ResponseField>

    <ResponseField name="json" type="object">
      The JSON body of the request. This will be undefined if the content-type is not JSON.
    </ResponseField>

    <ResponseField name="text" type="string">
      The raw body of the request. This will be undefined if the content-type is not text.
    </ResponseField>
  </Expandable>
</ResponseField>

<ResponseField name="response" type="Response object">
  <Expandable title="properties">
    <ResponseField name="status" type="number">
      The HTTP status code of the response.
    </ResponseField>

    <ResponseField name="headers" type="object">
      A key-value object containing the response headers.
    </ResponseField>

    <ResponseField name="json" type="object">
      The JSON body of the response. This will be undefined if the content-type is not JSON.
    </ResponseField>

    <ResponseField name="text" type="string">
      The raw body of the response. This will be undefined if the content-type is not text.
    </ResponseField>
  </Expandable>
</ResponseField>


# Remove mock route
Source: https://momentic.ai/docs/steps/remove-mock-route

Stop mocking network requests to a given route

After this step is run, subsequent requests will be routed to their original
destination.

For more information about using this step, see our guide on
[request mocking](../request-mocking).

## Inputs

<ResponseField name="Key" type="string">
  The key that was defined when mocking the route. If not specified, this step
  will remove all mocks.
</ResponseField>


# Save auth state
Source: https://momentic.ai/docs/steps/save-auth-state

Return the values of cookies and local storage as a JSON object

Save auth state (cookies, local storage) into a JavaScript object format usable
by the [Load auth state](/steps/load-auth-state) step.

## Configs

<ResponseField name="Save to environment variable" type="string">
  Store the output of this step into the environment at the given key. This
  configuration only applies for steps that output data.
</ResponseField>


# Scroll
Source: https://momentic.ai/docs/steps/scroll

Scroll the page

Scroll up, down, left, or right by a specified amount.

## Inputs

<ResponseField name="Pixels to scroll" type="number">
  Number of pixels to scroll the page. Positive values scroll down, negative
  values scroll up. If omitted, scrolls the full height of the viewport for
  vertical directions and the full width for horizontal directions.
</ResponseField>

<ResponseField name="Element to hover when scrolling" type="string">
  Description of the element you want to interact with.
</ResponseField>

## Configs

<ResponseField name="Disable stability checks" type="boolean">
  Do not wait for the element to be visible, stable and actionable before
  interacting. Useful for elements that are constantly animating or partially
  obscured.
</ResponseField>

<ResponseField name="Use CSS selector" type="boolean">
  Treat the element description as a CSS selector. This is not recommended for
  maintainability reasons but can be useful for dynamic pages.
</ResponseField>

<ResponseField name="Disable caching" type="boolean">
  Disable [caching](/step-cache) for this step. Useful for elements that should
  always be located dynamically, such as table rows, search results, or graph
  nodes that may be re-ordered.
</ResponseField>

<ResponseField name="Act within iframe" type="string">
  Specify an exact URL or a regex to match the URL of the iframe in which the element is located.
  The provided matcher must match exactly one iframe element on the page. To provide a custom regex, use the `/<regex-here>/` format.
</ResponseField>


# Select
Source: https://momentic.ai/docs/steps/select

Interact with native HTML select elements

Select an `<option>` from an HTML Select `<select>` element based on a
description.

## Inputs

<ResponseField name="Element to select an option from" type="string">
  Description of the select.
</ResponseField>

## Configs

<ResponseField name="Disable stability checks" type="boolean">
  Do not wait for the element to be visible, stable and actionable before
  interacting. Useful for elements that are constantly animating or partially
  obscured.
</ResponseField>

<ResponseField name="Use CSS selector" type="boolean">
  Treat the element description as a CSS selector. This is not recommended for
  maintainability reasons but can be useful for dynamic pages.
</ResponseField>

<ResponseField name="Disable caching" type="boolean">
  Disable [caching](/step-cache) for this step. Useful for elements that should
  always be located dynamically, such as table rows, search results, or graph
  nodes that may be re-ordered.
</ResponseField>

<ResponseField name="Act within iframe" type="string">
  Specify an exact URL or a regex to match the URL of the iframe in which the element is located.
  The provided matcher must match exactly one iframe element on the page. To provide a custom regex, use the `/<regex-here>/` format.
</ResponseField>


# Set header
Source: https://momentic.ai/docs/steps/set-header

Adds a custom header to later requests

You should use this step before the request is initiated. If you need to add a
custom header to the initial page load, you can use this step followed by either
a [navigate](../steps/navigate) step or a [refresh](../steps/refresh) step.

## Inputs

<ResponseField name="Name" type="string">
  The name of the header. This should be a valid HTTP header name.
</ResponseField>

<ResponseField name="Value" type="string">
  The value of the header. This can be any string value.
</ResponseField>

<ResponseField name="URL Matcher" type="object">
  <Expandable>
    <Tabs>
      <Tab title="Substring">
        <ResponseField name="url" type="string">
          The substring to look for
        </ResponseField>
      </Tab>

      <Tab title="Glob">
        <ResponseField name="glob" type="string">
          The glob pattern to match against
        </ResponseField>
      </Tab>

      <Tab title="Regex">
        <ResponseField name="regex" type="string">
          The regex pattern to match against
        </ResponseField>
      </Tab>

      <Tab title="Domain">
        <ResponseField name="domain" type="string">
          The domain to match against. If matching a subdomain, the exact subdomain is required.
        </ResponseField>
      </Tab>
    </Tabs>
  </Expandable>
</ResponseField>

<ResponseField name="HTTP Method" type="POST | GET | DELETE | PUT | PATCH | OPTIONS">
  Only match requests that have this HTTP Method
</ResponseField>


# Switch tab
Source: https://momentic.ai/docs/steps/switch-tab

Switch to a different tab

Switch to different tab in the browser.


# Type
Source: https://momentic.ai/docs/steps/type

Typing text into an input field

Type the specified text into an element.

## Inputs

<ResponseField name="Value" type="string">
  The text you want to type into the input field.
</ResponseField>

<ResponseField name="Element to type into" type="string">
  Description of the element you want to interact with.
</ResponseField>

## Configs

<ResponseField name="Replace content" type="string">
  Choose when the typed content should replace the existing content.

  * `Only inputs and textareas`: Only replace content in input and textarea
    elements.
  * `Never`: Never replace existing content.
  * `Always`: Always replace existing content, regardless of element type (useful
    custom `contenteditable` elements).
</ResponseField>

<ResponseField name="Press enter" type="boolean">
  Press the Enter key after typing the text.
</ResponseField>

<ResponseField name="Key press delay" type="number">
  Amount of milliseconds to wait after each key press. This is useful for
  triggering on-press event handlers such as autocomplete.
</ResponseField>

<ResponseField name="Disable stability checks" type="boolean">
  Do not wait for the element to be visible, stable and actionable before
  interacting. Useful for elements that are constantly animating or partially
  obscured.
</ResponseField>

<ResponseField name="Use CSS selector" type="boolean">
  Treat the element description as a CSS selector. This is not recommended for
  maintainability reasons but can be useful for dynamic pages.
</ResponseField>

<ResponseField name="Disable caching" type="boolean">
  Disable [caching](/step-cache) for this step. Useful for elements that should
  always be located dynamically, such as table rows, search results, or graph
  nodes that may be re-ordered.
</ResponseField>

<ResponseField name="Act within iframe" type="string">
  Specify an exact URL or a regex to match the URL of the iframe in which the element is located.
  The provided matcher must match exactly one iframe element on the page. To provide a custom regex, use the `/<regex-here>/` format.
</ResponseField>


# Visual diff
Source: https://momentic.ai/docs/steps/visual-diff

Compare screenshots

Compare a screenshot of the page or a specific element to a baseline image.

## Inputs

<ResponseField name="Description" type="string">
  Description of the element that you want to screenshot. If not provided, the
  entire page will be captured.
</ResponseField>

## Configs

<ResponseField name="Threshold" type="number">
  Percentage of total pixels that can be different before the step fails.
</ResponseField>

<ResponseField name="Disable stability checks" type="boolean">
  Do not wait for the element to be visible, stable and actionable before
  interacting. Useful for elements that are constantly animating or partially
  obscured.
</ResponseField>

<ResponseField name="Use CSS selector" type="boolean">
  Treat the element description as a CSS selector. This is not recommended for
  maintainability reasons but can be useful for dynamic pages.
</ResponseField>

<ResponseField name="Disable caching" type="boolean">
  Disable [caching](/step-cache) for this step. Useful for elements that should
  always be located dynamically, such as table rows, search results, or graph
  nodes that may be re-ordered.
</ResponseField>

<ResponseField name="Act within iframe" type="string">
  Specify an exact URL or a regex to match the URL of the iframe in which the element is located.
  The provided matcher must match exactly one iframe element on the page. To provide a custom regex, use the `/<regex-here>/` format.
</ResponseField>


# Wait
Source: https://momentic.ai/docs/steps/wait

Wait a certain amount of time before continuing

Wait for a specified number of seconds.

## Inputs

<ResponseField name="Seconds" type="number">
  Number of seconds to wait before continuing.
</ResponseField>


# Wait for URL
Source: https://momentic.ai/docs/steps/wait-for-url

Wait for the active page to match a URL

## Inputs

<ResponseField name="URL Matcher" type="object">
  <Expandable>
    <Tabs>
      <Tab title="Substring">
        <ResponseField name="url" type="string">
          The substring to look for
        </ResponseField>
      </Tab>

      <Tab title="Glob">
        <ResponseField name="glob" type="string">
          The glob pattern to match against
        </ResponseField>
      </Tab>

      <Tab title="Regex">
        <ResponseField name="regex" type="string">
          The regex pattern to match against
        </ResponseField>
      </Tab>

      <Tab title="Domain">
        <ResponseField name="domain" type="string">
          The domain to match against. If matching a subdomain, the exact subdomain is required.
        </ResponseField>
      </Tab>
    </Tabs>
  </Expandable>
</ResponseField>

## Configs

<ResponseField name="Case sensitive" type="boolean">
  Ignore case when comparing the URL.
</ResponseField>

<ResponseField name="Negate comparison" type="boolean">
  Wait for the URL to NOT match the given pattern instead.
</ResponseField>


# Suites
Source: https://momentic.ai/docs/suites



<Info>Suites are only available on Momentic Cloud.</Info>

You can use suites to group and run tests together. You can configure shared
schedules, notifications, and environments for all tests in a suite.

Select **Suites** on the left sidebar to view all your suites. Click on the
**Create suite** button in the top-right corner to create a new suite.

<Frame>
  <img />
</Frame>

## Setup & teardown

The setup test will always run first before any other tests in the suite. If it
fails, the rest of the suite will be skipped and the entire suite will be marked
as failed.

If the setup test succeeds, Momentic will continue running the tests in the
suite. **All tests in the suite will run in parallel**.

Whenever the suite's final result is determined, Momentic will start running the
teardown test. The teardown test's result does not affect the overall suite
result.

### Persistent variables

To allow passing data between tests in a suite, Momentic exposes the
`setPersistentVariable` JavaScript function. This function allows users to set a
[variable](/variables) that is accessible by later tests.

```javascript theme={null}
setPersistentVariable("CREATED_USERNAME", "randomusername");
```


# Variables
Source: https://momentic.ai/docs/variables



Variables are a powerful feature in Momentic that allow you to store and reuse
data across your tests. They can be used to store values like user credentials,
URLs, or any other data that you want to reference multiple times in your tests.

## Environment variables

All variables are stored on a global object `env` that is accessible from any
step in your test. You can access these variables using the templating syntax
`{{ env.VARIABLE_NAME }}`.

Reserved variables:

* `BASE_URL`: The base URL of the environment. This is automatically set when
  you create a new environment and can be used to construct URLs for your tests.
* `CURRENT_URL`: The current URL of the page being tested. This is updated
  automatically as you navigate through your test.
* `ENV_NAME`: The name of the environment. This is also automatically set when
  you create a new environment and can be used to identify the environment in
  your tests.
* `TEST_NAME`: The name of the test. This is automatically set when you create a
  new test and can be used to identify the test in your tests.

You can add any number of key-value pairs as environment variables when you
create a new environment in Momentic. Any tests that you create using that
environment will have access to these variables.

If you're using the [Momentic CLI](/quickstart/cli), you can also load
environment variables from a `.env` or JSON file.

## Setting variables

### `setVariable`

You can use [JavaScript](/steps/javascript) steps to set variables using the
`setVariable` function.

```javascript theme={null}
setVariable("USERNAME", "testuser");
setVariable("PASSWORD", Math.random().toString(36).substring(2, 15));
```

This will set the `USERNAME` variable to `testuser` and the `PASSWORD` variable
to a random string. You can then access these variables in other steps using the
templating syntax `{{ env.USERNAME }}` or `{{ env.PASSWORD }}`.

### Save to environment variable

For steps that can have a return value such as [AI extract](/steps/ai-extract)
or [JavaScript](/steps/javascript), there's an option on the step that allows
you to input a string key to set on the environment. After this step is executed
you will be able to access the variable using `{{ env.NUM_BUTTONS }}`.

<Frame>
  <img />
</Frame>

## Accessing variables

Variables can be accessed using JavaScript. You can use it directly inside
[JavaScript](/steps/javascript) steps or by using the templating syntax `{{ }}`.
All input fields support the templating syntax.

For example, if you have set a variable named `USERNAME`, you can access it like
this:

<Frame>
  <img />
</Frame>

### Module parameters

Module parameters are also variables. If you have a module parameter named
`API_KEY`, you can access it using `{{ env.API_KEY }}`.

## Variable scope

Variables in Momentic tests all live on the global test scope, which means they
are accessible from any step in the test. This allows you to set a variable in
one step and use it in another step later in the test.


