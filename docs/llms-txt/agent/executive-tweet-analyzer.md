# Source: https://docs.agent.ai/recipes/executive-tweet-analyzer.md

# Executive Tweet Analyzer Agent

> How to build an Executive Tweet Analyzer agent

When you're preparing for important meetings or trying to understand an executive's public persona, analyzing their Twitter activity can provide valuable insights. This guide will walk you through creating an agent that fetches and summarizes an executive's recent tweets using [Agent.ai](http://Agent.ai).

<iframe width="560" height="315" src="https://www.youtube.com/embed/1UqmkC8rhyk?si=sgtkG7g3iuFtaTM4" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

# **Step 1: Create a New Agent**

1. Start by creating a new agent in the Builder Tool.
2. Name your agent "Executive Tweets"
3. Add a description like "Given the Twitter handle of an executive, this agent will return a summary of their tweets"
4. Set the trigger as "Manual"

# **Step 2: Get the Twitter Handle**

1. Add a "Get User Input" action
2. Set the prompt to "Enter the handle of the executive"
3. Add examples like "@username" to guide users
4. Set the output variable name to "out\_handle"
5. Save this step

# **Step 3: Fetch Recent Tweets**

1. Add a "Social Media & Online Presence" action
2. Select "Recent Tweets" from the available data sources
3. Set it to fetch the 20 most recent tweets
4. Insert the handle variable you collected in the previous step
5. Set the output variable name to "out\_tweets"
6. Save this step

# **Step 4: Generate a Summary**

1. Add a “Generate content” action (you can use Claude or another available model)
2. Create a prompt like: "I am providing you with a list of tweets. Please generate a summary about these tweets."
3. Pass in the tweets variable from the previous step
4. Set the output variable name to "out\_summary"
5. Save this step

# **Step 5: Display the Results**

1. Add a "Show User Output" action
2. Include both the summary and the raw tweets for reference
3. To improve readability, consider adding formatting like line breaks between tweets
4. Save this step

# **Step 6: Test Your Agent**

1. Run your agent
2. Enter an executive's Twitter handle (e.g., @username)
3. Review the summary and raw tweets that are returned

The summary will typically include:

* Main topics the executive discusses
* Their engagement patterns
* Any recurring themes or interests
* Recent announcements or news they've shared

# **Tips for Improvement**

For better formatting and readability, you can:

* Add line breaks between tweets in your output
* Use the LLM to format the tweets in a more structured way
* Create a more detailed prompt that asks for specific insights about the executive's Twitter activity

This agent provides a quick way to understand an executive's public messaging and interests before important meetings or as part of your research process.

Have questions or need help with your agent? Reach out to our [support team](https://agent.ai/feedback) or [community](https://community.agent.ai/feed).
