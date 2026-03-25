# Source: https://docs.acceldata.io/documentation/context-switching-in-heterogeneous-pipelines.md

# Context Switching in Heterogeneous Pipelines


## Introduction

In some ETL pipelines, it is possible to have a DAG dependent on another. In such cases, you may want to represent and track both DAGs as part of a single pipeline in ADOC. This article will describe how one can achieve that.

## Summary

This guide demonstrates a context switching between two ETL pipelines.


![](https://uploads.developerhub.io/prod/Yoq2/7imjvjih3wca14hbktz6kvisjtycyg3tt1zqdmrzxk25cgfbnh4okd8g2nghme41.png)


In this example scenario, the ADOC pipeline run begins in dag 1 and ends in dag 2.

### DAG1

In dag1 `override_success_callback=True` is set in the `DAG`  ensuring that the new pipeline_run is not closed at the end of dag1. In addition to that, `continuation_id` is passed in the `TorchInitializer` task which will be used to link this run of dag1 to a specific run of dag2.


```python
dag = DAG(
    dag_id='demo_donot_end_pipeline_run',
    schedule_interval=None,
    default_args=default_args,
    start_date=datetime(2022, 5, 11),
    on_success_callback=_send_success_event,
    on_failure_callback=_send_failure_event,
    override_success_callback=True,
    override_failure_callback=True
)

torch_initializer_task = TorchInitializer(
    task_id='torch_pipeline_initializer',
    pipeline_uid=pipeline_uid,
    pipeline_name=pipeline_name,
    continuation_id=continuation_id,
    dag=dag,
    meta=PipelineMetadata(owner='Demo', team='demo_team', codeLocation='...')
```




### DAG2

In dag2, `create pipeline=False` is set in the `TorchInitializer` task, ensuring that when TorchInitializer is called in dag2, a new pipeline run is not started. The dag2`TorchInitializer` task is passed the same `continuation_id` as dag1, which will be used to link this run of dag2 to the run of dag1.


```python
dag = DAG(
    dag_id='demo_donot_start_pipeline_run',
    schedule_interval=None,
    default_args=default_args,
    start_date=datetime(2022, 5, 11),
    on_success_callback=_send_success_event,
    on_failure_callback=_send_failure_event
)

# create_pipeline=False ensures that a new pipeline_run is not started when TorchInitializer is called
torch_initializer_task = TorchInitializer(
    task_id='torch_pipeline_initializer',
    pipeline_uid=pipeline_uid,
    pipeline_name=pipeline_name,
    dag=dag,
    continuation_id=f"{{{{ task_instance.xcom_pull(key='continuation_id') }}}}",
    create_pipeline=False
)
```




## Conclusion

In this guide, we learnt how to write an Airflow DAG when the ADOC pipeline run is not closed at the end of the dag run and the same pipeline run is continued in another and context is passed between both dags.


> Here is an example demonstrating a context switch happening between two Airflow DAGs. This is a working code example that you can test on your own.> > [Context Switching](https://bitbucket.org/acceldata/ad-pipelines-integ-example/src/master/airflow/full_code/03example/)


