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

Now that your environment is ready, let’s generate the agents that will power the travel planning workflow. These agents are created using the AgentStack CLI and are defined declaratively in `agents.yaml`.

### Step 1: Generate the Agents

You’ll use the following command to scaffold each agent:

```bash  theme={null}
agentstack generate agent
```

You’ll be prompted to enter the agent's name, role, goal, backstory, and model. Repeat this step for each agent in your system.

Here are the agents created for this project:

#### 🗺️ `travel_planner`

```bash  theme={null}
agentstack g a travel_planner \
  --role="A real-time travel assistant that collects weather data, events, and hotel information using the Dappier real-time web search tool." \
  --goal="To generate personalized multi-day itineraries based on current weather, events, and travel deals." \
  --backstory="Trained to support personalized trip planning, this agent uses Dappier's real-time search to retrieve local weather, events, and hotel offers for a target city and date. It creates structured itineraries tailored to weather conditions and event availability." \
  --llm=openai/gpt-4o
```

#### 📋 `itinerary_reporter`

```bash  theme={null}
agentstack g a itinerary_reporter \
  --role="A travel itinerary formatter that compiles data into a complete multi-day markdown itinerary." \
  --goal="To generate a markdown-formatted travel itinerary based on outputs from the travel planner." \
  --backstory="This agent specializes in transforming weather and event-based trip data into user-friendly markdown plans. It includes timing, local tips, daily highlights, and weather context for each activity." \
  --llm=openai/gpt-4o
```

## ✅ Creating Tasks

Each task defines a specific responsibility to be performed by one of the agents. In this project, tasks are tightly scoped and executed sequentially by CrewAI, allowing agents to collaborate and generate a complete travel itinerary using real-time data.

Tasks are defined declaratively in `tasks.yaml` and are created using the AgentStack CLI.

### Step 1: Generate Tasks Using the CLI

Run the following command to create a new task:

```bash  theme={null}
agentstack generate task
```

You’ll be prompted to provide:

* `task_name` (required)
* `--description` – a detailed instruction including `{city}`, `{travel_date}`, `{num_days}`, and `{timestamp}`
* `--expected_output` – structured data, tables, or markdown expected from the task
* `--agent` – the agent responsible for this task

Here are the tasks used in this project:

#### 📅 `determine_travel_period`

```bash  theme={null}
agentstack g t determine_travel_period \
  --description="As of {timestamp}, use real-time web search to determine the current date and calculate the travel period based on the user's selected travel date: {travel_date} and trip length: {num_days} days in {city}." \
  --expected_output="A structured summary showing current date, travel start and end dates for the selected trip." \
  --agent=travel_planner
```

#### 🌤 `fetch_weather_forecast`

```bash  theme={null}
agentstack g t fetch_weather_forecast \
  --description="As of {timestamp}, use real-time web search to retrieve the multi-day weather forecast for {city} during the selected travel period starting on {travel_date} for {num_days} days." \
  --expected_output="Daily weather forecast for {city} including temperature, conditions, and any alerts during the trip." \
  --agent=travel_planner
```

#### 🎉 `fetch_live_events`

```bash  theme={null}
agentstack g t fetch_live_events \
  --description="As of {timestamp}, use real-time web search to find live events happening in {city} during the travel period starting on {travel_date} for {num_days} days. Include concerts, festivals, sports, and cultural events." \
  --expected_output="A list of events with names, dates, descriptions, and links where applicable for each day of the trip." \
  --agent=travel_planner
```

#### 🏨 `fetch_hotel_deals`

```bash  theme={null}
agentstack g t fetch_hotel_deals \
  --description="As of {timestamp}, use real-time web search to find hotel deals in {city} during the travel period starting on {travel_date} for {num_days} days. Include price estimates and booking links." \
  --expected_output="Top hotel deals with prices, availability, and booking URLs for the selected city and dates." \
  --agent=travel_planner
```

#### 📆 `generate_travel_itinerary`

```bash  theme={null}
agentstack g t generate_travel_itinerary \
  --description="As of {timestamp}, compile a detailed {num_days}-day travel itinerary for {city} by combining the outputs of all previous tasks: travel period, weather forecast, live events, and hotel deals. Include day-wise plans with weather-based suggestions, timing, activities, event highlights, hotel info, and booking links." \
  --expected_output="A markdown-formatted itinerary for {city} covering {num_days} days, including: daily schedule, activity suggestions, weather, events, hotel info, and travel tips." \
  --agent=itinerary_reporter
```

> ⚠️ The following two fields must be added manually to the `generate_travel_itinerary` task inside `tasks.yaml`, as they are not currently supported via the CLI:

```yaml  theme={null}
output_file: reports/{city}_travel_itinerary.md
create_directory: true
```

> 🪄 All of the above tasks will be executed in sequence using CrewAI when you run the crew.

## 🛠️ Adding Tools to Agents

Tools enable agents to interact with external services like Dappier. In this project, Dappier provides real-time access to weather data, live events, and hotel deals, powering all the data-gathering tasks.

### Add Dappier Tools to the Project

Instead of manually assigning tools one-by-one, you can add the full Dappier toolkit using:

```bash  theme={null}
agentstack tools add dappier
```

This:

* Adds all Dappier tools to the AgentStack project
* Automatically installs the `dappier` package by updating your `pyproject.toml` file
* Registers the tools under `agentstack.tools["dappier"]` for in-code access

## 📝 Providing Inputs & Setting Timestamps

Before running the crew, you need to define the runtime inputs that agents and tasks will use. The AgentStack project already includes an `inputs.yaml` file, which is used to inject these inputs when the crew is executed.

In this project, we use three dynamic inputs:

* `city`: The destination city (e.g., "paris")
* `travel_date`: The planned start date of the trip (e.g., "tomorrow")
* `num_days`: The number of days for the trip (e.g., 5)
* `timestamp`: The current UTC time, injected automatically via code

### Step 1: Update `inputs.yaml`

Open the pre-generated `inputs.yaml` file and set the travel details:

```yaml  theme={null}
city: paris
travel_date: tomorrow
num_days: 5
```

You can modify the values to plan your own custom itinerary.

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

> ⏱️ Timestamped input ensures your travel itinerary is grounded in real-time context.

## 🚀 Running the Crew

Once your agents, tasks, tools, and inputs are all set up, you're ready to run the multi-agent crew. The crew will execute each task in sequence, collaborating to generate a fully structured itinerary using real-time data.

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
* Stores the final output (e.g., markdown itinerary) in the path defined in `tasks.yaml`

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

After the crew finishes execution, you’ll find the generated itinerary at:

```
reports/paris_travel_itinerary.md
```

```markdown  theme={null}