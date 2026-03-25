# Source: https://docs.axonius.com/docs/automox-run-worklet-per-asset.md

# Automox - Run Worklet per Asset

**Automox - Run Worklet per Asset** runs an Automox worklet for each asset that matches the parameters of the saved query supplied as a trigger (or from the assets selected in the asset table).

This removes the need to have a domain admin account on all your systems for WMI ECS. It also allows you to leverage the recipes you already have in Automox.

See [Creating Enforcement Sets](/docs/create-ec-set) to learn more about adding Enforcement Actions to Enforcement Sets.

<Callout icon="📘" theme="info">
  Note

  * Not all asset types are supported for all Enforcement Actions.
  * See Actions supported for [Activity Logs, Adapters Fetch History, and Asset Investigation modules](/docs/creating-queries-filters#using-activity-log-adapter-fetch-history-asset-investigation-and-findings-queries-in-enforcement-actions).
  * See Actions supported for [Aggregated Security Findings](https://docs.axonius.com/docs/vulnerabilities#using-aggregated-security-findings-queries-in-enforcement-actions).
  * See Actions supported for [Software](software#using-software-queries-in-enforcement-actions).
</Callout>

<br />

## General Settings

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.
* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Worklet ID** - the ID of the worklet

## APIs

Refer to [ How we Worklet:](https://www.automox.com/blog/winning-worklets-on-demand) for information on how to get the API key.

## Required Permissions

The value supplied in [User name](#parameters) must have permissions to run a worklet.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).