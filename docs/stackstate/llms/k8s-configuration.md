# Source: https://archivedocs.stackstate.com/guided-troubleshooting/k8s-configuration.md

# YAML Configuration

If a pod is experiencing issues such as crashes, failures to start or misconfigurations, inspecting the YAML configuration can help you identify the root cause. You can see YAML configuration by clicking on **Show configuration** button.

![](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-0f88977a9dc6201d750eaeb3ecd06aaa4c0cd8ce%2Fk8s-configuration.png?alt=media)

This gives the same output as `kubectl describe` command applied for service, pod or other resource.

![](https://2245176135-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNEvjJkYDpdslyPRQlRIf%2Fuploads%2Fgit-blob-9776d2eb1f38417f64c192e568014000f9d79641%2Fk8s-configuration-opened.png?alt=media)
