# Source: https://docs.kubearmor.io/kubearmor/quick-links/kubearmor_overview.md

# Wiki

KubeArmor is a **runtime security enforcement system** for containers and nodes.\
It uses *security policies* (defined as Kubernetes Custom Resources like KSP, HSP, and CSP)\
to define allowed, audited, or blocked actions for workloads.\
The system *monitors system activity* using kernel technologies such as eBPF\
and enforces the defined policies by integrating with the underlying operating system's\
security modules like AppArmor, SELinux, or BPF-LSM, sending security alerts\
and telemetry through a log feeder.

## Visual Overview

![](https://900196120-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MPsOItOtXvqxa1thD0e%2Fuploads%2Fgit-blob-d3c7f60f7d3b258146ec63fa8005901c68ba00ab%2Fkubearmor_overview.png?alt=media)
