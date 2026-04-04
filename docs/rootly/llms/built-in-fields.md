# Source: https://docs.rootly.com/configuration/built-in-fields.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.rootly.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Built In Fields

> Manage Rootly's pre-configured incident fields including services, severity, environment, and teams to capture essential incident metadata.

# **Overview**

Rootly comes with a series of built-in incident properties that are carefully selected to meet common incident characterization requirements. These properties are used to provide incidents with additional metadata so teams can dynamically trigger automations and run metrics reports based on these properties. Please see the [Incident Properties](/configuration) page to learn more about them.

You can access the Built-In Fields page by navigating to **Configurations >  Fields > Built-in-fields**

<img src="https://mintcdn.com/rootly/RUi0EYcf6x_7UXYC/images/CleanShot2025-08-20at13.47.26@2x.png?fit=max&auto=format&n=RUi0EYcf6x_7UXYC&q=85&s=f4a26bed91bd555ea9eadf497d0ae73d" alt="Clean Shot2025 08 20at13 47 26@2x Pn" width="3454" height="1974" data-path="images/CleanShot2025-08-20at13.47.26@2x.png" />

# Managing Built-In Fields

## Enable/Disable Field

Only enabled fields are considered to be live fields - meaning they can appear on UI screens and be updated during incidents. Disabled fields are NOT usable during incidents and cannot be updated by workflows either.

You can use the toggle switch next to the field name to enable/disable it.

<Frame>
    <img src="https://mintcdn.com/rootly/R81sNIO9rI160XHL/images/built-in-fields/3.webp?fit=max&auto=format&n=R81sNIO9rI160XHL&q=85&s=34b8a035e49dfdae8635f2040c2bc924" alt="Document image" width="867" height="219" data-path="images/built-in-fields/3.webp" />
</Frame>

## Edit Field

You can edit a specific field by clicking on the edit icon on the right-hand side of the field.

Once selected, you will see an Edit Form Field pane open. From here, you'll be able to edit how this particular field appears in the forms.

<img src="https://mintcdn.com/rootly/RUi0EYcf6x_7UXYC/images/CleanShot2025-08-20at13.49.35@2x.png?fit=max&auto=format&n=RUi0EYcf6x_7UXYC&q=85&s=905f1cc401fd21bfe8e050c382b49e9d" alt="Clean Shot2025 08 20at13 49 35@2x Pn" width="3456" height="1980" data-path="images/CleanShot2025-08-20at13.49.35@2x.png" />

<AccordionGroup>
  <Accordion title="ID">
    This is an unique identifier for the form field. It is automatically generated for you upon field creation and cannot be edited. This `id` will be used to reference the specific form field in API calls and Liquid syntaxes.
  </Accordion>

  <Accordion title="Name">
    This field is auto generated for built-in fields and can be edited. The name entered here will be the value that appears on user-facing forms. However, it will NOT alter the Liquid syntax used to reference this property.

    For example, if you set this field to `ENV`, it will be reflected in the forms. However, when you go to reference it using Liquid syntax, it would still be `{{incident.environments[0]}}`.
  </Accordion>

  <Accordion title="Field Type">
    Depending on the built-in field being referenced, you can alter its field type. If the built-in field is an array of values (e.g. Services, Environments, etc.), you can change the field type to either a simple `Select` or `Multiple Select` type. For example, if you want to enforce that users can only select a single `Incident Type`, then you can update the `Incident Type` field to be a `Select` field type.

    Not all built-in fields can have customizable field types. For example a checkbox field (e.g. `Backfill Incident` toggle, `Mark as Triage` toggle) can only be that type.
  </Accordion>

  <Accordion title="Default">
    Built-in fields can be configured to have a default value. For example, if you want all your incidents to default to `SEV4` for the `Severity` field, then you can set it here.
  </Accordion>

  <Accordion title="Enabled">
    Only enabled fields are considered to be live fields - meaning they can appear on UI screens and be updated during incidents. Disabled fields are NOT usable during incidents and cannot be updated by workflows either.

    You can use the toggle switch next to the field name to enable/disable it.

    <Note>
      This is the same setting as the toggle described in the **Enable/Disable Field** section above
    </Note>
  </Accordion>

  <Accordion title="Display This Field in the Incident Details">
    This switch allows you to display or hide the specific field on the **Details** section of the **Incident Details** page.

    <Note>
      **Hiding a field** from being displayed in the **Details** section **does not mean this field is turned off**. It just means users cannot edit it from the UI.

      This is typically used when teams want to configure a custom flag that gets systematically set by workflows, not manually by users.
    </Note>
  </Accordion>
</AccordionGroup>


Built with [Mintlify](https://mintlify.com).