# Source: https://docs.snowflake.com/en/collaboration/provider-profiles-managing.md

# Manage your provider profile

This topic provides information on managing your provider profile.

## Provider profile fields

When you create or modify your provider profile, you can change a number of fields. The following table describes the fields required for
creating and configuring your provider profile in the Snowflake Marketplace.

| Field Name | Description | Example |
| --- | --- | --- |
| Company Icon | A high-resolution image of your logo in the JPG or PNG format. The file size cannot exceed 2 MB. Square or circle 256px by 256px version of your company logo is recommended. | image.jpg |
| Company Name | Name of your company, which is displayed below the logo image on your listing tile. This is not the name of your Snowflake account. The company name is used as the name of the provider profile. As a provider, you can have more than one provider profile (the provider nickname must be unique for each profile). When you publish a listing, you associate it with a provider profile. | Example Company |
| Company Description | A short introduction (2-3 sentences) about your company, the provider. | Example Company, recognized and documented as the most accurate source of weather forecasts and warnings in the world, has saved tens of thousands of lives, prevented hundreds of thousands of injuries and tens of billions of dollars in property damage. With global headquarters in Palo Alto, CA and other offices around the world, Example Company serves more than 1.5 billion people daily to help them plan their lives. |
| Consumer Contact Email | An email that receives email notifications when a data consumer requests access to your data. The email also appears under Contact Provider on your listing. Providers often create an email alias so several people within their organization can respond to inquiries. Per the Snowflake Provider terms, requests should be responded to within 24 hours, ideally within hours. | `sales@example.com` |
| Support Link or Email | A link (URL) or an email for consumers to contact you for technical support related to the data you are providing. Please make sure to similarly respond to consumer requests quickly. | `support@example.com` |
| Privacy Policy Link | A link (URL) to the provider’s privacy policy. The link is not required for personalized shares. The URL should not be locked behind any login screens or walls. See the Snowflake [Provider Policies](https://www.snowflake.com/provider-policies/) for more information. | `https://www.example.com/privacy` |
| Business Contact Email | An email address for Snowflake to contact the provider with questions about listings. This email address is also used to notify providers when a listing associated with the profile is approved or denied. | `admin@example.com` |
| Technical Contact Email | An email address for Snowflake to contact the provider about shared data. This email address is also used to notify providers when a listing associated with the profile is approved or denied. | `operations@example.com` |

## Edit your provider profile

You can edit your provider profile at any time. Most updates to your profile must be reviewed and approved by Snowflake before they become
visible in the Snowflake Marketplace. Updating the Business Contact and Technical Contact fields in your provider profile does not
require approval from Snowflake.

After your updated profile is approved, the changes are visible for all listings associated with your provider profile.

To modify a provider profile, you must be the owner of the provider profile or you must use a role that has the MODIFY privilege on the
profile. For more information, see [Granting provider privileges to other roles in the Snowflake Marketplace or a Data Exchange](../user-guide/data-exchange-marketplace-privileges.md).

1. Sign in to [Snowsight](../user-guide/ui-snowsight-gs.md).
2. Switch to a role that has the [MODIFY privilege on the profile](../user-guide/data-exchange-marketplace-privileges.md).
3. In the navigation menu, select Marketplace » Provider Studio » Profiles.
4. Select the profile you want to update.
5. In the Manage drop-down menu, select Update Profile.
6. Edit the profile and then click Submit for Approval.

## Delete your provider profile

You can delete your provider profile as long as your profile is not associated with any listings, either published or unpublished.

1. Sign in to [Snowsight](../user-guide/ui-snowsight-gs.md).
2. Switch to a role that has the [MODIFY privilege on the profile](../user-guide/data-exchange-marketplace-privileges.md).
3. In the navigation menu, select Marketplace » Provider Studio » Profiles.
4. Select the profile you want to delete.
5. In the Manage drop-down menu, select Delete Profile.

   > **Note:**
   >
   > If the Delete Profile option is inactive, make sure that no listings are associated with the profile.
6. Click Delete.
