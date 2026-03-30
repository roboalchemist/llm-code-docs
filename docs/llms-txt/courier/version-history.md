# Source: https://www.courier.com/docs/platform/journeys/version-history.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.courier.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Version History

> Track published versions of your journeys, compare changes side-by-side, and revert to a previous version.

Every time you publish a journey, Courier saves a versioned snapshot. Version history lets you see what changed between publishes, compare any two versions side-by-side, and revert to a previous version if needed.

## Opening Version History

In the journey editor, click the **history** button (the clock-with-arrow icon next to the Publish button) to open the version history page. The button is disabled if the journey has never been published.

This opens the version history panel on the right side with a list of all previously published versions, each labeled with a version number (v1, v2, ...) and a relative timestamp. The most recent version is marked **Current**.

<Frame caption="Version history page showing a list of published versions">
  <img src="https://mintcdn.com/courier-4f1f25dc/kTEr7cZVe0KtgIWx/assets/platform/journeys/version-history-page.png?fit=max&auto=format&n=kTEr7cZVe0KtgIWx&q=85&s=7ba3df804f0861c4a8d92a4edbc25990" width="3454" height="1924" data-path="assets/platform/journeys/version-history-page.png" />
</Frame>

## Comparing Versions

Click any version in the list to see a side-by-side comparison: the selected version on the left and the current draft on the right. Both canvases are read-only. A banner at the top confirms which version you're comparing (e.g., "Comparing Version v2 with Current Draft - Read Only").

<Frame caption="Side-by-side comparison of version v2 (left) against the current draft (right)">
  <img src="https://mintcdn.com/courier-4f1f25dc/kTEr7cZVe0KtgIWx/assets/platform/journeys/version-comparison.png?fit=max&auto=format&n=kTEr7cZVe0KtgIWx&q=85&s=6369cea579a59f32407ceb471d1937ff" width="3452" height="1660" data-path="assets/platform/journeys/version-comparison.png" />
</Frame>

You can click individual nodes in either canvas to inspect how they were configured in that version. This lets you see the exact conditions, delay durations, template content, or schema fields that were active at a specific point in time.

This is useful for understanding what changed when a journey's behavior shifts unexpectedly.

## Reverting to a Previous Version

Hover over any previous version in the list to reveal the **Revert** button. Click it, or click **Revert to this version** in the comparison banner at the top. This loads that version's configuration into the editor as a new draft. You still need to publish the restored version for it to take effect.

Reverting does not delete any versions. It creates a new draft based on the selected version; publishing it creates a new version entry in the history. The full audit trail is preserved.

<Note>
  Runs that started on a previous version continue executing against that version's configuration. Reverting and re-publishing only affects new invocations.
</Note>

## What's Next

<CardGroup cols={2}>
  <Card title="Run Inspection" href="/platform/journeys/run-inspection" icon="magnifying-glass">
    Debug individual runs against their specific version
  </Card>

  <Card title="Metrics" href="/platform/journeys/metrics" icon="chart-line">
    Correlate version changes with performance shifts
  </Card>

  <Card title="Starting a Journey" href="/platform/journeys/invocation" icon="bolt">
    Configure triggers and publish your journey
  </Card>

  <Card title="Building Your Journey" href="/platform/journeys/building-journeys" icon="arrow-progress">
    Add nodes and modify your journey's structure
  </Card>
</CardGroup>
