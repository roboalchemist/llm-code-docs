# Source: https://buildkite.com/docs/agent/cli/reference/tool.md

# buildkite-agent tool

The Buildkite agent's `tool` subcommands are used for performing tasks that are expected to be called by a human as part of setting up a pipeline, rather than during the execution of a job. Any and all of these subcommand may be removed in the future into a separate CLI tool, so they should all be considered experimental.

> 🛠 Experimental feature
> The `tool` subcommand may be removed from the Buildkite agent in the future.

## Generate a JSON Web Key Set

### Usage

`buildkite-agent tool keygen [options...]`

### Description

This command generates a new JWS key pair, used for signing and verifying jobs
in Buildkite.

The pair is written as a JSON Web Key Set (JWKS) to two files, a private JWKS
file and a public JWKS file. The private JWKS should be used as for signing,
and the public JWKS for verification.

For more information about JWS, see https://tools.ietf.org/html/rfc7515 and
for information about JWKS, see https://tools.ietf.org/html/rfc7517

### Options

<table class="Docs__attribute__table">
<tr id="no-color"><th><code>--no-color </code> <a class="Docs__attribute__link" href="#no-color">#</a></th><td><p>Don't show colors in logging (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_NO_COLOR</code></p></td></tr>
<tr id="debug"><th><code>--debug </code> <a class="Docs__attribute__link" href="#debug">#</a></th><td><p>Enable debug mode. Synonym for `--log-level debug`. Takes precedence over `--log-level` (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_DEBUG</code></p></td></tr>
<tr id="log-level"><th><code>--log-level value</code> <a class="Docs__attribute__link" href="#log-level">#</a></th><td><p>Set the log level for the agent, making logging more or less verbose. Defaults to notice. Allowed values are: debug, info, error, warn, fatal (default: "notice")<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_LOG_LEVEL</code></p></td></tr>
<tr id="experiment"><th><code>--experiment value</code> <a class="Docs__attribute__link" href="#experiment">#</a></th><td><p>Enable experimental features within the buildkite-agent<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_EXPERIMENT</code></p></td></tr>
<tr id="profile"><th><code>--profile value</code> <a class="Docs__attribute__link" href="#profile">#</a></th><td><p>Enable a profiling mode, either cpu, memory, mutex or block<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_PROFILE</code></p></td></tr>
<tr id="alg"><th><code>--alg value</code> <a class="Docs__attribute__link" href="#alg">#</a></th><td><p>The JWS signing algorithm to use for the key pair. Defaults to 'EdDSA'. Valid algorithms are: [PS512 ES512 EdDSA]<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_KEYGEN_ALG</code></p></td></tr>
<tr id="key-id"><th><code>--key-id value</code> <a class="Docs__attribute__link" href="#key-id">#</a></th><td><p>The ID to use for the keys generated. If none is provided, a random one will be generated<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_KEYGEN_KEY_ID</code></p></td></tr>
<tr id="private-jwks-file"><th><code>--private-jwks-file value</code> <a class="Docs__attribute__link" href="#private-jwks-file">#</a></th><td><p>The filename to write the private key to. Defaults to a name based on the key id in the current directory<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_KEYGEN_PRIVATE_JWKS_FILE</code></p></td></tr>
<tr id="public-jwks-file"><th><code>--public-jwks-file value</code> <a class="Docs__attribute__link" href="#public-jwks-file">#</a></th><td><p>The filename to write the public keyset to. Defaults to a name based on the key id in the current directory<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_KEYGEN_PUBLIC_JWKS_FILE</code></p></td></tr>
</table>

## Sign a pipeline

### Usage

`buildkite-agent tool sign [options...] [pipeline-file]`

### Description

This command takes a pipeline in YAML format as input, and annotates the appropriate parts of
the pipeline with signatures. This can then be input into the YAML steps editor in the Buildkite
UI so that the agents running these steps can verify the signatures.

If a token is provided using the `graphql-token` flag, the tool will attempt to retrieve the
pipeline definition and repo using the Buildkite GraphQL API. If `update` is also set, it will
update the pipeline definition with the signed version using the GraphQL API too.

### Examples

Retrieving the pipeline from the GraphQL API and signing it:

```shell
$ buildkite-agent tool sign \
    --graphql-token <graphql token> \
    --organization-slug <your org slug> \
    --pipeline-slug <slug of the pipeline whose steps you want to sign \
    --jwks-file /path/to/private/key.json \
    --update
```

Signing a pipeline from a file:

```shell
$ buildkite-agent tool sign pipeline.yml \
    --jwks-file /path/to/private/key.json \
    --repo <repo url for your pipeline>
# or
$ cat pipeline.yml | buildkite-agent tool sign \
    --jwks-file /path/to/private/key.json \
    --repo <repo url for your pipeline>
```

### Options

