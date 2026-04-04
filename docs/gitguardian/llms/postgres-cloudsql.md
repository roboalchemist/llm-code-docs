# Source: https://docs.gitguardian.com/self-hosting/installation/databases/postgres-cloudsql.md

# Cloud SQL: PostgreSQL on GCP

> Configure Google Cloud SQL as the PostgreSQL database for GitGuardian self-hosted.

## Introduction

To deploy the GitGuardian app, a PostgreSQL instance is required. This page is
dedicated to helping you set up a PostgreSQL on GCP using Cloud SQL.

## High-Availability

GCP handles failover and redirects the traffic by itself. As long as your
Cloud SQL is set up to be highly available, upgrades and single-node issues
will not cause an outage.

## Installation

### From the Google Cloud Console

To create a PostgreSQL from the Google Cloud Console, we recommend following the
[official documentation](https://cloud.google.com/sql/docs/postgres/create-instance).

To customize the database name, please follow
[Create and manage databases](https://cloud.google.com/sql/docs/postgres/create-manage-databases).

To customize the user used to access the database, please follow
[Create and manage users](https://cloud.google.com/sql/docs/postgres/create-manage-users).

You need to ensure that the Availability mode is set to `Multiple zones (Highly
available)`.

### Using Terraform

To create a PostgreSQL instance using TF, you need the following resources:

- [google_sql_database_instance](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database_instance)
- (Optional) [google_sql_database](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_database)
- (Optional) [google_sql_user](https://registry.terraform.io/providers/hashicorp/google/latest/docs/resources/sql_user)

In addition to the fields required by Terraform, we require the following fields
to be set on the `google_sql_database_instance`:

- `availability_type="REGIONAL"`: the availability type of the Cloud SQL
  instance, high availability (REGIONAL) or single zone (ZONAL).
