# Source: https://learn.microsoft.com/en-us/clarity/clarity-api

Title: Clarity client API

URL Source: https://learn.microsoft.com/en-us/clarity/clarity-api

Published Time: Fri, 05 Dec 2025 18:51:05 GMT

Markdown Content:
Important

Clarity shouldn't be used on any websites/apps targeting users under the age of 18.

You can quickly get started with Clarity without coding but by interacting with the Clarity client API. This API can help you access advanced features as described in this reference. Access these features by adding the following calls to Clarity APIs to the HTML or JavaScript of your webpage.

Note

Your Clarity ID serves as your API key. No other client API key is necessary, and there is no cost for using Clarity client APIs.

| Purpose | Syntax | Parameters | Required? |
| --- | --- | --- | --- |
| [Cookie consent](https://learn.microsoft.com/en-us/clarity/setup-and-installation/clarity-consent-api-v1) | `window.clarity('consent')` | String | Yes |
| [Custom identifiers](https://learn.microsoft.com/en-us/clarity/setup-and-installation/identify-api) | `window.clarity("identify", "custom-id", "custom-session-id", "custom-page-id", "friendly-name")` | Strings | `"custom-id"`: Yes, `"custom-session-id"`: No, `"custom-page-id"`: No, `"friendly-name"`: No |
| Custom tags | `window.clarity("set", <key>, <value>)` | `<key>`: string, `<value>`: string or an array of strings | Yes |
| Events | `window.clarity("event", <value>)` | `<value>`: string of the event name | `<value>`: Yes |

| Purpose | Syntax | Parameters | Required? |
| --- | --- | --- | --- |
| Mask content | `data-clarity-mask="true"` | Boolean | Yes |
| Unmask content | `data-clarity-unmask="true"` | Boolean | Yes |

Custom Identifiers are informational data values about site visitors that your client-side code sends to Clarity over its Identify API. They include `custom-id`, `custom-session-id`, and `custom-page-id` and can help you customize the features on your site that requires it. Learn more on [custom identifiers](https://learn.microsoft.com/en-us/clarity/setup-and-installation/identify-api).

Clarity offers many predefined ways to filter and analyze website data. However, you might want to track elements specific to your site or user experience. With custom tags, you can apply arbitrary tags to your Clarity session.

To use custom tags, pass the `set` argument along with a key-value pair to define a tag in your JavaScript. When Clarity collects data for that tag, it appears in the [Filters](https://learn.microsoft.com/en-us/clarity/filters/clarity-filters) options.

| Syntax | Parameters | Required? |
| --- | --- | --- |
| `window.clarity ("set", "key", "value")` | `"key"`: string, `"value"`: string or an array of strings | Yes |

Note

You can call this API multiple times. There is no limit to the number of custom tags you can have.

```
window.clarity("set", "experiment", "experiment1") 
window.clarity("set", "flight", ["flight1", "flight2"])
```

**Note**: The last call has the same effect as:

```
window.clarity("set", "flight", "flight1")
window.clarity("set", "flight", "flight2")
```

Clarity offers no-code smart events, which automatically surface key user actions. Refer to [Smart events](https://learn.microsoft.com/en-us/clarity/setup-and-installation/smart-events) to learn how to view, create, and customize new smart events completely code free.

If you prefer to instrument these user actions manually via Clarity APIs, call the event API with the action you'd like to track. When Clarity collects data for this event, it appears with your other Smart events in the **Filters**, **Dashboard**, **Settings**, and **Recordings** vertical.

Note

You can call this API multiple times per page. Each event is logged individually and can be filtered, viewed in all the verticals.

```
window.clarity("event", "newsletterSignup")
```

By default, your users' sensitive content is masked. We classify all input box content, numbers, and email addresses as sensitive content. Masked content isn't uploaded to Clarity.

If you want more control over which content on your site is masked, you can [mask content using the Clarity website](https://learn.microsoft.com/en-us/clarity/setup-and-installation/clarity-masking#using-the-clarity-website-to-mask-and-unmask-content) or add the `data-clarity-mask` property to HTML elements on your site.

Note

Setting `data-clarity-mask` to false has no effect. To unmask content, use [`data-clarity-unmask`](https://learn.microsoft.com/en-us/clarity/clarity-api#unmask-your-site-content).

| Syntax | Parameters | Required? |
| --- | --- | --- |
| `data-clarity-mask="true"` | Boolean | Yes |

```
<form action="" method="get" data-clarity-mask="true">
    <label for="GET-name">User Name:</label>
    <input id="GET-name" type="text" name="name">
    <input type="submit" value="Submit">
</form>
```

Suppose you want to ensure that specific data items are sent to Clarity. In that case, you can unmask them by using `data-clarity-unmask`.

Note

Setting `data-clarity-unmask` to false has no effect. To mask content, use [`data-clarity-mask`](https://learn.microsoft.com/en-us/clarity/clarity-api#mask-your-site-content).

| Syntax | Parameters | Required? |
| --- | --- | --- |
| `data-clarity-unmask="true"` | Boolean | Yes |

```
<article class="Movie Review" data-clarity-unmask="true">
    <header>
        <h2>Star Wars</h2>
    </header>
    <section>
        <p>A classic!</p>
    </section>
</article>
```

Clarity keeps up to 100,000 session recordings per project per day. If your project's total volume of sessions exceeds the maximum daily limit, based on your traffic patterns, Clarity starts sampling the recordings it keeps. For example, if your site gets 200,000 sessions in a day, Clarity keeps every other recording.

You can use the `upgrade` API to prioritize specific types of sessions for recording. This is useful if you have sessions with specific types of events (such as clicks) that you want to look at or interactions with specific parts of your website (such as a shopping cart).

| Syntax | Parameters | Required? |
| --- | --- | --- |
| `window.clarity("upgrade", <upgrade reason>)` | Strings | `"upgrade"`: Yes, `<upgrade reason>`: Yes |

`window.clarity("upgrade", "button click")`
