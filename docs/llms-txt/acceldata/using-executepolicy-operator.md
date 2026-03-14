# Source: https://docs.acceldata.io/documentation/using-executepolicy-operator.md

# Using ExecutePolicy Operator

### ExecutePolicyOperator OPERATOR

`ExecutePolicyOperator` is used to execute a policy by passing `policy type` and `policy_id`. Only data quality and reconciliation policies are supported for ad-hoc execution using this operator.

The parameters for ExecutePolicyOperator include:

| Parameter | Description | 
| ---- | ---- | 
| sync | A **Boolean** parameter used to decide if the policy should be executed synchronously or asynchronously. It is a mandatory parameter. If it is set to `True` it will return only after the execution ends. If it is set to `False` it will return immediately after starting the execution. | 
| policy_type | A PolicyType parameter used to specify the policy type. It is a mandatory parameter. It is an enum which will take values from constants as PolicyType.DATA_QUALITY or PolicyType.RECONCILIATION. | 
| policy_id | A **String** parameter used to specify the policy id to be executed. It is a mandatory parameter. | 
| incremental | A **Boolean** parameter used to specify if the policy execution should be incremental or full. The default value is False. | 
| failure_strategy | An enum parameter used to decide the behaviour in case of failure. The default value is DoNotFail.\n\n\n\n- `failure_strategy` takes enum of type `FailureStrategy` which can have three values `DoNotFail`, `FailOnError` , and `FailOnWarning`.\n- `DoNotFail` will never throw. In case of errors in policy execution, it will log the error.\n- `FailOnError` will Throw an exception only if it's an error. In case of a warning, it will return without any errors.\n- `FailOnWarning` will throw exceptions on warnings as well as errors. | 


```python
from acceldata_airflow_sdk.operators.execute_policy_operator import ExecutePolicyOperator
from acceldata_sdk.constants import FailureStrategy, PolicyType
operator_task = ExecutePolicyOperator(
    task_id='torch_pipeline_operator_test',
    policy_type=PolicyType.DATA_QUALITY,
    policy_id=46,
    sync=True,
    failure_strategy=FailureStrategy.DoNotFail,
    dag=dag
)
```



`ExecutePolicyOperator` stores the execution id of the policy executed in xcom using the key {`policy_type.name`}_{`policy_id`}_execution_id. Replace the policy_type and policy_id based on the policy.

Hence, to query the result in another task you need to pull the execution id from xcom using the same key {`policy_type`}_{`policy_id`}_execution_id.

### Query the Result Using get_policy_execution_result

`get_policy_execution_result` is a helper function that can query the result of policy executed with the operator using the execution id pulled from xcom. In this example, the policy_type is `PolicyType.DATA_QUALITY.name` and the policy_id is `46.`

The parameters for get_polcy_execution_result include:

| Parameter | Description | 
| ---- | ---- | 
| policy_type | A `PolicyType` parameter used to specify the policy type. It is a mandatory parameter. It is an enum which will take values from constants as `PolicyType.DATA_QUALITY` or `PolicyType.RECONCILIATION`. | 
| execution_id | A **String** parameter specifying the execution id for which users want to query the results. It is a mandatory parameter. | 
| failure_strategy | An enum parameter used to decide the behaviour in case of failure. The default value is DoNotFail.\n\n\n\n- `failure_strategy` takes enum of type `FailureStrategy` which can have three values `DoNotFail`, `FailOnError` , and `FailOnWarning`.\n- `DoNotFail` will never throw. In case of errors in policy execution, it will log the error.\n- `FailOnError` will Throw an exception only if it's an error. In case of a warning, it will return without any errors.\n- `FailOnWarning` will throw exceptions on warnings as well as errors. | 


