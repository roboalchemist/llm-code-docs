# AgentOps (Optional but recommended)
AGENTOPS_API_KEY=your_agentops_key_here
```

You can get your keys here:

* 🔑 Get your OpenAI API Key [here](https://platform.openai.com/account/api-keys)
* 🔑 Get your Dappier API Key [here](https://platform.dappier.com/profile/api-keys) — free credits available
* 🔑 Get your AgentOps API Key [here](https://app.agentops.ai/signin) - enables run tracking and replay

> 🧪 Make sure to keep these keys private. Do not commit `.env` to version control.

## ⚙️ Installing Dependencies

After initializing the project and configuring your API keys, install the required dependencies to ensure everything runs smoothly.

The key packages used in this project are:

* [`crewai`](https://pypi.org/project/crewai/) – Multi-agent execution and orchestration
* [`agentstack`](https://pypi.org/project/agentstack/) – CLI toolchain for generating agents, tasks, and crews
* [`dappier`](https://pypi.org/project/dappier/) – Real-time data access layer for tools like stock search and news
* [`openai`](https://pypi.org/project/openai/) – LLM access to GPT-4o and other OpenAI models (automatically included)

### Step 1: Sync All Dependencies from `pyproject.toml`

If you're using the pre-generated project setup from `agentstack init`, run:

```bash  theme={null}
uv lock
uv sync
```

* `uv lock` will generate the `uv.lock` file based on your `pyproject.toml`
* `uv sync` will install all dependencies into the virtual environment

### Step 2: Add or Upgrade Individual Packages

You need to upgrade packages manually, use:

```bash  theme={null}
uv remove "agentstack[crewai]"
uv add crewai
uv add agentstack
```

> ✅ You now have all the required dependencies installed locally and locked for reproducible agent execution.

## 👤 Creating Agents

Now that your environment is ready, let’s generate the agents that will power the stock market research workflow. These agents are created using the AgentStack CLI and are defined declaratively in `agents.yaml`.

### Step 1: Generate the Agents

You’ll use the following command to scaffold each agent:

```bash  theme={null}
agentstack generate agent
```

You’ll be prompted to enter the agent's name, role, goal, backstory, and model. Repeat this step for each agent in your system.

Here are the agents created for this project:

#### 🧠 `web_researcher`

```bash  theme={null}
agentstack g a web_researcher \
  --role="A company research analyst that collects structured business data, financials, and competitive insights from the Dappier real-time web search." \
  --goal="To compile detailed company profiles using real-time data, covering company overview, financial performance, and peer benchmarking." \
  --backstory="Trained to support investment research workflows, this agent uses Dappier’s real-time web search to gather trustworthy and current business information. It builds company snapshots with industry, CEO, market cap, and financial metrics like revenue and net income." \
  --llm=openai/gpt-4o
```

#### 📊 `stock_insights_analyst`

```bash  theme={null}
agentstack g a stock_insights_analyst \
  --role="A stock market intelligence analyst that retrieves real-time financial data and curated news using the Dappier stock market data search." \
  --goal="To deliver up-to-date stock snapshots, performance metrics, and categorized financial news for informed investment analysis." \
  --backstory="Trained to analyze real-time financial markets using Dappier’s stock market data tool, this agent specializes in stock-specific queries. It provides live insights into stock price movements, valuation ratios, earnings, and sentiment-tagged news from reliable financial feeds like Polygon.io." \
  --llm=openai/gpt-4o
```

#### 📝 `report_analyst`

```bash  theme={null}
agentstack g a report_analyst \
  --role="A financial report analyst that consolidates real-time stock and company insights into a comprehensive markdown report." \
  --goal="To generate an investor-facing, markdown-formatted summary combining company profile, financials, benchmarking, stock performance, and real-time news with actionable insights." \
  --backstory="Specialized in synthesizing structured data retrieved by other research agents, this agent produces detailed markdown reports that explain what's happening with a given stock ticker, why it matters, and what the short-term outlook may be." \
  --llm=openai/gpt-4o
