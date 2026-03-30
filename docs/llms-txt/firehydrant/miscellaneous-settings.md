# Source: https://docs.firehydrant.com/docs/miscellaneous-settings.md

# Miscellaneous Settings

<Table align={["left","left"]}>
  <thead>
    <tr>
      <th style={{ textAlign: "left" }}>
        Plans
      </th>

      <th style={{ textAlign: "left" }}>
        Required Permissions
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td style={{ textAlign: "left" }}>
        * All
      </td>

      <td style={{ textAlign: "left" }}>
        * `Manage Organization Settings`
      </td>
    </tr>
  </tbody>
</Table>

<Image align="center" alt="Miscellaneous Organization settings" border={false} caption="Miscellaneous Organization settings" src="https://files.readme.io/a44145a062837b92645b09603b91770dfa34d83ab730d717754d568f03168f2c-CleanShot_2025-03-26_at_18.34.10.png" width="650px" />

The following settings are enforced organization-wide and can be found in **Settings** > **General** > **Organization**.

* **Name** - The name of the organization. This will automatically be shown as part of the page header in your [Retrospective exports](https://docs.firehydrant.com/docs/preview-export-retrospectives).
* **Website** - Home page of your organization.
* **Logo** - A logo for your organization. This will automatically be shown as part of the page header in your [Retrospective exports](https://docs.firehydrant.com/docs/preview-export-retrospectives).
* **Enable Incident Priority** - Some users find Priority to be redundant to Severity. If so, you can disable Incident Priority.
* **Enable Weekly Email Summaries** - Individual users can configure whether or not they'd like to receive weekly incident summary emails in their [Profile Settings](https://docs.firehydrant.com/docs/profile-settings). However, this toggle will disable for the entire organization.
* **Force Time Zone** - Allows an organization to force and use the same timezone globally across the entire organization. This will affect all timestamps displayed every in the platform (although in the database, everything is still stored in UTC).
* **Enable Live Collaboration in Retrospectives** - The new [Retrospectives](https://docs.firehydrant.com/docs/intro-to-retrospectives) experience allows live collaboration and live cursors shown in certain types of questions (freeform text). This feature can be preemptively disabled if users don't need the feature or if it slows down performance with many users typing at the same time.