```python
from acceldata_sdk.torch_client import TorchClient
from acceldata_airflow_sdk.initialiser import torch_credentials
from acceldata_sdk.constants import FailureStrategy, PolicyType, RuleExecutionStatus

 def ruleoperator_result(**context):
        xcom_key = f'{PolicyType.DATA_QUALITY.name}_46_execution_id'
        task_instance = context['ti']
        # pull the execution id from xcom
        if execution_id is not None:
           # `adoc_connection_id` represents the unique identifier for the connection established
           # between ADOC and Airflow.
        	 torch_client = TorchClient(**torch_credentials(conn_id=adoc_connection_id))
           result = torch_client.get_policy_execution_result(policy_type=PolicyType.DATA_QUALITY,
                                                              execution_id=execution_id,
                                                    failure_strategy=FailureStrategy.FailOnError)
           if result.execution.resultStatus == RuleExecutionStatus.ERRORED:         
              print(result.execution.executionError)
```



#### Circuit Breaker Pattern Based on Policy Execution Result

Users can interrupt DAG execution based on the result of policy execution. For example, if the policy execution encounters errors, the user may wish to exit the DAG execution. Then, `failure strategy=FailureStrategy.FailOnError` can be set. If policy execution fails, this will result in DAG execution being halted by throwing an exception.

```python
from acceldata_sdk.torch_client import TorchClient
from acceldata_airflow_sdk.initialiser import torch_credentials
from acceldata_sdk.constants import FailureStrategy, PolicyType, RuleExecutionStatus

def ruleoperator_result(**context):
    xcom_key = f'{PolicyType.DATA_QUALITY.name}_46_execution_id'
    task_instance = context['ti']
    # pull the execution id from xcom
    execution_id = task_instance.xcom_pull(key=xcom_key)
    if execution_id is not None:
        # `adoc_connection_id` represents the unique identifier for the connection established
        # between ADOC and Airflow.
        torch_client = TorchClient(**torch_credentials(conn_id=adoc_connection_id))
        result = torch_client.get_polcy_execution_result(policy_type=PolicyType.DATA_QUALITY,
                                                         execution_id=execution_id,
                                                    failure_strategy=FailureStrategy.FailOnError)
        if result.execution.resultStatus == RuleExecutionStatus.ERRORED:
            print(result.execution.executionError)
```



#### Query the Status Using get_policy_status

`get_policy_status` is a helper function that can query the current status of the policy executed using the operator.

The parameter for get_policy_status include:

| Parameter | Description | 
| ---- | ---- | 
| policy_type | A `PolicyType` parameter used to specify the policy type. It is a mandatory parameter. It is an enum which will take values from constants as `PolicyType.DATA_QUALITY` or `PolicyType.RECONCILIATION`. | 
| execution_id | A **String** parameter specifying the execution id for which users want to query the results. It is a mandatory parameter. | 


You need to pull the execution id from xcom using the same key {`policy_type.name`}_{`policy_id`}_execution_id which was pushed by `ExecutePolicyOperator`. Replace the policy_type and policy_id based on the policy. In this example the policy_type is `PolicyType.DATA_QUALITY.name` and the policy_id is `46`.

```python
from acceldata_sdk.torch_client import TorchClient
from acceldata_airflow_sdk.initialiser import torch_credentials
import acceldata_sdk.constants as const

def ruleoperator_status(**context):
    xcom_key = f'{const.PolicyType.DATA_QUALITY.name}_46_execution_id'
    task_instance = context['ti']
    # pull the execution id from xcom
    execution_id = task_instance.xcom_pull(key=xcom_key)
    if execution_id is not None:
        # `adoc_connection_id` represents the unique identifier for the connection established
        # between ADOC and Airflow.
        torch_client = TorchClient(**torch_credentials(conn_id=adoc_connection_id))
        result = torch_client.get_policy_status(policy_type=const.PolicyType.DATA_QUALITY,
                                                execution_id=execution_id)
        if result==const.RuleExecutionStatus.ERRORED:
            print("Policy execution encountered an error.")
```

