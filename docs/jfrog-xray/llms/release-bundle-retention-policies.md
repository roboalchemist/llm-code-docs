# Source: https://docs.jfrog.com/artifactory/docs/release-bundle-retention-policies.md

# Release Bundle Retention Policies

Policies are defined using the [RETENTION (Release Bundle v1)](/reference/getretentionpolicyconfiguration) REST APIs.

### Automatic Deletion

The retention policy enables you to set auto deletion for Release Bundles (v1 & v2) from Distribution Edges. This policy looks for Release Bundles that meet both of the following criteria and then automatically deletes the Release Bundles when the cleanup process runs. A Release Bundle version is automatically marked and deleted when it meets **both** of the following criteria:

* The maximum number of versions allowed for this Release Bundle has been reached

  **and**
* The Release Bundle version release date is older than the maximum number of days allowed for a released version

If a release bundle does not meet both of these criteria, it will not be deleted automatically (but can be deleted manually).

This feature is configured using the REST APIs - see <Anchor label="Get the Configured Retention Policies List" target="_blank" href="/administration/reference/getConfiguredRetentionPoliciesList">Get the Configured Retention Policies List</Anchor> for details.

<Callout icon="❗️" theme="error">
  **Important**

  Retention policies are designed to work with Postgres and Derby databases. Other databases are not officially supported.
</Callout>

### Reports for Manual Deletion

There are two parameters for the retention policy that are relevant to the manual deletion of a Release Bundle. If a Release Bundle meets one or both the parameters you set, this will make the Release Bundle a candidate for deletion, meaning it will appear in the report:

* Limit the number of versions per Release Bundle - Define the number of versions to keep for the Release Bundle.
* Release Bundle version release date - Define the maximum number of days to keep a released version.

You can define more than one policy; when defining more than one policy, if a Release Bundle meets one or more of the policies it will be marked for retention/deletion.

Note that the retention policy will always be a combination of the two settings (the number of versions and the number of days). If you change only one of these values, the other one will remain the default (the last defined value).