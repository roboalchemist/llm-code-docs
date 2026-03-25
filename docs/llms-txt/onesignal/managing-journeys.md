# Source: https://documentation.onesignal.com/docs/en/managing-journeys.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Managing Journeys

> Manage your OneSignal Journeys with confidence—learn how to edit steps, update message content, view stats, duplicate flows, archive or delete, and collaborate using team notes.

## Editing a Journey

To edit a Journey, click the **Edit** button. This activates **Edit Mode**, allowing you to modify steps, messages, wait durations, and other Journey components.

Once done, click **Settings > Save**. Changes are applied as follows:

* **Step changes** take effect immediately. Any active or future users will flow through the updated steps based on where they are in the Journey.
* **Settings changes** only affect users who enter the Journey *after* the changes are saved. Existing users in the flow remain unaffected.

### Editing wait steps

Changing the duration of a **Wait** step only affects users who enter the step after the change. Timers already set for existing users are not updated or reset.

### Editing message steps

* If you **update the content/template** of an existing message step, existing stats are retained and new metrics accumulate from the time of the change.
* If you **replace or remove** a message step, the new step starts tracking stats from zero.

### Editing split branches

Split Branches are locked once a Journey is live. If you need to change the number or structure of branches, you must **duplicate or create a new Journey**.

### Editing audience segments

Audience segments on a live Journey with [Future additions only](./journeys-settings#future-additions-only) enabled are locked and cannot be modified. If you need to change the target audience, you must **duplicate or create a new Journey**.

***

## Viewing and refreshing stats

* Click **View Stats** to exit Edit Mode and enter Stat Mode. This allows you to analyze message and Journey performance.
* Use **Refresh Stats** to reload the most recent user interaction data.

For a full breakdown of metrics and reporting, see [Journeys Analytics](./journeys-analytics).

***

## Journey actions

Click the **More Options** (⋯) menu to access additional Journey management tools:

### Stop or archive a Journey

* **Stop + Archive** halts all user progress through the Journey and marks it as archived.
* Archived Journeys can still be viewed and duplicated, but cannot resume sending.

### Duplicate a Journey

* **Duplicate** creates a new Journey with the same structure and settings.
* **Start and end times are not copied**—you must set them manually for the new Journey.

### Export a Journey as an image

* **Export as Image** downloads a PNG of your Journey canvas.
* Only visible steps on-screen are included in the snapshot.

### Delete a Journey

* **Delete** permanently removes the Journey and its data.
* This action is irreversible.

***

## Adding team notes

Use **Notes** to annotate Journey steps with important context, collaboration insights, or implementation rationale. This helps teams stay aligned when reviewing or editing Journeys.

### Benefits of notes

1. Keep all strategic context centralized in the Journey.
2. Communicate segmentation logic, personalization rules, or testing hypotheses.
3. Document what each message is intended to convey or test.

### How to add a note

1. Enter **Edit Mode**.
2. Select a message or action step.
3. Add your note.
4. Click **Save**.

<Frame caption="Adding a note to a Journey step">
  <img src="https://mintcdn.com/onesignal/3zq1PvSaqvUE2bIx/images/docs/2a757d717b335fea4cded29bd91f6d1f460f32424d4438f83bc52da39c0564eb-image.png?fit=max&auto=format&n=3zq1PvSaqvUE2bIx&q=85&s=536e9e23a12d199ebdf088113de2c84f" width="1314" height="438" data-path="images/docs/2a757d717b335fea4cded29bd91f6d1f460f32424d4438f83bc52da39c0564eb-image.png" />
</Frame>

Once saved, a note icon appears on the step. Click the icon to view or edit the note.

<Frame caption="A note added to a Journey step">
  <img src="https://mintcdn.com/onesignal/RWtLFPeffHrC81wI/images/docs/a94015318920521379892df5435f866eb8cdd391ba373bd57f42320123ff6588-image.png?fit=max&auto=format&n=RWtLFPeffHrC81wI&q=85&s=73deecbc57e0f2f3b778f8608a245499" width="720" height="432" data-path="images/docs/a94015318920521379892df5435f866eb8cdd391ba373bd57f42320123ff6588-image.png" />
</Frame>

***

Built with [Mintlify](https://mintlify.com).
