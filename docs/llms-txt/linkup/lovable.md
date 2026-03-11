# Source: https://docs.linkup.so/pages/integrations/lovable/lovable.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.linkup.so/llms.txt
> Use this file to discover all available pages before exploring further.

# Lovable

> How to use Linkup with Lovable

## Overview

This guide will show you how to integrate Linkup API into your Lovable applications, whether you're starting from scratch or adding Linkup to an existing app.

## Integration Steps

<Steps>
  <Step title="Access your Lovable account">
    Log in to your Lovable account at [lovable.dev](https://lovable.dev).
  </Step>

  <Step title="Get your Linkup API Key">
    <Card title="Get your API key" icon="key" href="https://app.linkup.so" horizontal="True">
      Create a Linkup account for free to get your API key.
    </Card>
  </Step>

  <Step title="Add Linkup to Your Lovable App">
    <Frame>
            <img src="https://mintcdn.com/linkup-8b5c238e/ht3XJF6azWwbELaV/pages/integrations/lovable/assets/lovable-chatbot.png?fit=max&auto=format&n=ht3XJF6azWwbELaV&q=85&s=f4a0dcb15126f8f07ab0547f263812cf" alt="Lovable Chatbot Interface" width="1020" height="514" data-path="pages/integrations/lovable/assets/lovable-chatbot.png" />
    </Frame>

    In your Lovable chatbot window, use the prompt below:

    ```bash  theme={null}
    # Install the Linkup SDK
    npm i linkup-sdk

    # Import and initialize the client
    import { LinkupClient } from 'linkup-sdk';

    const client = new LinkupClient({
      apiKey: '<YOUR API KEY>', # your api key here
    });

    # Create the search function
    const askLinkup = async () => {
      return await client.search({
        query: "Your Query here",
        depth: 'standard', # "standard" or "deep"
        outputType: 'sourcedAnswer',
      });
    };

    # Call the function
    askLinkup().then(console.log);
    ```

    <Info>
      <table>
        <thead>
          <tr>
            <th style={{ color: '#FFFFFF' }}>Parameter</th>
            <th style={{ color: '#FFFFFF' }}>Options</th>
            <th style={{ color: '#FFFFFF' }}>Description</th>
          </tr>
        </thead>

        <tbody>
          <tr>
            <td><code>depth</code></td>
            <td><code>standard</code>, <code>deep</code></td>
            <td>Controls search depth. <code>deep</code> performs more thorough research, <code>standard</code> is faster.</td>
          </tr>

          <tr>
            <td><code>output\_type</code></td>
            <td><code>searchResults</code>, <code>sourcedAnswer</code>, <code>structured</code></td>
            <td>Determines the format of returned information.</td>
          </tr>
        </tbody>
      </table>
    </Info>
  </Step>

  <Step title="Start Building Your Web-Connected App">
    Now that you have Linkup integrated with Lovable, you can start building applications that have access to the entire web. Your Lovable app can now:

    * Search and retrieve real-time information from across the web
    * Provide up-to-date answers with source citations
    * Access and analyze web content to enhance user interactions

    Start by testing your integration with a simple query, then expand your application's capabilities using the advanced configuration options below.
  </Step>
</Steps>

For advanced configuration like including images, date filtering and supported output types,
check <a href="/pages/sdk/js/js#input-parameters" target="_blank" rel="noopener noreferrer"> configuration parameters </a>.

## Best Practices

1. **API Key Security**: Never expose your API key in client-side code. Use environment variables or secure backend storage.

2. **Error Handling**: Implement proper error handling for API calls:

```javascript  theme={null}
const askLinkup = async () => {
  try {
    const result = await client.search({
      query: "Your query here",
      depth: 'deep',
      outputType: 'sourcedAnswer',
    });
    return result;
  } catch (error) {
    console.error('Error fetching data from Linkup:', error);
    // Handle error appropriately
  }
};
```

3. **Rate Limiting**: Be mindful of API rate limits and implement appropriate caching strategies if needed.

## Next Steps

* Check out [Lovable documentation](https://docs.lovable.dev) to enhance your Lovable application
* Join our [Discord community](https://discord.com/invite/9q9mCYJa86) for support and updates

<Info>
  Facing issues? Reach out to our engineering team at [support@linkup.so](mailto:support@linkup.so) or via our [Discord](https://discord.com/invite/9q9mCYJa86) or [book a 15 minutes call](https://calendar.app.google/tEzK3mMKyLyp5Hsv9) with a member of our technical team.
</Info>


Built with [Mintlify](https://mintlify.com).