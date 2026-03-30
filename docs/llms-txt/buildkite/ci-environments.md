# Source: https://buildkite.com/docs/test-engine/test-collection/ci-environments.md

# CI environments

Buildkite Test Engine collectors automatically detect common continuous integration (CI) environments.
If available, test collectors gather information about your test runs, such as branch names and build IDs.
Test collectors gather information from the following CI environments:

- [Buildkite](/docs/test-engine/test-collection/ci-environments#buildkite)
- [CircleCI](/docs/test-engine/test-collection/ci-environments#circleci)
- [GitHub Actions](/docs/test-engine/test-collection/ci-environments#github-actions)

If you run test collectors inside [containers](/docs/test-engine/test-collection/ci-environments#containers-and-test-collectors) or use another CI system, you must set variables to report your CI details to Buildkite.

If you're not using a test collector, see [Importing JSON](/docs/test-engine/test-collection/importing-json) and [Importing JUnit XML](/docs/test-engine/test-collection/importing-junit-xml) to learn how to provide run environment data.

## Run environment

### Required

- `run_env[key]`: The identifier of a run, which may be the same across multiple uploads; often the build ID.

### Recommended

If you're manually providing environment variables, we strongly recommend setting the following variables:

- `run_env[branch]`: Sends the branch or reference for this build, enabling you to filter data by branch.
- `run_env[commit_sha]`: Sends the commit hash for the head of the branch, enabling automatic flaky test detection in your builds.
- `run_env[message]`: Forwards the commit message for the head of the branch, helping you identify different runs more easily.
- `run_env[url]`: Provides the URL for the build on your CI provider, giving you a handy link back to the CI build.

## Containers and test collectors

If you're using containers within your CI system, then the environment variables used by test collectors may not be exposed to those containers by default.
Make sure to export your CI environment's variables and your Buildkite API token to your containerized builds and tests.

For example, by default Docker does not receive the host's environment variables.
To pass them through to the Docker container, use the `--env` option:

```
  docker run \
    --env BUILDKITE_ANALYTICS_TOKEN \
    --env BUILDKITE_BUILD_ID \
    --env BUILDKITE_BUILD_NUMBER \
    --env BUILDKITE_JOB_ID \
    --env BUILDKITE_BRANCH \
    --env BUILDKITE_COMMIT \
    --env BUILDKITE_MESSAGE \
    --env BUILDKITE_BUILD_URL \
    bundle exec rspec
```

Review the following sections for the environment variables expected by test collectors.

## Buildkite

During Buildkite pipeline runs, test collectors upload information from the following environment variables, and test importers use the following field names:

<table class="responsive-table">
  <thead>
    <tr>
      <th style="width:25%">Field name</th>
      <th style="width:30%">Environment variable</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>

      <tr>
        <td>
          <code>run_env[branch]</code>
        </td>
        <td>
          <code>BUILDKITE_BRANCH</code>
        </td>
        <td>
          The branch or reference for this build.
        </td>
      </tr>
    
      <tr>
        <td>
          <code>run_env[commit_sha]</code>
        </td>
        <td>
          <code>BUILDKITE_COMMIT</code>
        </td>
        <td>
          The commit hash for the head of the branch.
        </td>
      </tr>
    
      <tr>
        <td>
          <code>run_env[job_id]</code>
        </td>
        <td>
          <code>BUILDKITE_JOB_ID</code>
        </td>
        <td>
          The UUID of the job.
        </td>
      </tr>
    
      <tr>
        <td>
          <code>run_env[key]</code>
        </td>
        <td>
          <code>BUILDKITE_BUILD_ID</code>
        </td>
        <td>
          The UUID for the build.
        </td>
      </tr>
    
      <tr>
        <td>
          <code>run_env[message]</code>
        </td>
        <td>
          <code>BUILDKITE_MESSAGE</code>
        </td>
        <td>
          The commit message for the head of the branch.
        </td>
      </tr>
    
      <tr>
        <td>
          <code>run_env[number]</code>
        </td>
        <td>
          <code>BUILDKITE_BUILD_NUMBER</code>
        </td>
        <td>
          The build number.
        </td>
      </tr>
    
      <tr>
        <td>
          <code>run_env[url]</code>
        </td>
        <td>
          <code>BUILDKITE_BUILD_URL</code>
        </td>
        <td>
          The URL for the build on Buildkite.
        </td>
      </tr>
    
  </tbody>
</table>

## CircleCI

During CircleCI workflow runs, test collectors upload information from the following environment variables, and test importers use the following field names:

<table class="responsive-table">
  <thead>
    <tr>
      <th style="width:25%">Field name</th>
      <th>Environment variable(s)</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>

      <tr>
        <td>
          <code>run_env[branch]</code>
        </td>
        <td>
          <code>CIRCLE_BRANCH</code>
          
        </td>
        <td>
          The branch or reference being built.
        </td>
      </tr>
    
      <tr>
        <td>
          <code>run_env[commit_sha]</code>
        </td>
        <td>
          <code>CIRCLE_SHA1</code>
          
        </td>
        <td>
          The commit hash for the head of the branch.
        </td>
      </tr>
    
      <tr>
        <td>
          <code>run_env[key]</code>
        </td>
        <td>
          <code>CIRCLE_WORKFLOW_ID</code>
          
            <br/>
            <code>CIRCLE_BUILD_NUM</code>
          
        </td>
        <td>
          The unique identifier for the workflow run, and the number for the job, each separated by a hyphen. That is, <code>$CIRCLE_WORKFLOW_ID-$CIRCLE_BUILD_NUM</code>.
        </td>
      </tr>
    
      <tr>
        <td>
          <code>run_env[url]</code>
        </td>
        <td>
          <code>CIRCLE_BUILD_URL</code>
          
        </td>
        <td>
          The URL for the job on CircleCI.
        </td>
      </tr>
    
  </tbody>
</table>

## GitHub Actions

During GitHub Actions workflow runs, test collectors upload information from the following environment variables, and test importers use the following field names:

<table class="responsive-table">
  <thead>
    <tr>
      <th style="width:25%">Field name</th>
      <th>Environment variable(s)</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>

      <tr>
        <td>
          <code>run_env[branch]</code>
        </td>
        <td>
          <code>GITHUB_REF_NAME</code>
          
        </td>
        <td>
          The ref (branch or tag) that triggered the workflow run.
        </td>
      </tr>
    
      <tr>
        <td>
          <code>run_env[commit_sha]</code>
        </td>
        <td>
          <code>GITHUB_SHA</code>
          
        </td>
        <td>
          The commit hash for the head of the branch.
        </td>
      </tr>
    
      <tr>
        <td>
          <code>run_env[key]</code>
        </td>
        <td>
          <code>GITHUB_ACTION</code>
          
            <br/>
            <code>GITHUB_RUN_NUMBER</code>
            <br/>
            <code>GITHUB_RUN_ATTEMPT</code>
          
        </td>
        <td>
          The name of the action running or its step ID, the cumulative number of runs for the workflow, and the numbered attempt of the workflow run, each separated by a hyphen. That is, <code>$GITHUB_ACTION-$GITHUB_RUN_NUMBER-$GITHUB_RUN_ATTEMPT</code>.
        </td>
      </tr>
    
      <tr>
        <td>
          <code>run_env[number]</code>
        </td>
        <td>
          <code>GITHUB_RUN_ID</code>
          
        </td>
        <td>
          The unique number for the workflow run.
        </td>
      </tr>
    
      <tr>
        <td>
          <code>run_env[url]</code>
        </td>
        <td>
          <code>GITHUB_REPOSITORY</code>
          
        </td>
        <td>
          The repository owner and repository name.
        </td>
      </tr>
    
  </tbody>
</table>

## Other CI providers

If you're using other CI providers (or [containers](#containers-and-test-collectors)), then set environment variables for test collectors to gather information about your builds and tests.
If you don't set these environment variables, then Test Engine lacks the details needed to produce useful reports.

Each environment variable corresponds to a `run_env` key in the payload `https://analytics-api.buildkite.com/v1/uploads`. Read [Importing JSON](/docs/test-engine/test-collection/importing-json) to learn how these keys are used to make API calls.

<table class="responsive-table">
  <thead>
    <tr>
      <th style="width:25%">Field name</th>
      <th style="width:35%">Environment variable</th>
      <th style="width:40%">Description</th>
    </tr>
  </thead>
  <tbody>
          <tr>
        <td><code>run_env[branch]</code></td>
        <td><code>BUILDKITE_ANALYTICS_BRANCH</code></td>
        <td>
          <p>A version control branch or reference for this run</p>

          Examples:
          <code>main</code>, <code>ref/heads/develop</code>, <code>JIRA-3494-fix-off-by-one-error</code>
        </td>
      </tr>
          <tr>
        <td><code>run_env[commit_sha]</code></td>
        <td><code>BUILDKITE_ANALYTICS_SHA</code></td>
        <td>
          <p>A unique identifier for the version control revision for this run</p>

          Examples:
          <code>26a5144c</code>, <code>49239:a94f28be2e6e</code>, <code>26916</code>
        </td>
      </tr>
          <tr>
        <td><code>run_env[job_id]</code></td>
        <td><code>BUILDKITE_ANALYTICS_JOB_ID</code></td>
        <td>
          <p>An identifier for a job within a build</p>

          Examples:
          <code>build_stage_1</code>, <code>smoke-test</code>, <code>publish</code>
        </td>
      </tr>
          <tr>
        <td><code>run_env[key]</code></td>
        <td><code>BUILDKITE_ANALYTICS_KEY</code></td>
        <td>
          <p>A unique key for this run of the test suite. This key may be re-used across uploads to group them into a single run.</p>

          Examples:
          <code>c5636a53-b2d7-4224-92ee-1677b3e76910</code>
        </td>
      </tr>
          <tr>
        <td><code>run_env[message]</code></td>
        <td><code>BUILDKITE_ANALYTICS_MESSAGE</code></td>
        <td>
          <p>The commit message or other description of the build</p>

          Examples:
          <code>Fix off by one error</code>
        </td>
      </tr>
          <tr>
        <td><code>run_env[number]</code></td>
        <td><code>BUILDKITE_ANALYTICS_NUMBER</code></td>
        <td>
          <p>A counter for this build.</p>

<p>This number must be unique for each build key, but not necessarily globally unique.</p>

          Examples:
          <code>0</code>, <code>1</code>, <code>4</code>
        </td>
      </tr>
          <tr>
        <td><code>run_env[url]</code></td>
        <td><code>BUILDKITE_ANALYTICS_URL</code></td>
        <td>
          <p>A URL that links to the build in your CI system</p>

          Examples:
          <code>https://ci.example.com/project1/runs/a086005a/attempts/4</code>
        </td>
      </tr>
      </tbody>
</table>
