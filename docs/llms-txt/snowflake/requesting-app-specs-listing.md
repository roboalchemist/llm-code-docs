# Source: https://docs.snowflake.com/en/developer-guide/native-apps/requesting-app-specs-listing.md

# Request data sharing with app specifications

This topic describes how to configure the specifications of a Snowflake Native App
to request permission to share data with providers or third parties through
listings. This enables use cases such as compliance reporting, telemetry
sharing, and data preprocessing.

## Share data from an app with providers or third parties

Some Snowflake Native Apps need to share data back with the provider or with third-party Snowflake accounts for
various business purposes. Common use cases include the following:

* **Compliance reporting:** Sharing audit logs or compliance data with regulatory accounts
* **Telemetry and analytics:** Sending usage metrics back to the provider for product improvement
* **Data preprocessing:** Sharing transformed data with partner accounts
* **Support and troubleshooting:** Providing diagnostic data to support teams

To enable data sharing from an app, the app needs to provide both shares and
listings. A share contains the database objects to be shared, and a listing
provides the mechanism to share data across accounts and regions.

For more information about data shares, see [About Secure Data Sharing](../../user-guide/data-sharing-intro.md).

To configure an app to share data using listings, follow these steps:

1. Use [automated granting of privileges](requesting-auto-privs.md) to request privileges from
   the consumer to create shares and listings.
2. Create a share and grant database objects to it.
3. Create an external listing attached to the share.
4. To request permission from the consumer to share data with specific target
   accounts, use [application specifications](requesting-app-specs.md).

> **Note:**
>
> Unlike other app specification types, each LISTING specification is associated with exactly one
> listing object. An app cannot create multiple app specifications for the same listing.

## App specification workflow for sharing data

Configuring an app to share data by using listings follows this general workflow:

1. Providers configure [automated granting of privileges](requesting-auto-privs.md) for the app.
   This grants the app privileges to create shares and listings.

   > > **Note:**
   > >
   > > App specifications require `manifest_version: 2` to be set in the manifest file.
2. Providers add the
   CREATE SHARE and CREATE LISTING privileges to the
   manifest file.
3. Providers add SQL statements to the setup script to create the following objects as required:

   * [Share](../../sql-reference/sql/create-share.md)
   * [External listing](../../sql-reference/sql/create-listing.md)
   * [App specification](../../sql-reference/sql/alter-application-set-app-spec.md)

   The setup script creates the share and listing when the app is installed or
   upgraded. The app specification can be created during setup or at runtime
   through a stored procedure.
4. When configuring the app, consumers review and approve the target accounts
   and auto-fulfillment settings on the listing.
   Auto-fulfillment settings are only applicable for cross-region sharing.
   For more information on how consumers view and approve app specifications, see [Approve app specifications](ui-consumer-app-spec.md).

## App specification definition for sharing data

For an app specification of type LISTING, the app specification definition contains the following entries:

* `TARGET_ACCOUNTS`: A comma-separated list of target accounts to share
  data with, enclosed in single quotes. Each account must be specified in the
  format `OrgName.AccountName`; for example:
  `'ProviderOrg.ProviderAccount,PartnerOrg.PartnerAccount'`.
* `LISTING`: The identifier of the listing object created by the app.
* `AUTO_FULFILLMENT_REFRESH_SCHEDULE`: Optional. The refresh schedule for cross-region data
  sharing. Can be specified as `<num> MINUTE` or `USING CRON <expression>`.

> **Note:**
>
> The listing name in the app specification must match an existing listing created by the app.
> After this is set, the listing name cannot be changed.

## Set the version of the manifest file

To enable automated granting of privileges for an app, set the version at the
beginning of the manifest file, as shown in the following example:

```yaml
manifest_version: 2
```

## Add the CREATE SHARE and CREATE LISTING privileges to the manifest file

The CREATE SHARE and CREATE LISTING privileges allow the app to create shares
and listings during installation or upgrade.

* To configure an app to request
  these privileges, add the following code to the `privileges` section of
  the manifest file:

  > ```yaml
  > manifest_version: 2
  > ...
  > privileges:
  >   - CREATE SHARE:
  >       description: "Create a share for sharing compliance data with provider"
  >   - CREATE LISTING:
  >       description: "Create a listing for cross-region sharing of compliance data"
  > ...
  > ```

