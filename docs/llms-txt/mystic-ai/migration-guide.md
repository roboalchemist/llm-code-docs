# Source: https://docs.mystic.ai/docs/migration-guide.md

# Migration guide

How to migrate to v2 (i.e. API V4)

While the new version of Mystic should feel very similar to the previous one there are a few important changes you should be aware of.

## Getting started

You should be able to authenticate as you did previously and your existing API tokens should all work. You will probably need to re-authenticate with the new API by running:

```
pipeline cluster login catalyst-api API_TOKEN -u https://www.mystic.ai -a
```

## Naming conventions

All usernames, pipeline names, etc. are now required to be lowercase (as Docker image names do not support uppercase letters). Data from the previous version of the API has been migrated over and lowercased where necessary.

## Uploading pipelines

The most significant change in the Mystic V4 API is the way pipelines are created and uploaded.

The Python syntax for creating a pipeline has not changed, however pipelines are now built and uploaded using Docker (previously all Python code had to be serialised and uploaded).

The benefits of using Docker to author pipelines is:

1. Running pipelines locally should be similar as possible to running pipelines on Mystic's platform. This means if your pipeline is working locally, it should (in the majority of cases) work as expected when running on our servers.
2. Flexibility. In V3 you were able to create environments in order to specify any Python packages you needed. In V4 this is taken a level further, since you can now use any Python version you want (we recommend 3.10 and higher) and can also specify things such as OS-level packages you need.
3. Reliability and debugging are much improved. Running pipelines in containers means workloads are isolated from one another and things such as logs and errors are easier to report.
4. Scalability. Auto-scaling pipelines based on usage becomes a lot easier when everything is running in containers.

To see how to upload pipelines using Docker, please refer to the [Getting Started](https://docs.mystic.ai/docs/getting-started) guide.

## Goodbye environments!

Since pipelines are now packaged using Docker, there is no need for environments. As mentioned above, Docker containers provide a much more flexible way to specify the environment you need your code to run in. The pipeline configuration itself is specified in a YAML file that you define together with your Python code.

## Files

Using files for inputs and outputs is the same, but including extra files in your pipeline is now significantly easier. Any files in your pipeline's directory will be automatically copied into the docker image and accessible through the local filesystem!

## Running pipelines

Running pipelines is very similar to before. You can still use the `run_pipeline(...)`function to do this. If you're calling the API directly, you'll need to use the `/v4/runs`endpoints instead of `/v3/runs`

The main difference is that the response schema is slightly different. While the format of the results should be identical, some of the other fields may be slightly different, such the way errors are reported. You can view the API docs here: <https://docs.mystic.ai/reference/submit_run_v4_runs_post>

If you need time to migrate to the new V4 endpoints you can continue to use `/v3/runs` (and `/v3/pipeline-files`) for a short while, although the data returned may not be identical to before (for example there is no longer the concept of environments)

If you're running into any issues running your pipelines, please refer to the [Troubleshooting](https://docs.mystic.ai/docs/troubleshooting) guide.

## Scaling

The way pipelines deployed to Mystic scale has changed slightly. In the new version of our platform, pipelines that haven't been used for some time will be scaled down. This means the next time a run is executed against that pipeline, you may get a HTTP 503 in response as there are no resources to handle the request. In the background, this will trigger a scaling-up request. It may take a little bit of time (normally no longer than a few minutes) for the pipeline to scale back up and become available again. If you're still getting 503 errors after more than 5 minutes please contact us and we can check if there was an issue deploying your pipeline.