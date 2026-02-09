# Source: https://docs.avaamo.com/user-guide/skills/prompt-skill/prompt-versions.md

# Prompt Versions

Prompt versioning helps you track, compare, and restore changes made to a prompt skill over time. Each update to a prompt skill is automatically saved as a new version, allowing you to safely iterate and roll back when needed.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FUEK6L95rZ7ziaHdGU5FV%2FScreenshot%2015-01-2026%20at%2012.47.png?alt=media&#x26;token=b46b7867-d05f-4f76-b853-20ebbbc9af4c" alt=""><figcaption></figcaption></figure>

### Version history overview

The first time a prompt skill is added and saved, `version 1` is created. A new version is created whenever you `save changes` to any of the following sections in a prompt skill:

* Prompt content
* Functions
* Advanced settings

&#x20;[Version comparison](#version-comparison) becomes available once a second version exists.

**To create a new version:**

1. Open the agent and navigate to the `Prompt skill`.
2. Make changes to one or more sections:
   * Prompt
   * Functions
   * Advanced settings
3. Click **Save**.

A new version is created and added to the version history.

### Version details and history

When a version is created, you can view the following details at a glance:

* The `latest version` always appears at the top of the version list.
* Each version includes these details:
  * `Clone of`: Indicates the version from which the current version was generated.
  * `Created by:`: Displays the name of the user who created the version.
  * `Last modified`**:** Shows the date and time when the version was created.
  * `Restored from`**:** Indicates the version from which the current version was restored.
* You can click [View](#version-comparison) to see the details of a specific version.
* Click [Restore](#restoring-a-previous-version) to apply the changes from the selected version to the latest version.
* Versions are displayed with pagination:
  * Up to 10 versions per page
  * Up to 100 most recent versions are retained

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F5KiLFMztiUiFgoynm0Qw%2FScreenshot%2015-01-2026%20at%2012.49.png?alt=media&#x26;token=c38f81ab-e784-4ab8-b16b-b86b42e8f5c3" alt=""><figcaption></figcaption></figure>

### Version comparison

You can compare changes between any two versions to understand what was updated. This helps identify updates across prompt text, functions, and advanced settings.

**To compare versions:**

1. Open the `Prompt Versions` section of the prompt skill.
2. Click on `View` to open the selected prompt skill version.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F5KiLFMztiUiFgoynm0Qw%2FScreenshot%2015-01-2026%20at%2012.49.png?alt=media&#x26;token=c38f81ab-e784-4ab8-b16b-b86b42e8f5c3" alt=""><figcaption></figcaption></figure>

2. Select any two versions from the comparison dropdown.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F9GqrrBwhYVVL0xqXGad0%2FScreenshot%202026-01-30%20at%2010.50.34%E2%80%AFAM.png?alt=media&#x26;token=b7a0d830-78a8-45d3-8cd0-5082b703a208" alt=""><figcaption></figcaption></figure>

3. View the changes side by side.

Change in the prompt:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fa1oFSkXWz1nr2UrrfX6u%2FScreenshot%202026-01-30%20at%206.19.37%E2%80%AFPM.png?alt=media&#x26;token=0fd226ee-ee75-4c9f-a6ad-eb71bdc7c83d" alt=""><figcaption></figcaption></figure>

Change in the function calls:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F8XKRW35gazG5xY1MPyVZ%2FScreenshot%202026-01-30%20at%206.07.43%E2%80%AFPM.png?alt=media&#x26;token=77d869f0-8e71-4c3d-84b6-5046adc8757a" alt=""><figcaption></figcaption></figure>

Change in the Advanced settings:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FPTqezLzqTpuRNnCNYV46%2FScreenshot%202026-01-30%20at%2010.48.04%E2%80%AFAM.png?alt=media&#x26;token=29c1b921-49ff-42a3-a6f0-3db7cd4d9076" alt=""><figcaption></figcaption></figure>

4. You can use `Expand all` or `Collapse all` to view or hide all change details at once.
5. You can view the changes on the right side of each section with clear labels indicating whether a section is `Unchanged` or `Modified`.
6. If you expand a section marked as Modified, you can see exactly what changed between the two versions, whether content was `added` or `removed`. For changes in the Prompt section, the comparison also highlights the exact locations where the updates occurred.

### Restore selected

You can now selectively restore specific sections instead of restoring all changes at once.

Each section includes a checkbox to control what is restored. On the Version Comparison page, the following sections include selectable checkboxes:

* Prompt
* Function Calls
* Advanced Settings

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F9mi6C26vz25hBzs2BKqS%2FScreenshot%202026-01-30%20at%2010.41.15%E2%80%AFAM.png?alt=media&#x26;token=5a240f36-b943-4b1d-b5bf-33b7cb56f879" alt=""><figcaption></figcaption></figure>

Select one or more sections using the corresponding `checkboxes`. Click `Restore Selected`.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FjVfBvlZHLfvpSK11DK6k%2FScreenshot%202026-01-30%20at%2010.44.34%E2%80%AFAM.png?alt=media&#x26;token=2d122886-4f51-4b47-a25f-e3e94ad0c47a" alt=""><figcaption></figcaption></figure>

In the confirmation window, click `Yes, restore` to continue. The selected version is restored and saved as the latest version. Click `Cancel` to exit without restoring the version.

### Restoring a previous version

You can restore a prompt skill to an earlier version using the **Restore** option. This allows you to safely roll back changes while keeping a clear version history.

**How restoration works**

* Restoring a version reverts the prompt skill to the selected version, including the `prompt`, `functions`, and `advanced settings`.
* When a restore is performed, a new version is automatically created. This version includes a note indicating the previous version from which it was restored.
* Restoring a version brings back all changes captured in that version at once.
* If a version contains changes in only one section (for example, advanced settings), restoring that version updates only that section, as the other sections were unchanged.
* The latest version, including restored versions, always appears at the top of the version list.

**To restore a version:**

1. Open the `Prompt Versions` section of the prompt skill.
2. Select the version you want to restore. Click `Restore`.
3. In the confirmation window, click `Yes, restore` to continue. The selected version is restored and saved as the latest version. Click `Cancel` to exit without restoring the version.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fkmg8WYC4WXye3pOBu5Bd%2FScreenshot%202026-01-15%20at%2012.51.04%E2%80%AFPM.png?alt=media&#x26;token=5968377c-5245-4435-9e17-08274bb936f9" alt=""><figcaption></figcaption></figure>

### Pull and Promote behavior

* Prompt versioning is supported in all stages: Development, Testing, Staging, and Production.
* When an agent is `promoted` from one stage to another, the version history is not carried over. The promoted agent starts with a fresh version history, beginning from the copied state.
* When you `pull` updates from one stage to another, a `new version` is created in the target stage that reflects the pulled changes.

### Export and import behavior

* Version history is `not included` when exporting an agent.
* Only the latest prompt version is exported.
* When an agent is imported, versioning starts fresh from the imported state.
