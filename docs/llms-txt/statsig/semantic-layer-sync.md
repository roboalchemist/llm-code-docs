# Source: https://docs.statsig.com/statsig-warehouse-native/configuration/semantic-layer-sync.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Semantic Layer Sync

If you have centrally defined metrics, Statsig offers the ability to sync its data sources and metrics as part of your data version management workflow. Using Statsig's [Console API](/console-api/metrics) you can automatically sync changes you make to the matching definitions on Statsig, and you can optionally make the metrics read-only in the Statsig console.

We have a demonstration [GitHub repository](https://github.com/statsig-io/semantic_layer) that utilizes [a script](https://github.com/statsig-io/semantic_layer/blob/main/.github/scripts/statsig_sync.py) executed by [a GitHub Action](https://github.com/statsig-io/semantic_layer/blob/main/.github/workflows/statsig_sync.yml). This setup automatically synchronizes changes to .yml files located in the /metrics or /metric\_sources directories in the repo. This means that whenever you create or update these files, the script either updates existing metrics or metric sources in Statsig or creates new ones accordingly.

To use this example template, follow these steps:

1. Fork [this repository](https://github.com/statsig-io/semantic_layer) to get started.
2. In your forked repository, add your Statsig Console API Key to GitHub Secrets.
3. Tailor the metric definitions to align with your data needs.
4. Verify the automation by modifying relevant files and observing the triggered GitHub Action.

## Detailed Guide

### Forking the Repository

1. **Fork this repository** to create a copy in your GitHub account. <Frame><img width="1056" alt="Untitled" src="https://mintcdn.com/statsig-4b2ff144/DbEV6mNxirwT8Ol0/images/statsig-warehouse-native/configuration/semantic-layer-sync/79652104-6e13-467a-b4ef-dbbac83e15c9.png?fit=max&auto=format&n=DbEV6mNxirwT8Ol0&q=85&s=833a789bb7bafac14fac261d530439e1" data-path="images/statsig-warehouse-native/configuration/semantic-layer-sync/79652104-6e13-467a-b4ef-dbbac83e15c9.png" /></Frame>

### Adding the Statsig Console API Key

2. Navigate to `Settings > Secrets and variables > Actions` in your repository settings. Create a new secret named `STATSIG_API_KEY` with your Statsig Console API key as its value. This key facilitates authentication with the Statsig Console API for the synchronization process. <Frame><img width="1168" alt="Untitled" src="https://mintcdn.com/statsig-4b2ff144/x9lB50RxemB9ncWp/images/statsig-warehouse-native/configuration/semantic-layer-sync/0a627a98-3772-4c36-89d1-7587e3950e84.png?fit=max&auto=format&n=x9lB50RxemB9ncWp&q=85&s=23a08e8953c4069aff69651ee4e24d5e" data-path="images/statsig-warehouse-native/configuration/semantic-layer-sync/0a627a98-3772-4c36-89d1-7587e3950e84.png" /></Frame>

### Customizing Metric Definitions

3. Metric definitions reside within the `./metrics` directory, and metric source definitions are found in the `./metric_sources/` directory. To customize:

   * Utilize the Statsig Console API to fetch an existing **metric\_source** or **metric** using GET requests for [metric sources](/console-api/metrics#post-/metrics/metric_source/-name-) and [metrics](/console-api/metrics#get-/metrics/-metric_id-).
   * Remove the provided example metrics and metric sources, and replace them with your definitions in `./metric_sources/*.yml` and `./metrics/*.yml`.

*Note:* For enhanced readability, we modified `metric.warehouseNative[]` to `metric.metricDefinition[]` in our examples. You can see this change [here](https://github.com/statsig-io/semantic_layer/blob/1611a68703caf18d7fa32088ff06d568d8b3b03a/.github/scripts/statsig_sync.py#L38). Feel free to adjust the translations or revert to using `metric.warehouseNative[]` in your definitions.

### Verifying Automation

4. To test, edit a metric or metric source description in your repository. This action should trigger the GitHub Action, visible under the `Actions` tab. The process will then either create or update your metrics and metric sources in Statsig based on the repository's semantic definitions.

<Frame>
  <img width="1043" alt="Untitled" src="https://mintcdn.com/statsig-4b2ff144/x9lB50RxemB9ncWp/images/statsig-warehouse-native/configuration/semantic-layer-sync/2dcf8961-3591-4021-88fe-984994177f35.png?fit=max&auto=format&n=x9lB50RxemB9ncWp&q=85&s=cf03768005be9495523808e5f9975a1a" data-path="images/statsig-warehouse-native/configuration/semantic-layer-sync/2dcf8961-3591-4021-88fe-984994177f35.png" />
</Frame>

<Frame>
  <img width="1041" alt="Untitled" src="https://mintcdn.com/statsig-4b2ff144/x9lB50RxemB9ncWp/images/statsig-warehouse-native/configuration/semantic-layer-sync/04a084d6-ef6c-4b3f-aee9-41663ed47a60.png?fit=max&auto=format&n=x9lB50RxemB9ncWp&q=85&s=2bbdfe24c018dc06fd45d98335e026db" data-path="images/statsig-warehouse-native/configuration/semantic-layer-sync/04a084d6-ef6c-4b3f-aee9-41663ed47a60.png" />
</Frame>

<Frame>
  <img width="1031" alt="Untitled" src="https://mintcdn.com/statsig-4b2ff144/x9lB50RxemB9ncWp/images/statsig-warehouse-native/configuration/semantic-layer-sync/4442dd9d-313f-4b16-a978-59513e4e8469.png?fit=max&auto=format&n=x9lB50RxemB9ncWp&q=85&s=5ceaa2f64e08ea7155059fb1c5b33390" data-path="images/statsig-warehouse-native/configuration/semantic-layer-sync/4442dd9d-313f-4b16-a978-59513e4e8469.png" />
</Frame>

<br />

This example serves as a basic template. We encourage testing and further development to meet production standards. Please share any feedback or improvements you've made to this workflow with our support team, your sales contact, or in our [Slack community](https://statsig.com/slack). Thank you for any contributions!


Built with [Mintlify](https://mintlify.com).