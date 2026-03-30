# Set up model and tools
llm = init_chat_model("gpt-4o", model_provider="openai", streaming=True)
dappier_tool = DappierRealTimeSearchTool()
llm_with_tools = llm.bind_tools([dappier_tool])
```

Setup a function to handle the streaming output from the language model.

```python Python theme={null}
async def stream_llm_response(stream):
    """Print the LLM's response as it comes in"""
    async for event in stream:
        # Handle streaming chunks
        if event["event"] == "on_chat_model_stream":
            content = event["data"]["chunk"].content
            if content:
                print(content, end="", flush=True)

        # Return final output when stream ends
        if event["event"] == "on_chat_model_end":
            return event["data"]["output"]
```

Create a function to process any tool calls made by the language model.

```python Python theme={null}
async def process_tool_calls(tool_calls, messages):
    """Handle any tool calls the LLM makes"""
    print("\n\nProcessing tool calls...")
    for i, call in enumerate(tool_calls, 1):
        # Print tool call information
        print(f"\nTool Call {i}:")
        print(f"Name: {call['function']['name']}")
        print(f"Arguments: {call['function']['arguments']}")

        # Extract and process query
        args = call.get('function', {}).get('arguments', '{}')
        if isinstance(args, str):
            args = json.loads(args)
        query = args.get("query", "")

        # Execute tool and show result
        print(f"\nTool Response {i}:")
        result = await dappier_tool.ainvoke({"query": query})
        print(result)

        # Add tool response to message history
        messages.append(ToolMessage(
            content=result,
            tool_call_id=call['id'],
            name=call['function']['name']
        ))
```

Setup a function to finally generate a trading strategy using real-time data

```python Python theme={null}
async def generate_trading_strategy():
    """Generate a trading strategy using real-time data"""
    # Initialize message history and config
    messages = [HumanMessage(content=TASK_PROMPT)]
    config = RunnableConfig(callbacks=None)

    # Get initial response and handle tool calls
    print("Initial LLM response:")
    print("-------------------")
    initial_response = await stream_llm_response(
        llm_with_tools.astream_events(messages, config=config, version="v1")
    )

    # Process tool calls and get final response
    messages.append(initial_response)
    tool_calls = initial_response.additional_kwargs.get("tool_calls", [])
    if tool_calls:
        await process_tool_calls(tool_calls, messages)

    # Generate final response incorporating tool results
    print("\nFinal LLM response:")
    print("------------------")
    await stream_llm_response(
        llm_with_tools.astream_events(messages, config=config, version="v1")
    )
```

Execute the trading strategy generator

```python Python theme={null}
await generate_trading_strategy()
```

```json  theme={null}
Initial LLM response:
-------------------

Processing tool calls...

Tool Call 1:
Name: dappier_real_time_search
Arguments: {"query": "latest US financial news"}

Tool Response 1:
Here’s the latest scoop on US financial news:

- **Treasury Yields**: They’ve fallen slightly as investors are on the lookout for more economic data. 📉

- **Stock Movements**: Stocks are making waves after hours, so keep an eye on that!

- **Sustainability Attacks**: US financial firms are distancing themselves from right-wing attacks on sustainability, while the Transition Finance Council is working with cities to ramp up decarbonization efforts. 🌍

- **Alibaba's Performance**: Chinese giant Alibaba reported a profit and revenue beat for the December quarter, driven by strength in its cloud unit. 📊

- **Palantir’s Plunge**: Palantir's stock took a hit after CEO Alex Karp changed share sales, causing some market jitters.

- **Inflation and Fed Outlook**: December's inflation data is complicating the Federal Reserve's outlook on potential interest rate cuts. 📈

- **Student Debt Relief**: More relief is on the way as President Biden prepares to exit office.

If you want more details on any specific topic, just let me know! 😊

Tool Call 2:
Name: dappier_real_time_search
Arguments: {"query": "latest US stock market trends"}

Tool Response 2:
Here’s the latest on US stock market trends:

- **Dow Index**: 44,627.59 (+71.25, +0.16%)
- **S&P 500 Index**: 6,144.15 (+14.57, +0.24%)

### After-Hours:
- **Bitcoin**: $95,620.00 (-$534.00, -0.56%)
- **Ether**: $2,723.90 (+$63.10, +2.37%)

### Currency Rates:
- **Euro/US Dollar**: 1.0424 (-0.00, -0.02%)
- **British Pound/US Dollar**: 1.2584 (-0.00, -0.01%)

