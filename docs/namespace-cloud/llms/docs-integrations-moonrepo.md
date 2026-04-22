<!-- Source: https://namespace.so/docs/integrations/moonrepo -->

# Moonrepo support

Moonrepo is a build system designed to improve developer productivity and streamline workflows.

Moonrepo is API compatible with Bazel remote caching.
Namespace provides high-performance [Bazel caching](/docs/integrations/bazel) with
very low network latency between runners and the cache storage. This allows your
Moonrepo workflows to reuse build artifacts across runs, irrespective of your
chosen granularity, significantly reducing build times.

## Getting started

To use Bazel caching in your Moonrepo builds, you can produce a configuration file using the [CLI](/docs/reference/cli/installation):

### Configure cache access

```
$

```
nsc cache bazel setup -o json --cred_path /tmp/bazelcache > out.json
```
```

This command generates short-term credentials, and emits the configuration in JSON format.
You can produce a [workspace configuration](https://moonrepo.dev/docs/config/workspace#unstable_remote) as follows:

```
$ cat <<-EOF > workspace.yaml
unstable_remote:
  host: '`jq -r '.endpoint' out.json`'
  mtls:
    caCert: '`jq -r '.server_ca_cert' out.json`'
    clientCert: '`jq -r '.client_cert' out.json`'
    clientKey: '`jq -r '.client_key' out.json`'
EOF
```

### Use the remote cache

```
$

```
moon run app:build
```
```

The workspace configuration file is picked up automatically for the next build invocation.

For details on how the remote cache works and how usage is accounted, check out the [Bazel caching](/docs/integrations/bazel) documentation.

Last updated March 5, 2026
