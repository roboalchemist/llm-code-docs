# Source: https://planetscale.com/docs/vitess/regions.md

# Regions

## Overview

PlanetScale currently offers database deployment in multiple regions. Select the region closest to your application servers to reduce latency between your database and application. Deploy development branches in the region closest to your own location to reduce latency when working with the branch.

You may also add read-only regions to your production database. See our [Read-only regions documentation](/docs/vitess/scaling/read-only-regions) for more information.

A number of resources exist to help find which region has the lowest latency from your location – such as [CloudPing](https://www.cloudping.co/grid#).

## Available regions

<Note>
  If you don't see your preferred region(s) in the following list, [get in touch](https://planetscale.com/contact) to let us know what region(s) you would like to see added. Also, Enterprise plans can be deployed in any region(s) with three availability zones. See the [Deployment options documentation](/docs/plans/deployment-options#single-tenancy-highlights) for more information.
</Note>

Currently, the following regions are supported, with their respective PlanetScale slugs:

### AWS regions

* AWS ap-northeast-1 (Tokyo) — `ap-northeast`
* AWS ap-south-1 (Mumbai) — `ap-south`
* AWS ap-southeast-1 (Singapore) — `ap-southeast`
* AWS ap-southeast-2 (Sydney) — `aws-ap-southeast-2`
* AWS ca-central-1 (Montreal) — `aws-ca-central-1`
* AWS eu-central-1 (Frankfurt) — `eu-central`
* AWS eu-west-1 (Dublin) — `eu-west`
* AWS eu-west-2 (London) — `aws-eu-west-2`
* AWS sa-east-1 (Sao Paulo) — `aws-sa-east-1`
* AWS us-east-1 (Northern Virginia) — `us-east`
* AWS us-east-2 (Ohio) — `aws-us-east-2`
* AWS us-west-2 (Oregon) — `us-west`

### GCP regions

* GCP us-central1 (Council Bluffs, Iowa) — `gcp-us-central1`
* GCP us-east4 (Ashburn, Virginia) — `gcp-us-east4`
* GCP northamerica-northeast1 (Montréal, Québec, Canada) — `gcp-northamerica-northeast1`
* GCP asia-northeast3 (Seoul, South Korea) — `gcp-asia-northeast3`
* GCP europe-west1 (St Ghislain, Belgium) — `gcp-europe-west1`

## Selecting the database region

PlanetScale allows you to select the region for the [`main` branch](/docs/vitess/schema-changes/branching) of your database during database creation. By default, all database branches created within this database will also be created in this region. Once you select a region for your `main` branch, it cannot be changed.

You can also select the region while creating a database via the CLI by using
the `--region` flag with the region's slug.

<Note>
  The default region for all new databases is AWS us-east-2.
</Note>

Here's an example command for creating a database with a different region:

```shell  theme={null}
pscale database create <DATABASE_NAME> --region us-west
```

## Selecting the branch region

PlanetScale allows you to select a region for development branches during
creation as well. By default, it is set to the same region as its database.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/regions/branch.png?fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=eba391015d86aa737ccb15fb097ec0d2" alt="Select your branch region" data-og-width="2160" width="2160" data-og-height="1684" height="1684" data-path="docs/images/assets/docs/concepts/regions/branch.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/regions/branch.png?w=280&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=59c028aa00a9f300d35182ceace15d39 280w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/regions/branch.png?w=560&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=db5e1cc92f5a5c06dd8aed23fc6cff88 560w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/regions/branch.png?w=840&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=7ccc2c3bf3243ffd13484d8930481061 840w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/regions/branch.png?w=1100&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=e45170bd7de61ec7d76129304ccd081e 1100w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/regions/branch.png?w=1650&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=7bafc6bd620fea40af12569443ba124e 1650w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/regions/branch.png?w=2500&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=2d4e9925be1dea65a798a6f2e6ec573a 2500w" />
</Frame>

<Note>
  Once you select a branch region, it cannot be changed.
</Note>

You can also select the region while creating a branch via the CLI by using the
`--region` flag with the region's slug.

Here's an example command for creating a branch with a different region:

```shell  theme={null}
pscale branch create my-production-database add-tables --region eu-west
```

## Restricting the branch regions

[Organization Administrators](/docs/security/access-control#organization-administrator) can restrict branches to only being created in the same region as the one selected during database creation. To enable this setting, check the *Restrict region* setting in the settings page for the database: `app.planetscale.com/<org>/<database>/settings`.

<Frame>
  <img src="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/regions/restrict-2.png?fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=c11d99455ead1c10cd262e59aa6e4aa2" alt="Restrict your branches to one region" data-og-width="1658" width="1658" data-og-height="984" height="984" data-path="docs/images/assets/docs/concepts/regions/restrict-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/regions/restrict-2.png?w=280&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=44f76e329ef6096932b3931eae61e48d 280w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/regions/restrict-2.png?w=560&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=4da8a68494629cbc66986ac6cfe48f3f 560w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/regions/restrict-2.png?w=840&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=b6e73db587a61dcc55164b76348bec09 840w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/regions/restrict-2.png?w=1100&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=b918bebe8da232b523755ce37a405cde 1100w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/regions/restrict-2.png?w=1650&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=42b156825e80ede9fce3d94e969964c2 1650w, https://mintcdn.com/planetscale-cad1a68a/dVvNdxOWlcjFg3oF/docs/images/assets/docs/concepts/regions/restrict-2.png?w=2500&fit=max&auto=format&n=dVvNdxOWlcjFg3oF&q=85&s=9bf5f9438d21ab6e580d46e9155c5457 2500w" />
</Frame>

## Changing branch and database regions

Once you select a region for a production or development branch, it cannot be changed.

If you do need to move to a different region, we recommend taking the following steps:

<Steps>
  <Step>
    Create a new branch in the new region.
  </Step>

  <Step>
    [Backup and dump](/docs/cli/database) the original branch with:

    ```bash  theme={null}
    pscale database dump <DATABASE_NAME> <BRANCH_NAME>
    ```
  </Step>

  <Step>
    Restore the dump to the new branch with:

    ```bash  theme={null}
    pscale database restore-dump <DATABASE_NAME> <BRANCH_NAME>
    ```
  </Step>

  <Step>
    If this is for a production branch, [promote the new branch](/docs/cli/branch) to production:

    ```bash  theme={null}
    pscale branch promote <DATABASE_NAME> <BRANCH_NAME>
    ```
  </Step>

  <Step>
    Swap out the credentials in your app with the new branch.

    It's important to note that this will require downtime if done on a production branch, as the dump and restore process will take time to complete. To avoid data loss, you can temporarily block writes in your application before doing the dump, and re-enable them after the final credential swap.
  </Step>
</Steps>

## Need help?

Get help from [the PlanetScale Support team](https://support.planetscale.com/), or join our [GitHub discussion board](https://github.com/planetscale/discussion/discussions) to see how others are using PlanetScale.


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://planetscale.com/llms.txt