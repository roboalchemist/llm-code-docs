# --- Initial Agent to Resolve Ticker ---
ticker_resolution_agent = LlmAgent(
    name="TickerResolutionAgent",
    model=GEMINI_MODEL,
    instruction=f"""
As of {timestamp}, take a user-provided company name and use real-time web search to resolve its stock ticker symbol.
Return only the stock ticker symbol in uppercase.
""",
    description="Resolves stock ticker symbol from company name.",
    tools=[real_time_web_search],
    output_key="ticker_symbol"
)
```

> 🎯 This agent ensures the entire pipeline starts with an accurate stock symbol, derived from the latest web data.
> Dappier is used here to ensure up-to-date resolution, especially for lesser-known or recently listed companies.

## 💰 Financial Performance Agent

After gathering company basics, this agent dives into the company’s recent **financial performance** using real-time search.

It retrieves financial indicators such as:

* Revenue (TTM)
* Net Income (TTM)
* YoY growth
* Gross margin
* Key financial trends or earnings commentary

```python  theme={null}
financials_agent = LlmAgent(
    name="FinancialsPerformanceAgent",
    model=GEMINI_MODEL,
    instruction=f"""
As of "{timestamp}", use real-time web search with the timestamp to extract financial performance data for {{ticker_symbol}},
including Revenue (TTM), Net Income (TTM), YoY revenue growth, gross margin, and recent quarterly trends.
Include any earnings trends or management commentary.
""",
    description="Extracts financial metrics using real-time web search.",
    tools=[real_time_web_search],
    output_key="financials_summary"
)
```

## 🧮 Competitive Benchmarking Agent

To evaluate a company's standing in its industry, this agent identifies and compares **3–5 peer companies** using real-time web search.

It focuses on benchmarking key metrics:

* P/E ratio
* Revenue
* Stock Price
* Market Cap

It also highlights whether the target company **outperforms or underperforms** against its peers.

```python  theme={null}
benchmarking_agent = LlmAgent(
    name="CompetitiveBenchmarkingAgent",
    model=GEMINI_MODEL,
    instruction=f"""
As of {timestamp}, identify 3-5 peer companies in the same sector as {{ticker_symbol}} using real-time web search.
Extract and compare metrics: P/E ratio, revenue, stock price, market cap.
Highlight where {{ticker_symbol}} outperforms or underperforms.
""",
    description="Performs competitive benchmarking using real-time web search.",
    tools=[real_time_web_search],
    output_key="competitive_benchmarking"
)
```

## 📰 Stock News & Sentiment Agent

Fetches categorized real-time financial news for the given ticker.

```python  theme={null}
news_agent = LlmAgent(
    name="StockNewsAndSentimentAgent",
    model=GEMINI_MODEL,
    instruction=f"""
As of {timestamp}, fetch real-time financial news
for "{{ticker_symbol}}". Categorize by: Earnings, Analyst Ratings, Market Moves, Partnerships, Legal/Regulatory.
""",
    description="Fetches categorized stock news using stock_market_data_search.",
    tools=[stock_market_data_search],
    output_key="categorized_news"
)
```

## 🤖 Parallel Research Agents

Run multiple agents concurrently to improve performance and modularity.

### Web Research Agent Group

```python  theme={null}
parallel_web_research_agent = ParallelAgent(
    name="WebResearchAgentGroup",
    sub_agents=[company_overview_agent, financials_agent, benchmarking_agent],
    description="Gathers structured company data in parallel."
)
```

### Stock Insights Agent Group

```python  theme={null}
parallel_stock_insights_agent = ParallelAgent(
    name="StockInsightsAgentGroup",
    sub_agents=[stock_snapshot_agent, news_agent],
    description="Gathers real-time stock insights in parallel."
)
```

## 📝 Investment Report Generator Agent

Synthesizes all outputs into a single markdown-formatted investment report.

```python  theme={null}
report_generator_agent = LlmAgent(
    name="InvestmentReportGenerator",
    model=GEMINI_MODEL,
    instruction=f"""
As of {timestamp}, compile a comprehensive investment report for **{{stock_ticker}}**, formatted as markdown. Synthesize the outputs of all tasks: company overview, financial performance, competitive benchmarking, real-time stock snapshot, and categorized financial news.

The report must include the following structured sections:

1. **Quick Summary**  
2. **Company Profile Table**  
3. **Financial Performance Table**  
4. **Competitive Benchmarking Table**  
5. **Real-Time Stock Snapshot**  
6. **Categorized Financial News**  
7. **Insight Section**  

All the related information is below:

{{company_overview}}

{{financials_summary}}

{{competitive_benchmarking}}

{{stock_snapshot}}

{{categorized_news}}

Output only the final markdown report.
""",
    description="Generates a full investment report from aggregated data.",
    output_key="final_markdown_report"
)
```

## 🔁 Sequential Agent Pipeline

Defines the full multi-agent flow: resolves ticker → fetches data → generates report.

```python  theme={null}
sequential_pipeline_agent = SequentialAgent(
    name="StockMarketResearchPipeline",
    sub_agents=[
        ticker_resolution_agent,
        parallel_web_research_agent,
        parallel_stock_insights_agent,
        report_generator_agent
    ],
    description="Orchestrates multi-agent flow: resolves ticker, gathers data, and generates report."
)