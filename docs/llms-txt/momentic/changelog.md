# Source: https://momentic.ai/docs/changelog.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Product updates

> New updates and improvements

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


Built with [Mintlify](https://mintlify.com).