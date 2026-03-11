# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6125.md

# What's New in Axonius 6.1.25

#### Release Date: July 28th 2024

These Release Notes contain new features and enhancements added in version 6.1.25.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

* Axonius adds and updates adapters and enforcement actions all the time. Follow [Ongoing updates to adapters and enforcement actions in Axonius 6.1](/docs/axonius-61-ongoing-adapter-and-enforcement-action-updates).

## Assets Pages

The following features were added to all assets pages:

### Inline Editing to Add Values to Custom Fields

It is now possible to use inline editing to assign a value to an empty Custom Field directly from an Assets page table. This is in addition to the already existing capability to modify a Custom Field value using inline editing.

## Administrator Settings New Features and Enhancements

The following updates were made to various Administrator settings:

### Connectivity to Legacy Cypher Suites

The new option in [Certificate Settings](/docs/certificate-settings)**Allow legacy cipher suites** allows adapter connectivity to systems that support only legacy ciphers. This option is only available for customer hosted on-premise instances.

### Preferred Fields

* The following preferred fields were added to the system showing the earliest and latest values for the last and first seen, to help query on the latest/earliest seen from all adapters:
  * Preferred Latest Last Seen

  * Preferred Latest Last Seen (agents)

  * Preferred Earliest First Seen

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

### Dynamic Value Statement Updates

The following updates were made to the Dynamic Value statement functionality:

#### Dynamic Value Statement Simulator

The new **Simulator** tool enables users to debug Dynamic Value Statements. The [Dynamic Value Statement Simulator](/docs/using-the-simulator) simplifies the process of identifying and rectifying issues in statements, which despite successful syntax validation, yield unexpected results, often due to data type incompatibilities.

![SimulateDynamicStatement](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SimulateDynamicStatement.png)

The user clicks  **Simulate** to enter **Simulator Mode**, hovers over a phrase in the statement, and the Simulator immediately executes on the asset selected by the system, presenting the statement's behavior in terms of field type, input type, and value. Users can also select their own test asset using the **Replace** arrows, enabling them to test various scenarios.
In the screen below, the **set-value** phrase is simulated on an asset, and the result is **Single Value Integer 24**.

![SimulatorExample](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/SimulatorExample.png)