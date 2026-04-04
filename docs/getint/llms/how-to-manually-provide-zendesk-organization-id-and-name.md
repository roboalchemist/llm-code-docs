# Source: https://docs.getint.io/guides/integration-synchronization/jira-zendesk-integration/how-to-manually-provide-zendesk-organization-id-and-name.md

# How to Manually Provide Zendesk Organization ID and Name

When integrating with Zendesk, companies that do not own the Zendesk instance but have been provided credentials for an Agent user by the Zendesk instance owner may need to manually input the organization details during integration setup. This guide explains how to retrieve and provide the Zendesk organization ID and Name manually.

#### **Manually Providing Zendesk Organization Details** <a href="#manually-providing-zendesk-organization-details" id="manually-providing-zendesk-organization-details"></a>

1. In Getint, set up the Connection by following our [guide](https://docs.getint.io/guides/quickstart/connection#zendesk). On the integration setup screen, select the connection then click the **PROVIDE MANUALLY** button to access the organization details form.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FJBy33mJz4Gez3cLmq3Sn%2FEstablishing%20a%20connection%20with%20Zendesk.png?alt=media&#x26;token=cd63c59b-29f7-48d8-bc01-a868e464ffa6" alt=""><figcaption></figcaption></figure>

1. Enter the **Organization ID** and **Organization Name** fields with the details provided by the Zendesk instance owner then select **Connect**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FEm0Z498qYtMyFe0VZAft%2FConnection%20with%20Zendesk.png?alt=media&#x26;token=1a97b0aa-5c46-4b70-b2e9-812541429003" alt=""><figcaption></figcaption></figure>

1. Continue to set up the integration and **Save**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FUDpdxv44nODCJendyM94%2FCreating%20a%20ZD%20integration.png?alt=media&#x26;token=2f2e3c69-5b27-4d2e-9279-f9543029c1cc" alt=""><figcaption></figcaption></figure>

#### **How to Obtain Zendesk Organization ID and Name** <a href="#how-to-obtain-zendesk-organization-id-and-name" id="how-to-obtain-zendesk-organization-id-and-name"></a>

The Zendesk instance owner must retrieve the organization ID and Name and provide it to you. Here’s how they can locate this information:

1. **Log in to Zendesk as an Administrator**:
   * The instance owner must sign in with an administrator account.
2. **Access the Organization Information**:
   * Navigate to the following URL, replacing `<ZENDESK_INSTANCE_SUBDOMAIN>` with the Zendesk subdomain:

     `https://<ZENDESK_INSTANCE_SUBDOMAIN>.zendesk.com/api/v2/organizations.json`
3. **Find the Required Details in the API Response**:
   * The response will include a JSON object with the organization details.
   * Look for the `"id"` and `"name"` properties. For example:

     `{`\
     `"organizations": [`\
     `{`\
     `"url": "https://getintaugust.zendesk.com/api/v2/organizations/1900023220573.json",`\
     `"id": 1900023220573,`\
     `"name": "demogetint",`\
     `"shared_tickets": false,`\
     `"shared_comments": false,`\
     `"external_id": null,`\
     `"created_at": "2021-08-27T11:29:24Z",`\
     `"updated_at": "2021-08-27T11:29:24Z",`\
     `"domain_names": [],`\
     `"details": null,`\
     `"notes": null,`\
     `"group_id": null,`\
     `"tags": [],`\
     `"organization_fields": {}`\
     `}`\
     `],`\
     `"next_page": null,`\
     `"previous_page": null,`\
     `"count": 1`\
     `}`
4. **Extract the Details**:
   * **ID**: `1900023220573`
   * **Name**: `demogetint`

The instance owner should share these details with the company setting up the integration.

***

By following these steps, you can ensure the manual provision of Zendesk organization details is accurate, enabling a seamless integration setup.

If you encounter any issues or require further assistance, please contact our [Support Team](https://getint.io/help-center).

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FXjjsbK8xBZHLL005BsbD%2FGetint%20Banner%20-%20Schedule%20a%20Demo.jpg?alt=media&#x26;token=fb9ae7ba-3e7e-49b3-9e3d-b63377861f81" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
