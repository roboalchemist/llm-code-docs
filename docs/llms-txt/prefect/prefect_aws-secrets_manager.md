# Source: https://docs.prefect.io/integrations/prefect-aws/api-ref/prefect_aws-secrets_manager.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# secrets_manager

# `prefect_aws.secrets_manager`

Tasks for interacting with AWS Secrets Manager

## Functions

### `read_secret` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-aws/prefect_aws/secrets_manager.py#L17" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_secret(secret_name: str, aws_credentials: AwsCredentials, version_id: Optional[str] = None, version_stage: Optional[str] = None) -> Union[str, bytes]
```

Reads the value of a given secret from AWS Secrets Manager.

**Args:**

* `secret_name`: Name of stored secret.
* `aws_credentials`: Credentials to use for authentication with AWS.
* `version_id`: Specifies version of secret to read. Defaults to the most recent
  version if not given.
* `version_stage`: Specifies the version stage of the secret to read. Defaults to
  AWS\_CURRENT if not given.

**Returns:**

* The secret values as a `str` or `bytes` depending on the format in which the
  secret was stored.

### `update_secret` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-aws/prefect_aws/secrets_manager.py#L83" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
update_secret(secret_name: str, secret_value: Union[str, bytes], aws_credentials: AwsCredentials, description: Optional[str] = None) -> Dict[str, str]
```

Updates the value of a given secret in AWS Secrets Manager.

**Args:**

* `secret_name`: Name of secret to update.
* `secret_value`: Desired value of the secret. Can be either `str` or `bytes`.
* `aws_credentials`: Credentials to use for authentication with AWS.
* `description`: Desired description of the secret.

**Returns:**

* A dict containing the secret ARN (Amazon Resource Name),
  name, and current version ID.

```python  theme={null}
{
    "ARN": str,
    "Name": str,
    "VersionId": str
}
```

### `create_secret` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-aws/prefect_aws/secrets_manager.py#L160" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
create_secret(secret_name: str, secret_value: Union[str, bytes], aws_credentials: AwsCredentials, description: Optional[str] = None, tags: Optional[List[Dict[str, str]]] = None) -> Dict[str, str]
```

Creates a secret in AWS Secrets Manager.

**Args:**

* `secret_name`: The name of the secret to create.
* `secret_value`: The value to store in the created secret.
* `aws_credentials`: Credentials to use for authentication with AWS.
* `description`: A description for the created secret.
* `tags`: A list of tags to attach to the secret. Each tag should be specified as a
  dictionary in the following format:

```python  theme={null}
{
    "Key"\: str,
    "Value"\: str
}
```

**Returns:**

* A dict containing the secret ARN (Amazon Resource Name),
  name, and current version ID.

```python  theme={null}
{
    "ARN": str,
    "Name": str,
    "VersionId": str
}
```

Example:
Create a secret:

```python  theme={null}
from prefect import flow
from prefect_aws import AwsCredentials
from prefect_aws.secrets_manager import create_secret

@flow
def example_create_secret():
    aws_credentials = AwsCredentials(
        aws_access_key_id="access_key_id",
        aws_secret_access_key="secret_access_key"
    )
    create_secret(
        secret_name="life_the_universe_and_everything",
        secret_value="42",
        aws_credentials=aws_credentials
    )

example_create_secret()
```

### `delete_secret` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-aws/prefect_aws/secrets_manager.py#L249" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
delete_secret(secret_name: str, aws_credentials: AwsCredentials, recovery_window_in_days: int = 30, force_delete_without_recovery: bool = False) -> Dict[str, str]
```

Deletes a secret from AWS Secrets Manager.

Secrets can either be deleted immediately by setting `force_delete_without_recovery`
equal to `True`. Otherwise, secrets will be marked for deletion and available for
recovery for the number of days specified in `recovery_window_in_days`

**Args:**

* `secret_name`: Name of the secret to be deleted.
* `aws_credentials`: Credentials to use for authentication with AWS.
* `recovery_window_in_days`: Number of days a secret should be recoverable for
  before permanent deletion. Minimum window is 7 days and maximum window
  is 30 days. If `force_delete_without_recovery` is set to `True`, this
  value will be ignored.
* `force_delete_without_recovery`: If `True`, the secret will be immediately
  deleted and will not be recoverable.

**Returns:**

* A dict containing the secret ARN (Amazon Resource Name),
  name, and deletion date of the secret. DeletionDate is the date and
  time of the delete request plus the number of days in
  `recovery_window_in_days`.

```python  theme={null}
{
    "ARN": str,
    "Name": str,
    "DeletionDate": datetime.datetime
}
```

**Examples:**

Delete a secret immediately:

```python  theme={null}
from prefect import flow
from prefect_aws import AwsCredentials
from prefect_aws.secrets_manager import delete_secret

@flow
def example_delete_secret_immediately():
    aws_credentials = AwsCredentials(
        aws_access_key_id="access_key_id",
        aws_secret_access_key="secret_access_key"
    )
    delete_secret(
        secret_name="life_the_universe_and_everything",
        aws_credentials=aws_credentials,
        force_delete_without_recovery: True
    )

example_delete_secret_immediately()
```

Delete a secret with a 90 day recovery window:

