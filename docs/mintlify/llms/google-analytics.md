# Source: https://www.mintlify.com/docs/integrations/analytics/google-analytics.md

> ## Documentation Index
> Fetch the complete documentation index at: https://www.mintlify.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Google Analytics 4

> Track visitor behavior and engagement with Google Analytics.

You will need to generate a new <Tooltip tip="Google Analytics 4">GA4</Tooltip> property to use with Mintlify. The data collected will go into the same project as your other Google Analytics data.

If you are using the old version of Google Analytics, Universal Analytics, you will still be able to generate a <Tooltip tip="Google Analytics 4">GA4</Tooltip> property. <Tooltip tip="Google Analytics 4">GA4</Tooltip> data is slightly different from UA data but still gets collected in the same project.

## How to Connect GA4 to Mintlify

### Create a Web Stream

You will need to create a web stream to get the Measurement ID to put into Mintlify.

Click the cog at the bottom left of the Google Analytics screen. Then click on Data Streams.

<Frame><img src="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/ga4-web-streams.png?fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=3da279b4cbc0f73f3f08e72fa8502b94" alt="Screenshot of the Data Streams page in the Google Analytics dashboard." data-og-width="1400" width="1400" data-og-height="504" height="504" data-path="images/ga4-web-streams.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/ga4-web-streams.png?w=280&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=7ef49476940b7d4fd7d146791a4b67aa 280w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/ga4-web-streams.png?w=560&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=be528e9ba15115da76755acdb8106656 560w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/ga4-web-streams.png?w=840&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=6363c4eb9dc282f60d241327b88a76ba 840w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/ga4-web-streams.png?w=1100&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=e491f72d68f54f2bbeb45e68a1d2c1ce 1100w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/ga4-web-streams.png?w=1650&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=8b3c1dfd2b710c90aef89235918aee2f 1650w, https://mintcdn.com/mintlify/GiucHIlvP3i5L17o/images/ga4-web-streams.png?w=2500&fit=max&auto=format&n=GiucHIlvP3i5L17o&q=85&s=c0786ce67ebb7710d8d1b443269ed279 2500w" /></Frame>

Create a Web Stream and put the URL of your Mintlify docs site as the stream URL.

Your Measurement ID looks like `G-XXXXXXX` and will show up under Stream Details immediately after you create the Web Stream.

### Put Measurement ID in docs.json

Add your Measurement ID to your `docs.json` file like so:

```json docs.json theme={null}
"integrations": {
    "ga4": {
        "measurementId": "G-XXXXXXX"
    }
}
```

### Wait

Google Analytics takes two to three days to show your data.

You can use the [Google Analytics Debugger](https://chrome.google.com/webstore/detail/google-analytics-debugger/jnkmfdileelhofjcijamephohjechhna?hl=en) to check analytics are enabled correctly. The extension will log to your browser's console every time GA4 makes a request.

<Note>
  Preview links have analytics turned off.
</Note>
