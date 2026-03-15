# Source: https://docs.jit.io/docs/monorepo-support.md

# Monorepo Support

If you are using a monorepo development strategy in GitHub, an additional configuration file is required to enable dependency scanning.

**To enable monorepo support for GitHub**

1. Create a folder titled `.jit` in the root directory of your monorepo.
2. Create a file within this folder titled `jit-config.yml`.
3. Edit `jit-config.yml` to define folders you want Jit to monitor as separate *projects* that each require independent scans. For information on configuring folder exclusion via `jit-config.yml`, see [Folder Exclusion](https://docs.jit.io/docs/folder-exclusion).

```yaml .jit/jit-config.yml (example)
folders:
  - path: /project1
  - path: /project2
```