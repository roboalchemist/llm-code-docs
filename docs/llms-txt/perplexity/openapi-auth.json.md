# Source: https://docs.perplexity.ai/openapi-auth.json

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.perplexity.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Overview

export const PerplexityLogo = () => {
  return <div className="relative w-[300px] sm:w-[350px] h-[30px] sm:h-[35px] overflow-visible">
      <img src="/logo/Perplexity_API_Platform.svg" alt="Perplexity API Platform" className="block dark:hidden w-full h-full object-contain object-left rounded-none pointer-events-none" />
      <img src="/logo/Perplexity_API_Platform_Light.svg" alt="Perplexity API Platform" className="hidden dark:block w-full h-full object-contain object-left rounded-none pointer-events-none" />
    </div>;
};

export const QuickstartBanner = () => <div className="flex flex-col sm:flex-row sm:items-center sm:justify-between bg-[#1a6872] border border-border rounded-xl p-4 md:p-6 w-full mt-4 mb-8 gap-4">
    <div className="flex items-center gap-3 sm:gap-4 flex-1">
      <div className="flex flex-col min-w-0">
        <span className="font-semibold text-base md:text-lg text-[#F7F7F8]">Quickstart Guide</span>
        <span className="text-[14px] text-[#F7F7F8] opacity-80 mt-0.5 leading-[140%] tracking-[-0.02em] font-light">Getting started is simple and fast—make your first API call within minutes.</span>
      </div>
    </div>
    <div className="flex flex-col sm:flex-row gap-2 sm:ml-4">
      <a href="/docs/getting-started/quickstart" className="px-6 py-3 bg-[#35BDC8] hover:bg-[#92DCE2] text-[#121516] rounded-full font-medium text-[14px] shadow transition-all duration-200 whitespace-nowrap text-center">
        Get Started
      </a>
      <a href="https://console.perplexity.ai" className="px-6 py-3 bg-[#35BDC8] hover:bg-[#92DCE2] text-[#121516] rounded-full font-medium text-[14px] shadow transition-all duration-200 whitespace-nowrap text-center">
        Get Your API Key
      </a>
    </div>
  </div>;

