# Source: https://docs.infrahub.app/sync/reference/config.md

# Source: https://docs.infrahub.app/python-sdk/reference/config.md

# Python SDK Configuration

The Python SDK (Async or Sync) client can be configured using an instance of the `Config` class.

* Async
* Sync

```
from infrahub_sdk import Config, InfrahubClient
config = Config(address="http://infrahub:8080", api_token="123-xyz-invalid-token")
client = InfrahubClient(config=config)
```

```
from infrahub_sdk import Config, InfrahubClientSync
config = Config(address="http://infrahub:8080", api_token="123-xyz-invalid-token")
client = InfrahubClientSync(config=config)
```

The following settings can be defined in the `Config` class

## address[​](#address "Direct link to address")

**Description**: The URL to use when connecting to Infrahub.<br />**Type**: `string`<br />**Default value**: <http://localhost:8000><br />**Environment variable**: `INFRAHUB_ADDRESS`<br />

## api\_token[​](#api_token "Direct link to api_token")

**Description**: API token for authentication against Infrahub.<br />**Type**: `string`<br />**Environment variable**: `INFRAHUB_API_TOKEN`<br />

## echo\_graphql\_queries[​](#echo_graphql_queries "Direct link to echo_graphql_queries")

**Description**: If set the GraphQL query and variables will be echoed to the screen<br />**Type**: `boolean`<br />**Default value**: False<br />**Environment variable**: `INFRAHUB_ECHO_GRAPHQL_QUERIES`<br />

## username[​](#username "Direct link to username")

**Description**: Username for accessing Infrahub<br />**Type**: `string`<br />**Environment variable**: `INFRAHUB_USERNAME`<br />

## password[​](#password "Direct link to password")

**Description**: Password for accessing Infrahub<br />**Type**: `string`<br />**Environment variable**: `INFRAHUB_PASSWORD`<br />

## default\_branch[​](#default_branch "Direct link to default_branch")

**Description**: Default branch to target if not specified for each request.<br />**Type**: `string`<br />**Default value**: main<br />**Environment variable**: `INFRAHUB_DEFAULT_BRANCH`<br />

## default\_branch\_from\_git[​](#default_branch_from_git "Direct link to default_branch_from_git")

**Description**: Indicates if the default Infrahub branch to target should come from the active branch in the local Git repository.<br />**Type**: `boolean`<br />**Default value**: False<br />**Environment variable**: `INFRAHUB_DEFAULT_BRANCH_FROM_GIT`<br />

## identifier[​](#identifier "Direct link to identifier")

**Description**: Tracker identifier<br />**Type**: `string`<br />**Environment variable**: `INFRAHUB_IDENTIFIER`<br />

## insert\_tracker[​](#insert_tracker "Direct link to insert_tracker")

**Description**: Insert a tracker on queries to the server<br />**Type**: `boolean`<br />**Default value**: False<br />**Environment variable**: `INFRAHUB_INSERT_TRACKER`<br />

## max\_concurrent\_execution[​](#max_concurrent_execution "Direct link to max_concurrent_execution")

**Description**: Max concurrent execution in batch mode<br />**Type**: `integer`<br />**Default value**: 5<br />**Environment variable**: `INFRAHUB_MAX_CONCURRENT_EXECUTION`<br />

## mode[​](#mode "Direct link to mode")

**Description**: Default mode for the client<br />**Type**: `object`<br />**Environment variable**: `INFRAHUB_MODE`<br />

## pagination\_size[​](#pagination_size "Direct link to pagination_size")

**Description**: Page size for queries to the server<br />**Type**: `integer`<br />**Default value**: 50<br />**Environment variable**: `INFRAHUB_PAGINATION_SIZE`<br />

## retry\_delay[​](#retry_delay "Direct link to retry_delay")

**Description**: Number of seconds to wait until attempting a retry.<br />**Type**: `integer`<br />**Default value**: 5<br />**Environment variable**: `INFRAHUB_RETRY_DELAY`<br />

## retry\_on\_failure[​](#retry_on_failure "Direct link to retry_on_failure")

**Description**: Retry operation in case of failure<br />**Type**: `boolean`<br />**Default value**: False<br />**Environment variable**: `INFRAHUB_RETRY_ON_FAILURE`<br />

## max\_retry\_duration[​](#max_retry_duration "Direct link to max_retry_duration")

**Description**: Maximum duration until we stop attempting to retry if enabled.<br />**Type**: `integer`<br />**Default value**: 300<br />**Environment variable**: `INFRAHUB_MAX_RETRY_DURATION`<br />

## schema\_converge\_timeout[​](#schema_converge_timeout "Direct link to schema_converge_timeout")

**Description**: Number of seconds to wait for schema to have converged<br />**Type**: `integer`<br />**Default value**: 60<br />**Environment variable**: `INFRAHUB_SCHEMA_CONVERGE_TIMEOUT`<br />

## timeout[​](#timeout "Direct link to timeout")

**Description**: Default connection timeout in seconds<br />**Type**: `integer`<br />**Default value**: 60<br />**Environment variable**: `INFRAHUB_TIMEOUT`<br />

## transport[​](#transport "Direct link to transport")

**Description**: Set an alternate transport using a predefined option<br />**Type**: `object`<br />**Environment variable**: `INFRAHUB_TRANSPORT`<br />

## proxy[​](#proxy "Direct link to proxy")

**Description**: Proxy address<br />**Type**: `string`<br />**Environment variable**: `INFRAHUB_PROXY`<br />

## proxy\_mounts[​](#proxy_mounts "Direct link to proxy_mounts")

**Description**: Proxy mounts configuration<br />**Type**: `object`<br />**Environment variable**: `INFRAHUB_PROXY_MOUNTS`<br />

## update\_group\_context[​](#update_group_context "Direct link to update_group_context")

**Description**: Update GraphQL query groups<br />**Type**: `boolean`<br />**Default value**: False<br />**Environment variable**: `INFRAHUB_UPDATE_GROUP_CONTEXT`<br />

## tls\_insecure[​](#tls_insecure "Direct link to tls_insecure")

**Description**:<br /><!-- -->Indicates if TLS certificates are verified. Enabling this option will disable: CA verification, expiry date verification, hostname verification). Can be useful to test with self-signed certificates.<br />**Type**: `boolean`<br />**Default value**: False<br />**Environment variable**: `INFRAHUB_TLS_INSECURE`<br />

## tls\_ca\_file[​](#tls_ca_file "Direct link to tls_ca_file")

**Description**: File path to CA cert or bundle in PEM format<br />**Type**: `string`<br />**Environment variable**: `INFRAHUB_TLS_CA_FILE`<br />

## recorder[​](#recorder "Direct link to recorder")

**Property**: recorder<br />

**Description**: Select builtin recorder for later replay.<br />**Type**: `RecorderType`<br />**Default value**: RecorderType.NONE<br />

## custom\_recorder[​](#custom_recorder "Direct link to custom_recorder")

**Property**: custom\_recorder<br />

**Description**: Provides a way to record responses from the Infrahub API<br />**Type**: `Recorder` (protocol)<br />**Default value**: NoRecorder.default<br />

## requester[​](#requester "Direct link to requester")

**Property**: requester<br />

**Type**: `AsyncRequester`<br />**Default value**: None<br />

## sync\_requester[​](#sync_requester "Direct link to sync_requester")

**Property**: sync\_requester<br />

**Type**: `SyncRequester`<br />**Default value**: None<br />
