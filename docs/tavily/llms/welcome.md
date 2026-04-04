# Source: https://docs.tavily.com/welcome.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.tavily.com/llms.txt
> Use this file to discover all available pages before exploring further.

# null

<div className="w-full bg-white dark:bg-[#0a0a0a] text-black dark:text-white min-h-screen">
  <div className="w-full max-w-screen-xl mx-auto px-6 pt-20 pb-16 text-center">
    <h1 className="font-bold leading-tight mb-4" style={{ fontSize: "3.5rem" }}>
      Build with <span style={{ color: "#78b0a1" }}>Tavily</span>
    </h1>

    <p className="text-gray-600 dark:text-gray-400 text-lg max-w-2xl mx-auto">
      Your journey to state-of-the-art web search starts right here.
    </p>
  </div>

  <div className="w-full max-w-screen-xl mx-auto px-6 mb-16">
    <div className="bg-gray-50 dark:bg-[#1a1a1a] rounded-2xl p-8 border border-gray-200 dark:border-white/10">
      <div className="text-xs font-semibold text-[#78b0a1] mb-4 tracking-wider">
        Installation
      </div>

      <Columns cols={2}>
        <Card title="Python SDK" icon="python">
          ```bash  theme={null}
          pip install tavily-python
          ```
        </Card>

        <Card title="JavaScript SDK" icon="node">
          ```js  theme={null}
          npm i @tavily/core
          ```
        </Card>
      </Columns>

      <div className="text-xs font-semibold text-[#78b0a1] mb-4 mt-4 tracking-wider">
        Try it now
      </div>

      <Tabs className="welcome-tabs mb-3">
        <Tab title="Search the web" icon="search">
          <CodeGroup>
            ```python Python theme={null}
            from tavily import TavilyClient

            tavily_client = TavilyClient(api_key="tvly-YOUR_API_KEY")
            response = tavily_client.search("Who is Leo Messi?")

            print(response)
            ```

            ```javascript JavaScript theme={null}
            const { tavily } = require("@tavily/core");

            const tvly = tavily({ apiKey: "tvly-YOUR_API_KEY" });
            const response = await tvly.search("Who is Leo Messi?");

            console.log(response);
            ```

            ```bash cURL theme={null}
            curl --request POST \
              --url https://api.tavily.com/search \
              --header 'Authorization: Bearer <token>' \
              --header 'Content-Type: application/json' \
              --data '
            {
              "query": "who is Leo Messi?",
              "auto_parameters": false,
              "topic": "general",
              "search_depth": "basic",
              "chunks_per_source": 3,
              "max_results": 1,
              "time_range": null,
              "start_date": "2025-02-09",
              "end_date": "2025-12-29",
              "include_answer": false,
              "include_raw_content": false,
              "include_images": false,
              "include_image_descriptions": false,
              "include_favicon": false,
              "include_domains": [],
              "exclude_domains": [],
              "country": null,
              "include_usage": false
            }
            '
            ```
          </CodeGroup>

          <a href="/documentation/api-reference/endpoint/search" className="welcome-learn-more">
            Learn more about the Search API →
          </a>
        </Tab>

        <Tab title="Extract webpages" icon="file-code">
          <CodeGroup>
            ```python Python theme={null}
            from tavily import TavilyClient

            tavily_client = TavilyClient(api_key="tvly-YOUR_API_KEY")
            response = tavily_client.extract("https://en.wikipedia.org/wiki/Artificial_intelligence")

            print(response)
            ```

            ```javascript JavaScript theme={null}
            const { tavily } = require("@tavily/core");

            const tvly = tavily({ apiKey: "tvly-YOUR_API_KEY" });
            const response = await tvly.extract("https://en.wikipedia.org/wiki/Artificial_intelligence");

            console.log(response);
            ```

            ```bash cURL theme={null}
            curl --request POST \
              --url https://api.tavily.com/extract \
              --header 'Authorization: Bearer <token>' \
              --header 'Content-Type: application/json' \
              --data '
            {
              "urls": "https://en.wikipedia.org/wiki/Artificial_intelligence",
              "query": "<string>",
              "chunks_per_source": 3,
              "extract_depth": "basic",
              "include_images": false,
              "include_favicon": false,
              "format": "markdown",
              "timeout": "None",
              "include_usage": false
            }
            '
            ```
          </CodeGroup>

          <a href="/documentation/api-reference/endpoint/extract" className="welcome-learn-more">
            Learn more about the Extract API →
          </a>
        </Tab>

        <Tab title="Crawl webpages" icon="spider">
          <CodeGroup>
            ```python Python theme={null}
            from tavily import TavilyClient

            tavily_client = TavilyClient(api_key="tvly-YOUR_API_KEY")
            response = tavily_client.crawl("https://docs.tavily.com", instructions="Find all pages on the Python SDK")

            print(response)
            ```

            ```javascript JavaScript theme={null}
            const { tavily } = require("@tavily/core");

            const tvly = tavily({ apiKey: "tvly-YOUR_API_KEY" });
            const response = await tvly.crawl("https://docs.tavily.com", { instructions: "Find all pages on the Python SDK" });

            console.log(response);
            ```

            ```bash cURL theme={null}
            curl --request POST \
              --url https://api.tavily.com/crawl \
              --header 'Authorization: Bearer <token>' \
              --header 'Content-Type: application/json' \
              --data '
            {
              "url": "docs.tavily.com",
              "instructions": "Find all pages about the Python SDK",
              "chunks_per_source": 3,
              "max_depth": 1,
              "max_breadth": 20,
              "limit": 50,
              "select_paths": null,
              "select_domains": null,
              "exclude_paths": null,
              "exclude_domains": null,
              "allow_external": true,
              "include_images": false,
              "extract_depth": "basic",
              "format": "markdown",
              "include_favicon": false,
              "timeout": 150,
              "include_usage": false
            }
            '
            ```
          </CodeGroup>

          <a href="/documentation/api-reference/endpoint/crawl" className="welcome-learn-more">
            Learn more about the Crawl API →
          </a>
        </Tab>

        <Tab title="Map webpages" icon="map">
          <CodeGroup>
            ```python Python theme={null}
            from tavily import TavilyClient

            tavily_client = TavilyClient(api_key="tvly-YOUR_API_KEY")
            response = tavily_client.map("https://docs.tavily.com")

            print(response)
            ```

            ```javascript JavaScript theme={null}
            const { tavily } = require("@tavily/core");

            const tvly = tavily({ apiKey: "tvly-YOUR_API_KEY" });
            const response = await tvly.map("https://docs.tavily.com");

            console.log(response);
            ```

            ```bash cURL theme={null}
            curl --request POST \
              --url https://api.tavily.com/map \
              --header 'Authorization: Bearer <token>' \
              --header 'Content-Type: application/json' \
              --data '
            {
              "url": "docs.tavily.com",
              "instructions": "Find all pages about the Python SDK",
              "max_depth": 1,
              "max_breadth": 20,
              "limit": 50,
              "select_paths": null,
              "select_domains": null,
              "exclude_paths": null,
              "exclude_domains": null,
              "allow_external": true,
              "timeout": 150,
              "include_usage": false
            }
            '
            ```
          </CodeGroup>

          <a href="/documentation/api-reference/endpoint/map" className="welcome-learn-more">
            Learn more about the Map API →
          </a>
        </Tab>

        <Tab title="Create Research Task" icon="book">
          <CodeGroup>
            ```python Python theme={null}
            from tavily import TavilyClient

            tavily_client = TavilyClient(api_key="tvly-YOUR_API_KEY")
            response = tavily_client.research("What are the latest developments in AI?")

            print(response)
            ```

            ```javascript JavaScript theme={null}
            const { tavily } = require("@tavily/core");

            const tvly = tavily({ apiKey: "tvly-YOUR_API_KEY" });
            const response = await tvly.research("What are the latest developments in AI?");

            console.log(response);
            ```

            ```bash cURL theme={null}
            curl --request POST \
              --url https://api.tavily.com/research \
              --header 'Authorization: Bearer <token>' \
              --header 'Content-Type: application/json' \
              --data '
            {
              "input": "What are the latest developments in AI?",
              "model": "auto",
              "stream": false,
              "output_schema": {
                "properties": {
                  "company": {
                    "type": "string",
                    "description": "The name of the company"
                  },
                  "key_metrics": {
                    "type": "array",
                    "description": "List of key performance metrics",
                    "items": {
                      "type": "string"
                    }
                  },
                  "financial_details": {
                    "type": "object",
                    "description": "Detailed financial breakdown",
                    "properties": {
                      "operating_income": {
                        "type": "number",
                        "description": "Operating income for the period"
                      }
                    }
                  }
                },
                "required": [
                  "company"
                ]
              },
              "citation_format": "numbered"
            }
            '
            ```
          </CodeGroup>

          <a href="/documentation/api-reference/endpoint/research" className="welcome-learn-more">
            Learn more about the Research API →
          </a>
        </Tab>
      </Tabs>
    </div>
  </div>

  {" "}

  <div className="w-full max-w-screen-xl mx-auto px-2 lg:px-6 mt-16 mb-6">
    <div className="h-px w-full bg-gray-300 dark:bg-gray-700/60" />

    <h3 className="text-xl font-semibold text-black dark:text-white mt-6">
      Developer Resources
    </h3>
  </div>

  {" "}

  <div className="w-full max-w-screen-xl mx-auto px-2 lg:px-6 mb-20">
    <CardGroup cols={3}>
      <Card title="API Credits Overview" icon="book-open" href="/documentation/api-credits">
        Learn how Tavily API credits work.
      </Card>

      <Card title="Rate Limits" icon="gauge" href="/documentation/rate-limits">
        Understand Tavily's rate limits and policies.
      </Card>

      <Card title="Playground" icon="play" href="https://app.tavily.com/playground">
        Try Tavily's APIs interactively.
      </Card>
    </CardGroup>
  </div>