export const UseCaseTabs = () => {
  const [selected, setSelected] = useState(0);
  const useCases = [{
    label: 'Search The Web',
    codeExamples: [{
      language: 'bash',
      code: `curl https://api.perplexity.ai/search \\
  -H "Authorization: Bearer $PERPLEXITY_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{
    "query": [
      "What is Comet Browser?",
      "Perplexity AI",
      "Perplexity Changelog"
    ]
  }' | jq`
    }, {
      language: 'python',
      code: `from perplexity import Perplexity

client = Perplexity()

search = client.search.create(
    query=[
      "What is Comet Browser?",
      "Perplexity AI",
      "Perplexity Changelog"
    ]
)

for result in search.results:
    print(f"{result.title}: {result.url}")`
    }, {
      language: 'typescript',
      code: `import Perplexity from '@perplexity-ai/perplexity_ai';

const client = new Perplexity();

const search = await client.search.create({
  query: [
    "What is Comet Browser?",
    "Perplexity AI",
    "Perplexity Changelog"
  ]
});

search.results.forEach(result => {
  console.log(\`\${result.title}: \${result.url}\`);
});`
    }]
  }, {
    label: 'Use Any Frontier Model',
    codeExamples: [{
      language: 'bash',
      code: `curl https://api.perplexity.ai/v1/agent \\
  -H "Authorization: Bearer $PERPLEXITY_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{
    "model": "openai/gpt-5.4",
    "input": "What are the major AI developments and announcements from today across the tech industry?"
  }' | jq`
    }, {
      language: 'python',
      code: `from perplexity import Perplexity

client = Perplexity()

response = client.responses.create(
    model="openai/gpt-5.4",
    input="What are the major AI developments and announcements from today across the tech industry?"
)

print(response.output_text)`
    }, {
      language: 'javascript',
      code: `import Perplexity from '@perplexity-ai/perplexity_ai';

const client = new Perplexity();

const response = await client.responses.create({
  model: 'openai/gpt-5.2',
  input: 'What are the major AI developments and announcements from today across the tech industry?'
});

console.log(response.output_text);`
    }]
  }, {
    label: 'Filter your sources',
    codeExamples: [{
      language: 'bash',
      code: `curl https://api.perplexity.ai/v1/agent \\
  -H "Authorization: Bearer $PERPLEXITY_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{
    "model": "openai/gpt-5.4",
    "input": "What are the most promising machine learning breakthroughs in computer vision and multimodal AI from recent arXiv publications?",
    "tools": [
      {
        "type": "web_search",
        "filters": {
          "search_domain_filter": ["arxiv.org"],
          "search_recency_filter": "month"
        }
      }
    ],
    "instructions": "You have access to a web_search tool. Use it for current information."
  }' | jq`
    }, {
      language: 'python',
      code: `from perplexity import Perplexity

client = Perplexity()

response = client.responses.create(
    model="openai/gpt-5.4",
    input="What are the most promising machine learning breakthroughs in computer vision and multimodal AI from recent arXiv publications?",
    tools=[
        {
            "type": "web_search",
            "filters": {
                "search_domain_filter": ["arxiv.org"],
                "search_recency_filter": "month"
            }
        }
    ],
    instructions="You have access to a web_search tool. Use it for current information."
)

print(response.output_text)`
    }, {
      language: 'javascript',
      code: `import Perplexity from '@perplexity-ai/perplexity_ai';

const client = new Perplexity();

const response = await client.responses.create({
  model: 'openai/gpt-5.2',
  input: 'What are the most promising machine learning breakthroughs in computer vision and multimodal AI from recent arXiv publications?',
  tools: [
    {
      type: 'web_search',
      filters: {
        search_domain_filter: ['arxiv.org'],
        search_recency_filter: 'month'
      }
    }
  ],
  instructions: 'You have access to a web_search tool. Use it for current information.'
});

console.log(response.output_text);`
    }]
  }, {
    label: 'Structure Results',
    codeExamples: [{
      language: 'bash',
      code: `curl https://api.perplexity.ai/v1/agent \\
  -H "Authorization: Bearer $PERPLEXITY_API_KEY" \\
  -H "Content-Type: application/json" \\
  -d '{
    "model": "openai/gpt-5.4",
    "input": "What were the largest AI startup funding rounds announced this week?",
    "tools": [{"type": "web_search"}],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "funding_rounds",
        "schema": {
          "type": "object",
          "properties": {
            "deals": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "company": {"type": "string"},
                  "amount": {"type": "string"},
                  "round": {"type": "string"},
                  "lead_investors": {
                    "type": "array",
                    "items": {"type": "string"}
                  }
                },
                "required": ["company", "amount", "round", "lead_investors"]
              }
            }
          },
          "required": ["deals"]
        }
      }
    }
  }' | jq`
    }, {
      language: 'python',
      code: `from perplexity import Perplexity

client = Perplexity()

response = client.responses.create(
    model="openai/gpt-5.4",
    input="What were the largest AI startup funding rounds announced this week?",
    tools=[{"type": "web_search"}],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "funding_rounds",
            "schema": {
                "type": "object",
                "properties": {
                    "deals": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "company": {"type": "string"},
                                "amount": {"type": "string"},
                                "round": {"type": "string"},
                                "lead_investors": {
                                    "type": "array",
                                    "items": {"type": "string"}
                                }
                            },
                            "required": ["company", "amount", "round", "lead_investors"]
                        }
                    }
                },
                "required": ["deals"]
            }
        }
    }
)

print(response.output_text)`
    }, {
      language: 'javascript',
      code: `import Perplexity from '@perplexity-ai/perplexity_ai';

const client = new Perplexity();

const response = await client.responses.create({
  model: 'openai/gpt-5.2',
  input: 'What were the largest AI startup funding rounds announced this week?',
  tools: [{ type: 'web_search' }],
  response_format: {
    type: 'json_schema',
    json_schema: {
      name: 'funding_rounds',
      schema: {
        type: 'object',
        properties: {
          deals: {
            type: 'array',
            items: {
              type: 'object',
              properties: {
                company: { type: 'string' },
                amount: { type: 'string' },
                round: { type: 'string' },
                lead_investors: {
                  type: 'array',
                  items: { type: 'string' }
                }
              },
              required: ['company', 'amount', 'round', 'lead_investors']
            }
          }
        },
        required: ['deals']
      }
    }
  }
});

console.log(response.output_text);`
    }]
  }];
  const selectedUseCase = useCases[selected];
  return <section className="mx-auto w-full p-4 sm:p-[24px_24px_24px_36px] rounded-[12px] bg-[#121516] dark:bg-[#F7F7F8] flex flex-col lg:flex-row gap-4 sm:gap-6 lg:gap-8 not-prose" aria-label="Sonar use case examples" style={{
    boxSizing: 'border-box'
  }}>
      <nav className="flex flex-col lg:w-1/4 lg:min-w-[240px]" aria-label="Use case tabs">
        <h2 className="text-xl mt-2 font-semibold mb-4 text-white dark:text-[#121516]">Try Our APIs</h2>
        <div className="flex flex-wrap lg:flex-col gap-1 lg:flex-1 pb-2 lg:pb-0">
          {useCases.map((uc, idx) => <button key={uc.label} type="button" aria-current={selected === idx} aria-controls={`usecase-panel-${idx}`} className={`px-[12px] py-[8px] flex items-center justify-start rounded-[8px] transition-all duration-200 text-sm lg:text-base ${selected === idx ? 'bg-white/10 dark:bg-[#E0E0E0] text-white dark:text-[#121516]' : 'text-white opacity-80 dark:text-[#121516] dark:opacity-80 hover:bg-white/10 dark:hover:bg-[#E0E0E0] hover:text-white hover:opacity-100 dark:hover:text-[#121516] dark:hover:opacity-100'}`} onClick={() => setSelected(idx)}>
              {uc.label}
            </button>)}
        </div>
        {}
        <a href="https://console.perplexity.ai" className="hidden lg:block mt-auto text-sm underline px-2 text-white dark:text-[#121516] opacity-80 hover:opacity-100 transition-opacity">Get Started</a>
      </nav>

      <div className="flex-1 w-full relative bg-[#121516] dark:bg-[#121516] lg:self-start rounded-[6px] overflow-hidden homepage-code-block min-w-0" id={`usecase-panel-${selected}`} role="tabpanel" aria-live="polite">
        <CodeGroup>
            <pre className="language-python" filename="Python">
              <code>{selectedUseCase.codeExamples[1].code}</code>
            </pre>
            <pre className="language-typescript" filename="Typescript">
              <code>{selectedUseCase.codeExamples[2].code}</code>
            </pre>
            <pre className="language-bash" filename="cURL">
              <code>{selectedUseCase.codeExamples[0].code}</code>
            </pre>
          </CodeGroup>
      </div>

      {}
      <a href="https://console.perplexity.ai" className="lg:hidden text-sm text-center underline text-white dark:text-[#121516] opacity-80 hover:opacity-100 transition-opacity py-1">Get Started</a>
    </section>;
};

