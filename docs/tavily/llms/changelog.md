# Source: https://docs.tavily.com/changelog.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavily.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Changelog

<AccordionGroup>
  <Accordion title="Project tracking with X-Project-ID header" icon="rocket" description="January 2026">
    <b><br />Track API usage by project with the new <code>X-Project-ID</code> header</b><br />

    <ul>
      <li>
        You can now attach a Project ID to your API requests to organize and track usage by project. This is useful when a single API key is used across multiple projects or applications.
      </li>

      <li>
        <b>HTTP Header:</b> Add <code>X-Project-ID: your-project-id</code> to any API request
      </li>

      <li>
        <b>Python SDK:</b> Pass <code>project\_id="your-project-id"</code> when instantiating the client, or set the <code>TAVILY\_PROJECT</code> environment variable
      </li>

      <li>
        <b>JavaScript SDK:</b> Pass <code>projectId: "your-project-id"</code> when instantiating the client, or set the <code>TAVILY\_PROJECT</code> environment variable
      </li>

      <li>
        An API key can be associated with multiple projects
      </li>

      <li>
        Filter requests by project in the <a href="/documentation/api-reference/endpoint/usage">/logs endpoint</a> and platform usage dashboard to keep track of where requests originate from
      </li>
    </ul>
  </Accordion>

  <Accordion title="New search_depth options fast and ultra-fast (BETA)" icon="rocket" description="December 2025">
    <b><br /><a href="/documentation/api-reference/endpoint/search#body-search-depth"><code>search\_depth</code> parameter</a> - New options: <code>fast</code> and <code>ultra-fast</code></b><br />

    <ul>
      <li>
        <b><code>fast</code> (BETA)</b><br />

        <ul>
          <li>Optimized for low latency while maintaining high relevance to the user query</li>
          <li><b>Cost:</b> 1 API Credit</li>
        </ul>
      </li>

      <li>
        <b><code>ultra-fast</code> (BETA)</b><br />

        <ul>
          <li>Optimized strictly for latency</li>
          <li><b>Cost:</b> 1 API Credit</li>
        </ul>
      </li>
    </ul>
  </Accordion>

  <Accordion title="Intent Based Extraction" icon="rocket" description="December 2025">
    <b><br /><a href="/documentation/api-reference/endpoint/extract#body-query"><code>query</code></a> and <a href="/documentation/api-reference/endpoint/extract#body-chunks-per-source"><code>chunks\_per\_source</code></a> parameters for Extract and Crawl</b><br />

    <ul>
      <li>
        <b><code>query</code> (Extract)</b><br />

        <ul>
          <li><b>Type:</b> <code>string</code></li>
          <li>User intent for reranking extracted content chunks. When provided, chunks are reranked based on relevance to this query.</li>
        </ul>
      </li>

      <li>
        <b><code>chunks\_per\_source</code> (Extract & Crawl)</b><br />

        <ul>
          <li><b>Type:</b> <code>integer</code></li>
          <li><b>Range:</b> 1 to 5</li>
          <li><b>Default:</b> 3</li>
          <li>Chunks are short content snippets (maximum 500 characters each) pulled directly from the source.</li>
          <li>Use <code>chunks\_per\_source</code> to define the maximum number of relevant chunks returned per source and to control the <code>raw\_content</code> length.</li>
          <li>Chunks will appear in the <code>raw\_content</code> field as: <code>\<chunk 1> \[...] \<chunk 2> \[...] \<chunk 3></code>.</li>
          <li>Available only when <code>query</code> is provided (Extract) or <code>instructions</code> are provided (Crawl).</li>
        </ul>
      </li>
    </ul>
  </Accordion>

  <Accordion title="Include usage parameter" icon="rocket" description="December 2025">
    <b><br /><a href="/documentation/api-reference/endpoint/search#body-include-usage"><code>include\_usage</code> parameter</a></b><br />

    <ul>
      <li>
        You can now include credit usage information in the API response for the <a href="/documentation/api-reference/endpoint/search#body-include-usage">Search</a>, <a href="/documentation/api-reference/endpoint/extract#body-include-usage">Extract</a>, <a href="/documentation/api-reference/endpoint/crawl#body-include-usage">Crawl</a>, and <a href="/documentation/api-reference/endpoint/map#body-include-usage">Map</a> endpoints.
      </li>

      <li>
        Set the <code>include\_usage</code> parameter to <code>true</code> to receive credit usage information in the API response.
      </li>

      <li>
        <b>Type:</b> <code>boolean</code>
      </li>

      <li>
        <b>Default:</b> <code>false</code>
      </li>

      <li>
        When enabled, the response includes a <code>usage</code> object with <code>credits</code> information, making it easy to track API credit consumption for each request.
      </li>

      <li>
        <b>Note:</b> The value may be 0 if the total successful calls have not yet reached the minimum threshold. See our <a href="/documentation/api-credits">Credits & Pricing documentation</a> for details.
      </li>
    </ul>
  </Accordion>

  <Accordion title="Vercel AI SDK v5 integration" icon="rocket" description="November 2025">
    <b><br /><a href="/documentation/integrations/vercel">Tavily is now integrated with Vercel AI SDK v5</a></b><br />

    <ul>
      <li>
        We've released a new <a href="https://www.npmjs.com/package/@tavily/ai-sdk" target="_blank"><code>@tavily/ai-sdk</code></a> package that provides pre-built AI SDK tools for Vercel's AI SDK v5.
      </li>

      <li>
        Easily add real-time web search, content extraction, intelligent crawling, and site mapping to your AI SDK project with ready-to-use tools.
      </li>

      <li>
        <b>Available Tools:</b> <code>tavilySearch</code>, <code>tavilyExtract</code>, <code>tavilyCrawl</code>, and <code>tavilyMap</code>
      </li>

      <li>
        Full TypeScript support with proper type definitions and seamless integration with Vercel AI SDK v5.
      </li>

      <li>
        Check out our <a href="/documentation/integrations/vercel"> integration guide</a> to get started.
      </li>
    </ul>
  </Accordion>

  <Accordion title="Crawl & Map timeout parameter" icon="rocket" description="November 2025">
    <b><br /><a href="/documentation/api-reference/endpoint/crawl#body-timeout"><code>timeout</code> parameter for Crawl</a> and <a href="/documentation/api-reference/endpoint/map#body-timeout"><code>timeout</code> parameter for Map</a></b><br />

    <ul>
      <li>
        You can now specify a custom timeout for the <a href="/documentation/api-reference/endpoint/crawl">Crawl</a> and <a href="/documentation/api-reference/endpoint/map">Map</a> endpoints to control how long to wait for the operation before timing out.
      </li>

      <li>
        <b>Type:</b> <code>float</code>
      </li>

      <li>
        <b>Range:</b> Between 10 and 150 seconds
      </li>

      <li>
        <b>Default:</b> 150 seconds
      </li>

      <li>
        This gives you fine-grained control over crawl and map operation timeouts, allowing you to balance between reliability and speed based on your specific use case.
      </li>
    </ul>
  </Accordion>

  <Accordion title="New team roles & permissions" icon="rocket" description="August 2025">
    <p /><b>Role options: Owner, Admin, Member</b>
    <p />You can now assign roles to team members, giving you more control over access and permissions. Each team has one owner, while there can be multiple admins and multiple members.
    The key distinction between roles is in their permissions for Billing and Settings:<p />

    <ul>
      <li>
        <b>Owner</b><br />

        <ul>
          <li>Full access to all Settings</li>
          <li>Access and ownership of the Billing account</li>
        </ul>
      </li>

      <li>
        <b>Admin</b><br />

        <ul>
          <li>Full access to Settings except ownership transfer</li>
          <li>No access to Billing</li>
        </ul>
      </li>

      <li>
        <b>Member</b><br />

        <ul>
          <li>Limited Settings access (view members only)</li>
          <li>No access to Billing</li>
        </ul>
      </li>
    </ul>
  </Accordion>

  <Accordion title="Extract timeout parameter" icon="rocket" description="August 2025">
    <b><br /><a href="/documentation/api-reference/endpoint/extract#body-timeout"><code>timeout</code> parameter</a></b><br />

    <ul>
      <li>
        You can now specify a custom timeout for the <a href="/documentation/api-reference/endpoint/extract">Extract</a> endpoint to control how long to wait for URL extraction before timing out.
      </li>

      <li>
        <b>Type:</b> <code>number</code> (float)
      </li>

      <li>
        <b>Range:</b> Between 1.0 and 60.0 seconds
      </li>

      <li>
        <b>Default behavior:</b> If not specified, automatic timeouts are applied based on <code>extract\_depth</code>: 10 seconds for basic extraction and 30 seconds for advanced extraction.
      </li>

      <li>
        This gives you fine-grained control over extraction timeouts, allowing you to balance between reliability and speed based on your specific use case.
      </li>
    </ul>
  </Accordion>

  <Accordion title="Start date & end date Parameters" icon="rocket" description="July 2025">
    <b><br /><a href="/documentation/api-reference/endpoint/search#body-start_date"><code>start\_date</code> parameter</a>,<a href="/documentation/api-reference/endpoint/search#body-end-date"><code>end\_date</code> parameter</a></b><br />

    <ul>
      <li>
        You can now use both the <code>start\_date</code> and <code>end\_date</code> parameters in the <a href="/documentation/api-reference/endpoint/search">Search</a> endpoints.
      </li>

      <li>
        <code>start\_date</code> will return all results after the specified start date. Required to be written in the format YYYY-MM-DD.
      </li>

      <li>
        <code>end\_date</code> will return all results before the specified end date. Required to be written in the format YYYY-MM-DD.
      </li>

      <li>
        Set <code>start\_date</code> to <code>2025-01-01</code> and <code>end\_date</code> to <code>2025-04-01</code> to reiceive results strictly from this time range.
      </li>
    </ul>
  </Accordion>

  <Accordion title="Usage dashboard" icon="rocket" description="July 2025">
    <b><br /><a href="https://www.tavily.com/">Login to your account to view the usage dashboard</a></b><br />
    <br />The usage dashboard provides the following features to paid users/teams:<br />

    <ul>
      <li>
        The Usage Graph offers a breakdown of daily usage across all Tavily endpoints with historical data to enable month over month usage and spend comparison.
      </li>

      <li>
        The Logs Table offers granular insight into each API request to ensure visibility and traceability with every Tavily interaction.
      </li>
    </ul>
  </Accordion>

  <Accordion title="Include favicon parameter" icon="rocket" description="June 2025">
    <b><br /><a href="/documentation/api-reference/endpoint/search#body-include-favicon"><code>include\_favicon</code> parameter</a></b><br />

    <ul>
      <li>
        You can now include the favicon URL for each result in the <a href="/documentation/api-reference/endpoint/search">Search</a>, <a href="/documentation/api-reference/endpoint/extract">Extract</a>, and <a href="/documentation/api-reference/endpoint/crawl">Crawl</a> endpoints.
      </li>

      <li>
        Set the <code>include\_favicon</code> parameter to <code>true</code> to receive the favicon URL (if available) for each result in the API response.
      </li>

      <li>
        This makes it easy to display website icons alongside your search, extraction, or crawl results, improving the visual context and user experience in your application.
      </li>
    </ul>
  </Accordion>

  <Accordion title="Auto parameters" icon="rocket" description="June 2025">
    <b>Tavily Search<br /><a href="/documentation/api-reference/endpoint/search#body-auto-parameters"><code>auto\_parameters</code></a></b><br />

    <ul>
      <li><b>Boolean default:</b> <code>false</code></li>
      <li>When <code>auto\_parameters</code> is enabled, Tavily automatically configures search parameters based on your query's content and intent. You can still set other parameters manually, and your explicit values will override the automatic ones.</li>
      <li>The parameters <code>include\_answer</code>, <code>include\_raw\_content</code>, and <code>max\_results</code> must always be set manually, as they directly affect response size.</li>
      <li><b>Note:</b> <code>search\_depth</code> may be automatically set to <code>advanced</code> when it's likely to improve results. This uses <b>2 API credits per request</b>. To avoid the extra cost, you can explicitly set <code>search\_depth</code> to <code>basic</code>.</li>
    </ul>
  </Accordion>

  <Accordion title="Usage endpoint" icon="rocket" description="May 2025">
    <b><a href="/documentation/api-reference/endpoint/usage"><code>/usage</code> endpoint</a></b><br />

    <ul>
      <b>Easily check your API usage and plan limits.</b><br />Just <code>GET [https://api.tavily.com/usage](https://api.tavily.com/usage)</code> with your API key to monitor your account in real time.
    </ul>
  </Accordion>

  <Accordion title="Country parameter" icon="rocket" description="May 2025">
    <b>Tavily Search<br /><a href="/documentation/api-reference/endpoint/search#body-country"><code>country</code> parameter</a><br /><p>Boost search results from a specific country.</p></b>

    <ul>
      This will prioritize content from the selected country in the search results. Available only if <code>topic</code> is <code>general</code>.
    </ul>
  </Accordion>

  <Accordion title="Make & n8n integrations" icon="rocket" description="May 2025">
    <b>Make & n8n Integrations</b><br />

    <ul>
      <li>
        <b><a href="/documentation/integrations/n8n">Tavily is now available for no-code integration through n8n.</a></b><br />
        <p>Integrate Tavily with n8n to enhance your workflows with real-time web search and content extraction—without writing code. With Tavily's powerful search and extraction capabilities, you can seamlessly integrate up-to-date online information into your n8n automations.</p>
      </li>

      <li>
        <b><a href="/documentation/integrations/make">Integrate Tavily with Make without writing a single line of code.</a></b><br />
        <p>With Tavily's powerful search and content extraction capabilities, you can seamlessly integrate real-time online information into your Make workflows and automations.</p>
      </li>
    </ul>
  </Accordion>

  <Accordion title="Markdown format" icon="rocket" description="May 2025">
    <b>Tavily Extract<br /><a href="/documentation/api-reference/endpoint/extract#body-format"><code>format</code> parameter</a></b>

    <ul>
      <li><b>Type:</b> <code>enum\<string></code></li>
      <li><b>Default:</b> <code>markdown</code></li>
      <li>The format of the extracted web page content. <code>markdown</code> returns content in markdown format. <code>text</code> returns plain text and may increase latency.</li>
      <li><b>Available options:</b> <code>markdown</code>, <code>text</code></li>
    </ul>
  </Accordion>

  <Accordion title="Advanced search & chunks per source" icon="rocket" description="April 2025">
    <b>Tavily Search<br /><a href="/documentation/api-reference/endpoint/search#body-search-depth"><code>search\_depth</code></a> and <a href="/documentation/api-reference/endpoint/search#body-chunks-per-source"><code>chunks\_per\_source</code></a>parameters</b>

    <ul>
      <li>
        <b><code>search\_depth</code></b><br />

        <div>
          <ul>
            <li><b>Type:</b> <code>enum\<string></code></li>
            <li><b>Default:</b> <code>basic</code></li>
            <li>The depth of the search. <code>advanced</code> search is tailored to retrieve the most relevant sources and content snippets for your query, while <code>basic</code> search provides generic content snippets from each source.</li>
            <li>A <code>basic</code> search costs 1 API Credit, while an <code>advanced</code> search costs 2 API Credits.</li>
            <li><b>Available options:</b> <code>basic</code>, <code>advanced</code></li>
          </ul>
        </div>
      </li>

      <li>
        <b><code>chunks\_per\_source</code></b><br />

        <div>
          <ul>
            <li>Chunks are short content snippets (maximum 500 characters each) pulled directly from the source.</li>
            <li>Use <code>chunks\_per\_source</code> to define the maximum number of relevant chunks returned per source and to control the content length.</li>
            <li>Chunks will appear in the content field as: <code>\<chunk 1> \[...] \<chunk 2> \[...] \<chunk 3></code>.</li>
            <li>Available only when <code>search\_depth</code> is <code>advanced</code>.</li>
            <li><b>Required range:</b> <code>1 \< x \< 3</code></li>
          </ul>
        </div>
      </li>
    </ul>
  </Accordion>

  <Accordion title="Tavily crawl (BETA)" icon="rocket" description="April 2025">
    <a href="https://docs.tavily.com/documentation/api-reference/endpoint/crawl">Tavily Crawl</a><br />

    <ul>
      <li>
        Tavily Crawl enables you to traverse a website like a graph, starting from a base URL and automatically discovering and extracting content from multiple linked pages. With Tavily Crawl, you can:

        <ul>
          <li>Specify the starting URL and let the crawler intelligently follow links to map out the site structure.</li>
          <li>Control the depth and breadth of the crawl, allowing you to focus on specific sections or perform comprehensive site-wide analysis.</li>
          <li>Apply filters and custom instructions to target only the most relevant pages or content types.</li>
          <li>Aggregate extracted content for further analysis, reporting, or integration into your workflows.</li>
          <li>Seamlessly integrate with your automation tools or use the API directly for flexible, programmatic access.</li>
        </ul>

        Tavily Crawl is ideal for use cases such as large-scale content aggregation, competitive research, knowledge base creation, and more.<br />
        For full details and API usage examples, see the <a href="https://docs.tavily.com/documentation/api-reference/endpoint/crawl" target="_blank">Tavily Crawl API reference</a>.
      </li>
    </ul>
  </Accordion>
</AccordionGroup>
