# Source: https://docs.agent.ai/recipes/company-research-agent.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Company Research Agent

> How to build a Company Research agent in Agent.ai

Need to quickly research companies before meetings or sales calls? This guide will show you how to build a simple AI agent that can automatically research any company and provide information about their products and industry. You don't need technical skills—just follow these steps to create your own company research assistant.

<iframe width="560" height="315" src="https://www.youtube.com/embed/j2wG29JRx6U?si=S8vUiBHyycE7T5eP" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

# **Step 1: Create a New Agent**

To get started with your company research agent:

1. Navigate to the Agent Builder section in [Agent.ai](http://Agent.ai)
2. Click "Create Agent"
3. Select "Start from scratch"
4. Name your agent (e.g., "Simple Company Research")
5. Add a description like "This agent will take the name of a company and do some research on what products the company sells"

# **Step 2: Set Up the Trigger**

For this simple agent, you'll use a manual trigger:

1. In the trigger section, select "Manual"
2. This means users will manually start the agent when they need company information

# **Step 3: Create the Input Action**

Now you'll set up how the agent collects the company name:

1. Go to the Actions screen
2. Click to add a new action
3. Select "Inputs & Data Retrieval"
4. Choose "Text box" as the input type
5. Add a prompt like "Enter the name of the company"
6. Optionally, add an example (e.g., "Upsot")
7. In the "Store value in" field, enter "out\_company" (this creates a variable to store the company name)
8. Save this action

# **Step 4: Create the Research Action**

Next, set up the AI to research the company:

1. Add another action
2. Select "AI & Content Generation" then "Generate Content"
3. Choose an LLM model (e.g., GPT-4 Mini for cost efficiency)
4. In the instructions field, enter your prompt:
5. You are an experienced researcher. I am giving you the name of a company: out\_company. I would like you to research this company and list out the products this company sells and what industry it is in.
6. In the "Store output in" field, enter "out\_company\_research"
7. Save this action

# **Step 5: Display the Results**

Finally, set up how the agent will show the research results:

1. Add a final action
2. Select "Outputs"
3. Choose the variable "out\_company\_research" to display
4. Save this action

# **Step 6: Test Your Agent**

Your company research agent is now ready to use:

1. Click the "Run" button to test your agent
2. When prompted, enter a company name (e.g., "[Pigment.com](http://Pigment.com)")
3. The agent will process the request and display information about the company's products and industry

## **Example Output**

When testing with "[Pigment.com](http://Pigment.com)", the agent might return something like:

"Pigment operates in the field of business intelligence and data visualization, focusing on helping organizations manage their data more effectively. Their main product is a SaaS platform that offers business planning, forecasting, and analytics solutions."

# **Advanced Options**

Once you're comfortable with your basic agent, you can explore more advanced features:

* Set up automatic email generation of results
* Create more complex research workflows
* Add additional data sources
* Customize the output format

Have questions or need help with your agent? Reach out to our [support team](https://agent.ai/feedback) or [community](https://community.agent.ai/feed).
