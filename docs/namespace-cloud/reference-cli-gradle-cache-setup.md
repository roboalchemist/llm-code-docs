<!-- Source: https://namespace.so/docs/reference/cli/gradle-cache-setup -->

# nsc cache gradle setup

Set up a remote Gradle build cache.

Namespace provides high-performance Gradle build caching with very low network latency between runners and the cache storage.
This allows your Gradle workflows to reuse build outputs across runs, significantly reducing build times.
`cache gradle setup` sets up a remote Gradle build cache and generates an init script to use it.

[Learn more about Gradle caching →](/docs/integrations/gradle)

## Usage

```
nsc cache gradle setup [--init-gradle <target init script path>]
```

### Example

The following example creates a remote Gradle build cache and uses it during a build invocation.

```
$ nsc cache gradle setup --init-gradle=/tmp/init.gradle
```

Next, let's use the generated configuration

```
$ gradle --init-script=/tmp/init.gradle build
```

## Options

### --init-gradle

If specified, write the init script to this path.

### --user

If specified, write the configuration to the Gradle user home directory.

### --token

Path to a token file for long-term access (e.g. from local workstations). If not specified, short-term credentials are generated.

Last updated March 5, 2026