```

Once generated, AgentStack automatically adds these to your `agents.yaml` file.

> 👥 These agents will work together to build a real-time stock market report using data from Dappier and OpenAI reasoning.

## ✅ Creating Tasks

Each task defines a specific responsibility to be performed by one of the agents. In this project, tasks are tightly scoped and executed sequentially by CrewAI, allowing agents to collaborate and generate a full investment report.

Tasks are defined declaratively in `tasks.yaml` and are created using the AgentStack CLI.

### Step 1: Generate Tasks Using the CLI

Run the following command to create a new task:

```bash  theme={null}
agentstack generate task
```

You’ll be prompted to provide:

* `task_name` (required)
* `--description` – a detailed instruction including `{company_name}` and `{timestamp}`
* `--expected_output` – structured data, tables, or markdown expected from the task
* `--agent` – the agent responsible for this task

Here are the tasks used in this project:

#### 🏢 `company_overview`

```bash  theme={null}
agentstack g t company_overview \
  --description="As of {timestamp}, fetch the company overview for {company_name} using real-time web search with the timestamp. Include company profile, industry, sector, CEO, headquarters location, employee count, market capitalization and stock ticker symbol." \
  --expected_output="A structured company profile including: Industry, Sector, CEO, HQ Location, Employees, Market Cap, and Ticker Symbol." \
  --agent=web_researcher
```

#### 📉 `financials_performance`

```bash  theme={null}
agentstack g t financials_performance \
  --description="As of {timestamp}, use real-time web search with the timestamp to extract financial performance data for {company_name}, including Revenue (TTM), Net Income (TTM), Year-over-Year revenue growth, gross margin, and recent quarterly trends. Include any earnings trends or management commentary available." \
  --expected_output="A summary of financial metrics for {company_name}: Revenue (TTM), Net Income (TTM), YoY Growth, Gross Margin, and Quarterly Trends." \
  --agent=web_researcher
```

#### 🆚 `competitive_benchmarking`

```bash  theme={null}
agentstack g t competitive_benchmarking \
  --description="As of {timestamp}, perform real-time web search with the timestamp to identify 3-5 peer companies in the same sector as {company_name}. Extract and compare key metrics such as P/E ratio, revenue,stock price, and market cap. Highlight any standout metrics where {company_name} outperforms or underperforms." \
  --expected_output="A table comparing {company_name} and 3–5 peers on P/E, revenue, stock price, and market cap with highlights." \
  --agent=web_researcher
```

#### 💹 `real_time_stock_snapshot`

```bash  theme={null}
agentstack g t real_time_stock_snapshot \
  --description="As of {timestamp}, convert {company_name} to its stock ticker symbol and retrieve a real-time stock snapshot using Dappier’s stock market data tool with the timestamp. Include current price with % daily change, volume, 52-week high/low, P/E ratio, EPS, dividend yield, and chart data for 1D, 5D, 1M, YTD, and 1Y in the query." \
  --expected_output="Structured snapshot of {company_name}: Price, Change %, Volume, 52W High/Low, P/E, EPS, Dividend, and Charts." \
  --agent=stock_insights_analyst
```

#### 📰 `news_and_sentiment`

```bash  theme={null}
agentstack g t news_and_sentiment \
  --description="As of {timestamp}, compile a comprehensive, markdown-formatted investment report for {company_name} by synthesizing the outputs of all prior tasks: company overview, financial performance, competitive benchmarking, real-time stock snapshot, and categorized financial news. Use the timestamp in all queries. Include a concise AI-generated company summary, structured data tables, sentiment-tagged news, and a narrative insight section." \
  --expected_output="A markdown-formatted investment report containing:
      1. Quick AI summary of {company_name} (e.g., "Apple is a global tech leader…")
      2. Structured company profile: Industry, Sector, CEO, HQ, Employees, Market Cap
      3. Financial performance metrics: Revenue (TTM), Net Income (TTM), YoY Growth, Gross Margin, Trends
      4. Competitive benchmarking table: P/E, Revenue, Stock Price, Market Cap vs. 3–5 peers
      5. Real-time stock snapshot: Price, % Change, Volume, 52W High/Low, P/E, EPS, Dividend, charts
      6. Categorized news: Earnings, Analyst Ratings, Market Moves, Partnerships, Legal/Regulatory (with sentiment tags)
      7. Final 3-part insight section:
         - What's going on with {company_name}
         - Why it matters
         - Outlook (clearly marked as not financial advice)" \
  --agent=stock_insights_analyst
```

#### 📄 `generate_investment_report`

```bash  theme={null}
agentstack g t generate_investment_report \
  --description="As of {timestamp}, compile a markdown-formatted investment report for {company_name} using all prior task outputs. Include a summary, structured profile, financial metrics, peer comparisons, charts, news, and a 3-part insight section." \
  --expected_output="A markdown report with company overview, financials, benchmarking, stock snapshot, categorized news, and AI-generated outlook." \
  --agent=report_analyst
