# Source: https://docs.jfrog.com/artifactory/docs/monitor-the-distribution-service.md

# Monitor the Distribution Service

Administrators can monitor the status of all active and previous distribution operations, including the size and duration of the operation. This capability lets you see which distributions are currently in progress, which are pending an Xray scan, and which have been completed.

**To access the Distribution service monitor:**

1. In the **Administration** module, select **Monitoring > Distribution Status**.
2. Select one or more distribution targets from the **Target** list and click **Apply**. The table is updated with the information for the selected targets.
3. Select one of the following tabs:

   * **Active**: Contains information about currently active distribution operations.
   * **History**: Contains information about previous distribution operations.

### Active Distributions Table

<Image align="center" alt="Hezi_distribution-tracker_in-progress.png" border={false} width="70% " src="https://files.readme.io/00bae0571eca0fcef3f65a815688311ddf4098964455000fca0beadb8c858130-uuid-dc8ecfae-03a7-1114-ae08-6aed13132f9f.png" />

When the **Active** tab is selected, the table includes the following information about each active distribution:

<Table>
  <thead>
    <tr>
      <th>
        Column
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Name
      </td>

      <td>
        The name of the Release Bundle.
      </td>
    </tr>

    <tr>
      <td>
        Version
      </td>

      <td>
        The Release Bundle version.
      </td>
    </tr>

    <tr>
      <td>
        Project
      </td>

      <td>
        The <Anchor label="project" target="_blank" href="/projects/docs/projects">project</Anchor> associated with the Release Bundle.
      </td>
    </tr>

    <tr>
      <td>
        Action
      </td>

      <td>
        The action that was performed (Distribute or Delete).
      </td>
    </tr>

    <tr>
      <td>
        Target
      </td>

      <td>
        The distribution target.

        If the Release Bundle was distributed to multiple targets (for example, multiple Edge nodes), a line for each target is added to the table.
      </td>
    </tr>

    <tr>
      <td>
        Duration
      </td>

      <td>
        The total duration since the request was initiated.
      </td>
    </tr>

    <tr>
      <td>
        Status
      </td>

      <td>
        The current status of the operation. Possible statuses include:

        * **Storing Release Bundle**
        * **In queue**
        * **Pending Xray scan results** (relevant for users who have <Anchor label="JFrog Xray" target="_blank" href="/security/docs/xray">JFrog Xray</Anchor> installed)
        * **In progress**
        * **Finalizing distribution**
        * **Not distributed**
        * **Abort in progress**
      </td>
    </tr>

    <tr>
      <td>
        Size
      </td>

      <td>
        The number of artifacts included in the distribution and their total size.
      </td>
    </tr>
  </tbody>
</Table>

### Distribution History Table

<Image align="center" alt="Hezi_distribution-tracker_history-tab.png" border={false} width="70% " src="https://files.readme.io/3c5ff845636e3ab5e661eda6d5df9e17841359256a8a0f7d9b75335b33aa9fec-uuid-2f1c9e44-f8dc-7066-cb52-1343c6d0233b.png" />

To view the table containing the history of previous distribution operations, click the **History** tab and select the desired timeframe from the **Time** list (the default is the past 24 hours). The table includes the following information about each distribution:

<Table>
  <thead>
    <tr>
      <th>
        Column
      </th>

      <th>
        Description
      </th>
    </tr>
  </thead>

  <tbody>
    <tr>
      <td>
        Name
      </td>

      <td>
        The name of the Release Bundle.
      </td>
    </tr>

    <tr>
      <td>
        Version
      </td>

      <td>
        The Release Bundle version.
      </td>
    </tr>

    <tr>
      <td>
        Action
      </td>

      <td>
        The action that was performed (Distribute or Delete).
      </td>
    </tr>

    <tr>
      <td>
        Target
      </td>

      <td>
        The distribution target.

        If the Release Bundle was distributed to multiple targets (for example, multiple Edge nodes), a line for each target is added to the table.
      </td>
    </tr>

    <tr>
      <td>
        Started
      </td>

      <td>
        The timestamp of when the operation began.
      </td>
    </tr>

    <tr>
      <td>
        Duration
      </td>

      <td>
        The total duration of the operation.
      </td>
    </tr>

    <tr>
      <td>
        Status
      </td>

      <td>
        The final status of the operation. Possible statuses include:

        * **Completed**

        * **Failed**

        * **Aborted**

        * **Partially aborted**

        <Callout icon="✅" theme="okay">
          **Tip**

          If the distribution failed, hover above the information icon to see details about the error that caused the failure.
        </Callout>
      </td>
    </tr>
  </tbody>
</Table>

### Viewing Distribution Details

Click anywhere on the row in the distribution table to view the following details about the operation:

* The name of the person who performed the operation.
* The list of distributed artifacts, including:

  * Artifact name
  * Artifact type
  * Target location
  * Size
  * SHA-256
    ![](https://files.readme.io/2ecc87d30ac36d1630c6a28c364d073dcea5c2398d85b14daf3ff199d877f6fd-uuid-b99099cb-103c-3090-12fd-4857c54c1902.png)