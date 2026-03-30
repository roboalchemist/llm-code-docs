# Source: https://momentic.ai/docs/failure-analysis.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Failure analysis

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


Built with [Mintlify](https://mintlify.com).