```

> ⚠️ The following two fields must be added manually to the `generate_investment_report` task inside `tasks.yaml`, as they are not currently supported via the CLI:

```yaml  theme={null}
output_file: reports/{company_name}_investment_report.md
create_directory: true
```

> 🪄 All of the above tasks will be executed in sequence using CrewAI when you run the crew.

## 🛠️ Adding Tools to Agents

Tools enable agents to interact with external services like Dappier. In this project, Dappier provides real-time access to financial data and web search, powering all the data-gathering tasks.

### Step 1: Add Dappier Tools to the Project

Instead of manually assigning tools one-by-one, you can add all Dappier tools at once using:

```bash  theme={null}
agentstack tools add dappier
```

This will register the full Dappier toolset to the project and make it available through the `agentstack.tools["dappier"]` registry.

### Step 2: Select Specific Tools Per Agent in Code

Instead of assigning tools via CLI, agents in this project filter and attach only the tools they need using a custom helper function in `crew.py`:

```python  theme={null}
def get_dappier_tool(tool_name: str):
    for tool in agentstack.tools["dappier"]:
        if tool.name == tool_name:
            return tool
    return None
```

Then each agent uses this function to assign a single tool:

#### 🧠 web\_researcher

```python  theme={null}
tools = [get_dappier_tool("real_time_web_search")]
```

#### 📊 stock\_insights\_analyst

```python  theme={null}
tools = [get_dappier_tool("stock_market_data_search")]
```

> ⚙️ This approach ensures that each agent only receives the exact tool it needs, while keeping tool registration centralized and clean.

## 📝 Providing Inputs & Setting Timestamps

Before running the crew, you need to define the runtime inputs that agents and tasks will use. The AgentStack project already includes an `inputs.yaml` file, which is used to inject these inputs when the crew is executed.

In this project, we use two dynamic inputs:

* `company_name`: The company to analyze (e.g., "tesla")
* `timestamp`: The current UTC time, injected automatically via code

### Step 1: Update `inputs.yaml`

Open the pre-generated `inputs.yaml` file and set the target company:

```yaml  theme={null}
company_name: tesla
```

You can modify `"tesla"` to any other publicly traded company.

### Step 2: Inject a Real-Time Timestamp in `main.py`

To provide the current timestamp at execution time, update the `run()` function in `main.py`:

```python  theme={null}
from datetime import datetime, timezone

def run():
    """
    Run the agent.
    """
    inputs = agentstack.get_inputs()
    inputs["timestamp"] = datetime.now(timezone.utc).isoformat()

    instance.kickoff(inputs=inputs)
```

This will:

* Dynamically inject the current UTC timestamp into the input dictionary
* Allow all tasks referencing `{timestamp}` in `tasks.yaml` to use consistent timing context

> ⏱️ Timestamped input ensures your reports are anchored to the moment of execution.

## 🚀 Running the Crew

Once your agents, tasks, tools, and inputs are all set up, you're ready to run the multi-agent crew. The crew will execute each task in sequence, collaborating to generate a fully structured investment research report using real-time data.

### Step 1: Run the AgentStack Project

To start the crew execution, run the following command from the project root:

```bash  theme={null}
agentstack run
```

This command:

* Loads your agents from `agents.yaml`
* Loads your tasks from `tasks.yaml`
* Injects inputs from `inputs.yaml` (including the runtime `timestamp`)
* Executes all tasks sequentially via CrewAI
* Stores the final output (e.g., markdown report) in the path defined in `tasks.yaml`

> ✅ You should see terminal output as each agent completes its assigned task.

### Step 2: Debug with `--debug` Mode (Optional)

For detailed execution traces, run with the debug flag:

```bash  theme={null}
agentstack run --debug
```

This enables verbose logging, including:

* Which agent is running
* Which tool is being used
* Real-time function call results
* Intermediate outputs for each task

> 🧪 Use debug mode to troubleshoot tool usage or model behavior during each step.

### Step 3: View the Final Output

After the crew finishes execution, you’ll find the generated investment report at:

```
reports/tesla_investment_report.md
```

You can open this file in any markdown viewer or commit it to your workspace.

```markdown  theme={null}