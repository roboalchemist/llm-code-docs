# Entry point
root_agent = sequential_pipeline_agent
```

## 💻 Running the Agent

This app is fully interactive — you don’t need to write any code to run it.

Just open the Replit app and use the built-in **chat interface** to enter a travel request (e.g., `"Plan a 3-day trip to Tokyo starting June 10"`). The agent pipeline will:

1. Extract city, start date, and duration.
2. Fetch real-time weather forecast, restaurants, and hotels.
3. Generate a day-wise travel itinerary in markdown format.

> 💬 The chat interface will display the itinerary directly in the console or browser output pane.

## 🌟 Highlights

This app has guided you through building and running a dynamic travel planner using Google ADK and Dappier. By combining real-time local data, multi-agent workflows, and markdown generation, you’ve created a complete pipeline that turns natural language travel requests into structured itineraries.

Key tools utilized in this app include:

* **Google ADK**: A flexible framework that enables sequential agent orchestration, built around modular LLM-based agents for intelligent task automation.
* **Dappier**: A platform connecting LLMs to real-time, rights-cleared data across domains like travel, hospitality, weather, and web search. It delivers prompt-ready insights that power practical agent workflows.
* **Gemini Models**: LLMs used to reason over user input and real-time data to generate complete, usable travel plans.
* **Replit**: An interactive development and execution environment that makes it easy to deploy, test, and interact with the pipeline via a chat interface.

This app can be adapted to support a wide range of location-based use cases such as:

* Weekend getaway planners
* Family or solo travel guides
* Local event finders
* AI-powered travel chatbots

It serves as a practical template for building LLM agents that reason over live, user-relevant data to generate structured and actionable outputs.