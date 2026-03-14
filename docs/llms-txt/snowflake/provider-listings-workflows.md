# Source: https://docs.snowflake.com/en/collaboration/provider-listings-workflows.md

# Provider workflows

This section describes the workflows that providers follow to become a Snowflake Marketplace provider and to offer data/share listings and Snowflake Native App listings on Snowflake Marketplace.

## Provider approval process

The image below shows the approval process for becoming a Snowflake Marketplace provider. The steps below the image describe the actions that providers take when following the workflow.

1. If you don’t have one already, [create a Snowflake account](https://signup.snowflake.com).
2. Configure your provider profile.

   1. Sign in to [Snowsight](../user-guide/ui-snowsight-gs.md).
   2. In the navigation menu, select Marketplace » Provider Studio.
   3. Select the Profiles tab.
   4. Select + Create profile » External profile.

   For more information, see [Manage your provider profile](provider-profiles-managing.md).
3. Submit your profile for approval.

Snowflake will review your profile and respond to you within approximately 1 business day.

> * If your submission is approved, you can then begin publishing listings on Snowflake Marketplace.
> * If your submission is rejected because of a policy violation, Snowflake will provide instructions via email on what needs to be corrected. You can then revise your profile and resubmit it.
>
>   For more information on details for provider profile requirements, see the Snowflake [Provider and Consumer Policies](https://www.snowflake.com/en/legal/provider-and-consumer-policies/).

> **Note:**
>
> Provider profiles won’t be visible on Snowflake Marketplace until a public listing is published.

## Data/share listing approval flow

The following image shows the approval process for publishing listings on Snowflake Marketplace. The steps below the image describe the actions that providers take when following the workflow.

1. Identify the objects that you want to share in a listing.

   For more information, see [Prepare to create a listing](provider-listings-preparing.md).
2. Create a listing and submit it for publishing.

   1. Sign in to [Snowsight](../user-guide/ui-snowsight-gs.md).
   2. In the navigation menu, select Marketplace » Provider Studio.
   3. To create your listing, select Create Listing » Snowflake Marketplace.

      For more information on how to create a Snowflake Marketplace listing, see [Share data or apps publicly on Snowflake Marketplace](provider-listings-creating-publishing.md).
   4. Submit your listing for approval.
3. Snowflake reviews the listing metadata and will respond within approximately 1 business day.

   * If your listing is approved, then it will be published and available on Snowflake Marketplace.

     > **Note:**
     >
     > If you submitted your listing using manual publishing, the listing will not be published. The listing will remain approved until you manually publish the listing. For more information, see [Submit your listing for approval](provider-listings-creating-publishing.md).
   * If your listing is rejected, Snowflake will provide instructions via email on what needs to be corrected. You can then revise your listing and resubmit it.
   > For more information on details for provider profile requirements, see the Snowflake [Provider and Consumer Policies](https://www.snowflake.com/en/legal/provider-and-consumer-policies/).

## Snowflake Native App listing approval flow

The image below shows the approval process for a Snowflake Native App listing on Snowflake Marketplace. The steps below the image describe the actions that providers take when following the workflow.

> **Note:**
>
> Snowflake recommends that you test your application by privately sharing it with another account prior to submitting for publishing. This may expedite the review process.

1. Create a Snowflake Native App package.

   For more information, see [Tutorial 1: Create a basic Snowflake Native App](../developer-guide/native-apps/tutorials/getting-started-tutorial.md).
2. To initiate an automated security scan, [set the DISTRIBUTION property for the application package](../developer-guide/native-apps/security-run-scan.md) to `EXTERNAL`.

   * If the automated security scan fails, Snowflake will perform a manual security review that can take approximately 3 business days.
   * If the Snowflake Native App uses Snowpark Container Services (SPCS), then you must complete a [security questionnaire](https://docs.google.com/forms/d/1XLjbcSrp689kXEvVELa6KbEUOPfsJIirSTG5pGQDMZE/viewform?ts=65fb4866&edit_requested=true). After the questionnaire is approved, the automated security scan starts.
3. Create a listing and submit it for approval.

   For more information, see [Publish an app to consumers](../developer-guide/native-apps/ui-provider-publishing-app-package.md).
4. Snowflake reviews the listing metadata and conducts a functional review of the Native App, ensuring that it meets all Snowflake Marketplace [enforced requirements](../developer-guide/native-apps/publish-guidelines.md).

   * If your listing is approved, it will then be published and available on Snowflake Marketplace.

     > **Note:**
     >
     > If you submitted your listing using manual publishing, the listing will not be published. The listing will remain approved until you manually publish the listing. For more information, see [Submit your listing for approval](provider-listings-creating-publishing.md).
   * If your listing is rejected, Snowflake will reach out using the emails listed in the profile contacts (business and technical) with feedback on the application. Reviews may take up to 14 days.
