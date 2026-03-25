# Source: https://buildkite.com/docs/platform/cli/reference/configure.md

# Source: https://buildkite.com/docs/pipelines/configure.md

# Source: https://buildkite.com/docs/agent/self-hosted/configure.md

# Buildkite agent configuration

Every agent installer comes with a configuration file. You can also customize many of the configuration values using environment variables.

## Example configuration file

```sh
token="24db61df8338027652b24aadf82dd483b016eef98fcd332815"
name="my-app-%spawn"
tags="ci=true,docker=true"
git-clean-flags="-ffdqx"
debug=true
```

{: codeblock-file="/buildkite/buildkite-agent.cfg"}

You can find the directory location of your configuration file in your platform's installation documentation. You can also set this folder using the `--config` command line argument or the `BUILDKITE_AGENT_CONFIG` environment variable.

```sh
BUILDKITE_AGENT_CONFIG="/etc/buildkite-agent/custom-config-files-dir" buildkite-agent start
```

## Configuration settings

<table class="Docs__attribute__table">
  <colgroup>
    <col>
    <col>
  </colgroup>
  <tbody>
    <tr class="importance required"><th>Required</th></tr>

        <tr id="build-path">
          <th>
            <code>build-path<a class="Docs__attribute__link" href="#build-path">#</a></code>
            <span class="Docs__attribute__importance">Required</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_BUILD_PATH
</code>
            </p>

          </th>
          <td>
            <p>Path to where the builds will run from</p>
          </td>
        </tr>
                                                                                                                                                                                                                                                                                                                                                                                                                                
        <tr id="token">
          <th>
            <code>token<a class="Docs__attribute__link" href="#token">#</a></code>
            <span class="Docs__attribute__importance">Required</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_AGENT_TOKEN
</code>
            </p>

          </th>
          <td>
            <p>Your account agent token</p>
          </td>
        </tr>
                                                                                                                                      <tr class="importance optional"><th>Optional</th></tr>
          
        <tr id="no-color">
          <th>
            <code>no-color<a class="Docs__attribute__link" href="#no-color">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_AGENT_NO_COLOR
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>false
</code>
            </p>

          </th>
          <td>
            
            <p>Don't show colors in logging</p>
          </td>
        </tr>
                
        <tr id="debug">
          <th>
            <code>debug<a class="Docs__attribute__link" href="#debug">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_AGENT_DEBUG
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>false
</code>
            </p>

          </th>
          <td>
            
            <p>Enable debug mode. Synonym for ′--log-level debug′. Takes precedence over ′--log-level′</p>
          </td>
        </tr>
                
        <tr id="log-level">
          <th>
            <code>log-level<a class="Docs__attribute__link" href="#log-level">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_AGENT_LOG_LEVEL
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>"notice"
</code>
            </p>

          </th>
          <td>
            
            <p>Set the log level for the agent, making logging more or less verbose. Defaults to notice. Allowed values are: debug, info, error, warn, fatal</p>
          </td>
        </tr>
                
        <tr id="experiment">
          <th>
            <code>experiment<a class="Docs__attribute__link" href="#experiment">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_AGENT_EXPERIMENT
</code>
            </p>

          </th>
          <td>
            
            <p>Enable experimental features within the buildkite-agent</p>
          </td>
        </tr>
                
        <tr id="profile">
          <th>
            <code>profile<a class="Docs__attribute__link" href="#profile">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_AGENT_PROFILE
</code>
            </p>

          </th>
          <td>
            
            <p>Enable a profiling mode, either cpu, memory, mutex or block</p>
          </td>
        </tr>
                
        <tr id="name">
          <th>
            <code>name<a class="Docs__attribute__link" href="#name">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_AGENT_NAME
</code>
            </p>

          </th>
          <td>
            
            <p>The name of the agent</p>
          </td>
        </tr>
                
        <tr id="priority">
          <th>
            <code>priority<a class="Docs__attribute__link" href="#priority">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_AGENT_PRIORITY
</code>
            </p>

          </th>
          <td>
            
            <p>The priority of the agent (higher priorities are assigned work first)</p>
          </td>
        </tr>
                
        <tr id="acquire-job">
          <th>
            <code>acquire-job<a class="Docs__attribute__link" href="#acquire-job">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_AGENT_ACQUIRE_JOB
