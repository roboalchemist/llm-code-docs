# Source: https://developers.make.com/custom-apps-documentation/app-review/request-app-review.md

# Request app review

Once you make sure that your app meets Make's [requirements](https://developers.make.com/custom-apps-documentation/app-review/prerequisites) and follows Make's [best practices](https://github.com/integromat/make-apps-sdk-docs/blob/master/app-review/broken-reference/README.md), you can request an app review:

## Request a review

To request an app review:

{% stepper %}
{% step %}
Remove the test modules or test connections before you publish an app. When your app is public, you can't delete its modules, connections, or other components.
{% endstep %}

{% step %}
Navigate to your custom app's code and click the **Publish** button.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-e140b69584aa586e1c2ee29aa572e966b185f361%2Fpublishapp.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>

{% hint style="warning" %}
Once you publish your app, you can't unpublish it. See the [app visibility section](https://developers.make.com/custom-apps-documentation/create-your-first-app/app-visibility) for more details.
{% endhint %}
{% endstep %}

{% step %}
In the **Modules** tab, click the switch to set the visible status of each module in the app that you want to publish.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-655deacdf0a7074ed5f8bb3e021aa735d0711554%2Fvisibility.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
You will see a new **Review** tab in the top panel.

<div align="left"><figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-7ddcdb6d04682f975e00fa056ea3998528fd934b%2Freviewtab.png?alt=media" alt="" width="563"><figcaption></figcaption></figure></div>
{% endstep %}

{% step %}
Complete the form on the **Review** page.

* Add a link to the API documentation of the service for which you are creating a custom app.
* Add a link to scenarios with the custom app modules. Check the testing scenarios section in the [App review prerequisites](https://developers.make.com/custom-apps-documentation/app-review/prerequisites).
  {% endstep %}

{% step %}
Click the **Request review** button at the bottom of the page.
{% endstep %}
{% endstepper %}

The data you submit is sent to Make QA developers for review. At the top of the page, the **Request review** button changes to **Review process started** and becomes inactive. Also, the app status changes to **pending approval**.

<figure><img src="https://1562974717-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FNS0mCBwODiYtOVXjc6qf%2Fuploads%2Fgit-blob-104db6d7ba29257e0706af64ebead6a3f003e249%2Freviewprocessstarted.png?alt=media" alt="" width="563"><figcaption></figcaption></figure>

Once you request the app review, Make sends you an email with the subject: "*App review: YourApp'sName*". If you have any questions or additional information to share, reply to the email.

Each time you update your app based on reviewer feedback, run your scenarios to generate new logs.

If you need to edit your links, you can update your form and submit the changes by clicking the **Update review** button

## Review process

The review process contains three phases: form submission, automatic review, and manual review.

### Form submission

Once you hit the **Request Review** button, you will receive an e-mail containing a link to our form where you will be prompted to share the following information about you and your app. This will help us to provide better service to you:

* **Developer information** - What is your relationship with the vendor of the API service?
* **Partnership contact** - Applicable for ISV. The details of a contact person or team on your end responsible for partnership-related discussions.
* **Support contact** - Details of the contact person or team that should be contacted in case of any app issues reported by users.
* **Categories and subcategories of your app** - The categories and subcategories in which you wish to have the app listed on the [make.com integrations page](https://make.com/en/integrations).
* **Logo of your company** - Applicable for ISV. The logo should appear on the app's landing page on make.com.
* **URL to the service** - The URL leading to your website that should appear on the app's landing page on make.com.

Upon completing the form, you will receive feedback from the automatic review.

### Automatic review (beta)

Your app is first reviewed by our application. The automatic review checks for common issues and generates a PDF file with the issues found.

The PDF file with feedback from the automatic review is sent to the existing app review email thread.

{% hint style="info" %}
The automatic review is in beta and is still in the process of improvement. Therefore, there might be inconsistencies.
{% endhint %}

### Manual review

Once your app passes the automatic review, it is reviewed by our QA engineer who makes sure that your app follows our best practices and is user-friendly.

The QA engineer shares the feedback in the existing app review email thread.

Once your app successfully passes the manual review, your app is listed in our planned release. You will be informed about the app approval as well as the app release.