If you set the `manifest_version` to 2 in the manifest file, Snowflake automatically grants
the CREATE SHARE and CREATE LISTING privileges to the app during installation or upgrade.

## Create a share and grant objects to it

1. To create a share for data sharing, add the
   [CREATE SHARE](../../sql-reference/sql/create-share.md) command to the setup script, as shown
   in the following example:

```sqlexample
CREATE SHARE IF NOT EXISTS compliance_share;
```

1. Grant the database objects you want to share, as shown in the following
   example:

> ```sqlexample
> GRANT USAGE ON DATABASE app_created_db TO SHARE compliance_share;
> GRANT USAGE ON SCHEMA app_created_db.reporting TO SHARE compliance_share;
> GRANT SELECT ON TABLE app_created_db.reporting.metrics TO SHARE compliance_share;
> ```

> **Note:**
>
> Apps can only share data from the following sources:
>
> * Databases created by the app: The app must be the owner of these databases.
>
> Apps can choose to directly grant privileges on an object to a share or grant a database
> role to share. For more information, see [How to share database objects](../../user-guide/data-sharing-gs.md).
> Apps cannot directly add target accounts to the share. This is controlled through the app specification.

## Create an external listing

1. To create an external listing attached to the share, add the
   [CREATE LISTING](../../sql-reference/sql/create-listing.md) command to the setup script as shown in the following
   example:

   ```sqlexample
   CREATE EXTERNAL LISTING IF NOT EXISTS compliance_listing
   SHARE compliance_share
     AS
     $$
       title: "Compliance Data Share"
       subtitle: "Regulatory compliance reporting data"
       description: "Share compliance and audit data with authorized accounts"
       listing_terms:
         type: "OFFLINE"
     $$
     PUBLISH = FALSE
     REVIEW = FALSE;
   ```

> **Note:**
>
> * Apps can only attach shares, not application packages, to a listing.
> * Apps cannot directly add target accounts or auto-fulfillment configuration
>   to the listing.
> * The listing manifest can only include the following properties: title,
>   subtitle, description, and listing_terms.
> * All new listings must be created in an unpublished state, with both PUBLISH
>   and REVIEW set to FALSE.
> * The listing title and description can be customized based on the consumer
>   info, allowing providers to distinguish data sources.

## Create an app specification for a listing

1. To create an app specification for a listing, follow this example:

   ```sqlexample
   ALTER APPLICATION SET SPECIFICATION shareback_spec
     TYPE = LISTING
     LABEL = 'Compliance Data Sharing'
     DESCRIPTION = 'Share compliance data with provider for regulatory reporting'
     TARGET_ACCOUNTS = 'ProviderOrg.ProviderAccount,AuditorOrg.AuditorAccount'
     LISTING = compliance_listing
     AUTO_FULFILLMENT_REFRESH_SCHEDULE = '720 MINUTE';
   ```

   This command creates an app specification named `shareback_spec` that requests permission to
   share data with the specified target accounts.
2. For cross-region sharing, the `AUTO_FULFILLMENT_REFRESH_SCHEDULE` parameter is required.
   You can set it to one of the following values:

   * `'<num> MINUTE'`: Number of minutes, with a minimum of 10 minutes,
   * and a maximum of 8 days or 11520 minutes (eight days)
   * `'USING CRON <expression> <time_zone>'`: Cron expression with time
     zone

> **Note:**
>
> * The app should only create the app specification after the listing and share objects exist.
> * Each listing can only have one associated app specification.
> * Updating the target accounts creates a new pending request for consumer approval.

## Consumer approval workflow

For more information on how consumers view and approve app specifications, see [Approve app specifications](ui-consumer-app-spec.md).

Consumer approval of a LISTING app specification triggers this workflow:

* Snowflake automatically adds the target accounts to the listing.
* If specified, Snowflake configures the auto-fulfillment refresh schedule.
* The listing becomes visible to the target accounts.
* Data attached to the listing can be queried from the approved accounts.

Consumer rejection of a LISTING app specification triggers this workflow:

* Auto-fulfillment is disabled.
* The listing remains published, allowing the consumer to continue viewing the shared data.
* All target accounts are removed from the listing, with the exception of the current account where the app is installed.
* Auto-fulfillment is disabled.
* Data attached to the listing can no longer be queried by target accounts other than the current account.