</code>
            </p>

          </th>
          <td>
            
            <p>Start this agent and only run the specified job, disconnecting after it's finished</p>
          </td>
        </tr>
                
        <tr id="reflect-exit-status">
          <th>
            <code>reflect-exit-status<a class="Docs__attribute__link" href="#reflect-exit-status">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_AGENT_REFLECT_EXIT_STATUS
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>false
</code>
            </p>

          </th>
          <td>
            
            <p>When used with --acquire-job, causes the agent to exit with the same exit status as the job</p>
          </td>
        </tr>
                
        <tr id="disconnect-after-job">
          <th>
            <code>disconnect-after-job<a class="Docs__attribute__link" href="#disconnect-after-job">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_AGENT_DISCONNECT_AFTER_JOB
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>false
</code>
            </p>

          </th>
          <td>
            
            <p>Disconnect the agent after running exactly one job. When used in conjunction with the ′--spawn′ flag, each worker booted will run exactly one job</p>
          </td>
        </tr>
                
        <tr id="disconnect-after-idle-timeout">
          <th>
            <code>disconnect-after-idle-timeout<a class="Docs__attribute__link" href="#disconnect-after-idle-timeout">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_AGENT_DISCONNECT_AFTER_IDLE_TIMEOUT
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>0
</code>
            </p>

          </th>
          <td>
            
            <p>The maximum idle time in seconds to wait for a job before disconnecting. The default of 0 means no timeout</p>
          </td>
        </tr>
                
        <tr id="disconnect-after-uptime">
          <th>
            <code>disconnect-after-uptime<a class="Docs__attribute__link" href="#disconnect-after-uptime">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_AGENT_DISCONNECT_AFTER_UPTIME
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>0
</code>
            </p>

          </th>
          <td>
            
            <p>The maximum uptime in seconds before the agent stops accepting new jobs and shuts down after any running jobs complete. The default of 0 means no timeout</p>
          </td>
        </tr>
                
        <tr id="cancel-grace-period">
          <th>
            <code>cancel-grace-period<a class="Docs__attribute__link" href="#cancel-grace-period">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_CANCEL_GRACE_PERIOD
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>10
</code>
            </p>

          </th>
          <td>
            
            <p>The number of seconds a canceled or timed out job is given to gracefully terminate and upload its artifacts</p>
          </td>
        </tr>
                
        <tr id="enable-job-log-tmpfile">
          <th>
            <code>enable-job-log-tmpfile<a class="Docs__attribute__link" href="#enable-job-log-tmpfile">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_ENABLE_JOB_LOG_TMPFILE
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>false
</code>
            </p>

          </th>
          <td>
            
            <p>Store the job logs in a temporary file ′BUILDKITE_JOB_LOG_TMPFILE′ that is accessible during the job and removed at the end of the job</p>
          </td>
        </tr>
                
        <tr id="job-log-path">
          <th>
            <code>job-log-path<a class="Docs__attribute__link" href="#job-log-path">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_JOB_LOG_PATH