</div>

<div className="w-full max-w-screen-xl mx-auto px-2 lg:px-6 mt-16 mb-8">
  <div className="flex flex-col gap-3 text-xs text-gray-700 dark:text-gray-50 mt-6 mb-6">
    <div className="flex items-center gap-2 leading-none">
      <Icon icon="circle-question" size={12} className="shrink-0" />

      <span className="flex items-center gap-1">
        <span>Question?</span>

        <a href="mailto:support@tavily.com" className="text-[#78b0a1] hover:underline underline-offset-2">
          Contact Us
        </a>
      </span>
    </div>

    <div className="flex items-center gap-2 leading-none">
      <Icon icon="discourse" size={12} className="shrink-0" />

      <span className="flex items-center gap-1">
        <span>Integration issues?</span>

        <a href="https://community.tavily.com/" target="_blank" rel="noopener noreferrer" className="text-[#78b0a1] hover:underline underline-offset-2">
          Join Community
        </a>
      </span>
    </div>

    <div className="flex items-center gap-2 leading-none">
      <Icon icon="sparkles" size={12} className="shrink-0" />

      <span className="flex items-center gap-1">
        <span>Using LLMs?</span>

        <a href="/llms.txt" className="text-[#78b0a1] hover:underline underline-offset-2">
          Read LLMs.txt
        </a>
      </span>
    </div>

    <div className="flex items-center gap-2 leading-none">
      <Icon icon="circle-check" size={12} className="shrink-0" />

      <span className="flex items-center gap-1">
        <span>Something not right?</span>

        <a href="https://status.tavily.com/" target="_blank" rel="noopener noreferrer" className="text-[#78b0a1] hover:underline underline-offset-2">
          Check Status
        </a>
      </span>
    </div>
  </div>

  <div className="h-px w-full bg-gray-300 dark:bg-gray-700/60 mb-2" />

  <div className="relative z-10 pointer-events-auto">
    <div className="max-w-screen-xl mx-auto py-1">
      <div className="flex flex-col sm:flex-row items-center justify-between gap-4 text-xs text-gray-600 dark:text-gray-300">
        <div className="flex flex-wrap items-center gap-x-2 gap-y-1">
          <span>© Tavily</span>

          <a href="https://www.tavily.com/privacy" target="_blank" rel="noopener noreferrer" className="hover:text-black dark:hover:text-white hover:underline underline-offset-2">
            Privacy Policy
          </a>

          <span className="opacity-60">·</span>

          <a href="https://www.tavily.com/website-terms" target="_blank" rel="noopener noreferrer" className="hover:text-black dark:hover:text-white hover:underline underline-offset-2">
            Website Terms of Use
          </a>

          <span className="opacity-60">·</span>

          <a href="https://www.tavily.com/terms" target="_blank" rel="noopener noreferrer" className="hover:text-black dark:hover:text-white hover:underline underline-offset-2">
            Platform Terms of Use
          </a>

          <span className="opacity-60">·</span>

          <a href="https://www.tavily.com/cookie-policy" target="_blank" rel="noopener noreferrer" className="hover:text-black dark:hover:text-white hover:underline underline-offset-2">
            Cookie Policy
          </a>
        </div>

        <div className="flex items-center gap-4 footer-social-icons">
          <a href="https://www.linkedin.com/company/tavily" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn">
            <Icon icon="linkedin" size={14} />
          </a>

          <a href="https://x.com/tavilyai" target="_blank" rel="noopener noreferrer" aria-label="Twitter">
            <Icon icon="twitter" size={14} />
          </a>

          <a href="https://github.com/tavily-ai" target="_blank" rel="noopener noreferrer" aria-label="GitHub">
            <Icon icon="github" size={14} />
          </a>

          <a href="https://www.youtube.com/@TavilyAI" target="_blank" rel="noopener noreferrer" aria-label="YouTube">
            <Icon icon="youtube" size={14} />
          </a>
        </div>
      </div>
    </div>
  </div>
</div>
