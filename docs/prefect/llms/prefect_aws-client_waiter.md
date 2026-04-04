# Source: https://docs.prefect.io/integrations/prefect-aws/api-ref/prefect_aws-client_waiter.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.prefect.io/llms.txt
> Use this file to discover all available pages before exploring further.

# client_waiter

# `prefect_aws.client_waiter`

Task for waiting on a long-running AWS job

## Functions

### `aclient_waiter` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-aws/prefect_aws/client_waiter.py#L15" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
aclient_waiter(client: str, waiter_name: str, aws_credentials: AwsCredentials, waiter_definition: Optional[Dict[str, Any]] = None, **waiter_kwargs: Optional[Dict[str, Any]])
```

Asynchronously uses the underlying boto3 waiter functionality.

**Args:**

* `client`: The AWS client on which to wait (e.g., 'client\_wait', 'ec2', etc).
* `waiter_name`: The name of the waiter to instantiate.
  You may also use a custom waiter name, if you supply
  an accompanying waiter definition dict.
* `aws_credentials`: Credentials to use for authentication with AWS.
* `waiter_definition`: A valid custom waiter model, as a dict. Note that if
  you supply a custom definition, it is assumed that the provided
  'waiter\_name' is contained within the waiter definition dict.
* `**waiter_kwargs`: Arguments to pass to the `waiter.wait(...)` method. Will
  depend upon the specific waiter being called.

### `client_waiter` <sup><a href="https://github.com/PrefectHQ/prefect/blob/main/src/integrations/prefect-aws/prefect_aws/client_waiter.py#L80" target="_blank"><Icon icon="github" style="width: 14px; height: 14px;" /></a></sup>

```python  theme={null}
client_waiter(client: str, waiter_name: str, aws_credentials: AwsCredentials, waiter_definition: Optional[Dict[str, Any]] = None, **waiter_kwargs: Optional[Dict[str, Any]])
```

Uses the underlying boto3 waiter functionality.

**Args:**

* `client`: The AWS client on which to wait (e.g., 'client\_wait', 'ec2', etc).
* `waiter_name`: The name of the waiter to instantiate.
  You may also use a custom waiter name, if you supply
  an accompanying waiter definition dict.
* `aws_credentials`: Credentials to use for authentication with AWS.
* `waiter_definition`: A valid custom waiter model, as a dict. Note that if
  you supply a custom definition, it is assumed that the provided
  'waiter\_name' is contained within the waiter definition dict.
* `**waiter_kwargs`: Arguments to pass to the `waiter.wait(...)` method. Will
  depend upon the specific waiter being called.


Built with [Mintlify](https://mintlify.com).