<div className="w-full max-w-6xl mx-auto px-4 sm:px-6 md:px-8 lg:px-12 py-6 sm:py-8">
  <div className="flex flex-col lg:flex-row justify-between items-start lg:items-center mt-6 sm:mt-8 mb-8 sm:mb-12 gap-4">
    <div className="flex items-center overflow-visible">
      <PerplexityLogo />
    </div>

    <div className="lg:ml-8 max-w-full lg:max-w-md lg:text-right">
      <span className="text-xs sm:text-sm text-muted-foreground font-mono leading-relaxed">
        Power your products with unparalleled real-time, web-wide research and Q\&A capabilities.
      </span>
    </div>
  </div>

  <QuickstartBanner />

  <UseCaseTabs />

  <div className="mt-12">
    <div className="flex justify-between items-center mb-6">
      <h2 className="text-xl font-semibold text-foreground">Available APIs</h2>
    </div>

    <div className="grid grid-cols-1 md:grid-cols-3 gap-6">
      <div className="flex flex-col items-start">
        <a href="/docs/agent-api/quickstart" className="block rounded-xl overflow-hidden shadow-md hover:shadow-lg hover:scale-105 transform transition-all duration-300 cursor-pointer w-full border border-border mb-4 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 focus-visible:ring-offset-background">
          <img src="https://mintcdn.com/perplexity/38tmR5FPCzFbGyn-/docs/assets/images/overview/Agent.jpg?fit=max&auto=format&n=38tmR5FPCzFbGyn-&q=85&s=738ba1d84eb63748cf3e38c2fec0a6e7" alt="Agent API" className="w-full h-48 object-cover pointer-events-none" draggable="false" width="1216" height="720" data-path="docs/assets/images/overview/Agent.jpg" />
        </a>

        <a href="/docs/agent-api/quickstart" className="text-xl font-semibold text-foreground mb-2 hover:underline">
          Agent API
        </a>

        <p className="text-sm text-muted-foreground">Access third-party models with web search tools and presets.</p>
      </div>

      <div className="flex flex-col items-start">
        <a href="/docs/search/quickstart" className="block rounded-xl overflow-hidden shadow-md hover:shadow-lg hover:scale-105 transform transition-all duration-300 cursor-pointer w-full border border-border mb-4 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 focus-visible:ring-offset-background">
          <img src="https://mintcdn.com/perplexity/38tmR5FPCzFbGyn-/docs/assets/images/overview/Search.jpg?fit=max&auto=format&n=38tmR5FPCzFbGyn-&q=85&s=84d08a7c89feb2ff330f8bf6e9d814cc" alt="Search API" className="w-full h-48 object-cover pointer-events-none" draggable="false" width="1216" height="720" data-path="docs/assets/images/overview/Search.jpg" />
        </a>

        <a href="/docs/search/quickstart" className="text-xl font-semibold text-foreground mb-2 hover:underline">
          Search API
        </a>

        <p className="text-sm text-muted-foreground">Get raw, ranked web search results with advanced filtering and real-time data.</p>
      </div>

      <div className="flex flex-col items-start">
        <a href="/docs/embeddings/quickstart" className="block rounded-xl overflow-hidden shadow-md hover:shadow-lg hover:scale-105 transform transition-all duration-300 cursor-pointer w-full border border-border mb-4 focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-ring focus-visible:ring-offset-2 focus-visible:ring-offset-background">
          <img src="https://mintcdn.com/perplexity/38tmR5FPCzFbGyn-/docs/assets/images/overview/Embeddings.jpg?fit=max&auto=format&n=38tmR5FPCzFbGyn-&q=85&s=921a7fa48c1654a77ff21b1287f95369" alt="Embeddings API" className="w-full h-48 object-cover pointer-events-none" draggable="false" width="1216" height="720" data-path="docs/assets/images/overview/Embeddings.jpg" />
        </a>

        <a href="/docs/embeddings/quickstart" className="text-xl font-semibold text-foreground mb-2 hover:underline">
          Embeddings API
        </a>

        <p className="text-sm text-muted-foreground">Generate high-quality embeddings for semantic search and RAG pipelines.</p>
      </div>
    </div>
  </div>
</div>


Built with [Mintlify](https://mintlify.com).