# Source: https://docs.getint.io/getintio-platform/settings/how-to-override-getint-behavior-using-custom-properties.md

# How to Override Getint Behavior Using Custom Properties

Custom properties in Getint give you the ability to tweak and adjust how Getint operates by default to match your specific needs. By utilizing these properties, you can boost both the functionality and flexibility of your integrations, ensuring they match your business processes.

{% hint style="warning" %}
Please note that this feature is only supported for Jira Data Center apps and Getint On-premise customers. This guide is not meant for Jira Software.
{% endhint %}

### Use Cases for Custom Properties <a href="#use-cases-for-custom-properties" id="use-cases-for-custom-properties"></a>

1. **Custom Workflows:** Override default behavior to support specific workflows and automate processes based on custom criteria.
2. **Enhanced Data Synchronization:** Customize how data is synchronized between systems by adding rules and conditions that reflect your business needs.
3. **Detailed Reporting:** Capture additional data points for more comprehensive reporting and analytics.

### How to Access Custom Properties <a href="#how-to-access-custom-properties" id="how-to-access-custom-properties"></a>

#### Jira Data Center <a href="#jira-data-center" id="jira-data-center"></a>

1. In the integration setup, go to **Settings** > **Custom Properties**.
2. Click on **Add Property** to define a new custom property.
3. Provide a name for the property and select the appropriate data type (e.g., text, number, date).
4. Specify any default values or conditions that need to be met for this property.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Fm2FIfZ0dqs7UnU74HnfT%2FJira%20DC%20Custom%20Properties.png?alt=media&#x26;token=e52789e3-4247-4088-a144-e9bd66afd252" alt=""><figcaption></figcaption></figure>

#### Getint On-Premise <a href="#getint-on-premise" id="getint-on-premise"></a>

1. In the integration setup, go to **System** > **Custom Properties**.
2. Click on **Add Property** to define a new custom property.
3. Provide a name for the property and select the appropriate data type (e.g., text, number, date).
4. Specify any default values or conditions that need to be met for this property.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FxIUDsjC6Kchalu1Oym4o%2FHow%20to%20access%20custom%20properties.png?alt=media&#x26;token=44d30994-6e59-4ea1-ae1a-550d9bf5638c" alt=""><figcaption></figcaption></figure>

### Configure These Properties Using Available Flags <a href="#configure-these-properties-using-available-flags" id="configure-these-properties-using-available-flags"></a>

Use available flags to determine how these properties should influence the integration behavior. For example, you can set conditions to trigger specific actions or override default flags based on the custom property values.

#### Values That Can Be Modified <a href="#values-that-can-be-modified" id="values-that-can-be-modified"></a>

1. `CLEAN_UP_MAX_RUNS`
   * How many runs Getint cleans up in one cleanup cycle.
2. `CLEAN_UP_INTERVAL_IN_HOURS`
   * How long Getint waits between cleanup cycles.
3. `CLEAN_UP_THREADS_COUNT`
   * The number of cleanup threads working in parallel.
4. `ENABLED_DETAILED_LOGGING`
   * Getint prints more detailed information about errors.
5. `MAX_NUMBER_OF_ITEMS_PER_RUN`
   * The maximum number of items that Getint can sync per run.
6. `MAXIMUM_AGE_OF_LOGS_IN_DAYS`
   * Duration for which Getint will keep sync data.
7. `FF_SKIP_COMMENTS_CREATED_BEFORE`
   * Comments created before a specific date (e.g., 2024-01-01) will be skipped during syncs.
8. `DO_NOT_STORE_BROKE_PIPELINE_SYNCS`
   * If set to true, Getint won't save information about items that failed to sync. Useful for saving storage and when filters are applied.
9. `MAX_HISTORY_CHANGES_PER_INTEGRATION_SUITE`
   * Controls how many integration changes are stored in Getint (default: 20).

#### Specific Flags for Data Cleanup <a href="#specific-flags-to-data-cleanup" id="specific-flags-to-data-cleanup"></a>

1. `CLEAN_UP_INTERVAL_IN_HOURS`
   * Interval in hours for cleanup (default: 4).
2. `NUMBER_OF_RUNS_TO_CLEAN_UP`
   * The number of runs to clean per cleanup cycle (default: 500). Getint performs 10 cycles per cleanup, removing 5.000 runs of data per cleanup.

#### Specific Flag to Show Stack Traces

`LOG_STACK_TRACE` is a **boolean** custom property that controls whether advanced scripting errors write full stack traces to logs, and it is disabled by default.

