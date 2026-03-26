# Source: https://docs.infrahub.app/infrahubctl/infrahubctl-protocols.md

# `infrahubctl protocols`

Export Python protocols corresponding to a schema.

**Usage**:

```
$ infrahubctl protocols [OPTIONS]
```

**Options**:

* `--schemas PATH`: List of schemas or directory to load.
* `--branch TEXT`: Branch of schema to export Python protocols for.
* `--sync / --no-sync`: Generate for sync or async. \[default: no-sync]
* `--config-file TEXT`: \[env var: INFRAHUBCTL\_CONFIG; default: infrahubctl.toml]
* `--out TEXT`: Path to a file to save the result. \[default: schema\_protocols.py]
* `--install-completion`: Install completion for the current shell.
* `--show-completion`: Show completion for the current shell, to copy it or customize the installation.
* `--help`: Show this message and exit.
