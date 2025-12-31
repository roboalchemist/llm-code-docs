# Source: https://docs.aporia.com/api-reference/code-based-metrics.md

# Code-Based Metrics

Code-based metrics allow users to define Pyspark-based metrics that allow for computation on raw data, element-wise operations, and support third-party libraries.

In the following guide we will explain how one can use code-based metrics in Aporia to gain higher flexibility on the metric’s calculation.

<figure><img src="https://691195388-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMGlr0qI6TBrhv4rIjaKP%2Fuploads%2FfvmFwqpDdKhIuWVb3WCW%2Fimage.png?alt=media&#x26;token=08671c4c-4ab4-477b-be31-cc81e6536f48" alt=""><figcaption></figcaption></figure>

## Building the metric code

A code-based metric in Aporia gets a Pyspark data frame as an input and should return a numeric value/NaN as an output. Similar to custom metrics, code-based metrics are defined for a specific model and can be used with all versions/datasets/segments of that model.

Let's take a look at the following example:

```python
import numpy as np

def calc_metric(df):
	"""
	My function simply returns the average age, but I can do whatever calculation
  	I wish with the data frame
	"""
	return np.average(df.collect().columns.age)
```

Supported libraries can be found below.

Code-based metrics are calculated at the same frequency of all other calculation jobs as specified by your model's aggregation period. The code-based metric will be calculated on the following data frames:&#x20;

1. all data over your model's retention period (you can filter this data to a specific time period)
2. all segments (separately) over your model's retention period (you can filter this data to a specific time period)

{% hint style="info" %}
Performance wise, it is best practice to perform the calculation on top of the Pyspark data frame rather than collecting it first using `df.collect()`
{% endhint %}

## Registering your metric

Once you have your metric ready, you can register it to the relevant Aporia model. Below you will find example code to help you get started:

```python
import requests
from http import HTTPStatus

ACCOUNT = <<comlete your account ID>>
WORKSPACE = <<complete your workspace ID>>
MODEL_ID = <<complete the model ID to which you want to register the metric>>

BASE_URL =  f"https://platform.aporia.com/api/v1/{ACCOUNT}/{WORKSPACE}"
BASE_METRICS_URL = f"{BASE_URL}/metrics"

API_KEY = <<complete your API key>>
AUTH_HEADERS = {"Authorization": f"Bearer {API_KEY}"}

# First we read the code we prepared for our metric
with open('my_metric.py') as f:
	METRIC_CODE = f.read()

# Then we register it to the relevant Aporia model
metric_creation_body = {
    "model_id": MODEL_ID,
    "name": "my cool metric",
    "code": METRIC_CODE
}	
CREATE_METRIC_EP = f"{BASE_METRICS_URL}/code-based-metrics"
response = requests.post(
    url=CREATE_METRIC_EP,
    json=metric_creation_body,
    headers={"Authorization": f"Bearer {API_KEY}"}
)

# We'll use the metric ID later in order to test it
if (response.status_code == HTTPStatus.OK):
	metric_id = response.json().get('id')
	print(f"Successfully created metric, id: {metric_id}")
```

## Testing your metric

Once you have your metric registered, it is time to test it. Testing a code-based metric can be performed on a dataset of your choice. Below you will find example code for testing your metric on the latest version's serving dataset:

```python
MODEL_VERSIONS_EP = f'{BASE_URL}/model-versions'

# Select which version I want to use for the test
model_version_params = {"model_id" : MODEL_ID}
response = requests.get(
	MODEL_VERSIONS_EP,
	params=model_version_params,
	headers=AUTH_HEADERS
)
if response.status_code != HTTPStatus.OK:
    raise Exception(f"Failed getting model versions, error: {response.status_code}")

# We will use the last version returned, but you can choose a different one
versions = response.json()
dataset_id = versions[-1].get('serving_dataset').get('id')

# Test the metric to make sure it works
validate_metric_ep = f"{BASE_METRICS_URL}/code-based-metrics/validate"
body = {"metric_id" : metric_id, "dataset_id": dataset_id}
response = requests.post(
    url=validate_metric_ep,
    json=body,
    headers=AUTH_HEADERS
)

while HTTPStatus.OK == response.status_code and "pending" == response.json().get('status'):
	print(f"{response.json().get('progress')}% of metric validation task is completed")
	
	response = requests.post(
	    url=validate_metric_ep,
	    json=body,
	    headers=AUTH_HEADERS
	)

print(response.status_code)
print(response.json())
```

## Supported 3rd party libraries

* pyspark
* pyspark.sql
* pyspark.sql.functions
* snowflake
* snowflake.snowpark
* snowflake.snowpark.functions
* numpy
* numpy.core.\_methods
* pandas
* math
* scipy
* scipy.stats
* statsmodels
* statsmodels.stats.proportion

You can further explore all available code-based metrics features via REST API in our docs, [here](https://platform.aporia.com/api/v1/docs#tag/Metrics-\(Experimental\)/operation/get_many_code_based_metrics_api_v1__account_name___workspace_name__metrics_code_based_metrics_get).
