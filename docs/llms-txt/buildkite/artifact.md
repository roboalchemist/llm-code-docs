# Source: https://buildkite.com/docs/agent/cli/reference/artifact.md

# buildkite-agent artifact

The Buildkite agent's `artifact` command provides support for uploading and
downloading of build artifacts, allowing you to share binary data between build
steps no matter the machine or network.

See the [Using build artifacts](/docs/pipelines/configure/artifacts) guide for a step-by-step
example.

## Uploading artifacts

You can use this command in your build scripts to store artifacts. Artifacts are accessible using the web interface and can be downloaded by future build steps.
Artifacts can be stored in the Buildkite-managed artifact store, or your own storage location, depending on how you have configured your Buildkite agent.

Be aware that the Buildkite-managed artifact store has an upload size limit of 5Gb per file/artifact.

For documentation on configuring a custom storage location, see:

- [Using your private AWS S3 bucket](#using-your-private-aws-s3-bucket)
- [Using your private Google Cloud bucket](#using-your-private-google-cloud-bucket)
- [Using your private Azure Blob container](#using-your-private-azure-blob-container)
- [Using your Artifactory instance](#using-your-artifactory-instance)

You can also configure the agent to automatically upload artifacts after your
step's command has completed based on a file pattern (see the
[Using build artifacts guide](/docs/pipelines/configure/artifacts) for details).

### Usage

`buildkite-agent artifact upload [options] <pattern> [destination]`

### Description

Uploads files to a job as artifacts.

You need to ensure that the paths are surrounded by quotes otherwise the
built-in shell path globbing will provide the files, which is currently not
supported.

You can specify an alternate destination on Amazon S3, Google Cloud Storage
or Artifactory as per the examples below. This may be specified in the
&#39;destination&#39; argument, or in the &#39;BUILDKITE_ARTIFACT_UPLOAD_DESTINATION&#39;
environment variable.  Otherwise, artifacts are uploaded to a
Buildkite-managed Amazon S3 bucket, where they’re retained for six months.

### Example

```shell
buildkite-agent artifact upload "log/**/*.log"
```

You can also upload directly to Amazon S3 if you&#39;d like to host your own artifacts:

```shell
export BUILDKITE_S3_ACCESS_KEY_ID=xxx
export BUILDKITE_S3_SECRET_ACCESS_KEY=yyy
export BUILDKITE_S3_DEFAULT_REGION=eu-central-1 # default is us-east-1
export BUILDKITE_S3_ACL=private # default is public-read
buildkite-agent artifact upload "log/**/*.log" s3://name-of-your-s3-bucket/$BUILDKITE_JOB_ID
```

You can use Amazon IAM assumed roles by specifying the session token:

```shell
export BUILDKITE_S3_SESSION_TOKEN=zzz
```

Or upload directly to Google Cloud Storage:

```shell
export BUILDKITE_GS_ACL=private
buildkite-agent artifact upload "log/**/*.log" gs://name-of-your-gs-bucket/$BUILDKITE_JOB_ID
```

Or upload directly to Artifactory:

```shell
export BUILDKITE_ARTIFACTORY_URL=http://my-artifactory-instance.com/artifactory
export BUILDKITE_ARTIFACTORY_USER=carol-danvers
export BUILDKITE_ARTIFACTORY_PASSWORD=xxx
buildkite-agent artifact upload "log/**/*.log" rt://name-of-your-artifactory-repo/$BUILDKITE_JOB_ID
```

By default, symlinks to directories will not be explored when resolving the glob, but symlinks to
files will be uploaded as the linked files. To ignore symlinks to files use:

```shell
buildkite-agent artifact upload --upload-skip-symlinks "log/**/*.log"
```

Note: uploading symlinks to files without following them is not supported.
If you need to preserve them in a directory, we recommend creating a tar archive:

```shell
tar -cvf log.tar log/**/*
buildkite-agent upload log.tar
```

### Options

<table class="Docs__attribute__table">
<tr id="no-color"><th><code>--no-color </code> <a class="Docs__attribute__link" href="#no-color">#</a></th><td><p>Don't show colors in logging (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_NO_COLOR</code></p></td></tr>
<tr id="debug"><th><code>--debug </code> <a class="Docs__attribute__link" href="#debug">#</a></th><td><p>Enable debug mode. Synonym for `--log-level debug`. Takes precedence over `--log-level` (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_DEBUG</code></p></td></tr>
<tr id="log-level"><th><code>--log-level value</code> <a class="Docs__attribute__link" href="#log-level">#</a></th><td><p>Set the log level for the agent, making logging more or less verbose. Defaults to notice. Allowed values are: debug, info, error, warn, fatal (default: "notice")<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_LOG_LEVEL</code></p></td></tr>
<tr id="experiment"><th><code>--experiment value</code> <a class="Docs__attribute__link" href="#experiment">#</a></th><td><p>Enable experimental features within the buildkite-agent<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_EXPERIMENT</code></p></td></tr>
<tr id="profile"><th><code>--profile value</code> <a class="Docs__attribute__link" href="#profile">#</a></th><td><p>Enable a profiling mode, either cpu, memory, mutex or block<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_PROFILE</code></p></td></tr>
<tr id="agent-access-token"><th><code>--agent-access-token value</code> <a class="Docs__attribute__link" href="#agent-access-token">#</a></th><td><p>The access token used to identify the agent<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_ACCESS_TOKEN</code></p></td></tr>
<tr id="endpoint"><th><code>--endpoint value</code> <a class="Docs__attribute__link" href="#endpoint">#</a></th><td><p>The Agent API endpoint (default: "<code>https://agent.buildkite.com/v3</code>")<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_ENDPOINT</code></p></td></tr>
<tr id="no-http2"><th><code>--no-http2 </code> <a class="Docs__attribute__link" href="#no-http2">#</a></th><td><p>Disable HTTP2 when communicating with the Agent API (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_NO_HTTP2</code></p></td></tr>
<tr id="debug-http"><th><code>--debug-http </code> <a class="Docs__attribute__link" href="#debug-http">#</a></th><td><p>Enable HTTP debug mode, which dumps all request and response bodies to the log (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_DEBUG_HTTP</code></p></td></tr>
<tr id="trace-http"><th><code>--trace-http </code> <a class="Docs__attribute__link" href="#trace-http">#</a></th><td><p>Enable HTTP trace mode, which logs timings for each HTTP request. Timings are logged at the debug level unless a request fails at the network level in which case they are logged at the error level (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_TRACE_HTTP</code></p></td></tr>
<tr id="job"><th><code>--job value</code> <a class="Docs__attribute__link" href="#job">#</a></th><td><p>Which job should the artifacts be uploaded to<br /><strong>Environment variable</strong>: <code>$BUILDKITE_JOB_ID</code></p></td></tr>
<tr id="content-type"><th><code>--content-type value</code> <a class="Docs__attribute__link" href="#content-type">#</a></th><td><p>A specific Content-Type to set for the artifacts (otherwise detected)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_ARTIFACT_CONTENT_TYPE</code></p></td></tr>
<tr id="literal"><th><code>--literal </code> <a class="Docs__attribute__link" href="#literal">#</a></th><td><p>Disables parsing of the upload paths as glob patterns; each path will be treated as a single literal file path (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_ARTIFACT_LITERAL</code></p></td></tr>
<tr id="delimiter"><th><code>--delimiter value</code> <a class="Docs__attribute__link" href="#delimiter">#</a></th><td><p>Changes the delimiter used to split the upload paths into multiple paths; it can be more than 1 character. When set to the empty string, no splitting occurs (default: ";")<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_ARTIFACT_DELIMITER</code></p></td></tr>
<tr id="glob-resolve-follow-symlinks"><th><code>--glob-resolve-follow-symlinks </code> <a class="Docs__attribute__link" href="#glob-resolve-follow-symlinks">#</a></th><td><p>Follow symbolic links to directories while resolving globs. Note: this will not prevent symlinks to files from being uploaded. Use --upload-skip-symlinks to do that (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_ARTIFACT_GLOB_RESOLVE_FOLLOW_SYMLINKS</code></p></td></tr>
<tr id="upload-skip-symlinks"><th><code>--upload-skip-symlinks </code> <a class="Docs__attribute__link" href="#upload-skip-symlinks">#</a></th><td><p>After the glob has been resolved to a list of files to upload, skip uploading those that are symlinks to files (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_ARTIFACT_UPLOAD_SKIP_SYMLINKS</code></p></td></tr>
<tr id="follow-symlinks"><th><code>--follow-symlinks --glob-resolve-follow-symlinks</code> <a class="Docs__attribute__link" href="#follow-symlinks">#</a></th><td><p>Follow symbolic links while resolving globs. Note this argument is deprecated. Use --glob-resolve-follow-symlinks instead (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_ARTIFACT_SYMLINKS</code></p></td></tr>
<tr id="no-multipart-artifact-upload"><th><code>--no-multipart-artifact-upload </code> <a class="Docs__attribute__link" href="#no-multipart-artifact-upload">#</a></th><td><p>For Buildkite-hosted artifacts, disables the use of multipart uploads. Has no effect on uploads to other destinations such as custom cloud buckets (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_NO_MULTIPART_ARTIFACT_UPLOAD</code></p></td></tr>
</table>

### Artifact upload examples

Uploading a specific file:

```bash
buildkite-agent artifact upload log/test.log
```

Uploading all the jpegs and pngs, in all folders and subfolders:

```bash
buildkite-agent artifact upload "*/**/*.jpg;*/**/*.jpeg;*/**/*.png"
```

Uploading all the log files in the log folder:

```bash
buildkite-agent artifact upload "log/*.log"
```

Uploading all the files and folders inside the `coverage` directory:

```bash
buildkite-agent artifact upload "coverage/**/*"
```

Uploading a file name with special characters, for example, `hello??.html`:

```bash
buildkite-agent artifact upload "hello\?\?.html"
```

### Artifact upload glob syntax

Glob path patterns are used throughout Buildkite for specifying artifact uploads.

The source path you supply to the upload command will be replicated exactly at the destination. If you run:

```bash
buildkite-agent artifact upload log/test.log
```

Buildkite will store the file at `log/test.log`. If you want it to be stored as `test.log` without the full path, then you'll need to change into the file's directory before running your upload command:

```bash
cd log
buildkite-agent artifact upload test.log
```

Learn more about Buildkite's glob syntax from the [Glob pattern syntax](/docs/pipelines/configure/glob-pattern-syntax) page.

## Downloading artifacts

Use this command in your build scripts to download artifacts.

### Usage

`buildkite-agent artifact download [options] <query> <destination>`

### Description

Downloads artifacts matching &lt;query&gt; from Buildkite to &lt;destination&gt;
directory on the local machine.

Note: You need to ensure that your search query is surrounded by quotes if
using a wild card as the built-in shell path globbing will expand the wild
card and break the query.

If the last path component of &lt;destination&gt; matches the first path component
of your &lt;query&gt;, the last component of &lt;destination&gt; is dropped from the
final path. For example, a query of &#39;app/logs/*&#39; with a destination of
&#39;foo/app&#39; will write any matched artifact files to &#39;foo/app/logs/&#39;, relative
to the current working directory.

You can also change working directory to the intended destination and use a
&lt;destination&gt; of &#39;.&#39; to always create a directory hierarchy matching the
artifact paths.

### Example

```shell
buildkite-agent artifact download "pkg/*.tar.gz" . --build xxx
```

This will search across all the artifacts for the build with files that match that part.
The first argument is the search query, and the second argument is the download destination.

If you&#39;re trying to download a specific file, and there are multiple artifacts from different
jobs, you can target the particular job you want to download the artifact from:

```shell
buildkite-agent artifact download "pkg/*.tar.gz" . --step "tests" --build xxx
```

You can also use the step&#39;s jobs id (provided by the environment variable $BUILDKITE_JOB_ID)

### Options

<table class="Docs__attribute__table">
<tr id="no-color"><th><code>--no-color </code> <a class="Docs__attribute__link" href="#no-color">#</a></th><td><p>Don't show colors in logging (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_NO_COLOR</code></p></td></tr>
<tr id="debug"><th><code>--debug </code> <a class="Docs__attribute__link" href="#debug">#</a></th><td><p>Enable debug mode. Synonym for `--log-level debug`. Takes precedence over `--log-level` (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_DEBUG</code></p></td></tr>
<tr id="log-level"><th><code>--log-level value</code> <a class="Docs__attribute__link" href="#log-level">#</a></th><td><p>Set the log level for the agent, making logging more or less verbose. Defaults to notice. Allowed values are: debug, info, error, warn, fatal (default: "notice")<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_LOG_LEVEL</code></p></td></tr>
<tr id="experiment"><th><code>--experiment value</code> <a class="Docs__attribute__link" href="#experiment">#</a></th><td><p>Enable experimental features within the buildkite-agent<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_EXPERIMENT</code></p></td></tr>
<tr id="profile"><th><code>--profile value</code> <a class="Docs__attribute__link" href="#profile">#</a></th><td><p>Enable a profiling mode, either cpu, memory, mutex or block<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_PROFILE</code></p></td></tr>
<tr id="agent-access-token"><th><code>--agent-access-token value</code> <a class="Docs__attribute__link" href="#agent-access-token">#</a></th><td><p>The access token used to identify the agent<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_ACCESS_TOKEN</code></p></td></tr>
<tr id="endpoint"><th><code>--endpoint value</code> <a class="Docs__attribute__link" href="#endpoint">#</a></th><td><p>The Agent API endpoint (default: "<code>https://agent.buildkite.com/v3</code>")<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_ENDPOINT</code></p></td></tr>
<tr id="no-http2"><th><code>--no-http2 </code> <a class="Docs__attribute__link" href="#no-http2">#</a></th><td><p>Disable HTTP2 when communicating with the Agent API (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_NO_HTTP2</code></p></td></tr>
<tr id="debug-http"><th><code>--debug-http </code> <a class="Docs__attribute__link" href="#debug-http">#</a></th><td><p>Enable HTTP debug mode, which dumps all request and response bodies to the log (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_DEBUG_HTTP</code></p></td></tr>
<tr id="trace-http"><th><code>--trace-http </code> <a class="Docs__attribute__link" href="#trace-http">#</a></th><td><p>Enable HTTP trace mode, which logs timings for each HTTP request. Timings are logged at the debug level unless a request fails at the network level in which case they are logged at the error level (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_TRACE_HTTP</code></p></td></tr>
<tr id="step"><th><code>--step value</code> <a class="Docs__attribute__link" href="#step">#</a></th><td><p>Scope the search to a particular step. Can be the step's key or label, or a Job ID</p></td></tr>
<tr id="build"><th><code>--build value</code> <a class="Docs__attribute__link" href="#build">#</a></th><td><p>The build that the artifacts were uploaded to<br /><strong>Environment variable</strong>: <code>$BUILDKITE_BUILD_ID</code></p></td></tr>
<tr id="include-retried-jobs"><th><code>--include-retried-jobs </code> <a class="Docs__attribute__link" href="#include-retried-jobs">#</a></th><td><p>Include artifacts from retried jobs in the search (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_INCLUDE_RETRIED_JOBS</code></p></td></tr>
</table>

### Artifact download examples

Downloading a specific file into the current directory:

```bash
buildkite-agent artifact download build.zip .
```

Downloading a specific file into a specific directory (note the trailing slash):

```bash
buildkite-agent artifact download build.zip tmp/
```

Downloading all the files uploaded to `log` (including all subdirectories) into a local `log` directory (note that local directories will be created to match the uploaded file paths):

```bash
buildkite-agent artifact download "log/*" .
```

Downloading all the files uploaded to `coverage` (including all subdirectories) into a local `tmp/coverage` directory (note that local directories are created to match the uploaded file path):

```bash
buildkite-agent artifact download "coverage/*" tmp/
```

Downloading all images (from any directory) into a local `images/` directory (note that local directories are created to match the uploaded file path, and that you can run multiple download commands into the same directory):

```bash
buildkite-agent artifact download "*.jpg" images/
buildkite-agent artifact download "*.jpeg" images/
buildkite-agent artifact download "*.png" images/
```

### Artifact download pattern syntax

Artifact downloads support pattern-matching using the `*` character.

Unlike artifact upload glob patterns, these operate over the entire path and not just between separator characters. For example, a download path pattern of `log/*` matches all files under the log directory and all subdirectories.

There is no need to escape characters such as `?`, `[` and `]`.

## Downloading artifacts outside a running build

The `buildkite-agent artifact download` command relies on environment variables that are set by the agent while a build is running.

For example, executing the `buildkite-agent artifact download` command on your local machine would return an error about missing environment variables. However, when this command is executed as part of a build, the agent has set the required variables, and the command will be able to run.

If you want to download an artifact from outside a build, you can use the [Artifact Download API](/docs/apis/rest-api/artifacts#download-an-artifact).

## Searching artifacts

Return a list of artifacts that match a query.

### Usage

`buildkite-agent artifact search [options] <query>`

### Description

Searches for build artifacts specified by &lt;query&gt; on Buildkite

Note: You need to ensure that your search query is surrounded by quotes if
using a wild card as the built-in shell path globbing will provide files,
which will break the search.

### Example

```shell
buildkite-agent artifact search "pkg/*.tar.gz" --build xxx
```

This will search across all uploaded artifacts in a build for files that match that query.
The first argument is the search query.

If you&#39;re trying to find a specific file, and there are multiple artifacts from different
jobs, you can target the particular job you want to search the artifacts from using --step:

```shell
buildkite-agent artifact search "pkg/*.tar.gz" --step "tests" --build xxx
```

You can also use the step&#39;s job id (provided by the environment variable $BUILDKITE_JOB_ID)

Output formatting can be altered with the --format flag as follows:

```shell
buildkite-agent artifact search "*" --format "%p\n"
```

The above will return a list of filenames separated by newline.

### Options

<table class="Docs__attribute__table">
<tr id="no-color"><th><code>--no-color </code> <a class="Docs__attribute__link" href="#no-color">#</a></th><td><p>Don't show colors in logging (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_NO_COLOR</code></p></td></tr>
<tr id="debug"><th><code>--debug </code> <a class="Docs__attribute__link" href="#debug">#</a></th><td><p>Enable debug mode. Synonym for `--log-level debug`. Takes precedence over `--log-level` (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_DEBUG</code></p></td></tr>
<tr id="log-level"><th><code>--log-level value</code> <a class="Docs__attribute__link" href="#log-level">#</a></th><td><p>Set the log level for the agent, making logging more or less verbose. Defaults to notice. Allowed values are: debug, info, error, warn, fatal (default: "notice")<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_LOG_LEVEL</code></p></td></tr>
<tr id="experiment"><th><code>--experiment value</code> <a class="Docs__attribute__link" href="#experiment">#</a></th><td><p>Enable experimental features within the buildkite-agent<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_EXPERIMENT</code></p></td></tr>
<tr id="profile"><th><code>--profile value</code> <a class="Docs__attribute__link" href="#profile">#</a></th><td><p>Enable a profiling mode, either cpu, memory, mutex or block<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_PROFILE</code></p></td></tr>
<tr id="agent-access-token"><th><code>--agent-access-token value</code> <a class="Docs__attribute__link" href="#agent-access-token">#</a></th><td><p>The access token used to identify the agent<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_ACCESS_TOKEN</code></p></td></tr>
<tr id="endpoint"><th><code>--endpoint value</code> <a class="Docs__attribute__link" href="#endpoint">#</a></th><td><p>The Agent API endpoint (default: "<code>https://agent.buildkite.com/v3</code>")<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_ENDPOINT</code></p></td></tr>
<tr id="no-http2"><th><code>--no-http2 </code> <a class="Docs__attribute__link" href="#no-http2">#</a></th><td><p>Disable HTTP2 when communicating with the Agent API (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_NO_HTTP2</code></p></td></tr>
<tr id="debug-http"><th><code>--debug-http </code> <a class="Docs__attribute__link" href="#debug-http">#</a></th><td><p>Enable HTTP debug mode, which dumps all request and response bodies to the log (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_DEBUG_HTTP</code></p></td></tr>
<tr id="trace-http"><th><code>--trace-http </code> <a class="Docs__attribute__link" href="#trace-http">#</a></th><td><p>Enable HTTP trace mode, which logs timings for each HTTP request. Timings are logged at the debug level unless a request fails at the network level in which case they are logged at the error level (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_TRACE_HTTP</code></p></td></tr>
<tr id="step"><th><code>--step value</code> <a class="Docs__attribute__link" href="#step">#</a></th><td><p>Scope the search to a particular step by using either its name or job ID</p></td></tr>
<tr id="build"><th><code>--build value</code> <a class="Docs__attribute__link" href="#build">#</a></th><td><p>The build that the artifacts were uploaded to<br /><strong>Environment variable</strong>: <code>$BUILDKITE_BUILD_ID</code></p></td></tr>
<tr id="include-retried-jobs"><th><code>--include-retried-jobs </code> <a class="Docs__attribute__link" href="#include-retried-jobs">#</a></th><td><p>Include artifacts from retried jobs in the search (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_INCLUDE_RETRIED_JOBS</code></p></td></tr>
<tr id="allow-empty-results"><th><code>--allow-empty-results </code> <a class="Docs__attribute__link" href="#allow-empty-results">#</a></th><td><p>By default, searches exit 1 if there are no results. If this flag is set, searches will exit 0 with an empty set (default: false)</p></td></tr>
<tr id="format"><th><code>--format value</code> <a class="Docs__attribute__link" href="#format">#</a></th><td><p>Output formatting of results. See below for listing of available format specifiers. (default: "%j %p %c\\n")</p></td></tr>
</table>

Format specifiers:

%i    UUID of the artifact

%p    Artifact path

%c    Artifact creation time (an ISO 8601 / RFC-3339 formatted UTC timestamp)

%j    UUID of the job that uploaded the artifact, helpful for subsequent artifact downloads

%s    File size of the artifact in bytes

%S    SHA1 checksum of the artifact

%T    SHA256 checksum of the artifact

%u    Download URL for the artifact, though consider using &#39;buildkite-agent artifact download&#39; instead

## Parallelized steps

Currently, Buildkite does not support collating artifacts from parallelized steps under a single key. Thus using the `--step` option with a parallelized step key will return only artifacts from the last completed step.

If you are trying to collate artifacts from parallelized steps, it is best to upload these files with a unique path or name and omit the `--step` flag.

```bash
buildkite-agent artifact <download or search> "artifacts/path/*" . --build $BUILDKITE_BUILD_ID
```

## Fetching the SHA of an artifact

Use this command in your build scripts to verify downloaded artifacts against the original SHA-1 of the file.

### Usage

`buildkite-agent artifact shasum [options...]`

### Description

Prints the SHA-1 or SHA-256 hash for the single artifact specified by a
search query.

The hash is fetched from Buildkite&#39;s API, having been generated client-side
by the agent during artifact upload.

A search query that does not match exactly one artifact results in an error.

Note: You need to ensure that your search query is surrounded by quotes if
using a wild card as the built-in shell path globbing will provide files,
which will break the download.

### Example

```shell
buildkite-agent artifact shasum "pkg/release.tar.gz" --build xxx
```

This will search for all files in the build with path &#34;pkg/release.tar.gz&#34;,
and if exactly one match is found, the SHA-1 hash generated during upload
is printed.

If you would like to target artifacts from a specific build step, you can do
so by using the --step argument.

```shell
buildkite-agent artifact shasum "pkg/release.tar.gz" --step "release" --build xxx
```

You can also use the step&#39;s job ID (provided by the environment variable $BUILDKITE_JOB_ID)

The `--sha256` argument requests SHA-256 instead of SHA-1; this is only
available for artifacts uploaded since SHA-256 support was added to the
agent.

### Options

<table class="Docs__attribute__table">
<tr id="no-color"><th><code>--no-color </code> <a class="Docs__attribute__link" href="#no-color">#</a></th><td><p>Don't show colors in logging (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_NO_COLOR</code></p></td></tr>
<tr id="debug"><th><code>--debug </code> <a class="Docs__attribute__link" href="#debug">#</a></th><td><p>Enable debug mode. Synonym for `--log-level debug`. Takes precedence over `--log-level` (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_DEBUG</code></p></td></tr>
<tr id="log-level"><th><code>--log-level value</code> <a class="Docs__attribute__link" href="#log-level">#</a></th><td><p>Set the log level for the agent, making logging more or less verbose. Defaults to notice. Allowed values are: debug, info, error, warn, fatal (default: "notice")<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_LOG_LEVEL</code></p></td></tr>
<tr id="experiment"><th><code>--experiment value</code> <a class="Docs__attribute__link" href="#experiment">#</a></th><td><p>Enable experimental features within the buildkite-agent<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_EXPERIMENT</code></p></td></tr>
<tr id="profile"><th><code>--profile value</code> <a class="Docs__attribute__link" href="#profile">#</a></th><td><p>Enable a profiling mode, either cpu, memory, mutex or block<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_PROFILE</code></p></td></tr>
<tr id="agent-access-token"><th><code>--agent-access-token value</code> <a class="Docs__attribute__link" href="#agent-access-token">#</a></th><td><p>The access token used to identify the agent<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_ACCESS_TOKEN</code></p></td></tr>
<tr id="endpoint"><th><code>--endpoint value</code> <a class="Docs__attribute__link" href="#endpoint">#</a></th><td><p>The Agent API endpoint (default: "<code>https://agent.buildkite.com/v3</code>")<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_ENDPOINT</code></p></td></tr>
<tr id="no-http2"><th><code>--no-http2 </code> <a class="Docs__attribute__link" href="#no-http2">#</a></th><td><p>Disable HTTP2 when communicating with the Agent API (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_NO_HTTP2</code></p></td></tr>
<tr id="debug-http"><th><code>--debug-http </code> <a class="Docs__attribute__link" href="#debug-http">#</a></th><td><p>Enable HTTP debug mode, which dumps all request and response bodies to the log (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_DEBUG_HTTP</code></p></td></tr>
<tr id="trace-http"><th><code>--trace-http </code> <a class="Docs__attribute__link" href="#trace-http">#</a></th><td><p>Enable HTTP trace mode, which logs timings for each HTTP request. Timings are logged at the debug level unless a request fails at the network level in which case they are logged at the error level (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_TRACE_HTTP</code></p></td></tr>
<tr id="sha256"><th><code>--sha256 </code> <a class="Docs__attribute__link" href="#sha256">#</a></th><td><p>Request SHA-256 instead of SHA-1, errors if SHA-256 not available (default: false)</p></td></tr>
<tr id="step"><th><code>--step value</code> <a class="Docs__attribute__link" href="#step">#</a></th><td><p>Scope the search to a particular step by its name or job ID</p></td></tr>
<tr id="build"><th><code>--build value</code> <a class="Docs__attribute__link" href="#build">#</a></th><td><p>The build that the artifact was uploaded to<br /><strong>Environment variable</strong>: <code>$BUILDKITE_BUILD_ID</code></p></td></tr>
<tr id="include-retried-jobs"><th><code>--include-retried-jobs </code> <a class="Docs__attribute__link" href="#include-retried-jobs">#</a></th><td><p>Include artifacts from retried jobs in the search (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_INCLUDE_RETRIED_JOBS</code></p></td></tr>
</table>

## Using your private AWS S3 bucket

You can configure the `buildkite-agent artifact` command to store artifacts in
your private Amazon S3 bucket. To do so, you'll need to export some artifact
environment variables.

Environment Variable | Required | Default Value | Description
--- | --- | --- | ---
`BUILDKITE_ARTIFACT_UPLOAD_DESTINATION` | Yes | N/A | An S3 scheme URL for the bucket and path prefix, for example, s3://your-bucket/path/prefix/
`BUILDKITE_S3_DEFAULT_REGION` | No | N/A | Which AWS Region to use to locate your S3 bucket, if absent or blank `buildkite-agent` will also consult `AWS_REGION`, `AWS_DEFAULT_REGION`, and finally the EC2 instance metadata service.
`BUILDKITE_S3_ACL` | No | `public-read` | The S3 Object ACL to apply to uploads, one of `private`, `public-read`, `public-read-write`, `authenticated-read`, `bucket-owner-read`, `bucket-owner-full-control`.
`BUILDKITE_S3_SSE_ENABLED` | No | `false` | If `true`, bucket uploads request AES256 server side encryption.
`BUILDKITE_S3_ACCESS_URL` | No | `https://$bucket.s3.amazonaws.com` | If set, overrides the base URL used for the artifact's location stored with the Buildkite API.
`BUILDKITE_S3_ENDPOINT` | No | N/A | URL of the self-hosted S3 compatible endpoint, for example, `https://instance_public_ip:port`. Note that setting this environment variable still requires setting the `BUILDKITE_ARTIFACT_UPLOAD_DESTINATION` environment variable value. However, the `BUILDKITE_ARTIFACT_UPLOAD_DESTINATION` value is ignored during the artifacts upload process, and artifacts will be uploaded to the respective S3 compatible endpoint.
{: class="responsive-table"}

You can set these environment variables from a variety of places. Exporting them
from an [environment hook](/docs/agent/hooks#job-lifecycle-hooks) defined in
your [agent `hooks-path` directory](/docs/agent/hooks#hook-locations-agent-hooks)
ensures they are applied to all jobs:

```bash
export BUILDKITE_ARTIFACT_UPLOAD_DESTINATION="s3://name-of-your-s3-bucket/$BUILDKITE_PIPELINE_ID/$BUILDKITE_BUILD_ID/$BUILDKITE_JOB_ID"
export BUILDKITE_S3_DEFAULT_REGION="eu-central-1" # default: us-east-1
```

### Uploading artifacts to multiple AWS S3 buckets in different regions

To upload artifacts to multiple AWS S3 buckets in different regions within a single pipeline, configure the `BUILDKITE_ARTIFACT_UPLOAD_DESTINATION` and `BUILDKITE_S3_DEFAULT_REGION` environment variables at the step level. Defining these variables per step ensures that each upload uses the correct bucket and region. For example, one step can target a bucket in `us-east-1`, while another targets a bucket in `eu-central-1`:

```bash
steps:
  - label: "Upload to us-east-1 bucket"
    command:
      - echo "hello world" > test1.txt
      - buildkite-agent artifact upload test1.txt
    env:
      BUILDKITE_S3_DEFAULT_REGION: "us-east-1"
      BUILDKITE_ARTIFACT_UPLOAD_DESTINATION: "s3://my-bucket-east/"

  - label: "Upload to eu-central-1 bucket"
    command:
      - echo "hello world" > test2.txt
      - buildkite-agent artifact upload test2.txt
    env:
      BUILDKITE_S3_DEFAULT_REGION: "eu-central-1"
      BUILDKITE_ARTIFACT_UPLOAD_DESTINATION: "s3://my-bucket-central/"
```

### IAM permissions

Make sure your agent instances have the following IAM policy to
read and write objects in the bucket, for example:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "s3:GetObject",
                "s3:GetObjectAcl",
                "s3:GetObjectVersion",
                "s3:GetObjectVersionAcl",
                "s3:ListBucket",
                "s3:PutObject",
                "s3:PutObjectAcl",
                "s3:PutObjectVersionAcl"
            ],
            "Resource": [
               "arn\:aws\:s3:::my-s3-bucket",
               "arn\:aws\:s3:::my-s3-bucket/*"
            ]
        }
    ]
}
```

If you are using the Elastic CI Stack for AWS, provide your bucket name in the
`ArtifactsBucket` template parameter for an appropriate IAM policy to be
included in the instance's IAM role.

### Credentials

`buildkite-agent artifact upload` will use the first available AWS credentials
from the following locations:

- Buildkite environment variables, `BUILDKITE_S3_ACCESS_KEY_ID`, `BUILDKITE_S3_SECRET_ACCESS_KEY`, `BUILDKITE_S3_SESSION_TOKEN`
- AWS environment variables, `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, `AWS_SESSION_TOKEN`
- Web Identity environment variables, `AWS_ROLE_ARN`, `AWS_ROLE_SESSION_NAME`, `AWS_WEB_IDENTITY_TOKEN_FILE`
- EC2 or ECS role, your EC2 instance or ECS task's IAM Role

If your agents are running on an AWS EC2 Instance, adding the
policy above to the instance's [IAM Role](http://docs.aws.amazon.com/AWSEC2/latest/UserGuide/iam-roles-for-amazon-ec2.html) and using the instance profile credentials is the
most secure option as there are no long lived credentials to manage.

If your agents are running outside of AWS, or you're unable to use an instance
profile, you can export
[long lived credentials](http://docs.aws.amazon.com/IAM/latest/UserGuide/id_credentials_access-keys.html)
belonging to an IAM user using one of the environment variable groups listed
above. See the [Managing pipeline secrets](/docs/pipelines/security/secrets/managing)
documentation for how to securely set up these environment variables.

### Access control

By default the agent will create objects with the [`public-read` ACL](https://docs.aws.amazon.com/AmazonS3/latest/userguide/acl-overview.html#canned-acl). This allows the artifact links in the
Buildkite web interface to show the S3 object directly in the browser. You can
set this to `private` instead, exporting a value for the `BUILDKITE_S3_ACL`
environment variable:

```bash
export BUILDKITE_S3_ACL="private"
```

If you set your S3 ACL to `private` you won't be able to click through to the
artifacts in the Buildkite web interface. You can use an authenticating S3 proxy
such as [aws-s3-proxy](https://github.com/pottava/aws-s3-proxy) to provide web
access protected by HTTP Basic authentication, which will allow you to view
embedded assets such as HTML pages with images. To set the access URL for your
artifacts, export a value for the `BUILDKITE_S3_ACCESS_URL` environment
variable:

```bash
export BUILDKITE_S3_ACCESS_URL="https://buildkite-artifacts.example.com/"
```

## Using your private Google Cloud bucket

You can configure the `buildkite-agent artifact` command to store artifacts in
your private Google Cloud Storage bucket. For instructions for how to set this
up, see the [Google Cloud installation guide](/docs/agent/self-hosted/gcp#uploading-artifacts-to-google-cloud-storage).

## Using your Artifactory instance

You can configure the `buildkite-agent artifact` command to store artifacts in
Artifactory. For instructions for how to set this up, see our
[Artifactory guide](/docs/pipelines/integrations/artifacts-and-packages/artifactory).

## Using your private Azure Blob container

You can configure the `buildkite-agent artifact` command to store artifacts in
your private [Azure Blob Storage container](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-blobs-introduction).
Support for uploading artifacts to Azure Blob Storage was added in
[Agent v3.53.0](https://github.com/buildkite/agent/releases/tag/v3.53.0).

### Preparation

Firstly, make sure that each agent has access to Azure credentials.
[By default](https://pkg.go.dev/github.com/Azure/azure-sdk-for-go/sdk/azidentity#readme-defaultazurecredential),
these can be provided using:

- Azure environment variables such as `AZURE_CLIENT_ID`.
- Loaded by a Kubernetes workload identity hook.
- Loaded on a host with Azure Managed Identity enabled.
- Loaded from a user logged in with the Azure CLI.

You can also use an account key or connection string by setting one of these
environment variables:

```shell
# To use an account key:
export BUILDKITE_AZURE_BLOB_ACCESS_KEY='...'

# To use a connection string:
export BUILDKITE_AZURE_BLOB_CONNECTION_STRING='...'
```

Since these can contain access credentials, they are
[redacted from job logs by default](/docs/pipelines/configure/managing-log-output#redacted-environment-variables).

Make sure you have a valid storage account name and container. These can be
created with the Azure web console or Azure CLI.

Make sure the Azure principal for the Azure credential has a role assignment
that permits reading and writing to the container, for example,
[Storage Blob Data Contributor](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#storage-blob-data-contributor).

### Configuration

Configure the agent to target your container by exporting the
`BUILDKITE_ARTIFACT_UPLOAD_DESTINATION` environment variable using an
[environment agent hook](/docs/agent/hooks) (this can not be set using the
Buildkite web interface, API, or during pipeline upload). For example:

```shell
export BUILDKITE_ARTIFACT_UPLOAD_DESTINATION="https://mystorageaccountname.blob.core.windows.net/my-container/$BUILDKITE_PIPELINE_ID/$BUILDKITE_BUILD_ID/$BUILDKITE_JOB_ID"
```

Alternatively, when running `buildkite-agent artifact upload` or `buildkite-agent artifact
download`, you can specify the full upload destination in the form:

```
https://[storageaccountname].blob.core.windows.net/[container]/[path]
```

### Usage

If you have not [explicitly enabled anonymous public access](https://learn.microsoft.com/en-us/azure/storage/blobs/anonymous-read-access-configure?tabs=portal)
to data in your container, you won't have automatic access to your artifacts
through the links in the Buildkite web interface.

To generate SAS (shared access signatures) as part of each artifact URL, which
allow temporary access to your artifacts, you will need to set a token duration
as well as use a shared key for the credential:

```shell
# Provide a token duration; SAS URLs will expire after this length of time.
export BUILDKITE_AZURE_BLOB_SAS_TOKEN_DURATION=1h

# Generating SAS tokens requires an account key.
export BUILDKITE_AZURE_BLOB_ACCOUNT_KEY='...'
```