Looks like the markets are showing some positive movement overall! 📈 If you need more details or specific stocks, just let me know! 😊

Final LLM response:
------------------
### Summary of Latest Financial News and Stock Trends:

#### Latest US Financial News:
- **Treasury Yields**: Slight drop as investors anticipate more economic data.
- **After-Hours Stock Movements**: Some fluctuations observed in post-market trading.
- **Sustainability and Decarbonization**: Financial firms distancing from right-wing attacks as cities gear up for decarbonization.
- **Alibaba**: Reports a profit and revenue beat, driven by cloud services.
- **Palantir**: Sees a stock dip due to CEO's share sales changes.
- **Inflation Data**: Complicates Federal Reserve's interest rate decisions.
- **Student Debt Relief**: More expected as part of President Biden's agenda.

#### Latest US Stock Market Trends:
- **Dow Index**: 44,627.59, up by 0.16%.
- **S&P 500 Index**: 6,144.15, up by 0.24%.
- **Bitcoin**: Dropped slightly in after-hours trading.
- **Ether**: Notable increase in value after hours.

### Top 5 Selected Stocks:

1. **Alibaba (BABA)**:
    - **Analysis**: Strong quarterly performance with profit and revenue beats, particularly in cloud services. Positive outlook on tech sector and digital transformation efforts.

2. **Palantir Technologies (PLTR)**:
    - **Analysis**: Recent stock dip provides a potential buying opportunity. The company remains pivotal in the data analytics sector, with focus on government and corporate contracts.

3. **TESLA (TSLA)**:
    - **Analysis**: Growing advancements in electric vehicles and sustainability; long-term growth potential.

4. **Apple Inc. (AAPL)**:
    - **Analysis**: New product launches and strong ecosystem create consistent market performance. The tech giant’s adaptability to market demands is commendable.

5. **NVIDIA Corporation (NVDA)**:
    - **Analysis**: Strength as a leader in semiconductor space, heavily involved in AI and gaming industries.

### Trading Strategy:

- **Entry and Exit Points**:
    - **Alibaba**: Enter at current levels or slight pullbacks, targeting upside with expected growth from cloud services expansion.
    - **Palantir**: Enter on further dips to leverage volatility, aiming for recovery to previous high levels.
    - **Tesla, Apple, NVIDIA**: Enter at current levels with plans to hold for medium-term appreciating valuation. Expect short-term fluctuations, yet long-term upward potential due to sector leadership.

- **Risk Management Techniques**:
    - Implement stop-loss orders around 5% below entry price to safeguard against unexpected downturns.
    - Diversify holdings to mitigate sector-specific risks.

- **Time Horizon**:
    - Primarily medium-term (6-12 months), with potential for some long-term positions based on stock performance and sector evolution.

- **Sector Diversification**:
    - Technology focus, with exposure to electric vehicles (Tesla), semiconductors (NVIDIA), and cloud services (Alibaba).

- **Influence of Current News and Trends**:
    - Market-moving news such as inflation and Federal Reserve actions are immediate focus areas to gauge broader economic impact.
    - Positive corporate earnings and sustainability initiatives serve as strong catalysts for tech and related sectors.

This strategy leverages the latest financial insights and trends, aiming to capitalize on economic shifts and sector strengths. Please invest wisely, considering personal risk tolerance and financial objectives.
```

## 🌟 Highlights

This notebook has guided you through setting up and running a Langchain RAG workflow with Dappier for a generating Real-Time Market Analysis & Trading Strategy. You can adapt and expand this example for various other scenarios requiring advanced web information retrieval and AI collaboration.

Key tools utilized in this notebook include:

* **LangChain**: A versatile framework for chaining together language models and other components to create sophisticated AI-driven workflows. It enables seamless integration of LLMs with external tools and data sources, making it ideal for tasks like summarization, question-answering, and more.
* **Dappier**: A platform connecting LLMs and Agentic AI agents to real-time, rights-cleared data from trusted sources, specializing in domains like web search, finance, and news. It delivers enriched, prompt-ready data, empowering AI with verified and up-to-date information for diverse applications.
* **OpenAI**: A leading provider of advanced AI models capable of natural language understanding, contextual reasoning, and content generation. It enables intelligent, human-like interactions and supports a wide range of applications across various domains.
* **LangSmith**: A platform for debugging, testing, and monitoring LangChain applications. It provides detailed tracing and analytics to help you understand and optimize the performance of your AI workflows.

This comprehensive setup allows you to adapt and expand the example for various scenarios requiring advanced web information retrieval, AI collaboration, and multi-source data aggregation.