# Source: https://buildkite.com/docs/agent/self-hosted/agent-stack-k8s/controller-configuration.md

# Controller configuration

This page covers the available commands for:

- `agent-stack-k8s [flags]`
- `agent-stack-k8s [command]`

All references to "controller" on this page refer to the Agent Stack for Kubernetes controller.

## Available commands

| Command     | Description                                                       |
|-------------|-------------------------------------------------------------------|
| `completion`| Generate the autocompletion script for the specified shell        |
| `help`      | Help about any command                                            |
| `lint`      | A tool for linting Buildkite pipelines                            |
| `version`   | Prints the version                                                |

Use `agent-stack-k8s [command] --help` for more information about a command.

## Flags

<table>
  <thead>
    <tr>
      <th style="width:25%">Flag and value type if applicable</th>
      <th style="width:75%">Description</th>
    </tr>
  </thead>
  <tbody>

      <tr>
        <td>
          <p><code>--agent-token-secret</code></p>
          
            <strong>&nbsp;&nbsp;Type:</strong> <code>string</code>
          
         </td>
        <td>
          <p>The name of the Buildkite agent token secret.</p>
          
            <strong>Default:</strong> <code>buildkite-agent-token</code>
          
        </td>
      </tr>
    
      <tr>
        <td>
          <p><code>--allow-pod-spec-patch-unsafe-command-modification</code></p>
          
         </td>
        <td>
          <p>Permits podSpecPatch to modify the <code>command</code> or <code>args</code> fields of stack-provided containers. See the warning in the agent-stack-k8s README before enabling this option.</p>
          
        </td>
      </tr>
    
      <tr>
        <td>
          <p><code>--cluster-uuid</code></p>
          
            <strong>&nbsp;&nbsp;Type:</strong> <code>string</code>
          
         </td>
        <td>
          <p>The UUID of the Buildkite cluster. The agent token must be for the Buildkite cluster.</p>
          
        </td>
      </tr>
    
      <tr>
        <td>
          <p><code>-f, --config</code></p>
          
            <strong>&nbsp;&nbsp;Type:</strong> <code>string</code>
          
         </td>
        <td>
          <p>The config file path.</p>
          
        </td>
      </tr>
    
      <tr>
        <td>
          <p><code>--debug</code></p>
          
         </td>
        <td>
          <p>Debug logs.</p>
          
        </td>
      </tr>
    
      <tr>
        <td>
          <p><code>--default-image-check-pull-policy</code></p>
          
            <strong>&nbsp;&nbsp;Type:</strong> <code>string</code>
          
         </td>
        <td>
          <p>Sets a default PullPolicy for image-check init containers, used if an image pull policy is not set for the corresponding container in a podSpec or podSpecPatch.</p>
          
        </td>
      </tr>
    
      <tr>
        <td>
          <p><code>--default-image-pull-policy</code></p>
          
            <strong>&nbsp;&nbsp;Type:</strong> <code>string</code>
          
         </td>
        <td>
          <p>Configures a default image pull policy for containers that do not specify a pull policy and non-init containers created by the stack itself.</p>
          
        </td>
      </tr>
    
      <tr>
        <td>
          <p><code>--default-termination-grace-period-seconds</code></p>
          
            <strong>&nbsp;&nbsp;Type:</strong> <code>integer</code>
          
         </td>
        <td>
          <p>The maximum number of seconds a pod will run after being told to terminate, if not otherwise set by a podSpec.</p>
          
            <strong>Default:</strong> <code>60</code>
          
        </td>
      </tr>
    
      <tr>
        <td>
          <p><code>--empty-job-grace-period</code></p>
          
            <strong>&nbsp;&nbsp;Type:</strong> <code>duration</code>
          
         </td>
        <td>
          <p>The duration after starting a Kubernetes job that the controller will wait before considering failing the job due to a missing pod (for example, when the podSpec specifies a missing service account).</p>
          
            <strong>Default:</strong> <code>30s</code>
          
        </td>
      </tr>
    
      <tr>
        <td>
          <p><code>--enable-queue-pause</code></p>
          
            <strong>&nbsp;&nbsp;Type:</strong> <code>bool</code>
          
         </td>
        <td>
          <p>Allow the controller to pause processing the jobs when the queue is paused on Buildkite.<br/>This flag is only available in version 0.24.0 and later of the controller.</p>
          
            <strong>Default:</strong> <code>false</code>
          
        </td>
      </tr>
    
      <tr>
        <td>
          <p><code>-h, --help</code></p>
          
         </td>
        <td>
          <p>Displays help for the agent-stack-k8s.</p>
          
        </td>
      </tr>
    
      <tr>
        <td>
          <p><code>--http-timeout</code></p>
          
            <strong>&nbsp;&nbsp;Type:</strong> <code>duration</code>
          
         </td>
        <td>
          <p>Timeout for HTTP requests to the Buildkite agent API.</p>
          
            <strong>Default:</strong> <code>60s</code>
          
        </td>
      </tr>
    
      <tr>
        <td>
          <p><code>--image</code></p>
          
            <strong>&nbsp;&nbsp;Type:</strong> <code>string</code>
          
         </td>
        <td>
          <p>The container image to use for the Buildkite agent. Defaults to a version of <code>ghcr.io/buildkite/agent</code> matching the agent-stack-k8s release.</p>
          
        </td>
      </tr>
    
      <tr>
        <td>
          <p><code>--image-check-container-cpu-limit</code></p>
          
            <strong>&nbsp;&nbsp;Type:</strong> <code>string</code>
          
         </td>
        <td>
          <p>Configures the CPU resource limit for all <code>imagecheck-*</code> init containers.</p>
          
            <strong>Default:</strong> <code>200m</code>
          
        </td>
      </tr>
    
      <tr>
        <td>
          <p><code>--image-check-container-memory-limit</code></p>
          
            <strong>&nbsp;&nbsp;Type:</strong> <code>string</code>
          
         </td>
        <td>
          <p>Configures the memory resource limit for all <code>imagecheck-*</code> init containers.</p>
          
            <strong>Default:</strong> <code>128Mi</code>
          
        </td>
      </tr>
    
      <tr>
        <td>
          <p><code>--image-pull-backoff-grace-period</code></p>
          
            <strong>&nbsp;&nbsp;Type:</strong> <code>duration</code>
          
         </td>
        <td>
          <p>Duration after starting a pod that the controller will wait before considering cancelling a job due to ImagePullBackOff (e.g., when the podSpec specifies container images that cannot be pulled).</p>
          
            <strong>Default:</strong> <code>30s</code>
          
        </td>
      </tr>
    
      <tr>
        <td>
          <p><code>--job-active-deadline-seconds</code></p>
          
            <strong>&nbsp;&nbsp;Type:</strong> <code>integer</code>
          
         </td>
        <td>
          <p>The maximum number of seconds a Kubernetes job is allowed to run before terminating all pods and failing.</p>
          
            <strong>Default:</strong> <code>21600</code>
          
        </td>
      </tr>
    
      <tr>
        <td>
          <p><code>--job-cancel-checker-poll-interval</code></p>
          
            <strong>&nbsp;&nbsp;Type:</strong> <code>duration</code>
          
         </td>
        <td>
          <p>Controls the interval between job state queries while a pod is still Pending.</p>
          
            <strong>Default:</strong> <code>5s</code>
          
        </td>
      </tr>
    
      <tr>
        <td>
          <p><code>--job-creation-concurrency</code></p>
          
            <strong>&nbsp;&nbsp;Type:</strong> <code>integer</code>
          
         </td>
        <td>
          <p>The number of concurrent goroutines for converting Buildkite jobs into Kubernetes jobs.</p>
          
            <strong>Default:</strong> <code>25</code>
          
        </td>
      </tr>
    
      <tr>
        <td>
          <p><code>--job-prefix</code></p>
          
            <strong>&nbsp;&nbsp;Type:</strong> <code>string</code>
          
         </td>
        <td>
          <p>The prefix to use when creating Kubernetes job names.</p>
          
            <strong>Default:</strong> <code>buildkite-</code>
          
        </td>
      </tr>
    
      <tr>
        <td>
          <p><code>--job-ttl</code></p>
          
            <strong>&nbsp;&nbsp;Type:</strong> <code>duration</code>
          
         </td>
        <td>
          <p>The time to retain Kubernetes jobs after completion.</p>
          
            <strong>Default:</strong> <code>10m0s</code>
          
        </td>
      </tr>
    
      <tr>
        <td>
          <p><code>--k8s-client-rate-limiter-burst</code></p>
          
            <strong>&nbsp;&nbsp;Type:</strong> <code>integer</code>
          
         </td>
        <td>
          <p>The burst value of the K8s client rate limiter.</p>
          
            <strong>Default:</strong> <code>20</code>
          
        </td>
      </tr>
    
      <tr>
        <td>
          <p><code>--k8s-client-rate-limiter-qps</code></p>
          
            <strong>&nbsp;&nbsp;Type:</strong> <code>integer</code>
          
         </td>
        <td>
          <p>The QPS value of the K8s client rate limiter.</p>
          
            <strong>Default:</strong> <code>10</code>
          
        </td>
      </tr>
    
      <tr>
        <td>
          <p><code>--log-format</code></p>
          
            <strong>&nbsp;&nbsp;Type:</strong> <code>string</code>
          
         </td>
        <td>
          <p>Sets the log format. One of <code>logfmt</code> (plain or colored text) or <code>json</code>.</p>
          
            <strong>Default:</strong> <code>logfmt</code>
          
        </td>
      </tr>
    
      <tr>
        <td>
          <p><code>--log-http-payloads</code></p>
          
         </td>
        <td>
          <p>Logs full HTTP request and response payloads. Only active when log level is debug. This may log sensitive information including tokens and secrets.</p>
          
        </td>
      </tr>
    
      <tr>
        <td>
          <p><code>--log-level</code></p>
          
            <strong>&nbsp;&nbsp;Type:</strong> <code>string</code>
          
         </td>
        <td>
          <p>Sets the log level. One of <code>debug</code>, <code>info</code>, <code>warn</code>, or <code>error</code>. Overridden by <code>--debug</code> if set.</p>
          
            <strong>Default:</strong> <code>info</code>
          
        </td>
      </tr>
    
      <tr>
        <td>
          <p><code>--max-in-flight</code></p>
          
            <strong>&nbsp;&nbsp;Type:</strong> <code>integer</code>
          
         </td>
        <td>
          <p>The maximum jobs in flight, where a value of 0 means no maximum.</p>
          
            <strong>Default:</strong> <code>25</code>
          
        </td>
      </tr>
    
      <tr>
        <td>
          <p><code>--namespace</code></p>
          
            <strong>&nbsp;&nbsp;Type:</strong> <code>string</code>
          
         </td>
        <td>
          <p>The Kubernetes namespace to create resources in.</p>
          
            <strong>Default:</strong> <code>default</code>
          
        </td>
      </tr>
    
      <tr>
        <td>
          <p><code>--no-color</code></p>
          
         </td>
        <td>
          <p>Disables colored log output (ANSI escape codes). Colors are disabled automatically when the output is not a terminal.</p>
          
        </td>
      </tr>
    
      <tr>
        <td>
          <p><code>--org</code></p>
          
            <strong>&nbsp;&nbsp;Type:</strong> <code>string</code>
          
         </td>
        <td>
          <p>The Buildkite organization name to watch.</p>
          
        </td>
      </tr>
    
      <tr>
        <td>
          <p><code>--pagination-depth-limit</code></p>
          
            <strong>&nbsp;&nbsp;Type:</strong> <code>integer</code>
          
         </td>
        <td>
          <p>Sets the maximum number of pages when retrieving Buildkite jobs to be scheduled. Increasing this value will increase the number of requests made to the Buildkite API and number of jobs to be scheduled on the Kubernetes cluster.</p>
          
            <strong>Default:</strong> <code>2</code>
          
        </td>
      </tr>
    
      <tr>
        <td>
          <p><code>--pagination-page-size</code></p>
          
            <strong>&nbsp;&nbsp;Type:</strong> <code>integer</code>
          
         </td>
        <td>
          <p>Sets the maximum number of jobs per page when retrieving Buildkite jobs to be scheduled.</p>
          
            <strong>Default:</strong> <code>1000</code>
          
        </td>
      </tr>
    
      <tr>
        <td>
          <p><code>--poll-interval</code></p>
          
            <strong>&nbsp;&nbsp;Type:</strong> <code>duration</code>
          
         </td>
        <td>
          <p>The time to wait between polling for new jobs (minimum <code>1s</code>). Note that increasing this causes jobs to be slower to start.</p>
          
            <strong>Default:</strong> <code>1s</code>
          
        </td>
      </tr>
    
      <tr>
        <td>
          <p><code>--profiler-address</code></p>
          
            <strong>&nbsp;&nbsp;Type:</strong> <code>string</code>
          
         </td>
        <td>
          <p>The bind address to expose the pprof profiler (for example, <code>localhost:6060</code>).</p>
          
        </td>
      </tr>
    
      <tr>
        <td>
          <p><code>--prohibit-kubernetes-plugin</code></p>
          
         </td>
        <td>
          <p>Causes the controller to prohibit the Kubernetes plugin specified within jobs (pipeline YAML). Enabling this causes jobs with a Kubernetes plugin to fail, preventing the pipeline YAML from having any influence over the podSpec.</p>
          
        </td>
      </tr>
    
      <tr>
        <td>
          <p><code>--prometheus-port</code></p>
          
            <strong>&nbsp;&nbsp;Type:</strong> <code>uint16</code>
          
         </td>
        <td>
          <p>The bind port to expose Prometheus /metrics. Specifying 0 disables this feature.</p>
          
        </td>
      </tr>
    
      <tr>
        <td>
          <p><code>--query-reset-interval</code></p>
          
            <strong>&nbsp;&nbsp;Type:</strong> <code>duration</code>
          
         </td>
        <td>
          <p>Controls the interval between pagination cursor resets. Increasing this value will increase the number of jobs to be scheduled but also delay picking up any jobs that were missed from the start of the query.</p>
          
            <strong>Default:</strong> <code>10s</code>
          
        </td>
      </tr>
    
      <tr>
        <td>
          <p><code>--queue</code></p>
          
            <strong>&nbsp;&nbsp;Type:</strong> <code>string</code>
          
         </td>
        <td>
          <p>The Buildkite queue to poll for jobs. If set, overrides the queue tag.</p>
          
        </td>
      </tr>
    
      <tr>
        <td>
          <p><code>--skip-image-check-containers</code></p>
          
         </td>
        <td>
          <p>Disables and skips all <code>imagecheck-*</code> init containers.</p>
          
        </td>
      </tr>
    
      <tr>
        <td>
          <p><code>--tags</code></p>
          
            <strong>&nbsp;&nbsp;Type:</strong> <code>strings</code>
          
         </td>
        <td>
          <p>A comma-separated list of agent tags. The "queue" tag must be unique (for example, "queue=kubernetes,os=linux").</p>
          
            <strong>Default:</strong> <code>[queue=kubernetes]</code>
          
        </td>
      </tr>
    
      <tr>
        <td>
          <p><code>--work-queue-limit</code></p>
          
            <strong>&nbsp;&nbsp;Type:</strong> <code>integer</code>
          
         </td>
        <td>
          <p>Sets the maximum number of jobs the controller will hold in the work queue.</p>
          
            <strong>Default:</strong> <code>1000000</code>
          
        </td>
      </tr>
    
  </tbody>
