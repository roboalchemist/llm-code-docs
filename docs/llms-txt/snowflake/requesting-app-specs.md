# Source: https://docs.snowflake.com/en/developer-guide/native-apps/requesting-app-specs.md

# Overview of app specifications

This topic describes how a provider can configure a Snowflake Native App to use
app specifications to request controlled access from consumers. App specifications
allow consumers to review and approve or decline requests for the following
actions:

* Connections to external endpoints outside of Snowflake
* Authentication with third-party services
* Data sharing with other Snowflake accounts

## Types of controlled access for Snowflake Native Apps

Snowflake Native Apps often need to interact with resources beyond the consumer’s Snowflake account.
These interactions can include connecting to external services, authenticating with third-party
providers, or sharing data with other Snowflake accounts.

To access external services and share data, Snowflake provides the following objects:

External access integrations:
:   Allow secure access to external network endpoints within a user-defined function or stored
    procedure. External access integrations use network rules to restrict access to specific external
    network locations.

Security integrations:
:   Allow secure access to third-party authentication providers such as OAuth. Security integrations
    provide secure authentication and access control.

Shares and listings:
:   Allow apps to share data back to providers or third-party Snowflake accounts.
    Shares contain database objects to be shared, and listings provide the
    mechanism to share data across accounts and regions.

When using [automated granting of privileges](requesting-auto-privs.md), an
app has the required privileges to create these objects when running the setup
script. However, because these objects enable external connections or data
sharing, consumers must approve these operations when configuring the app.

Using automated granting of privileges with app specifications has the following benefits:

* Consumers do not have to manually create integrations, shares, or listings required by the app
  and approve access to them using references.
* Providers do not have to write code that checks for the existence of the required privileges and
  objects during installation or upgrade.
* Consumers have clear visibility and control over external connections and data sharing requests.

## Use app specifications for consumer approval

App specifications allow you to specify what controlled access the app
requires. After the consumer installs the app, they review the app specification and
approve or decline each request as necessary. This includes requests for external connections,
authentication integrations, and data sharing permissions.

* For information about using app specifications to request access to external
  endpoint access, see [Request external access integrations (EAIs) with app specifications](requesting-app-specs-eai.md).
* For information about
  using app specifications to request access to OAuth integrations, see
  [Request security integrations with app specifications](requesting-app-specs-sec-integ.md).
* For information about using app specifications to share data through listings, see
  [Request data sharing with app specifications](requesting-app-specs-listing.md).

## App specification definition

An app specification definition contains the properties that are required for the app to perform
controlled operations such as external connections or data sharing. These properties are displayed
to the consumer for approval. The app specification definition contains a subset of the metadata and
properties specific to each type of operation: external access integration, security integration, or listing.

For information about the app specification definition for security integrations, see
[App specification definition for security integrations](requesting-app-specs-sec-integ.md).

For information about the app specification definition for external access integrations, see [App specification definition for an EAI](requesting-app-specs-eai.md).

For information about the app specification definition for listings, see [Create an app specification for a listing](requesting-app-specs-listing.md).

## Sequence numbers of an app specification

The sequence number is similar to a version number for the app specification. Sequence numbers
are automatically incremented when a provider changes the definition of the app specification.
The definition of an app specification includes configuration details and other required information.
Fields that are not part of the definition, such as `description`, do not trigger an update to the
sequence number.

Sequence numbers allow providers and consumers to identify different versions of an app specification.
For example, if a provider adds a new configuration detail to the app specification definition,
the sequence number is incremented. When the consumer views the app specification, they can see that
the sequence number has changed, and they can review the updated app specification.

## Best practices when using app specifications

[Automated granting of privileges](requesting-auto-privs.md) ensures that the app has the required
privileges to create objects like external access integrations, security integrations, or listings. However,
consumers can choose to decline the app specification that enables external connections or data sharing.
When developing an app, you must account for situations where app specifications might not be approved.

Consider the following scenarios:

* An app might request multiple network ports for an external access integration, but the consumer might
  allow only one. The app should include logic to handle errors that occur if a network port is not available.
* A data sharing request might be declined or only partially approved for some target accounts but not others.
  The app should gracefully handle these cases.
* Authentication integrations might be rejected, requiring the app to use
  alternative methods.

As a best practice, always include proper error handling and provide clear feedback to consumers about
which features require approved specifications to function.

## Using callback functions with app specifications

In some contexts, an app might need to know when the consumer has approved or declined an
app specification. For example:

* The app might need to wait until an external access specification is approved before making API calls.
* Data population might need to start only after a listing specification is approved.
* OAuth flows might need to be initialized after security integration approval.

To handle this situation, the Snowflake Native App Framework provides a mechanism that allows provider to define a callback
stored procedure that runs when the consumer approves or declines an app specification.

Providers can add a stored procedure to the manifest file as shown in the following example:

```yaml
lifecycle_callbacks:
  specification_action: callbacks.on_spec_update
```

This example shows how to add a stored procedure named `callbacks.on_spec_update` to the manifest
file. In the setup script, providers can add a stored procedure as shown in
the following example:

```sqlexample
CREATE OR REPLACE PROCEDURE callbacks.on_spec_update (
  name STRING,
  status STRING,
  payload STRING)
  ...
```

This example shows the signature of a stored procedure called `callbacks.on_spec_update`.
You include the code in the body of this procedure to check the status of the app specification, create objects, and perform actions as required.
