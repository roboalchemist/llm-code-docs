# Source: https://doc.keepnetlabs.com/next-generation-product/platform/threat-intelligence.md

# Threat Intelligence

This guide explains the Threat Intelligence product and how to use it.

This includes:

* What is Threat Intelligence?
* How to export a list of breached accounts?

## What is Threat Intelligence?

The **Threat Intelligence** product scans the web, searching for signals and data that may represent a breach of your data security and a threat to your business. The constant vigilance afforded to you by the Threat Intelligence product shortens the time between the potential data breach and defensive response, reducing the opportunity for fraudulent activity.

In the Threat Intelligence product, you can check for data leaks for your previously allowed email domains in the **Domain** **Allowlist** menu.

Please find the documentation for the domain allowlist [here](https://doc.keepnetlabs.com/next-generation-product/platform/company/company-settings/allowed-domains).

Go to the **Threat Intelligence** menu from the left menu on the dashboard to review the following functions.

## **Breached Accounts**

This table contains all breached email accounts. This table includes information such as breached account, the source of the breach, the password type of the email account, and the leak date.&#x20;

The components of the **Breached Accounts** page are explained in the table below.

<table><thead><tr><th width="129.5"></th><th></th></tr></thead><tbody><tr><td>Breached Account</td><td>Information about the breached email account is located in this column.</td></tr><tr><td>Source</td><td>This column shows from which source the account was leaked or under what name it was leaked.</td></tr><tr><td>Password Type</td><td>Indicates the status of the password information contained in the data leak. eg. Cleartext, hash, MD5, etc.</td></tr><tr><td>Leak Date</td><td>This column shows the information about the date when the data leak was disclosed.</td></tr></tbody></table>

## Table Actions

You can take manual actions on breached accounts table. You can click the buttons top of the data table for the appropriate steps you want to perform.

<table><thead><tr><th width="130.5"></th><th></th></tr></thead><tbody><tr><td>Download</td><td>The list of the breached accounts can be downloaded. You can click the button to download all pages or the current page and download the data in the table in XLSX, CSV and PDF formats.</td></tr><tr><td>Refresh</td><td>By clicking this button, you can reload the page and view it if new data has been added.</td></tr><tr><td>Table Settings</td><td>With the table settings button, you can show and hide the columns or freeze the columns.</td></tr><tr><td>Sorting</td><td>According to which column you want to sort, you can change the order when you click on the relevant column heading.</td></tr></tbody></table>

## Video Tutorial

This tutorial explains the Threat Intelligence product and how to use it.

{% embed url="<https://youtu.be/uj_hEFv0lFc>" %}

## FAQ

### Q: Can I delete breached account from the platform?

A: No, you can only list, copy to clipboard and download the list of the breached accounts.

### Q: Can I integrate the breached accounts with my SOAR products by obtaining the details using the API?

A: You can perform almost every operation in the Threat Intelligence product using API. You can refer to our Rest API document to see the details.
