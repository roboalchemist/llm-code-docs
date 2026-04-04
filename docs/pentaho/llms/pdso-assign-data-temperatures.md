# Source: https://docs.pentaho.com/pdc-10.2-data-optimizer/pdso-use-data-storage-optimizer/pdso-assign-data-temperatures.md

# Assign data temperatures

Use **Check Data Temperature** to check the domain and classification of the files in the data source that you want to optimize.

To perform rules-based tiering or purging, Data Optimizer requires a specific domain name and business terms within a hierarchy. If the domain and terms do not exist, you must create them in Data Catalog:

* Create a domain named `Data Temperature`.
* Create business terms within that domain. Data temperature terms can be used to identify the usage and age of your data. You may want to consider the data temperature examples, below, when creating or assigning terms:

{% hint style="info" %}
You must use the Data Temperature domain, but you can choose different terms to better fit your environment or workflow. A category is not required.
{% endhint %}

<table><thead><tr><th width="178">Data temperature</th><th>Criteria</th></tr></thead><tbody><tr><td><code>Boiling</code></td><td>Regularly searched, regularly read, created less than 180 days ago, and with a last modified date of less than 30 days.</td></tr><tr><td><code>Hot</code></td><td>Frequently searched, frequently read, created less than 366 days ago, and with a last modified date of less than 90 days.</td></tr><tr><td><code>Warm</code></td><td>Frequently searched, less frequently read, created less than 366 days ago, and with a last modified date of less than 180 days.</td></tr><tr><td><code>Cold</code></td><td>Rarely searched, rarely read, created more than 366 days ago, and with a last modified date of more than 366 days.</td></tr><tr><td><code>Frozen</code></td><td>Never searched, never read, created more than 732 days ago, and with a last modified date of more than 732 days.</td></tr></tbody></table>

Click **Check Data Temperature** to open the Business Glossary in Data Catalog. To add a domain or term, click **Add New**. See [Manage Business Glossary in Data Catalog](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/pdc-manage-business-glossary-administer-pdc) for details.
