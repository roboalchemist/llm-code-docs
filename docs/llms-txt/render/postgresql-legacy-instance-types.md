# Source: https://render.com/docs/postgresql-legacy-instance-types.md

# Render Postgres Legacy Instance Types

In October 2024, Render introduced [flexible plans](postgresql-refresh) for Render Postgres. These plans enable you to set your database's storage and compute separately. Storage for a database on a flexible plan is billed at a fixed rate per GB, separate from compute.

Databases created _before_ this change use *legacy instance types* that determine both storage _and_ compute, billed together.

If you have a database on a legacy instance type, you can optionally move it to a flexible plan by [changing its instance type](postgresql-creating-connecting#changing-your-instance-type) in the Render Dashboard. You cannot move _back_ to a legacy instance type.

## Specs

> *These specs are provided as reference for existing databases on a legacy instance type.*
>
> Legacy instance types are not available for new databases.

| Legacy Instance Type | Compute | Storage | Max Connections | Price |
| --- | --- | --- | --- | --- |
| *Starter* | 256 MB RAM 0.1 CPU | 1 GB | 97 | $7/month |
| *Standard* | 1 GB RAM 1 CPU | 16 GB | 97 | $20/month |
| *Pro* | 4 GB RAM 2 CPU | 96 GB | 97 | $95/month |
| *Pro Plus* | 8 GB RAM 4 CPU | 256 GB | 197 | $185/month |
