# Source: https://docs.axonius.com/docs/whats-new-in-axonius-613.md

# What's New in Axonius 6.1.3

#### Release Date: February 25th 2024

These Release Notes contain new features and enhancements added in version 6.1.3

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

* Axonius adds and updates adapters and enforcement actions all the time. Follow [Ongoing updates to adapters and enforcement actions in Axonius 6.1](/docs/axonius-61-ongoing-adapter-and-enforcement-action-updates).

## Assets Pages

The following features were added to all assets pages:

### Asset Investigation

Support for the following fields was added to [**Asset Investigation**](/docs/advanced-asset-investigation):

**Devices:**

* Airwave: Last AP
* Airwave: SSID
* Cisco ARP: Switch PORT

### Query Wizard Enhancements

### AND NOT and OR NOT Operators  in  More Query Types

Users can select AND NOT and OR NOT operators for  child expressions in Asset Entity (ENT) and Complex (OBJ) Queries.

## Administrator Settings New Features and Enhancements

The following updates were made to various Administrator settings:

**Set default Adapters page view as list**
Added a setting on [GUI>UI](/docs/configuring-user-interface-settings) to set whether the Adapters page is displayed as a list by default rather than tile view.

### User Name in SAML Configurations can be Case Insensitive

The ability has been added to ignore case sensitivity in the [SAML](/docs/saml-based-login-settings) account user name. This prevents duplicate accounts from being created when an existing user connects with an account where their user name is in a different case than the already existing account.

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

### Enhancements to Axonius Actions

\####[**Axonius - Send Email**](/docs/send-email)
It is now possible to send an email from a sender other than the one configured in the **Sender address** in [Email Settings](/docs/configuring-email-settings)(or if empty, the default sender address).