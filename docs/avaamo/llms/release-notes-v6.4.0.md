# Source: https://docs.avaamo.com/user-guide/release-notes/v6.0-to-v6.4.x-releases/v6.4.x/release-notes-v6.4.0.md

# Release notes v6.4.0

The Avaamo Conversational AI Platform v6.4.0 release includes 1 new feature, 7 enhancements, and 1 change distributed as follows:

**New feature:** This release includes the introduction of a new **Outreach Campaign** featur&#x65;**.** See [What's new in v6.4.0?](https://docs.avaamo.com/user-guide/release-notes/v6.0-to-v6.4.x-releases/v6.4.x/whats-new-in-v6.4.0) for more information.

**Enhancements**: This release includes enhancements related to the following existing features:

<table><thead><tr><th width="197">Module</th><th>Enhancements</th></tr></thead><tbody><tr><td>MS Teams</td><td><a href="#ms-teams-ability-to-integrate-with-other-applications-on-behalf-of-the-user">MS Teams: Ability to integrate with other applications on behalf of the user</a></td></tr><tr><td>Accessibility</td><td><a href="#accessibility-improvements">Accessibility improvements</a></td></tr><tr><td>Regression testing </td><td><a href="#regression-testing-file-format-version-2">Regression testing file format - Version 2</a></td></tr><tr><td>REST APIs</td><td><a href="#performance-improvements-in-analytics-apis">Performance improvements in Analytics APIs</a></td></tr><tr><td>Answers skill</td><td><a href="#filter-documents-in-the-answers-skill-based-on-the-upload-status">Filter documents in the Answers skill based on the upload status</a></td></tr><tr><td>Javascript code </td><td><a href="#ability-to-set-multiple-user-properties-in-a-single-method">Ability to set multiple user properties in a single method</a></td></tr><tr><td>Analytics</td><td><a href="#sms-gateway-analytics">SMS Gateway Analytics</a></td></tr></tbody></table>

**Changes:** This release includes changes related to the following modules:&#x20;

