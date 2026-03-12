# Source: https://docs.statsig.com/statsig-warehouse-native/guides/sdks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Working With the SDK

Warehouse Native Works with any of Statsig's SDKs for logging events and getting feature flags or experiment assignments.

This page is a brief overview of how Warehouse Native works with Statsig's SDKs.
Refer to the [client](../../client/introduction) or [server](../../server/introduction) SDK docs for help setting up SDKs.

## Data Forwarding

When you first set up your data connection, Statsig will create tables to forward datasets to, and generate an assignment/metric sources which includes any user-level metadata fields you log as part of your evaluation.

You can find the configuration for these datasets and the table we create/output data to in the advanced section of the warehouse connection page.

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/y4LPJ9r3dQ39KuxK/images/whn/data_forwarding_whn.png?fit=max&auto=format&n=y4LPJ9r3dQ39KuxK&q=85&s=5b09b71cd181f619aa28a4bdbfe0f5ae" alt="Choose Groups" width="3018" height="1650" data-path="images/whn/data_forwarding_whn.png" />
</Frame>

## Exposures

Statsig calculates deduplicated first-exposure rollups for you on a daily basis and exports that miniaturized dataset to your warehouse. Additionally, on every Pulse load on the first day of a experiment, deduplicated exposures for the day will be exported to your warehouse in near real-time, up to 1 million exposures.

## Log Events

You can also use Statsig's powerful event logging to send events to the Statsig SDK and have them later exported to your warehouse for analysis.


Built with [Mintlify](https://mintlify.com).