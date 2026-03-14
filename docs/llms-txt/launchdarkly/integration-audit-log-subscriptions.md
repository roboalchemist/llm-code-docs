# Source: https://launchdarkly.com/docs/api/integration-audit-log-subscriptions.md

Audit log integration subscriptions allow you to send audit log events hooks to one of dozens of external tools. For example, you can send flag change event webhooks to external third party software. To learn more, read [Building your own integrations](https://launchdarkly.com/docs/integrations/building-integrations#building-your-own-integrations).

You can use the integration subscriptions API to create, delete, and manage your integration audit log subscriptions.

Each of these operations requires an `integrationKey` that refers to the type of integration. The required `config` fields to create a subscription vary depending on the `integrationKey`. You can find a full list of the fields for each integration below.

Several of these operations require a subscription ID. The subscription ID is returned as part of the [Create audit log subscription](https://launchdarkly.com/docs/api/integration-audit-log-subscriptions/create-subscription) and [Get audit log subscriptions by integration](https://launchdarkly.com/docs/api/integration-audit-log-subscriptions/get-subscriptions) responses. It is the `_id` field, or the `_id` field of each element in the `items` array.

### Configuration bodies by integrationKey

#### datadog

`apiKey` is a sensitive value.

`hostURL` must evaluate to either `"https://api.datadoghq.com"` or `"https://api.datadoghq.eu"` and will default to the former if not explicitly defined.

```
"config": {
    "apiKey": <string, optional>, # sensitive value
    "hostURL": <string, optional>
}
```

#### dynatrace

`apiToken` is a sensitive value.

`entity` must evaluate to one of the following fields and will default to `"APPLICATION"` if not explicitly defined:

<details>
<summary>Click to expand list of fields</summary>
<br/>
"APPLICATION"<br/>
"APPLICATION_METHOD"<br/>
"APPLICATION_METHOD_GROUP"<br/>
"AUTO_SCALING_GROUP"<br/>
"AUXILIARY_SYNTHETIC_TEST"<br/>
"AWS_APPLICATION_LOAD_BALANCER"<br/>
"AWS_AVAILABILITY_ZONE"<br/>
"AWS_CREDENTIALS"<br/>
"AWS_LAMBDA_FUNCTION"<br/>
"AWS_NETWORK_LOAD_BALANCER"<br/>
"AZURE_API_MANAGEMENT_SERVICE"<br/>
"AZURE_APPLICATION_GATEWAY"<br/>
"AZURE_COSMOS_DB"<br/>
"AZURE_CREDENTIALS"<br/>
"AZURE_EVENT_HUB"<br/>
"AZURE_EVENT_HUB_NAMESPACE"<br/>
"AZURE_FUNCTION_APP"<br/>
"AZURE_IOT_HUB"<br/>
"AZURE_LOAD_BALANCER"<br/>
"AZURE_MGMT_GROUP"<br/>
"AZURE_REDIS_CACHE"<br/>
"AZURE_REGION"<br/>
"AZURE_SERVICE_BUS_NAMESPACE"<br/>
"AZURE_SERVICE_BUS_QUEUE"<br/>
"AZURE_SERVICE_BUS_TOPIC"<br/>
"AZURE_SQL_DATABASE"<br/>
"AZURE_SQL_ELASTIC_POOL"<br/>
"AZURE_SQL_SERVER"<br/>
"AZURE_STORAGE_ACCOUNT"<br/>
"AZURE_SUBSCRIPTION"<br/>
"AZURE_TENANT"<br/>
"AZURE_VM"<br/>
"AZURE_VM_SCALE_SET"<br/>
"AZURE_WEB_APP"<br/>
"CF_APPLICATION"<br/>
"CF_FOUNDATION"<br/>
"CINDER_VOLUME"<br/>
"CLOUD_APPLICATION"<br/>
"CLOUD_APPLICATION_INSTANCE"<br/>
"CLOUD_APPLICATION_NAMESPACE"<br/>
"CONTAINER_GROUP"<br/>
"CONTAINER_GROUP_INSTANCE"<br/>
"CUSTOM_APPLICATION"<br/>
"CUSTOM_DEVICE"<br/>
"CUSTOM_DEVICE_GROUP"<br/>
"DCRUM_APPLICATION"<br/>
"DCRUM_SERVICE"<br/>
"DCRUM_SERVICE_INSTANCE"<br/>
"DEVICE_APPLICATION_METHOD"<br/>
"DISK"<br/>
"DOCKER_CONTAINER_GROUP_INSTANCE"<br/>
"DYNAMO_DB_TABLE"<br/>
"EBS_VOLUME"<br/>
"EC2_INSTANCE"<br/>
"ELASTIC_LOAD_BALANCER"<br/>
"ENVIRONMENT"<br/>
"EXTERNAL_SYNTHETIC_TEST_STEP"<br/>
"GCP_ZONE"<br/>
"GEOLOCATION"<br/>
"GEOLOC_SITE"<br/>
"GOOGLE_COMPUTE_ENGINE"<br/>
"HOST"<br/>
"HOST_GROUP"<br/>
"HTTP_CHECK"<br/>
"HTTP_CHECK_STEP"<br/>
"HYPERVISOR"<br/>
"KUBERNETES_CLUSTER"<br/>
"KUBERNETES_NODE"<br/>
"MOBILE_APPLICATION"<br/>
"NETWORK_INTERFACE"<br/>
"NEUTRON_SUBNET"<br/>
"OPENSTACK_PROJECT"<br/>
"OPENSTACK_REGION"<br/>
"OPENSTACK_VM"<br/>
"OS"<br/>
"PROCESS_GROUP"<br/>
"PROCESS_GROUP_INSTANCE"<br/>
"RELATIONAL_DATABASE_SERVICE"<br/>
"SERVICE"<br/>
"SERVICE_INSTANCE"<br/>
"SERVICE_METHOD"<br/>
"SERVICE_METHOD_GROUP"<br/>
"SWIFT_CONTAINER"<br/>
"SYNTHETIC_LOCATION"<br/>
"SYNTHETIC_TEST"<br/>
"SYNTHETIC_TEST_STEP"<br/>
"VIRTUALMACHINE"<br/>
"VMWARE_DATACENTER"
</details>

```
"config": {
    "apiToken": <string, required>,
    "url": <string, required>,
    "entity": <string, optional>
}
```

#### elastic

`token` is a sensitive field.

```
"config": {
    "url": <string, required>,
    "token": <string, required>,
    "index": <string, required>
}
```

#### honeycomb

`apiKey` is a sensitive field.

```
"config": {
    "datasetName": <string, required>,
    "apiKey": <string, required>
}
```

#### logdna

`ingestionKey` is a sensitive field.

```
"config": {
    "ingestionKey": <string, required>,
    "level": <string, optional>
}
```

#### msteams

```
"config": {
    "url": <string, required>
}
```

#### new-relic-apm

`apiKey` is a sensitive field.

`domain` must evaluate to either `"api.newrelic.com"` or `"api.eu.newrelic.com"` and will default to the former if not explicitly defined.

```
"config": {
    "apiKey": <string, required>,
    "applicationId": <string, required>,
    "domain": <string, optional>
}
```

#### signalfx

`accessToken` is a sensitive field.

```
"config": {
    "accessToken": <string, required>,
    "realm": <string, required>
}
```

#### splunk

`token` is a sensitive field.

```
"config": {
    "base-url": <string, required>,
    "token": <string, required>,
    "skip-ca-verification": <boolean, required>
}
```
