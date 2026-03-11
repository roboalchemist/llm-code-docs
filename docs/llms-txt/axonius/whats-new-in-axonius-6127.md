# Source: https://docs.axonius.com/docs/whats-new-in-axonius-6127.md

# What's New in Axonius 6.1.27

#### Release Date: August 11th 2024

These Release Notes contain new features and enhancements added in version 6.1.27.

* Read [**What's New in Axonius 6.1**](/docs/whats-new-in-axonius-610) to see all Axonius 6.1 features.

* Axonius adds and updates adapters and enforcement actions all the time. Follow [Ongoing updates to adapters and enforcement actions in Axonius 6.1](/docs/axonius-61-ongoing-adapter-and-enforcement-action-updates).

## Assets Pages

The following features were added to  assets pages:

### Devices

#### New Last Used Users Complex Association Field for Devices

The new 'Last Used Users' field displays data for the users associated with a given device.

## Users and Groups Pages New Features and Enhancements

The following new features and enhancements were added to the **Users** and **Groups** pages.

### Create User Action

It is now possible to create one or more selected users in a third-party vendor directly from the **Users** page using the [**Create User** action](/docs/devices-actions#create-user). When this action is selected, it is possible to select a 'Create User' Enforcement Action and to fill in the fields required to run the Enforcement Action that creates the selected users in the third-party vendor. It is also possible to click **Advanced** to navigate to the Enforcement Set configuration and fill in additional configuration.

![CreateUserActioninDD](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CreateUserActioninDD.png)

### Create Group Action

It is now possible to create one or more selected groups in a third-party vendor directly from the **Groups** page using the [**Create Group** action](/docs/devices-actions#create-group). When this action is selected, it is possible to select a 'Create Group' Enforcement Action and fill in the fields required to run the Enforcement Action that creates the selected groups in the third-party vendor. It is also possible to click **Advanced** to navigate to the Enforcement Set configuration and fill in additional configuration.
![CreateGroupActioninDD](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/CreateGroupActioninDD.png)

## Administrator Settings New Features and Enhancements

The following updates were made to various Administrator settings:

### Updates to Enrichment Settings

'Don’t create new users from WMI devices' is now default system behavior, and the system setting for this was removed.

### Include Specific Fields in Data Scopes

The capability has been added to include specific fields when configuring [Data Scopes](/docs/data-scope-management#creating-a-data-scope). This gives granular control over what data is available to users with access to a particular Data Scope.
![DataScope-IncludeFields.png](https://raw.githubusercontent.com/Axonius/ax-docs-pub/refs/heads/main/Images/DataScope-IncludeFields.png)

## Enforcement Center New Features and Enhancements

The following new features and enhancements were added to the Enforcement Center:

### Dynamic Value Statement Updates

The following updates were made to the Dynamic Value statement functionality:

#### New Functions

The following functions can now be used in a Dynamic Value statement:

* **regex\_extract**
  * The new [*regex\_extract*](/docs/using-functions-and-keywords#using-the-regexextract-function) function extracts from 'adapter.field' the part of the string that matches regex\_expression so that it can be used to populate Custom Fields or Tags.\
    Syntax: **regex\_extract** (*\[adapter.field], regexexpression*)
    For example: **device all then form.tag\_name set\_value regex\_extract (\[device.specific\_data.data.name], "demo")**
    When an asset name returned from the query includes the string "demo", it places that string in a tag.
* **to\_date**
  * The new [*to\_date*](/docs/using-functions-and-keywords#using-the-todate-function) function converts the results of a date calculation (epoch date in milliseconds) to a date in human-readable Date format.
    Syntax: **to\_date**(number of milliseconds)
    For example: **to\_date(add(now(),2592000000))**
    **add (now(),2592000000)** adds 2592000000 milliseconds (**30** days) to the value of the current epoch date (in milliseconds) resulting in the epoch date 30 days later. The *to\_date* function converts the epoch date into Date format.