{% hint style="info" %}
**Available for**: On-Premise, Jira Data Center, and Cloud deployments.
{% endhint %}

* By default, stack traces are not shown in regular logs or advanced scripting logs to avoid exposing stack traces in regular logs
* When `LOG_STACK_TRACE` is set to true, advanced scripting errors can include stack traces in the log output.
* To enable the property, add a new entry with the following details:
  * **Property Name**: `LOG_STACK_TRACE`
  * **Property Value**: `true`

#### Specific Flag for Retry Logic Configuration

Retry logic is a **configurable** exponential backoff mechanism for Jira, Salesforce, and ServiceNow that also refreshes OAuth tokens mid-run, starting from specific connector versions.

**Purpose**

* Reduce failed syncs caused by Atlassian, Salesforce, or ServiceNow API rate limits and temporary outages.
* Allow customers to tune retry behavior per environment using custom properties, based on their own traffic profile and vendor limits.
* Minimize duplicate records and partial runs by applying controlled retries with exponential backoff.

**Jira and Salesforce Configuration**

Use the following custom properties to control the retry policy for Jira and Salesforce:

* `JIRA_RETRY_LOGIC_CONFIG`
* `SALESFORCE_RETRY_LOGIC_CONFIG`

Example configuration:

```
JIRA_RETRY_LOGIC_CONFIG
{
  "ENABLED": "true",
  "INITIAL_WAIT_MS": "500",
  "MAX_WAIT_MS": "15000",
  "MAX_ATTEMPTS": "4",
  "MULTIPLIER": "2"
}

SALESFORCE_RETRY_LOGIC_CONFIG
{
  "ENABLED": "true",
  "INITIAL_WAIT_MS": "500",
  "MAX_WAIT_MS": "15000",
  "MAX_ATTEMPTS": "4",
  "MULTIPLIER": "2"
}
```

**Parameter Details**:

* `ENABLED`: Turns retry logic on or off.
* `INITIAL_WAIT_MS`: Initial wait time before the first retry attempt (e.g., 500 ms = 0.5 s).
* `MAX_WAIT_MS`: Maximum wait time between retries (e.g. 15000 ms = 15 s).
* `MAX_ATTEMPTS`: Maximum number of retry attempts for a single request.
* `MULTIPLIER`: Factor used to increase the delay between subsequent attempts (e.g., 2 = doubles the wait time each retry).

**ServiceNow Configuration**

For ServiceNow, use the `SNOW_RETRY_LOGIC_CONFIG` custom property (available since v1.98):

```
SNOW_RETRY_LOGIC_CONFIG
{
  "ENABLED": "true",
  "INITIAL_WAIT_MS": "500",
  "MAX_WAIT_MS": "15000",
  "MAX_ATTEMPTS": "4",
  "MULTIPLIER": "2"
}
```

Behavior is equivalent to the Jira/Salesforce retry property:

* Enables retries on transient errors (e.g., 429, 503).
* Uses the same exponential backoff parameters (`ENABLED, INITIAL_WAIT_MS, MAX_WAIT_MS, MAX_ATTEMPTS, MULTIPLIER`).

**OAuth Token Refresh Behavior**

* When `JIRA_RETRY_LOGIC_CONFIG`, `SALESFORCE_RETRY_LOGIC_CONFIG`, or `SNOW_RETRY_LOGIC_CONFIG` is enabled, the connector can refresh the OAuth token in the middle of a run.
* This reduces failures caused by access tokens expiring during long-running synchronizations.

{% hint style="danger" %}
Monitor external service quotas like Salesforce API limits closely. Persistent 429 responses indicate fundamental capacity issues—retries provide temporary relief but won't bypass plan restrictions, so review your vendor tier or optimize sync frequency/volume instead.
{% endhint %}

#### Save and Test the Configuration <a href="#save-and-test-the-configuration" id="save-and-test-the-configuration"></a>

1. Once you have configured the custom properties, save the settings.
2. Test your integration(s) to ensure that the custom properties are correctly influencing how Getint operates.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FXMdc9phmD6dJzFaXidhe%2FAdding%20a%20custom%20property.png?alt=media&#x26;token=a7d19849-aa84-443e-9aef-5bda1d578826" alt=""><figcaption></figcaption></figure>

### Support and Assistance <a href="#support-and-assistance" id="support-and-assistance"></a>

Our support team is available to provide guidance and assistance with configuring custom properties and overriding integration behaviors. For any questions or support needs, don’t hesitate to reach out to us [here.](https://getint.io/help-center)

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
