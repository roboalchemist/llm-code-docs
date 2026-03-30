# Source: https://docs.fiddler.ai/integrations/data-platforms-and-pipelines/data-platforms/bigquery-integration.md

# BigQuery

### Integrating Fiddler with BigQuery

Learn how to connect Fiddler's ML monitoring platform with your BigQuery data to enable comprehensive model tracking and analysis. This guide covers:

* Using BigQuery data to onboard models in Fiddler
* Loading baseline datasets from BigQuery tables
* Monitoring production data by connecting BigQuery to Fiddler

#### Prerequisites:

* A Google Cloud account with BigQuery access
* Fiddler account [credentials](https://app.gitbook.com/s/82RHcnYWV62fvrxMeeBB/reference/settings#credentials)
* [Python Client SDK](https://app.gitbook.com/s/rsvU8AIQ2ZL9arerribd/fiddler-python-client-sdk) installed

### Configure BigQuery Access

Before importing data, you'll need to set up BigQuery API access and authentication:

1. In the GCP platform, Go to the navigation menu -> click APIs & Services. Once you are there, click + Enable APIs and Services (Highlighted below). In the search bar, enter BigQuery API and click Enable.

![GCP APIs & Services dashboard with the Enable APIs and Services button highlights.](https://1800696242-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fkcq97TxAnbTVaNJOQHbQ%2Fuploads%2Fgit-blob-e947b5ae31e6a6fb613c34306115b7d3c4daa4b8%2F75ca647-screen-shot-2022-05-19-at-12633-pm.png?alt=media)

![BigQuery API landing page highlighting the Try This API button and showing the API as enabled.](https://1800696242-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fkcq97TxAnbTVaNJOQHbQ%2Fuploads%2Fgit-blob-5c99aebd5363ac056b073df393284715cc6e3421%2F3dd5deb-screen-shot-2022-05-19-at-33343-pm.png?alt=media)

2. In order to make a request to the API enabled in Step #1, you need to create a service account and get an authentication file for your Jupyter Notebook. To do so, navigate to the Credentials tab under APIs and Services console and click Create Credentials tab, and then Service account under dropdown.

![APIs & Services credentials landing page showing the Credentials left navigation link and the Create Credentials button highlighted.](https://1800696242-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fkcq97TxAnbTVaNJOQHbQ%2Fuploads%2Fgit-blob-8091f1249364a3978dd8afe5042bf97357bd6b7a%2Fea63eca-screen-shot-2022-05-19-at-33424-pm.png?alt=media)

3. Enter the Service account name and description and click Done. You can use the BigQuery Admin role under Grant this service account access to the project. You can now see the new service account under the Credentials screen. Click the pencil icon beside the new service account you have created and click Add Key to add auth key. Please choose JSON and click CREATE. It will download the JSON file with auth key info. (Download path will be used to authenticate)

![Showing Keys tab of the new service account and the create private key model for example account "fiddler" with JSON key type option selected.](https://1800696242-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2Fkcq97TxAnbTVaNJOQHbQ%2Fuploads%2Fgit-blob-9944d42c3d0d70b98e0b5945e44b2dfb20f53041%2F662315e-screen-shot-2022-05-19-at-33924-pm.png?alt=media)

### Connect to BigQuery Data

Set up your Python environment and connect to BigQuery:

1. Install Required Packages

```bash
pip install google-cloud google-cloud-bigquery[pandas] google-cloud-storage
```

2. Configure Authentication

```python
# Set environment variables for your notebook
import os
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'path/to/your/auth-key.json'
```

3. Initialize BigQuery Client

```python
# Imports google cloud client library and initiates BQ service
from google.cloud import bigquery
bigquery_client = bigquery.Client()
```

4. Query Your Data

```python
# Example query to fetch baseline data
query = """
SELECT * FROM `fiddler-bq.fiddler_test.churn_prediction_baseline` 
"""

# Execute query and load into pandas DataFrame
baseline_df = bigquery_client.query(query).to_dataframe()
```

#### Next Steps

Now that you've connected BigQuery to Fiddler, you can:

1. [Onboard a model](https://app.gitbook.com/s/jZC6ysdlGhDKECaPCjwm/client-library-reference/model-onboarding/create-a-project-and-model) using the baseline dataset for the model schema inference sample.
2. [Upload a Baseline dataset](https://app.gitbook.com/s/jZC6ysdlGhDKECaPCjwm/client-library-reference/publishing-production-data/creating-a-baseline-dataset), which is optional but recommended for monitoring comparisons.
3. [Publish production events](https://app.gitbook.com/s/jZC6ysdlGhDKECaPCjwm/client-library-reference/publishing-production-data) for continuous monitoring.
