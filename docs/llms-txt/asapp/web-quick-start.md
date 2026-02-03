# Source: https://docs.asapp.com/agent-desk/integrations/web-sdk/web-quick-start.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.asapp.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Web Quick Start

If you want to start fast, follow these steps:

1. Embed the Script
2. Initialize the SDK
3. Customize the SDK
4. Authenticate Users

In addition, see an example of a [Full Snippet](#full-snippet "Full Snippet").

## 1. Embed the Script

1. Embed the script directly inline. See the instructions below.
2. Use a tag manager to control where and how the scripts load. The ASAPP Chat SDK works with most tag managers. See the tag manager documentation for more detailed instructions.

To enable the ASAPP Chat SDK, you'll first need to paste the [ASAPP Chat SDK Web snippet](#full-snippet) into your site's HTML. You can place it anywhere in your markup, but it's ideal to place it near the top of the `<head>` element.

```
<script> 
(function(w,d,h,n,s){s=d.createElement('script');w[n]=w[n]||function(){(w[n]._=w[n]._||[]).push(arguments)},w[n].Host=h,s.async=1,s.src=h+'/chat-sdk.js',s.type='text/javascript',d.body.appendChild(s)}(window,document,'https://sdk.asapp.com','ASAPP')); 
</script> 
```

This snippet does two things:

1. Creates a `<script>` element that asynchronously downloads the `https://sdk.asapp.com/chat-sdk.js` JavaScript.
2. Creates a global `ASAPP` function that enables you to interact with [ASAPP's JavaScript API](/agent-desk/integrations/web-sdk/web-javascript-api "Web JavaScript API").

If you're curious, feel free to view the [Full Snippet](#full-snippet "Full Snippet").

## 2. Initialize the SDK

After you [Embed the Script](#1-embed-the-script "1. Embed the Script") into the page, you can start using the [JavaScript API](/agent-desk/integrations/web-sdk/web-javascript-api "Web JavaScript API") to initialize and display the application.

To initialize the ASAPP Chat SDK, call the `ASAPP('load')` method as seen below:

```
     <script> ASAPP('load', { 
     APIHostname: 'API_HOSTNAME', 
     AppId: 'APP_ID' 
}); 
</script> 
```

**Note:** ASAPP will provide the `APIHostname` and `AppId` values to you after coordination between your organization and your ASAPP Implementation Manager. Once ASAPP determines and provides these values, you can make the following updates:

1. Replace `API_HOSTNAME` with the hostname of your ASAPP API location. This string will look something like

   ```screen  theme={null}
   'examplecompanyapi.asapp.com'.
   ```

2. Replace `APP_ID` with your Company Marker identifier. This string will look something like `'examplecompany'`.

Calling `ASAPP('load')` will make a network request to your APIHostname and determine whether or not it should display the Chat SDK Badge. The Badge displays based on your company's business hours, your trigger settings, and whether or not you have enabled the SDK in your Admin control panel.

For more advanced ways to display the ASAPP Chat SDK, see the [JavaScript API Documentation](/agent-desk/integrations/web-sdk/web-javascript-api "Web JavaScript API").

## 3. Customize the SDK

After you  Embed the Script and Initialize the SDK, the ASAPP Chat SDK should display and function on your web page. You may wish to head to the [Customization](/agent-desk/integrations/web-sdk/web-customization "Web Customization") section of the documentation to learn how to customize the appearance of the ASAPP Chat SDK.

## 4. Authenticate Users

Some integrations of the ASAPP Chat SDK allow users to access sensitive account information. If any of your use cases fall under this category, please read the [Authentication](/agent-desk/integrations/web-sdk/web-authentication "Web Authentication") section to ensure your users experience a secure and seamless session.

## Full Snippet

For additional legibility, here's the full Chat SDK Web integration snippet:

```json  theme={null}
(function(win, doc, hostname, namespace, script) {
    script = doc.createElement('script');
    win[namespace] = win[namespace] || function() {
        (win[namespace]._ = win[namespace]._ || []).push(arguments)
    }
    win[namespace].Host = hostname;
    script.async = 1;
    script.src = hostname + '/chat-sdk.js';
    script.type = 'text/javascript';
    doc.body.appendChild(script);
})(window, document, 'https://sdk.asapp.com', 'ASAPP');
```
