# Source: https://docs.mystic.ai/docs/troubleshooting.md

# Troubleshooting

What to do when your pipeline is not working

There are generally 2 types of errors you'll run into when building a new pipeline:

1. Build-time errors
2. Run-time errors

## Build-time errors

Pipeline Docker images are built on your local machine, so normally if there is an error during this stage it should be reported directly in your terminal. If the error is not clear there are a couple of things you can try:

1. Make sure you're using the latest version of the pipeline-ai library (you can do this using `pip install -U pipeline-ai`)
2. Double-check the syntax of your `pipeline.yaml` file, paying particular attention to your pipeline's requirements

## Run-time errors

If you're getting errors running your pipeline, first check what type of error it is.

### 503 errors

Mystic scales pipelines up and down based on traffic. If a particular pipeline has not been used for a while it will be scaled down. This means the next time a run is made against that pipeline, you will get a 503 error, which signifies there are no compute resources to satisfy the request. In the background, your pipeline will be scaled up, so you should be able to use it again within a few minutes (the time it takes for a pipeline to become ready depends on a few factors such as the hardware it's running on and the time your pipeline takes to run any startup functions).

You can check how many instances there are of a particular pipeline running by using the `/v4/pipelines/<pipeline_id>/scaling` endpoint.

If you're still getting 503 errors after more than 5 minutes please contact us and we can look into it.

### Pipeline errors

If the error type is `pipeline_error` or `startup_error` then there's likely an issue with your Pipeline, either during pipeline startup or at inference time.

Here are some tips for resolving these issues:

#### 1. Try running your pipeline locally

One of the benefits of the Mystic platform is that we run everything in containers. Therefore, if your pipeline runs locally, then (most of the time) it should run on our cloud.

You can run your pipeline locally using the `pipeline container up` command. For more info, refer to the [Getting Started](https://docs.mystic.ai/docs/getting-started) guide.

There will be certain cases in which you won't be able to run your pipeline locally (for example, if you need access to a particular GPU). If this is the case, check out the next tips.

#### 2. Review the error traceback

If there is a pipeline error or startup error, you should see a `traceback` returned in the API response. This is a copy of the Python traceback for the exception that was raised.

#### 3. Look at the run logs

You can check the logs for a run using the pipeline CLI or the API. This shows you all the logs that were captured during pipeline execution.

For the CLI, you can use the `pipeline logs run <run_id>` command.

Using the API, you can call the `/v4/logs/run/<run_id>` endpoint.

#### 4. Pipeline startup errors

If you receive a `startup_error` then in addition to the error message and traceback, you can also view the logs of your pipeline during startup.

For the CLI, you can use the `pipeline logs startup <pipeline_id> command`.

Using the API, you can call the `/v4/logs/pipeline-startup/<pipeline_id_or_pointer>` endpoint.

### Unknown errors

If the error type is `unknown` then please contact our support at <support@mystic.ai> or on [Discord](https://discord.gg/7REbAX5v3N). If you have a `request_id` in your error, please provide this too as it will make debugging the issue a lot easier.