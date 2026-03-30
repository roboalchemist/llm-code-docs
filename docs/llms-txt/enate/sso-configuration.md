# Source: https://docs.enate.net/enate-help/builder/builder-2021.1/administration/sso-configuration.md

# SSO Configuration

## SSO Configuration in Azure Active Directory

This article outlines the steps to follow to configure SSO in Azure Active Directory.

1\) Register a new application from the Enterprise Application | All Applications screen in the Azure Active Directory portal: <https://aad.portal.azure.com/#blade/Microsoft_AAD_IAM/StartboardApplicationsMenuBlade/AppAppsPreview/menuId/>

2\) Create a new non-gallery application. Including SSO or SAML in the name for this application can help to distinguish this from future GraphAPI applications for the same instance.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FC4qvxaNLJ6tJddx6ToIH%2Fimage.png?alt=media\&token=68bc957a-4b0b-4194-ac08-d8e51b8ce781)

3\) Once the application has been created and the configuration pages are visible, navigate to Single sign-on under the Manage section and select SAML.

4\) Enate will supply an XML metadata file for each instance. This can be imported using the “Upload metadata file” button at the top of the page.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FYBPzyrJRUpTxDLTJBZAl%2Fimage.png?alt=media\&token=c744afe1-d63b-4c9d-8ce1-a98c52ceb799)

5\) Once imported, verify that the Identifier (Entity ID) and the Reply URL (Assertion Consumer Service URL) have been populated and the press Save.

6\) On the Single sign-on page with the newly populated Basic SAML Configuration section, you should be able to download the Federation Metadata XML under section 3, SAML Signing Certificate.

![](https://3859925423-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MWYnDNwe3Cuo4zlGbs5-887967055%2Fuploads%2FLSbjTXKfKlO6gzbamwlq%2Fimage.png?alt=media\&token=8db9510c-87f7-4c02-933b-472462fdd773)

{% hint style="info" %}
**Note**: Enate typically uses the Email Address field configured for users within Enate to validate claims. This must match one of the supplied claims. User.userprincipalname or user.mail typically satisfy this but if you domain has multiple email addresses or situations where the userprincipalname may not always match the email address you may need to transform a claim to provide the correct information.
{% endhint %}

7\) This downloaded XML file should be supplied to Enate to complete the Enate side of the SSO configuration prior to testing.

8\) On the Properties page under the Manage section, you should change the “Visible to users?” setting to “No”.

9\) Depending on your configuration you can also change the “Assignment required?” to “No” and then manually assign Users to the application under the Users and groups page under the Manage section.
