# Source: https://docs.roboflow.com/roboflow/roboflow-ko/deploy/dedicated-deployments/manage-dedicated-deployments-with-an-api.md

# Source: https://docs.roboflow.com/roboflow/roboflow-jp/depuroi/dedicated-deployments/manage-dedicated-deployments-with-an-api.md

# Source: https://docs.roboflow.com/roboflow/roboflow-hi/deploy/dedicated-deployments/manage-dedicated-deployments-with-an-api.md

# Source: https://docs.roboflow.com/deploy/dedicated-deployments/manage-dedicated-deployments-with-an-api.md

# Manage Dedicated Deployments with an API

Notices:

* All endpoints are hosted at `https://roboflow.cloud`.
* Check the response code:
  * If it's `200`, decode the response body as a JSON object.
  * Otherwise, the response body contains an error message as a string.

<details>

<summary>POST /add — create a dedicated deployment</summary>

**Request Body Example (json)**

```
{
	"api_key": API_KEY,
	"deployment_name": "dev-testing",
	"machine_type": "dev-gpu",
	"creator_email": YOUR_EMAIL_ADDRESS,
	"duration": 3.0,
	"inference_version": "latest",
	"min_replicas": 1,
	"max_replicas": 1
}
```

**Request Body Schema (json)**

* api\_key (string): required
* deployment\_name (string): required
* machine\_type (string): required
* creator\_email (string): required
* duration (float): optional, unit is hour. default is `3`
* inference\_version (string): optional, default is `latest`
* min\_replicas (integer): optional, default is `1`
* max\_replicas (integer): optional, default is `1`

**Response Example (json)**

```
{
	"deployment_id": "IwzJ5YLQ0iDhwzqoh3Ae",
	"deployment_name": "dev-testing",
	"machine_type": "dev-gpu",
	"creator_email": YOUR_EMAIL_ADDRESS,
	"creator_id": YOUR_USER_ID,
	"subdomain": "dev-testing",
	"domain": "dev-testing.roboflow.cloud",
	"duration": 3.0,
	"inference_version": "0.45.0",
	"max_replicas": 1,
	"min_replicas": 1,
	"num_replicas": 0,
	"status": "pending",
	"workspace_id": YOUR_WORKSPACE_ID,
	"workspace_url": YOUR_WORKSPACE_URL
}
```

**Response Schema (json)**

* deployment\_id (string): an unique identifier
* deployment\_name (string)
* machine\_type (string)
* creator\_email (string)
* creator\_id (string): the user id corresponding to `creator_email`
* subdomain (string): not always the same as `deployment_name`, we'll add some suffix if the subdomain is already taken
* domain (string)
* duration (float)
* inference\_version (string)
* min\_replicas (integer)
* max\_replicas (integer)
* num\_replicas (integer): current available replicas
* status (string)
* workspace\_id (string)
* workspace\_url (string)

</details>

<details>

<summary>GET /list — list dedicated deployments in your workspace</summary>

**Query Parameters**

* api\_key (string): required
* show\_expired (string): optional, default is `false`
* show\_deleted (string): optional, default is `false`

**Response Example (json)**

```
[
{
	"deployment_id": "IwzJ5YLQ0iDhwzqoh3Ae",
	"deployment_name": "dev-testing",
	"machine_type": "dev-gpu",
	"creator_email": YOUR_EMAIL_ADDRESS,
	"creator_id": YOUR_USER_ID,
	"subdomain": "dev-testing",
	"domain": "dev-testing.roboflow.cloud",
	"duration": 3.0,
	"inference_version": "0.45.0",
	"max_replicas": 1,
	"min_replicas": 1,
	"num_replicas": 0,
	"status": "pending",
	"workspace_id": YOUR_WORKSPACE_ID,
	"workspace_url": YOUR_WORKSPACE_URL
}
]
```

**Response Schema (json)**

