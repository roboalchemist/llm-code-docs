# Source: https://docs.axonius.com/docs/discovery-cycle.md

# Discovery Cycle

Axonius runs a periodic automatic  global discovery cycle  that consists of several phases to pull and correlate the data from all adapters. The **[global discovery cycle](/docs/configuring-discovery-settings)** schedule (for example, every 12 hours) is determined based on the system [Lifecycle Settings](/docs/lifecycle-settings-overview).

You can also manually initiate a new global discovery cycle by clicking **Discover Now** on the top right corner of any page.  The **Discover Now** button is only visible once one  adapter is connected.

The latest global discovery cycle status is displayed in the **[System Lifecycle](/docs/system-lifecycle-chart)** chart. The chart also displays the following details:

* The number of hours until the next automatic discovery cycle starts.
* The last discovery cycle's start and end timestamps.
* The duration of the cycle.

<Image alt="AxoniusDashboard_Nov24" border={false} src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AxoniusDashboard_Nov24.png" />

<br />

<Callout icon="📘">
  Note:

  Axonius also lets you configure individual discovery cycles for specific adapters and for specific adapter connections.

  * **Adapter custom cycle** – This cycle includes only the following phases:
    * Fetch Assets / Scanner Assets
    * Clean
    * Correlation

  * **Connection custom cycle** – This cycle includes only the following phases:
    * Fetch Assets / Scanner Assets

  For more details, see [Adapter Discovery Configuration](/docs/adapter-discovery-configuration).
</Callout>

## Global Discovery Cycle Phases

The global discovery cycle (automatic and manual) consists of several sequenced phases:

1. **Fetch Adapter Assets**
   * Data is pulled from all adapter connections, except for adapters of vulnerability  assessment tools, and the Axonius adapter used for tickets.

<Callout icon="📘" theme="info">
  Note

  * Adapters configured with a custom cycle are skipped.

  * Adapter connections configured with a custom cycle are skipped.
</Callout>

2. **Fetch Scanner Assets**
   * Data is pulled from all adapter connections of vulnerability assessment tools.
   * Devices that have the same IP address and have no other unique identifier (no hostname, MAC address, etc.) are correlated together.

<Callout icon="📘" theme="info">
  Note

  * Adapters configured with a custom cycle are skipped.

  * Adapter connections configured with a custom cycle are skipped.
</Callout>

3. **Clean Assets**
   * "Old" devices and other asset entities (excluding tickets) are cleaned and deleted. The definition of "old" asset entity may be different for each adapter, and determined based on the following adapter advanced setting:
     * [Delete devices and other assets that have not been returned from the source in the last X hours](/docs/advanced-settings#delete-devices-and-other-assets-that-have-not-been-returned-from-the-source-in-the-last-x-hours)
   * Then, "old" users asset entities are cleaned and deleted. The definition of "old" asset entity may be different for each adapter, and determined based on the following adapter advanced setting:
     * [Delete users that have not been returned from the source in the last X hours](/docs/advanced-settings#delete-users-that-have-not-been-returned-from-the-source-in-the-last-x-hours)

<Callout icon="📘" theme="info">
  Note

  * Tickets are linked to an Axonius pseudo adapter and not to the adapter connections of their linked assets.
  * Adapters configured with a custom cycle are skipped.
  * You can also run [adapter cleanup manually](/docs/advanced-settings#Running-cleanup-manually) for a single adapter.
</Callout>

* **Clean Tickets**
  * Cleans tickets that have been opened for assets that are no longer seen by their vendor adapter. This means that tickets, which have no links to assets existing in the system, are cleaned and deleted.

4. **Pre-Correlation**
   * [‘Equals’](/docs/query-wizard-and-query-filter#8-value-field) values list is calculated.
   * [Cloud Asset Compliance rules](/docs/cloud-asset-compliance-overview) are implemented, if enabled.
5. **Correlation**
   * The correlation engine runs and correlates relevant assets together.
6. **Post-Correlation**

   * User-device  associations are created.
     * **Last Used Users** field is populated on devices with the user names associated with each device.
     * **Last Used Users \[XXXX]** fields (for example, Last Used Users Email, Last Used Users Departments, and more) are populated based on the user fields and data of the **Last Used Users** associated with each device.
     * User assets are enriched with 'Associated Devices'.
     * Later you can query devices based on the associated user name or user department.
   * Preferred fields are recalculated.
   * Custom enrichment runs.
   * Enforcement sets scheduled to run at the end of each discovery cycle are executed.
   * Enforcement sets whose scheduled start times fell on the time that the discovery cycle was already running, but have the **Wait until cycle ends** option enabled, are executed now.
   * [Field Mapping](/docs/managing-field-mapping) Enforcement sets are triggered in the Post-Correlation phase of the Discovery Cycle after all other Enforcement sets runs have concluded, but continue running asynchronously outside the Discovery Cycle. This enables the Discovery Cycle to proceed to the next phase before the Field Mapping Enforcement set runs are completed.
   * Findings rules are run.
   * Reports are generated.
7. **Save Historical**
   * Historical collected data is saved, based on the [Historical Snapshot Scheduling Settings](/docs/configuring-retention-settings#setting-historical-snapshot-scheduling).
   * Historical data can be used in the dashboard, in the asset pages, and in the **Users** page to show insights on historical data.

<Callout icon="📘" theme="info">
  Note

  * If historical snapshot data has been configured to be saved at a specific time and not at the end of a discovery cycle, this phase is skipped.
</Callout>

* Vulnerabilities details are enriched from the vulnerability enrichments such as NIST National Vulnerabilities Database (NVD), CISA, EPSS (Exploit Prediction Scoring System) etc.