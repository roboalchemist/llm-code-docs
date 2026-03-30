# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6012.md

# What's New in Axonius 6.0.12

#### Release Date: December 10th 2023

These Release Notes contain new features and enhancements added in versions 6.0.11 and 6.0.12.

* Read [What's New in Axonius 6.0](/docs/whats-new-in-axonius-600) to see all Axonius 6.0 features.

* Axonius adds and updates adapters and enforcement actions all the time. Follow [ongoing updates to adapters and enforcement actions in Axonius 6.0](/docs/axonius-60-ongoing-adapter-and-enforcement-action-updates).

## Query Management New Features and Enhancements

The following new features and enhancements were added to the Queries:

### Export/Import Queries

It is now possible to [export and import queries](/docs/importing-and-exporting-queries) using the Axonius User Interface, from the Queries page.

## Reports New Features and Enhancements

The following enhancements were added to reports.

**New Report Editor**

Use the new [Report Editor](/docs/report-configuration-page) drawer for a more streamlined experience for creating and editing reports.

## Administrator Settings New Features and Enhancements

The following updates were made to various Administrator settings:

### Role-based Access Control (RBAC)

**Connect to Data Scopes in a Streamlined Way**
You can now easily [move between Data Scopes](/docs/data-scope-management) in a streamlined manner for easier management of data scopes. Click on the avatar and then **Connect To**. Select a Data Scope from the list.

### Azure Authentication Added to Email Settings

Azure Authentication (using MS Graph API), was added was added as an option under 'SMTP Authentication Type' for [Email Settings](/docs/configuring-email-settings#azure-authentication).

### SAML Configuration Examples Updated

The following examples for using SAML for Single Sign-on were updated:

* [SAML Based Authentication with Okta](/docs/example-saml-based-authentication-with-okta)

* [SAML Based Authentication with Microsoft Entra ID](/docs/example-saml-based-authentication-with-azure-active-directory) - Includes instructions on how to download the PEM format certificate.

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

### Dynamic Value Statement Updates

The following update was made to the Dynamic Value statement functionality:

* **unique Function** - The new [unique](/docs/using-functions-and-keywords#using-the-unique-function-for-array-fields) function can be used in a Dynamic Value statement to remove all duplicate elements in a list (array) and keep only the  unique values. Its syntax is: **unique** (\[list field]).