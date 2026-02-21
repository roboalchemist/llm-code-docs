# Source: https://airflow.apache.org/docs/apache-airflow-providers-microsoft-azure/stable/index.html

Title: apache-airflow-providers-microsoft-azure — apache-airflow-providers-microsoft-azure Documentation

URL Source: https://airflow.apache.org/docs/apache-airflow-providers-microsoft-azure/stable/index.html

Markdown Content:
apache-airflow-providers-microsoft-azure package[¶](https://airflow.apache.org/docs/apache-airflow-providers-microsoft-azure/stable/index.html#apache-airflow-providers-microsoft-azure-package "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

[Microsoft Azure](https://azure.microsoft.com/)

Release: 12.10.3

Provider package[¶](https://airflow.apache.org/docs/apache-airflow-providers-microsoft-azure/stable/index.html#provider-package "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------

This package is for the `microsoft.azure` provider. All classes for this package are included in the `airflow.providers.microsoft.azure` python package.

Installation[¶](https://airflow.apache.org/docs/apache-airflow-providers-microsoft-azure/stable/index.html#installation "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------

You can install this package on top of an existing Airflow installation via `pip install apache-airflow-providers-microsoft-azure`. For the minimum Airflow version supported, see `Requirements` below.

Requirements[¶](https://airflow.apache.org/docs/apache-airflow-providers-microsoft-azure/stable/index.html#requirements "Link to this heading")
-----------------------------------------------------------------------------------------------------------------------------------------------

The minimum Apache Airflow version supported by this provider distribution is `2.11.0`.

| PIP package | Version required |
| --- | --- |
| `apache-airflow` | `>=2.11.0` |
| `apache-airflow-providers-common-compat` | `>=1.13.0` |
| `adlfs` | `>=2023.10.0` |
| `azure-batch` | `>=8.0.0` |
| `azure-cosmos` | `>=4.6.0` |
| `azure-mgmt-cosmosdb` | `>=3.0.0` |
| `azure-datalake-store` | `>=0.0.45` |
| `azure-identity` | `>=1.3.1` |
| `azure-keyvault-secrets` | `>=4.1.0` |
| `azure-mgmt-datalake-store` | `>=0.5.0` |
| `azure-mgmt-resource` | `>=2.2.0` |
| `azure-storage-blob` | `>=12.26.0` |
| `azure-mgmt-storage` | `>=16.0.0` |
| `azure-storage-file-share` | `>=12.7.0` |
| `azure-servicebus` | `>=7.12.1` |
| `azure-synapse-spark` | `>=0.2.0` |
| `azure-synapse-artifacts` | `>=0.17.0` |
| `azure-storage-file-datalake` | `>=12.9.1` |
| `azure-kusto-data` | `>=4.1.0,!=4.6.0,!=5.0.0` |
| `azure-mgmt-datafactory` | `>=2.0.0` |
| `azure-mgmt-containerregistry` | `>=8.0.0` |
| `azure-mgmt-containerinstance` | `>=10.1.0` |
| `msgraph-core` | `>=1.3.3` |
| `msgraphfs` | `>=0.3.0` |
| `microsoft-kiota-http` | `>=1.9.4,<2.0.0` |
| `microsoft-kiota-serialization-json` | `>=1.9.4` |
| `microsoft-kiota-serialization-text` | `>=1.9.4` |
| `microsoft-kiota-abstractions` | `>=1.9.4,<2.0.0` |
| `microsoft-kiota-authentication-azure` | `>=1.9.4,<2.0.0` |
| `msal-extensions` | `>=1.3.0` |

Cross provider package dependencies[¶](https://airflow.apache.org/docs/apache-airflow-providers-microsoft-azure/stable/index.html#cross-provider-package-dependencies "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Those are dependencies that might be needed in order to use all the features of the package. You need to install the specified provider distributions in order to use them.

You can install such cross-provider dependencies when installing from PyPI. For example:

pip install apache-airflow-providers-microsoft-azure[amazon]

| Dependent package | Extra |
| --- | --- |
| [apache-airflow-providers-amazon](https://airflow.apache.org/docs/apache-airflow-providers-amazon) | `amazon` |
| [apache-airflow-providers-common-compat](https://airflow.apache.org/docs/apache-airflow-providers-common-compat) | `common.compat` |
| [apache-airflow-providers-oracle](https://airflow.apache.org/docs/apache-airflow-providers-oracle) | `oracle` |
| [apache-airflow-providers-sftp](https://airflow.apache.org/docs/apache-airflow-providers-sftp) | `sftp` |

Downloading official packages[¶](https://airflow.apache.org/docs/apache-airflow-providers-microsoft-azure/stable/index.html#downloading-official-packages "Link to this heading")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

You can download officially released packages and verify their checksums and signatures from the [Official Apache Download site](https://downloads.apache.org/airflow/providers/)

*   [The apache-airflow-providers-microsoft-azure 12.10.3 sdist package](https://downloads.apache.org/airflow/providers/apache_airflow_providers_microsoft_azure-12.10.3.tar.gz) ([asc](https://downloads.apache.org/airflow/providers/apache_airflow_providers_microsoft_azure-12.10.3.tar.gz.asc), [sha512](https://downloads.apache.org/airflow/providers/apache_airflow_providers_microsoft_azure-12.10.3.tar.gz.sha512))

*   [The apache-airflow-providers-microsoft-azure 12.10.3 wheel package](https://downloads.apache.org/airflow/providers/apache_airflow_providers_microsoft_azure-12.10.3-py3-none-any.whl) ([asc](https://downloads.apache.org/airflow/providers/apache_airflow_providers_microsoft_azure-12.10.3-py3-none-any.whl.asc), [sha512](https://downloads.apache.org/airflow/providers/apache_airflow_providers_microsoft_azure-12.10.3-py3-none-any.whl.sha512))
