# Source: https://docs.getint.io/getintio-platform/workflows/mapping-labels.md

# Mapping Labels

Labels play a crucial role in most integrations. They allow you to tag items differently from their current statuses, enhancing how your organization deals with issues while improving workflows. Remember that labels have varying names across different apps and item types, so it’s essential to identify them to map the appropriate label field option.

### How to map Labels <a href="#how-to-map-labels" id="how-to-map-labels"></a>

1. Navigate to your integration settings and access the type mappings. From there, add the appropriate field mappings based on how labels are named in the apps you’re integrating. For instance, in the case of Jira - Azure DevOps, the corresponding mapping would be **Labels** - **Tags**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FxOLWh168NJ6lNGQQ3lbg%2F4446feac8cba4eb71a663955c9e02f4c.png?alt=media&#x26;token=fc9c9d02-d8cc-41ff-a123-1f0b0799aedd" alt=""><figcaption></figcaption></figure>

1. Click **Apply,** and ensure to save your integration.

{% hint style="danger" %}
Please note that there is no need to add additional mapping options for labels. As shown in the image below, the dropdown does not offer any mapping options because it is unnecessary. Getint will automatically identify the label/tag associated with the corresponding item and transfer it to the other app.
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FjjKWjKKXUruSj1XPzU5p%2F2ab10c9f9ba5ec2b19706dc9ba2c4783.png?alt=media&#x26;token=015e0628-fe9d-4a9a-84de-1fc169afccc2" alt=""><figcaption></figcaption></figure>

Some apps, such as Asana, do not support two-way syncing for labels because the fields are read-only, which means either there is no technical possibility or it's not implemented yet. To avoid errors, always choose the correct field mapping for labels. For additional information or if you need further assistance, please reach out to us via our support portal at [Getint Support.](https://getint.io/help-center)
