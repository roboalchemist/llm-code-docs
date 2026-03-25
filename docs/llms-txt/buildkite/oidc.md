# Source: https://buildkite.com/docs/package-registries/security/oidc.md

# Source: https://buildkite.com/docs/pipelines/security/oidc.md

# Source: https://buildkite.com/docs/agent/cli/reference/oidc.md

# buildkite-agent oidc

The Buildkite agent's `oidc` command allows you to request an OpenID Connect (OIDC) token from Buildkite, representing the current pipeline and its job. These tokens can be exchanged for specific roles on federated systems like [AWS](https://aws.amazon.com/), [GCP](https://cloud.google.com/), [Azure](https://azure.microsoft.com/) and many others.

Refer to the following documentation for more information:

- The [What is OpenID Connect](https://openid.net/developers/how-connect-works/) overview on the OpenID web site for more details about how OIDC works.
- The [OpenID Connect Core documentation](https://openid.net/specs/openid-connect-core-1_0.html#IDToken) for more information about how OIDC tokens are constructed and how to extract and use claims.

Learn more about how to restrict your Buildkite agents' access to deployment environments like AWS, from the OIDC in [Buildkite Pipelines](/docs/pipelines/security/oidc) and with [AWS](/docs/pipelines/security/oidc/aws) documentation pages, as well as the [Buildkite Package Registries](/docs/package-registries/security/oidc) documentation page.

> 📘
> From version 3.104.0 of the Buildkite agent, OIDC tokens are automatically redacted from build logs by default, with an optional `skip-redaction` flag to disable this behavior when needed. This behavior is similar to the [buildkite-agent secret get](/docs/agent/cli/reference/secret) command for redacting the token.

## Request OIDC token

### Usage

`buildkite-agent oidc request-token [options...]`

### Description

Requests and prints an OIDC token from Buildkite that claims the Job ID
(amongst other things) and the specified audience. If no audience is
specified, the endpoint&#39;s default audience will be claimed.

### Example

```shell
buildkite-agent oidc request-token --audience sts.amazonaws.com
```

Requests and prints an OIDC token from Buildkite that claims the Job ID
(amongst other things) and the audience &#34;sts.amazonaws.com&#34;.

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
<tr id="audience"><th><code>--audience value</code> <a class="Docs__attribute__link" href="#audience">#</a></th><td><p>The audience that will consume the OIDC token. The API will choose a default audience if it is omitted.</p></td></tr>
<tr id="lifetime"><th><code>--lifetime value</code> <a class="Docs__attribute__link" href="#lifetime">#</a></th><td><p>The time (in seconds) the OIDC token will be valid for before expiry. Must be a non-negative integer. If the flag is omitted or set to 0, the API will choose a default finite lifetime. (default: 0)</p></td></tr>
<tr id="job"><th><code>--job value</code> <a class="Docs__attribute__link" href="#job">#</a></th><td><p>Buildkite Job Id to claim in the OIDC token<br /><strong>Environment variable</strong>: <code>$BUILDKITE_JOB_ID</code></p></td></tr>
<tr id="claim"><th><code>--claim value</code> <a class="Docs__attribute__link" href="#claim">#</a></th><td><p>Claims to add to the OIDC token<br /><strong>Environment variable</strong>: <code>$BUILDKITE_OIDC_TOKEN_CLAIMS</code></p></td></tr>
<tr id="aws-session-tag"><th><code>--aws-session-tag value</code> <a class="Docs__attribute__link" href="#aws-session-tag">#</a></th><td><p>Add claims as AWS Session Tags<br /><strong>Environment variable</strong>: <code>$BUILDKITE_OIDC_TOKEN_AWS_SESSION_TAGS</code></p></td></tr>
<tr id="skip-redaction"><th><code>--skip-redaction </code> <a class="Docs__attribute__link" href="#skip-redaction">#</a></th><td><p>Skip redacting the OIDC token from the logs. Then, the command will print the token to the Job's logs if called directly (default: false)<br /><strong>Environment variable</strong>: <code>$BUILDKITE_AGENT_OIDC_REQUEST_TOKEN_SKIP_TOKEN_REDACTION</code></p></td></tr>
<tr id="format"><th><code>--format value</code> <a class="Docs__attribute__link" href="#format">#</a></th><td><p>The format to output the token in. Supported values are 'jwt' (the default) and 'gcp'. When 'gcp' is specified, the token will be output in a JSON structure compatible with GCP's workload identity federation. (default: "jwt")</p></td></tr>
</table>

## OIDC URLs

If using a plugin, such as the [AWS assume-role-with-web-identity](https://github.com/buildkite-plugins/aws-assume-role-with-web-identity-buildkite-plugin) plugin, you'll need to provide an OpenID provider URL. You should set the provider URL to: https://agent.buildkite.com.

For specific endpoints for OpenID or JWKS, use:

- **OpenID Connect Discovery URL:** https://agent.buildkite.com/.well-known/openid-configuration
- **JWKS URI:** https://agent.buildkite.com/.well-known/jwks

## Claims

All of the following claims (with the exception of the [`aud` claim](#aud), which is usually overridden by the [`--audience` option](#audience)) are automatically generated by the Buildkite agent, and are based on metadata from the pipeline job it is currently building.

<table data-attributes data-attributes-required>
  <thead>
    <tr>
      <th>Claim</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
  <tr>
    <td><code>iss</code></td>
    <td>
      <p>Issuer</p>
      <p>Identifies the entity that issued the JWT.</p>
      <p><em>Example:</em> <code>https://agent.buildkite.com</code></p>
    </td>
  </tr>
   <tr>
    <td><code>sub</code></td>
    <td>
      <p>Subject</p>
      <p>Identifies the subject of the JWT, typically representing the user or entity being authenticated.</p>
      <p><em>Format:</em>
        <code>organization:ORGANIZATION_SLUG:pipeline:PIPELINE_SLUG:ref:REF:
        commit:BUILD_COMMIT:step:STEP_KEY</code>. </p>
      <p>If the build has a tag, <code>REF</code> is <code>refs/tags/TAG</code>.</p>
      <p>Otherwise, <code>REF</code> is <code>refs/heads/BRANCH</code>.</p>
      <p><em>Example:</em><code>organization:acme-inc:pipeline:super-duper-app:ref:refs/heads/main:commit:9f3182061f1e2cca4702c368cbc039b7dc9d4485:step:build</code></p>
    </td>
  </tr>
   <tr id="aud">
    <td><code>aud</code></td>
    <td>
      <p>Audience</p>
      <p>Identifies the intended audience for the JWT.</p>
      <p>Defaults to <code>https://buildkite.com/ORGANIZATION_SLUG</code>
         but can be overridden using the <code>
        --audience</code> flag</p>
    </td>
  </tr>
   <tr id="exp">
    <td><code>exp</code></td>
    <td>
      <p>Expiration time</p>
      <p>Specifies the expiration time of the JWT, after which the token is no longer valid.</p>
      <p>Defaults to 5 minutes in the future at generation, but can be overridden using the <code>
        --lifetime</code> flag.</p>
      <p><em>Example:</em> <code>1669015898</code></p>
    </td>
  </tr>
   <tr id="nbf">
    <td><code>nbf</code></td>
    <td>
      <p>Not before</p>
      <p>Specifies the time before which the JWT must not be accepted for processing.</p>
      <p>Set to the current timestamp at generation.</p>
      <p><em>Example:</em> <code>1669014898</code></p>
    </td>
  </tr>
   <tr id="iat">
    <td><code>iat</code></td>
    <td>
      <p>Issued at</p>
      <p>Specifies the time at which the JWT was issued. Set to the current timestamp
        at generation.</p>
      <p><em>Example:</em> <code>1669014898</code></p>
    </td>
  </tr>
   <tr id="organization-slug">
    <td><code>organization_slug</code></td>
    <td>
      <p>The organization's slug.</p>
      <p><em>Example:</em> <code>acme-inc</code></p>
    </td>
  </tr>
   <tr id="pipeline-slug">
    <td><code>pipeline_slug</code></td>
    <td>
      <p>The pipeline's slug.</p>
      <p><em>Example:</em> <code>super-duper-app</code></p>
    </td>
  </tr>
   <tr>
    <td><code>build_number</code></td>
    <td>
      <p>The build number.</p>
      <p><em>Example:</em> <code>1</code></p>
    </td>
  </tr>
   <tr id="build-branch">
    <td><code>build_branch</code></td>
    <td>
      <p>The repository branch used in the build.</p>
      <p><em>Example:</em> <code>main</code></p>
    </td>
  </tr>
  <tr>
    <td><code>build_tag</code></td>
    <td>
      <p>The tag of the build if enabled in Buildkite. This claim is only included
        if the tag is set.</p>
      <p><em>Example:</em> <code>1</code></p>
    </td>
  </tr>
  <tr>
    <td><code>build_commit</code></td>
    <td>
      <p>The SHA commit from the repository.</p>
      <p><em>Example:</em> <code>9f3182061f1e2cca4702c368cbc039b7dc9d4485</code></p>
    </td>
  </tr>
  <tr>
    <td><code>step_key</code></td>
    <td>
      <p>The <code>key</code> attribute of the step from the pipeline.
        If the key is not set for the step, <code>nil</code> is returned.</p>
      <p><em>Example:</em> <code>build_step</code></p>
    </td>
  </tr>
  <tr>
    <td><code>job_id</code></td>
    <td>
      <p>The job UUID.</p>
      <p><em>Example:</em> <code>0184990a-477b-4fa8-9968-496074483cee</code></p>
    </td>
  </tr>
  <tr>
    <td><code>agent_id</code></td>
    <td>
      <p>The agent UUID.</p>
      <p><em>Example:</em> <code>0184990a-4782-42b5-afc1-16715b10b8ff</code></p>
    </td>
  </tr>
  <tr>
    <td><code>runner_environment</code></td>
    <td>
      <p>Indicates whether the current job is being run on Buildkite hosted agents or the customer's own self-hosted agents.</p>
      <p><em>Valid values:</em> <code>buildkite-hosted</code>, <code>self-hosted</code></p>
    </td>
  </tr>
  <tr>
    <td><code>build_source</code></td>
    <td>
      <p>The source of the event that created the build.</p>
      <p><em>Valid values:</em> <code>ui</code>, <code>api</code>, <code>webhook</code>, <code>trigger_job</code>, <code>schedule</code></p>
    </td>
  </tr>
  </tbody>
</table>

### Optional claims

You can generate additional optional claims by adding `--claims` to the `buildkite-agent oidc request-token` command. The `--claims` option can also take multiple values.

For example, this command adds the Buildkite organization's UUID value as a claim to the OIDC token:

```sh
buildkite-agent oidc request-token ... --claim "organization_id"
```

This command adds both the Buildkite organization's UUID and pipeline's UUID values in their own additional claims to the OIDC token:

```sh
buildkite-agent oidc request-token ... --claim "organization_id,pipeline_id"
```

The following optional claims can be added, whose values are automatically generated by the Buildkite agent, and are based on the pipeline job it is currently building.

<table data-attributes data-attributes-required>
  <thead>
    <tr>
      <th>Claim</th>
      <th>Description</th>
    </tr>
  </thead>
  <tbody>
  <tr>
    <td><code>organization_id</code></td>
    <td>
      <p>The organization UUID.</p>
      <p><em>Example:</em> <code>0184990a-477b-4fa8-9968-496074483k77</code></p>
    </td>
  </tr>
  <tr>
    <td><code>pipeline_id</code></td>
    <td>
      <p>The pipeline UUID.</p>
      <p><em>Example:</em> <code>0184990a-4782-42b5-afc1-16715b10b1l0</code></p>
    </td>
  </tr>
  <tr>
    <td><code>build_id</code></td>
    <td>
      <p>The build UUID.</p>
      <p><em>Example:</em> <code>019583d7-3737-4e38-af67-f7cc356bd580</code></p>
    </td>
  </tr>
  <tr>
    <td><code>cluster_id</code></td>
    <td>
      <p>The cluster UUID if using clusters.</p>
      <p><em>Example:</em> <code>0191f956-042f-7ec4-aa62-8e5eeae396d0</code></p>
    </td>
  </tr>
  <tr>
    <td><code>cluster_name</code></td>
    <td>
      <p>The cluster name if using clusters.</p>
      <p><em>Example:</em> <code>default</code></p>
    </td>
  </tr>
  <tr>
    <td><code>queue_id</code></td>
    <td>
      <p>The cluster queue UUID if using clusters.</p>
      <p><em>Example:</em> <code>0191f956-62da-7515-b79b-bdecb519aa32</code></p>
    </td>
  </tr>
  <tr>
    <td><code>queue_key</code></td>
    <td>
      <p>The cluster queue key if using clusters.</p>
      <p><em>Example:</em> <code>runners</code></p>
    </td>
  </tr>
  <tr>
    <td><code>agent_tag:<var>NAME</var></code></td>
    <td>
      <p>An <a href="/docs/agent/cli/reference/start#setting-tags">agent tag</a></p>
      <p><em>Example:</em> <code>agent_tag:queue</code></p>
    </td>
  </tr>
  </tbody>
</table>

### Example token contents

OIDC tokens are JSON Web Tokens — [JWTs](https://datatracker.ietf.org/doc/html/rfc7519) — and the following is a complete example:

```json
{
  "iss": "https://agent.buildkite.com",
  "sub": "organization:acme-inc:pipeline:super-duper-app:ref:refs/heads/main:commit:9f3182061f1e2cca4702c368cbc039b7dc9d4485:step:build",
  "aud": "https://buildkite.com/acme-inc",
  "iat": 1669014898,
  "nbf": 1669014898,
  "exp": 1669015198,
  "organization_slug": "acme-inc",
  "pipeline_slug": "super-duper-app",
  "build_number": 1,
  "build_branch": "main",
  "build_tag": "v1.0.0",
  "build_commit": "9f3182061f1e2cca4702c368cbc039b7dc9d4485",
  "step_key": "build",
  "job_id": "0184990a-477b-4fa8-9968-496074483cee",
  "agent_id": "0184990a-4782-42b5-afc1-16715b10b8ff",
  "build_source": "ui",
  "runner_environment": "buildkite-hosted"
}
```

## AWS session tags

For Buildkite OIDC tokens used to integrate with Amazon Web Services (AWS), you can optionally include any of the supported claims in the [AWS session tag format required by the `AssumeRoleWithWebIdentity` operation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_session-tags.html#id_session-tags_adding-assume-role-idp).

These OIDC tokens also typically have an audience of `sts.amazonaws.com`. For example, this command generates an AWS compatible OIDC token that includes the `organization_slug` and `organization_id`:

```sh
buildkite-agent oidc request-token --audience sts.amazonaws.com --aws-session-tag "organization_slug,organization_id"
```

AWS requires that session tags are string values. Therefore:

- Numeric claim values (for example, `build_number`) are presented as strings.
- Nullable claim values (for example, `step_key`) are presented as `""` instead of the literal value `null`.

Learn more about using Buildkite OIDC tokens with AWS in [OIDC with AWS](/docs/pipelines/security/oidc/aws).

### Example token contents

When the `--aws-session-tag` flag has been used to generate an OIDC token, the contents includes a nested `https://aws.amazon.com/tags` claim:

```json
{
  "iss": "https://agent.buildkite.com",
  "sub": "organization:acme-inc:pipeline:super-duper-app:ref:refs/heads/main:commit:9f3182061f1e2cca4702c368cbc039b7dc9d4485:step:build",
  "aud": "https://buildkite.com/acme-inc",
  "iat": 1669014898,
  "nbf": 1669014898,
  "exp": 1669015198,
  "organization_slug": "acme-inc",
  "pipeline_slug": "super-duper-app",
  "build_number": 1,
  "build_branch": "main",
  "build_tag": "v1.0.0",
  "build_commit": "9f3182061f1e2cca4702c368cbc039b7dc9d4485",
  "step_key": "build",
  "job_id": "0184990a-477b-4fa8-9968-496074483cee",
  "agent_id": "0184990a-4782-42b5-afc1-16715b10b8ff",
  "build_source": "ui",
  "runner_environment": "buildkite-hosted",
  "https://aws.amazon.com/tags": {
    "principal_tags": {
      "organization_slug": [
        "acme-inc"
      ],
      "organization_id": [
        "f892efa9-103e-4d28-97a1-3b8616a0994d"
      ]
    }
  }
}
```
