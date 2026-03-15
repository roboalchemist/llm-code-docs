# Source: https://docs.jit.io/docs/folder-exclusion.md

# Files and Folder Exclusions

### GitHub file and folder exclusion

The `jit-config.yml` configuration file is used to enable exclusion of specific paths from Jit monitoring. This file is automatically created in the `.jit` directory of the repository selected for [GitHub integration](https://docs.jit.io/docs/integrating-with-github). Paths defined in this file are excluded from all repositories in your organization. You can define path exclusions unique to a specific repository by adding a `.jit/jit-config.yml` to the selected repository.

```yaml .jit/jit-config.yml (organization-level example)
folders:
  - path: /abc
    exclude:
      - /inner
      - /inner/*
  - path: /foo
    exclude:
      - /example1-dir
```

> 🚧
>
> The code blocks below are for illustrative purposes and are not valid `jit-config.yml` files.

```yaml Combining org-level and repo-level exclusion lists
# Combining the mapping in this organization-level jit-config.yml file...
folders:
  - path: /abc
    exclude:
      - /inner
      - /inner/*
  - path: /foo
    exclude:
      - /example1-dir
 
#... With the mapping in this repository-level jit-config.yml file...
folders:
  - path: /bar
    exclude:
      - /dir
  - path: /foo
    exclude:
      - /example2-dir
      
#... Results in exclusion behavior within the repository identical to this mapping...
folders:
  - path: /abc
    exclude:
      - /inner
      - /inner/*
  - path: /bar
    exclude:
      - /dir
  - path: /foo
    exclude:
      - /example2-dir
```
```yaml Additional exclusion options
folders:
  # Excluding a directory and inner files
  - path: /abc
    exclude:
      - /inner
      - /inner/*

  # Excluding a single file
  - path: /def
    exclude:
      - /excluded.txt

  # Excluding a directory only
  - path: /ghi
    exclude: [ /inner/ ]

  # Excluding a directory only ending without a slash
  - path: /jkl
    exclude:
      - /inner

  # Excluding inner files only
  - path: /mno
    exclude:
      - /inner/*

  # Exclude patterns doesn't have to start with a slash
  - path: /pqr
    exclude:
      - inner/*

  # Exclude everything starting with a ./
  - path: /stu
    exclude:
      - ./*

  # Exclude everything with '*'
  - path: /vwx
    exclude:
      - '*'
```

**To configure folder exclusion at the organization level—**

1. Locate `jit-config.yml` in the `.jit` directory of the repository selected for [GitHub integration](https://docs.jit.io/docs/integrating-with-github).
2. Edit `jit-config.yml` to define paths to exclude. Glob patterns are supported.

**To configure folder exclusion for a specific repository—**

1. Create a folder titled `.jit` in the root directory of any repo containing paths you want to exclude from Jit monitoring
2. Create a file within this directory titled `jit-config.yml`.
3. Edit `jit-config.yml` to define paths to exclude. Glob patterns are supported.

> 📘 Monorepo support
>
> If you are already using a `jit-config.yml`file to enable dependency scanning within a monorepo, use this existing `jit-config.yml`file to define paths to exclude.

### Other SCM file and folder exclusion

Use Jit's 'Update configuration file' API endpoint to enable the exclusion of specific paths from Jit monitoring. Paths defined in this file are excluded from all repositories in your organization.

For more information, please see [API: Update configuration file.](https://docs.jit.io/reference/tenant-7ddaef1e-4ba5-4c0d-964b-d62a699c9e2f)