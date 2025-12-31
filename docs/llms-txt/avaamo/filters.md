# Source: https://docs.avaamo.com/user-guide/outreach/filters.md

# Filters

You can configure filters based on the column names and values in the recipient CSV such as location, age, date of birth, or gender. When a filter is associated with a campaign, the campaign is triggered to only those recipients matching the filter criteria.&#x20;

**Example**: Consider you wish to trigger campaign messages to only those recipients who are above 18 years of age. In this case, you can configure a filter - "Age greater than 18 years" and associate it with a campaign. &#x20;

This feature combined with the ability to configure multiple messages in a single campaign for different languages, allows you to reuse the same campaign configuration and tailor the messages to different sets of recipients as per the requirement. It helps in:

* Rapid development: You can use the same campaign and tailor the responses to different sets of recipients as per the requirement
* Providing personalized responses, say, for example, based on the location of the user or department a user belongs to.

See [Campaign - Add Message](https://docs.avaamo.com/user-guide/campaigns/create-new-campaign#add-message), for more information on how to associate filters to the campaign.

{% hint style="info" %}
**Notes**:&#x20;

* See [Quick start](https://docs.avaamo.com/user-guide/outreach/quick-start), for a quick article on creating your first outreach program.
* Ensure you have met the [pre-requisites](https://docs.avaamo.com/user-guide/outreach/before-you-begin) before creating a new recipient list.
  {% endhint %}

### Create new filter - Attribute filter

In the Avaamo Platform UI, click the **Outreach** option in the top menu, navigate to the **Filters** tab, and click **Create new filter -> Attribute Filter**. Specify the following details in the pop-up window:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Fla1as0ZSqayBboCrmlr8%2Foutreach-create-filter.png?alt=media&#x26;token=7d34d368-e21e-4be0-b3bf-3fdc162e06a8" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="144.44475920679886">Parameters</th><th width="469.798167959476">Description</th><th>Maximum length</th></tr></thead><tbody><tr><td>Filter name</td><td><p>Indicates the name of the filter. </p><p></p><p>Provide a name that is easily identifiable to pick when you create a campaign. </p></td><td>50 characters</td></tr><tr><td>Filter description</td><td>Indicates the description of the filter. Use this to specify the purpose of the filter. </td><td>200 characters</td></tr><tr><td>Filter conditions</td><td><p>Indicates the conditions that are used to filter the recipient list. </p><ul><li>Column: Column name in the recipient list CSV. Column names are case-sensitive, which implies that the name you provide in the filter condition must be an exact match and in the same case as the column name in the recipient list CSV.</li><li>Type: The type of data the column contains. Supported values: Text, Number, Date</li><li>Operator: Used to perform operations on column value with the specified criteria. </li><li><p>Criteria: Indicates the value that the actual column value in the recipient CSV must satisfy when applied with the operator. If the data type is Date, then the criteria can be in one of the following formats:</p><ul><li>YYYY-MM-DD</li><li>YYYY/MM/DD</li></ul></li></ul></td><td>N/A</td></tr></tbody></table>

* Note that the list of operators displayed is based on the type of data. The following are supported operators for each data type:

<table><thead><tr><th width="208">Data type</th><th>Operators</th></tr></thead><tbody><tr><td>Number</td><td><ul><li>Greater than </li><li>Less than </li><li>Equal to </li><li>Greater than or equal to </li><li>Less than or equal to </li><li>Include</li></ul></td></tr><tr><td>Text</td><td><ul><li>Equal to </li><li>Include</li></ul></td></tr><tr><td>Date</td><td><ul><li>Greater than </li><li>Less than </li><li>Equal to </li><li>Greater than or equal to </li><li>Less than or equal to </li><li>Include</li></ul></td></tr></tbody></table>

* Click **Add new Condition** and select the data type to add new filters. You can add up to 50 conditions in a single filter.
* You can add multiple filters and each filter is an "AND" condition. For example: If you have added two filter conditions - one for "age" greater than 18 and another one for "country" equal to India, then only the recipients with the country as India **and** age greater than 18 are picked for delivering the campaign message.
* **Include** operator: Each filter condition also has an "include" operator that allows you to specify multiple values. In this case, the filter is applied to either of the values mentioned in the criteria. This is an "OR" condition. For example: If you have added a country filter condition with the "include" operator and specified India and the United States, then the recipients with the country as either India or the United States are picked for delivering the campaign message.

Click **Create** after specifying all the details in the **Attribute filter** pop-up window. The newly created filter is displayed in the **Filters** tab. The **Attribute filter** is indicated using <img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FAFA9ZS6hsMYC98ZIPtQm%2FScreenshot%202023-03-22%20at%2012.34.48%20PM.png?alt=media&#x26;token=f8fb15db-a277-4f1e-bf2b-ca76d6f1e8bc" alt="" data-size="line">icon in the **Filters** tab.

### Create new filter - Code filter

These are filters with custom JavaScript code. You can use the **Code filter** option when you wish to check for certain business logic and then apply the recipient filter condition.&#x20;

In the Avaamo Platform UI, click the **Outreach** option in the top menu, navigate to the **Filters** tab, and click **Create new filter -> Code Filter**. Specify the following details in the pop-up window:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FaTFdIfAgyXVFcyvtBfDZ%2Foutreach-create-new-code-filter.png?alt=media&#x26;token=5e0882e5-ece3-4603-afe7-b561a0d1b7fb" alt=""><figcaption></figcaption></figure>

<table><thead><tr><th width="166.44475920679886">Parameters</th><th width="308.798167959476">Description</th><th>Maximum length</th></tr></thead><tbody><tr><td>Filter name</td><td><p>Indicates the name of the filter. </p><p></p><p>Provide a name that is easily identifiable to pick when you create a campaign.</p></td><td>50 characters</td></tr><tr><td>Filter description</td><td>Indicates the description of the filter. Use this to specify the purpose of the filter. </td><td>200 characters</td></tr><tr><td>JS code</td><td><p>Indicates custom Javascript code where you specify the filter condition to match with the recipient list. </p><p></p><p>You can use the following format to specify the column name from the CSV:</p><p>headers["&#x3C;&#x3C;column_name>>"] </p></td><td>N/A</td></tr></tbody></table>

Click **Create** after specifying all the details in the **Code filter** pop-up window. The newly created filter is displayed in the **Filters** tab. The **Code filter** is indicated using <img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FFDf0GjAiocWG88cQvkp6%2FScreenshot%202023-03-22%20at%2012.37.03%20PM.png?alt=media&#x26;token=8f6b61ab-98aa-45de-8ef5-3e62f1561332" alt="" data-size="line">icon in the **Filters** tab.

### **Search filter**

In the **Outreach -> Filters** tab, start entering the text in the **Search** text box and press the **Enter** key or click the **Search** icon. The results are filtered and displayed based on the text entered in the **Search** text box.

### Edit filter

You can edit a template from the **Outreach -> Filters** tab. Click on any filter in the **Filters** page to open the filter in edit mode. Edit the required details and click **Update**.

### Delete filter

* In the **Outreach -> Filters** tab, click three ellipse dots in the **Actions** column of the filter to view the extended menu and click **Delete.**&#x20;
* Click **OK** in the confirmation message to delete the filter.

{% hint style="info" %}
**Note**: You can delete a filter only when it is not associated with any campaign.
{% endhint %}

### Example 1: Multiple filters (Age + Location)

Consider you wish to trigger a campaign message based on the location of the user and to only those recipients who are above 18 years of age.&#x20;

The following example demonstrates how to configure filters for this scenario. In this example, when you associate this filter with a campaign, only those recipients above the age of 18 and from either Mumbai or Pune location are picked for delivering the campaign message:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FX67cGOpY3LnjV2RdCjwT%2Foutreach-filter-example-1.png?alt=media&#x26;token=3cd5390e-261c-47d0-978b-ae6fa4da3795" alt=""><figcaption></figcaption></figure>

### Example 2: Multiple filters with Language (Age + Location in English and French)

Consider you wish to trigger a campaign message based on the location of the user and to only those recipients who are above 18 years of age. Further, you wish to send an English message to recipients from the United States and a French message to recipients from Canada.

The following example demonstrates how to configure filters and campaigns for this scenario:

* Create a filter, say "Location - United States": Age > 18 and Location equals United States.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F10F3XZCm02vcGLveINxP%2Foutreach-filter-example-2-US.png?alt=media&#x26;token=654a5908-84b3-40d9-ade9-8d218eb3cf72" alt=""><figcaption></figcaption></figure>

* Create another filter, say "Location - Canada": Age > 18 and Location equals Canada.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FAAH84SnfSQd8PHUp8zeR%2Foutreach-filter-example-2-US.png?alt=media&#x26;token=2fef2401-b19a-418b-a73c-9113cc19a2e4" alt=""><figcaption></figcaption></figure>

* In the Campaign -> Add Message section, you can add two messages&#x20;
  * One in en-US language and associate the "Location - United States" filter:
  * Another one in fr-FR language and associate the "Location - Canada" filter:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FptczoFe5RJinENksxWOP%2Foutreach-filter-example-2-en-us.png?alt=media&#x26;token=6131a85a-aa12-4a42-86c1-6298f4f6fc43" alt=""><figcaption></figcaption></figure>

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F75WnsS3ZHzcz6fjL30ED%2Foutreach-filter-example-2-fr-FR.png?alt=media&#x26;token=b9bd30b9-a07c-4bfc-b8fb-8bec08f493a0" alt=""><figcaption></figcaption></figure>

Now, when the campaign is triggered, the French message is sent to all the recipients whose location is Canada and age above 18 years and the English message is sent to all the recipients whose location is United States and age above 18 years.

### Example 3: Code filter (All users with appointment date later than today)

Consider that you wish to trigger a campaign message to only those users whose appointment date is later than today.&#x20;

In this scenario, you can configure filters using the Code filters as follows:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FxGYkg04m9NV3svsVEOVK%2Foutreach-filter-example-3.png?alt=media&#x26;token=863fcbfd-ea37-41c0-9682-ea397cdc1b96" alt=""><figcaption></figcaption></figure>
