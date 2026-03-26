# Source: https://docs.tabnine.com/main/getting-started/context-engine/admin-console/data-sources.md

# Data Sources

Use the Overview and Codebase tabs together as your single place to onboard and inspect repositories and depots. Whenever you want Context Engine to understand additional code, come here first to connect, review, and scope those sources.

### Overview tab

To see all data sources that Context Engine can use, go to Data Sources and open the Overview tab. Use this tab whenever you want a high‑level picture of connected sources and their analyzers.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FEa223F4DGHRK5mdfwYOB%2Funknown.png?alt=media&#x26;token=6714e293-6f0f-422c-b196-c2332cf0bf41" alt=""><figcaption></figcaption></figure>

To narrow the list, use the search box and filters at the top of the grid. You can filter by team, equality, and analyzers to focus on a specific subset of data sources.

To inspect a particular source, find its card in the grid. You will be able to review its connection status, analyzers (such as “Symbols” or “Summary & API”),  assigned teams, and/or the time it was last synced.

Use this tab to confirm that new repositories or depots appear after you connect them.

### Codebase tab

To configure which codebases Context Engine and Tabnine can analyze, open the Codebase tab under Data Sources. At the top of the tab, locate the Tabnine Context section and use the Enable Tabnine Context toggle switch to turn workspace context on or off.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FzSpzL0hMEYo7ctR9R0wb%2Funknown.png?alt=media&#x26;token=3dbeec0f-eea7-4d05-9387-fbd721fa7ea0" alt=""><figcaption></figcaption></figure>

When you want Tabnine to process and analyze user workspace content and connected repositories, turn this switch on. Read the explanatory text to confirm how data is encrypted and how content is kept within your organization.

After you enable Tabnine Context, allow up to an hour for the change to reach all users. Ask users to restart their IDEs if they want the change to apply immediately.

To manage Git repositories, scroll to the Git Repositories section on the same tab. Choose the relevant scope in the Team selector, for example “Org level repos”, to view or configure repositories for that level.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FufhutfPigoX0RsKSSXdU%2Funknown.png?alt=media&#x26;token=7bc8f017-efe4-4260-a0b5-4db838dc1477" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
As a reminder, when connecting repos, Tabnine indexes code snippets from them, becoming available to your team from Tabnine servers when using Tabnine.
{% endhint %}

To add a new Git repository, click the Add Repository button and follow the steps in the dialog. To find an existing repository, type part of its name in the “Search repository” field and select it from the results.

#### Perforce

To manage Perforce depots, scroll further down to the Perforce Depots section. Select the appropriate team scope and read the note describing how Tabnine indexes connected depots.

<figure><img src="https://3436682446-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FY2qxVf5VTm3fmwP4B4Gx%2Fuploads%2FOPPxxVj1ciVTkXaWloJn%2Funknown.png?alt=media&#x26;token=91633770-9793-4701-b0a8-ecb4819bd745" alt=""><figcaption></figcaption></figure>

If no Perforce servers are configured, look for the empty state message in this section. To connect a server, click the Connect a Perforce server button and complete the setup form with your Perforce settings.

Once you connect a Perforce server, enable the relevant depots according to your policy. After that, expect these depots to appear as data sources for Context Engine runs and assets.
