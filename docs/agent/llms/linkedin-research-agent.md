# Source: https://docs.agent.ai/recipes/linkedin-research-agent.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# LinkedIn Research Agent

> How to build a LinkedIn Research agent

Building an Executive Research agent with [Agent.ai](http://Agent.ai) allows you to automatically gather and summarize information about executives from their LinkedIn profiles and posts. This guide will walk you through creating an agent that takes a LinkedIn handle as input, retrieves profile data and recent posts, and generates a comprehensive summary.

<iframe width="560" height="315" src="https://www.youtube.com/embed/qTn6fc_vICE?si=amGeexutAwndCSoH" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

# **Before You Begin**

Planning your agent's workflow before building is crucial. Taking time to visualize the process and break it down into smaller tasks will help you create more effective agents. Consider sketching out your workflow using a tool like Miro or a simple flowchart to map the steps.

# **Step 1: Create a New Agent**

1. Go to [Agent.ai](http://Agent.ai) and click "Create an Agent"
2. Select "Start from scratch"
3. Name your agent (e.g., "Simple Executive Research")
4. Add a description: "Given the LinkedIn handle of an executive, this will generate a summary about the executive"
5. Set the trigger to "Manual"

# **Step 2: Configure User Input**

1. Add an action to get user input
2. Set the prompt to "Enter the LinkedIn handle of the executive"
3. Name the output variable "out\_handle"
4. Save the action

# **Step 3: Retrieve LinkedIn Profile Data**

1. Add another workflow action
2. Select the "Social Media & Online Presence" option
3. Select "LinkedIn Profile" as the data source
4. Insert the variable "out\_handle" as the profile handle
5. Name the output "out\_LinkedIn\_data"
6. Save the action

# **Step 4: Retrieve LinkedIn Posts**

1. Add another workflow action
2. Go to the "Social Media & Online Presence"option again
3. Select "LinkedIn Activity" as the data source
4. Insert the LinkedIn URL (you'll need to format this correctly)
5. Name the output "out\_LinkedIn\_posts"
6. Save the action

# **Step 5: Generate the Executive Summary**

1. Add a \*\*Generate Content \*\*action
2. Select GPT-4 Mini (or another model of your choice)
3. Create a prompt like: "I am providing you with the LinkedIn profile and posts of an executive. Please generate a detailed summary."
4. Insert the LinkedIn data variables, labeling them clearly (e.g., "profile data" and "posts")
5. Name the output "out\_summary"
6. Save the action

# **Step 6: Display the Results**

1. Add an action to show the output
2. Insert the "out\_summary" variable
3. Save the action

## **Step 7: Test Your Agent**

1. Run your agent
2. Enter a LinkedIn handle when prompted
3. The agent will retrieve the profile data and posts
4. Review the generated summary

## **Customization Options**

You can enhance your agent by modifying the prompt in Step 5. Consider requesting specific information such as:

* Education details
* Career progression
* Post sentiment analysis
* Common topics in their content
* Professional interests

The more detailed your prompt, the more tailored the summary will be.

## **Troubleshooting**

If you encounter issues, use the dev console to debug. You can access this from the agent builder interface to see what data is being retrieved at each step and identify any problems.

Have questions or need help with your agent? Reach out to our [support team](https://agent.ai/feedback) or [community](https://community.agent.ai/feed).
