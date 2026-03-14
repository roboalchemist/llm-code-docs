# Source: https://docs.getint.io/getintio-platform/workflows/advanced-scripting.md

# Advanced Scripting

Advanced mode (scripting) allows you to customize app logic for building data that will be sent to apps via API. When adding a script to the fields in the Advanced Configuration section, ensure that it adheres to JavaScript (JS) syntax. Essentially, this script runs within Getint when specific events are triggered.

Read more about advanced scripting [here](https://getint.io/introducing-getint-io-advanced-scripting/).

### How to Access the Advanced Scripting tab <a href="#how-to-access-the-advanced-scripting-tab" id="how-to-access-the-advanced-scripting-tab"></a>

To access the Advanced Scripting tab and understand the available variables for your integration, follow these steps:

1. From your integration editor, click the **More** button.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FxGTJHIhycekMWS6H5S2I%2FAccesing%20the%20Advance%20Scripting%20Settings.png?alt=media&#x26;token=7c41880c-a134-43c4-a309-02649b8ddf08" alt=""><figcaption><p>We’re using a Jira Jira integration as an example, but this concept applies to our other supported apps.</p></figcaption></figure>

1. Then, click **Advanced**.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FTofuf1y4CMQ4YUDgV55h%2FClick%20Advanced%20to%20access%20the%20settings.png?alt=media&#x26;token=97af0514-e84c-4292-a3a6-eefb4333f600" alt=""><figcaption></figcaption></figure>

1. The **Advanced Configuration** tab will be displayed. Each checkbox enables a code row that can be used to run custom scripts that make the tool send specific requests before specific steps of the synchronization process.

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2FueEyOh0BjcVGJiaqzjIq%2FAdvanced%20Configuration.png?alt=media&#x26;token=6a01e785-eda0-4564-aa07-eb95936dd07f" alt=""><figcaption></figcaption></figure>

{% hint style="info" %}
Scripts applied to **Before integration runs** will trigger every time an integration is going to run. Here, we can provide some logic whenever an integration is syncing, as long as it complies with JavaScript (JS) syntax.
{% endhint %}

### **List of Events You Can Define with the Scripting Feature**

#### Before Integration Runs

It runs every time just before integration runs:

{% code overflow="wrap" %}

```
api.leftApp.fetch(url) - fetch data from endpoint from LEFT side app
api.leftApp.post(url, postData) - post data to LEFT side app
api.rightApp.fetch(url) - fetch data from endpoint from RIGHT side app
api.rightApp.post(url, postData) - post data to RIGHT side app
api.log(string) - write a log line to log file of the run
```

{% endcode %}

#### Before the Item Request Object Is Sent

It runs before CREATE or UPDATE requests are sent with item data:

{% code overflow="wrap" %}

```
api.leftApp.fetch(url) - fetch data from endpoint from LEFT side app
api.leftApp.post(url, postData) - post data to LEFT side app
api.rightApp.fetch(url) - fetch data from endpoint from RIGHT side app
api.rightApp.post(url, postData) - post data to RIGHT side app
api.log(string) - write a log line to log file of the run

state.syncAction - Create or Update 
state.reqObj - request object data (containing fields) that was prepared by GetInt
state.triggerObj - data of the trigger/source object
state.skipSync - if set to true, the synchronization for this item will be skipped entirely
```

{% endcode %}

For instance, if ITEM-1 was modified in Jira and will be synced with Azure Work Item #32, `state.triggerObj` contains data of ITEM-1 and `state.reqObj` is a constructed data object that will update #32.

#### Before a Comment Is Created

<pre data-overflow="wrap"><code>api.leftApp.fetch(url) - fetch data from endpoint from LEFT side app
api.leftApp.post(url, postData) - post data to LEFT side app
api.rightApp.fetch(url) - fetch data from endpoint from RIGHT side app
api.rightApp.post(url, postData) - post data to RIGHT side app
api.log(string) - write a log line to log file of the run

<strong>state.comment - comment data that was prepared by GetInt to send
</strong></code></pre>

If the `state.comment.skipped`  flag is set up, an equal true comment will be skipped, and the request won't be sent.

#### Mapping ServiceNow User ID to Jira Username

To ensure proper synchronization between ServiceNow and Jira when the ServiceNow User ID equals the Jira username, use the following scripts. Make sure the default mapping for both sides is set to Use value from the other side

**Jira Side Script**

The following script should be used on the Jira side to map the ServiceNow user correctly:

```

if (state.reqObj.fields && state.reqObj.fields.assignee) {
    var userIdentifier = state.reqObj.fields.assignee.name;
    var response = api.rightApp.fetch('/api/now/v2/table/sys_user?sysparm_query=sys_id=' + userIdentifier + '&sysparm_fields=user_name');
    if (response && response.result && response.result[0]) {
        api.log('found snow user ' + response.result[0].user_name + ' by searching for ' + userIdentifier);
        state.reqObj.fields.assignee.name = response.result[0].user_name;
    }
}
```

**ServiceNow Side Script**

The following script should be used on the SNOW side to map the Jira user correctly:

```
if (state.reqObj.assignee) {
    var userIdentifier = state.reqObj.assignee.name;
    var response = api.rightApp.fetch('/api/now/v2/table/sys_user?sysparm_query=sys_id=' + userIdentifier + '&sysparm_fields=user_name');
    if (response && response.result && response.result[0]) {
        api.log('found snow user ' + response.result[0].sys_id + ' by searching for ' + userIdentifier);
        state.reqObj.assignee.name = response.result[0].user_name;
    }
}
```

By using these scripts, you can effectively map ServiceNow User IDs to Jira usernames, ensuring seamless integration and synchronization between your systems.

### Example

Request to migrate a GitLab issue to Jira. Except for the field data, we want to copy to Jira information about related merge requests to the given GitLab issue. GitLab offers an API where we can fetch the necessary information and obtain pull request data in JSON format. Jira is on the left side in integration, and GitLab is on the right side. To achieve what we need, we have to put below JavaScript code below under the **Before item request object sent (left app)** option.

```
// 1 - fetch merge requests data frmo rightApp (GitLab)
var links = api.rightApp.fetch('/api/v4/projects/' + state.triggerObj.project_id + '/issues/' + state.triggerObj.iid + '/related_merge_requests');
if (links) {
  // 2 - iterate over links and add to the array
  for (var i=0; i<links.length; i++) {
    var link = links[i].web_url;
    linksArray.push('[' + link + '|' + link + ']');
  }
}
// 3 - join links together and insert into a customfield
state.reqObj.fields['customfield_10174'] = mergesArray.join('\n');
```

{% hint style="info" %}
If you encounter any issues or need further assistance, please contact our support team [here](https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team). Our fantastic team at Getint is always ready to assist you!
{% endhint %}

<figure><img src="https://4106311246-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MR6Z9V8zLATPQPOGSDf%2Fuploads%2F9OSEDBl869gRue9mQAwv%2FGetint%20Yellow%20Banner.png?alt=media&#x26;token=9cc42142-6e48-4931-8fd5-cbf7dcf4cdc1" alt=""><figcaption><p><a href="https://calendly.com/d/cpws-jb2-8xx/demo-call-all-team">Start your integration journey. Schedule a free consultation with our Getint Integration Expert today!</a></p></figcaption></figure>