</code>
            </p>

          </th>
          <td>
            
            <p>Location to store job logs created by configuring ′enable-job-log-tmpfile`, by default job log will be stored in TempDir</p>
          </td>
        </tr>
                
        <tr id="write-job-logs-to-stdout">
          <th>
            <code>write-job-logs-to-stdout<a class="Docs__attribute__link" href="#write-job-logs-to-stdout">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_WRITE_JOB_LOGS_TO_STDOUT
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>false
</code>
            </p>

          </th>
          <td>
            
            <p>Writes job logs to the agent process' stdout. This simplifies log collection if running agents in Docker</p>
          </td>
        </tr>
                
        <tr id="shell">
          <th>
            <code>shell<a class="Docs__attribute__link" href="#shell">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_SHELL
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>"/bin/bash -e -c"
</code>
            </p>

          </th>
          <td>
            
            <p>The shell command used to interpret build commands, e.g /bin/bash -e -c</p>
          </td>
        </tr>
                
        <tr id="queue">
          <th>
            <code>queue<a class="Docs__attribute__link" href="#queue">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_AGENT_QUEUE
</code>
            </p>

          </th>
          <td>
            
            <p>The queue the agent will listen to for jobs. If not set, the agent will use the default queue. Overwrites the queue tag in the agent's tags</p>
          </td>
        </tr>
                
        <tr id="tags">
          <th>
            <code>tags<a class="Docs__attribute__link" href="#tags">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_AGENT_TAGS
</code>
            </p>

          </th>
          <td>
            
            <p>A comma-separated list of tags for the agent (for example, "linux" or "mac,xcode=8")</p>
          </td>
        </tr>
                
        <tr id="tags-from-host">
          <th>
            <code>tags-from-host<a class="Docs__attribute__link" href="#tags-from-host">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_AGENT_TAGS_FROM_HOST
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>false
</code>
            </p>

          </th>
          <td>
            
            <p>Include tags from the host (hostname, machine-id, os)</p>
          </td>
        </tr>
                
        <tr id="tags-from-ec2-meta-data">
          <th>
            <code>tags-from-ec2-meta-data<a class="Docs__attribute__link" href="#tags-from-ec2-meta-data">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_AGENT_TAGS_FROM_EC2_META_DATA
</code>
            </p>

          </th>
          <td>
            
            <p>Include the default set of host EC2 meta-data as tags (instance-id, instance-type, ami-id, and instance-life-cycle)</p>
          </td>
        </tr>
                
        <tr id="tags-from-ec2-meta-data-paths">
          <th>
            <code>tags-from-ec2-meta-data-paths<a class="Docs__attribute__link" href="#tags-from-ec2-meta-data-paths">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_AGENT_TAGS_FROM_EC2_META_DATA_PATHS
</code>
            </p>

          </th>
          <td>
            
            <p>Include additional tags fetched from EC2 meta-data using tag &amp; path suffix pairs, e.g "tag_name=path/to/value"</p>
          </td>
        </tr>
                
        <tr id="tags-from-ec2-tags">
          <th>
            <code>tags-from-ec2-tags<a class="Docs__attribute__link" href="#tags-from-ec2-tags">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_AGENT_TAGS_FROM_EC2_TAGS
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>false
</code>
            </p>

          </th>
          <td>
            
            <p>Include the host's EC2 tags as tags</p>
          </td>
        </tr>
                
        <tr id="tags-from-ecs-meta-data">
          <th>
            <code>tags-from-ecs-meta-data<a class="Docs__attribute__link" href="#tags-from-ecs-meta-data">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_AGENT_TAGS_FROM_ECS_META_DATA
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>false
</code>
            </p>

          </th>
          <td>
            
            <p>Include the host's ECS meta-data as tags (container-name, image, and task-arn)</p>
          </td>
        </tr>
                
        <tr id="tags-from-gcp-meta-data">
          <th>
            <code>tags-from-gcp-meta-data<a class="Docs__attribute__link" href="#tags-from-gcp-meta-data">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_AGENT_TAGS_FROM_GCP_META_DATA
</code>
            </p>

          </th>
          <td>
            
            <p>Include the default set of host Google Cloud instance meta-data as tags (instance-id, machine-type, preemptible, project-id, region, and zone)</p>
          </td>
        </tr>
                
        <tr id="tags-from-gcp-meta-data-paths">
          <th>
            <code>tags-from-gcp-meta-data-paths<a class="Docs__attribute__link" href="#tags-from-gcp-meta-data-paths">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_AGENT_TAGS_FROM_GCP_META_DATA_PATHS
</code>
            </p>

          </th>
          <td>
            
            <p>Include additional tags fetched from Google Cloud instance meta-data using tag &amp; path suffix pairs, e.g "tag_name=path/to/value"</p>
          </td>
        </tr>
                
        <tr id="tags-from-gcp-labels">
          <th>
            <code>tags-from-gcp-labels<a class="Docs__attribute__link" href="#tags-from-gcp-labels">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_AGENT_TAGS_FROM_GCP_LABELS
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>false
</code>
            </p>

          </th>
          <td>
            
            <p>Include the host's Google Cloud instance labels as tags</p>
          </td>
        </tr>
                
        <tr id="wait-for-ec2-tags-timeout">
          <th>
            <code>wait-for-ec2-tags-timeout<a class="Docs__attribute__link" href="#wait-for-ec2-tags-timeout">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_AGENT_WAIT_FOR_EC2_TAGS_TIMEOUT
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>10s
</code>
            </p>

          </th>
          <td>
            
            <p>The amount of time to wait for tags from EC2 before proceeding</p>
          </td>
        </tr>
                
        <tr id="wait-for-ec2-meta-data-timeout">
          <th>
            <code>wait-for-ec2-meta-data-timeout<a class="Docs__attribute__link" href="#wait-for-ec2-meta-data-timeout">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_AGENT_WAIT_FOR_EC2_META_DATA_TIMEOUT
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>10s
</code>
            </p>

          </th>
          <td>
            
            <p>The amount of time to wait for meta-data from EC2 before proceeding</p>
          </td>
        </tr>
                
        <tr id="wait-for-ecs-meta-data-timeout">
          <th>
            <code>wait-for-ecs-meta-data-timeout<a class="Docs__attribute__link" href="#wait-for-ecs-meta-data-timeout">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_AGENT_WAIT_FOR_ECS_META_DATA_TIMEOUT
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>10s
</code>
            </p>

          </th>
          <td>
            
            <p>The amount of time to wait for meta-data from ECS before proceeding</p>
          </td>
        </tr>
                
        <tr id="wait-for-gcp-labels-timeout">
          <th>
            <code>wait-for-gcp-labels-timeout<a class="Docs__attribute__link" href="#wait-for-gcp-labels-timeout">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_AGENT_WAIT_FOR_GCP_LABELS_TIMEOUT
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>10s
</code>
            </p>

          </th>
          <td>
            
            <p>The amount of time to wait for labels from GCP before proceeding</p>
          </td>
        </tr>
                
        <tr id="git-checkout-flags">
          <th>
            <code>git-checkout-flags<a class="Docs__attribute__link" href="#git-checkout-flags">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_GIT_CHECKOUT_FLAGS
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>"-f"
</code>
            </p>

          </th>
          <td>
            
            <p>Flags to pass to "git checkout" command</p>
          </td>
        </tr>
                
        <tr id="git-clone-flags">
          <th>
            <code>git-clone-flags<a class="Docs__attribute__link" href="#git-clone-flags">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_GIT_CLONE_FLAGS
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>"-v"
</code>
            </p>

          </th>
          <td>
            
            <p>Flags to pass to the "git clone" command</p>
          </td>
        </tr>
                
        <tr id="git-clean-flags">
          <th>
            <code>git-clean-flags<a class="Docs__attribute__link" href="#git-clean-flags">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_GIT_CLEAN_FLAGS
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>"-ffxdq"
</code>
            </p>

          </th>
          <td>
            
            <p>Flags to pass to "git clean" command</p>
          </td>
        </tr>
                
        <tr id="git-fetch-flags">
          <th>
            <code>git-fetch-flags<a class="Docs__attribute__link" href="#git-fetch-flags">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_GIT_FETCH_FLAGS
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>"-v --prune"
</code>
            </p>

          </th>
          <td>
            
            <p>Flags to pass to "git fetch" command</p>
          </td>
        </tr>
                
        <tr id="git-clone-mirror-flags">
          <th>
            <code>git-clone-mirror-flags<a class="Docs__attribute__link" href="#git-clone-mirror-flags">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_GIT_CLONE_MIRROR_FLAGS
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>"-v"
</code>
            </p>

          </th>
          <td>
            
            <p>Flags to pass to the "git clone" command when used for mirroring</p>
          </td>
        </tr>
                
        <tr id="git-mirrors-path">
          <th>
            <code>git-mirrors-path<a class="Docs__attribute__link" href="#git-mirrors-path">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_GIT_MIRRORS_PATH
</code>
            </p>

          </th>
          <td>
            
            <p>Path to where mirrors of git repositories are stored</p>
          </td>
        </tr>
                
        <tr id="git-mirrors-lock-timeout">
          <th>
            <code>git-mirrors-lock-timeout<a class="Docs__attribute__link" href="#git-mirrors-lock-timeout">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_GIT_MIRRORS_LOCK_TIMEOUT
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>300
</code>
            </p>

          </th>
          <td>
            
            <p>Seconds to lock a git mirror during clone, should exceed your longest checkout</p>
          </td>
        </tr>
                
        <tr id="git-mirrors-skip-update">
          <th>
            <code>git-mirrors-skip-update<a class="Docs__attribute__link" href="#git-mirrors-skip-update">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_GIT_MIRRORS_SKIP_UPDATE
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>false
</code>
            </p>

          </th>
          <td>
            
            <p>Skip updating the Git mirror</p>
          </td>
        </tr>
                
        <tr id="bootstrap-script">
          <th>
            <code>bootstrap-script<a class="Docs__attribute__link" href="#bootstrap-script">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_BOOTSTRAP_SCRIPT_PATH
</code>
            </p>

          </th>
          <td>
            
            <p>The command that is executed for bootstrapping a job, defaults to the bootstrap sub-command of this binary</p>
          </td>
        </tr>
                          
        <tr id="hooks-path">
          <th>
            <code>hooks-path<a class="Docs__attribute__link" href="#hooks-path">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_HOOKS_PATH
</code>
            </p>

          </th>
          <td>
            
            <p>Directory where the hook scripts are found</p>
          </td>
        </tr>
                
        <tr id="additional-hooks-paths">
          <th>
            <code>additional-hooks-paths<a class="Docs__attribute__link" href="#additional-hooks-paths">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_ADDITIONAL_HOOKS_PATHS
</code>
            </p>

          </th>
          <td>
            
            <p>Additional directories to look for agent hooks</p>
          </td>
        </tr>
                
        <tr id="sockets-path">
          <th>
            <code>sockets-path<a class="Docs__attribute__link" href="#sockets-path">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_SOCKETS_PATH
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>"~/.buildkite-agent/sockets"
</code>
            </p>

          </th>
          <td>
            
            <p>Directory where the agent will place sockets</p>
          </td>
        </tr>
                
        <tr id="plugins-path">
          <th>
            <code>plugins-path<a class="Docs__attribute__link" href="#plugins-path">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_PLUGINS_PATH
</code>
            </p>

          </th>
          <td>
            
            <p>Directory where the plugins are saved to</p>
          </td>
        </tr>
                
        <tr id="no-ansi-timestamps">
          <th>
            <code>no-ansi-timestamps<a class="Docs__attribute__link" href="#no-ansi-timestamps">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_NO_ANSI_TIMESTAMPS
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>false
</code>
            </p>

          </th>
          <td>
            
            <p>Do not insert ANSI timestamp codes at the start of each line of job output</p>
          </td>
        </tr>
                
        <tr id="timestamp-lines">
          <th>
            <code>timestamp-lines<a class="Docs__attribute__link" href="#timestamp-lines">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_TIMESTAMP_LINES
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>false
</code>
            </p>

          </th>
          <td>
            
            <p>Prepend timestamps on each line of job output. Has no effect unless --no-ansi-timestamps is also used</p>
          </td>
        </tr>
                
        <tr id="health-check-addr">
          <th>
            <code>health-check-addr<a class="Docs__attribute__link" href="#health-check-addr">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_AGENT_HEALTH_CHECK_ADDR
</code>
            </p>

          </th>
          <td>
            
            <p>Start an HTTP server on this addr:port that returns whether the agent is healthy, disabled by default</p>
          </td>
        </tr>
                
        <tr id="no-pty">
          <th>
            <code>no-pty<a class="Docs__attribute__link" href="#no-pty">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_NO_PTY
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>false
</code>
            </p>

          </th>
          <td>
            
            <p>Do not run jobs within a pseudo terminal</p>
          </td>
        </tr>
                
        <tr id="no-ssh-keyscan">
          <th>
            <code>no-ssh-keyscan<a class="Docs__attribute__link" href="#no-ssh-keyscan">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_NO_SSH_KEYSCAN
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>false
</code>
            </p>

          </th>
          <td>
            
            <p>Don't automatically run ssh-keyscan before checkout</p>
          </td>
        </tr>
                
        <tr id="no-command-eval">
          <th>
            <code>no-command-eval<a class="Docs__attribute__link" href="#no-command-eval">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_NO_COMMAND_EVAL
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>false
</code>
            </p>

          </th>
          <td>
            
            <p>Don't allow this agent to run arbitrary console commands, including plugins</p>
          </td>
        </tr>
                
        <tr id="no-plugins">
          <th>
            <code>no-plugins<a class="Docs__attribute__link" href="#no-plugins">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_NO_PLUGINS
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>false
</code>
            </p>

          </th>
          <td>
            
            <p>Don't allow this agent to load plugins</p>
          </td>
        </tr>
                
        <tr id="no-plugin-validation">
          <th>
            <code>no-plugin-validation<a class="Docs__attribute__link" href="#no-plugin-validation">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_NO_PLUGIN_VALIDATION
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>true
</code>
            </p>

          </th>
          <td>
            
            <p>Don't validate plugin configuration and requirements</p>
          </td>
        </tr>
                
        <tr id="plugins-always-clone-fresh">
          <th>
            <code>plugins-always-clone-fresh<a class="Docs__attribute__link" href="#plugins-always-clone-fresh">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_PLUGINS_ALWAYS_CLONE_FRESH
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>false
</code>
            </p>

          </th>
          <td>
            
            <p>Always make a new clone of plugin source, even if already present</p>
          </td>
        </tr>
                
        <tr id="no-local-hooks">
          <th>
            <code>no-local-hooks<a class="Docs__attribute__link" href="#no-local-hooks">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_NO_LOCAL_HOOKS
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>false
</code>
            </p>

          </th>
          <td>
            
            <p>Don't allow local hooks to be run from checked out repositories</p>
          </td>
        </tr>
                
        <tr id="no-git-submodules">
          <th>
            <code>no-git-submodules<a class="Docs__attribute__link" href="#no-git-submodules">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_NO_GIT_SUBMODULES
$BUILDKITE_DISABLE_GIT_SUBMODULES
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>false
</code>
            </p>

          </th>
          <td>
            
            <p>Don't automatically checkout git submodules</p>
          </td>
        </tr>
                
        <tr id="skip-checkout">
          <th>
            <code>skip-checkout<a class="Docs__attribute__link" href="#skip-checkout">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_SKIP_CHECKOUT
</code>
            </p>

          </th>
          <td>
            
            <p>Skip the git checkout phase entirely</p>
          </td>
        </tr>
                
        <tr id="no-feature-reporting">
          <th>
            <code>no-feature-reporting<a class="Docs__attribute__link" href="#no-feature-reporting">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_AGENT_NO_FEATURE_REPORTING
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>false
</code>
            </p>

          </th>
          <td>
            
            <p>Disables sending a list of enabled features back to the Buildkite mothership. We use this information to measure feature usage, but if you're not comfortable sharing that information then that's totally okay :)</p>
          </td>
        </tr>
                
        <tr id="allowed-repositories">
          <th>
            <code>allowed-repositories<a class="Docs__attribute__link" href="#allowed-repositories">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_ALLOWED_REPOSITORIES
</code>
            </p>

          </th>
          <td>
            
            <p>A comma-separated list of regular expressions representing repositories the agent is allowed to clone (for example, "^<a href="mailto:git@github.com">git@github.com</a>:buildkite/.<em>" or "^<a href="https://github.com/buildkite/" class="external-link" target="_blank">https://github.com/buildkite/</a>.</em>")</p>
          </td>
        </tr>
                
        <tr id="enable-environment-variable-allowlist">
          <th>
            <code>enable-environment-variable-allowlist<a class="Docs__attribute__link" href="#enable-environment-variable-allowlist">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_ENABLE_ENVIRONMENT_VARIABLE_ALLOWLIST
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>false
</code>
            </p>

          </th>
          <td>
            
            <p>Only run jobs where all environment variables are allowed by the allowed-environment-variables option, or have been set by Buildkite</p>
          </td>
        </tr>
                
        <tr id="allowed-environment-variables">
          <th>
            <code>allowed-environment-variables<a class="Docs__attribute__link" href="#allowed-environment-variables">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_ALLOWED_ENVIRONMENT_VARIABLES
</code>
            </p>

          </th>
          <td>
            
            <p>A comma-separated list of regular expressions representing environment variables the agent will pass to jobs (for example, "^MYAPP_.*$"). Environment variables set by Buildkite will always be allowed. Requires --enable-environment-variable-allowlist to be set</p>
          </td>
        </tr>
                
        <tr id="allowed-plugins">
          <th>
            <code>allowed-plugins<a class="Docs__attribute__link" href="#allowed-plugins">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_ALLOWED_PLUGINS
</code>
            </p>

          </th>
          <td>
            
            <p>A comma-separated list of regular expressions representing plugins the agent is allowed to use (for example, "^buildkite-plugins/.<em>$" or "^/var/lib/buildkite-plugins/.</em>")</p>
          </td>
        </tr>
                
        <tr id="metrics-datadog">
          <th>
            <code>metrics-datadog<a class="Docs__attribute__link" href="#metrics-datadog">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_METRICS_DATADOG
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>false
</code>
            </p>

          </th>
          <td>
            
            <p>Send metrics to DogStatsD for Datadog</p>
          </td>
        </tr>
                
        <tr id="metrics-datadog-host">
          <th>
            <code>metrics-datadog-host<a class="Docs__attribute__link" href="#metrics-datadog-host">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_METRICS_DATADOG_HOST
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>"127.0.0.1:8125"
</code>
            </p>

          </th>
          <td>
            
            <p>The dogstatsd instance to send metrics to using udp</p>
          </td>
        </tr>
                
        <tr id="metrics-datadog-distributions">
          <th>
            <code>metrics-datadog-distributions<a class="Docs__attribute__link" href="#metrics-datadog-distributions">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_METRICS_DATADOG_DISTRIBUTIONS
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>false
</code>
            </p>

          </th>
          <td>
            
            <p>Use Datadog Distributions for Timing metrics</p>
          </td>
        </tr>
                
        <tr id="log-format">
          <th>
            <code>log-format<a class="Docs__attribute__link" href="#log-format">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_LOG_FORMAT
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>"text"
</code>
            </p>

          </th>
          <td>
            
            <p>The format to use for the logger output</p>
          </td>
        </tr>
                
        <tr id="spawn">
          <th>
            <code>spawn<a class="Docs__attribute__link" href="#spawn">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_AGENT_SPAWN
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>1
</code>
            </p>

          </th>
          <td>
            
            <p>The number of agents to spawn in parallel (mutually exclusive with --spawn-per-cpu)</p>
          </td>
        </tr>
                
        <tr id="spawn-per-cpu">
          <th>
            <code>spawn-per-cpu<a class="Docs__attribute__link" href="#spawn-per-cpu">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_AGENT_SPAWN_PER_CPU
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>0
</code>
            </p>

          </th>
          <td>
            
            <p>The number of agents to spawn per cpu in parallel (mutually exclusive with --spawn)</p>
          </td>
        </tr>
                
        <tr id="spawn-with-priority">
          <th>
            <code>spawn-with-priority<a class="Docs__attribute__link" href="#spawn-with-priority">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_AGENT_SPAWN_WITH_PRIORITY
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>false
</code>
            </p>

          </th>
          <td>
            
            <p>Assign priorities to every spawned agent (when using --spawn or --spawn-per-cpu) equal to the agent's index</p>
          </td>
        </tr>
                
        <tr id="cancel-signal">
          <th>
            <code>cancel-signal<a class="Docs__attribute__link" href="#cancel-signal">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_CANCEL_SIGNAL
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>"SIGTERM"
</code>
            </p>

          </th>
          <td>
            
            <p>The signal to use for cancellation</p>
          </td>
        </tr>
                
        <tr id="signal-grace-period-seconds">
          <th>
            <code>signal-grace-period-seconds<a class="Docs__attribute__link" href="#signal-grace-period-seconds">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_SIGNAL_GRACE_PERIOD_SECONDS
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>-1
</code>
            </p>

          </th>
          <td>
            
            <p>The number of seconds given to a subprocess to handle being sent ′cancel-signal′. After this period has elapsed, SIGKILL will be sent. Negative values are taken relative to ′cancel-grace-period′. The default value (-1) means that the effective signal grace period is equal to ′cancel-grace-period′ minus 1.</p>
          </td>
        </tr>
                
        <tr id="tracing-backend">
          <th>
            <code>tracing-backend<a class="Docs__attribute__link" href="#tracing-backend">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_TRACING_BACKEND
</code>
            </p>

          </th>
          <td>
            
            <p>Enable tracing for build jobs by specifying a backend, "datadog" or "opentelemetry"</p>
          </td>
        </tr>
                
        <tr id="tracing-propagate-traceparent">
          <th>
            <code>tracing-propagate-traceparent<a class="Docs__attribute__link" href="#tracing-propagate-traceparent">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_TRACING_PROPAGATE_TRACEPARENT
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>false
</code>
            </p>

          </th>
          <td>
            
            <p>Enable accepting traceparent context from Buildkite control plane (only supported for OpenTelemetry backend)</p>
          </td>
        </tr>
                
        <tr id="tracing-service-name">
          <th>
            <code>tracing-service-name<a class="Docs__attribute__link" href="#tracing-service-name">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_TRACING_SERVICE_NAME
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>"buildkite-agent"
</code>
            </p>

          </th>
          <td>
            
            <p>Service name to use when reporting traces.</p>
          </td>
        </tr>
                
        <tr id="verification-jwks-file">
          <th>
            <code>verification-jwks-file<a class="Docs__attribute__link" href="#verification-jwks-file">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_AGENT_VERIFICATION_JWKS_FILE
</code>
            </p>

          </th>
          <td>
            
            <p>Path to a file containing a JSON Web Key Set (JWKS), used to verify job signatures.</p>
          </td>
        </tr>
                
        <tr id="signing-jwks-file">
          <th>
            <code>signing-jwks-file<a class="Docs__attribute__link" href="#signing-jwks-file">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_AGENT_SIGNING_JWKS_FILE
</code>
            </p>

          </th>
          <td>
            
            <p>Path to a file containing a signing key. Passing this flag enables pipeline signing for all pipelines uploaded by this agent. For hmac-sha256, the raw file content is used as the shared key. When using Docker containers to upload pipeline steps dynamically, use environment variable propagation (for example, "docker run -e BUILDKITE_AGENT_JWKS_FILE") to allow all steps within the pipeline to be signed.</p>
          </td>
        </tr>
                
        <tr id="signing-jwks-key-id">
          <th>
            <code>signing-jwks-key-id<a class="Docs__attribute__link" href="#signing-jwks-key-id">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_AGENT_SIGNING_JWKS_KEY_ID
</code>
            </p>

          </th>
          <td>
            
            <p>The JWKS key ID to use when signing the pipeline. If omitted, and the signing JWKS contains only one key, that key will be used.</p>
          </td>
        </tr>
                
        <tr id="signing-aws-kms-key">
          <th>
            <code>signing-aws-kms-key<a class="Docs__attribute__link" href="#signing-aws-kms-key">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_AGENT_SIGNING_AWS_KMS_KEY
</code>
            </p>

          </th>
          <td>
            
            <p>The KMS KMS key ID, or key alias used when signing and verifying the pipeline.</p>
          </td>
        </tr>
                
        <tr id="debug-signing">
          <th>
            <code>debug-signing<a class="Docs__attribute__link" href="#debug-signing">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_AGENT_DEBUG_SIGNING
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>false
</code>
            </p>

          </th>
          <td>
            
            <p>Enable debug logging for pipeline signing. This can potentially leak secrets to the logs as it prints each step in full before signing. Requires debug logging to be enabled</p>
          </td>
        </tr>
                
        <tr id="verification-failure-behavior">
          <th>
            <code>verification-failure-behavior<a class="Docs__attribute__link" href="#verification-failure-behavior">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>block warn
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>"block"
</code>
            </p>

          </th>
          <td>
            
            <p>The behavior when a job is received without a valid verifiable signature (without a signature, with an invalid signature, or with a signature that fails verification). One of: [block warn]. Defaults to block</p>
          </td>
        </tr>
                
        <tr id="disable-warnings-for">
          <th>
            <code>disable-warnings-for<a class="Docs__attribute__link" href="#disable-warnings-for">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_AGENT_DISABLE_WARNINGS_FOR
</code>
            </p>

          </th>
          <td>
            
            <p>A list of warning IDs to disable</p>
          </td>
        </tr>
                          
        <tr id="endpoint">
          <th>
            <code>endpoint<a class="Docs__attribute__link" href="#endpoint">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_AGENT_ENDPOINT
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>"https://agent.buildkite.com/v3"
</code>
            </p>

          </th>
          <td>
            
            <p>The Agent API endpoint</p>
          </td>
        </tr>
                
        <tr id="no-http2">
          <th>
            <code>no-http2<a class="Docs__attribute__link" href="#no-http2">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_NO_HTTP2
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>false
</code>
            </p>

          </th>
          <td>
            
            <p>Disable HTTP2 when communicating with the Agent API</p>
          </td>
        </tr>
                
        <tr id="debug-http">
          <th>
            <code>debug-http<a class="Docs__attribute__link" href="#debug-http">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_AGENT_DEBUG_HTTP
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>false
</code>
            </p>

          </th>
          <td>
            
            <p>Enable HTTP debug mode, which dumps all request and response bodies to the log</p>
          </td>
        </tr>
                
        <tr id="trace-http">
          <th>
            <code>trace-http<a class="Docs__attribute__link" href="#trace-http">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_AGENT_TRACE_HTTP
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>false
</code>
            </p>

          </th>
          <td>
            
            <p>Enable HTTP trace mode, which logs timings for each HTTP request. Timings are logged at the debug level unless a request fails at the network level in which case they are logged at the error level</p>
          </td>
        </tr>
                
        <tr id="kubernetes-exec">
          <th>
            <code>kubernetes-exec<a class="Docs__attribute__link" href="#kubernetes-exec">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_KUBERNETES_EXEC
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>false
</code>
            </p>

          </th>
          <td>
            
            <p>This is intended to be used only by the Buildkite k8s stack (github.com/buildkite/agent-stack-k8s); it enables a Unix socket for transporting logs and exit statuses between containers in a pod</p>
          </td>
        </tr>
                
        <tr id="redacted-vars">
          <th>
            <code>redacted-vars<a class="Docs__attribute__link" href="#redacted-vars">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_REDACTED_VARS
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>"*_PASSWORD", "*_SECRET", "*_TOKEN", "*_PRIVATE_KEY", "*_ACCESS_KEY", "*_SECRET_KEY", "*_CONNECTION_STRING"
</code>
            </p>

          </th>
          <td>
            
            <p>Pattern of environment variable names containing sensitive values</p>
          </td>
        </tr>
                
        <tr id="strict-single-hooks">
          <th>
            <code>strict-single-hooks<a class="Docs__attribute__link" href="#strict-single-hooks">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_STRICT_SINGLE_HOOKS
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>false
</code>
            </p>

          </th>
          <td>
            
            <p>Enforces that only one checkout hook, and only one command hook, can be run</p>
          </td>
        </tr>
                
        <tr id="trace-context-encoding">
          <th>
            <code>trace-context-encoding<a class="Docs__attribute__link" href="#trace-context-encoding">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_TRACE_CONTEXT_ENCODING
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>"gob"
</code>
            </p>

          </th>
          <td>
            
            <p>Sets the inner encoding for BUILDKITE_TRACE_CONTEXT. Must be either json or gob</p>
          </td>
        </tr>
                
        <tr id="no-multipart-artifact-upload">
          <th>
            <code>no-multipart-artifact-upload<a class="Docs__attribute__link" href="#no-multipart-artifact-upload">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_NO_MULTIPART_ARTIFACT_UPLOAD
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>false
</code>
            </p>

          </th>
          <td>
            
            <p>For Buildkite-hosted artifacts, disables the use of multipart uploads. Has no effect on uploads to other destinations such as custom cloud buckets</p>
          </td>
        </tr>
                
        <tr id="kubernetes-log-collection-grace-period">
          <th>
            <code>kubernetes-log-collection-grace-period<a class="Docs__attribute__link" href="#kubernetes-log-collection-grace-period">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_KUBERNETES_LOG_COLLECTION_GRACE_PERIOD
</code>
            </p>

            <p class="Docs__attribute__default">
              <strong>Default value: </strong>
              <code>50s
</code>
            </p>

          </th>
          <td>
            
            <p>Deprecated, do not use</p>
          </td>
        </tr>
                
        <tr id="tags-from-ec2">
          <th>
            <code>tags-from-ec2<a class="Docs__attribute__link" href="#tags-from-ec2">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_AGENT_TAGS_FROM_EC2
</code>
            </p>

          </th>
          <td>
            
            <p>Include the host's EC2 meta-data as tags (instance-id, instance-type, and ami-id)</p>
          </td>
        </tr>
                
        <tr id="tags-from-gcp">
          <th>
            <code>tags-from-gcp<a class="Docs__attribute__link" href="#tags-from-gcp">#</a></code>
            <span class="Docs__attribute__importance">Optional</span>
            <p class="Docs__attribute__env-var">
              <strong>Environment variable: </strong>
              <br/>
              <code>$BUILDKITE_AGENT_TAGS_FROM_GCP
</code>
            </p>

          </th>
          <td>
            
            <p>Include the host's Google Cloud instance meta-data as tags (instance-id, machine-type, preemptible, project-id, region, and zone)</p>
          </td>
        </tr>
            </tbody>
</table>

### Experimental features

Buildkite frequently introduces new experimental features to the agent, which can be enabled using the [`experiment` flag or the `$BUILDKITE_AGENT_EXPERIMENT` environment variable setting](#experiment). These features are not yet considered stable and may change or be removed in future versions of the agent. Learn more about these experimental features in [Agent experiments](/docs/agent/self-hosted/configure/experiments).

## Deprecated configuration settings

<table>
  <tbody>
    <tr id="disconnect-after-job-timeout">
      <th><code>disconnect-after-job-timeout</code></th>
      <td>
        <p>When <code>disconnect-after-job</code> is specified, the number of seconds to wait for a job before shutting down.</p>
        <p>Not to be confused with <a href="/docs/pipelines/configure/build-timeouts#command-timeouts">default and maximum build timeouts</a>.</p>
        <p class="Docs__api-param-eg"><em>Default:</em> <code>120</code></p>
        <p class="Docs__api-param-eg"><em>Environment variable:</em> <code>BUILDKITE_AGENT_DISCONNECT_AFTER_JOB_TIMEOUT</code></p>
      </td>
    </tr>

    <tr id="meta-data">
      <th><code>meta-data</code></th>
      <td>
        Meta data for the agent.
        <p class="Docs__api-param-eg"><em>Default:</em> <code>"queue=default"</code></p>
        <p class="Docs__api-param-eg"><em>Environment variable:</em> <code>BUILDKITE_AGENT_META_DATA</code></p>
        <p class="Docs__api-param-eg"><a href="#tags"><em>Use instead:</em> <code>tags</code></a></p>
      </td>
    </tr>

    <tr id="meta-data-ec2">
      <th><code>meta-data-ec2</code></th>
      <td>
        Include the host's EC2 meta-data (instance-id, instance-type, and ami-id) as meta-data.
        <p class="Docs__api-param-eg"><em>Default:</em> <code>false</code></p>
        <p class="Docs__api-param-eg"><em>Environment variable:</em> <code>BUILDKITE_AGENT_META_DATA_EC2</code></p>
        <p class="Docs__api-param-eg"><a href="#tags-from-ec2"><em>Use instead:</em> <code>tags-from-ec2</code></a></p>
      </td>
    </tr>

    <tr id="meta-data-ec2-tags">
      <th><code>meta-data-ec2-tags</code></th>
      <td>
        Include the host's EC2 tags as meta-data.
        <p class="Docs__api-param-eg"><em>Default:</em> <code>false</code></p>
        <p class="Docs__api-param-eg"><em>Environment variable:</em> <code>BUILDKITE_AGENT_META_DATA_EC2_TAGS</code></p>
        <p class="Docs__api-param-eg"><a href="#tags-from-ec2-tags"><em>Use instead:</em> <code>tags-from-ec2-tags</code></a></p>
      </td>
    </tr>

    <tr id="meta-data-gcp">
      <th><code>meta-data-gcp</code></th>
      <td>
        Include the host's GCP meta-data as meta-data.
        <p class="Docs__api-param-eg"><em>Default:</em> <code>false</code></p>
        <p class="Docs__api-param-eg"><em>Environment variable:</em> <code>BUILDKITE_AGENT_META_DATA_GCP_TAGS</code></p>
        <p class="Docs__api-param-eg"><a href="#tags-from-gcp"><em>Use instead:</em> <code>tags-from-gcp</code></a></p>
      </td>
    </tr>

    <tr id="no-automatic-ssh-fingerprint-verification">
      <th><code>no-automatic-ssh-fingerprint-verification</code></th>
      <td>
        Do not automatically verify SSH fingerprints for first-time checkouts.
        <p class="Docs__api-param-eg"><em>Default:</em> <code>false</code></p>
        <p class="Docs__api-param-eg"><em>Environment variable:</em> <code>BUILDKITE_NO_AUTOMATIC_SSH_FINGERPRINT_VERIFICATION</code></p>
        <p class="Docs__api-param-eg"><a href="#no-ssh-keyscan"><em>Use instead:</em> <code>no-ssh-keyscan</code></a></p>
      </td>
    </tr>
  </tbody>
</table>

## Environment variables

Most configuration options can be specified as environment variables when starting the agent, for example:

```sh
BUILDKITE_AGENT_TAGS="queue=deploy,host=$(hostname)" buildkite-agent start
```

These variables cannot be modified through the Buildkite web interface, API or using pipeline upload for security reasons. You may be able to modify some of the options, such as `BUILDKITE_GIT_CLONE_FLAGS`, from within [hooks](/docs/agent/hooks).

## Agent Naming

The following template variables are supported when configuring the agent name:

- `%hostname` - the agent machine's hostname
- `%spawn` - the spawn index number (1, 2, 3, etc.) when launching multiple agents per host
- `%random` - six (6) random alphanumeric characters [a-zA-Z0-9]
- `%pid` - the agent's process ID

> 📘 Note
> If you're using `--spawn` to run multiple agents on a single host, it's recommended to use `%spawn` in your agent name to ensure that each agent running on the host using the same `build-path` has a unique agent name.
