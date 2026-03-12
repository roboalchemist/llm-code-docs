# Source: https://docs.pentaho.com/pdc-10.2-install/install-pentaho-data-catalog.md

# Install Pentaho Data Catalog

Pentaho Data Catalog is a powerful solution for data discovery, data cataloging, and data governance. Installing Data Catalog in your environment enables you to manage structured and unstructured data using intelligent automation and machine learning, while laying the groundwork for advanced features like Pentaho Data Optimizer (PDO) and Pentaho Data Mastering (PDM) if licensed.

This guide helps you install Data Catalog and its optional components across various deployment scenarios, ranging from a single-node server to a distributed, containerized environment. You can also deploy Remote Workers to support scalable and secure metadata processing across different network zones.

## What’s included with installation

When you install Data Catalog, the following are also installed (based on your license):

* **Pentaho Data Optimizer (PDO)**: Automates intelligent data tiering to object storage.
* **Pentaho Data Mastering (PDM)**: Enables advanced data mastering and curation workflows.

{% hint style="info" %}
To access the appropriate release package, Pentaho provides specific credentials along with a URL download link. These credentials grant you access to download the required package for your server. For more information, contact [Pentaho support](https://support.pentaho.com/hc/en-us).
{% endhint %}

To install Data Catalog, see the following topics:

* [components-reference](https://docs.pentaho.com/pdc-10.2-install/install-pentaho-data-catalog/components-reference "mention")
* [install-docker](https://docs.pentaho.com/pdc-10.2-install/install-pentaho-data-catalog/install-docker "mention")
* [install-data-catalog](https://docs.pentaho.com/pdc-10.2-install/install-pentaho-data-catalog/install-data-catalog "mention")

To install and configure a remote worker, see [install-and-configure-a-remote-worker](https://docs.pentaho.com/pdc-10.2-install/install-pentaho-data-catalog/install-and-configure-a-remote-worker "mention").

For Data Catalog upgrade instructions, see [upgrade-data-catalog](https://docs.pentaho.com/pdc-10.2-install/install-pentaho-data-catalog/upgrade-data-catalog "mention") and to upgrade to a patch version, see [upgrade-data-catalog-to-a-patch-version](https://docs.pentaho.com/pdc-10.2-install/install-pentaho-data-catalog/upgrade-data-catalog/upgrade-data-catalog-to-a-patch-version "mention").

For cloud-based deployments, see [hyperscalers](https://docs.pentaho.com/pdc-10.2-install/install-pentaho-data-catalog/hyperscalers "mention").

{% hint style="info" %}
Use the Chrome browser to access the PDC user interface after installation. Default users are available for demo environments. For production environments, it is strongly recommended to create your own user accounts and disable default credentials.
{% endhint %}

For more help or access to downloads, visit the [Pentaho Support Portal](https://support.pentaho.com/).

## Additional Resources

* For advanced setup and custom configurations, see the [Advanced configuration](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/ldc-advanced-configuration-ut_cp "mention") section in the [Administer Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/cUaDtyTop3vo8cjqgjGk/).
* For help with common issues, refer to the [Troubleshooting Pentaho Data Catalog](https://app.gitbook.com/s/cUaDtyTop3vo8cjqgjGk/pdc-troubleshooting-cp-ag "mention") section in the [Administer Pentaho Data Catalog](https://app.gitbook.com/o/PtpmPYUKgAsUWgv8SVUt/s/cUaDtyTop3vo8cjqgjGk/).
