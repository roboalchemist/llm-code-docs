# Source: https://docs.datafold.com/integrations/databases/postgresql.md

# PostgreSQL

<Note>
  **INFO**

  Column-level Lineage is supported for AWS Aurora and RDS Postgres and *requires* Cloudwatch to be configured.
</Note>

**Steps to complete:**

1. [Run SQL script and create schema for Datafold](/integrations/databases/postgresql#run-sql-script-and-create-schema-for-datafold)
2. [Configure your data connection in Datafold](/integrations/databases/postgresql#configure-in-datafold)

## Run SQL script and create schema for Datafold

To connect to Postgres, you need to create a user with read-only access to all tables in all schemas, write access to Datafold-specific schema for temporary tables:

```Bash  theme={null}
/* Datafold utilizes a temporary dataset to materialize scratch work and keep data processing in your warehouse. */

CREATE SCHEMA datafold_tmp;

/* Create a datafold user */

CREATE ROLE datafold WITH LOGIN ENCRYPTED PASSWORD 'SOMESECUREPASSWORD';

/* Give the datafold role write access to the temporary schema */

GRANT ALL ON SCHEMA datafold_tmp TO datafold;

/* Make sure that the postgres user has read permissions on the tables */

GRANT USAGE ON SCHEMA <myschema> TO datafold;
GRANT SELECT ON ALL TABLES IN SCHEMA <myschema> TO datafold;

```

Datafold utilizes a temporary schema, named `datafold_tmp` in the above script, to materialize scratch work and keep data processing in the your warehouse.

## Configure in Datafold

| Field Name                  | Description                                                     |
| --------------------------- | --------------------------------------------------------------- |
| Name                        | A name given to the data connection within Datafold             |
| Host                        | The hostname address for your database; default value 127.0.0.1 |
| Port                        | Postgres connection port; default value is 5432                 |
| User                        | The user role created in our SQL script, named datafold         |
| Password                    | The password created in our SQL script                          |
| Database Name               | The name of the Postgres database you want to connect to        |
| Schema for temporary tables | The schema (datafold\_tmp) created in our SQL script            |

Click **Create**. Your data connection is ready!

***

## Column-level Lineage with Aurora & RDS

This will guide you through setting up Column-level Lineage with AWS Aurora & RDS using CloudWatch.

**Steps to complete:**

1. [Setup Postgres with Permissions](#run-sql-script)
2. [Increase the logging verbosity of Postgres](#increase-logging-verbosity) so Datafold can parse lineage
3. [Set up an account for fetching the logs from CloudWatch.](#connect-datafold-to-cloudwatch)
4. [Configure your data connection in Datafold](#configure-in-datafold)

### Run SQL Script

To connect to Postgres, you need to create a user with read-only access to all tables in all schemas, write access to Datafold-specific schema for temporary tables:

```Bash  theme={null}
/* Datafold utilizes a temporary dataset to materialize scratch work and keep data processing in the your warehouse. */

CREATE SCHEMA datafold_tmp;

/* Create a datafold user */

CREATE ROLE datafold WITH LOGIN ENCRYPTED PASSWORD 'SOMESECUREPASSWORD';

/* Give the datafole role write access to the temporary schema */

GRANT ALL ON SCHEMA datafold_tmp TO datafold;

/* Make sure that the postgres user has read permissions on the tables */

GRANT USAGE ON SCHEMA <myschema> TO datafold;
GRANT SELECT ON ALL TABLES IN SCHEMA <myschema> TO datafold;

```

### Increase logging verbosity

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_dbs-89843982d984ed977c0254adca7a5fa0.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=9714c4922ccea50fd944c73765583084" data-og-width="1277" width="1277" data-og-height="820" height="820" data-path="images/psql_aurora_dbs-89843982d984ed977c0254adca7a5fa0.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_dbs-89843982d984ed977c0254adca7a5fa0.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=5892e6b7f262fd48952d484b7fbeecd0 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_dbs-89843982d984ed977c0254adca7a5fa0.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=5e5f0c59794c822122d6d068027ec288 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_dbs-89843982d984ed977c0254adca7a5fa0.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=186f4698af0774324dd98257b5473cca 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_dbs-89843982d984ed977c0254adca7a5fa0.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=fa0f4b0353acda27d205cf19db73ff58 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_dbs-89843982d984ed977c0254adca7a5fa0.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=6bde0405bbeb3bf9ce3a351c7efdf250 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_dbs-89843982d984ed977c0254adca7a5fa0.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=f448733acfbb18e4b43ccda538d934f8 2500w" />
</Frame>

Then, create a new `Parameter Group`. Database instances run with default parameters that do not include logging verbosity. To turn on the logging verbosity, you'll need to create a new Parameter Group. Hit **Parameter Groups** on the menu and create a new Parameter Group.

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_parameter_group-044563cebd48ae81a9d22ab2319d160e.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=6bffe4b697e92e129c84c504967b3b4e" data-og-width="1277" width="1277" data-og-height="886" height="886" data-path="images/psql_aurora_parameter_group-044563cebd48ae81a9d22ab2319d160e.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_parameter_group-044563cebd48ae81a9d22ab2319d160e.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=2041e8487561dc68a632f4b0e2146a57 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_parameter_group-044563cebd48ae81a9d22ab2319d160e.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=3f4bdd72d5beca4ef1d1ab3786e5238c 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_parameter_group-044563cebd48ae81a9d22ab2319d160e.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=6030776af5fa07f7f9c3c829b03f2504 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_parameter_group-044563cebd48ae81a9d22ab2319d160e.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=9c1abf936a8486048f9df6770bbb33e8 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_parameter_group-044563cebd48ae81a9d22ab2319d160e.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=2b76bb13e41e3036efdff2202abce1de 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_parameter_group-044563cebd48ae81a9d22ab2319d160e.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=eba29682db0813d1cd2fc571d138ba25 2500w" />
</Frame>

Next, select the `aurora-postgresql10` parameter group family. This depends on the cluster that you're running. For Aurora serverless, this is the appropriate family.

Finally, set the `log_statement` enum field to `mod` - meaning that it will log all the DDL statements, plus data-modifying statements. Note: This field isn't set by default.

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_logstatement-6f0ba20fd7217047ae62fd01cbfa50d4.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=b1243c6b87aaa2c4b9efea52f51b8b61" data-og-width="1682" width="1682" data-og-height="927" height="927" data-path="images/psql_aurora_logstatement-6f0ba20fd7217047ae62fd01cbfa50d4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_logstatement-6f0ba20fd7217047ae62fd01cbfa50d4.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=59e3a715d3073f4e86fede0f67b76618 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_logstatement-6f0ba20fd7217047ae62fd01cbfa50d4.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=902351c9a3648501d87d4e5c3b5e8202 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_logstatement-6f0ba20fd7217047ae62fd01cbfa50d4.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=d3fb96d7d514ef4e653ab88fde3bf946 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_logstatement-6f0ba20fd7217047ae62fd01cbfa50d4.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=9767a83de15f37aae0411f5e0d80d7f1 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_logstatement-6f0ba20fd7217047ae62fd01cbfa50d4.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=c6dd5452612e966f6552444b3f965c2d 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_logstatement-6f0ba20fd7217047ae62fd01cbfa50d4.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=9edc31c9df62dc827068629124d59ccd 2500w" />
</Frame>

After saving the parameter group, go back to your database, and select the database cluster parameter group.

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_clustergroup-6a1c25e3eae1563130b7565a5b5f0ba7.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=5fed528e2e74cbc506ca4ddda648eede" data-og-width="1682" width="1682" data-og-height="927" height="927" data-path="images/psql_aurora_clustergroup-6a1c25e3eae1563130b7565a5b5f0ba7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_clustergroup-6a1c25e3eae1563130b7565a5b5f0ba7.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=e0c72e0110c73e39886248a33bc88d8b 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_clustergroup-6a1c25e3eae1563130b7565a5b5f0ba7.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=f9df5cb6534a765cca36ad27a1b5a484 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_clustergroup-6a1c25e3eae1563130b7565a5b5f0ba7.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=cfc93b154ba010abd7b33494ccd60029 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_clustergroup-6a1c25e3eae1563130b7565a5b5f0ba7.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=1533f80eeafef52f89330efe764ed921 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_clustergroup-6a1c25e3eae1563130b7565a5b5f0ba7.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=12f6acc1a4312b193baaf31a1698cee8 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_clustergroup-6a1c25e3eae1563130b7565a5b5f0ba7.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=8a9ee9cb47064620821294b0c82fd031 2500w" />
</Frame>

### Connect Datafold to CloudWatch

Start by creating a new user to isolate the permissions as much as possible. Go to IAM and create a new user.

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_iam_user-0d82fc2408ab78e2bd94b20e0e2d363e.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=aa54c7573e13e8eaff8e277bd549b692" data-og-width="1682" width="1682" data-og-height="927" height="927" data-path="images/psql_aurora_iam_user-0d82fc2408ab78e2bd94b20e0e2d363e.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_iam_user-0d82fc2408ab78e2bd94b20e0e2d363e.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=96e5b50dfd4a19ef3d614ea73a18f33a 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_iam_user-0d82fc2408ab78e2bd94b20e0e2d363e.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=21a72f6e384694ff0720c3e79b8d5a0d 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_iam_user-0d82fc2408ab78e2bd94b20e0e2d363e.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=c4c587d5be8b2798703061b4bd6282fd 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_iam_user-0d82fc2408ab78e2bd94b20e0e2d363e.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=fceab1ef25b9cc390873b16a61b4b335 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_iam_user-0d82fc2408ab78e2bd94b20e0e2d363e.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=3ec007a2e3ea3628f010734dae89ee9c 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_iam_user-0d82fc2408ab78e2bd94b20e0e2d363e.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=eacf5a8a9d312cacbf028d16244c3124 2500w" />
</Frame>

Next, create a new group named `CloudWatchLogsReadOnly` and attach the `CloudWatchLogsReadOnlyAccess` policy to it. Next, select the group.

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_user_permissions-f48596fc79a01aea8d9aadd3688381ce.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=130f10b905ba8f0c7360b671ec6459b1" data-og-width="1682" width="1682" data-og-height="927" height="927" data-path="images/psql_aurora_user_permissions-f48596fc79a01aea8d9aadd3688381ce.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_user_permissions-f48596fc79a01aea8d9aadd3688381ce.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=14889ace18815496827c61737f4502e9 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_user_permissions-f48596fc79a01aea8d9aadd3688381ce.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=004bf17bb2b50ed79e38922b010171fd 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_user_permissions-f48596fc79a01aea8d9aadd3688381ce.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=94a4957af7561fe701efe0b1ca0628cd 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_user_permissions-f48596fc79a01aea8d9aadd3688381ce.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=7765c8d5939dcead840e602494e5ea2e 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_user_permissions-f48596fc79a01aea8d9aadd3688381ce.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=58e3d859eea26a6a22d162c4117476c1 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_user_permissions-f48596fc79a01aea8d9aadd3688381ce.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=06db75d6ad2b1ef631329ac4ebce8eed 2500w" />
</Frame>

When reviewing the user, it should have the freshly created group attached to it.

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_user_review-637256675791599a381ee290bd7e05b7.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=6f96f214f462c92d2304250cad4c11e5" data-og-width="1682" width="1682" data-og-height="927" height="927" data-path="images/psql_aurora_user_review-637256675791599a381ee290bd7e05b7.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_user_review-637256675791599a381ee290bd7e05b7.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=07ee7e456f35447302edcd92861c9175 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_user_review-637256675791599a381ee290bd7e05b7.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=19abeb9bebff8315c7e66b8dedc598f1 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_user_review-637256675791599a381ee290bd7e05b7.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=408286dc865ce8808d5b91cec556a3ea 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_user_review-637256675791599a381ee290bd7e05b7.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=2a056ee5a24578d14afd3fcce43e1f81 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_user_review-637256675791599a381ee290bd7e05b7.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=ab153ddbf6bd25f4e3b06d134247e960 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_user_review-637256675791599a381ee290bd7e05b7.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=adee5a0232d4f6a4c27a41602d6f11b7 2500w" />
</Frame>

After confirming the new user you should be given the `Access Key` and `Secret Key`. Save these two codes securely to finish configurations on Datafold.

The last piece of information Datafold needs is the CloudWatch Log Group. You will find this in CloudWatch under the Log Group section in the sidebar. It will be formatted as `/aws/rds/cluster/<my_cluster_name>/postgresql`.

<Frame>
  <img src="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_log_group-5dd6c4c2728cf4d55352976449d05c12.png?fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=0178488e4be5c0b38a28d569bf0d799f" data-og-width="1682" width="1682" data-og-height="927" height="927" data-path="images/psql_aurora_log_group-5dd6c4c2728cf4d55352976449d05c12.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_log_group-5dd6c4c2728cf4d55352976449d05c12.png?w=280&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=7ef3458807c7936a1cbbdf293c4ce462 280w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_log_group-5dd6c4c2728cf4d55352976449d05c12.png?w=560&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=d82747cd6550946fcb86d0f0f03373cc 560w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_log_group-5dd6c4c2728cf4d55352976449d05c12.png?w=840&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=f60eafe13510cae11665893aca6b32a8 840w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_log_group-5dd6c4c2728cf4d55352976449d05c12.png?w=1100&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=219611a2a8db03a439b44921dc5e6b61 1100w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_log_group-5dd6c4c2728cf4d55352976449d05c12.png?w=1650&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=17536d004b1d58015cb6a7c9899967fd 1650w, https://mintcdn.com/datafold/9DgdnO4sVNte36u-/images/psql_aurora_log_group-5dd6c4c2728cf4d55352976449d05c12.png?w=2500&fit=max&auto=format&n=9DgdnO4sVNte36u-&q=85&s=54ef54cd781e6b548f4e2f4026065b4c 2500w" />
</Frame>

### Configure in Datafold

| Field Name                    | Description                                                                                                                             |
| ----------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- |
| Name                          | A name given to the data connection within Datafold                                                                                     |
| Host                          | The hostname address for your database; default value 127.0.0.1                                                                         |
| Port                          | Postgres connection port; default value is 5432                                                                                         |
| User                          | The user role created in the SQL script; datafold                                                                                       |
| Password                      | The password created in the SQL permissions script                                                                                      |
| Database Name                 | The name of the Postgres database you want to connect to                                                                                |
| AWS Access Key                | The Access Key provided in the [Connect Datafold to CloudWatch](/integrations/databases/postgresql#connect-datafold-to-cloudwatch) step |
| AWS Secret                    | The Secret Key provided in the [Connect Datafold to CloudWatch](/integrations/databases/postgresql#connect-datafold-to-cloudwatch) step |
| Cloudwatch Postgres Log Group | The path of the Log Group; formatted as /aws/rds/cluster/\<my\_cluster\_name>/postgresql                                                |
| Schema for temporary tables   | The schema created in the SQL setup script; datafold\_tmp                                                                               |

Click **Create**. Your data connection is ready!