```python  theme={null}
from prefect import flow
from prefect_aws import AwsCredentials
from prefect_aws.secrets_manager import delete_secret

@flow
def example_delete_secret_with_recovery_window():
    aws_credentials = AwsCredentials(
        aws_access_key_id="access_key_id",
        aws_secret_access_key="secret_access_key"
    )
    delete_secret(
        secret_name="life_the_universe_and_everything",
        aws_credentials=aws_credentials,
        recovery_window_in_days=90
    )

example_delete_secret_with_recovery_window()
```

## Classes

### `AwsSecret` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-aws/prefect_aws/secrets_manager.py#L359" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

Manages a secret in AWS's Secrets Manager.

**Attributes:**

* `aws_credentials`: The credentials to use for authentication with AWS.
* `secret_name`: The name of the secret.

**Methods:**

#### `adelete_secret` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-aws/prefect_aws/secrets_manager.py#L547" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
adelete_secret(self, recovery_window_in_days: int = 30, force_delete_without_recovery: bool = False, **delete_kwargs: Dict[str, Any]) -> str
```

Asynchronously deletes the secret from the secret storage service.

**Args:**

* `recovery_window_in_days`: The number of days to wait before permanently
  deleting the secret. Must be between 7 and 30 days.
* `force_delete_without_recovery`: If True, the secret will be deleted
  immediately without a recovery window.
* `**delete_kwargs`: Additional keyword arguments to pass to the
  delete\_secret method of the boto3 client.

**Returns:**

* The path that the secret was deleted from.

**Examples:**

Deletes the secret with a recovery window of 15 days.

```python  theme={null}
secrets_manager = SecretsManager.load("MY_BLOCK")
await secrets_manager.adelete_secret(recovery_window_in_days=15)
```

#### `aread_secret` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-aws/prefect_aws/secrets_manager.py#L375" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
aread_secret(self, version_id: Optional[str] = None, version_stage: Optional[str] = None, **read_kwargs: Any) -> bytes
```

Asynchronously reads the secret from the secret storage service.

**Args:**

* `version_id`: The version of the secret to read. If not provided, the latest
  version will be read.
* `version_stage`: The version stage of the secret to read. If not provided,
  the latest version will be read.
* `read_kwargs`: Additional keyword arguments to pass to the
  `get_secret_value` method of the boto3 client.

**Returns:**

* The secret data.

**Examples:**

Reads a secret.

```python  theme={null}
secrets_manager = SecretsManager.load("MY_BLOCK")
await secrets_manager.aread_secret()
```

#### `awrite_secret` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-aws/prefect_aws/secrets_manager.py#L460" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
awrite_secret(self, secret_data: bytes, **put_or_create_secret_kwargs: Dict[str, Any]) -> str
```

Asynchronously writes the secret to the secret storage service as a SecretBinary;
if it doesn't exist, it will be created.

**Args:**

* `secret_data`: The secret data to write.
* `**put_or_create_secret_kwargs`: Additional keyword arguments to pass to
  put\_secret\_value or create\_secret method of the boto3 client.

**Returns:**

* The path that the secret was written to.

**Examples:**

Write some secret data.

```python  theme={null}
secrets_manager = SecretsManager.load("MY_BLOCK")
await secrets_manager.awrite_secret(b"my_secret_data")
```

#### `delete_secret` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-aws/prefect_aws/secrets_manager.py#L597" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
delete_secret(self, recovery_window_in_days: int = 30, force_delete_without_recovery: bool = False, **delete_kwargs: Dict[str, Any]) -> str
```

Deletes the secret from the secret storage service.

**Args:**

* `recovery_window_in_days`: The number of days to wait before permanently
  deleting the secret. Must be between 7 and 30 days.
* `force_delete_without_recovery`: If True, the secret will be deleted
  immediately without a recovery window.
* `**delete_kwargs`: Additional keyword arguments to pass to the
  delete\_secret method of the boto3 client.

**Returns:**

* The path that the secret was deleted from.

**Examples:**

Deletes the secret with a recovery window of 15 days.

```python  theme={null}
secrets_manager = SecretsManager.load("MY_BLOCK")
secrets_manager.delete_secret(recovery_window_in_days=15)
```

#### `read_secret` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-aws/prefect_aws/secrets_manager.py#L419" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
read_secret(self, version_id: Optional[str] = None, version_stage: Optional[str] = None, **read_kwargs: Any) -> bytes
```

Reads the secret from the secret storage service.

**Args:**

* `version_id`: The version of the secret to read. If not provided, the latest
  version will be read.
* `version_stage`: The version stage of the secret to read. If not provided,
  the latest version will be read.
* `read_kwargs`: Additional keyword arguments to pass to the
  `get_secret_value` method of the boto3 client.

**Returns:**

* The secret data.

**Examples:**

Reads a secret.

```python  theme={null}
secrets_manager = SecretsManager.load("MY_BLOCK")
secrets_manager.read_secret()
```

#### `write_secret` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-aws/prefect_aws/secrets_manager.py#L505" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
write_secret(self, secret_data: bytes, **put_or_create_secret_kwargs: Dict[str, Any]) -> str
```

Writes the secret to the secret storage service as a SecretBinary;
if it doesn't exist, it will be created.

**Args:**

* `secret_data`: The secret data to write.
* `**put_or_create_secret_kwargs`: Additional keyword arguments to pass to
  put\_secret\_value or create\_secret method of the boto3 client.

**Returns:**

* The path that the secret was written to.

**Examples:**

Write some secret data.

```python  theme={null}
secrets_manager = SecretsManager.load("MY_BLOCK")
secrets_manager.write_secret(b"my_secret_data")
```


Built with [Mintlify](https://mintlify.com).