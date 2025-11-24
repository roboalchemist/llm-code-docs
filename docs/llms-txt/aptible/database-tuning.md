# Source: https://www.aptible.com/docs/core-concepts/managed-databases/managing-databases/database-tuning.md

# Database Performance Tuning

# Database IOPS Performance

Database IOPS (Input/Output Operations Per Second) refer to the number of read/write [Operations](/core-concepts/architecture/operations) that a Database can perform within a second.

**Baseline IOPS:**

* **gp3 Volume:** Aptible provisions new Databases with AWS gp3 volumes, which provide a minimum baseline IOPS performance of 3,000 IOPS no matter how small your volume is. The maximum IOPS is 16,000, but you must meet a minimum ratio of 1 GB disk size per 500 IOPS. For example, to reach 16,000 IOPS, you must have at least a 32 GB or larger disk.
* **gp2 Volume:** Older Databases may be using gp2 volumes, which provide a baseline IOPS performance of 3 IOPS / GB of disk, with a minimum allocation of 100 IOPS. In addition to the baseline performance, gp2 volumes also offer burst IOPS capacity up to 3,000 IOPS, which lets you exceed the baseline performance for a period of time. You should not rely on the volume's burst capacity during normal activity. Doing so will likely cause your performance to drop once you exhaust the volume's burst capacity, which will likely cause your app to go down.

Disk IO performance can be determined by viewing [Dashboard Metrics](/core-concepts/observability/metrics/overview#dashboard-metrics) or monitoring [Metric Drains](/core-concepts/observability/metrics/metrics-drains/overview) (`disk_read_iops` and `disk_write_iops` metrics).

IOPS can also be scaled on-demand to meet performance needs. For more information on scaling IOPS, refer to [Database Scaling.](/core-concepts/scaling/database-scaling#iops-scaling)

# Database Throughput Performance

Database throughput performance refers to the amount of data that a database system can process in a given time period.

**Baseline Throughput:**

* **gp3 Volume:** gp3 volumes have a default throughput performance of 125MiB/s, and can be scaled up to 1,000MiB/s by contacting [Aptible Support](/how-to-guides/troubleshooting/aptible-support).
* **gp2 Volume:** gp2 volumes have a maximum throughput performance of between 128MiB/s and 250MiB/s, depending on volume size. Volumes smaller or equal to 170 GB in size are allocated 128MiB/s of throughput. The throughput scales up until you reach a volume size of 334 GB. At 334 GB in size or larger, you have the full 250MiB/s performance possible with a GP2 volume. If you need more throughput, you may upgrade to a GP3 volume at any time by using the [`aptible db:modify`](/reference/aptible-cli/cli-commands/cli-db-modify) command.

Database Throughput can be monitored within [Metric Drains](/core-concepts/observability/metrics/metrics-drains/overview) (`disk_read_kbps` and `disk_write_kbps` metrics).

Database Throughput can be scaled by the Aptible Support Team only. For more information on scaling Throughput, refer to [Database Scaling.](/core-concepts/scaling/database-scaling#throughput-performance)