## Validating the listing configuration

Apps can validate that the listing has been properly configured after approval by running the following commands:

```sqlexample
-- Check if the app specification is approved:
SHOW APPROVED SPECIFICATIONS IN APPLICATION;

-- Validate the listing configuration:
DESC LISTING compliance_listing;
```

## Best practices for LISTING app specifications

When implementing data sharing through app specification, consider the following
best practices:

* **Share integrity:** Snowflake does not prevent consumers from modifying
  shares created by an application. As a result, the provider is responsible
  for implementing measures to protect the integrity of the underlying shared
  data.
* **Error handling:** Implement proper error handling for cases where the app
  specification is declined or not yet approved.
* **Cross-region considerations:** The app provider is responsible for setting
  refresh schedules that balance data freshness requirements with cost
  considerations. Although Listing Auto Fulfillment costs are billed to the app
  consumer, the provider’s choice of schedule should be cost-aware to minimize
  the unnecessary cost for the app consumer.
* **Compliance:** Document clearly what data you are sharing, and why you are
  sharing it, in the app specification description.

## Using callback functions with LISTING app specifications

Apps can use lifecycle callbacks to respond when consumers approve or decline
listing specifications by adding the following code to the manifest file:

```yaml
lifecycle_callbacks:
  specification_action: callbacks.on_spec_update
```

In the setup script, add the following callback stored procedure:

```sqlexample
CREATE OR REPLACE PROCEDURE callbacks.on_spec_update (
  name STRING,
  status STRING,
  payload STRING)
RETURNS STRING
LANGUAGE SQL
AS
$$
BEGIN
  IF (name = 'SHAREBACK_SPEC' AND status = 'APPROVED') THEN
    -- Start populating shared tables
    CALL populate_compliance_data();
  ELSEIF (name = 'SHAREBACK_SPEC' AND status = 'DECLINED') THEN
    -- Clean up or notify provider
    CALL cleanup_share_data();
  END IF;
  RETURN 'Processed specification update';
END;
$$;
```

The procedure allows the app to react appropriately to consumer decisions about app’s data sharing request.

## Viewing data shared with the provider

Consumers can view the data that has been shared with the provider using either Snowsight
or by querying the data via SQL or the Snowflake CLI.

### To view data shared with the provider using Snowsight

1. Sign in to [Snowsight](../../user-guide/ui-snowsight-gs.md) as a user with the ACCOUNTADMIN role.
2. Navigate to the app’s page.
3. In the application page, select the Permissions tab.
4. Under Data sharing, click Review for a requested data share. The following details are displayed:

   * The name of the data share listing
   * The reason that the app is requesting to share data
   * The accounts that have access to the data share
   * The replication schedule for the data share
5. To view the data shared with the provider, click the Preview data button. The shared data is displayed in
   table format, grouped by schema. Note that the shared data is not editable.
6. To view shared data for other schemas or tables, use the drop-down menus.
7. To view data shared with the provider using a worksheet, click the Open in workspace button.

### To view data shared with the provider using a worksheet

The Uniform Listing Locator (ULL) is a unique identifier for app-created listings that allows consumers to query datasets directly. To find the ULL for a specific listing, check the `uniform_listing_locator` column in the output of the `SHOW LISTINGS` or `DESC LISTINGS` commands.

To view data shared with the provider, reference the objects using the ULL which contains a `NATIVEAPP$` prefix following the listing SQL name:

```sqlexample
SHOW SCHEMAS IN DATABASE NATIVEAPP$MY_LISTING;
SHOW OBJECTS IN SCHEMA NATIVEAPP$MY_LISTING.MY_SCHEMA;
SELECT * FROM NATIVEAPP$MY_LISTING.MY_SCHEMA.MY_TABLE;
```

## Limitations

This section describes limitations when using app specifications.

Auditing
:   Snowflake doesn’t offer built-in auditing for data that an app shares
    back to the provider. If a consumer has compliance or regulatory requirements
    that include an audit trail, they must coordinate directly with the provider
    to implement their own separate monitoring solutions.

Sharing from within the application
:   Snowflake does not recommend data sharing with the provider directly from
    within the application because Listing Auto Fulfillment is not currently
    supported for data shared in this manner.
