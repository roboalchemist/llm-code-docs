# Source: https://www.aptible.com/docs/core-concepts/scaling/database-scaling.md

# Database Scaling

> Learn about scaling Databases CPU, RAM, IOPS and throughput

# Overview

Scaling your Databases on Aptible is straightforward and efficient. You can scale Database from the Dashboard, CLI, or Terraform to adjust your database resources like CPU, RAM, IOPS, and throughput, and Aptible ensures appropriate hardware is provisioned. All Database scaling operations are performed with **minimal downtime**, typically less than one minute.

## Vertical Scaling

Scale Databases vertically by changing the size of Containers, i.e., changing the [Memory Limits](/core-concepts/scaling/memory-limits) and [CPU Limits](/core-concepts/scaling/container-profiles). The available sizes are determined by the [Container Profile.](/core-concepts/scaling/container-profiles)

## Horizontal Scaling

While Databases cannot be scaled horizontally by adding more Containers, horizontal scaling can be achieved by setting up database replication and clustering. Refer to [Database Replication and Clustering](/core-concepts/managed-databases/managing-databases/replication-clustering) for more information.

## Disk Scaling

Database Disks can be scaled up to 16384GB. Database Disks can be resized at most once a day and can only be resized up (i.e., you cannot shrink your Database Disk).

If you do need to scale Database Disk down, you can either dump and restore to a smaller Database or create a replica and failover. Refer to our [Supported Databases](/core-concepts/managed-databases/supported-databases/overview) documentation to see if replication and failover is supported for your Database type.

Related: [Why Can’t I Shrink My Database Disk?](https://support.aptible.com/articles/8772915319-can-i-reduce-the-disk-size-allocated-to-a-database-instance)

## IOPS Scaling

Database IOPS can be scaled with no downtime. Database IOPS can only be scaled using the [`aptible db:modify`](/reference/aptible-cli/cli-commands/cli-db-modify) command. Refer to [Database Performance Tuning](/core-concepts/managed-databases/managing-databases/database-tuning#database-iops-performance) for more information.

## Throughput performance

All new Databases are provisioned with GP3 volume, with a default throughput performance of 125MiB/s. This can be scaled up to 1,000MiB/s by contacting [Aptible Support](/how-to-guides/troubleshooting/aptible-support). Refer to [Database Performance Tuning](/core-concepts/managed-databases/managing-databases/database-tuning#database-throughput-performance) for more information.

# FAQ

<AccordionGroup>
  <Accordion title="Is there downtime from scaling a Database?">
    Yes, all Database scaling operations are performed with **minimal downtime**, typically less than one minute.
  </Accordion>

  <Accordion title="How do I scale a Database">
    See related guide:

    <Card title="How to scale Databases" icon="book-open-reader" iconType="duotone" href="https://www.aptible.com/docs/scale-databases" />
  </Accordion>
</AccordionGroup>
