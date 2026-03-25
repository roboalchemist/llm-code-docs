# Source: https://docs.axonius.com/docs/whats-new-in-axonius-606.md

# What's New in Axonius 6.0.6

#### Release Date: October 29th 2023

These Release Notes contain new features and enhancements added in version 6.0.5 and 6.0.6.

* Read [What's New in Axonius 6.0](/docs/whats-new-in-axonius-600) to see all Axonius 6.0 features.

* Axonius adds and updates adapters and enforcement actions all the time. Follow [ongoing updates to adapters and enforcement actions in Axonius 6.0](/docs/axonius-60-ongoing-adapter-and-enforcement-action-updates).

## Assets Pages

The following features were added to all assets pages:

#### Tags Supported for Asset Investigation

It is now possible to use [**Asset Investigation**](/docs/advanced-asset-investigation#tags-on-asset-investigation) to track changes made to tags on the system. Support of tags in Asset Investigation means that a user  can track when a tag is added or removed from an asset, whether this is done manually, or using an [Enforcement Action](/docs/add-remove-tag).

#### Data Refinement Supported for Date Fields

* Data refinement is now supported for date fields.

**Export CSV Include Associated Devices**
When [Export CSV](/docs/exporting-devices-data-to-csv) is created from the **Vulnerabilities** or **Software**  page, an option is now available to include the associated devices. When this option is selected, the user can then choose the device fields to include in the CSV file.

## Vulnerability Management Module New Features and Enhancements

The following new features and enhancements were added to the Vulnerability Management Module:

### Unique Devices

The [total number of unique devices](/docs/vulnerabilities) on which Vulnerabilities were found is now shown above the table.

## Software Management Module New Features and Enhancements

The following new features and enhancements were added to the Software Management Module:

### Unique Devices

The total number of [unique devices](/docs/software) on which **Software** was found is now shown above the table.

## Asset Graph New Features and Enhancements

The following new features and enhancements were added to the **Asset Graph**:

### Viewing the Asset Graph on a Single Asset Doesn't Expand

When viewing the [Asset Graph](/docs/asset-graph#accessing-the-asset-graph) of a single asset from the Asset page, the asset node of the single asset remains unexpanded.

### Using Enforcement Actions from the Asset Graph

You can now create new Enforcement Actions and run existing Enforcement Actions from the [Asset Graph](/docs/asset-graph).

### Color Coding of Icons for Asset Types

The icons for the different asset types shown in the [Asset Graph](/docs/asset-graph) are now color coded.

<Image alt="AssetGraphColors.png" width="500px" src="https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/AssetGraphColors.png" />

## Query Management New Features and Enhancements

The following new features and enhancements were added to the Queries:

### Source IP Added to Query History Page

The Source IP Address was added to the [Query History](/docs/viewing-query-history) page. This is the IP address that ran this query.

## Adapter Pages and Adapter Interface New Features and Enhancements

The following updates were made to the common functionality across all adapters:

### Adapter Interface

#### On Demand Cleanup for Adapters

It is now possible to run [cleanup for a single adapter](/docs/advanced-settings#Running-cleanup-manually) manually.

#### Custom Adapter Value

New Adapter Advanced Setting added called **[Custom Adapter Value](/docs/advanced-settings#custom-adapter-value)**. This is a value that the user defines that will be displayed as part of every entity fetched from the adapter as an added field on the asset called **Custom Adapter Value**.

## Administrator Settings New Features and Enhancements

The following updates were made to various Administrator settings:

### Enterprise Password Management settings

**Tunnel Support Added to the Following Enterprise Password Managers**
Added capability to select the tunnel through which to connect to the following Enterprise Password Managers under Enterprise Password Management Settings.

* Akeyless Vault
* Click Studios Passwordstate
* Thycotic Secret Server

**New Enterprise Password Manager**

**[1Password Connect Server](/docs/1password-connect-server)**

### Unique IDP Field is Persistent in SAML Configurations

When configuring [SAML parameters](/docs/saml-based-login-settings) for multiple SSO providers, the IDP field where each provider is named, remains visible but disabled once the configuration is saved.

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

### Dynamic Value Statement Updates

The following updates were made to the Dynamic Value statement functionality:

* **not\_contains Operator**

  * New *[not\_contains](/docs/enforcement-action-condition-syntax-table)* operator added to Dynamic Value Statements.