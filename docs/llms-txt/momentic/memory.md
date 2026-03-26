# Source: https://momentic.ai/docs/memory.md

> ## Documentation Index
> Fetch the complete documentation index at: https://momentic.ai/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Memory

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


Built with [Mintlify](https://mintlify.com).