</table>

## Kubernetes node selection

The Buildkite Agent Stack for Kubernetes controller can be deployed to particular Kubernetes Nodes, using the Kubernetes PodSpec [`nodeSelector`](https://kubernetes.io/docs/tasks/configure-pod-container/assign-pods-nodes/#create-a-pod-that-gets-scheduled-to-your-chosen-node) field.

The `nodeSelector` field can be defined in the controller's configuration:

```yaml
# values.yml
...
nodeSelector:
  teamowner: "services"
config:
...
```

## Additional environment variables for the controller container

If the Buildkite Agent Stack for Kubernetes controller container requires extra environment variables in order to correctly operate inside your Kubernetes cluster, they can be added to your values YAML file and applied during a deployment with Helm.

The `controllerEnv` field can be used to define extra Kubernetes EnvVar environment variables that will apply to the Buildkite Agent Stack for Kubernetes controller container:

```yaml
# values.yml
...
controllerEnv:
  - name: KUBERNETES_SERVICE_HOST
    value: "10.10.10.10"
  - name: KUBERNETES_SERVICE_PORT
    value: "8443"
config:
...
```

## Custom annotations for the controller

If you need to add custom annotations to the Agent Stack for Kubernetes controller pod, these annotations can be defined in your values YAML file and applied during a deployment with Helm. Note that the controller pod will also have the annotations `checksum/config` and `checksum/secrets` to track changes to the configuration and secrets.

The `annotations` field can be used to define custom annotations that will be applied to the Buildkite Agent Stack for Kubernetes controller pod:

```yaml
# values.yml
...
annotations:
  kubernetes.io/description: "Agent Stack K8s Controller"
  prometheus.io/scrape: "true"
  prometheus.io/port: "8080"
config:
...
```

## Cleaning up old Buildkite Pipelines jobs

If you are using Kubernetes v1.23 and earlier, you may sometimes find that old jobs are still present in your Kubernetes cluster and are not getting automatically cleaned up. This may consume unnecessary space and potentially cause other disruptions with deployments.

If you notice old Buildkite Pipelines jobs still present in your Kubernetes cluster, you can use the [`clean-up-job.yaml`](https://github.com/buildkite/agent-stack-k8s/blob/main/utils/clean-up-job.yaml) script (with usage instructions provided at the top of this file) located in [Agent Stack for Kubernetes](https://github.com/buildkite/agent-stack-k8s) repository to clean up your old Buildkite jobs.
