# Source: https://doc.keepnetlabs.com/next-generation-product/customer-success/faqs.md

# FAQs

**Q: When I try to log-in, I get a "invalid token" error**

A: This error message appears when customers try to access keepnet using their "account creation" link on the original email you received when joining Keepnet. Instead, navigate to dash.keepnetlabs.com to login and you won't have any issues!&#x20;

<div align="left"><figure><img src="https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2FDeUf4N0i5cUGcQDMcgtL%2Fimage.png?alt=media&#x26;token=87663dba-aaff-4d28-8493-8eda74bdb86e" alt="" width="375"><figcaption></figcaption></figure></div>

**Q: I added the new Just-in-time Red Flags landing page as a 2nd landing page for a data submission campaign. However, the email template didn't pull through when I tested.**

A: Great idea! When you copy the HTML of the Red Flags landing page to use as a 2nd step, you will also need to copy the custom javascript code. This is the code which loads the email template use in the campaign with the red flags highlighted. Below is a 5 minute video on how to resolve this!&#x20;

[**https://www.loom.com/share/79889043685147479f35c80696442723**](https://www.loom.com/share/79889043685147479f35c80696442723)

We're also going to be improving the customer experience for adding 2nd landing pages which will allow you to select an existing landing page for page 2 without copying HTML at all!&#x20;

**Q: What is Bot Activity and why might I see it on my Campaign Report?**

Bot Activity means something has scanned the link on your phishing email. This could be a security tool, a chrome extension or an analysis engine. Keepnet has highly sophisticated methods of detecting bot activity to ensure your reports only include the human activity of your employees. Here is an explainer deck which covers each Bot Activity type in more detail 👇

{% file src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2FIELIpGT3puSMIZy0f2UI%2FBOT%20ACTIVITY%20EXPLAINED.pdf?alt=media&token=2187047d-486e-4820-beb0-a51892d16bf7>" %}

**Q: How do I remove users from the platform if I've used SCIM to pull in from Entra ID?**

To remove users from Keepnet when connected to Entra ID, please go to portal.azure.com and find the Enterprise Application you made for Keepnet SCIM. Navigate to **Users & Groups** and manage users from here. Add and remove users to Keepnet from this application. Microsoft updates Keepnet every 40 minutes!&#x20;

**Q: Can you share the compliance information for Vishing and Smishing?**

{% file src="<https://3453589210-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LMcQ_WCXOrHv3r05ae5%2Fuploads%2F16fYDqmY1fL34jU21HSK%2FVishing%20and%20Smishing%20Platform%20Security%20and%20Compliance%20(1).pdf?alt=media&token=3ac4c322-7da3-4091-a91b-c8c7741ef01d>" %}
