# Source: https://docs.ox.security/inventory-with-ox-bom/saas-bom.md

# SaaS BOM

{% hint style="success" %}
**At a glance:** Review a list of all SaaS services referenced by your code. Understand precisely how and where these services are used so you can efficiently change SaaS references when necessary.
{% endhint %}

{% hint style="warning" %}
See the list of currently supported [SaaS services](#supported-saas-services).
{% endhint %}

## Overview

<div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-6e00a5a95eb4e41c448c7574f9900c3a0020c614%2Fsaasbom.png?alt=media" alt=""><figcaption></figcaption></figure></div>

**SaaS BOM** provides you with a detailed inventory of the SaaS services referenced by your code, including:

* Name of the SaaS service and a link to its website
* Service category (for example, logging, messaging, ticketing, etc.)
* Repository (application) in which the reference was detected
* The way in which the SaaS service is referenced by your code and its precise location (file and line number)

{% hint style="info" %}
**Why does it matter?**

**Consider the following scenario:**\
Your development organization works in squads, developing app features independently. Some of these teams incorporate SaaS services into your code. These services work well in your product, helping it to process customer data more effectively and efficiently. However, because of the independent nature of your dev teams, there's no centralized list of the SaaS services referenced in your code.

Recently, a major SaaS provider experienced a data breach. If your code references that service, you need to act quickly to change your API tokens so that your customer data isn't compromised.

**With SaaS BOM, you have exactly the information you need:** Does your code reference that SaaS service? What are the precise locations in your code that need to be addressed?
{% endhint %}

## Using SaaS BOM

In the **summary table:**

* A specific SaaS service is listed **once for each application** in which it is detected.
* For a single application, multiple references to the same SaaS service are listed in a single row, with each location listed separately in the **Where found** column.
* Use the filters on the left side of the page to view specific information in the table according to your preferences.
* Click the <img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-ec0b73c8d2ef577d1ae1c36d63d758904adf186b%2Fexport_button.png?alt=media" alt="Export" data-size="line"> button to export the full or filtered table as a CSV file.
* Select a row to open detailed information at the bottom of the page, including a complete usage table in the **Where found** tab. \\

  <div align="left"><figure><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-e727167dd173823dff47b49be485a50267a69173%2Fsaasbom_where_found_tab.png?alt=media" alt=""><figcaption></figcaption></figure></div>

## Reference types detected

OX detects the following types of references to SaaS services in your code:

<table><thead><tr><th width="209">Reference type</th><th>Details</th></tr></thead><tbody><tr><td><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-457c92b616266f0d64b80b8385384aabe3012630%2Fdependency_icon.png?alt=media" alt=""> Dependency</td><td>SDK declared as an application dependency</td></tr><tr><td><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-7ea60cc375a9198ea3aaa4bd4633de0584ec62a9%2Fimport_icon.png?alt=media" alt=""> Import</td><td>SDK libraries imported into code in the files in which it will be used</td></tr><tr><td><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-0728451eca6579a5a6df490d514b070348ef0b94%2Fsdk_usage_icon.png?alt=media" alt=""> SDK usage</td><td>SDK libraries used in the code</td></tr><tr><td><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-94024f8dd025993efa5a467287aefeee1d608572%2Ftoken_icon.png?alt=media" alt=""> Token/secret</td><td>Token detected in the code</td></tr><tr><td><img src="https://884876233-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FdK3XMLdV8zRg847RmGmZ%2Fuploads%2Fgit-blob-65d46a1feac0613a7d81a81f6ac01d9925eee1a6%2Fdirect_reference_icon.png?alt=media" alt=""> Direct API call</td><td>Direct call to a SaaS API endpoint URL</td></tr></tbody></table>

## Supported SaaS services

OX detects the following SaaS services, with more added all the time:

{% embed url="<https://docs.google.com/spreadsheets/d/13DncuiSt4QVKAyc-kAxoIOba65GJcoDqiPYSlp12wrg/edit#gid=0>" fullWidth="false" %}
Scroll down to see more. Click [here](https://docs.google.com/spreadsheets/d/13DncuiSt4QVKAyc-kAxoIOba65GJcoDqiPYSlp12wrg/edit?usp=sharing) to open or download the full list.
{% endembed %}
