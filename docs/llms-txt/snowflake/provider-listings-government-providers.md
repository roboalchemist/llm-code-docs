# Source: https://docs.snowflake.com/en/collaboration/provider-listings-government-providers.md

# Government providers

If you’re a government provider, this section provides information on how you can prepare to provide listings.

## Prepare to provide listings from accounts in U.S. government regions

If your account is in a [U.S. government region](../user-guide/intro-regions.md) and you want to install data products offered privately or on the Snowflake Marketplace, or
offer listings either privately or on the Snowflake Marketplace, you must review and acknowledge the following cross-region disclaimer for your
organization.

> **Important:**
>
> To get data products and share listings with Snowflake customers outside your region, Snowflake shares organization and account metadata
> and usage analytics with the customers you collaborate with outside of your region.
>
> Compliance standards, such as [FedRAMP](../user-guide/cert-fedramp.md), and support for different regulated workloads, such as [ITAR](../user-guide/cert-itar.md), might be different or unavailable
> outside of your U.S. Government Region. Consider your compliance requirements before choosing to move or share data between Snowflake regions.

> **Note:**
>
> You must use the ORGADMIN role to accept the terms. You only need to accept terms once for your Snowflake account. If you do not have
> the ORGADMIN role, see [Enabling the ORGADMIN role in an account](https:/docs.snowflake.com/en/user-guide/organization-administrators).

1. Sign in to [Snowsight](../user-guide/ui-snowsight-gs.md).
2. In the navigation menu, select Admin » Terms.
3. In the Snowflake Marketplace section, for Sharing & Collaboration, select Review & Enable.
4. Review the cross-region disclaimer and select Acknowledge & Continue.
5. Select Done.

> **Note:**
>
> * Providers can enable [Egress Cost Optimizer (ECO)](provider-listings-auto-fulfillment-eco.md) in a primary account in any commercial region and create listings targeted to any other region, including government regions.
> * By default, ECO is unavailable to customers on a government cloud. If you’re a Gov customer, you can reach out to your Snowflake account executive for more information about ECO enablement.

You must use the ORGADMIN role and you only need to complete this step once for your organization:

1. Sign in to [Snowsight](../user-guide/ui-snowsight-gs.md).
2. In the navigation menu, select Admin » Terms.
3. In the Snowflake Marketplace section, for Sharing & Collaboration, select Review & Enable.
4. Review the cross-region disclaimer and select Acknowledge & Continue.
5. Select Done.

> **Note:**
>
> If you see an error, your user profile might be missing some contact information. If you have an administrator role, see
> [Add user details to your user profile](../user-guide/ui-snowsight-profile.md) to update your profile using Snowsight. Otherwise, contact an
> account administrator to update your user details.

### Stop sharing and collaboration from an account in a US government region

If you no longer want to offer or access listings from your account in a US government region, do the following:

1. [Delete all of your listings](provider-listings-removing.md) shared from your account, consistent with the applicable
   requirements in the Provider and Consumer Terms.
2. Stop consuming listings by dropping the databases imported when you
   [accessed listings](consumer-listings-access.md).
3. [Contact Snowflake Support](../user-guide/contacting-support.md) to have data sharing and collaboration disabled for your organization.

### Limitations for providing listings from accounts in U.S. government regions

If you provide listings from an account in a U.S. government region, the following limitations apply:

* You cannot offer paid or personalized listings.
* You must use Cross-Cloud Auto-Fulfillment, and your data product can only contain
  [objects supported for auto-fulfillment](provider-understand-auto-fulfillment-objects.md).

Additional considerations apply to providers in non-US-government regions who want to offer listings to accounts in US government regions.
See [Considerations for sharing listings to accounts in US government regions](provider-listings-creating-publishing.md).

## Prepare to provide listings from accounts in the Kingdom of Saudi Arabia (KSA) region

If your account is in a [Europe and Middle East region](../user-guide/intro-regions.md), specifically Dammam (me-central2), and you want to install data products offered privately or on the Snowflake Marketplace, or
offer listings either privately or on the Snowflake Marketplace, you must review and acknowledge the following cross-region disclaimer for your
organization.

> **Important:**
>
> To get data products and share listings with Snowflake customers outside your region, Snowflake shares organization and account metadata
> and usage analytics with the customers you collaborate with outside of your region. Compliance standards and support for different
> regulated workloads might be different or unavailable outside of your region.
> Consider your compliance requirements before choosing to move or share data between Snowflake regions.

> **Note:**
>
> You must use the ORGADMIN role to accept the terms. You only need to accept terms once for your Snowflake account. If you do not have
> the ORGADMIN role, see [Enabling the ORGADMIN role in an account](https:/docs.snowflake.com/en/user-guide/organization-administrators).

1. Sign in to [Snowsight](../user-guide/ui-snowsight-gs.md).
2. In the navigation menu, select Admin » Terms.
3. In the Snowflake Marketplace section, for Sharing & Collaboration, select Review & Enable.
4. Review the cross-region disclaimer and select Acknowledge & Continue.
5. Select Done.

> **Note:**
>
> If you see an error, your user profile might be missing some contact information. If you have an administrator role, see
> [Add user details to your user profile](../user-guide/ui-snowsight-profile.md) to update your profile using Snowsight. Otherwise, contact an
> account administrator to update your user details.

### Stop sharing and collaboration from an account in a KSA region

If you no longer want to offer or access listings from your account in a KSA region, do the following:

1. [Delete all of your listings](provider-listings-removing.md) shared from your account, consistent with the applicable
   requirements in the Provider and Consumer Terms.
2. Stop consuming listings by dropping the databases imported when you
   [accessed listings](consumer-listings-access.md).
3. [Contact Snowflake Support](../user-guide/contacting-support.md) to have data sharing and collaboration disabled for your organization.
