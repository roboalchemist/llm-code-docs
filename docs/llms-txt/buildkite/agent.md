# Source: https://buildkite.com/docs/platform/cli/reference/agent.md

# Source: https://buildkite.com/docs/agent.md

# The Buildkite agent

The Buildkite agent is a small, reliable and cross-platform build runner that makes it easy to run automated builds on [your own self-hosted](/docs/agent/self-hosted) or [Buildkite's hosted](/docs/agent/buildkite-hosted) infrastructure. The agent's main responsibilities are polling buildkite.com for work, running a build's jobs, reporting back the status code and output log of the job, and uploading the job's artifacts.

This page provides Buildkite organization administrators with an overview of the [differences between self-hosted and Buildkite hosted agents](#self-hosted-and-buildkite-hosted-agents-compared), [how the Buildkite agent works](/docs/agent#how-it-works), the [agent's lifecycle](#agent-lifecycle), how to [customize the agent's functionality with hooks](#customizing-with-hooks), and the agent's [command line usage](#command-line-usage).

If you're new to Buildkite Pipelines, run through the [Getting started with Pipelines](/docs/pipelines/getting-started) tutorial, which will initially set you up to run [Buildkite hosted agents](/docs/agent/buildkite-hosted). From there, you can decide whether to continue using Buildkite hosted agents, or set yourself up to run [self-hosted agents](/docs/agent/self-hosted).

## Self-hosted and Buildkite hosted agents compared

The following table lists key feature differences between [self-hosted](/docs/agent/self-hosted) and [Buildkite hosted](/docs/agent/buildkite-hosted) agents. If you are looking to establish, expand or modify your Buildkite agent infrastructure, this table should help you choose which path or paths to take.

In summary though:

- _Self-hosted agents_ are suitable when your organization has any of the following requirements:

  - You need full control over your agent infrastructure.
  - Your agents need a lot of customization.
  - You operate under strict security conditions that requires your source code and CI/CD build runners (the agents) to be managed on premises or in your own cloud-based infrastructure.

- _Buildkite hosted agents_ is a fully-managed platform that offers fast and specialized CI/CD build runners, which work well under default conditions. This option lets you get up and running rapidly to build your projects.

<table>
  <thead>
    <tr>
      <th>Feature</th>
      <th>Self-hosted agents</th>
      <th>Buildkite hosted agents</th>
    </tr>
  </thead>
  <tbody>

      <tr>
        <td><p>Infrastructure management</p>
</td>
        <td><p>You provision, scale, and maintain your own servers</p>
</td>
        <td><p>Fully managed by Buildkite</p>
</td>
      </tr>

      <tr>
        <td><p>Supported platforms</p>
</td>
        <td><p><a href="/docs/agent/self-hosted/install/linux">Linux</a>, <a href="/docs/agent/self-hosted/install/macos">macOS</a>, <a href="/docs/agent/self-hosted/install/windows">Windows</a>, <a href="/docs/agent/self-hosted/install/docker">Docker</a>, and <a href="/docs/agent/self-hosted/install">more</a></p>
</td>
        <td><p><a href="/docs/agent/buildkite-hosted/linux">Linux</a> and <a href="/docs/agent/buildkite-hosted/macos">macOS</a></p>
</td>
      </tr>

      <tr>
        <td><p>Agent lifecycle</p>
</td>
        <td><p>Persistent or ephemeral (your choice)</p>
</td>
        <td><p>Always <a href="/docs/pipelines/glossary#ephemeral-agent">ephemeral</a>, destroyed after each job</p>
</td>
      </tr>

      <tr>
        <td><p>Scaling</p>
</td>
        <td><p>Manual or through tools such as the <a href="/docs/agent/self-hosted/aws/elastic-ci-stack">Elastic CI Stack for AWS</a> or <a href="/docs/agent/self-hosted/agent-stack-k8s">Agent Stack for Kubernetes</a></p>
</td>
        <td><p>Automatic, scales on demand</p>
</td>
      </tr>

      <tr>
        <td><p>Agent version updates</p>
</td>
        <td><p>You manage upgrades across your fleet</p>
</td>
        <td><p>Managed by Buildkite</p>
</td>
      </tr>

      <tr>
        <td><p>Configuration</p>
</td>
        <td><p>Full control through <a href="/docs/agent/self-hosted/configure">configuration file</a>, environment variables, and command-line flags</p>
</td>
        <td><p>Configured through <a href="/docs/agent/queues/managing#create-a-buildkite-hosted-queue">queue settings</a> in the Buildkite interface</p>
</td>
      </tr>

      <tr>
        <td><p><a href="#customizing-with-hooks">Hooks</a></p>
</td>
        <td><p>All <a href="/docs/agent/hooks">agent and job lifecycle hooks</a> supported</p>
</td>
        <td><p><a href="/docs/agent/hooks#job-lifecycle-hooks">Job lifecycle hooks</a> supported through <a href="/docs/agent/buildkite-hosted/linux/custom-base-images#create-an-agent-image-using-agent-hooks">custom base images</a></p>
</td>
      </tr>

      <tr>
        <td><p>Cache volumes</p>
</td>
        <td><p>You manage your own caching</p>
</td>
        <td><p>Built-in <a href="/docs/agent/buildkite-hosted/cache-volumes">NVMe-backed cache volumes</a> at no extra cost</p>
</td>
      </tr>

      <tr>
        <td><p>Docker builds</p>
</td>
        <td><p>You configure Docker on your agents</p>
</td>
        <td><p><a href="/docs/agent/buildkite-hosted/linux/remote-docker-builders">Remote Docker builders</a> with layer caching (Enterprise only)</p>
</td>
      </tr>

      <tr>
        <td><p>Container registry</p>
</td>
        <td><p>You manage your own registries</p>
</td>
        <td><p>Built-in <a href="/docs/agent/buildkite-hosted/internal-container-registry">internal container registry</a></p>
</td>
      </tr>

      <tr>
        <td><p>Network access</p>
</td>
        <td><p>Full control over networking</p>
</td>
        <td><p>US East Coast data centers with configurable <a href="/docs/agent/buildkite-hosted/network-security">network security</a></p>
</td>
      </tr>

      <tr>
        <td><p>Experimental features</p>
</td>
        <td><p>Access to <a href="/docs/agent/self-hosted/configure/experiments">agent experiments</a></p>
</td>
        <td><p>Not available</p>
</td>
      </tr>

  </tbody>
</table>

## How it works

The agent works by polling Buildkite's agent API over HTTPS. There is no need to forward ports or provide incoming firewall access, and the agents can be run across any number of machines and networks.

The agent starts by registering itself with Buildkite, and once registered it's placed into your organization's agents pool. The agent periodically polls the Buildkite platform, looking for new work, waiting to accept an available job.

After accepting a build job the agent will execute the command, streaming back the build script's output and then posting the final exit status.

Whilst the job is running you can use the `buildkite-agent meta-data` command to set and get build-wide meta-data, and `buildkite-agent artifact` for fetching and retrieving binary build-wide artifacts. These two commands allow you to have completely isolated build jobs (similar to a 12 factor web application) but have access to shared state and data storage across any number of machines and networks.

### Job routing

By default, a pipeline's jobs run on the first available agent associated with the relevant [queues](/docs/agent/queues) that the pipeline's [cluster](/docs/pipelines/security/clusters) is set to. Agents associated with a queue are ordered for selection by how recently these agents successfully completed a job. This takes advantage of warm caches to guarantee the fastest run time possible.

Learn more about how Buildkite routes jobs to queues in the [Queues overview](/docs/agent/queues) page.

## Agent lifecycle

The agent goes through several stages during its operation, from starting up and registering with Buildkite, through to polling for and running jobs, and shutting down. For details on signal handling, exit codes, and troubleshooting common lifecycle issues, see the [Agent lifecycle](/docs/agent/lifecycle) page.

## Customizing with hooks

The agent's behavior can be customized using hooks, which are shell scripts that exist on your build machines or in each pipeline's code repository. Hooks can be used to set up [secrets](/docs/pipelines/security/secrets/managing) as well as overriding default behavior. See the [hooks](/docs/agent/hooks) documentation for full details.

## Command line usage

The Buildkite agent has a command line interface (CLI) that lets you interact with and control the agent through the command line. For a complete reference of all available commands, see the [Command-line reference](/docs/agent/cli/reference).
