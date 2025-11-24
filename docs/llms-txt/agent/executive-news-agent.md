# Source: https://docs.agent.ai/recipes/executive-news-agent.md

# Executive News Agent

> How to build an Executive News agent

Need to stay updated on the latest news about specific executives? You can build a simple agent that searches Google News for recent articles about an executive and provides you with a summarized report. This guide will walk you through creating an agent that gathers and summarizes news about any executive from the past week.

<iframe width="560" height="315" src="https://www.youtube.com/embed/QTlrTpbcJJw?si=V8tLcnlYqYRcm2E5" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

# **Step 1: Plan Your Agent's Workflow**

Before building your agent, it's helpful to map out the steps it will follow:

1. Get the name of the executive and their company from the user
2. Search Google News for recent articles about that executive
3. Generate a summary of the news articles found
4. Display the formatted summary to the user

# **Step 2: Create a New Agent**

1. In the Builder Tool, click "Create a new agent" and select "Start from scratch"
2. Name your agent (e.g., "Executive News")
3. Add a description: "Given the name and Company of an executive, summarize the news about them from the past week"

# **Step 3: Configure User Input**

1. Add a "Get user input" action
2. Enter the prompt: "Enter the name and Company of the executive"
3. Save the output as "exec"

# **Step 4: Set Up Google News Search**

1. Add a new action and select "Input & Data Retieval"
2. Choose the "Google News" connector
3. Configure the search to use the executive's name and company
4. Set the time period to "Last 7 days" (you can adjust to 30 days if needed)
5. Save the output as "news"

# **Step 5: Create a Summary with AI**

1. Add a “Generate Content” action under AI & Content Generation
2. Select your preferred model (e.g., GPT-4)
3. Write a prompt like: "I am providing you with news articles about an executive. Please review each article and generate a summary that includes: 1) the title of the article, 2) the link to the article, and 3) a brief summary of the content."
4. Make sure to include the variable containing your news articles: "news"
5. Save the output as "formatted\_news\_summary"

# **Step 6: Display the Results**

1. Add a "Show user output" action
2. Insert the variable containing your formatted summary: "formatted\_news\_summary"
3. Save your agent

# **Step 7: Test and Debug**

1. Run your agent from the Run screen
2. Enter an executive's name and company (e.g., "Satya Nadella Microsoft")
3. Review the results
4. If needed, go back and refine your prompts or settings

# **Tips for Improvement**

* You can enhance your agent by adding instructions to remove duplicate articles
* Consider adjusting the time period if you need more or fewer results
* Refine your AI prompt to get more specific types of information about the executive

Have questions or need help with your agent? Reach out to our [support team](https://agent.ai/feedback) or [community](https://community.agent.ai/feed).
