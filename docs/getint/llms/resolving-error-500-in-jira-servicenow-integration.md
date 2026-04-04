# Source: https://docs.getint.io/support-legal-and-others/troubleshooting-guide-for-getint-users/resolving-error-500-in-jira-servicenow-integration.md

# Resolving Error 500 in Jira ServiceNow Integration

### Introduction

Integrating Jira and ServiceNow enhances collaboration across software development and IT service management teams. However, an Error 500, indicating a server error often due to non-authorized access or connection issues, can halt this process. This guide outlines steps to troubleshoot and resolve such issues.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2Firgv7vgP8bS7k3bAwakf%2Fimage.png?alt=media&#x26;token=b018f34d-26cc-4939-a388-535fcc6411ec" alt=""><figcaption></figcaption></figure>

### Troubleshooting Steps

**Common Issue: Error 500 - Non-Authorized or Connection Issues**

**1. Verify Service Now URL**

Incorrect URLs can often lead to connection issues. Ensure the URL for ServiceNow instances is correct in the Getint integration settings.

* Double-check the URLs configured in the Getint integration setup to ensure they accurately reflect your Jira and ServiceNow instances.

**2. Verify Access Control List (ACL) Settings in ServiceNow**

First, ensure that the ACL settings in ServiceNow are correctly configured to grant the necessary permissions for accessing resources:

1. **Log in** to your ServiceNow instance.
2. Navigate to **System Security > User**
3. Search for the ACL rules related to the integration user and verify the following:
   * The integration user has **read and write access** to necessary tables and fields.

**3. Configure Dictionary\_sys with Read Access**

Correct configuration of the sys\_dictionary table is essential to prevent authorization errors:

1. In ServiceNow, go to **System Definition > Dictionary**.\
   ![](https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FJSMgBbEK6jcNKLxlHXUV%2Fimage.png?alt=media\&token=0ce9fd86-2923-4167-b7e5-da4081e3ddfb)
2. Filter by Table name and locate sys\_dictionary.
3. Ensure the field has **read and write access** to the sys\_dictionary table to avoid schema access issues.

**4. Disable Password Reset Requirement**

1. Navigate to **System Properties > Security**.
2. Find the property related to **password reset requirements** and disable it.

   * This ensures the integration's service account doesn't face authentication issues due to periodic password changes.

   <figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F0jvqenNvXj7CMXkBYC2d%2Fimage.png?alt=media&#x26;token=7abe0728-83d7-48a1-ad62-84d975df03d8" alt=""><figcaption></figcaption></figure>

**5: Ensure Proper ITIL Role Setup**

The ITIL role is crucial for comprehensive access to necessary functionalities in ServiceNow.

1. Go to **User Administration > Users**.
2. Select the integration user account.
3. In the **Roles** tab, ensure the **ITIL role** is assigned.
   * This role is crucial for the user to perform necessary operations within ServiceNow.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FVeYQHUNl0GZxoKPwMVAm%2Fimage.png?alt=media&#x26;token=dd0f450e-9c19-4dab-bb7b-0a12d12a0efc" alt=""><figcaption></figcaption></figure>

### **Conclusion**

Following the steps should address the Error 500, smoothing the integration path between Jira and ServiceNow. Please also view the steps in the guide: [Creating a ServiceNow User for Getint Integration](https://docs.getint.io/guides/integration-synchronization/jira-servicenow-integration/creating-a-servicenow-user-for-getint-integration)

{% hint style="info" %}
If you require more personalized assistance or encounter any obstacles not covered in this guide, don't hesitate to contact our support team [here.](https://getint.io/help-center)
{% endhint %}