a list of dedicated deployment entries, while each entry has the same schema as describe in the [/add](#post-add-create-a-dedicated-deployment) endpoint.

</details>

<details>

<summary>GET /get — get details of a dedicated deployment</summary>

**Query Parameters**

* api\_key (string): required
* deployment\_name (string): required

**Response Example (json)**

```
{
	"deployment_id": "IwzJ5YLQ0iDhwzqoh3Ae",
	"deployment_name": "dev-testing",
	"machine_type": "dev-gpu",
	"creator_email": YOUR_EMAIL_ADDRESS,
	"creator_id": YOUR_USER_ID,
	"subdomain": "dev-testing",
	"domain": "dev-testing.roboflow.cloud",
	"duration": 3.0,
	"inference_version": "0.45.0",
	"max_replicas": 1,
	"min_replicas": 1,
	"num_replicas": 0,
	"status": "pending",
	"workspace_id": YOUR_WORKSPACE_ID,
	"workspace_url": YOUR_WORKSPACE_URL
}
```

**Response Schema (json)**

the same schema as the response of the [/add](#post-add-create-a-dedicated-deployment) endpoint.

</details>

<details>

<summary>GET /get_log — get logs of a dedicated deployment</summary>

**Query Parameters**

* api\_key (string): required
* deployment\_name (string): required
* max\_entries (integer): optional, default is 50
* from\_timestamp (string): optional, in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, default is 1 hour before current time
* to\_timestamp (string): optional, in [ISO 8601](https://en.wikipedia.org/wiki/ISO_8601) format, default is current time

**Response Example (json)**

```
[
	{
		"insert_id": "gpwrgrw55p7b9jdq",
		"payload": "INFO:     10.18.0.38:46296 - \"GET /info HTTP/1.1\" 200 OK",
		"severity": "INFO",
		"timestamp": "2025-01-22T13:23:14.209436+00:00"
	},
	{
		"insert_id": "mbieh16zdjvqp81j",
		"payload": "INFO:     10.18.0.38:46294 - \"GET /info HTTP/1.1\" 200 OK",
		"severity": "INFO",
		"timestamp": "2025-01-22T13:23:14.208738+00:00"
	},
	{
		"insert_id": "0odfnfwh8ts6e4jt",
		"payload": "INFO:     10.18.0.38:54650 - \"GET /info HTTP/1.1\" 200 OK",
		"severity": "INFO",
		"timestamp": "2025-01-22T13:22:14.209054+00:00"
	},
	{
		"insert_id": "s3nabhyhejuke6ub",
		"payload": "INFO:     10.18.0.38:54640 - \"GET /info HTTP/1.1\" 200 OK",
		"severity": "INFO",
		"timestamp": "2025-01-22T13:22:14.208329+00:00"
	},
	{
		"insert_id": "2cz5u3jx4ma22tl8",
		"payload": "INFO:     10.18.0.38:40264 - \"GET /info HTTP/1.1\" 200 OK",
		"severity": "INFO",
		"timestamp": "2025-01-22T13:21:14.209900+00:00"
	}
]
```

**Response Schema (json)**

a list of log entries, while each entry has following attributes:

* insert\_id (string): unique identifier for each log entry
* payload (string): log content
* severity (string)
* timestamp (string)

</details>

<details>

<summary>POST /pause — pause a dedicated deployment</summary>

**Request Body Example (json)**

```
{
	"api_key": API_KEY,
	"deployment_name": "dev-testing"
}
```

**Request Body Schema (json)**

* api\_key (string): required
* deployment\_name (string): require

**Response Example (json)**

```
{
	"message": "OK"
}
```

**Response Schema**

* message (string)

</details>

<details>

<summary>POST /resume — resume a dedicated deployment</summary>

**Request Body Example (json)**

```
{
	"api_key": API_KEY,
	"deployment_name": "dev-testing"
}
```

**Request Body Schema (json)**

* api\_key (string): required
* deployment\_name (string): require

**Response Example (json)**

```
{
	"message": "OK"
}
```

**Response Schema**

* message (string)

</details>

<details>

<summary>POST /delete — delete a dedicated deployment</summary>

**Request Body Example (json)**

```
{
	"api_key": API_KEY,
	"deployment_name": "dev-testing"
}
```

**Request Body Schema (json)**

* api\_key (string): required
* deployment\_name (string): require

**Response Example (json)**

```
{
	"message": "OK"
}
```

**Response Schema**

* message (string)

</details>