<table class="Docs__attribute__table">
<tr id="no-color"><th><code>--no-color </code> <a class="Docs__attribute__link" href="#no-color">#</a></th><td><p>Don't show colors in logging (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_NO_COLOR</code></p></td></tr>
<tr id="debug"><th><code>--debug </code> <a class="Docs__attribute__link" href="#debug">#</a></th><td><p>Enable debug mode. Synonym for `--log-level debug`. Takes precedence over `--log-level` (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_DEBUG</code></p></td></tr>
<tr id="log-level"><th><code>--log-level value</code> <a class="Docs__attribute__link" href="#log-level">#</a></th><td><p>Set the log level for the agent, making logging more or less verbose. Defaults to notice. Allowed values are: debug, info, error, warn, fatal (default: "notice")<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_LOG_LEVEL</code></p></td></tr>
<tr id="experiment"><th><code>--experiment value</code> <a class="Docs__attribute__link" href="#experiment">#</a></th><td><p>Enable experimental features within the buildkite-agent<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_EXPERIMENT</code></p></td></tr>
<tr id="profile"><th><code>--profile value</code> <a class="Docs__attribute__link" href="#profile">#</a></th><td><p>Enable a profiling mode, either cpu, memory, mutex or block<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_PROFILE</code></p></td></tr>
<tr id="graphql-token"><th><code>--graphql-token value</code> <a class="Docs__attribute__link" href="#graphql-token">#</a></th><td><p>A token for the buildkite graphql API. This will be used to populate the value of the repository URL, and download the pipeline definition. Both `repo` and `pipeline-file` will be ignored in preference of values from the GraphQL API if the token in provided.<br /><strong>Environment variable</strong>: <code>$BUILDKITE_GRAPHQL_TOKEN</code></p></td></tr>
<tr id="update"><th><code>--update </code> <a class="Docs__attribute__link" href="#update">#</a></th><td><p>Update the pipeline using the GraphQL API after signing it. This can only be used if `graphql-token` is provided (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_TOOL_SIGN_UPDATE</code></p></td></tr>
<tr id="no-confirm"><th><code>--no-confirm </code> <a class="Docs__attribute__link" href="#no-confirm">#</a></th><td><p>Show confirmation prompts before updating the pipeline with the GraphQL API (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_TOOL_SIGN_NO_CONFIRM</code></p></td></tr>
<tr id="jwks-file"><th><code>--jwks-file value</code> <a class="Docs__attribute__link" href="#jwks-file">#</a></th><td><p>Path to a file containing a JWKS.<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_JWKS_FILE</code></p></td></tr>
<tr id="jwks-key-id"><th><code>--jwks-key-id value</code> <a class="Docs__attribute__link" href="#jwks-key-id">#</a></th><td><p>The JWKS key ID to use when signing the pipeline. If none is provided and the JWKS file contains only one key, that key will be used.<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_JWKS_KEY_ID</code></p></td></tr>
<tr id="signing-aws-kms-key"><th><code>--signing-aws-kms-key value</code> <a class="Docs__attribute__link" href="#signing-aws-kms-key">#</a></th><td><p>The AWS KMS key identifier which is used to sign pipelines.<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_AWS_KMS_KEY</code></p></td></tr>
<tr id="debug-signing"><th><code>--debug-signing </code> <a class="Docs__attribute__link" href="#debug-signing">#</a></th><td><p>Enable debug logging for pipeline signing. This can potentially leak secrets to the logs as it prints each step in full before signing. Requires debug logging to be enabled (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_DEBUG_SIGNING</code></p></td></tr>
<tr id="organization-slug"><th><code>--organization-slug value</code> <a class="Docs__attribute__link" href="#organization-slug">#</a></th><td><p>The organization slug. Required to connect to the GraphQL API.<br /><strong>Environment variable</strong>: <code>$BUILDKITE_ORGANIZATION_SLUG</code></p></td></tr>
<tr id="pipeline-slug"><th><code>--pipeline-slug value</code> <a class="Docs__attribute__link" href="#pipeline-slug">#</a></th><td><p>The pipeline slug. Required to connect to the GraphQL API.<br /><strong>Environment variable</strong>: <code>$BUILDKITE_PIPELINE_SLUG</code></p></td></tr>
<tr id="graphql-endpoint"><th><code>--graphql-endpoint value</code> <a class="Docs__attribute__link" href="#graphql-endpoint">#</a></th><td><p>The endpoint for the Buildkite GraphQL API. This is only needed if you are using the the graphql-token flag, and is mostly useful for development purposes (default: "https://graphql.buildkite.com/v1")<br /><strong>Environment variable</strong>: <code>$BUILDKITE_GRAPHQL_ENDPOINT</code></p></td></tr>
<tr id="repo"><th><code>--repo value</code> <a class="Docs__attribute__link" href="#repo">#</a></th><td><p>The URL of the pipeline's repository, which is used in the pipeline signature. If the GraphQL token is provided, this will be ignored.<br /><strong>Environment variable</strong>: <code>$BUILDKITE_REPO</code></p></td></tr>
</table>
