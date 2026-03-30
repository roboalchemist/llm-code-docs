# Source: https://docs.snowflake.com/en/developer-guide/native-apps/security-run-scan.md

# Run the automated security scan

This topic describes how to initiate the automated security scan and view the current status.

## Security scan workflow

The following diagram shows how the security scan fits within the workflow for developing and
publishing a Snowflake Native App:

This workflow includes the following steps:

1. Create an application package.
2. Update the application code and related files.

   Before running the automated security scan, ensure that the app conforms to the security
   requirements and best practices outline in [Security requirements and best practices for a Snowflake Native App](security-app-requirements.md). If the app is
   a Snowflake Native App with Snowpark Container Services, review the additional security requirements outlined in [Secure a Snowflake Native App with Snowpark Container Services](security-na-spcs.md).
3. Add a version or patch to the application package.
4. Run the automated security scan. The automated security scan starts when the provider does one of the following:

   * Adds a new version or patch to the application package when the DISTRIBUTION property is set to
     `EXTERNAL`. The new version is scanned automatically.
   * Sets the DISTRIBUTION property to “EXTERNAL” on an application package that already has a version
     defined. The ten most recent versions of the application package are scanned automatically. All
     patches for these version are also scanned.
5. Await the results of the scan.

   If the scan is approved, the provider can continue with the process of publishing the app.

   If the scan is rejected, the provider must update the application code based on the results of the scan.
   Alternatively, the provider can appeal the rejection.
6. Create or modify the release directive for the app.
7. Create a listing for the app.
8. Submit the listing to Snowflake for approval.

   If the listing is approved, the provider can publish the listing on the Snowflake Marketplace.

   If the listing is rejected, the provider must update the listing and resubmit for approval.
9. Publish the listing.

## Set the DISTRIBUTION property on an application package

The DISTRIBUTION property of an application package indicates the type of listing a provider can
create when using the application package as the data product of a listing. This property has the
following values:

* `INTERNAL` indicates that a provider can only create a private listing within the same organization
  where the application package was created. The automated security scan is not performed when
  the DISTRIBUTION property is set to `INTERNAL`.
* `EXTERNAL` indicates that a provider can create listings outside the same organization where the
  application package was created. This includes the following:

  * Private listings outside the provider’s organization.
  * Public listings.
  * Marketplace listings.

A provider can set the DISTRIBUTION property when creating the application package or afterwards.

To set the DISTRIBUTION property when creating an application package, run the
[CREATE APPLICATION PACKAGE](../../sql-reference/sql/create-application-package.md) as shown in the following example:

```sqlexample
CREATE APPLICATION PACKAGE hello_snowflake_package
  DISTRIBUTION = EXTERNAL;
```

When a provider sets the DISTRIBUTION property when creating the application package, any versions or
patches added to the application package later are scanned immediately.

To set the DISTRIBUTION property for an existing application package run the
[ALTER APPLICATION PACKAGE](../../sql-reference/sql/alter-application-package.md) as shown in the following example:

```sqlexample
ALTER APPLICATION PACKAGE hello_snowflake_package
  SET DISTRIBUTION = EXTERNAL;
```

When a provider sets the DISTRIBUTION property for an existing application package, the automated
security scan is automatically run on the ten most recent versions of the app. All patches for these
versions are also scanned.

## View the status of the security scan

After initiating the security scan for a version or patch, providers can view that status
in the application package. The possible statuses are:

* `NOT_REVIEWED` indicates that the automated security scan has not been performed on this application
  package.
* `IN_PROGRESS` indicates that the automated security scan is currently in progress.
* `APPROVED` indicates that the automated security scan completed and the application package
  has been approved. The provider can set the release directive for the application package.
* `REJECTED` indicates that the automated security scan completed, but the application package
  was not approved.

> **Note:**
>
> When an automated security scan fails, the Snowflake manually reviews the application package.
> After the manual review is complete, the status is updated to `APPROVED` or `REJECTED`.

### View the status of the security scan using SQL

To view the status of the security scan, run the [SHOW VERSIONS IN APPLICATION PACKAGE](../../sql-reference/sql/show-versions.md)
command as shown in the following example:

```sqlexample
SHOW VERSIONS IN APPLICATION PACKAGE hello_snowflake_package;
```

The `review_status` column displays the status of the automated review scan.

### View the status of the security scan using Snowsight

1. Sign in to [Snowsight](../../user-guide/ui-snowsight-gs.md).
2. In the navigation menu, select Projects » App packages.
3. Select the application package whose status you want to view.

   The Security Scan Status column shows the current status of the review of
   each version and patch associated with the application package.
4. If the status is Rejected, select the app package to see the reason for
   the rejection.

## Appealing a rejection

If critical vulnerabilities or policy violations are found after Snowflake performs a manual review,
the application package is rejected and the reason for the rejection can be
reviewed in the application package.

A provider can appeal the rejection by opening a severity 4 support ticket. When appealing a CVE-based
rejection, providers must submit detailed documentation explaining the following:

* Why the CVE is not exploitable in the application
* Reachability analysis report, if available
* A plan for updating to the fixed version
* If there are no plans for an update, a detailed explanation of why a vulnerable version cannot be updated

The Snowflake Security team reviews and issues decisions for all appeals.

For additional information on the appeal process, see [Appeal a failed security review](security-appeal.md).

## Ongoing security monitoring and remediation

After an app is approved and published on the Snowflake Marketplace, it undergoes continuous security
monitoring to ensure ongoing safety and compliance. This includes:

* Periodic image security analysis to detect new vulnerabilities or policy violations.
* If issues are discovered, the provider is notified and given 30 business days to patch the app or
  can request an exception within 15 days.
