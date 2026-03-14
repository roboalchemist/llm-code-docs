# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/custom-data-and-custom-card-configuration/quickfind-with-custom-data-configuration-and-rules.md

# Quickfind with Custom Data – Configuration and Rules

### Setting a Custom field as Searchable <a href="#a-setting-a-custom-field-as-searchable-adding-a-short-code" id="a-setting-a-custom-field-as-searchable-adding-a-short-code"></a>

You can set a [custom data field](https://docs.enate.net/enate-help/builder/builder-2021.1/custom-data-and-custom-card-configuration/creating-custom-data-fields) to be an explicit search field as part of the configuration when [creating Custom Data items](https://docs.enate.net/enate-help/builder/builder-2021.1/custom-data-and-custom-card-configuration) in Builder.&#x20;

To do this, when you are creating / editing custom data fields, make sure to select the ‘Searchable’ flag option.

{% hint style="info" %}
Note that currently, only the following data types can be set as searchable in Quickfind:

* Short Text
* List (not multiple-level lists)
  {% endhint %}

### Adding a Short Code <a href="#a-setting-a-custom-field-as-searchable-adding-a-short-code" id="a-setting-a-custom-field-as-searchable-adding-a-short-code"></a>

You then need to enter a short code. This is a text character that can be entered by users in [Quickfind ](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/quickfind)in order to search for work items with this field. The short code will also be added to the [Quickfind list](https://docs.enate.net/enate-help/work-manager/work-manager-2021.1/quickfind/quickfind-searches-with-custom-data-fields) in Work Manager.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-MWYnDNwe3Cuo4zlGbs5%2F-MWpixQQ-XB_sHNapfgn%2F-MWprR-gpJCwkQHvurdO%2Fimage.png?alt=media\&token=2a321d7f-4927-4811-a2ed-95ce49ac974c)

You can specify up to two characters, but they must be unique in the system. They are case insensitive, so it does not matter whether you / the end users enter in upper or lower case when using.

{% hint style="info" %}
Note that the following short codes are reserved for standard system usage and therefore cannot be entered here:

* r: work item reference number
* ‘RE:’ and ‘FW:’ (as this may impact searching against titles which come from emails subjects)
* Further shortcodes are reserved for *future* system usage: T, S, SD, DD, ED, AU, OU and RD.
  {% endhint %}

Click ‘OK’ to save changes.&#x20;

### **Default Short Code for a User** <a href="#default-short-code-for-a-user" id="default-short-code-for-a-user"></a>

You are able to set one of the short codes in the list to be your default short code. If a short code is selected, this will mean that you will not have to input the prefix (e.g. ‘p:’ before the search text).
