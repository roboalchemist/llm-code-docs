# Cortex Documentation

Source: https://docs.cortexlabs.com/llms-full.txt

---

# Get started

## Install the CLI

```bash
$ pip install cortex
```

See [here](https://docs.cortexlabs.com/clients/install) for alternative installation options.

## Create a cluster

* [Launch a Cortex cluster on your AWS account](https://docs.cortexlabs.com/clusters/cortex-cloud-on-aws/install)
* [Launch a Cortex cluster on your GCP account](https://docs.cortexlabs.com/clusters/cortex-cloud-on-gcp/install)
* [Install Cortex on your Kubernetes cluster](https://docs.cortexlabs.com/clusters/cortex-core-on-kubernetes/install)

## Run inference workloads

* [Realtime API](https://docs.cortexlabs.com/workloads/realtime-apis/example)
* [Batch API](https://docs.cortexlabs.com/workloads/batch-apis/example)
* [Task API](https://docs.cortexlabs.com/workloads/task-apis/example)


# Install

## Install with pip

To install the latest version:

```bash
pip install cortex
```

To install or upgrade to a specific version (e.g. v0.28.0):

```bash
pip install cortex==0.28.0
```

To upgrade to the latest version:

```bash
pip install --upgrade cortex
```

## Install without the Python client

```bash
# For example to download CLI version 0.28.0 (Note the "v"):
$ bash -c "$(curl -sS https://raw.githubusercontent.com/cortexlabs/cortex/v0.28.0/get-cli.sh)"
```

By default, the Cortex CLI is installed at `/usr/local/bin/cortex`. To install the executable elsewhere, export the `CORTEX_INSTALL_PATH` environment variable to your desired location before running the command above.

## Changing the CLI/client configuration directory

By default, the Cortex CLI/client creates a directory at `~/.cortex/` and uses it to store environment configuration. To use a different directory, export the `CORTEX_CLI_CONFIG_DIR` environment variable before running any `cortex` commands.


# CLI commands

## deploy

```
create or update apis

Usage:
  cortex deploy [CONFIG_FILE] [flags]

Flags:
  -e, --env string      environment to use
  -f, --force           override the in-progress api update
  -y, --yes             skip prompts
  -o, --output string   output format: one of pretty|json (default "pretty")
  -h, --help            help for deploy
```

## get

```
get information about apis or jobs

Usage:
  cortex get [API_NAME] [JOB_ID] [flags]

Flags:
  -e, --env string      environment to use
  -w, --watch           re-run the command every 2 seconds
  -o, --output string   output format: one of pretty|json (default "pretty")
  -v, --verbose         show additional information (only applies to pretty output format)
  -h, --help            help for get
```

## logs

```
stream logs from a single replica of an api or a single worker for a job

Usage:
  cortex logs API_NAME [JOB_ID] [flags]

Flags:
  -e, --env string   environment to use
  -y, --yes          skip prompts
  -h, --help         help for logs
```

## patch

```
update API configuration for a deployed API

Usage:
  cortex patch [CONFIG_FILE] [flags]

Flags:
  -e, --env string      environment to use
  -f, --force           override the in-progress api update
  -o, --output string   output format: one of pretty|json (default "pretty")
  -h, --help            help for patch
```

## refresh

```
restart all replicas for an api (without downtime)

Usage:
  cortex refresh API_NAME [flags]

Flags:
  -e, --env string      environment to use
  -f, --force           override the in-progress api update
  -o, --output string   output format: one of pretty|json (default "pretty")
  -h, --help            help for refresh
```

## delete

```
delete any kind of api or stop a batch job

Usage:
  cortex delete API_NAME [JOB_ID] [flags]

Flags:
  -e, --env string      environment to use
  -f, --force           delete the api without confirmation
  -c, --keep-cache      keep cached data for the api
  -o, --output string   output format: one of pretty|json (default "pretty")
  -h, --help            help for delete
```

## cluster up

```
spin up a cluster on aws

Usage:
  cortex cluster up [flags]

Flags:
  -c, --config string               path to a cluster configuration file
      --aws-key string              aws access key id
      --aws-secret string           aws secret access key
      --cluster-aws-key string      aws access key id to be used by the cluster
      --cluster-aws-secret string   aws secret access key to be used by the cluster
  -e, --configure-env string        name of environment to configure (default "aws")
  -y, --yes                         skip prompts
  -h, --help                        help for up
```

## cluster info

```
get information about a cluster

Usage:
  cortex cluster info [flags]

Flags:
  -c, --config string          path to a cluster configuration file
  -n, --name string            name of the cluster
  -r, --region string          aws region of the cluster
      --aws-key string         aws access key id
      --aws-secret string      aws secret access key
  -e, --configure-env string   name of environment to configure
  -d, --debug                  save the current cluster state to a file
  -y, --yes                    skip prompts
  -h, --help                   help for info
```

## cluster configure

```
update a cluster's configuration

Usage:
  cortex cluster configure [flags]

Flags:
  -c, --config string               path to a cluster configuration file
      --aws-key string              aws access key id
      --aws-secret string           aws secret access key
      --cluster-aws-key string      aws access key id to be used by the cluster
      --cluster-aws-secret string   aws secret access key to be used by the cluster
  -e, --configure-env string        name of environment to configure
  -y, --yes                         skip prompts
  -h, --help                        help for configure
```

## cluster down

```
spin down a cluster

Usage:
  cortex cluster down [flags]

Flags:
  -c, --config string       path to a cluster configuration file
  -n, --name string         name of the cluster
  -r, --region string       aws region of the cluster
      --aws-key string      aws access key id
      --aws-secret string   aws secret access key
  -y, --yes                 skip prompts
  -h, --help                help for down
```

## cluster export

```
download the code and configuration for APIs

Usage:
  cortex cluster export [API_NAME] [API_ID] [flags]

Flags:
  -c, --config string       path to a cluster configuration file
  -n, --name string         name of the cluster
  -r, --region string       aws region of the cluster
      --aws-key string      aws access key id
      --aws-secret string   aws secret access key
  -h, --help                help for export
```

## cluster-gcp up

```
spin up a cluster on gcp

Usage:
  cortex cluster-gcp up [flags]

Flags:
  -c, --config string          path to a cluster configuration file
  -e, --configure-env string   name of environment to configure (default "gcp")
  -y, --yes                    skip prompts
  -h, --help                   help for up
```

## cluster-gcp info

```
get information about a cluster

Usage:
  cortex cluster-gcp info [flags]

Flags:
  -c, --config string          path to a cluster configuration file
  -n, --name string            name of the cluster
  -p, --project string         gcp project id
  -z, --zone string            gcp zone of the cluster
  -e, --configure-env string   name of environment to configure
  -d, --debug                  save the current cluster state to a file
  -y, --yes                    skip prompts
  -h, --help                   help for info
```

## cluster-gcp down

```
spin down a cluster

Usage:
  cortex cluster-gcp down [flags]

Flags:
  -c, --config string    path to a cluster configuration file
  -n, --name string      name of the cluster
  -p, --project string   gcp project id
  -z, --zone string      gcp zone of the cluster
  -y, --yes              skip prompts
  -h, --help             help for down
```

## env configure

```
configure an environment

Usage:
  cortex env configure [ENVIRONMENT_NAME] [flags]

Flags:
  -o, --operator-endpoint string   set the operator endpoint without prompting
  -h, --help                       help for configure
```

## env list

```
list all configured environments

Usage:
  cortex env list [flags]

Flags:
  -o, --output string   output format: one of pretty|json (default "pretty")
  -h, --help            help for list
```

## env default

```
set the default environment

Usage:
  cortex env default [ENVIRONMENT_NAME] [flags]

Flags:
  -h, --help   help for default
```

## env delete

```
delete an environment configuration

Usage:
  cortex env delete [ENVIRONMENT_NAME] [flags]

Flags:
  -h, --help   help for delete
```

## version

```
print the cli and cluster versions

Usage:
  cortex version [flags]

Flags:
  -e, --env string   environment to use
  -h, --help         help for version
```

## completion

```
generate shell completion scripts

to enable cortex shell completion:
    bash:
        add this to ~/.bash_profile (mac) or ~/.bashrc (linux):
            source <(cortex completion bash)

        note: bash-completion must be installed on your system; example installation instructions:
            mac:
                1) install bash completion:
                   brew install bash-completion
                2) add this to your ~/.bash_profile:
                   source $(brew --prefix)/etc/bash_completion
                3) log out and back in, or close your terminal window and reopen it
            ubuntu:
                1) install bash completion:
                   apt update && apt install -y bash-completion  # you may need sudo
                2) open ~/.bashrc and uncomment the bash completion section, or add this:
                   if [ -f /etc/bash_completion ] && ! shopt -oq posix; then . /etc/bash_completion; fi
                3) log out and back in, or close your terminal window and reopen it

    zsh:
        option 1:
            add this to ~/.zshrc:
                source <(cortex completion zsh)
            if that failed, you can try adding this line (above the source command you just added):
                autoload -Uz compinit && compinit
        option 2:
            create a _cortex file in your fpath, for example:
                cortex completion zsh > /usr/local/share/zsh/site-functions/_cortex

Note: this will also add the "cx" alias for cortex for convenience

Usage:
  cortex completion SHELL [flags]

Flags:
  -h, --help   help for completion
```


# Python API

## Python API

* [cortex](#cortex)
  * [client](#client)
  * [new\_client](#new_client)
  * [env\_list](#env_list)
  * [env\_delete](#env_delete)
* [cortex.client.Client](#cortex-client-client)
  * [create\_api](#create_api)
  * [get\_api](#get_api)
  * [list\_apis](#list_apis)
  * [get\_job](#get_job)
  * [refresh](#refresh)
  * [patch](#patch)
  * [delete\_api](#delete_api)
  * [stop\_job](#stop_job)
  * [stream\_api\_logs](#stream_api_logs)
  * [stream\_job\_logs](#stream_job_logs)

## cortex

### client

```python
client(env: str) -> Client
```

Initialize a client based on the specified environment.

**Arguments**:

* `env` - Name of the environment to use.

**Returns**:

Cortex client that can be used to deploy and manage APIs in the specified environment.

### new\_client

```python
new_client(name: str, operator_endpoint: str) -> Client
```

Create a new environment to connect to an existing Cortex Cluster, and initialize a client to deploy and manage APIs on that cluster.

**Arguments**:

* `name` - Name of the environment to create.
* `operator_endpoint` - The endpoint for the operator of your Cortex Cluster. You can get this endpoint by running the CLI command `cortex cluster info` for an AWS provider or `cortex cluster-gcp info` for a GCP provider.

**Returns**:

Cortex client that can be used to deploy and manage APIs on a Cortex Cluster.

### env\_list

```python
env_list() -> list
```

List all environments configured on this machine.

### env\_delete

```python
env_delete(name: str)
```

Delete an environment configured on this machine.

**Arguments**:

* `name` - Name of the environment to delete.

## cortex.client.Client

### create\_api

```python
 | create_api(api_spec: dict, predictor=None, task=None, requirements=[], conda_packages=[], project_dir: Optional[str] = None, force: bool = True, wait: bool = False) -> list
```

Deploy an API.

**Arguments**:

* `api_spec` - A dictionary defining a single Cortex API. See <https://docs.cortex.dev/v/0.28/> for schema.
* `predictor` - A Cortex Predictor class implementation. Not required for TaskAPI/TrafficSplitter kinds.
* `task` - A callable class/function implementation. Not required for RealtimeAPI/BatchAPI/TrafficSplitter kinds.
* `requirements` - A list of PyPI dependencies that will be installed before the predictor class implementation is invoked.
* `conda_packages` - A list of Conda dependencies that will be installed before the predictor class implementation is invoked.
* `project_dir` - Path to a python project.
* `force` - Override any in-progress api updates.
* `wait` - Streams logs until the APIs are ready.

**Returns**:

Deployment status, API specification, and endpoint for each API.

### get\_api

```python
 | get_api(api_name: str) -> dict
```

Get information about an API.

**Arguments**:

* `api_name` - Name of the API.

**Returns**:

Information about the API, including the API specification, endpoint, status, and metrics (if applicable).

### list\_apis

```python
 | list_apis() -> list
```

List all APIs in the environment.

**Returns**:

List of APIs, including information such as the API specification, endpoint, status, and metrics (if applicable).

### get\_job

```python
 | get_job(api_name: str, job_id: str) -> dict
```

Get information about a submitted job.

**Arguments**:

* `api_name` - Name of the Batch/Task API.
* `job_id` - Job ID.

**Returns**:

Information about the job, including the job status, worker status, and job progress.

### refresh

```python
 | refresh(api_name: str, force: bool = False)
```

Restart all of the replicas for a Realtime API without downtime.

**Arguments**:

* `api_name` - Name of the API to refresh.
* `force` - Override an already in-progress API update.

### patch

```python
 | patch(api_spec: dict, force: bool = False) -> dict
```

Update the api specification for an API that has already been deployed.

**Arguments**:

* `api_spec` - The new api specification to apply
* `force` - Override an already in-progress API update.

### delete\_api

```python
 | delete_api(api_name: str, keep_cache: bool = False)
```

Delete an API.

**Arguments**:

* `api_name` - Name of the API to delete.
* `keep_cache` - Whether to retain the cached data for this API.

### stop\_job

```python
 | stop_job(api_name: str, job_id: str, keep_cache: bool = False)
```

Stop a running job.

**Arguments**:

* `api_name` - Name of the Batch/Task API.
* `job_id` - ID of the Job to stop.

### stream\_api\_logs

```python
 | stream_api_logs(api_name: str)
```

Stream the logs of an API.

**Arguments**:

* `api_name` - Name of the API.

### stream\_job\_logs

```python
 | stream_job_logs(api_name: str, job_id: str)
```

Stream the logs of a Job.

**Arguments**:

* `api_name` - Name of the Batch API.
* `job_id` - Job ID.


# Environments

When you create a cluster with `cortex cluster up`, an environment named `aws` or `gcp` is automatically created to point to your cluster and is configured to be the default environment. You can name the environment something else via the `--configure-env` flag, e.g. `cortex cluster up --configure-env prod`. You can also use the `--configure-env` flag with `cortex cluster info` and `cortex cluster configure` to create / update the specified environment.

You can list your environments with `cortex env list`, change the default environment with `cortex env default`, delete an environment with `cortex env delete`, and create/update an environment with `cortex env configure`.

## Multiple clusters

```bash
cortex cluster up --config cluster1.yaml --configure-env cluster1  # configures the cluster1 env
cortex cluster up --config cluster2.yaml --configure-env cluster2  # configures the cluster2 env

cortex deploy --env cluster1
cortex logs my-api --env cluster1
cortex delete my-api --env cluster1

cortex deploy --env cluster2
cortex logs my-api --env cluster2
cortex delete my-api --env cluster2
```

## Multiple clusters, if you omitted the `--configure-env` on `cortex cluster up`

```bash
cortex cluster info --config cluster1.yaml --configure-env cluster1  # configures the cluster1 env
cortex cluster info --config cluster2.yaml --configure-env cluster2  # configures the cluster2 env

cortex deploy --env cluster1
cortex logs my-api --env cluster1
cortex delete my-api --env cluster1

cortex deploy --env cluster2
cortex logs my-api --env cluster2
cortex delete my-api --env cluster2
```

## Configure `cortex` CLI to connect to an existing cluster

If you are installing the `cortex` CLI on a new machine, you can configure it to access an existing Cortex cluster.

On the machine which already has the CLI configured, run:

```bash
cortex env list
```

Take note of the environment name and operator endpoint of the desired environment.

On your new machine, run:

```bash
cortex env configure
```


# Telemetry

By default, Cortex sends anonymous usage data to Cortex Labs.

## What data is collected?

If telemetry is enabled, events and errors are collected. Each time you run a command an event will be sent with a randomly generated unique CLI ID and the name of the command. For example, if you run `cortex get`, Cortex Labs will receive an event of the structure `{id: 1234, command: "get"}`. In addition, the operator sends heartbeats that include cluster metrics like the types of instances running in your cluster.

## How do I opt out?

If you'd like to disable telemetry, modify your `~/.cortex/cli.yaml` file (or create it if it doesn't exist) and add `telemetry: false` before spinning up your cluster.


# Uninstall

## Uninstall (if installed with pip)

```bash
pip uninstall cortex
rm -rf ~/.cortex
```

## Uninstall (if installed without pip)

```bash
rm /usr/local/bin/cortex
rm -rf ~/.cortex
```


# Realtime APIs


# Example

Create APIs that can respond to prediction requests in real-time.

## Implement

```bash
$ mkdir text-generator && cd text-generator
$ touch predictor.py requirements.txt text_generator.yaml
```

```python
# predictor.py

from transformers import pipeline

class PythonPredictor:
    def __init__(self, config):
        self.model = pipeline(task="text-generation")

    def predict(self, payload):
        return self.model(payload["text"])[0]
```

```python
# requirements.txt

transformers
torch
```

```yaml
# text_generator.yaml

- name: text-generator
  kind: RealtimeAPI
  predictor:
    type: python
    path: predictor.py
  compute:
    gpu: 1
```

## Deploy

```bash
$ cortex deploy text_generator.yaml
```

## Monitor

```bash
$ cortex get text-generator --watch
```

## Stream logs

```bash
$ cortex logs text-generator
```

## Make a request

```bash
$ curl http://***.elb.us-west-2.amazonaws.com/text-generator -X POST -H "Content-Type: application/json" -d '{"text": "hello world"}'
```

## Delete

```bash
$ cortex delete text-generator
```


# Predictor

Which Predictor you use depends on how your model is exported:

* [TensorFlow Predictor](#tensorflow-predictor) if your model is exported as a TensorFlow `SavedModel`
* [ONNX Predictor](#onnx-predictor) if your model is exported in the ONNX format
* [Python Predictor](#python-predictor) for all other cases

The response type of the predictor can vary depending on your requirements, see [API responses](#api-responses) below.

## Project files

Cortex makes all files in the project directory (i.e. the directory which contains `cortex.yaml`) available for use in your Predictor implementation. Python bytecode files (`*.pyc`, `*.pyo`, `*.pyd`), files or folders that start with `.`, and the api configuration file (e.g. `cortex.yaml`) are excluded.

The following files can also be added at the root of the project's directory:

* `.cortexignore` file, which follows the same syntax and behavior as a [.gitignore file](https://git-scm.com/docs/gitignore).
* `.env` file, which exports environment variables that can be used in the predictor. Each line of this file must follow the `VARIABLE=value` format.

For example, if your directory looks like this:

```
./my-classifier/
├── cortex.yaml
├── values.json
├── predictor.py
├── ...
└── requirements.txt
```

You can access `values.json` in your Predictor like this:

```python
import json

class PythonPredictor:
    def __init__(self, config):
        with open('values.json', 'r') as values_file:
            values = json.load(values_file)
        self.values = values
```

## Python Predictor

### Interface

```python
# initialization code and variables can be declared here in global scope

class PythonPredictor:
    def __init__(self, config, python_client):
        """(Required) Called once before the API becomes available. Performs
        setup such as downloading/initializing the model or downloading a
        vocabulary.

        Args:
            config (required): Dictionary passed from API configuration (if
                specified). This may contain information on where to download
                the model and/or metadata.
            python_client (optional): Python client which is used to retrieve
                models for prediction. This should be saved for use in predict().
                Required when `predictor.multi_model_reloading` is specified in the api configuration.
        """
        self.client = python_client # optional

    def predict(self, payload, query_params, headers):
        """(Required) Called once per request. Preprocesses the request payload
        (if necessary), runs inference, and postprocesses the inference output
        (if necessary).

        Args:
            payload (optional): The request payload (see below for the possible
                payload types).
            query_params (optional): A dictionary of the query parameters used
                in the request.
            headers (optional): A dictionary of the headers sent in the request.

        Returns:
            Prediction or a batch of predictions.
        """
        pass

    def post_predict(self, response, payload, query_params, headers):
        """(Optional) Called in the background after returning a response.
        Useful for tasks that the client doesn't need to wait on before
        receiving a response such as recording metrics or storing results.

        Note: post_predict() and predict() run in the same thread pool. The
        size of the thread pool can be increased by updating
        `threads_per_process` in the api configuration yaml.

        Args:
            response (optional): The response as returned by the predict method.
            payload (optional): The request payload (see below for the possible
                payload types).
            query_params (optional): A dictionary of the query parameters used
                in the request.
            headers (optional): A dictionary of the headers sent in the request.
        """
        pass

    def load_model(self, model_path):
        """(Optional) Called by Cortex to load a model when necessary.

        This method is required when `predictor.multi_model_reloading`
        field is specified in the api configuration.

        Warning: this method must not make any modification to the model's
        contents on disk.

        Args:
            model_path: The path to the model on disk.

        Returns:
            The loaded model from disk. The returned object is what
            self.client.get_model() will return.
        """
        pass
```

When explicit model paths are specified in the Python predictor's API configuration, Cortex provides a `python_client` to your Predictor's constructor. `python_client` is an instance of [PythonClient](https://github.com/cortexlabs/cortex/tree/0.28/pkg/cortex/serve/cortex_internal/lib/client/python.py) that is used to load model(s) (it calls the `load_model()` method of your predictor, which must be defined when using explicit model paths). It should be saved as an instance variable in your Predictor, and your `predict()` function should call `python_client.get_model()` to load your model for inference. Preprocessing of the JSON payload and postprocessing of predictions can be implemented in your `predict()` function as well.

When multiple models are defined using the Predictor's `models` field, the `python_client.get_model()` method expects an argument `model_name` which must hold the name of the model that you want to load (for example: `self.client.get_model("text-generator")`). There is also an optional second argument to specify the model version.

For proper separation of concerns, it is recommended to use the constructor's `config` parameter for information such as from where to download the model and initialization files, or any configurable model parameters. You define `config` in your API configuration, and it is passed through to your Predictor's constructor.

Your API can accept requests with different types of payloads such as `JSON`-parseable, `bytes` or `starlette.datastructures.FormData` data. Navigate to the [API requests](#api-requests) section to learn about how headers can be used to change the type of `payload` that is passed into your `predict` method.

Your `predictor` method can return different types of objects such as `JSON`-parseable, `string`, and `bytes` objects. Navigate to the [API responses](#api-responses) section to learn about how to configure your `predictor` method to respond with different response codes and content-types.

## TensorFlow Predictor

**Uses TensorFlow version 2.3.0 by default**

### Interface

```python
class TensorFlowPredictor:
    def __init__(self, tensorflow_client, config):
        """(Required) Called once before the API becomes available. Performs
        setup such as downloading/initializing a vocabulary.

        Args:
            tensorflow_client (required): TensorFlow client which is used to
                make predictions. This should be saved for use in predict().
            config (required): Dictionary passed from API configuration (if
                specified).
        """
        self.client = tensorflow_client
        # Additional initialization may be done here

    def predict(self, payload, query_params, headers):
        """(Required) Called once per request. Preprocesses the request payload
        (if necessary), runs inference (e.g. by calling
        self.client.predict(model_input)), and postprocesses the inference
        output (if necessary).

        Args:
            payload (optional): The request payload (see below for the possible
                payload types).
            query_params (optional): A dictionary of the query parameters used
                in the request.
            headers (optional): A dictionary of the headers sent in the request.

        Returns:
            Prediction or a batch of predictions.
        """
        pass

    def post_predict(self, response, payload, query_params, headers):
        """(Optional) Called in the background after returning a response.
        Useful for tasks that the client doesn't need to wait on before
        receiving a response such as recording metrics or storing results.

        Note: post_predict() and predict() run in the same thread pool. The
        size of the thread pool can be increased by updating
        `threads_per_process` in the api configuration yaml.

        Args:
            response (optional): The response as returned by the predict method.
            payload (optional): The request payload (see below for the possible
                payload types).
            query_params (optional): A dictionary of the query parameters used
                in the request.
            headers (optional): A dictionary of the headers sent in the request.
        """
        pass
```

Cortex provides a `tensorflow_client` to your Predictor's constructor. `tensorflow_client` is an instance of [TensorFlowClient](https://github.com/cortexlabs/cortex/tree/0.28/pkg/cortex/serve/cortex_internal/lib/client/tensorflow.py) that manages a connection to a TensorFlow Serving container to make predictions using your model. It should be saved as an instance variable in your Predictor, and your `predict()` function should call `tensorflow_client.predict()` to make an inference with your exported TensorFlow model. Preprocessing of the JSON payload and postprocessing of predictions can be implemented in your `predict()` function as well.

When multiple models are defined using the Predictor's `models` field, the `tensorflow_client.predict()` method expects a second argument `model_name` which must hold the name of the model that you want to use for inference (for example: `self.client.predict(payload, "text-generator")`). There is also an optional third argument to specify the model version.

For proper separation of concerns, it is recommended to use the constructor's `config` parameter for information such as configurable model parameters or download links for initialization files. You define `config` in your API configuration, and it is passed through to your Predictor's constructor.

Your API can accept requests with different types of payloads such as `JSON`-parseable, `bytes` or `starlette.datastructures.FormData` data. Navigate to the [API requests](#api-requests) section to learn about how headers can be used to change the type of `payload` that is passed into your `predict` method.

Your `predictor` method can return different types of objects such as `JSON`-parseable, `string`, and `bytes` objects. Navigate to the [API responses](#api-responses) section to learn about how to configure your `predictor` method to respond with different response codes and content-types.

If you need to share files between your predictor implementation and the TensorFlow Serving container, you can create a new directory within `/mnt` (e.g. `/mnt/user`) and write files to it. The entire `/mnt` directory is shared between containers, but do not write to any of the directories in `/mnt` that already exist (they are used internally by Cortex).

## ONNX Predictor

**Uses ONNX Runtime version 1.4.0 by default**

### Interface

```python
class ONNXPredictor:
    def __init__(self, onnx_client, config):
        """(Required) Called once before the API becomes available. Performs
        setup such as downloading/initializing a vocabulary.

        Args:
            onnx_client (required): ONNX client which is used to make
                predictions. This should be saved for use in predict().
            config (required): Dictionary passed from API configuration (if
                specified).
        """
        self.client = onnx_client
        # Additional initialization may be done here

    def predict(self, payload, query_params, headers):
        """(Required) Called once per request. Preprocesses the request payload
        (if necessary), runs inference (e.g. by calling
        self.client.predict(model_input)), and postprocesses the inference
        output (if necessary).

        Args:
            payload (optional): The request payload (see below for the possible
                payload types).
            query_params (optional): A dictionary of the query parameters used
                in the request.
            headers (optional): A dictionary of the headers sent in the request.

        Returns:
            Prediction or a batch of predictions.
        """
        pass

    def post_predict(self, response, payload, query_params, headers):
        """(Optional) Called in the background after returning a response.
        Useful for tasks that the client doesn't need to wait on before
        receiving a response such as recording metrics or storing results.

        Note: post_predict() and predict() run in the same thread pool. The
        size of the thread pool can be increased by updating
        `threads_per_process` in the api configuration yaml.

        Args:
            response (optional): The response as returned by the predict method.
            payload (optional): The request payload (see below for the possible
                payload types).
            query_params (optional): A dictionary of the query parameters used
                in the request.
            headers (optional): A dictionary of the headers sent in the request.
        """
        pass
```

Cortex provides an `onnx_client` to your Predictor's constructor. `onnx_client` is an instance of [ONNXClient](https://github.com/cortexlabs/cortex/tree/0.28/pkg/cortex/serve/cortex_internal/lib/client/onnx.py) that manages an ONNX Runtime session to make predictions using your model. It should be saved as an instance variable in your Predictor, and your `predict()` function should call `onnx_client.predict()` to make an inference with your exported ONNX model. Preprocessing of the JSON payload and postprocessing of predictions can be implemented in your `predict()` function as well.

When multiple models are defined using the Predictor's `models` field, the `onnx_client.predict()` method expects a second argument `model_name` which must hold the name of the model that you want to use for inference (for example: `self.client.predict(model_input, "text-generator")`). There is also an optional third argument to specify the model version.

For proper separation of concerns, it is recommended to use the constructor's `config` parameter for information such as configurable model parameters or download links for initialization files. You define `config` in your API configuration, and it is passed through to your Predictor's constructor.

Your API can accept requests with different types of payloads such as `JSON`-parseable, `bytes` or `starlette.datastructures.FormData` data. Navigate to the [API requests](#api-requests) section to learn about how headers can be used to change the type of `payload` that is passed into your `predict` method.

Your `predictor` method can return different types of objects such as `JSON`-parseable, `string`, and `bytes` objects. Navigate to the [API responses](#api-responses) section to learn about how to configure your `predictor` method to respond with different response codes and content-types.

## API requests

The type of the `payload` parameter in `predict(self, payload)` can vary based on the content type of the request. The `payload` parameter is parsed according to the `Content-Type` header in the request. Here are the parsing rules (see below for examples):

1. For `Content-Type: application/json`, `payload` will be the parsed JSON body.
2. For `Content-Type: multipart/form-data` / `Content-Type: application/x-www-form-urlencoded`, `payload` will be `starlette.datastructures.FormData` (key-value pairs where the values are strings for text data, or `starlette.datastructures.UploadFile` for file uploads; see [Starlette's documentation](https://www.starlette.io/requests/#request-files)).
3. For `Content-Type: text/plain`, `payload` will be a string. `utf-8` encoding is assumed, unless specified otherwise (e.g. via `Content-Type: text/plain; charset=us-ascii`)
4. For all other `Content-Type` values, `payload` will be the raw `bytes` of the request body.

Here are some examples:

### JSON data

#### Making the request

```bash
$ curl http://***.amazonaws.com/my-api \
    -X POST -H "Content-Type: application/json" \
    -d '{"key": "value"}'
```

#### Reading the payload

When sending a JSON payload, the `payload` parameter will be a Python object:

```python
class PythonPredictor:
    def __init__(self, config):
        pass

    def predict(self, payload):
        print(payload["key"])  # prints "value"
```

### Binary data

#### Making the request

```bash
$ curl http://***.amazonaws.com/my-api \
    -X POST -H "Content-Type: application/octet-stream" \
    --data-binary @object.pkl
```

#### Reading the payload

Since the `Content-Type: application/octet-stream` header is used, the `payload` parameter will be a `bytes` object:

```python
import pickle

class PythonPredictor:
    def __init__(self, config):
        pass

    def predict(self, payload):
        obj = pickle.loads(payload)
        print(obj["key"])  # prints "value"
```

Here's an example if the binary data is an image:

```python
from PIL import Image
import io

class PythonPredictor:
    def __init__(self, config):
        pass

    def predict(self, payload, headers):
        img = Image.open(io.BytesIO(payload))  # read the payload bytes as an image
        print(img.size)
```

### Form data (files)

#### Making the request

```bash
$ curl http://***.amazonaws.com/my-api \
    -X POST \
    -F "text=@text.txt" \
    -F "object=@object.pkl" \
    -F "image=@image.png"
```

#### Reading the payload

When sending files via form data, the `payload` parameter will be `starlette.datastructures.FormData` (key-value pairs where the values are `starlette.datastructures.UploadFile`, see [Starlette's documentation](https://www.starlette.io/requests/#request-files)). Either `Content-Type: multipart/form-data` or `Content-Type: application/x-www-form-urlencoded` can be used (typically `Content-Type: multipart/form-data` is used for files, and is the default in the examples above).

```python
from PIL import Image
import pickle

class PythonPredictor:
    def __init__(self, config):
        pass

    def predict(self, payload):
        text = payload["text"].file.read()
        print(text.decode("utf-8"))  # prints the contents of text.txt

        obj = pickle.load(payload["object"].file)
        print(obj["key"])  # prints "value" assuming `object.pkl` is a pickled dictionary {"key": "value"}

        img = Image.open(payload["image"].file)
        print(img.size)  # prints the dimensions of image.png
```

### Form data (text)

#### Making the request

```bash
$ curl http://***.amazonaws.com/my-api \
    -X POST \
    -d "key=value"
```

#### Reading the payload

When sending text via form data, the `payload` parameter will be `starlette.datastructures.FormData` (key-value pairs where the values are strings, see [Starlette's documentation](https://www.starlette.io/requests/#request-files)). Either `Content-Type: multipart/form-data` or `Content-Type: application/x-www-form-urlencoded` can be used (typically `Content-Type: application/x-www-form-urlencoded` is used for text, and is the default in the examples above).

```python
class PythonPredictor:
    def __init__(self, config):
        pass

    def predict(self, payload):
        print(payload["key"])  # will print "value"
```

### Text data

#### Making the request

```bash
$ curl http://***.amazonaws.com/my-api \
    -X POST -H "Content-Type: text/plain" \
    -d "hello world"
```

#### Reading the payload

Since the `Content-Type: text/plain` header is used, the `payload` parameter will be a `string` object:

```python
class PythonPredictor:
    def __init__(self, config):
        pass

    def predict(self, payload):
        print(payload)  # prints "hello world"
```

## API responses

The response of your `predict()` function may be:

1. A JSON-serializable object (*lists*, *dictionaries*, *numbers*, etc.)
2. A `string` object (e.g. `"class 1"`)
3. A `bytes` object (e.g. `bytes(4)` or `pickle.dumps(obj)`)
4. An instance of [starlette.responses.Response](https://www.starlette.io/responses/#response)

## Chaining APIs

It is possible to make requests from one API to another within a Cortex cluster. All running APIs are accessible from within the predictor at `http://api-<api_name>:8888/predict`, where `<api_name>` is the name of the API you are making a request to.

For example, if there is an api named `text-generator` running in the cluster, you could make a request to it from a different API by using:

```python
import requests

class PythonPredictor:
    def predict(self, payload):
        response = requests.post("http://api-text-generator:8888/predict", json={"text": "machine learning is"})
        # ...
```

Note that the autoscaling configuration (i.e. `target_replica_concurrency`) for the API that is making the request should be modified with the understanding that requests will still be considered "in-flight" with the first API as the request is being fulfilled in the second API (during which it will also be considered "in-flight" with the second API).

## Structured logging

You can use Cortex's logger in your predictor implemention to log in JSON. This will enrich your logs with Cortex's metadata, and you can add custom metadata to the logs by adding key value pairs to the `extra` key when using the logger. For example:

```python
...
from cortex_internal.lib.log import logger as cortex_logger

class PythonPredictor:
    def predict(self, payload):
        cortex_logger.info("received payload", extra={"payload": payload})
```

The dictionary passed in via the `extra` will be flattened by one level. e.g.

```
{"asctime": "2021-01-19 15:14:05,291", "levelname": "INFO", "message": "received payload", "process": 235, "payload": "this movie is awesome"}
```

To avoid overriding essential Cortex metadata, please refrain from specifying the following extra keys: `asctime`, `levelname`, `message`, `labels`, and `process`. Log lines greater than 5 MB in size will be ignored.


# Configuration

```yaml
- name: <string>
  kind: RealtimeAPI
  predictor: # detailed configuration below
  compute: # detailed configuration below
  autoscaling: # detailed configuration below
  update_strategy: # detailed configuration below
  networking: # detailed configuration below
```

## Predictor

### Python Predictor

```yaml
predictor:
  type: python
  path: <string>  # path to a python file with a PythonPredictor class definition, relative to the Cortex root (required)
  multi_model_reloading:  # use this to serve one or more models with live reloading (optional)
    path: <string> # S3/GCS path to an exported model directory (e.g. s3://my-bucket/exported_model/) (either this, 'dir', or 'paths' must be provided if 'multi_model_reloading' is specified)
    paths:  # list of S3/GCS paths to exported model directories (either this, 'dir', or 'path' must be provided if 'multi_model_reloading' is specified)
      - name: <string>  # unique name for the model (e.g. text-generator) (required)
        path: <string>  # S3/GCS path to an exported model directory (e.g. s3://my-bucket/exported_model/) (required)
      ...
    dir: <string>  # S3/GCS path to a directory containing multiple models (e.g. s3://my-bucket/models/) (either this, 'path', or 'paths' must be provided if 'multi_model_reloading' is specified)
    cache_size: <int>  # the number models to keep in memory (optional; all models are kept in memory by default)
    disk_cache_size: <int>  # the number of models to keep on disk (optional; all models are kept on disk by default)
  server_side_batching:  # (optional)
    max_batch_size: <int>  # the maximum number of requests to aggregate before running inference
    batch_interval: <duration>  # the maximum amount of time to spend waiting for additional requests before running inference on the batch of requests
  processes_per_replica: <int>  # the number of parallel serving processes to run on each replica (default: 1)
  threads_per_process: <int>  # the number of threads per process (default: 1)
  config: <string: value>  # arbitrary dictionary passed to the constructor of the Predictor (optional)
  python_path: <string>  # path to the root of your Python folder that will be appended to PYTHONPATH (default: folder containing cortex.yaml)
  image: <string>  # docker image to use for the Predictor (default: quay.io/cortexlabs/python-predictor-cpu:0.28.0, quay.io/cortexlabs/python-predictor-gpu:0.28.0, or quay.io/cortexlabs/python-predictor-inf:0.28.0 based on compute)
  env: <string: string>  # dictionary of environment variables
  log_level: <string>  # log level that can be "debug", "info", "warning" or "error" (default: "info")
  shm_size: <string>  # size of shared memory (/dev/shm) for sharing data between multiple processes, e.g. 64Mi or 1Gi (default: Null)
```

### TensorFlow Predictor

```yaml
predictor:
  type: tensorflow
  path: <string>  # path to a python file with a TensorFlowPredictor class definition, relative to the Cortex root (required)
  models:  # (required)
    path: <string> # S3/GCS path to an exported SavedModel directory (e.g. s3://my-bucket/exported_model/) (either this, 'dir', or 'paths' must be provided)
    paths:  # list of S3/GCS paths to exported SavedModel directories (either this, 'dir', or 'path' must be provided)
      - name: <string>  # unique name for the model (e.g. text-generator) (required)
        path: <string>  # S3/GCS path to an exported SavedModel directory (e.g. s3://my-bucket/exported_model/) (required)
        signature_key: <string>  # name of the signature def to use for prediction (required if your model has more than one signature def)
      ...
    dir: <string>  # S3/GCS path to a directory containing multiple SavedModel directories (e.g. s3://my-bucket/models/) (either this, 'path', or 'paths' must be provided)
    signature_key:  # name of the signature def to use for prediction (required if your model has more than one signature def)
    cache_size: <int>  # the number models to keep in memory (optional; all models are kept in memory by default)
    disk_cache_size: <int>  # the number of models to keep on disk (optional; all models are kept on disk by default)
  server_side_batching:  # (optional)
    max_batch_size: <int>  # the maximum number of requests to aggregate before running inference
    batch_interval: <duration>  # the maximum amount of time to spend waiting for additional requests before running inference on the batch of requests
  processes_per_replica: <int>  # the number of parallel serving processes to run on each replica (default: 1)
  threads_per_process: <int>  # the number of threads per process (default: 1)
  config: <string: value>  # arbitrary dictionary passed to the constructor of the Predictor (optional)
  python_path: <string>  # path to the root of your Python folder that will be appended to PYTHONPATH (default: folder containing cortex.yaml)
  image: <string>  # docker image to use for the Predictor (default: quay.io/cortexlabs/tensorflow-predictor:0.28.0)
  tensorflow_serving_image: <string>  # docker image to use for the TensorFlow Serving container (default: quay.io/cortexlabs/tensorflow-serving-cpu:0.28.0, quay.io/cortexlabs/tensorflow-serving-gpu:0.28.0, or quay.io/cortexlabs/tensorflow-serving-inf:0.28.0 based on compute)
  env: <string: string>  # dictionary of environment variables
  log_level: <string>  # log level that can be "debug", "info", "warning" or "error" (default: "info")
  shm_size: <string>  # size of shared memory (/dev/shm) for sharing data between multiple processes, e.g. 64Mi or 1Gi (default: Null)
```

### ONNX Predictor

```yaml
predictor:
  type: onnx
  path: <string>  # path to a python file with an ONNXPredictor class definition, relative to the Cortex root (required)
  models:  # (required)
    path: <string> # S3/GCS path to an exported model directory (e.g. s3://my-bucket/exported_model/) (either this, 'dir', or 'paths' must be provided)
    paths:  # list of S3/GCS paths to exported model directories (either this, 'dir', or 'path' must be provided)
      - name: <string>  # unique name for the model (e.g. text-generator) (required)
        path: <string>  # S3/GCS path to an exported model directory (e.g. s3://my-bucket/exported_model/) (required)
      ...
    dir: <string>  # S3/GCS path to a directory containing multiple model directories (e.g. s3://my-bucket/models/) (either this, 'path', or 'paths' must be provided)
    cache_size: <int>  # the number models to keep in memory (optional; all models are kept in memory by default)
    disk_cache_size: <int>  # the number of models to keep on disk (optional; all models are kept on disk by default)
  processes_per_replica: <int>  # the number of parallel serving processes to run on each replica (default: 1)
  threads_per_process: <int>  # the number of threads per process (default: 1)
  config: <string: value>  # arbitrary dictionary passed to the constructor of the Predictor (optional)
  python_path: <string>  # path to the root of your Python folder that will be appended to PYTHONPATH (default: folder containing cortex.yaml)
  image: <string>  # docker image to use for the Predictor (default: quay.io/cortexlabs/onnx-predictor-cpu:0.28.0 or quay.io/cortexlabs/onnx-predictor-gpu:0.28.0 based on compute)
  env: <string: string>  # dictionary of environment variables
  log_level: <string>  # log level that can be "debug", "info", "warning" or "error" (default: "info")
  shm_size: <string>  # size of shared memory (/dev/shm) for sharing data between multiple processes, e.g. 64Mi or 1Gi (default: Null)
```

## Compute

```yaml
compute:
  cpu: <string | int | float>  # CPU request per replica. One unit of CPU corresponds to one virtual CPU; fractional requests are allowed, and can be specified as a floating point number or via the "m" suffix (default: 200m)
  gpu: <int>  # GPU request per replica. One unit of GPU corresponds to one virtual GPU (default: 0)
  mem: <string>  # memory request per replica. One unit of memory is one byte and can be expressed as an integer or by using one of these suffixes: K, M, G, T (or their power-of two counterparts: Ki, Mi, Gi, Ti) (default: Null)
```

## Autoscaling

```yaml
autoscaling:
  min_replicas: <int>  # minimum number of replicas (default: 1)
  max_replicas: <int>  # maximum number of replicas (default: 100)
  init_replicas: <int>  # initial number of replicas (default: <min_replicas>)
  max_replica_concurrency: <int>  # the maximum number of in-flight requests per replica before requests are rejected with error code 503 (default: 1024)
  target_replica_concurrency: <float>  # the desired number of in-flight requests per replica, which the autoscaler tries to maintain (default: processes_per_replica * threads_per_process) (aws only)
  window: <duration>  # the time over which to average the API's concurrency (default: 60s) (aws only)
  downscale_stabilization_period: <duration>  # the API will not scale below the highest recommendation made during this period (default: 5m) (aws only)
  upscale_stabilization_period: <duration>  # the API will not scale above the lowest recommendation made during this period (default: 1m) (aws only)
  max_downscale_factor: <float>  # the maximum factor by which to scale down the API on a single scaling event (default: 0.75) (aws only)
  max_upscale_factor: <float>  # the maximum factor by which to scale up the API on a single scaling event (default: 1.5) (aws only)
  downscale_tolerance: <float>  # any recommendation falling within this factor below the current number of replicas will not trigger a scale down event (default: 0.05) (aws only)
  upscale_tolerance: <float>  # any recommendation falling within this factor above the current number of replicas will not trigger a scale up event (default: 0.05) (aws only)
```

## Update strategy

```yaml
update_strategy:
  max_surge: <string | int>  # maximum number of replicas that can be scheduled above the desired number of replicas during an update; can be an absolute number, e.g. 5, or a percentage of desired replicas, e.g. 10% (default: 25%) (set to 0 to disable rolling updates)
  max_unavailable: <string | int>  # maximum number of replicas that can be unavailable during an update; can be an absolute number, e.g. 5, or a percentage of desired replicas, e.g. 10% (default: 25%)
```

## Networking

```yaml
  networking:
    endpoint: <string>  # the endpoint for the API (default: <api_name>)
```


# Models

## Model directory format

Whenever a model path is specified in an API configuration file, it should be a path to an S3/GCS prefix which contains your exported model. Directories may include a single model, or multiple folders each with a single model (note that a "single model" need not be a single file; there can be multiple files for a single model). When multiple folders are used, the folder names must be integer values, and will be interpreted as the model version. Model versions can be any integer, but are typically integer timestamps. It is always assumed that the highest version number is the latest version of your model.

Each predictor type expects a different model format:

### Python

For the Python predictor, any model structure is accepted. Here is an example:

```
  s3://my-bucket/models/text-generator/
  ├── model.pkl
  └── data.txt
```

or for a versioned model:

```
  s3://my-bucket/models/text-generator/
  ├── 1523423423/  (version number, usually a timestamp)
  |   ├── model.pkl
  |   └── data.txt
  └── 2434389194/  (version number, usually a timestamp)
      ├── model.pkl
      └── data.txt
```

### TensorFlow

For the TensorFlow predictor, the model path must be a SavedModel export:

```
  s3://my-bucket/models/text-generator/
  ├── saved_model.pb
  └── variables/
      ├── variables.index
      ├── variables.data-00000-of-00003
      ├── variables.data-00001-of-00003
      └── variables.data-00002-of-...
```

or for a versioned model:

```
  s3://my-bucket/models/text-generator/
  ├── 1523423423/  (version number, usually a timestamp)
  |   ├── saved_model.pb
  |   └── variables/
  |       ├── variables.index
  |       ├── variables.data-00000-of-00003
  |       ├── variables.data-00001-of-00003
  |       └── variables.data-00002-of-...
  └── 2434389194/  (version number, usually a timestamp)
      ├── saved_model.pb
      └── variables/
          ├── variables.index
          ├── variables.data-00000-of-00003
          ├── variables.data-00001-of-00003
          └── variables.data-00002-of-...
```

#### Inferentia

When Inferentia models are used, the directory structure is slightly different:

```
  s3://my-bucket/models/text-generator/
  └── saved_model.pb
```

or for a versioned model:

```
  s3://my-bucket/models/text-generator/
  ├── 1523423423/  (version number, usually a timestamp)
  |   └── saved_model.pb
  └── 2434389194/  (version number, usually a timestamp)
      └── saved_model.pb
```

### ONNX

For the ONNX predictor, the model path must contain a single `*.onnx` file:

```
  s3://my-bucket/models/text-generator/
  └── model.onnx
```

or for a versioned model:

```
  s3://my-bucket/models/text-generator/
  ├── 1523423423/  (version number, usually a timestamp)
  |   └── model.onnx
  └── 2434389194/  (version number, usually a timestamp)
      └── model.onnx
```

## Single model

The most common pattern is to serve a single model per API. The path to the model is specified in the `path` field in the `predictor.models` configuration. For example:

```yaml
# cortex.yaml

- name: iris-classifier
  kind: RealtimeAPI
  predictor:
    # ...
    models:
      path: s3://my-bucket/models/text-generator/
```

For the Python predictor type, the `models` field comes under the name of `multi_model_reloading`. It is also not necessary to specify the `multi_model_reloading` section at all, since you can download and load the model in your predictor's `__init__()` function. That said, it is necessary to use the `path` field to take advantage of [live model reloading](#live-model-reloading).

## Multiple models

It is possible to serve multiple models from a single API. The paths to the models are specified in the api configuration, either via the `models.paths` or `models.dir` field in the `predictor` configuration. For example:

```yaml
# cortex.yaml

- name: iris-classifier
  kind: RealtimeAPI
  predictor:
    # ...
    models:
      paths:
        - name: iris-classifier
          path: s3://my-bucket/models/text-generator/
        # ...
```

or:

```yaml
# cortex.yaml

- name: iris-classifier
  kind: RealtimeAPI
  predictor:
    # ...
    models:
      dir: s3://my-bucket/models/
```

For the Python predictor type, the `models` field comes under the name of `multi_model_reloading`. It is also not necessary to specify the `multi_model_reloading` section at all, since you can download and load the model in your predictor's `__init__()` function. That said, it is necessary to use the `models` field to take advantage of live model reloading or multi-model caching.

When using the `models.paths` field, each path must be a valid model directory (see above for valid model directory structures).

When using the `models.dir` field, the directory provided may contain multiple subdirectories, each of which is a valid model directory. For example:

```
  s3://my-bucket/models/
  ├── text-generator
  |   └── * (model files)
  └── sentiment-analyzer
      ├── 24753823/
      |   └── * (model files)
      └── 26234288/
          └── * (model files)
```

In this case, there are two models in the directory, one of which is named "text-generator", and the other is named "sentiment-analyzer".

## Live model reloading

Live model reloading is a mechanism that periodically checks for updated models in the model path(s) provided in `predictor.models`. It is automatically enabled for all predictor types, including the Python predictor type (as long as model paths are specified via `multi_model_reloading` in the `predictor` configuration).

The following is a list of events that will trigger the API to update its model(s):

* A new model is added to the model directory.
* A model is removed from the model directory.
* A model changes its directory structure.
* A file in the model directory is updated in-place.

Usage varies based on the predictor type:

### Python

To use live model reloading with the Python predictor, the model path(s) must be specified in the API's `predictor` configuration, via the `models` field. When models are specified in this manner, your `PythonPredictor` class must implement the `load_model()` function, and models can be retrieved by using the `get_model()` method of the `python_client` that's passed into your predictor's constructor.

The `load_model()` function that you implement in your `PythonPredictor` can return anything that you need to make a prediction. There is one caveat: whatever the return value is, it must be unloadable from memory via the `del` keyword. The following frameworks have been tested to work:

* PyTorch (CPU & GPU)
* ONNX (CPU & GPU)
* Sklearn/MLFlow (CPU)
* Numpy (CPU)
* Pandas (CPU)
* Caffe (not tested, but should work on CPU & GPU)

Python data structures containing these types are also supported (e.g. lists and dicts).

The `load_model()` function takes a single argument, which is a path (on disk) to the model to be loaded. Your `load_model()` function is called behind the scenes by Cortex when you call the `python_client`'s `get_model()` method. Cortex is responsible for downloading your model from S3/GCS onto the local disk before calling `load_model()` with the local path. Whatever `load_model()` returns will be the exact return value of `python_client.get_model()`. Here is the schema for `python_client.get_model()`:

```python
def get_model(model_name, model_version):
    """
    Retrieve a model for inference.

    Args:
        model_name (optional): Name of the model to retrieve (when multiple models are deployed in an API).
            When predictor.models.paths is specified, model_name should be the name of one of the models listed in the API config.
            When predictor.models.dir is specified, model_name should be the name of a top-level directory in the models dir.
        model_version (string, optional): Version of the model to retrieve. Can be omitted or set to "latest" to select the highest version.

    Returns:
        The value that's returned by your predictor's load_model() method.
    """
```

Here's an example:

```python
class PythonPredictor:
    def __init__(self, config, python_client):
        self.client = python_client

    def load_model(self, model_path):
        # model_path is a path to your model's directory on disk
        return load_from_disk(model_path)

    def predict(self, payload):
      model = self.client.get_model()
      return model.predict(payload)
```

When multiple models are being served in an API, `python_client.get_model()` can accept a model name:

```python
class PythonPredictor:
    # ...

    def predict(self, payload, query_params):
      model = self.client.get_model(query_params["model"])
      return model.predict(payload)
```

`python_client.get_model()` can also accept a model version if a version other than the highest is desired:

```python
class PythonPredictor:
    # ...

    def predict(self, payload, query_params):
      model = self.client.get_model(query_params["model"], query_params["version"])
      return model.predict(payload)
```

### TensorFlow

When using the TensorFlow predictor, inference is performed by using the `predict()` method of the `tensorflow_client` that's passed to the predictor's constructor:

```python
def predict(model_input, model_name, model_version) -> dict:
    """
    Run prediction.

    Args:
        model_input: Input to the model.
        model_name (optional): Name of the model to retrieve (when multiple models are deployed in an API).
            When predictor.models.paths is specified, model_name should be the name of one of the models listed in the API config.
            When predictor.models.dir is specified, model_name should be the name of a top-level directory in the models dir.
        model_version (string, optional): Version of the model to retrieve. Can be omitted or set to "latest" to select the highest version.

    Returns:
        dict: TensorFlow Serving response converted to a dictionary.
    """
```

For example:

```python
class TensorFlowPredictor:
    def __init__(self, tensorflow_client, config):
        self.client = tensorflow_client

    def predict(self, payload):
      return self.client.predict(payload)
```

When multiple models are being served in an API, `tensorflow_client.predict()` can accept a model name:

```python
class TensorFlowPredictor:
    # ...

    def predict(self, payload, query_params):
      return self.client.predict(payload, query_params["model"])
```

`tensorflow_client.predict()` can also accept a model version if a version other than the highest is desired:

```python
class TensorFlowPredictor:
    # ...

    def predict(self, payload, query_params):
      return self.client.predict(payload, query_params["model"], query_params["version"])
```

Note: when using Inferentia models with the TensorFlow predictor, live model reloading is only supported if `predictor.processes_per_replica` is set to 1 (the default value).

### ONNX

When using the ONNX predictor, inference is performed by using the `predict()` method of the `onnx_client` that's passed to the predictor's constructor:

```python
def predict(model_input: Any, model_name: Optional[str] = None, model_version: str = "latest") -> Any:
    """
    Run prediction.

    Args:
        model_input: Input to the model.
        model_name (optional): Name of the model to retrieve (when multiple models are deployed in an API).
            When predictor.models.paths is specified, model_name should be the name of one of the models listed in the API config.
            When predictor.models.dir is specified, model_name should be the name of a top-level directory in the models dir.
        model_version (string, optional): Version of the model to retrieve. Can be omitted or set to "latest" to select the highest version.

    Returns:
        The prediction returned from the model.
    """
```

For example:

```python
class ONNXPredictor:
    def __init__(self, onnx_client, config):
        self.client = onnx_client

    def predict(self, payload):
      return self.client.predict(payload)
```

When multiple models are being served in an API, `onnx_client.predict()` can accept a model name:

```python
class ONNXPredictor:
    # ...

    def predict(self, payload, query_params):
      return self.client.predict(payload, query_params["model"])
```

`onnx_client.predict()` can also accept a model version if a version other than the highest is desired:

```python
class ONNXPredictor:
    # ...

    def predict(self, payload, query_params):
      return self.client.predict(payload, query_params["model"], query_params["version"])
```

You can also retrieve information about the model by calling the `onnx_client`'s `get_model()` method (it supports model name and model version arguments, like its `predict()` method). This can be useful for retrieving the model's input/output signatures. For example, `self.client.get_model()` might look like this:

```python
{
    "session": "<onnxruntime.InferenceSession model object>",
    "signatures": "<onnxruntime.InferenceSession model object>['session'].get_inputs()",
    "input_signatures": {
        "<signature-name>": {
            "shape": "<input shape>",
            "type": "<numpy type>"
        }
        ...
    }
}
```


# Parallelism

Replica parallelism can be configured with the following fields in the `predictor` configuration:

* `processes_per_replica` (default: 1): Each replica runs a web server with `processes_per_replica` processes. For APIs running with multiple CPUs per replica, using 1-3 processes per unit of CPU generally leads to optimal throughput. For example, if `cpu` is 2, a value between 2 and 6 `processes_per_replica` is reasonable. The optimal number will vary based on the workload's characteristics and the CPU compute request for the API.
* `threads_per_process` (default: 1): Each process uses a thread pool of size `threads_per_process` to process requests. For applications that are not CPU intensive such as high I/O (e.g. downloading files), GPU-based inference, or Inferentia-based inference, increasing the number of threads per process can increase throughput. For CPU-bound applications such as running your model inference on a CPU, using 1 thread per process is recommended to avoid unnecessary context switching. Some applications are not thread-safe, and therefore must be run with 1 thread per process.

`processes_per_replica` \* `threads_per_process` represents the total number of requests that your replica can work on concurrently. For example, if `processes_per_replica` is 2 and `threads_per_process` is 2, and the replica was hit with 5 concurrent requests, 4 would immediately begin to be processed, and 1 would be waiting for a thread to become available. If the replica were hit with 3 concurrent requests, all three would begin processing immediately.


# Server-side batching

Server-side batching is the process of aggregating multiple real-time requests into a single batch inference, which increases throughput at the expense of latency. Inference is triggered when either a maximum number of requests have been received, or when a certain amount of time has passed since receiving the first request, whichever comes first. Once a threshold is reached, inference is run on the received requests and responses are returned individually back to the clients. This process is transparent to the clients.

The Python and TensorFlow predictors allow for the use of the following 2 fields in the `server_side_batching` configuration:

* `max_batch_size`: The maximum number of requests to aggregate before running inference. This is an instrument for controlling throughput. The maximum size can be achieved if `batch_interval` is long enough to collect `max_batch_size` requests.
* `batch_interval`: The maximum amount of time to spend waiting for additional requests before running inference on the batch of requests. If fewer than `max_batch_size` requests are received after waiting the full `batch_interval`, then inference will run on the requests that have been received. This is an instrument for controlling latency.

## Python predictor

When using server-side batching with the Python predictor, the arguments that are passed into your predictor's `predict()` function will be lists: `payload` will be a list of payloads, `query_params` will be a list of query parameter dictionaries, and `headers` will be a list of header dictionaries. The lists will all have the same length, where a particular index accross all arguments corresponds to a single request (i.e. `payload[2]`, `query_params[2]`, and `headers[2]` correspond to a single prediction request). Your `predict()` function must return a list of responses in the same order that they were received (i.e. the 3rd element in returned list must be the response associated with `payload[2]`).

## TensorFlow predictor

In order to use server-side batching with the TensorFlow predictor, the only requirement is that model's graph must be built such that batches can be accepted as input/output. No modifications to your `TensorFlowPredictor` implementation are required.

The following is an example of how the input `x` and the output `y` of the graph could be shaped to be compatible with server-side batching:

```python
batch_size = None
sample_shape = [340, 240, 3] # i.e. RGB image
output_shape = [1000] # i.e. image labels

with graph.as_default():
    # ...
    x = tf.placeholder(tf.float32, shape=[batch_size] + sample_shape, name="input")
    y = tf.placeholder(tf.float32, shape=[batch_size] + output_shape, name="output")
    # ...
```

### Troubleshooting

Errors will be encountered if the model hasn't been built for batching.

The following error is an example of what happens when the input shape doesn't accommodate batching - e.g. when its shape is `[height, width, 3]` instead of `[batch_size, height, width, 3]`:

```
Batching session Run() input tensors must have at least one dimension.
```

Here is another example of setting the output shape inappropriately for batching - e.g. when its shape is `[labels]` instead of `[batch_size, labels]`:

```
Batched output tensor has 0 dimensions.
```

The solution to these errors is to incorporate into the model's graph another dimension (a placeholder for batch size) placed on the first position for both its input and output.

The following is an example of how the input `x` and the output `y` of the graph could be shaped to be compatible with server-side batching:

```python
batch_size = None
sample_shape = [340, 240, 3] # i.e. RGB image
output_shape = [1000] # i.e. image labels

with graph.as_default():
    # ...
    x = tf.placeholder(tf.float32, shape=[batch_size] + sample_shape, name="input")
    y = tf.placeholder(tf.float32, shape=[batch_size] + output_shape, name="output")
    # ...
```

## Optimization

When optimizing for both throughput and latency, you will likely want keep the `max_batch_size` to a relatively small value. Even though a higher `max_batch_size` with a low `batch_interval` (when there are many requests coming in) can offer a significantly higher throughput, the overall latency could be quite large. The reason is that for a request to get back a response, it has to wait until the entire batch is processed, which means that the added latency due to the `batch_interval` can pale in comparison. For instance, let's assume that a single prediction takes 50ms, and that when the batch size is set to 128, the processing time for a batch is 1280ms (i.e. 10ms per sample). So while the throughput is now 5 times higher, it takes 1280ms + `batch_interval` to get back a response (instead of 50ms). This is the trade-off with server-side batching.

When optimizing for maximum throughput, a good rule of thumb is to follow these steps:

1. Determine the maximum throughput of one API replica when `server_side_batching` is not enabled (same as if `max_batch_size` were set to 1). This can be done with a load test (make sure to set `max_replicas` to 1 to disable autoscaling).
2. Determine the highest `batch_interval` with which you are still comfortable for your application. Keep in mind that the batch interval is not the only component of the overall latency - the inference on the batch and the pre/post processing also have to occur.
3. Multiply the maximum throughput from step 1 by the `batch_interval` from step 2. The result is a number which you can assign to `max_batch_size`.
4. Run the load test again. If the inference fails with that batch size (e.g. due to running out of GPU or RAM memory), then reduce `max_batch_size` to a level that works (reduce `batch_interval` by the same factor).
5. Use the load test to determine the peak throughput of the API replica. Multiply the observed throughput by the `batch_interval` to calculate the average batch size. If the average batch size coincides with `max_batch_size`, then it might mean that the throughput could still be further increased by increasing `max_batch_size`. If it's lower, then it means that `batch_interval` is triggering the inference before `max_batch_size` requests have been aggregated. If modifying both `max_batch_size` and `batch_interval` doesn't improve the throughput, then the service may be bottlenecked by something else (e.g. CPU, network IO, `processes_per_replica`, `threads_per_process`, etc).


# Autoscaling

Cortex autoscales your web services on a per-API basis based on your configuration.

## Autoscaling replicas

**`min_replicas`**: The lower bound on how many replicas can be running for an API.

**`max_replicas`**: The upper bound on how many replicas can be running for an API.

**`target_replica_concurrency`** (default: `processes_per_replica` \* `threads_per_process`): This is the desired number of in-flight requests per replica, and is the metric which the autoscaler uses to make scaling decisions.

Replica concurrency is simply how many requests have been sent to a replica and have not yet been responded to (also referred to as in-flight requests). Therefore, it includes requests which are currently being processed and requests which are waiting in the replica's queue.

The autoscaler uses this formula to determine the number of desired replicas:

`desired replicas = sum(in-flight requests accross all replicas) / target_replica_concurrency`

For example, setting `target_replica_concurrency` to `processes_per_replica` \* `threads_per_process` (the default) causes the cluster to adjust the number of replicas so that on average, requests are immediately processed without waiting in a queue, and processes/threads are never idle.

**`max_replica_concurrency`** (default: 1024): This is the maximum number of in-flight requests per replica before requests are rejected with HTTP error code 503. `max_replica_concurrency` includes requests that are currently being processed as well as requests that are waiting in the replica's queue (a replica can actively process `processes_per_replica` \* `threads_per_process` requests concurrently, and will hold any additional requests in a local queue). Decreasing `max_replica_concurrency` and configuring the client to retry when it receives 503 responses will improve queue fairness accross replicas by preventing requests from sitting in long queues.

**`window`** (default: 60s): The time over which to average the API wide in-flight requests (which is the sum of in-flight requests in each replica). The longer the window, the slower the autoscaler will react to changes in API wide in-flight requests, since it is averaged over the `window`. API wide in-flight requests is calculated every 10 seconds, so `window` must be a multiple of 10 seconds.

**`downscale_stabilization_period`** (default: 5m): The API will not scale below the highest recommendation made during this period. Every 10 seconds, the autoscaler makes a recommendation based on all of the other configuration parameters described here. It will then take the max of the current recommendation and all recommendations made during the `downscale_stabilization_period`, and use that to determine the final number of replicas to scale to. Increasing this value will cause the cluster to react more slowly to decreased traffic, and will reduce thrashing.

**`upscale_stabilization_period`** (default: 1m): The API will not scale above the lowest recommendation made during this period. Every 10 seconds, the autoscaler makes a recommendation based on all of the other configuration parameters described here. It will then take the min of the current recommendation and all recommendations made during the `upscale_stabilization_period`, and use that to determine the final number of replicas to scale to. Increasing this value will cause the cluster to react more slowly to increased traffic, and will reduce thrashing.

**`max_downscale_factor`** (default: 0.75): The maximum factor by which to scale down the API on a single scaling event. For example, if `max_downscale_factor` is 0.5 and there are 10 running replicas, the autoscaler will not recommend fewer than 5 replicas. Increasing this number will allow the cluster to shrink more quickly in response to dramatic dips in traffic.

**`max_upscale_factor`** (default: 1.5): The maximum factor by which to scale up the API on a single scaling event. For example, if `max_upscale_factor` is 10 and there are 5 running replicas, the autoscaler will not recommend more than 50 replicas. Increasing this number will allow the cluster to grow more quickly in response to dramatic spikes in traffic.

**`downscale_tolerance`** (default: 0.05): Any recommendation falling within this factor below the current number of replicas will not trigger a scale down event. For example, if `downscale_tolerance` is 0.1 and there are 20 running replicas, a recommendation of 18 or 19 replicas will not be acted on, and the API will remain at 20 replicas. Increasing this value will prevent thrashing, but setting it too high will prevent the cluster from maintaining it's optimal size.

**`upscale_tolerance`** (default: 0.05): Any recommendation falling within this factor above the current number of replicas will not trigger a scale up event. For example, if `upscale_tolerance` is 0.1 and there are 20 running replicas, a recommendation of 21 or 22 replicas will not be acted on, and the API will remain at 20 replicas. Increasing this value will prevent thrashing, but setting it too high will prevent the cluster from maintaining it's optimal size.

## Autoscaling instances

Cortex spins up and down instances based on the aggregate resource requests of all APIs. The number of instances will be at least `min_instances` and no more than `max_instances` (configured during installation and modifiable via `cortex cluster configure`).

## Overprovisioning

The default value for `target_replica_concurrency` is `processes_per_replica` \* `threads_per_process`, which behaves well in many situations (see above for an explanation of how `target_replica_concurrency` affects autoscaling). However, if your application is sensitive to spikes in traffic or if creating new replicas takes too long (see below), you may find it helpful to maintain extra capacity to handle the increased traffic while new replicas are being created. This can be accomplished by setting `target_replica_concurrency` to a lower value relative to the expected replica's concurrency. The smaller `target_replica_concurrency` is, the more unused capacity your API will have, and the more room it will have to handle sudden increased load. The increased request rate will still trigger the autoscaler, and your API will stabilize again (maintaining the overprovisioned capacity).

For example, if you've determined that each replica in your API can handle 2 requests, you would set `target_replica_concurrency` to 2. In a scenario where your API is receiving 8 concurrent requests on average, the autoscaler would maintain 4 live replicas (8/2 = 4). If you wanted to overprovision by 25%, you can set `target_replica_concurrency` to 1.6 causing the autoscaler maintain 5 live replicas (8/1.6 = 5).

## Autoscaling responsiveness

Assuming that `window` and `upscale_stabilization_period` are set to their default values (1 minute), it could take up to 2 minutes of increased traffic before an extra replica is requested. As soon as the additional replica is requested, the replica request will be visible in the output of `cortex get`, but the replica won't yet be running. If an extra instance is required to schedule the newly requested replica, it could take a few minutes for AWS to provision the instance (depending on the instance type), plus a few minutes for the newly provisioned instance to download your api image and for the api to initialize (via its `__init__()` method).

Keep these delays in mind when considering overprovisioning (see above) and when determining appropriate values for `window` and `upscale_stabilization_period`. If you want the autoscaler to react as quickly as possible, set `upscale_stabilization_period` and `window` to their minimum values (0s and 10s respectively).

If it takes a long time to initialize your API replica (i.e. install dependencies and run your predictor's `__init__()` function), consider building your own API image to use instead of the default image. With this approach, you can pre-download/build/install any custom dependencies and bake them into the image.


# Statuses

| Status                | Meaning                                                                                                                                                                                              |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| live                  | API is deployed and ready to serve prediction requests (at least one replica is running)                                                                                                             |
| updating              | API is updating                                                                                                                                                                                      |
| error                 | API was not created due to an error; run `cortex logs <name>` to view the logs                                                                                                                       |
| error (image pull)    | API was not created because one of the specified Docker images was inaccessible at runtime; check that your API's docker images exist and are accessible via your cluster operator's AWS credentials |
| error (out of memory) | API was terminated due to excessive memory usage; try allocating more memory to the API and re-deploying                                                                                             |
| compute unavailable   | API could not start due to insufficient memory, CPU, GPU or Inf in the cluster; some replicas may be ready                                                                                           |


# Multi-model


# Example

Deploy several models in a single API to improve resource utilization efficiency.

## Define a multi-model API

```python
# multi_model.py

import cortex

class PythonPredictor:
    def __init__(self, config):
        from transformers import pipeline
        self.analyzer = pipeline(task="sentiment-analysis")

        import wget
        import fasttext
        wget.download(
            "https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin", "/tmp/model"
        )
        self.language_identifier = fasttext.load_model("/tmp/model")

    def predict(self, query_params, payload):
        model = query_params.get("model")
        if model == "sentiment":
            return self.analyzer(payload["text"])[0]
        elif model == "language":
            return self.language_identifier.predict(payload["text"])[0][0][-2:]

requirements = ["tensorflow", "transformers", "wget", "fasttext"]

api_spec = {"name": "multi-model", "kind": "RealtimeAPI"}

cx = cortex.client("aws")
cx.create_api(api_spec, predictor=PythonPredictor, requirements=requirements)
```

## Deploy

```bash
$ python multi_model.py
```


# Configuration

## `PythonPredictor`

### Specifying models in API configuration

#### `cortex.yaml`

The directory `s3://cortex-examples/sklearn/mpg-estimator/linreg/` contains 4 different versions of the model.

```yaml
- name: mpg-estimator
  kind: RealtimeAPI
  predictor:
    type: python
    path: predictor.py
    models:
      path: s3://cortex-examples/sklearn/mpg-estimator/linreg/
```

#### `predictor.py`

```python
import mlflow.sklearn
import numpy as np


class PythonPredictor:
    def __init__(self, config, python_client):
        self.client = python_client

    def load_model(self, model_path):
        return mlflow.sklearn.load_model(model_path)

    def predict(self, payload, query_params):
        model_version = query_params.get("version")

        # model_input = ...

        model = self.client.get_model(model_version=model_version)
        result = model.predict(model_input)

        return {"prediction": result, "model": {"version": model_version}}
```

### Without specifying models in API configuration

#### `cortex.yaml`

```yaml
- name: text-analyzer
  kind: RealtimeAPI
  predictor:
    type: python
    path: predictor.py
    ...
```

#### `predictor.py`

```python
class PythonPredictor:
    def __init__(self, config):
        self.analyzer = initialize_model("sentiment-analysis")
        self.summarizer = initialize_model("summarization")

    def predict(self, query_params, payload):
        model_name = query_params.get("model")
        model_input = payload["text"]

        # ...

        if model_name == "analyzer":
            results = self.analyzer(model_input)
            predicted_label = postprocess(results)
            return {"label": predicted_label}
        elif model_name == "summarizer":
            results = self.summarizer(model_input)
            predicted_label = postprocess(results)
            return {"label": predicted_label}
        else:
            return JSONResponse({"error": f"unknown model: {model_name}"}, status_code=400)
```

## `TensorFlowPredictor`

### `cortex.yaml`

```yaml
- name: multi-model-classifier
  kind: RealtimeAPI
  predictor:
    type: tensorflow
    path: predictor.py
    models:
      paths:
        - name: inception
          path: s3://cortex-examples/tensorflow/image-classifier/inception/
        - name: iris
          path: s3://cortex-examples/tensorflow/iris-classifier/nn/
        - name: resnet50
          path: s3://cortex-examples/tensorflow/resnet50/
      ...
```

### `predictor.py`

```python
class TensorFlowPredictor:
    def __init__(self, tensorflow_client, config):
        self.client = tensorflow_client

    def predict(self, payload, query_params):
        model_name = query_params["model"]
        model_input = preprocess(payload["url"])
        results = self.client.predict(model_input, model_name)
        predicted_label = postprocess(results)
        return {"label": predicted_label}
```

## `ONNXPredictor`

### `cortex.yaml`

```yaml
- name: multi-model-classifier
  kind: RealtimeAPI
  predictor:
    type: onnx
    path: predictor.py
    models:
      paths:
        - name: resnet50
          path: s3://cortex-examples/onnx/resnet50/
        - name: mobilenet
          path: s3://cortex-examples/onnx/mobilenet/
        - name: shufflenet
          path: s3://cortex-examples/onnx/shufflenet/
      ...
```

### `predictor.py`

```python
class ONNXPredictor:
    def __init__(self, onnx_client, config):
        self.client = onnx_client

    def predict(self, payload, query_params):
        model_name = query_params["model"]
        model_input = preprocess(payload["url"])
        results = self.client.predict(model_input, model_name)
        predicted_label = postprocess(results)
        return {"label": predicted_label}
```


# Caching

Multi-model caching allows each replica to serve more models than would fit into its memory by keeping a specified number of models in memory (and disk) at a time. When the in-memory model limit is reached, the least recently accessed model is evicted from the cache. This can be useful when you have many models, and some models are frequently accessed while a larger portion of them are rarely used, or when running on smaller instances to control costs.

The model cache is a two-layer cache, configured by the following parameters in the `predictor.models` configuration:

* `cache_size` sets the number of models to keep in memory
* `disk_cache_size` sets the number of models to keep on disk (must be greater than or equal to `cache_size`)

Both of these fields must be specified, in addition to either the `dir` or `paths` field (which specifies the model paths, see [models](https://docs.cortexlabs.com/workloads/realtime-apis/models) for documentation). Multi-model caching is only supported if `predictor.processes_per_replica` is set to 1 (the default value).

## Out of memory errors

Cortex runs a background process every 10 seconds that counts the number of models in memory and on disk, and evicts the least recently used models if the count exceeds `cache_size` / `disk_cache_size`. If many new models are requested between executions of the process, there may be more models in memory and/or on disk than the configured `cache_size` or `disk_cache_size` limits which could lead to out of memory errors.


# Traffic Splitter


# Example

Expose multiple RealtimeAPIs as a single endpoint for A/B tests, multi-armed bandits, or canary deployments.

## Deploy APIs

```python
import cortex

class PythonPredictor:
    def __init__(self, config):
        from transformers import pipeline
        self.model = pipeline(task="text-generation")

    def predict(self, payload):
        return self.model(payload["text"])[0]

requirements = ["tensorflow", "transformers"]

api_spec_cpu = {
    "name": "text-generator-cpu",
    "kind": "RealtimeAPI",
    "compute": {
        "cpu": 1,
    },
}

api_spec_gpu = {
    "name": "text-generator-gpu",
    "kind": "RealtimeAPI",
    "compute": {
        "gpu": 1,
    },
}

cx = cortex.client("aws")
cx.create_api(api_spec_cpu, predictor=PythonPredictor, requirements=requirements)
cx.create_api(api_spec_gpu, predictor=PythonPredictor, requirements=requirements)
```

## Deploy a traffic splitter

```python
traffic_splitter_spec = {
    "name": "text-generator",
    "kind": "TrafficSplitter",
    "apis": [
        {"name": "text-generator-cpu", "weight": 50},
        {"name": "text-generator-gpu", "weight": 50},
    ],
}

cx.create_api(traffic_splitter_spec)
```

## Update the weights of the traffic splitter

```python
traffic_splitter_spec = cx.get_api("text-generator")["spec"]["submitted_api_spec"]

# send 99% of the traffic to text-generator-gpu
traffic_splitter_spec["apis"][0]["weight"] = 1
traffic_splitter_spec["apis"][1]["weight"] = 99

cx.patch(traffic_splitter_spec)
```


# Configuration

```yaml
- name: <string>  # Traffic Splitter name (required)
  kind: TrafficSplitter
  networking:
    endpoint: <string>  # the endpoint for the Traffic Splitter (default: <name>)
  apis:  # list of Realtime APIs to target
    - name: <string>  # name of a Realtime API that is already running or is included in the same configuration file (required)
      weight: <int>   # percentage of traffic to route to the Realtime API (all weights must sum to 100) (required)
```


# Troubleshooting

## 404 or 503 error responses from API requests

When making prediction requests to your API, it's possible to get a `{"message":"Not Found"}` error message (with HTTP status code `404`), or a `no healthy upstream` error message (with HTTP status code `503`). This means that there are currently no live replicas running for your API. This could happen for a few reasons:

1. It's possible that your API is simply not ready yet. You can check the status of your API with `cortex get API_NAME`, and stream the logs with `cortex logs API_NAME`.
2. Your API may have errored during initialization or while responding to a previous request. `cortex get API_NAME` will show the status of your API, and you can view the logs with `cortex logs API_NAME`.

It is also possible to receive a `{"message":"Service Unavailable"}` error message (with HTTP status code `503`) if you are using API Gateway in front of your API endpoints and if your request exceeds API Gateway's 29 second timeout. If the request is exceeding the API Gateway timeout, your client should receive the `{"message":"Service Unavailable"}` response \~29 seconds after making the request. To confirm that this is the issue, you can modify your `predict()` function to immediately return a response (e.g. `return "ok"`), re-deploy your API, wait for the update to complete, and try making a request. If your client successfully receives the "ok" response, it is likely that the API Gateway timeout is occurring. You can either modify your `predict()` implementation to take less time, run on faster hardware (e.g. GPUs), or don't use API Gateway (there is no timeout when using the API's endpoint).

## API is stuck updating

If your API is stuck in the "updating" or "compute unavailable" state (which is displayed when running `cortex get`), there are a few possible causes. Here are some things to check:

### Check `cortex logs API_NAME`

If no logs appear (e.g. it just says "fetching logs..."), continue down this list.

### Check `max_instances` for your cluster

When you created your Cortex cluster, you configured `max_instances` (either from the command prompts or via a cluster configuration file, e.g. `cluster.yaml`). If your cluster already has `min_instances` running instances, additional instances cannot be created and APIs may not be able to deploy, scale, or update.

You can check the current value of `max_instances` by running `cortex cluster info` (or `cortex cluster info --config cluster.yaml` if you have a cluster configuration file).

You can update `max_instances` by running `cortex cluster configure` (or by modifying `max_instances` in your cluster configuration file and running `cortex cluster configure --config cluster.yaml`).

## Check your AWS auto scaling group activity history

In most cases when AWS is unable to provision additional instances, the reason will be logged in the auto scaling group's activity history.

Here is how you can check these logs:

1. Log in to the AWS console and go to the EC2 service page
2. Click "Auto Scaling Groups" on the bottom of the side panel on the left
3. Select one of the "worker" autoscaling groups for your cluster (there may be two)
4. Click the "Activity" tab at the bottom half of the screen (it may also be called "Activity History" depending on which AWS console UI you're using)
5. Scroll down (if necessary) and inspect the activity history, looking for any errors and their causes
6. Repeat steps 3-5 for the other worker autoscaling group (if applicable)

Here is how it looks on the new console UI:

![new ui](https://user-images.githubusercontent.com/808475/78153371-852d2c00-742a-11ea-9bde-dbad5c603f8f.png)

On the old UI:

![old ui](https://user-images.githubusercontent.com/808475/78153350-7e9eb480-742a-11ea-9221-1f6559db45fd.png)

The most common reason AWS is unable to provision instances is that you have reached your instance limit. There is an instance limit associated with your AWS account for each instance family in each region, for on-demand and for spot instances. You can check your current limit and request an increase [here](https://console.aws.amazon.com/servicequotas/home?#!/services/ec2/quotas) (set the region in the upper right corner to your desired region, type "on-demand" or "spot" in the search bar, and click on the quota that matches your instance type). Note that the quota values indicate the number of vCPUs available, not the number of instances; different instances have a different numbers of vCPUs, which can be seen [here](https://aws.amazon.com/ec2/instance-types).

If you are using spot instances and don't have `on_demand_backup` set to true, it is also possible that AWS has run out of spot instances for your requested instance type and region. You can enable `on_demand_backup` to allow Cortex to fall back to on-demand instances when spot instances are unavailable, or you can try adding additional alternative instance types in `instance_distribution`.

### Disabling rolling updates

By default, cortex performs rolling updates on all APIs. This is to ensure that traffic can continue to be served during updates, and that there is no downtime if there's an error in the new version. However, this can lead to APIs getting stuck in the "updating" state when the cluster is unable to increase its instance count (e.g. for one of the reasons above).

Here is an example: You set `max_instances` to 1, or your AWS account limits you to a single `g4dn.xlarge` instance (i.e. your G instance vCPU limit is 4). You have an API running which requested 1 GPU. When you update your API via `cortex deploy`, Cortex attempts to deploy the updated version, and will only take down the old version once the new one is running. In this case, since there is no GPU available on the single running instance (it's taken by the old version of your API), the new version of your API requests a new instance to run on. Normally this will be ok (it might just take a few minutes since a new instance has to spin up): the new instance will become live, the new API replica will run on it, once it starts up successfully the old replica will be terminated, and eventually the old instance will spin down. In this case, however, the new version gets stuck because the second instance cannot be created, and the first instance cannot be freed up until the new version is running.

If you're running in a development environment, this rolling update behavior can be undesirable.

You can disable rolling updates for your API in your API configuration (e.g. in `cortex.yaml`): set `max_surge` to 0 (in the `update_strategy` configuration). E.g.:

```yaml
- name: text-generator
  predictor:
    type: python
    ...
  update_strategy:
    max_surge: 0
```

## TensorFlow session

When doing inferences with TensorFlow using the Realtime API Python Predictor or Batch API Python Predictor, it should be noted that your Python Predictor's `__init__()` constructor is only called on one thread, whereas its `predict()` method can run on any of the available threads (which is configured via the `threads_per_process` field in the API's `predictor` configuration). If `threads_per_process` is set to `1` (the default value), then there is no concern, since `__init__()` and `predict()` will run on the same thread. However, if `threads_per_process` is greater than `1`, then only one of the inference threads will have executed the `__init__()` function. This can cause issues with TensorFlow because the default graph is a property of the current thread, so if `__init__()` initializes the TensorFlow graph, only the thread that executed `__init__()` will have the default graph set.

The error you may see if the default graph is not set (as a consequence of `__init__()` and `predict()` running in separate threads) is:

```
TypeError: Cannot interpret feed_dict key as Tensor: Tensor Tensor("Placeholder:0", shape=(1, ?), dtype=int32) is not an element of this graph.
```

To avoid this error, you can set the default graph before running the prediction in the `predict()` method:

```python
def predict(self, payload):
    with self.sess.graph.as_default():
        # perform your inference here
```


# Batch APIs


# Example

Create APIs that can orchestrate distributed batch inference jobs on large datasets.

## Implement

```bash
$ mkdir image-classifier && cd image-classifier
$ touch predictor.py requirements.txt image_classifier.yaml
```

```python
# predictor.py

class PythonPredictor:
    def __init__(self, config, job_spec):
        from torchvision import transforms
        import torchvision
        import requests
        import boto3
        import re

        self.model = torchvision.models.alexnet(pretrained=True).eval()
        self.labels = requests.get(config["labels"]).text.split("\n")[1:]

        normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        self.preprocess = transforms.Compose(
            [transforms.Resize(256), transforms.CenterCrop(224), transforms.ToTensor(), normalize]
        )

        self.s3 = boto3.client("s3")  # initialize S3 client to save results
        self.bucket, self.key = re.match("s3://(.+?)/(.+)", config["dest_s3_dir"]).groups()
        self.key = os.path.join(self.key, job_spec["job_id"])

    def predict(self, payload, batch_id):
        import json
        import torch
        from PIL import Image
        from io import BytesIO
        import requests

        tensor_list = []
        for image_url in payload:  # download and preprocess each image
            img_pil = Image.open(BytesIO(requests.get(image_url).content))
            tensor_list.append(self.preprocess(img_pil))

        img_tensor = torch.stack(tensor_list)
        with torch.no_grad():  # classify the batch of images
            prediction = self.model(img_tensor)
        _, indices = prediction.max(1)

        results = [{"url": payload[i], "class": self.labels[class_idx]} for i, class_idx in enumerate(indices)]
        self.s3.put_object(Bucket=self.bucket, Key=f"{self.key}/{batch_id}.json", Body=json.dumps(results))
```

```python
# requirements.txt

torch
boto3
pillow
torchvision
requests
```

```yaml
# image_classifier.yaml

- name: image-classifier
  kind: BatchAPI
  predictor:
    type: python
    path: predictor.py
    config:
      labels: "https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt"
```

## Deploy

```bash
$ cortex deploy image_classifier.yaml
```

## Describe

```bash
$ cortex get image-classifier
```

## Submit a job

```python
import cortex
import requests

cx = cortex.client("aws")
batch_endpoint = cx.get_api("image-classifier")["endpoint"]

dest_s3_dir = # specify S3 directory for the results, e.g. "s3://my-bucket/dir" or "gs://my-bucket/dir" (make sure your cluster has access to this bucket)

job_spec = {
    "workers": 1,
    "item_list": {
        "items": [
            "https://i.imgur.com/PzXprwl.jpg",
            "https://i.imgur.com/E4cOSLw.jpg",
            "https://i.imgur.com/jDimNTZ.jpg",
            "https://i.imgur.com/WqeovVj.jpg"
        ],
        "batch_size": 2
    },
    "config": {
        "dest_s3_dir": dest_s3_dir
    }
}

response = requests.post(batch_endpoint, json=job_spec)
print(response.text)
# > {"job_id":"69b183ed6bdf3e9b","api_name":"image-classifier", "config": {"dest_s3_dir": ...}}
```

## Monitor the job

```bash
$ cortex get image-classifier 69b183ed6bdf3e9b
```

## Stream logs

```bash
$ cortex logs image-classifier 69b183ed6bdf3e9b
```

## View the results

Once the job is complete, you should be able to find the results in the directory you've specified.

## Delete

```bash
$ cortex delete image-classifier
```


# Predictor

Which Predictor you use depends on how your model is exported:

* [TensorFlow Predictor](#tensorflow-predictor) if your model is exported as a TensorFlow `SavedModel`
* [ONNX Predictor](#onnx-predictor) if your model is exported in the ONNX format
* [Python Predictor](#python-predictor) for all other cases

## Project files

Cortex makes all files in the project directory (i.e. the directory which contains `cortex.yaml`) available for use in your Predictor implementation. Python bytecode files (`*.pyc`, `*.pyo`, `*.pyd`), files or folders that start with `.`, and the api configuration file (e.g. `cortex.yaml`) are excluded.

The following files can also be added at the root of the project's directory:

* `.cortexignore` file, which follows the same syntax and behavior as a [.gitignore file](https://git-scm.com/docs/gitignore).
* `.env` file, which exports environment variables that can be used in the predictor. Each line of this file must follow the `VARIABLE=value` format.

For example, if your directory looks like this:

```
./my-classifier/
├── cortex.yaml
├── values.json
├── predictor.py
├── ...
└── requirements.txt
```

You can access `values.json` in your Predictor like this:

```python
import json

class PythonPredictor:
    def __init__(self, config):
        with open('values.json', 'r') as values_file:
            values = json.load(values_file)
        self.values = values
```

## Python Predictor

### Interface

```python
# initialization code and variables can be declared here in global scope

class PythonPredictor:
    def __init__(self, config, job_spec):
        """(Required) Called once during each worker initialization. Performs
        setup such as downloading/initializing the model or downloading a
        vocabulary.

        Args:
            config (required): Dictionary passed from API configuration (if
                specified) merged with configuration passed in with Job
                Submission API. If there are conflicting keys, values in
                configuration specified in Job submission takes precedence.
            job_spec (optional): Dictionary containing the following fields:
                "job_id": A unique ID for this job
                "api_name": The name of this batch API
                "config": The config that was provided in the job submission
                "workers": The number of workers for this job
                "total_batch_count": The total number of batches in this job
                "start_time": The time that this job started
        """
        pass

    def predict(self, payload, batch_id):
        """(Required) Called once per batch. Preprocesses the batch payload (if
        necessary), runs inference, postprocesses the inference output (if
        necessary), and writes the predictions to storage (i.e. S3 or a
        database, if desired).

        Args:
            payload (required): a batch (i.e. a list of one or more samples).
            batch_id (optional): uuid assigned to this batch.
        Returns:
            Nothing
        """
        pass

    def on_job_complete(self):
        """(Optional) Called once after all batches in the job have been
        processed. Performs post job completion tasks such as aggregating
        results, executing web hooks, or triggering other jobs.
        """
        pass
```

## TensorFlow Predictor

**Uses TensorFlow version 2.3.0 by default**

### Interface

```python
class TensorFlowPredictor:
    def __init__(self, tensorflow_client, config, job_spec):
        """(Required) Called once during each worker initialization. Performs
        setup such as downloading/initializing the model or downloading a
        vocabulary.

        Args:
            tensorflow_client (required): TensorFlow client which is used to
                make predictions. This should be saved for use in predict().
            config (required): Dictionary passed from API configuration (if
                specified) merged with configuration passed in with Job
                Submission API. If there are conflicting keys, values in
                configuration specified in Job submission takes precedence.
            job_spec (optional): Dictionary containing the following fields:
                "job_id": A unique ID for this job
                "api_name": The name of this batch API
                "config": The config that was provided in the job submission
                "workers": The number of workers for this job
                "total_batch_count": The total number of batches in this job
                "start_time": The time that this job started
        """
        self.client = tensorflow_client
        # Additional initialization may be done here

    def predict(self, payload, batch_id):
        """(Required) Called once per batch. Preprocesses the batch payload (if
        necessary), runs inference (e.g. by calling
        self.client.predict(model_input)), postprocesses the inference output
        (if necessary), and writes the predictions to storage (i.e. S3 or a
        database, if desired).

        Args:
            payload (required): a batch (i.e. a list of one or more samples).
            batch_id (optional): uuid assigned to this batch.
        Returns:
            Nothing
        """
        pass

    def on_job_complete(self):
        """(Optional) Called once after all batches in the job have been
        processed. Performs post job completion tasks such as aggregating
        results, executing web hooks, or triggering other jobs.
        """
        pass
```

Cortex provides a `tensorflow_client` to your Predictor's constructor. `tensorflow_client` is an instance of [TensorFlowClient](https://github.com/cortexlabs/cortex/tree/0.28/pkg/cortex/serve/cortex_internal/lib/client/tensorflow.py) that manages a connection to a TensorFlow Serving container to make predictions using your model. It should be saved as an instance variable in your Predictor, and your `predict()` function should call `tensorflow_client.predict()` to make an inference with your exported TensorFlow model. Preprocessing of the JSON payload and postprocessing of predictions can be implemented in your `predict()` function as well.

When multiple models are defined using the Predictor's `models` field, the `tensorflow_client.predict()` method expects a second argument `model_name` which must hold the name of the model that you want to use for inference (for example: `self.client.predict(payload, "text-generator")`).

If you need to share files between your predictor implementation and the TensorFlow Serving container, you can create a new directory within `/mnt` (e.g. `/mnt/user`) and write files to it. The entire `/mnt` directory is shared between containers, but do not write to any of the directories in `/mnt` that already exist (they are used internally by Cortex).

## ONNX Predictor

**Uses ONNX Runtime version 1.4.0 by default**

### Interface

```python
class ONNXPredictor:
    def __init__(self, onnx_client, config, job_spec):
        """(Required) Called once during each worker initialization. Performs
        setup such as downloading/initializing the model or downloading a
        vocabulary.

        Args:
            onnx_client (required): ONNX client which is used to make
                predictions. This should be saved for use in predict().
            config (required): Dictionary passed from API configuration (if
                specified) merged with configuration passed in with Job
                Submission API. If there are conflicting keys, values in
                configuration specified in Job submission takes precedence.
            job_spec (optional): Dictionary containing the following fields:
                "job_id": A unique ID for this job
                "api_name": The name of this batch API
                "config": The config that was provided in the job submission
                "workers": The number of workers for this job
                "total_batch_count": The total number of batches in this job
                "start_time": The time that this job started
        """
        self.client = onnx_client
        # Additional initialization may be done here

    def predict(self, payload, batch_id):
        """(Required) Called once per batch. Preprocesses the batch payload (if
        necessary), runs inference (e.g. by calling
        self.client.predict(model_input)), postprocesses the inference output
        (if necessary), and writes the predictions to storage (i.e. S3 or a
        database, if desired).

        Args:
            payload (required): a batch (i.e. a list of one or more samples).
            batch_id (optional): uuid assigned to this batch.
        Returns:
            Nothing
        """
        pass

    def on_job_complete(self):
        """(Optional) Called once after all batches in the job have been
        processed. Performs post job completion tasks such as aggregating
        results, executing web hooks, or triggering other jobs.
        """
        pass
```

Cortex provides an `onnx_client` to your Predictor's constructor. `onnx_client` is an instance of [ONNXClient](https://github.com/cortexlabs/cortex/tree/0.28/pkg/cortex/serve/cortex_internal/lib/client/onnx.py) that manages an ONNX Runtime session to make predictions using your model. It should be saved as an instance variable in your Predictor, and your `predict()` function should call `onnx_client.predict()` to make an inference with your exported ONNX model. Preprocessing of the JSON payload and postprocessing of predictions can be implemented in your `predict()` function as well.

When multiple models are defined using the Predictor's `models` field, the `onnx_client.predict()` method expects a second argument `model_name` which must hold the name of the model that you want to use for inference (for example: `self.client.predict(model_input, "text-generator")`).

## Structured logging

You can use Cortex's logger in your predictor implemention to log in JSON. This will enrich your logs with Cortex's metadata, and you can add custom metadata to the logs by adding key value pairs to the `extra` key when using the logger. For example:

```python
...
from cortex_internal.lib.log import logger as cortex_logger

class PythonPredictor:
    def predict(self, payload, batch_id):
        cortex_logger.info("completed processing batch", extra={"batch_id": batch_id, "confidence": confidence})
```

The dictionary passed in via the `extra` will be flattened by one level. e.g.

```
{"asctime": "2021-01-19 15:14:05,291", "levelname": "INFO", "message": "completed processing batch", "process": 235, "batch_id": "iuasyd8f7", "confidence": 0.97}
```

To avoid overriding essential Cortex metadata, please refrain from specifying the following extra keys: `asctime`, `levelname`, `message`, `labels`, and `process`. Log lines greater than 5 MB in size will be ignored.


# Configuration

```yaml
- name: <string>
  kind: BatchAPI
  predictor: # detailed configuration below
  compute: # detailed configuration below
  networking: # detailed configuration below
```

## Predictor

### Python Predictor

```yaml
predictor:
  type: python
  path: <string>  # path to a python file with a PythonPredictor class definition, relative to the Cortex root (required)
  config: <string: value>  # arbitrary dictionary passed to the constructor of the Predictor (can be overridden by config passed in job submission) (optional)
  python_path: <string>  # path to the root of your Python folder that will be appended to PYTHONPATH (default: folder containing cortex.yaml)
  image: <string> # docker image to use for the Predictor (default: quay.io/cortexlabs/python-predictor-cpu:0.28.0 or quay.io/cortexlabs/python-predictor-gpu:0.28.0 based on compute)
  env: <string: string>  # dictionary of environment variables
  log_level: <string>  # log level that can be "debug", "info", "warning" or "error" (default: "info")
  shm_size: <string>  # size of shared memory (/dev/shm) for sharing data between multiple processes, e.g. 64Mi or 1Gi (default: Null)
```

### TensorFlow Predictor

```yaml
predictor:
  type: tensorflow
  path: <string>  # path to a python file with a TensorFlowPredictor class definition, relative to the Cortex root (required)
  models:  # use this to serve a single model or multiple ones
    path: <string>  # S3 path to an exported model (e.g. s3://my-bucket/exported_model) (either this or 'paths' field must be provided)
    paths:  # (either this or 'path' must be provided)
      - name: <string> # unique name for the model (e.g. text-generator) (required)
        path: <string>  # S3 path to an exported model (e.g. s3://my-bucket/exported_model) (required)
        signature_key: <string>  # name of the signature def to use for prediction (required if your model has more than one signature def)
      ...
    signature_key: <string>  # name of the signature def to use for prediction (required if your model has more than one signature def)
  server_side_batching:  # (optional)
    max_batch_size: <int>  # the maximum number of requests to aggregate before running inference
    batch_interval: <duration>  # the maximum amount of time to spend waiting for additional requests before running inference on the batch of requests
  config: <string: value>  # arbitrary dictionary passed to the constructor of the Predictor (can be overridden by config passed in job submission) (optional)
  python_path: <string>  # path to the root of your Python folder that will be appended to PYTHONPATH (default: folder containing cortex.yaml)
  image: <string> # docker image to use for the Predictor (default: quay.io/cortexlabs/tensorflow-predictor:0.28.0)
  tensorflow_serving_image: <string> # docker image to use for the TensorFlow Serving container (default: quay.io/cortexlabs/tensorflow-serving-cpu:0.28.0 or quay.io/cortexlabs/tensorflow-serving-gpu:0.28.0 based on compute)
  env: <string: string>  # dictionary of environment variables
  log_level: <string>  # log level that can be "debug", "info", "warning" or "error" (default: "info")
  shm_size: <string>  # size of shared memory (/dev/shm) for sharing data between multiple processes, e.g. 64Mi or 1Gi (default: Null)
```

### ONNX Predictor

```yaml
predictor:
  type: onnx
  path: <string>  # path to a python file with an ONNXPredictor class definition, relative to the Cortex root (required)
  models:  # use this to serve a single model or multiple ones
    path: <string>  # S3 path to an exported model (e.g. s3://my-bucket/exported_model) (either this or 'paths' must be provided)
    paths:  # (either this or 'path' must be provided)
      - name: <string> # unique name for the model (e.g. text-generator) (required)
        path: <string>  # S3 path to an exported model (e.g. s3://my-bucket/exported_model.onnx) (required)
      ...
  config: <string: value>  # arbitrary dictionary passed to the constructor of the Predictor (can be overridden by config passed in job submission) (optional)
  python_path: <string>  # path to the root of your Python folder that will be appended to PYTHONPATH (default: folder containing cortex.yaml)
  image: <string> # docker image to use for the Predictor (default: quay.io/cortexlabs/onnx-predictor-cpu:0.28.0 or quay.io/cortexlabs/onnx-predictor-gpu:0.28.0 based on compute)
  env: <string: string>  # dictionary of environment variables
  log_level: <string>  # log level that can be "debug", "info", "warning" or "error" (default: "info")
  shm_size: <string>  # size of shared memory (/dev/shm) for sharing data between multiple processes, e.g. 64Mi or 1Gi (default: Null)
```

## Compute

```yaml
compute:
  cpu: <string | int | float>  # CPU request per worker. One unit of CPU corresponds to one virtual CPU; fractional requests are allowed, and can be specified as a floating point number or via the "m" suffix (default: 200m)
  gpu: <int>  # GPU request per worker. One unit of GPU corresponds to one virtual GPU (default: 0)
  mem: <string>  # memory request per worker. One unit of memory is one byte and can be expressed as an integer or by using one of these suffixes: K, M, G, T (or their power-of two counterparts: Ki, Mi, Gi, Ti) (default: Null)
```

## Networking

```yaml
networking:
  endpoint: <string>  # the endpoint for the API (default: <api_name>)
```


# Jobs

## Get the TaskAPI endpoint

```bash
$ cortex get <batch_api_name>
```

## Submit a Job

There are three options for providing the dataset for your job:

1. [Data in the request](#data-in-the-request)
2. [List S3 file paths](#s3-file-paths)
3. [Newline delimited JSON file(s) in S3](#newline-delimited-json-files-in-s3)

### Data in the request

The input data for your job can be included directly in your job submission request by specifying an `item_list` in your json request payload. Each item can be any type (object, list, string, etc.) and is treated as a single sample. `item_list.batch_size` specifies how many items to include in a single batch.

**Each batch must be smaller than 256 KiB, and the total request size must be less than 10 MiB.** If you want to submit more data, explore the other job submission methods.

Submitting data in the request can be useful in the following scenarios:

* the request only has a few items
* each item in the request is small (e.g. urls to images/videos)
* you want to avoid using S3 as an intermediate storage layer

```yaml
POST <batch_api_endpoint>:
{
    "workers": <int>,         # the number of workers to allocate for this job (required)
    "timeout": <int>,         # duration in seconds since the submission of a job before it is terminated (optional)
    "sqs_dead_letter_queue": {      # specify a queue to redirect failed batches (optional)
        "arn": <string>,            # arn of dead letter queue e.g. arn:aws:sqs:us-west-2:123456789:failed.fifo
        "max_receive_count": <int>  # number of a times a batch is allowed to be handled by a worker before it is considered to be failed and transferred to the dead letter queue (must be >= 1)
    },
    "item_list": {
        "items": [            # a list items that can be of any type (required)
            <any>,
            <any>
        ],
        "batch_size": <int>,  # the number of items per batch (the predict() function is called once per batch) (required)
    }
    "config": {               # custom fields for this specific job (will override values in `config` specified in your api configuration) (optional)
        "string": <any>
    }
}

RESPONSE:
{
    "job_id": <string>,
    "api_name": <string>,
    "kind": "BatchAPI",
    "workers": <int>,
    "config": {<string>: <any>},
    "api_id": <string>,
    "sqs_url": <string>,
    "timeout": <int>,
    "sqs_dead_letter_queue": {
        "arn": <string>,
        "max_receive_count": <int>
    },
    "created_time": <string>
}
```

### S3 file paths

If your input data is a list of files such as images/videos in an S3 directory, you can define `file_path_lister` in your submission request payload. You can use `file_path_lister.s3_paths` to specify a list of files or prefixes, and `file_path_lister.includes` and/or `file_path_lister.excludes` to remove unwanted files. The S3 file paths will be aggregated into batches of size `file_path_lister.batch_size`. To learn more about fine-grained S3 file filtering see [filtering files](#filtering-files).

**The total size of a batch must be less than 256 KiB.**

This submission pattern can be useful in the following scenarios:

* you have a list of images/videos in an S3 directory
* each S3 file represents a single sample or a small number of samples

If a single S3 file contains a lot of samples/rows, try the next submission strategy.

```yaml
POST <batch_api_endpoint>:
{
    "workers": <int>,            # the number of workers to allocate for this job (required)
    "timeout": <int>,            # duration in seconds since the submission of a job before it is terminated (optional)
    "sqs_dead_letter_queue": {      # specify a queue to redirect failed batches (optional)
        "arn": <string>,            # arn of dead letter queue e.g. arn:aws:sqs:us-west-2:123456789:failed.fifo
        "max_receive_count": <int>  # number of a times a batch is allowed to be handled by a worker before it is considered to be failed and transferred to the dead letter queue (must be >= 1)
    },
    "file_path_lister": {
        "s3_paths": [<string>],  # can be S3 prefixes or complete S3 paths (required)
        "includes": [<string>],  # glob patterns (optional)
        "excludes": [<string>],  # glob patterns (optional)
        "batch_size": <int>,     # the number of S3 file paths per batch (the predict() function is called once per batch) (required)
    }
    "config": {                  # custom fields for this specific job (will override values in `config` specified in your api configuration) (optional)
        "string": <any>
    }
}

RESPONSE:
{
    "job_id": <string>,
    "api_name": <string>,
    "kind": "BatchAPI",
    "workers": <int>,
    "config": {<string>: <any>},
    "api_id": <string>,
    "sqs_url": <string>,
    "timeout": <int>,
    "sqs_dead_letter_queue": {
        "arn": <string>,
        "max_receive_count": <int>
    },
    "created_time": <string>
}
```

### Newline delimited JSON files in S3

If your input dataset is a newline delimited json file in an S3 directory (or a list of them), you can define `delimited_files` in your request payload to break up the contents of the file into batches of size `delimited_files.batch_size`.

Upon receiving `delimited_files`, your Batch API will iterate through the `delimited_files.s3_paths` to generate the set of S3 files to process. You can use `delimited_files.includes` and `delimited_files.excludes` to filter out unwanted files. Each S3 file will be parsed as a newline delimited JSON file. Each line in the file should be a JSON object, which will be treated as a single sample. The S3 file will be broken down into batches of size `delimited_files.batch_size` and submitted to your workers. To learn more about fine-grained S3 file filtering see [filtering files](#filtering-files).

**The total size of a batch must be less than 256 KiB.**

This submission pattern is useful in the following scenarios:

* one or more S3 files contains a large number of samples and must be broken down into batches

```yaml
POST <batch_api_endpoint>:
{
    "workers": <int>,            # the number of workers to allocate for this job (required)
    "timeout": <int>,            # duration in seconds since the submission of a job before it is terminated (optional)
    "sqs_dead_letter_queue": {      # specify a queue to redirect failed batches (optional)
        "arn": <string>,            # arn of dead letter queue e.g. arn:aws:sqs:us-west-2:123456789:failed.fifo
        "max_receive_count": <int>  # number of a times a batch is allowed to be handled by a worker before it is considered to be failed and transferred to the dead letter queue (must be >= 1)
    },
    "delimited_files": {
        "s3_paths": [<string>],  # can be S3 prefixes or complete S3 paths (required)
        "includes": [<string>],  # glob patterns (optional)
        "excludes": [<string>],  # glob patterns (optional)
        "batch_size": <int>,     # the number of json objects per batch (the predict() function is called once per batch) (required)
    }
    "config": {                  # custom fields for this specific job (will override values in `config` specified in your api configuration) (optional)
        "string": <any>
    }
}

RESPONSE:
{
    "job_id": <string>,
    "api_name": <string>,
    "kind": "BatchAPI",
    "workers": <int>,
    "config": {<string>: <any>},
    "api_id": <string>,
    "sqs_url": <string>,
    "timeout": <int>,
    "sqs_dead_letter_queue": {
        "arn": <string>,
        "max_receive_count": <int>
    },
    "created_time": <string>
}
```

## Get a job's status

```bash
$ cortex get <batch_api_name> <job_id>
```

Or make a GET request to `<batch_api_endpoint>?jobID=<jobID>`:

```yaml
GET <batch_api_endpoint>?jobID=<jobID>:

RESPONSE:
{
    "job_status": {
        "job_id": <string>,
        "api_name": <string>,
        "kind": "BatchAPI",
        "workers": <int>,
        "config": {<string>: <any>},
        "api_id": <string>,
        "sqs_url": <string>,
        "status": <string>,
        "batches_in_queue": <int>        # number of batches remaining in the queue
        "batch_metrics": {
            "succeeded": <int>           # number of succeeded batches
            "failed": int                # number of failed attempts
            "avg_time_per_batch": <float> (optional)  # average time spent working on a batch (only considers successful attempts)
        },
        "worker_counts": {               # worker counts are only available while a job is running
            "pending": <int>,            # number of workers that are waiting for compute resources to be provisioned
            "initializing": <int>,       # number of workers that are initializing (downloading images or running your predictor's init function)
            "running": <int>,            # number of workers that are actively working on batches from the queue
            "succeeded": <int>,          # number of workers that have completed after verifying that the queue is empty
            "failed": <int>,             # number of workers that have failed
            "stalled": <int>,            # number of workers that have been stuck in pending for more than 10 minutes
        },
        "created_time": <string>
        "start_time": <string>
        "end_time": <string> (optional)
    },
    "endpoint": <string>
    "api_spec": {
        ...
    }
}
```

## Stop a job

```bash
$ cortex delete <batch_api_name> <job_id>
```

Or make a DELETE request to `<batch_api_endpoint>?jobID=<jobID>`:

```yaml
DELETE <batch_api_endpoint>?jobID=<jobID>:

RESPONSE:
{"message":"stopped job <job_id>"}
```

## Additional Information

### Filtering files

When submitting a job using `delimited_files` or `file_path_lister`, you can use `s3_paths` in conjunction with `includes` and `excludes` to precisely filter files.

The Batch API will iterate through each S3 path in `s3_paths`. If the S3 path is a prefix, it iterates through each file in that prefix. For each file, if `includes` is non-empty, it will discard the S3 path if the S3 file doesn't match any of the glob patterns provided in `includes`. After passing the `includes` filter (if specified), if the `excludes` is non-empty, it will discard the S3 path if the S3 files matches any of the glob patterns provided in `excludes`.

If you aren't sure which files will be processed in your request, specify the `dryRun=true` query parameter in the job submission request to see the target list.

Here are a few examples of filtering for a folder structure like this:

```
├── s3://bucket
    └── images
        ├── img_1.png
        ├── img_2.jpg
        ├── img_3.jpg
        └── img_4.gif
```

Select all files

```yaml
{
    "s3_paths": ["s3://bucket/images/"]
}

# or

{
    "s3_paths": ["s3://bucket/images/img"]
}

# Would select the following files:
# s3://bucket/images/img_1.png
# s3://bucket/images/img_2.jpg
# s3://bucket/images/img_3.jpg
# s3://bucket/images/img_4.gif
```

Select specific files

```yaml
{
    "s3_paths": [
        "s3://bucket/images/img_1.png",
        "s3://bucket/images/img_2.jpg"
    ]
}

# Would select the following files:
# s3://bucket/images/img_1.png
# s3://bucket/images/img_2.jpg
```

Only select JPG files

```yaml
{
    "s3_paths": ["s3://bucket/images/"],
    "includes": ["**.jpg"]
}

# Would select the following files:
# s3://bucket/images/img_2.jpg
# s3://bucket/images/img_3.jpg
```

Select all JPG files except one specific JPG file

```yaml
{
    "s3_paths": ["s3://bucket/images/"],
    "includes": ["**.jpg"],
    "excludes": ["**_3.jpg"]
}

# Would select the file:
# s3://bucket/images/img_2.jpg
```

Select all files except GIFs

```yaml
{
    "s3_paths": ["s3://bucket/images/"],
    "excludes": ["**.gif"]
}

# Would select the files:
# s3://bucket/images/img_1.png
# s3://bucket/images/img_2.jpg
# s3://bucket/images/img_3.jpg
```


# Statuses

| Status                  | Meaning                                                                                                                                                |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| enqueuing               | Job is being split into batches and placed into a queue                                                                                                |
| running                 | Workers are retrieving batches from the queue and running inference                                                                                    |
| succeeded               | Workers completed all items in the queue without any failures                                                                                          |
| failed while enqueuing  | Failure occurred while enqueuing; check job logs for more details                                                                                      |
| completed with failures | Workers completed all items in the queue but some of the batches weren't processed successfully and raised exceptions; check job logs for more details |
| worker error            | One or more workers experienced an irrecoverable error, causing the job to fail; check job logs for more details                                       |
| out of memory           | One or more workers ran out of memory, causing the job to fail; check job logs for more details                                                        |
| timed out               | Job was terminated after the specified timeout has elapsed                                                                                             |
| stopped                 | Job was stopped by the user or the Batch API was deleted                                                                                               |


# Task APIs


# Example

Create APIs that can perform arbitrary tasks like training or fine-tuning a model.

## Implement

```python
# train_iris.py

import os
import boto3
import pickle
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


class Task:
    def __call__(self, config):
        # get the iris flower dataset
        iris = load_iris()
        data, labels = iris.data, iris.target
        training_data, test_data, training_labels, test_labels = train_test_split(data, labels)
        print("loaded dataset")

        # train the model
        model = LogisticRegression(solver="lbfgs", multi_class="multinomial", max_iter=1000)
        model.fit(training_data, training_labels)
        accuracy = model.score(test_data, test_labels)
        print("model trained; accuracy: {:.2f}".format(accuracy))

        # upload the model
        dest_dir = config["dest_s3_dir"]
        bucket, key = dest_dir.replace("s3://", "").split("/", 1)
        pickle.dump(model, open("model.pkl", "wb"))
        s3 = boto3.client("s3")
        s3.upload_file("model.pkl", bucket, os.path.join(key, "model.pkl"))
        print(f"model uploaded to {dest_dir}/model.pkl")
```

```python
# requirements.txt

boto3
scikit-learn==0.23.2
```

```yaml
# cortex.yaml

- name: train-iris
  kind: TaskAPI
  definition:
    path: train_iris.py
```

## Deploy

```bash
$ cortex deploy
```

## Describe

```bash
$ cortex get train-iris

# > endpoint: http://***.elb.us-west-2.amazonaws.com/train-iris
```

## Submit a job

You can submit a job by making a POST request to the Task API's endpoint.

Using `curl`:

```bash
$ export TASK_API_ENDPOINT=<TASK_API_ENDPOINT>  # e.g. export TASK_API_ENDPOINT=https://***.elb.us-west-2.amazonaws.com/train-iris
$ export DEST_S3_DIR=<YOUR_S3_DIRECTORY>  # e.g. export DEST_S3_DIR=s3://my-bucket/dir

$ curl $TASK_API_ENDPOINT \
    -X POST -H "Content-Type: application/json" \
    -d "{\"config\": {\"dest_s3_dir\": \"$DEST_S3_DIR\"}}"
# > {"job_id":"69b183ed6bdf3e9b","api_name":"train-iris",...}
```

Or, using Python `requests`:

```python
import cortex
import requests

cx = cortex.client("aws")  # "aws" is the name of the Cortex environment used in this example
task_endpoint = cx.get_api("train-iris")["endpoint"]

dest_s3_dir =  # S3 directory where the model will be uploaded, e.g. "s3://my-bucket/dir"
job_spec = {
    "config": {
        "dest_s3_dir": dest_s3_dir
    }
}
response = requests.post(task_endpoint, json=job_spec)
print(response.text)
# > {"job_id":"69b183ed6bdf3e9b","api_name":"train-iris",...}
```

## Monitor the job

```bash
$ cortex get train-iris 69b183ed6bdf3e9b
```

## View the results

Once the job is complete, you should be able to find the trained model in the directory you've specified.

## Delete

```bash
$ cortex delete train-iris
```


# Definition

## Project files

Cortex makes all files in the project directory (i.e. the directory which contains `cortex.yaml`) available for use in your Task implementation. Python bytecode files (`*.pyc`, `*.pyo`, `*.pyd`), files or folders that start with `.`, and the api configuration file (e.g. `cortex.yaml`) are excluded.

The following files can also be added at the root of the project's directory:

* `.cortexignore` file, which follows the same syntax and behavior as a [.gitignore file](https://git-scm.com/docs/gitignore).
* `.env` file, which exports environment variables that can be used in the task. Each line of this file must follow the `VARIABLE=value` format.

For example, if your directory looks like this:

```
./my-classifier/
├── cortex.yaml
├── values.json
├── task.py
├── ...
└── requirements.txt
```

You can access `values.json` in your Task like this:

```python
import json

class Task:
    def __call__(self, config):
        with open('values.json', 'r') as values_file:
            values = json.load(values_file)
        self.values = values
```

## Task

### Interface

```python
# initialization code and variables can be declared here in global scope

class Task:
    def __call__(self, config):
        """(Required) Task runnable.

        Args:
            config (required): Dictionary passed from API configuration (if
                specified) merged with configuration passed in with Job
                Submission API. If there are conflicting keys, values in
                configuration specified in Job submission takes precedence.
        """
        pass
```

## Structured logging

You can use Cortex's logger in your predictor implementation to log in JSON. This will enrich your logs with Cortex's metadata, and you can add custom metadata to the logs by adding key value pairs to the `extra` key when using the logger. For example:

```python
...
from cortex_internal.lib.log import logger as cortex_logger

class Task:
    def __call__(self, config):
        ...
        cortex_logger.info("completed validations", extra={"accuracy": accuracy})
```

The dictionary passed in via the `extra` will be flattened by one level. e.g.

```
{"asctime": "2021-01-19 15:14:05,291", "levelname": "INFO", "message": "completed validations", "process": 235, "accuracy": 0.97}
```

To avoid overriding essential Cortex metadata, please refrain from specifying the following extra keys: `asctime`, `levelname`, `message`, `labels`, and `process`. Log lines greater than 5 MB in size will be ignored.


# Configuration

```yaml
- name: <string>  # API name (required)
  kind: TaskAPI
  definition:
    path: <string>  # path to a python file with a Task class definition, relative to the Cortex root (required)
    config: <string: value>  # arbitrary dictionary passed to the callable method of the Task class (can be overridden by config passed in job submission) (optional)
    python_path: <string>  # path to the root of your Python folder that will be appended to PYTHONPATH (default: folder containing cortex.yaml)
    image: <string> # docker image to use for the Task (default: quay.io/cortexlabs/python-predictor-cpu:0.28.0, quay.io/cortexlabs/python-predictor-gpu:0.28.0, or quay.io/cortexlabs/python-predictor-inf:0.28.0 based on compute)
    env: <string: string>  # dictionary of environment variables
    log_level: <string>  # log level that can be "debug", "info", "warning" or "error" (default: "info")
  networking:
    endpoint: <string>  # the endpoint for the API (default: <api_name>)
  compute:
    cpu: <string | int | float>  # CPU request per worker. One unit of CPU corresponds to one virtual CPU; fractional requests are allowed, and can be specified as a floating point number or via the "m" suffix (default: 200m)
    gpu: <int>  # GPU request per worker. One unit of GPU corresponds to one virtual GPU (default: 0)
    inf: <int> # Inferentia request per worker. One unit corresponds to one Inferentia ASIC with 4 NeuronCores and 8GB of cache memory. Each process will have one NeuronCore Group with (4 * inf / processes_per_replica) NeuronCores, so your model should be compiled to run on (4 * inf / processes_per_replica) NeuronCores. (default: 0) (aws only)
    mem: <string>  # memory request per worker. One unit of memory is one byte and can be expressed as an integer or by using one of these suffixes: K, M, G, T (or their power-of two counterparts: Ki, Mi, Gi, Ti) (default: Null)
```


# Jobs

## Get the TaskAPI endpoint

```bash
$ cortex get <task_api_name>
```

## Submit a Job

```yaml
POST <task_api_endpoint>:
{
    "timeout": <int>,  # duration in seconds since the submission of a job before it is terminated (optional)
    "config": {  # custom fields for this specific job (will override values in `config` specified in your api configuration) (optional)
        "string": <any>
    }
}

RESPONSE:
{
    "job_id": <string>,
    "api_name": <string>,
    "kind": "TaskAPI",
    "workers": 1,
    "config": {<string>: <any>},
    "api_id": <string>,
    "timeout": <int>,
    "created_time": <string>
}
```

## Get a job's status

```bash
$ cortex get <task_api_name> <job_id>
```

Or make a GET request to `<task_api_endpoint>?jobID=<jobID>`:

```yaml
GET <task_api_endpoint>?jobID=<jobID>:

RESPONSE:
{
    "job_status": {
        "job_id": <string>,
        "api_name": <string>,
        "kind": "TaskAPI",
        "workers": 1,
        "config": {<string>: <any>},
        "api_id": <string>,
        "status": <string>,
        "created_time": <string>
        "start_time": <string>
        "end_time": <string> (optional)
    },
    "endpoint": <string>
    "api_spec": {
        ...
    }
}
```

## Stop a job

```bash
$ cortex delete <task_api_name> <job_id>
```

Or make a DELETE request to `<task_api_endpoint>?jobID=<jobID>`:

```yaml
DELETE <task_api_endpoint>?jobID=<jobID>:

RESPONSE:
{"message":"stopped job <job_id>"}
```


# Statuses

| Status        | Meaning                                                                                                   |
| ------------- | --------------------------------------------------------------------------------------------------------- |
| running       | Task is running                                                                                           |
| succeeded     | Task has finished without errors                                                                          |
| worker error  | The task has experienced an irrecoverable error, causing the job to fail; check job logs for more details |
| out of memory | The task has ran out of memory, causing the job to fail; check job logs for more details                  |
| timed out     | Job was terminated after the specified timeout has elapsed                                                |
| stopped       | Job was stopped by the user or the Task API was deleted                                                   |


# Dependencies


# Example

You can deploy an API by providing a project directory. Cortex will save the project directory and make it available during API initialization.

```bash
project/
  ├── model.py
  ├── util.py
  ├── predictor.py
  ├── requirements.txt
  └── ...
```

You can define your Predictor class in a separate python file and import code from your project.

```python
# predictor.py

from model import MyModel

class PythonPredictor:
    def __init__(self, config):
        model = MyModel()

    def predict(payload):
        return model(payload)
```

## Deploy using the Python Client

```python
import cortex

api_spec = {
    "name": "text-generator",
    "kind": "RealtimeAPI",
    "predictor": {
        "type": "python",
        "path": "predictor.py"
    }
}

cx = cortex.client("aws")
cx.create_api(api_spec, project_dir=".")
```

## Deploy using the CLI

```yaml
# api.yaml

- name: text-generator
  kind: RealtimeAPI
  predictor:
    type: python
    path: predictor.py
```

```bash
$ cortex deploy api.yaml
```


# Python packages

## PyPI packages

You can install your required PyPI packages and import them in your Python files using pip. Cortex looks for a `requirements.txt` file in the top level Cortex project directory (i.e. the directory which contains `cortex.yaml`):

```
./my-classifier/
├── cortex.yaml
├── predictor.py
├── ...
└── requirements.txt
```

If you want to use `conda` to install your python packages, see the [Conda section](#conda-packages) below.

Note that some packages are pre-installed by default (see "pre-installed packages" for your Predictor type in the Realtime API Predictor documentation and Batch API Predictor documentation).

## Private PyPI packages

To install packages from a private PyPI index, create a `pip.conf` inside the same directory as `requirements.txt`, and add the following contents:

```
[global]
extra-index-url = https://<username>:<password>@<my-private-index>.com/pip
```

In same directory, create a [`dependencies.sh` script](https://docs.cortexlabs.com/workloads/dependencies/system-packages) and add the following:

```bash
cp pip.conf /etc/pip.conf
```

You may now add packages to `requirements.txt` which are found in the private index.

## GitHub packages

You can also install public/private packages from git registries (such as GitHub) by adding them to `requirements.txt`. Here's an example for GitHub:

```
# requirements.txt

# public access
git+https://github.com/<username>/<repo name>.git@<tag or branch name>#egg=<package name>

# private access
git+https://<personal access token>@github.com/<username>/<repo name>.git@<tag or branch name>#egg=<package name>
```

On GitHub, you can generate a personal access token by following [these steps](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line).

## Installing with Setup

Python packages can also be installed by providing a `setup.py` that describes your project's modules. Here's an example directory structure:

```
./my-classifier/
├── cortex.yaml
├── predictor.py
├── ...
├── mypkg
│   └── __init__.py
├── requirements.txt
└── setup.py
```

In this case, `requirements.txt` will have this form:

```
# requirements.txt

.
```

## Conda packages

Cortex supports installing Conda packages. We recommend only using Conda when your required packages are not available in PyPI. Cortex looks for a `conda-packages.txt` file in the top level Cortex project directory (i.e. the directory which contains `cortex.yaml`):

```
./my-classifier/
├── cortex.yaml
├── predictor.py
├── ...
└── conda-packages.txt
```

The `conda-packages.txt` file follows the format of `conda list --export`. Each line of `conda-packages.txt` should follow this pattern: `[channel::]package[=version[=buildid]]`.

Here's an example of `conda-packages.txt`:

```
conda-forge::rdkit
conda-forge::pygpu
```

In situations where both `requirements.txt` and `conda-packages.txt` are provided, Cortex installs Conda packages in `conda-packages.txt` followed by PyPI packages in `requirements.txt`. Conda and Pip package managers install packages and dependencies independently. You may run into situations where Conda and pip package managers install different versions of the same package because they install and resolve dependencies independently from one another. To resolve package version conflicts, it may be in your best interest to specify their exact versions in `conda-packages.txt`.

The current version of Python is `3.6.9`. Updating Python to a different version is possible with Conda, but there are no guarantees that Cortex's web server will continue functioning correctly. If there's a change in Python's version, the necessary core packages for the web server will be reinstalled. If you are using a custom base image, any other Python packages that are built in to the image won't be accessible at runtime.

Check the [best practices](https://www.anaconda.com/using-pip-in-a-conda-environment/) on using `pip` inside `conda`.


# System packages

Cortex looks for a file named `dependencies.sh` in the top level Cortex project directory (i.e. the directory which contains `cortex.yaml`). For example:

```
./my-classifier/
├── cortex.yaml
├── predictor.py
├── ...
└── dependencies.sh
```

`dependencies.sh` is executed with `bash` shell during the initialization of each replica (before installing Python packages in `requirements.txt` or `conda-packages.txt`). Typical use cases include installing required system packages to be used in your Predictor, building Python packages from source, etc.

Here is an example `dependencies.sh`, which installs the `tree` utility:

```bash
apt-get update && apt-get install -y tree
```

The `tree` utility can now be called inside your `predictor.py`:

```python
# predictor.py
import subprocess

class PythonPredictor:
    def __init__(self, config):
        subprocess.run(["tree"])
    ...
```


# Custom images

Cortex includes a default set of Docker images with pre-installed Python and system packages but you can build custom images for use in your APIs. Common reasons to do this are to avoid installing dependencies during replica initialization, to have smaller images, and/or to mirror images to your cloud's container registry (for speed and reliability).

## Create a Dockerfile

```bash
mkdir my-api && cd my-api && touch Dockerfile
```

Cortex's base Docker images are listed below. Depending on the Cortex Predictor and compute type specified in your API configuration, choose one of these images to use as the base for your Docker image:

* Python Predictor (CPU): `quay.io/cortexlabs/python-predictor-cpu-slim:0.28.0`
* Python Predictor (GPU): choose one of the following:
  * `quay.io/cortexlabs/python-predictor-gpu-slim:0.28.0-cuda10.0-cudnn7`
  * `quay.io/cortexlabs/python-predictor-gpu-slim:0.28.0-cuda10.1-cudnn7`
  * `quay.io/cortexlabs/python-predictor-gpu-slim:0.28.0-cuda10.1-cudnn8`
  * `quay.io/cortexlabs/python-predictor-gpu-slim:0.28.0-cuda10.2-cudnn7`
  * `quay.io/cortexlabs/python-predictor-gpu-slim:0.28.0-cuda10.2-cudnn8`
  * `quay.io/cortexlabs/python-predictor-gpu-slim:0.28.0-cuda11.0-cudnn8`
  * `quay.io/cortexlabs/python-predictor-gpu-slim:0.28.0-cuda11.1-cudnn8`
* Python Predictor (Inferentia): `quay.io/cortexlabs/python-predictor-inf-slim:0.28.0`
* TensorFlow Predictor (CPU, GPU, Inferentia): `quay.io/cortexlabs/tensorflow-predictor-slim:0.28.0`
* ONNX Predictor (CPU): `quay.io/cortexlabs/onnx-predictor-cpu-slim:0.28.0`
* ONNX Predictor (GPU): `quay.io/cortexlabs/onnx-predictor-gpu-slim:0.28.0`

Note: the images listed above use the `-slim` suffix; Cortex's default API images are not `-slim`, since they have additional dependencies installed to cover common use cases. If you are building your own Docker image, starting with a `-slim` Predictor image will result in a smaller image size.

The sample `Dockerfile` below inherits from Cortex's Python CPU serving image, and installs 3 packages. `tree` is a system package and `pandas` and `rdkit` are Python packages.

```
# Dockerfile

FROM quay.io/cortexlabs/python-predictor-cpu-slim:0.28.0

RUN apt-get update \
    && apt-get install -y tree \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir pandas \
    && conda install -y conda-forge::rdkit \
    && conda clean -a
```

## Build your image

```bash
docker build . -t org/my-api:latest
```

## Push your image to a container registry

You can push your built Docker image to a public registry of your choice (e.g. Docker Hub), or to a private registry on ECR or Docker Hub.

For example, to use ECR, first create a repository to store your image:

```bash
# We create a repository in ECR

export AWS_REGION="***"
export AWS_ACCESS_KEY_ID="***"
export AWS_SECRET_ACCESS_KEY="***"
export REGISTRY_URL="***"  # this will be in the format "<aws_account_id>.dkr.ecr.<aws_region>.amazonaws.com"

aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $REGISTRY_URL

aws ecr create-repository --repository-name=org/my-api --region=$AWS_REGION
# take note of repository url
```

Build and tag your image, and push it to your ECR repository:

```bash
docker build . -t org/my-api:latest -t <repository_url>:latest

docker push <repository_url>:latest
```

## Configure your API

```yaml
# cortex.yaml

- name: my-api
  ...
  predictor:
    image: <repository_url>:latest
  ...
```

Note: for TensorFlow Predictors, two containers run together to serve predictions: one runs your Predictor code (`quay.io/cortexlabs/tensorflow-predictor`), and the other is TensorFlow serving to load the SavedModel (`quay.io/cortexlabs/tensorflow-serving-gpu` or `quay.io/cortexlabs/tensorflow-serving-cpu`). There's a second available field `tensorflow_serving_image` that can be used to override the TensorFlow Serving image. Both of the default serving images (`quay.io/cortexlabs/tensorflow-serving-gpu` and `quay.io/cortexlabs/tensorflow-serving-cpu`) are based on the official TensorFlow Serving image (`tensorflow/serving`). Unless a different version of TensorFlow Serving is required, the TensorFlow Serving image shouldn't have to be overridden, since it's only used to load the SavedModel and does not run your Predictor code.


# Cortex Cloud on AWS


# Install

## Prerequisites

1. [Docker](https://docs.docker.com/install) must be installed and running on your machine (to verify, check that running `docker ps` does not return an error)
2. Subscribe to the [EKS-optimized AMI with GPU Support](https://aws.amazon.com/marketplace/pp/B07GRHFXGM) (for GPU clusters)
3. An IAM user with `AdministratorAccess` and programmatic access (see [security](https://docs.cortexlabs.com/clusters/cortex-cloud-on-aws/security) if you'd like to use less privileged credentials after spinning up your cluster)
4. You may need to [request a limit increase](https://console.aws.amazon.com/servicequotas/home?#!/services/ec2/quotas) for your desired instance type

## Spin up Cortex on your AWS account

```bash
# install the CLI
pip install cortex

# spin up Cortex on your AWS account
cortex cluster up  # or: cortex cluster up --config cluster.yaml (see configuration options below)
```

## Configure Cortex

```yaml
# cluster.yaml

# EKS cluster name
cluster_name: cortex

# AWS region
region: us-east-1

# list of availability zones for your region
availability_zones:  # default: 3 random availability zones in your region, e.g. [us-east-1a, us-east-1b, us-east-1c]

# instance type
instance_type: m5.large

# minimum number of instances
min_instances: 1

# maximum number of instances
max_instances: 5

# disk storage size per instance (GB)
instance_volume_size: 50

# instance volume type [gp2 | io1 | st1 | sc1]
instance_volume_type: gp2

# instance volume iops (only applicable to io1)
# instance_volume_iops: 3000

# subnet visibility [public (instances will have public IPs) | private (instances will not have public IPs)]
subnet_visibility: public

# NAT gateway (required when using private subnets) [none | single | highly_available (a NAT gateway per availability zone)]
nat_gateway: none

# API load balancer scheme [internet-facing | internal]
api_load_balancer_scheme: internet-facing

# operator load balancer scheme [internet-facing | internal]
# note: if using "internal", you must configure VPC Peering to connect your CLI to your cluster operator
operator_load_balancer_scheme: internet-facing

# to install Cortex in an existing VPC, you can provide a list of subnets for your cluster to use
# subnet_visibility (specified above in this file) must match your subnets' visibility
# this is an advanced feature (not recommended for first-time users) and requires your VPC to be configured correctly; see https://eksctl.io/usage/vpc-networking/#use-existing-vpc-other-custom-configuration
# here is an example:
# subnets:
#   - availability_zone: us-west-2a
#     subnet_id: subnet-060f3961c876872ae
#   - availability_zone: us-west-2b
#     subnet_id: subnet-0faed05adf6042ab7

# additional tags to assign to AWS resources (all resources will automatically be tagged with cortex.dev/cluster-name: <cluster_name>)
tags:  # <string>: <string> map of key/value pairs

# enable spot instances
spot: false

# SSL certificate ARN (only necessary when using a custom domain)
ssl_certificate_arn:

# primary CIDR block for the cluster's VPC
vpc_cidr: 192.168.0.0/16
```

The docker images used by the Cortex cluster can also be overridden, although this is not common. They can be configured by adding any of these keys to your cluster configuration file (default values are shown):

```yaml
image_operator: quay.io/cortexlabs/operator:0.28.0
image_manager: quay.io/cortexlabs/manager:0.28.0
image_downloader: quay.io/cortexlabs/downloader:0.28.0
image_request_monitor: quay.io/cortexlabs/request-monitor:0.28.0
image_cluster_autoscaler: quay.io/cortexlabs/cluster-autoscaler:0.28.0
image_metrics_server: quay.io/cortexlabs/metrics-server:0.28.0
image_inferentia: quay.io/cortexlabs/inferentia:0.28.0
image_neuron_rtd: quay.io/cortexlabs/neuron-rtd:0.28.0
image_nvidia: quay.io/cortexlabs/nvidia:0.28.0
image_fluent_bit: quay.io/cortexlabs/fluent-bit:0.28.0
image_istio_proxy: quay.io/cortexlabs/istio-proxy:0.28.0
image_istio_pilot: quay.io/cortexlabs/istio-pilot:0.28.0
image_prometheus: quay.io/cortexlabs/prometheus:0.28.0
image_prometheus_config_reloader: quay.io/cortexlabs/prometheus-config-reloader:0.28.0
image_prometheus_operator: quay.io/cortexlabs/prometheus-operator:0.28.0
image_prometheus_statsd_exporter: quay.io/cortexlabs/prometheus-statsd-exporter:0.28.0
image_prometheus_to_cloudwatch: quay.io/cortexlabs/prometheus-to-cloudwatch:0.28.0
```


# Update

## Update Cortex configuration

```bash
cortex cluster configure  # or: cortex cluster configure --config cluster.yaml
```

## Upgrade to a newer version of Cortex

```bash
# spin down your cluster
cortex cluster down

# update your CLI to the latest version
pip install --upgrade cortex

# confirm version
cortex version

# spin up your cluster
cortex cluster up
```

## Upgrade without downtime

In production environments, you can upgrade your cluster without downtime if you have a backend service or DNS in front of your Cortex cluster:

1. Spin up a new cluster. For example: `cortex cluster up --config new-cluster.yaml --configure-env new` (this will create a CLI environment named `new` for accessing the new cluster).
2. Re-deploy your APIs in your new cluster. For example, if the name of your CLI environment for your old cluster is `old`, you can use `cortex get --env old` to list all running APIs in your old cluster, and re-deploy them in the new cluster by changing directories to each API's project folder and running `cortex deploy --env new`.
3. Route requests to your new cluster.
   * If you are using a custom domain: update the A record in your Route 53 hosted zone to point to your new cluster's API load balancer.
   * If you have a backend service which makes requests to Cortex: update your backend service to make requests to the new cluster's endpoints.
   * If you have a self-managed API Gateway in front of your Cortex cluster: update the routes to use new cluster's endpoints.
4. Spin down your old cluster. If you updated DNS settings, wait 24-48 hours before spinning down your old cluster to allow the DNS cache to be flushed.


# Security

## Private cluster subnets

By default, instances are created in public subnets and are assigned public IP addresses. You can configure all instances in your cluster to use private subnets by setting `subnet_visibility: private` in your [cluster configuration](https://docs.cortexlabs.com/clusters/cortex-cloud-on-aws/install) file before creating your cluster. If private subnets are used, instances will not have public IP addresses, and Cortex will create a NAT gateway to allow outgoing network requests.

## Private APIs

See [networking](https://docs.cortexlabs.com/clusters/cortex-cloud-on-aws/index) for a discussion of API visibility.

## Private operator

By default, the Cortex cluster operator's load balancer is internet-facing, and therefore publicly accessible (the operator is what the `cortex` CLI connects to). The operator's load balancer can be configured to be private by setting `operator_load_balancer_scheme: internal` in your [cluster configuration](https://docs.cortexlabs.com/clusters/cortex-cloud-on-aws/install) file. If you do this, you will need to configure [VPC Peering](https://docs.cortexlabs.com/clusters/cortex-cloud-on-aws/index/vpc-peering) to allow your CLI to connect to the Cortex operator (this will be necessary to run any `cortex` commands).

## IAM permissions

If you are not using a sensitive AWS account and do not have a lot of experience with IAM configuration, attaching the built-in `AdministratorAccess` policy to your IAM user will make getting started much easier. If you would like to limit IAM permissions, continue reading.

Cortex uses AWS credentials for 3 main purposes:

1. Spinning up a cluster (credentials with `AdministratorAccess` is recommended)
2. Cluster runtime (see [operator policy](#operator))
3. CLI authentication (no special permissions are required)

### Cluster spin-up

You can specify credentials for spinning up the cluster in four ways (in order of precedence):

1. You can specify `--aws-key` and `--aws-secret` flags with the command `cortex cluster up` to indicate the credentials that will be used to create your cluster. Optionally, you can specify `--cluster-aws-key` and `--cluster-aws-secret` to specify credentials which will be used by the cluster. When all four flags are specified, the credentials used when spinning up the cluster will not be used by the cluster itself. If `--cluster-aws-key` and `--cluster-aws-secret` flags are not specified, then they'll get set to the values of `--aws-key` and `--aws-secret` respectively.
2. From your Cortex CLI cluster cache. If a cluster with the same name and region has existed before, the AWS credentials of that will now be used for the current creation of the cluster.
3. You can export the environment variables `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` which will be used to create your cluster. Optionally, you can export `CLUSTER_AWS_ACCESS_KEY_ID` and `CLUSTER_AWS_SECRET_ACCESS_KEY` to specify credentials which will be used by the cluster. When all four environment variables are set, the credentials used when spinning up the cluster will not be used by the cluster itself. If `CLUSTER_AWS_ACCESS_KEY_ID` and `CLUSTER_AWS_SECRET_ACCESS_KEY` environment variables are not set, then they'll get set to the values of `AWS_ACCESS_KEY_ID` and `AWS_SECRET_ACCESS_KEY` respectively.
4. You can configure the shared AWS credentials with `aws configure` which will then be used to create your cluster.
5. You can specify the AWS credentials `"aws access key id"` and `"aws secret access key"` at the CLI's prompt when requested.

It is recommended to use an IAM user with the `AdministratorAccess` policy to create your cluster, since the CLI requires many permissions for this step, and the list of permissions is evolving as Cortex adds new features. If it is not possible to use `AdministratorAccess` in your existing AWS account, you could create a separate AWS account for your Cortex cluster, or you could ask someone within your organization to create the Cortex cluster for you.

### Operator

A process called the Cortex operator runs on your cluster and is responsible for deploying and managing your APIs on the cluster. The operator will use the designated cluster credentials (e.g. `--cluster-aws-key` or `$CLUSTER_AWS_ACCESS_KEY_ID`) if specified, otherwise it will default to using the credentials used to spin up the cluster (e.g. `--aws-key` or `$AWS_ACCESS_KEY_ID`).

The operator requires read permissions for any S3 bucket containing exported models, read/write permissions for the Cortex S3 bucket, read permissions for ECR, read permissions for ELB, read/write permissions for CloudWatch metrics, and read/write permissions for the Cortex CloudWatch log group. The policy below may be used to restrict the Operator's access:

```javascript
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "s3:*",
            "Resource": "*"
        },
        {
            "Action": [
                "sts:GetCallerIdentity",
                "ecr:GetAuthorizationToken",
                "ecr:BatchGetImage",
                "elasticloadbalancing:Describe*",
                "cloudwatch:*",
                "logs:*",
                "sqs:*"
            ],
            "Effect": "Allow",
            "Resource": "*"
        }
    ]
}
```

It is possible to further restrict access by limiting access to particular resources (e.g. allowing access to only the bucket containing your models and the cortex bucket).

### Running `cortex cluster` commands from different IAM users

By default, the `cortex cluster *` commands can only be executed by the IAM user who created the Cortex cluster. To grant access to additional IAM users, follow these steps:

1. Install `eksctl` by following these [instructions](https://eksctl.io/introduction/#installation).
2. Determine the ARN of the IAM user that you would like to grant access to. You can get the ARN via the [IAM dashboard](https://console.aws.amazon.com/iam/home#/users), or by running `aws iam get-user` on a machine that is authenticated as the IAM user (or `AWS_ACCESS_KEY_ID=*** AWS_SECRET_ACCESS_KEY=*** aws iam get-user` on any machine, using the credentials of the IAM user). The ARN should look similar to `arn:aws:iam::764403040417:user/my-username`.
3. Set the following environment variables:

   ```bash
    CREATOR_AWS_ACCESS_KEY_ID=***      # access key ID for the IAM user that created the cluster
    CREATOR_AWS_SECRET_ACCESS_KEY=***  # secret access key for the IAM user that created the cluster
    NEW_USER_ARN=***                   # ARN of the IAM user to grant access to
    CLUSTER_NAME=***                   # the name of your cortex cluster (will be "cortex" unless you specified a different name in your cluster configuration file)
    CLUSTER_REGION=***                 # the region of your cortex cluster
   ```
4. Run the following command:

   ```bash
    AWS_ACCESS_KEY_ID=$CREATOR_AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY=$CREATOR_AWS_SECRET_ACCESS_KEY eksctl create iamidentitymapping --region $CLUSTER_REGION --cluster $CLUSTER_NAME --arn $NEW_USER_ARN --group system:masters --username $NEW_USER_ARN
   ```
5. To revoke access in the future, run:

   ```bash
    AWS_ACCESS_KEY_ID=$CREATOR_AWS_ACCESS_KEY_ID AWS_SECRET_ACCESS_KEY=$CREATOR_AWS_SECRET_ACCESS_KEY eksctl delete iamidentitymapping --region $CLUSTER_REGION --cluster $CLUSTER_NAME --arn $NEW_USER_ARN --all
   ```


# Logging

By default, logs will be pushed to [CloudWatch](https://console.aws.amazon.com/cloudwatch/home) using fluent-bit. A log group with the same name as your cluster will be created to store your logs. API logs are tagged with labels to help with log aggregation and filtering. Below are some sample CloudWatch Log Insight queries:

RealtimeAPI:

```
fields @timestamp, log
| filter labels.apiName="<INSERT API NAME>"
| filter labels.apiKind="RealtimeAPI"
| sort @timestamp asc
| limit 1000
```

BatchAPI:

```
fields @timestamp, log
| filter labels.apiName="<INSERT API NAME>"
| filter labels.jobID="<INSERT JOB ID>"
| filter labels.apiKind="BatchAPI"
| sort @timestamp asc
| limit 1000
```

TaskAPI:

```
fields @timestamp, log
| filter labels.apiName="<INSERT API NAME>"
| filter labels.jobID="<INSERT JOB ID>"
| filter labels.apiKind="TaskAPI"
| sort @timestamp asc
| limit 1000
```

Please make sure to select the log group for your cluster and adjust the time range accordingly before running the queries.

## Structured logging

You can use Cortex's logger in your Python code to log in JSON, which will enrich your logs with Cortex's metadata, and enable you to add custom metadata to the logs. See the structured logging docs for [Realtime](https://docs.cortexlabs.com/workloads/realtime-apis/predictors#structured-logging), [Batch](https://docs.cortexlabs.com/workloads/batch-apis/predictors#structured-logging), and [Task](https://docs.cortexlabs.com/workloads/task-apis/definitions#structured-logging) APIs.


# Spot instances

```yaml
# cluster.yaml

# whether to use spot instances in the cluster (default: false)
spot: false

spot_config:
  # additional instance types with identical or better specs than the primary cluster instance type (defaults to only the primary instance type)
  instance_distribution: # [similar_instance_type_1, similar_instance_type_2]

  # minimum number of on demand instances (default: 0)
  on_demand_base_capacity: 0

  # percentage of on demand instances to use after the on demand base capacity has been met [0, 100] (default: 50)
  # note: setting this to 0 may hinder cluster scale up when spot instances are not available
  on_demand_percentage_above_base_capacity: 0

  # max price for spot instances (default: the on-demand price of the primary instance type)
  max_price: # <float>

  # number of spot instance pools across which to allocate spot instances [1, 20] (default: number of instances in instance distribution)
  instance_pools: 3

  # fallback to on-demand instances if spot instances were unable to be allocated (default: true)
  on_demand_backup: true
```

Spot instances are not guaranteed to be available. The chances of getting spot instances can be improved by providing `instance_distribution`, a list of alternative instance types to the primary `instance_type` you specified. If left blank, Cortex will only include the primary instance type in the `instance_distribution`. When using `instance_distribution`, use the instance type with the fewest compute resources as your primary `instance_type`. Note that the default value for `max_price` is the on-demand price of the primary instance type, but you may wish to set this to the on-demand price of the most expensive instance type in your `instance_distribution`.

Spot instances can be mixed with on-demand instances by configuring `on_demand_base_capacity` and `on_demand_percentage_above_base_capacity`. `on_demand_base_capacity` enforces the minimum number of nodes that will be fulfilled by on-demand instances as your cluster is scaling up. `on_demand_percentage_above_base_capacity` defines the percentage of instances that will be on-demand after the base capacity has been fulfilled (the rest being spot instances). `instance_pools` is the number of pools per availability zone to allocate your instances from. See [here](https://docs.aws.amazon.com/autoscaling/ec2/APIReference/API_InstancesDistribution.html) for more details.

Even if multiple instances are specified in your `instance_distribution` on-demand instances are mixed, there is still a possibility of running into scale up issues when attempting to spin up spot instances. Spot instance requests may not be fulfilled for several reasons. Spot instance pricing fluctuates, therefore the `max_price` may be lower than the current spot pricing rate. Another possibility could be that the availability zones of the cluster ran out of spot instances. `on_demand_backup` can be used mitigate the impact of unfulfilled spot requests by enabling the cluster to spin up on-demand instances if spot instance requests are not fulfilled within 5 minutes.

There is a spot instance limit associated with your AWS account for each instance family in each region. You can check your current limit and request an increase [here](https://console.aws.amazon.com/servicequotas/home?#!/services/ec2/quotas) (set the region in the upper right corner to your desired region, type "spot" in the search bar, and click on the quota that matches your instance type). Note that the quota values indicate the number of vCPUs available, not the number of instances; different instances have a different numbers of vCPUs, which can be seen [here](https://aws.amazon.com/ec2/instance-types/).

## Example spot configuration

### Only spot instances with backup

```yaml
spot: true

spot_config:
    on_demand_base_capacity: 0
    on_demand_percentage_above_base_capacity: 0
    on_demand_backup: true # recommended for production clusters
```

### 3 on-demand base capacity with 0% on-demand above base capacity

```yaml
min_instances: 0
max_instances: 5

spot: true
spot_config:
    on_demand_base_capacity: 3
    on_demand_percentage_above_base_capacity: 0

# instance 1-3: on-demand
# instance 4-5: spot
```

### 0 on-demand base capacity with 50% on-demand above base capacity

```yaml
min_instances: 0
max_instances: 4

spot: true
spot_config:
    on_demand_base_capacity: 0
    on_demand_percentage_above_base_capacity: 50

# instance 1: on-demand
# instance 2: spot
# instance 3: on-demand
# instance 4: spot
```


# Networking

![api architecture diagram](https://user-images.githubusercontent.com/808475/103417256-dd6e9700-4b3e-11eb-901e-90425f1f8fd4.png)

All APIs share a single API load balancer. By default, the API load balancer is public. You can configure your API load balancer to be private by setting `api_load_balancer_scheme: internal` in your cluster configuration file (before creating your cluster). This will make your API only accessible through [VPC Peering](https://docs.cortexlabs.com/clusters/cortex-cloud-on-aws/index/vpc-peering).

The SSL certificate on the API load balancer is autogenerated during installation using `localhost` as the Common Name (CN). Therefore, clients will need to skip certificate verification when making HTTPS requests to your APIs (e.g. `curl -k https://***`), or make HTTP requests instead (e.g. `curl http://***`). Alternatively, you can enable HTTPS by using a [custom domain](https://docs.cortexlabs.com/clusters/cortex-cloud-on-aws/index/custom-domain) or by [creating an API Gateway](https://docs.cortexlabs.com/clusters/cortex-cloud-on-aws/index/https) to forward requests to your API load balancer.

There is a separate load balancer for the Cortex operator. By default, the operator load balancer is public. You can configure your operator load balancer to be private by setting `operator_load_balancer_scheme: internal` in your cluster configuration file (before creating your cluster). You can use [VPC Peering](https://docs.cortexlabs.com/clusters/cortex-cloud-on-aws/index/vpc-peering) to enable your Cortex CLI to connect to your cluster operator from another VPC.


# Custom domain

You can use any custom domain (that you own) for your prediction endpoints. For example, you can make your API accessible via `api.example.com/text-generator`. This guide will demonstrate how to create a dedicated subdomain in AWS Route 53 and, if desired, configure your API load balancer to use an SSL certificate provisioned by AWS Certificate Manager.

## Configure DNS

Decide on a subdomain that you want to dedicate to Cortex APIs. For example if your domain is `example.com`, a valid subdomain can be `api.example.com`. This guide will use `cortexlabs.dev` as the example domain and `api.cortexlabs.dev` as the subdomain.

We will set up a hosted zone on Route 53 to manage the DNS records for the subdomain. Go to the [Route 53 console](https://console.aws.amazon.com/route53/home) and click "Hosted Zones".

![](https://user-images.githubusercontent.com/4365343/82210754-a6b07d00-98dd-11ea-9cec-9f6b07282aa8.png)

Click "Create Hosted Zone" and then enter your subdomain as the domain name for your hosted zone and click "Create".

![](https://user-images.githubusercontent.com/4365343/82211091-4968fb80-98de-11ea-8ec4-8d26d1aea77a.png)

Take note of the values in the NS record.

![](https://user-images.githubusercontent.com/4365343/82211656-386cba00-98df-11ea-8c86-4961082b5f49.png)

Navigate to your root DNS service provider (e.g. Google Domains, AWS Route 53, Go Daddy). Your root DNS service provider is typically the registrar where you purchased your domain (unless you have transferred DNS management elsewhere). The procedure for adding DNS records may vary based on your service provider.

We are going to add an NS (name server) record that specifies that any traffic to your subdomain should use the name servers of your hosted zone in Route 53 for DNS resolution.

`cortexlabs.dev` is managed by Google Domains. The image below is a screenshot for adding a DNS record in Google Domains (your UI may differ based on your DNS service provider).

![](https://user-images.githubusercontent.com/4365343/82211959-bcbf3d00-98df-11ea-834d-692b3bcf9332.png)

## Generate an SSL certificate

You can skip this section (and continue to [add the DNS record](#add-dns-record)) if you don't need an SSL certificate for your custom domain. If you don't use an SSL certificate, you will need to skip certificate verification when making HTTPS requests to your APIs (e.g. `curl -k https://***`), or make HTTP requests instead (e.g. `curl http://***`).

To create an SSL certificate, go to the [ACM console](https://us-west-2.console.aws.amazon.com/acm/home) and click "Get Started" under the "Provision certificates" section.

![](https://user-images.githubusercontent.com/4365343/82202340-c04ac800-98cf-11ea-9472-89dd6d67eb0d.png)

Select "Request a public certificate" and then "Request a certificate".

![](https://user-images.githubusercontent.com/4365343/82202654-3e0ed380-98d0-11ea-8c57-025f0b69c54f.png)

Enter your subdomain and then click "Next".

![](https://user-images.githubusercontent.com/4365343/82224652-1cbedf00-98f2-11ea-912b-466cee2f6e25.png)

Select "DNS validation" and then click "Next".

![](https://user-images.githubusercontent.com/4365343/82205311-66003600-98d4-11ea-90e3-da7e8b0b2b9c.png)

Add tags for searchability (optional) then click "Review".

![](https://user-images.githubusercontent.com/4365343/82206485-52ee6580-98d6-11ea-95a9-1d0ebafc178a.png)

Click "Confirm and request".

![](https://user-images.githubusercontent.com/4365343/82206602-84ffc780-98d6-11ea-9f2f-ce383404ec67.png)

Click "Create record in Route 53". A popup will appear indicating that a Record is going to be added to Route 53. Click "Create" to automatically add the DNS record to your subdomain's hosted zone. Then click "Continue".

![](https://user-images.githubusercontent.com/4365343/82223539-c8ffc600-98f0-11ea-93a2-044aa0c9670d.png)

Wait for the Certificate Status to be "issued". This might take a few minutes.

![](https://user-images.githubusercontent.com/4365343/82209663-a616e700-98db-11ea-95cb-c6efedadb942.png)

Take note of the certificate's ARN. The certificate is ineligible for renewal because it is currently not being used. It will be eligible for renewal once it's used in Cortex.

![](https://user-images.githubusercontent.com/4365343/82222684-9e613d80-98ef-11ea-98c0-5a20b457f062.png)

Add the following field to your cluster configuration:

```yaml
# cluster.yaml

...

ssl_certificate_arn: <ARN of your certificate>
```

Create a Cortex cluster:

```bash
$ cortex cluster up --config cluster.yaml
```

## Add DNS record

Navigate to your [EC2 Load Balancer console](https://us-west-2.console.aws.amazon.com/ec2/v2/home#LoadBalancers:sort=loadBalancerName) and locate the Cortex API load balancer. You can determine which is the API load balancer by inspecting the `kubernetes.io/service-name` tag.

Take note of the load balancer's name.

![](https://user-images.githubusercontent.com/808475/80142777-961c1980-8560-11ea-9202-40964dbff5e9.png)

Go back to the [Route 53 console](https://console.aws.amazon.com/route53/home#hosted-zones:) and select the hosted zone you created earlier. Click "Create Record Set", and add an Alias record that routes traffic to your Cortex cluster's API load balancer (leave "Name" blank).

![](https://user-images.githubusercontent.com/808475/84083422-6ac97e80-a996-11ea-9679-be37268a2133.png)

## Use your new endpoint

Wait a few minutes to allow the DNS changes to propagate. You may now use your subdomain in place of your API load balancer endpoint in your client. For example, this curl request:

```bash
curl http://a5044e34a352d44b0945adcd455c7fa3-32fa161d3e5bcbf9.elb.us-west-2.amazonaws.com/text-generator -X POST -H "Content-Type: application/json" -d @sample.json
```

Would become:

```bash
# add the `-k` flag or use http:// instead of https:// if you didn't configure an SSL certificate
curl https://api.cortexlabs.dev/text-generator -X POST -H "Content-Type: application/json" -d @sample.json
```

## Debugging connectivity issues

You could run into connectivity issues if you make a request to your API without waiting long enough for your DNS records to propagate after creating them (it usually takes 5-10 mintues). If you are updating existing DNS records, it could take anywhere from a few minutes to 48 hours for the DNS cache to expire (until then, your previous DNS configuration will be used).

To test connectivity, try the following steps:

1. Deploy any api (e.g. examples/pytorch/iris-classifier).
2. Make a GET request to the your api (e.g. `curl https://api.cortexlabs.dev/iris-classifier` or paste the url into your browser).
3. If you run into an error such as `curl: (6) Could not resolve host: api.cortexlabs.dev` wait a few minutes and make the GET request from another device that hasn't made a request to that url in a while. A successful request looks like this:

```
{"message":"make a prediction by sending a post request to this endpoint with a json payload",...}
```

## Cleanup

Spin down your Cortex cluster.

Delete the hosted zone for your subdomain in the [Route 53 console](https://console.aws.amazon.com/route53/home#hosted-zones:):

![](https://user-images.githubusercontent.com/4365343/82228729-81306d00-98f7-11ea-8570-e9de15f5267f.png)

If you created an SSL certificate, delete it from the [ACM console](https://us-west-2.console.aws.amazon.com/acm/home):

![](https://user-images.githubusercontent.com/4365343/82228835-a624e000-98f7-11ea-92e2-cb4fb0f591e2.png)


# HTTPS (via API Gateway)

If you would like to support HTTPS endpoints for your Cortex APIs, here are a few options:

* Custom domain with an SSL certificate: See [here](https://docs.cortexlabs.com/clusters/cortex-cloud-on-aws/index/custom-domain) for instructions.
* AWS API Gateway: This is the simplest approach if a custom domain is not required; continue reading this guide for instructions.

Please note that one limitation of API Gateway is that there is a 30-second time limit for all requests.

If your API load balancer is internet-facing (which is the default, or you set `api_load_balancer_scheme: internet-facing` in your cluster configuration file before creating your cluster), use the [first section](#internet-facing-load-balancer) of this guide.

If your API load balancer is internal (i.e. you set `api_load_balancer_scheme: internal` in your cluster configuration file before creating your cluster), use the [second section](#internal-load-balancer) of this guide.

## Internet-facing load balancer

*This section applies if your API load balancer is internet-facing (which is the default, or you set `api_load_balancer_scheme: internet-facing` in your cluster configuration file before creating your cluster). If your API load balancer is internal, see the* [*internal load balancer*](#internal-load-balancer) *section below.*

### Create an API Gateway

Go to the [API Gateway console](https://console.aws.amazon.com/apigateway/home), select "REST API" under "Choose an API type", and click "Build".

![](https://user-images.githubusercontent.com/808475/78293216-18269e80-74dd-11ea-9e68-86922c2cbc7c.png)

Select "REST" and "New API", name your API (e.g. "cortex"), select either "Regional" or "Edge optimized" (depending on your preference), and click "Create API".

![](https://user-images.githubusercontent.com/808475/78293434-66d43880-74dd-11ea-92d6-692158171a3f.png)

Select "Actions" > "Create Resource":

![](https://user-images.githubusercontent.com/808475/80154502-8b6b7f80-8574-11ea-9c78-7d9f277bf55b.png)

Select "Configure as proxy resource" and "Enable API Gateway CORS", and click "Create Resource"

![](https://user-images.githubusercontent.com/808475/80154565-ad650200-8574-11ea-8753-808cd35902e2.png)

Select "HTTP Proxy" and set "Endpoint URL" to "http\:///{proxy}". You can get your API load balancer endpoint via `cortex cluster info`; make sure to prepend `http://` and append `/{proxy}`. For example, mine is: `http://a9eaf69fd125947abb1065f62de59047-81cdebc0275f7d96.elb.us-west-2.amazonaws.com/{proxy}`.

Leave "Content Handling" set to "Passthrough" and Click "Save".

![](https://user-images.githubusercontent.com/808475/80154735-13ea2000-8575-11ea-83ca-58f182df83c6.png)

Select "Actions" > "Deploy API"

![](https://user-images.githubusercontent.com/808475/80154802-2c5a3a80-8575-11ea-9ab3-de89885fd658.png)

Create a new stage (e.g. "dev") and click "Deploy"

![](https://user-images.githubusercontent.com/808475/80154859-4431be80-8575-11ea-9305-50384b1f9847.png)

Copy your "Invoke URL"

![](https://user-images.githubusercontent.com/808475/80154911-5dd30600-8575-11ea-9682-1a7328783011.png)

### Use your new endpoint

You may now use the "Invoke URL" in place of your API load balancer endpoint in your client. For example, this curl request:

```bash
curl http://a9eaf69fd125947abb1065f62de59047-81cdebc0275f7d96.elb.us-west-2.amazonaws.com/iris-classifier -X POST -H "Content-Type: application/json" -d @sample.json
```

Would become:

```bash
curl https://31qjv48rs6.execute-api.us-west-2.amazonaws.com/dev/iris-classifier -X POST -H "Content-Type: application/json" -d @sample.json
```

### Cleanup

Delete the API Gateway before spinning down your Cortex cluster:

![](https://user-images.githubusercontent.com/808475/80155073-bdc9ac80-8575-11ea-99a1-95c0579da79e.png)

## Internal load balancer

*This section applies if your API load balancer is internal (i.e. you set `api_load_balancer_scheme: internal` in your cluster configuration file before creating your cluster). If your API load balancer is internet-facing, see the* [*internet-facing load balancer*](#internet-facing-load-balancer) *section above.*

### Create a VPC Link

Navigate to AWS's EC2 Load Balancer dashboard and locate the Cortex API load balancer. You can determine which is the API load balancer by inspecting the `kubernetes.io/service-name` tag:

![](https://user-images.githubusercontent.com/808475/80142777-961c1980-8560-11ea-9202-40964dbff5e9.png)

Take note of the load balancer's name.

Go to the [API Gateway console](https://console.aws.amazon.com/apigateway/home), click "VPC Links" on the left sidebar, and click "Create"

![](https://user-images.githubusercontent.com/808475/80142466-0c6c4c00-8560-11ea-8293-eb5e5572b797.png)

Select "VPC link for REST APIs", name your VPC link (e.g. "cortex"), select the API load balancer, and click "Create".

![](https://user-images.githubusercontent.com/808475/80143027-03c84580-8561-11ea-92de-9ed0a5dfa593.png)

Wait for the VPC link to be created (it will take a few minutes)

![](https://user-images.githubusercontent.com/808475/80144088-bbaa2280-8562-11ea-901b-8520eb253df7.png)

### Create an API Gateway

Go to the [API Gateway console](https://console.aws.amazon.com/apigateway/home), select "REST API" under "Choose an API type", and click "Build"

![](https://user-images.githubusercontent.com/808475/78293216-18269e80-74dd-11ea-9e68-86922c2cbc7c.png)

Select "REST" and "New API", name your API (e.g. "cortex"), select either "Regional" or "Edge optimized" (depending on your preference), and click "Create API"

![](https://user-images.githubusercontent.com/808475/78293434-66d43880-74dd-11ea-92d6-692158171a3f.png)

Select "Actions" > "Create Resource"

![](https://user-images.githubusercontent.com/808475/80141938-3cffb600-855f-11ea-9c1c-132ca4503b7a.png)

Select "Configure as proxy resource" and "Enable API Gateway CORS", and click "Create Resource"

![](https://user-images.githubusercontent.com/808475/80142124-80f2bb00-855f-11ea-8e4e-9413146e0815.png)

Select "VPC Link", select "Use Proxy Integration", choose your newly-created VPC Link, and set "Endpoint URL" to "http\:///{proxy}". You can get your API load balancer endpoint via `cortex cluster info`; make sure to prepend `http://` and append `/{proxy}`. For example, mine is: `http://a5044e34a352d44b0945adcd455c7fa3-32fa161d3e5bcbf9.elb.us-west-2.amazonaws.com/{proxy}`. Click "Save"

![](https://user-images.githubusercontent.com/808475/80147407-4f322200-8568-11ea-8ef5-df5164c1375f.png)

Select "Actions" > "Deploy API"

![](https://user-images.githubusercontent.com/808475/80147555-86083800-8568-11ea-86af-1b1e38c9d322.png)

Create a new stage (e.g. "dev") and click "Deploy"

![](https://user-images.githubusercontent.com/808475/80147631-a7692400-8568-11ea-8a09-13dbd50b17b9.png)

Copy your "Invoke URL"

![](https://user-images.githubusercontent.com/808475/80147716-c798e300-8568-11ea-9aef-7dd6fdf4a68a.png)

### Use your new endpoint

You may now use the "Invoke URL" in place of your API load balancer endpoint in your client. For example, this curl request:

```bash
curl http://a5044e34a352d44b0945adcd455c7fa3-32fa161d3e5bcbf9.elb.us-west-2.amazonaws.com/iris-classifier -X POST -H "Content-Type: application/json" -d @sample.json
```

Would become:

```bash
curl https://lrivodooqh.execute-api.us-west-2.amazonaws.com/dev/iris-classifier -X POST -H "Content-Type: application/json" -d @sample.json
```

### Cleanup

Delete the API Gateway and VPC Link before spinning down your Cortex cluster:

![](https://user-images.githubusercontent.com/808475/80149163-05970680-856b-11ea-9f82-61f4061a3321.png)

![](https://user-images.githubusercontent.com/808475/80149204-1ba4c700-856b-11ea-83f7-9741c78b6b95.png)


# VPC peering

If you are using an internal operator load balancer (i.e. you set `operator_load_balancer_scheme: internal` in your cluster configuration file before creating your cluster), you can use VPC Peering to enable your Cortex CLI to connect to your cluster operator from another VPC so that you may run `cortex` commands.

If you are using an internal API load balancer (i.e. you set `api_load_balancer_scheme: internal` in your cluster configuration file before creating your cluster), you can use VPC Peering to make prediction requests from another VPC.

This guide illustrates how to create a VPC Peering connection between a VPC of your choice and the Cortex load balancers.

## Gather Cortex's VPC information

Navigate to AWS's EC2 Load Balancer dashboard and locate the Cortex operator's load balancer. You can determine which is the operator load balancer by inspecting the `kubernetes.io/service-name` tag:

![](https://user-images.githubusercontent.com/808475/80126132-804e2a80-8547-11ea-8ce4-57d3fd96e2c4.png)

Click back to the "Description" tab and note the VPC ID of the load balancer and the ID of each of the subnets associated with the load balancer:

![](https://user-images.githubusercontent.com/808475/80127144-c2c43700-8548-11ea-95b4-ce9d1df024cc.png)

Navigate to AWS's VPC dashboard and identify the ID and CIDR block of Cortex's VPC:

![](https://user-images.githubusercontent.com/808475/80125554-af17d100-8546-11ea-96ec-00e2aaee7100.png)

The VPC ID here should match that of the load balancer.

## Create peering connection

Identify the ID and CIDR block of the VPC from which you'd like to connect to the Cortex VPC.

In my case, I have a VPC in the same AWS account and region, and I can locate its ID and CIDR block from AWS's VPC dashboard:

![](https://user-images.githubusercontent.com/808475/80125729-eb4b3180-8546-11ea-8d20-6bc2478747ae.png)

From AWS's VPC dashboard, navigate to the "Peering Connections" page, and click "Create Peering Connection":

![](https://user-images.githubusercontent.com/808475/80127600-67df0f80-8549-11ea-9e10-765a6e273b54.png)

Name your new VPC Peering Connection (I used "cortex-operator", but "cortex" or "cortex-api" may make more sense depending on your use case). Then configure the connection such that the "Requester" is the VPC from which you'll connect to the Cortex VPC, and the "Accepter" is Cortex's VPC.

![](https://user-images.githubusercontent.com/808475/80131545-3f5a1400-854f-11ea-9ca0-c51433d3fa3d.png)

Click "Create Peering Connection", navigate back to the Peering Connections dashboard, select the newly created peering connection, and click "Actions" > "Accept Request":

![](https://user-images.githubusercontent.com/808475/80132168-21d97a00-8550-11ea-8c22-79c65710d369.png)

![](https://user-images.githubusercontent.com/808475/80132179-26059780-8550-11ea-80fc-6670fcab7026.png)

## Update route tables

Navigate to the VPC Route Tables page. Select the route table for the VPC from which you'd like to connect to the Cortex cluster (in my case, I just have one route table for this VPC). Select the "Routes" tab, and click "Edit routes":

![](https://user-images.githubusercontent.com/808475/80135180-b940cc00-8554-11ea-8162-c7409090897b.png)

Add a route where the "Destination" is the CIDR block for Cortex's VPC, and the "Target" is the newly-created Peering Connection:

![](https://user-images.githubusercontent.com/808475/80137033-78968200-8557-11ea-9d84-9221b772f0fc.png)

Do not create new route tables or change subnet associations.

Navigate back to the VPC Route Tables page. There will be a route table for each of the subnets associated with the Cortex operator load balancer:

![](https://user-images.githubusercontent.com/808475/80138244-5dc50d00-8559-11ea-9248-fc201d011530.png)

For each of these route tables, click "Edit routes" and add a new route where the "Destination" is the CIDR block for the VPC from which you will be connecting to the Cortex cluster, and the "Target" is the newly-created Peering Connection:

![](https://user-images.githubusercontent.com/808475/80138653-f78cba00-8559-11ea-8444-406e218c3bab.png)

Repeat adding this route for each route table associated with the Cortex operator's subnets; in my case there were three. Do not create new route tables or change subnet associations.

You should now be able to use the Cortex CLI and make prediction requests from your VPC.

## Cleanup

Delete the VPC Peering connection before spinning down your Cortex cluster:

![](https://user-images.githubusercontent.com/808475/80138851-57836080-855a-11ea-92f1-06d501932a41.png)


# Setting up kubectl

## Install kubectl

Follow these [instructions](https://kubernetes.io/docs/tasks/tools/install-kubectl).

## Install the AWS CLI

Follow these [instructions](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-install.html).

## Configure the AWS CLI

```bash
aws --version  # should be >= 1.16

aws configure
```

## Update kubeconfig

```bash
aws eks update-kubeconfig --name=<cluster_name> --region=<region>
```

## Test kubectl

```bash
kubectl get pods
```


# Uninstall

```bash
cortex cluster down
```

## Delete metadata and log groups

Since you may wish to have access to your data after spinning down your cluster, Cortex's bucket, log groups, and Prometheus volume are not automatically deleted when running `cortex cluster down`.

To delete them:

```bash
# set AWS credentials
export AWS_ACCESS_KEY_ID=***
export AWS_SECRET_ACCESS_KEY=***

# identify the name of your cortex S3 bucket
aws s3 ls

# delete the S3 bucket
aws s3 rb --force s3://<bucket>

# delete the log group (replace <cluster_name> with the name of your cluster, default: cortex)
aws logs describe-log-groups --log-group-name-prefix=<cluster_name> --query logGroups[*].[logGroupName] --output text | xargs -I {} aws logs delete-log-group --log-group-name {}
```

To delete the Prometheus volume, navigate to the [EC2 volumes page](https://console.aws.amazon.com/ec2/v2/home?#Volumes) in the AWS console (be sure to set the appropriate region), select the volume, and click "Actions" and then "Delete Volume". A Prometheus volume that Cortex created has a name that starts with `kubernetes-dynamic-pvc`, the `kubernetes.io/cluster/<cluster name>` tag is set to `owned`, and the `kubernetes.io/created-for/pvc/name` tag starts with `prometheus-`.

If you've configured a custom domain for your APIs, you can remove the SSL Certificate and Hosted Zone for the domain by following these [instructions](https://docs.cortexlabs.com/clusters/index/custom-domain#cleanup).

## Troubleshooting

On rare occasions, `cortex cluster down` may not be able to spin down your Cortex cluster. When this happens, follow these steps:

1. If you've manually created any AWS networking resources that are pointed to the cluster or its VPC (e.g. API Gateway VPC links, custom domains, etc), delete them from the AWS console.
2. Replace "" and "" in the following URL, and open it in your browser: `https://console.aws.amazon.com/cloudformation/home?region=<region>#/stacks?filteringText=eksctl-<cluster_name>-`

   ![image](https://user-images.githubusercontent.com/808475/97790394-963b4880-1b85-11eb-8e27-ba5a551606b3.png)
3. For each CloudFormation stack which contains the word "nodegroup", select the stack and click "Delete".
4. Select the final stack (the one that ends in "-cluster") and click "Delete".

   If deleting the stack fails, navigate to the EC2 dashboard in the AWS console, delete the load balancers that are associated with the cluster, and try again (you can determine which load balancers are associated with the cluster by setting the correct region in the console and checking the `cortex.dev/cluster-name` tag on all load balancers). If the problem still persists, delete any other AWS resources that are blocking the stack deletion and try again.
5. In rare cases, you may need to delete other AWS resources associated with your Cortex cluster. For each the following resources, go to the appropriate AWS Dashboard (in the region that your cluster was in), and confirm that there are no resources left behind by the cluster: CloudWatch Dashboard, SQS Queues, S3 Bucket, and CloudWatch LogGroups (the Cortex bucket and log groups are not deleted by `cluster down` in order to preserve your data).


# Cortex Cloud on GCP


# Install

## Prerequisites

1. [Docker](https://docs.docker.com/install) must be installed and running on your machine (to verify, check that running `docker ps` does not return an error)
2. You may need to [request a quota increase](https://cloud.google.com/compute/quotas) for your desired instance type and/or GPU type
3. Export the `GOOGLE_APPLICATION_CREDENTIALS` environment variable, containing the path to your GCP credentials file (e.g. `export GOOGLE_APPLICATION_CREDENTIALS=~/.config/gcloud/myproject-8a41417a968a.json`)
4. If you haven't done so already, enable the Kubernetes Engine API in your GCP project ([here](https://console.developers.google.com/apis/api/container.googleapis.com/overview))

## Spin up Cortex on your GCP account

```bash
# install the CLI
pip install cortex

# spin up Cortex on your GCP account
cortex cluster-gcp up  # or: cortex cluster-gcp up --config cluster.yaml (see configuration options below)
```

## Configure Cortex

```yaml
# cluster.yaml

# GKE cluster name
cluster_name: cortex

# GCP project ID
project: <your GCP project ID>

# GCP zone for your cluster
zone: us-central1-a

# instance type
instance_type: n1-standard-2

# minimum number of instances
min_instances: 1

# maximum number of instances
max_instances: 5

# enable the use of preemptible instances
preemptible: false

# enable the use of on-demand backup instances which will be used when preemptible capacity runs out
# default is true when preemptible instances are used
# on_demand_backup: true

# GPU to attach to your instance (optional)
# accelerator_type: nvidia-tesla-t4

# the number of GPUs to attach to each instance (optional)
# accelerators_per_instance: 1

# the name of the network in which to create your cluster
# network: default

# the name of the subnetwork in which to create your cluster
# subnet: default

# API load balancer scheme [internet-facing | internal]
api_load_balancer_scheme: internet-facing

# operator load balancer scheme [internet-facing | internal]
# note: if using "internal", you must be within the cluster's VPC or configure VPC Peering to connect your CLI to your cluster operator
operator_load_balancer_scheme: internet-facing
```

The docker images used by the Cortex cluster can also be overridden, although this is not common. They can be configured by adding any of these keys to your cluster configuration file (default values are shown):

```yaml
image_operator: quay.io/cortexlabs/operator:0.28.0
image_manager: quay.io/cortexlabs/manager:0.28.0
image_downloader: quay.io/cortexlabs/downloader:0.28.0
image_istio_proxy: quay.io/cortexlabs/istio-proxy:0.28.0
image_istio_pilot: quay.io/cortexlabs/istio-pilot:0.28.0
image_google_pause: quay.io/cortexlabs/google-pause:0.28.0
image_prometheus: quay.io/cortexlabs/prometheus:0.28.0
image_prometheus_config_reloader: quay.io/cortexlabs/prometheus-config-reloader:0.28.0
image_prometheus_operator: quay.io/cortexlabs/prometheus-operator:0.28.0
image_prometheus_statsd_exporter: quay.io/cortexlabs/prometheus-statsd-exporter:0.28.0
image_prometheus_stackdriver_sidecar: quay.io/cortexlabs/prometheus-stackdriver-sidecar:0.28.0
```


# Logging

By default, logs will be pushed to [StackDriver](https://console.cloud.google.com/logs/query) using fluent-bit. API logs are tagged with labels to help with log aggregation and filtering. Below are some sample Stackdriver queries:

RealtimeAPI:

```
resource.type="k8s_container"
resource.labels.cluster_name="<INSERT CLUSTER NAME>"
jsonPayload.labels.apiKind="RealtimeAPI"
jsonPayload.labels.apiName="<INSERT API NAME>"
```

TaskAPI:

```
resource.type="k8s_container"
resource.labels.cluster_name="<INSERT CLUSTER NAME>"
jsonPayload.labels.apiKind="TaskAPI"
jsonPayload.labels.apiName="<INSERT API NAME>"
jsonPayload.labels.jobID="<INSERT JOB ID>"
```

Please make sure to navigate to the project containing your cluster and adjust the time range accordingly before running queries.

## Structured logging

You can use Cortex's logger in your Python code to log in JSON, which will enrich your logs with Cortex's metadata, and enable you to add custom metadata to the logs. See the structured logging docs for [Realtime](https://docs.cortexlabs.com/workloads/realtime-apis/predictors#structured-logging) and [Task](https://docs.cortexlabs.com/workloads/task-apis/definitions#structured-logging) APIs.


# Credentials

1. Create a service account for your GCP project as described [here](https://cloud.google.com/iam/docs/creating-managing-service-accounts#iam-service-accounts-create-console) with the following roles (these roles could be more restrictive if required):
   1. `Editor` role.
   2. `Kubernetes Engine Admin` role.
   3. `Container Registry Service Agent` role.
   4. `Storage Admin` role.
   5. `Storage Object Admin` role.
2. Generate a service account key for your service account as described [here](https://cloud.google.com/iam/docs/creating-managing-service-account-keys) and export it as a JSON file.
3. Export the `GOOGLE_APPLICATION_CREDENTIALS` variable and point it to the downloaded service account key from the previous step. For example: `export GOOGLE_APPLICATION_CREDENTIALS=/home/ubuntu/.config/gcloud/sample-269400-9a41792a969b.json`


# Setting up kubectl

## Install kubectl

Follow these [instructions](https://kubernetes.io/docs/tasks/tools/install-kubectl).

## Install gcloud

Follow these [instructions](https://cloud.google.com/sdk/docs/install).

## Update kubeconfig

```bash
gcloud container clusters get-credentials <cluster_name> --zone <zone> --project <project_id>
```

## Test kubectl

```bash
kubectl get pods
```


# Uninstall

```bash
cortex cluster-gcp down
```

The `cortex cluster-gcp down` command doesn't wait for the cluster to spin down. You can ensure that the cluster has spun down by checking the GKE console.

## Delete Prometheus Volume

The volume used by Cortex's Prometheus instance is not deleted by default, as it might contain important information. If this volume is not required anymore, you can delete it in the GCP console. Navigate to the [Disks](https://console.cloud.google.com/compute/disks) page (be sure to set the appropriate project), select the volume, and click "Delete". A Prometheus volume that Cortex created has a name that starts with `gke-<cluster name>-`, and the `kubernetes.io/created-for/pvc/name` tag starts with `prometheus-`.


# Cortex Core on Kubernetes


# Install

Cortex currently relies on cloud provider specific functionality such as load balancers and storage. Kubernetes clusters in the following cloud providers are supported:

* [AWS](#aws)
* [GCP](#gcp)

Cortex uses helm to install the Cortex operator and its dependencies on your Kubernetes cluster.

## AWS

### Prerequisites

* kubectl
* aws cli
* helm 3
* EKS cluster
  * at least 3 t3.medium (2 vCPU, 4 GB mem) instances

You may install Cortex in any namespace in your cluster. In the guide that follows, the "default" namespace is assumed; if you're using a different namespace, replace all occurrences of "default" with the name of your namespace.

Note that installing Cortex on your Kubernetes cluster will not provide some of the cluster-level features such as cluster autoscaling and spot instances with on-demand backup.

### Download Cortex charts

```bash
wget https://s3-us-west-2.amazonaws.com/get-cortex/0.28.0/charts/cortex-0.28.0.tar.gz
tar -xzf cortex-0.28.0.tar.gz
```

### Create a bucket in S3

The Cortex operator will use this bucket to store API state and dependencies.

```yaml
aws s3api create-bucket --bucket <CORTEX_S3_BUCKET> --region <CORTEX_REGION>
```

### Credentials

The credentials need to have at least these [permissions](https://docs.cortexlabs.com/cortex-cloud-on-aws/security#operator).

```yaml
export CORTEX_AWS_ACCESS_KEY_ID=<AWS_ACCESS_KEY_ID>
export CORTEX_AWS_SECRET_ACCESS_KEY=<AWS_SECRET_ACCESS_KEY>

kubectl --namespace default create secret generic 'aws-credentials' \
    --from-literal='AWS_ACCESS_KEY_ID'=$CORTEX_AWS_ACCESS_KEY_ID \
    --from-literal='AWS_SECRET_ACCESS_KEY'=$CORTEX_AWS_SECRET_ACCESS_KEY \
    -o yaml --dry-run=client | kubectl apply -f - >/dev/null
```

### Install Cortex

Define a `values.yaml` with the following information provided:

```yaml
# values.yaml

cortex:
  region: <CORTEX_REGION>
  bucket: <CORTEX_S3_BUCKET>  # e.g. "my-cortex-bucket" (without s3://)
  cluster_name: <CORTEX_CLUSTER_NAME>
global:
  provider: "aws"
```

```bash
helm install cortex charts/ --namespace default -f values.yaml
```

### Configure Cortex client

Wait for the loadbalancers to be provisioned and connected to your cluster.

Get the Cortex operator endpoint:

```bash
kubectl get service --namespace default ingressgateway-operator -o jsonpath='{.status.loadBalancer.ingress[0].hostname}'
```

You can use the curl command below to verify that your load balancer is ready. It can take 5-10 minutes for the setup to complete. You can expect to encounter `Could not resolve host` or timeouts when running the verification request before the load balancer is initialized.

```bash
export CORTEX_OPERATOR_ENDPOINT=$(kubectl get service --namespace default ingressgateway-operator -o jsonpath='{.status.loadBalancer.ingress[0].hostname}')

curl http://$CORTEX_OPERATOR_ENDPOINT/verifycortex --max-time 5
```

A successful response looks like this:

```bash
{"provider":"aws"}
```

Once you receive a successful response, configure your Cortex client:

```bash
cortex env configure --operator-endpoint $CORTEX_OPERATOR_ENDPOINT
```

### Using GPU/Inf resources on your cluster

The following tolerations are added to Deployments and Jobs orchestrated by Cortex.

```yaml
  - effect: NoSchedule
    key: nvidia.com/gpu
    operator: Exists
  - effect: NoSchedule
    key: aws.amazon.com/neuron
    operator: Equal
    value: "true"
```

## GCP

### Prerequisites

* kubectl
* gsutil
* helm 3
* GKE cluster
  * at least 2 n1-standard-2 (2 vCPU, 8 GB mem) (with monitoring and logging disabled)

You may install Cortex in any namespace in your cluster. In the guide that follows, the "default" namespace is assumed; if you're using a different namespace, replace all occurrences of "default" with the name of your namespace.

Note that installing Cortex on your Kubernetes cluster will not provide some of the cluster-level features such as cluster autoscaling and preemptible instances.

### Download Cortex charts

```bash
wget https://s3-us-west-2.amazonaws.com/get-cortex/0.28.0/charts/cortex-0.28.0.tar.gz
tar -xzf cortex-0.28.0.tar.gz
```

### Create a bucket in GCS

The Cortex operator will use this bucket to store API state and dependencies.

```yaml
gsutil mb gs://CORTEX_GCS_BUCKET
```

### Credentials

The credentials need to have at least these [permissions](https://docs.cortexlabs.com/clusters/cortex-cloud-on-gcp/credentials).

```yaml
export CORTEX_GOOGLE_APPLICATION_CREDENTIALS=<PATH_TO_CREDENTIALS>

kubectl create secret generic 'gcp-credentials' --namespace default --from-file=key.json=$CORTEX_GOOGLE_APPLICATION_CREDENTIALS
```

### Install Cortex

Define a `values.yaml` with the following information provided:

```yaml
# values.yaml

cortex:
  project: <CORTEX_PROJECT>
  zone: <CORTEX_ZONE>
  bucket: <CORTEX_GCS_BUCKET>  # e.g. "my-cortex-bucket" (without gs://)
  cluster_name: <CORTEX_CLUSTER_NAME>
global:
  provider: "gcp"
```

```bash
helm install cortex charts/ --namespace default -f values.yaml
```

### Configure Cortex client

Wait for the loadbalancers to be provisioned and connected to your cluster.

Get the Cortex operator endpoint:

```bash
kubectl get service --namespace default ingressgateway-operator -o jsonpath='{.status.loadBalancer.ingress[0].ip}'
```

You can use the curl command below to verify that your load balancer is ready. It can take 5-10 minutes for the setup to complete. You can expect to encounter `Could not resolve host` or timeouts when running the verification request before the load balancer is initialized.

```bash
export CORTEX_OPERATOR_ENDPOINT=$(kubectl get service --namespace default ingressgateway-operator -o jsonpath='{.status.loadBalancer.ingress[0].ip}')

curl http://$CORTEX_OPERATOR_ENDPOINT/verifycortex --max-time 5
```

A successful response looks like this:

```bash
{"provider":"gcp"}
```

Once you receive a successful response, configure your Cortex client:

```bash
cortex env configure --operator-endpoint $CORTEX_OPERATOR_ENDPOINT
```

### Using GPU resources on your cluster

The following tolerations are added to Deployments and Jobs orchestrated by Cortex.

```yaml
  - effect: NoSchedule
    key: nvidia.com/gpu
    operator: Exists
```


# Uninstall

Identify the Cortex installation's release name:

```bash
helm list
```

Uninstall Cortex:

```bash
helm uninstall <RELEASE_NAME>
```

Resources in your cloud such as the bucket and logs will not be deleted.


# Private Docker registry

## Install and configure kubectl

Follow the instructions for [AWS](https://docs.cortexlabs.com/clusters/cortex-cloud-on-aws/kubectl) or [GCP](https://docs.cortexlabs.com/clusters/cortex-cloud-on-gcp/kubectl).

## Setting credentials

```bash
$ DOCKER_USERNAME=***
$ DOCKER_PASSWORD=***

$ kubectl create secret docker-registry registry-credentials \
    --namespace default \
    --docker-username=$DOCKER_USERNAME \
    --docker-password=$DOCKER_PASSWORD

$ kubectl patch serviceaccount default --namespace default \
    -p "{\"imagePullSecrets\": [{\"name\": \"registry-credentials\"}]}"
```

## Deleting credentials

```bash
$ kubectl delete secret --namespace default registry-credentials

$ kubectl patch serviceaccount default --namespace default \
    -p "{\"imagePullSecrets\": []}"
```


# Get started

## Install the CLI

```bash
$ pip install cortex
```

See [here](https://docs.cortexlabs.com/clients/install) for alternative installation options.

## Create a cluster

* [Launch a Cortex cluster on your AWS account](https://docs.cortexlabs.com/clusters/cortex-cloud-on-aws/install)
* [Launch a Cortex cluster on your GCP account](https://docs.cortexlabs.com/clusters/cortex-cloud-on-gcp/install)
* [Install Cortex on your Kubernetes cluster](https://docs.cortexlabs.com/clusters/cortex-core-on-kubernetes/install)

## Run inference workloads

* [Realtime API](https://docs.cortexlabs.com/workloads/realtime-apis/example)
* [Batch API](https://docs.cortexlabs.com/workloads/batch-apis/example)
* [Task API](https://docs.cortexlabs.com/workloads/task-apis/example)


# Install

## Install with pip

To install the latest version:

```bash
pip install cortex
```

To install or upgrade to a specific version (e.g. v0.29.0):

```bash
pip install cortex==0.29.0
```

To upgrade to the latest version:

```bash
pip install --upgrade cortex
```

## Install without the Python client

```bash
# For example to download CLI version 0.29.0 (Note the "v"):
$ bash -c "$(curl -sS https://raw.githubusercontent.com/cortexlabs/cortex/v0.29.0/get-cli.sh)"
```

By default, the Cortex CLI is installed at `/usr/local/bin/cortex`. To install the executable elsewhere, export the `CORTEX_INSTALL_PATH` environment variable to your desired location before running the command above.

## Changing the CLI/client configuration directory

By default, the Cortex CLI/client creates a directory at `~/.cortex/` and uses it to store environment configuration. To use a different directory, export the `CORTEX_CLI_CONFIG_DIR` environment variable before running any `cortex` commands.


# CLI commands

## deploy

```
create or update apis

Usage:
  cortex deploy [CONFIG_FILE] [flags]

Flags:
  -e, --env string      environment to use
  -f, --force           override the in-progress api update
  -y, --yes             skip prompts
  -o, --output string   output format: one of pretty|json (default "pretty")
  -h, --help            help for deploy
```

## get

```
get information about apis or jobs

Usage:
  cortex get [API_NAME] [JOB_ID] [flags]

Flags:
  -e, --env string      environment to use
  -w, --watch           re-run the command every 2 seconds
  -o, --output string   output format: one of pretty|json (default "pretty")
  -v, --verbose         show additional information (only applies to pretty output format)
  -h, --help            help for get
```

## logs

```
stream logs from a single replica of an api or a single worker for a job

Usage:
  cortex logs API_NAME [JOB_ID] [flags]

Flags:
  -e, --env string   environment to use
  -y, --yes          skip prompts
  -h, --help         help for logs
```

## patch

```
update API configuration for a deployed API

Usage:
  cortex patch [CONFIG_FILE] [flags]

Flags:
  -e, --env string      environment to use
  -f, --force           override the in-progress api update
  -o, --output string   output format: one of pretty|json (default "pretty")
  -h, --help            help for patch
```

## refresh

```
restart all replicas for an api (without downtime)

Usage:
  cortex refresh API_NAME [flags]

Flags:
  -e, --env string      environment to use
  -f, --force           override the in-progress api update
  -o, --output string   output format: one of pretty|json (default "pretty")
  -h, --help            help for refresh
```

## delete

```
delete any kind of api or stop a batch job

Usage:
  cortex delete API_NAME [JOB_ID] [flags]

Flags:
  -e, --env string      environment to use
  -f, --force           delete the api without confirmation
  -c, --keep-cache      keep cached data for the api
  -o, --output string   output format: one of pretty|json (default "pretty")
  -h, --help            help for delete
```

## cluster up

```
spin up a cluster on aws

Usage:
  cortex cluster up [flags]

Flags:
  -c, --config string               path to a cluster configuration file
      --aws-key string              aws access key id
      --aws-secret string           aws secret access key
      --cluster-aws-key string      aws access key id to be used by the cluster
      --cluster-aws-secret string   aws secret access key to be used by the cluster
  -e, --configure-env string        name of environment to configure (default "aws")
  -y, --yes                         skip prompts
  -h, --help                        help for up
```

## cluster info

```
get information about a cluster

Usage:
  cortex cluster info [flags]

Flags:
  -c, --config string          path to a cluster configuration file
  -n, --name string            name of the cluster
  -r, --region string          aws region of the cluster
      --aws-key string         aws access key id
      --aws-secret string      aws secret access key
  -e, --configure-env string   name of environment to configure
  -d, --debug                  save the current cluster state to a file
  -y, --yes                    skip prompts
  -h, --help                   help for info
```

## cluster configure

```
update a cluster's configuration

Usage:
  cortex cluster configure [flags]

Flags:
  -c, --config string               path to a cluster configuration file
      --aws-key string              aws access key id
      --aws-secret string           aws secret access key
      --cluster-aws-key string      aws access key id to be used by the cluster
      --cluster-aws-secret string   aws secret access key to be used by the cluster
  -e, --configure-env string        name of environment to configure
  -y, --yes                         skip prompts
  -h, --help                        help for configure
```

## cluster down

```
spin down a cluster

Usage:
  cortex cluster down [flags]

Flags:
  -c, --config string       path to a cluster configuration file
  -n, --name string         name of the cluster
  -r, --region string       aws region of the cluster
      --aws-key string      aws access key id
      --aws-secret string   aws secret access key
  -y, --yes                 skip prompts
  -h, --help                help for down
```

## cluster export

```
download the code and configuration for APIs

Usage:
  cortex cluster export [API_NAME] [API_ID] [flags]

Flags:
  -c, --config string       path to a cluster configuration file
  -n, --name string         name of the cluster
  -r, --region string       aws region of the cluster
      --aws-key string      aws access key id
      --aws-secret string   aws secret access key
  -h, --help                help for export
```

## cluster-gcp up

```
spin up a cluster on gcp

Usage:
  cortex cluster-gcp up [flags]

Flags:
  -c, --config string          path to a cluster configuration file
  -e, --configure-env string   name of environment to configure (default "gcp")
  -y, --yes                    skip prompts
  -h, --help                   help for up
```

## cluster-gcp info

```
get information about a cluster

Usage:
  cortex cluster-gcp info [flags]

Flags:
  -c, --config string          path to a cluster configuration file
  -n, --name string            name of the cluster
  -p, --project string         gcp project id
  -z, --zone string            gcp zone of the cluster
  -e, --configure-env string   name of environment to configure
  -d, --debug                  save the current cluster state to a file
  -y, --yes                    skip prompts
  -h, --help                   help for info
```

## cluster-gcp down

```
spin down a cluster

Usage:
  cortex cluster-gcp down [flags]

Flags:
  -c, --config string    path to a cluster configuration file
  -n, --name string      name of the cluster
  -p, --project string   gcp project id
  -z, --zone string      gcp zone of the cluster
  -y, --yes              skip prompts
  -h, --help             help for down
```

## env configure

```
configure an environment

Usage:
  cortex env configure [ENVIRONMENT_NAME] [flags]

Flags:
  -o, --operator-endpoint string   set the operator endpoint without prompting
  -h, --help                       help for configure
```

## env list

```
list all configured environments

Usage:
  cortex env list [flags]

Flags:
  -o, --output string   output format: one of pretty|json (default "pretty")
  -h, --help            help for list
```

## env default

```
set the default environment

Usage:
  cortex env default [ENVIRONMENT_NAME] [flags]

Flags:
  -h, --help   help for default
```

## env delete

```
delete an environment configuration

Usage:
  cortex env delete [ENVIRONMENT_NAME] [flags]

Flags:
  -h, --help   help for delete
```

## version

```
print the cli and cluster versions

Usage:
  cortex version [flags]

Flags:
  -e, --env string   environment to use
  -h, --help         help for version
```

## completion

```
generate shell completion scripts

to enable cortex shell completion:
    bash:
        add this to ~/.bash_profile (mac) or ~/.bashrc (linux):
            source <(cortex completion bash)

        note: bash-completion must be installed on your system; example installation instructions:
            mac:
                1) install bash completion:
                   brew install bash-completion
                2) add this to your ~/.bash_profile:
                   source $(brew --prefix)/etc/bash_completion
                3) log out and back in, or close your terminal window and reopen it
            ubuntu:
                1) install bash completion:
                   apt update && apt install -y bash-completion  # you may need sudo
                2) open ~/.bashrc and uncomment the bash completion section, or add this:
                   if [ -f /etc/bash_completion ] && ! shopt -oq posix; then . /etc/bash_completion; fi
                3) log out and back in, or close your terminal window and reopen it

    zsh:
        option 1:
            add this to ~/.zshrc:
                source <(cortex completion zsh)
            if that failed, you can try adding this line (above the source command you just added):
                autoload -Uz compinit && compinit
        option 2:
            create a _cortex file in your fpath, for example:
                cortex completion zsh > /usr/local/share/zsh/site-functions/_cortex

Note: this will also add the "cx" alias for cortex for convenience

Usage:
  cortex completion SHELL [flags]

Flags:
  -h, --help   help for completion
```


# Python API

## Python API

* [cortex](#cortex)
  * [client](#client)
  * [new\_client](#new_client)
  * [env\_list](#env_list)
  * [env\_delete](#env_delete)
* [cortex.client.Client](#cortex-client-client)
  * [create\_api](#create_api)
  * [get\_api](#get_api)
  * [list\_apis](#list_apis)
  * [get\_job](#get_job)
  * [refresh](#refresh)
  * [patch](#patch)
  * [delete\_api](#delete_api)
  * [stop\_job](#stop_job)
  * [stream\_api\_logs](#stream_api_logs)
  * [stream\_job\_logs](#stream_job_logs)

## cortex

### client

```python
client(env: str) -> Client
```

Initialize a client based on the specified environment.

**Arguments**:

* `env` - Name of the environment to use.

**Returns**:

Cortex client that can be used to deploy and manage APIs in the specified environment.

### new\_client

```python
new_client(name: str, operator_endpoint: str) -> Client
```

Create a new environment to connect to an existing Cortex Cluster, and initialize a client to deploy and manage APIs on that cluster.

**Arguments**:

* `name` - Name of the environment to create.
* `operator_endpoint` - The endpoint for the operator of your Cortex Cluster. You can get this endpoint by running the CLI command `cortex cluster info` for an AWS provider or `cortex cluster-gcp info` for a GCP provider.

**Returns**:

Cortex client that can be used to deploy and manage APIs on a Cortex Cluster.

### env\_list

```python
env_list() -> list
```

List all environments configured on this machine.

### env\_delete

```python
env_delete(name: str)
```

Delete an environment configured on this machine.

**Arguments**:

* `name` - Name of the environment to delete.

## cortex.client.Client

### create\_api

```python
 | create_api(api_spec: dict, predictor=None, task=None, requirements=[], conda_packages=[], project_dir: Optional[str] = None, force: bool = True, wait: bool = False) -> list
```

Deploy an API.

**Arguments**:

* `api_spec` - A dictionary defining a single Cortex API. See <https://docs.cortex.dev/v/0.29/> for schema.
* `predictor` - A Cortex Predictor class implementation. Not required for TaskAPI/TrafficSplitter kinds.
* `task` - A callable class/function implementation. Not required for RealtimeAPI/BatchAPI/TrafficSplitter kinds.
* `requirements` - A list of PyPI dependencies that will be installed before the predictor class implementation is invoked.
* `conda_packages` - A list of Conda dependencies that will be installed before the predictor class implementation is invoked.
* `project_dir` - Path to a python project.
* `force` - Override any in-progress api updates.
* `wait` - Streams logs until the APIs are ready.

**Returns**:

Deployment status, API specification, and endpoint for each API.

### get\_api

```python
 | get_api(api_name: str) -> dict
```

Get information about an API.

**Arguments**:

* `api_name` - Name of the API.

**Returns**:

Information about the API, including the API specification, endpoint, status, and metrics (if applicable).

### list\_apis

```python
 | list_apis() -> list
```

List all APIs in the environment.

**Returns**:

List of APIs, including information such as the API specification, endpoint, status, and metrics (if applicable).

### get\_job

```python
 | get_job(api_name: str, job_id: str) -> dict
```

Get information about a submitted job.

**Arguments**:

* `api_name` - Name of the Batch/Task API.
* `job_id` - Job ID.

**Returns**:

Information about the job, including the job status, worker status, and job progress.

### refresh

```python
 | refresh(api_name: str, force: bool = False)
```

Restart all of the replicas for a Realtime API without downtime.

**Arguments**:

* `api_name` - Name of the API to refresh.
* `force` - Override an already in-progress API update.

### patch

```python
 | patch(api_spec: dict, force: bool = False) -> dict
```

Update the api specification for an API that has already been deployed.

**Arguments**:

* `api_spec` - The new api specification to apply
* `force` - Override an already in-progress API update.

### delete\_api

```python
 | delete_api(api_name: str, keep_cache: bool = False)
```

Delete an API.

**Arguments**:

* `api_name` - Name of the API to delete.
* `keep_cache` - Whether to retain the cached data for this API.

### stop\_job

```python
 | stop_job(api_name: str, job_id: str, keep_cache: bool = False)
```

Stop a running job.

**Arguments**:

* `api_name` - Name of the Batch/Task API.
* `job_id` - ID of the Job to stop.

### stream\_api\_logs

```python
 | stream_api_logs(api_name: str)
```

Stream the logs of an API.

**Arguments**:

* `api_name` - Name of the API.

### stream\_job\_logs

```python
 | stream_job_logs(api_name: str, job_id: str)
```

Stream the logs of a Job.

**Arguments**:

* `api_name` - Name of the Batch API.
* `job_id` - Job ID.


# Environments

When you create a cluster with `cortex cluster up`, an environment named `aws` or `gcp` is automatically created to point to your cluster and is configured to be the default environment. You can name the environment something else via the `--configure-env` flag, e.g. `cortex cluster up --configure-env prod`. You can also use the `--configure-env` flag with `cortex cluster info` and `cortex cluster configure` to create / update the specified environment.

You can list your environments with `cortex env list`, change the default environment with `cortex env default`, delete an environment with `cortex env delete`, and create/update an environment with `cortex env configure`.

## Multiple clusters

```bash
cortex cluster up --config cluster1.yaml --configure-env cluster1  # configures the cluster1 env
cortex cluster up --config cluster2.yaml --configure-env cluster2  # configures the cluster2 env

cortex deploy --env cluster1
cortex logs my-api --env cluster1
cortex delete my-api --env cluster1

cortex deploy --env cluster2
cortex logs my-api --env cluster2
cortex delete my-api --env cluster2
```

## Multiple clusters, if you omitted the `--configure-env` on `cortex cluster up`

```bash
cortex cluster info --config cluster1.yaml --configure-env cluster1  # configures the cluster1 env
cortex cluster info --config cluster2.yaml --configure-env cluster2  # configures the cluster2 env

cortex deploy --env cluster1
cortex logs my-api --env cluster1
cortex delete my-api --env cluster1

cortex deploy --env cluster2
cortex logs my-api --env cluster2
cortex delete my-api --env cluster2
```

## Configure `cortex` CLI to connect to an existing cluster

If you are installing the `cortex` CLI on a new machine, you can configure it to access an existing Cortex cluster.

On the machine which already has the CLI configured, run:

```bash
cortex env list
```

Take note of the environment name and operator endpoint of the desired environment.

On your new machine, run:

```bash
cortex env configure
```


# Telemetry

By default, Cortex sends anonymous usage data to Cortex Labs.

## What data is collected?

If telemetry is enabled, events and errors are collected. Each time you run a command an event will be sent with a randomly generated unique CLI ID and the name of the command. For example, if you run `cortex get`, Cortex Labs will receive an event of the structure `{id: 1234, command: "get"}`. In addition, the operator sends heartbeats that include cluster metrics like the types of instances running in your cluster.

## How do I opt out?

If you'd like to disable telemetry, modify your `~/.cortex/cli.yaml` file (or create it if it doesn't exist) and add `telemetry: false` before spinning up your cluster.


# Uninstall

## Uninstall (if installed with pip)

```bash
pip uninstall cortex
rm -rf ~/.cortex
```

## Uninstall (if installed without pip)

```bash
rm /usr/local/bin/cortex
rm -rf ~/.cortex
```


# Realtime APIs


# Example

Create APIs that can respond to prediction requests in real-time.

## Implement

```bash
$ mkdir text-generator && cd text-generator
$ touch predictor.py requirements.txt text_generator.yaml
```

```python
# predictor.py

from transformers import pipeline

class PythonPredictor:
    def __init__(self, config):
        self.model = pipeline(task="text-generation")

    def predict(self, payload):
        return self.model(payload["text"])[0]
```

```python
# requirements.txt

transformers
torch
```

```yaml
# text_generator.yaml

- name: text-generator
  kind: RealtimeAPI
  predictor:
    type: python
    path: predictor.py
  compute:
    gpu: 1
```

## Deploy

```bash
$ cortex deploy text_generator.yaml
```

## Monitor

```bash
$ cortex get text-generator --watch
```

## Stream logs

```bash
$ cortex logs text-generator
```

## Make a request

```bash
$ curl http://***.elb.us-west-2.amazonaws.com/text-generator -X POST -H "Content-Type: application/json" -d '{"text": "hello world"}'
```

## Delete

```bash
$ cortex delete text-generator
```


# Predictor

Which Predictor you use depends on how your model is exported:

* [TensorFlow Predictor](#tensorflow-predictor) if your model is exported as a TensorFlow `SavedModel`
* [ONNX Predictor](#onnx-predictor) if your model is exported in the ONNX format
* [Python Predictor](#python-predictor) for all other cases

The response type of the predictor can vary depending on your requirements, see [API responses](#api-responses) below.

## Project files

Cortex makes all files in the project directory (i.e. the directory which contains `cortex.yaml`) available for use in your Predictor implementation. Python bytecode files (`*.pyc`, `*.pyo`, `*.pyd`), files or folders that start with `.`, and the api configuration file (e.g. `cortex.yaml`) are excluded.

The following files can also be added at the root of the project's directory:

* `.cortexignore` file, which follows the same syntax and behavior as a [.gitignore file](https://git-scm.com/docs/gitignore).
* `.env` file, which exports environment variables that can be used in the predictor. Each line of this file must follow the `VARIABLE=value` format.

For example, if your directory looks like this:

```
./my-classifier/
├── cortex.yaml
├── values.json
├── predictor.py
├── ...
└── requirements.txt
```

You can access `values.json` in your Predictor like this:

```python
import json

class PythonPredictor:
    def __init__(self, config):
        with open('values.json', 'r') as values_file:
            values = json.load(values_file)
        self.values = values
```

## Python Predictor

### Interface

```python
# initialization code and variables can be declared here in global scope

class PythonPredictor:
    def __init__(self, config, python_client):
        """(Required) Called once before the API becomes available. Performs
        setup such as downloading/initializing the model or downloading a
        vocabulary.

        Args:
            config (required): Dictionary passed from API configuration (if
                specified). This may contain information on where to download
                the model and/or metadata.
            python_client (optional): Python client which is used to retrieve
                models for prediction. This should be saved for use in predict().
                Required when `predictor.multi_model_reloading` is specified in the api configuration.
        """
        self.client = python_client # optional

    def predict(self, payload, query_params, headers):
        """(Required) Called once per request. Preprocesses the request payload
        (if necessary), runs inference, and postprocesses the inference output
        (if necessary).

        Args:
            payload (optional): The request payload (see below for the possible
                payload types).
            query_params (optional): A dictionary of the query parameters used
                in the request.
            headers (optional): A dictionary of the headers sent in the request.

        Returns:
            Prediction or a batch of predictions.
        """
        pass

    def post_predict(self, response, payload, query_params, headers):
        """(Optional) Called in the background after returning a response.
        Useful for tasks that the client doesn't need to wait on before
        receiving a response such as recording metrics or storing results.

        Note: post_predict() and predict() run in the same thread pool. The
        size of the thread pool can be increased by updating
        `threads_per_process` in the api configuration yaml.

        Args:
            response (optional): The response as returned by the predict method.
            payload (optional): The request payload (see below for the possible
                payload types).
            query_params (optional): A dictionary of the query parameters used
                in the request.
            headers (optional): A dictionary of the headers sent in the request.
        """
        pass

    def load_model(self, model_path):
        """(Optional) Called by Cortex to load a model when necessary.

        This method is required when `predictor.multi_model_reloading`
        field is specified in the api configuration.

        Warning: this method must not make any modification to the model's
        contents on disk.

        Args:
            model_path: The path to the model on disk.

        Returns:
            The loaded model from disk. The returned object is what
            self.client.get_model() will return.
        """
        pass
```

When explicit model paths are specified in the Python predictor's API configuration, Cortex provides a `python_client` to your Predictor's constructor. `python_client` is an instance of [PythonClient](https://github.com/cortexlabs/cortex/tree/0.29/pkg/cortex/serve/cortex_internal/lib/client/python.py) that is used to load model(s) (it calls the `load_model()` method of your predictor, which must be defined when using explicit model paths). It should be saved as an instance variable in your Predictor, and your `predict()` function should call `python_client.get_model()` to load your model for inference. Preprocessing of the JSON payload and postprocessing of predictions can be implemented in your `predict()` function as well.

When multiple models are defined using the Predictor's `models` field, the `python_client.get_model()` method expects an argument `model_name` which must hold the name of the model that you want to load (for example: `self.client.get_model("text-generator")`). There is also an optional second argument to specify the model version.

For proper separation of concerns, it is recommended to use the constructor's `config` parameter for information such as from where to download the model and initialization files, or any configurable model parameters. You define `config` in your API configuration, and it is passed through to your Predictor's constructor.

Your API can accept requests with different types of payloads such as `JSON`-parseable, `bytes` or `starlette.datastructures.FormData` data. Navigate to the [API requests](#api-requests) section to learn about how headers can be used to change the type of `payload` that is passed into your `predict` method.

Your `predictor` method can return different types of objects such as `JSON`-parseable, `string`, and `bytes` objects. Navigate to the [API responses](#api-responses) section to learn about how to configure your `predictor` method to respond with different response codes and content-types.

## TensorFlow Predictor

**Uses TensorFlow version 2.3.0 by default**

### Interface

```python
class TensorFlowPredictor:
    def __init__(self, tensorflow_client, config):
        """(Required) Called once before the API becomes available. Performs
        setup such as downloading/initializing a vocabulary.

        Args:
            tensorflow_client (required): TensorFlow client which is used to
                make predictions. This should be saved for use in predict().
            config (required): Dictionary passed from API configuration (if
                specified).
        """
        self.client = tensorflow_client
        # Additional initialization may be done here

    def predict(self, payload, query_params, headers):
        """(Required) Called once per request. Preprocesses the request payload
        (if necessary), runs inference (e.g. by calling
        self.client.predict(model_input)), and postprocesses the inference
        output (if necessary).

        Args:
            payload (optional): The request payload (see below for the possible
                payload types).
            query_params (optional): A dictionary of the query parameters used
                in the request.
            headers (optional): A dictionary of the headers sent in the request.

        Returns:
            Prediction or a batch of predictions.
        """
        pass

    def post_predict(self, response, payload, query_params, headers):
        """(Optional) Called in the background after returning a response.
        Useful for tasks that the client doesn't need to wait on before
        receiving a response such as recording metrics or storing results.

        Note: post_predict() and predict() run in the same thread pool. The
        size of the thread pool can be increased by updating
        `threads_per_process` in the api configuration yaml.

        Args:
            response (optional): The response as returned by the predict method.
            payload (optional): The request payload (see below for the possible
                payload types).
            query_params (optional): A dictionary of the query parameters used
                in the request.
            headers (optional): A dictionary of the headers sent in the request.
        """
        pass
```

Cortex provides a `tensorflow_client` to your Predictor's constructor. `tensorflow_client` is an instance of [TensorFlowClient](https://github.com/cortexlabs/cortex/tree/0.29/pkg/cortex/serve/cortex_internal/lib/client/tensorflow.py) that manages a connection to a TensorFlow Serving container to make predictions using your model. It should be saved as an instance variable in your Predictor, and your `predict()` function should call `tensorflow_client.predict()` to make an inference with your exported TensorFlow model. Preprocessing of the JSON payload and postprocessing of predictions can be implemented in your `predict()` function as well.

When multiple models are defined using the Predictor's `models` field, the `tensorflow_client.predict()` method expects a second argument `model_name` which must hold the name of the model that you want to use for inference (for example: `self.client.predict(payload, "text-generator")`). There is also an optional third argument to specify the model version.

For proper separation of concerns, it is recommended to use the constructor's `config` parameter for information such as configurable model parameters or download links for initialization files. You define `config` in your API configuration, and it is passed through to your Predictor's constructor.

Your API can accept requests with different types of payloads such as `JSON`-parseable, `bytes` or `starlette.datastructures.FormData` data. Navigate to the [API requests](#api-requests) section to learn about how headers can be used to change the type of `payload` that is passed into your `predict` method.

Your `predictor` method can return different types of objects such as `JSON`-parseable, `string`, and `bytes` objects. Navigate to the [API responses](#api-responses) section to learn about how to configure your `predictor` method to respond with different response codes and content-types.

If you need to share files between your predictor implementation and the TensorFlow Serving container, you can create a new directory within `/mnt` (e.g. `/mnt/user`) and write files to it. The entire `/mnt` directory is shared between containers, but do not write to any of the directories in `/mnt` that already exist (they are used internally by Cortex).

## ONNX Predictor

**Uses ONNX Runtime version 1.6.0 by default**

### Interface

```python
class ONNXPredictor:
    def __init__(self, onnx_client, config):
        """(Required) Called once before the API becomes available. Performs
        setup such as downloading/initializing a vocabulary.

        Args:
            onnx_client (required): ONNX client which is used to make
                predictions. This should be saved for use in predict().
            config (required): Dictionary passed from API configuration (if
                specified).
        """
        self.client = onnx_client
        # Additional initialization may be done here

    def predict(self, payload, query_params, headers):
        """(Required) Called once per request. Preprocesses the request payload
        (if necessary), runs inference (e.g. by calling
        self.client.predict(model_input)), and postprocesses the inference
        output (if necessary).

        Args:
            payload (optional): The request payload (see below for the possible
                payload types).
            query_params (optional): A dictionary of the query parameters used
                in the request.
            headers (optional): A dictionary of the headers sent in the request.

        Returns:
            Prediction or a batch of predictions.
        """
        pass

    def post_predict(self, response, payload, query_params, headers):
        """(Optional) Called in the background after returning a response.
        Useful for tasks that the client doesn't need to wait on before
        receiving a response such as recording metrics or storing results.

        Note: post_predict() and predict() run in the same thread pool. The
        size of the thread pool can be increased by updating
        `threads_per_process` in the api configuration yaml.

        Args:
            response (optional): The response as returned by the predict method.
            payload (optional): The request payload (see below for the possible
                payload types).
            query_params (optional): A dictionary of the query parameters used
                in the request.
            headers (optional): A dictionary of the headers sent in the request.
        """
        pass
```

Cortex provides an `onnx_client` to your Predictor's constructor. `onnx_client` is an instance of [ONNXClient](https://github.com/cortexlabs/cortex/tree/0.29/pkg/cortex/serve/cortex_internal/lib/client/onnx.py) that manages an ONNX Runtime session to make predictions using your model. It should be saved as an instance variable in your Predictor, and your `predict()` function should call `onnx_client.predict()` to make an inference with your exported ONNX model. Preprocessing of the JSON payload and postprocessing of predictions can be implemented in your `predict()` function as well.

When multiple models are defined using the Predictor's `models` field, the `onnx_client.predict()` method expects a second argument `model_name` which must hold the name of the model that you want to use for inference (for example: `self.client.predict(model_input, "text-generator")`). There is also an optional third argument to specify the model version.

For proper separation of concerns, it is recommended to use the constructor's `config` parameter for information such as configurable model parameters or download links for initialization files. You define `config` in your API configuration, and it is passed through to your Predictor's constructor.

Your API can accept requests with different types of payloads such as `JSON`-parseable, `bytes` or `starlette.datastructures.FormData` data. Navigate to the [API requests](#api-requests) section to learn about how headers can be used to change the type of `payload` that is passed into your `predict` method.

Your `predictor` method can return different types of objects such as `JSON`-parseable, `string`, and `bytes` objects. Navigate to the [API responses](#api-responses) section to learn about how to configure your `predictor` method to respond with different response codes and content-types.

## API requests

The type of the `payload` parameter in `predict(self, payload)` can vary based on the content type of the request. The `payload` parameter is parsed according to the `Content-Type` header in the request. Here are the parsing rules (see below for examples):

1. For `Content-Type: application/json`, `payload` will be the parsed JSON body.
2. For `Content-Type: multipart/form-data` / `Content-Type: application/x-www-form-urlencoded`, `payload` will be `starlette.datastructures.FormData` (key-value pairs where the values are strings for text data, or `starlette.datastructures.UploadFile` for file uploads; see [Starlette's documentation](https://www.starlette.io/requests/#request-files)).
3. For `Content-Type: text/plain`, `payload` will be a string. `utf-8` encoding is assumed, unless specified otherwise (e.g. via `Content-Type: text/plain; charset=us-ascii`)
4. For all other `Content-Type` values, `payload` will be the raw `bytes` of the request body.

Here are some examples:

### JSON data

#### Making the request

```bash
$ curl http://***.amazonaws.com/my-api \
    -X POST -H "Content-Type: application/json" \
    -d '{"key": "value"}'
```

#### Reading the payload

When sending a JSON payload, the `payload` parameter will be a Python object:

```python
class PythonPredictor:
    def __init__(self, config):
        pass

    def predict(self, payload):
        print(payload["key"])  # prints "value"
```

### Binary data

#### Making the request

```bash
$ curl http://***.amazonaws.com/my-api \
    -X POST -H "Content-Type: application/octet-stream" \
    --data-binary @object.pkl
```

#### Reading the payload

Since the `Content-Type: application/octet-stream` header is used, the `payload` parameter will be a `bytes` object:

```python
import pickle

class PythonPredictor:
    def __init__(self, config):
        pass

    def predict(self, payload):
        obj = pickle.loads(payload)
        print(obj["key"])  # prints "value"
```

Here's an example if the binary data is an image:

```python
from PIL import Image
import io

class PythonPredictor:
    def __init__(self, config):
        pass

    def predict(self, payload, headers):
        img = Image.open(io.BytesIO(payload))  # read the payload bytes as an image
        print(img.size)
```

### Form data (files)

#### Making the request

```bash
$ curl http://***.amazonaws.com/my-api \
    -X POST \
    -F "text=@text.txt" \
    -F "object=@object.pkl" \
    -F "image=@image.png"
```

#### Reading the payload

When sending files via form data, the `payload` parameter will be `starlette.datastructures.FormData` (key-value pairs where the values are `starlette.datastructures.UploadFile`, see [Starlette's documentation](https://www.starlette.io/requests/#request-files)). Either `Content-Type: multipart/form-data` or `Content-Type: application/x-www-form-urlencoded` can be used (typically `Content-Type: multipart/form-data` is used for files, and is the default in the examples above).

```python
from PIL import Image
import pickle

class PythonPredictor:
    def __init__(self, config):
        pass

    def predict(self, payload):
        text = payload["text"].file.read()
        print(text.decode("utf-8"))  # prints the contents of text.txt

        obj = pickle.load(payload["object"].file)
        print(obj["key"])  # prints "value" assuming `object.pkl` is a pickled dictionary {"key": "value"}

        img = Image.open(payload["image"].file)
        print(img.size)  # prints the dimensions of image.png
```

### Form data (text)

#### Making the request

```bash
$ curl http://***.amazonaws.com/my-api \
    -X POST \
    -d "key=value"
```

#### Reading the payload

When sending text via form data, the `payload` parameter will be `starlette.datastructures.FormData` (key-value pairs where the values are strings, see [Starlette's documentation](https://www.starlette.io/requests/#request-files)). Either `Content-Type: multipart/form-data` or `Content-Type: application/x-www-form-urlencoded` can be used (typically `Content-Type: application/x-www-form-urlencoded` is used for text, and is the default in the examples above).

```python
class PythonPredictor:
    def __init__(self, config):
        pass

    def predict(self, payload):
        print(payload["key"])  # will print "value"
```

### Text data

#### Making the request

```bash
$ curl http://***.amazonaws.com/my-api \
    -X POST -H "Content-Type: text/plain" \
    -d "hello world"
```

#### Reading the payload

Since the `Content-Type: text/plain` header is used, the `payload` parameter will be a `string` object:

```python
class PythonPredictor:
    def __init__(self, config):
        pass

    def predict(self, payload):
        print(payload)  # prints "hello world"
```

## API responses

The response of your `predict()` function may be:

1. A JSON-serializable object (*lists*, *dictionaries*, *numbers*, etc.)
2. A `string` object (e.g. `"class 1"`)
3. A `bytes` object (e.g. `bytes(4)` or `pickle.dumps(obj)`)
4. An instance of [starlette.responses.Response](https://www.starlette.io/responses/#response)

## Chaining APIs

It is possible to make requests from one API to another within a Cortex cluster. All running APIs are accessible from within the predictor at `http://api-<api_name>:8888/predict`, where `<api_name>` is the name of the API you are making a request to.

For example, if there is an api named `text-generator` running in the cluster, you could make a request to it from a different API by using:

```python
import requests

class PythonPredictor:
    def predict(self, payload):
        response = requests.post("http://api-text-generator:8888/predict", json={"text": "machine learning is"})
        # ...
```

Note that the autoscaling configuration (i.e. `target_replica_concurrency`) for the API that is making the request should be modified with the understanding that requests will still be considered "in-flight" with the first API as the request is being fulfilled in the second API (during which it will also be considered "in-flight" with the second API).

## Structured logging

You can use Cortex's logger in your predictor implemention to log in JSON. This will enrich your logs with Cortex's metadata, and you can add custom metadata to the logs by adding key value pairs to the `extra` key when using the logger. For example:

```python
...
from cortex_internal.lib.log import logger as cortex_logger

class PythonPredictor:
    def predict(self, payload):
        cortex_logger.info("received payload", extra={"payload": payload})
```

The dictionary passed in via the `extra` will be flattened by one level. e.g.

```
{"asctime": "2021-01-19 15:14:05,291", "levelname": "INFO", "message": "received payload", "process": 235, "payload": "this movie is awesome"}
```

To avoid overriding essential Cortex metadata, please refrain from specifying the following extra keys: `asctime`, `levelname`, `message`, `labels`, and `process`. Log lines greater than 5 MB in size will be ignored.


# Configuration

```yaml
- name: <string>
  kind: RealtimeAPI
  predictor: # detailed configuration below
  compute: # detailed configuration below
  autoscaling: # detailed configuration below
  update_strategy: # detailed configuration below
  networking: # detailed configuration below
```

## Predictor

### Python Predictor

```yaml
predictor:
  type: python
  path: <string>  # path to a python file with a PythonPredictor class definition, relative to the Cortex root (required)
  multi_model_reloading:  # use this to serve one or more models with live reloading (optional)
    path: <string> # S3/GCS path to an exported model directory (e.g. s3://my-bucket/exported_model/) (either this, 'dir', or 'paths' must be provided if 'multi_model_reloading' is specified)
    paths:  # list of S3/GCS paths to exported model directories (either this, 'dir', or 'path' must be provided if 'multi_model_reloading' is specified)
      - name: <string>  # unique name for the model (e.g. text-generator) (required)
        path: <string>  # S3/GCS path to an exported model directory (e.g. s3://my-bucket/exported_model/) (required)
      ...
    dir: <string>  # S3/GCS path to a directory containing multiple models (e.g. s3://my-bucket/models/) (either this, 'path', or 'paths' must be provided if 'multi_model_reloading' is specified)
    cache_size: <int>  # the number models to keep in memory (optional; all models are kept in memory by default)
    disk_cache_size: <int>  # the number of models to keep on disk (optional; all models are kept on disk by default)
  server_side_batching:  # (optional)
    max_batch_size: <int>  # the maximum number of requests to aggregate before running inference
    batch_interval: <duration>  # the maximum amount of time to spend waiting for additional requests before running inference on the batch of requests
  processes_per_replica: <int>  # the number of parallel serving processes to run on each replica (default: 1)
  threads_per_process: <int>  # the number of threads per process (default: 1)
  config: <string: value>  # arbitrary dictionary passed to the constructor of the Predictor (optional)
  python_path: <string>  # path to the root of your Python folder that will be appended to PYTHONPATH (default: folder containing cortex.yaml)
  image: <string>  # docker image to use for the Predictor (default: quay.io/cortexlabs/python-predictor-cpu:0.29.0, quay.io/cortexlabs/python-predictor-gpu:0.29.0-cuda10.2-cudnn8, or quay.io/cortexlabs/python-predictor-inf:0.29.0 based on compute)
  env: <string: string>  # dictionary of environment variables
  log_level: <string>  # log level that can be "debug", "info", "warning" or "error" (default: "info")
  shm_size: <string>  # size of shared memory (/dev/shm) for sharing data between multiple processes, e.g. 64Mi or 1Gi (default: Null)
```

### TensorFlow Predictor

```yaml
predictor:
  type: tensorflow
  path: <string>  # path to a python file with a TensorFlowPredictor class definition, relative to the Cortex root (required)
  models:  # (required)
    path: <string> # S3/GCS path to an exported SavedModel directory (e.g. s3://my-bucket/exported_model/) (either this, 'dir', or 'paths' must be provided)
    paths:  # list of S3/GCS paths to exported SavedModel directories (either this, 'dir', or 'path' must be provided)
      - name: <string>  # unique name for the model (e.g. text-generator) (required)
        path: <string>  # S3/GCS path to an exported SavedModel directory (e.g. s3://my-bucket/exported_model/) (required)
        signature_key: <string>  # name of the signature def to use for prediction (required if your model has more than one signature def)
      ...
    dir: <string>  # S3/GCS path to a directory containing multiple SavedModel directories (e.g. s3://my-bucket/models/) (either this, 'path', or 'paths' must be provided)
    signature_key:  # name of the signature def to use for prediction (required if your model has more than one signature def)
    cache_size: <int>  # the number models to keep in memory (optional; all models are kept in memory by default)
    disk_cache_size: <int>  # the number of models to keep on disk (optional; all models are kept on disk by default)
  server_side_batching:  # (optional)
    max_batch_size: <int>  # the maximum number of requests to aggregate before running inference
    batch_interval: <duration>  # the maximum amount of time to spend waiting for additional requests before running inference on the batch of requests
  processes_per_replica: <int>  # the number of parallel serving processes to run on each replica (default: 1)
  threads_per_process: <int>  # the number of threads per process (default: 1)
  config: <string: value>  # arbitrary dictionary passed to the constructor of the Predictor (optional)
  python_path: <string>  # path to the root of your Python folder that will be appended to PYTHONPATH (default: folder containing cortex.yaml)
  image: <string>  # docker image to use for the Predictor (default: quay.io/cortexlabs/tensorflow-predictor:0.29.0)
  tensorflow_serving_image: <string>  # docker image to use for the TensorFlow Serving container (default: quay.io/cortexlabs/tensorflow-serving-cpu:0.29.0, quay.io/cortexlabs/tensorflow-serving-gpu:0.29.0, or quay.io/cortexlabs/tensorflow-serving-inf:0.29.0 based on compute)
  env: <string: string>  # dictionary of environment variables
  log_level: <string>  # log level that can be "debug", "info", "warning" or "error" (default: "info")
  shm_size: <string>  # size of shared memory (/dev/shm) for sharing data between multiple processes, e.g. 64Mi or 1Gi (default: Null)
```

### ONNX Predictor

```yaml
predictor:
  type: onnx
  path: <string>  # path to a python file with an ONNXPredictor class definition, relative to the Cortex root (required)
  models:  # (required)
    path: <string> # S3/GCS path to an exported model directory (e.g. s3://my-bucket/exported_model/) (either this, 'dir', or 'paths' must be provided)
    paths:  # list of S3/GCS paths to exported model directories (either this, 'dir', or 'path' must be provided)
      - name: <string>  # unique name for the model (e.g. text-generator) (required)
        path: <string>  # S3/GCS path to an exported model directory (e.g. s3://my-bucket/exported_model/) (required)
      ...
    dir: <string>  # S3/GCS path to a directory containing multiple model directories (e.g. s3://my-bucket/models/) (either this, 'path', or 'paths' must be provided)
    cache_size: <int>  # the number models to keep in memory (optional; all models are kept in memory by default)
    disk_cache_size: <int>  # the number of models to keep on disk (optional; all models are kept on disk by default)
  processes_per_replica: <int>  # the number of parallel serving processes to run on each replica (default: 1)
  threads_per_process: <int>  # the number of threads per process (default: 1)
  config: <string: value>  # arbitrary dictionary passed to the constructor of the Predictor (optional)
  python_path: <string>  # path to the root of your Python folder that will be appended to PYTHONPATH (default: folder containing cortex.yaml)
  image: <string>  # docker image to use for the Predictor (default: quay.io/cortexlabs/onnx-predictor-cpu:0.29.0 or quay.io/cortexlabs/onnx-predictor-gpu:0.29.0 based on compute)
  env: <string: string>  # dictionary of environment variables
  log_level: <string>  # log level that can be "debug", "info", "warning" or "error" (default: "info")
  shm_size: <string>  # size of shared memory (/dev/shm) for sharing data between multiple processes, e.g. 64Mi or 1Gi (default: Null)
```

## Compute

```yaml
compute:
  cpu: <string | int | float>  # CPU request per replica. One unit of CPU corresponds to one virtual CPU; fractional requests are allowed, and can be specified as a floating point number or via the "m" suffix (default: 200m)
  gpu: <int>  # GPU request per replica. One unit of GPU corresponds to one virtual GPU (default: 0)
  mem: <string>  # memory request per replica. One unit of memory is one byte and can be expressed as an integer or by using one of these suffixes: K, M, G, T (or their power-of two counterparts: Ki, Mi, Gi, Ti) (default: Null)
```

## Autoscaling

```yaml
autoscaling:
  min_replicas: <int>  # minimum number of replicas (default: 1)
  max_replicas: <int>  # maximum number of replicas (default: 100)
  init_replicas: <int>  # initial number of replicas (default: <min_replicas>)
  max_replica_concurrency: <int>  # the maximum number of in-flight requests per replica before requests are rejected with error code 503 (default: 1024)
  target_replica_concurrency: <float>  # the desired number of in-flight requests per replica, which the autoscaler tries to maintain (default: processes_per_replica * threads_per_process) (aws only)
  window: <duration>  # the time over which to average the API's concurrency (default: 60s) (aws only)
  downscale_stabilization_period: <duration>  # the API will not scale below the highest recommendation made during this period (default: 5m) (aws only)
  upscale_stabilization_period: <duration>  # the API will not scale above the lowest recommendation made during this period (default: 1m) (aws only)
  max_downscale_factor: <float>  # the maximum factor by which to scale down the API on a single scaling event (default: 0.75) (aws only)
  max_upscale_factor: <float>  # the maximum factor by which to scale up the API on a single scaling event (default: 1.5) (aws only)
  downscale_tolerance: <float>  # any recommendation falling within this factor below the current number of replicas will not trigger a scale down event (default: 0.05) (aws only)
  upscale_tolerance: <float>  # any recommendation falling within this factor above the current number of replicas will not trigger a scale up event (default: 0.05) (aws only)
```

## Update strategy

```yaml
update_strategy:
  max_surge: <string | int>  # maximum number of replicas that can be scheduled above the desired number of replicas during an update; can be an absolute number, e.g. 5, or a percentage of desired replicas, e.g. 10% (default: 25%) (set to 0 to disable rolling updates)
  max_unavailable: <string | int>  # maximum number of replicas that can be unavailable during an update; can be an absolute number, e.g. 5, or a percentage of desired replicas, e.g. 10% (default: 25%)
```

## Networking

```yaml
  networking:
    endpoint: <string>  # the endpoint for the API (default: <api_name>)
```


# Models

## Model directory format

Whenever a model path is specified in an API configuration file, it should be a path to an S3/GCS prefix which contains your exported model. Directories may include a single model, or multiple folders each with a single model (note that a "single model" need not be a single file; there can be multiple files for a single model). When multiple folders are used, the folder names must be integer values, and will be interpreted as the model version. Model versions can be any integer, but are typically integer timestamps. It is always assumed that the highest version number is the latest version of your model.

Each predictor type expects a different model format:

### Python

For the Python predictor, any model structure is accepted. Here is an example:

```
  s3://my-bucket/models/text-generator/
  ├── model.pkl
  └── data.txt
```

or for a versioned model:

```
  s3://my-bucket/models/text-generator/
  ├── 1523423423/  (version number, usually a timestamp)
  |   ├── model.pkl
  |   └── data.txt
  └── 2434389194/  (version number, usually a timestamp)
      ├── model.pkl
      └── data.txt
```

### TensorFlow

For the TensorFlow predictor, the model path must be a SavedModel export:

```
  s3://my-bucket/models/text-generator/
  ├── saved_model.pb
  └── variables/
      ├── variables.index
      ├── variables.data-00000-of-00003
      ├── variables.data-00001-of-00003
      └── variables.data-00002-of-...
```

or for a versioned model:

```
  s3://my-bucket/models/text-generator/
  ├── 1523423423/  (version number, usually a timestamp)
  |   ├── saved_model.pb
  |   └── variables/
  |       ├── variables.index
  |       ├── variables.data-00000-of-00003
  |       ├── variables.data-00001-of-00003
  |       └── variables.data-00002-of-...
  └── 2434389194/  (version number, usually a timestamp)
      ├── saved_model.pb
      └── variables/
          ├── variables.index
          ├── variables.data-00000-of-00003
          ├── variables.data-00001-of-00003
          └── variables.data-00002-of-...
```

#### Inferentia

When Inferentia models are used, the directory structure is slightly different:

```
  s3://my-bucket/models/text-generator/
  └── saved_model.pb
```

or for a versioned model:

```
  s3://my-bucket/models/text-generator/
  ├── 1523423423/  (version number, usually a timestamp)
  |   └── saved_model.pb
  └── 2434389194/  (version number, usually a timestamp)
      └── saved_model.pb
```

### ONNX

For the ONNX predictor, the model path must contain a single `*.onnx` file:

```
  s3://my-bucket/models/text-generator/
  └── model.onnx
```

or for a versioned model:

```
  s3://my-bucket/models/text-generator/
  ├── 1523423423/  (version number, usually a timestamp)
  |   └── model.onnx
  └── 2434389194/  (version number, usually a timestamp)
      └── model.onnx
```

## Single model

The most common pattern is to serve a single model per API. The path to the model is specified in the `path` field in the `predictor.models` configuration. For example:

```yaml
# cortex.yaml

- name: iris-classifier
  kind: RealtimeAPI
  predictor:
    # ...
    models:
      path: s3://my-bucket/models/text-generator/
```

For the Python predictor type, the `models` field comes under the name of `multi_model_reloading`. It is also not necessary to specify the `multi_model_reloading` section at all, since you can download and load the model in your predictor's `__init__()` function. That said, it is necessary to use the `path` field to take advantage of [live model reloading](#live-model-reloading).

## Multiple models

It is possible to serve multiple models from a single API. The paths to the models are specified in the api configuration, either via the `models.paths` or `models.dir` field in the `predictor` configuration. For example:

```yaml
# cortex.yaml

- name: iris-classifier
  kind: RealtimeAPI
  predictor:
    # ...
    models:
      paths:
        - name: iris-classifier
          path: s3://my-bucket/models/text-generator/
        # ...
```

or:

```yaml
# cortex.yaml

- name: iris-classifier
  kind: RealtimeAPI
  predictor:
    # ...
    models:
      dir: s3://my-bucket/models/
```

For the Python predictor type, the `models` field comes under the name of `multi_model_reloading`. It is also not necessary to specify the `multi_model_reloading` section at all, since you can download and load the model in your predictor's `__init__()` function. That said, it is necessary to use the `models` field to take advantage of live model reloading or multi-model caching.

When using the `models.paths` field, each path must be a valid model directory (see above for valid model directory structures).

When using the `models.dir` field, the directory provided may contain multiple subdirectories, each of which is a valid model directory. For example:

```
  s3://my-bucket/models/
  ├── text-generator
  |   └── * (model files)
  └── sentiment-analyzer
      ├── 24753823/
      |   └── * (model files)
      └── 26234288/
          └── * (model files)
```

In this case, there are two models in the directory, one of which is named "text-generator", and the other is named "sentiment-analyzer".

## Live model reloading

Live model reloading is a mechanism that periodically checks for updated models in the model path(s) provided in `predictor.models`. It is automatically enabled for all predictor types, including the Python predictor type (as long as model paths are specified via `multi_model_reloading` in the `predictor` configuration).

The following is a list of events that will trigger the API to update its model(s):

* A new model is added to the model directory.
* A model is removed from the model directory.
* A model changes its directory structure.
* A file in the model directory is updated in-place.

Usage varies based on the predictor type:

### Python

To use live model reloading with the Python predictor, the model path(s) must be specified in the API's `predictor` configuration, via the `models` field. When models are specified in this manner, your `PythonPredictor` class must implement the `load_model()` function, and models can be retrieved by using the `get_model()` method of the `python_client` that's passed into your predictor's constructor.

The `load_model()` function that you implement in your `PythonPredictor` can return anything that you need to make a prediction. There is one caveat: whatever the return value is, it must be unloadable from memory via the `del` keyword. The following frameworks have been tested to work:

* PyTorch (CPU & GPU)
* ONNX (CPU & GPU)
* Sklearn/MLFlow (CPU)
* Numpy (CPU)
* Pandas (CPU)
* Caffe (not tested, but should work on CPU & GPU)

Python data structures containing these types are also supported (e.g. lists and dicts).

The `load_model()` function takes a single argument, which is a path (on disk) to the model to be loaded. Your `load_model()` function is called behind the scenes by Cortex when you call the `python_client`'s `get_model()` method. Cortex is responsible for downloading your model from S3/GCS onto the local disk before calling `load_model()` with the local path. Whatever `load_model()` returns will be the exact return value of `python_client.get_model()`. Here is the schema for `python_client.get_model()`:

```python
def get_model(model_name, model_version):
    """
    Retrieve a model for inference.

    Args:
        model_name (optional): Name of the model to retrieve (when multiple models are deployed in an API).
            When predictor.models.paths is specified, model_name should be the name of one of the models listed in the API config.
            When predictor.models.dir is specified, model_name should be the name of a top-level directory in the models dir.
        model_version (string, optional): Version of the model to retrieve. Can be omitted or set to "latest" to select the highest version.

    Returns:
        The value that's returned by your predictor's load_model() method.
    """
```

Here's an example:

```python
class PythonPredictor:
    def __init__(self, config, python_client):
        self.client = python_client

    def load_model(self, model_path):
        # model_path is a path to your model's directory on disk
        return load_from_disk(model_path)

    def predict(self, payload):
      model = self.client.get_model()
      return model.predict(payload)
```

When multiple models are being served in an API, `python_client.get_model()` can accept a model name:

```python
class PythonPredictor:
    # ...

    def predict(self, payload, query_params):
      model = self.client.get_model(query_params["model"])
      return model.predict(payload)
```

`python_client.get_model()` can also accept a model version if a version other than the highest is desired:

```python
class PythonPredictor:
    # ...

    def predict(self, payload, query_params):
      model = self.client.get_model(query_params["model"], query_params["version"])
      return model.predict(payload)
```

### TensorFlow

When using the TensorFlow predictor, inference is performed by using the `predict()` method of the `tensorflow_client` that's passed to the predictor's constructor:

```python
def predict(model_input, model_name, model_version) -> dict:
    """
    Run prediction.

    Args:
        model_input: Input to the model.
        model_name (optional): Name of the model to retrieve (when multiple models are deployed in an API).
            When predictor.models.paths is specified, model_name should be the name of one of the models listed in the API config.
            When predictor.models.dir is specified, model_name should be the name of a top-level directory in the models dir.
        model_version (string, optional): Version of the model to retrieve. Can be omitted or set to "latest" to select the highest version.

    Returns:
        dict: TensorFlow Serving response converted to a dictionary.
    """
```

For example:

```python
class TensorFlowPredictor:
    def __init__(self, tensorflow_client, config):
        self.client = tensorflow_client

    def predict(self, payload):
      return self.client.predict(payload)
```

When multiple models are being served in an API, `tensorflow_client.predict()` can accept a model name:

```python
class TensorFlowPredictor:
    # ...

    def predict(self, payload, query_params):
      return self.client.predict(payload, query_params["model"])
```

`tensorflow_client.predict()` can also accept a model version if a version other than the highest is desired:

```python
class TensorFlowPredictor:
    # ...

    def predict(self, payload, query_params):
      return self.client.predict(payload, query_params["model"], query_params["version"])
```

Note: when using Inferentia models with the TensorFlow predictor, live model reloading is only supported if `predictor.processes_per_replica` is set to 1 (the default value).

### ONNX

When using the ONNX predictor, inference is performed by using the `predict()` method of the `onnx_client` that's passed to the predictor's constructor:

```python
def predict(model_input: Any, model_name: Optional[str] = None, model_version: str = "latest") -> Any:
    """
    Run prediction.

    Args:
        model_input: Input to the model.
        model_name (optional): Name of the model to retrieve (when multiple models are deployed in an API).
            When predictor.models.paths is specified, model_name should be the name of one of the models listed in the API config.
            When predictor.models.dir is specified, model_name should be the name of a top-level directory in the models dir.
        model_version (string, optional): Version of the model to retrieve. Can be omitted or set to "latest" to select the highest version.

    Returns:
        The prediction returned from the model.
    """
```

For example:

```python
class ONNXPredictor:
    def __init__(self, onnx_client, config):
        self.client = onnx_client

    def predict(self, payload):
      return self.client.predict(payload)
```

When multiple models are being served in an API, `onnx_client.predict()` can accept a model name:

```python
class ONNXPredictor:
    # ...

    def predict(self, payload, query_params):
      return self.client.predict(payload, query_params["model"])
```

`onnx_client.predict()` can also accept a model version if a version other than the highest is desired:

```python
class ONNXPredictor:
    # ...

    def predict(self, payload, query_params):
      return self.client.predict(payload, query_params["model"], query_params["version"])
```

You can also retrieve information about the model by calling the `onnx_client`'s `get_model()` method (it supports model name and model version arguments, like its `predict()` method). This can be useful for retrieving the model's input/output signatures. For example, `self.client.get_model()` might look like this:

```python
{
    "session": "<onnxruntime.InferenceSession model object>",
    "signatures": "<onnxruntime.InferenceSession model object>['session'].get_inputs()",
    "input_signatures": {
        "<signature-name>": {
            "shape": "<input shape>",
            "type": "<numpy type>"
        }
        ...
    }
}
```


# Parallelism

Replica parallelism can be configured with the following fields in the `predictor` configuration:

* `processes_per_replica` (default: 1): Each replica runs a web server with `processes_per_replica` processes. For APIs running with multiple CPUs per replica, using 1-3 processes per unit of CPU generally leads to optimal throughput. For example, if `cpu` is 2, a value between 2 and 6 `processes_per_replica` is reasonable. The optimal number will vary based on the workload's characteristics and the CPU compute request for the API.
* `threads_per_process` (default: 1): Each process uses a thread pool of size `threads_per_process` to process requests. For applications that are not CPU intensive such as high I/O (e.g. downloading files), GPU-based inference, or Inferentia-based inference, increasing the number of threads per process can increase throughput. For CPU-bound applications such as running your model inference on a CPU, using 1 thread per process is recommended to avoid unnecessary context switching. Some applications are not thread-safe, and therefore must be run with 1 thread per process.

`processes_per_replica` \* `threads_per_process` represents the total number of requests that your replica can work on concurrently. For example, if `processes_per_replica` is 2 and `threads_per_process` is 2, and the replica was hit with 5 concurrent requests, 4 would immediately begin to be processed, and 1 would be waiting for a thread to become available. If the replica were hit with 3 concurrent requests, all three would begin processing immediately.


# Server-side batching

Server-side batching is the process of aggregating multiple real-time requests into a single batch inference, which increases throughput at the expense of latency. Inference is triggered when either a maximum number of requests have been received, or when a certain amount of time has passed since receiving the first request, whichever comes first. Once a threshold is reached, inference is run on the received requests and responses are returned individually back to the clients. This process is transparent to the clients.

The Python and TensorFlow predictors allow for the use of the following 2 fields in the `server_side_batching` configuration:

* `max_batch_size`: The maximum number of requests to aggregate before running inference. This is an instrument for controlling throughput. The maximum size can be achieved if `batch_interval` is long enough to collect `max_batch_size` requests.
* `batch_interval`: The maximum amount of time to spend waiting for additional requests before running inference on the batch of requests. If fewer than `max_batch_size` requests are received after waiting the full `batch_interval`, then inference will run on the requests that have been received. This is an instrument for controlling latency.

## Python predictor

When using server-side batching with the Python predictor, the arguments that are passed into your predictor's `predict()` function will be lists: `payload` will be a list of payloads, `query_params` will be a list of query parameter dictionaries, and `headers` will be a list of header dictionaries. The lists will all have the same length, where a particular index accross all arguments corresponds to a single request (i.e. `payload[2]`, `query_params[2]`, and `headers[2]` correspond to a single prediction request). Your `predict()` function must return a list of responses in the same order that they were received (i.e. the 3rd element in returned list must be the response associated with `payload[2]`).

## TensorFlow predictor

In order to use server-side batching with the TensorFlow predictor, the only requirement is that model's graph must be built such that batches can be accepted as input/output. No modifications to your `TensorFlowPredictor` implementation are required.

The following is an example of how the input `x` and the output `y` of the graph could be shaped to be compatible with server-side batching:

```python
batch_size = None
sample_shape = [340, 240, 3] # i.e. RGB image
output_shape = [1000] # i.e. image labels

with graph.as_default():
    # ...
    x = tf.placeholder(tf.float32, shape=[batch_size] + sample_shape, name="input")
    y = tf.placeholder(tf.float32, shape=[batch_size] + output_shape, name="output")
    # ...
```

### Troubleshooting

Errors will be encountered if the model hasn't been built for batching.

The following error is an example of what happens when the input shape doesn't accommodate batching - e.g. when its shape is `[height, width, 3]` instead of `[batch_size, height, width, 3]`:

```
Batching session Run() input tensors must have at least one dimension.
```

Here is another example of setting the output shape inappropriately for batching - e.g. when its shape is `[labels]` instead of `[batch_size, labels]`:

```
Batched output tensor has 0 dimensions.
```

The solution to these errors is to incorporate into the model's graph another dimension (a placeholder for batch size) placed on the first position for both its input and output.

The following is an example of how the input `x` and the output `y` of the graph could be shaped to be compatible with server-side batching:

```python
batch_size = None
sample_shape = [340, 240, 3] # i.e. RGB image
output_shape = [1000] # i.e. image labels

with graph.as_default():
    # ...
    x = tf.placeholder(tf.float32, shape=[batch_size] + sample_shape, name="input")
    y = tf.placeholder(tf.float32, shape=[batch_size] + output_shape, name="output")
    # ...
```

## Optimization

When optimizing for both throughput and latency, you will likely want keep the `max_batch_size` to a relatively small value. Even though a higher `max_batch_size` with a low `batch_interval` (when there are many requests coming in) can offer a significantly higher throughput, the overall latency could be quite large. The reason is that for a request to get back a response, it has to wait until the entire batch is processed, which means that the added latency due to the `batch_interval` can pale in comparison. For instance, let's assume that a single prediction takes 50ms, and that when the batch size is set to 128, the processing time for a batch is 1280ms (i.e. 10ms per sample). So while the throughput is now 5 times higher, it takes 1280ms + `batch_interval` to get back a response (instead of 50ms). This is the trade-off with server-side batching.

When optimizing for maximum throughput, a good rule of thumb is to follow these steps:

1. Determine the maximum throughput of one API replica when `server_side_batching` is not enabled (same as if `max_batch_size` were set to 1). This can be done with a load test (make sure to set `max_replicas` to 1 to disable autoscaling).
2. Determine the highest `batch_interval` with which you are still comfortable for your application. Keep in mind that the batch interval is not the only component of the overall latency - the inference on the batch and the pre/post processing also have to occur.
3. Multiply the maximum throughput from step 1 by the `batch_interval` from step 2. The result is a number which you can assign to `max_batch_size`.
4. Run the load test again. If the inference fails with that batch size (e.g. due to running out of GPU or RAM memory), then reduce `max_batch_size` to a level that works (reduce `batch_interval` by the same factor).
5. Use the load test to determine the peak throughput of the API replica. Multiply the observed throughput by the `batch_interval` to calculate the average batch size. If the average batch size coincides with `max_batch_size`, then it might mean that the throughput could still be further increased by increasing `max_batch_size`. If it's lower, then it means that `batch_interval` is triggering the inference before `max_batch_size` requests have been aggregated. If modifying both `max_batch_size` and `batch_interval` doesn't improve the throughput, then the service may be bottlenecked by something else (e.g. CPU, network IO, `processes_per_replica`, `threads_per_process`, etc).


# Autoscaling

Cortex autoscales your web services on a per-API basis based on your configuration.

## Autoscaling replicas

**`min_replicas`**: The lower bound on how many replicas can be running for an API.

**`max_replicas`**: The upper bound on how many replicas can be running for an API.

**`target_replica_concurrency`** (default: `processes_per_replica` \* `threads_per_process`): This is the desired number of in-flight requests per replica, and is the metric which the autoscaler uses to make scaling decisions.

Replica concurrency is simply how many requests have been sent to a replica and have not yet been responded to (also referred to as in-flight requests). Therefore, it includes requests which are currently being processed and requests which are waiting in the replica's queue.

The autoscaler uses this formula to determine the number of desired replicas:

`desired replicas = sum(in-flight requests accross all replicas) / target_replica_concurrency`

For example, setting `target_replica_concurrency` to `processes_per_replica` \* `threads_per_process` (the default) causes the cluster to adjust the number of replicas so that on average, requests are immediately processed without waiting in a queue, and processes/threads are never idle.

**`max_replica_concurrency`** (default: 1024): This is the maximum number of in-flight requests per replica before requests are rejected with HTTP error code 503. `max_replica_concurrency` includes requests that are currently being processed as well as requests that are waiting in the replica's queue (a replica can actively process `processes_per_replica` \* `threads_per_process` requests concurrently, and will hold any additional requests in a local queue). Decreasing `max_replica_concurrency` and configuring the client to retry when it receives 503 responses will improve queue fairness accross replicas by preventing requests from sitting in long queues.

**`window`** (default: 60s): The time over which to average the API wide in-flight requests (which is the sum of in-flight requests in each replica). The longer the window, the slower the autoscaler will react to changes in API wide in-flight requests, since it is averaged over the `window`. API wide in-flight requests is calculated every 10 seconds, so `window` must be a multiple of 10 seconds.

**`downscale_stabilization_period`** (default: 5m): The API will not scale below the highest recommendation made during this period. Every 10 seconds, the autoscaler makes a recommendation based on all of the other configuration parameters described here. It will then take the max of the current recommendation and all recommendations made during the `downscale_stabilization_period`, and use that to determine the final number of replicas to scale to. Increasing this value will cause the cluster to react more slowly to decreased traffic, and will reduce thrashing.

**`upscale_stabilization_period`** (default: 1m): The API will not scale above the lowest recommendation made during this period. Every 10 seconds, the autoscaler makes a recommendation based on all of the other configuration parameters described here. It will then take the min of the current recommendation and all recommendations made during the `upscale_stabilization_period`, and use that to determine the final number of replicas to scale to. Increasing this value will cause the cluster to react more slowly to increased traffic, and will reduce thrashing.

**`max_downscale_factor`** (default: 0.75): The maximum factor by which to scale down the API on a single scaling event. For example, if `max_downscale_factor` is 0.5 and there are 10 running replicas, the autoscaler will not recommend fewer than 5 replicas. Increasing this number will allow the cluster to shrink more quickly in response to dramatic dips in traffic.

**`max_upscale_factor`** (default: 1.5): The maximum factor by which to scale up the API on a single scaling event. For example, if `max_upscale_factor` is 10 and there are 5 running replicas, the autoscaler will not recommend more than 50 replicas. Increasing this number will allow the cluster to grow more quickly in response to dramatic spikes in traffic.

**`downscale_tolerance`** (default: 0.05): Any recommendation falling within this factor below the current number of replicas will not trigger a scale down event. For example, if `downscale_tolerance` is 0.1 and there are 20 running replicas, a recommendation of 18 or 19 replicas will not be acted on, and the API will remain at 20 replicas. Increasing this value will prevent thrashing, but setting it too high will prevent the cluster from maintaining it's optimal size.

**`upscale_tolerance`** (default: 0.05): Any recommendation falling within this factor above the current number of replicas will not trigger a scale up event. For example, if `upscale_tolerance` is 0.1 and there are 20 running replicas, a recommendation of 21 or 22 replicas will not be acted on, and the API will remain at 20 replicas. Increasing this value will prevent thrashing, but setting it too high will prevent the cluster from maintaining it's optimal size.

## Autoscaling instances

Cortex spins up and down instances based on the aggregate resource requests of all APIs. The number of instances will be at least `min_instances` and no more than `max_instances` (configured during installation and modifiable via `cortex cluster configure`).

## Overprovisioning

The default value for `target_replica_concurrency` is `processes_per_replica` \* `threads_per_process`, which behaves well in many situations (see above for an explanation of how `target_replica_concurrency` affects autoscaling). However, if your application is sensitive to spikes in traffic or if creating new replicas takes too long (see below), you may find it helpful to maintain extra capacity to handle the increased traffic while new replicas are being created. This can be accomplished by setting `target_replica_concurrency` to a lower value relative to the expected replica's concurrency. The smaller `target_replica_concurrency` is, the more unused capacity your API will have, and the more room it will have to handle sudden increased load. The increased request rate will still trigger the autoscaler, and your API will stabilize again (maintaining the overprovisioned capacity).

For example, if you've determined that each replica in your API can handle 2 requests, you would set `target_replica_concurrency` to 2. In a scenario where your API is receiving 8 concurrent requests on average, the autoscaler would maintain 4 live replicas (8/2 = 4). If you wanted to overprovision by 25%, you can set `target_replica_concurrency` to 1.6 causing the autoscaler maintain 5 live replicas (8/1.6 = 5).

## Autoscaling responsiveness

Assuming that `window` and `upscale_stabilization_period` are set to their default values (1 minute), it could take up to 2 minutes of increased traffic before an extra replica is requested. As soon as the additional replica is requested, the replica request will be visible in the output of `cortex get`, but the replica won't yet be running. If an extra instance is required to schedule the newly requested replica, it could take a few minutes for AWS to provision the instance (depending on the instance type), plus a few minutes for the newly provisioned instance to download your api image and for the api to initialize (via its `__init__()` method).

Keep these delays in mind when considering overprovisioning (see above) and when determining appropriate values for `window` and `upscale_stabilization_period`. If you want the autoscaler to react as quickly as possible, set `upscale_stabilization_period` and `window` to their minimum values (0s and 10s respectively).

If it takes a long time to initialize your API replica (i.e. install dependencies and run your predictor's `__init__()` function), consider building your own API image to use instead of the default image. With this approach, you can pre-download/build/install any custom dependencies and bake them into the image.


# Statuses

| Status                | Meaning                                                                                                                                                                                              |
| --------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| live                  | API is deployed and ready to serve prediction requests (at least one replica is running)                                                                                                             |
| updating              | API is updating                                                                                                                                                                                      |
| error                 | API was not created due to an error; run `cortex logs <name>` to view the logs                                                                                                                       |
| error (image pull)    | API was not created because one of the specified Docker images was inaccessible at runtime; check that your API's docker images exist and are accessible via your cluster operator's AWS credentials |
| error (out of memory) | API was terminated due to excessive memory usage; try allocating more memory to the API and re-deploying                                                                                             |
| compute unavailable   | API could not start due to insufficient memory, CPU, GPU or Inf in the cluster; some replicas may be ready                                                                                           |


# Metrics

The `cortex get` and `cortex get API_NAME` commands display the request time (averaged over the past 2 weeks) and response code counts (summed over the past 2 weeks) for your APIs:

```bash
$ cortex get

env   api                         status   up-to-date   requested   last update   avg request   2XX
aws   iris-classifier             live     1            1           17m           24ms          1223
aws   text-generator              live     1            1           8m            180ms         433
aws   image-classifier-resnet50   live     2            2           1h            32ms          1121126
```

The `cortex get API_NAME` command also provides a link to a Grafana dashboard:

![dashboard](https://user-images.githubusercontent.com/7456627/107253455-9c6b7b80-6a36-11eb-8600-f36a7bab6d3b.png)

## Metrics in the dashboard

| Panel             | Description                                                                        | Note                                                                                               |
| ----------------- | ---------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------- |
| Request Rate      | Request rate, computed over every minute, of an API                                |                                                                                                    |
| In Flight Request | Active in-flight requests for an API.                                              | In-flight requests are recorded every 10 seconds, which will correspond to the minimum resolution. |
| Active Replicas   | Active replicas for an API                                                         |                                                                                                    |
| 2XX Responses     | Request rate, computed over a minute, for responses with status code 2XX of an API |                                                                                                    |
| 4XX Responses     | Request rate, computed over a minute, for responses with status code 4XX of an API |                                                                                                    |
| 5XX Responses     | Request rate, computed over a minute, for responses with status code 5XX of an API |                                                                                                    |
| p99 Latency       | 99th percentile latency, computed over a minute, for an API                        | Value might not be accurate because the histogram buckets are not dynamically set.                 |
| p90 Latency       | 90th percentile latency, computed over a minute, for an API                        | Value might not be accurate because the histogram buckets are not dynamically set.                 |
| p50 Latency       | 50th percentile latency, computed over a minute, for an API                        | Value might not be accurate because the histogram buckets are not dynamically set.                 |
| Average Latency   | Average latency, computed over a minute, for an API                                |                                                                                                    |

## Accessing the dashboard

The dashboard URL is displayed once you run a `cortex get <api_name>` command.

Alternatively, you can access it on `http://<operator_url>/dashboard`. Run the following command to get the operator URL:

```
cortex env list
```

### Default credentials

The dashboard is protected with username / password authentication, which by default are:

* Username: admin
* Password: admin

You will be prompted to change the admin user password in the first time you log in.

Grafana allows managing the access of several users and managing teams. For more information on this topic check the [grafana documentation](https://grafana.com/docs/grafana/latest/manage-users/).

### Selecting an API

You can select one or more APIs to visualize in the top left corner of the dashboard.

![](https://user-images.githubusercontent.com/7456627/107375721-57545180-6ae9-11eb-9474-ba58ad7eb0c5.png)

### Selecting a time range

Grafana allows you to select a time range on which the metrics will be visualized. You can do so in the top right corner of the dashboard.

![](https://user-images.githubusercontent.com/7456627/107376148-d9dd1100-6ae9-11eb-8c2b-c678b41ade01.png)

**Note: Cortex only retains a maximum of 2 weeks worth of data at any moment in time**

### Available dashboards

There are more than one dashboard available by default. You can view the available dashboards by accessing the Grafana menu: `Dashboards -> Manage -> Cortex folder`.

## Exposed metrics

Cortex exposes more metrics with Prometheus, that can be potentially useful. To check the available metrics, access the `Explore` menu in grafana and press the `Metrics` button.

![](https://user-images.githubusercontent.com/7456627/107377492-515f7000-6aeb-11eb-9b46-909120335060.png)

You can use any of these metrics to set up your own dashboards.


# Multi-model


# Example

Deploy several models in a single API to improve resource utilization efficiency.

## Define a multi-model API

```python
# multi_model.py

import cortex

class PythonPredictor:
    def __init__(self, config):
        from transformers import pipeline
        self.analyzer = pipeline(task="sentiment-analysis")

        import wget
        import fasttext
        wget.download(
            "https://dl.fbaipublicfiles.com/fasttext/supervised-models/lid.176.bin", "/tmp/model"
        )
        self.language_identifier = fasttext.load_model("/tmp/model")

    def predict(self, query_params, payload):
        model = query_params.get("model")
        if model == "sentiment":
            return self.analyzer(payload["text"])[0]
        elif model == "language":
            return self.language_identifier.predict(payload["text"])[0][0][-2:]

requirements = ["tensorflow", "transformers", "wget", "fasttext"]

api_spec = {"name": "multi-model", "kind": "RealtimeAPI"}

cx = cortex.client("aws")
cx.create_api(api_spec, predictor=PythonPredictor, requirements=requirements)
```

## Deploy

```bash
$ python multi_model.py
```


# Configuration

## `PythonPredictor`

### Specifying models in API configuration

#### `cortex.yaml`

The directory `s3://cortex-examples/sklearn/mpg-estimator/linreg/` contains 4 different versions of the model.

```yaml
- name: mpg-estimator
  kind: RealtimeAPI
  predictor:
    type: python
    path: predictor.py
    models:
      path: s3://cortex-examples/sklearn/mpg-estimator/linreg/
```

#### `predictor.py`

```python
import mlflow.sklearn
import numpy as np


class PythonPredictor:
    def __init__(self, config, python_client):
        self.client = python_client

    def load_model(self, model_path):
        return mlflow.sklearn.load_model(model_path)

    def predict(self, payload, query_params):
        model_version = query_params.get("version")

        # model_input = ...

        model = self.client.get_model(model_version=model_version)
        result = model.predict(model_input)

        return {"prediction": result, "model": {"version": model_version}}
```

### Without specifying models in API configuration

#### `cortex.yaml`

```yaml
- name: text-analyzer
  kind: RealtimeAPI
  predictor:
    type: python
    path: predictor.py
    ...
```

#### `predictor.py`

```python
class PythonPredictor:
    def __init__(self, config):
        self.analyzer = initialize_model("sentiment-analysis")
        self.summarizer = initialize_model("summarization")

    def predict(self, query_params, payload):
        model_name = query_params.get("model")
        model_input = payload["text"]

        # ...

        if model_name == "analyzer":
            results = self.analyzer(model_input)
            predicted_label = postprocess(results)
            return {"label": predicted_label}
        elif model_name == "summarizer":
            results = self.summarizer(model_input)
            predicted_label = postprocess(results)
            return {"label": predicted_label}
        else:
            return JSONResponse({"error": f"unknown model: {model_name}"}, status_code=400)
```

## `TensorFlowPredictor`

### `cortex.yaml`

```yaml
- name: multi-model-classifier
  kind: RealtimeAPI
  predictor:
    type: tensorflow
    path: predictor.py
    models:
      paths:
        - name: inception
          path: s3://cortex-examples/tensorflow/image-classifier/inception/
        - name: iris
          path: s3://cortex-examples/tensorflow/iris-classifier/nn/
        - name: resnet50
          path: s3://cortex-examples/tensorflow/resnet50/
      ...
```

### `predictor.py`

```python
class TensorFlowPredictor:
    def __init__(self, tensorflow_client, config):
        self.client = tensorflow_client

    def predict(self, payload, query_params):
        model_name = query_params["model"]
        model_input = preprocess(payload["url"])
        results = self.client.predict(model_input, model_name)
        predicted_label = postprocess(results)
        return {"label": predicted_label}
```

## `ONNXPredictor`

### `cortex.yaml`

```yaml
- name: multi-model-classifier
  kind: RealtimeAPI
  predictor:
    type: onnx
    path: predictor.py
    models:
      paths:
        - name: resnet50
          path: s3://cortex-examples/onnx/resnet50/
        - name: mobilenet
          path: s3://cortex-examples/onnx/mobilenet/
        - name: shufflenet
          path: s3://cortex-examples/onnx/shufflenet/
      ...
```

### `predictor.py`

```python
class ONNXPredictor:
    def __init__(self, onnx_client, config):
        self.client = onnx_client

    def predict(self, payload, query_params):
        model_name = query_params["model"]
        model_input = preprocess(payload["url"])
        results = self.client.predict(model_input, model_name)
        predicted_label = postprocess(results)
        return {"label": predicted_label}
```


# Caching

Multi-model caching allows each replica to serve more models than would fit into its memory by keeping a specified number of models in memory (and disk) at a time. When the in-memory model limit is reached, the least recently accessed model is evicted from the cache. This can be useful when you have many models, and some models are frequently accessed while a larger portion of them are rarely used, or when running on smaller instances to control costs.

The model cache is a two-layer cache, configured by the following parameters in the `predictor.models` configuration:

* `cache_size` sets the number of models to keep in memory
* `disk_cache_size` sets the number of models to keep on disk (must be greater than or equal to `cache_size`)

Both of these fields must be specified, in addition to either the `dir` or `paths` field (which specifies the model paths, see [models](https://docs.cortexlabs.com/workloads/realtime-apis/models) for documentation). Multi-model caching is only supported if `predictor.processes_per_replica` is set to 1 (the default value).

## Out of memory errors

Cortex runs a background process every 10 seconds that counts the number of models in memory and on disk, and evicts the least recently used models if the count exceeds `cache_size` / `disk_cache_size`. If many new models are requested between executions of the process, there may be more models in memory and/or on disk than the configured `cache_size` or `disk_cache_size` limits which could lead to out of memory errors.


# Traffic Splitter


# Example

Expose multiple RealtimeAPIs as a single endpoint for A/B tests, multi-armed bandits, or canary deployments.

## Deploy APIs

```python
import cortex

class PythonPredictor:
    def __init__(self, config):
        from transformers import pipeline
        self.model = pipeline(task="text-generation")

    def predict(self, payload):
        return self.model(payload["text"])[0]

requirements = ["tensorflow", "transformers"]

api_spec_cpu = {
    "name": "text-generator-cpu",
    "kind": "RealtimeAPI",
    "compute": {
        "cpu": 1,
    },
}

api_spec_gpu = {
    "name": "text-generator-gpu",
    "kind": "RealtimeAPI",
    "compute": {
        "gpu": 1,
    },
}

cx = cortex.client("aws")
cx.create_api(api_spec_cpu, predictor=PythonPredictor, requirements=requirements)
cx.create_api(api_spec_gpu, predictor=PythonPredictor, requirements=requirements)
```

## Deploy a traffic splitter

```python
traffic_splitter_spec = {
    "name": "text-generator",
    "kind": "TrafficSplitter",
    "apis": [
        {"name": "text-generator-cpu", "weight": 50},
        {"name": "text-generator-gpu", "weight": 50},
    ],
}

cx.create_api(traffic_splitter_spec)
```

## Update the weights of the traffic splitter

```python
traffic_splitter_spec = cx.get_api("text-generator")["spec"]["submitted_api_spec"]

# send 99% of the traffic to text-generator-gpu
traffic_splitter_spec["apis"][0]["weight"] = 1
traffic_splitter_spec["apis"][1]["weight"] = 99

cx.patch(traffic_splitter_spec)
```


# Configuration

```yaml
- name: <string>  # Traffic Splitter name (required)
  kind: TrafficSplitter
  networking:
    endpoint: <string>  # the endpoint for the Traffic Splitter (default: <name>)
  apis:  # list of Realtime APIs to target
    - name: <string>  # name of a Realtime API that is already running or is included in the same configuration file (required)
      weight: <int>   # percentage of traffic to route to the Realtime API (all weights must sum to 100) (required)
```


# Troubleshooting

## 404 or 503 error responses from API requests

When making prediction requests to your API, it's possible to get a `{"message":"Not Found"}` error message (with HTTP status code `404`), or a `no healthy upstream` error message (with HTTP status code `503`). This means that there are currently no live replicas running for your API. This could happen for a few reasons:

1. It's possible that your API is simply not ready yet. You can check the status of your API with `cortex get API_NAME`, and stream the logs with `cortex logs API_NAME`.
2. Your API may have errored during initialization or while responding to a previous request. `cortex get API_NAME` will show the status of your API, and you can view the logs with `cortex logs API_NAME`.

It is also possible to receive a `{"message":"Service Unavailable"}` error message (with HTTP status code `503`) if you are using API Gateway in front of your API endpoints and if your request exceeds API Gateway's 29 second timeout. If the request is exceeding the API Gateway timeout, your client should receive the `{"message":"Service Unavailable"}` response \~29 seconds after making the request. To confirm that this is the issue, you can modify your `predict()` function to immediately return a response (e.g. `return "ok"`), re-deploy your API, wait for the update to complete, and try making a request. If your client successfully receives the "ok" response, it is likely that the API Gateway timeout is occurring. You can either modify your `predict()` implementation to take less time, run on faster hardware (e.g. GPUs), or don't use API Gateway (there is no timeout when using the API's endpoint).

## API is stuck updating

If your API is stuck in the "updating" or "compute unavailable" state (which is displayed when running `cortex get`), there are a few possible causes. Here are some things to check:

### Check `cortex logs API_NAME`

If no logs appear (e.g. it just says "fetching logs..."), continue down this list.

### Check `max_instances` for your cluster

When you created your Cortex cluster, you configured `max_instances` (either from the command prompts or via a cluster configuration file, e.g. `cluster.yaml`). If your cluster already has `min_instances` running instances, additional instances cannot be created and APIs may not be able to deploy, scale, or update.

You can check the current value of `max_instances` by running `cortex cluster info` (or `cortex cluster info --config cluster.yaml` if you have a cluster configuration file).

You can update `max_instances` by running `cortex cluster configure` (or by modifying `max_instances` in your cluster configuration file and running `cortex cluster configure --config cluster.yaml`).

## Check your AWS auto scaling group activity history

In most cases when AWS is unable to provision additional instances, the reason will be logged in the auto scaling group's activity history.

Here is how you can check these logs:

1. Log in to the AWS console and go to the EC2 service page
2. Click "Auto Scaling Groups" on the bottom of the side panel on the left
3. Select one of the "worker" autoscaling groups for your cluster (there may be two)
4. Click the "Activity" tab at the bottom half of the screen (it may also be called "Activity History" depending on which AWS console UI you're using)
5. Scroll down (if necessary) and inspect the activity history, looking for any errors and their causes
6. Repeat steps 3-5 for the other worker autoscaling group (if applicable)

Here is how it looks on the new console UI:

![new ui](https://user-images.githubusercontent.com/808475/78153371-852d2c00-742a-11ea-9bde-dbad5c603f8f.png)

On the old UI:

![old ui](https://user-images.githubusercontent.com/808475/78153350-7e9eb480-742a-11ea-9221-1f6559db45fd.png)

The most common reason AWS is unable to provision instances is that you have reached your instance limit. There is an instance limit associated with your AWS account for each instance family in each region, for on-demand and for spot instances. You can check your current limit and request an increase [here](https://console.aws.amazon.com/servicequotas/home?#!/services/ec2/quotas) (set the region in the upper right corner to your desired region, type "on-demand" or "spot" in the search bar, and click on the quota that matches your instance type). Note that the quota values indicate the number of vCPUs available, not the number of instances; different instances have a different numbers of vCPUs, which can be seen [here](https://aws.amazon.com/ec2/instance-types).

If you are using spot instances and don't have `on_demand_backup` set to true, it is also possible that AWS has run out of spot instances for your requested instance type and region. You can enable `on_demand_backup` to allow Cortex to fall back to on-demand instances when spot instances are unavailable, or you can try adding additional alternative instance types in `instance_distribution`.

### Disabling rolling updates

By default, cortex performs rolling updates on all APIs. This is to ensure that traffic can continue to be served during updates, and that there is no downtime if there's an error in the new version. However, this can lead to APIs getting stuck in the "updating" state when the cluster is unable to increase its instance count (e.g. for one of the reasons above).

Here is an example: You set `max_instances` to 1, or your AWS account limits you to a single `g4dn.xlarge` instance (i.e. your G instance vCPU limit is 4). You have an API running which requested 1 GPU. When you update your API via `cortex deploy`, Cortex attempts to deploy the updated version, and will only take down the old version once the new one is running. In this case, since there is no GPU available on the single running instance (it's taken by the old version of your API), the new version of your API requests a new instance to run on. Normally this will be ok (it might just take a few minutes since a new instance has to spin up): the new instance will become live, the new API replica will run on it, once it starts up successfully the old replica will be terminated, and eventually the old instance will spin down. In this case, however, the new version gets stuck because the second instance cannot be created, and the first instance cannot be freed up until the new version is running.

If you're running in a development environment, this rolling update behavior can be undesirable.

You can disable rolling updates for your API in your API configuration (e.g. in `cortex.yaml`): set `max_surge` to 0 (in the `update_strategy` configuration). E.g.:

```yaml
- name: text-generator
  predictor:
    type: python
    ...
  update_strategy:
    max_surge: 0
```

## TensorFlow session

When doing inferences with TensorFlow using the Realtime API Python Predictor or Batch API Python Predictor, it should be noted that your Python Predictor's `__init__()` constructor is only called on one thread, whereas its `predict()` method can run on any of the available threads (which is configured via the `threads_per_process` field in the API's `predictor` configuration). If `threads_per_process` is set to `1` (the default value), then there is no concern, since `__init__()` and `predict()` will run on the same thread. However, if `threads_per_process` is greater than `1`, then only one of the inference threads will have executed the `__init__()` function. This can cause issues with TensorFlow because the default graph is a property of the current thread, so if `__init__()` initializes the TensorFlow graph, only the thread that executed `__init__()` will have the default graph set.

The error you may see if the default graph is not set (as a consequence of `__init__()` and `predict()` running in separate threads) is:

```
TypeError: Cannot interpret feed_dict key as Tensor: Tensor Tensor("Placeholder:0", shape=(1, ?), dtype=int32) is not an element of this graph.
```

To avoid this error, you can set the default graph before running the prediction in the `predict()` method:

```python
def predict(self, payload):
    with self.sess.graph.as_default():
        # perform your inference here
```


# Batch APIs


# Example

Create APIs that can orchestrate distributed batch inference jobs on large datasets.

## Implement

```bash
$ mkdir image-classifier && cd image-classifier
$ touch predictor.py requirements.txt image_classifier.yaml
```

```python
# predictor.py

class PythonPredictor:
    def __init__(self, config, job_spec):
        from torchvision import transforms
        import torchvision
        import requests
        import boto3
        import re

        self.model = torchvision.models.alexnet(pretrained=True).eval()
        self.labels = requests.get(config["labels"]).text.split("\n")[1:]

        normalize = transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225])
        self.preprocess = transforms.Compose(
            [transforms.Resize(256), transforms.CenterCrop(224), transforms.ToTensor(), normalize]
        )

        self.s3 = boto3.client("s3")  # initialize S3 client to save results
        self.bucket, self.key = re.match("s3://(.+?)/(.+)", config["dest_s3_dir"]).groups()
        self.key = os.path.join(self.key, job_spec["job_id"])

    def predict(self, payload, batch_id):
        import json
        import torch
        from PIL import Image
        from io import BytesIO
        import requests

        tensor_list = []
        for image_url in payload:  # download and preprocess each image
            img_pil = Image.open(BytesIO(requests.get(image_url).content))
            tensor_list.append(self.preprocess(img_pil))

        img_tensor = torch.stack(tensor_list)
        with torch.no_grad():  # classify the batch of images
            prediction = self.model(img_tensor)
        _, indices = prediction.max(1)

        results = [{"url": payload[i], "class": self.labels[class_idx]} for i, class_idx in enumerate(indices)]
        self.s3.put_object(Bucket=self.bucket, Key=f"{self.key}/{batch_id}.json", Body=json.dumps(results))
```

```python
# requirements.txt

torch
boto3
pillow
torchvision
requests
```

```yaml
# image_classifier.yaml

- name: image-classifier
  kind: BatchAPI
  predictor:
    type: python
    path: predictor.py
    config:
      labels: "https://storage.googleapis.com/download.tensorflow.org/data/ImageNetLabels.txt"
```

## Deploy

```bash
$ cortex deploy image_classifier.yaml
```

## Describe

```bash
$ cortex get image-classifier
```

## Submit a job

```python
import cortex
import requests

cx = cortex.client("aws")
batch_endpoint = cx.get_api("image-classifier")["endpoint"]

dest_s3_dir = # specify S3 directory for the results, e.g. "s3://my-bucket/dir" or "gs://my-bucket/dir" (make sure your cluster has access to this bucket)

job_spec = {
    "workers": 1,
    "item_list": {
        "items": [
            "https://i.imgur.com/PzXprwl.jpg",
            "https://i.imgur.com/E4cOSLw.jpg",
            "https://i.imgur.com/jDimNTZ.jpg",
            "https://i.imgur.com/WqeovVj.jpg"
        ],
        "batch_size": 2
    },
    "config": {
        "dest_s3_dir": dest_s3_dir
    }
}

response = requests.post(batch_endpoint, json=job_spec)
print(response.text)
# > {"job_id":"69b183ed6bdf3e9b","api_name":"image-classifier", "config": {"dest_s3_dir": ...}}
```

## Monitor the job

```bash
$ cortex get image-classifier 69b183ed6bdf3e9b
```

## Stream logs

```bash
$ cortex logs image-classifier 69b183ed6bdf3e9b
```

## View the results

Once the job is complete, you should be able to find the results in the directory you've specified.

## Delete

```bash
$ cortex delete image-classifier
```


# Predictor

Which Predictor you use depends on how your model is exported:

* [TensorFlow Predictor](#tensorflow-predictor) if your model is exported as a TensorFlow `SavedModel`
* [ONNX Predictor](#onnx-predictor) if your model is exported in the ONNX format
* [Python Predictor](#python-predictor) for all other cases

## Project files

Cortex makes all files in the project directory (i.e. the directory which contains `cortex.yaml`) available for use in your Predictor implementation. Python bytecode files (`*.pyc`, `*.pyo`, `*.pyd`), files or folders that start with `.`, and the api configuration file (e.g. `cortex.yaml`) are excluded.

The following files can also be added at the root of the project's directory:

* `.cortexignore` file, which follows the same syntax and behavior as a [.gitignore file](https://git-scm.com/docs/gitignore).
* `.env` file, which exports environment variables that can be used in the predictor. Each line of this file must follow the `VARIABLE=value` format.

For example, if your directory looks like this:

```
./my-classifier/
├── cortex.yaml
├── values.json
├── predictor.py
├── ...
└── requirements.txt
```

You can access `values.json` in your Predictor like this:

```python
import json

class PythonPredictor:
    def __init__(self, config):
        with open('values.json', 'r') as values_file:
            values = json.load(values_file)
        self.values = values
```

## Python Predictor

### Interface

```python
# initialization code and variables can be declared here in global scope

class PythonPredictor:
    def __init__(self, config, job_spec):
        """(Required) Called once during each worker initialization. Performs
        setup such as downloading/initializing the model or downloading a
        vocabulary.

        Args:
            config (required): Dictionary passed from API configuration (if
                specified) merged with configuration passed in with Job
                Submission API. If there are conflicting keys, values in
                configuration specified in Job submission takes precedence.
            job_spec (optional): Dictionary containing the following fields:
                "job_id": A unique ID for this job
                "api_name": The name of this batch API
                "config": The config that was provided in the job submission
                "workers": The number of workers for this job
                "total_batch_count": The total number of batches in this job
                "start_time": The time that this job started
        """
        pass

    def predict(self, payload, batch_id):
        """(Required) Called once per batch. Preprocesses the batch payload (if
        necessary), runs inference, postprocesses the inference output (if
        necessary), and writes the predictions to storage (i.e. S3 or a
        database, if desired).

        Args:
            payload (required): a batch (i.e. a list of one or more samples).
            batch_id (optional): uuid assigned to this batch.
        Returns:
            Nothing
        """
        pass

    def on_job_complete(self):
        """(Optional) Called once after all batches in the job have been
        processed. Performs post job completion tasks such as aggregating
        results, executing web hooks, or triggering other jobs.
        """
        pass
```

## TensorFlow Predictor

**Uses TensorFlow version 2.3.0 by default**

### Interface

```python
class TensorFlowPredictor:
    def __init__(self, tensorflow_client, config, job_spec):
        """(Required) Called once during each worker initialization. Performs
        setup such as downloading/initializing the model or downloading a
        vocabulary.

        Args:
            tensorflow_client (required): TensorFlow client which is used to
                make predictions. This should be saved for use in predict().
            config (required): Dictionary passed from API configuration (if
                specified) merged with configuration passed in with Job
                Submission API. If there are conflicting keys, values in
                configuration specified in Job submission takes precedence.
            job_spec (optional): Dictionary containing the following fields:
                "job_id": A unique ID for this job
                "api_name": The name of this batch API
                "config": The config that was provided in the job submission
                "workers": The number of workers for this job
                "total_batch_count": The total number of batches in this job
                "start_time": The time that this job started
        """
        self.client = tensorflow_client
        # Additional initialization may be done here

    def predict(self, payload, batch_id):
        """(Required) Called once per batch. Preprocesses the batch payload (if
        necessary), runs inference (e.g. by calling
        self.client.predict(model_input)), postprocesses the inference output
        (if necessary), and writes the predictions to storage (i.e. S3 or a
        database, if desired).

        Args:
            payload (required): a batch (i.e. a list of one or more samples).
            batch_id (optional): uuid assigned to this batch.
        Returns:
            Nothing
        """
        pass

    def on_job_complete(self):
        """(Optional) Called once after all batches in the job have been
        processed. Performs post job completion tasks such as aggregating
        results, executing web hooks, or triggering other jobs.
        """
        pass
```

Cortex provides a `tensorflow_client` to your Predictor's constructor. `tensorflow_client` is an instance of [TensorFlowClient](https://github.com/cortexlabs/cortex/tree/0.29/pkg/cortex/serve/cortex_internal/lib/client/tensorflow.py) that manages a connection to a TensorFlow Serving container to make predictions using your model. It should be saved as an instance variable in your Predictor, and your `predict()` function should call `tensorflow_client.predict()` to make an inference with your exported TensorFlow model. Preprocessing of the JSON payload and postprocessing of predictions can be implemented in your `predict()` function as well.

When multiple models are defined using the Predictor's `models` field, the `tensorflow_client.predict()` method expects a second argument `model_name` which must hold the name of the model that you want to use for inference (for example: `self.client.predict(payload, "text-generator")`).

If you need to share files between your predictor implementation and the TensorFlow Serving container, you can create a new directory within `/mnt` (e.g. `/mnt/user`) and write files to it. The entire `/mnt` directory is shared between containers, but do not write to any of the directories in `/mnt` that already exist (they are used internally by Cortex).

## ONNX Predictor

**Uses ONNX Runtime version 1.6.0 by default**

### Interface

```python
class ONNXPredictor:
    def __init__(self, onnx_client, config, job_spec):
        """(Required) Called once during each worker initialization. Performs
        setup such as downloading/initializing the model or downloading a
        vocabulary.

        Args:
            onnx_client (required): ONNX client which is used to make
                predictions. This should be saved for use in predict().
            config (required): Dictionary passed from API configuration (if
                specified) merged with configuration passed in with Job
                Submission API. If there are conflicting keys, values in
                configuration specified in Job submission takes precedence.
            job_spec (optional): Dictionary containing the following fields:
                "job_id": A unique ID for this job
                "api_name": The name of this batch API
                "config": The config that was provided in the job submission
                "workers": The number of workers for this job
                "total_batch_count": The total number of batches in this job
                "start_time": The time that this job started
        """
        self.client = onnx_client
        # Additional initialization may be done here

    def predict(self, payload, batch_id):
        """(Required) Called once per batch. Preprocesses the batch payload (if
        necessary), runs inference (e.g. by calling
        self.client.predict(model_input)), postprocesses the inference output
        (if necessary), and writes the predictions to storage (i.e. S3 or a
        database, if desired).

        Args:
            payload (required): a batch (i.e. a list of one or more samples).
            batch_id (optional): uuid assigned to this batch.
        Returns:
            Nothing
        """
        pass

    def on_job_complete(self):
        """(Optional) Called once after all batches in the job have been
        processed. Performs post job completion tasks such as aggregating
        results, executing web hooks, or triggering other jobs.
        """
        pass
```

Cortex provides an `onnx_client` to your Predictor's constructor. `onnx_client` is an instance of [ONNXClient](https://github.com/cortexlabs/cortex/tree/0.29/pkg/cortex/serve/cortex_internal/lib/client/onnx.py) that manages an ONNX Runtime session to make predictions using your model. It should be saved as an instance variable in your Predictor, and your `predict()` function should call `onnx_client.predict()` to make an inference with your exported ONNX model. Preprocessing of the JSON payload and postprocessing of predictions can be implemented in your `predict()` function as well.

When multiple models are defined using the Predictor's `models` field, the `onnx_client.predict()` method expects a second argument `model_name` which must hold the name of the model that you want to use for inference (for example: `self.client.predict(model_input, "text-generator")`).

## Structured logging

You can use Cortex's logger in your predictor implemention to log in JSON. This will enrich your logs with Cortex's metadata, and you can add custom metadata to the logs by adding key value pairs to the `extra` key when using the logger. For example:

```python
...
from cortex_internal.lib.log import logger as cortex_logger

class PythonPredictor:
    def predict(self, payload, batch_id):
        cortex_logger.info("completed processing batch", extra={"batch_id": batch_id, "confidence": confidence})
```

The dictionary passed in via the `extra` will be flattened by one level. e.g.

```
{"asctime": "2021-01-19 15:14:05,291", "levelname": "INFO", "message": "completed processing batch", "process": 235, "batch_id": "iuasyd8f7", "confidence": 0.97}
```

To avoid overriding essential Cortex metadata, please refrain from specifying the following extra keys: `asctime`, `levelname`, `message`, `labels`, and `process`. Log lines greater than 5 MB in size will be ignored.


# Configuration

```yaml
- name: <string>
  kind: BatchAPI
  predictor: # detailed configuration below
  compute: # detailed configuration below
  networking: # detailed configuration below
```

## Predictor

### Python Predictor

```yaml
predictor:
  type: python
  path: <string>  # path to a python file with a PythonPredictor class definition, relative to the Cortex root (required)
  config: <string: value>  # arbitrary dictionary passed to the constructor of the Predictor (can be overridden by config passed in job submission) (optional)
  python_path: <string>  # path to the root of your Python folder that will be appended to PYTHONPATH (default: folder containing cortex.yaml)
  image: <string> # docker image to use for the Predictor (default: quay.io/cortexlabs/python-predictor-cpu:0.29.0 or quay.io/cortexlabs/python-predictor-gpu:0.29.0-cuda10.2-cudnn8 based on compute)
  env: <string: string>  # dictionary of environment variables
  log_level: <string>  # log level that can be "debug", "info", "warning" or "error" (default: "info")
  shm_size: <string>  # size of shared memory (/dev/shm) for sharing data between multiple processes, e.g. 64Mi or 1Gi (default: Null)
```

### TensorFlow Predictor

```yaml
predictor:
  type: tensorflow
  path: <string>  # path to a python file with a TensorFlowPredictor class definition, relative to the Cortex root (required)
  models:  # use this to serve a single model or multiple ones
    path: <string>  # S3 path to an exported model (e.g. s3://my-bucket/exported_model) (either this or 'paths' field must be provided)
    paths:  # (either this or 'path' must be provided)
      - name: <string> # unique name for the model (e.g. text-generator) (required)
        path: <string>  # S3 path to an exported model (e.g. s3://my-bucket/exported_model) (required)
        signature_key: <string>  # name of the signature def to use for prediction (required if your model has more than one signature def)
      ...
    signature_key: <string>  # name of the signature def to use for prediction (required if your model has more than one signature def)
  server_side_batching:  # (optional)
    max_batch_size: <int>  # the maximum number of requests to aggregate before running inference
    batch_interval: <duration>  # the maximum amount of time to spend waiting for additional requests before running inference on the batch of requests
  config: <string: value>  # arbitrary dictionary passed to the constructor of the Predictor (can be overridden by config passed in job submission) (optional)
  python_path: <string>  # path to the root of your Python folder that will be appended to PYTHONPATH (default: folder containing cortex.yaml)
  image: <string> # docker image to use for the Predictor (default: quay.io/cortexlabs/tensorflow-predictor:0.29.0)
  tensorflow_serving_image: <string> # docker image to use for the TensorFlow Serving container (default: quay.io/cortexlabs/tensorflow-serving-cpu:0.29.0 or quay.io/cortexlabs/tensorflow-serving-gpu:0.29.0 based on compute)
  env: <string: string>  # dictionary of environment variables
  log_level: <string>  # log level that can be "debug", "info", "warning" or "error" (default: "info")
  shm_size: <string>  # size of shared memory (/dev/shm) for sharing data between multiple processes, e.g. 64Mi or 1Gi (default: Null)
```

### ONNX Predictor

```yaml
predictor:
  type: onnx
  path: <string>  # path to a python file with an ONNXPredictor class definition, relative to the Cortex root (required)
  models:  # use this to serve a single model or multiple ones
    path: <string>  # S3 path to an exported model (e.g. s3://my-bucket/exported_model) (either this or 'paths' must be provided)
    paths:  # (either this or 'path' must be provided)
      - name: <string> # unique name for the model (e.g. text-generator) (required)
        path: <string>  # S3 path to an exported model (e.g. s3://my-bucket/exported_model.onnx) (required)
      ...
  config: <string: value>  # arbitrary dictionary passed to the constructor of the Predictor (can be overridden by config passed in job submission) (optional)
  python_path: <string>  # path to the root of your Python folder that will be appended to PYTHONPATH (default: folder containing cortex.yaml)
  image: <string> # docker image to use for the Predictor (default: quay.io/cortexlabs/onnx-predictor-cpu:0.29.0 or quay.io/cortexlabs/onnx-predictor-gpu:0.29.0 based on compute)
  env: <string: string>  # dictionary of environment variables
  log_level: <string>  # log level that can be "debug", "info", "warning" or "error" (default: "info")
  shm_size: <string>  # size of shared memory (/dev/shm) for sharing data between multiple processes, e.g. 64Mi or 1Gi (default: Null)
```

## Compute

```yaml
compute:
  cpu: <string | int | float>  # CPU request per worker. One unit of CPU corresponds to one virtual CPU; fractional requests are allowed, and can be specified as a floating point number or via the "m" suffix (default: 200m)
  gpu: <int>  # GPU request per worker. One unit of GPU corresponds to one virtual GPU (default: 0)
  mem: <string>  # memory request per worker. One unit of memory is one byte and can be expressed as an integer or by using one of these suffixes: K, M, G, T (or their power-of two counterparts: Ki, Mi, Gi, Ti) (default: Null)
```

## Networking

```yaml
networking:
  endpoint: <string>  # the endpoint for the API (default: <api_name>)
```


# Jobs

## Get the TaskAPI endpoint

```bash
$ cortex get <batch_api_name>
```

## Submit a Job

There are three options for providing the dataset for your job:

1. [Data in the request](#data-in-the-request)
2. [List S3 file paths](#s3-file-paths)
3. [Newline delimited JSON file(s) in S3](#newline-delimited-json-files-in-s3)

### Data in the request

The input data for your job can be included directly in your job submission request by specifying an `item_list` in your json request payload. Each item can be any type (object, list, string, etc.) and is treated as a single sample. `item_list.batch_size` specifies how many items to include in a single batch.

**Each batch must be smaller than 256 KiB, and the total request size must be less than 10 MiB.** If you want to submit more data, explore the other job submission methods.

Submitting data in the request can be useful in the following scenarios:

* the request only has a few items
* each item in the request is small (e.g. urls to images/videos)
* you want to avoid using S3 as an intermediate storage layer

```yaml
POST <batch_api_endpoint>:
{
    "workers": <int>,         # the number of workers to allocate for this job (required)
    "timeout": <int>,         # duration in seconds since the submission of a job before it is terminated (optional)
    "sqs_dead_letter_queue": {      # specify a queue to redirect failed batches (optional)
        "arn": <string>,            # arn of dead letter queue e.g. arn:aws:sqs:us-west-2:123456789:failed.fifo
        "max_receive_count": <int>  # number of a times a batch is allowed to be handled by a worker before it is considered to be failed and transferred to the dead letter queue (must be >= 1)
    },
    "item_list": {
        "items": [            # a list items that can be of any type (required)
            <any>,
            <any>
        ],
        "batch_size": <int>,  # the number of items per batch (the predict() function is called once per batch) (required)
    }
    "config": {               # custom fields for this specific job (will override values in `config` specified in your api configuration) (optional)
        "string": <any>
    }
}

RESPONSE:
{
    "job_id": <string>,
    "api_name": <string>,
    "kind": "BatchAPI",
    "workers": <int>,
    "config": {<string>: <any>},
    "api_id": <string>,
    "sqs_url": <string>,
    "timeout": <int>,
    "sqs_dead_letter_queue": {
        "arn": <string>,
        "max_receive_count": <int>
    },
    "created_time": <string>
}
```

### S3 file paths

If your input data is a list of files such as images/videos in an S3 directory, you can define `file_path_lister` in your submission request payload. You can use `file_path_lister.s3_paths` to specify a list of files or prefixes, and `file_path_lister.includes` and/or `file_path_lister.excludes` to remove unwanted files. The S3 file paths will be aggregated into batches of size `file_path_lister.batch_size`. To learn more about fine-grained S3 file filtering see [filtering files](#filtering-files).

**The total size of a batch must be less than 256 KiB.**

This submission pattern can be useful in the following scenarios:

* you have a list of images/videos in an S3 directory
* each S3 file represents a single sample or a small number of samples

If a single S3 file contains a lot of samples/rows, try the next submission strategy.

```yaml
POST <batch_api_endpoint>:
{
    "workers": <int>,            # the number of workers to allocate for this job (required)
    "timeout": <int>,            # duration in seconds since the submission of a job before it is terminated (optional)
    "sqs_dead_letter_queue": {      # specify a queue to redirect failed batches (optional)
        "arn": <string>,            # arn of dead letter queue e.g. arn:aws:sqs:us-west-2:123456789:failed.fifo
        "max_receive_count": <int>  # number of a times a batch is allowed to be handled by a worker before it is considered to be failed and transferred to the dead letter queue (must be >= 1)
    },
    "file_path_lister": {
        "s3_paths": [<string>],  # can be S3 prefixes or complete S3 paths (required)
        "includes": [<string>],  # glob patterns (optional)
        "excludes": [<string>],  # glob patterns (optional)
        "batch_size": <int>,     # the number of S3 file paths per batch (the predict() function is called once per batch) (required)
    }
    "config": {                  # custom fields for this specific job (will override values in `config` specified in your api configuration) (optional)
        "string": <any>
    }
}

RESPONSE:
{
    "job_id": <string>,
    "api_name": <string>,
    "kind": "BatchAPI",
    "workers": <int>,
    "config": {<string>: <any>},
    "api_id": <string>,
    "sqs_url": <string>,
    "timeout": <int>,
    "sqs_dead_letter_queue": {
        "arn": <string>,
        "max_receive_count": <int>
    },
    "created_time": <string>
}
```

### Newline delimited JSON files in S3

If your input dataset is a newline delimited json file in an S3 directory (or a list of them), you can define `delimited_files` in your request payload to break up the contents of the file into batches of size `delimited_files.batch_size`.

Upon receiving `delimited_files`, your Batch API will iterate through the `delimited_files.s3_paths` to generate the set of S3 files to process. You can use `delimited_files.includes` and `delimited_files.excludes` to filter out unwanted files. Each S3 file will be parsed as a newline delimited JSON file. Each line in the file should be a JSON object, which will be treated as a single sample. The S3 file will be broken down into batches of size `delimited_files.batch_size` and submitted to your workers. To learn more about fine-grained S3 file filtering see [filtering files](#filtering-files).

**The total size of a batch must be less than 256 KiB.**

This submission pattern is useful in the following scenarios:

* one or more S3 files contains a large number of samples and must be broken down into batches

```yaml
POST <batch_api_endpoint>:
{
    "workers": <int>,            # the number of workers to allocate for this job (required)
    "timeout": <int>,            # duration in seconds since the submission of a job before it is terminated (optional)
    "sqs_dead_letter_queue": {      # specify a queue to redirect failed batches (optional)
        "arn": <string>,            # arn of dead letter queue e.g. arn:aws:sqs:us-west-2:123456789:failed.fifo
        "max_receive_count": <int>  # number of a times a batch is allowed to be handled by a worker before it is considered to be failed and transferred to the dead letter queue (must be >= 1)
    },
    "delimited_files": {
        "s3_paths": [<string>],  # can be S3 prefixes or complete S3 paths (required)
        "includes": [<string>],  # glob patterns (optional)
        "excludes": [<string>],  # glob patterns (optional)
        "batch_size": <int>,     # the number of json objects per batch (the predict() function is called once per batch) (required)
    }
    "config": {                  # custom fields for this specific job (will override values in `config` specified in your api configuration) (optional)
        "string": <any>
    }
}

RESPONSE:
{
    "job_id": <string>,
    "api_name": <string>,
    "kind": "BatchAPI",
    "workers": <int>,
    "config": {<string>: <any>},
    "api_id": <string>,
    "sqs_url": <string>,
    "timeout": <int>,
    "sqs_dead_letter_queue": {
        "arn": <string>,
        "max_receive_count": <int>
    },
    "created_time": <string>
}
```

## Get a job's status

```bash
$ cortex get <batch_api_name> <job_id>
```

Or make a GET request to `<batch_api_endpoint>?jobID=<jobID>`:

```yaml
GET <batch_api_endpoint>?jobID=<jobID>:

RESPONSE:
{
    "job_status": {
        "job_id": <string>,
        "api_name": <string>,
        "kind": "BatchAPI",
        "workers": <int>,
        "config": {<string>: <any>},
        "api_id": <string>,
        "sqs_url": <string>,
        "status": <string>,
        "batches_in_queue": <int>        # number of batches remaining in the queue
        "batch_metrics": {
            "succeeded": <int>           # number of succeeded batches
            "failed": int                # number of failed attempts
            "avg_time_per_batch": <float> (optional)  # average time spent working on a batch (only considers successful attempts)
        },
        "worker_counts": {               # worker counts are only available while a job is running
            "pending": <int>,            # number of workers that are waiting for compute resources to be provisioned
            "initializing": <int>,       # number of workers that are initializing (downloading images or running your predictor's init function)
            "running": <int>,            # number of workers that are actively working on batches from the queue
            "succeeded": <int>,          # number of workers that have completed after verifying that the queue is empty
            "failed": <int>,             # number of workers that have failed
            "stalled": <int>,            # number of workers that have been stuck in pending for more than 10 minutes
        },
        "created_time": <string>
        "start_time": <string>
        "end_time": <string> (optional)
    },
    "endpoint": <string>
    "api_spec": {
        ...
    }
}
```

## Stop a job

```bash
$ cortex delete <batch_api_name> <job_id>
```

Or make a DELETE request to `<batch_api_endpoint>?jobID=<jobID>`:

```yaml
DELETE <batch_api_endpoint>?jobID=<jobID>:

RESPONSE:
{"message":"stopped job <job_id>"}
```

## Additional Information

### Filtering files

When submitting a job using `delimited_files` or `file_path_lister`, you can use `s3_paths` in conjunction with `includes` and `excludes` to precisely filter files.

The Batch API will iterate through each S3 path in `s3_paths`. If the S3 path is a prefix, it iterates through each file in that prefix. For each file, if `includes` is non-empty, it will discard the S3 path if the S3 file doesn't match any of the glob patterns provided in `includes`. After passing the `includes` filter (if specified), if the `excludes` is non-empty, it will discard the S3 path if the S3 files matches any of the glob patterns provided in `excludes`.

If you aren't sure which files will be processed in your request, specify the `dryRun=true` query parameter in the job submission request to see the target list.

Here are a few examples of filtering for a folder structure like this:

```
├── s3://bucket
    └── images
        ├── img_1.png
        ├── img_2.jpg
        ├── img_3.jpg
        └── img_4.gif
```

Select all files

```yaml
{
    "s3_paths": ["s3://bucket/images/"]
}

# or

{
    "s3_paths": ["s3://bucket/images/img"]
}

# Would select the following files:
# s3://bucket/images/img_1.png
# s3://bucket/images/img_2.jpg
# s3://bucket/images/img_3.jpg
# s3://bucket/images/img_4.gif
```

Select specific files

```yaml
{
    "s3_paths": [
        "s3://bucket/images/img_1.png",
        "s3://bucket/images/img_2.jpg"
    ]
}

# Would select the following files:
# s3://bucket/images/img_1.png
# s3://bucket/images/img_2.jpg
```

Only select JPG files

```yaml
{
    "s3_paths": ["s3://bucket/images/"],
    "includes": ["**.jpg"]
}

# Would select the following files:
# s3://bucket/images/img_2.jpg
# s3://bucket/images/img_3.jpg
```

Select all JPG files except one specific JPG file

```yaml
{
    "s3_paths": ["s3://bucket/images/"],
    "includes": ["**.jpg"],
    "excludes": ["**_3.jpg"]
}

# Would select the file:
# s3://bucket/images/img_2.jpg
```

Select all files except GIFs

```yaml
{
    "s3_paths": ["s3://bucket/images/"],
    "excludes": ["**.gif"]
}

# Would select the files:
# s3://bucket/images/img_1.png
# s3://bucket/images/img_2.jpg
# s3://bucket/images/img_3.jpg
```


# Statuses

| Status                  | Meaning                                                                                                                                                |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ |
| enqueuing               | Job is being split into batches and placed into a queue                                                                                                |
| running                 | Workers are retrieving batches from the queue and running inference                                                                                    |
| succeeded               | Workers completed all items in the queue without any failures                                                                                          |
| failed while enqueuing  | Failure occurred while enqueuing; check job logs for more details                                                                                      |
| completed with failures | Workers completed all items in the queue but some of the batches weren't processed successfully and raised exceptions; check job logs for more details |
| worker error            | One or more workers experienced an irrecoverable error, causing the job to fail; check job logs for more details                                       |
| out of memory           | One or more workers ran out of memory, causing the job to fail; check job logs for more details                                                        |
| timed out               | Job was terminated after the specified timeout has elapsed                                                                                             |
| stopped                 | Job was stopped by the user or the Batch API was deleted                                                                                               |


# Task APIs


# Example

Create APIs that can perform arbitrary tasks like training or fine-tuning a model.

## Implement

```python
# train_iris.py

import os
import boto3
import pickle
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


class Task:
    def __call__(self, config):
        # get the iris flower dataset
        iris = load_iris()
        data, labels = iris.data, iris.target
        training_data, test_data, training_labels, test_labels = train_test_split(data, labels)
        print("loaded dataset")

        # train the model
        model = LogisticRegression(solver="lbfgs", multi_class="multinomial", max_iter=1000)
        model.fit(training_data, training_labels)
        accuracy = model.score(test_data, test_labels)
        print("model trained; accuracy: {:.2f}".format(accuracy))

        # upload the model
        dest_dir = config["dest_s3_dir"]
        bucket, key = dest_dir.replace("s3://", "").split("/", 1)
        pickle.dump(model, open("model.pkl", "wb"))
        s3 = boto3.client("s3")
        s3.upload_file("model.pkl", bucket, os.path.join(key, "model.pkl"))
        print(f"model uploaded to {dest_dir}/model.pkl")
```

```python
# requirements.txt

boto3
scikit-learn==0.23.2
```

```yaml
# cortex.yaml

- name: train-iris
  kind: TaskAPI
  definition:
    path: train_iris.py
```

## Deploy

```bash
$ cortex deploy
```

## Describe

```bash
$ cortex get train-iris

# > endpoint: http://***.elb.us-west-2.amazonaws.com/train-iris
```

## Submit a job

You can submit a job by making a POST request to the Task API's endpoint.

Using `curl`:

```bash
$ export TASK_API_ENDPOINT=<TASK_API_ENDPOINT>  # e.g. export TASK_API_ENDPOINT=https://***.elb.us-west-2.amazonaws.com/train-iris
$ export DEST_S3_DIR=<YOUR_S3_DIRECTORY>  # e.g. export DEST_S3_DIR=s3://my-bucket/dir

$ curl $TASK_API_ENDPOINT \
    -X POST -H "Content-Type: application/json" \
    -d "{\"config\": {\"dest_s3_dir\": \"$DEST_S3_DIR\"}}"
# > {"job_id":"69b183ed6bdf3e9b","api_name":"train-iris",...}
```

Or, using Python `requests`:

```python
import cortex
import requests

cx = cortex.client("aws")  # "aws" is the name of the Cortex environment used in this example
task_endpoint = cx.get_api("train-iris")["endpoint"]

dest_s3_dir =  # S3 directory where the model will be uploaded, e.g. "s3://my-bucket/dir"
job_spec = {
    "config": {
        "dest_s3_dir": dest_s3_dir
    }
}
response = requests.post(task_endpoint, json=job_spec)
print(response.text)
# > {"job_id":"69b183ed6bdf3e9b","api_name":"train-iris",...}
```

## Monitor the job

```bash
$ cortex get train-iris 69b183ed6bdf3e9b
```

## View the results

Once the job is complete, you should be able to find the trained model in the directory you've specified.

## Delete

```bash
$ cortex delete train-iris
```


# Definition

## Project files

Cortex makes all files in the project directory (i.e. the directory which contains `cortex.yaml`) available for use in your Task implementation. Python bytecode files (`*.pyc`, `*.pyo`, `*.pyd`), files or folders that start with `.`, and the api configuration file (e.g. `cortex.yaml`) are excluded.

The following files can also be added at the root of the project's directory:

* `.cortexignore` file, which follows the same syntax and behavior as a [.gitignore file](https://git-scm.com/docs/gitignore).
* `.env` file, which exports environment variables that can be used in the task. Each line of this file must follow the `VARIABLE=value` format.

For example, if your directory looks like this:

```
./my-classifier/
├── cortex.yaml
├── values.json
├── task.py
├── ...
└── requirements.txt
```

You can access `values.json` in your Task like this:

```python
import json

class Task:
    def __call__(self, config):
        with open('values.json', 'r') as values_file:
            values = json.load(values_file)
        self.values = values
```

## Task

### Interface

```python
# initialization code and variables can be declared here in global scope

class Task:
    def __call__(self, config):
        """(Required) Task runnable.

        Args:
            config (required): Dictionary passed from API configuration (if
                specified) merged with configuration passed in with Job
                Submission API. If there are conflicting keys, values in
                configuration specified in Job submission takes precedence.
        """
        pass
```

## Structured logging

You can use Cortex's logger in your predictor implementation to log in JSON. This will enrich your logs with Cortex's metadata, and you can add custom metadata to the logs by adding key value pairs to the `extra` key when using the logger. For example:

```python
...
from cortex_internal.lib.log import logger as cortex_logger

class Task:
    def __call__(self, config):
        ...
        cortex_logger.info("completed validations", extra={"accuracy": accuracy})
```

The dictionary passed in via the `extra` will be flattened by one level. e.g.

```
{"asctime": "2021-01-19 15:14:05,291", "levelname": "INFO", "message": "completed validations", "process": 235, "accuracy": 0.97}
```

To avoid overriding essential Cortex metadata, please refrain from specifying the following extra keys: `asctime`, `levelname`, `message`, `labels`, and `process`. Log lines greater than 5 MB in size will be ignored.


# Configuration

```yaml
- name: <string>  # API name (required)
  kind: TaskAPI
  definition:
    path: <string>  # path to a python file with a Task class definition, relative to the Cortex root (required)
    config: <string: value>  # arbitrary dictionary passed to the callable method of the Task class (can be overridden by config passed in job submission) (optional)
    python_path: <string>  # path to the root of your Python folder that will be appended to PYTHONPATH (default: folder containing cortex.yaml)
    image: <string> # docker image to use for the Task (default: quay.io/cortexlabs/python-predictor-cpu:0.29.0, quay.io/cortexlabs/python-predictor-gpu:0.29.0-cuda10.2-cudnn8, or quay.io/cortexlabs/python-predictor-inf:0.29.0 based on compute)
    env: <string: string>  # dictionary of environment variables
    log_level: <string>  # log level that can be "debug", "info", "warning" or "error" (default: "info")
  networking:
    endpoint: <string>  # the endpoint for the API (default: <api_name>)
  compute:
    cpu: <string | int | float>  # CPU request per worker. One unit of CPU corresponds to one virtual CPU; fractional requests are allowed, and can be specified as a floating point number or via the "m" suffix (default: 200m)
    gpu: <int>  # GPU request per worker. One unit of GPU corresponds to one virtual GPU (default: 0)
    inf: <int> # Inferentia request per worker. One unit corresponds to one Inferentia ASIC with 4 NeuronCores and 8GB of cache memory. Each process will have one NeuronCore Group with (4 * inf / processes_per_replica) NeuronCores, so your model should be compiled to run on (4 * inf / processes_per_replica) NeuronCores. (default: 0) (aws only)
    mem: <string>  # memory request per worker. One unit of memory is one byte and can be expressed as an integer or by using one of these suffixes: K, M, G, T (or their power-of two counterparts: Ki, Mi, Gi, Ti) (default: Null)
```


# Jobs

## Get the TaskAPI endpoint

```bash
$ cortex get <task_api_name>
```

## Submit a Job

```yaml
POST <task_api_endpoint>:
{
    "timeout": <int>,  # duration in seconds since the submission of a job before it is terminated (optional)
    "config": {  # custom fields for this specific job (will override values in `config` specified in your api configuration) (optional)
        "string": <any>
    }
}

RESPONSE:
{
    "job_id": <string>,
    "api_name": <string>,
    "kind": "TaskAPI",
    "workers": 1,
    "config": {<string>: <any>},
    "api_id": <string>,
    "timeout": <int>,
    "created_time": <string>
}
```

## Get a job's status

```bash
$ cortex get <task_api_name> <job_id>
```

Or make a GET request to `<task_api_endpoint>?jobID=<jobID>`:

```yaml
GET <task_api_endpoint>?jobID=<jobID>:

RESPONSE:
{
    "job_status": {
        "job_id": <string>,
        "api_name": <string>,
        "kind": "TaskAPI",
        "workers": 1,
        "config": {<string>: <any>},
        "api_id": <string>,
        "status": <string>,
        "created_time": <string>
        "start_time": <string>
        "end_time": <string> (optional)
    },
    "endpoint": <string>
    "api_spec": {
        ...
    }
}
```

## Stop a job

```bash
$ cortex delete <task_api_name> <job_id>
```

Or make a DELETE request to `<task_api_endpoint>?jobID=<jobID>`:

```yaml
DELETE <task_api_endpoint>?jobID=<jobID>:

RESPONSE:
{"message":"stopped job <job_id>"}
```


# Statuses

| Status        | Meaning                                                                                                   |
| ------------- | --------------------------------------------------------------------------------------------------------- |
| running       | Task is running                                                                                           |
| succeeded     | Task has finished without errors                                                                          |
| worker error  | The task has experienced an irrecoverable error, causing the job to fail; check job logs for more details |
| out of memory | The task has ran out of memory, causing the job to fail; check job logs for more details                  |
| timed out     | Job was terminated after the specified timeout has elapsed                                                |
| stopped       | Job was stopped by the user or the Task API was deleted                                                   |




---

[Next Page](/llms-full.txt/1)

