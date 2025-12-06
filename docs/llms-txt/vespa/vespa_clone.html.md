# Source: https://docs.vespa.ai/en/reference/clients/vespa-cli/vespa_clone.html.md

# vespa clone

 

## vespa clone

Create files and directory structure from a Vespa sample application

### Synopsis

Create files and directory structure from a Vespa sample application.

Sample applications are downloaded from https://github.com/vespa-engine/sample-apps.

By default, sample applications are cached in the user's cache directory. This directory can be overridden by setting the VESPA\_CLI\_CACHE\_DIR environment variable.

```
vespa clone sample-application-path target-directory [flags]
```

### Examples

```
$ vespa clone album-recommendation my-app
```

### Options

```
-f, --force Ignore cache and force downloading the latest sample application from GitHub
  -h, --help help for clone
  -l, --list List available sample applications
```

### Options inherited from parent commands

```
-a, --application string The application to use (cloud only). Format "tenant.application.instance" - instance is optional
  -C, --cluster string The container cluster to use. This is only required for applications with multiple clusters
  -c, --color string Whether to use colors in output. Must be "auto", "never", or "always" (default "auto")
  -i, --instance string The instance of the application to use (cloud only)
  -q, --quiet Print only errors
  -t, --target string The target platform to use. Must be "local", "cloud", "hosted" or an URL (default "local")
  -z, --zone string The zone to use. This defaults to a dev zone (cloud only)
```

### SEE ALSO

- [vespa](vespa.html) - The command-line tool for Vespa.ai

 Copyright © 2025 - [Cookie Preferences](#)

### On this page:

- [vespa clone](#vespa-clone)
- [Synopsis](#synopsis)
- [Examples](#examples)
- [Options](#options)
- [Options inherited from parent commands](#options-inherited-from-parent-commands)
- [SEE ALSO](#see-also)

