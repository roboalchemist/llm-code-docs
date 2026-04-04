# Source: https://docs.infrahub.app/backup.md

# Infrahub Backup

## Overview[​](#overview "Direct link to Overview")

### Why reliable backups matter[​](#why-reliable-backups-matter "Direct link to Why reliable backups matter")

Infrahub stores critical state for your infrastructure in multiple systems: the Neo4j graph database, the PostgreSQL database that powers the task manager, and external artifact storage. If any piece is lost or corrupted, you can end up with drifted configurations, orphaned tasks, or a completely unusable deployment. Regulatory requirements and business continuity plans often demand auditable recovery procedures, so "having some dumps around" is rarely enough—you need consistent, verifiable recovery points.

### How the tool keeps environments recoverable[​](#how-the-tool-keeps-environments-recoverable "Direct link to How the tool keeps environments recoverable")

Infrahub Backup orchestrates backup and restore workflows across deployment targets. It coordinates quiescing and snapshotting services, pulls data out with the right credentials, and packages everything so restores are deterministic. During restore, the tool brings services back in dependency order, reapplies data, and captures logs so you can prove the operation succeeded. Whether you install with Docker Compose, Kubernetes, or a bespoke stack, the CLI abstracts away provider-specific commands and ensures each step runs in a supported sequence.

For Kubernetes deployments, the `infrahub-backup` Helm chart provides a declarative way to manage backups through your existing GitOps pipeline. Enable scheduled backups via CronJob, push artifacts to S3-compatible storage, and perform restores—all without requiring direct kubectl access.

### High availability support[​](#high-availability-support "Direct link to High availability support")

Infrahub Backup supports high availability (HA) deployments on both Kubernetes and Docker Compose:

* **Kubernetes**: HA PostgreSQL is supported via [CloudNativePG](https://cloudnative-pg.io/) only. The tool automatically detects and targets the primary pod during backup and restore — no additional configuration is needed.
* **Docker Compose**: HA setups require stopping the `task-manager` and `task-manager-background-svc` containers before running a restore to prevent database accesses during the process. See [How to restore from backup](/backup/guides/restore-backup.md#docker-high-availability-deployments) for details.

### Community edition support[​](#community-edition-support "Direct link to Community edition support")

The CLI supports Infrahub Community Edition in addition to Enterprise deployments. When you run a backup against Community Edition, the tool stops the Infrahub service while the snapshot is captured, so plan for temporary downtime. Restores must target the same edition that generated the backup—Enterprise backups cannot be applied to Community Edition instances.

### Best practices[​](#best-practices "Direct link to Best practices")

#### Schedule regular backups[​](#schedule-regular-backups "Direct link to Schedule regular backups")

* For Kubernetes deployments, enable the `infrahub-backup` Helm chart with CronJob mode for fully automated, declarative backup scheduling integrated with your GitOps workflow.
* For Docker Compose deployments, automate backups via cron, systemd timers, or CI workflows; daily is a good baseline, with more frequent snapshots for high-change environments.
* Configure S3-compatible storage to automatically push backups off-cluster and apply bucket lifecycle policies for retention management.
* Rotate backup artifacts with a retention policy that matches your recovery point objectives, and replicate critical backups to an off-site location.
* Monitor backup jobs and alert on failures—silent backup gaps often surface only when it is too late.

#### Run regular restore tests[​](#run-regular-restore-tests "Direct link to Run regular restore tests")

* Practice restores in a disposable environment at least monthly to confirm that credentials, network access, and storage quotas are still correct.
* Track the time required to restore and compare it to your recovery time objectives; tune the schedule or resource sizing if the gap widens.
* Document each drill, including any manual steps uncovered, and fold the lessons back into your runbooks so production incidents are predictable.

#### Validate backups after major Infrahub upgrades[​](#validate-backups-after-major-infrahub-upgrades "Direct link to Validate backups after major Infrahub upgrades")

* Every time you perform a major Infrahub version upgrade, capture a fresh backup immediately afterward and run a full restore rehearsal.
* Watch for schema migrations or new services introduced by the upgrade that might require additional credentials, storage buckets, or hooks in your automation.
* Keep the validation artifacts—logs, checksums, and timelines—so you can prove post-upgrade recoverability during audits.

## Getting started[​](#getting-started "Direct link to Getting started")

### Tutorials[​](#tutorials "Direct link to Tutorials")

Learn the fundamentals through hands-on exercises:

* [Getting started with the tool](/backup/tutorials/getting-started.md) - Your first backup and restore operation

### How-to guides[​](#how-to-guides "Direct link to How-to guides")

Accomplish specific tasks:

* [How to install](/backup/guides/install.md) - Install the tool on your system
* [How to backup your Infrahub instance](/backup/guides/backup-instance.md) - Create comprehensive backups
* [How to restore from backup](/backup/guides/restore-backup.md) - Restore your instance from a backup file
* [How to backup Infrahub on Kubernetes](/backup/guides/kubernetes-backup.md) - Backup using the Helm chart
* [How to restore Infrahub on Kubernetes](/backup/guides/kubernetes-restore.md) - Restore using the Helm chart

### Reference[​](#reference "Direct link to Reference")

Technical specifications and command details:

* [CLI command reference](/backup/reference/commands.md) - Complete list of commands and options
* [Configuration reference](/backup/reference/configuration.md) - Environment variables and settings
