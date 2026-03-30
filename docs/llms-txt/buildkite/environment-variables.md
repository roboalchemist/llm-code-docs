# Source: https://buildkite.com/docs/pipelines/configure/environment-variables.md

# Environment variables

When the agent invokes your build scripts it passes in a set of standard Buildkite environment variables, along with any that you've defined in your build configuration. You can use these environment variables in your [build steps](/docs/pipelines/configure/defining-steps) and
[job lifecycle hooks](/docs/agent/hooks#job-lifecycle-hooks).

Environment variable size limits are dependent on the operating systems the agents are run on. When a program or process is started, it can typically accept inputs as either one or more environment variables in the form of `key=value` pairs, or a list (array) of command line arguments (referred to as a vector of arguments or `argv`). Depending on the operating system, these limits could be shared size limit across all such environment variables and `argv`, whereas others impose size limits per item (such as an environment variable's size limit).

For best practices and recommendations about using secrets in your environment variables, see the [Managing secrets](/docs/pipelines/security/secrets/managing) guide.

## Buildkite environment variables

The following environment variables may be visible in your commands, plugins, and hooks.

> 🚧 Unverified commits
> Note that GitHub accepts <a href="https://docs.github.com/en/authentication/managing-commit-signature-verification/about-commit-signature-verification">unsigned commits</a>, including information about the commit author and passes them along to webhooks, so you should not rely on these for authentication unless you are confident that all of your commits are trusted.

<table class="Docs__attribute__table">
  <colgroup>
    <col>
    <col>
  </colgroup>
  <tbody>

    <tr id="BUILDKITE">
      <th>
        <code>BUILDKITE</code> <a class="Docs__attribute__link" href="#BUILDKITE">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>Always <code>true</code></p>

              </td>
    </tr>
      
    <tr id="BUILDKITE_AGENT_ACCESS_TOKEN">
      <th>
        <code>BUILDKITE_AGENT_ACCESS_TOKEN</code> <a class="Docs__attribute__link" href="#BUILDKITE_AGENT_ACCESS_TOKEN">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The agent session token for the job. The variable is read by the agent <code>artifact</code> and <code>meta-data</code> commands.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>83d544ccc223c157d2bf80d3f2a32982c32c3c0db8e3674820da5064783fb091</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_AGENT_DEBUG">
      <th>
        <code>BUILDKITE_AGENT_DEBUG</code> <a class="Docs__attribute__link" href="#BUILDKITE_AGENT_DEBUG">#</a>

        <ul class="comma-separated Docs__attribute__env-var">
          <li><strong>Possible values:</strong></li>
                        <li><code>true</code></li>
                      <li><code>false</code></li>
          
          </ul>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The value of the <code>debug</code> <a href="/docs/agent/self-hosted/configure">agent configuration option</a>.</p>

              </td>
    </tr>
      
    <tr id="BUILDKITE_AGENT_DISCONNECT_AFTER_JOB">
      <th>
        <code>BUILDKITE_AGENT_DISCONNECT_AFTER_JOB</code> <a class="Docs__attribute__link" href="#BUILDKITE_AGENT_DISCONNECT_AFTER_JOB">#</a>

        <ul class="comma-separated Docs__attribute__env-var">
          <li><strong>Possible values:</strong></li>
                        <li><code>true</code></li>
                      <li><code>false</code></li>
          
          </ul>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The value of the <code>disconnect-after-job</code> <a href="/docs/agent/self-hosted/configure">agent configuration option</a>.</p>

              </td>
    </tr>
      
    <tr id="BUILDKITE_AGENT_DISCONNECT_AFTER_IDLE_TIMEOUT">
      <th>
        <code>BUILDKITE_AGENT_DISCONNECT_AFTER_IDLE_TIMEOUT</code> <a class="Docs__attribute__link" href="#BUILDKITE_AGENT_DISCONNECT_AFTER_IDLE_TIMEOUT">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The value of the <code>disconnect-after-idle-timeout</code> <a href="/docs/agent/self-hosted/configure">agent configuration option</a>.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>10</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_AGENT_ENDPOINT">
      <th>
        <code>BUILDKITE_AGENT_ENDPOINT</code> <a class="Docs__attribute__link" href="#BUILDKITE_AGENT_ENDPOINT">#</a>
        
          <p class="Docs__attribute__env-var">
            <strong>Default</strong>:
            <code>https://agent.buildkite.com/v3</code>
          </p>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The value of the <code>endpoint</code> <a href="/docs/agent/self-hosted/configure">agent configuration option</a>. This is set as an environment variable by the bootstrap and then read by most of the <code>buildkite-agent</code> commands.</p>

              </td>
    </tr>
      
    <tr id="BUILDKITE_AGENT_EXPERIMENT">
      <th>
        <code>BUILDKITE_AGENT_EXPERIMENT</code> <a class="Docs__attribute__link" href="#BUILDKITE_AGENT_EXPERIMENT">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>A list of the <a href="/docs/agent/self-hosted#experimental-features">experimental agent features</a> that are currently enabled. The value can be set using the <code>--experiment</code> flag on the <a href="/docs/agent/cli/reference/start#starting-an-agent"><code>buildkite-agent start</code> command</a> or in your <a href="/docs/agent/self-hosted/configure">agent configuration file</a>.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>experiment1,experiment2</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_AGENT_HEALTH_CHECK_ADDR">
      <th>
        <code>BUILDKITE_AGENT_HEALTH_CHECK_ADDR</code> <a class="Docs__attribute__link" href="#BUILDKITE_AGENT_HEALTH_CHECK_ADDR">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The value of the <code>health-check-addr</code> <a href="/docs/agent/self-hosted/configure">agent configuration option</a>.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>localhost:8080</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_AGENT_ID">
      <th>
        <code>BUILDKITE_AGENT_ID</code> <a class="Docs__attribute__link" href="#BUILDKITE_AGENT_ID">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The UUID of the agent.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>1a222222-e999-3636-8ddd-802222222222</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_AGENT_META_DATA_">
      <th>
        <code>BUILDKITE_AGENT_META_DATA_*</code> <a class="Docs__attribute__link" href="#BUILDKITE_AGENT_META_DATA_">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The value of each <a href="/docs/agent/cli/reference/start#setting-tags">agent tag</a>. The tag name is appended to the end of the variable name. They can be set using the <code>--tags</code> flag on the <code>buildkite-agent start</code> command, or in the <a href="/docs/agent/self-hosted/configure">agent configuration file</a>. The <a href="/docs/agent/queues">Queue tag</a> is specifically used for isolating jobs and agents, and appears as the <code>BUILDKITE_AGENT_META_DATA_QUEUE</code> environment variable.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>"BUILDKITE_AGENT_META_DATA_TAGNAME=tagvalue", "BUILDKITE_AGENT_META_DATA_QUEUE=some-queue"</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_AGENT_NAME">
      <th>
        <code>BUILDKITE_AGENT_NAME</code> <a class="Docs__attribute__link" href="#BUILDKITE_AGENT_NAME">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The name of the agent that ran the job.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>elastic-builders-088264dc4f9</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_AGENT_PID">
      <th>
        <code>BUILDKITE_AGENT_PID</code> <a class="Docs__attribute__link" href="#BUILDKITE_AGENT_PID">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The process ID of the agent.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>6</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_ARTIFACT_PATHS">
      <th>
        <code>BUILDKITE_ARTIFACT_PATHS</code> <a class="Docs__attribute__link" href="#BUILDKITE_ARTIFACT_PATHS">#</a>

      </th>
      <td>
        <p>The artifact paths to upload after the job, if any have been specified. The value can be modified by exporting the environment variable in the <code>environment</code> or <code>pre-checkout</code> hooks.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>tmp/capybara/**/*;coverage/**/*</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_ARTIFACT_UPLOAD_DESTINATION">
      <th>
        <code>BUILDKITE_ARTIFACT_UPLOAD_DESTINATION</code> <a class="Docs__attribute__link" href="#BUILDKITE_ARTIFACT_UPLOAD_DESTINATION">#</a>

      </th>
      <td>
        <p>The path where artifacts will be uploaded. This variable is read by the <code>buildkite-agent artifact upload</code> command, and during the artifact upload phase of <a href="/docs/pipelines/command-step#command-step-attributes">command steps</a>. It can only be set by exporting the environment variable in the <code>environment</code>, <code>pre-checkout</code> or <code>pre-command</code> hooks.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>s3://name-of-your-s3-bucket/$BUILDKITE_PIPELINE_ID/$BUILDKITE_BUILD_ID/$BUILDKITE_JOB_ID</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_BIN_PATH">
      <th>
        <code>BUILDKITE_BIN_PATH</code> <a class="Docs__attribute__link" href="#BUILDKITE_BIN_PATH">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The path to the directory containing the <code>buildkite-agent</code> binary.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>/usr/local/bin</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_BRANCH">
      <th>
        <code>BUILDKITE_BRANCH</code> <a class="Docs__attribute__link" href="#BUILDKITE_BRANCH">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The branch being built. Note that for manually triggered builds, this branch is not guaranteed to contain the commit specified by <code>BUILDKITE_COMMIT</code>.</p>

<p>When a build is triggered by a GitHub webhook tag <code>push</code> event, this variable will also be set to the name of the tag being built (same value as <code>BUILDKITE_TAG</code>).</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>main</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_BUILD_CHECKOUT_PATH">
      <th>
        <code>BUILDKITE_BUILD_CHECKOUT_PATH</code> <a class="Docs__attribute__link" href="#BUILDKITE_BUILD_CHECKOUT_PATH">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The path where the agent has checked out your code for this build. This variable is read by the bootstrap when the agent is started, and can only be set by exporting the environment variable in the <code>environment</code> or <code>pre-checkout</code> hooks.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>/var/lib/buildkite-agent/builds/agent-1/pipeline-2</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_BUILD_AUTHOR">
      <th>
        <code>BUILDKITE_BUILD_AUTHOR</code> <a class="Docs__attribute__link" href="#BUILDKITE_BUILD_AUTHOR">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The name of the user who authored the commit being built. May be <strong><a href="#unverified-commits">unverified</a></strong>. This value can be blank in some situations, including builds manually triggered using API or Buildkite web interface.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>Carol Danvers</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_BUILD_AUTHOR_EMAIL">
      <th>
        <code>BUILDKITE_BUILD_AUTHOR_EMAIL</code> <a class="Docs__attribute__link" href="#BUILDKITE_BUILD_AUTHOR_EMAIL">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The notification email of the user who authored the commit being built. May be <strong><a href="#unverified-commits">unverified</a></strong>. This value can be blank in some situations, including builds manually triggered using API or Buildkite web interface.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>cdanvers@kree-net.com</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_BUILD_CREATOR">
      <th>
        <code>BUILDKITE_BUILD_CREATOR</code> <a class="Docs__attribute__link" href="#BUILDKITE_BUILD_CREATOR">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The name of the user who created the build. The value differs depending on how the build was created:</p>

<ul>
<li>
<strong>Buildkite dashboard:</strong> Set based on who manually created the build.</li>
<li>
<strong>GitHub webhook:</strong> Set from the  <strong><a href="#unverified-commits">unverified</a></strong> HEAD commit.</li>
<li>
<strong>Webhook:</strong> Set based on which user is attached to the API Key used.</li>
</ul>

          <p>
            <strong class="h5">Example:</strong>
            <code>Carol Danvers</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_BUILD_CREATOR_EMAIL">
      <th>
        <code>BUILDKITE_BUILD_CREATOR_EMAIL</code> <a class="Docs__attribute__link" href="#BUILDKITE_BUILD_CREATOR_EMAIL">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The notification email of the user who created the build. The value differs depending on how the build was created:</p>

<ul>
<li>
<strong>Buildkite dashboard:</strong> Set based on who manually created the build.</li>
<li>
<strong>GitHub webhook:</strong> Set from the  <strong><a href="#unverified-commits">unverified</a></strong> HEAD commit.</li>
<li>
<strong>Webhook:</strong> Set based on which user is attached to the API Key used.</li>
</ul>

          <p>
            <strong class="h5">Example:</strong>
            <code>cdanvers@kree-net.com</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_BUILD_CREATOR_TEAMS">
      <th>
        <code>BUILDKITE_BUILD_CREATOR_TEAMS</code> <a class="Docs__attribute__link" href="#BUILDKITE_BUILD_CREATOR_TEAMS">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>A colon separated list of non-private team slugs that the build creator belongs to. The value differs depending on how the build was created:</p>

<ul>
<li>
<strong>Buildkite dashboard:</strong> Set based on who manually created the build.</li>
<li>
<strong>GitHub webhook:</strong> Set from the  <strong><a href="#unverified-commits">unverified</a></strong> HEAD commit.</li>
<li>
<strong>Webhook:</strong> Set based on which user is attached to the API Key used.</li>
</ul>

          <p>
            <strong class="h5">Example:</strong>
            <code>everyone:platform</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_BUILD_ID">
      <th>
        <code>BUILDKITE_BUILD_ID</code> <a class="Docs__attribute__link" href="#BUILDKITE_BUILD_ID">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The UUID of the build.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>4735ba57-80d0-46e2-8fa0-b28223a86586</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_BUILD_NUMBER">
      <th>
        <code>BUILDKITE_BUILD_NUMBER</code> <a class="Docs__attribute__link" href="#BUILDKITE_BUILD_NUMBER">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The build number. This number increases with every build, and is guaranteed to be unique within each pipeline.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>1514</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_BUILD_PATH">
      <th>
        <code>BUILDKITE_BUILD_PATH</code> <a class="Docs__attribute__link" href="#BUILDKITE_BUILD_PATH">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The value of the <code>build-path</code> <a href="/docs/agent/self-hosted/configure">agent configuration option</a>.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>/var/lib/buildkite-agent/builds/</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_BUILD_URL">
      <th>
        <code>BUILDKITE_BUILD_URL</code> <a class="Docs__attribute__link" href="#BUILDKITE_BUILD_URL">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The url for this build on Buildkite.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>https://buildkite.com/acme-inc/my-project/builds/1514</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_CANCEL_GRACE_PERIOD">
      <th>
        <code>BUILDKITE_CANCEL_GRACE_PERIOD</code> <a class="Docs__attribute__link" href="#BUILDKITE_CANCEL_GRACE_PERIOD">#</a>
        
          <p class="Docs__attribute__env-var">
            <strong>Default</strong>:
            <code>10</code>
          </p>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The value of the <code>cancel-grace-period</code> <a href="/docs/agent/self-hosted/configure">agent configuration option</a> in seconds.</p>

              </td>
    </tr>
      
    <tr id="BUILDKITE_CANCEL_SIGNAL">
      <th>
        <code>BUILDKITE_CANCEL_SIGNAL</code> <a class="Docs__attribute__link" href="#BUILDKITE_CANCEL_SIGNAL">#</a>
        
          <p class="Docs__attribute__env-var">
            <strong>Default</strong>:
            <code>SIGTERM</code>
          </p>

      </th>
      <td>
        <p>The value of the <code>cancel-signal</code> <a href="/docs/agent/self-hosted/configure">agent configuration option</a>.</p>

              </td>
    </tr>
      
    <tr id="BUILDKITE_CLEAN_CHECKOUT">
      <th>
        <code>BUILDKITE_CLEAN_CHECKOUT</code> <a class="Docs__attribute__link" href="#BUILDKITE_CLEAN_CHECKOUT">#</a>

        <ul class="comma-separated Docs__attribute__env-var">
          <li><strong>Possible values:</strong></li>
                        <li><code>true</code></li>
                      <li><code>false</code></li>
          
          </ul>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>Whether the build should perform a clean checkout. The variable is read during the default checkout phase of the bootstrap and can be overridden in <code>environment</code> or <code>pre-checkout</code> hooks.</p>

              </td>
    </tr>
      
    <tr id="BUILDKITE_CLUSTER_ID">
      <th>
        <code>BUILDKITE_CLUSTER_ID</code> <a class="Docs__attribute__link" href="#BUILDKITE_CLUSTER_ID">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The UUID value of the cluster, but only if the build has an associated <code>cluster_queue</code>. Otherwise, this environment variable is not set.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>4735ba57-80d0-46e2-8fa0-b28223a86586</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_CLUSTER_NAME">
      <th>
        <code>BUILDKITE_CLUSTER_NAME</code> <a class="Docs__attribute__link" href="#BUILDKITE_CLUSTER_NAME">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The name of the cluster in which the job is running.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>production</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_COMMAND">
      <th>
        <code>BUILDKITE_COMMAND</code> <a class="Docs__attribute__link" href="#BUILDKITE_COMMAND">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The command that will be run for the job.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>script/buildkite/specs</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_COMMAND_EVAL">
      <th>
        <code>BUILDKITE_COMMAND_EVAL</code> <a class="Docs__attribute__link" href="#BUILDKITE_COMMAND_EVAL">#</a>

        <ul class="comma-separated Docs__attribute__env-var">
          <li><strong>Possible values:</strong></li>
                        <li><code>true</code></li>
                      <li><code>false</code></li>
          
          </ul>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The opposite of the value of the <code>no-command-eval</code> <a href="/docs/agent/self-hosted/configure">agent configuration option</a>.</p>

              </td>
    </tr>
      
    <tr id="BUILDKITE_COMMAND_EXIT_STATUS">
      <th>
        <code>BUILDKITE_COMMAND_EXIT_STATUS</code> <a class="Docs__attribute__link" href="#BUILDKITE_COMMAND_EXIT_STATUS">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The exit code from the last command run in the command hook.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>-1</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_COMPUTE_TYPE">
      <th>
        <code>BUILDKITE_COMPUTE_TYPE</code> <a class="Docs__attribute__link" href="#BUILDKITE_COMPUTE_TYPE">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p><code>hosted</code> if the job is running on Hosted Agents, otherwise <code>self-hosted</code>.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>hosted</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_COMMIT">
      <th>
        <code>BUILDKITE_COMMIT</code> <a class="Docs__attribute__link" href="#BUILDKITE_COMMIT">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The git commit object of the build. This is usually a 40-byte hexadecimal SHA-1 hash, but can also be a symbolic name like <code>HEAD</code>.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>83a20ec058e2fb00e7fa4558c4c6e81e2dcf253d</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_COMMIT_RESOLVED">
      <th>
        <code>BUILDKITE_COMMIT_RESOLVED</code> <a class="Docs__attribute__link" href="#BUILDKITE_COMMIT_RESOLVED">#</a>

        <ul class="comma-separated Docs__attribute__env-var">
          <li><strong>Possible values:</strong></li>
                        <li><code>true</code></li>
                      <li><code>false</code></li>
          
          </ul>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>Tells the Buildkite agent if BUILDKITE_COMMIT has been resolved to a full Git SHA and its metadata (author, subject, body) has been uploaded.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>"BUILDKITE_COMMIT_RESOLVED=true", "BUILDKITE_COMMIT_RESOLVED=false"</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_CONFIG_PATH">
      <th>
        <code>BUILDKITE_CONFIG_PATH</code> <a class="Docs__attribute__link" href="#BUILDKITE_CONFIG_PATH">#</a>
        
          <p class="Docs__attribute__env-var">
            <strong>Default</strong>:
            <code>/buildkite/buildkite-agent.cfg</code>
          </p>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The path to the agent config file.</p>

              </td>
    </tr>
      
    <tr id="BUILDKITE_ENV_FILE">
      <th>
        <code>BUILDKITE_ENV_FILE</code> <a class="Docs__attribute__link" href="#BUILDKITE_ENV_FILE">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The path to the file containing the job's environment variables.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>/tmp/job-env-36711a2a-711a-484e-b180-e1b3711a80cf51b18711a</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_GIT_CLEAN_FLAGS">
      <th>
        <code>BUILDKITE_GIT_CLEAN_FLAGS</code> <a class="Docs__attribute__link" href="#BUILDKITE_GIT_CLEAN_FLAGS">#</a>

      </th>
      <td>
        <p>The value of the <code>git-clean-flags</code> <a href="/docs/agent/self-hosted/configure">agent configuration option</a>. The value can be modified by exporting the environment variable in the <code>environment</code> or <code>pre-checkout</code> hooks.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>-ffxdq</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_GIT_CLONE_FLAGS">
      <th>
        <code>BUILDKITE_GIT_CLONE_FLAGS</code> <a class="Docs__attribute__link" href="#BUILDKITE_GIT_CLONE_FLAGS">#</a>

      </th>
      <td>
        <p>The value of the <code>git-clone-flags</code> <a href="/docs/agent/self-hosted/configure">agent configuration option</a>. The value can be modified by exporting the environment variable in the <code>environment</code> or <code>pre-checkout</code> hooks.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>-v</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_GIT_FETCH_FLAGS">
      <th>
        <code>BUILDKITE_GIT_FETCH_FLAGS</code> <a class="Docs__attribute__link" href="#BUILDKITE_GIT_FETCH_FLAGS">#</a>

      </th>
      <td>
        <p>The value of the <code>git-fetch-flags</code> <a href="/docs/agent/self-hosted/configure">agent configuration option</a>. The value can be modified by exporting the environment variable in the <code>environment</code> or <code>pre-checkout</code> hooks.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>-v --prune</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_GIT_SUBMODULES">
      <th>
        <code>BUILDKITE_GIT_SUBMODULES</code> <a class="Docs__attribute__link" href="#BUILDKITE_GIT_SUBMODULES">#</a>

        <ul class="comma-separated Docs__attribute__env-var">
          <li><strong>Possible values:</strong></li>
                        <li><code>true</code></li>
                      <li><code>false</code></li>
          
          </ul>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The opposite of the value of the <code>no-git-submodules</code> <a href="/docs/agent/self-hosted/configure">agent configuration option</a>.</p>

              </td>
    </tr>
      
    <tr id="BUILDKITE_GITHUB_DEPLOYMENT_ID">
      <th>
        <code>BUILDKITE_GITHUB_DEPLOYMENT_ID</code> <a class="Docs__attribute__link" href="#BUILDKITE_GITHUB_DEPLOYMENT_ID">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The GitHub deployment ID. Only available on builds triggered by a <a href="https://developer.github.com/v3/repos/deployments/" class="external-link" target="_blank">GitHub Deployment</a>.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>87972451</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_GITHUB_DEPLOYMENT_ENVIRONMENT">
      <th>
        <code>BUILDKITE_GITHUB_DEPLOYMENT_ENVIRONMENT</code> <a class="Docs__attribute__link" href="#BUILDKITE_GITHUB_DEPLOYMENT_ENVIRONMENT">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The name of the GitHub deployment environment. Only available on builds triggered by a <a href="https://developer.github.com/v3/repos/deployments/" class="external-link" target="_blank">GitHub Deployment</a>.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>production</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_GITHUB_DEPLOYMENT_TASK">
      <th>
        <code>BUILDKITE_GITHUB_DEPLOYMENT_TASK</code> <a class="Docs__attribute__link" href="#BUILDKITE_GITHUB_DEPLOYMENT_TASK">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The name of the GitHub deployment task. Only available on builds triggered by a <a href="https://developer.github.com/v3/repos/deployments/" class="external-link" target="_blank">GitHub Deployment</a>.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>deploy</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_GITHUB_DEPLOYMENT_PAYLOAD">
      <th>
        <code>BUILDKITE_GITHUB_DEPLOYMENT_PAYLOAD</code> <a class="Docs__attribute__link" href="#BUILDKITE_GITHUB_DEPLOYMENT_PAYLOAD">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The GitHub deployment payload data as serialized JSON. Only available on builds triggered by a <a href="https://developer.github.com/v3/repos/deployments/" class="external-link" target="_blank">GitHub Deployment</a>.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>production</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_GROUP_ID">
      <th>
        <code>BUILDKITE_GROUP_ID</code> <a class="Docs__attribute__link" href="#BUILDKITE_GROUP_ID">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The UUID of the <a href="/docs/pipelines/group-step">group step</a> the job belongs to. This variable is only available if the job belongs to a group step.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>4a331026-8c9a-4714-aff0-8aa30211a34e</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_GROUP_KEY">
      <th>
        <code>BUILDKITE_GROUP_KEY</code> <a class="Docs__attribute__link" href="#BUILDKITE_GROUP_KEY">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The value of the <code>key</code> attribute of the <a href="/docs/pipelines/group-step">group step</a> the job belongs to. This variable is only available if the job belongs to a group step.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>audit-tasks</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_GROUP_LABEL">
      <th>
        <code>BUILDKITE_GROUP_LABEL</code> <a class="Docs__attribute__link" href="#BUILDKITE_GROUP_LABEL">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The label/name of the <a href="/docs/pipelines/group-step">group step</a> the job belongs to. This variable is only available if the job belongs to a group step.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>:lock: Audit</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_HOOKS_PATH">
      <th>
        <code>BUILDKITE_HOOKS_PATH</code> <a class="Docs__attribute__link" href="#BUILDKITE_HOOKS_PATH">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The value of the <code>hooks-path</code> <a href="/docs/agent/self-hosted/configure">agent configuration option</a>.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>/etc/buildkite-agent/hooks/</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_IGNORED_ENV">
      <th>
        <code>BUILDKITE_IGNORED_ENV</code> <a class="Docs__attribute__link" href="#BUILDKITE_IGNORED_ENV">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>A list of environment variables that have been set in your pipeline that are protected and will be overridden, used internally to pass data from the bootstrap to the agent.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>BUILDKITE_GIT_CLEAN_FLAGS</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_JOB_ID">
      <th>
        <code>BUILDKITE_JOB_ID</code> <a class="Docs__attribute__link" href="#BUILDKITE_JOB_ID">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The internal UUID Buildkite uses for this job.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>e44f9784-e20e-4b93-a21d-f41fd5869db9</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_JOB_CANCELLED">
      <th>
        <code>BUILDKITE_JOB_CANCELLED</code> <a class="Docs__attribute__link" href="#BUILDKITE_JOB_CANCELLED">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>Is initially undefined, but gets defined with the value <code>true</code> by the agent when the job has been canceled. This value can be used by subsequent hooks to opt out of executing.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>true</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_JOB_LOG_TMPFILE">
      <th>
        <code>BUILDKITE_JOB_LOG_TMPFILE</code> <a class="Docs__attribute__link" href="#BUILDKITE_JOB_LOG_TMPFILE">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The path to a temporary file containing the logs for this job. Requires enabling the <code>enable-job-log-tmpfile</code> <a href="/docs/agent/self-hosted/configure">agent configuration option</a>.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>/tmp/buildkite_job_log1931317484</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_LABEL">
      <th>
        <code>BUILDKITE_LABEL</code> <a class="Docs__attribute__link" href="#BUILDKITE_LABEL">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The label/name of the current job.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>:hammer: Specs</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_LAST_HOOK_EXIT_STATUS">
      <th>
        <code>BUILDKITE_LAST_HOOK_EXIT_STATUS</code> <a class="Docs__attribute__link" href="#BUILDKITE_LAST_HOOK_EXIT_STATUS">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The exit code of the last hook that ran, used internally by the hooks.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>-1</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_LOCAL_HOOKS_ENABLED">
      <th>
        <code>BUILDKITE_LOCAL_HOOKS_ENABLED</code> <a class="Docs__attribute__link" href="#BUILDKITE_LOCAL_HOOKS_ENABLED">#</a>

        <ul class="comma-separated Docs__attribute__env-var">
          <li><strong>Possible values:</strong></li>
                        <li><code>true</code></li>
                      <li><code>false</code></li>
          
          </ul>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The opposite of the value of the <code>no-local-hooks</code> <a href="/docs/agent/self-hosted/configure">agent configuration option</a>.</p>

              </td>
    </tr>
      
    <tr id="BUILDKITE_MERGE_QUEUE_BASE_BRANCH">
      <th>
        <code>BUILDKITE_MERGE_QUEUE_BASE_BRANCH</code> <a class="Docs__attribute__link" href="#BUILDKITE_MERGE_QUEUE_BASE_BRANCH">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The target branch which the merge queue build will be merged into.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>main</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_MERGE_QUEUE_BASE_COMMIT">
      <th>
        <code>BUILDKITE_MERGE_QUEUE_BASE_COMMIT</code> <a class="Docs__attribute__link" href="#BUILDKITE_MERGE_QUEUE_BASE_COMMIT">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The <a href="https://git-scm.com/docs/git-merge-base" class="external-link" target="_blank">merge base</a> of the proposed merge commit (<code>BUILDKITE_COMMIT</code>) for a merge queue build.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>44af8aa0007898d08f1bec401df7c077c1df0722</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_MESSAGE">
      <th>
        <code>BUILDKITE_MESSAGE</code> <a class="Docs__attribute__link" href="#BUILDKITE_MESSAGE">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The message associated with the build, usually the commit message or the message provided when the build is triggered. The value is empty when a message is not set. For example, when a user triggers a build from the Buildkite dashboard without entering a message, the variable returns an empty value.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>Added a great new feature</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_ORGANIZATION_ID">
      <th>
        <code>BUILDKITE_ORGANIZATION_ID</code> <a class="Docs__attribute__link" href="#BUILDKITE_ORGANIZATION_ID">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The UUID of the organization.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>6abcd532-f9b7-41e9-8717-40fb75a82b5d</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_ORGANIZATION_SLUG">
      <th>
        <code>BUILDKITE_ORGANIZATION_SLUG</code> <a class="Docs__attribute__link" href="#BUILDKITE_ORGANIZATION_SLUG">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The organization name on Buildkite as used in URLs.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>acme-inc</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_PARALLEL_JOB">
      <th>
        <code>BUILDKITE_PARALLEL_JOB</code> <a class="Docs__attribute__link" href="#BUILDKITE_PARALLEL_JOB">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The index of each parallel job created from a parallel build step, starting from 0. For a build step with <code>parallelism: 5</code>, the value would be 0, 1, 2, 3, and 4 respectively.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>0</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_PARALLEL_JOB_COUNT">
      <th>
        <code>BUILDKITE_PARALLEL_JOB_COUNT</code> <a class="Docs__attribute__link" href="#BUILDKITE_PARALLEL_JOB_COUNT">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The total number of parallel jobs created from a parallel build step. For a build step with <code>parallelism: 5</code>, the value is 5.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>5</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_PIPELINE_DEFAULT_BRANCH">
      <th>
        <code>BUILDKITE_PIPELINE_DEFAULT_BRANCH</code> <a class="Docs__attribute__link" href="#BUILDKITE_PIPELINE_DEFAULT_BRANCH">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The default branch for this pipeline.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>main</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_PIPELINE_ID">
      <th>
        <code>BUILDKITE_PIPELINE_ID</code> <a class="Docs__attribute__link" href="#BUILDKITE_PIPELINE_ID">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The UUID of the pipeline.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>d18439cc-df59-45b0-97cc-98d7fb69d983</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_PIPELINE_NAME">
      <th>
        <code>BUILDKITE_PIPELINE_NAME</code> <a class="Docs__attribute__link" href="#BUILDKITE_PIPELINE_NAME">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The displayed pipeline name on Buildkite.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>my_project</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_PIPELINE_PROVIDER">
      <th>
        <code>BUILDKITE_PIPELINE_PROVIDER</code> <a class="Docs__attribute__link" href="#BUILDKITE_PIPELINE_PROVIDER">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The ID of the source code provider for the pipeline's repository.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>github</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_PIPELINE_SLUG">
      <th>
        <code>BUILDKITE_PIPELINE_SLUG</code> <a class="Docs__attribute__link" href="#BUILDKITE_PIPELINE_SLUG">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The pipeline slug on Buildkite as used in URLs.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>my-project</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_PIPELINE_TEAMS">
      <th>
        <code>BUILDKITE_PIPELINE_TEAMS</code> <a class="Docs__attribute__link" href="#BUILDKITE_PIPELINE_TEAMS">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>A colon separated list of the pipeline's non-private team slugs.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>deploy:ops:production</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_PLUGIN_CONFIGURATION">
      <th>
        <code>BUILDKITE_PLUGIN_CONFIGURATION</code> <a class="Docs__attribute__link" href="#BUILDKITE_PLUGIN_CONFIGURATION">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>A JSON string holding the current plugin's configuration (as opposed to all the plugin configurations in the <code>BUILDKITE_PLUGINS</code> environment variable).</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>{"image":"node:lts-alpine3.14"}</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_PLUGIN_NAME">
      <th>
        <code>BUILDKITE_PLUGIN_NAME</code> <a class="Docs__attribute__link" href="#BUILDKITE_PLUGIN_NAME">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The current plugin's name, with all letters in uppercase and any spaces replaced with underscores.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>DOCKER</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_PLUGINS">
      <th>
        <code>BUILDKITE_PLUGINS</code> <a class="Docs__attribute__link" href="#BUILDKITE_PLUGINS">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>A JSON object containing a list plugins used in the step, and their configuration.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>[{"github.com/buildkite-plugins/docker-buildkite-plugin#v3.7.0":{"image":"node:lts-alpine3.14"}}]</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_PLUGINS_ENABLED">
      <th>
        <code>BUILDKITE_PLUGINS_ENABLED</code> <a class="Docs__attribute__link" href="#BUILDKITE_PLUGINS_ENABLED">#</a>

        <ul class="comma-separated Docs__attribute__env-var">
          <li><strong>Possible values:</strong></li>
                        <li><code>true</code></li>
                      <li><code>false</code></li>
          
          </ul>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The opposite of the value of the <code>no-plugins</code> <a href="/docs/agent/self-hosted/configure">agent configuration option</a>.</p>

              </td>
    </tr>
      
    <tr id="BUILDKITE_PLUGINS_PATH">
      <th>
        <code>BUILDKITE_PLUGINS_PATH</code> <a class="Docs__attribute__link" href="#BUILDKITE_PLUGINS_PATH">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The value of the <code>plugins-path</code> <a href="/docs/agent/self-hosted/configure">agent configuration option</a>.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>/etc/buildkite-agent/plugins/</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_PLUGIN_VALIDATION">
      <th>
        <code>BUILDKITE_PLUGIN_VALIDATION</code> <a class="Docs__attribute__link" href="#BUILDKITE_PLUGIN_VALIDATION">#</a>
        
          <p class="Docs__attribute__env-var">
            <strong>Default</strong>:
            <code>false</code>
          </p>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>Whether to validate plugin configuration and requirements. The value can be modified by exporting the environment variable in the <code>environment</code> or <code>pre-checkout</code> hooks, or in a <code>pipeline.yml</code> file. It can also be enabled using the <code>no-plugin-validation</code> <a href="/docs/agent/self-hosted/configure">agent configuration option</a>.</p>

              </td>
    </tr>
      
    <tr id="BUILDKITE_PULL_REQUEST">
      <th>
        <code>BUILDKITE_PULL_REQUEST</code> <a class="Docs__attribute__link" href="#BUILDKITE_PULL_REQUEST">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The number of the pull request or <code>false</code> if not a pull request.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>123</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_PULL_REQUEST_BASE_BRANCH">
      <th>
        <code>BUILDKITE_PULL_REQUEST_BASE_BRANCH</code> <a class="Docs__attribute__link" href="#BUILDKITE_PULL_REQUEST_BASE_BRANCH">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The base branch that the pull request is targeting or <code>""</code> if not a pull request.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>main</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_PULL_REQUEST_DRAFT">
      <th>
        <code>BUILDKITE_PULL_REQUEST_DRAFT</code> <a class="Docs__attribute__link" href="#BUILDKITE_PULL_REQUEST_DRAFT">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>Set to <code>true</code> when the pull request is a draft. This variable is only available if a build contains a draft pull request.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>true</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_PULL_REQUEST_LABELS">
      <th>
        <code>BUILDKITE_PULL_REQUEST_LABELS</code> <a class="Docs__attribute__link" href="#BUILDKITE_PULL_REQUEST_LABELS">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>A comma-separated list of labels attached to the pull request, or <code>""</code> if not a pull request or no labels are attached.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>label1,label2</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_PULL_REQUEST_REPO">
      <th>
        <code>BUILDKITE_PULL_REQUEST_REPO</code> <a class="Docs__attribute__link" href="#BUILDKITE_PULL_REQUEST_REPO">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The repository URL of the pull request or <code>""</code> if not a pull request.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>git://github.com/acme-inc/my-project.git</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_REBUILT_FROM_BUILD_ID">
      <th>
        <code>BUILDKITE_REBUILT_FROM_BUILD_ID</code> <a class="Docs__attribute__link" href="#BUILDKITE_REBUILT_FROM_BUILD_ID">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The UUID of the original build this was rebuilt from or <code>""</code> if not a rebuild.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>4735ba57-80d0-46e2-8fa0-b28223a86586</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_REBUILT_FROM_BUILD_NUMBER">
      <th>
        <code>BUILDKITE_REBUILT_FROM_BUILD_NUMBER</code> <a class="Docs__attribute__link" href="#BUILDKITE_REBUILT_FROM_BUILD_NUMBER">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The number of the original build this was rebuilt from or <code>""</code> if not a rebuild.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>1514</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_REFSPEC">
      <th>
        <code>BUILDKITE_REFSPEC</code> <a class="Docs__attribute__link" href="#BUILDKITE_REFSPEC">#</a>

      </th>
      <td>
        <p>A custom refspec for the buildkite-agent bootstrap script to use when checking out code. This variable can be modified by exporting the environment variable in the <code>environment</code> or <code>pre-checkout</code> hooks.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>+refs/weird/123abc:refs/local/weird/456</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_REPO">
      <th>
        <code>BUILDKITE_REPO</code> <a class="Docs__attribute__link" href="#BUILDKITE_REPO">#</a>

      </th>
      <td>
        <p>The repository of your pipeline. This variable can be set by exporting the environment variable in the <code>environment</code> or <code>pre-checkout</code> hooks.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>git@github.com:acme-inc/my-project.git</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_REPO_MIRROR">
      <th>
        <code>BUILDKITE_REPO_MIRROR</code> <a class="Docs__attribute__link" href="#BUILDKITE_REPO_MIRROR">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The path to the shared git mirror. Introduced in <a href="https://github.com/buildkite/agent/releases/tag/v3.47.0" class="external-link" target="_blank">v3.47.0</a>.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>/tmp/buildkite-git-mirrors</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_RETRY_COUNT">
      <th>
        <code>BUILDKITE_RETRY_COUNT</code> <a class="Docs__attribute__link" href="#BUILDKITE_RETRY_COUNT">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>How many times this job has been retried.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>0</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_S3_ACCESS_KEY_ID">
      <th>
        <code>BUILDKITE_S3_ACCESS_KEY_ID</code> <a class="Docs__attribute__link" href="#BUILDKITE_S3_ACCESS_KEY_ID">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The access key ID for your S3 IAM user, for use with <a href="/docs/agent/cli/reference/artifact#using-your-private-aws-s3-bucket">private S3 buckets</a>. The variable is read by the <code>buildkite-agent artifact upload</code> command, and during the artifact upload phase of <a href="/docs/pipelines/command-step#command-step-attributes">command steps</a>. The value can only be set by exporting the environment variable in the <code>environment</code>, <code>pre-checkout</code> or <code>pre-command</code> hooks.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>AKIAIOSFODNN7EXAMPLE</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_S3_ACCESS_URL">
      <th>
        <code>BUILDKITE_S3_ACCESS_URL</code> <a class="Docs__attribute__link" href="#BUILDKITE_S3_ACCESS_URL">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The access URL for your <a href="/docs/agent/cli/reference/artifact#using-your-private-aws-s3-bucket">private S3 bucket</a>, if you are using a proxy. The variable is read by the <code>buildkite-agent artifact upload</code> command, as well as during the artifact upload phase of <a href="/docs/pipelines/command-step#command-step-attributes">command steps</a>. The value can only be set by exporting the environment variable in the <code>environment</code>, <code>pre-checkout</code> or <code>pre-command</code> hooks.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>https://buildkite-artifacts.example.com/</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_S3_ACL">
      <th>
        <code>BUILDKITE_S3_ACL</code> <a class="Docs__attribute__link" href="#BUILDKITE_S3_ACL">#</a>
        
          <p class="Docs__attribute__env-var">
            <strong>Default</strong>:
            <code>public-read</code>
          </p>

        <ul class="comma-separated Docs__attribute__env-var">
          <li><strong>Possible values:</strong></li>
                        <li><code>private</code></li>
                      <li><code>public-read-write</code></li>
                      <li><code>public-read</code></li>
                      <li><code>authenticated-read</code></li>
                      <li><code>bucket-owner-read</code></li>
                      <li><code>bucket-owner-full-control</code></li>
          
          </ul>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The Access Control List to be set on artifacts being uploaded to your <a href="/docs/agent/cli/reference/artifact#using-your-private-aws-s3-bucket">private S3 bucket</a>. The variable is read by the <code>buildkite-agent artifact upload</code> command, as well as during the artifact upload phase of <a href="/docs/pipelines/command-step#command-step-attributes">command steps</a>. The value can only be set by exporting the environment variable in the <code>environment</code>, <code>pre-checkout</code> or <code>pre-command</code> hooks.</p>

<p>Must be one of the following values which map to <a href="https://docs.aws.amazon.com/AmazonS3/latest/dev/acl-overview.html#canned-acl" class="external-link" target="_blank">S3 Canned ACL grants</a>.</p>

              </td>
    </tr>
      
    <tr id="BUILDKITE_S3_DEFAULT_REGION">
      <th>
        <code>BUILDKITE_S3_DEFAULT_REGION</code> <a class="Docs__attribute__link" href="#BUILDKITE_S3_DEFAULT_REGION">#</a>
        
          <p class="Docs__attribute__env-var">
            <strong>Default</strong>:
            <code>us-east-1</code>
          </p>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The region of your <a href="/docs/agent/cli/reference/artifact#using-your-private-aws-s3-bucket">private S3 bucket</a>. The variable is read by the <code>buildkite-agent artifact upload</code> command, as well as during the artifact upload phase of <a href="/docs/pipelines/command-step#command-step-attributes">command steps</a>. The value can only be set by exporting the environment variable in the <code>environment</code>, <code>pre-checkout</code> or <code>pre-command</code> hooks.</p>

              </td>
    </tr>
      
    <tr id="BUILDKITE_S3_SECRET_ACCESS_KEY">
      <th>
        <code>BUILDKITE_S3_SECRET_ACCESS_KEY</code> <a class="Docs__attribute__link" href="#BUILDKITE_S3_SECRET_ACCESS_KEY">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The secret access key for your S3 IAM user, for use with <a href="/docs/agent/cli/reference/artifact#using-your-private-aws-s3-bucket">private S3 buckets</a>. The variable is read by the <code>buildkite-agent artifact upload</code> command, as well as during the artifact upload phase of <a href="/docs/pipelines/command-step#command-step-attributes">command steps</a>. The value can only be set by exporting the environment variable in the <code>environment</code>, <code>pre-checkout</code> or <code>pre-command</code> hooks. Do not print or export this variable anywhere except your agent hooks.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_S3_SSE_ENABLED">
      <th>
        <code>BUILDKITE_S3_SSE_ENABLED</code> <a class="Docs__attribute__link" href="#BUILDKITE_S3_SSE_ENABLED">#</a>
        
          <p class="Docs__attribute__env-var">
            <strong>Default</strong>:
            <code>false</code>
          </p>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>Whether to enable encryption for the artifacts in your <a href="/docs/agent/cli/reference/artifact#using-your-private-aws-s3-bucket">private S3 bucket</a>. The variable is read by the <code>buildkite-agent artifact upload</code> command, as well as during the artifact upload phase of <a href="/docs/pipelines/command-step#command-step-attributes">command steps</a>. The value can only be set by exporting the environment variable in the <code>environment</code>, <code>pre-checkout</code> or <code>pre-command</code> hooks.</p>

              </td>
    </tr>
      
    <tr id="BUILDKITE_SHELL">
      <th>
        <code>BUILDKITE_SHELL</code> <a class="Docs__attribute__link" href="#BUILDKITE_SHELL">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The value of the <code>shell</code> <a href="/docs/agent/self-hosted/configure">agent configuration option</a>.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>"/bin/bash -e -c"</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_SOURCE">
      <th>
        <code>BUILDKITE_SOURCE</code> <a class="Docs__attribute__link" href="#BUILDKITE_SOURCE">#</a>

        <ul class="comma-separated Docs__attribute__env-var">
          <li><strong>Possible values:</strong></li>
                        <li><code>webhook</code></li>
                      <li><code>api</code></li>
                      <li><code>ui</code></li>
                      <li><code>trigger_job</code></li>
                      <li><code>schedule</code></li>
          
          </ul>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The source of the event that created the build.</p>

              </td>
    </tr>
      
    <tr id="BUILDKITE_SSH_KEYSCAN">
      <th>
        <code>BUILDKITE_SSH_KEYSCAN</code> <a class="Docs__attribute__link" href="#BUILDKITE_SSH_KEYSCAN">#</a>

        <ul class="comma-separated Docs__attribute__env-var">
          <li><strong>Possible values:</strong></li>
                        <li><code>true</code></li>
                      <li><code>false</code></li>
          
          </ul>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The opposite of the value of the <code>no-ssh-keyscan</code> <a href="/docs/agent/self-hosted/configure">agent configuration option</a>.</p>

              </td>
    </tr>
      
    <tr id="BUILDKITE_STEP_ID">
      <th>
        <code>BUILDKITE_STEP_ID</code> <a class="Docs__attribute__link" href="#BUILDKITE_STEP_ID">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>A unique string that identifies a step.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>080b7d73-986d-4a39-a510-b34f9faf4710</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_STEP_KEY">
      <th>
        <code>BUILDKITE_STEP_KEY</code> <a class="Docs__attribute__link" href="#BUILDKITE_STEP_KEY">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The value of the <code>key</code> <a href="/docs/pipelines/command-step#command-step-attributes">command step attribute</a>, a unique string set by you to identify a step.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>tests-06</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_TAG">
      <th>
        <code>BUILDKITE_TAG</code> <a class="Docs__attribute__link" href="#BUILDKITE_TAG">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The name of the tag being built, if this build was triggered from a tag.</p>

<p>When a build is triggered by a GitHub webhook tag <code>push</code> event, <code>BUILDKITE_BRANCH</code> will also be set to the name of the tag being built.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>v1.2.3</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_TIMEOUT">
      <th>
        <code>BUILDKITE_TIMEOUT</code> <a class="Docs__attribute__link" href="#BUILDKITE_TIMEOUT">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The number of minutes until Buildkite automatically cancels this job, if a timeout has been specified, otherwise it <code>false</code> if no timeout is set. Jobs that time out with an exit status of 0 are marked as "passed".</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>15</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_TRACING_BACKEND">
      <th>
        <code>BUILDKITE_TRACING_BACKEND</code> <a class="Docs__attribute__link" href="#BUILDKITE_TRACING_BACKEND">#</a>
        
          <p class="Docs__attribute__env-var">
            <strong>Default</strong>:
            <code></code>
          </p>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>Set to <code>"datadog"</code> to send metrics to the <a href="https://docs.datadoghq.com/tracing/" class="external-link" target="_blank">Datadog APM</a> using <code>localhost:8126</code>, or <code>DD_AGENT_HOST:DD_AGENT_APM_PORT</code>.</p>

<p>Also available as a <a href="/docs/agent/self-hosted/configure#configuration-settings">buildkite agent configuration option.</a></p>

          <p>
            <strong class="h5">Example:</strong>
            <code>datadog</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_TRIGGERED_FROM_BUILD_ID">
      <th>
        <code>BUILDKITE_TRIGGERED_FROM_BUILD_ID</code> <a class="Docs__attribute__link" href="#BUILDKITE_TRIGGERED_FROM_BUILD_ID">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The UUID of the build that triggered this build. This will be empty if the build was not triggered from another build.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>5aa7c894-c8c0-435b-bc17-13923b90f163</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_TRIGGERED_FROM_BUILD_NUMBER">
      <th>
        <code>BUILDKITE_TRIGGERED_FROM_BUILD_NUMBER</code> <a class="Docs__attribute__link" href="#BUILDKITE_TRIGGERED_FROM_BUILD_NUMBER">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The number of the build that triggered this build or <code>""</code> if the build was not triggered from another build.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>1264</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_TRIGGERED_FROM_BUILD_PIPELINE_SLUG">
      <th>
        <code>BUILDKITE_TRIGGERED_FROM_BUILD_PIPELINE_SLUG</code> <a class="Docs__attribute__link" href="#BUILDKITE_TRIGGERED_FROM_BUILD_PIPELINE_SLUG">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The slug of the pipeline that was used to trigger this build or <code>""</code> if the build was not triggered from another build.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>build-and-test</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_UNBLOCKER">
      <th>
        <code>BUILDKITE_UNBLOCKER</code> <a class="Docs__attribute__link" href="#BUILDKITE_UNBLOCKER">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The name of the user who unblocked the build.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>Carol Danvers</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_UNBLOCKER_EMAIL">
      <th>
        <code>BUILDKITE_UNBLOCKER_EMAIL</code> <a class="Docs__attribute__link" href="#BUILDKITE_UNBLOCKER_EMAIL">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The notification email of the user who unblocked the build.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>carol@nasa.gov</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_UNBLOCKER_ID">
      <th>
        <code>BUILDKITE_UNBLOCKER_ID</code> <a class="Docs__attribute__link" href="#BUILDKITE_UNBLOCKER_ID">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>The UUID of the user who unblocked the build.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>4735ba57-80d0-46e2-8fa0-b28223a86586</code>
          </p>
              </td>
    </tr>
      
    <tr id="BUILDKITE_UNBLOCKER_TEAMS">
      <th>
        <code>BUILDKITE_UNBLOCKER_TEAMS</code> <a class="Docs__attribute__link" href="#BUILDKITE_UNBLOCKER_TEAMS">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>A colon separated list of non-private team slugs that the user who unblocked the build belongs to.</p>

          <p>
            <strong class="h5">Example:</strong>
            <code>everyone:platform</code>
          </p>
              </td>
    </tr>
      
    <tr id="CI">
      <th>
        <code>CI</code> <a class="Docs__attribute__link" href="#CI">#</a>

          <small>This value cannot be modified</small>
        
      </th>
      <td>
        <p>Always <code>true</code>.</p>

              </td>
    </tr>
    </tbody>
</table>

## Deprecated environment variables

The following environment variables have been deprecated.

<table class="responsive-table">
<tbody>
  <tr>
    <th><code>BUILDKITE_PROJECT_PROVIDER</code></th>
    <td>This has been renamed to <code>BUILDKITE_PIPELINE_PROVIDER</code>.</td>
  </tr>
  <tr>
    <th><code>BUILDKITE_PROJECT_SLUG</code></th>
    <td>This has been renamed to <code>BUILDKITE_PIPELINE_SLUG</code>.</td>
  </tr>
  <tr>
    <th><code>BUILDKITE_SCRIPT_PATH</code></th>
    <td>This has been renamed to <code>BUILDKITE_COMMAND</code></td>
  </tr>
  <tr>
    <th><code>BUILDKITE_STEP_IDENTIFIER</code></th>
    <td>This has been renamed to <code>BUILDKITE_STEP_KEY</code></td>
  </tr>
  <tr>
    <th><code>BUILDBOX_AGENT_ID</code></th>
    <td>This has been renamed to <code>BUILDKITE_AGENT_ID</code></td>
  </tr>
  <tr>
    <th><code>BUILDBOX_AGENT_NAME</code></th>
    <td>This has been renamed to <code>BUILDKITE_AGENT_NAME</code></td>
  </tr>
  <tr>
    <th><code>BUILDBOX_AGENT_META_DATA_*</code></th>
    <td>This has been renamed to <code>BUILDKITE_AGENT_META_DATA_*</code></td>
  </tr>
  <tr>
    <th><code>BUILDBOX_AGENT_ACCESS_TOKEN</code></th>
    <td>This has been renamed to <code>BUILDKITE_AGENT_ACCESS_TOKEN</code></td>
  </tr>
  <tr>
    <th><code>BUILDBOX_AGENT_API_URL</code></th>
    <td>This has been removed with no replacement</td>
  </tr>
</tbody>
</table>

## Defining your own

You can define environment variables in your jobs in a few ways, depending on the nature of the value being set:

- The **YAML Steps editor** in your pipeline settings, using a top-level `env` attribute before your steps — for values that are *not secret*.
- [Build pipeline configuration](/docs/pipelines/configure/step-types/command-step) — for values that are *not secret*.
- An `environment` or `pre-command` [agent hook](/docs/agent/hooks) — for values that are secret or agent-specific.

> 🚧 Secrets in environment variables
> Do not print or export secrets in your pipelines. See the [Secrets](/docs/pipelines/security/secrets/managing) documentation for further information and best practices.

## Variable interpolation

Any environment variables set by Buildkite will be interpolated by the Agent.

If you're using the **YAML Steps editor** to define your pipeline, only the following subset of the environment variables are available:

- `BUILDKITE_BRANCH`
- `BUILDKITE_TAG`
- `BUILDKITE_MESSAGE`
- `BUILDKITE_COMMIT`
- `BUILDKITE_PIPELINE_SLUG`
- `BUILDKITE_PIPELINE_NAME`
- `BUILDKITE_PIPELINE_ID`
- `BUILDKITE_ORGANIZATION_SLUG`
- `BUILDKITE_TRIGGERED_FROM_BUILD_PIPELINE_SLUG`
- `BUILDKITE_REPO`
- `BUILDKITE_PULL_REQUEST`
- `BUILDKITE_PULL_REQUEST_BASE_BRANCH`
- `BUILDKITE_PULL_REQUEST_REPO`
- `BUILDKITE_MERGE_QUEUE_BASE_BRANCH`
- `BUILDKITE_MERGE_QUEUE_BASE_COMMIT`

Some variables, for example `BUILDKITE_BUILD_NUMBER`, cannot be supported in the **YAML Steps editor** as the interpolation happens before the build is created. In those cases, interpolate them at the [runtime](/docs/pipelines/configure/environment-variables#runtime-variable-interpolation).

Alternatively, you can also access the rest of the Buildkite [environment variables](/docs/pipelines/configure/environment-variables#buildkite-environment-variables) by using a `pipeline.yml` file. Either define your entire pipeline in the YAML file, or you do a [pipeline upload](/docs/agent/cli/reference/pipeline) part way through your build that adds only the steps that use environment variables. See the [dynamic pipelines](/docs/pipelines/configure/dynamic-pipelines) docs for more information about adding steps with pipeline uploads.

## Runtime variable interpolation

When using environment variables that will be evaluated at run-time, make sure you escape the `$` character using `$$` or `\$`. For example:

```yml
- command: "deploy.sh $$SERVER"
  env:
    SERVER: "server-a"
```

Further details about environment variable interpolation can be found in the [pipeline upload](/docs/agent/cli/reference/pipeline#environment-variable-substitution) CLI guide.

## Environment variable precedence

You can set environment variables in lots of different places, and which ones take precedence can get a little confusing.
There are many different levels at which environment variables are merged together. The following walkthrough and examples demonstrate the order in which variables are combined, as if you had set variables in every available place.

### Job environment

When a job runs on an agent, the first combination of environment variables happens in the job environment itself. This is the environment you can see in a job's Environment tab in the Buildkite dashboard, and the one returned by the REST and GraphQL APIs.

> 📘
> If you are not using YAML steps, the precedence of environment variables is different from the list below.
> Please [migrate your pipelines](/docs/pipelines/tutorials/pipeline-upgrade) to use YAML steps.

The job environment is made by merging the following sets of values, where values in each successive set take precedence:

<table>
<tbody>
  <tr>
    <th><em>Pipeline</em></th>
    <td>Optional variables set by you in the YAML Steps editor using a top-level <code>env</code> attribute</td>
  </tr>
  <tr>
    <th><em>Build</em></th>
    <td>Optional variables set by you on the build when creating a new build in the UI or using the REST API</td>
  </tr>
    <tr>
    <th><em>Step</em></th>
    <td>Optional variables set by you on a step in the YAML steps editor or a pipeline.yml file</td>
  </tr>
  <tr>
    <th><em>Standard</em></th>
    <td>The set of variables provided by Buildkite to every job</td>
  </tr>
</tbody>
</table>

For example, if you had configured the following environment variables:

<table>
  <tbody>
    <tr>
      <th><em>Pipeline</em></th>
      <td><code>MY_ENV1="a"</code></td>
    </tr>
    <tr>
      <th><em>Build</em></th>
      <td><code>MY_ENV1="b"</code></td>
    </tr>
        <tr>
      <th><em>Step</em></th>
      <td><code>MY_ENV1="c"</code></td>
    </tr>
  </tbody>
</table>

In the final job environment, the value of `MY_ENV1` would be `"c"`.

#### Setting variables in a pipeline.yml

There are two places in a pipeline.yml file that you can set environment variables:

  1. In the `env` attribute of command and trigger steps.
  1. In the `env` attribute at the top of the yaml file, before you define your pipeline's steps.

Defining an environment variable at the top of your yaml file will set that variable on each of the command steps in the pipeline that have not already started running, and is equivalent to setting the `env` attribute on every step. This includes further pipeline uploads through `buildkite-agent pipeline upload`.

> 🚧 Concurrent pipeline uploads and environment variables
> Concurrent pipeline uploads with build-level environment variables can cause unpredictable behavior by modifying the environment for steps that haven't started yet.
> This affects steps running after pipeline uploads, signed pipeline steps (where environment variables affect signature verification), and jobs that depend on specific environment variable values.
> Issues typically occur when multiple pipeline uploads that include build-level environment variables happen at the same time or set the same environment variable to different values.

#### Setting variables in a Trigger step

Environment variables are not automatically passed through to builds created with [trigger steps](/docs/pipelines/configure/step-types/trigger-step). To set build-level environment variables on triggered builds, set the trigger step's `env` attribute.

### Agent environment

Separate to the job's base environment, your `buildkite-agent` process has an environment of its own. This is made up of:

- operating system environment variables
- any variables you set on your agent when you started it
- any environment variables that were inherited from how you started the process (for example, systemd sets some env vars for you)

For a list of variables and configuration flags, you can set on your agent, see the Buildkite agent's [start command documentation](/docs/agent/cli/reference/start).

> 📘
> When using the [Agent Stack for Kubernetes](/docs/agent/self-hosted/agent-stack-k8s) controller, environment variables declared as part of a PodSpec will also take precedence when the Kubernetes job is created. Learn more about this in [Kubernetes PodSpec generation](/docs/agent/self-hosted/agent-stack-k8s/podspec#kubernetes-podspec-generation).

### Job runtime environment

Once the job is accepted by an agent, more environment merging happens. Starting with the environment that we put together in the [Job Environment section](#environment-variable-precedence-job-environment), we merge in some of the variables from the agent environment.

> 📘
> Not all variables from the agent are available in the job runtime. For example, we remove the agent's registration token and replace it with a build session token that has limited permissions. This new session token is used when you run the `artifact`, `meta-data` and `pipeline` commands inside the job.

After the agent variables have been merged, the bootstrap script is run.

The bootstrap runs any hooks that have been defined by your
[agent](/docs/agent/hooks#hook-locations-agent-hooks), your [repository](/docs/agent/hooks#hook-locations-repository-hooks) or [plugins](/docs/agent/hooks#hook-locations-plugin-hooks).
Variables that are set in these hooks will be merged into the runtime
environment, and will override any previous values that are set.

> 🚧 Take care with environment variables in hooks
> Variables that are defined in hooks can override anything that exists in the environment.

This is the environment your command runs in 🎉

Finally, if your job's commands make any changes to the environment, those changes will only survive as long as the script is running.
