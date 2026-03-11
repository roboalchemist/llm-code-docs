# Source: https://docs.axonius.com/docs/axonius-enrich-physical-location.md

# Axonius - Enrich Physical Location

**Axonius - Enrich Physical Location** enriches devices returned by the selected query or selected on the relevant asset page with their full addresses, based on longitude and latitude data.

<Callout icon="📘" theme="info">
  Note

  This action is supported for Devices only.
</Callout>

## Required Fields

These fields must be configured to run the Enforcement Set.

* **Action name** - The name of this Enforcement Action. The system sets a default name. You can change the name.

* **Configure Dynamic Values** *(optional)* - Toggle on to enter a Dynamic Value statement. See [Creating Enforcement Action Dynamic Value Statements](https://docs.axonius.com/docs/config-ec-conditions) to learn more about Dynamic Value statement syntax.

* **Longitude** - Select the adapter field from which to fetch longitude information.

* **Latitude** -  Select the adapter field from which to fetch latitude information.

* **Compute Node**  - The Axonius node to use when connecting to the specified host. For more details, see [Working with Axonius Compute Nodes](https://docs.axonius.com/docs/connecting-additional-axonius-nodes).

<Callout icon="📘" theme="info">
  Note

  The enriched address information will appear for each device under the **Physical Location** field.
</Callout>

## APIs

Axonius uses [Nominatim](https://nominatim.org/), an open-source geocoding service, to provide address information based on the longitude and latitude values received from the adapter fields.

***

For more details about other enforcement actions available, see [Action Library](/docs/action-library).