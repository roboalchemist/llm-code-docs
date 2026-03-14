# Source: https://virustotal.readme.io/docs/consumption-quotas-handled.md

# How consumption quotas are handled

VirusTotal Intelligence quotas are monthly. All Intelligence quota consumption metrics are reset at 00:00 UTC  on the 1st of the month.

API quotas have 3 limits:

* Per minute.
* Daily.
* Monthly.

When you have reached your API quota, API requests will respond with 204 (API v2) or 429 (API v3)

To find your current quota usage click on the "API key" link on the menu under your username or visit <https://www.virustotal.com/gui/my-apikey>

![My API key link on the menu](https://storage.googleapis.com/vtdocresources/guides/faq/img/quotashandled_menu_20231128.png)

On your API key page, you can fin your quota allowances, and you can click on an specific day to view more details.

![My API key link on the menu](https://storage.googleapis.com/vtdocresources/guides/faq/img/quotashandled_consumption_20231121.png)

<br />

In the case of a group's API key you will find two columns:

* Consumption by endpoint for the specific date you select. Endpoints not consuming quota will be tagged accordingly.
* Consumption by users where there is a line per user.

![](https://files.readme.io/06f4a5a3eb16572da5245d2c3e578aea75806dbfa4023d6a0d843aed92c43c7a-image.png)

Daily API quotas are reset every day at 00:00 UTC.  If you have a monthly API quota, it is reset at 00:00 UTC  on the 1st of the month.