* Defining attributes for documents or URLs. See [Enforce document attributes to be a JSON](#enforce-document-attributes-to-be-in-json), for more information.
* Deeplink URL value in agent responses. See [Deeplink URL value](#deeplink-url-value), for more information.

{% hint style="info" %}
**Deprecation notice**: In this release, the usage of URLs for deep links in the agent responses has been deprecated. See [Deprecation notice](#deprecation-notice), for more information.
{% endhint %}

## Component-wise distribution

The following table lists the component-wise distribution of new features, enhancements, and changes in the v6.4.0 release:

{% tabs %}
{% tab title="New features" %}

<table><thead><tr><th width="178">New feature</th><th>Component</th></tr></thead><tbody><tr><td><a href="whats-new-in-v6.4.0">Outreach</a></td><td><ul><li>Dashboard -> Outreach</li><li>REST APIs -> Outreach Insights API </li><li>REST APIs -> Outreach Changelog API </li><li>REST APIs -> SMS Reporting API </li><li>REST APIs -> SMS Opt status API</li></ul></td></tr></tbody></table>
{% endtab %}

{% tab title="Enhancements" %}

<table><thead><tr><th width="359">Enhancements</th><th>Component</th></tr></thead><tbody><tr><td><a href="#ms-teams-ability-to-integrate-with-other-applications-on-behalf-of-the-user">MS Teams: Ability to integrate with other applications on behalf of the user</a></td><td><ul><li>Channels -> MS Teams</li></ul></td></tr><tr><td><a href="#accessibility-improvements">Accessibility improvements</a></td><td><ul><li>Agent widget</li></ul></td></tr><tr><td><a href="#regression-testing-file-format-version-2">Regression testing file format - Version 2</a></td><td><ul><li>Regression test</li></ul></td></tr><tr><td><a href="#sms-gateway-analytics">SMS Gateway Analytics</a></td><td><ul><li>Monitor -> SMS Gateway Analytics</li></ul></td></tr><tr><td><a href="#performance-improvements-in-analytics-apis">Performance improvements in Analytics APIs</a></td><td><ul><li>Analytics - Message API </li><li>Analytics - Unhandled API </li><li>Analytics - Successful Message API</li><li>Analytics - User Session API</li></ul></td></tr><tr><td><a href="#filter-documents-in-the-answers-skill-based-on-the-upload-status">Filter documents in the Answers skill based on the upload status</a></td><td><ul><li>Answers skill -> Document groups</li></ul></td></tr></tbody></table>
{% endtab %}

{% tab title="Changes" %}

<table><thead><tr><th width="249">Change</th><th>Component</th></tr></thead><tbody><tr><td><a href="#deeplink-url-value">Deeplink URL value</a></td><td><ul><li>Deeplinks in Quickreply </li><li>Deeplinks in Card </li><li>Deeplinks in Carousel </li><li>Deeplinks in ListView </li><li>Deeplinks in Persistent menu</li></ul></td></tr><tr><td><a href="#enforce-document-attributes-to-be-in-json">Enforce document attributes to be a JSON</a></td><td><ul><li>Answers skill -> Edit -> Update Document </li></ul></td></tr></tbody></table>
{% endtab %}
{% endtabs %}

## Enhancements

### MS Teams: Ability to integrate with other applications on behalf of the user &#x20;

In this release, the MS Teams channel has been enhanced with a new `Get user access token` configuration option. When this option is enabled, the OAuth user access token generated in the Azure bot is available in the `context.user.sso_token` object. You can use this token to access other applications on behalf of the user seamlessly.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FUoqB8iwDHKZybhAs5p8U%2F6.4-ms-teams-get-user-access-token.png?alt=media&#x26;token=9ecbfadd-cda3-466c-b939-736149693f9a" alt=""><figcaption></figcaption></figure>

See [MS Teams](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/microsoft-teams-ms-teams) and [Use case: Get user access token](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/microsoft-teams-ms-teams/use-case-get-user-access-token), for more information.

### Accessibility improvements

In this release, the Accessibility inclusivity in the agents built using Avaamo Conversation AI Platform has been improved. The following are a few key enhancements incorporated in this release:

* **Accessibility improvements specific to Windows:** In the Windows High Contrast mode as enabled via Windows settings, the focus indication of the agent icon button at the bottom-right corner has been enhanced and the border of the chat window is accessible and easy to identify.
* **Minimize the agent widget using the Escape button**: The user can now press the `Escape` button on the keyboard to minimize the agent widget at any point in time in the conversation flow, as long as the focus is inside the agent chat widget.

### Regression testing file format - Version 2

In this release, the regression test file format has been enhanced with a new and improved version referred to as - Version 2 (V2) format.&#x20;

Regression test - V2 format is based on test identifiers. Based on the way the test identifiers are defined, the platform infers the flow and the sequence of execution. The following example demonstrates a sample Regression test - V2 format file:

<table><thead><tr><th width="241">ID</th><th width="146">QUERY</th><th width="149">TYPE</th><th>EXPECTED_VALUE</th></tr></thead><tbody><tr><td>OrderPizza-1</td><td>I want to order pizza</td><td>intent</td><td>macpizza_order.1</td></tr><tr><td>OrderPizza-2</td><td>veg</td><td>intent</td><td>macpizza_order.2</td></tr><tr><td>OrderPizza-3</td><td>cheese</td><td>intent</td><td>macpizza_order.4</td></tr><tr><td>OrderPizzaStarter-1</td><td>I want to order pizza</td><td>intent</td><td>macpizza_order.1</td></tr><tr><td>OrderPizzaStarter-2</td><td>veg</td><td>intent</td><td>macpizza_order.2</td></tr><tr><td>OrderPizzaStarter-3</td><td>cheese</td><td>response_node</td><td>macpizza_order.starters</td></tr><tr><td>PizzaLiveAgent</td><td>I want to talk to an agent</td><td>intent</td><td>agent_request</td></tr><tr><td>StoreFAQ</td><td>where is your store?</td><td>intent</td><td>mac_pizza_faqs.store_faqs</td></tr><tr><td>Unhandled</td><td>do you use organic ingredients?</td><td>intent</td><td>unhandled</td></tr><tr><td>OrderFAQDisambiguation</td><td>order</td><td>disambiguation</td><td>macpizza_order.1|mac_pizza_faqs.order_faq</td></tr><tr><td>Disambiguation</td><td>order</td><td>disambiguation</td><td>disambiguation</td></tr></tbody></table>

The following table summarizes a few key differences and improvements of the Regression test - V2 format file:

<table><thead><tr><th width="162.33333333333331">Areas</th><th>Regression test file format - V1</th><th>Regression test file format - V2</th></tr></thead><tbody><tr><td>Ease-of-use</td><td><p>Understanding and writing test cases is a time-consuming process. </p><p></p><p></p></td><td><p>Test identifiers make it easier to write test cases. </p><p></p><p></p></td></tr><tr><td>Multi-turn conversation flow testing</td><td>Requires a long list of comma-separated flows with skill and intent keys and many additional columns with responses for each node.</td><td>Requires the developers to write the test cases with proper test identifiers, each in a separate row. The rest of the inference of grouping and executing the test cases is done by the Platform.</td></tr><tr><td>Scalability and Maintainability </td><td><p>With the comma-separated list, it is not easy to scale and maintain new test cases or to augment the existing test cases.</p><p></p><p>Troubleshooting any error in the test case is time-consuming.</p></td><td><p>Helps to enhance the existing test case flow just by adding new identifiers. </p><p></p><p>Troubleshooting any error is easier since each row is a separate test case in a flow. </p></td></tr><tr><td>Flow control testing </td><td>A limitation of the V1 format, as it is only based on the skill key and intent key. </td><td>Allows complete test coverage of the flow control statements as it offers a combination of both intent and response node matching. </td></tr></tbody></table>

See [Regression test file format - V2](https://docs.avaamo.com/user-guide/how-to/build-agents/test-agents/regression-testing/regression-test-file-format-1), for more information.

### SMS Gateway Analytics

In this release, the **Monitor** section of the agent has been enhanced with a new analytics page referred to as **SMS Gateway Analytics**.

SMS Gateway Analytics is a dashboard that allows you to view the SMS report of the messages sent through the SMS Send API. With these statistics, you can decide how and where to further improve the user experience with your agent based on your business requirements.

{% hint style="info" %}
**Note**: SMS Gateway Analytics is available only when the SMS channel is enabled for the agent. See [SMS channel](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/sms), for more information.
{% endhint %}

See [SMS Gateway Analytics](https://docs.avaamo.com/user-guide/how-to/build-agents/monitor-and-analyze/sms-gateway-analytics), for more information.

### Performance improvements in Analytics APIs

In this release, the performance of the following APIs has been improved, to allow fetching a larger set of records at a faster rate.&#x20;

* [Analytics - Message API](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/analytics-api/messages)
* [Analytics - Unhandled API](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/analytics-api/unhandled-messages)
* [Analytics - Successful Message API](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/analytics-api/successful-messages)
* [Analytics - User Session API](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/analytics-api/user-sessions)

Along with this improvement, note that there is also a recommendation for time duration mentioned for all the REST APIs where you can specify a date range. For optimal API performance, the recommended time duration for fetching data from any REST APIs supporting a date range or time period is 7 days.&#x20;

### Filter documents in the Answers skill based on the upload status

In this release, the Document groups page has been enhanced with a new **Status** dropdown. It helps you to filter documents based on their upload status. Along with the status, you can also view the count of documents for each status in the dropdown. This feature is helpful when you have a large set of documents uploaded in a document group and say you wish to view only errored-out documents in the group.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FfSs1tpMuUVz7S5ryAUPl%2F6.4-answers-document-group-status.png?alt=media&#x26;token=649190c3-bd04-4969-b7aa-11c8fa703085" alt=""><figcaption></figcaption></figure>

See [Document groups](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/manage-avaamo-answers-1/create-document-groups) and [Upload Content](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/manage-avaamo-answers-1/add-document-or-url-1), for more information.

### Ability to set multiple user properties in a single method&#x20;

In this release, the ability to set user property in the Javascript code has been enhanced with a new method `User.setProperties`.

{% code overflow="wrap" %}

```javascript
User.setProperties({"<<key1>>":"<<value1>>","<<key2>>":"<<value2>>","<<key3>>":"<<value3>>",...})

... - Indicates one or more parameter
```

{% endcode %}

The new method accepts multiple key-value pairs in the input parameters, hence the agent developers can set all the user properties in a single call instead of using multiple calls for setting user properties individually using [`User.setProperty`](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/user.setproperty). It helps in optimizing the code and making the code more efficient.

See [User.setProperties](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/user.setproperties), for more information.

## Changes

### Enforce document attributes to be in JSON

In this release, the validation for defining the attributes for the uploaded documents or URLs in the Answers skill has been changed. When you specify the document attributes in the **Update Document** pop-up window, the platform validates and allows you to proceed only if it is a valid JSON.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F3jVzYOAdm4e32thn8YYO%2F6.1-preview-url.png?alt=media\&token=73130cee-0751-4837-8efe-d2a6b52253e3)&#x20;

{% hint style="info" %}
**Note**: For existing documents with invalid attributes, there is no impact. It will continue to work as before.
{% endhint %}

In the previous release, it was possible to save attributes with invalid JSON, and since the attributes were in invalid JSON format, it was not used by the Answers skill and hence was not useful. &#x20;

See [Defining attributes for documents or URLs](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-avaamo-answers-1/manage-avaamo-answers-1/perform-common-actions#defining-attributes-for-documents-or-urls), for more information.

### Deeplink URL value&#x20;

In this release, the URL parameter value of Deeplink responses has been changed for security reasons. With this change, the URL, even when copied and used in the browser does not redirect to any site as there is no valid domain or host.&#x20;

{% hint style="success" %}
**Key points**:

* The URL change is backward compatible and the old URL in your agent implementation continues to work as-is.
* In this release, the usage of URLs in deep links is deprecated due to security reasons. See [Deprecation notice](#deprecation-notice), for more information.
  {% endhint %}

The following lists a few examples of this change:

<table><thead><tr><th width="155">Deeplink type</th><th width="266">Old URL for Deeplink</th><th>New URL for Deeplink</th></tr></thead><tbody><tr><td>Date picker</td><td><code>https://web.avaamo.com#app/datepicker/messages/new?format=&#x3C;&#x3C;date_format>></code></td><td><code>avaamo:#app/datepicker/messages/new?format=&#x3C;&#x3C;date_format>></code></td></tr><tr><td>Goto node</td><td><code>https://web.avaamo.com#messages/hidden/%23goto_node_&#x3C;&#x3C;skill_key>>_&#x3C;&#x3C;intent_key>>/new/&#x3C;&#x3C;message>></code></td><td><code>avaamo:/#messages/hidden/%23goto_node_&#x3C;&#x3C;skill_key>>_&#x3C;&#x3C;intent_key>>/new/&#x3C;&#x3C;message>></code></td></tr><tr><td>Start over</td><td><code>https://web.avaamo.com#messages/hidden/start%20over/new/start</code></td><td><code>avaamo:#messages/hidden/start%20over/new/start</code></td></tr></tbody></table>

See the following modules for more information:

* [Deeplinks in Quickreply](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response/quick-reply#values-in-deeplinks)
* [Deeplinks in Card](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response/card/card-links#deep-links)
* [Deeplinks in Carousel](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response/carousel)
* [Deeplinks in ListView](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response/list-view)
* [Deeplinks in Persistent menu ](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-persistent-menu#deep-link)

## Deprecation notice

As per the security guidelines, the usage of URLs for deep links in the agent responses has been deprecated from the v6.4.0 release onwards.&#x20;

Instead, you can use an improved and easy-to-use format for providing deep links. See [What action to take?](#what-action-to-take) for more information. The easy-to-use format helps towards providing a pleasant development experience for the developers implementing the agent in the Avaamo Conversational AI Platform.

### Why?

In the legacy implementation, developers had to specify URLs in the value parameter for deep links when a date picker response was required. For example, the following is a sample JS to use a date picker in a quick reply response:

{% code overflow="wrap" %}

```javascript
return[{
quick_reply: {
    "content": "Pick a delivery date",
    "links": [
      {
            "title": "Delivery date",
            "type": "deeplink",
            "value": "avaamo:#app/datepicker/messages/new?format=DD/MM/YYYY"
       }
    ]
}
}]
```

{% endcode %}

The legacy implementation was tedious to use and error-prone. Debugging and troubleshooting the errors caused by the incorrect usage of URLs was time-consuming. The new format for using deep links is simple and easy to use, hence making the development experience pleasant.&#x20;

### When is the support completely stopped?

This feature will be removed from the next release onwards.

### What action to take?

Use the following format for using deep links in agent responses (Quick reply, Cards, Persistent menu, Carousel):

<table><thead><tr><th width="179">Function</th><th>Example formats in Quick Reply</th></tr></thead><tbody><tr><td>Date picker</td><td><pre class="language-javascript"><code class="lang-javascript">return {
    quick_reply: {
        content: "Pick a delivery date",
        links: [{
            title: "Delivery date",
            type: "date",
            format: "YYYY-DD-MM"
        }]
    }
}
</code></pre></td></tr><tr><td>Date picker with min and max dates</td><td><pre class="language-javascript"><code class="lang-javascript">return {
    quick_reply: {
        content: "Pick a delivery date",
        links: [{
            title: "Delivery date",
            type: "date",
            format: "YYYY-DD-MM",
            minDate: "2023-10-01",
            maxDate: "2023-12-01"
        }]
    }
}
</code></pre></td></tr><tr><td>Goto node </td><td><pre class="language-javascript" data-overflow="wrap"><code class="lang-javascript">return [{
    quick_reply: {
        "content": "Do you want to get some starters?",
        "links": [{
            "title": "Get Starters",
            "type": "post_message",
            "hidden_content": "#goto_node_macpizza.starters"
        }]
    }
}]
</code></pre></td></tr><tr><td>start over</td><td><pre class="language-javascript"><code class="lang-javascript">return [{
    quick_reply: {
        "content": "Wrong order. Start again",
        "links": [{
            "title": "Wrong order",
            "type": "post_message",
            "hidden_content": "#start over"
        }]
    }
}]
</code></pre></td></tr></tbody></table>

See the following modules for more information:

* [Deeplinks in Quickreply](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response/quick-reply#values-in-deeplinks)
* [Deeplinks in Card](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response/card/card-links#deep-links)
* [Deeplinks in Carousel](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response/carousel)
* [Deeplinks in ListView](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response/list-view)
* [Deeplinks in Persistent menu ](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/add-persistent-menu#deep-link)
