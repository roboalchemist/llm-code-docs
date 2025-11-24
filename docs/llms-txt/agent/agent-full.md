# Agent Documentation

Source: https://docs.agent.ai/llms-full.txt

---

# Action Availability
Source: https://docs.agent.ai/actions-available

Agent.ai provides actions across the builder and SDKs.

## **Action Availability**

This document provides an overview of which Agent.ai actions are available across different platforms and SDKs, along with installation instructions for each package.

## Installation Instructions

### Python SDK

The Agent.ai Python SDK provides a simple way to interact with the Agent.ai Actions API.

**Installation:**

```bash  theme={null}
pip install agentai
```

**Links:**

* [PIP Package](https://pypi.org/project/agentai/)
* [GitHub Repository](https://github.com/OnStartups/python_sdk)

### JavaScript SDK

The Agent.ai JavaScript SDK allows you to integrate Agent.ai actions into your JavaScript applications.

**Installation:**

```bash  theme={null}
# Using yarn
yarn add @agentai/agentai

# Using npm
npm install @agentai/agentai
```

**Links:**

* [NPM Package](https://www.npmjs.com/package/@agentai/agentai)
* [GitHub Repository](https://github.com/OnStartups/js_sdk)

### MCP Server

The MCP (Multi-Channel Platform) Server provides a server-side implementation of all API functions.

**Installation:**

```bash  theme={null}
# Using yarn
yarn add @agentai/mcp-server

# Using npm
npm install @agentai/mcp-server
```

**Links:**

* [NPM Package](https://www.npmjs.com/package/@agentai/mcp-server)
* [GitHub Repository](https://github.com/OnStartups/agentai-mcp-server)
* [Documentation](https://docs.agent.ai/mcp-server)

**Legend:**

* ✅ - Feature is available
* ❌ - Feature is not available

**Notes:**

* The Builder UI has the most comprehensive set of actions available
* The MCP Server implements all API functions
* The Python and JavaScript SDKs currently implement the same set of actions
* Some actions are only available in the Builder UI and are not exposed via the API yet, but we plan to get to 100% parity scross our packaged offerings.

## Action Availability Table

| Action                                 | Docs                                                                       | API                                                                            | Builder UI | API | MCP Server | Python SDK | JS SDK |
| -------------------------------------- | -------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | ---------- | --- | ---------- | ---------- | ------ |
| Get User Input                         | [Docs](https://docs.agent.ai/actions/get_user_input)                       | -                                                                              | ✅          | ❌   | ❌          | ❌          | ❌      |
| Get User List                          | [Docs](https://docs.agent.ai/actions/get_user_list)                        | -                                                                              | ✅          | ❌   | ❌          | ❌          | ❌      |
| Get User Files                         | [Docs](https://docs.agent.ai/actions/get_user_file)                        | -                                                                              | ✅          | ❌   | ❌          | ❌          | ❌      |
| Get User Knowledge Base and Files      | [Docs](https://docs.agent.ai/actions/get_user_knowledge_base_and_files)    | -                                                                              | ✅          | ❌   | ❌          | ❌          | ❌      |
| Web Page Content                       | [Docs](https://docs.agent.ai/actions/web_page_content)                     | [API](https://docs.agent.ai/api-reference/get-data/web-page-content)           | ✅          | ✅   | ✅          | ✅          | ✅      |
| Web Page Screenshot                    | [Docs](https://docs.agent.ai/actions/web_page_screenshot)                  | [API](https://docs.agent.ai/api-reference/get-data/web-page-screenshot)        | ✅          | ✅   | ✅          | ✅          | ✅      |
| YouTube Transcript                     | [Docs](https://docs.agent.ai/actions/youtube_transcript)                   | [API](https://docs.agent.ai/api-reference/get-data/youtube-transcript)         | ✅          | ✅   | ✅          | ✅          | ✅      |
| YouTube Channel Data                   | [Docs](https://docs.agent.ai/actions/youtube_channel_data)                 | [API](https://docs.agent.ai/api-reference/get-data/youtube-channel-data)       | ✅          | ✅   | ✅          | ✅          | ✅      |
| Get Twitter Users                      | [Docs](https://docs.agent.ai/actions/get_twitter_users)                    | [API](https://docs.agent.ai/api-reference/get-data/get-twitter-users)          | ✅          | ✅   | ✅          | ✅          | ✅      |
| Google News Data                       | [Docs](https://docs.agent.ai/actions/google_news_data)                     | [API](https://docs.agent.ai/api-reference/get-data/google-news-data)           | ✅          | ✅   | ✅          | ✅          | ✅      |
| YouTube Search Results                 | [Docs](https://docs.agent.ai/actions/youtube_search_results)               | [API](https://docs.agent.ai/api-reference/get-data/youtube-search-results)     | ✅          | ✅   | ✅          | ✅          | ✅      |
| Search Results                         | [Docs](https://docs.agent.ai/actions/search_results)                       | [API](https://docs.agent.ai/api-reference/get-data/search-results)             | ✅          | ✅   | ✅          | ✅          | ✅      |
| Search HubSpot (V2)                    | [Docs](https://docs.agent.ai/actions/hubspot-v2-search-objects)            | -                                                                              | ✅          | ❌   | ❌          | ❌          | ❌      |
| Lookup HubSpot Object (V2)             | [Docs](https://docs.agent.ai/actions/hubspot-v2-lookup-object)             | -                                                                              | ✅          | ❌   | ❌          | ❌          | ❌      |
| Create HubSpot Object (V2)             | [Docs](https://docs.agent.ai/actions/hubspot-v2-create-object)             | -                                                                              | ✅          | ❌   | ❌          | ❌          | ❌      |
| Update HubSpot Object (V2)             | [Docs](https://docs.agent.ai/actions/hubspot-v2-update-object)             | -                                                                              | ✅          | ❌   | ❌          | ❌          | ❌      |
| Get Timeline Events (V2)               | [Docs](https://docs.agent.ai/actions/hubspot-v2-get-timeline-events)       | -                                                                              | ✅          | ❌   | ❌          | ❌          | ❌      |
| Create Timeline Event (V2)             | [Docs](https://docs.agent.ai/actions/hubspot-v2-create-timeline-event)     | -                                                                              | ✅          | ❌   | ❌          | ❌          | ❌      |
| Get Engagements (V2)                   | [Docs](https://docs.agent.ai/actions/hubspot-v2-get-engagements)           | -                                                                              | ✅          | ❌   | ❌          | ❌          | ❌      |
| Create Engagement (V2)                 | [Docs](https://docs.agent.ai/actions/hubspot-v2-create-engagement)         | -                                                                              | ✅          | ❌   | ❌          | ❌          | ❌      |
| Recent Tweets                          | [Docs](https://docs.agent.ai/actions/get_recent_tweets)                    | [API](https://docs.agent.ai/api-reference/get-data/recent-tweets)              | ✅          | ✅   | ✅          | ✅          | ✅      |
| LinkedIn Profile                       | [Docs](https://docs.agent.ai/actions/get_linkedin_profile)                 | [API](https://docs.agent.ai/api-reference/get-data/linkedin-profile)           | ✅          | ✅   | ✅          | ✅          | ✅      |
| Get LinkedIn Activity                  | [Docs](https://docs.agent.ai/actions/get_linkedin_activity)                | [API](https://docs.agent.ai/api-reference/get-data/linkedin-activity)          | ✅          | ✅   | ✅          | ✅          | ✅      |
| Enrich with Breeze Intelligence        | [Docs](https://docs.agent.ai/actions/enrich_with_breeze_intelligence)      | [API](https://docs.agent.ai/api-reference/get-data/enrich-company-data)        | ✅          | ✅   | ✅          | ✅          | ✅      |
| Company Earnings Info                  | [Docs](https://docs.agent.ai/actions/company_earnings_info)                | [API](https://docs.agent.ai/api-reference/get-data/company-earnings-info)      | ✅          | ✅   | ✅          | ❌          | ❌      |
| Company Financial Profile              | [Docs](https://docs.agent.ai/actions/company_financial_profile)            | [API](https://docs.agent.ai/api-reference/get-data/company-financial-profile)  | ✅          | ✅   | ✅          | ❌          | ❌      |
| Domain Info                            | [Docs](https://docs.agent.ai/actions/domain_info)                          | [API](https://docs.agent.ai/api-reference/get-data/domain-info)                | ✅          | ✅   | ✅          | ❌          | ❌      |
| Get Data from Builder's Knowledge Base | [Docs](https://docs.agent.ai/actions/get_data_from_builders_knowledgebase) | -                                                                              | ✅          | ❌   | ❌          | ❌          | ❌      |
| Get Data from User's Uploaded Files    | [Docs](https://docs.agent.ai/actions/get_data_from_users_uploaded_files)   | -                                                                              | ✅          | ❌   | ❌          | ❌          | ❌      |
| Set Variable                           | [Docs](https://docs.agent.ai/actions/set-variable)                         | -                                                                              | ✅          | ❌   | ❌          | ❌          | ❌      |
| Add to List                            | [Docs](https://docs.agent.ai/actions/add_to_list)                          | -                                                                              | ✅          | ❌   | ❌          | ❌          | ❌      |
| Click Go to Continue                   | [Docs](https://docs.agent.ai/actions/click_go_to_continue)                 | -                                                                              | ✅          | ❌   | ❌          | ❌          | ❌      |
| Use GenAI (LLM)                        | [Docs](https://docs.agent.ai/actions/use_genai)                            | [API](https://docs.agent.ai/api-reference/use-ai/invoke-llm)                   | ✅          | ✅   | ✅          | ✅          | ✅      |
| Generate Image                         | [Docs](https://docs.agent.ai/actions/generate_image)                       | [API](https://docs.agent.ai/api-reference/use-ai/generate-image)               | ✅          | ✅   | ✅          | ✅          | ✅      |
| Generate Audio Output                  | [Docs](https://docs.agent.ai/actions/generate_audio_output)                | [API](https://docs.agent.ai/api-reference/use-ai/output-audio)                 | ✅          | ✅   | ✅          | ✅          | ✅      |
| Orchestrate Tasks                      | [Docs](https://docs.agent.ai/actions/orchestrate_tasks)                    | -                                                                              | ✅          | ❌   | ❌          | ❌          | ❌      |
| Orchestrate Agents                     | [Docs](https://docs.agent.ai/actions/orchestrate_agents)                   | -                                                                              | ✅          | ❌   | ❌          | ❌          | ❌      |
| Convert File                           | [Docs](https://docs.agent.ai/actions/convert_file)                         | [API](https://docs.agent.ai/api-reference/advanced/convert-file)               | ✅          | ✅   | ✅          | ✅          | ✅      |
| Continue or Exit Workflow              | [Docs](https://docs.agent.ai/actions/continue_or_exit_workflow)            | -                                                                              | ✅          | ❌   | ❌          | ❌          | ❌      |
| If/Else Statement                      | [Docs](https://docs.agent.ai/actions/if_else)                              | -                                                                              | ✅          | ❌   | ❌          | ❌          | ❌      |
| For Loop                               | [Docs](https://docs.agent.ai/actions/for_loop)                             | -                                                                              | ✅          | ❌   | ❌          | ❌          | ❌      |
| End If/Else/For Statement              | [Docs](https://docs.agent.ai/actions/end_statement)                        | -                                                                              | ✅          | ❌   | ❌          | ❌          | ❌      |
| Wait for User Confirmation             | [Docs](https://docs.agent.ai/actions/wait_for_user_confirmation)           | -                                                                              | ✅          | ❌   | ❌          | ❌          | ❌      |
| Get Assigned Company                   | [Docs](https://docs.agent.ai/actions/get_assigned_company)                 | -                                                                              | ✅          | ❌   | ❌          | ❌          | ❌      |
| Query HubSpot CRM                      | [Docs](https://docs.agent.ai/actions/query_hubspot_crm)                    | -                                                                              | ✅          | ✅   | ✅          | ✅          | ✅      |
| Create Web Page                        | [Docs](https://docs.agent.ai/actions/create_web_page)                      | -                                                                              | ✅          | ❌   | ❌          | ❌          | ❌      |
| Get HubDB Data                         | [Docs](https://docs.agent.ai/actions/get_hubdb_data)                       | -                                                                              | ✅          | ❌   | ❌          | ❌          | ❌      |
| Update HubDB                           | [Docs](https://docs.agent.ai/actions/update_hubdb)                         | -                                                                              | ✅          | ❌   | ❌          | ❌          | ❌      |
| Get Conversation                       | [Docs](https://docs.agent.ai/actions/get_conversation)                     | -                                                                              | ✅          | ❌   | ❌          | ❌          | ❌      |
| Start Browser Operator                 | [Docs](https://docs.agent.ai/actions/start_browser_operator)               | [API](https://docs.agent.ai/api-reference/advanced/start-browser-operator)     | ✅          | ✅   | ✅          | ❌          | ❌      |
| Browser Operator Results               | [Docs](https://docs.agent.ai/actions/results_browser_operator)             | [API](https://docs.agent.ai/api-reference/advanced/browser-operator-results)   | ✅          | ✅   | ✅          | ❌          | ❌      |
| Invoke Web API                         | [Docs](https://docs.agent.ai/actions/invoke_web_api)                       | [API](https://docs.agent.ai/api-reference/advanced/invoke-web-api)             | ✅          | ✅   | ✅          | ✅          | ✅      |
| Invoke Other Agent                     | [Docs](https://docs.agent.ai/actions/invoke_other_agent)                   | [API](https://docs.agent.ai/api-reference/advanced/invoke-other-agent)         | ✅          | ✅   | ✅          | ✅          | ✅      |
| Show User Output                       | [Docs](https://docs.agent.ai/actions/show_user_output)                     | -                                                                              | ✅          | ❌   | ❌          | ❌          | ❌      |
| Send Message                           | [Docs](https://docs.agent.ai/actions/send_message)                         | -                                                                              | ✅          | ❌   | ❌          | ❌          | ❌      |
| Create Blog Post                       | [Docs](https://docs.agent.ai/actions/create_blog_post)                     | -                                                                              | ✅          | ❌   | ❌          | ❌          | ❌      |
| Save To Google Doc                     | [Docs](https://docs.agent.ai/actions/save_to_google_doc)                   | -                                                                              | ✅          | ❌   | ❌          | ❌          | ❌      |
| Save To File                           | [Docs](https://docs.agent.ai/actions/save_to_file)                         | [API](https://docs.agent.ai/api-reference/create-output/save-to-file)          | ✅          | ✅   | ✅          | ❌          | ❌      |
| Save To Google Sheet                   | [Docs](https://docs.agent.ai/actions/save_to_google_sheet)                 | -                                                                              | ✅          | ❌   | ❌          | ❌          | ❌      |
| Format Text                            | [Docs](https://docs.agent.ai/actions/format_text)                          | -                                                                              | ✅          | ❌   | ❌          | ❌          | ❌      |
| Store Variable to Database             | [Docs](https://docs.agent.ai/actions/store_variable_to_database)           | [API](https://docs.agent.ai/api-reference/advanced/store-variable-to-database) | ✅          | ✅   | ✅          | ✅          | ✅      |
| Get Variable from Database             | [Docs](https://docs.agent.ai/actions/get_variable_from_database)           | [API](https://docs.agent.ai/api-reference/advanced/get-variable-from-database) | ✅          | ✅   | ✅          | ✅          | ✅      |
| Bluesky Posts                          | [Docs](https://docs.agent.ai/actions/get_bluesky_posts)                    | [API](https://docs.agent.ai/api-reference/get-data/bluesky-posts)              | ✅          | ✅   | ✅          | ✅          | ✅      |
| Search Bluesky Posts                   | [Docs](https://docs.agent.ai/actions/search_bluesky_posts)                 | [API](https://docs.agent.ai/api-reference/get-data/search-bluesky-posts)       | ✅          | ✅   | ✅          | ✅          | ✅      |
| Post to Bluesky                        | [Docs](https://docs.agent.ai/actions/post_to_bluesky)                      | -                                                                              | ✅          | ❌   | ❌          | ❌          | ❌      |
| Get Instagram Profile                  | [Docs](https://docs.agent.ai/actions/get_instagram_profile)                | [API](https://docs.agent.ai/api-reference/get-data/get-instagram-profile)      | ✅          | ✅   | ✅          | ✅          | ✅      |
| Get Instagram Followers                | [Docs](https://docs.agent.ai/actions/get_instagram_followers)              | [API](https://docs.agent.ai/api-reference/get-data/get-instagram-followers)    | ✅          | ✅   | ✅          | ✅          | ✅      |
| Call Serverless Function               | [Docs](https://docs.agent.ai/actions/serverless_function)                  | -                                                                              | ✅          | ❌   | ❌          | ❌          | ❌      |

## Summary

* **UI Builder** supports all 65 actions listed above
* **API** supports 31 actions
* **MCP Server** supports the same 31 actions as the API
* **Python SDK** supports 25 actions
* **JavaScript SDK** supports 25 actions

The Python and JavaScript SDKs currently implement the same set of core data retrieval and AI generation functions as the builder, but there are some actions that either don't make sense to implement via our API (i.e. get user input) or aren't useful as standalone actions (i.e. for loops).
You can always implement an agent throught the builder UI and invoke it via API or daisy chain agents together.


# Add to List
Source: https://docs.agent.ai/actions/add_to_list



## Overview

The "Add to List" action lets you add items to an existing list variable. This allows you to collect multiple entries or build up data over time within your workflow.

### Use Cases

* **Data Aggregation**: Collect multiple responses or items into a single list

* **Iterative Storage**: Track user selections or actions throughout a workflow

* **Building Collections**: Create lists of related items step by step

* **Dynamic Lists**: Add user-provided items to predefined lists

## Configuration Fields

### Input Text

* **Description**: Enter the text to append to the list.

* **Example**:  Enter what you want to add to the list

  1. Can be a fixed value: "Sample item"

  2. Or a variable: \{\{first\_task}}

  3. Or another list: \{\{additional\_tasks}}

* **Required**: Yes

### Output Variable Name

* **Description**: Assign a variable name to store the updated list.

* **Example**: "task\_list" or "user\_choices."

* **Validation**: Only letters, numbers, and underscores (\_) are allowed.

* **Required**: Yes

## **Example: Example Agent for Adding and Using Lists**

See this [simple Task Organizer Agent](https://agent.ai/agent/lists-agent-example). It collects an initial task, creates a list with it, then gathers additional tasks and adds them to the list. The complete list is then passed to an AI for analysis.&#x20;


# Click Go to Continue
Source: https://docs.agent.ai/actions/click_go_to_continue



#

## Overview

The "Click Go to Continue" action adds a button that prompts users to proceed to the next step in the workflow.

### Use Cases

* **Workflow Navigation**: Simplify user progression with a clickable button.

* **Confirmation**: Add a step for users to confirm their readiness to proceed.

## Configuration Fields

### Variable Value

* **Description**: Set the display text for the button.

* **Example**: "Proceed to Next Step" or "Continue."

* **Required**: Yes


# Continue or Exit Workflow
Source: https://docs.agent.ai/actions/continue_or_exit_workflow



## Overview

Evaluate conditions to decide whether to continue or exit the workflow, providing control over the process flow.

### Use Cases

* **Conditional Completion**: End a workflow if certain criteria are met.
* **Dynamic Navigation**: Determine the next step in the workflow based on user input or data.

## Configuration Fields

### Condition Logic

* **Description**: Define the condition logic using Jinja template syntax.
* **Example**: "if user\_age > 18" or "agent\_control = 'exit'."
* **Required**: Yes


# Convert File
Source: https://docs.agent.ai/actions/convert_file



## Overview

Convert uploaded files to different formats, such as PDF, TXT, or PNG, within workflows.

### Use Cases

* **Document Management**: Convert user-uploaded files to preferred formats.
* **Data Transformation**: Process files for compatibility with downstream actions.

<iframe width="560" height="315" src="https://www.youtube.com/embed/WWRn_d4uQhc?si=x_FTZ9AG0fzuNuOR" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

## Configuration Fields

### Input Files

* **Description**: Select the files to be converted.
* **Example**: "uploaded\_documents" or "images."
* **Required**: Yes

### Show All Conversion Options

* **Description**: Enable to display all available conversion options.
* **Required**: Yes

### Convert to Extension

* **Description**: Specify the desired output file format.
* **Example**: "pdf," "txt," or "png."
* **Required**: No

### Output Variable Name

* **Description**: Assign a variable name to store the converted files.
* **Example**: "converted\_documents" or "output\_images."
* **Validation**: Only letters, numbers, and underscores (\_) are allowed.
* **Required**: Yes


# Create Blog Post
Source: https://docs.agent.ai/actions/create_blog_post



## Overview

Generate a blog post with a title and body, allowing for easy content creation and publishing.

### Use Cases

* **Content Marketing**: Draft blog posts for campaigns or updates.
* **Knowledge Sharing**: Create posts to share information with your audience.

## Configuration Fields

### Title

* **Description**: Enter the title of the blog post.
* **Example**: "5 Tips for Better Marketing" or "Understanding AI in Business."
* **Required**: Yes

### Body

* **Description**: Provide the content for the blog post, including text, headings, and relevant details.
* **Example**: "This blog covers the top 5 trends in AI marketing..."
* **Required**: Yes


# End If/Else/For Statement
Source: https://docs.agent.ai/actions/end_statement



Mark the end of If/Else blocks or For loops - required to close conditional logic or iteration blocks.

<iframe width="560" height="315" src="https://www.youtube.com/embed/vG61oEyqDtQ?si=VA1yu9ouWYYhN7HD" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

Mark the end of conditional blocks - closes For Loops, If Conditions, and other control flow actions.

**Common uses:**

* Close every For Loop
* Close every If Condition
* Close every If/Else block
* Define the boundary of conditional actions

**Action type:** `end_condition`

***

## What This Does (The Simple Version)

Think of this like a closing bracket or parenthesis. When you open a For Loop or If Condition, you need to close it. End Condition tells the workflow "this is where the conditional block ends."

**Real-world example:**
You have a For Loop that updates 50 deals. The End Condition marks where the loop ends, so the workflow knows to jump back to the top and process the next deal, or continue to the next action if all deals are done.

***

## How It Works

The End Condition action closes any conditional block (For Loop, If Condition, If/Else). When the workflow reaches this action:

**For Loops:**

1. Checks if there are more items to process
2. If yes → Jumps back to For Loop, updates current item, runs actions again
3. If no → Exits and continues with actions after End Condition

**If Conditions:**

1. Marks where the "if true" actions end
2. Workflow continues with actions after End Condition

**If/Else Blocks:**

1. Marks where the entire if/else block ends
2. Workflow continues with actions after End Condition

**It's required** - every For Loop, If Condition, or If/Else must have a matching End Condition.

***

## Setting It Up

### When to Add It

Add the End Condition action **after all the actions inside your conditional block**.

### For Loops

**Structure:**

```
1. For Loop (start)
   - Loop through: target_deals
   - Current item: current_deal

2. Update HubSpot Object (repeats for each item)
3. Create Timeline Event (repeats for each item)

4. End Condition (marks the end of loop)

5. Send Email (runs once after loop finishes)
```

### If Conditions

**Structure:**

```
1. If Condition (check if deal amount > 10000)

2. Update HubSpot Object (runs only if condition is true)
3. Send Email (runs only if condition is true)

4. End Condition (marks the end of if block)

5. Log to Console (runs regardless of condition)
```

### If/Else Blocks

**Structure:**

```
1. If Condition (check if contact has email)

2. Send Email (runs if condition is true)

3. Else Condition (if condition is false)

4. Log to Console (runs if condition is false)

5. End Condition (marks the end of entire if/else block)

6. Update Contact (runs regardless of condition)
```

### How to Add It

When building your workflow:

1. Add your conditional action (For Loop, If Condition, etc.)
2. Add all the actions that should be inside that block
3. Add the **End Condition** action
4. (Optional) Add actions after End Condition that should run after the block

**No configuration needed** - End Condition has no settings to configure. Just add it to your workflow.

***

## What Happens at End Condition

### In a For Loop

**Loop continues:**

* If more items exist, current item variable updates and workflow jumps back
* All actions between For Loop and End Condition run again

**Loop exits:**

* If no more items, workflow continues with action after End Condition
* Loop variables no longer exist

### In an If Condition

**After true actions:**

* End Condition marks where the "if true" actions end
* Workflow continues with actions after End Condition
* If condition was false, these actions were skipped entirely

### In an If/Else Block

**After entire block:**

* End Condition marks where the entire if/else block ends
* Either the "if true" or "else" actions ran (never both)
* Workflow continues with actions after End Condition

***

## Common Workflows

### For Loop with End Condition

**Goal:** Update multiple deals and send confirmation when done

1. **Search HubSpot (V2)**
   * Find deals
   * Output Variable: `target_deals`

2. **For Loop**
   * Loop through: `target_deals`
   * Current item: `current_deal`

3. **Update HubSpot Object** (inside loop)
   * Update the deal

4. **End Condition** ← Closes the For Loop

5. **Send Email** (after loop)
   * Confirmation that all deals were updated

### If Condition with End Condition

**Goal:** Only update high-value deals

1. **Lookup HubSpot Object (V2)**
   * Get deal details
   * Output Variable: `deal`

2. **If Condition**
   * Check if `deal.properties.amount` > 10000

3. **Update HubSpot Object** (only runs if true)
   * Update the deal stage

4. **Send Email** (only runs if true)
   * Notify sales team

5. **End Condition** ← Closes the If Condition

6. **Log to Console** (runs regardless)
   * Log that workflow completed

### If/Else with End Condition

**Goal:** Send email if contact has email address, otherwise log

1. **Lookup HubSpot Object (V2)**
   * Get contact
   * Output Variable: `contact`

2. **If Condition**
   * Check if `contact.properties.email` is not empty

3. **Send Email** (runs if true)
   * Send to contact's email

4. **Else Condition**

5. **Log to Console** (runs if false)
   * Log "No email address found"

6. **End Condition** ← Closes the entire if/else block

7. **Update Contact** (runs regardless)
   * Update last contacted date

***

## Real Examples

### Loop with Count Tracking

**Scenario:** Update deals and count how many were updated

1. **Set Variable**
   * `count` = `0`

2. **Search HubSpot (V2)**
   * Output Variable: `deals`

3. **For Loop**
   * Loop through: `deals`
   * Current item: `current_deal`

4. **Update HubSpot Object**
   * Update deal

5. **Set Variable**
   * Increment `count`

6. **End Condition** ← Closes For Loop

7. **Send Email**
   * Subject: "Updated \[count] deals"

### Conditional Update

**Scenario:** Update contact only if they're in a specific lifecycle stage

1. **Lookup HubSpot Object (V2)**
   * Get contact
   * Output Variable: `contact`

2. **If Condition**
   * Check if `contact.properties.lifecycle_stage` equals "lead"

3. **Update HubSpot Object**
   * Set lifecycle\_stage to "marketingqualifiedlead"

4. **Create Timeline Event**
   * Log stage change

5. **End Condition** ← Closes If Condition

6. **Log to Console**
   * "Workflow complete"

***

## Troubleshooting

### "Missing End Condition" Error

**Error:** Conditional block without End Condition

**How to fix:**

1. After all actions inside your conditional block, add an **End Condition** action
2. Make sure there's exactly one End Condition for each conditional block
3. Check that End Condition is after all the actions you want inside the block

### Actions After End Condition Don't Run

**Actions after End Condition are skipped**

**Possible causes:**

1. Error inside conditional block stops execution
2. For Loop timeout

**How to fix:**

1. Check execution log for errors
2. Fix errors in actions inside the block
3. For loops: reduce item count to test

### Wrong Actions Repeating

**Actions outside the block are repeating (For Loop)**

**Possible causes:**

1. End Condition is in the wrong place (too far down)

**How to fix:**

1. Move End Condition to immediately after the last action you want repeated
2. Actions after End Condition should only run once

### If/Else Not Working as Expected

**Wrong branch is executing**

**Possible causes:**

1. End Condition missing or in wrong place
2. Else Condition missing

**How to fix:**

1. Structure should be: If Condition → \[true actions] → Else Condition → \[false actions] → End Condition
2. Make sure End Condition is after both branches

***

## Tips & Best Practices

**✅ Do:**

* Always add End Condition after every conditional block
* Place End Condition after all actions you want inside the block
* Use one End Condition per conditional block (For Loop, If, If/Else)
* Check execution log to verify blocks executed correctly

**❌ Don't:**

* Forget to add End Condition (conditional blocks won't work)
* Put End Condition in the middle of actions you want in the block
* Add multiple End Conditions for one conditional block
* Try to access loop variables after End Condition (they're gone)

**Structure tips:**

* Conditional actions and End Condition are like opening and closing brackets
* Everything between them is inside the block
* Everything after End Condition runs after the block completes
* Keep blocks simple - complex nested conditions are harder to debug

***

## Related Actions

**Always used together:**

* [For Loop](./for_loop) - Starts a loop (requires End Condition)
* [If Condition](./if_else) - Conditional execution (requires End Condition)
* [Set Variable](./set-variable) - Save data from inside blocks

**Related guides:**

* [Variable System](./builder/template-variables) - Understanding variable scope

***

**Last Updated:** 2025-10-01


# Enrich with Breeze Intelligence
Source: https://docs.agent.ai/actions/enrich_with_breeze_intelligence



## Overview

Gather enriched company data using Breeze Intelligence for deeper analysis and insights.

### Use Cases

* **Company Research**: Retrieve detailed information about a specific company for due diligence.
* **Sales and Marketing**: Enhance workflows with enriched data for targeted campaigns.

## Configuration Fields

### Domain Name

* **Description**: Enter the domain of the company to retrieve enriched data.
* **Example**: "hubspot.com" or "example.com."
* **Required**: Yes

### Output Variable Name

* **Description**: Assign a variable name to store the enriched company data.
* **Example**: "company\_info" or "enriched\_data."
* **Validation**: Only letters, numbers, and underscores (\_) are allowed.
* **Required**: Yes


# For Loop
Source: https://docs.agent.ai/actions/for_loop



Repeat actions for each item in a list or a specific number of times - automate repetitive tasks efficiently.

<iframe width="560" height="315" src="https://www.youtube.com/embed/3J3TKMJ4pXI?si=vFycP1JMoowvaJqe" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

Process multiple items one at a time - perfect for updating, analyzing, or taking action on lists of records.

**Common uses:**

* Loop through search results and update each record
* Process each contact in a list
* Analyze multiple deals one by one
* Send emails to a list of people

**Action type:** `for_condition`

***

## What This Does (The Simple Version)

Think of this like going through a stack of papers on your desk, one at a time. You pick up the first paper, do something with it, put it down, then pick up the next one. The loop continues until you've gone through the entire stack.

**Real-world example:**
You search HubSpot and find 50 deals in "Presentation Scheduled" stage. You want to update each one to the next stage. The For Loop lets you go through all 50 deals, one by one, and update each one.

***

## How It Works

This action repeats the actions inside the loop for each item in a list. You provide:

1. **What to loop through** (usually a list from a search action)
2. **What to call each item** (the variable name for the current item)

The loop automatically:

* Starts at the first item
* Runs all actions inside the loop
* Moves to the next item
* Repeats until all items are processed

***

## Setting It Up

### Step 1: Add a For Loop Action

When you add a For Loop action to your workflow, you'll see two main fields.

### Step 2: Choose What to Loop Through

In the **"Loop through"** field, click the `{}` button to select the list you want to process.

**Usually this is:**

* Search results from a **Search HubSpot (V2)** action
* A list from a previous action
* An array variable from your trigger

**Example:**

1. Earlier in your workflow, you ran **Search HubSpot (V2)** and saved results to `target_deals`
2. In the For Loop, click `{}` → select `target_deals`

**You can also type a number** to loop a specific number of times:

* Type `5` to loop 5 times
* Type `10` to loop 10 times
* Click `{}` to insert a variable containing a number

### Step 3: Name the Current Item

In the **"Current item variable"** field, type a name for the variable that will hold each item as you loop through.

**Good names:**

* If looping through deals: `current_deal`
* If looping through contacts: `current_contact`
* If looping through companies: `current_company`
* If looping through tickets: `current_ticket`

**This variable will change on each iteration** - first it's the 1st item, then the 2nd, then the 3rd, etc.

### Step 4: Add Actions Inside the Loop

After the For Loop action, add the actions you want to run for each item. These actions will execute once per item.

**Common actions inside loops:**

* **Update HubSpot Object (V2)** - Update the current record
* **Create Timeline Event (V2)** - Log an event on each record
* **If Condition** - Check something about the current item
* **Set Variable** - Calculate or store data

**Inside these actions**, use the current item variable by clicking `{}` and selecting it.

**Example:** Inside an Update HubSpot Object action:

* Object ID: Click `{}` → select `current_deal` → `hs_object_id`
* Properties: Update based on `current_deal` data

### Step 5: End the Loop

After all the actions you want repeated, add an **End Loop** action. This tells the workflow where the loop ends.

**The workflow structure looks like:**

1. Search HubSpot (V2) → saves to `target_deals`
2. **For Loop** → loop through `target_deals`, current item: `current_deal`
3. Update HubSpot Object (V2) → update `current_deal`
4. Create Timeline Event (V2) → log event on `current_deal`
5. **End Loop**
6. (Actions here run after the loop finishes)

***

## How Variables Work in Loops

### Current Item Variable

Each time through the loop, the current item variable gets updated with the next item.

**Example:** Looping through 3 deals saved to `target_deals`

**Iteration 1:**

```
current_deal = {
  "dealname": "Acme Corp Deal",
  "hs_object_id": "12345",
  "amount": "50000"
}
```

**Iteration 2:**

```
current_deal = {
  "dealname": "TechCo Deal",
  "hs_object_id": "67890",
  "amount": "25000"
}
```

**Iteration 3:**

```
current_deal = {
  "dealname": "BigBiz Deal",
  "hs_object_id": "11111",
  "amount": "100000"
}
```

**After the loop ends,** `current_deal` no longer exists (it's scoped to the loop only).

### Loop Index (Optional)

You can also track which iteration you're on with an index variable. This is automatic - you don't need to set it up.

**Usage:** In advanced scenarios, you might reference the loop index to know "I'm on item 5 of 50".

***

## Common Workflows

### Update All Deals in a Stage

**Goal:** Find all deals in a specific stage and move them to the next stage

1. **Search HubSpot (V2)**
   * Object Type: Deals
   * Search Filters: Click "+ Add Property"
     * Property: Deal Stage
     * Operator: Equals
     * Value: "presentationscheduled"
   * Retrieve Properties: Select `dealname`, `hs_object_id`
   * Output Variable: `deals_to_update`

2. **For Loop**
   * Loop through: Click `{}` → select `deals_to_update`
   * Current item variable: `current_deal`

3. **Update HubSpot Object (V2)** (inside loop)
   * Object Type: Deals
   * Identify by: Lookup by Object ID
   * Identifier: Click `{}` → `current_deal` → `hs_object_id`
   * Update Properties:
     * `dealstage`: "decisionmakerboughtin"
   * Output Variable: `updated_deal`

4. **End Loop**

### Send Email to Each Contact

**Goal:** Loop through a list of contacts and send each one a personalized email

1. **Search HubSpot (V2)**
   * Object Type: Contacts
   * Search Filters: (your criteria)
   * Retrieve Properties: Select `firstname`, `email`, `company`
   * Output Variable: `target_contacts`

2. **For Loop**
   * Loop through: Click `{}` → select `target_contacts`
   * Current item variable: `current_contact`

3. **Send Email** (inside loop)
   * To: Click `{}` → `current_contact` → `properties` → `email`
   * Subject: Type "Hi " then click `{}` → `current_contact` → `properties` → `firstname`
   * Body: Use personalized content with variables from `current_contact`

4. **End Loop**

### Log Timeline Events on Multiple Records

**Goal:** Create a timeline event on each deal in a list

1. **Search HubSpot (V2)**
   * Find your target deals
   * Output Variable: `opportunity_deals`

2. **For Loop**
   * Loop through: Click `{}` → select `opportunity_deals`
   * Current item variable: `deal`

3. **Create Timeline Event (V2)** (inside loop)
   * Object Type: Deals
   * Target Object ID: Click `{}` → `deal` → `hs_object_id`
   * Event Type: `opportunity_reviewed`
   * Event Title: Type "Deal Reviewed: " then click `{}` → `deal` → `properties` → `dealname`
   * Output Variable: `event_result`

4. **End Loop**

***

## Real Examples

### Deal Health Check Loop

**Scenario:** Every morning, find all deals in "Presentation Scheduled" stage and analyze each one.

**Trigger:** Scheduled (daily at 9:00 AM)

1. **Search HubSpot (V2)**
   * Object Type: Deals
   * Search Filters:
     * Property: Deal Stage
     * Operator: Equals
     * Value: "presentationscheduled"
   * Retrieve Properties: `dealname`, `hs_object_id`, `amount`, `closedate`
   * Output Variable: `active_deals`

2. **For Loop**
   * Loop through: `active_deals`
   * Current item variable: `current_deal`

3. **Get Timeline Events (V2)** (inside loop)
   * Object Type: Deals
   * Object ID: Click `{}` → `current_deal` → `hs_object_id`
   * Output Variable: `deal_events`

4. **If Condition** (inside loop)
   * Condition: Check if `deal_events` is empty (no recent activity)
   * If true: Update deal stage to "stalled"

5. **End Loop**

**Result:** All active deals are checked, and deals with no activity are flagged.

### Contact Enrichment Loop

**Scenario:** Enrich all new contacts with external data.

**Trigger:** Scheduled (daily at midnight)

1. **Search HubSpot (V2)**
   * Object Type: Contacts
   * Search Filters:
     * Property: Lifecycle Stage
     * Operator: Equals
     * Value: "lead"
   * Retrieve Properties: `email`, `firstname`, `lastname`, `hs_object_id`
   * Limit: 100
   * Output Variable: `new_leads`

2. **For Loop**
   * Loop through: `new_leads`
   * Current item variable: `lead`

3. **External API Call** (inside loop)
   * Lookup company data using `lead.properties.email`
   * Output Variable: `enrichment_data`

4. **Update HubSpot Object (V2)** (inside loop)
   * Object Type: Contacts
   * Identify by: Lookup by Object ID
   * Identifier: Click `{}` → `lead` → `hs_object_id`
   * Update Properties with enrichment data

5. **End Loop**

***

## Troubleshooting

### Loop Doesn't Run

**The loop actions are skipped completely**

**Possible causes:**

1. The list you're looping through is empty
2. Variable doesn't exist or is not a list
3. Loop count is 0

**How to fix:**

1. Check the execution log - what was the loop count?
2. Verify the search action returned results (check its output in the log)
3. Make sure you're using the correct variable name (the one from the search action's output variable)
4. Test your search manually in HubSpot to confirm records exist

### Loop Only Runs Once

**Loop processes only the first item then stops**

**Possible causes:**

1. Missing **End Loop** action
2. Error inside the loop on the 2nd iteration
3. Break condition triggered

**How to fix:**

1. Make sure you added an **End Loop** action after all loop body actions
2. Check execution log - did an error occur on iteration 2?
3. Fix any errors in actions inside the loop (they might work for some items but fail for others)

### Can't Access Loop Variable After Loop

**Error:** Variable `current_deal` not found (outside the loop)

**This is expected behavior** - loop variables only exist inside the loop.

**How to fix:**

1. If you need data from the loop later, use **Set Variable** inside the loop to save it
2. Save results to a list variable that persists after the loop

**Example:**
Inside loop:

* **Set Variable** → `all_updated_ids` → append `current_deal.hs_object_id`

After loop:

* Access `all_updated_ids` (still available)

### Loop Running Too Long

**Loop takes forever or times out**

**Possible causes:**

1. Looping through too many items (1000+)
2. Slow actions inside the loop (external API calls)
3. Nested loops (loop inside a loop)

**How to fix:**

1. Limit search results to smaller batches (100-500)
2. Optimize actions inside loop - remove unnecessary steps
3. Consider breaking into multiple workflows
4. Use result limits on your search action

***

## Tips & Best Practices

**✅ Do:**

* Always use **End Loop** to close the loop
* Use descriptive current item variable names (`current_deal` not `item`)
* Limit search results while testing (10-20 items to start)
* Check loop variable in execution log to see what's being processed
* Use **If Condition** inside loops to skip items that don't meet criteria

**❌ Don't:**

* Forget to add **End Loop** (loop won't work)
* Loop through thousands of items at once (use batches)
* Create variables inside loops without understanding scope (they'll be overwritten each iteration)
* Put slow external API calls inside loops without considering total time
* Access loop variables outside the loop (they won't exist)

**Performance tips:**

* Loops can handle 100-500 items comfortably
* Each action inside the loop adds to total time (5 actions × 100 items = 500 action executions)
* For large lists (1000+), consider splitting into multiple workflow runs
* Use search result limits to control loop size

***

## Related Actions

**What to use with loops:**

* [Search HubSpot (V2)](./hubspot-v2-search-objects) - Get lists to loop through
* [Update HubSpot Object (V2)](./hubspot-v2-update-object) - Update each record in loop
* [End Loop](./end_statement) - Required to close the loop
* [If Condition](./if_else) - Conditionally process items in loop

**Related guides:**

* [Variable System](./builder/template-variables) - Understanding variable scope in loops
* [Deal Analysis Workflow](./recipes/hubspot-deal-analysis) - Complete example with loops

***

**Last Updated:** 2025-10-01


# Format Text
Source: https://docs.agent.ai/actions/format_text



## Overview

Apply formatting to text, such as changing case, removing characters, or truncating, to prepare it for specific uses.

### Use Cases

* **Text Standardization**: Convert inputs to a consistent format.
* **Data Cleaning**: Remove unwanted characters or HTML from text.

## Configuration Fields

### Format Type

* **Description**: Select the type of formatting to apply.
* **Options**: Make Uppercase, Make Lowercase, Capitalize, Remove Characters, Trim Whitespace, Split Text By Delimiter, Join Text By Delimiter, Remove HTML, Truncate
* **Example**: "Make Uppercase" for standardizing text.
* **Required**: Yes

### Characters/Delimiter/Truncation Length

* **Description**: Specify the characters to remove or delimiter to split/join text, or length for truncation.
* **Example**: "@" to remove mentions or "5" for truncation length.
* **Required**: No

### Input Text

* **Description**: Enter the text to format.
* **Example**: "Hello, World!"
* **Required**: Yes

### Output Variable Name

* **Description**: Assign a variable name to store the formatted text.
* **Example**: "formatted\_text" or "cleaned\_data."
* **Validation**: Only letters, numbers, and underscores (\_) are allowed.
* **Required**: Yes


# Generate Image
Source: https://docs.agent.ai/actions/generate_image



## Overview

Create visually engaging images using AI models, with options for style, aspect ratio, and detailed prompts.

### Use Cases

* **Creative Design**: Generate digital art, illustrations, or concept visuals.
* **Marketing Campaigns**: Produce images for advertisements or social media posts.
* **Visualization**: Create representations of ideas or concepts.

## Configuration Fields

### Model

* **Description**: Select the AI model to generate images.
* **Options**: DALL-E 3, Playground v3, FLUX 1.1 Pro, Ideogram.
* **Example**: "DALL-E 3" for high-quality digital art.
* **Required**: Yes

### Style

* **Description**: Choose the style for the generated image.
* **Options**: Default, Photo, Digital Art, Illustration, Drawing.
* **Example**: "Digital Art" for a creative design.
* **Required**: Yes

### Aspect Ratio

* **Description**: Set the aspect ratio for the image.
* **Options**: 9:16, 1:1, 4:3, 16:9.
* **Example**: "16:9" for widescreen formats.
* **Required**: Yes

### Prompt

* **Description**: Enter a prompt to describe the image.
* **Example**: "A futuristic cityscape" or "A serene mountain lake at sunset."
* **Required**: Yes

### Output Variable Name

* **Description**: Provide a variable name to store the generated image.
* **Example**: "generated\_image" or "ai\_image."
* **Validation**: Only letters, numbers, and underscores (\_) are allowed.
* **Required**: Yes

***


# Get Bluesky Posts
Source: https://docs.agent.ai/actions/get_bluesky_posts



## Overview

Fetch recent posts from a specified Bluesky user handle, making it easy to monitor activity on the platform.

### Use Cases

* **Social Media Analysis**: Track a user's recent posts for sentiment analysis or topic extraction.
* **Competitor Insights**: Observe recent activity from competitors or key influencers.

## Configuration Fields

### User Handle

* **Description**: Enter the Bluesky handle to fetch posts from.
* **Example**: "jay.bsky.social."
* **Required**: Yes

### Number of Posts to Retrieve

* **Description**: Specify how many recent posts to fetch.
* **Options**: 1, 5, 10, 25, 50, 100
* **Required**: Yes

### Output Variable Name

* **Description**: Assign a variable name to store the retrieved posts.
* **Example**: "recent\_posts" or "bsky\_feed."
* **Validation**: Only letters, numbers, and underscores (\_) are allowed.
* **Required**: Yes


# Get Data from Builder's Knowledge Base
Source: https://docs.agent.ai/actions/get_data_from_builders_knowledgebase



## Overview

Fetch semantic search results from the builder's knowledge base, enabling you to use structured data for analysis and decision-making.

### Use Cases

* **Content Retrieval**: Search for specific information in a structured knowledge base, such as FAQs or product documentation.
* **Automated Assistance**: Power AI agents with relevant context from internal resources.

## Configuration Fields

### Query

* **Description**: Enter the search query to retrieve relevant knowledge base entries.
* **Example**: "Latest sales strategies" or "Integration instructions."
* **Required**: Yes

### Builder Knowledge Base to Use

* **Description**: Select the knowledge base to search from.
* **Example**: "Product Documentation" or "Employee Handbook."
* **Required**: Yes

### Max Number of Document Chunks to Retrieve

* **Description**: Specify the maximum number of document chunks to return.
* **Example**: "5" or "10."
* **Required**: Yes

### Qualitative Vector Score Cutoff for Semantic Search Cosine Similarity

* **Description**: Set the score threshold for search relevance.
* **Example**: "0.2" for broad results or "0.7" for precise matches.
* **Required**: Yes

### Output Variable Name

* **Description**: Assign a variable name to store the search results.
* **Example**: "knowledge\_base\_results" or "kb\_entries."
* **Validation**: Only letters, numbers, and underscores (\_) are allowed.
* **Required**: Yes


# Get Data from User's Uploaded Files
Source: https://docs.agent.ai/actions/get_data_from_users_uploaded_files



## Overview

Retrieve semantic search results from user-uploaded files for targeted information extraction.

### Use Cases

* **Data Analysis**: Quickly retrieve insights from reports or project files uploaded by users.
* **Customized Searches**: Provide tailored responses by extracting specific data from user-uploaded files.

## Configuration Fields

### Query

* **Description**: Enter the search query to find relevant information in uploaded files.
* **Example**: "Revenue breakdown" or "Budget overview."
* **Required**: Yes

### User Uploaded Files to Use

* **Description**: Specify which uploaded files to search within.
* **Example**: "Recent uploads" or "project\_documents."
* **Required**: Yes

### Max Number of Document Chunks to Retrieve

* **Description**: Set the maximum number of document chunks to return.
* **Example**: "5" or "10."
* **Required**: Yes

### Qualitative Vector Score Cutoff for Semantic Search Cosine Similarity

* **Description**: Adjust the score threshold for search relevance.
* **Example**: "0.2" for broad results or "0.5" for specific results.
* **Required**: Yes

### Output Variable Name

* **Description**: Assign a variable name to store the search results.
* **Example**: "file\_search\_results" or "upload\_data."
* **Validation**: Only letters, numbers, and underscores (\_) are allowed.
* **Required**: Yes


# Get Instagram Followers
Source: https://docs.agent.ai/actions/get_instagram_followers



## Overview

Retrieve a list of top followers from a specified Instagram account for social media analysis.

### Use Cases

* **Audience Insights**: Understand the followers of an Instagram account for marketing purposes.
* **Engagement Monitoring**: Track influential followers.

## Configuration Fields

### Instagram Username

* **Description**: Enter the Instagram username (without @) to fetch followers.
* **Example**: "fashionblogger123."
* **Required**: Yes

### Number of Top Followers

* **Description**: Select the number of top followers to retrieve.
* **Options**: 10, 20, 50, 100
* **Required**: Yes

### Output Variable Name

* **Description**: Assign a variable name to store the followers data.
* **Example**: "instagram\_followers" or "top\_followers."
* **Validation**: Only letters, numbers, and underscores (\_) are allowed.
* **Required**: Yes


# Get Instagram Profile
Source: https://docs.agent.ai/actions/get_instagram_profile



## Overview

Fetch detailed profile information for a specified Instagram username.

### Use Cases

* **Competitor Analysis**: Understand details of an Instagram profile for benchmarking.
* **Content Creation**: Identify influencers or collaborators.

## Configuration Fields

### Instagram Username

* **Description**: Enter the Instagram username (without @) to fetch profile details.
* **Example**: "travelguru."
* **Required**: Yes

### Output Variable Name

* **Description**: Assign a variable name to store the profile data.
* **Example**: "instagram\_profile" or "profile\_data."
* **Validation**: Only letters, numbers, and underscores (\_) are allowed.
* **Required**: Yes

***


# Get LinkedIn Activity
Source: https://docs.agent.ai/actions/get_linkedin_activity



## Overview

Retrieve recent LinkedIn posts from specified profiles to analyze professional activity and engagement.

### Use Cases

* **Recruitment**: Monitor LinkedIn activity for potential candidates.
* **Industry Trends**: Analyze posts for emerging topics.

## Configuration Fields

### LinkedIn Profile URLs

* **Description**: Enter one or more LinkedIn profile URLs, each on a new line.
* **Example**: "[https://linkedin.com/in/janedoe](https://linkedin.com/in/janedoe)."
* **Required**: Yes

### Number of Posts to Retrieve

* **Description**: Specify how many recent posts to fetch from each profile.
* **Options**: 1, 5, 10, 25, 50, 100
* **Required**: Yes

### Output Variable Name

* **Description**: Assign a variable name to store LinkedIn activity data.
* **Example**: "linkedin\_activity" or "recent\_posts."
* **Validation**: Only letters, numbers, and underscores (\_) are allowed.
* **Required**: Yes


# Get LinkedIn Profile
Source: https://docs.agent.ai/actions/get_linkedin_profile



## Overview

Retrieve detailed information from a specified LinkedIn profile for professional insights.

### Use Cases

* **Candidate Research**: Gather details about a LinkedIn profile for recruitment.
* **Lead Generation**: Analyze profiles for sales and marketing.

## Configuration Fields

### Profile Handle

* **Description**: Enter the LinkedIn profile handle to retrieve details.
* **Example**: "[https://linkedin.com/in/johndoe](https://linkedin.com/in/johndoe)."
* **Required**: Yes

### Output Variable Name

* **Description**: Assign a variable name to store the LinkedIn profile data.
* **Example**: "linkedin\_profile" or "professional\_info."
* **Validation**: Only letters, numbers, and underscores (\_) are allowed.
* **Required**: Yes


# Get Recent Tweets
Source: https://docs.agent.ai/actions/get_recent_tweets



## Overview

Fetch recent tweets from a specified Twitter handle, enabling social media tracking and analysis.

### Use Cases

* **Real-time Monitoring**: Track the latest activity from a key influencer or competitor.
* **Sentiment Analysis**: Analyze recent tweets for tone and sentiment.

## Configuration Fields

### Twitter Handle

* **Description**: Enter the Twitter handle to fetch tweets from (without the @ symbol).
* **Example**: "elonmusk."
* **Required**: Yes

### Number of Tweets to Retrieve

* **Description**: Specify how many recent tweets to fetch.
* **Options**: 1, 5, 10, 25, 50, 100
* **Required**: Yes

### Output Variable Name

* **Description**: Assign a variable name to store the retrieved tweets.
* **Example**: "recent\_tweets" or "tweet\_feed."
* **Validation**: Only letters, numbers, and underscores (\_) are allowed.
* **Required**: Yes


# Get Twitter Users
Source: https://docs.agent.ai/actions/get_twitter_users



## Overview

Search and retrieve Twitter user profiles based on specific keywords for targeted social media analysis.

### Use Cases

* **Influencer Marketing**: Identify key Twitter users for promotional campaigns.
* **Competitor Research**: Find relevant profiles in your industry.

## Configuration Fields

### Search Keywords

* **Description**: Enter keywords to find relevant Twitter users.
* **Example**: "AI experts" or "marketing influencers."
* **Required**: Yes

### Number of Users to Retrieve

* **Description**: Specify how many user profiles to retrieve.
* **Options**: 1, 5, 10, 25, 50, 100
* **Required**: Yes

### Output Variable Name

* **Description**: Assign a variable name to store the retrieved Twitter users.
* **Example**: "twitter\_users" or "social\_media\_profiles."
* **Validation**: Only letters, numbers, and underscores (\_) are allowed.
* **Required**: Yes


# Get User File
Source: https://docs.agent.ai/actions/get_user_file



## Overview

The "Get User File" action allows users to upload files for processing, storage, or review.

<Info>
  Most common file types—including `.pdf`, `.txt`, and `.csv`—are supported.\
  Improved CSV handling for Claude Sonnet was introduced in July 2025 to increase reliability with structured data inputs.
</Info>

### Use Cases

* **Resume Collection**: Upload resumes in PDF format.
* **File Processing**: Gather data files for analysis.
* **Document Submission**: Collect required documentation from users.

## Configuration Fields

### User Prompt

* **Description**: Provide clear instructions for users to upload files.
* **Example**: "Upload your resume as a PDF."
* **Required**: Yes

### Required?

* **Description**: Mark this checkbox if file upload is necessary for the workflow to proceed.
* **Required**: No

### Output Variable Name

* **Description**: Assign a variable name for the uploaded files.
* **Example**: "user\_documents" or "uploaded\_images."
* **Validation**:
  * Only letters, numbers, and underscores (\_) are allowed.
  * No spaces, special characters, or dashes.
  * **Regex**: `^[a-zA-Z0-9_]+$`
* **Hint**: This variable will be used to reference the files in subsequent steps.
* **Required**: Yes

### Show Only Files Uploaded in the Current Session

* **Description**: Restrict access to files uploaded only during the current session.
* **Required**: No


# Get User Input
Source: https://docs.agent.ai/actions/get_user_input



## Overview

The "Get User Input" action allows you to capture dynamic responses from users, such as text, numbers, URLs, and dropdown selections. This action is essential for workflows that require specific input from users to proceed.

### Use Cases

* **Survey Form**: Collect user preferences or feedback.
* **Authentication**: Prompt for email addresses or verification codes.
* **Customized Workflow**: Ask users to select options to determine the next steps.

## Configuration Fields

### Input Type

* **Description**: Choose the type of input you want to capture from the user.
* **Options**:
  * **Text**: Open-ended text input.
  * **Number**: Numeric input only.
  * **Yes/No**: Binary selection.
  * **Textarea**: Multi-line text input.
  * **URL**: Input limited to URLs.
  * **Website Domain**: Input limited to domains.
  * **Dropdown (single)**: Single selection from a dropdown.
  * **Dropdown (multiple)**: Multiple selections from a dropdown.
  * **Multi-Item Selector**: Allows selecting multiple items.
  * **Multi-Item Selector (Table View)**: Allows selecting multiple items in a table view.
  * **Radio Select (single)**: Single selection using radio buttons.
  * **HubSpot Portal**: Select a portal.
  * **HubSpot Company**: Select a company.
  * **Knowledge Base**: Select a knowledge base.
* **Hint**: Select the appropriate input type based on your data collection needs. For example, use "Text" for open-ended input or "Yes/No" for binary responses.
* **Required**: Yes

### User Prompt

* **Description**: Write a clear prompt to guide users on what information is required.
* **Example**: "Please enter your email address" or "Select your preferred contact method."
* **Required**: Yes

### Default Value

* **Description**: Provide a default response that appears automatically in the input field.
* **Example**: "[example@domain.com](mailto:example@domain.com)" for an email field.
* **Hint**: Use this field to pre-fill common or expected responses to simplify input for users.
* **Required**: No

### Required?

* **Description**: Mark this checkbox if this input is mandatory.
* **Example**: Enable if a response is essential to proceed in the workflow.
* **Required**: No

### Output Variable Name

* **Description**: Assign a unique variable name for the input value.
* **Example**: "user\_email" or "preferred\_contact."
* **Validation**:
  * Only letters, numbers, and underscores (\_) are allowed.
  * No spaces, special characters, or dashes.
  * **Regex**: `^[a-zA-Z0-9_]+$`
* **Hint**: This variable will be used to reference the input value in subsequent steps.
* **Required**: Yes


# Get User KBs and Files
Source: https://docs.agent.ai/actions/get_user_knowledge_base_and_files



## Overview

The "Get User Knowledge Base and Files" action retrieves information from user-selected knowledge bases and uploaded files to support decision-making within the workflow.

### Use Cases

* **Content Search**: Allow users to select a knowledge base to search from.
* **Resource Management**: Link workflows to specific user-uploaded files.

## Configuration Fields

### User Prompt

* **Description**: Provide a prompt for users to select a knowledge base.
* **Example**: "Choose the knowledge base to search from."
* **Required**: Yes

### Required?

* **Description**: Mark as required if selecting a knowledge base is essential for the workflow.
* **Required**: No

### Output Variable Name

* **Description**: Assign a variable name to store the knowledge base ID.
* **Example**: "selected\_kb" or "kb\_source."
* **Validation**:
  * Only letters, numbers, and underscores (\_) are allowed.
  * No spaces, special characters, or dashes.
  * **Regex**: `^[a-zA-Z0-9_]+$`
* **Hint**: This variable will be used to reference the knowledge base in subsequent steps.
* **Required**: Yes


# Get User List
Source: https://docs.agent.ai/actions/get_user_list



## Overview

The "Get User List" action collects a list of items entered by users and splits them based on a specified delimiter or newline.

### Use Cases

* **Batch Data Input**: Gather a list of email addresses or item names.
* **Bulk Selection**: Allow users to input multiple options in one field.

## Configuration Fields

### User Prompt

* **Description**: Write a clear prompt to guide users on what information is required.
* **Example**: "Enter the list of email addresses separated by commas."
* **Required**: Yes

### List Delimiter (leave blank for newline)

* **Description**: Specify the character that separates the list items.
* **Example**: Use a comma (,) for "item1,item2,item3" or leave blank for newlines.
* **Required**: No

### Required?

* **Description**: Mark this checkbox if this input is mandatory.
* **Example**: Enable if a response is essential to proceed in the workflow.
* **Required**: No

### Output Variable Name

* **Description**: Assign a unique variable name for the input value.
* **Example**: "email\_list" or "item\_names."
* **Validation**:
  * Only letters, numbers, and underscores (\_) are allowed.
  * No spaces, special characters, or dashes.
  * **Regex**: `^[a-zA-Z0-9_]+$`
* **Hint**: This variable will be used to reference the list in subsequent steps.
* **Required**: Yes


# Get Variable from Database
Source: https://docs.agent.ai/actions/get_variable_from_database



## Overview

Retrieve stored variables from the agent's database for use in workflows.

### Use Cases

* **Data Reuse**: Leverage previously stored variables for decision-making.
* **Trend Analysis**: Access historical data for analysis.

## Configuration Fields

### Variable

* **Description**: Specify the variable to retrieve from the database.
* **Example**: "user\_input" or "order\_status."
* **Required**: Yes

### Retrieval Depth

* **Description**: Choose how far back to retrieve the data.
* **Options**: Most Recent Value, Historical Values
* **Example**: "Most Recent Value" for the latest data.
* **Required**: Yes

### Historical Data Interval (optional)

* **Description**: Define the interval for historical data retrieval.
* **Options**: Hour, Day, Week, Month, All Time
* **Example**: "Last 7 Days" for weekly data.
* **Required**: No

### Number of Items to Retrieve (optional)

* **Description**: Enter the number of items to retrieve from historical data.
* **Example**: "10" to fetch the last 10 entries.
* **Required**: No

### Output Variable Name

* **Description**: Assign a variable name to store the retrieved data.
* **Example**: "tracked\_values" or "historical\_data."
* **Validation**: Only letters, numbers, and underscores (\_) are allowed.
* **Required**: Yes


# Google News Data
Source: https://docs.agent.ai/actions/google_news_data



## Overview

Fetch news articles based on queries and date ranges to stay updated on relevant topics or trends.

### Use Cases

* **Market Analysis**: Track news articles for industry trends.
* **Brand Monitoring**: Stay updated on mentions of your company or competitors.

## Configuration Fields

### Query

* **Description**: Enter search terms to find news articles.
* **Example**: "AI advancements" or "global market trends."
* **Required**: Yes

### Since

* **Description**: Select the timeframe for news articles.
* **Options**: Last 24 hours, 7 days, 30 days, 90 days
* **Required**: Yes

### Location

* **Description**: Specify a location to filter news results (optional).
* **Example**: "New York" or "London."
* **Required**: No

### Output Variable Name

* **Description**: Assign a variable name to store the news data.
* **Example**: "news\_data" or "articles."
* **Validation**: Only letters, numbers, and underscores (\_) are allowed.
* **Required**: Yes


# Create Engagement
Source: https://docs.agent.ai/actions/hubspot-v2-create-engagement



Log calls, emails, meetings, notes, and tasks to HubSpot records - create engagement records programmatically.

**Common uses:**

* Log external calls to HubSpot
* Create notes from AI analysis
* Schedule follow-up tasks
* Record meetings from other systems
* Track email outreach

**Action type:** `hubspot.v2.create_engagement`

***

## What This Does (The Simple Version)

Think of this like adding an entry to someone's activity log. When your team calls, emails, or meets with someone, HubSpot tracks it as an "engagement". This action creates those engagement records from your workflows.

**Real-world example:**
After an AI analyzes a deal and generates insights, you want to log those insights as a note on the deal. This action creates a note engagement with the AI's analysis, visible in HubSpot's timeline.

***

## How It Works

This action creates engagement records (calls, emails, meetings, notes, tasks) in HubSpot. You specify:

1. **Engagement type** (call, email, meeting, note, task)
2. **Content** (body/description of the engagement)
3. **Who/what it's about** (associated contact, deal, company)
4. **Additional details** (title, duration, status, etc.)

The engagement appears in HubSpot on the associated record's timeline.

***

## Setting It Up

### Step 1: Choose Engagement Type

Select which type of engagement to create:

* **Note** - Add notes/comments
* **Call** - Log phone calls
* **Email** - Record email communications
* **Meeting** - Log meetings
* **Task** - Create tasks

**Choose from dropdown:** Engagement Type

### Step 2: Add Content (Required)

In the **"Content/Body"** field, enter the main content.

**This is the description/body of the engagement.**

**You can:**

* Type directly
* Click `{}` to insert variables
* Mix text and variables

**Examples:**

**For notes:**

```
AI Analysis: [insert deal_insights variable]
```

**For calls:**

```
Discussed [deal name] with [contact first name]. Next steps: [next actions]
```

**For tasks:**

```
Follow up on deal [deal name] - review proposal and schedule demo
```

### Step 3: Add Title/Subject (Optional)

In the **"Title/Subject"** field, add a title.

**Different engagement types use this differently:**

* **Note:** Note title
* **Call:** Call title
* **Email:** Email subject
* **Meeting:** Meeting title
* **Task:** Task subject

**Example:**

```
Discovery Call - [company_name]
```

### Step 4: Add Associations (Required)

In the **"Associations"** field, specify which records this engagement relates to.

**Format:** One per line: `object_type:object_id`

**Example:**

```
contact:[contact_id]
deal:[deal_record.id]
company:[company_id]
```

**Common patterns:**

**Associate with contact from lookup:**

```
contact:[contact_data.id]
```

**Associate with deal from search:**

```
deal:[current_deal.hs_object_id]
```

**Associate with multiple:**

```
contact:[contact_id]
deal:[deal_id]
```

### Step 5: Add Type-Specific Details (Optional)

Depending on engagement type, additional fields appear:

**For calls:**

* **Duration:** Call length in minutes (e.g., `30`)
* **Status:** Call outcome (e.g., `Connected`, `No Answer`, `Left Voicemail`)

**For meetings:**

* **Duration:** Meeting length in minutes (e.g., `60`)
* **Status:** Meeting outcome (e.g., `Scheduled`, `Completed`, `Rescheduled`)

**For tasks:**

* **Status:** Task status (e.g., `NOT_STARTED`, `IN_PROGRESS`, `COMPLETED`)
* **Priority:** Task priority (e.g., `HIGH`, `MEDIUM`, `LOW`)

**For emails:**

* **Status:** Email status (e.g., `SENT`, `SCHEDULED`)

### Step 6: Additional Properties (Optional)

In the **"Additional Properties"** field, add custom engagement properties.

**Format:** Key-value pairs, one per line:

```
property_name=value
another_property=another_value
```

**Or JSON:**

```json  theme={null}
{
  "custom_field": "value",
  "another_field": "[variable]"
}
```

### Step 7: Name Output Variable

In the **"Output Variable Name"** field, name the created engagement.

**Good names:**

* `created_note`
* `logged_call`
* `scheduled_task`
* `meeting_record`

**Default:** `created_engagement`

***

## What You Get Back

The action returns the created engagement record.

**Example output saved to `created_note`:**

```javascript  theme={null}
{
  "id": "123456789",
  "engagement_type": "note",
  "properties": {
    "hs_note_body": "AI Analysis: Deal shows strong engagement...",
    "hs_note_title": "Deal Health Analysis",
    "hs_timestamp": "2025-01-15T14:30:00Z",
    "hs_created_at": "2025-01-15T14:30:00Z"
  },
  "createdAt": "2025-01-15T14:30:00Z",
  "updatedAt": "2025-01-15T14:30:00Z"
}
```

**What's included:**

* `id` - Engagement ID
* `engagement_type` - Type you created
* `properties` - Engagement properties
* `createdAt` - When created

***

## Common Workflows

### Log AI Insights as Notes

**Goal:** Create notes with AI analysis results

1. **Lookup HubSpot Object (V2)**
   * Get deal
   * Output Variable: `deal_record`

2. **Get Timeline Events (V2)**
   * Get deal history
   * Output Variable: `deal_timeline`

3. **Invoke LLM**
   * Prompt: "Analyze \[deal\_record] and \[deal\_timeline]"
   * Output Variable: `insights`

4. **Create Engagement (V2)**
   * Engagement Type: Note
   * Content/Body: Click `{}` → `insights`
   * Title/Subject: "AI Deal Analysis"
   * Associations: `deal:[deal_record.id]`
   * Output Variable: `analysis_note`

### Log External Calls

**Goal:** Record calls from external phone system

1. **Webhook receives:**
   * `contact_id`
   * `call_duration`
   * `call_notes`
   * `call_outcome`

2. **Create Engagement (V2)**
   * Engagement Type: Call
   * Content/Body: Click `{}` → `call_notes`
   * Title/Subject: Type "Outbound Sales Call"
   * Duration: Click `{}` → `call_duration`
   * Status: Click `{}` → `call_outcome`
   * Associations: `contact:[contact_id]`

### Create Follow-Up Tasks

**Goal:** Create tasks after enrichment

1. **Search HubSpot (V2)**
   * Find high-priority leads
   * Output Variable: `priority_leads`

2. **For Loop**
   * Loop through: `priority_leads`
   * Current item: `current_lead`

3. **Create Engagement (V2)** (inside loop)
   * Engagement Type: Task
   * Content/Body: Type "Review enrichment data and reach out to " then click `{}` → `current_lead` → `properties` → `firstname`
   * Title/Subject: "Follow-up: High Priority Lead"
   * Status: `NOT_STARTED`
   * Priority: `HIGH`
   * Associations: `contact:[current_lead.hs_object_id]`

4. **End Loop**

***

## Real Examples

### Post-Analysis Note

**Scenario:** After AI analyzes deal health, log insights

**Configuration:**

* **Engagement Type:** Note
* **Content/Body:** `[deal_health_analysis]`
* **Title/Subject:** "Automated Health Check"
* **Associations:** `deal:[deal_id]`

**Result:** Note appears on deal timeline with AI insights

### External Call Logging

**Scenario:** Phone system sends webhook after calls

**Webhook payload:**

```json  theme={null}
{
  "contact_id": "123456",
  "duration_minutes": "15",
  "outcome": "Connected",
  "notes": "Discussed pricing, sending proposal"
}
```

**Configuration:**

* **Engagement Type:** Call
* **Content/Body:** `[notes]`
* **Title/Subject:** "Sales Call"
* **Duration:** `[duration_minutes]`
* **Status:** `[outcome]`
* **Associations:** `contact:[contact_id]`

**Result:** Call logged to contact with all details

### Automated Task Creation

**Scenario:** Create task when deal reaches certain stage

**Trigger:** Webhook when deal stage = "Decision Stage"

**Configuration:**

* **Engagement Type:** Task
* **Content/Body:** "Review decision criteria with \[contact\_name] and address any concerns"
* **Title/Subject:** "Decision Stage Follow-up"
* **Status:** `NOT_STARTED`
* **Priority:** `HIGH`
* **Associations:** `deal:[deal_id]\ncontact:[primary_contact_id]`

**Result:** High-priority task created for sales rep

***

## Troubleshooting

### Missing Associations Error

**"Associations are required" error**

**Possible causes:**

1. Associations field empty
2. Wrong format
3. Invalid object ID

**How to fix:**

1. Add at least one association: `contact:[contact_id]`
2. Use format: `object_type:object_id` (one per line)
3. Verify object IDs are valid HubSpot IDs
4. Check execution log for exact error

### Engagement Not Appearing

**Created but can't find in HubSpot**

**Possible causes:**

1. Associated with wrong record
2. Looking at wrong record type
3. Timeline filter hiding it

**How to fix:**

1. Check associations - verify correct record ID
2. Check execution log - see which ID was used
3. In HubSpot timeline, clear filters
4. Search for engagement by ID in execution log

### Duration Not Saving

**Duration field ignored**

**Possible causes:**

1. Wrong format (needs minutes)
2. Non-numeric value
3. Only applies to calls/meetings

**How to fix:**

1. Use number of minutes: `30` not `30 minutes`
2. Ensure numeric value: `[duration]` must resolve to number
3. Duration only works for calls and meetings

### Status Invalid

**Status value rejected**

**Possible causes:**

1. Invalid status for engagement type
2. Custom status not recognized

**How to fix:**

1. Use standard values:
   * Calls: `Connected`, `No Answer`, `Left Voicemail`, `Busy`
   * Meetings: `Scheduled`, `Completed`, `Rescheduled`, `Canceled`
   * Tasks: `NOT_STARTED`, `IN_PROGRESS`, `COMPLETED`, `WAITING`, `DEFERRED`
   * Emails: `SENT`, `SCHEDULED`, `BOUNCED`, `FAILED`
2. Check HubSpot settings for custom values

***

## Tips & Best Practices

**✅ Do:**

* Always include meaningful content/body
* Associate with relevant records (contact, deal, company)
* Use descriptive titles/subjects
* Include duration for calls and meetings (helps reporting)
* Set task priority for action items
* Use variables to make content dynamic
* Log AI insights as notes for context

**❌ Don't:**

* Create engagements without associations (required)
* Leave content/body empty
* Use invalid status values
* Forget duration is in minutes (not seconds/hours)
* Create duplicate engagements (check if exists first)
* Log sensitive information in engagements

**Performance tips:**

* Creating engagement takes \~1-2 seconds
* No limit on engagements created
* Bulk creation: use loops with rate limiting

**Engagement type selection:**

* **Notes:** AI insights, analysis results, internal comments
* **Calls:** Phone conversations (manual or from phone system)
* **Emails:** Email outreach (if not using HubSpot email)
* **Meetings:** Meeting records from external calendars
* **Tasks:** Follow-up actions, reminders, to-dos

***

## Related Actions

**Before creating engagement:**

* [Lookup HubSpot Object (V2)](./hubspot-v2-lookup-object) - Get record to associate
* [Search HubSpot (V2)](./hubspot-v2-search-objects) - Find records to log engagements on

**After creating engagement:**

* [Get Engagements (V2)](./hubspot-v2-get-engagements) - Retrieve engagements later
* [Update HubSpot Object (V2)](./hubspot-v2-update-object) - Update associated record

**Related actions:**

* [Create Timeline Event (V2)](./hubspot-v2-create-timeline-event) - Custom timeline events (different from engagements)
* [For Loop](./for_loop) - Create multiple engagements

**Related workflows:**

* [HubSpot Customer Onboarding](../recipes/hubspot-customer-onboarding) - Uses engagements for context

***

**Last Updated:** 2025-10-01


# Create HubSpot Object
Source: https://docs.agent.ai/actions/hubspot-v2-create-object



Create new contacts, deals, companies, and other HubSpot records from your workflows.

**Common uses:**

* Create contacts from form submissions
* Generate deals when opportunities arise
* Add companies from enrichment data
* Create tickets from customer requests

**Action type:** `hubspot.v2.create_object`

***

## What This Does (The Simple Version)

Think of this like adding a new contact to your phone. You choose what type of record to create (contact, company, deal, etc.), fill in the details, and save it to HubSpot.

**Real-world example:**
Someone fills out a "Request Demo" form on your website. You use this action to create a new contact in HubSpot with their name, email, company, and set their lifecycle stage to "Lead". You can even link them to an existing company record.

***

## How It Works

This action creates a brand new record in your HubSpot CRM. You choose:

1. **What type** of record to create (contact, deal, company, etc.)
2. **Which properties** to set
3. **What values** to use (typed values or variables from previous actions)

The new record is saved to a variable containing the HubSpot ID and all properties you set.

***

## Setting It Up

### Step 1: Choose Object Type

When you add the Create HubSpot Object action, you'll see clickable cards for each object type:

* **Contacts** - People in your CRM
* **Companies** - Organizations
* **Deals** - Sales opportunities
* **Tickets** - Support tickets
* **Calls** - Call records
* **Emails** - Email engagement records
* **Meetings** - Meeting records
* **Notes** - Notes attached to records
* **Tasks** - Tasks in HubSpot

**Click the card** for the type you want to create.

### Step 2: Add Properties

In the **"Contacts Object Properties"** section (or "Deals Object Properties", etc.), click the **"+ Add Property"** button to select which properties you want to set on the new record.

**This opens a property picker modal showing:**

* Search bar at the top
* List of all available properties for that object type
* Click properties to select them (they'll show a checkmark)
* Click **Done** when finished

**After closing the modal**, you'll see individual input fields for each property you selected.

**For each property:**

* The field is labeled with the property name (e.g., "First Name", "Email", "Company Name")
* Type the value directly, OR
* Hover over the field to see the `{}` button, then click it to insert a variable

**Example - Creating a contact:**

1. Click "+ Add Property"
2. Select `firstname`, `lastname`, `email`, `company`, `lifecycle_stage`
3. Click Done
4. Now you see five fields:
   * **First Name**: Click `{}` → select `first_name` (from webhook)
   * **Last Name**: Click `{}` → select `last_name` (from webhook)
   * **Email**: Click `{}` → select `email` (from webhook)
   * **Company**: Click `{}` → select `company_name` (from webhook)
   * **Lifecycle Stage**: Type "lead"

**Required properties:**
Different object types require different properties. Common requirements:

* **Contacts:** Usually just `email` (but best to include `firstname` and `lastname` too)
* **Companies:** Usually just `name` or `domain`
* **Deals:** Usually `dealname` and `pipeline` and `dealstage`
* **Tickets:** Usually `subject` and `hs_pipeline` and `hs_pipeline_stage`

**Tips:**

* Use the property picker to see all available properties and avoid typos
* Click `{}` to insert variables from triggers or previous actions
* HubSpot will use default values for properties you don't set

### Step 3: Name Your Output Variable

Give the created record a descriptive name in the **"Output Variable Name"** field.

**Good names:**

* `created_contact`
* `new_deal`
* `new_ticket`
* `contact_record`

This variable contains the new record with its HubSpot ID and all properties.

***

## What You Get Back

The action returns the **complete created object** with all its properties, including the HubSpot-generated ID.

**Example:** If you created a contact with `firstname`, `lastname`, `email`:

**Output saved to `created_contact`:**

```
{
  "id": "67890",
  "properties": {
    "firstname": "Jane",
    "lastname": "Smith",
    "email": "jane@example.com",
    "createdate": "2025-10-01T14:30:00Z",
    "hs_object_id": "67890"
  },
  "createdAt": "2025-10-01T14:30:00Z",
  "archived": false
}
```

**The `id` field is the HubSpot Object ID** - save this if you need to update or reference this record later.

***

## Using the Results

### Access the New Record's ID

The most common use is getting the HubSpot ID to use in later actions:

**In any field that accepts variables:**

* Click the **Insert Variable** button (`{}` icon)
* Navigate to your output variable (e.g., `created_contact`)
* Select `id` or `properties` → `hs_object_id` (they're the same)

**Example:** Create a deal associated with the new contact

1. **Create HubSpot Object (V2)** - Create contact, output: `created_contact`
2. **Create HubSpot Object (V2)** - Create deal:
   * Set deal properties (dealname, dealstage, etc.)
   * In associations field: Type `contact:` then click `{}` → `created_contact` → `id`

### Access Other Properties

You can access any property from the created record:

* Click `{}` → `created_contact` → `properties` → `email`
* Click `{}` → `created_contact` → `properties` → `createdate`

### Check If Creation Succeeded

The creation either succeeds (returns the full record) or throws an error. If required properties are missing or credentials are wrong, the workflow stops with an error message.

***

## Common Workflows

### Create Contact from Form

**Goal:** When someone submits a form, create a contact in HubSpot

**Trigger:** Webhook from website form

**Webhook receives:** `first_name`, `last_name`, `email`, `company` variables

1. **Create HubSpot Object (V2)**
   * Object Type: Contacts
   * Properties: Click "+ Add Property" and select:
     * `firstname`: Click `{}` → select `first_name`
     * `lastname`: Click `{}` → select `last_name`
     * `email`: Click `{}` → select `email`
     * `company`: Click `{}` → select `company`
     * `lifecycle_stage`: Type "lead"
   * Output Variable: `created_contact`

2. **Send confirmation email** using `created_contact` data...

### Create Deal for New Contact

**Goal:** After creating a contact, automatically create a deal for them

1. **Create HubSpot Object (V2)** - Create contact
   * Object Type: Contacts
   * Properties: Set `firstname`, `lastname`, `email`
   * Output Variable: `new_contact`

2. **Create HubSpot Object (V2)** - Create deal
   * Object Type: Deals
   * Properties: Click "+ Add Property" and select:
     * `dealname`: Type "New Opportunity - " then click `{}` → `new_contact` → `properties` → `firstname`
     * `dealstage`: Type "appointmentscheduled"
     * `pipeline`: Type "default"
     * `amount`: Type "5000"
   * Output Variable: `new_deal`

3. **Associate them** (if needed) using Update or Association action...

### Create Company from Enrichment

**Goal:** Look up company data and create a company record

**Trigger:** Manual or webhook with company domain

1. **Enrich Company Data** (external API action)
   * Domain: `acme.com`
   * Output Variable: `company_data`

2. **Create HubSpot Object (V2)**
   * Object Type: Companies
   * Properties: Click "+ Add Property" and select:
     * `name`: Click `{}` → `company_data` → `name`
     * `domain`: Click `{}` → `company_data` → `domain`
     * `industry`: Click `{}` → `company_data` → `industry`
     * `numberofemployees`: Click `{}` → `company_data` → `employee_count`
   * Output Variable: `created_company`

***

## Real Examples

### Lead Capture Workflow

**Scenario:** Website visitor submits "Download Whitepaper" form, create contact and mark as MQL.

**Webhook receives:** `email`, `first_name`, `last_name`, `phone` variables

**Create Configuration:**

* **Object Type:** Contacts
* **Properties:** Click "+ Add Property" and select:
  * `email`: Click `{}` → select `email`
  * `firstname`: Click `{}` → select `first_name`
  * `lastname`: Click `{}` → select `last_name`
  * `phone`: Click `{}` → select `phone`
  * `lifecycle_stage`: "marketingqualifiedlead"
  * `lead_source`: "Whitepaper Download"
* **Output Variable:** `new_lead`

**Next steps:** Send whitepaper download link to `new_lead.properties.email`.

### New Deal from Opportunity

**Scenario:** Sales rep fills out "New Opportunity" form, create deal with their info.

**Webhook receives:** `deal_name`, `contact_email`, `amount`, `close_date` variables

**Create Configuration:**

* **Object Type:** Deals
* **Properties:** Click "+ Add Property" and select:
  * `dealname`: Click `{}` → select `deal_name`
  * `amount`: Click `{}` → select `amount`
  * `closedate`: Click `{}` → select `close_date`
  * `dealstage`: "qualifiedtobuy"
  * `pipeline`: "default"
  * `deal_source`: "Sales Generated"
* **Output Variable:** `new_deal`

**Next steps:** Look up contact by `contact_email` and associate with `new_deal`.

***

## Troubleshooting

### "Missing Required Property" Error

**Error:** "Property 'email' is required" or similar

**Possible causes:**

1. Required property not selected in property picker
2. Required property field left empty
3. Variable inserted but it has no value

**How to fix:**

1. Click "+ Add Property" and select all required properties for that object type
2. Fill in values for all required fields
3. Check that variables you inserted actually have values (check execution log)
4. For contacts: always include `email`
5. For companies: always include `name` or `domain`
6. For deals: always include `dealname`, `pipeline`, `dealstage`

### "Property Does Not Exist" Error

**Error:** "Property 'custom\_field' does not exist"

**Possible causes:**

1. Property name is misspelled
2. Property doesn't exist in your HubSpot account
3. Property exists but not for that object type

**How to fix:**

1. Always use the "+ Add Property" button (shows only valid properties)
2. Go to HubSpot → Settings → Properties to verify the property exists
3. Make sure you're creating the right object type for that property
4. Custom properties must be created in HubSpot first

### "Missing OAuth Scope" Error

**You don't have permission to create that object type**

**How to fix:**

1. Go to Settings → Integrations
2. Click "Reconnect" on HubSpot
3. Make sure you check the box to authorize **WRITE** access to that object type
4. Save and try creating again

**Required permissions by object:**

* **Contacts:** "Write Contacts"
* **Companies:** "Write Companies"
* **Deals:** "Write Deals"
* **Tickets:** "Write Tickets"

### Duplicate Records Created

**Multiple records created instead of one**

**Possible causes:**

1. Workflow running multiple times
2. No duplicate checking (HubSpot allows duplicate emails if not prevented)

**How to fix:**

1. Check trigger settings - is it triggering multiple times?
2. Before creating, use **Search HubSpot (V2)** to check if record exists:
   * Search by email (for contacts) or domain (for companies)
   * Use **If Condition** to only create if search returns empty
3. Enable duplicate prevention in HubSpot settings (contacts only)

***

## Tips & Best Practices

**✅ Do:**

* Always use the "+ Add Property" button to select from actual HubSpot properties
* Include all required properties for that object type
* Use descriptive `dealname`, `firstname`/`lastname`, or `name` values
* Set `lifecycle_stage` for contacts to track their journey
* Save the output variable to use the HubSpot ID later
* Test with one record before running in a loop

**❌ Don't:**

* Create contacts without email addresses (HubSpot requires it)
* Forget to set `pipeline` and `dealstage` for deals (required)
* Create duplicate records - search first if unsure
* Forget to check permissions (need WRITE access, not just READ)
* Set properties that don't exist in your HubSpot account

**Performance tips:**

* Creating records is fast (usually under 1 second)
* If creating many records in a loop, consider batching (100-500 at a time)
* Use variables from previous actions instead of hardcoded values

***

## Related Actions

**What to do next:**

* [Update HubSpot Object (V2)](./hubspot-v2-update-object) - Update records you created
* [Search HubSpot (V2)](./hubspot-v2-search-objects) - Check if record exists before creating
* [Lookup HubSpot Object (V2)](./hubspot-v2-lookup-object) - Get full details on created record
* [If Condition](./if_else) - Only create if certain conditions are met

**Related guides:**

* [Variable System](../builder/template-variables) - Using variables in property values
* [HubSpot Setup](../integrations/hubspot-v2/guides/hubspot-setup) - Getting write permissions

***

**Last Updated:** 2025-10-01


# Create Timeline Event
Source: https://docs.agent.ai/actions/hubspot-v2-create-timeline-event



Add custom events to the timeline of any HubSpot record - perfect for tracking activities that happen outside HubSpot.

**Common uses:**

* Log customer actions from your app (logins, feature usage, purchases)
* Track external system events (support calls, shipping updates)
* Record custom milestones (onboarding completed, renewal date)
* Document important interactions (demo attended, contract signed)

**Action type:** `hubspot.v2.create_timeline_event`

***

## What This Does (The Simple Version)

Think of this like adding a note to someone's activity feed, but way more powerful. Instead of just text, you can log structured events that show up on contact, deal, or company timelines in HubSpot.

**Real-world example:**
A customer completes onboarding in your app. You create a timeline event on their contact record showing "Onboarding Completed" with details like completion date, steps finished, and time spent. Your sales team sees this in HubSpot and knows the customer is ready for upsell conversations.

***

## How It Works

This action creates a custom event that appears on the timeline of a HubSpot record. You choose:

1. **What record** to add the event to (contact, deal, company, etc.)
2. **Event type** identifier (you create this)
3. **Event details** (title, description, timestamp)
4. **Custom properties** (optional - any additional data you want to track)

The event appears on the record's timeline in HubSpot, just like emails, calls, and meetings.

***

## Setting It Up

### Step 1: Choose Target Object Type

Select which type of HubSpot record you want to add the timeline event to:

* **Contacts** - Add event to a person's timeline
* **Companies** - Add event to an organization's timeline
* **Deals** - Add event to a deal's timeline
* **Tickets** - Add event to a ticket's timeline

**Choose the object type** from the dropdown.

### Step 2: Enter Target Object ID

In the **"Target Object ID"** field, enter the HubSpot ID of the record you want to add the event to.

**Usually you'll insert a variable here:**

* Click the `{}` button
* Select the object ID from a previous action:
  * From a search: `current_contact` → `hs_object_id`
  * From a lookup: `found_deal` → `id`
  * From a webhook: `contact_id` (if provided)

**Example:** Click `{}` → select `contact_record` → `id`

### Step 3: Enter Event Type

The **"Event Type"** is a unique identifier for this kind of event. This helps HubSpot group similar events together.

**Format:** Use lowercase with underscores, like:

* `onboarding_completed`
* `feature_activated`
* `purchase_made`
* `support_call_completed`
* `renewal_reminder`

**Type directly** in the field or click `{}` to insert a variable.

**Note:** Use the same event type for similar events. For example, all "Feature Activated" events should use `feature_activated` so they're grouped together on the timeline.

### Step 4: Enter Event Title

The **"Event Title"** is the headline that appears on the timeline - like a subject line.

**Examples:**

* "Onboarding Completed"
* "Feature Activated: Advanced Reporting"
* "Purchase: Enterprise Plan"
* "Support Call: Billing Question"

Type directly or click `{}` to insert variables. You can combine text and variables:

* Type "Purchase: " then click `{}` → select `plan_name`
* Type "Feature Activated: " then click `{}` → select `feature_name`

### Step 5: Enter Event Description (Optional)

The **"Event Description"** provides additional details that appear when someone clicks the event on the timeline.

**Examples:**

* "Customer completed all 5 onboarding steps in 3 days"
* "Activated Advanced Reporting feature on 2025-10-01"
* "Upgraded from Starter to Enterprise plan, annual billing"

Type directly or click `{}` to insert variables with details.

**Leave blank** if you don't need additional description.

### Step 6: Add Event Properties (Optional)

Click **"+ Add Property"** if you want to attach custom data to this event.

**This is different from HubSpot properties.** These are custom key-value pairs specific to this event.

**Format:** Each property is `key=value`, one per line:

```
steps_completed=5
time_spent_minutes=45
completion_date=2025-10-01
```

Or use variables by clicking `{}` in the value field.

**Leave blank** if you don't need custom properties.

### Step 7: Set Event Timestamp (Optional)

The **"Event Timestamp"** controls when the event appears on the timeline.

**Default:** If you leave this blank, it uses the current time (right now).

**Formats supported:**

* ISO 8601: `2025-10-01T14:30:00Z`
* Date only: `2025-10-01` (assumes midnight)
* US format: `10/01/2025`
* Timestamp in milliseconds: `1727790600000` (13 digits)
* Timestamp in seconds: `1727790600` (10 digits)

**Usually you'll:**

* Leave blank to use "now"
* Click `{}` to insert a date variable from your trigger or previous action
* Type a specific date if logging a past event

### Step 8: Name Your Output Variable

Give the event result a descriptive name in the **"Output Variable Name"** field.

**Good names:**

* `onboarding_event`
* `purchase_event`
* `timeline_event`
* `logged_activity`

This variable contains the event ID and confirmation details.

***

## What You Get Back

The action returns confirmation that the event was created, including the event ID.

**Example output saved to `onboarding_event`:**

```
{
  "id": "evt_12345",
  "event_type": "onboarding_completed",
  "event_title": "Onboarding Completed",
  "event_description": "Customer completed all steps",
  "timestamp": 1727790600000,
  "object_id": "67890",
  "object_type": "contacts",
  "created_at": "2025-10-01T14:30:00Z",
  "properties": {
    "steps_completed": "5",
    "time_spent_minutes": "45"
  }
}
```

***

## Using the Results

### Confirm Event Was Created

The event either succeeds (returns event ID) or throws an error. The output variable contains the event ID, which you can use to verify creation succeeded.

### Access Event Details

Use the output variable to access event information in later actions:

* Click `{}` → `onboarding_event` → `id` (the event ID)
* Click `{}` → `onboarding_event` → `timestamp`
* Click `{}` → `onboarding_event` → `properties` → `steps_completed`

***

## Common Workflows

### Log App Activity

**Goal:** When a user completes onboarding in your app, log it on their HubSpot contact

**Trigger:** Webhook from your app

**Webhook receives:** `contact_id`, `steps_completed`, `completion_time` variables

1. **Create Timeline Event (V2)**
   * Object Type: Contacts
   * Target Object ID: Click `{}` → select `contact_id`
   * Event Type: `onboarding_completed`
   * Event Title: "Onboarding Completed Successfully"
   * Event Description: Type "Completed " then click `{}` → select `steps_completed` → type " steps"
   * Event Properties:
     ```
     steps_completed={{steps_completed}}
     time_spent_minutes={{completion_time}}
     ```
   * Event Timestamp: Leave blank (use current time)
   * Output Variable: `onboarding_event`

2. **Update contact** or send notification...

### Track Purchase on Company Timeline

**Goal:** When a company makes a purchase, log it on their company record

**Trigger:** Webhook from payment processor

**Webhook receives:** `company_domain`, `plan_name`, `amount`, `purchase_date`

1. **Lookup HubSpot Object (V2)**
   * Object Type: Companies
   * Lookup by: Domain
   * Domain: Click `{}` → select `company_domain`
   * Output Variable: `company_record`

2. **Create Timeline Event (V2)**
   * Object Type: Companies
   * Target Object ID: Click `{}` → `company_record` → `id`
   * Event Type: `purchase_made`
   * Event Title: Type "Purchase: " then click `{}` → select `plan_name`
   * Event Description: Type "Purchased " then click `{}` → select `plan_name` → type " for \$" → click `{}` → select `amount`
   * Event Properties:
     ```
     plan_name={{plan_name}}
     amount={{amount}}
     billing_frequency=annual
     ```
   * Event Timestamp: Click `{}` → select `purchase_date`
   * Output Variable: `purchase_event`

### Log Support Call on Deal

**Goal:** After a support call, log it on the related deal's timeline

1. **Search HubSpot (V2)**
   * Find the deal associated with the customer
   * Output Variable: `customer_deal`

2. **Create Timeline Event (V2)**
   * Object Type: Deals
   * Target Object ID: Click `{}` → `customer_deal` → `hs_object_id`
   * Event Type: `support_call_completed`
   * Event Title: Type "Support Call: " then click `{}` → select `call_topic`
   * Event Description: Click `{}` → select `call_notes`
   * Event Properties:
     ```
     duration_minutes={{call_duration}}
     resolution={{resolution_status}}
     agent={{support_agent_name}}
     ```
   * Event Timestamp: Click `{}` → select `call_time`
   * Output Variable: `support_event`

***

## Real Examples

### Feature Activation Tracking

**Scenario:** Track when customers activate premium features in your SaaS app.

**Webhook receives:** `user_email`, `feature_name`, `activation_date`

**Timeline Event Configuration:**

* **Object Type:** Contacts
* **Target Object ID:** Click `{}` → select `contact_id` (from lookup action)
* **Event Type:** `feature_activated`
* **Event Title:** Type "Feature Activated: " then click `{}` → select `feature_name`
* **Event Description:** Type "Customer activated " then click `{}` → select `feature_name` → type " on " → click `{}` → select `activation_date`
* **Event Properties:**
  ```
  feature_name={{feature_name}}
  plan_tier={{user_plan}}
  activation_date={{activation_date}}
  ```
* **Event Timestamp:** Click `{}` → select `activation_date`
* **Output Variable:** `feature_event`

**Next steps:** Check if they've activated 3+ features and update lifecycle stage.

### Renewal Reminder Logging

**Scenario:** Log when renewal reminders are sent to customers.

**Trigger:** Scheduled (runs daily)

**Timeline Event Configuration:**

* **Object Type:** Deals
* **Target Object ID:** Click `{}` → select `current_deal` → `hs_object_id` (from loop)
* **Event Type:** `renewal_reminder_sent`
* **Event Title:** "Renewal Reminder Sent"
* **Event Description:** Type "Renewal reminder sent for contract ending " then click `{}` → select `contract_end_date`
* **Event Properties:**
  ```
  contract_value={{deal_amount}}
  days_until_renewal={{days_remaining}}
  reminder_number={{reminder_count}}
  ```
* **Event Timestamp:** Leave blank (current time)
* **Output Variable:** `reminder_event`

***

## Troubleshooting

### "Target Object Not Found" Error

**Error:** Can't find the object to add event to

**Possible causes:**

1. Object ID is wrong or doesn't exist
2. Variable containing ID is empty
3. Using wrong object type for that ID

**How to fix:**

1. Check the execution log - what ID was used?
2. Verify the object exists in HubSpot (search by ID)
3. Make sure previous action (lookup/search) found the record successfully
4. Check that object type matches the ID (contact ID needs object type = Contacts)

### "Invalid Event Type" Error

**Error:** Event type format is incorrect

**Possible causes:**

1. Event type contains spaces or special characters
2. Event type is empty

**How to fix:**

1. Use lowercase with underscores only: `onboarding_completed` not "Onboarding Completed"
2. No spaces, no special characters except underscore
3. Make sure the field isn't empty

### Events Not Showing on Timeline

**Events created but don't appear in HubSpot**

**Possible causes:**

1. Looking at wrong record
2. Timeline filtered to hide custom events
3. Timestamp is far in past/future

**How to fix:**

1. Verify you're looking at the correct contact/company/deal in HubSpot
2. In HubSpot timeline, click "Filter" and make sure custom events are enabled
3. Check the timestamp - events in the far future or distant past might not show by default
4. Refresh the HubSpot page

### Timestamp Not Parsing

**Timestamp field showing current time instead of expected date**

**Possible causes:**

1. Date format not recognized
2. Variable is empty or has invalid value

**How to fix:**

1. Use one of the supported formats (ISO 8601 is most reliable: `2025-10-01T14:30:00Z`)
2. Check execution log to see what value was sent
3. If using a variable, verify it contains a valid date
4. Leave blank to use current time

***

## Tips & Best Practices

**✅ Do:**

* Use consistent event types across workflows (helps with reporting)
* Include meaningful descriptions that provide context
* Set custom properties for data you'll want to filter/report on later
* Use descriptive event titles that make sense at a glance
* Test with a single record before running on multiple records
* Use past timestamps to backfill historical events

**❌ Don't:**

* Use spaces or special characters in event type (breaks filtering)
* Create events without checking if target object exists first
* Log too many events (clutters timeline) - be selective
* Forget to include key context in description or properties
* Use vague event types like "event1" or "update" (not helpful later)

**Performance tips:**

* Creating timeline events is fast (under 1 second typically)
* You can create many events in a loop without issues
* Consider batching if creating thousands of events

***

## Related Actions

**What to do next:**

* [Lookup HubSpot Object (V2)](./hubspot-v2-lookup-object) - Find object ID before creating event
* [Search HubSpot (V2)](./hubspot-v2-search-objects) - Find multiple records to log events on
* [Get Timeline Events](./hubspot-v2-get-timeline-events) - Retrieve events from a record's timeline
* [For Loop](./for_loop) - Create events on multiple records

**Related guides:**

* [Variable System](../builder/template-variables) - Using variables in event properties
* [Webhook Triggers (HubSpot)](../integrations/hubspot-v2/guides/webhook-triggers) - Triggering workflows from HubSpot

***

**Last Updated:** 2025-10-01


# Get Engagements
Source: https://docs.agent.ai/actions/hubspot-v2-get-engagements



Retrieve calls, emails, meetings, notes, and tasks associated with any HubSpot record.

**Common uses:**

* Get call history for a contact
* Review all emails sent to a prospect
* Count meetings scheduled with a deal
* Analyze engagement patterns
* Gather relationship context

**Action type:** `hubspot.v2.get_engagements`

***

## What This Does (The Simple Version)

Think of this like pulling up someone's communication history. Every time your team calls, emails, or meets with a contact/company/deal, HubSpot logs it as an "engagement". This action retrieves those engagement records.

**Real-world example:**
You want to analyze how engaged a deal is. This action gets all calls, emails, and meetings associated with that deal - showing 15 calls, 32 emails, 4 meetings over 3 months. High engagement = healthy deal.

***

## How It Works

This action retrieves engagement records (calls, emails, meetings, notes, tasks) associated with a HubSpot record. You specify:

1. **What type of record** (contact, deal, company, ticket)
2. **Which record** (the HubSpot ID)
3. **Which engagement types** to get (calls, emails, meetings, notes, tasks)
4. **Date range** (optional)
5. **How many to retrieve**

The engagements are saved to a variable as a list you can analyze or loop through.

***

## Setting It Up

### Step 1: Choose Source Object Type

Select which type of HubSpot record to get engagements from:

* **Contacts** - Person's engagement history
* **Companies** - Organization's engagement history
* **Deals** - Deal's engagement history
* **Tickets** - Ticket's engagement history

**Choose the object type** from the dropdown.

### Step 2: Enter Object ID

In the **"Object ID"** field, enter the HubSpot ID of the record.

**Usually you'll insert a variable here:**

* Click the `{}` button
* Select the object ID from a previous action:
  * From a search: `current_contact` → `hs_object_id`
  * From a lookup: `deal_record` → `id`
  * From a webhook: `deal_id` (if provided)

**Example:** Click `{}` → select `contact_record` → `hs_object_id`

### Step 3: Select Engagement Types

Choose which types of engagements to retrieve. You can select multiple:

* **Calls** - Phone call records
* **Emails** - Email communications
* **Meetings** - Scheduled meetings
* **Notes** - Notes logged by your team
* **Tasks** - Tasks associated with this record

**Select all that apply** or choose specific types.

**Most common:** Select all types to get complete engagement history.

### Step 4: Set Date Range (Optional)

Want engagements from a specific time period?

**Start Date field:**

* Enter start date (engagements after this date)
* Formats: `2025-01-01` or `01/01/2025`
* Or click `{}` to insert date variable

**End Date field:**

* Enter end date (engagements before this date)
* Same format options

**Leave both blank** to get engagements from all time.

**Example:** Start Date = `2025-01-01` (get engagements from this year)

### Step 5: Set Result Limit (Optional)

Enter the maximum number of engagements to return.

**Default:** 100
**Maximum:** 500

**When to adjust:**

* **Testing?** Use 10-20
* **Recent activity?** Use 50
* **Complete history?** Use 500

### Step 6: Name Your Output Variable

Give the engagements list a descriptive name in the **"Output Variable Name"** field.

**Good names:**

* `deal_engagements`
* `contact_calls`
* `relationship_history`
* `recent_emails`

This variable contains the list of engagements.

***

## What You Get Back

The action returns a **list of engagement records**, each containing engagement details.

**Example output saved to `deal_engagements`:**

```javascript  theme={null}
[
  {
    "id": "123456",
    "type": "meeting",
    "createdAt": "2025-01-15T14:00:00Z",
    "properties": {
      "hs_meeting_title": "Product Demo",
      "hs_meeting_body": "Demonstrated enterprise features, answered technical questions about integrations",
      "hs_meeting_outcome": "Scheduled",
      "hs_meeting_start_time": "2025-01-15T14:00:00Z",
      "hs_meeting_duration": "3600000"
    }
  },
  {
    "id": "789012",
    "type": "call",
    "createdAt": "2025-01-10T10:30:00Z",
    "properties": {
      "hs_call_title": "Discovery Call",
      "hs_call_body": "Discussed requirements, budget, timeline. Strong interest in enterprise plan.",
      "hs_call_duration": "1800000",
      "hs_call_disposition": "Connected"
    }
  },
  {
    "id": "345678",
    "type": "email",
    "createdAt": "2025-01-08T09:00:00Z",
    "properties": {
      "hs_email_subject": "Proposal for Acme Corp",
      "hs_email_text": "Attached is our proposal...",
      "hs_email_status": "SENT"
    }
  },
  {
    "id": "901234",
    "type": "note",
    "createdAt": "2025-01-05T16:00:00Z",
    "properties": {
      "hs_note_body": "Follow-up from initial call. Need to connect with CTO about security requirements."
    }
  }
]
```

**Each engagement includes:**

* `id` - Engagement ID
* `type` - Type (meeting, call, email, note, task)
* `createdAt` - When it was created/logged
* `properties` - Type-specific details (subject, body, duration, outcome, etc.)

***

## Using the Results

### Pass to AI for Analysis

The most common use - send engagements to AI for relationship analysis:

**In Invoke LLM action:**

* Prompt: Type "Analyze this engagement history and assess relationship strength: " then click `{}` → select `deal_engagements`
  Example: `Analyze this engagement history: {{deal_engagements}}`
* AI receives all engagements and can identify patterns, frequency, quality

### Count Engagements

Want to know how many calls/emails/meetings?

**Add Set Variable action:**

* Use variable picker to count items in `deal_engagements` array
* Or count specific types: loop through and count where `type = "call"`

### Loop Through Engagements

Process each engagement individually:

1. **For Loop**
   * Loop through: Click `{}` → select `deal_engagements`
   * Current item: `current_engagement`

2. **Inside loop:** Access engagement details
   * Click `{}` → `current_engagement` → `type`
   * Click `{}` → `current_engagement` → `properties` → `hs_call_title`

### Check Recent Activity

**Add If Condition:**

* Check if `deal_engagements` list is not empty
* Check if first engagement (most recent) is within last 7 days
* Tag record based on engagement level

***

## Common Workflows

### Deal Engagement Analysis

**Goal:** Analyze all engagements for a deal to assess activity level

1. **Lookup HubSpot Object (V2)**
   * Get deal details
   * Output Variable: `deal_record`

2. **Get Engagements (V2)**
   * Object Type: Deals
   * Object ID: Click `{}` → `deal_record` → `id`
   * Engagement Types: Select all (Calls, Emails, Meetings, Notes)
   * Limit: 100
   * Output Variable: `deal_engagements`

3. **Invoke LLM**
   * Prompt: "Analyze this deal's engagement history. Assess: engagement frequency, quality, gaps, and health score." + `deal_engagements` variable
   * Output Variable: `engagement_analysis`

4. **Update HubSpot Object (V2)**
   * Update deal with engagement score

### Contact Communication History

**Goal:** Get all emails sent to a contact before sending another

1. **Get Engagements (V2)**
   * Object Type: Contacts
   * Object ID: Click `{}` → `contact_id`
   * Engagement Types: Select "Emails"
   * Start Date: Click `{}` → `thirty_days_ago`
   * Limit: 50
   * Output Variable: `recent_emails`

2. **If Condition**
   * Check if `recent_emails` count \< 3 (not over-emailing)

3. **Send Email** (inside if block)
   * Only sends if they haven't received too many emails

4. **End Condition**

### Meeting Count Report

**Goal:** Count meetings scheduled with each deal in a list

1. **Search HubSpot (V2)**
   * Find target deals
   * Output Variable: `target_deals`

2. **For Loop**
   * Loop through: `target_deals`
   * Current item: `current_deal`

3. **Get Engagements (V2)** (inside loop)
   * Object Type: Deals
   * Object ID: Click `{}` → `current_deal` → `hs_object_id`
   * Engagement Types: Select "Meetings"
   * Output Variable: `deal_meetings`

4. **Set Variable** (inside loop)
   * Count meetings and store

5. **End Loop**

***

## Real Examples

### Prospect Research

**Scenario:** Before calling a prospect, see all previous interactions.

**Trigger:** Manual

**Configuration:**

* **Object Type:** Contacts
* **Object ID:** (enter contact ID or use search first)
* **Engagement Types:** Select all
* **Start Date:** Leave blank (all time)
* **Limit:** 100
* **Output Variable:** `contact_history`

**Next steps:** AI summarizes history, identifies last touchpoint, suggests talking points.

### Sales Velocity Tracking

**Scenario:** Measure how many touchpoints it takes to close deals.

**Trigger:** When deal closes (webhook)

**Configuration:**

* **Object Type:** Deals
* **Object ID:** Click `{}` → `deal_id` (from webhook)
* **Engagement Types:** Select Calls, Emails, Meetings
* **Limit:** 500 (complete history)
* **Output Variable:** `sales_cycle_engagements`

**Next steps:** Count total engagements, calculate velocity, log metrics.

***

## Troubleshooting

### No Engagements Returned

**Action returns empty list `[]`**

**Possible causes:**

1. Record has no engagements
2. Wrong engagement types selected
3. Date range excludes all engagements
4. Object ID doesn't exist

**How to fix:**

1. Check HubSpot - does this record have logged calls/emails/meetings?
2. Select all engagement types to test
3. Remove date range filters
4. Verify object ID is correct
5. Check if engagements are actually associated with this record

### Missing Expected Engagements

**Some engagements you know exist aren't showing up**

**Possible causes:**

1. Engagements not associated with this specific record
2. Hit the limit before reaching those engagements
3. Date range excluding them

**How to fix:**

1. Check in HubSpot - are these engagements actually associated with this record?
2. Increase limit to 500
3. Expand date range or remove it
4. Engagements might be associated with related records (contact vs. company)

### Different Object Has Different Engagements

**Contact has different engagements than associated company**

**This is normal** - engagements are object-specific:

* Contact engagements: logged directly on the contact
* Company engagements: logged directly on the company
* Deal engagements: logged directly on the deal

**To get complete picture:**

1. Get engagements for contact
2. Get engagements for associated company
3. Get engagements for associated deal
4. Combine all three for full relationship history

### Properties Missing

**Engagements returned but missing details**

**Possible causes:**

1. Engagement was logged without details
2. Specific properties not filled in

**This is normal** - not all engagements have all properties:

* Quick notes might only have `hs_note_body`
* Some calls might not have duration logged
* Old emails might have limited data

**How to handle:**

* Check which properties exist before using them
* Use default values for missing properties
* Focus on properties that are consistently filled

***

## Tips & Best Practices

**✅ Do:**

* Select all engagement types unless you need specific ones
* Use result limit to control volume
* Pass engagements to AI for pattern analysis
* Check execution log to see what was returned
* Use date range for "recent activity" checks
* Consider getting engagements from related records too (contact + company + deal)

**❌ Don't:**

* Forget that engagements are object-specific (contact ≠ company ≠ deal)
* Assume all engagements have full details
* Request engagements without checking if record exists first
* Exceed 500 limit (HubSpot maximum)
* Expect engagements to include associations to other records (this action gets the engagements only)

**Performance tips:**

* Getting 100 engagements takes \~2-3 seconds
* More engagement types = slightly slower
* Date range filters can speed up retrieval
* Limit keeps results manageable

**Analysis ideas:**

* **Engagement frequency:** Count engagements per month
* **Engagement quality:** Analyze call notes and meeting outcomes
* **Response time:** Time between emails and responses
* **Engagement gaps:** Long periods with no activity
* **Activity patterns:** Which days/times have most engagement

***

## Difference from Get Timeline Events

**Get Engagements vs. Get Timeline Events - what's the difference?**

**Get Engagements (this action):**

* Retrieves: Calls, emails, meetings, notes, tasks
* These are standard HubSpot activity records
* Logged by your team
* Used for: Relationship analysis, activity tracking, communication history

**Get Timeline Events:**

* Retrieves: All timeline events (including custom events)
* Includes: Standard events + custom events you create
* Used for: Complete timeline history, custom milestone tracking

**When to use which:**

* **Get Engagements:** When you need sales/service activity (calls, emails, meetings)
* **Get Timeline Events:** When you need complete timeline including custom events

**You can use both** in the same workflow for complete context!

***

## Related Actions

**What to do with engagements:**

* [For Loop](./for_loop) - Process each engagement
* [If Condition](./if_else) - Check engagement patterns
* [Invoke LLM](./use_genai) - Analyze engagement quality

**Related actions:**

* [Get Timeline Events (V2)](./hubspot-v2-get-timeline-events) - Get timeline events (includes custom events)
* [Lookup HubSpot Object (V2)](./hubspot-v2-lookup-object) - Get object before retrieving engagements

**Related workflows:**

* [HubSpot Customer Onboarding](../recipes/hubspot-customer-onboarding) - Uses engagement history for onboarding context
* [HubSpot Deal Analysis](../recipes/hubspot-deal-analysis) - Uses timeline events (similar pattern)

***

**Last Updated:** 2025-10-01


# Get Timeline Events
Source: https://docs.agent.ai/actions/hubspot-v2-get-timeline-events



Retrieve timeline events from any HubSpot record - see what happened and when.

**Common uses:**

* Get deal activity history for AI analysis
* Review contact engagement timeline
* Check recent events before taking action
* Gather context for decision-making
* Audit what happened on a record

**Action type:** `hubspot.v2.get_timeline_events`

***

## What This Does (The Simple Version)

Think of this like viewing someone's activity feed or history log. Every HubSpot record (contact, deal, company, etc.) has a timeline showing what's happened - emails sent, meetings scheduled, custom events logged. This action retrieves that timeline.

**Real-world example:**
Before calling a lead, you want to see their recent activity. This action gets their timeline showing: form submitted 3 days ago, whitepaper downloaded yesterday, demo requested today. Now you have context for the call.

***

## How It Works

This action retrieves timeline events from a HubSpot record. You specify:

1. **What type** of record (contact, deal, company, etc.)
2. **Which record** (the HubSpot ID)
3. **Filter options** (optional - specific event types, date ranges)
4. **How many events** to retrieve

The events are saved to a variable as a list you can use in later actions (like AI analysis or loops).

***

## Setting It Up

### Step 1: Choose Object Type

Select which type of HubSpot record to get events from:

* **Contacts** - Person timeline
* **Companies** - Organization timeline
* **Deals** - Deal timeline
* **Tickets** - Ticket timeline

**Choose the object type** from the dropdown.

### Step 2: Enter Object ID

In the **"Object ID"** field, enter the HubSpot ID of the record.

**Usually you'll insert a variable here:**

* Click the `{}` button
* Select the object ID from a previous action:
  * From a search: `current_deal` → `hs_object_id`
  * From a lookup: `contact_record` → `id`
  * From a webhook: `deal_id` (if provided)

**Example:** Click `{}` → select `deal_record` → `hs_object_id`

### Step 3: Filter by Event Type (Optional)

Want only specific types of events? Enter an event type in the **"Event Type Filter"** field.

**Leave blank** to get all event types (most common).

**Or enter a specific type:**

* `NOTE` - Only notes
* `MEETING` - Only meetings
* `EMAIL` - Only emails
* Custom event types you've created (e.g., `onboarding_completed`)

**Example:** Type `NOTE` to get only notes

### Step 4: Set Date Range (Optional)

Want events from a specific time period?

**Start Date field:**

* Enter start date (events after this date)
* Formats: `2025-01-01` or `01/01/2025`
* Or click `{}` to insert date variable

**End Date field:**

* Enter end date (events before this date)
* Same format options

**Leave both blank** to get events from all time.

**Example:** Start Date = `2025-01-01`, End Date = `2025-03-31` (Q1 2025 events only)

### Step 5: Set Result Limit (Optional)

Enter the maximum number of events to return.

**Default:** 100
**Maximum:** 500

**When to adjust:**

* **Testing?** Use 10-20 for faster results
* **AI analysis?** Use 50-100 (enough context, not overwhelming)
* **Complete history?** Use 500

### Step 6: Name Your Output Variable

Give the events list a descriptive name in the **"Output Variable Name"** field.

**Good names:**

* `deal_timeline`
* `contact_events`
* `recent_activity`
* `timeline_history`

This variable contains the list of events.

***

## What You Get Back

The action returns a **list of timeline events**, each containing event details.

**Example output saved to `deal_timeline`:**

```javascript  theme={null}
[
  {
    "id": "evt_12345",
    "eventType": "MEETING",
    "timestamp": "2025-01-15T14:00:00Z",
    "headline": "Product Demo",
    "details": "Demonstrated enterprise features, answered technical questions",
    "objectId": "987654"
  },
  {
    "id": "evt_67890",
    "eventType": "EMAIL",
    "timestamp": "2025-01-10T09:30:00Z",
    "headline": "Proposal Sent",
    "details": "Sent pricing proposal and implementation timeline",
    "objectId": "987654"
  },
  {
    "id": "evt_11111",
    "eventType": "NOTE",
    "timestamp": "2025-01-05T16:00:00Z",
    "headline": "Discovery Call",
    "details": "Discussed requirements, budget, timeline. Strong fit for enterprise plan.",
    "objectId": "987654"
  }
]
```

**Each event includes:**

* `id` - Event ID
* `eventType` - Type of event (MEETING, EMAIL, NOTE, custom types)
* `timestamp` - When it occurred
* `headline` - Event title/subject
* `details` - Event description/body
* `objectId` - The record it's associated with

***

## Using the Results

### Pass to AI for Analysis

The most common use - send timeline events to AI for context:

**In Invoke LLM action:**

* Prompt: Type "Analyze this deal timeline: " then click `{}` → select `deal_timeline`
  Example: `Analyze this deal timeline: {{deal_timeline}}`
* AI receives the full event list and can analyze patterns, identify risks, suggest next steps

### Loop Through Events

Process each event individually:

1. **For Loop**
   * Loop through: Click `{}` → select `deal_timeline`
   * Current item: `current_event`

2. **Inside loop:** Access event details
   * Click `{}` → `current_event` → `headline`
   * Click `{}` → `current_event` → `timestamp`

### Count Events

Want to know how many events there are?

**Add Set Variable action:**

* Use variable picker to count items in `deal_timeline` array

### Check for Recent Activity

**Add If Condition:**

* Check if `deal_timeline` list length > 0
* Check if most recent event timestamp is within last 7 days
* Take action based on activity level

***

## Common Workflows

### Deal Health Analysis

**Goal:** Analyze deal activity before updating

1. **Lookup HubSpot Object (V2)**
   * Get deal details
   * Output Variable: `deal_record`

2. **Get Timeline Events (V2)**
   * Object Type: Deals
   * Object ID: Click `{}` → `deal_record` → `id`
   * Limit: 50
   * Output Variable: `deal_timeline`

3. **Invoke LLM**
   * Prompt: "Analyze this deal timeline and assess health: " + `deal_timeline` variable
   * Output Variable: `health_assessment`

4. **Update HubSpot Object (V2)**
   * Update deal with health score

### Check Recent Contact Activity

**Goal:** Only send email if contact hasn't been contacted recently

1. **Get Timeline Events (V2)**
   * Object Type: Contacts
   * Object ID: Click `{}` → `contact_id`
   * Event Type Filter: `EMAIL`
   * Start Date: Click `{}` → `seven_days_ago` (system variable)
   * Output Variable: `recent_emails`

2. **If Condition**
   * Check if `recent_emails` is empty (no emails in last 7 days)

3. **Send Email** (inside if block)
   * Only runs if no recent emails

4. **End Condition**

### Gather Context for Sales Call

**Goal:** Get complete activity history before calling prospect

1. **Search HubSpot (V2)**
   * Find target contact
   * Output Variable: `target_contact`

2. **Get Timeline Events (V2)**
   * Object Type: Contacts
   * Object ID: Click `{}` → `target_contact` → `hs_object_id`
   * Limit: 100
   * Output Variable: `contact_history`

3. **Invoke LLM**
   * Prompt: "Summarize this contact's history and suggest talking points: " + `contact_history` variable
   * Output Variable: `call_prep`

***

## Real Examples

### Pre-Call Research

**Scenario:** Sales rep clicks "Run" before calling a lead to get instant context.

**Trigger:** Manual

**Configuration:**

* **Object Type:** Contacts
* **Object ID:** (manually enter contact ID or use search first)
* **Event Type Filter:** Leave blank (get all events)
* **Start Date:** Leave blank
* **End Date:** Leave blank
* **Limit:** 100
* **Output Variable:** `contact_timeline`

**Next steps:** AI summarizes timeline, identifies recent activity, suggests talking points.

### Deal Stall Detection

**Scenario:** Every morning, check deals for inactivity.

**Trigger:** Scheduled (daily at 9:00 AM)

**Configuration:**

* **Object Type:** Deals
* **Object ID:** Click `{}` → `current_deal` → `hs_object_id` (from loop)
* **Event Type Filter:** Leave blank
* **Start Date:** Click `{}` → `thirty_days_ago`
* **End Date:** Leave blank
* **Limit:** 10 (just need to know if ANY activity exists)
* **Output Variable:** `recent_activity`

**Next steps:** If `recent_activity` is empty, flag deal as stalled.

***

## Troubleshooting

### No Events Returned

**Action returns empty list `[]`**

**Possible causes:**

1. Record has no timeline events
2. Event type filter doesn't match any events
3. Date range excludes all events
4. Object ID doesn't exist

**How to fix:**

1. Check HubSpot - does this record have timeline events?
2. Remove event type filter (leave blank to get all types)
3. Remove date range filters
4. Verify object ID is correct (check execution log)
5. Try with a record you know has events

### Wrong Event Type

**Filter returns no results but events exist**

**Possible causes:**

1. Event type name is case-sensitive or misspelled
2. Using wrong event type identifier

**How to fix:**

1. Event types are usually UPPERCASE: `EMAIL`, `MEETING`, `NOTE`
2. For custom events, check exact event type identifier
3. Leave filter blank first to see all event types, then filter

### Too Many Events

**Returns 500 events but there are more**

**Possible causes:**

1. HubSpot maximum limit is 500
2. Record has thousands of events

**How to fix:**

1. Use date range to focus on recent events
2. Use start\_date to get last 30/60/90 days only
3. Use event type filter to narrow down
4. If you need all events, make multiple calls with different date ranges

### Events Missing Details

**Events returned but `details` field is empty**

**This is normal** - not all event types have details. Some only have headlines.

**How to handle:**

1. Check `headline` field (always present)
2. Some events just track "this happened" without description
3. Use `eventType` to understand what kind of event it was

***

## Tips & Best Practices

**✅ Do:**

* Use result limit to control how many events you get
* Pass timeline to AI for analysis (great context)
* Filter by date range for recent activity checks
* Use in loops to analyze multiple records
* Leave event type filter blank unless you need specific types
* Check execution log to see what events were returned

**❌ Don't:**

* Request all events for records with thousands (use date range)
* Forget that event types are case-sensitive
* Assume all events have detailed descriptions
* Use without object ID (it's required)
* Expect events from the future (end\_date should be past or present)

**Performance tips:**

* Getting 100 events takes \~1-2 seconds
* Fewer events = faster response
* Date range filters speed up retrieval
* Event type filters reduce result size

**Use cases by event type:**

* **All events:** Complete history for AI analysis
* **EMAIL only:** Check email frequency/timing
* **MEETING only:** Count of meetings scheduled
* **NOTE only:** Sales notes and context
* **Custom events:** Track specific milestones

***

## Related Actions

**What to do with events:**

* [For Loop](./for_loop) - Process each event
* [If Condition](./if_else) - Check if events exist
* [Create Timeline Event (V2)](./hubspot-v2-create-timeline-event) - Add new events
* [Invoke LLM](./use_genai) - Analyze events with AI

**Related actions:**

* [Get Engagements (V2)](./hubspot-v2-get-engagements) - Similar but for engagements (calls, emails, meetings, notes)
* [Lookup HubSpot Object (V2)](./hubspot-v2-lookup-object) - Get object before retrieving timeline

**Related workflows:**

* [HubSpot Deal Analysis](../recipes/hubspot-deal-analysis) - Uses timeline events for AI analysis
* [HubSpot Customer Onboarding](../recipes/hubspot-customer-onboarding) - Uses engagement history

***

**Last Updated:** 2025-10-01


# Look up HubSpot Object
Source: https://docs.agent.ai/actions/hubspot-v2-lookup-object



Get detailed information about a specific HubSpot record when you know its ID, email, or domain.

**Common uses:**

* Get full details for a contact after searching
* Look up a deal triggered by a webhook
* Find a contact by their email address
* Fetch company information by domain
* Retrieve specific record properties

**Action type:** `hubspot.v2.lookup_object`

***

## What This Does (The Simple Version)

Think of this like looking up someone in a phone book. If you know their name (or in our case, their email, domain, or ID), you can find their full listing with all their details.

**Real-world example:**

Your website has a "Check your deal status" form. A customer enters their email. You use this action to look up their contact record in HubSpot by that email, then show them information about their deals.

**Another example:**

Someone fills out a contact form and you get their email address. Instead of creating a duplicate contact, you look them up by email first. If they exist, you update their info. If not, you create a new contact.

**The key difference from Search:**

* **Search** is like asking "Show me all contacts who work at Acme Corp" (might get many results)
* **Lookup** is like asking "Show me the contact with email [john@acme.com](mailto:john@acme.com)" (gets one specific record)

***

## How It Works

This action retrieves a single HubSpot record using a unique identifier. Depending on the object type, you can look up records in different ways:

* **Contacts:** By Object ID or Email address
* **Companies:** By Object ID or Domain name
* **All other objects (Deals, Tickets, etc.):** By Object ID only

You provide the identifier (usually from a webhook, search result, or previous action), and HubSpot returns the properties you request for that record.

**Why different lookup methods?**

Because different identifiers make sense for different object types:

* For **contacts**, email is unique - every contact has one email
* For **companies**, domain is unique - every company has one website domain
* For **deals/tickets/etc.**, you need the HubSpot ID since they don't have unique external identifiers

***

## When to Use Lookup vs. Search

**Use Lookup when:**

* You have a specific unique identifier (ID, email, or domain)
* You need exactly one record
* A webhook sent you an email or ID
* You know exactly which record you want

**Use Search when:**

* You don't have a unique identifier
* You need to find records matching criteria (like "all deals in this stage")
* You might get multiple results
* You're filtering by properties other than ID/email/domain

**Common pattern:** Search finds multiple records → Loop through results → Look up each one for complete details

***

## Setting It Up

### Step 1: Choose Object Type

When you add the Look up HubSpot Object action, you'll see clickable cards for each object type:

* **Contacts** - Person records (can lookup by ID or Email)
* **Companies** - Organization records (can lookup by ID or Domain)
* **Deals** - Sales opportunities (lookup by ID only)
* **Tickets** - Support tickets (lookup by ID only)
* **Calls** - Call engagement records (lookup by ID only)
* **Emails** - Email engagement records (lookup by ID only)
* **Meetings** - Meeting records (lookup by ID only)
* **Notes** - Note records (lookup by ID only)
* **Tasks** - Task records (lookup by ID only)

**Click the card** for the type of record you're looking up.

### Step 2: Choose Lookup Method (Contacts & Companies Only)

**For Contacts, you'll see a dropdown to choose:**

* **Lookup by Object ID** - Use the HubSpot record ID (e.g., "12345")
* **Lookup by Email** - Use the contact's email address (e.g., "[john@acme.com](mailto:john@acme.com)")

**For Companies, you'll see a dropdown to choose:**

* **Lookup by Object ID** - Use the HubSpot record ID (e.g., "67890")
* **Lookup by Domain** - Use the company's domain (e.g., "acme.com")

**For all other object types:**

* Only Object ID is available (no dropdown shown)

**Which should you choose?**

**Use Object ID when:**

* You got the ID from a search result
* You're looping through search results
* A webhook sent you the specific HubSpot record ID
* You have the ID from a previous action

**Use Email (for Contacts) when:**

* You have the contact's email but not their ID
* A form submission sends the email address
* You're enriching data from an external source that only has emails
* Example: "Look up the contact who just submitted our form using email [sarah@company.com](mailto:sarah@company.com)"

**Use Domain (for Companies) when:**

* You have the company website but not the HubSpot ID
* You're enriching company data from external sources
* A form captures the company website
* Example: "Look up the company with domain acme.com"

### Step 3: Enter the Lookup Value

In the lookup field (labeled based on your method selection), provide the identifier.

**If looking up by Object ID:**

Click into the field—the `{}` insert variable icon appears. Click it to select:

* From a webhook: The ID variable sent by the trigger (e.g., `contact_id`, `deal_id`)
* From a search/loop: `current_contact` → `hs_object_id`
* From a previous action: The output variable → `hs_object_id`

**Example:** Webhook sends `deal_id` → Click `{}` → select `deal_id`

**If looking up by Email (Contacts only):**

Click into the field and use the `{}` button to select:

* From a webhook: The email variable (e.g., `email`, `submitted_email`)
* From a form: The form submission email field
* From a search/loop: `current_contact` → `email`

**Example:** Form webhook sends `submitted_email` with value "[sarah@company.com](mailto:sarah@company.com)" → Click `{}` → select `submitted_email`

**If looking up by Domain (Companies only):**

Click into the field and use the `{}` button to select:

* From a webhook: The domain variable
* From a form: The company website/domain field
* From enrichment data: External data source with domain

**Example:** Webhook sends `company_website` with value "acme.com" → Click `{}` → select `company_website`

**Important for domains:** Use just the domain without "www" or "https\://"

* ✅ Good: `acme.com`
* ❌ Bad: `www.acme.com` or `https://acme.com`

**You can also type values directly** (less common):

* Object ID: `12345`
* Email: `john@acme.com`
* Domain: `acme.com`

### Step 4: Choose Properties to Retrieve (Optional)

Click the **"+ Add Property"** button to select which HubSpot properties you want to get back.

**This opens the property picker modal:**

* Search bar at the top to find properties quickly
* List of all available properties for that object type
* Click properties to select them (checkmark appears)
* Click **Done** when finished

**If you don't add any properties:**
The action will return a default set of basic properties for that object type.

**Tips:**

* Only select properties you'll actually use
* Use the search bar to quickly find specific properties
* Always include `hs_object_id` if you'll reference or update the record later

**Example properties to select:**

For **Contacts:**

* `firstname`
* `lastname`
* `email`
* `phone`
* `company`
* `lifecyclestage`
* `hs_object_id`

For **Companies:**

* `name`
* `domain`
* `industry`
* `city`
* `state`
* `numberofemployees`
* `hs_object_id`

For **Deals:**

* `dealname`
* `dealstage`
* `amount`
* `closedate`
* `pipeline`
* `hubspot_owner_id`
* `hs_object_id`

### Step 5: Get Associated Objects (Optional)

Want to also retrieve IDs of related records? Type the object types in the "Associated Object Types" field, separated by commas.

**Examples:**

```
contacts,companies
```

Returns IDs of contacts and companies associated with this record.

```
deals
```

Returns IDs of deals associated with this contact/company.

**What you get back:**
Just the IDs of associated records (not their full details). You can then look up those IDs if needed.

**Leave blank if:**
You don't need related record IDs.

### Step 6: Name Your Output Variable

In the "Output Variable Name" field, give this record a descriptive name.

**Good names:**

* `contact_details`
* `deal_info`
* `company_data`
* `retrieved_ticket`
* `found_contact`

This is how you'll reference the record's properties in later actions.

***

## What You Get Back

You get a single object containing the properties you selected.

**Example 1:** Looking up a contact by email with properties `firstname`, `lastname`, `email`

**Output saved to `contact_details`:**

```
{
  "firstname": "Sarah",
  "lastname": "Johnson",
  "email": "sarah@company.com",
  "hs_object_id": "12345"
}
```

**Example 2:** Looking up a company by domain with properties `name`, `domain`, `industry`

**Output saved to `company_info`:**

```
{
  "name": "Acme Corp",
  "domain": "acme.com",
  "industry": "Technology",
  "hs_object_id": "67890"
}
```

**Example 3:** With associations included

If you requested associated `deals`:

```
{
  "firstname": "Sarah",
  "lastname": "Johnson",
  "email": "sarah@company.com",
  "hs_object_id": "12345",
  "associations": {
    "deals": ["11111", "22222"]
  }
}
```

***

## Using the Retrieved Data

### Access Properties in Next Actions

For any field that needs a value, click the `{}` insert variable icon:

1. Select your output variable (e.g., `contact_details`)
2. Select the property you want (e.g., `email`, `firstname`)

**Example - Sending an email:**

* **To:** Click `{}` → select `contact_details` → select `email`
* **Subject:** Type "Hi " then click `{}` → select `contact_details` → select `firstname`

**Result:** Email goes to "[sarah@company.com](mailto:sarah@company.com)" with subject "Hi Sarah"

### Check If Property Has a Value

Some properties might be empty in HubSpot. Use an **If Condition** action to check first:

1. **Add If Condition** after the lookup
2. **Condition:** Check if `contact_details` → `phone` exists or is not empty
3. **If true:** Do something with the phone number
4. **If false:** Handle the missing data differently

### Use Associated Object IDs

If you retrieved associations, you can loop through them:

1. **Add For Loop** action
2. **Loop through:** Click to select `contact_details` → `associations` → `companies`
3. **Current item:** Name it `company_id`
4. Inside the loop, look up each company using that ID

***

## Common Workflows

### Form Submission → Lookup Contact by Email

**Goal:** When someone submits a form, find their existing contact record using their email.

**Real-world scenario:** You have a "Request a Demo" form. When Sarah fills it out, you want to check if she's already in your CRM before creating a new contact.

**Trigger:** Webhook receives `email` variable from form

1. **Look up HubSpot Object (V2)**
   * Object Type: Contacts
   * Lookup Method: **Lookup by Email**
   * Email: Click `{}` → select `email`
   * Add Properties: Select `firstname`, `lastname`, `email`, `company`, `hs_object_id`
   * Output Variable: `found_contact`

2. **If Condition** - Check if contact was found
   * If found: Update their info using `found_contact` → `hs_object_id`
   * If not found: Create new contact

3. **Send confirmation email**
   * To: `found_contact` → `email`
   * Subject: "Hi " + `found_contact` → `firstname` + ", thanks for your interest!"

### Enrich Company Data by Domain

**Goal:** External tool sends you a company domain, and you want to enrich it with HubSpot data.

**Real-world scenario:** Your sales team uses a Chrome extension that captures company domains from LinkedIn. You want to look up those companies in HubSpot to see if you already have them.

**Trigger:** Webhook with `company_domain` variable

1. **Look up HubSpot Object (V2)**
   * Object Type: Companies
   * Lookup Method: **Lookup by Domain**
   * Domain: Click `{}` → select `company_domain`
   * Add Properties: Select `name`, `industry`, `numberofemployees`, `city`, `hs_object_id`
   * Output Variable: `company_info`

2. **If Condition** - Check if company exists
   * If found: Display `company_info` → `name` and `company_info` → `industry`
   * If not found: Create new company with that domain

### Webhook → Lookup Deal by ID → Send Update

**Goal:** When a deal reaches a certain stage in HubSpot, send an email to the deal owner.

**Real-world scenario:** Your HubSpot workflow triggers when deals move to "Contract Sent" stage. You want to email the owner with deal details.

**Trigger:** HubSpot workflow sends webhook with `deal_id`

1. **Look up HubSpot Object (V2)**
   * Object Type: Deals
   * Object ID: Click `{}` → select `deal_id`
   * Add Properties: Select `dealname`, `amount`, `dealstage`, `closedate`, `hubspot_owner_id`
   * Output Variable: `deal_details`

2. **Send Email**
   * To: Look up owner email using `deal_details` → `hubspot_owner_id`
   * Subject: "Contract sent for " + `deal_details` → `dealname`
   * Body: Include `deal_details` → `amount` and `deal_details` → `closedate`

### Search → Loop → Lookup Pattern

**Goal:** Find all contacts in a certain lifecycle stage, then get complete details for each.

**Real-world scenario:** You want to find all "Lead" contacts and send them a nurture email with personalized details.

1. **Search HubSpot (V2)**
   * Object Type: Contacts
   * Filters: `lifecyclestage=lead`
   * Properties: Just get `hs_object_id` (basic info)
   * Output: `lead_contacts`

2. **For Loop**
   * Loop through: `lead_contacts`
   * Current item: `current_contact`

3. **Look up HubSpot Object (V2)** - inside loop
   * Object Type: Contacts
   * Lookup Method: Lookup by Object ID
   * Object ID: Click `{}` → select `current_contact` → `hs_object_id`
   * Add Properties: Select all the properties you need for the email
   * Output Variable: `full_contact`

4. **Send Email** - inside loop
   * To: `full_contact` → `email`
   * Personalized with their data

5. **End Loop**

***

## Real Examples

### Example 1: Form Submission with Email

**Scenario:** "Contact Us" form sends email address. Look up the contact to personalize the response.

**Webhook receives:** `submitted_email` = "[sarah@company.com](mailto:sarah@company.com)"

**Configuration:**

* **Object Type:** Contacts
* **Lookup Method:** Lookup by Email
* **Email:** Click `{}` → select `submitted_email`
* **Properties:** Click "+ Add Property" and select:
  * `firstname`
  * `lastname`
  * `email`
  * `company`
  * `lifecyclestage`
  * `hs_object_id`
* **Output Variable:** `contact_info`

**What happens:**

* Action finds Sarah's contact record
* Returns: `{"firstname": "Sarah", "lastname": "Johnson", "email": "sarah@company.com", ...}`

**Next step:** Send email: "Hi Sarah, thanks for reaching out!"

### Example 2: Company Enrichment

**Scenario:** Sales rep enters a company domain in your tool. Get HubSpot company data.

**Variable:** `company_domain` = "acme.com"

**Configuration:**

* **Object Type:** Companies
* **Lookup Method:** Lookup by Domain
* **Domain:** Click `{}` → select `company_domain`
* **Properties:** Select `name`, `industry`, `numberofemployees`, `city`, `state`, `hs_object_id`
* **Associated Object Types:** `contacts` (get contact IDs at this company)
* **Output Variable:** `company_data`

**What happens:**

* Action finds Acme Corp company record
* Returns company details plus IDs of contacts at that company
* `company_data` → `associations` → `contacts` = \["123", "456", "789"]

**Next step:** Loop through contact IDs and email each person at the company

### Example 3: Deal Update Notification

**Scenario:** HubSpot workflow fires when deal stage changes to "Closed Won". Send celebration email to owner.

**Webhook receives:** `deal_id` = "12345"

**Configuration:**

* **Object Type:** Deals
* **Object ID:** Click `{}` → select `deal_id`
* **Properties:** Select `dealname`, `dealstage`, `amount`, `closedate`, `hubspot_owner_id`
* **Output Variable:** `won_deal`

**What happens:**

* Retrieves: `{"dealname": "Acme Corp - Enterprise", "amount": "50000", ...}`

**Next step:**

* Email owner: "Congrats! " + `won_deal` → `dealname` + " closed for \$" + `won_deal` → `amount`

***

## Troubleshooting

### "Object not found" Error

**The record doesn't exist with that identifier**

**Possible causes:**

1. Wrong ID, email, or domain was provided
2. Record was deleted from HubSpot
3. Email/domain doesn't match exactly
4. Variable is empty or undefined

**How to fix:**

1. **Check the execution log** - See exactly what value was sent to the action
2. **Verify in HubSpot** - Does a record with that ID/email/domain actually exist?
3. **For email lookups:** Check for typos, extra spaces, or wrong capitalization
4. **For domain lookups:** Make sure it's just the domain (e.g., "acme.com" not "[https://www.acme.com](https://www.acme.com)")
5. **Add safety check:** Use an If Condition before the lookup to verify the variable has a value

**Example fix:**

```
If Condition: Check if {email} is not empty
  If true: Look up contact by email
  If false: Skip lookup or create new contact
```

### No Record Found by Email

**Looked up contact by email but got "not found"**

**Possible causes:**

1. Contact doesn't exist in HubSpot with that email
2. Email has typo or formatting issue
3. Email has extra whitespace

**How to fix:**

1. **Search HubSpot manually** - Does a contact with that email exist?
2. **Trim whitespace** - Strip spaces before/after the email
3. **Check format** - Emails should be lowercase typically
4. **Create if not found** - Use If Condition to create contact if lookup fails

**Pattern:**

```
1. Look up contact by email
2. If Condition: Check if contact was found
   - If found: Update contact
   - If not found: Create new contact
```

### No Company Found by Domain

**Looked up company by domain but got "not found"**

**Possible causes:**

1. Domain format is incorrect
2. Company doesn't exist in HubSpot
3. Domain includes "www" or "https\://" prefix
4. Domain has path or query parameters

**How to fix:**

1. **Use clean domain only:** Just `acme.com` (not `www.acme.com` or `https://acme.com/about`)
2. **Strip prefixes:** Remove "[www](http://www).", "http\://", "https\://"
3. **Remove paths:** Remove everything after the domain ("/about", "?page=1")
4. **Check HubSpot** - Verify the company exists with that exact domain

**Example:** If webhook sends `https://www.acme.com/products`

* Strip to just: `acme.com`
* Then do the lookup

### Properties Are Empty Even Though Record Found

**Record was found but specific properties are blank**

**Possible causes:**

1. Those properties are actually empty in HubSpot (not filled out)
2. Property names don't match exactly
3. Didn't select those properties in the property picker

**How to fix:**

1. **Check HubSpot record** - Open the actual record in HubSpot and see if those fields have values
2. **Use property picker** - Don't type property names, use the "+ Add Property" button
3. **Handle empty values** - Use If Condition to check if property has a value before using it

**Example:**

```
Look up contact by email
If Condition: Check if contact_details → phone is not empty
  - If has phone: Send SMS
  - If no phone: Send email instead
```

### "Missing OAuth Scope" Error

**Don't have permission to access that object type**

**How to fix:**

1. Go to **Settings → Integrations**
2. Find HubSpot and click **"Reconnect"**
3. Make sure you check the box for that object type's read permission
4. Save and try the workflow again

**Required permissions:**

* Contacts: "Read Contacts"
* Companies: "Read Companies"
* Deals: "Read Deals"
* Tickets: "Read Tickets"

***

## Tips & Best Practices

**✅ Do:**

* **Use Lookup by Email** for contacts when you only have the email (super common with forms!)
* **Use Lookup by Domain** for companies when enriching external data
* **Use the `{}` button** to insert variables instead of typing
* **Always handle "not found"** - Use If Condition to check if the lookup succeeded
* **Clean domains** - Strip "www" and "https\://" before looking up by domain
* **Use descriptive variable names** - `found_contact` is better than `c`
* **Include `hs_object_id`** in properties if you'll update/reference the record later

**❌ Don't:**

* Hard-code specific IDs, emails, or domains (they change between portals)
* Assume the record exists - always handle the not-found case
* Include URL prefixes in domain lookups ("[https://acme.com](https://acme.com)" won't work)
* Forget to select properties - you'll only get defaults
* Use the wrong lookup method (can't look up deals by email!)

**Performance tips:**

* Lookups are very fast - don't worry about using them in loops
* Lookup by email/domain is just as fast as by ID
* Only select properties you need (though lookup is fast regardless)
* If you're looking up many records, Search might be more efficient than individual lookups

***

## Lookup Methods Quick Reference

| Object Type   | Can Lookup By         |
| ------------- | --------------------- |
| **Contacts**  | Object ID, **Email**  |
| **Companies** | Object ID, **Domain** |
| **Deals**     | Object ID only        |
| **Tickets**   | Object ID only        |
| **Calls**     | Object ID only        |
| **Emails**    | Object ID only        |
| **Meetings**  | Object ID only        |
| **Notes**     | Object ID only        |
| **Tasks**     | Object ID only        |

**Bold** = Special lookup methods (beyond just ID)

***

## Related Actions

**Use with Lookup:**

* [Search HubSpot (V2)](./hubspot-v2-search-objects) - Find records before looking them up
* [Update HubSpot Object (V2)](./hubspot-v2-update-object) - Update the record after looking it up
* [Create HubSpot Object (V2)](./hubspot-v2-create-object) - Create record if lookup fails (common pattern!)
* [If Condition](./if_else) - Check if lookup succeeded
* [For Loop](./for_loop) - Loop through associated record IDs

**Related guides:**

* [Variable System](../builder/template-variables) - Using retrieved data in actions
* [Webhook Triggers (HubSpot)](../integrations/hubspot-v2/guides/webhook-triggers) - Getting IDs/emails from HubSpot workflows

***

**Last Updated:** 2025-10-01


# Search HubSpot
Source: https://docs.agent.ai/actions/hubspot-v2-search-objects



Find contacts, deals, companies, and other HubSpot records based on criteria you specify.

**Common uses:**

* Find all deals in a specific stage
* Get contacts matching certain criteria
* Search for companies by property values
* Pull records for bulk processing

**Action type:** `hubspot.v2.search_objects`

***

## How It Works

This action searches your HubSpot CRM and returns a list of matching records. You choose what type of object to search (contacts, deals, etc.), optionally add filters to narrow results, and select which properties to get back.

The results are saved to a variable you can use in later actions—usually in a loop to process each record.

***

## Setting It Up

### Step 1: Choose Object Type

When you add the Search HubSpot action, you'll see clickable cards for each object type:

* **Contacts** - People in your CRM
* **Companies** - Organizations
* **Deals** - Sales opportunities
* **Tickets** - Support tickets
* **Calls** - Call records
* **Emails** - Email engagement records
* **Meetings** - Meeting records
* **Notes** - Notes attached to records
* **Tasks** - Tasks in HubSpot

**Click the card** for the type you want to search. For example, click **Deals** if you're searching for deals.

### Step 2: Add Search Filters (Optional)

After selecting the object type, you'll see a "Search Contact Properties" section (or "Search Deal Properties", etc. depending on your object type).

**Leave it empty** to get all records (up to your limit).

**To add filters:**

1. Click the **"+ Add Property"** button
2. This opens the property picker - select a property to filter by (e.g., "City", "Deal Stage", "Lifecycle Stage")
3. Click **Done**

**For each filter you add, you'll see:**

* **Property name** (e.g., "City")
* **Operator dropdown** - Choose how to compare:
  * **Equals** - Exact match
  * **Not Equals** - Doesn't match
  * **Contains** - Text contains this value
  * **Greater Than** - Number/date is greater
  * **Less Than** - Number/date is less
  * **Greater Than or Equal**
  * **Less Than or Equal**
  * **Has Property** - Property has any value
  * **Not Has Property** - Property is empty
* **Value field** - Enter the value or click `{}` to insert a variable

**Example filters:**

**Find closed-won deals:**

* Property: Deal Stage
* Operator: Equals
* Value: "closedwon"

**Find contacts in a specific city:**

* Property: City
* Operator: Equals
* Value: "San Francisco"

**Find deals over \$10,000:**

* Property: Amount
* Operator: Greater Than
* Value: "10000"

**Find contacts who haven't been contacted recently:**

* Property: Last Contact Date
* Operator: Less Than
* Value: Click `{}` → select `thirty_days_ago` variable

**Using variables in filter values:**

Click the `{}` button in the value field to insert a variable from previous actions or the trigger.

**Example:** Filter by a stage that was sent via webhook

* Property: Deal Stage
* Operator: Equals
* Value: Click `{}` → select `target_stage` (from webhook)

**Adding multiple filters:**
Each filter you add works with AND logic (records must match ALL filters).

**Tips:**

* Use the property picker to avoid typos in property names
* Operator choice matters: "Equals" requires exact match, "Contains" is more flexible
* Use Greater Than/Less Than for numbers and dates
* Values are case-sensitive for exact matches

### Step 3: Choose Properties to Retrieve

In the "Retrieve Contact Properties" section (or "Retrieve Deal Properties", etc.), click the **"+ Add Property"** button to select which HubSpot properties you want to get back in your search results.

**This opens a property picker modal showing:**

* Search bar at the top
* List of all available properties for that object type
* Click properties to select them (they'll show a checkmark)
* Click **Done** when finished

**The properties you select will be included in each search result.**

**Note:** This is a separate section from the search filters. Search filters determine WHICH records to find. Retrieve properties determine WHAT data to get back from those records.

**Tips for choosing properties:**

* Only select what you'll actually use (faster searches)
* Always include `hs_object_id` if you'll update records or look up related data later
* Use the search bar to quickly find properties
* Common properties for contacts: `firstname`, `lastname`, `email`, `phone`
* Common properties for deals: `dealname`, `dealstage`, `amount`, `closedate`, `hs_object_id`

**Can't find a property?** It might not exist in your HubSpot. Check HubSpot → Settings → Properties to see all available properties.

### Step 4: Sort Results (Optional)

Choose how to order your results by entering a sort value.

**Examples:**

* `createdate` - Oldest first
* `-createdate` - Newest first (the minus sign means descending)
* `amount` - Smallest to largest
* `-amount` - Largest to smallest

**Leave blank** for HubSpot's default order (usually by creation date).

### Step 5: Set Result Limit (Optional)

Enter the maximum number of results to return.

**Default:** 100
**Maximum:** 1000

**When to adjust:**

* **Testing?** Use 10-20 to run faster
* **Production?** Set based on how many you expect (100-500 is common)
* **Processing in a loop?** Remember that 1000 records takes time!

### Step 6: Name Your Output Variable

Give the search results a descriptive name in the "Output Variable Name" field.

**Good names:**

* `qualified_deals`
* `inactive_contacts`
* `target_companies`
* `recent_tickets`

This is the variable name you'll use to access the results in later actions.

***

## What You Get Back

The search returns a **list** of objects. Each object contains the properties you selected in Step 3.

**Example:** If you searched for deals and selected properties `dealname`, `amount`, `hs_object_id`:

**Output saved to `qualified_deals`:**

```
[
  {
    "dealname": "Acme Corp - Enterprise",
    "amount": "50000",
    "hs_object_id": "12345"
  },
  {
    "dealname": "TechCo Deal",
    "amount": "25000",
    "hs_object_id": "67890"
  }
]
```

***

## Using the Results

### In a For Loop (Most Common)

After your search action, add a **For Loop** action:

1. **Loop through:** Click to select your search results variable (e.g., `qualified_deals`)
2. **Current item variable:** Give each item a name (e.g., `current_deal`)

**Inside the loop, access properties:**

For any field that needs a value, click the **Insert Variable** button (the `{}` icon) and navigate:

* Select `current_deal`
* Then select the property you want (e.g., `dealname`, `amount`, `hs_object_id`)

**Example:** In an Update HubSpot Object action inside the loop:

* **Object ID:** Insert variable → `current_deal` → `hs_object_id`
* **Property to update:** Insert variable → `current_deal` → `dealname`

### Count How Many Results

Want to know how many records matched?

Add a **Set Variable** action after the search and use the variable picker to count the items in your results array.

### Get Just the First Result

To grab only the first record, use the variable picker to select the first item from your results array in any subsequent action.

***

## Common Workflows

### Find and Update Pattern

**Goal:** Search for records, then update each one

1. **Search HubSpot (V2)**
   * Object Type: Deals
   * Search Filters: Click "+ Add Property"
     * Property: Deal Stage
     * Operator: Equals
     * Value: "presentationscheduled"
   * Retrieve Properties: Click "+ Add Property" and select `dealname`, `hs_object_id`
   * Output Variable: `deals_to_update`

2. **For Loop**
   * Loop through: `deals_to_update`
   * Current item: `current_deal`

3. **Update HubSpot Object (V2)** - inside loop
   * Object ID: Insert variable → `current_deal` → `hs_object_id`
   * Update whatever properties you need

4. **End Loop**

### Search Using Trigger Data

**Goal:** Use data from a webhook to filter your search

**Webhook receives:** `target_stage` variable

1. **Search HubSpot (V2)**
   * Object Type: Deals
   * Search Filters: Click "+ Add Property"
     * Property: Deal Stage
     * Operator: Equals
     * Value: Click `{}` → select `target_stage` (from webhook)
   * Output Variable: `matching_deals`

2. Process the results...

### Daily Report

**Goal:** Count records and send an email

1. **Search HubSpot (V2)**
   * Object Type: Tickets
   * Search Filters: Click "+ Add Property"
     * Property: Ticket Pipeline Stage
     * Operator: Equals
     * Value: "open"
   * Limit: 1000
   * Output Variable: `open_tickets`

2. **Set Variable**
   * Variable name: `ticket_count`
   * Value: Use variable picker to count `open_tickets`

3. **Send Email**
   * Subject: Type "You have " then insert `ticket_count` variable

***

## Real Examples

### Daily Deal Health Check

**Scenario:** Every morning at 9 AM, find all deals in "Presentation Scheduled" stage.

**Trigger:** Schedule (daily at 9:00 AM)

**Search Configuration:**

* **Object Type:** Deals
* **Search Filters:** Click "+ Add Property"
  * Property: Deal Stage
  * Operator: Equals
  * Value: "presentationscheduled"
* **Retrieve Properties:** Click "+ Add Property" and select:
  * `dealname`
  * `dealstage`
  * `amount`
  * `closedate`
  * `hs_object_id`
  * `hubspot_owner_id`
* **Sort:** Select "Create Date" descending (newest first)
* **Limit:** 50
* **Output Variable:** `active_deals`

**Next steps:** Loop through `active_deals` and analyze each one.

### Find Contacts from Form Submission

**Scenario:** When someone submits a form, find their contact record.

**Webhook receives:** `email` variable from HubSpot form

**Search Configuration:**

* **Object Type:** Contacts
* **Search Filters:** Click "+ Add Property"
  * Property: Email
  * Operator: Equals
  * Value: Click `{}` → select `email` (from webhook)
* **Retrieve Properties:** Click "+ Add Property" and select:
  * `firstname`
  * `lastname`
  * `email`
  * `hs_object_id`
* **Limit:** 1 (expecting only one match)
* **Output Variable:** `found_contact`

**Next steps:** Check if contact was found, then enrich their data.

***

## Troubleshooting

### No Results Found

**The search returns an empty list `[]`**

**Possible causes:**

1. No records actually match your filters
2. Property name is misspelled in filters
3. Property value doesn't match exactly

**How to fix:**

1. Go to HubSpot and manually search using the same criteria—do records exist?
2. Double-check property names (they're case-sensitive!)
3. Look at an actual HubSpot record to see the exact value format
4. Try removing filters one by one to see which is excluding results

### Missing Properties in Results

**Records come back but properties you selected aren't showing up**

**Possible causes:**

1. You didn't add that property using "+ Add Property"
2. The property is actually empty in HubSpot
3. Property was added but not saved before running

**How to fix:**

1. Make sure you clicked "+ Add Property" and selected all properties you need
2. Check an actual HubSpot record—does it have values for those properties?
3. Re-add the property and save the action
4. Check the execution log to see exactly what was returned

### "Missing OAuth Scope" Error

**You don't have permission to access that object type**

**How to fix:**

1. Go to Settings → Integrations
2. Click "Reconnect" on HubSpot
3. Make sure you check the box to authorize access to that object type
4. Save and try the search again

**Required permissions by object:**

* **Contacts:** "Read Contacts"
* **Companies:** "Read Companies"
* **Deals:** "Read Deals"
* **Tickets:** "Read Tickets"

### Search is Slow (Takes 10+ Seconds)

**Possible causes:**

1. Returning too many results
2. Requesting too many properties
3. HubSpot account has millions of records

**How to fix:**

1. **Add filters** to narrow the search scope
2. **Lower the limit** (100 instead of 1000)
3. **Request fewer properties** (only what you need)
4. **Add specific filters** like date ranges instead of searching everything

***

## Tips & Best Practices

**✅ Do:**

* Always include `hs_object_id` in your properties if you'll update or reference records later
* Use the "+ Add Property" button to browse and select from your actual HubSpot properties
* Start with small limits while testing (10-20), then increase for production
* Test your filters in HubSpot's UI first to verify they return the right records
* Use descriptive output variable names
* Add filters to narrow results whenever possible

**❌ Don't:**

* Search for all records without filters (could return thousands!)
* Request every property when you only need a few
* Forget to set a limit (defaults to 100 but be explicit)
* Assume all properties have values—some might be empty
* Use misspelled property names in filters

**Performance tips:**

* Filters make searches faster—use them!
* Limit results to what you need (don't fetch 1000 if you'll only process 50)
* If looping through results, remember each iteration takes time
* The fewer properties you request, the faster the search

***

## Advanced Filtering

The simple `property=value` format works for exact matches. For more complex scenarios like:

* "Greater than" or "less than" comparisons
* Date range filtering
* OR logic between filters
* "Contains" text searches

See the **[Advanced Variable Usage](../builder/template-variables)** guide for JSON filter syntax.

***

## Related Actions

**What to do next:**

* [For Loop](./for_loop) - Process search results one by one
* [Update HubSpot Object (V2)](./hubspot-v2-update-object) - Update records you found
* [Lookup HubSpot Object (V2)](./hubspot-v2-lookup-object) - Get full details for specific records
* [If Condition](./if_else) - Filter results based on conditions

**Related guides:**

* [Variable System](../builder/template-variables) - Using search results in other actions
* [Webhook Triggers (HubSpot)](../integrations/hubspot-v2/guides/webhook-triggers) - Use webhook payloads to drive searches
* [Deal Analysis Workflow](../recipes/hubspot-deal-analysis) - Complete example

***

**Last Updated:** 2025-10-01


# Update HubSpot Object
Source: https://docs.agent.ai/actions/hubspot-v2-update-object



Update contacts, deals, companies, and other HubSpot records with new information.

**Common uses:**

* Update deal stages when deals progress
* Change contact properties based on form submissions
* Update company information from webhook data
* Modify ticket status and priority

**Action type:** `hubspot.v2.update_object`

***

## What This Does (The Simple Version)

Think of this like editing a contact card in your phone. You find the person (by their name, email, or phone number), then update whatever details changed.

**Real-world example:**
A customer fills out a "Request Enterprise Demo" form. You use this action to find their contact record by email and update their `lifecycle_stage` to "Sales Qualified Lead" and set `demo_requested` to "Yes".

***

## How It Works

This action finds a HubSpot record and updates it with new property values. You choose:

1. **What type** of record to update (contact, deal, company, etc.)
2. **How to find it** (by ID, email, or domain)
3. **Which properties** to update
4. **What values** to set

The updated record is saved to a variable you can use in later actions.

***

## Setting It Up

### Step 1: Choose Object Type

When you add the Update HubSpot Object action, you'll see clickable cards for each object type:

* **Contacts** - People in your CRM
* **Companies** - Organizations
* **Deals** - Sales opportunities
* **Tickets** - Support tickets
* **Calls** - Call records
* **Emails** - Email engagement records
* **Meetings** - Meeting records
* **Notes** - Notes attached to records
* **Tasks** - Tasks in HubSpot

**Click the card** for the type you want to update.

### Step 2: Choose How to Find the Record

After selecting the object type, you'll see a **"Identify by"** dropdown with different lookup methods:

**For Contacts:**

* **Lookup by Object ID** - If you have the HubSpot ID
* **Lookup by Email** - Find by email address

**For Companies:**

* **Lookup by Object ID** - If you have the HubSpot ID
* **Lookup by Domain** - Find by company domain (e.g., "acme.com")

**For all other objects (Deals, Tickets, etc.):**

* **Lookup by Object ID** - Only option (must have the HubSpot ID)

**Choose your method** from the dropdown.

### Step 3: Enter the Identifier

In the **identifier field** below the dropdown, enter the value to find the record:

**Examples:**

* If you chose "Lookup by Email": Enter `jane@example.com` or click `{}` to insert an email variable
* If you chose "Lookup by Domain": Enter `acme.com` or click `{}` to insert a domain variable
* If you chose "Lookup by Object ID": Enter `12345` or click `{}` to insert an ID variable from a previous action

**Using variables:**
Click the `{}` button to insert a variable from previous actions. Common patterns:

* Email from webhook: Click `{}` → select `contact_email` (from your trigger)
* ID from search: Click `{}` → select `current_deal` → `hs_object_id` (from a loop)

### Step 4: Add Properties to Update

In the **"Update Contact Properties"** section (or "Update Deal Properties", etc.), click the **"+ Add Property"** button to select which properties you want to update.

**This opens a property picker modal showing:**

* Search bar at the top
* List of all available properties for that object type
* Click properties to select them (they'll show a checkmark)
* Click **Done** when finished

**After closing the modal**, you'll see individual input fields for each property you selected.

**For each property:**

* The field is labeled with the property name (e.g., "Lifecycle Stage", "Deal Stage", "City")
* Type the new value directly, OR
* Hover over the field to see the `{}` button, then click it to insert a variable

**Example - Updating a contact:**

1. Click "+ Add Property"
2. Select `lifecycle_stage`, `deal_stage_requested`, `city`
3. Click Done
4. Now you see three fields:
   * **Lifecycle Stage**: Type "Sales Qualified Lead"
   * **Deal Stage Requested**: Type "Yes"
   * **City**: Click `{}` → select `form_city` (from webhook)

**Tips:**

* Only add properties you actually want to change (you don't need to include properties that aren't changing)
* Use the property picker to avoid typos
* Click `{}` to insert variables from triggers, previous actions, or loop items

### Step 5: Name Your Output Variable

Give the updated record a descriptive name in the **"Output Variable Name"** field.

**Good names:**

* `updated_contact`
* `updated_deal`
* `modified_ticket`
* `current_record`

This variable contains the full record with all its properties after the update.

***

## What You Get Back

The action returns the **complete updated object** with all its properties (not just the ones you changed).

**Example:** If you updated a contact's `lifecycle_stage` and selected properties `firstname`, `email`, `lifecycle_stage`:

**Output saved to `updated_contact`:**

```
{
  "id": "12345",
  "properties": {
    "firstname": "Jane",
    "email": "jane@example.com",
    "lifecycle_stage": "salesqualifiedlead"
  },
  "createdAt": "2025-01-15T10:30:00Z",
  "updatedAt": "2025-10-01T14:22:00Z"
}
```

**Note:** The full record is returned, but you control which properties are visible by what you selected in the property picker.

***

## Using the Results

### Access Updated Properties

After the update action, use the output variable to access the updated record:

**In any field that accepts variables:**

* Click the **Insert Variable** button (`{}` icon)
* Navigate to your output variable (e.g., `updated_contact`)
* Select the property you want (e.g., `id`, `properties` → `email`)

### In a Loop

If you're updating multiple records in a loop:

**Example workflow:**

1. **Search HubSpot (V2)** - Find contacts matching criteria, save to `contacts_to_update`
2. **For Loop** - Loop through `contacts_to_update`, current item: `current_contact`
3. **Update HubSpot Object (V2)** - Inside the loop:
   * Object Type: Contacts
   * Identify by: Lookup by Object ID
   * Identifier: Click `{}` → `current_contact` → `hs_object_id`
   * Update properties (e.g., set `last_contacted` to today)
   * Output Variable: `updated_contact`
4. **End Loop**

### Check If Update Succeeded

The update either succeeds (returns the full record) or throws an error. If the record isn't found or credentials are wrong, the workflow stops with an error message.

***

## Common Workflows

### Update from Form Submission

**Goal:** When someone fills out a form, update their contact record

**Trigger:** Webhook from HubSpot form

**Webhook receives:** `email`, `requested_demo` variables

1. **Update HubSpot Object (V2)**
   * Object Type: Contacts
   * Identify by: Lookup by Email
   * Identifier: Click `{}` → select `email` (from webhook)
   * Update Properties: Click "+ Add Property" and select:
     * `demo_requested`: Set to "Yes"
     * `lifecycle_stage`: Set to "Sales Qualified Lead"
   * Output Variable: `updated_contact`

2. **Send notification** or continue workflow\...

### Update Deal Stage in Loop

**Goal:** Move multiple deals to the next stage

1. **Search HubSpot (V2)**
   * Object Type: Deals
   * Search Filters: Click "+ Add Property"
     * Property: Deal Stage
     * Operator: Equals
     * Value: "presentationscheduled"
   * Retrieve Properties: Select `dealname`, `hs_object_id`
   * Output Variable: `deals_to_progress`

2. **For Loop**
   * Loop through: `deals_to_progress`
   * Current item: `current_deal`

3. **Update HubSpot Object (V2)** - inside loop
   * Object Type: Deals
   * Identify by: Lookup by Object ID
   * Identifier: Click `{}` → `current_deal` → `hs_object_id`
   * Update Properties: Click "+ Add Property"
     * `dealstage`: Set to "decisionmakerboughtin"
   * Output Variable: `updated_deal`

4. **End Loop**

### Update Company by Domain

**Goal:** Update a company's information when you know their domain

**Trigger:** Manual or webhook with company domain

1. **Update HubSpot Object (V2)**
   * Object Type: Companies
   * Identify by: Lookup by Domain
   * Identifier: Type "acme.com" or click `{}` to insert domain variable
   * Update Properties: Click "+ Add Property"
     * `industry`: Set to "Technology"
     * `company_size`: Set to "500+"
   * Output Variable: `updated_company`

***

## Real Examples

### Contact Lifecycle Update

**Scenario:** When a contact downloads a whitepaper, update their lifecycle stage.

**Webhook receives:** `email` variable from form

**Update Configuration:**

* **Object Type:** Contacts
* **Identify by:** Lookup by Email
* **Identifier:** Click `{}` → select `email` (from webhook)
* **Update Properties:** Click "+ Add Property" and select:
  * `lifecycle_stage`: "marketingqualifiedlead"
  * `last_engagement_date`: Click `{}` → select `today` (system variable)
  * `content_downloads`: Click `{}` → select `download_count` (from previous action)
* **Output Variable:** `updated_contact`

**Next steps:** Send confirmation email using updated contact data.

### Deal Amount Update

**Scenario:** When a deal reaches "Contract Sent" stage, update the expected close date.

**Trigger:** Manual or scheduled

**Update Configuration:**

* **Object Type:** Deals
* **Identify by:** Lookup by Object ID
* **Identifier:** Click `{}` → select `deal_id` (from search or webhook)
* **Update Properties:** Click "+ Add Property" and select:
  * `closedate`: Click `{}` → select `thirty_days_from_now` (calculated variable)
  * `dealstage`: "contractsent"
* **Output Variable:** `updated_deal`

***

## Troubleshooting

### Record Not Found

**Error:** "Object not found" or "No record with that email/domain"

**Possible causes:**

1. The email/domain/ID doesn't exist in HubSpot
2. Typo in the identifier value
3. Using wrong identification method

**How to fix:**

1. Check HubSpot manually - does the record exist?
2. Verify the identifier value (email is case-insensitive, but check for typos)
3. For email lookup, make sure you selected "Contacts" (not Companies or Deals)
4. For domain lookup, make sure you selected "Companies" (not Contacts)
5. Check the execution log to see the exact value that was used

### "Missing OAuth Scope" Error

**You don't have permission to update that object type**

**How to fix:**

1. Go to Settings → Integrations
2. Click "Reconnect" on HubSpot
3. Make sure you check the box to authorize **WRITE** access to that object type
4. Save and try the update again

**Required permissions by object:**

* **Contacts:** "Write Contacts" (not just "Read Contacts")
* **Companies:** "Write Companies"
* **Deals:** "Write Deals"
* **Tickets:** "Write Tickets"

### Properties Not Updating

**The action succeeds but properties don't change**

**Possible causes:**

1. Property name is misspelled
2. Property value format is wrong (e.g., date format)
3. Property is read-only in HubSpot
4. Property doesn't exist for that object type

**How to fix:**

1. Use the "+ Add Property" button to select from actual HubSpot properties (avoids typos)
2. Check HubSpot → Settings → Properties to see valid values for that property
3. Look at a HubSpot record to see the expected format (dates, picklists, etc.)
4. Try updating the property manually in HubSpot to verify it's editable
5. Check the execution log - the response shows which properties were actually updated

### No Properties Selected

**Error:** "At least one property is required to update an object"

**How to fix:**

1. Click the "+ Add Property" button
2. Select at least one property to update
3. Enter a value for that property
4. Make sure you clicked "Done" in the property picker modal

***

## Tips & Best Practices

**✅ Do:**

* Use the "+ Add Property" button to browse and select from your actual HubSpot properties
* Use "Lookup by Email" for contacts when you have their email (more reliable than searching)
* Use "Lookup by Domain" for companies when you know the domain
* Always use `hs_object_id` when you have it (fastest, most reliable)
* Test with a single record before running in a loop on hundreds of records
* Use descriptive output variable names

**❌ Don't:**

* Try to update properties that don't exist for that object type
* Forget to check permissions (need WRITE access, not just READ)
* Assume email/domain lookup works for all object types (Contacts/Companies only)
* Update properties that are managed by HubSpot workflows (may get overwritten)

**Performance tips:**

* Updating by Object ID is fastest (no extra lookup required)
* Only update properties that actually changed (don't update everything)
* If updating many records, use a loop with reasonable batch sizes (100-500)

***

## Related Actions

**What to do next:**

* [Search HubSpot (V2)](./hubspot-v2-search-objects) - Find records to update
* [Lookup HubSpot Object (V2)](./hubspot-v2-lookup-object) - Get record details before updating
* [For Loop](./for_loop) - Update multiple records one by one
* [If Condition](./if_else) - Conditionally update based on property values

**Related guides:**

* [Variable System](../builder/template-variables) - Using variables in update values
* [HubSpot Setup](../user/integrations) - Getting write permissions

***

**Last Updated:** 2025-10-01


# If/Else Statement
Source: https://docs.agent.ai/actions/if_else



Run actions only when certain conditions are met - perfect for conditional logic and branching workflows.

<iframe width="560" height="315" src="https://www.youtube.com/embed/SICac2Zw9kQ?si=q3q2WjgUBd74pvlk" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

Run actions only when certain conditions are met - perfect for conditional logic and branching workflows.

**Common uses:**

* Only update high-value deals
* Skip contacts without email addresses
* Route based on deal stage
* Check if variables exist before using them
* Different actions for different scenarios

**Action type:** `if_condition`

***

## What This Does (The Simple Version)

Think of this like an "if this, then that" rule. You set a condition, and actions inside the if block only run when that condition is true. If it's false, they're skipped.

**Real-world example:**
You're sending follow-up emails to leads. You only want to email contacts who haven't been contacted in the last 7 days. Add an If Condition that checks "last contact date > 7 days ago" - the email action inside only runs if true.

***

## How It Works

The If Condition action evaluates a condition you provide. Based on the result:

**If TRUE:**

* Actions immediately after the If Condition run
* Continues until it reaches an Else Condition or End Condition

**If FALSE:**

* Actions after the If Condition are skipped
* Jumps to Else Condition (if present) or End Condition

**You must end every If Condition with an End Condition action.**

***

## Setting It Up

### Step 1: Add If Condition Action

When you add an If Condition action to your workflow, you'll see a query/condition field.

### Step 2: Write Your Condition

In the **"Condition"** field, describe what you want to check in plain English.

**The condition is evaluated by AI** - you can write it naturally:

**Examples:**

**Check if a value is above a threshold:**

```
The deal amount is greater than 10000
```

**Check if a field has a value:**

```
The contact email is not empty
```

**Check if a date is recent:**

```
The last contact date was within the last 7 days
```

**Check if a variable exists:**

```
The search results variable is not empty
```

**Compare values:**

```
The contact lifecycle stage equals "salesqualifiedlead"
```

**You can use variables** by clicking `{}` or typing them:

```
[deal amount] > 50000
```

### Step 3: Add Actions to Run If True

After the If Condition, add the actions that should run when the condition is TRUE.

**Example:**

1. **If Condition** - Check if deal amount greater than 10000
2. **Update HubSpot Object** - Update to VIP status (runs if TRUE)
3. **Send Email** - Notify sales director (runs if TRUE)
4. **End Condition** - Marks end of if block

### Step 4: Add Else Condition (Optional)

Want different actions if the condition is FALSE?

**Add an Else Condition action** after your "if true" actions:

1. **If Condition** - Check if contact has email
2. **Send Email** - (runs if TRUE)
3. **Else Condition**
4. **Create Task** - Manually find email (runs if FALSE)
5. **End Condition**

### Step 5: Close with End Condition

**Always add End Condition** at the end to close the if/else block.

***

## Condition Examples

### Numeric Comparisons

```
[deal amount] > 10000
[relevance_score] >= 8
[contact_count] < 5
```

### String Comparisons

```
[contact lifecycle_stage] equals "lead"
[deal stage] is "closedwon"
[company industry] contains "technology"
```

### Empty/Exists Checks

```
[contact email] is not empty
[search_results] has items
[timeline_events] is empty
The contact has a phone number
```

### Date Comparisons

```
[deal closedate] is in the future
[contact lastmodifieddate] is within last 30 days
The last activity was more than 7 days ago
```

### Boolean Checks

```
[enrichment_complete] is true
[contact emailoptout] equals false
The contact has not unsubscribed
```

### Complex Conditions

```
The deal amount is greater than 50000 AND the deal stage is "presentationscheduled"
The contact has an email OR a phone number
The lifecycle stage is "lead" or "marketingqualifiedlead"
```

***

## Common Workflows

### Only Update High-Value Deals

**Goal:** Update deal priority only if amount exceeds threshold

1. **Lookup HubSpot Object (V2)**
   * Get deal details
   * Output Variable: `deal`

2. **If Condition**
   * Condition: `[deal amount] > 50000`

3. **Update HubSpot Object (V2)** (inside if block)
   * Update `priority` to "High"

4. **End Condition**

### Skip Contacts Without Email

**Goal:** Send email only if contact has email address

1. **Search HubSpot (V2)**
   * Find contacts
   * Output Variable: `contacts`

2. **For Loop**
   * Loop through: `contacts`
   * Current item: `current_contact`

3. **If Condition** (inside loop)
   * Condition: `[current contact email] is not empty`

4. **Send Email** (inside if block)
   * Send to: `[current contact email]`

5. **End Condition**

6. **End Loop**

### Route by Deal Stage

**Goal:** Different actions based on deal stage

1. **Lookup HubSpot Object (V2)**
   * Get deal
   * Output Variable: `deal`

2. **If Condition**
   * Condition: `[deal stage] equals "closedwon"`

3. **Create Timeline Event** (if won)
   * Log onboarding kickoff

4. **Else Condition**

5. **Update HubSpot Object** (if not won)
   * Update follow-up date

6. **End Condition**

### Check Before Using Variable

**Goal:** Only process if search found results

1. **Search HubSpot (V2)**
   * Search for deals
   * Output Variable: `deals`

2. **If Condition**
   * Condition: `[deals] is not empty`

3. **For Loop** (inside if block)
   * Loop through deals

4. **Process each deal...**

5. **End Loop**

6. **End Condition**

***

## Real Examples

### Lead Qualification

**Scenario:** Auto-qualify leads based on criteria

**Trigger:** Contact created webhook

**Condition:**

```
[contact company] is not empty AND [contact jobtitle] contains "Director" or "VP" or "C-level"
```

**If TRUE:**

* Update lifecycle stage to "salesqualifiedlead"
* Assign to senior sales rep
* Send immediate notification

**If FALSE:**

* Keep as "lead"
* Add to nurture sequence

### Deal Health Check

**Scenario:** Flag stale deals

**Trigger:** Scheduled (daily)

**Inside loop for each deal:**

**If Condition:**

```
The last activity was more than 14 days ago
```

**If TRUE:**

* Update deal property `status` to "stale"
* Create task for owner to follow up

**End Condition**

### Conditional Enrichment

**Scenario:** Only enrich important contacts

**Trigger:** Contact updated webhook

**Condition:**

```
[contact company] is not empty AND [contact lifecycle_stage] equals "salesqualifiedlead"
```

**If TRUE:**

* Run web search for company
* AI enrichment analysis
* Update contact with insights

**Else:**

* Log that contact wasn't enriched
* Add to later enrichment queue

**End Condition**

***

## If/Else Patterns

### Simple If (No Else)

```
1. If Condition
2. Action (runs if true)
3. Action (runs if true)
4. End Condition
5. Action (always runs)
```

### If/Else

```
1. If Condition
2. Action (runs if true)
3. Else Condition
4. Action (runs if false)
5. End Condition
6. Action (always runs)
```

### Multiple Conditions (Nested)

```
1. If Condition - Check A
2.   If Condition - Check B (nested)
3.     Action (runs if both A and B are true)
4.   End Condition
5. End Condition
```

### Sequential Checks

```
1. If Condition - Check if deal > 10000
2.   Update to "High Priority"
3. End Condition

4. If Condition - Check if deal > 50000
5.   Notify VP Sales
6. End Condition
```

***

## Troubleshooting

### Condition Always TRUE (or Always FALSE)

**Actions always run (or never run)**

**Possible causes:**

1. Condition is written incorrectly
2. Variable doesn't exist
3. Variable has unexpected value

**How to fix:**

1. Check execution log - what did the AI evaluate?
2. Test condition with known values first
3. Use simple conditions initially (e.g., `5 > 3` should always be true)
4. Make sure variables exist before referencing them
5. Check variable values in execution log

### Can't Access Variables

**Variable in condition shows as empty**

**Possible causes:**

1. Variable doesn't exist (action before if condition failed)
2. Variable name spelled wrong
3. Wrong path to nested property

**How to fix:**

1. Check execution log - does the variable exist?
2. Verify variable name matches output from previous action
3. For nested properties: `[contact email]` not `[contact.email]`

### Actions After If Condition Not Running

**Expected actions are skipped**

**Possible causes:**

1. Condition evaluated to FALSE
2. Missing End Condition
3. Error inside if block

**How to fix:**

1. Check execution log - what was the condition result (true/false)?
2. Add End Condition after if block
3. Look for errors in actions inside the if block

### Else Block Not Running

**Else actions don't execute when condition is false**

**Possible causes:**

1. Missing Else Condition action
2. Else Condition in wrong place
3. Missing End Condition

**How to fix:**

1. Structure must be: If Condition → \[true actions] → Else Condition → \[false actions] → End Condition
2. Make sure Else Condition is before End Condition
3. Check execution log to see execution path

***

## Tips & Best Practices

**✅ Do:**

* Write conditions in plain English (AI evaluates them)
* Use clear, simple conditions when possible
* Always add End Condition to close if blocks
* Test conditions with known values first
* Check execution log to see true/false result
* Use variables by clicking `{}` button for accuracy
* Add Else Condition for "if false" actions

**❌ Don't:**

* Forget to add End Condition (required)
* Reference variables that might not exist without checking first
* Write overly complex conditions (break into multiple if statements)
* Assume condition will always evaluate as expected (test it)
* Nest too many if conditions (hard to debug)

**Writing good conditions:**

* **Clear:** "The deal amount is greater than 10000"
* **Specific:** "The contact lifecycle stage equals 'salesqualifiedlead'"
* **Testable:** Use values you can verify
* **Safe:** Check if variable exists first if unsure

**Performance tips:**

* Conditions evaluate quickly (less than 1 second)
* Simple conditions faster than complex
* Avoid unnecessary nesting

***

## Related Actions

**Always used together:**

* [End Condition](./end_statement) - Required to close if blocks (can close If, For, or If/Else)
* [Set Variable](./set-variable) - Often used inside if blocks

**Common patterns:**

* Use inside [For Loop](./for_loop) to conditionally process items
* Use with [Update HubSpot Object (V2)](./hubspot-v2-update-object) to conditionally update

**Related guides:**

* [Variable System](./builder/template-variables) - Using variables in conditions

***

**Last Updated:** 2025-10-01


# Invoke Other Agent
Source: https://docs.agent.ai/actions/invoke_other_agent



## Overview

Trigger another agent to perform additional processing or data handling within workflows.

### Use Cases

* **Multi-Agent Workflows**: Delegate tasks to specialized agents.
* **Cross-Functionality**: Utilize existing agent capabilities for enhanced results.

<iframe width="560" height="315" src="https://www.youtube.com/embed/DqWPxjlsT6o?si=uf7kUR209DgbpGpT" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

## Configuration Fields

### Agent ID

* **Description**: Enter the ID of the agent to invoke.
* **Example**: "agent\_123" or "data\_processor."
* **Required**: Yes

### Parameters

* **Description**: Specify parameters for the agent as key-value pairs, one per line.
* **Example**: "action=update" or "user\_id=567."
* **Required**: No

### Output Variable Name

* **Description**: Assign a variable name to store the agent's response.
* **Example**: "agent\_output" or "result\_data."
* **Validation**: Only letters, numbers, and underscores (\_) are allowed.
* **Required**: Yes


# Invoke Web API
Source: https://docs.agent.ai/actions/invoke_web_api



## Overview

The Invoke Web API action allows your agents to make RESTful API calls to external systems and services. This enables access to third-party data sources, submission of information to web services, and integration with existing infrastructure.

### Use Cases

* **External Data Retrieval**: Connect to public or private APIs to fetch real-time data 
* **Data Querying**: Search external databases or services using specific parameters 
* **Third-Party Integrations**: Access services that expose information via REST APIs 
* **Enriching Workflows**: Incorporate external data sources into your agent's processing

<iframe width="560" height="315" src="https://www.youtube.com/embed/WWRn_d4uQhc?si=4bQ0c4K2Dm5m_hwG" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

## **How to Configure Web API Calls**

### **Add the Action**

1. In the Actions drawer, click "Add action"
2. Select the "Workflow and Logic" category
3. Choose "Invoke Web API"

## Configuration Fields

### URL

* **Description**: Enter the web address of the API you want to connect to (this information should be provided in the API documentation) 
* **Example**: [https://api.nasa.gov/planetary/apod?api\_key=DEMO\_KEY](https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY)
* **Required**: Yes

### Method

* **Description**: Choose how you want to interact with the API
* **Options:** 
  * **GET**: Retrieve information (most common) 
  * **POST**: Send information to create something new 
  * **PUT**: Update existing information 
  * **HEAD**: Check if a resource exists without retrieving it
* **Required**: Yes

### Headers (JSON)

* **Description**: Think of these as your "ID card" when talking to an API..
* **Example**: Many APIs need to know who you are before giving you information. For instance, for the X (Twitter) API, you’d need: `{"Authorization": "Bearer YOUR_ACCESS_TOKEN"}`. The API's documentation will usually tell you exactly what to put here.
* **Required**: No

### Body (JSON)

* **Description**: This is the information you want to send to the API. 
  * Only needed when you're sending data (POST or PUT methods). 
* **Example**: when posting a tweet with the X API, you'd include:
  * body:

    ```
    {"text":"Hello world!"}
    ```
  * When using GET requests (just retrieving information), you typically leave this empty.
  * The API's documentation will specify exactly what format to use
* **Required**: No

### Output Variable Name

* **Description**: Assign a variable name to store the API response.
* **Example**: "api\_response" or "rest\_data."
* **Validation**: Only letters, numbers, and underscores (\_) are allowed.
* **Required**: Yes

## **Using API Responses**

The API response will be stored in your specified output variable. You can access specific data points using dot notation:

* `{{variable_name.property}}` 
* `{{variable_name.nested.property}}`

## **Example:** RESTful API Example Agent

See [this simple Grant Search Agent ](https://agent.ai/agent/RESTful-API-Example)that demonstrates API usage:

1. **Step 1**: Collects a research focus from the user
2. **Step 3**: Makes a REST API call to a government grants database with these keywords
3. **Step 5**: Presents the information to the user as a formatted output

This workflow shows how external APIs can significantly expand an agent's capabilities by providing access to specialized data sources that aren't available within the Agent.ai platform itself.


# Post to Bluesky
Source: https://docs.agent.ai/actions/post_to_bluesky



## Overview

Create and post content to Bluesky, allowing for seamless social media updates within workflows.

### Use Cases

* **Social Media Automation**: Share updates directly to Bluesky.
* **Marketing Campaigns**: Schedule and post campaign content.

## Configuration Fields

### Bluesky Username

* **Description**: Enter your Bluesky username/handle (e.g., username.bsky.social).
* **Required**: Yes

### Bluesky Password

* **Description**: Enter your Bluesky account password.
* **Required**: Yes

### Post Content

* **Description**: Provide the text content for your Bluesky post.
* **Example**: "Check out our latest product launch!"
* **Required**: Yes

### Output Variable Name

* **Description**: Assign a variable name to store the post result.
* **Example**: "post\_response" or "bluesky\_post."
* **Validation**: Only letters, numbers, and underscores (\_) are allowed.
* **Required**: Yes


# Save To File
Source: https://docs.agent.ai/actions/save_to_file



## Overview

Save text content as a downloadable file in various formats, including PDF, Microsoft Word, HTML, and more within workflows.

### Use Cases

* **Content Export**: Allow users to download generated content in their preferred file format.
* **Report Generation**: Create downloadable reports from workflow data.
* **Documentation**: Generate and save technical documentation or user guides.

<iframe width="560" height="315" src="https://www.youtube.com/embed/EAbJ9ksHbP8?si=Oyym3CNsMFR98heg" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

## Configuration Fields

### File Type

* **Description**: Select the output file format for the saved content.
* **Options**: PDF, Microsoft Word, HTML, Markdown, OpenDocument Text, TeX File, Amazon Kindle Book File, eBook File, PNG Image File
* **Default**: PDF
* **Required**: Yes

### Body

* **Description**: Provide the content to be saved in the file, including text, bullet points, or other structured information.
* **Example**: "# Project Summary\n\nThis document outlines the key deliverables for the Q3 project."
* **Required**: Yes

### Output Variable Name

* **Description**: Assign a variable name to store the file URL for later reference in the workflow.
* **Example**: "saved\_file" or "report\_document"
* **Validation**: Only letters, numbers, and underscores (\_) are allowed in variable names.
* **Required**: Yes

## Beta Feature

This action is currently in beta. While fully functional, it may undergo changes based on user feedback.


# Save To Google Doc
Source: https://docs.agent.ai/actions/save_to_google_doc



## Overview

Save text content as a Google Doc for documentation, collaboration, or sharing.

### Use Cases

* **Documentation**: Save workflow results as structured documents.
* **Team Collaboration**: Share generated content via Google Docs.

## Configuration Fields

### Title

* **Description**: Enter the title of the Google Doc.
* **Example**: "Project Plan" or "Meeting Notes."
* **Required**: Yes

### Body

* **Description**: Provide the content to be saved in the Google Doc.
* **Example**: "This document outlines the key objectives for Q1..."
* **Required**: Yes


# Search Bluesky Posts
Source: https://docs.agent.ai/actions/search_bluesky_posts



## Overview

Search for Bluesky posts matching specific keywords or criteria to gather social media insights.

### Use Cases

* **Keyword Monitoring**: Track specific terms or hashtags on Bluesky.
* **Trend Analysis**: Identify trending topics or content on the platform.

## Configuration Fields

### Search Query

* **Description**: Enter keywords or hashtags to search for relevant Bluesky posts.
* **Example**: "#AI" or "climate change."
* **Required**: Yes

### Number of Posts to Retrieve

* **Description**: Specify how many posts to fetch.
* **Options**: 1, 5, 10, 25, 50, 100
* **Required**: Yes

### Output Variable Name

* **Description**: Assign a variable name to store the search results.
* **Example**: "bluesky\_search\_results" or "matching\_posts."
* **Validation**: Only letters, numbers, and underscores (\_) are allowed.
* **Required**: Yes


# Search Results
Source: https://docs.agent.ai/actions/search_results



## Overview

Fetch search results from Google or YouTube for specific queries, providing valuable insights and content.

### Use Cases

* **Market Research**: Gather data on trends or competitors.
* **Content Discovery**: Find relevant articles or videos for your workflow.

<iframe width="560" height="315" src="https://www.youtube.com/embed/U7CpTt-Fpco?si=EhprGYprRGY5vuTm" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

## Configuration Fields

### Query

* **Description**: Enter search terms to find relevant results.
* **Example**: "Best AI tools" or "Marketing strategies."
* **Required**: Yes

### Search Engine

* **Description**: Choose the search engine to use for the query.
* **Options**: Google, YouTube
* **Required**: Yes

### Number of Results to Retrieve

* **Description**: Specify how many results to fetch.
* **Options**: 1, 5, 10, 25, 50, 100
* **Required**: Yes

### Output Variable Name

* **Description**: Assign a variable name to store the search results.
* **Example**: "search\_results" or "google\_data."
* **Validation**: Only letters, numbers, and underscores (\_) are allowed.
* **Required**: Yes


# Send Message
Source: https://docs.agent.ai/actions/send_message



## Overview

Send messages to specified recipients, such as emails with formatted content or notifications. All messages are sent from [agent@agentaimail.com](mailto:agent@agentaimail.com).

### Use Cases

* **Customer Communication**: Notify users about updates or confirmations.
* **Team Collaboration**: Share workflow results via email.

<iframe width="560" height="315" src="https://www.youtube.com/embed/dimzBWcPcX0?si=lNJ0mWxvj-9YDR-F" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

## Configuration Fields

### Message Type

* **Description**: Select the type of message to send.
* **Options**: Email
* **Required**: Yes

### Send To

* **Description**: Enter the recipient's address.
* **Example**: "[john.doe@example.com](mailto:john.doe@example.com)."
* **Required**: Yes

### Email Subject

* **Description:** The subject line of the email to be sent
* **Example:** "Agent results for Agent X"
* **Required:** yes

### Output Formatted

* **Description**: Provide the message content, formatted as needed.
* **Example**: "Hello, your order is confirmed!" or formatted HTML for emails.
* **Required**: Yes


# Call Serverless Function
Source: https://docs.agent.ai/actions/serverless_function



## Overview

Serverless Functions allow your agents to execute custom code in the cloud without managing infrastructure. This powerful capability enables complex operations and integrations beyond what standard actions can provide.

### Use Cases

* **Custom Logic Implementation**: Execute specialized code for unique business requirements
* **External System Integration**: Connect with third-party services and APIs
* **Advanced Data Processing**: Perform complex calculations and transformations
* **Extended Functionality**: Add capabilities not available in standard Agent.ai actions

<iframe width="560" height="315" src="https://www.youtube.com/embed/n5nTAzKGy18?si=6iUG3xZu3ekwG3GU" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

## **How Serverless Functions Work**

Serverless Functions in Agent.ai:

1. Run in AWS Lambda (fully managed by Agent.ai)
2. Support Python and Node.js
3. Automatically deploy when you save the action
4. Generate a REST API endpoint for programmatic access

## Creating a Serverless Function

1. In the Actions tab, click "Add action"
2. Select the "Workflow & Logic" category
3. Choose "Call Serverless Function"

## Configuration Fields

### Language

* **Description**: Select the programming language for the serverless function.
* **Options**: Python, Node
* **Required**: Yes

### Serverless Code

* **Description**: Write your custom code.
* **Example**: Python or Node script performing custom logic.
* **Required**: Yes

### Serverless API URL

* **Description**: Provide the API URL for the deployed serverless function.
* **Required**: Yes (auto-generated upon deployment)

### Output Variable Name

* **Description**: Assign a variable name to store the result of the serverless function.
* **Example**: "function\_result" or "api\_response."
* **Validation**: Only letters, numbers, and underscores (`_`) are allowed.
* **Required**: Yes

### Deploy and Save

1. Click "Save"
2. After successful deployment, the serverless action can be used

### Using Function Results

The function's output is stored in your specified variable name. You can access specific data points using dot notation, for example:

* `{{variable_name.message}}`
* `{{variable_name.input}}`

## Accessing Agent Variables

When your agent runs a serverless function, any context variables created earlier in the workflow are passed into your function as part of the event object.

Understanding how to access these variables is key to using serverless functions effectively.

<iframe width="560" height="315" src="https://www.youtube.com/embed/bGnCZpjKJWw?si=oeyi6XDsFcW-sTOl" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

### Inspecting the Event Structure

To inspect the data being passed to your function, you can set up a basic debug function. This is helpful for confirming that your agent variables are available and structured as expected.

```python  theme={null}
import json

def execute(event, context):
    debug_info = {
        "received_event": json.dumps(event),
        "received_context": str(context)
    }

    return {
        "statusCode": 200,
        "body": json.dumps({
            "debug_info": debug_info
        })
    }
```

Running your agent with this code will return the full contents of the event and context objects. In most cases, the information you’ll want is located here:

`event['body']['context']`

This nested context object contains your agent's variables—such as out\_topic, out\_summary, and others defined earlier in your workflow.

### Accessing Variables in Your Code

Once you understand the structure, you can write your function to access specific values like this:

```python  theme={null}
import json

def execute(event, context):
    body = event.get('body', {})
    agent_context = body.get('context', {})

    topic = agent_context.get('out_topic')
    summary = agent_context.get('out_summary')

    result = f"The topic is {topic} and the summary is {summary}"

    return {
        "statusCode": 200,
        "body": json.dumps({
            "result": result
        })
    }
```

You can now use these variables to power more complex logic in your serverless functions.

### Notes on Debugging

* Use the `return` statement to pass debugging information back to the agent UI. `print()` statements will only appear in AWS logs.
* The context panel in [Agent.ai](http://Agent.ai) shows the variables currently available to your serverless function—this can help confirm what’s being passed in.
* If your function isn’t behaving as expected, start by confirming that the data is structured as described above.

## Example: Serverless Function Agent

See [this simple Message Analysis Agent](https://agent.ai/agent/serverless-function-example) that demonstrates how to use Serverless Functions:

1. **Step 1**: Get user input text message
2. **Step 2**: Call a serverless function that analyzes:
   * Word count
   * Character count
   * Sentiment (positive/negative/neutral)
3. **Step 3**: Display the results in a formatted output

This sample agent shows how Serverless Functions can extend your agent's capabilities with custom logic that would be difficult to implement using standard actions alone.


# Set Variable
Source: https://docs.agent.ai/actions/set-variable



Create or update variables during workflow execution - store values, build counters, calculate totals, or save results for later actions.

<img src="https://mintcdn.com/agentai/UYmyskpA4wsMD1WI/images/set_variable.png?fit=max&auto=format&n=UYmyskpA4wsMD1WI&q=85&s=7b7eb43e684aeb09dc2dcbec1f2c055d" alt="Set Variable Pn" data-og-width="1194" width="1194" data-og-height="1148" height="1148" data-path="images/set_variable.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/UYmyskpA4wsMD1WI/images/set_variable.png?w=280&fit=max&auto=format&n=UYmyskpA4wsMD1WI&q=85&s=dc714a20e0020bb27efce40ed8fadda7 280w, https://mintcdn.com/agentai/UYmyskpA4wsMD1WI/images/set_variable.png?w=560&fit=max&auto=format&n=UYmyskpA4wsMD1WI&q=85&s=2f14286f91b09bccc6ba1493548f7e8f 560w, https://mintcdn.com/agentai/UYmyskpA4wsMD1WI/images/set_variable.png?w=840&fit=max&auto=format&n=UYmyskpA4wsMD1WI&q=85&s=0b6ce0c1b590a3fb33749806a0eb9681 840w, https://mintcdn.com/agentai/UYmyskpA4wsMD1WI/images/set_variable.png?w=1100&fit=max&auto=format&n=UYmyskpA4wsMD1WI&q=85&s=58fffd19d8edf62b8d4bc84f274d0bd4 1100w, https://mintcdn.com/agentai/UYmyskpA4wsMD1WI/images/set_variable.png?w=1650&fit=max&auto=format&n=UYmyskpA4wsMD1WI&q=85&s=9e4010787ea8b5794f8af5803b27f6af 1650w, https://mintcdn.com/agentai/UYmyskpA4wsMD1WI/images/set_variable.png?w=2500&fit=max&auto=format&n=UYmyskpA4wsMD1WI&q=85&s=092b65ef7234c0d728a3775fb1a49e82 2500w" />

**Common uses:**

* Create counters in loops
* Store calculated values
* Build text from multiple sources
* Save API responses
* Track totals across iterations
* Set default values

**Action type:** `set_variable`

***

## What This Does (The Simple Version)

Think of this like creating a sticky note during your workflow. You can write down a value and give it a name - then use that name in later actions. It's useful for calculations, counters, or storing data you'll need again.

**Real-world example:**
You're looping through 50 deals and want to count how many are high-value. Create a counter variable set to `0`, then inside the loop, increase it by 1 each time you find a high-value deal. After the loop, you know exactly how many there are.

***

## How It Works

The Set Variable action creates or updates a variable. You specify:

1. **Variable name** - What to call it
2. **Value** - What to store (text, number, or data from other variables)

**If the variable exists:** It updates it
**If it doesn't exist:** It creates it

The variable persists through the rest of the workflow and can be referenced in any later action.

***

## Setting It Up

### Step 1: Add Set Variable Action

Add the **Set Variable** action to your workflow.

### Step 2: Name Your Variable

In the **"Variable Name"** field, type a name for your variable.

**Good names:**

* `deal_count`
* `total_amount`
* `high_priority_deals`
* `enrichment_result`
* `calculated_score`

**Naming rules:**

* Use lowercase letters, numbers, underscores
* No spaces or special characters
* Make it descriptive

### Step 3: Set the Value

In the **"Value"** field, enter what you want to store.

**Three ways to set values:**

**Option 1: Type directly**

* Type text or numbers directly
* Example: `0` (for a counter)
* Example: `High Priority` (for a status)

**Option 2: Insert variables**

* Hover to see `{}` button
* Click to select variable from previous action
* Example: Click `{}` → `deal_record` → `properties` → `amount`

**Option 3: Combine text and variables**

* Mix typed text with variables
* Example: Type "Total: \$" then click `{}` → select `total_amount`
* Result: "Total: \$50000"

***

## Common Patterns

### Create a Counter

**Goal:** Count items in a loop

**Setup:**

1. **Before loop** - Set Variable
   * Variable Name: `counter`
   * Value: `0`

2. **Inside loop** - Set Variable
   * Variable Name: `counter`
   * Value: Click `{}` → `counter`, then type ` + 1` (AI evaluates math)

**Result:** After loop, `counter` contains total count

### Calculate a Total

**Goal:** Add up deal amounts

**Setup:**

1. **Before loop** - Set Variable
   * Variable Name: `total_amount`
   * Value: `0`

2. **Inside loop** - Set Variable
   * Variable Name: `total_amount`
   * Value: \{\{total\_amount}} + \{\{current\_deal.properties.amount}}

**Result:** After loop, `total_amount` is the sum

### Store a Calculation

**Goal:** Calculate a percentage

**Setup:**

* **Set Variable**
  * Variable Name: `win_rate`
  * Value: \{\{won\_deals}} / \{\{total\_deals}} \* 100

**Result:** `win_rate` contains the percentage

### Build Text from Multiple Parts

**Goal:** Create a summary message

**Setup:**

* **Set Variable**
  * Variable Name: `summary`
  * Value: Type "Deal " then click `{}` → `deal_name`, type " worth \$" then click `{}` → `deal_amount`, type " closed on " then click `{}` → `close_date`

**Result:** `summary` = "Deal Acme Corp worth \$50000 closed on 2025-01-15"

### Set a Default Value

**Goal:** Provide fallback if data is missing

**Setup:**

* **Set Variable**
  * Variable Name: `contact_name`
  * Value: \{\{contact.properties.firstname}} \{\{contact.properties.lastname}} or if empty `Unknown Contact`

**Result:** `contact_name` has name or "Unknown Contact"

***

## Common Workflows

### Count High-Value Deals

**Goal:** Count how many deals exceed threshold

1. **Set Variable** (before loop)
   * Variable Name: `high_value_count`
   * Value: `0`

2. **Search HubSpot (V2)**
   * Find all deals
   * Output Variable: `all_deals`

3. **For Loop**
   * Loop through: `all_deals`
   * Current item: `current_deal`

4. **If Condition** (inside loop)
   * Condition: \{\{current\_deal.properties.amount}} > 50000

5. **Set Variable** (inside if block)
   * Variable Name: `high_value_count`
   * Value: \{\{high\_value\_count}} + 1

6. **End Condition**

7. **End Loop**

**Result:** `high_value_count` contains the total

### Build a Report Summary

**Goal:** Create text summary from multiple sources

1. **Search HubSpot (V2)**
   * Find deals
   * Output Variable: `deals`

2. **Get Timeline Events**
   * Get activity
   * Output Variable: `events`

3. **Set Variable**
   * Variable Name: `report`
   * Value: "Found \{\{deals}} deals with \{\{events}} total activities"

4. **Send Email**
   * Body: Click `{}` → select `report`

### Track Running Total

**Goal:** Sum deal amounts across multiple stages

1. **Set Variable**
   * Variable Name: `total_pipeline`
   * Value: `0`

2. **For Loop** through deals

3. **Set Variable** (inside loop)
   * Variable Name: `total_pipeline`
   * Value: \{\{total\_pipeline}} + \{\{current\_deal.properties.amount}}

4. **End Loop**

5. **Update HubSpot Object**
   * Update custom property with `total_pipeline`

***

## Real Examples

### Deal Stage Counter

**Scenario:** Count deals in each stage

**Before loop:**

* Set `proposal_count` = `0`
* Set `negotiation_count` = `0`
* Set `closed_won_count` = `0`

**Inside loop:**

* If stage = "proposal" → Increment `proposal_count`
* If stage = "negotiation" → Increment `negotiation_count`
* If stage = "closedwon" → Increment `closed_won_count`

**After loop:** Use counts in report or dashboard update

### Enrichment Scoring

**Scenario:** Build a lead score from multiple factors

**Setup:**

* Set `score` = `0`
* If company exists → Set `score` = \{\{score}} + 10
* If job title contains "VP" → Set `score` = \{\{score}} + 15
* If email domain is corporate → Set `score` = \{\{score}} + 5
* If LinkedIn profile found → Set `score` = \{\{score}} + 10

**Result:** `score` contains total lead score

***

## Troubleshooting

### Variable Not Updating

**Value stays the same despite Set Variable**

**Possible causes:**

1. Set Variable action not running (inside skipped if block)
2. Variable name misspelled
3. Value formula incorrect

**How to fix:**

1. Check execution log - did action run?
2. Verify exact variable name (case-sensitive)
3. Test formula with simple values first
4. Check if variable exists before trying to update

### Math Not Working

**Calculation returns wrong value**

**Possible causes:**

1. Variables are text, not numbers
2. Formula syntax incorrect
3. Empty/null values in calculation

**How to fix:**

1. AI evaluates math - write it naturally: `5 + 3` or \{\{count}} + 1
2. Check execution log for actual values
3. Handle empty values: use If Condition to check first
4. Convert text to numbers if needed

### Variable Not Available Later

**Can't select variable in later action**

**Possible causes:**

1. Variable created inside loop (only exists inside loop)
2. Variable created inside if block (only exists in that block)
3. Set Variable action failed

**How to fix:**

1. Create variable BEFORE loop/if block if you need it after
2. Check execution log - did Set Variable succeed?
3. Variables created inside loops/if blocks have limited scope

### Wrong Variable Used

**Selected wrong variable from picker**

**Possible causes:**

1. Similar variable names
2. Variable from different loop iteration

**How to fix:**

1. Use descriptive names: `deal_count` not `count`
2. Check variable picker shows correct source
3. Review execution log to verify values

***

## Tips & Best Practices

**✅ Do:**

* Use descriptive variable names (`high_value_count` not `x`)
* Initialize counters to `0` before loops
* Initialize totals to `0` before calculations
* Use Set Variable for values you'll reference multiple times
* Create variables outside loops if you need them after
* Check execution log to verify values

**❌ Don't:**

* Use variable names that are too similar (`count1`, `count2`)
* Forget to initialize counters (leads to errors)
* Try to use variables before creating them
* Assume variables from loops persist after loop
* Overcomplicate formulas (break into multiple Set Variable actions)

**Performance tips:**

* Set Variable is instant (less than 0.1 seconds)
* No limit on number of variables
* Variables are lightweight (don't impact performance)

**Naming conventions:**

* **Counters:** `item_count`, `total_deals`, `high_priority_count`
* **Totals:** `total_amount`, `sum_value`, `pipeline_total`
* **Calculations:** `win_rate`, `average_score`, `conversion_rate`
* **Text:** `summary`, `message`, `report_text`
* **Status:** `processing_status`, `result_code`

***

**Last Updated:** 2025-10-01


# Show User Output
Source: https://docs.agent.ai/actions/show_user_output



## Overview

The "Show User Output" action displays information to users in a visually organized way. It lets you present data, results, or messages in different formats to make them easy to read and understand.

### Use Cases

* **Real-time Feedback**: Display data summaries or workflow outputs to users.

* **Interactive Reports**: Present results in a structured format like tables or markdown.

## **How to Configure**

### **Step 1: Add the Action**

1. In the Actions tab, click "Add action"

2. Select "Show User Output" from the options

## Step 2: Configuration Fields

### Heading

* **Description**: Provide a heading for the output display.

* **Example**: "User Results" or "Analysis Summary."

* **Required**: No

### Output Formatted

* **Description**: Enter the formatted output in HTML, JSON, or Markdown.

* **Example**:&#x20;

1. Can be text: "Here are your results"

2. Or a variable: \{\{analysis\_results}}

3. Or a mix of both: "Analysis complete: \{\{analysis\_results}}"

* **Required**: Yes

### Format

* **Description**: Choose the format for output display.

* **Options**: Auto, HTML, JSON, Table, Markdown, Audio, Text, JSX

* **Example**: "HTML" for web-based formatting.

* **Required**: Yes

## **Output Formats Explained**

### **Auto**

Agent.AI will try to detect the best format automatically based on your content. Use this when you're unsure which format to choose.

### **HTML**

Displays content with web formatting (like colors, spacing, and styles).

* Example: \<h1>Results\</h1>\<p>Your information is ready.\</p>

* Good for: Creating visually structured content with different text sizes, colors, or layouts

* Tip: When using AI tools like Claude or GPT, you can ask them to format their responses in HTML

### **Markdown**

A simple way to format text with headings, lists, and emphasis.

* Example: # Results\n\n- First item\n- Second item

* Good for: Creating organized content with simple formatting needs

* Tip: You can ask AI models to output their responses in Markdown format for easier display

### **JSON**

Displays data in a structured format with keys and values.

* Example: \{"name": "John", "age": 30, "email": "[john@example.com](mailto:john@example.com)"}

* Good for: Displaying data in an organized, hierarchical structure

* To get a specific part of a JSON string, use dot notation:

  * \{\{user\_data.name}} to display just the name

  * \{\{weather.forecast.temperature}} to display a nested value

  * For array items, use: \{\{items.0}} for the first item, \{\{items.1}} for the second, etc.

* Tip: You can request AI models to respond in JSON format when you need structured data

### **Table**

Shows information in rows and columns, like a spreadsheet.

* **Important**: Tables requires a very specific format:

1\) A JSON array of arrays:

```
[
  ["Column 1", "Column 2", "Column 3"],
  ["Row 1 Data", "More Data", "Even More"],
  ["Row 2 Data", "More Data", "Even More"]
]
```

2\) Or a CSV:

```
Column 1,Column 2,Column 3
Row 1 Data,More Data,Even More
Row 2 Data,More Data,Even More
```

See [<u>this example agent</u>](https://agent.ai/agent/Table-Creator) for table output format.

### **Text**

Simple plain text without any special formatting. What you type is exactly what the user sees.

* Good for: Simple messages or information that doesn't need special formatting

### **Audio**

Displays an audio player to play sound files. See [<u>this agent</u>](https://agent.ai/agent/autio-template) as an example. 

### **JSX**

For technical users who need to create complex, interactive displays.

* Good for: Interactive components with special styling needs

* Requires knowledge of React JSX formatting


# Store Variable to Database
Source: https://docs.agent.ai/actions/store_variable_to_database



# Overview

Store variables in the agent's database for tracking and retrieval in future workflows.

### Use Cases

* **Historical Tracking**: Save variables for analysis over time.

* **Data Persistence**: Ensure key variables are available across workflows.

## Configuration Fields

### Variable

* **Description**: Specify the variable to store in the database.

* **Example**: "user\_input" or "order\_status."

* **Required**: Yes

***


# Use GenAI (LLM)
Source: https://docs.agent.ai/actions/use_genai



## Overview

Invoke a language model (LLM) to generate text based on input instructions, enabling creative and dynamic text outputs.

### Use Cases

* **Content Generation**: Draft blog posts, social media captions, or email templates.
* **Summarization**: Generate concise summaries of complex documents.
* **Customer Support**: Create personalized responses or FAQs.

## Configuration Fields

### LLM Engine

* **Description**: Select the language model to use for generating text.
* **Options**: Auto Optimized, GPT-4o, Claude Opus, Gemini 2.0 Flash, and more.
* **Example**: "GPT-4o" for detailed responses or "Claude Opus" for creative writing.
* **Required**: Yes

### Instructions

* **Description**: Enter detailed instructions for the language model.
* **Example**: "Write a summary of this document" or "Generate a persuasive email."
* **Required**: Yes

### Output Variable Name

* **Description**: Assign a variable name to store the generated text.
* **Example**: "llm\_output" or "ai\_generated\_text."
* **Validation**: Only letters, numbers, and underscores (\_) are allowed.
* **Required**: Yes


# Wait for User Confirmation
Source: https://docs.agent.ai/actions/wait_for_user_confirmation



## Overview

The "Wait for User Confirmation" action pauses the workflow until the user explicitly confirms to proceed.

### Use Cases

* **Decision Points**: Pause workflows at critical junctures to confirm user consent.
* **Verification**: Ensure users are ready to proceed to the next steps.

## Configuration Fields

### Message to Show User (optional)

* **Description**: Enter a message to prompt the user for confirmation.
* **Example**: "Are you sure you want to proceed?" or "Click OK to continue."
* **Required**: No


# Web Page Content
Source: https://docs.agent.ai/actions/web_page_content



## Overview

Extract text content from a specified web page for analysis or use in workflows.

### Use Cases

* **Data Extraction**: Retrieve content from web pages for structured analysis.
* **Content Review**: Automate the review of online articles or blogs.

## Configuration Fields

### URL

* **Description**: Enter the URL of the web page to extract content from.
* **Example**: "[https://example.com/article](https://example.com/article)."
* **Required**: Yes

### Mode

* **Description**: Choose between scraping a single page or crawling multiple pages.
* **Options**: Single Page, Multi-page Crawl
* **Required**: Yes

### Output Variable Name

* **Description**: Assign a variable name to store the extracted content.
* **Example**: "web\_content" or "page\_text."
* **Validation**: Only letters, numbers, and underscores (\_) are allowed.
* **Required**: Yes


# Web Page Screenshot
Source: https://docs.agent.ai/actions/web_page_screenshot



## Overview

Capture a visual screenshot of a specified web page for documentation or analysis.

### Use Cases

* **Archiving**: Save visual records of web pages.
* **Presentation**: Use screenshots for reports or presentations.

## Configuration Fields

### URL

* **Description**: Enter the URL of the web page to capture.
* **Example**: "[https://example.com](https://example.com)."
* **Required**: Yes

### Cache Expiration Time

* **Description**: Specify how often to refresh the screenshot.
* **Options**: 1 hour, 1 day, 1 week, 1 month
* **Required**: Yes

### Output Variable Name

* **Description**: Assign a variable name to store the screenshot.
* **Example**: "web\_screenshot" or "page\_image."
* **Validation**: Only letters, numbers, and underscores (\_) are allowed.
* **Required**: Yes


# YouTube Channel Data
Source: https://docs.agent.ai/actions/youtube_channel_data



## Overview

Retrieve detailed information about a YouTube channel, including its videos and statistics.

### Use Cases

* **Audience Analysis**: Understand the content and engagement metrics of a channel.
* **Competitive Research**: Analyze competitors' channels.

## Configuration Fields

### YouTube Channel URL

* **Description**: Provide the URL of the YouTube channel to analyze.
* **Example**: "[https://youtube.com/channel/UC12345](https://youtube.com/channel/UC12345)."
* **Required**: Yes

### Output Variable Name

* **Description**: Assign a variable name to store the channel data.
* **Example**: "channel\_data" or "youtube\_info."
* **Validation**: Only letters, numbers, and underscores (\_) are allowed.
* **Required**: Yes


# YouTube Search Results
Source: https://docs.agent.ai/actions/youtube_search_results



## Overview

Perform a YouTube search and retrieve results for specified queries.

### Use Cases

* **Content Discovery**: Find relevant YouTube videos for research or campaigns.
* **Trend Monitoring**: Identify trending videos or topics.

<iframe width="560" height="315" src="https://www.youtube.com/embed/yrHbh5pnCW8?si=_nhWaN3B6auJXZX1" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

## Configuration Fields

### Query

* **Description**: Enter search terms for YouTube.
* **Example**: "Machine learning tutorials" or "Travel vlogs."
* **Required**: Yes

### Output Variable Name

* **Description**: Assign a variable name to store the search results.
* **Example**: "youtube\_results" or "video\_list."
* **Validation**: Only letters, numbers, and underscores (\_) are allowed.
* **Required**: Yes


# AI Agents Explained
Source: https://docs.agent.ai/ai-agents-explained

Understanding the basics of AI agents for beginners

<iframe width="560" height="315" src="https://www.youtube.com/embed/RbnXeQkzyWg?si=WjE6maYfY5K5qmfl" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

# **What Is an AI Agent?**

An AI agent is essentially a digital worker that helps you achieve specific objectives. Think of it as a virtual assistant that can take on tasks with varying levels of independence. Unlike basic AI tools that simply respond to prompts, agents can work toward goals by taking multiple steps and making decisions along the way.

When you work with an AI agent:

* You define a goal for the agent to accomplish
* The agent selects appropriate actions to meet that goal
* It interacts with its environment and adapts to changes
* It collects and processes necessary data
* It executes tasks to achieve the defined goal

# **How AI Agents Work: A Real Example**

Let's say you create an AI sales development representative (SDR) agent with the goal of generating leads. Here's how it would work:

1. You define the objective: "Generate 20 qualified leads this month"
2. The agent selects necessary tasks:
3. Find potential leads from various sources
   * Research information about those leads
   * Generate personalized outreach messages
   * Send initial emails
   * Monitor for responses
   * Send follow-up emails when needed
4. The agent gathers and processes information about the leads
5. It executes each task in sequence
6. It works toward achieving your defined goal

# **Understanding Levels of AI Agent Autonomy**

It's important to understand that AI agents exist on a spectrum of autonomy. Current technology isn't yet at the point where you can simply define a goal and let the agent handle everything independently. Here's how to think about the different levels:

## **Level 0: No Autonomy**

* Acts purely as a tool with no initiative
* Similar to traditional machine learning algorithms
* Only does exactly what it was programmed to do

## **Level 1: Assistive Autonomy**

* Handles simple tasks with direct instruction
* Similar to how ChatGPT works - you provide a prompt, it responds
* Each interaction requires specific direction

## **Level 2: Partial Autonomy**

* Manages multi-step tasks
* Requires human oversight and intervention
* This is where most current agent platforms like [Agent.ai](http://Agent.ai) operate

## **Level 3: High Autonomy**

* Achieves complex tasks with minimal human input
* Requires occasional guidance

## **Level 4: Full Autonomy**

* Handles all aspects of tasks independently
* You simply define the goal and the agent figures out everything else

# [******What Is Agent.ai?******](http://Agent.ai)

[Agent.ai](http://Agent.ai) is a low-code/no-code platform that allows you to build AI agents without programming knowledge. While developers have access to tools like LangChain or [Crew.ai](http://Crew.ai) that require coding, [Agent.ai](http://Agent.ai) gives business stakeholders the ability to configure their own agents through a user-friendly interface.

With [Agent.ai](http://Agent.ai), you can:

* Create custom AI agents tailored to your specific needs
* Configure multi-step workflows
* Define how your agent should interact with various systems
* Set up decision-making parameters
* Deploy agents that can help achieve your business goals

## **Getting Started**

To begin using [Agent.ai](http://Agent.ai), you'll need to:

1. Clearly define the goal you want your agent to accomplish
2. Break down the steps required to achieve that goal
3. Configure your agent using the [Agent.ai](http://Agent.ai) platform
4. Test your agent's performance
5. Refine and improve as needed

In the current state of AI agent technology, you'll still need to provide some oversight and guidance, but the platform handles much of the complexity for you.

Have questions or need help? Reach out to our [support team](https://agent.ai/feedback) or [community](https://community.agent.ai/feed).


# Convert file
Source: https://docs.agent.ai/api-reference/advanced/convert-file

api-reference/v1/v1.0.1_openapi.json post /action/convert_file
Convert a file to a different format.



# Convert file options
Source: https://docs.agent.ai/api-reference/advanced/convert-file-options

api-reference/v1/v1.0.1_openapi.json post /action/convert_file_options
Gets the full set of options that a file extension can be converted to.



# Invoke Agent
Source: https://docs.agent.ai/api-reference/advanced/invoke-agent

api-reference/v1/v1.0.1_openapi.json post /action/invoke_agent
Trigger another agent to perform additional processing or data handling within workflows.



# REST call
Source: https://docs.agent.ai/api-reference/advanced/rest-call

api-reference/v1/v1.0.1_openapi.json post /action/rest_call
Make a REST API call to a specified endpoint.



# Retrieve Variable
Source: https://docs.agent.ai/api-reference/advanced/retrieve-variable

api-reference/v1/v1.0.1_openapi.json post /action/get_variable_from_database
Retrieve a variable from the agent's database



# Store Variable
Source: https://docs.agent.ai/api-reference/advanced/store-variable

api-reference/v1/v1.0.1_openapi.json post /action/store_variable_to_database
Store a variable in the agent's database



# Search
Source: https://docs.agent.ai/api-reference/agent-discovery/search

api-reference/v1/v1.0.1_openapi.json post /action/search
Search and discover agents based on various criteria including status, tags, and search terms.



# Save To File
Source: https://docs.agent.ai/api-reference/create-output/save-to-file

api-reference/v1/v1.0.1_openapi.json post /action/create_file
Save text content as a downloadable file.



# Enrich Company Data
Source: https://docs.agent.ai/api-reference/get-data/enrich-company-data

api-reference/v1/v1.0.1_openapi.json post /action/get_company_object
Gather enriched company data using Breeze Intelligence for deeper analysis and insights.



# Find LinkedIn Profile
Source: https://docs.agent.ai/api-reference/get-data/find-linkedin-profile

api-reference/v1/v1.0.1_openapi.json post /action/find_linkedin_profile
Find the LinkedIn profile slug for a person.



# Get Bluesky Posts
Source: https://docs.agent.ai/api-reference/get-data/get-bluesky-posts

api-reference/v1/v1.0.1_openapi.json post /action/get_bluesky_posts
Fetch recent posts from a specified Bluesky user handle, making it easy to monitor activity on the platform.



# Get Company Earnings Info
Source: https://docs.agent.ai/api-reference/get-data/get-company-earnings-info

api-reference/v1/v1.0.1_openapi.json post /action/company_financial_info
Retrieve company earnings information for a given stock symbol over time.



# Get Company Financial Profile
Source: https://docs.agent.ai/api-reference/get-data/get-company-financial-profile

api-reference/v1/v1.0.1_openapi.json post /action/company_financial_profile
Retrieve detailed financial and company profile information for a given stock symbol, such as market cap and the last known stock price for any company.



# Get Domain Information
Source: https://docs.agent.ai/api-reference/get-data/get-domain-information

api-reference/v1/v1.0.1_openapi.json post /action/domain_info
Retrieve detailed information about a domain, including its registration details, DNS records, and more.



# Get Instagram Followers
Source: https://docs.agent.ai/api-reference/get-data/get-instagram-followers

api-reference/v1/v1.0.1_openapi.json post /action/get_instagram_followers
Retrieve a list of top followers from a specified Instagram account for social media analysis.



# Get Instagram Profile
Source: https://docs.agent.ai/api-reference/get-data/get-instagram-profile

api-reference/v1/v1.0.1_openapi.json post /action/get_instagram_profile
Fetch detailed profile information for a specified Instagram username.



# Get LinkedIn Activity
Source: https://docs.agent.ai/api-reference/get-data/get-linkedin-activity

api-reference/v1/v1.0.1_openapi.json post /action/get_linkedin_activity
Retrieve recent LinkedIn posts from specified profiles to analyze professional activity and engagement.



# Get LinkedIn Profile
Source: https://docs.agent.ai/api-reference/get-data/get-linkedin-profile

api-reference/v1/v1.0.1_openapi.json post /action/get_linkedin_profile
Retrieve detailed information from a specified LinkedIn profile for professional insights.



# Get Recent Tweets
Source: https://docs.agent.ai/api-reference/get-data/get-recent-tweets

api-reference/v1/v1.0.1_openapi.json post /action/get_recent_tweets
This action fetches recent tweets from a specified Twitter handle.



# Get Twitter Users
Source: https://docs.agent.ai/api-reference/get-data/get-twitter-users

api-reference/v1/v1.0.1_openapi.json post /action/get_twitter_users
Search and retrieve Twitter user profiles based on specific keywords for targeted social media analysis.



# Google News Data
Source: https://docs.agent.ai/api-reference/get-data/google-news-data

api-reference/v1/v1.0.1_openapi.json post /action/get_google_news
Fetch news articles based on queries and date ranges to stay updated on relevant topics or trends.



# Search Bluesky Posts
Source: https://docs.agent.ai/api-reference/get-data/search-bluesky-posts

api-reference/v1/v1.0.1_openapi.json post /action/search_bluesky_posts
Search for Bluesky posts matching specific keywords or criteria to gather social media insights.



# Search Results
Source: https://docs.agent.ai/api-reference/get-data/search-results

api-reference/v1/v1.0.1_openapi.json post /action/get_search_results
Fetch search results from Google or YouTube for specific queries, providing valuable insights and content.



# Web Page Content
Source: https://docs.agent.ai/api-reference/get-data/web-page-content

api-reference/v1/v1.0.1_openapi.json post /action/grab_web_text
Extract text content from a specified web page or domain.



# Web Page Screenshot
Source: https://docs.agent.ai/api-reference/get-data/web-page-screenshot

api-reference/v1/v1.0.1_openapi.json post /action/grab_web_screenshot
Capture a visual screenshot of a specified web page for documentation or analysis.



# YouTube Channel Data
Source: https://docs.agent.ai/api-reference/get-data/youtube-channel-data

api-reference/v1/v1.0.1_openapi.json post /action/get_youtube_channel
Retrieve detailed information about a YouTube channel, including its videos and statistics.



# YouTube Search Results
Source: https://docs.agent.ai/api-reference/get-data/youtube-search-results

api-reference/v1/v1.0.1_openapi.json post /action/run_youtube_search
Perform a YouTube search and retrieve results for specified queries.



# YouTube Video Transcript
Source: https://docs.agent.ai/api-reference/get-data/youtube-video-transcript

api-reference/v1/v1.0.1_openapi.json post /action/get_youtube_transcript
Fetches the transcript of a YouTube video using the video URL.



# Get HubSpot Company Data
Source: https://docs.agent.ai/api-reference/hubspot/get-hubspot-company-data

api-reference/v1/v1.0.1_openapi.json post /action/get_hubspot_company_object
Retrieve company data from HubSpot based on a query or get the most recent company.



# Get HubSpot Contact Data
Source: https://docs.agent.ai/api-reference/hubspot/get-hubspot-contact-data

api-reference/v1/v1.0.1_openapi.json post /action/get_hubspot_contact_object
Retrieve contact data from HubSpot based on a query or get the most recent contact.



# Get HubSpot Object Data
Source: https://docs.agent.ai/api-reference/hubspot/get-hubspot-object-data

api-reference/v1/v1.0.1_openapi.json post /action/get_hubspot_object
Retrieve data for any supported HubSpot object type based on a query or get the most recent object.



# Get HubSpot Owners
Source: https://docs.agent.ai/api-reference/hubspot/get-hubspot-owners

api-reference/v1/v1.0.1_openapi.json post /action/get_hubspot_owners
Retrieve all owners (users) from a HubSpot portal.



# Convert text to speech
Source: https://docs.agent.ai/api-reference/use-ai/convert-text-to-speech

api-reference/v1/v1.0.1_openapi.json post /action/output_audio
Convert text to a generated audio voice file.



# Generate Image
Source: https://docs.agent.ai/api-reference/use-ai/generate-image

api-reference/v1/v1.0.1_openapi.json post /action/generate_image
Create visually engaging images using AI models, with options for style, aspect ratio, and detailed prompts.



# Use GenAI (LLM)
Source: https://docs.agent.ai/api-reference/use-ai/use-genai-llm

api-reference/v1/v1.0.1_openapi.json post /action/invoke_llm
Invoke a language model (LLM) to generate text based on input instructions, enabling creative and dynamic text outputs.



# Knowledge Base & Files
Source: https://docs.agent.ai/builder/kb-and-files



[Knowledge bases in ](https://agent.ai/builder/files)[Agent.ai](http://Agent.ai) are organized collections of documents that your agents can reference in their workflows. Think of them as specialized folders containing information that you want your agents to know and use. You could have separate knowledge bases for product documentation, internal policies, and more.

Knowledge bases and files can be used in certain agent actions like:

[Get User KBs and Files](https://docs.agent.ai/actions/get_user_knowledge_base_and_files)

[Get Data from Builder’s Knowledge Base](https://docs.agent.ai/actions/get_data_from_builders_knowledgebase)

<img src="https://mintcdn.com/agentai/124P12t85CIi-2hH/images/kb-files.png?fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=730204d9290bf377707a3ab0072881f0" alt="Kb Files Pn" data-og-width="2664" width="2664" data-og-height="754" height="754" data-path="images/kb-files.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/124P12t85CIi-2hH/images/kb-files.png?w=280&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=a5b891ee317f6ba5a16ee9b27b46d0ee 280w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/kb-files.png?w=560&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=e2a9e11070102606ff5dd5097a790ac1 560w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/kb-files.png?w=840&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=b97b500d38305e802608585e0a3a5f44 840w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/kb-files.png?w=1100&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=702b08dd5bc3b019ce919d453bc7a83e 1100w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/kb-files.png?w=1650&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=1c554607a1f6dcd81024a1a8113bc030 1650w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/kb-files.png?w=2500&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=aca9743abff6c295486536ca865baa9f 2500w" />

On this page, you can see how many files and vectors are in each knowledge base. Vectors are small chunks of text from your uploaded files that have been converted into a format the AI can search and understand. They help the agent find and respond with the right information.

You can edit the name or description by clicking the **Edit** icon. You can also delete a knowledge base by clicking the **trash** icon.

<Warning>
  Deleting a knowledge base will also delete all files within the knowledge base.
</Warning>

## Upload Files to Knowledge Bases

In the “Files” section, you can upload files directly to a knowledge base. You can also click on a file name to preview its contents or click the **trash** icon next to a file to delete it.

<img src="https://mintcdn.com/agentai/124P12t85CIi-2hH/images/kb-files2.png?fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=f4f5d95282f94f0221428a3b460f765a" alt="Kb Files2 Pn" data-og-width="2668" width="2668" data-og-height="1008" height="1008" data-path="images/kb-files2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/124P12t85CIi-2hH/images/kb-files2.png?w=280&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=d29d8cb68ff5d05d4f434f083627a78c 280w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/kb-files2.png?w=560&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=48a15e0ad069899e2170192203f712b4 560w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/kb-files2.png?w=840&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=e3d81b444c35d5fb3ef58f69d968d828 840w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/kb-files2.png?w=1100&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=c72338f19f115233eb83ab38bb1c92d8 1100w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/kb-files2.png?w=1650&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=72aa218950d65035c768015c4256e0eb 1650w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/kb-files2.png?w=2500&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=4da0de5d76393258905c4bcb6a9d57d5 2500w" />

If you have any questions about setting up Knowledge Bases or managing your files in [Agent.ai](http://Agent.ai), please reach out to our [support team](https://agent.ai/feedback).


# Lead Magnet
Source: https://docs.agent.ai/builder/lead-magnet

Require opt-in before running an agent and automatically add leads to your CRM.

## Why use a Lead Magnet

Use a Lead Magnet when you want visitors who run your public agent to first opt in to communications. This ensures you can follow up and automatically add the user to your CRM (e.g., HubSpot).

Common scenarios:

* Capture newsletter/demo opt-ins before running an assistant
* Gate premium agents behind a quick consent form
* Sync new leads directly to HubSpot contacts (optionally create deals)

***

## How it works (toggle-based)

1. In Builder settings, turn on **Lead Magnet** (after connecting HubSpot).
2. Agent.ai automatically displays a consent UI (email + opt-in) before the run.
3. On accept, Agent.ai automatically creates/updates the contact in HubSpot.
4. Your agent then runs as normal.

Notes:

* No custom prompt or consent form required — it’s built-in.
* No manual contact creation step — Agent.ai handles that for you.
* You can still enrich, associate, or update properties later in your workflow if you want.

***

## Configure your Lead Magnet

1. **Prepare HubSpot**

* Connect HubSpot: [HubSpot Setup](../integrations/hubspot-v2/guides/hubspot-setup)
* Confirm write scopes for Contacts

2. **Toggle Lead Magnet on**

* Agent.ai will present the consent UI and collect email automatically

3. **Optional: create a deal or subscription**

* Create a deal associated with the contact
* Or add them to a specific list or workflow

4. **Proceed to the agent flow**

* After consent and contact sync, your agent executes its steps

***

## Best practices

* Keep the opt-in step short (email + one checkbox)
* Clearly explain value of opting in
* Set `lead_source` (e.g., "Agent Magnet") for reporting
* Respect user consent; don’t proceed without it
* Add an audit note via [Create Timeline Event](../actions/hubspot-v2-create-timeline-event)

***

## Troubleshooting

* Contact not created? Verify OAuth scopes and that Lead Magnet is enabled
* Unexpected duplicates? Contact creation is automatic; if you add manual creates, ensure you check first
* Not showing in lists? Confirm internal property names and values

***

## Related

* Start here: [Using Agent.ai with HubSpot](../builder/using-hubspot)
* Actions: [Lookup](../actions/hubspot-v2-lookup-object), [Create](../actions/hubspot-v2-create-object), [Update](../actions/hubspot-v2-update-object)
* Guides: [Webhook Triggers (HubSpot)](../integrations/hubspot-v2/guides/webhook-triggers)

***

## Visual

<img src="https://mintcdn.com/agentai/6I_mB495iSFC6FbT/images/lead-magnet-hero.svg?fit=max&auto=format&n=6I_mB495iSFC6FbT&q=85&s=3517dab5a2cc74dd0c6b22da59b881bd" alt="Lead Magnet Flow" data-og-width="920" width="920" data-og-height="240" height="240" data-path="images/lead-magnet-hero.svg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/6I_mB495iSFC6FbT/images/lead-magnet-hero.svg?w=280&fit=max&auto=format&n=6I_mB495iSFC6FbT&q=85&s=c540792eb205be3d28499bc8a74d2da5 280w, https://mintcdn.com/agentai/6I_mB495iSFC6FbT/images/lead-magnet-hero.svg?w=560&fit=max&auto=format&n=6I_mB495iSFC6FbT&q=85&s=97446eae5af18b507cc8e7d0cfe54608 560w, https://mintcdn.com/agentai/6I_mB495iSFC6FbT/images/lead-magnet-hero.svg?w=840&fit=max&auto=format&n=6I_mB495iSFC6FbT&q=85&s=aa20f5da15b550eb512fb69212d451c0 840w, https://mintcdn.com/agentai/6I_mB495iSFC6FbT/images/lead-magnet-hero.svg?w=1100&fit=max&auto=format&n=6I_mB495iSFC6FbT&q=85&s=4b3a47a5dcb067d5719e78fc0d5ab97c 1100w, https://mintcdn.com/agentai/6I_mB495iSFC6FbT/images/lead-magnet-hero.svg?w=1650&fit=max&auto=format&n=6I_mB495iSFC6FbT&q=85&s=985f732eb62e26eaf30ff9d55c6355c1 1650w, https://mintcdn.com/agentai/6I_mB495iSFC6FbT/images/lead-magnet-hero.svg?w=2500&fit=max&auto=format&n=6I_mB495iSFC6FbT&q=85&s=53e64063e8f48e9209767a05988c35c5 2500w" />


# Builder Overview
Source: https://docs.agent.ai/builder/overview



The Agent.AI Builder is a no-code tool that allows users at all technical levels to build powerful agentic AI applications in minutes.

Once you sign up for your Agent.AI account, enable your Builder account by clicking on "Agent Builder" in the menu bar. Then, head over to the [Agent Builder](https://agent.ai/builder/agents) to get started.

## Create Your First Agent

To create an agent, click on the "Create Agent" modal. You can either start building an agent from scratch or start building from one of our existing templates.

Let's start by building an agent from scratch. Don't worry, it's easier than it sounds!

## Settings

The builder has 2 sections: the core Builder canvas and settings. Most information in settings is optional, so don't if you don't know what some of those words mean.

Let's start with the settings panel. Here we define how the agent will show up when users try to use it and how it will show up in the marketplace.

<img alt="Builder Settings panel" classname="hidden dark:block" src="https://mintcdn.com/agentai/UYmyskpA4wsMD1WI/settings.png?fit=max&auto=format&n=UYmyskpA4wsMD1WI&q=85&s=a5d86a8701f7f4b2ff3527bebcf5d5a2" title={true} data-og-width="858" width="858" data-og-height="1811" height="1811" data-path="settings.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/UYmyskpA4wsMD1WI/settings.png?w=280&fit=max&auto=format&n=UYmyskpA4wsMD1WI&q=85&s=17fb33cd34b88e21590d158354ca4a91 280w, https://mintcdn.com/agentai/UYmyskpA4wsMD1WI/settings.png?w=560&fit=max&auto=format&n=UYmyskpA4wsMD1WI&q=85&s=4472d69c1d317db4e04671a7bc15193d 560w, https://mintcdn.com/agentai/UYmyskpA4wsMD1WI/settings.png?w=840&fit=max&auto=format&n=UYmyskpA4wsMD1WI&q=85&s=70d9ac45d0bd8ad2e65b546c86e88b4b 840w, https://mintcdn.com/agentai/UYmyskpA4wsMD1WI/settings.png?w=1100&fit=max&auto=format&n=UYmyskpA4wsMD1WI&q=85&s=911f8112ed78a0d721910fc578b08c69 1100w, https://mintcdn.com/agentai/UYmyskpA4wsMD1WI/settings.png?w=1650&fit=max&auto=format&n=UYmyskpA4wsMD1WI&q=85&s=0400d3f76d69d94bb14adaabc58f0314 1650w, https://mintcdn.com/agentai/UYmyskpA4wsMD1WI/settings.png?w=2500&fit=max&auto=format&n=UYmyskpA4wsMD1WI&q=85&s=39099a46005e443f3a8ecb27d27916c7 2500w" />

#### Required Information

The following information is required:

* \*\*Agent Name: \*\*Name your agent based on its function. Make this descriptive to reflect what the agent does (e.g., "Data Fetcher," "Customer Profile Enricher").
* \*\*Agent Description: \*\*Describe what your agent is built to do. This can include any specific automation or tasks it handles (e.g., "Fetches and enriches customer data from LinkedIn profiles").
* **Agent Tag(s):** Add tags that make it easier to search or categorize your agent for quick access.

#### Optional Information

The following information is not required, but will help people get a better understanding of what your agent can do and will help it stand out:

* **Icon URL:** You can add a visual representation by uploading an icon or linking to an image file that represents your agent's purpose.
* **Sharing and Visibility:**
  * Private (only me): Only your user has access to run the agent
  * Private: unlisted, where only people with the link can use the agent
  * User only: only the author can use this agent
  * Specific HubSpot Portals: Only users connected to a a HubSpot portal ID you provide can view and run this agent
  * Specific users:  define a list of user's email addresses that can use the agent
  * Public: all users can use this agent
* **Video Demo:** Provide the public video URL of a live demo of your agent in action from Youtube, Loom, Vimeo, or Wistia, or upload a local recording. You can copy this URL from the video player on any of these sites. This video will be shown to Agent.AI site explorers to help better understand the value and behavior of your agent.
* **Agent Username:** This is the unique identifier for your agent, which will be used in the agent URL.

#### Advanced Options

The following settings allow you to control behavior of your agent's that you may want to change in less situations. We recommend you only update these settings if you know their impact.

* **Automatically generate sharable URLs:** When this setting is enabled, user inputs will automatically be appended to browser urls as new parameters. Users can then share the URL with others, or reload the url themselves to automatically run your agent with those same values.
* **Cache agent LLM actions for 7 days:**  When enabled, this feature stores LLM responses for up to seven days. If the same exact prompt is used again during that period, the system will return the cached response instead of generating a new one. This feature is intended to support faster, more predictable agent runs by re-using responses between runs.
* **External Agent URL:** When enabled, this feature allows your agent profile to point to an external URL (outside of Agent.ai) where your agent will be run
* \*\*HubSpot Lead Magent: \*\*When enabled, this feature requires users of your agent to opt-in to sharing their infromation prior to running the agent. When they agree, their email address will be used to automatically create a new contact in the connected HubSpot portal. You can then use this email to update data throughout the run in HubSpot.  To use this option you must have an existing, connected HubSpot Portal.

## Trigger

Triggers determine when the Agent will be run. You can see and configure triggers at the top of the Builder canvas.

<img src="https://mintcdn.com/agentai/UYmyskpA4wsMD1WI/images/triggers_new_builder_new.png?fit=max&auto=format&n=UYmyskpA4wsMD1WI&q=85&s=fa1ff0383f2ed78d08bd04cf0f41067c" alt="Triggers New Builder New Pn" data-og-width="2406" width="2406" data-og-height="1818" height="1818" data-path="images/triggers_new_builder_new.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/UYmyskpA4wsMD1WI/images/triggers_new_builder_new.png?w=280&fit=max&auto=format&n=UYmyskpA4wsMD1WI&q=85&s=628009e89273f80d8fadb2866ddeea4f 280w, https://mintcdn.com/agentai/UYmyskpA4wsMD1WI/images/triggers_new_builder_new.png?w=560&fit=max&auto=format&n=UYmyskpA4wsMD1WI&q=85&s=303be235769bca37f84c22aa71ab491f 560w, https://mintcdn.com/agentai/UYmyskpA4wsMD1WI/images/triggers_new_builder_new.png?w=840&fit=max&auto=format&n=UYmyskpA4wsMD1WI&q=85&s=8e9366ef53bcc8099c7cad1b751c9f2e 840w, https://mintcdn.com/agentai/UYmyskpA4wsMD1WI/images/triggers_new_builder_new.png?w=1100&fit=max&auto=format&n=UYmyskpA4wsMD1WI&q=85&s=81de1c4061a27d5a02f61b5148f68f95 1100w, https://mintcdn.com/agentai/UYmyskpA4wsMD1WI/images/triggers_new_builder_new.png?w=1650&fit=max&auto=format&n=UYmyskpA4wsMD1WI&q=85&s=be9d8dac145fdaa6520f340b7b5d691e 1650w, https://mintcdn.com/agentai/UYmyskpA4wsMD1WI/images/triggers_new_builder_new.png?w=2500&fit=max&auto=format&n=UYmyskpA4wsMD1WI&q=85&s=963caf3771e6453c8608b187d9846da5 2500w" />

There are a variety of ways to trigger and agent:

#### **Manual**

Agents can always be run manually, but selecting ‘Manual Only’ ensures this agent can only be triggered directly from Agent.AI

#### **User configured schedule**

Enabling user configured schedules allows users of your agent to set up recurring runs of the agent using inputs from their previously defined inputs.

**How it works**

1. When a user runs your agent that has "User configured schedule" enabled, they will see an "Auto Schedule" button
2. Clicking "Auto Schedule" opens a scheduling dialog where:
   * The inputs from their last run will be pre-filled
   * They can choose a frequency (Daily, Weekly, Monthly, or Quarterly)
   * They can review and confirm the schedule
3. After clicking "Save Schedule", the agent will run automatically on the selected schedule

**Note**: You can see and manage all your agent schedules in your [<u>Agent Scheduled Runs</u>](https://agent.ai/user/agent-runs). You will receive email notifications with outputs of each run as they complete.

#### **Enable agent via email**

When this setting is enabled, the agent will also be accessible via email. Users can email the agent's address and receive a full response back.

<Note>
  Agents will only respond to emails sent from the same address you use to log into [Agent.ai](http://Agent.ai).
</Note>

#### **HubSpot Contact/Company Added**

Automatically trigger the agent when a new contact or company is added to HubSpot, a useful feature for CRM automation.

#### **Webhook**

By enabling a webhook, the agent can be triggered whenever an external system sends a request to the specified endpoint. This ensures your agent remains up to date and reacts instantly to new events or data.

**How to Use Webhooks**

When enabled, your agent can be triggered by sending an HTTP POST request to the webhook URL, it would look like:

```
curl -L -X POST -H 'Content-Type: application/json' \
    'https://api-lr.agent.ai/v1/agent/and2o07w2lqhwjnn/webhook/ef2681a0' \
    -d '{"user_input":"REPLACE_ME"}'
```

**Manual Testing:**

1. Copy the curl command from your agent's webhook configuration
2. Replace placeholder values with your actual data
3. Run the command in your terminal for testing
4. Your agent will execute automatically with the provided inputs

**Example: Webhook Example Agent**

See [this example agent ](https://agent.ai/agent/webhook-template)that demonstrates webhook usage. The agent delivers a summary of a YouTube video to a provided email address.

```
curl -L -X POST -H 'Content-Type: application/json' \
  'https://api-lr.agent.ai/v1/agent/2uu8sx3kiip82da4/webhook/7a1e56b0' \
  -d '{"user_input_url":"REPLACE_ME","user_email":"REPLACE_ME"}'
```

To trigger this agent via webhook: 

* Replace the first "REPLACE\_ME" with a YouTube URL 
* Replace the second "REPLACE\_ME" with your email address 
* Paste and run in your terminal (command prompt)
* You'll receive an email with the video summary shortly

## Actions

In the Actions section of the Builder, users define the steps the agent will perform. Each action is a building block in your workflow, and the order of these actions will determine how the agent operates. Below is a breakdown of the available actions and how you can use them effectively.

<img alt="Builder Triggers panel" classname="hidden dark:block" src="https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/actions_new_builder.png?fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=52b187a836a5dbcebbd8ef603e12ee1b" title={true} data-og-width="1590" width="1590" data-og-height="1522" height="1522" data-path="actions_new_builder.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/actions_new_builder.png?w=280&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=6958c24d6c4dd84f37178c79e8ed5526 280w, https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/actions_new_builder.png?w=560&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=c8d1c4a06c435e17deb67031351f9945 560w, https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/actions_new_builder.png?w=840&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=a143fe82672155c426520e67d66671aa 840w, https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/actions_new_builder.png?w=1100&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=858defd14cf477dc5a8ce5b9163c0daf 1100w, https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/actions_new_builder.png?w=1650&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=7aec6b4cbdbc3bf05d90ee264cf7bbbc 1650w, https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/actions_new_builder.png?w=2500&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=1c5d246a22a3c625ed871c978a188bfa 2500w" />

The builder provides a rich library of actions, organized into categories to help you find the right tool for the job. Here's a high-level overview of each category and what it's used for.

#### Inputs & Data Retrieval

Gather, manage, and retrieve the data your agent needs to operate. This category includes actions for prompting users for input, fetching information from websites, searching the web, and reading from your knowledge base. Use these actions to make your agents interactive, conduct research, and provide them with the data they need to perform their tasks.

#### Social Media & Online Presence

Connect to social media platforms to automate your online presence. These actions allow you to interact with platforms like X (formerly Twitter), LinkedIn, and Instagram. You can build agents to monitor social media for mentions of your brand, post updates, or gather information about users and trends.

#### Hubspot CRM & Automation

Connect directly to your HubSpot CRM to manage and automate your customer relationships. These actions allow you to create, retrieve, update, and delete objects in HubSpot, such as contacts, companies, and deals. For example, you can build an agent that automatically adds new leads to your CRM or updates a contact's information based on a user's interaction.

#### Business & Financial Data

Access valuable business and financial information to power your agents. This category includes actions for getting company details, financial statements, and stock prices. These tools are perfect for building agents that perform market research, competitive analysis, or financial monitoring.

#### Workflow & Logic

Control the flow of your agent's execution with powerful workflow actions. This category includes actions for running custom code, calling external APIs, invoking other agents, and implementing conditional logic. Use these actions to build complex, multi-step workflows, create branching logic, and integrate with almost any third-party service.

#### AI & Content Generation

Leverage the power of large language models (LLMs) to perform complex tasks. These actions allow you to generate text, analyze sentiment, summarize information, generate images, and more. This is where you can integrate models from providers like OpenAI and Anthropic to build sophisticated AI-powered agents.

#### Outputs

Deliver meaningful, formatted results that can be communicated or saved for further use. Create engaging outputs like email messages, blog posts, Google Docs, or formatted tables based on workflow data. For example, send users a custom report via email, save generated content as a document, or display a summary table directly on the interface—ensuring results are clear, actionable, and easy to understand.

<img alt="Builder Triggers panel" classname="hidden dark:block" src="https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/action_library.png?fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=b7ae5e49ae650517b0af12b30cbf7c1c" title={true} data-og-width="1704" width="1704" data-og-height="1810" height="1810" data-path="action_library.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/action_library.png?w=280&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=56ad80777b51b475958979d190487710 280w, https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/action_library.png?w=560&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=2abd573d9c88312f443b1ed79ee7d61b 560w, https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/action_library.png?w=840&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=8ff1752de13eb6e398cfef35f87c7a1c 840w, https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/action_library.png?w=1100&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=dd357511b97c3da134980181cead7395 1100w, https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/action_library.png?w=1650&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=7660a78aba04b22a3c52b87ccbe3ada9 1650w, https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/action_library.png?w=2500&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=7ef81872f4281230fb42e0ff243b9d61 2500w" />

We'll run through each available action in the Actions page.

<Info>
  Not sure where to find an action? You can search in the action library too!
</Info>

## Agent Preview Panel

The "Preview" panel is an essential tool for testing and debugging your agent as you build. It allows you to see how your agent will run, inspect its data at every step, and quickly iterate on your design.

### Running your agent

To start a preview, simply add an action that requires user input (like "Get User Input") and fill in the required fields. The agent will automatically run up to that first input step. From there, you can continue the run step-by-step.

<img src="https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/images/preview_init.png?fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=09c2143ff4e87f737dd4486622511db0" alt="Preview Init Pn" data-og-width="1322" width="1322" data-og-height="1392" height="1392" data-path="images/preview_init.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/images/preview_init.png?w=280&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=3d7dca97d8cc609255188e8a08204dac 280w, https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/images/preview_init.png?w=560&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=9168e1893ff78f455e57bf6d819935fe 560w, https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/images/preview_init.png?w=840&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=c024baf8044f85b22ae7673503c86d55 840w, https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/images/preview_init.png?w=1100&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=1cfc2b087811e54b7af6078f44b69707 1100w, https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/images/preview_init.png?w=1650&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=ae3d503e69b0baf4197ab507d129fd29 1650w, https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/images/preview_init.png?w=2500&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=8ed0289b973481291811a9f3d70a12b8 2500w" />

### Details Toggle

The "Details" toggle at the top of the panel allows you to switch between two views:

* **Simple View (Details Off):** This view shows you the inputs and outputs of your agent, just as a user would see them. It's great for testing the overall user experience.
* **Detailed View (Details On):** This view provides a step-by-step log of your agent's execution. It's an essential tool for debugging, as it allows you to see the inner workings of your agent.

<img src="https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/images/preview_details.png?fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=7269e345639bf61f10820e1cd9dc3562" alt="Preview Details Pn" data-og-width="1322" width="1322" data-og-height="1392" height="1392" data-path="images/preview_details.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/images/preview_details.png?w=280&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=8eefc3e910d05c4d1d7d00ade075f680 280w, https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/images/preview_details.png?w=560&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=cfc4057780c373bcc2679d1776f29ca5 560w, https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/images/preview_details.png?w=840&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=2b7ebd4aef2c823ac419cf9bd5b8fcf2 840w, https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/images/preview_details.png?w=1100&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=2e7792043090dbcce64849f9092ca68f 1100w, https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/images/preview_details.png?w=1650&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=3b7155d38e054cb886ae6393c5016427 1650w, https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/images/preview_details.png?w=2500&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=82d04fb7df1435a93135465561dbf60b 2500w" />

When you turn on the "Details" toggle, you'll see a log of every action your agent has performed. Each entry in the log corresponds to a step in your agent's workflow and is broken down into two main sections:

* **Log:** This section provides a summary of what happened during the step. It will show you the action that was run, whether it was successful, and how long it took.
* **Context:** This section shows you the state of all the variables in your agent *after* the step was completed. This is incredibly useful for debugging, as you can see exactly what data the agent was working with at any given point.

<img src="https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/images/Screenshot2025-08-25at7.03.10PM.png?fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=a85cc3e16f59f8bc195458b3d9bc3c9f" alt="Screenshot 2025-08-25 at 7.03.10 PM.png" data-og-width="1212" width="1212" data-og-height="1066" height="1066" data-path="images/Screenshot2025-08-25at7.03.10PM.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/images/Screenshot2025-08-25at7.03.10PM.png?w=280&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=5a12584414ccc8d851344d2ba0bba301 280w, https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/images/Screenshot2025-08-25at7.03.10PM.png?w=560&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=036ba73aaad83bf9be554a2afc3dbb8f 560w, https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/images/Screenshot2025-08-25at7.03.10PM.png?w=840&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=563d043380dfbcb279b5d509e501f482 840w, https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/images/Screenshot2025-08-25at7.03.10PM.png?w=1100&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=27414e55867408e12b18cf05b4d62b26 1100w, https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/images/Screenshot2025-08-25at7.03.10PM.png?w=1650&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=3c9ebab8cefc45ccd49ae299a3fa34f7 1650w, https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/images/Screenshot2025-08-25at7.03.10PM.png?w=2500&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=156c28584e90628826fd8d26b9802cae 2500w" />

### Restarting and rerunning steps

The Preview panel makes it easy to iterate on your agent's design without having to start from scratch every time.

* \*\*Restarting the Entire run: \*\*\
  Clicking the "Restart" button at the top of the panel will completely reset the agent's run. This is useful when you want to test your agent from the very beginning with new inputs.
* \*\*Restarting from a specific step: \*\*\
  The builder is smart enough to know when you've made a change to your agent's workflow. When you modify an action, the agent will automatically restart the run from the step you changed. This allows you to quickly test your changes without having to rerun the entire agent.

  For example, if you have a 10-step agent and you modify step 5, the agent will preserve the results of steps 1-4 and restart the run from step 5. This is a huge time-saver when you're building complex agents.

<img src="https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/images/Screenshot2025-08-25at7.05.12PM.png?fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=82f24dc744b3281e14d015d1ef5cc9c4" alt="Screenshot 2025-08-25 at 7.05.12 PM.png" data-og-width="1272" width="1272" data-og-height="162" height="162" data-path="images/Screenshot2025-08-25at7.05.12PM.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/images/Screenshot2025-08-25at7.05.12PM.png?w=280&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=e2d754b15710db0e62f90ad227c7e5a2 280w, https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/images/Screenshot2025-08-25at7.05.12PM.png?w=560&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=30968d00dd9515c450343458acc09c34 560w, https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/images/Screenshot2025-08-25at7.05.12PM.png?w=840&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=b153ef4544b325aa338a406e960d31ca 840w, https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/images/Screenshot2025-08-25at7.05.12PM.png?w=1100&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=ff46d14195764868b2319b8b30195bb4 1100w, https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/images/Screenshot2025-08-25at7.05.12PM.png?w=1650&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=b09516e16a6c76b0f2d613f2f8abef32 1650w, https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/images/Screenshot2025-08-25at7.05.12PM.png?w=2500&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=35762105fdc97c334502a05bea2e05aa 2500w" />


# Policy for Public Agents
Source: https://docs.agent.ai/builder/public-agent-policy

This is the Agent.ai policy for publishing public agents. Below you’ll find the criteria your agent needs to meet to be published. Published agents can show up in search so other users can find and use them. This document should be viewed alongside our Terms of Service and Privacy Policy.

*Last updated May 14, 2025. Subject to change.*

## Public Agents need to meet our standards for Usability, Remarkability, and Safety (URS).

### **Usability** means that the agent:

* **Runs successfully**: executes its assigned tasks as described without bugs or crashes.
* **Has a clear and unique name**: Is easily found by users searching for something that does what it does. Avoids using trademarked terms without permission
* **Has a helpful description:** Explains expected user inputs, outputs, agent behavior and purpose
  * Ideally includes a short demo video.
* **Doesn’t break easily**:
  * Handles poor/incomplete inputs without failing
  * Handles errors gracefully via dependent APIs
  * Avoids brittle logic, (e.g. looks for LinkedIn handle, breaks when given a full URL.)
* **Is useful and formatted well**:
  * Provides output that is readable, helpful and aligned with the task (text, HTML, JSON, etc.)

### **Remarkability** means that the agent:

* **Is unique**: Isn’t a copy of another agent or serves a duplicate function of another agent already listed.
* **Has a purpose**: Solves a clear user problem or provides unique utility
* **Demonstrates value:**
  * Goes beyond a basic LLM call through thoughtful prompt design.
  * Adds novel methods, integrations, or problem-solving techniques not yet found on [Agent.ai](http://Agent.ai).
  * Incorporates your own perspective, unique insights or subject matter expertise to delight users.

### **Safety** means that the agent:

* **Avoids inappropriate language or content:** No prohibited content or behavior.
* **Is not spammy:** Doesn’t send emails or other messages without explicit user permission.
* **Asks for user consent:** Asks for explicit permission before collecting email addresses, user\_context, personally identifying information (PII) or before sending any data to a third party.
* **Does not aim to deceive:** Does not contain aggressive or deceptive calls to action or claims.
* **Respects user security:** Does not collect passwords, payment information, government IDs or other sensitive information.
* **Displays proper disclaimers if they’re related to regulated services**: Any agents that in fields like finance, legal, medicine, or other regulated industries must display a disclaimer.
* **Self-identifies honestly**: Doesn’t pretend to be human or hide its nature as an AI.

## Agents may be delisted if they:

* No longer meet the above criteria.
* Get too many bad reviews, recurring issues, or poor user feedback.
* Are changed in a way that violates our Terms of Service.


# Using Secrets in Agent.ai
Source: https://docs.agent.ai/builder/secrets



Secrets let you securely store sensitive data like API keys or tokens and use them in your agents without hardcoding values directly into your workflow. This is especially useful when using REST actions to call external services.

By using secrets, you can keep credentials safe, reduce duplication across agents, and simplify maintenance if values ever change.

## When to Use Secrets

Use a secret whenever you're working with:

* API keys (e.g. OpenWeather, Slack, Notion)
* Authorization tokens
* Other sensitive config values you don’t want exposed in your agent steps

<img src="https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/secrets.png?fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=91ec146116757d831aed47442d2f5a62" alt="Secrets Pn" data-og-width="2734" width="2734" data-og-height="794" height="794" data-path="images/secrets.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/secrets.png?w=280&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=e8219845fce5443fd4e30766fed32534 280w, https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/secrets.png?w=560&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=0c0dd8cc637413305f82b13b1dab345d 560w, https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/secrets.png?w=840&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=f16011724a7c46f94db3726016115b05 840w, https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/secrets.png?w=1100&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=eca83c1dbf4b6a19907018630d18bcb3 1100w, https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/secrets.png?w=1650&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=8b588f2298369a0aef153c78f5bb27d3 1650w, https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/secrets.png?w=2500&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=b8b0779f4f161c4dd45ef65f73b71039 2500w" />

## How to Add a Secret

To add a new secret:

1. Go to the [Secrets tab](https://agent.ai/builder/secrets) from the profile navigation menu.
2. Click **Add secret**
3. Enter a **name** (e.g. weather\_api\_key) and the **secret value**
4. Click **Save**

Once saved, your secret will appear in the list as a masked value. You’ll reference it by name in your agents, not by its raw value.

## How to Use a Secret in an Agent

Anywhere you'd normally paste an API key or token in a REST call or prompt, use the secret reference format:

```
{{secrets.weather_api_key}}
```

For example, in your REST action’s header:

```json  theme={null}
{
  "Authorization": "Bearer {{secrets.weather_api_key}}"
}
```

Or directly in your request URL or body:

```json  theme={null}
{
  "url": "https://api.example.com/data?key={{secrets.weather_api_key}}"
}
```

## Best Practices

* Use clear, descriptive names (e.g. `notion_token`, `slack_webhook`)
* Avoid including the actual key in prompt text or test runs
* Rotate or update secrets as needed in the Secrets tab without having to update your agents

Questions about configuring secrets and handling sensitive credentials in Agent.ai? Reach out to our [support team](https://agent.ai/feedback).


# Managing Serverless Functions
Source: https://docs.agent.ai/builder/serverless-functions



Builders can use the **Call Serverless Function** action to execute custom code as part of advanced agent workflows. Once a serverless function has been created, it will appear on the **Serverless Functions** page, accessible from the profile navigation menu.

<img src="https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/serverless-functions.png?fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=537084f4e4a4ba0a6df7da783d8335bb" alt="Serverless Functions Pn" data-og-width="2710" width="2710" data-og-height="684" height="684" data-path="images/serverless-functions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/serverless-functions.png?w=280&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=4d1f4756baf4c4a78599622dbc87f20c 280w, https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/serverless-functions.png?w=560&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=1fdc591cf7ea5fcc14b15b6697b9529c 560w, https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/serverless-functions.png?w=840&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=952c6dcccebf5807ee54174af3b507c7 840w, https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/serverless-functions.png?w=1100&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=68b9dbdf853025008a5bfd8a820608d9 1100w, https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/serverless-functions.png?w=1650&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=93567539754e05a88e4cbaee76f02dd5 1650w, https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/serverless-functions.png?w=2500&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=99ef8d4203ca7f76ae730153d3d52c9e 2500w" />

From this page, you can view key details about each function and take the following actions:

* **View the agent** – Click the Agent ID to open the associated agent in the builder tool
* **Check logs** – Click the log icon to see runtime logs for that function
* **Delete** – Click the trash icon to permanently remove the function

<Warning>
  Deleting a serverless function from this page will also remove the action from the agent’s workflow.
</Warning>

If you have any questions about serverless functions, you can reach out to our [support team](https://agent.ai/feedback).


# Using Snippets in Agent.ai
Source: https://docs.agent.ai/builder/snippets



Use [**Snippets**](https://agent.ai/builder/snippets) to define reusable values that are available to all agents across the platform. This is useful for things like shared sign-offs, disclaimers, or other repeated text.

To reference a snippet in your agent’s prompt or output, use:\
`{{snippets.var_name}}`

For example, a snippet with the name signature could be used as `{{snippets.signature}}`.

<Note>
  Snippets are not encrypted and should not be used to store API keys, passwords, or other sensitive information. Use the [**Secrets**](https://agent.ai/builder/secrets) feature for storing production credentials or private data securely.
</Note>

You can add, edit, or delete snippets from this page.

<img src="https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/snippets.png?fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=9c97fdb0dcc715904a9ecfb05f0ece9c" alt="Snippets Pn" data-og-width="2708" width="2708" data-og-height="700" height="700" data-path="images/snippets.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/snippets.png?w=280&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=a267ca672ee2e1fb33be8dc209d85130 280w, https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/snippets.png?w=560&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=0c19929fd58e3edde741cf34aec062c7 560w, https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/snippets.png?w=840&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=729d1d23c7a419ad13cba1b52320eb18 840w, https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/snippets.png?w=1100&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=b73f5b54fc1866149ddc1061455cf7d8 1100w, https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/snippets.png?w=1650&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=a1d5c8ac5474cdd2d10f1ba5e6195044 1650w, https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/snippets.png?w=2500&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=43ce462d5e0eb71ea6993f1f7ac8d18f 2500w" />

Reach out to our [support team](https://agent.ai/feedback) if you need help with snippets.


# Template Variables
Source: https://docs.agent.ai/builder/template-variables

Use the variable syntax and curly braces button to insert data from previous actions into your workflow

Use the \{\{variable}} syntax and `{}` button to insert data from previous actions into your workflow.

**Common uses:**

* Insert search results into AI prompts
* Use deal amount in update actions
* Reference contact email in conditions
* Access nested properties like `contact.properties.firstname`
* Build text with multiple variables

***

## What This Does (The Simple Version)

Think of variables like passing notes between actions. One action finds data (like a contact record) and saves it with a name. Later actions can reference that name to use the data.

**Real-world example:**
A search action finds deals and saves them as `target_deals`. A loop action references `target_deals` to process each one. Inside the loop, you reference `current_deal.properties.amount` to get each deal's amount.

***

## The `{}` Button

**The easiest way to insert variables:**

1. **Hover** over any input field
2. **`{}` button appears** on the right
3. **Click it** to open variable picker
4. **Select the variable** you want
5. **Variable is inserted** in correct syntax

**Where you'll see it:**

* All action input fields
* Condition fields
* Update value fields
* Prompt fields
* Email body fields

***

## Variable Syntax

### Basic Variable

**Format:** \{\{variable\_name}}

**Example:**

```
\{\{contact\_email\}}
\{\{deal\_amount\}}
\{\{search\_results\}}
```

### Accessing Properties

**Format:** \{\{variable.properties.property\_name}}

**Example:**

```
\{\{contact\_data.properties.email\}}
\{\{deal\_record.properties.amount\}}
\{\{company\_info.properties.domain\}}
```

### Accessing Nested Data

**Format:** \{\{variable.path.to.data}}

**Example:**

```
\{\{contact\_data.properties.firstname\}}
\{\{deal\_record.associations.contacts\}}
\{\{current\_item.id\}}
```

### Accessing Array Items

**Format:** \{\{variable\[0]}} (first item)

**Example:**

```
\{\{search\_results[0]\}}
\{\{contact\_data.associations.companies[0].id\}}
\{\{deals[0].properties.dealname\}}
```

***

## Common Patterns

### From Search Action

**After Search HubSpot (V2):**

**Output variable:** `target_deals`

**Access in later actions:**

* Whole list: \{\{target\_deals}}
* First deal: \{\{target\_deals\[0]}}
* First deal's name: \{\{target\_deals\[0].properties.dealname}}

### From Lookup Action

**After Lookup HubSpot Object (V2):**

**Output variable:** `contact_record`

**Access properties:**

* Email: \{\{contact\_record.properties.email}}
* First name: \{\{contact\_record.properties.firstname}}
* Company: \{\{contact\_record.properties.company}}
* Object ID: \{\{contact\_record.id}} or \{\{contact\_record.hs\_object\_id}}

### From Loop

**Inside For Loop:**

**Current item variable:** `current_deal`

**Access current item:**

* Whole object: \{\{current\_deal}}
* Deal name: \{\{current\_deal.properties.dealname}}
* Deal amount: \{\{current\_deal.properties.amount}}
* Object ID: \{\{current\_deal.hs\_object\_id}}

### From Webhook

**After webhook trigger:**

**Webhook variables available immediately:**

* \{\{contact\_id}}
* \{\{deal\_name}}
* \{\{\_hubspot\_portal}}
* Whatever you included in HubSpot webhook payload

### From Set Variable

**After Set Variable action:**

**Variable name:** `total_count`

**Access anywhere after:**

* \{\{total\_count}}

**Can use in:**

* Conditions: \{\{total\_count}} > 10
* Updates: Set property to \{\{total\_count}}
* Math: \{\{total\_count}} + 1

***

## Using Variables in Different Actions

### In Update Actions

**Update HubSpot Object (V2):**

1. Select property to update
2. In value field, hover and click `{}`
3. Select variable
4. Or mix text + variables: "Total: \$\{\{deal\_amount}}"

**Example:**

* Update `hs_lead_status` with: \{\{enrichment\_result}}
* Update `notes` with: "Score: \{\{lead\_score}} - Company: \{\{company\_name}}"

### In Conditions

**If Condition:**

1. Type condition naturally
2. Click `{}` to insert variables
3. AI evaluates the condition

**Example:**

```
\{\{deal\_record.properties.amount\}} > 50000
\{\{contact\_data.properties.email\}} is not empty
\{\{lifecycle\_stage\}} equals "salesqualifiedlead"
```

### In AI Prompts

**Invoke LLM:**

1. Type prompt text
2. Click `{}` to insert variables
3. AI receives the data

**Example:**

```
Analyze this deal: \{\{deal\_record\}}

Based on this timeline: \{\{deal\_timeline\}}

Provide insights about \{\{contact\_data.properties.firstname\}}'s engagement.
```

### In Loops

**For Loop:**

1. "Loop through" field: Click `{}` → select list variable
2. "Current item" field: Type name like `current_contact`

**Inside loop, access:**

* \{\{current\_contact.properties.email}}
* \{\{current\_contact.properties.firstname}}

### In Search Filters

**Search HubSpot (V2):**

1. Add filter
2. In value field: Click `{}`
3. Insert variable for dynamic search

**Example:**

* Find deals where `amount` Greater Than \{\{minimum\_threshold}}
* Find contacts where `company` Equals \{\{target\_company}}

***

## Real Examples

### Deal Analysis with Variables

**Step 1: Lookup Deal**

* Output Variable: `deal_data`

**Step 2: Get Timeline**

* Object ID: \{\{deal\_data.id}}
* Output Variable: `deal_timeline`

**Step 3: AI Analysis**

* Prompt: "Analyze deal \{\{deal\_data.properties.dealname}} with timeline \{\{deal\_timeline}}"
* Output Variable: `insights`

**Step 4: Update Deal**

* Update `deal_health_score` with: \{\{insights.health\_score}}

### Contact Enrichment with Variables

**Step 1: Webhook receives**

* Variables: `contact_id`, `contact_email`, `contact_company`

**Step 2: Lookup Contact**

* Object ID: `\{\{contact\_id\}\}`
* Output Variable: `contact_data`

**Step 3: Web Search**

* Query: "\{\{contact\_data.properties.company}} \{\{contact\_data.properties.jobtitle}}"
* Output Variable: `web_results`

**Step 4: AI Enrichment**

* Prompt: "Enrich \{\{contact\_data.properties.firstname}} from \{\{web\_results}}"
* Output Variable: `enrichment`

**Step 5: Update Contact**

* Update `hs_lead_status` with: `\{\{enrichment.lead\_category\}\}`

### Loop with Counter

**Step 1: Set Variable**

* Variable Name: `high_value_count`
* Value: `0`

**Step 2: For Loop**

* Loop through: \{\{all\_deals}}
* Current item: `current_deal`

**Step 3: If Condition (inside loop)**

* Condition: \{\{current\_deal.properties.amount}} > 100000

**Step 4: Set Variable (inside if)**

* Variable Name: `high_value_count`
* Value: \{\{high\_value\_count}} + 1

**Step 5: End Condition**

**Step 6: End Loop**

**After loop:** Use `\{\{high\_value\_count\}\}`

***

## Accessing Associations

**After Lookup with Associations:**

**Output variable:** `deal_data` (with contacts and companies retrieved)

**Access associated contact ID:**

```
\{\{deal\_data.associations.contacts[0].id\}\}
```

**Access associated company ID:**

```
\{\{deal\_data.associations.companies[0].id\}\}
```

**Use in another Lookup:**

* Object Type: Contacts
* Object ID: `\{\{deal\_data.associations.contacts[0].id\}\}`

***

## Troubleshooting

### Variable Not Found

**Can't select variable in `{}` picker**

**Possible causes:**

1. Variable not created yet (action hasn't run)
2. Variable only exists inside loop/if block
3. Action that creates it failed

**How to fix:**

1. Check action order - variable must be created before use
2. Create variable outside loop if needed after loop
3. Check execution log - did creating action succeed?

### Empty Value

**Variable exists but has no value**

**Possible causes:**

1. Previous action returned empty result
2. Property doesn't exist on object
3. Search/lookup found nothing

**How to fix:**

1. Check execution log - what did previous action return?
2. Verify property name is correct
3. Add If Condition to check if variable is empty first

### Wrong Syntax

**Variable doesn't insert correctly**

**Common mistakes:**

* ❌ `{variable}` (single braces)
* ❌ `\{\{variable.property\_name\}\}` (should be `properties.property_name`)
* ❌ `\{\{variable.0\}\}` (should be `variable[0]`)

**Correct:**

* ✅ \{\{variable}}
* ✅ \{\{variable.properties.property\_name}}
* ✅ \{\{variable\[0]}}

### Can't Access Nested Property

**Error accessing `contact.properties.email`**

**Possible causes:**

1. Using `.email` instead of `.properties.email`
2. Property doesn't exist on this object type
3. Property name wrong

**How to fix:**

1. HubSpot properties are always under `.properties.`
2. Check property exists: Look at object in execution log
3. Use exact internal property name (lowercase, no spaces)

***

## Tips & Best Practices

**✅ Do:**

* Use `{}` button instead of typing manually
* Use descriptive variable names (`contact_data` not `c`)
* Check execution log to see variable values
* Test with If Condition to check if variable exists
* Use variables to make workflows dynamic
* Access properties through `.properties.` for HubSpot objects

**❌ Don't:**

* Type `{{}}` manually (typo-prone)
* Assume variables always have values
* Use variables before they're created
* Reference loop variables outside the loop
* Forget `.properties.` when accessing HubSpot properties

**Common HubSpot property paths:**

* Contact email: `.properties.email`
* Contact name: `.properties.firstname` and `.properties.lastname`
* Deal amount: `.properties.amount`
* Deal stage: `.properties.dealstage`
* Company domain: `.properties.domain`
* Object ID: `.id` or `.hs_object_id`

***

## Related Actions

**Foundation:**

* [Variable System](../builder/template-variables) - How variables work
* [Action Execution](../builder/overview) - Variable scope and lifecycle

**Actions that create variables:**

* [Search HubSpot (V2)](./hubspot-v2-search-objects) - Creates list of results
* [Lookup HubSpot Object (V2)](./hubspot-v2-lookup-object) - Creates object variable
* [Set Variable](../actions/set-variable) - Creates custom variables
* [For Loop](./for_loop) - Creates current item variable

**Actions that use variables:**

* [Update HubSpot Object (V2)](./hubspot-v2-update-object) - Insert in update values
* [If Condition](./if_else) - Use in conditions
* [Invoke LLM](./use_genai) - Insert in prompts

***

**Last Updated:** 2025-10-01


# Using Agent.ai with HubSpot
Source: https://docs.agent.ai/builder/using-hubspot

Start here to connect HubSpot, learn core patterns, and jump to actions, guides, and recipes.

The HubSpot integration connects Agent.ai directly to your CRM, enabling AI agents to read, analyze, and update your contacts, companies, deals, and custom objects in real time. Whether you're enriching lead data, automating deal updates, or building customer onboarding flows, this integration gives your agents native access to HubSpot's full data model.

**How it works**: Your agents can search for records, pull complete histories (including timeline events and engagements), process data with AI, then write back updates or create new records—all without leaving your workflow. Combine HubSpot actions with loops, conditionals, and LLM calls to build sophisticated automations that would normally require custom code or third-party tools.

### Why use HubSpot with Agent.ai

Your CRM is where revenue conversations live. Agent.ai turns that data into action:

* **Move deals forward, faster**: Pull a deal's full history (emails, meetings, notes), have AI assess momentum and risk, then update health fields or create next steps automatically.
* **Capture and convert more leads**: With features like Lead Magnet, visitors opt in before using your agent, and new contacts are synced to HubSpot automatically (no manual wiring).
* **Give ops superpowers**: Search, loop, and update at scale. Fix data hygiene, normalize stages, or tag segments across hundreds of records in minutes.
* **Create memorable experiences**: Personalize outreach, onboard customers with timely nudges, and keep teams aligned with concise AI summaries.

The result: less swivel-chair work, more time closing deals, and a CRM that stays up to date on its own.

***

## Quick start

This 3‑minute setup connects your CRM and gets you running your first Agent.ai flow.

| 1. Connect HubSpot                                                                                                                                                                                                        | 2. Run your first flow                                                                                                                                                                                                                                        | 3. Use a recipe                                                                                                                                                                                                                         |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Connect your portal and verify permissions so Agent.ai can read/write CRM data.<br />[HubSpot Setup](../integrations/hubspot-v2/guides/hubspot-setup) · [OAuth scopes](../integrations/hubspot-v2/reference/oauth-scopes) | Search deals → For Loop → Update stage to see end‑to‑end value fast.<br />Tip: use the `{}` button to insert variables.<br />[Search](../actions/hubspot-v2-search-objects) · [For Loop](../actions/for_loop) · [Update](../actions/hubspot-v2-update-object) | Start from a proven workflow, then customize for your team.<br />[Deal Analysis](../recipes/hubspot-deal-analysis) · [Onboarding](../recipes/hubspot-customer-onboarding) · [Contact Enrichment](../recipes/hubspot-contact-enrichment) |

***

## HubSpot actions (V2)

Use this as your action index—jump straight to the tool you need while building.

* [Search Objects](../actions/hubspot-v2-search-objects)
* [Lookup Object](../actions/hubspot-v2-lookup-object)
* [Create Object](../actions/hubspot-v2-create-object)
* [Update Object](../actions/hubspot-v2-update-object)
* [Get Timeline Events](../actions/hubspot-v2-get-timeline-events)
* [Create Timeline Event](../actions/hubspot-v2-create-timeline-event)
* [Get Engagements](../actions/hubspot-v2-get-engagements)
* [Create Engagement](../actions/hubspot-v2-create-engagement)

Related general actions:

* [Invoke LLM](../actions/use_genai)
* [For Loop](../actions/for_loop)
* [If Condition](../actions/if_else)
* [Set Variable](../actions/set-variable)

***

## HubSpot guides and references

Bookmark these essentials for setup, debugging, and deeper understanding.

* [Setup](../integrations/hubspot-v2/guides/hubspot-setup)
* [Triggers](../integrations/hubspot-v2/guides/webhook-triggers)
* [Variable System](../integrations/hubspot-v2/foundation/02-variable-system)
* [Troubleshooting](../integrations/hubspot-v2/guides/troubleshooting)
* [Error Messages](../integrations/hubspot-v2/reference/error-messages)

***

## Patterns you’ll use

Use these as blueprints—copy the shape, then swap in your objects and fields.

### Deal health analysis with AI

1. Lookup deal → 2. Get Timeline Events → 3. Invoke LLM (analyze) → 4. Update deal

### Engagement summary for contacts

1. Get Engagements → 2. Invoke LLM (summarize) → 3. Send notification or update property

### Bulk updates from searches

1. Search (e.g., deals in stage) → 2. For Loop → 3. Update each record

***

***

## Troubleshooting

Running into bumps? Start here before you dig into logs or support.

* Check OAuth scopes and reconnect if missing permissions
* Verify property internal names and value formats
* Use smaller limits while testing (10–20)
* Inspect execution logs to see data returned

***

## What to build next

A few great next steps to go from first success to repeatable impact.

* Explore recipes: [Deal Analysis](../recipes/hubspot-deal-analysis), [Customer Onboarding](../recipes/hubspot-customer-onboarding), [Contact Enrichment](../recipes/hubspot-contact-enrichment)
* Add a [Lead Magnet](./lead-magnet) to capture opt-ins and sync to HubSpot


# Explore and Clone Existing Agent Flows
Source: https://docs.agent.ai/clone-agents

When builders allow others to view and clone their agents, it makes it easier for the community to explore how things work and build on top of them.

The "Clone Agent" feature makes it easy to understand and even build upon the work of other [Agent.ai](http://Agent.ai) builders. From the "View Agent Flow" screen, you can quickly clone any agent that’s been made visible to the community—including all its actions, prompts, and configurations. This essentially "open sources" agents within [Agent.ai](http://Agent.ai), so you can not only see how others have built their agents, but also extend and customize them to fit your own needs.

Note: Outside of starter agents, only agents that have **Allow other builders to view actions and details** enabled can be cloned.

## Enable Visibility for Your Agent

<img src="https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/allow_builders_to_view_actions_new.png?fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=4c72f608218b9c0dbd0b58d8fd45ca1f" alt="Enable Agent Visibility Pn" data-og-width="2308" width="2308" data-og-height="666" height="666" data-path="allow_builders_to_view_actions_new.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/allow_builders_to_view_actions_new.png?w=280&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=619dfbb100153f2049c2682e0966958a 280w, https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/allow_builders_to_view_actions_new.png?w=560&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=3774175017af6276ef3b3f2caca737aa 560w, https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/allow_builders_to_view_actions_new.png?w=840&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=2426f33f019f16769032f0db46a99c5d 840w, https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/allow_builders_to_view_actions_new.png?w=1100&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=e57968d2860895621dfea918b0c0f684 1100w, https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/allow_builders_to_view_actions_new.png?w=1650&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=41d0442c90990d9f188fc412b13590aa 1650w, https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/allow_builders_to_view_actions_new.png?w=2500&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=1496cf832a102805e9286b439736080b 2500w" />

If you want other builders to be able to view and clone your agent:

1. Go to the agent's Settings page.
2. Under the "Sharing & visibility", check the box that says "Allow other builders to view this agent's actions and details".
3. Click the **Publish changes** button to save your change.

## View an Agent's Actions

<img src="https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/view-agent-actions.png?fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=e81feae2ed1c848eecd4220a038b43ae" alt="View Agent Actions Pn" data-og-width="2588" width="2588" data-og-height="694" height="694" data-path="images/view-agent-actions.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/view-agent-actions.png?w=280&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=69daad8a3d81a2587b1086990ad6268f 280w, https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/view-agent-actions.png?w=560&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=4bd908a8f5aea888612d95c91bc395c5 560w, https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/view-agent-actions.png?w=840&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=4bcfa70841bec5cbc76f0e8a6472383d 840w, https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/view-agent-actions.png?w=1100&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=37f5e90cde9cc894a9d3ce15932e0ad5 1100w, https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/view-agent-actions.png?w=1650&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=34d40d879a2422401f690e664883ce92 1650w, https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/view-agent-actions.png?w=2500&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=3f77c1db1231a85369645a5e70fbb676 2500w" />

To see how another builder's agent works (if it's been made visible), go to the agent run page and click **View Agent Flow** to explore the full flow.

## Clone an Agent

<img src="https://mintcdn.com/agentai/124P12t85CIi-2hH/images/clone-agent.png?fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=d2f692144339f97df7b683ade8c2339f" alt="Clone Agent Pn" data-og-width="2744" width="2744" data-og-height="998" height="998" data-path="images/clone-agent.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/124P12t85CIi-2hH/images/clone-agent.png?w=280&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=cc726ba510d7a4d285bfd33162c11e9a 280w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/clone-agent.png?w=560&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=f0c0d25a8c956dc1f153f16525427951 560w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/clone-agent.png?w=840&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=192aaa09144a85b50d3605353f378095 840w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/clone-agent.png?w=1100&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=bfab7a5fb8c0242a631cdca61a5af4a5 1100w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/clone-agent.png?w=1650&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=a921a81fdec799f373589a04bfc6a6da 1650w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/clone-agent.png?w=2500&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=34f712fa742b6bc992dd36f2a8e0c0de 2500w" />

Once you're viewing an agent's flow, click **Clone Agent** to copy it to your builder account and open it in the editor.

While on the "View Agent Flow" page, you can also explore all the agent's actions in detail. Click on any action to expand it and view prompts or other configuration details.

You can try it yourself by cloning this [test agent](https://agent.ai/agent/test-webpage-summarizer).

## Clone Your Own Agent

In the Builder Tool, you can also clone your own agent to make changes and test things without messing with your existing, working agent. You can do this by opening the agent editor, clicking the **three dots** next to your agent's Publish Changes button and selecting **Clone**.

<img src="https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/images/clone_agent_from_top_bar.png?fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=1ea50ae568148ee36f8501dd49e83dcd" alt="Clone Agent From Top Bar Pn" data-og-width="2412" width="2412" data-og-height="366" height="366" data-path="images/clone_agent_from_top_bar.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/images/clone_agent_from_top_bar.png?w=280&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=2a9fd8b3e0f7e080efa2cea23d2e14cb 280w, https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/images/clone_agent_from_top_bar.png?w=560&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=f49811dce30013ea49c8a60a8a7ee6b6 560w, https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/images/clone_agent_from_top_bar.png?w=840&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=69c2dfe04b3445e499053b08fd6bc442 840w, https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/images/clone_agent_from_top_bar.png?w=1100&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=b88d47350c45deefe16d244ee74859b0 1100w, https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/images/clone_agent_from_top_bar.png?w=1650&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=4633ee2726389137ddab770afd8bbcad 1650w, https://mintcdn.com/agentai/_VdnuioxFuZgtZH4/images/clone_agent_from_top_bar.png?w=2500&fit=max&auto=format&n=_VdnuioxFuZgtZH4&q=85&s=bdea22fc5db6f2b65286e096898996da 2500w" />

## Need Help?

If you have any questions about cloning agents or making your own agents visible to the community, please reach out to our [support team](https://agent.ai/feedback).


# Best Practices
Source: https://docs.agent.ai/knowledge-agents/best-practices

Advanced techniques and strategies for building exceptional knowledge agents

## Overview

This guide covers advanced best practices for creating knowledge agents that are powerful, reliable, and delightful to use. These techniques come from real-world usage and help you avoid common pitfalls.

## Prompt Engineering Best Practices

### Write for AI, Not Humans

System instructions should be explicit and structured, not conversational.

**Don't:**

```
You're really good at helping people and should try your best
to be helpful and nice when they ask you things.
```

**Do:**

```
You are a research assistant. When users ask questions:
1. Search your knowledge base first
2. If information isn't found, use the Web Research tool
3. Cite sources in your responses
4. Ask clarifying questions for ambiguous requests
```

**Why:** AI models follow explicit instructions better than vague guidance.

### Be Specific About Tool Usage

Tell the AI exactly when and how to use each tool.

**Vague (Bad):**

```
You have access to several tools to help users.
```

**Specific (Good):**

```
Tools available:
- "Company Research" workflow: Use when users ask about specific companies
  Input: Company name
  Output: Company data, funding, employee count

- "LinkedIn Enrichment" workflow: Use after Company Research to get people
  Input: Company name from previous research
  Output: Key decision-makers and their profiles

- HubSpot integration: Use to save contacts
  Input: Person name, email, company
  Action: Creates contact in CRM

Workflow order: Research → Enrich → Save to CRM
Always get user approval before saving to HubSpot.
```

**Why:** Specificity reduces guesswork and increases reliability.

### Use Examples in System Instructions

Show the agent what good looks like.

**Without Examples:**

```
Present research findings clearly.
```

**With Examples:**

```
Present research findings in this format:

## [Company Name]
- Industry: [industry]
- Size: [employee count]
- Funding: [total raised]

**Key People:**
- [Name] - [Title]
- [Name] - [Title]

**Recent News:**
- [News item 1]
- [News item 2]

**Competitive Positioning:**
[Analysis paragraph]

Sources: [List sources used]
```

**Why:** Examples create consistency and quality.

### Define Boundaries Clearly

Tell the agent what NOT to do is as important as what to do.

**Good boundaries:**

```
Do NOT:
- Make up information if you don't know something
- Claim certainty when data is uncertain
- Send emails without showing user the draft first
- Create CRM records without confirming details
- Provide financial or legal advice

If asked to do something outside your capabilities:
"I'm specialized in [your domain]. For [their request],
I recommend [alternative or human handoff]."
```

**Why:** Prevents the agent from hallucinating or overstepping.

### Iterative Prompting Strategy

Build your system instructions incrementally:

**Day 1: Basic role**

```
You are a marketing assistant that helps create campaigns.
```

**Day 2: Add workflow**

```
You are a marketing assistant. When users want campaigns:
1. Ask about goals and audience
2. Use "Competitor Research" workflow
3. Present findings and recommendations
```

**Day 3: Add output formatting**

```
[Previous instructions]

Format campaign plans like this:
**Objective:** [goal]
**Audience:** [target]
**Channels:** [list]
**Timeline:** [schedule]
**Budget:** [estimate]
```

**Day 4: Add error handling**

```
[Previous instructions]

If Competitor Research fails:
- Explain the error to the user
- Offer to proceed without competitor data
- Or suggest trying again later
```

**Why:** Gradual refinement based on real usage beats trying to write perfect prompts upfront.

## Knowledge Base Optimization

### Chunk Your Knowledge Strategically

**Poor knowledge structure:**

* One massive 100-page PDF with everything mixed together
* Lots of irrelevant content (legal boilerplate, footers, headers)

**Good knowledge structure:**

* Separate documents by topic: "Product Features.pdf", "Pricing.pdf", "API Docs.pdf"
* Remove boilerplate and navigation text
* Use clear headings and sections
* Each document focused on one topic area

**Why:** Better chunks = better retrieval = more accurate responses.

### Use Markdown Formatting in Knowledge

When creating knowledge documents, use structure:

**Poorly formatted:**

```
Our product has three features first is automation which does
X and Y second is reporting that shows Z third is integrations
that connect to A B and C.
```

**Well formatted:**

```
# Product Features

## 1. Automation
- Capability X: [description]
- Capability Y: [description]

## 2. Reporting
- Shows metric Z
- Exportable to CSV, PDF

## 3. Integrations
- Connect to: A, B, C
- Two-way sync available
```

**Why:** Structured content is easier for the AI to parse and retrieve accurately.

### Name Files Descriptively

**Bad file names:**

* "Document1.pdf"
* "Final\_v2\_FINAL.docx"
* "Untitled.pdf"

**Good file names:**

* "\[POLICY] Refund and Return Policy.pdf"
* "\[GUIDE] API Authentication Guide.pdf"
* "\[FAQ] Common Customer Questions.pdf"

**Why:** File names provide context for retrieval.

### Keep Knowledge Current

**Weekly:**

* Check if any major facts changed
* Update URLs that may have refreshed content

**Monthly:**

* Review all knowledge for accuracy
* Remove outdated information
* Add new relevant content

**Quarterly:**

* Audit entire knowledge base
* Reorganize if needed
* Test retrieval quality

**Why:** Stale knowledge leads to incorrect responses.

### Quality Metrics for Knowledge

**Good knowledge base:**

* 80%+ of user questions can be answered from knowledge
* Responses cite relevant, accurate sources
* Knowledge is current (updated within 3 months)
* Focused on your domain (minimal irrelevant content)

**Poor knowledge base:**

* Agent frequently says "I don't have information about that"
* Cites wrong or irrelevant sources
* Information is outdated
* Too much noise (agent retrieves irrelevant chunks)

## Tool Orchestration Patterns

### Start with 1-2 Tools, Scale Gradually

**Phase 1: Single tool**

```
Enable: Web Research workflow
Test: "Research [topic]"
Perfect: Get this working reliably
```

**Phase 2: Add complementary tool**

```
Enable: Data Analysis workflow
Test: "Research [topic] and analyze trends"
Perfect: Ensure tools work together
```

**Phase 3: Add output tool**

```
Enable: Google Docs integration
Test: "Research [topic], analyze, and save report"
Perfect: Complete workflow end-to-end
```

**Why:** Testing sequentially isolates issues. Adding 10 tools at once makes debugging impossible.

### Design Tool Chains

Think about natural sequences:

**Research Chain:**

```
Input → Search → Enrich → Analyze → Output
```

**System instructions:**

```
For research requests:
1. Use Web Search to find companies
2. Use LinkedIn Enrichment to get key people
3. Use Company Analysis to assess fit
4. Use Google Docs to save findings
```

**Sales Chain:**

```
Identify → Research → Qualify → Enrich → Save
```

**System instructions:**

```
For lead generation:
1. Use Company Search to find prospects
2. Use Web Research to check recent news
3. Use Qualification Checklist to assess fit
4. Use LinkedIn Enrichment to find contacts
5. Use HubSpot integration to create deals
```

**Why:** Designed chains create reliable, repeatable workflows.

### Add Confirmation Gates

For sensitive or irreversible actions, add approval steps:

**Pattern:**

```
Tool call → Show results → Get approval → Execute action
```

**Implementation:**

```
System instructions:
"After using Company Research and Enrichment workflows,
show the user:

'I've found [N] prospects:
[List with key details]

Should I create these contacts in HubSpot?'

Only proceed if user explicitly confirms."
```

**Why:** Prevents unintended actions and builds user trust.

### Handle Tool Failures Gracefully

**Bad error handling:**

```
Agent: "Error occurred. Tool failed."
[Conversation stalls]
```

**Good error handling:**

```
System instructions:
"If a tool fails:
1. Explain what happened in plain language
2. Offer alternative approaches
3. Ask user what they'd prefer

Example:
'The LinkedIn Enrichment tool isn't responding (likely API rate limit).
I can:
- Continue with the data we have
- Use an alternative enrichment source
- Try again in a few minutes
What works best?'"
```

**Why:** Resilient agents maintain momentum even when tools fail.

## Testing Strategies

### The 3-Phase Testing Approach

**Phase 1: Unit testing (Individual capabilities)**

```
Test each tool separately:
- "Use Company Research to research Microsoft"
- "Use LinkedIn Enrichment for TechCorp"
- "Create a test contact in HubSpot"

Verify:
 Tool is called
 Returns expected data
 Agent presents results clearly
```

**Phase 2: Integration testing (Tool combinations)**

```
Test tool chains:
- "Research Company X and add to HubSpot"
- "Analyze data and save to Google Sheets"

Verify:
 Tools called in logical order
 Data flows between tools
 Final output is complete
```

**Phase 3: User acceptance testing (Real scenarios)**

```
Test like a real user would:
- Ask vague questions
- Change mind mid-conversation
- Request edge cases
- Try to break it

Verify:
 Agent asks clarifying questions
 Handles ambiguity
 Recovers from errors
 Boundaries are respected
```

### Build a Test Suite

Create a document with standard test cases:

**Example test suite:**

```
BASIC FUNCTIONALITY
✓ Agent responds to greetings
✓ Sample questions all work
✓ Knowledge retrieval works
✓ Tool calling works

KNOWLEDGE TESTS
✓ "What do you know about [topic from knowledge]?"
✓ "Explain [concept from documentation]"
✓ "What's our policy on [policy from knowledge]?"

TOOL TESTS (for each tool)
✓ "[Simple tool request]"
✓ "[Complex tool request with multiple parameters]"
✓ "[Error scenario - invalid input]"

INTEGRATION TESTS
✓ "[Request requiring 2 tools]"
✓ "[Request requiring 3+ tools in sequence]"
✓ "[Request requiring approval gates]"

EDGE CASES
✓ Very long conversation (10+ turns)
✓ Ambiguous request
✓ Request outside capabilities
✓ Tool failure during workflow
✓ User says "no" to confirmation

USER EXPERIENCE
✓ Conversation feels natural
✓ Progress updates are clear
✓ Errors explained helpfully
✓ Responses are concise
```

Run through this suite:

* After every major change
* Before launching publicly
* Weekly for public agents

### A/B Test System Instructions

For public agents with traffic, test variations:

**Create two versions:**

```
Version A: Current system instructions
Version B: Modified instructions (one variable changed)
```

**Run both for a week, then:**

* Review conversations from each
* Which version led to better outcomes?
* Which had fewer errors?
* Which had better user engagement?

**Example A/B test:**

```
A: "Always cite sources"
B: "Cite sources when providing factual information"

Outcome: B was better - users found constant citations annoying
for conversational responses
```

## Performance Optimization

### Response Speed

**Slow agents are frustrating.** Optimize for speed:

**Knowledge base optimization:**

* Don't upload hundreds of documents (50-100 focused docs is plenty)
* Remove duplicate/overlapping content
* Keep individual documents under 25MB

**Tool optimization:**

* Ensure workflow agents complete quickly (under 30 seconds ideal)
* Use async operations when possible
* Add timeout handling

**Prompt optimization:**

* Shorter system instructions = faster processing
* Remove unnecessary examples
* Focus on essential guidance

### Reduce Hallucinations

**System instruction pattern:**

```
Accuracy guidelines:
- Only use information from your knowledge base or tool results
- If you're not certain, say so explicitly
- Never make up data, statistics, or quotes
- Use phrases like "Based on my knowledge..." or "I don't have information about..."
- When making inferences, clearly mark them as such

If you don't know: "I don't have that information in my knowledge base.
I can try to find it using [tool name] if you'd like."
```

**Why:** Explicit anti-hallucination instructions reduce confident but wrong answers.

### Token Efficiency

Long conversations can hit token limits:

**In system instructions:**

```
Conversation management:
- Keep responses concise (2-3 paragraphs max unless detailed output requested)
- Summarize long tool outputs instead of repeating everything
- After 10+ conversation turns, offer to start fresh if shifting topics
```

**Why:** Efficient token usage extends conversation length before context limits.

## User Experience Design

### Progressive Disclosure

Don't overwhelm users with all capabilities at once:

**Welcome message progression:**

```
Basic welcome:
"Hi! I can help with [primary use case]. What would you like to do?"

After 1-2 successful interactions:
"By the way, I can also [secondary capability]. Interested?"

After they're comfortable:
Mention advanced features as relevant
```

**Why:** Gradual exposure improves onboarding and reduces cognitive load.

### Conversation Pacing

**Too fast:**

```
User: "Research Acme Corp"
Agent: [Immediately dumps 500 words of research]
```

**Good pacing:**

```
User: "Research Acme Corp"
Agent: "I'll research Acme Corp for you. One moment..."
[Calls tool]
Agent: "Found it! Acme Corp is a B2B SaaS company ($50M revenue, 200 employees).
Would you like the full analysis or specific aspects?"

User: "Full analysis"
Agent: [Now provides complete details]
```

**Why:** Pacing gives users control and prevents information overload.

### Personality Consistency

Choose a tone and stick to it:

**Professional:**

```
"I'll analyze the competitive landscape and present findings.
One moment while I gather data..."
```

**Friendly:**

```
"Let me look into that for you! Gathering competitor info now..."
```

**Technical:**

```
"Executing competitor analysis workflow.
Estimated completion: 15 seconds.
Standby..."
```

**Why:** Consistent personality builds trust and feels more professional.

### Error Recovery

**Good error recovery pattern:**

```
1. Acknowledge the error
2. Explain what happened (simple terms)
3. Offer alternatives
4. Let user decide next step

Example:
"I tried to call the Company Research tool but it returned an error
(API rate limit). This means we've made too many requests recently.

I can:
1. Try a different research tool
2. Wait 2 minutes and retry
3. Continue without external research using my knowledge base

What would you prefer?"
```

**Why:** Users forgive errors if handled well.

## Security & Privacy

### Public Agent Considerations

If your agent is public, assume anyone might use it:

**Don't:**

* Give it access to sensitive integrations (your email, internal CRM)
* Upload confidential knowledge
* Enable destructive actions
* Store API keys in knowledge base

**Do:**

* Use read-only integrations when possible
* Curate knowledge for public consumption
* Add strong confirmation gates for any writes
* Review conversations regularly for misuse

### Sensitive Data Handling

**System instructions for sensitive scenarios:**

```
Data privacy:
- Never ask users for passwords, credit cards, or SSNs
- If users share sensitive information, remind them:
  "Please don't share sensitive personal information in this chat.
  Conversations may be logged."
- Don't store sensitive data in variables or tool calls
```

### Rate Limiting User Actions

For agents that call expensive or limited APIs:

**System instructions:**

```
Resource limits:
- Maximum 10 company researches per conversation
- After 10 researches: "We've hit the research limit for this conversation.
  Start a new chat to continue, or let me know if you want to analyze
  what we've found so far."
```

**Why:** Prevents abuse and runaway costs.

## Maintenance & Iteration

### The Weekly Review

Spend 30 minutes weekly reviewing your agent:

**What to check:**

```
1. Recent conversations (sample 10-20)
   - Any errors or confusion?
   - New use cases emerging?
   - Tools working properly?

2. Knowledge base
   - Anything outdated?
   - Missing information users asked about?

3. System instructions
   - Any patterns the agent isn't following?
   - Need to add new guidance?

4. Tools
   - All integrations still connected?
   - Workflows completing successfully?
```

**Make 1-2 improvements** based on what you find.

### Version Control for Prompts

Keep a changelog of system instruction changes:

**Example:**

```
Version 1.0 (2024-01-15)
- Initial system instructions
- Basic research capability

Version 1.1 (2024-01-22)
- Added: Explicit citation requirements
- Added: HubSpot confirmation gates
- Fixed: Too verbose responses

Version 1.2 (2024-02-01)
- Added: LinkedIn enrichment workflow
- Updated: Research workflow order
- Removed: Outdated policy reference
```

**Why:** You can roll back if a change makes things worse.

### Feedback Loops

Create mechanisms to gather feedback:

**In system instructions:**

```
After completing significant tasks:
"How did that go? Let me know if you'd like me to:
- Provide more detail
- Try a different approach
- Adjust anything"
```

**Via shared conversations:**

* Ask early users to share conversations
* Review what worked and what didn't
* Implement improvements

## Common Pitfalls & Solutions

<AccordionGroup>
  <Accordion title="Pitfall: Agent is too chatty">
    **Problem:** Agent writes paragraphs when users want quick answers

    **Solution:**
    Add to system instructions:

    ```
    Response length:
    - Default to concise responses (2-3 sentences)
    - Only provide detailed explanations if:
      a) User asks for more detail
      b) Request requires comprehensive analysis
      c) Complex topic needs context
    ```
  </Accordion>

  <Accordion title="Pitfall: Agent doesn't use tools">
    **Problem:** You enabled tools but agent just talks

    **Solution:**

    1. Check tools are actually enabled (Action Agents tab)
    2. Add explicit tool instructions to system prompt
    3. Test with direct requests: "Use \[tool name] to..."
    4. Verify tool names are clear
  </Accordion>

  <Accordion title="Pitfall: Knowledge retrieval isn't working">
    **Problem:** Agent doesn't use uploaded knowledge

    **Solution:**

    1. Verify files finished processing
    2. Ask directly: "What do you know about \[topic from knowledge]?"
    3. Check knowledge is well-structured with headings
    4. Remove duplicate/conflicting content
    5. Add to system instructions: "Always search knowledge base first"
  </Accordion>

  <Accordion title="Pitfall: Inconsistent behavior">
    **Problem:** Agent acts differently each time

    **Solution:**

    * AI is probabilistic by nature (some variation is normal)
    * Reduce variation by being MORE specific in system instructions
    * Use examples to show exact format you want
    * Test the same query 5 times - if wildly different, prompt needs work
  </Accordion>

  <Accordion title="Pitfall: Users confused about capabilities">
    **Problem:** Users ask for things agent can't do

    **Solution:**

    1. Improve welcome message clarity
    2. Better sample questions showing what agent CAN do
    3. Add to system instructions:
       "If asked about \[outside scope], say:
       'I specialize in \[your domain]. For \[their request], try \[alternative]."
  </Accordion>

  <Accordion title="Pitfall: Tool chains breaking">
    **Problem:** Multi-tool workflows fail midway

    **Solution:**

    1. Test each tool individually first
    2. Add error handling to system instructions
    3. Design tools to be independent (one tool failure doesn't break everything)
    4. Add checkpoints: After each tool, summarize what you have before calling next
  </Accordion>
</AccordionGroup>

## Advanced Patterns

### The Expert Escalation Pattern

```
System instructions:
"You are a Level 1 assistant. For simple requests, handle directly.

For complex requests involving [specific criteria]:
1. Gather initial information
2. Explain: 'This is a complex scenario. I recommend consulting
   [Knowledge Agent/Human] who specializes in [area].'
3. Offer to prepare a summary for handoff
4. Provide link to [specialized agent] if available

Complex scenarios include:
- [Criteria 1]
- [Criteria 2]
- [Criteria 3]"
```

**Use case:** Tiered support, specialized domains

### The Learning Agent Pattern

```
System instructions:
"After each conversation:
1. Note what worked well
2. Note what the user asked for that you couldn't provide
3. Suggest improvements:
   'I noticed you asked about [X]. While I can't help with that now,
   I've flagged it for my creator to add that capability.'

4. Keep a running list of feature requests in the conversation"
```

**Use case:** Continuous improvement, user research

### The Collaborative Builder Pattern

```
System instructions:
"You work iteratively with users to create [output].

Your process:
1. Understand requirements (ask questions)
2. Create initial draft (show user)
3. Get feedback (what to change)
4. Revise (incorporate feedback)
5. Repeat until user is satisfied
6. Finalize (execute output workflow)

Never deliver final output without at least 1 revision cycle.
Always show drafts before finalizing."
```

**Use case:** Content creation, design work, strategic planning

## Metrics for Success

Track these to measure your agent's effectiveness:

**Qualitative:**

* Are conversations achieving user goals?
* Do users return for multiple conversations?
* Are shared conversations examples of success?

**Quantitative:**

* Average conversation length (too short = not useful, too long = struggling)
* Tool call success rate (should be >90%)
* Knowledge retrieval frequency (are you using knowledge effectively?)

**User Feedback:**

* Explicit positive feedback
* Feature requests
* Bug reports

**Ideal Knowledge Agent:**

* Conversations: 5-15 messages to complete a task
* Tool success: 95%+ successful tool calls
* Knowledge usage: Cites knowledge in 70%+ of responses
* User satisfaction: Repeat usage, positive shared examples

## Next Steps

You now have advanced techniques for building exceptional knowledge agents:

<CardGroup cols={2}>
  <Card title="Troubleshooting" icon="triangle-exclamation" href="/knowledge-agents/troubleshooting">
    Solve specific issues and optimize performance
  </Card>

  <Card title="Configuration" icon="sliders" href="/knowledge-agents/configuration">
    Apply best practices to your system instructions
  </Card>

  <Card title="Tools Integration" icon="wrench" href="/knowledge-agents/tools-integration">
    Implement advanced tool orchestration patterns
  </Card>

  <Card title="Knowledge Base" icon="book" href="/knowledge-agents/knowledge-base">
    Optimize your knowledge for better retrieval
  </Card>
</CardGroup>

<Note>
  **Remember:** Building great knowledge agents is iterative. Start simple, launch quickly, learn from real usage, and continuously improve. The best agents evolve over time based on user feedback and measured outcomes.
</Note>


# Configuration
Source: https://docs.agent.ai/knowledge-agents/configuration

Configure your knowledge agent's personality, welcome message, and conversation settings

## Overview

Configuration is where you define your knowledge agent's personality, behavior, and first impression. These settings shape how your agent communicates and what users expect when they start a conversation.

All configuration happens in the **Introduction** and **Sample Questions** tabs of the knowledge agent builder.

## System Instructions (The Most Important Setting)

System instructions are the "brain" of your knowledge agent. This is where you define:

* Who the agent is
* What it does
* How it should behave
* When to use tools
* What boundaries exist

Think of system instructions as the agent's job description and operating manual combined.

### Anatomy of Good System Instructions

**Structure:**

```
[Role & Identity]
You are [role/title]. You [primary function].

[Capabilities]
You can:
- [Capability 1]
- [Capability 2]
- [Capability 3]

[Behavior & Approach]
When users ask you to [task]:
1. [Step 1]
2. [Step 2]
3. [Step 3]

[Tools & When to Use Them]
- Use [tool name] when [condition]
- Call [workflow name] to [accomplish task]

[Boundaries & Limitations]
- Do not [restriction]
- Always [requirement]
- If [condition], then [action]
```

### Example: Research Assistant

```
You are a research assistant that helps users conduct thorough research and analysis.

You can:
- Search your knowledge base for information on topics you've been trained on
- Use the web research tool to find current information online
- Analyze data and generate insights
- Synthesize information from multiple sources

When users ask you to research something:
1. First, search your knowledge base for relevant information
2. If you need current data or information not in your knowledge, use the web research tool
3. Present findings in a clear, organized format with sources cited
4. Ask if they want you to dig deeper into any specific aspect

Use the "Company Research" workflow when users ask about specific companies.
Use the "Web Search" workflow when you need current events or news.

Always cite your sources. If you're not confident about something, say so.
Never make up information - use your tools to find real data.
```

### Example: Marketing Assistant

```
You are a marketing strategist trained on our brand guidelines and past campaigns.

Your role is to help users create effective marketing content and campaigns.

You can:
- Understand campaign goals and target audiences
- Generate content ideas based on our brand voice
- Use the "Content Generator" workflow to create drafts
- Use the "Competitor Analysis" workflow to research competitors
- Schedule social media posts using the "Social Poster" workflow

When creating campaigns:
1. Ask clarifying questions about goals, audience, and timeline
2. Research competitors if needed using your workflow tool
3. Draft content that matches our brand voice (check your knowledge base)
4. Get user approval before executing any posting or publishing

Our brand voice is: [describe tone - professional, friendly, etc.]

Always prioritize brand consistency. If unsure about brand guidelines, check your knowledge base first.
Never post publicly without explicit user approval.
```

### Example: Development Assistant

```
You are a development assistant familiar with our codebase and development practices.

You help developers by:
- Answering questions about our architecture and APIs
- Running tests using the "Test Runner" workflow
- Creating pull requests using the "Create PR" workflow
- Deploying to staging using the "Deploy" workflow

When developers ask you to run tests or deploy:
1. Confirm which environment or test suite they want
2. Execute the appropriate workflow
3. Report results clearly, including any failures
4. Suggest next steps based on results

Reference our API documentation and architecture docs in your knowledge base when explaining technical concepts.

Only deploy to production if explicitly requested AND tests have passed.
Always create PRs for review - never push directly to main.
```

### Tips for Writing System Instructions

**Be specific about tools:**

```
Good: "Use the 'Email Sender' workflow when users ask you to send emails or notify someone."
Bad: "You can send emails."
```

**Define the workflow:**

```
Good: "When researching companies: 1) Check knowledge base first, 2) Use Company Research tool, 3) Present findings in bullet points, 4) Ask if they want more details."
Bad: "Research companies when asked."
```

**Set clear boundaries:**

```
Good: "Never make financial recommendations. Instead, present data and let users decide."
Bad: "Help with finance questions."
```

**Use examples in instructions:**

```
Good: "When presenting research, format like this:
## Key Findings
- Finding 1
- Finding 2

## Sources
- Source 1
- Source 2"

Bad: "Present research clearly."
```

## Welcome Message

The welcome message is the first thing users see when they open a chat with your agent. It should:

* Set expectations for what the agent can do
* Show personality/tone
* Encourage engagement
* Include a clear call-to-action

### Good Welcome Messages

**Research Assistant:**

```
Hi! I'm your Research Assistant. I can help you:

- Research companies, industries, and trends
- Analyze information and generate insights
- Find and summarize content from multiple sources

I have access to [describe knowledge base] and can search the web for current information.

What would you like to research today?
```

**Marketing Assistant:**

```
Hey there! I'm your Marketing Assistant, trained on our brand and past campaigns.

I can help you:
- Brainstorm campaign ideas
- Create content that matches our brand voice
- Research competitors
- Schedule social posts

Ready to create something great? What are you working on?
```

**Development Assistant:**

```
Hi! I'm here to help with development tasks.

I can:
- Answer questions about our codebase and APIs
- Run tests and report results
- Create PRs and deploy to staging
- Explain architectural decisions

What can I help you build or debug today?
```

### Welcome Message Best Practices

**Do:**

* List specific capabilities (not vague "I can help")
* Use bullet points for scannability
* Match your brand tone (professional, friendly, technical, etc.)
* End with a question to prompt engagement

**Don't:**

* Write long paragraphs
* Make promises you can't keep
* Use overly formal or stiff language (unless that's your brand)
* Forget to mention key capabilities

## Prompt Hint

The prompt hint appears in the input field as placeholder text. It guides users on what to ask or how to phrase requests.

### Effective Prompt Hints

**Examples:**

```
Research Assistant:
"Ask me to research a company or topic..."

Marketing Assistant:
"What campaign are you working on?"

Development Assistant:
"Ask me to run tests, create a PR, or explain our architecture..."

Sales Assistant:
"Enter a company name to research..."

Content Creator:
"What content do you need help creating?"

Data Analyst:
"Ask me to analyze data or generate a report..."
```

### Best Practices

**Be specific:**

```
Good: "Ask me to research a company, trend, or industry..."
Bad: "Type your question here..."
```

**Show format:**

```
Good: "Example: Research [company name] and competitors"
Bad: "Ask anything"
```

**Match your agent's purpose:**

```
For action-oriented agent: "Tell me what you need done..."
For Q&A agent: "What would you like to know?"
For creative agent: "What are you creating today?"
```

## Sample Questions

Sample questions appear as clickable buttons when users first see your agent. They:

* Show what the agent can do
* Provide examples of how to phrase requests
* Make it easy to get started (no typing needed)
* Set expectations for complexity

### How to Write Sample Questions

**Make them specific and actionable:**

```
Good:
- "Research the top 10 SaaS companies and their pricing models"
- "Create a social media campaign for our new product launch"
- "Run tests on the authentication module"
- "Analyze our competitors' content strategy"

Bad:
- "Help me with research"
- "Marketing stuff"
- "Run some tests"
- "Look at competitors"
```

**Show different capabilities:**

Don't make all sample questions do the same thing. Showcase variety:

```
For Marketing Assistant:
- "Research our top 3 competitors' content strategy"
- "Draft a product launch campaign for Q2"
- "Create social posts for our new feature announcement"
- "Analyze performance of our last campaign"
```

**Match real use cases:**

Use questions you actually expect users to ask:

```
For Development Assistant:
- "Run tests on the API endpoint changes"
- "Explain how the authentication system works"
- "Create a PR for my latest changes"
- "Deploy to staging and run smoke tests"
```

### Sample Questions Format

In the builder, enter one question per line:

```
Research the latest AI automation trends
Find information about sustainable energy startups
Analyze competitive landscape for CRM tools
Summarize key insights from tech industry news
```

These will appear as individual clickable buttons in the chat interface.

## Prompt Filtering (Content Moderation)

Prompt filtering helps prevent misuse of your agent. You can set content guidelines that the agent will follow.

### When to Use Prompt Filtering

Use filtering when your agent:

* Is public and could be misused
* Handles sensitive topics
* Should stay on-topic
* Needs to avoid certain subjects

### Example Filters

**Stay on-topic:**

```
Only respond to questions about [your domain].
If users ask about unrelated topics, politely redirect them to your area of expertise.
```

**Professional boundaries:**

```
Do not provide:
- Legal advice
- Medical advice
- Financial investment recommendations

Instead, present information and recommend consulting professionals.
```

**Brand protection:**

```
Do not:
- Make negative comments about competitors
- Discuss pricing without citing official sources
- Make promises about future features

If asked about these topics, provide factual information only.
```

### Where to Add Filtering

Include filtering rules in your **System Instructions**:

```
You are a [role].

[Main instructions...]

Content Guidelines:
- Only respond to questions about [topic area]
- Do not provide [restricted advice]
- If asked about [off-topic], say: "I specialize in [your area]. For [their topic], I recommend [alternative]."
- Remain professional and helpful even if users are frustrated
```

## Configuration Templates by Use Case

### Personal Clone / Expert Assistant

```
**System Instructions:**
You are [Your Name]'s AI assistant, trained on their work, thinking, and expertise in [domain].

You can help users by:
- Answering questions about [your expertise]
- Using workflows to [accomplish tasks]
- Providing insights based on [your knowledge]

When helping users:
1. Draw from [Your Name]'s documented knowledge and approach
2. Use available workflows to accomplish tasks
3. Admit when you need clarification
4. Maintain [your personal tone - professional, casual, etc.]

Use [workflow names] to [accomplish specific tasks].

**Welcome Message:**
Hi! I'm [Your Name]'s AI assistant. I can help you with [key areas of expertise] and can execute tasks using my integrated workflows.

What can I help you with today?

**Prompt Hint:**
Ask me anything about [your domain] or tell me what you need done...

**Sample Questions:**
- [Example question 1 that showcases knowledge]
- [Example question 2 that uses a workflow]
- [Example question 3 that combines both]
```

### Collaborative Builder

```
**System Instructions:**
You are a collaborative assistant that works iteratively with users to build and create [type of output].

Your approach:
1. Understand what the user wants to create
2. Ask clarifying questions about requirements
3. Use your workflows to generate initial drafts
4. Get feedback and iterate
5. Refine until the user is satisfied

Available workflows:
- [Content Generator] - Creates initial drafts
- [Analyzer] - Reviews and suggests improvements
- [Publisher] - Outputs final version

Always collaborate - never just output without discussion.
Ask for feedback at each step.

**Welcome Message:**
Hi! I'm here to help you build [type of thing].

I work collaboratively - we'll discuss what you need, I'll create drafts, and we'll refine together until it's exactly what you want.

What are you looking to create?

**Prompt Hint:**
Tell me what you want to build and we'll create it together...

**Sample Questions:**
- "Create a comprehensive guide about [topic]"
- "Build a campaign strategy for [purpose]"
- "Design a workflow for [process]"
```

### Domain Expert Tool

```
**System Instructions:**
You are an expert in [specific domain] with deep knowledge of [subtopics].

You help by:
- Answering complex questions about [domain]
- Performing analysis using your integrated tools
- Providing actionable recommendations
- Explaining concepts clearly

When users ask questions:
1. Search your knowledge base for relevant information
2. If analysis is needed, use the [Analysis workflow]
3. Present findings with sources and citations
4. Offer to dig deeper or explore related topics

For tasks requiring action, use:
- [Tool 1] for [purpose]
- [Tool 2] for [purpose]

Your knowledge is current as of [date knowledge was added].
For very current information, use the web search tool.

**Welcome Message:**
Hi! I'm your [domain] expert with deep knowledge of [subtopics].

I can:
- Answer questions and explain concepts
- Analyze [types of data/content]
- Provide strategic recommendations

I have access to [knowledge sources] and analytical tools.

What would you like to explore?

**Prompt Hint:**
Ask me about [domain topics] or request analysis...

**Sample Questions:**
- "Explain [complex concept] in [domain]"
- "Analyze [specific type of data/situation]"
- "What are best practices for [domain activity]?"
- "Compare [option A] vs [option B] for [use case]"
```

## Testing Your Configuration

After setting up your configuration:

1. **Start fresh conversation** - Test the welcome message

2. **Click sample questions** - Verify they work as expected

3. **Test prompt hint** - Does it guide users appropriately?

4. **Test system instructions:**
   * Does the agent stay in character?
   * Does it use tools when appropriate?
   * Does it follow the workflow you defined?
   * Does it respect boundaries?

5. **Test edge cases:**
   * Ask off-topic questions (does filtering work?)
   * Request things outside capabilities (does it admit limitations?)
   * Give ambiguous requests (does it ask clarifying questions?)

## Common Configuration Mistakes

<Warning>
  **Mistake #1: Vague System Instructions**

  Bad: "You are helpful and answer questions."

  Good: "You are a research assistant. When users ask you to research topics, first search your knowledge base, then use the Web Research workflow if needed. Present findings in bullet points with sources."

  **Fix:** Be specific about what, when, and how.
</Warning>

<Warning>
  **Mistake #2: Not Mentioning Tools**

  Bad: System instructions don't mention the workflow agents you enabled.

  Good: "Use the 'Email Sender' workflow when users ask you to send emails. Use the 'Data Analyzer' workflow to process and analyze datasets."

  **Fix:** Explicitly tell the agent when to use each tool.
</Warning>

<Warning>
  **Mistake #3: Overlong Welcome Messages**

  Bad: 5 paragraphs explaining every feature in detail.

  Good: 3-4 bullet points highlighting key capabilities + a question.

  **Fix:** Users won't read long welcomes. Keep it scannable.
</Warning>

<Warning>
  **Mistake #4: Generic Sample Questions**

  Bad: "Help me with my work" / "Answer questions" / "Do research"

  Good: "Research top 10 AI companies and their funding rounds" / "Create a content calendar for April"

  **Fix:** Make sample questions specific enough to be useful examples.
</Warning>

## Next Steps

Now that you understand configuration:

<CardGroup cols={2}>
  <Card title="Add Knowledge" icon="book" href="/knowledge-agents/knowledge-base">
    Train your agent with domain expertise
  </Card>

  <Card title="Enable Tools" icon="wrench" href="/knowledge-agents/tools-integration">
    Give your agent action-taking capabilities
  </Card>

  <Card title="Best Practices" icon="star" href="/knowledge-agents/best-practices">
    Learn advanced prompt engineering techniques
  </Card>

  <Card title="Troubleshooting" icon="triangle-exclamation" href="/knowledge-agents/troubleshooting">
    Fix common configuration issues
  </Card>
</CardGroup>

<Note>
  **Remember:** Configuration is iterative. Start with a basic setup, test with real users, and refine based on what works. Your system instructions will evolve as you learn how users interact with your agent.
</Note>


# Conversations & Sharing
Source: https://docs.agent.ai/knowledge-agents/conversations

Manage conversations, share your knowledge agent, and create great user experiences

## How Conversations Work

When someone interacts with your knowledge agent, each interaction creates a **conversation**. Think of conversations like chat threads - they have:

* **History** - All messages in the conversation
* **Context** - The AI remembers previous messages
* **Auto-generated titles** - AI creates descriptive names
* **Shareable links** - Can be shared publicly
* **Forking** - Others can copy and continue from any point

Each conversation is isolated - what happens in one doesn't affect others.

## Conversation Lifecycle

```
User opens your knowledge agent
        ↓
New conversation created automatically
        ↓
User and agent exchange messages
        ↓
AI generates a descriptive title
        ↓
Conversation saved to history
        ↓
User can share, fork, or continue later
```

## Auto-Generated Titles

Your knowledge agent automatically generates descriptive titles for conversations after the first few messages.

**How it works:**

* AI analyzes the conversation topic
* Generates a concise, descriptive title
* Title appears in conversation history
* Makes it easy to find past conversations

**Examples of auto-generated titles:**

* "Researching AI automation competitors"
* "Creating social media campaign for product launch"
* "Analyzing Q3 sales data and trends"
* "Debugging authentication module errors"

**You can't customize the title format**, but you can influence it through:

* Clear user requests (AI titles based on main topic)
* Focused conversations (don't jump between unrelated topics)

<Tip>
  If a conversation covers multiple topics, the AI typically titles it based on the first major topic discussed.
</Tip>

## Conversation History

All conversations are automatically saved and accessible from the conversation history panel.

### Accessing Your Conversations

**As the agent builder:**

1. Open your knowledge agent
2. Look for the conversation list (usually left sidebar)
3. See all conversations sorted by most recent
4. Click any conversation to reopen it

**For users interacting with your agent:**

1. Conversations are saved in their account
2. They can return and continue conversations
3. History persists across sessions

### What's Saved

Each conversation stores:

* All messages (user and agent)
* Tool calls made
* Knowledge retrieved
* Timestamps
* Auto-generated title

<Note>
  **Privacy note:** Builders can see conversations with their own knowledge agents. Consider this when deciding what features to enable on public agents.
</Note>

## Sharing Conversations

One of the most powerful features of knowledge agents is the ability to share individual conversations via public links.

### How to Share a Conversation

1. **Have a conversation** with your knowledge agent
2. **Look for the share icon** (usually top-right of conversation)
3. **Click to generate a shareable link**
4. **Copy and share** the link anywhere

The link looks like: `https://agent.ai/chat/[conversation-id]`

### What Shared Links Include

When someone opens a shared conversation link, they see:

* **Full conversation history** - All messages in the conversation
* **Read-only view** - They can read but not modify the original
* **Fork option** - They can copy the conversation and continue it
* **Agent information** - Who built it, description

### Use Cases for Sharing

**Showcase examples:**

```
Share great examples of your knowledge agent in action:
- Marketing campaigns it created
- Research it conducted
- Code it helped debug
- Reports it generated

Use these as portfolio pieces or demos.
```

**Collaborative work:**

```
Work with someone on a project:
- Start conversation with your knowledge agent
- Get to a point where you want input
- Share link with colleague
- They can fork and continue
```

**Support and troubleshooting:**

```
If something isn't working:
- Create a conversation showing the issue
- Share with support or the agent builder
- They can see exactly what happened
```

**Teaching and examples:**

```
Create example conversations showing:
- How to use the agent effectively
- What kinds of questions to ask
- Sample workflows end-to-end

Share these as tutorials.
```

### Privacy Considerations

<Warning>
  **Important:** Shared conversation links are **public** - anyone with the link can view the conversation.

  **Don't share conversations containing:**

  * Personal information (emails, phone numbers, addresses)
  * Confidential business data
  * API keys, passwords, or credentials
  * Private customer information
  * Sensitive internal discussions

  **Before sharing, review the entire conversation** to ensure nothing sensitive is included.
</Warning>

### Best Practices for Sharing

**Do:**

* Review the conversation before sharing
* Share conversations that demonstrate value
* Use as examples in documentation
* Share success stories and use cases
* Include context when sharing (explain why it's interesting)

**Don't:**

* Share sensitive information
* Share conversations with errors if showcasing capabilities
* Share incomplete conversations that might confuse viewers
* Assume shared links are private (they're public)

## Forking Conversations

**Forking** lets users copy a conversation and continue it themselves. This creates powerful collaboration and learning opportunities.

### How Forking Works

```
Original conversation (shared by builder)
        ↓
User clicks "Fork" or "Continue this conversation"
        ↓
Exact copy created in user's account
        ↓
User can now continue the conversation
        ↓
Original conversation unchanged
```

### When Users Might Fork

**To build on examples:**

```
Builder shares: "Here's how to research competitors"
User forks: Continues with their own competitor list
```

**To customize for their needs:**

```
Builder shares: "Campaign strategy for SaaS product"
User forks: Adapts strategy for their specific product
```

**To learn and experiment:**

```
Builder shares: "Complex data analysis workflow"
User forks: Tries with their own data
```

**To collaborate asynchronously:**

```
Team member 1 starts conversation
Shares link
Team member 2 forks and continues
Shares updated version back
```

### Enabling Productive Forking

As a builder, you can encourage forking by:

**Creating "template" conversations:**

* Start a conversation with your agent
* Walk through a complete workflow
* Stop at a point where users can customize
* Share with instruction: "Fork this and add your data"

**Example:**

```
Title: "Competitor Research Template"

Conversation:
Agent: "I'll help you research competitors. What industry are you in?"
[Builder]: "SaaS"
Agent: "Great! I'll research SaaS competitors. Which companies should I analyze?"
[Builder]: "Add your companies here →"

[Share this - users fork and replace with their companies]
```

**Building progressive examples:**

* Share multiple conversations showing progression
* Each one builds on the previous
* Users can fork at any stage
* Creates learning pathways

## Managing Conversations as a Builder

### Testing Your Agent

As you build and refine your knowledge agent, you'll have many test conversations:

**Organizing test conversations:**

* Use consistent naming in your test prompts
* Delete obviously failed test conversations
* Keep successful examples to share later
* Archive old tests after major updates

**Starting fresh tests:**

* Always start a new conversation for each test scenario
* Don't reuse old conversations (context bleeds through)
* Test with realistic user scenarios

### Monitoring Usage

Check your conversation history to understand:

* What users are asking for
* Where the agent succeeds
* Where it gets confused
* What workflows are most popular

**Use this feedback to:**

* Refine system instructions
* Add relevant knowledge
* Enable additional tools
* Update sample questions

<Tip>
  **Pro tip:** Review your first 10-20 real user conversations carefully. They'll reveal assumptions you made that users don't share, and unexpected use cases you didn't anticipate.
</Tip>

## User Experience Best Practices

### Setting Expectations in the First Message

Your welcome message is critical. It should:

**Be clear about capabilities:**

```
Good:
"Hi! I can research companies, enrich with LinkedIn data,
and add them to HubSpot. What would you like to research?"

Bad:
"Hello! How can I help you today?"
```

**Show example interactions:**

```
Include in your welcome message:
"Try asking me:
- 'Research TechCorp and its competitors'
- 'Find 10 AI startups in San Francisco'
- 'Enrich this list with funding data'"
```

**Set boundaries:**

```
"I specialize in company research and CRM enrichment.
For general questions, I recommend [alternative]."
```

### Conversational Flow

**Acknowledge long-running tasks:**

```
Bad:
[Agent calls tool, user sees nothing for 30 seconds, then results]

Good:
"Let me research that for you..."
[Calls tool]
"Found 15 companies, now enriching with LinkedIn data..."
[Calls tool]
"Analysis complete! Here are the results:"
```

**Ask clarifying questions early:**

```
User: "Research competitors"

Good agent response:
"I'd be happy to research competitors. A few questions:
- What industry or product category?
- Geographic focus?
- Should I include indirect competitors too?"

Bad agent response:
"Okay, researching competitors..."
[Doesn't know what to research]
```

**Confirm before sensitive actions:**

```
Good:
"I've drafted an email to the CEO. Here's what I'll send:
[Shows email]
Should I send this?"

Bad:
"Email sent to CEO."
[User had no chance to review]
```

### Error Handling

When things go wrong, your agent should:

**Explain what happened:**

```
Good:
"I tried to call the Company Research workflow but it returned
an error: 'API rate limit exceeded'. This means we've made too
many requests. I can try again in a few minutes, or we can
approach this differently. What would you prefer?"

Bad:
"Error occurred."
```

**Offer alternatives:**

```
"The LinkedIn enrichment tool isn't responding. I can:
1. Try a different enrichment source
2. Continue with the data we have
3. Wait and try again later

What works best for you?"
```

**Don't get stuck:**

```
If a tool fails repeatedly, don't keep trying.
Agent should: "This tool seems to be having issues. Let me try
a different approach..." or "I'll skip this step for now..."
```

## Conversation Analytics

While you can't export conversation data directly, you can learn from patterns:

### What to Look For

**Common question patterns:**

* Are users asking for things your agent can't do?
* → Consider adding new tools or knowledge

**Where conversations succeed:**

* Which workflows work smoothly?
* → Highlight these in examples

**Where conversations fail:**

* Where does the agent get confused?
* → Update system instructions or add knowledge

**Unexpected use cases:**

* Are users doing things you didn't anticipate?
* → Consider optimizing for these patterns

### Iterating Based on Conversations

**Weekly review process:**

1. Review 10-20 recent conversations
2. Identify 3 common issues
3. Make 1-2 specific improvements
4. Test improvements with new conversations
5. Repeat

**Example improvement cycle:**

```
Week 1 observation: Users often ask for data exports
Action: Enable Google Sheets integration

Week 2 observation: Agent doesn't explain what it's doing
Action: Update system instructions to narrate actions

Week 3 observation: Users confused about what agent can do
Action: Update welcome message and sample questions
```

## Advanced: Conversation Handoffs

For complex agents, you might want to design conversation handoffs:

### Handing Off to Humans

```
System instructions:
"If the user requests something outside your capabilities,
offer to connect them with a human:

'This requires human expertise. I can:
1. Summarize our conversation so far
2. Send a notification to [team/person]
3. Save our discussion for their review

What would you prefer?'"
```

### Handing Off to Other Agents

```
System instructions:
"For [specific task type], suggest forking to the
specialized agent:

'For advanced data analysis, I recommend forking this
conversation to our Data Analysis Knowledge agent:
[link]. It has specialized tools for [capability].
Should I prepare a summary to start there?'"
```

## Troubleshooting Conversations

<AccordionGroup>
  <Accordion title="Conversation history isn't saving">
    **Symptoms:** Conversations disappear or don't persist

    **Possible causes:**

    1. Browser cookies/storage disabled
    2. Incognito/private browsing mode
    3. Account authentication issues

    **Solutions:**

    * Ensure user is logged in
    * Check browser allows cookies and local storage
    * Try a different browser
    * Clear cache and reload
  </Accordion>

  <Accordion title="Agent loses context mid-conversation">
    **Symptoms:** Agent forgets what was discussed earlier

    **Possible causes:**

    1. Conversation is very long (approaching token limits)
    2. User jumped between multiple unrelated topics
    3. Technical issue with conversation state

    **Solutions:**

    * Start a new conversation for new topics
    * Keep conversations focused on one main task
    * If very long conversation, fork and continue fresh
    * This is rare - if it happens often, report to support
  </Accordion>

  <Accordion title="Shared link isn't working">
    **Symptoms:** Link shows error or "not found"

    **Possible causes:**

    1. Conversation was deleted
    2. Agent was made private
    3. Link was copied incorrectly

    **Solutions:**

    * Verify the agent is still public
    * Check conversation still exists in your history
    * Copy the share link again
    * Ensure full URL is included (including https\://)
  </Accordion>

  <Accordion title="How do I delete a conversation?">
    **Answer:**

    1. Find the conversation in your history
    2. Look for delete/trash icon (usually hover or right-click)
    3. Confirm deletion

    **Note:** Deleted conversations cannot be recovered. If you shared the conversation link, it will no longer work.
  </Accordion>

  <Accordion title="Can I edit messages in a conversation?">
    **Answer:** No, conversations are immutable. You cannot edit messages after they're sent. If you made a mistake:

    * Continue the conversation with clarification
    * Start a new conversation
    * Fork the conversation at an earlier point

    This ensures shared conversations remain truthful representations.
  </Accordion>

  <Accordion title="How do I export a conversation?">
    **Answer:** There's no built-in export feature currently, but you can:

    * Copy and paste the conversation text
    * Take screenshots
    * Share the link and reference it externally
    * Use the conversation as training data (upload as knowledge)
  </Accordion>
</AccordionGroup>

## Next Steps

Now that you understand conversation management and sharing:

<CardGroup cols={2}>
  <Card title="Best Practices" icon="star" href="/knowledge-agents/best-practices">
    Learn advanced techniques for building exceptional knowledge agents
  </Card>

  <Card title="Troubleshooting" icon="triangle-exclamation" href="/knowledge-agents/troubleshooting">
    Solve common issues and optimize your agent's performance
  </Card>

  <Card title="Configuration" icon="sliders" href="/knowledge-agents/configuration">
    Review how to write better system instructions and prompts
  </Card>

  <Card title="Tools Integration" icon="wrench" href="/knowledge-agents/tools-integration">
    Give your agent more capabilities to create better conversations
  </Card>
</CardGroup>

<Note>
  **Remember:** Every conversation is an opportunity to learn what works and what doesn't. Review conversations regularly, share your best examples, and continuously refine based on real usage.
</Note>


# Knowledge Base
Source: https://docs.agent.ai/knowledge-agents/knowledge-base

Train your knowledge agent with custom knowledge from documents, websites, videos, and more

## What is a Knowledge Base?

A knowledge base is the collection of information your knowledge agent can search and reference when answering questions or making decisions. Think of it as your agent's memory - the more relevant knowledge you add, the more helpful and accurate your agent becomes.

Unlike traditional chatbots that only know what they were trained on, knowledge agents use **Retrieval Augmented Generation (RAG)** to dynamically search your knowledge and incorporate it into responses.

## How Knowledge Retrieval Works (RAG Simplified)

Here's what happens when someone asks your knowledge agent a question:

```
User asks: "What's our refund policy?"
        ↓
Agent converts question to a search query
        ↓
Searches knowledge base for relevant content
        ↓
Finds: "Refund Policy.pdf" - page 2, section 3
        ↓
AI reads the relevant section
        ↓
Generates answer using that specific information
        ↓
Responds: "According to our refund policy, customers can..."
```

**Key point:** Your agent doesn't memorize everything - it searches and retrieves relevant pieces on-demand. This means:

* You can add lots of knowledge without "retraining"
* Answers come from your actual documents
* You can update knowledge anytime
* Agent cites sources (useful for verification)

## Supported Knowledge Sources

You can train your knowledge agent with six types of content:

| Source Type       | What It's For                      | Processing Time |
| ----------------- | ---------------------------------- | --------------- |
| **Files**         | PDFs, Word docs, text files        | 10-30 seconds   |
| **URLs**          | Web pages, articles, documentation | 15-45 seconds   |
| **YouTube**       | Video transcripts                  | 20-60 seconds   |
| **Google Docs**   | Workspace documents                | 10-30 seconds   |
| **Google Sheets** | Spreadsheet data                   | 10-30 seconds   |
| **Twitter/X**     | Tweets and threads                 | 15-45 seconds   |
| **LinkedIn**      | Profiles and posts                 | 20-60 seconds   |

All sources are automatically:

* Chunked into searchable segments
* Embedded as vectors for semantic search
* Stored in your agent's vector database
* Instantly available for retrieval

## Adding Knowledge: Step-by-Step

### Files (PDF, DOCX, TXT)

**Best for:** Documentation, reports, guides, research papers

**How to add:**

1. Navigate to your knowledge agent builder
2. Click the **"Training"** tab
3. Click the **"Files"** sub-tab
4. Click **"Upload"** or drag and drop files
5. Wait for processing (progress bar shows status)
6. File appears in the list when ready

**Supported formats:**

* PDF (.pdf)
* Microsoft Word (.doc, .docx)
* Plain text (.txt)
* Markdown (.md)

**Tips:**

* PDFs work best when they contain actual text (not scanned images)
* Remove unnecessary pages to improve relevance
* File names help the agent understand context - use descriptive names

<Warning>
  **File size limit:** 25MB per file. For larger documents, consider splitting them or using a URL if the content is available online.
</Warning>

### Web URLs

**Best for:** Websites, blog posts, online documentation, public articles

**How to add:**

1. Go to the **"Training"** tab
2. Click the **"URLs"** sub-tab
3. Paste the full URL (starting with https\://)
4. Click **"Add URL"**
5. Content is scraped and processed automatically

**What gets extracted:**

* Main text content from the page
* Headings and structure
* Some metadata (title, author if available)
* **Not extracted:** Images, videos, interactive elements

**Special handling:**

**Google Docs:**

* Paste the sharing link (make sure it's accessible via link)
* Agent automatically exports to readable format
* Formatting is preserved

**Google Sheets:**

* Paste the sharing link
* Data is exported and indexed
* Useful for product catalogs, pricing, data tables

<Tip>
  **Pro tip:** For documentation sites with many pages, add the most important/overview pages. You don't need every single page - the agent will direct users based on what you've added.
</Tip>

### YouTube Videos

**Best for:** Tutorials, presentations, interviews, educational content

**How to add:**

1. Go to the **"Training"** tab
2. Click the **"YouTube Videos"** sub-tab
3. Paste the YouTube video URL
4. Click **"Add Video"**
5. Agent automatically extracts the transcript

**What gets indexed:**

* Full transcript of spoken words
* Video title and description
* Channel information
* Key moments/chapters (if available)

**Important notes:**

* Video must have captions/subtitles (auto-generated works)
* Videos without transcripts cannot be processed
* Transcript language is auto-detected

**Use cases:**

* Index your tutorial videos so agent can answer "how-to" questions
* Add conference talks or presentations
* Include product demos or walkthroughs
* Reference expert interviews or talks

### Twitter/X Posts

**Best for:** Twitter threads, announcements, thought leadership content

**How to add:**

1. Go to the **"Training"** tab
2. Click the **"Twitter"** sub-tab
3. Enter a Twitter username (without @) or paste a tweet URL
4. Click **"Add"**

**What gets indexed:**

* Tweet text content
* Thread structure (if it's a thread)
* Author information
* Timestamps

**Use cases:**

* Add your own tweets to train agent on your thinking
* Include industry expert threads
* Reference announcement tweets
* Capture Twitter-based discussions

### LinkedIn Content

**Best for:** Professional profiles, thought leadership posts, company updates

**How to add:**

1. Go to the **"Training"** tab
2. Click the **"LinkedIn"** sub-tab
3. Enter a LinkedIn profile URL or post URL
4. Click **"Add"**

**What gets indexed:**

* Profile headline and about section
* Recent posts and articles
* Experience and background (for profiles)
* Post content and engagement

**Use cases:**

* Add your LinkedIn profile to train agent on your expertise
* Include company LinkedIn posts
* Reference industry leader profiles
* Capture professional insights and articles

## Managing Your Knowledge Base

### Viewing Your Knowledge

In the **Training** tab, you'll see all your knowledge sources listed with:

* Source name/title
* Type (file, URL, video, etc.)
* Upload date
* Processing status
* File size or length

### Refreshing Content

For URLs, YouTube videos, and social media sources, you can refresh the content to get updates:

1. Find the source in the list
2. Click the **refresh icon** next to it
3. Agent re-fetches and re-processes the content
4. Updated content replaces the old version

**When to refresh:**

* Documentation has been updated
* YouTube video captions were improved
* Twitter thread was extended
* Website content changed

<Note>
  **Files can't be refreshed** - you'll need to delete and re-upload if you have a newer version.
</Note>

### Deleting Knowledge

To remove a knowledge source:

1. Find it in the Training tab list
2. Click the **delete icon** (trash can)
3. Confirm deletion
4. Source is removed immediately from knowledge base

**Important:** Deleting knowledge affects all future conversations. Past conversations won't change, but new chats won't have access to that information anymore.

### Organizing Your Knowledge

While there's no folder structure, you can organize by:

* Using clear, descriptive file names
* Adding related content in batches
* Keeping a separate document tracking what you've added
* Deleting outdated content regularly

## Knowledge Base Best Practices

### Quality Over Quantity

**Don't do this:**

* Upload hundreds of barely relevant documents
* Add your entire website including footer text and navigation
* Include duplicate or very similar content
* Add content "just in case"

**Do this instead:**

* Curate high-quality, relevant sources
* Include core documentation and key resources
* Remove or don't include boilerplate/duplicate content
* Think "What do users actually need to know?"

**Why:** Too much irrelevant content can actually hurt performance. The agent might retrieve less relevant chunks if there's too much noise.

### Keep Content Fresh

* **Review quarterly:** Check if knowledge is still accurate
* **Update when things change:** New product features, policy changes, etc.
* **Remove outdated info:** Delete deprecated content
* **Refresh URLs:** Re-fetch content from living documents

### Structure Matters

**Good knowledge sources:**

* Well-organized with clear headings
* Use bullet points and lists
* Have logical flow
* Include examples and specifics

**Poor knowledge sources:**

* Wall of text with no structure
* Overly vague or general
* Lots of irrelevant tangents
* Poorly formatted (weird spacing, encoding issues)

### Match Your Use Case

**For Q\&A agents:**

* Add FAQs, help docs, policies
* Include troubleshooting guides
* Add product documentation

**For research agents:**

* Add research papers and reports
* Include industry analysis
* Add expert content and thought leadership

**For task-oriented agents:**

* Add process documentation
* Include how-to guides
* Add standard operating procedures

### Test Your Knowledge

After adding knowledge, test if the agent can retrieve it:

1. Ask direct questions from the content
2. Ask questions that require combining multiple sources
3. Try edge cases or less obvious questions
4. Check if sources are cited correctly

**If retrieval isn't working:**

* Question may not match terminology in knowledge
* Content may be too scattered or vague
* May need more (or different) context
* Try rephrasing the question

## Troubleshooting Knowledge Issues

<AccordionGroup>
  <Accordion title="Agent isn't using my knowledge">
    **Symptoms:** Agent gives generic answers instead of using uploaded content

    **Possible causes:**

    1. Knowledge still processing (check for status indicator)
    2. Question doesn't semantically match content
    3. System prompt doesn't encourage knowledge use
    4. Content is too vague or poorly structured

    **Solutions:**

    * Wait for all files to finish processing
    * Ask questions more directly related to your content
    * Update system prompt: "Always search your knowledge base first"
    * Restructure content with clear headings and sections
    * Try asking: "What do you know about \[topic from your knowledge]?"
  </Accordion>

  <Accordion title="Agent retrieves wrong or irrelevant knowledge">
    **Symptoms:** Agent cites sources but they're not relevant to the question

    **Possible causes:**

    1. Knowledge base has too much content
    2. Multiple sources with similar but different info
    3. Content lacks clear topic markers
    4. Semantic search matching wrong chunks

    **Solutions:**

    * Remove less relevant sources
    * Add more specific/targeted knowledge
    * Use clearer headings in source documents
    * Be more specific in questions
    * Consider splitting large documents into focused pieces
  </Accordion>

  <Accordion title="Upload fails or gets stuck">
    **Symptoms:** File upload never completes or shows error

    **Possible causes:**

    1. File too large (>25MB limit)
    2. File format not supported
    3. File is corrupted or password-protected
    4. Network connection issue

    **Solutions:**

    * Check file size (compress or split if too large)
    * Convert to supported format (PDF, DOCX, TXT)
    * Remove password protection
    * Try uploading again with stable connection
    * For large documents, try URL if available online
  </Accordion>

  <Accordion title="YouTube video transcript not extracting">
    **Symptoms:** Error when adding YouTube video

    **Possible causes:**

    1. Video doesn't have captions/transcripts
    2. Video is private or age-restricted
    3. Captions are disabled by creator
    4. Invalid YouTube URL

    **Solutions:**

    * Check if video has captions (watch on YouTube first)
    * Use public, unrestricted videos
    * Ensure URL is correct YouTube format
    * Try a different video if captions unavailable
  </Accordion>

  <Accordion title="Google Docs/Sheets not loading">
    **Symptoms:** Can't add Google Workspace content

    **Possible causes:**

    1. Sharing settings not set to "Anyone with the link"
    2. Document is private
    3. Requires authentication to access
    4. Invalid share link

    **Solutions:**

    * Change sharing to "Anyone with the link can view"
    * Copy the full sharing URL (should have /edit or /view)
    * Make sure document isn't restricted to your organization
    * Test link in incognito browser to verify public access
  </Accordion>

  <Accordion title="How do I know which knowledge was used?">
    **Answer:** As a builder, when you test your knowledge agent, you can see knowledge retrieval:

    * Look for **\[file search]** indicator in responses
    * Agent may cite sources in its answer
    * Some responses show which documents were referenced

    For end users, citations depend on how you've prompted the agent. You can encourage citations in system instructions: "Always cite which document you used."
  </Accordion>
</AccordionGroup>

## Knowledge Base Limits

**Per agent:**

* No hard limit on number of sources
* Recommended: 50-100 high-quality sources for best performance
* Each file limited to 25MB

**Processing:**

* Files process individually (can upload multiple at once)
* URLs are processed on-demand
* Large knowledge bases may have slightly slower retrieval

**Storage:**

* Knowledge is stored in vector database
* Counts toward your plan's storage limits
* Deleted knowledge is removed from storage

## Advanced Tips

<Tip>
  **Create a "master FAQ" document**

  Instead of uploading 20 separate PDFs, create one well-structured FAQ document with all common questions. Use clear headings like "## Pricing Questions" and "## Feature Questions". This helps retrieval accuracy.
</Tip>

<Tip>
  **Use knowledge categories**

  Name your files descriptively and consider prefixes:

  * "\[POLICY] Refund Policy.pdf"
  * "\[GUIDE] Getting Started Guide.pdf"
  * "\[FAQ] Common Questions.pdf"

  This helps both you and the agent understand context.
</Tip>

<Tip>
  **Test with "knowledge audit" questions**

  After adding knowledge, ask: "What do you know about \[topic]?" or "What information do you have about \[subject]?" This shows you what the agent can access.
</Tip>

<Tip>
  **Combine sources for depth**

  For comprehensive topics, add multiple source types:

  * Documentation (files)
  * Tutorial video (YouTube)
  * FAQ page (URL)
  * Expert thread (Twitter)

  This gives the agent multiple perspectives and formats.
</Tip>

<Tip>
  **Keep a knowledge changelog**

  Track what you've added and when. This helps you:

  * Remember what's in the knowledge base
  * Know when content was last updated
  * Identify gaps in coverage
  * Plan future additions
</Tip>

## Next Steps

Now that you understand the knowledge base system:

<CardGroup cols={2}>
  <Card title="Configure Your Agent" icon="sliders" href="/knowledge-agents/configuration">
    Write system prompts that encourage knowledge use
  </Card>

  <Card title="Add Tools" icon="wrench" href="/knowledge-agents/tools-integration">
    Combine knowledge with action-taking capabilities
  </Card>

  <Card title="Best Practices" icon="star" href="/knowledge-agents/best-practices">
    Learn optimization strategies for knowledge bases
  </Card>

  <Card title="Troubleshooting" icon="triangle-exclamation" href="/knowledge-agents/troubleshooting">
    Solve common knowledge retrieval issues
  </Card>
</CardGroup>

<Note>
  **Remember:** Your knowledge base is living and evolving. Start with core content, test with real questions, and continuously refine based on what works. Quality, relevance, and organization matter more than quantity.
</Note>


# Knowledge Agents Overview
Source: https://docs.agent.ai/knowledge-agents/overview

Build powerful AI assistants that think, converse, and take action

## What Are Knowledge Agents?

Knowledge Agents are conversational AI assistants that combine knowledge, reasoning, and the ability to take action. They're not just chatbots that answer questions - they're collaborative partners that can help you get work done.

Think of knowledge agents as building your own specialized AI assistant that:

* Understands your specific domain or expertise
* Converses naturally to understand what you need
* Calls tools and workflows to actually accomplish tasks
* Works iteratively with you to solve problems
* Gets better as you train it with more knowledge

**The key difference:** Knowledge agents don't just tell you how to do something - they can actually do it for you by invoking workflow agents and integrations.

<Note>
  **Example:** The [Knowledge Agent Builder Assistant](https://agent.ai/agent/wckej2awts7l2ffv) you see on Agent.AI is itself an knowledge agent! It helps you build knowledge agents by understanding what you want to create and can even invoke workflows to help set things up.
</Note>

## Knowledge Agents vs Workflow Agents

Agent.AI offers two types of agents that work powerfully together:

| Aspect               | Knowledge Agent          | Workflow Agent             |
| -------------------- | ------------------------ | -------------------------- |
| **Interface**        | Conversational chat      | Step-by-step workflow      |
| **How it works**     | AI-driven, adaptive      | Deterministic, predictable |
| **Best for**         | Understanding + action   | Automation + tasks         |
| **Execution**        | Decides what to do       | Follows exact steps        |
| **User interaction** | Collaborative dialogue   | Input → Run → Output       |
| **When to use**      | Complex, varied requests | Repeatable processes       |

### The Power of Combining Both

The magic happens when knowledge agents **invoke workflow agents as tools**:

```
User: "Find 10 tech companies in SF and enrich them with LinkedIn data"
         ↓
Knowledge Agent understands the request
         ↓
Calls your "Company Search" workflow agent
         ↓
Gets results, then calls "LinkedIn Enrichment" workflow
         ↓
Presents enriched data conversationally
         ↓
User: "Now save the top 5 to a Google Sheet"
         ↓
Knowledge Agent calls "Export to Sheets" workflow
         ↓
Done! User can keep iterating
```

This creates a natural, conversational way to orchestrate complex multi-step work.

## When to Use Knowledge Agents

Choose knowledge agents when you want to:

### Build a Personal Clone or Expert Assistant

Create an AI version of yourself or an expert in your domain:

* **Your personal assistant** - Trained on your work, knows your processes, can execute tasks
* **Domain expert** - Deep knowledge in a specific field (marketing, development, research)
* **Collaborative partner** - Works iteratively with users to build/create something
* **Problem solver** - Understands complex requests and orchestrates multiple tools

**Example use cases:**

* Marketing strategist that can research, analyze, and create campaigns
* Development assistant that understands your codebase and can run workflows
* Research assistant that finds papers, analyzes them, and generates summaries
* Sales assistant that researches companies and drafts outreach

### Create Interactive Tools

Build powerful interactive experiences:

* **Guided workflows** - Conversational interface for complex processes
* **Data analysts** - Ask questions about data, agent runs analysis workflows
* **Content creators** - Collaborate on creating content across multiple steps
* **Report generators** - Understand report requirements and orchestrate creation

### Orchestrate Multiple Workflows

Use knowledge agents as intelligent orchestrators:

* Understand natural language requests
* Decide which workflow(s) to run
* Chain multiple workflows together
* Handle variations in user requests
* Iterate based on results

## When to Use Workflow Agents

Choose workflow agents when you need:

* **Automation** - Scheduled or triggered tasks that run unattended
* **Predictable processes** - Same steps every time, no variation needed
* **Backend tasks** - No user conversation required
* **Integration pipelines** - Connecting multiple systems
* **As tools** - Called by knowledge agents to do the actual work!

**The pattern:** Build workflow agents for specific tasks, then create knowledge agents that intelligently decide when to call them.

## How Knowledge Agents Work

Here's what happens when someone chats with your knowledge agent:

```
User makes a request in natural language
        ↓
Knowledge Agent analyzes the request
        ↓
Searches knowledge base for relevant context
        ↓
AI decides what action(s) to take
        ↓
Calls workflow agents / tools as needed
        ↓
Processes results and responds conversationally
        ↓
User can iterate and refine
```

This creates an intelligent interface layer over your automations.

## Key Capabilities

### 1. Knowledge Base

Train your agent with domain expertise:

* **Documents** - PDFs, docs, research papers
* **Web content** - Scrape websites and documentation
* **Videos** - YouTube transcripts automatically extracted
* **Social content** - Twitter/X threads, LinkedIn posts
* **Google Workspace** - Docs, Sheets, Drive files
* **Direct input** - Type or paste knowledge manually

The agent searches this knowledge to inform its responses and decisions.

### 2. Tool Integration - The Real Power

This is where knowledge agents become truly powerful:

**A. Workflow Agents as Tools**

* Add any of your existing workflow agents as tools
* Knowledge agent decides when to call them
* Pass data between conversation and workflow
* Chain multiple workflows together
* Example: "Research agent" → "Enrichment agent" → "Output agent"

**B. MCP (Model Context Protocol) Servers**

* Connect custom tools you build
* Advanced developer capability
* Extend agent capabilities infinitely

**C. Composio Integrations**

* 100+ app integrations (Slack, Gmail, HubSpot, etc.)
* Take real actions in external systems
* Authenticate once, agent uses as needed

### 3. Conversational Intelligence

Natural back-and-forth dialogue:

* **Context aware** - Remembers conversation history
* **Clarifying questions** - Asks when it needs more info
* **Multi-turn** - Complex requests over multiple messages
* **Adaptive** - Adjusts based on user feedback

### 4. System Configuration

Define how your agent behaves:

* **System instructions** - Guide personality and approach
* **Welcome message** - Set expectations for users
* **Sample questions** - Show what the agent can do
* **Prompt hints** - Guide user input

### 5. Conversation Management

* **Auto-titled** - AI generates conversation titles
* **Searchable history** - Find past conversations
* **Public sharing** - Share conversations via link
* **Forking** - Users can copy and continue shared chats

## Real-World Examples

### Personal Marketing Clone

**What it does:** Acts as your marketing expert, understanding strategy and executing tasks

**Configuration:**

* Knowledge: Your marketing playbooks, past campaigns, brand guidelines
* Tools:
  * "Competitor Research" workflow agent
  * "Content Generator" workflow agent
  * "Social Media Poster" workflow agent
  * HubSpot integration for CRM
* System prompt: "You are a marketing strategist. You understand our brand and can execute campaigns."

**Sample interaction:**

```
User: "Create a launch campaign for our new product feature"

Agent: "I'll help you create a comprehensive launch campaign.
Let me start by researching what competitors are doing...
[calls Competitor Research workflow]

Based on the competitive analysis, I recommend focusing on
[unique value props]. Should I draft the campaign content?"

User: "Yes, and schedule posts for next week"

Agent: "Great! [calls Content Generator workflow]
Here's the campaign content... [shows drafts]
[calls Social Media Poster workflow to schedule]
All set! 5 posts scheduled across LinkedIn and Twitter."
```

### Development Assistant

**What it does:** Understands your codebase and can run development workflows

**Configuration:**

* Knowledge: Your API docs, architecture decisions, coding standards
* Tools:
  * "Run Tests" workflow agent
  * "Deploy" workflow agent
  * "Create PR" workflow agent
  * GitHub integration
* System prompt: "You are a development assistant familiar with our codebase."

**Sample interaction:**

```
User: "I just pushed changes to the authentication module"

Agent: "Let me run the test suite to make sure everything passes...
[calls Run Tests workflow]

Tests passed! Ready to deploy to staging?"

User: "Yes, and create a PR for review"

Agent: [calls Deploy workflow for staging]
Deployed to staging ✓

[calls Create PR workflow]
PR created: #123 'Update authentication module'
Reviewers assigned based on CODEOWNERS.
```

### Research & Analysis Assistant

**What it does:** Conducts research and generates insights

**Configuration:**

* Knowledge: Your research methodology, data sources, analysis frameworks
* Tools:
  * "Web Scraper" workflow agent
  * "Data Analysis" workflow agent
  * "Report Generator" workflow agent
  * Google Sheets integration
* System prompt: "You conduct thorough research and generate actionable insights."

**Sample interaction:**

```
User: "Analyze the competitive landscape for AI agent platforms"

Agent: "I'll conduct comprehensive research. Let me start by
identifying key players... [calls Web Scraper workflow]

Found 15 competitors. Now analyzing their features and pricing...
[calls Data Analysis workflow]

Here are the key insights:
- [Insight 1]
- [Insight 2]

Should I generate a full report and save to Google Sheets?"
```

### Collaborative Content Creator

**What it does:** Works with you iteratively to create content

**Configuration:**

* Knowledge: Your brand voice, writing samples, content guidelines
* Tools:
  * "Content Generator" workflow agent
  * "SEO Optimizer" workflow agent
  * "Image Generator" workflow agent
  * Google Docs integration
* System prompt: "You help create high-quality content that matches our brand voice."

**Sample interaction:**

```
User: "I need a blog post about AI automation best practices"

Agent: "Great topic! Let me draft an outline based on our
content guidelines... [uses knowledge base]

Here's a proposed structure:
1. [Section 1]
2. [Section 2]
...

Does this flow work for you?"

User: "Perfect, write it and optimize for SEO"

Agent: [calls Content Generator workflow]
First draft complete! Now optimizing for SEO...
[calls SEO Optimizer workflow]

Added target keywords, meta description, and internal links.
Should I save this to Google Docs?
```

## Getting Started

Ready to build your powerful AI assistant?

<Card title="Quickstart Guide" icon="rocket" href="/knowledge-agents/quickstart">
  Build your first knowledge agent in under 10 minutes
</Card>

<CardGroup cols={2}>
  <Card title="Configure Your Agent" icon="sliders" href="/knowledge-agents/configuration">
    Set up system prompts, personality, and sample questions
  </Card>

  <Card title="Add Knowledge" icon="book" href="/knowledge-agents/knowledge-base">
    Train your agent with domain expertise
  </Card>

  <Card title="Enable Tools" icon="wrench" href="/knowledge-agents/tools-integration">
    Give your agent the power to take action
  </Card>

  <Card title="Best Practices" icon="star" href="/knowledge-agents/best-practices">
    Tips for creating effective knowledge agents
  </Card>
</CardGroup>

## Frequently Asked Questions

<AccordionGroup>
  <Accordion title="Do I need technical skills to build an knowledge agent?">
    No! Knowledge agents are built using a no-code interface. If you can configure settings and upload files, you can build an knowledge agent. The platform handles all the AI complexity behind the scenes.
  </Accordion>

  <Accordion title="How is this different from ChatGPT?">
    Knowledge agents give you:

    * **Custom knowledge** - Train on your specific domain
    * **Action capability** - Call workflows and integrations, not just answer questions
    * **Tool orchestration** - Intelligently chain multiple automations
    * **Controlled behavior** - Define personality and boundaries
    * **Shareable** - Public agents others can use
    * **Integrated** - Works with your Agent.AI workflows
  </Accordion>

  <Accordion title="What's the relationship between knowledge agents and workflow agents?">
    Think of workflow agents as the "hands" (they do specific tasks) and knowledge agents as the "brain" (they decide what to do and orchestrate the hands). Knowledge agents call workflow agents as tools to actually get work done.

    **Best practice:** Build focused workflow agents for specific tasks, then create knowledge agents that intelligently decide when to call them.
  </Accordion>

  <Accordion title="Can knowledge agents access the internet?">
    Only through tools you enable. You can add:

    * Web search tools
    * Workflow agents that call APIs
    * Integrations that access external services

    By default, they only know what's in their knowledge base.
  </Accordion>

  <Accordion title="Are knowledge agents always public?">
    No, but they're typically designed to be shared. You can:

    * Share publicly on the Agent.AI marketplace
    * Share specific conversation links
    * Keep completely private for your own use

    **Best practice:** Don't put sensitive/confidential information in public knowledge agents.
  </Accordion>

  <Accordion title="How do I make my knowledge agent actually DO things instead of just talking?">
    Add tools! Specifically:

    1. **Build workflow agents** for specific tasks (e.g., "send email", "create report")
    2. **Add them as tools** in the knowledge agent's Action Agents tab
    3. **Write good system prompts** that tell the agent when to use each tool
    4. The knowledge agent will call these workflows when appropriate

    See the [Tools Integration guide](/knowledge-agents/tools-integration) for details.
  </Accordion>

  <Accordion title="Can one knowledge agent call another knowledge agent?">
    Not directly, but you can create workflow agents that call knowledge agents via API, then have knowledge agents call those workflows. This creates powerful chains of AI reasoning and action.
  </Accordion>
</AccordionGroup>

<Note>
  **Pro Tip:** Start with a simple conversational agent, then gradually add workflow agents as tools. Test each tool individually before combining them. This iterative approach helps you build complex, powerful assistants reliably.
</Note>


# Knowledge Agent Quickstart
Source: https://docs.agent.ai/knowledge-agents/quickstart

Build your first action-taking knowledge agent in under 10 minutes

## What You'll Build

In this quickstart, you'll create a **Research Assistant** knowledge agent that can:

* Understand research requests in natural language
* Search its knowledge base for relevant information
* Call a workflow agent to gather additional data
* Present results conversationally

This will show you the core power of knowledge agents: combining knowledge with the ability to take action.

**Time required:** 10 minutes

## Prerequisites

Before you begin, make sure you have:

* An Agent.AI account (sign up at [agent.ai](https://agent.ai))
* Builder access enabled (click "Agent Builder" in the menu)
* At least one workflow agent created (or use one from the marketplace)

<Note>
  Don't have a workflow agent yet? That's okay! You can start with knowledge-only and add tools later. Or clone a simple workflow from the marketplace to use as a tool.
</Note>

## Step 1: Create Your Knowledge Agent

Navigate to the [Agent Builder](https://agent.ai/builder/agents) and click **"Create Agent"**.

In the modal that appears:

1. Select **"Knowledge Agent"** as the type (not workflow agent)
2. Give it a name: "Research Assistant"
3. Add a description: "Helps conduct research and gather insights"
4. Click **"Create"**

You'll be taken to the knowledge agent builder interface with 5 tabs across the top.

## Step 2: Configure Introduction Settings

You're now on the **Introduction** tab. This is where you define how your agent behaves and greets users.

### Welcome Message

In the "Welcome Message" field, enter:

```
Hi! I'm your Research Assistant. I can help you:
- Answer questions about topics in my knowledge base
- Gather additional research from the web
- Analyze information and provide insights

What would you like to research today?
```

### System Instructions

In the "System Instructions" field, enter:

```
You are a helpful research assistant. Your role is to:

1. Understand what the user wants to research
2. Search your knowledge base for relevant information
3. If needed, use the web research tool to gather additional data
4. Synthesize findings into clear, actionable insights
5. Ask clarifying questions when requests are ambiguous

Always cite your sources and be thorough in your research.
```

### Prompt Hint

In the "Prompt Hint" field (the placeholder text users see), enter:

```
Ask me to research a topic or company...
```

Click **"Save Introduction Details"** at the bottom.

<Check>
  **Checkpoint:** Your agent now has personality and clear expectations for users!
</Check>

## Step 3: Add Sample Questions

Click the **"Sample Questions"** tab at the top.

Add these example questions (one per line):

```
Research the latest trends in AI automation
Find information about sustainable energy companies
Analyze the competitive landscape for SaaS tools
Summarize key insights from recent tech news
```

These will appear as clickable suggestions when users first interact with your agent.

Click **"Update Sample Questions"**.

## Step 4: Add Knowledge to Your Agent

Click the **"Training"** tab at the top. You'll see sub-tabs for different knowledge sources.

### Option A: Upload a File (Easiest)

1. Click the **"Files"** sub-tab
2. Click **"Upload"** or drag and drop a PDF, Word doc, or text file
3. Wait for it to process (usually under 30 seconds)

Good test files to use:

* A whitepaper or research paper in your field
* Company documentation or product guides
* Meeting notes or reports

### Option B: Add a Web URL

1. Click the **"URLs"** sub-tab
2. Paste a URL (e.g., a blog post, documentation page, Wikipedia article)
3. Click **"Add URL"**
4. The content will be scraped and added to your knowledge base

### Option C: Add YouTube Video

1. Click the **"YouTube Videos"** sub-tab
2. Paste a YouTube URL
3. Click **"Add Video"**
4. The transcript will be extracted automatically

<Tip>
  Start with just ONE knowledge source for testing. You can always add more later!
</Tip>

## Step 5: Add a Workflow Agent as a Tool (Optional but Powerful)

This is where knowledge agents become truly powerful - giving them the ability to **take action**.

Click the **"Action Agents"** tab at the top.

You'll see a list of your workflow agents. Select one that makes sense for research:

**Good examples:**

* **Web Search** workflow - Searches the internet
* **Company Research** - Looks up company information
* **Data Analyzer** - Analyzes data you provide
* **Any workflow you've built** that does a specific task

Check the box next to the workflow agent(s) you want to enable.

Click **"Save Action Agents Selection"**.

<Note>
  If you don't have any workflow agents yet, skip this step for now. Your agent will still work using just its knowledge base. You can add tools later!
</Note>

<Check>
  **Checkpoint:** Your agent can now call workflow agents to accomplish tasks!
</Check>

## Step 6: Test Your Knowledge Agent

Time to see it in action!

### Start a Conversation

1. Look for the **chat interface** on the right side of your screen
2. You should see your welcome message and sample questions

### Test Knowledge Retrieval

Type a question related to the knowledge you added. For example:

* If you uploaded a research paper: "What were the main findings?"
* If you added a URL: "Summarize the key points from \[topic]"
* If you added a YouTube video: "What did they discuss about \[topic]?"

**What you should see:**

* The agent searches its knowledge base
* Responds with information from your uploaded content
* May show "\[file search]" indicator (if you're the builder)

### Test Tool Calling (if you added workflow agents)

Ask the agent to do something that requires the workflow:

* "Research the latest news about AI"
* "Find information about \[company name]"
* "Analyze \[some data or topic]"

**What you should see:**

* Agent recognizes it needs to use a tool
* Calls the appropriate workflow agent
* Shows "Calling \[workflow name]..."
* Processes the results
* Responds conversationally with the findings

<Warning>
  **If the agent doesn't call the workflow:** Make sure your system instructions mention the tool or task. Example: "Use the web search tool when you need current information."
</Warning>

## Step 7: Iterate and Improve

Based on your testing, you might want to:

### Refine System Instructions

Go back to the **Introduction** tab and adjust your system instructions to:

* Be more specific about when to use tools
* Define the tone and style you want
* Set boundaries ("Don't make things up if you don't know")

### Add More Knowledge

Go to the **Training** tab and add more documents, URLs, or videos to expand what your agent knows.

### Enable More Tools

Go to **Action Agents** and add more workflow agents for different capabilities.

### Adjust Sample Questions

Update the **Sample Questions** to better reflect what users should ask.

## What You've Built

Congratulations! You now have a working knowledge agent that:

 Greets users with a custom welcome message
 Has a defined personality and role
 Searches a custom knowledge base to answer questions
 Can call workflow agents to take actions
 Engages in natural, multi-turn conversations

## Next Steps

Now that you have a basic knowledge agent, here's how to make it even more powerful:

<CardGroup cols={2}>
  <Card title="Deep Dive: Configuration" icon="sliders" href="/knowledge-agents/configuration">
    Learn advanced system prompt techniques and personality configuration
  </Card>

  <Card title="Master the Knowledge Base" icon="book" href="/knowledge-agents/knowledge-base">
    Add all types of knowledge sources and optimize for better retrieval
  </Card>

  <Card title="Add More Tools" icon="wrench" href="/knowledge-agents/tools-integration">
    Enable MCP servers and Composio integrations for even more capabilities
  </Card>

  <Card title="Share Your Agent" icon="share-nodes" href="/knowledge-agents/conversations">
    Learn how to share conversations and make your agent public
  </Card>
</CardGroup>

## Common Issues & Solutions

<AccordionGroup>
  <Accordion title="My agent isn't using the knowledge I uploaded">
    **Possible causes:**

    * File still processing (check Training tab for status)
    * Question doesn't match knowledge content
    * Knowledge base search not finding relevant chunks

    **Solutions:**

    * Wait for file to finish processing
    * Ask questions more directly related to your content
    * Try uploading different/better formatted content
    * Check the Training tab - is the document listed?
  </Accordion>

  <Accordion title="The agent isn't calling my workflow agent">
    **Possible causes:**

    * Workflow agent not properly enabled in Action Agents tab
    * System instructions don't mention using tools
    * Agent doesn't think the tool is relevant to the request

    **Solutions:**

    * Confirm workflow is checked in Action Agents tab
    * Update system instructions to explicitly mention when to use the tool
    * Ask more directly: "Use \[workflow name] to research..."
    * Make sure your workflow agent has a clear name/description
  </Accordion>

  <Accordion title="I can't find the chat interface">
    **Solution:** The chat interface should appear on the right side of the builder. If you don't see it:

    * Make sure you're viewing an Knowledge Agent (not Workflow Agent)
    * Try refreshing the page
    * Check that you're in the builder view, not settings
  </Accordion>

  <Accordion title="Changes I made aren't showing up">
    **Solution:** Make sure you clicked the "Save" button for each section:

    * "Save Introduction Details" for Introduction tab
    * "Update Sample Questions" for Sample Questions tab
    * "Save Action Agents Selection" for Action Agents tab

    If you saved and still don't see changes, start a new conversation in the chat.
  </Accordion>

  <Accordion title="How do I start a new test conversation?">
    Look for the "New Agent Run" or "+ New Chat" button in the chat interface, usually at the top of the conversation area.
  </Accordion>
</AccordionGroup>

## Pro Tips

<Tip>
  **Tip 1: Test Early, Test Often**
  Don't wait until you've configured everything to test. Add one piece at a time and test after each change. This helps you understand what each piece does.
</Tip>

<Tip>
  **Tip 2: Start Simple, Add Complexity**
  Begin with just knowledge and a simple system prompt. Once that works, add one tool. Test again. Then add more. This iterative approach prevents overwhelming yourself.
</Tip>

<Tip>
  **Tip 3: Be Specific in System Instructions**
  Instead of "You are helpful," try "You help users research companies by first searching your knowledge base, then using the web research tool if needed, and presenting findings in bullet points."
</Tip>

<Tip>
  **Tip 4: Use Sample Questions to Guide Users**
  Your sample questions train users on what your agent can do. Make them specific and actionable, like examples you want users to follow.
</Tip>

<Tip>
  **Tip 5: Name Tools Clearly**
  If you're enabling workflow agents, make sure they have descriptive names like "Web Search Tool" or "Company Research Agent" so the AI knows when to use them.
</Tip>

## You're Ready!

You've built your first knowledge agent and seen how it combines conversational AI with knowledge and action. The pattern is the same for any knowledge agent you build:

1. Define personality (system instructions)
2. Add knowledge (training)
3. Enable tools (action agents, MCP, integrations)
4. Test and iterate

Now go build something amazing!


# Tools & Integration
Source: https://docs.agent.ai/knowledge-agents/tools-integration

Give your knowledge agent the power to take action with workflow agents, MCP servers, and app integrations

## Overview

This is where knowledge agents become **truly powerful**. While knowledge lets your agent understand and answer questions, tools let it **actually do things**.

Knowledge agents can orchestrate three types of tools:

| Tool Type                 | What It Does                                    | Best For                        |
| ------------------------- | ----------------------------------------------- | ------------------------------- |
| **Workflow Agents**       | Call your existing Agent.AI workflow agents     | Custom automations you've built |
| **MCP Servers**           | Connect custom tools via Model Context Protocol | Advanced/developer capabilities |
| **Composio Integrations** | Take actions in 100+ external apps              | Slack, Gmail, HubSpot, etc.     |

**The key concept:** Your knowledge agent intelligently decides when to use each tool based on the conversation context. You just enable the tools and write good system prompts that guide when to use them.

## How Function Calling Works

When you enable tools for your knowledge agent, here's what happens:

```
User: "Research Acme Corp and add them to HubSpot"
        ↓
Knowledge Agent analyzes the request
        ↓
Recognizes it needs two tools: research + CRM
        ↓
Calls "Company Research" workflow agent
        ↓
Gets company data back
        ↓
Calls HubSpot integration to create contact
        ↓
Responds: "Done! I found Acme Corp, researched them,
and created a contact in HubSpot with [details]."
```

**Important:** The AI decides which tools to call and in what order. You guide this through:

* System instructions that explain when to use each tool
* Clear tool names and descriptions
* Good conversation design

## Workflow Agents as Tools

This is the most common and powerful integration. Your knowledge agent can call any of your workflow agents to accomplish tasks.

### How It Works

**Workflow agents** are your deterministic automations (step-by-step processes). **Knowledge agents** are conversational and decide when to invoke those automations.

Think of it like:

* **Workflow agents** = Specialized workers (do one thing really well)
* **Knowledge agents** = Manager (decides who to call for what task)

### Adding Workflow Agents

1. Navigate to your knowledge agent builder
2. Click the **"Action Agents"** tab
3. You'll see a list of all your workflow agents
4. Check the box next to each workflow you want to enable
5. Click **"Save Action Agents Selection"**

That's it! Your knowledge agent can now call those workflows.

<Tip>
  **Start with 2-3 workflows maximum** when testing. Add more once you've verified each one works individually.
</Tip>

### Making Your Knowledge Agent Use Workflows

Just enabling a workflow doesn't mean your knowledge agent will use it. You need to guide the AI through **system instructions**.

#### Good System Instructions for Workflow Tools

```
You are a marketing assistant with access to several workflows:

- Use the "Competitor Research" workflow when users ask about competitors
- Use the "Content Generator" workflow to create marketing content
- Use the "Social Media Poster" workflow to schedule or publish posts

When a user asks you to research competitors:
1. Call the Competitor Research workflow with the company names
2. Analyze the results
3. Present findings in bullet points
4. Ask if they want you to create content based on the research

When creating content:
1. Ask clarifying questions about audience and goals
2. Use the Content Generator workflow
3. Show the user the draft
4. Get approval before using Social Media Poster workflow

Never post publicly without explicit user approval.
```

<Warning>
  **Bad example:** "You have workflows available to help users."

  This is too vague. The AI won't know when to use what.
</Warning>

#### Naming Your Workflow Agents

Make sure your workflow agents have clear, descriptive names:

**Good names:**

* "Company Research Tool"
* "Email Sender"
* "Data Analyzer"
* "LinkedIn Profile Enricher"

**Bad names:**

* "Agent 1"
* "My Workflow"
* "Test"
* "Automation"

The name is part of the AI's decision-making process!

### Passing Data Between Expert and Workflow Agents

When your knowledge agent calls a workflow, it can:

**Send data to the workflow:**

* User input from the conversation
* Data retrieved from knowledge base
* Results from previous tool calls

**Receive data from the workflow:**

* Workflow outputs
* Structured data
* Generated content
* Status/error messages

The knowledge agent then uses this data to continue the conversation naturally.

### Example: Research Assistant with Multiple Workflows

**Enabled workflows:**

* "Web Search" - Searches the internet
* "Company Enrichment" - Gets company details
* "Create Google Doc" - Saves to Google Docs

**System instructions:**

```
You are a research assistant that helps users conduct thorough research.

When users ask you to research companies:
1. Use the "Web Search" workflow to find recent news and information
2. Use the "Company Enrichment" workflow to get detailed company data
3. Synthesize findings from both sources
4. If the user wants to save the research, use "Create Google Doc" workflow

Always cite your sources and ask before saving documents.
```

**Sample conversation:**

```
User: "Research TechCorp and competitors"

Agent: "I'll research TechCorp and their competitive landscape.
[Calls Web Search workflow with query: "TechCorp news competitors"]
[Calls Company Enrichment workflow with company: "TechCorp"]

Based on my research:

TechCorp:
- Revenue: $50M, 200 employees
- Recent news: Just raised Series B
- Main product: Enterprise SaaS

Top 3 Competitors:
- CompanyA: Similar product, larger scale
- CompanyB: Newer, focused on SMB
- CompanyC: Premium positioning

Would you like me to save this to a Google Doc?"

User: "Yes please"

Agent: [Calls Create Google Doc workflow]
Done! Research saved to 'TechCorp Analysis' in your Google Drive.
```

## MCP (Model Context Protocol) Servers

MCP is an advanced feature for developers who want to build custom tools for their knowledge agents.

### What is MCP?

**Model Context Protocol** is an open standard for connecting AI agents to external tools and data sources. It allows you to:

* Build custom tools in any programming language
* Connect to proprietary systems
* Extend agent capabilities beyond built-in features
* Share tools across different agents

### When to Use MCP

Use MCP servers when:

* You need custom functionality not available in workflow agents or integrations
* You're connecting to proprietary internal systems
* You want fine-grained control over tool behavior
* You're comfortable with development/technical setup

### Setting Up MCP Servers

<Note>
  **Technical knowledge required:** Setting up MCP servers requires development experience. Most users should start with workflow agents and Composio integrations.
</Note>

**High-level process:**

1. **Build your MCP server** following the [MCP specification](https://docs.agent.ai/mcp-server)
2. **Deploy it** somewhere your knowledge agent can access
3. **Register it** with your knowledge agent:
   * Go to knowledge agent settings
   * Navigate to MCP configuration
   * Add your server URL and authentication
4. **Reference it in system instructions** so the agent knows when to use it

**Example MCP server use case:**

```
You built an internal company database search tool as an MCP server.
Your knowledge agent can now search your proprietary data by calling this MCP tool.
```

### MCP vs Workflow Agents

| Aspect           | Workflow Agents         | MCP Servers                |
| ---------------- | ----------------------- | -------------------------- |
| Setup difficulty | Easy (no-code)          | Advanced (coding required) |
| Best for         | Business automations    | Custom technical tools     |
| Visibility       | Visual workflow builder | Code-based                 |
| Sharing          | Clone in platform       | Deploy infrastructure      |

**Recommendation:** Start with workflow agents. Only use MCP if you have specific technical requirements.

## Composio Integrations

Composio provides 100+ pre-built integrations with popular apps and services. This lets your knowledge agent take actions in external systems.

### Available Integrations

**Communication:**

* Slack - Send messages, create channels
* Gmail - Send emails, read inbox
* Discord - Post messages, manage servers

**CRM & Sales:**

* HubSpot - Create contacts, deals, notes
* Salesforce - Update records, search data
* Pipedrive - Manage pipeline

**Productivity:**

* Google Drive - Create/read documents
* Notion - Update databases, create pages
* Asana - Create/update tasks

**And 90+ more integrations** across categories like marketing, development, data, and analytics.

### Setting Up Composio Integrations

1. **Navigate to your knowledge agent builder**
2. Click the **"Integrations"** tab (or "Composio" tab)
3. **Browse available integrations**
4. Click on an integration you want to enable
5. **Authenticate** - Connect your account (OAuth flow)
6. **Configure permissions** - Choose what the agent can access
7. **Save the integration**

Now your knowledge agent can call that service!

### Guiding Your Agent to Use Integrations

Like with workflow agents, you need to tell your knowledge agent when to use integrations via system instructions.

#### Example: Slack Integration

**System instructions:**

```
You are a team communication assistant with access to Slack.

When users ask you to notify the team or send a message:
1. Ask which channel (if they didn't specify)
2. Confirm the message content
3. Use the Slack integration to send the message
4. Confirm it was sent

Always get approval before sending messages to public channels.
```

**Conversation:**

```
User: "Let the engineering team know the API is ready"

Agent: "I'll send a message to the engineering team on Slack.
Should I post in #engineering-general or a different channel?"

User: "#engineering-general"

Agent: "I'll send this message to #engineering-general:
'The API is ready for testing and integration.'

Should I send it?"

User: "Yes"

Agent: [Calls Slack integration]
Message sent to #engineering-general ✓
```

### Security Best Practices

<Warning>
  **Important:** Integrations have real access to your accounts. Be careful with public knowledge agents.

  * Don't share agents that have sensitive integrations
  * Review what permissions each integration needs
  * Add confirmation steps for destructive actions
  * Consider separate accounts for agent integrations
</Warning>

**Safe system instruction pattern:**

```
Before taking any action that:
- Sends messages/emails to others
- Creates/modifies records
- Posts publicly
- Deletes anything

Always ask the user to confirm explicitly.
```

## Combining Multiple Tools

The real power comes from knowledge agents orchestrating multiple tools together.

### Example: End-to-End Sales Research Agent

**Enabled tools:**

* "Company Research" workflow agent
* "LinkedIn Profile Enrichment" workflow agent
* HubSpot integration (Composio)
* Gmail integration (Composio)

**System instructions:**

```
You are a sales research assistant that helps research prospects
and add them to our CRM.

Your workflow:
1. When given a company name, use Company Research workflow
2. Identify key decision-makers
3. Use LinkedIn Profile Enrichment workflow for each person
4. Create contacts in HubSpot with all enriched data
5. Ask if user wants you to draft outreach emails
6. If yes, draft personalized emails using research insights
7. Send via Gmail integration (only after approval)

Always research thoroughly before taking CRM or email actions.
```

**Sample interaction:**

```
User: "Research Acme Corp and add decision-makers to HubSpot"

Agent: "I'll research Acme Corp for you.
[Calls Company Research workflow]

Found Acme Corp:
- Industry: Enterprise SaaS
- Size: 500 employees
- Key decision-makers identified: CEO, CTO, VP Sales

Let me enrich their LinkedIn profiles...
[Calls LinkedIn enrichment for each person]

Great! I have complete profiles for:
1. Jane Doe - CEO
2. John Smith - CTO
3. Sarah Johnson - VP Sales

Should I create these contacts in HubSpot?"

User: "Yes, and draft outreach emails"

Agent: [Calls HubSpot integration to create 3 contacts]
✓ Created 3 contacts in HubSpot

Now drafting personalized outreach emails based on their backgrounds...

[Shows 3 email drafts using research insights]

Ready to send via Gmail. Should I send all three?"

User: "Send only the CEO email for now"

Agent: [Calls Gmail integration]
✓ Email sent to Jane Doe (CEO of Acme Corp)

I've also added notes to her HubSpot record that we sent initial outreach.
```

### Multi-Tool Orchestration Best Practices

**Do:**

* Let the agent decide the order of tool calls
* Build confirmation steps for sensitive actions
* Chain related tools logically (research → enrich → save)
* Use results from one tool to inform the next

**Don't:**

* Try to hard-code exact sequences (let AI adapt)
* Enable too many tools at once (start with 3-5)
* Skip confirmation on actions like sending emails
* Forget to handle errors gracefully

## Troubleshooting Tools

<AccordionGroup>
  <Accordion title="Knowledge agent isn't calling my workflow">
    **Symptoms:** Agent responds conversationally but doesn't invoke the workflow

    **Possible causes:**

    1. Workflow not enabled in Action Agents tab
    2. System instructions don't mention when to use it
    3. Workflow name is unclear
    4. Agent doesn't think it's relevant to the request

    **Solutions:**

    * Verify workflow is checked in Action Agents tab
    * Add explicit instructions: "Use \[workflow name] when users ask to \[task]"
    * Rename workflow to be more descriptive
    * Ask more directly: "Use the \[workflow name] to research..."
    * Test workflow independently to ensure it works
  </Accordion>

  <Accordion title="Workflow keeps failing or returning errors">
    **Symptoms:** Agent calls the workflow but gets errors

    **Possible causes:**

    1. Workflow itself has a bug
    2. Knowledge agent passing wrong data format
    3. Workflow expecting different inputs

    **Solutions:**

    * Test the workflow agent independently (run it directly)
    * Check workflow input requirements
    * Review what data the knowledge agent is passing
    * Update system instructions to format data correctly
    * Add error handling to the workflow
  </Accordion>

  <Accordion title="Agent calls the wrong tool">
    **Symptoms:** Agent uses Tool A when Tool B would be better

    **Possible causes:**

    1. Tool names/descriptions are ambiguous
    2. System instructions unclear about when to use what
    3. User request was vague

    **Solutions:**

    * Make tool names more specific and distinct
    * Add clear boundaries in system instructions:
      "Use Tool A for \[specific case]. Use Tool B for \[different case]."
    * Test with specific requests that clearly need one tool
    * Reduce number of similar tools enabled
  </Accordion>

  <Accordion title="Composio integration authentication failed">
    **Symptoms:** Can't connect or authenticate with external service

    **Possible causes:**

    1. OAuth flow expired or interrupted
    2. Wrong permissions requested
    3. Service credentials changed
    4. Rate limits exceeded

    **Solutions:**

    * Re-authenticate the integration (disconnect and reconnect)
    * Check service status (is the external service down?)
    * Review required permissions for the integration
    * Wait if rate limited, then try again
    * Contact support if integration consistently fails
  </Accordion>

  <Accordion title="Agent calls too many tools for simple requests">
    **Symptoms:** Agent over-engineers simple tasks by calling multiple tools

    **Possible causes:**

    1. System instructions encourage thoroughness without boundaries
    2. Agent trying to be helpful but overdoing it

    **Solutions:**

    * Add efficiency guidelines to system instructions:
      "Use the minimum number of tools needed to complete the task"
    * Specify when NOT to use certain tools
    * Test with simple requests and iterate on prompts
    * Consider if you enabled too many overlapping tools
  </Accordion>

  <Accordion title="How do I know which tool was called?">
    **Answer:** As the builder testing your agent:

    * Look for "\[Calling workflow name...]" messages
    * Watch for integration loading states
    * Check agent response for explicit mentions

    For end users, the visibility depends on your UX preferences. You can:

    * Configure system instructions to announce tool usage
    * Have agent explain what it's doing
    * Keep tool calls invisible for seamless experience

    Example system instruction:
    "When you call a tool, tell the user: 'Let me use \[tool name] to \[accomplish task]...'"
  </Accordion>
</AccordionGroup>

## Advanced: Tool Call Patterns

### The Research-Execute Pattern

```
System instructions:
"Always research before executing actions.
1. Gather information using research tools
2. Present findings to user
3. Get approval
4. Execute action using integration tools
5. Confirm completion"
```

**Good for:** Sales outreach, content creation, CRM management

### The Pipeline Pattern

```
System instructions:
"Process requests through a pipeline:
1. Input validation
2. Data enrichment
3. Transformation
4. Storage/output
5. Notification

Use [Tool A] for step 2, [Tool B] for step 3, [Tool C] for step 4."
```

**Good for:** Data processing, lead enrichment, report generation

### The Approval-Gate Pattern

```
System instructions:
"For sensitive operations:
1. Explain what you're about to do
2. Show exactly what data will be used
3. Wait for explicit user approval
4. Execute only after confirmation
5. Confirm completion with details

Sensitive operations include: sending emails, posting publicly,
creating CRM records, making purchases."
```

**Good for:** Public-facing agents, agents with write permissions

### The Fallback Pattern

```
System instructions:
"Try tools in order of preference:
1. First, try [Primary Tool]
2. If that fails or isn't available, try [Secondary Tool]
3. If all tools fail, explain to user and suggest manual approach

Always try your tools before saying you can't do something."
```

**Good for:** Resilient agents, agents with redundant capabilities

## Testing Your Tools

After enabling tools, thoroughly test:

### 1. Individual Tool Testing

Test each tool separately:

* "Use \[workflow name] to research Microsoft"
* "Send a test message to #test-channel on Slack"
* "Create a test contact in HubSpot"

**Verify:**

* Tool is called correctly
* Data is passed properly
* Results come back as expected
* Errors are handled gracefully

### 2. Multi-Tool Sequences

Test tool combinations:

* "Research Company X and add them to HubSpot"
* "Analyze this data and save results to Google Sheets"
* "Find recent news and post summary to Slack"

**Verify:**

* Tools are called in logical order
* Data flows between tools correctly
* User gets progress updates
* Final result is complete

### 3. Edge Cases

Test failure scenarios:

* What happens if a workflow fails?
* What if an integration is disconnected?
* What if the user provides incomplete information?

**Verify:**

* Graceful error messages
* Agent asks clarifying questions
* Doesn't get stuck in loops
* Offers alternatives

### 4. Approval Workflows

Test confirmation flows:

* Does agent ask before sensitive actions?
* Can user say "no" and agent respects it?
* Does agent re-confirm if request changes?

## Best Practices Summary

<Card title="Tool Integration Best Practices" icon="star">
  **DO:**

  * Start with 2-3 tools and add more gradually
  * Write explicit system instructions for each tool
  * Use clear, descriptive tool names
  * Test each tool individually before combining
  * Add confirmation steps for sensitive actions
  * Let the AI decide when to use tools (don't hard-code)

  **DON'T:**

  * Enable every tool at once
  * Assume the AI knows when to use tools without guidance
  * Skip testing multi-tool scenarios
  * Give public agents access to sensitive integrations
  * Forget to handle errors and edge cases
</Card>

## Next Steps

Now that you understand how to give your knowledge agent powerful action-taking capabilities:

<CardGroup cols={2}>
  <Card title="Manage Conversations" icon="messages" href="/knowledge-agents/conversations">
    Learn about conversation management, sharing, and user experience
  </Card>

  <Card title="Best Practices" icon="star" href="/knowledge-agents/best-practices">
    Advanced techniques for building exceptional knowledge agents
  </Card>

  <Card title="Troubleshooting" icon="triangle-exclamation" href="/knowledge-agents/troubleshooting">
    Solve common issues and optimize performance
  </Card>

  <Card title="Build Workflow Agents" icon="diagram-project" href="/builder/overview">
    Create the workflow agents your knowledge agent will call
  </Card>
</CardGroup>

<Note>
  **Remember:** Tools transform your knowledge agent from a conversational assistant into a powerful automation orchestrator. Start simple, test thoroughly, and gradually build up to complex multi-tool workflows.
</Note>


# Troubleshooting
Source: https://docs.agent.ai/knowledge-agents/troubleshooting

Diagnose and fix common issues with your knowledge agents

## Diagnostic Workflow

When your knowledge agent isn't working as expected, follow this systematic approach:

```
1. Identify the symptom
   ↓
2. Isolate the component
   (Configuration? Knowledge? Tools? Conversation?)
   ↓
3. Test in isolation
   (Test just that component)
   ↓
4. Check the basics
   (Is it enabled? Saved? Loaded?)
   ↓
5. Review recent changes
   (What was modified last?)
   ↓
6. Apply fix
   ↓
7. Verify fix works
```

## Quick Diagnostic Checklist

Before diving deep, check these common issues:

```
✓ Did you click "Save" after making changes?
✓ Did you start a new conversation to test changes?
✓ Are all files finished processing?
✓ Are all tools/integrations still connected?
✓ Is the agent set to public/private correctly?
✓ Did you test with a clear, specific request?
✓ Is your internet connection stable?
```

**80% of issues** come from forgetting to save or not starting a fresh conversation.

## Configuration Issues

### Agent Not Responding or Acting Generically

**Symptoms:**

* Agent gives generic chatbot responses
* Ignores system instructions
* Doesn't use its personality

**Possible Causes:**

1. System instructions not saved
2. Testing in old conversation (has cached behavior)
3. System instructions too vague
4. Conflicting instructions

**How to Fix:**

**Step 1: Verify save**

```
1. Go to Introduction tab
2. Check your system instructions are there
3. Click "Save Introduction Details" again
4. Wait for confirmation message
```

**Step 2: Test fresh**

```
1. Start a brand new conversation
2. Test with a sample question
3. Check if behavior changed
```

**Step 3: Simplify to test**

```
Temporarily replace system instructions with:

"You are a test agent. When users say hello, respond
with 'SYSTEM INSTRUCTIONS WORKING' in all caps."

Save, start new conversation, say "hello"
- If you get the response → System instructions work, original prompt was the issue
- If you don't → Deeper technical issue
```

**Step 4: Review prompt quality**

* Are instructions specific enough?
* Any contradictions?
* See [Configuration guide](/knowledge-agents/configuration) for writing better prompts

### Welcome Message or Sample Questions Not Showing

**Symptoms:**

* Old welcome message appears
* Sample questions missing or outdated

**Possible Causes:**

1. Changes not saved
2. Cached in browser
3. Testing in existing conversation

**How to Fix:**

```
1. Verify changes saved:
   - Go to Introduction / Sample Questions tab
   - Confirm your text is there
   - Click save again

2. Clear browser cache:
   - Refresh page (Cmd+Shift+R or Ctrl+Shift+R)
   - Or clear browser cache completely

3. Start new conversation:
   - Don't reuse old conversation
   - Click "New Chat" or equivalent
   - Welcome message should update
```

### Agent Ignoring Boundaries or Prompt Filtering

**Symptoms:**

* Agent responds to off-topic requests
* Doesn't follow content guidelines
* Hallucinating information

**Possible Causes:**

1. Boundary instructions too soft
2. Conflicting instructions (be helpful vs. stay on topic)
3. AI interpreting edge cases differently than expected

**How to Fix:**

**Strengthen boundaries:**

```
Don't:
"Try to stay on topic about [domain]."

Do:
"ONLY respond to questions about [domain].

If users ask about anything else, respond exactly:
'I specialize in [domain]. I can't help with [their topic].
For general questions, try [alternative].'

Topics outside scope:
- [Topic 1]
- [Topic 2]
- [Topic 3]"
```

**Add explicit do-not-hallucinate instructions:**

```
"Accuracy rules:
- NEVER make up information
- If you don't know, say: 'I don't have that information'
- Only use data from knowledge base or tool results
- When uncertain, acknowledge uncertainty explicitly"
```

## Knowledge Base Issues

### Agent Says "I Don't Have Information" About Uploaded Content

**Symptoms:**

* You uploaded knowledge but agent doesn't use it
* Agent says it doesn't know things clearly in your documents

**Possible Causes:**

1. File still processing
2. File failed to process
3. Search query doesn't match content semantically
4. Too much noise in knowledge base

**Diagnostic Steps:**

**Step 1: Check processing status**

```
1. Go to Training tab
2. Look at uploaded files
3. Check for:
   - Processing spinner (still working)
   -  Checkmark (successfully processed)
   -  Error icon (failed)

If stuck processing >5 minutes → refresh page or re-upload
If error → file may be corrupted or unsupported format
```

**Step 2: Test knowledge directly**

```
Ask: "What files are in your knowledge base?"
Or: "What do you know about [exact topic from your doc]?"

If agent doesn't mention your file → not successfully added
If it does mention it but retrieves wrong info → retrieval issue
```

**Step 3: Improve retrieval**

```
Problem: Content isn't semantically matching

Solutions:
1. Restructure document with clear headings
2. Remove boilerplate/noise
3. Break large docs into focused pieces
4. Use descriptive file names
5. Add metadata headers

Example:
Instead of: "Document.pdf"
Use: "[POLICY] Customer Refund Policy - Updated 2024.pdf"
```

**Step 4: Check knowledge base size**

```
If you have 100+ documents:
- Too much content can dilute retrieval
- Remove less relevant docs
- Focus on highest quality sources
```

### Knowledge Retrieval is Slow

**Symptoms:**

* Long delays before agent responds
* Timeout errors

**Possible Causes:**

1. Knowledge base too large
2. Files are very large (many MB each)
3. Too many sources

**How to Fix:**

```
1. Audit knowledge base:
   - How many files? (>100 is a lot)
   - File sizes? (>10MB each is large)
   - Duplicate content?

2. Optimize:
   - Remove duplicates
   - Delete least-used sources
   - Split large files into smaller focused docs
   - Keep total under 50-75 high-quality sources

3. If must keep large knowledge base:
   - Consider multiple specialized agents instead of one
   - Use more targeted search prompts
```

### Wrong Knowledge Retrieved

**Symptoms:**

* Agent cites sources but they're not relevant
* Retrieves outdated version of information

**Possible Causes:**

1. Multiple conflicting sources
2. Poor document structure
3. Outdated content not removed

**How to Fix:**

```
1. Check for conflicts:
   - Do you have multiple docs on same topic?
   - Contradictory information?
   → Keep only most authoritative/current version

2. Improve structure:
   - Add clear section headers
   - Use bullet points and lists
   - Separate topics clearly

3. Remove outdated:
   - Delete old versions
   - Update changed information
   - Refresh URL-based knowledge
```

## Tool Integration Issues

### Workflow Agent Not Being Called

**Symptoms:**

* Agent talks about the task but doesn't call the workflow
* Responds conversationally instead of taking action

**Diagnostic Steps:**

**Step 1: Verify enabled**

```
1. Go to Action Agents tab
2. Is the workflow checked?
3. Click "Save Action Agents Selection"
4. Start new conversation
```

**Step 2: Test directly**

```
Ask: "Use [exact workflow name] to [task]"

If called → Agent CAN use it, just doesn't know when
If not called → Configuration or connection issue
```

**Step 3: Check system instructions**

```
Do your system instructions mention the workflow?

Add:
"When users ask to [task], use the '[Workflow Name]' workflow.
Example: User says 'research Company X' → call 'Company Research' workflow"
```

**Step 4: Verify workflow name clarity**

```
Bad name: "Agent 1", "My Workflow"
Good name: "Company Research Tool", "Email Sender"

Rename workflow to be more descriptive
```

**Step 5: Test workflow independently**

```
1. Go to the workflow agent itself
2. Run it manually
3. Does it complete successfully?

If workflow is broken, knowledge agent can't call it
```

### Workflow Returns Errors

**Symptoms:**

* Agent calls workflow but gets error response
* "Tool failed" messages

**How to Fix:**

```
1. Test workflow independently:
   - Run the workflow agent by itself
   - Does it work outside knowledge agent?
   - If no → fix the workflow first

2. Check data being passed:
   - What data is knowledge agent sending to workflow?
   - Does it match workflow's expected inputs?
   - Update system instructions to format data correctly

3. Check workflow requirements:
   - Does workflow need authentication?
   - API keys configured?
   - Rate limits hit?

4. Add error handling:
   System instructions:
   "If [Workflow Name] fails:
   1. Tell user what happened
   2. Offer alternative approach
   3. Don't keep retrying blindly"
```

### Composio Integration Not Working

**Symptoms:**

* "Authentication failed" errors
* Integration shows disconnected
* Actions don't execute

**How to Fix:**

**Step 1: Re-authenticate**

```
1. Go to Integrations tab
2. Find the integration
3. Click "Disconnect"
4. Click "Connect" again
5. Complete OAuth flow
6. Verify "Connected" status
```

**Step 2: Check permissions**

```
1. During OAuth, did you grant all needed permissions?
2. Some integrations need specific scopes
3. Re-connect and ensure all permissions granted
```

**Step 3: Test integration directly**

```
Ask agent: "Use [Integration] to [simple action]"
Example: "Use Slack to send a test message to #test"

If simple action works → complex use case is the issue
If simple action fails → integration configuration problem
```

**Step 4: Check service status**

```
Is the external service down?
- Check service status page (e.g., status.slack.com)
- Try accessing service directly in browser
- Wait and retry if service is down
```

### MCP Server Not Connecting

**Symptoms:**

* MCP tools not available
* Connection errors

**How to Fix:**

```
1. Verify server is running:
   - Check server endpoint is accessible
   - Test server health endpoint
   - Review server logs

2. Check configuration:
   - Correct server URL?
   - Authentication credentials correct?
   - Network access allowed?

3. Review MCP server implementation:
   - Following MCP specification?
   - See [MCP Server docs](/mcp-server)

4. Test with minimal MCP server:
   - Create simple "hello world" MCP server
   - If that works → your custom server has issues
   - If that fails → MCP configuration in agent is wrong
```

## Conversation & Chat Issues

### Conversations Not Saving

**Symptoms:**

* Conversation history disappears
* Can't find past conversations

**Possible Causes:**

1. Not logged in (guest mode)
2. Browser privacy mode
3. Cookies/storage disabled

**How to Fix:**

```
1. Verify logged in:
   - Check if you see your account name
   - If not, sign in
   - Try conversation again

2. Check browser settings:
   - Not in incognito/private mode?
   - Cookies enabled?
   - Local storage enabled?

3. Try different browser:
   - Test in Chrome/Firefox/Safari
   - If works in one browser → original browser settings issue
```

### Agent Losing Context Mid-Conversation

**Symptoms:**

* Agent forgets what was discussed earlier
* Doesn't remember previous tool results

**Possible Causes:**

1. Conversation too long (token limit)
2. Technical glitch

**How to Fix:**

```
1. Start new conversation:
   - Very long conversations (20+ turns) may hit limits
   - Fork or start fresh
   - Summarize what you need agent to remember

2. Keep conversations focused:
   - Don't jump between unrelated topics
   - One main task per conversation
   - Start new conversation for new topics

3. If happens in short conversations:
   - Report to support (this shouldn't happen)
   - Include conversation link
```

### Shared Conversation Link Not Working

**Symptoms:**

* "Not found" or error when opening shared link
* Link shows different content

**How to Fix:**

```
1. Verify link is complete:
   - Full URL including https://
   - No characters cut off
   - Copy link again fresh

2. Check conversation still exists:
   - Did you delete it?
   - Is agent still public?
   - Log in and view in your history

3. Check agent visibility:
   - Is knowledge agent set to public?
   - Private agents can't have public shared conversations
```

### Can't Start New Conversation

**Symptoms:**

* "New Chat" button not working
* Stuck in existing conversation

**How to Fix:**

```
1. Refresh page (Cmd+R or Ctrl+R)

2. Clear browser cache

3. Log out and log back in

4. Try different browser

5. If persists → technical issue, contact support
```

## Performance Issues

### Agent Responses Are Slow

**Symptoms:**

* Long wait times (>30 seconds) for responses
* Timeouts

**Diagnostic:**

```
Identify bottleneck:

1. Simple question, no tools/knowledge:
   - "Hello, how are you?"
   - Should be <3 seconds
   - If slow → platform performance issue

2. Knowledge retrieval:
   - Ask about knowledge base content
   - Should be 3-8 seconds
   - If slow → knowledge base too large

3. Tool calling:
   - Ask to use workflow
   - Timing = workflow execution time + overhead
   - If slow → workflow is slow or tool issue

4. Multiple tools:
   - Complex request with 3+ tools
   - Can take 30-60+ seconds (normal)
   - If >2 minutes → investigate individual tools
```

**Fixes Based on Bottleneck:**

```
If knowledge base is slow:
- Reduce number of documents
- Remove large files
- Optimize document structure

If tools are slow:
- Optimize workflow agents (see workflow docs)
- Use faster integrations
- Reduce number of sequential tool calls

If platform is slow:
- Check status page
- Try during off-peak hours
- Report persistent issues to support
```

### Agent Making Too Many Tool Calls

**Symptoms:**

* Calls 5+ tools for simple requests
* Over-complicates tasks

**How to Fix:**

**Add efficiency guidelines:**

```
System instructions:

"Efficiency rules:
- Use minimum tools needed to complete task
- Don't call tools 'just in case'
- If 1 tool can do the job, don't call 3
- Ask yourself: 'Is this tool call necessary?'

Example:
User: 'What is Company X's website?'
L Bad: Call research tool, enrichment tool, database tool
 Good: Search knowledge base or call 1 research tool"
```

### High API Costs or Rate Limits

**Symptoms:**

* Hitting rate limits frequently
* Unexpected costs

**How to Fix:**

```
1. Add usage controls:
   System instructions:
   "Resource limits:
   - Max [N] tool calls per conversation
   - After limit: 'We've reached the tool usage limit.
     Start new conversation to continue.'"

2. Optimize tool usage:
   - Review system instructions
   - Are you calling tools unnecessarily?
   - Can you batch operations?

3. Use caching:
   - Store common queries in knowledge base
   - Reduce repeated API calls

4. Monitor usage:
   - Review conversation patterns
   - Identify expensive operations
   - Optimize or restrict those operations
```

## Advanced Debugging

### Enable Verbose Logging (Builder Testing)

When testing, ask the agent to explain its thinking:

```
Test prompt:
"Research Company X. After responding, explain:
1. What knowledge you retrieved
2. Which tools you called and why
3. How you decided what to do"

This reveals the agent's decision-making process.
```

### Isolation Testing

Test components separately:

**Test knowledge only:**

```
System instructions (temporary):
"You can ONLY use your knowledge base. Do not call any tools.
If asked to do something requiring tools, say 'Tools disabled for testing.'"

Test: Does knowledge retrieval work?
```

**Test tools only:**

```
System instructions (temporary):
"Ignore your knowledge base. Only use tools to answer questions."

Test: Do tools work correctly?
```

**Test system instructions only:**

```
Remove all knowledge and tools temporarily.

Test: Does agent follow personality and boundaries?
```

### A/B Testing for Debugging

Create two versions of your agent:

```
Version A: Current (broken) configuration
Version B: Minimal working configuration

Compare:
- Which one works?
- What's different?
- Gradually add features from A to B until it breaks
- That feature is the culprit
```

### Check Browser Console

For technical issues:

```
1. Open browser developer tools (F12 or Cmd+Option+I)
2. Go to Console tab
3. Start conversation with agent
4. Look for error messages (red text)
5. Screenshot errors and report to support
```

## When to Contact Support

Contact support if:

* Issue persists after trying all troubleshooting steps
* Technical errors appear consistently
* Platform features aren't working (can't save, can't upload, etc.)
* Integrations fail repeatedly
* Performance degraded significantly
* Data appears corrupted or lost

**What to include in support request:**

```
1. Clear description of issue:
   "When I [action], I expect [result], but instead [actual result]"

2. Steps to reproduce:
   "1. Go to [location]
    2. Click [button]
    3. Error appears"

3. Screenshots:
   - Show the issue
   - Include any error messages
   - Show browser console if technical

4. Conversation link:
   - Share specific conversation where issue occurs
   - Helps support see exact problem

5. What you've tried:
   - List troubleshooting steps already attempted
   - Saves time ruling out common fixes
```

## Issue Prevention

### Pre-Launch Checklist

Before making your agent public:

```
→ Test all sample questions work
→ Test all workflows individually
→ Test multi-workflow scenarios
→ Test with ambiguous requests
→ Test error scenarios (tool failures)
→ Review 5-10 test conversations
→ Check knowledge retrieval accuracy
→ Verify all integrations connected
→ Confirm no sensitive data in knowledge
→ Test shared conversation links work
→ Review system instructions for clarity
→ Check welcome message and prompt hint
```

### Ongoing Maintenance

**Weekly:**

```
→ Review 10-20 recent conversations
→ Check for new error patterns
→ Verify integrations still connected
→ Test 3-5 common scenarios
```

**Monthly:**

```
→ Full test suite run
→ Knowledge base audit
→ Review and update system instructions
→ Check for broken workflow agents
→ Update outdated information
```

**After Major Changes:**

```
→ Full regression testing
→ Compare before/after behavior
→ Review first 10 conversations post-change
→ Be ready to rollback if issues appear
```

## Common Error Messages

<AccordionGroup>
  <Accordion title="'Tool execution failed'">
    **Meaning:** Workflow agent or integration returned an error

    **Fix:**

    1. Test the tool independently
    2. Check tool configuration (API keys, auth)
    3. Review what data was passed to tool
    4. Check tool error logs if available
    5. Add error handling to system instructions
  </Accordion>

  <Accordion title="'Knowledge retrieval timeout'">
    **Meaning:** Knowledge base search took too long

    **Fix:**

    1. Knowledge base too large → reduce size
    2. Large files → split into smaller docs
    3. Temporary platform issue → try again
    4. Persistent → contact support
  </Accordion>

  <Accordion title="'Rate limit exceeded'">
    **Meaning:** Too many requests to an API/tool

    **Fix:**

    1. Wait before retrying (usually 1-5 minutes)
    2. Add rate limit handling to system instructions
    3. Reduce tool call frequency
    4. Implement caching for common requests
    5. Consider upgrading API tier if consistently hitting limits
  </Accordion>

  <Accordion title="'Authentication failed'">
    **Meaning:** Can't connect to integration or tool

    **Fix:**

    1. Re-authenticate the integration
    2. Check credentials/API keys
    3. Verify permissions granted
    4. Check if service credentials changed
    5. Ensure service is accessible (not behind firewall)
  </Accordion>

  <Accordion title="'Invalid configuration'">
    **Meaning:** Something in agent setup is wrong

    **Fix:**

    1. Review all configuration tabs
    2. Ensure required fields filled
    3. Check for special characters in names
    4. Try simplifying configuration
    5. Contact support with details
  </Accordion>
</AccordionGroup>

## Getting Help

### Documentation Resources

<CardGroup cols={2}>
  <Card title="Configuration Guide" icon="sliders" href="/knowledge-agents/configuration">
    Review how to write system instructions
  </Card>

  <Card title="Knowledge Base" icon="book" href="/knowledge-agents/knowledge-base">
    Troubleshoot knowledge retrieval issues
  </Card>

  <Card title="Tools Integration" icon="wrench" href="/knowledge-agents/tools-integration">
    Debug workflow and integration problems
  </Card>

  <Card title="Best Practices" icon="star" href="/knowledge-agents/best-practices">
    Learn patterns that prevent common issues
  </Card>
</CardGroup>

### Community & Support

* **Community Forum:** [community.agent.ai](https://community.agent.ai) - Ask questions, share solutions
* **Support:** [agent.ai/feedback](https://agent.ai/feedback) - Report bugs and request help
* **Status Page:** Check platform status for ongoing issues
* **Documentation:** [docs.agent.ai](https://docs.agent.ai) - Full documentation

<Note>
  **Remember:** Most issues have simple solutions. Work through the diagnostic checklist systematically, isolate the problem component, and apply targeted fixes. The knowledge agent community is also a great resource for troubleshooting uncommon issues.
</Note>


# How to Use Lists in For Loops
Source: https://docs.agent.ai/lists-in-for-loops

How to transform multi-select values into a usable format in Agent.ai workflows

<iframe width="560" height="315" src="https://www.youtube.com/embed/qy84PxZPFhw?si=eNa6AxbJavt7EbiE" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

## **Overview**

When using **for loop** actions in [Agent.ai](http://Agent.ai), you might run into issues if you're working with multi-select dropdowns. The problem usually comes down to format: **for loop** expects a very specific type of input, and the raw output from a multi-dropdown list might not be an exact match.

This guide walks you through how to inspect your input, transform it using a built-in LLM, and successfully run a loop with multi-dropdown values.

## **Required Format for for loop**

[Agent.ai](http://Agent.ai)'s **for loop** requires a **plain list of strings** in the following format:

```
["item1", "item2", "item3"]
```

Unspecified

* Must include square brackets **\[]**
* Each item must be in quotes
* Items must be separated by commas

Structured JSON (e.g., objects with ) will not work directly.

## **Step 1: Inspect Multi-Dropdown Output**

Multi-dropdown inputs do not return a list of strings. Instead, you'll get a list of objects that looks like this:

```
[  
  {"label": "LinkedIn", "value": "LinkedIn"},
  {"label": "Twitter", "value": "Twitter"}
]
```

To verify this, add a **Create Output** action immediately after your multi-dropdown input and display the variable. This lets you confirm the exact format before using it in a loop.

## **Step 2: Transform the Input**

To convert this into a usable format, insert an **LLM** **action** before the the loop action. Use a prompt that extracts only the **value** fields and returns a plain list of strings.

### **Example Prompt**

You will receive a JSON array of objects. Each object has a "label" and "value."

Your task:

* Extract the "value" from each object
* Return a plain Python list of strings
* No extra text, no code block formatting, no JSON structure
* Only output something like: \["LinkedIn", "Twitter"]

## **Step 3: Use the Transformed List**

Once the LLM returns the cleaned-up list, pass it into your **for loop** action. The loop should now work as expected.

Have questions or need help with your agent? Reach out to our [support team](https://agent.ai/feedback) or [community](https://community.agent.ai/feed).


# LLM Models
Source: https://docs.agent.ai/llm-models

Agent.ai provides a number of LLM models that are available for use.

## **LLM Models**

Selecting the right Large Language Model (LLM) for your application is a critical decision that impacts performance, cost, and user experience. This guide provides a comprehensive comparison of leading LLMs to help you make an informed choice based on your specific requirements.

## How to Select the Right LLM

When choosing an LLM, consider these key factors:

1. **Task Complexity**: For complex reasoning, research, or creative tasks, prioritize models with high accuracy scores (8-10), even if they're slower or more expensive. For simpler, routine tasks, models with moderate accuracy (6-8) but higher speed may be sufficient.
2. **Response Time Requirements**: If your application needs real-time interactions, prioritize models with speed ratings of 8-10. Customer-facing applications generally benefit from faster models to maintain engagement.
3. **Context Needs**: If your application processes long documents or requires maintaining extended conversations, select models with context window ratings of 8 or higher. Some specialized tasks might work fine with smaller context windows.
4. **Budget Constraints**: Cost varies dramatically across models. Free and low-cost options (0-2 on our relative scale) can be excellent for startups or high-volume applications, while premium models (5+) might be justified for mission-critical enterprise applications where accuracy is paramount.
5. **Specific Capabilities**: Some models excel at particular tasks like code generation, multimodal understanding, or multilingual support. Review the use cases to find models that specialize in your specific needs.

The ideal approach is often to start with a model that balances your primary requirements, then test alternatives to fine-tune performance. Many organizations use multiple models: premium options for complex tasks and more affordable models for routine operations.

## Vendor Overview

**OpenAI**: Offers the most diverse range of models with industry-leading capabilities, though often at premium price points, with particular strengths in reasoning and multimodal applications.

**Anthropic (Claude)**: Focuses on highly reliable, safety-aligned models with exceptional context length capabilities, making them ideal for document analysis and complex reasoning tasks.

**Google**: Provides models with impressive context windows and competitive pricing, with the Gemini series offering particularly strong performance in creative and analytical tasks.

**Perplexity**: Specializes in research-oriented models with unique web search integration, offering free access to powerful research capabilities and real-time information.

**Other Vendors**: Offer open-source and specialized models that provide strong performance at minimal or no cost, making advanced AI accessible for deployment in resource-constrained environments.

## OpenAI Models

| Model        | Speed | Accuracy | Context Window | Relative Cost | Use Cases                                                                                                                                                                          |
| ------------ | :---: | :------: | :------------: | :-----------: | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| GPT-4o       |   9   |     9    |        9       |       3       | • Multimodal assistant for text, audio, and images<br /> • Complex reasoning and coding tasks<br /> • Cost-sensitive deployments                                                   |
| GPT-4o-Mini  |   10  |     8    |        9       |       1       | • Real-time chatbots and high-volume applications<br /> • Long-context processing<br /> • General AI assistant tasks where affordability and speed are prioritized                 |
| GPT-4 Vision |   5   |     9    |        5       |       5       | • Image analysis and description<br /> • High-accuracy general assistant tasks<br /> • Creative and technical writing with visual context                                          |
| o1           |   6   |    10    |        9       |       4       | • Tackling highly complex problems in science, math, and coding<br /> • Advanced strategy or research planning<br /> • Scenarios accepting high latency/cost for superior accuracy |
| o1 Mini      |   8   |     8    |        9       |       1       | • Coding assistants and developer tools<br /> • Reasoning tasks that need efficiency over broad knowledge<br /> • Applications requiring moderate reasoning but faster responses   |
| o3 Mini      |   9   |     9    |        9       |       1       | • General-purpose chatbot for coding, math, science<br /> • Developer integrations<br /> • High-throughput AI services                                                             |
| GPT-4.5      |   5   |    10    |        9       |       10      | • Mission-critical AI tasks requiring top-tier intelligence<br /> • Highly complex problem solving or content generation<br /> • Multi-modal and extended context applications     |

## Anthropic (Claude) Models

| Model                         | Speed | Accuracy | Context Window | Relative Cost | Use Cases                                                                                                                                                     |
| ----------------------------- | :---: | :------: | :------------: | :-----------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Claude 3.7 Sonnet             |   8   |     9    |        9       |       2       | • Advanced coding and debugging assistant<br /> • Complex analytical tasks<br /> • Fast turnaround on detailed answers                                        |
| Claude 3.5 Sonnet             |   7   |     8    |        9       |       2       | • General-purpose AI assistant for long documents<br /> • Coding help and Q\&A<br /> • Everyday reasoning tasks with high reliability and alignment           |
| Claude 3.5 Sonnet Multi-Modal |   7   |     8    |        9       |       2       | • Image understanding in French or English<br /> • Multi-modal customer support<br /> • Research assistants combining text and visual data                    |
| Claude Opus                   |   6   |     7    |        9       |       9       | • High-precision analysis for complex queries<br /> • Long-form content summarization or generation<br /> • Enterprise scenarios requiring strict reliability |

## Google Models

| Model                          | Speed | Accuracy | Context Window | Relative Cost | Use Cases                                                                                                                                                               |
| ------------------------------ | :---: | :------: | :------------: | :-----------: | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Gemini 2.0 Pro                 |   7   |    10    |        8       |       5       | • Expert code generation and debugging<br /> • Complex prompt handling and multi-step reasoning<br /> • Cutting-edge research applications requiring maximum accuracy   |
| Gemini 2.0 Flash               |   9   |     9    |       10       |       1       | • Interactive agents and chatbots<br /> • General enterprise AI tasks at scale<br /> • Large-context processing up to \~1M tokens                                       |
| Gemini 2.0 Flash Thinking Mode |   8   |     9    |       10       |       2       | • Improved reasoning in QA and problem-solving<br /> • Explainable AI scenarios<br /> • Tasks requiring a balance of speed and reasoning accuracy                       |
| Gemini 1.5 Pro                 |   7   |     9    |       10       |       1       | • Sophisticated coding and mathematical problem solving<br /> • Processing extremely large contexts<br /> • Use cases tolerating higher cost/latency for higher quality |
| Gemini 1.5 Flash               |   9   |     7    |       10       |       1       | • Real-time assistants and chat services<br /> • Handling lengthy inputs<br /> • General tasks requiring decent reasoning at minimal cost                               |
| Gemma 7B It                    |   10  |     6    |        4       |       1       | • Italian-language chatbot and content generation<br /> • Lightweight reasoning and coding help<br /> • On-device or private deployments                                |
| Gemma2 9B It                   |   9   |     7    |        5       |       1       | • Multilingual assistant<br /> • Developer assistant on a budget<br /> • Text analysis with moderate complexity                                                         |

## Perplexity Models

| Model                    | Speed | Accuracy | Context Window | Relative Cost | Use Cases                                                                                                                                                           |
| ------------------------ | :---: | :------: | :------------: | :-----------: | ------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Perplexity               |   10  |     7    |        4       |       1       | • Quick factual Q\&A with web citations<br /> • Fast information lookups<br /> • General knowledge queries for free                                                 |
| Perplexity Deep Research |   3   |     9    |       10       |       1       | • In-depth research reports on any topic<br /> • Complex multi-hop questions requiring reasoning and evidence<br /> • Scholarly or investigative writing assistance |

## Open Source Models

| Model            | Speed | Accuracy | Context Window | Relative Cost | Use Cases                                                                                                                                                                   |
| ---------------- | :---: | :------: | :------------: | :-----------: | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| DeepSeek R1      |   7   |     9    |        9       |       1       | • Advanced reasoning engine for math and code<br /> • Integrating into Retrieval-Augmented Generation pipelines<br /> • Open-source AI deployments needing strong reasoning |
| Llama 3.3 70B    |   8   |     9    |        9       |       1       | • Versatile technical and creative assistant<br /> • High-quality AI for smaller setups<br /> • Resource-efficient deployment                                               |
| Mixtral 8×7B 32K |   9   |     8    |        8       |       1       | • General-purpose open-source chatbot<br /> • Long document analysis and retrieval QA<br /> • Scenarios needing both efficiency and quality on modest hardware              |

## Model Deprecation

In the **LLM Engine** dropdown, there's a section labeled **"Legacy Models Soon To Be Deprecated"**. These are models we plan to remove soon, and we’ll automatically migrate agents using them to a recommended alternative.


# How Credits Work
Source: https://docs.agent.ai/marketplace-credits

Agent.ai uses credits to enable usage and reward actions in the community.

## **Agent.ai's Mission**

Agent.ai is free to use and build with.

As a platform, Agent.ai's goal is to build the world's best professional marketplace for AI agents.

## **How Credits Fit In**

Credits are an agent.ai marketplace currency with no monetary value. Credits cannot be bought, sold, or exchanged for money. They exist to enable usage of the platform and reward actions in the communiuty.

Generally speaking, running an agent costs 1 credit.

You can earn more credits by performing actions like completing your profile or referring new users. Additionally, [Agent.ai](http://Agent.ai) replenishes credits on a weekly basis — if your balance falls below 25, we’ll automatically top it back up to 100.

If you ever do happen to hit your credit limit (most people won't) and can't run agents because you need more credits, let us know — we're happy to top you back up.


# MCP Server
Source: https://docs.agent.ai/mcp-server

Connect Agent.ai tools to ChatGPT, Claude, Cursor, and other AI assistants.

## **Connect Agent.ai to Your AI Assistant**

> Use your Agent.ai tools with ChatGPT, Claude, Cursor, and other MCP-compatible applications

## What is MCP?

Model Context Protocol (MCP) allows AI assistants like ChatGPT and Claude to access your Agent.ai tools, agents, and actions. Once connected, you can ask your AI assistant to use any of your Agent.ai capabilities directly in conversation.

## Connection Methods

### ✨ Secure Sign-In (Recommended)

The easiest way to connect is using our secure sign-in method. Simply add Agent.ai to your AI assistant, and you'll sign in with your Agent.ai account - no API tokens needed!

**Server URL:** `https://mcp.agent.ai/mcp`

**Benefits:**

* ✅ Most secure - just sign in with your Agent.ai account
* ✅ Works with ChatGPT, Claude, Cursor, and other modern MCP clients
* ✅ No API tokens to copy or manage
* ✅ Automatic access to all your agents and tools

***

## Setup Instructions

Choose your AI assistant below for step-by-step instructions:

<Tabs>
  <Tab title="ChatGPT">
    ### Step 1: Open ChatGPT Settings

    Click on your profile icon in ChatGPT and select **Settings** from the dropdown menu.

        <img src="https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step1.jpg?fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=aeea20bf88170321b06c13a69761029c" alt="ChatGPT Settings" data-og-width="1370" width="1370" data-og-height="1206" height="1206" data-path="images/mcp/chatgpt/chatgpt_step1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step1.jpg?w=280&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=362d9b38dbf947cb8c1bc5c6ea3b36eb 280w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step1.jpg?w=560&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=db09d6dd1991b208740ca4876ca864da 560w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step1.jpg?w=840&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=45475194ceefc958e291a6a679b951d9 840w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step1.jpg?w=1100&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=d7d1bc627531adac66e3c223e7fb98b9 1100w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step1.jpg?w=1650&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=88884732296ba0576c086068dad202a9 1650w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step1.jpg?w=2500&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=9cbf5fa9df48d72b42cdfb75f5a55c14 2500w" />

    ***

    ### Step 2: Navigate to Apps & Connectors

    Go to the **Apps & Connectors** section and click on **Advanced Settings** to enable Developer mode.

        <img src="https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step2.jpg?fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=f596ed4105e4b861f557ef666f841509" alt="ChatGPT Apps & Connectors" data-og-width="1380" width="1380" data-og-height="1212" height="1212" data-path="images/mcp/chatgpt/chatgpt_step2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step2.jpg?w=280&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=43c016cea43f701c7f6da711744843e3 280w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step2.jpg?w=560&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=a40b76b8bb41acff563a97bb5bca19a6 560w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step2.jpg?w=840&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=dd67001cd0a5607698a457c5875c8c6b 840w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step2.jpg?w=1100&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=31804338f7475b4bb05d86746584b974 1100w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step2.jpg?w=1650&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=58e6d76d7b1f9d37a15650f5b8fcd233 1650w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step2.jpg?w=2500&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=f2393d2319cd90f27cc56aa5269fb625 2500w" />

    ***

    ### Step 3: Enable Developer Mode

    Toggle on Developer mode to access connector features.

        <img src="https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step3.jpg?fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=8e67c22898eea5678497639a96ad1138" alt="ChatGPT Developer Mode" data-og-width="1366" width="1366" data-og-height="1208" height="1208" data-path="images/mcp/chatgpt/chatgpt_step3.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step3.jpg?w=280&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=8820396478807218486227215c455a21 280w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step3.jpg?w=560&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=5bc3504a65c5dd0f2b39c8560f771a6a 560w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step3.jpg?w=840&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=7982f3d4a71b3b64f477453cc1340a27 840w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step3.jpg?w=1100&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=d0b91a06f953cb5da630899ac2b32b5f 1100w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step3.jpg?w=1650&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=5106700bb474caac4e10ab627d4d4bc7 1650w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step3.jpg?w=2500&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=93d3c388e734f1a7042afd66ba296802 2500w" />

    ***

    ### Step 4: Create New Connector

    Once in Developer Mode, click **Create (new connector)** in the top right of the "Apps and Connectors" section.

        <img src="https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step4.0.jpg?fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=1fa51f3d12a78dc052b378535ccb9e5b" alt="ChatGPT Create Button" data-og-width="1372" width="1372" data-og-height="1214" height="1214" data-path="images/mcp/chatgpt/chatgpt_step4.0.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step4.0.jpg?w=280&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=4b27e0ae0fbf9d96f944bd7c6bbab3c6 280w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step4.0.jpg?w=560&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=6320a6e71d98273a7ef08b71deb69405 560w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step4.0.jpg?w=840&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=efe3bd6d1be896ab1eb5f4d0665ebe96 840w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step4.0.jpg?w=1100&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=be5d83453f6efd9a1c284d60f9fd28a7 1100w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step4.0.jpg?w=1650&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=6659d6cc04c952bc19f4398e15184b76 1650w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step4.0.jpg?w=2500&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=f4cd24394230d949eddeb4dadd26c168 2500w" />

    Enter **Agent.ai Tools** as the name and paste this URL:

    ```
    https://mcp.agent.ai/mcp
    ```

    Select **OAuth** for authentication and click **Create**. You'll be taken to sign in with your Agent.ai account.

        <img src="https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step4.jpg?fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=cc11cb2147507caecd0f7ef047e56246" alt="ChatGPT Create Connector" data-og-width="902" width="902" data-og-height="1310" height="1310" data-path="images/mcp/chatgpt/chatgpt_step4.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step4.jpg?w=280&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=55f5ff181b98d1eac16459e0ea6a766e 280w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step4.jpg?w=560&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=4a4fb2e6e791c77a806a99c5f54fcac3 560w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step4.jpg?w=840&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=e4c3c038143168c173667d2a6ef3f170 840w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step4.jpg?w=1100&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=5565aa65e02f0ebf3edf80b5e6ca32d3 1100w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step4.jpg?w=1650&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=66f1ef9ba63a7ee698816b6ac1c12cea 1650w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step4.jpg?w=2500&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=0a16e4071630571a98a3993177bdf14e 2500w" />

    ***

    ### Step 5: Start Using Agent.ai

    Click the **"+"** icon in ChatGPT, select **"More"** from the dropdown, then select your Agent.ai connector.

        <img src="https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step5.jpg?fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=7cd2250cbfcbc79edc88c2ad7b0f0d66" alt="ChatGPT Use Connector" data-og-width="1360" width="1360" data-og-height="1144" height="1144" data-path="images/mcp/chatgpt/chatgpt_step5.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step5.jpg?w=280&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=98bc477c781ba5c93ddc04dc2885b279 280w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step5.jpg?w=560&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=499bc77cb2a049d139acc94e6945d763 560w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step5.jpg?w=840&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=debc04f58e4cf67a37be1584b3694b94 840w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step5.jpg?w=1100&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=9a9d09b7785978edf4d75aef1d476fb4 1100w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step5.jpg?w=1650&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=87637418d1f0cb495253c42c8d7e4841 1650w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step5.jpg?w=2500&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=015bccd18cbb6f2f167baaa6516b0141 2500w" />

        <img src="https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step5.1.jpg?fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=54df2490eebae585594fc8681b47b35b" alt="ChatGPT Select Agent.ai" data-og-width="1394" width="1394" data-og-height="494" height="494" data-path="images/mcp/chatgpt/chatgpt_step5.1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step5.1.jpg?w=280&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=5298c8956b0bc3342dc4591b1359158c 280w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step5.1.jpg?w=560&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=69530520a8fdc4394a8ba2b463543fd8 560w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step5.1.jpg?w=840&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=df9becb70e22a42a1f447e86c52faa89 840w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step5.1.jpg?w=1100&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=f92b605d67616f4f7ba0b58799d1597d 1100w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step5.1.jpg?w=1650&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=3e47281020b72c12e777843eedd4b9bb 1650w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/chatgpt/chatgpt_step5.1.jpg?w=2500&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=3d67ac7eca6e34d1a3088c538332c647 2500w" />

    <Check>
      **You're all set!** All your Agent.ai tools and agents are now available in ChatGPT. Try asking ChatGPT to use one of your agents or actions!
    </Check>
  </Tab>

  <Tab title="Claude">
    ### Step 1: Open Claude Settings

    In [Claude](https://claude.ai), go to **Settings** → **Connectors** section, then click **"Add custom connector"**.

        <img src="https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/claude/claude.step1.jpg?fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=90d4c358987bfb442bf29058179afdca" alt="Claude Settings" data-og-width="2438" width="2438" data-og-height="1778" height="1778" data-path="images/mcp/claude/claude.step1.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/claude/claude.step1.jpg?w=280&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=0f197e1c82b114449df0e195b2045c2a 280w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/claude/claude.step1.jpg?w=560&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=9be0d9ff599ee01f2fea2fdebff66107 560w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/claude/claude.step1.jpg?w=840&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=a0a206e70e481eeff4796d856c26bcb5 840w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/claude/claude.step1.jpg?w=1100&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=740f9477d98d0bcba89657f1b3b5fdea 1100w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/claude/claude.step1.jpg?w=1650&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=d98ff27f85caf919920dfbbb7ad01ba5 1650w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/claude/claude.step1.jpg?w=2500&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=04a93b6e2e297c700ebe08fad75bb138 2500w" />

    ***

    ### Step 2: Enter Name and URL

    Enter **Agent.ai Tools** as the name and paste this URL:

    ```
    https://mcp.agent.ai/mcp
    ```

    Click **"Add"** and you'll be taken to sign in with your Agent.ai account.

        <img src="https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/claude/claude.step2.jpg?fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=feb07dc34a9095ce217872890caa6b9e" alt="Claude Add Connector" data-og-width="1088" width="1088" data-og-height="926" height="926" data-path="images/mcp/claude/claude.step2.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/claude/claude.step2.jpg?w=280&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=294c2959db1ba07b66f4d5b3ab75ebb5 280w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/claude/claude.step2.jpg?w=560&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=109b33c8ff6b88ec021f7a8f6bdd29f3 560w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/claude/claude.step2.jpg?w=840&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=9127fb1aa41dc6ea58d9adc81f75e6b3 840w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/claude/claude.step2.jpg?w=1100&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=d3242cb9cccaac0713dc11cc196fb252 1100w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/claude/claude.step2.jpg?w=1650&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=cfc24b4848e4a163731def5dc5d79c22 1650w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/claude/claude.step2.jpg?w=2500&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=b0ccb407afcf68dac4206eb9b2ab3031 2500w" />

    ***

    ### Step 3: Enable and Start Chatting

    Click the **Tools icon** in Claude, toggle on your Agent.ai connector, and start using your tools!

        <img src="https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/claude/claude.step3.jpg?fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=54f5233695248f75dc5c9cdbc7fd8d87" alt="Claude Enable and Chat" data-og-width="1438" width="1438" data-og-height="1274" height="1274" data-path="images/mcp/claude/claude.step3.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/claude/claude.step3.jpg?w=280&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=b1993edf3ac32dc423b28c783e09ac59 280w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/claude/claude.step3.jpg?w=560&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=da1b677dc71461e1bdebd892fad6bef9 560w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/claude/claude.step3.jpg?w=840&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=f1ee8ce26bc36838d20df2961806e9e4 840w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/claude/claude.step3.jpg?w=1100&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=3f787101dd1d20cf70e6788a805edfdf 1100w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/claude/claude.step3.jpg?w=1650&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=48ef7c33c04b82bd2af86a0ba01a99b5 1650w, https://mintcdn.com/agentai/G4nQBlJJdQEu3WdT/images/mcp/claude/claude.step3.jpg?w=2500&fit=max&auto=format&n=G4nQBlJJdQEu3WdT&q=85&s=dca5d960a0afa22f02b4e7b0994f7e50 2500w" />

    <Check>
      **You're all set!** All your Agent.ai tools and agents are now available in Claude. Just mention your agents or ask Claude to use specific tools!
    </Check>
  </Tab>

  <Tab title="Cursor IDE">
    ### Setting Up in Cursor

    1. Open Cursor Settings
    2. Navigate to **MCP** or **Model Context Protocol** section
    3. Add a new MCP server with this configuration:

    ```json  theme={null}
    {
      "agentai": {
        "url": "https://mcp.agent.ai/mcp"
      }
    }
    ```

    4. Restart Cursor
    5. You'll be prompted to sign in with your Agent.ai account

    <Check>
      **You're all set!** Your Agent.ai tools will appear in Cursor's AI assistant features.
    </Check>
  </Tab>
</Tabs>

***

## Security & Privacy

* ✅ Secure sign-in with your Agent.ai account
* ✅ AI assistants will always ask your permission before using tools
* ✅ You can approve tools once or for the entire conversation
* ✅ All communication is encrypted

***

## Troubleshooting

### Connection Issues

**"Can't connect" or "Authentication failed"**

* Make sure you're using the correct URL: `https://mcp.agent.ai/mcp`
* Try clearing your browser cache and signing in again
* Ensure you're logged into Agent.ai in your browser

**"No tools available"**

* Make sure you're signed in to Agent.ai
* Try disconnecting and reconnecting the Agent.ai connector

**AI assistant isn't using my tools**

* Make sure you've enabled the Agent.ai connector/tools in your conversation
* Try specifically mentioning the tool or agent by name

Still having issues? Contact our support team for help.

***

## Testing Your Connection

You can test your Agent.ai MCP server using the [Cloudflare MCP Playground](https://playground.ai.cloudflare.com/):

1. Visit [https://playground.ai.cloudflare.com/](https://playground.ai.cloudflare.com/)
2. Enter your MCP server URL: `https://mcp.agent.ai/mcp`
3. Click "Connect" and sign in with your Agent.ai account
4. The playground will list all your available tools
5. Test individual tools by selecting them and providing inputs

This is a great way to verify everything is working before using it with your AI assistant.

***

<Accordion title="Legacy Connection Methods (Alternative Options)">
  ### HTTP over SSE (Legacy)

  This method uses an API token instead of signing in. It still works but is not recommended for new setups.

  **For Claude Desktop:**

  1. Get your API token from the [integrations page](https://agent.ai/user/integrations)
  2. Open Claude Desktop Settings → Developer → Edit Config
  3. Add this configuration:

  ```json  theme={null}
  {
    "mcpServers": {
      "agentai": {
        "command": "npx",
        "args": [
          "-y",
          "@modelcontextprotocol/server-sse",
          "https://mcp.agent.ai/YOUR_API_TOKEN_HERE/sse"
        ]
      }
    }
  }
  ```

  4. Replace `YOUR_API_TOKEN_HERE` with your actual API token
  5. Restart Claude Desktop

  ### Standard I/O (Legacy)

  This is the original connection method using our NPM package.

  1. Get your API token from the [integrations page](https://agent.ai/user/integrations)
  2. Open Claude Desktop Settings → Developer → Edit Config
  3. Add this configuration:

  ```json  theme={null}
  {
    "mcpServers": {
      "agentai": {
        "command": "npx",
        "args": ["-y", "@agentai/mcp-server"],
        "env": {
          "API_TOKEN": "YOUR_API_TOKEN_HERE"
        }
      }
    }
  }
  ```

  4. Replace `YOUR_API_TOKEN_HERE` with your actual API token
  5. Restart Claude Desktop

  **Troubleshooting Legacy Methods:**

  * **"Connection refused"**: Verify your API token is correct and hasn't expired
  * **"Authentication failed"**: Get a fresh token from the [integrations page](https://agent.ai/user/integrations)
  * **NPM errors**: Ensure you have Node.js installed and npx is available
</Accordion>

***

<Accordion title="For Developers & Advanced Users">
  ## Technical Details

  ### Server Configuration

  Agent.ai's MCP server implements secure authentication with automatic client registration.

  **Endpoints:**

  * MCP Server: `https://mcp.agent.ai/mcp`
  * OAuth Discovery: `https://mcp.agent.ai/.well-known/oauth-authorization-server`
  * Health Check: `https://mcp.agent.ai/health`

  ### Authentication Flow

  1. Client discovers OAuth endpoints via `.well-known/oauth-authorization-server`
  2. Client automatically registers using Dynamic Client Registration (DCR)
  3. User is redirected to authenticate with their Agent.ai account
  4. Authorization code is exchanged for an access token
  5. Client uses Bearer token for MCP requests

  ### Security Features

  * OAuth 2.1 with PKCE (Proof Key for Code Exchange)
  * JWT access tokens validated against Auth0
  * Automatic token refresh for long-lived sessions
  * Dynamic client registration (no pre-configuration needed)

  ### Available Tools

  All your Agent.ai agents and tools are automatically available through the MCP server, including:

  * Action Tools: Core Agent.ai capabilities
  * Team Agents: Shared within your organization
  * Private Agents: Your personal agents
  * Public Agents: Community agents you've added

  ### Protocol Support

  The server supports multiple MCP protocol versions:

  * 2024-11-05
  * 2025-03-26

  Version negotiation happens automatically during client initialization.

  ### Integration Example

  For custom MCP clients:

  ```javascript  theme={null}
  import { Client } from '@modelcontextprotocol/sdk/client/index.js';

  const client = new Client({
    name: 'my-mcp-client',
    version: '1.0.0',
  }, {
    capabilities: {}
  });

  // Connect with OAuth support
  await client.connect('https://mcp.agent.ai/mcp');

  // List available tools
  const tools = await client.request({
    method: 'tools/list'
  }, ListToolsResultSchema);

  // Call a tool
  const result = await client.request({
    method: 'tools/call',
    params: {
      name: 'tool-name',
      arguments: { /* tool arguments */ }
    }
  }, CallToolResultSchema);
  ```

  ### NPM Package

  The legacy NPM package is available at:
  [https://www.npmjs.com/package/@agentai/mcp-server](https://www.npmjs.com/package/@agentai/mcp-server)

  Note: New integrations should use the OAuth method instead of the NPM package.
</Accordion>

***

For additional help or to report issues, please contact our support team.


# How to Format Output for Better Readability
Source: https://docs.agent.ai/output-formatting



When working with data in [Agent.ai](http://Agent.ai), you might find that the default output format isn't always easy to read or interpret. This is especially true when dealing with structured data like tweets, JSON, or other complex information. In this guide, we'll show you simple but powerful techniques to transform messy output into beautifully formatted, readable content.

## Create Better Formatting Prompts

<iframe width="560" height="315" src="https://www.youtube.com/embed/yJmF7c0N4Vg?si=oISTh9cgo7pxkAkZ" frameBorder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowFullScreen />

### Step 1: Identify the Formatting Issue

First, recognize when your [Agent.ai](http://Agent.ai) output needs better formatting. If you're looking at data that's hard to read or doesn't have clear visual organization, it's time to improve the formatting.

### Step 2: Ask ChatGPT to Generate a Better Prompt

Take your unformatted output to ChatGPT and ask it to create a prompt specifically designed for better formatting. For example:

"I have a list of tweets with data about the tweets, etc. It's in a raw, non-human readable format. I'd like you to generate a prompt that'll do two things:

1. Generate a summary of the tweets
2. Return each tweet in a readable form"

Then paste your unformatted output so ChatGPT can see what you're working with.

### Step 3: Use the New Prompt in [Agent.ai](http://Agent.ai)

ChatGPT will provide you with a more detailed prompt that includes specific formatting instructions. It might look something like:

"I have a dataset of tweets in JSON format. Perform the following tasks:

1. Generate a summary of the tweets
2. For each tweet, reformat it so it looks like this: \[Example of nicely formatted output]"

Copy this entire prompt and paste it into your [Agent.ai](http://Agent.ai) editor, replacing your original prompt.

### Step 4: Run Your Agent with the New Prompt

When you run your agent with the improved prompt, you'll get much more readable output. For example, instead of jumbled text about tweets, you might get:

Summary of tweets: \[Clear summary of main topics]

Most notable tweet: \[Highlighted important tweet]

Tweet Details: Date: \[Date] Content: \[Tweet content] Retweets: \[Number] Impressions: \[Number]

## Create Markdown Tables

<iframe width="560" height="315" src="https://www.youtube.com/embed/ZHsrNv82B6U?si=sZ97MKlX8CjdMOLL" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

### Step 1: Set Up Your Agent's Data Collection

First, create an agent that collects the data you want to display. For example, you could create a news agent that:

* Takes a topic as input
* Uses an API (like Google News) to fetch relevant articles
* Stores the results in a variable

### Step 2: Add a Formatting Action

After collecting your data, add a new action that will format the results into a markdown table:

1. Create a new action in your agent workflow
2. Use the following prompt structure to instruct the AI to create a markdown table: Format the following \[data type] into a markdown table. The table should include the following columns: \[list your columns] Ensure the output is properly formatted for markdown rendering and all links are properly formatted using markdown syntax.

For example, if you're creating a news agent, your prompt might look like:

> Format the following JSON list into a markdown table. The table should include the following columns: Title, Source, and Link Ensure the output is properly formatted for markdown rendering and all links are properly formatted using markdown syntax.

### Step 3: Configure the Output Format

When setting up your final response:

1. Pass the formatted markdown table to your output
2. In the output settings, select "Format as Markdown" to ensure proper rendering

This will ensure that your table displays correctly with proper columns, rows, and formatting.

## Create Interactive HTML Output

<iframe width="560" height="315" src="https://www.youtube.com/embed/-3FHfdikyf8?si=0ZNsXsecJ7uKA2Xc" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen />

### Structuring Your Content

When designing an agent that outputs HTML, it's important to define a consistent structure.

Common sections for informational agents might include:

* Overview
* Financials
* Products
* Competitors
* News
* Additional Resources

You can also include a Table of Contents at the top of the page that links to each section. Passing structured variables makes it easier for the agent to organize the final output.

### Engineering the HTML Prompt

To generate HTML, add a final instruction asking the agent to format the response accordingly.

Example prompt:

> "Format the response as a complete HTML document. Include a Table of Contents linking to each section (Overview, Financials, Products, Competitors, News, Additional Resources). Organize the information with clear headings, bullet points, and tables where appropriate."

You can instruct the agent to create anchor links for navigation and use lightweight formatting for better readability. At the end of the prompt, add:

> "Format the response as HTML."

This tells [Agent.ai](http://Agent.ai) to render the final output as HTML rather than plain text.

### Best Practices

* Use section headers (\<h2>, \<h3>) to organize information.
* Add anchor links (\<a href="#section-id">) for easier navigation.
* Use tables for structured data like financials or product comparisons.
* Keep formatting lightweight and focused on clarity.

Formatting agent responses as HTML allows you to create more structured, interactive outputs without custom development.
By defining your content flow, gathering the right inputs, and prompting clearly, you can design richer user experiences directly inside Agent.ai.

Have questions or need help with your agent? Reach out to our [support team](https://agent.ai/feedback) or [community](https://community.agent.ai/feed).


# Rate Limits
Source: https://docs.agent.ai/ratelimits

Agent.ai implements rate limit logic to ensure a consistent user experience.

## **Rate Limits**

We implement the following rate limits to ensure a consistent user experience: 20 requests per minute and 1000 requests per day.

For each request, we expose the following rate limit headers so that you can monitor and adjust your application's behavior accordingly:

* `ratelimit-limit: 1000`: 1000
* `ratelimit-remaining`: 999
* `ratelimit-reset`: The timestamp when the rate limit resets.
* `ratelimit-reset-date`: The ISO UTC date when the rate limit resets.
* `retry-after`: The number of seconds to wait before retrying the request.


# Company Research Agent
Source: https://docs.agent.ai/recipes/company-research-agent

How to build a Company Research agent in Agent.ai

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


# Executive News Agent
Source: https://docs.agent.ai/recipes/executive-news-agent

How to build an Executive News agent

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


# Executive Tweet Analyzer Agent
Source: https://docs.agent.ai/recipes/executive-tweet-analyzer

How to build an Executive Tweet Analyzer agent

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


# HubSpot Contact Enrichment
Source: https://docs.agent.ai/recipes/hubspot-contact-enrichment

Automatically enrich contact records with company intelligence, news, and AI-powered insights whenever a contact is created or updated

Automatically enrich contact records with company intelligence, news, and AI-powered insights whenever a contact is created or updated.

**What it does:** Triggered by HubSpot, looks up contact details, searches the web for company info, generates AI insights, updates the contact, and logs the enrichment.

**Common uses:**

* Auto-research new leads
* Keep contact data current
* Provide sales context automatically
* Generate talking points for outreach
* Track enrichment history

**Complexity:** Intermediate - Uses webhooks, lookups, web search, AI analysis, and updates

***

## Overview

This workflow automatically enriches contacts the moment they're created or updated in HubSpot. It:

1. Receives webhook from HubSpot (contact created/updated)
2. Looks up full contact details
3. Searches web for company news and info
4. Uses AI to analyze and summarize intelligence
5. Updates contact with enrichment data
6. Creates timeline event to track enrichment

**Result:** Sales reps get instant context about new contacts without manual research.

***

## What You'll Need

### HubSpot Setup

**HubSpot Workflow (to trigger enrichment):**

* Trigger: Contact created OR Contact property changed
* Action: Send webhook to Agent.AI
* Payload includes: `contact_id`, `contact_email`, `contact_company`

**Custom Properties** (create in HubSpot → Settings → Properties → Contacts):

* `company_overview` (Multi-line text) - AI-generated company summary
* `recent_news` (Multi-line text) - News summary
* `talking_points` (Multi-line text) - Sales talking points
* `relevance_score` (Number) - 1-10 priority rating
* `outreach_approach` (Multi-line text) - Recommended approach
* `last_enriched` (Date) - Track when enriched

**Permissions:**

* Read Contacts
* Write Contacts
* Read Timeline Events
* Write Timeline Events

### Agent.AI Setup

**Actions needed:**

* Webhook Trigger
* Lookup HubSpot Object (V2)
* Get Search Results (web search)
* Invoke LLM
* Update HubSpot Object (V2)
* Create Timeline Event (V2)

**Requirements:**

* Web search API access (Google, Bing, or similar)
* LLM access (OpenAI, Anthropic, etc.)

***

## Step-by-Step Setup

### Step 1: Create the Agent.AI Workflow

**Add trigger:** Webhook

**Configuration:**

* Copy the webhook URL (you'll need this for HubSpot)
* Expected variables from HubSpot:
  * `_hubspot_portal` (automatically included)
  * `contact_id` (contact's HubSpot ID)
  * `contact_email` (contact's email)
  * `contact_company` (contact's company name)

### Step 2: Setup HubSpot Workflow

**In HubSpot:**

1. Go to Automation → Workflows
2. Create workflow
3. **Trigger:** Contact created OR Contact property "Email" is known
4. **Add action:** Send webhook
5. **Webhook URL:** Paste Agent.AI webhook URL from Step 1
6. **Method:** POST
7. **Payload:**

```json  theme={null}
{
  "_hubspot_portal": "[portal.id]",
  "contact_id": "[contact.hs_object_id]",
  "contact_email": "[contact.email]",
  "contact_company": "[contact.company]"
}
```

8. Save and activate

**Now when contacts are created in HubSpot, this webhook fires.**

### Step 3: Lookup Full Contact Details

**Add action:** Lookup HubSpot Object (V2)

**Configuration:**

* **Object Type:** Contacts
* **Lookup by:** Lookup by Object ID
* **Object ID:** Click `{}` → select `contact_id` (from webhook)
* **Retrieve Properties:** Click "+ Add Property" and select:
  * `firstname`
  * `lastname`
  * `email`
  * `company`
  * `jobtitle`
  * `phone`
  * `city`
  * `state`
  * `country`
  * `industry`
  * `hs_object_id`
* **Retrieve Associations:** Select "Companies" (get associated company records)
* **Output Variable:** `contact_data`

**What this does:** Gets complete contact profile with all details for enrichment.

### Step 4: Web Search for Company Info

**Add action:** Get Search Results (or Web Search)

**Configuration:**

* **Query:** Type text and insert variables:
  * Click `{}` → `contact_data` → `properties` → `company`
  * Type " news funding products recent"
* **Number of Results:** 5
* **Output Variable:** `web_research`

**Example query:** "Acme Corp news funding products recent"

**What this does:** Finds recent news, funding announcements, product launches, and company updates.

### Step 5: AI Enrichment Analysis

**Add action:** Invoke LLM

**Configuration:**

* **Prompt:**

```
Analyze this contact and create an enrichment summary:

Contact Information:
- Name: [contact first name] [contact last name]
- Title: [contact job title]
- Company: [contact company]
- Industry: [contact industry]
- Location: [contact city], [contact state]

Recent Company News & Information:
[web research results]

Please provide:
1. Company overview (2-3 sentences describing the company)
2. Recent news summary (key highlights from search results)
3. Talking points for sales (3-5 specific conversation starters)
4. Contact relevance score (1-10, where 10 is highest priority)
5. Recommended outreach approach (1-2 sentences)

Return as JSON with keys: company_overview, news_summary, talking_points, relevance_score, outreach_approach
```

* **Model:** gpt-4 (or your preferred LLM)
* **Output Variable:** `enrichment_insights`

**What this does:** AI analyzes all gathered data and creates actionable sales intelligence.

### Step 6: Update Contact with Enrichment

**Add action:** Update HubSpot Object (V2)

**Configuration:**

* **Object Type:** Contacts
* **Identify by:** Lookup by Object ID
* **Identifier:** Click `{}` → select `contact_id` (from webhook)
* **Update Properties:** Click "+ Add Property" and select custom properties:
  * `company_overview`: Click `{}` → `enrichment_insights` → `company_overview`
  * `recent_news`: Click `{}` → `enrichment_insights` → `news_summary`
  * `talking_points`: Click `{}` → `enrichment_insights` → `talking_points`
  * `relevance_score`: Click `{}` → `enrichment_insights` → `relevance_score`
  * `outreach_approach`: Click `{}` → `enrichment_insights` → `outreach_approach`
  * `last_enriched`: Type `[now]` or use current date variable
* **Output Variable:** `updated_contact`

**What this does:** Writes all enrichment data back to HubSpot contact record.

### Step 7: Log Enrichment Activity

**Add action:** Create Timeline Event (V2)

**Configuration:**

* **Object Type:** Contacts
* **Target Object ID:** Click `{}` → select `contact_id`
* **Event Type:** `contact_enriched`
* **Event Title:** "Contact Enriched with AI Insights"
* **Event Description:** Type "Enriched contact with company research and AI analysis. Relevance score: " then click `{}` → `enrichment_insights` → `relevance_score`
* **Event Properties:** (optional)
  ```
  sources=[web_research]
  ai_model=gpt-4
  ```
* **Event Timestamp:** Leave blank (uses current time)
* **Output Variable:** `enrichment_event`

**What this does:** Creates audit trail showing when and how contact was enriched.

***

## How It Works

**Execution flow:**

1. **Contact created in HubSpot** (e.g., from form submission)
2. **HubSpot workflow fires webhook** to Agent.AI with contact ID
3. **Lookup** gets full contact profile from HubSpot → `contact_data`
4. **Web Search** finds recent company news → `web_research`
5. **AI Analysis** combines contact + news → generates insights → `enrichment_insights`
6. **Update** writes enrichment data to contact record in HubSpot
7. **Timeline Event** logs that enrichment occurred

**Timeline:** \~10-15 seconds from contact creation to enriched profile

***

## Example Output

### What the AI Generates

**For contact "John Doe, VP Engineering at Acme Corp":**

```json  theme={null}
{
  "company_overview": "Acme Corp is a fast-growing enterprise AI platform company based in San Francisco. Recently raised $50M Series B led by Sequoia Capital, indicating strong investor confidence and expansion plans. Focus on enterprise machine learning solutions.",

  "news_summary": "Recent $50M Series B funding announced. New enterprise features launched including advanced analytics and custom model training. Expanding engineering team by 50% in next 6 months. Featured in TechCrunch for innovative AI approach.",

  "talking_points": "1. Congratulate on recent $50M Series B funding\n2. Discuss new enterprise features and how they align with engineering priorities\n3. Reference expansion plans and potential partnership opportunities\n4. Mention TechCrunch feature and industry recognition\n5. Connect on engineering team growth and talent needs",

  "relevance_score": 9,

  "outreach_approach": "High-priority contact. VP of Engineering at well-funded, rapidly growing company. Lead with technical value proposition and enterprise case studies. Timing is ideal given their product launch and team expansion."
}
```

### What Appears in HubSpot

In the contact record, sales reps see:

**Company Overview:**
"Acme Corp is a fast-growing enterprise AI platform company..."

**Recent News:**
"Recent \$50M Series B funding announced. New enterprise features..."

**Talking Points:**
"1. Congratulate on recent \$50M Series B funding
2\. Discuss new enterprise features..."

**Relevance Score:** 9

**Outreach Approach:**
"High-priority contact. VP of Engineering at well-funded..."

**Timeline Event:**
"Contact Enriched with AI Insights - Relevance score: 9"

***

## Customization Ideas

### Different Trigger Conditions

**In HubSpot workflow:**

* Trigger on specific forms (only enrich demo requests)
* Trigger on lifecycle stage change (enrich when MQL)
* Trigger on company property change (re-enrich when company changes)

### Industry-Specific Research

**Customize web search query:**

* Tech companies: "\[company] funding product launch tech news"
* Manufacturing: "\[company] acquisitions capacity expansion news"
* Healthcare: "\[company] FDA approvals clinical trials news"

### Different Enrichment Focus

**Adjust AI prompt for different goals:**

**For sales:**

```
Focus on: buying signals, budget indicators, decision maker access, competitive landscape
```

**For recruiting:**

```
Focus on: company culture, growth trajectory, engineering team size, tech stack
```

**For partnerships:**

```
Focus on: strategic initiatives, market positioning, partner ecosystem, expansion plans
```

### Conditional Enrichment

**Add If Condition after lookup:**

* Only enrich if `jobtitle` contains "VP", "Director", "C-level"
* Only enrich if `relevance_score` > 7
* Only enrich if company size > 100 employees

### Multi-Language Support

**For international contacts:**

* Detect `country` from contact data
* Adjust web search language
* Request AI response in appropriate language

***

## Troubleshooting

### Webhook Not Firing

**Agent.AI workflow doesn't run when contact created**

**Causes:**

1. HubSpot workflow not active
2. Webhook URL incorrect
3. Contact doesn't meet trigger criteria

**Fix:**

1. Check HubSpot workflow status (Automation → Workflows)
2. Verify webhook URL matches Agent.AI URL exactly
3. Test with a contact that definitely meets trigger conditions
4. Check HubSpot workflow execution history

### No Web Results

**Web search returns empty or irrelevant results**

**Causes:**

1. Company name is generic or missing
2. Search API limit reached
3. Company is very small/new

**Fix:**

1. Check `contact_data.properties.company` has a value
2. Add fallback: If no company, skip web search
3. Broaden search query (remove specific terms)
4. Add If Condition to skip search if company is empty

### AI Response Not Formatted

**Enrichment insights malformed or not JSON**

**Causes:**

1. LLM didn't follow format instructions
2. Web results overwhelming token limit

**Fix:**

1. Make prompt more explicit: "Return ONLY valid JSON"
2. Reduce web search results from 5 to 3
3. Try GPT-4 instead of GPT-3.5 (better at structured output)
4. Add error handling with Set Variable action

### Properties Not Updating

**Contact updated but enrichment fields empty**

**Causes:**

1. Custom properties not created in HubSpot
2. AI returned unexpected format
3. Variable path wrong

**Fix:**

1. Create all custom properties in HubSpot first
2. Check execution log - what did AI return?
3. Verify variable paths: `enrichment_insights.company_overview` not `company_overview`

### Enrichment Too Slow

**Workflow takes 30+ seconds**

**Causes:**

1. Web search slow
2. LLM processing large context
3. Multiple API calls stacking

**Fix:**

1. Reduce web search results (5 → 3)
2. Simplify AI prompt
3. Use faster LLM model (GPT-3.5 instead of GPT-4)
4. Consider async processing

***

## Tips & Best Practices

**✅ Do:**

* Test with a few contacts before activating for all
* Create all custom properties in HubSpot first
* Use specific, relevant web search queries
* Monitor LLM costs (each contact = 1 LLM call)
* Review AI-generated insights for accuracy
* Add timestamp to track when enriched
* Log enrichment to timeline for audit trail

**❌ Don't:**

* Enrich every contact (filter for quality leads only)
* Use vague search queries (be specific)
* Forget to handle missing company names
* Skip error handling for web search failures
* Enrich contacts without email or company data
* Re-enrich same contact multiple times per day

**Cost optimization:**

* Only enrich contacts above certain score threshold
* Use cheaper LLM for simple enrichment
* Limit web search to 3 results
* Add cooldown period (don't re-enrich within 30 days)

**Privacy considerations:**

* Web search is public data only
* Don't store sensitive info in custom properties
* Follow GDPR/privacy regulations
* Allow contacts to opt out of enrichment

***

## Related Resources

**Actions used:**

* [Lookup HubSpot Object (V2)](../actions/hubspot-v2-lookup-object)
* [Update HubSpot Object (V2)](../actions/hubspot-v2-update-object)
* [Create Timeline Event (V2)](../actions/hubspot-v2-create-timeline-event)

**Related workflows:**

* [HubSpot Deal Analysis](./hubspot-deal-analysis) - Similar AI analysis pattern
* [HubSpot Customer Onboarding](./hubspot-customer-onboarding) - Multi-step automation example

***

**Last Updated:** 2025-10-01


# HubSpot Customer Onboarding
Source: https://docs.agent.ai/recipes/hubspot-customer-onboarding

Automatically kickoff customer onboarding when deals close - analyze relationship history, generate personalized onboarding plans, and create timeline events with next steps

Automatically kickoff customer onboarding when deals close - analyze relationship history, generate personalized onboarding plans, and create timeline events with next steps.

**What it does:** Triggered when a deal closes, looks up customer details and engagement history, uses AI to create onboarding plan, and logs next steps to HubSpot timeline.

**Common uses:**

* Automate onboarding kickoff
* Generate personalized welcome sequences
* Ensure consistent onboarding experience
* Provide context to success team
* Track onboarding milestones

**Complexity:** Advanced - Uses webhooks, lookups, associations, engagements, AI analysis, and multiple timeline events

***

## Overview

This workflow automates the transition from sales to customer success when a deal closes. It:

1. Receives webhook when deal reaches "Closed Won"
2. Looks up deal details with associated contacts and companies
3. Gets primary contact information
4. Retrieves engagement history (calls, emails, meetings)
5. Uses AI to analyze relationship and create onboarding plan
6. Creates timeline events with personalized next steps
7. (Optional) Notifies success team

**Result:** Customer success team gets complete context and AI-generated onboarding plan the moment a deal closes.

***

## What You'll Need

### HubSpot Setup

**HubSpot Workflow (to trigger onboarding):**

* Trigger: Deal stage changed to "Closed Won"
* Action: Send webhook to Agent.AI
* Payload includes: `deal_id`, `deal_name`, `deal_amount`, `close_date`

**Permissions:**

* Read Deals
* Read Contacts
* Read Companies
* Read Engagements
* Write Timeline Events

**Optional Properties:**

* Custom deal properties for onboarding tracking
* Onboarding status field
* Implementation timeline field

### Agent.AI Setup

**Actions needed:**

* Webhook Trigger
* Lookup HubSpot Object (V2) - Used multiple times
* Get Engagements (V2) - Used multiple times
* Invoke LLM
* Create Timeline Event (V2) - Used multiple times
* If Condition (optional, for conditional logic)

**Requirements:**

* LLM access (OpenAI, Anthropic, etc.)

***

## Step-by-Step Setup

### Step 1: Create the Agent.AI Workflow

**Add trigger:** Webhook

**Configuration:**

* Copy the webhook URL (you'll need this for HubSpot)
* Expected variables from HubSpot:
  * `_hubspot_portal` (automatically included)
  * `deal_id` (deal's HubSpot ID)
  * `deal_name` (deal name for context)
  * `deal_amount` (contract value)
  * `close_date` (when deal closed)

### Step 2: Setup HubSpot Workflow

**In HubSpot:**

1. Go to Automation → Workflows
2. Create workflow
3. **Trigger:** Deal stage changed to "Closed Won"
4. **Add action:** Send webhook
5. **Webhook URL:** Paste Agent.AI webhook URL from Step 1
6. **Method:** POST
7. **Payload:**

```json  theme={null}
{
  "_hubspot_portal": "{{portal.id}}",
  "deal_id": "{{deal.hs_object_id}}",
  "deal_name": "{{deal.dealname}}",
  "deal_amount": "{{deal.amount}}",
  "close_date": "{{deal.closedate}}"
}
```

8. Save and activate

**Now when deals reach "Closed Won", this webhook fires.**

### Step 3: Lookup Deal with Associations

**Add action:** Lookup HubSpot Object (V2)

**Configuration:**

* **Object Type:** Deals
* **Lookup by:** Lookup by Object ID
* **Object ID:** Click `{}` → select `deal_id` (from webhook)
* **Retrieve Properties:** Click "+ Add Property" and select:
  * `dealname`
  * `dealstage`
  * `amount`
  * `closedate`
  * `pipeline`
  * `deal_type`
  * `contract_start_date`
  * `hs_object_id`
* **Retrieve Associations:** Select "Contacts" and "Companies"
* **Output Variable:** `deal_data`

**What this does:** Gets complete deal info plus IDs of associated contacts and companies.

### Step 4: Lookup Primary Contact

**Add action:** Lookup HubSpot Object (V2)

**Configuration:**

* **Object Type:** Contacts
* **Lookup by:** Lookup by Object ID
* **Object ID:** Click `{}` → `deal_data` → `associations` → `contacts` → `[0]` → `id`
* **Retrieve Properties:** Click "+ Add Property" and select:
  * `firstname`
  * `lastname`
  * `email`
  * `phone`
  * `jobtitle`
  * `department`
  * `hs_object_id`
* **Output Variable:** `primary_contact`

**What this does:** Gets detailed info about the primary contact (first associated contact).

**Note:** `[0]` gets the first contact from the associations array. You could add an If Condition to find a specific contact role instead.

### Step 5: Get Deal Engagement History

**Add action:** Get Engagements (V2)

**Configuration:**

* **Object Type:** Deals
* **Object ID:** Click `{}` → select `deal_id` (from webhook)
* **Engagement Types:** Select "Calls", "Emails", "Meetings", "Notes"
* **Limit:** 50
* **Output Variable:** `deal_engagements`

**What this does:** Retrieves all sales interactions (calls, emails, meetings, notes) associated with this deal.

### Step 6: Get Contact Engagement History

**Add action:** Get Engagements (V2)

**Configuration:**

* **Object Type:** Contacts
* **Object ID:** Click `{}` → `primary_contact` → `id`
* **Engagement Types:** Select "Calls", "Emails", "Meetings", "Notes"
* **Limit:** 50
* **Output Variable:** `contact_engagements`

**What this does:** Gets engagement history for the primary contact (might include interactions beyond this deal).

### Step 7: AI Onboarding Analysis

**Add action:** Invoke LLM

**Configuration:**

* **Prompt:**

```
Create a personalized customer onboarding plan based on this context:

DEAL INFORMATION:
- Deal: {{deal_data.properties.dealname}}
- Amount: ${{deal_data.properties.amount}}
- Close Date: {{deal_data.properties.closedate}}
- Contract Start: {{deal_data.properties.contract_start_date}}

PRIMARY CONTACT:
- Name: {{primary_contact.properties.firstname}} {{primary_contact.properties.lastname}}
- Title: {{primary_contact.properties.jobtitle}}
- Email: {{primary_contact.properties.email}}
- Department: {{primary_contact.properties.department}}

RELATIONSHIP HISTORY:
Deal Engagements: {{deal_engagements}}
Contact Engagements: {{contact_engagements}}

Based on this context, provide:

1. Onboarding complexity (Low/Medium/High)
2. Key stakeholders identified from engagements
3. Technical requirements mentioned in sales conversations
4. Recommended onboarding timeline (in days)
5. First 3 onboarding milestones with specific actions
6. Potential risks or concerns to watch for
7. Personalized welcome message for customer success team

Format as JSON with keys: complexity, stakeholders, technical_requirements, timeline_days, milestones, risks, welcome_message
```

* **Model:** gpt-4 (or your preferred LLM)
* **Output Variable:** `onboarding_plan`

**What this does:** AI analyzes all context and creates a detailed, personalized onboarding plan.

### Step 8: Create Kickoff Timeline Event

**Add action:** Create Timeline Event (V2)

**Configuration:**

* **Object Type:** Deals
* **Target Object ID:** Click `{}` → select `deal_id`
* **Event Type:** `onboarding_kickoff`
* **Event Title:** "Onboarding Plan Generated"
* **Event Description:** Click `{}` → `onboarding_plan` → `welcome_message`
* **Event Properties:**
  ```
  complexity={{onboarding_plan.complexity}}
  timeline_days={{onboarding_plan.timeline_days}}
  ```
* **Output Variable:** `kickoff_event`

**What this does:** Logs that onboarding started with AI-generated plan details.

### Step 9: Create Milestone Events (Loop Optional)

**Add action:** Create Timeline Event (V2) - Repeat for each milestone

**Milestone 1:**

* **Object Type:** Deals
* **Target Object ID:** Click `{}` → select `deal_id`
* **Event Type:** `onboarding_milestone`
* **Event Title:** "Milestone 1: " then click `{}` → `onboarding_plan` → `milestones` → `[0]`
* **Event Description:** Type "First milestone for customer onboarding"
* **Output Variable:** `milestone_1_event`

**Milestone 2:**

* Same pattern, using `milestones[1]`

**Milestone 3:**

* Same pattern, using `milestones[2]`

**What this does:** Creates separate timeline events for each onboarding milestone so success team can track progress.

### Step 10: Create Contact Timeline Event

**Add action:** Create Timeline Event (V2)

**Configuration:**

* **Object Type:** Contacts
* **Target Object ID:** Click `{}` → `primary_contact` → `id`
* **Event Type:** `customer_onboarding_start`
* **Event Title:** "Customer Onboarding Started"
* **Event Description:** Type "Onboarding kickoff for " then click `{}` → `deal_data` → `properties` → `dealname`
* **Event Properties:**
  ```
  deal_id={{deal_id}}
  complexity={{onboarding_plan.complexity}}
  ```
* **Output Variable:** `contact_event`

**What this does:** Logs onboarding start on the contact record too (visible in contact timeline).

### Step 11 (Optional): Send Notification

**Add action:** Send Email

**Configuration:**

* **To:** [success-team@yourcompany.com](mailto:success-team@yourcompany.com)
* **Subject:** Type "New Customer Onboarding: " then click `{}` → select `deal_name`
* **Body:**

```
New customer onboarding ready!

Deal: {{deal_name}}
Amount: ${{deal_amount}}
Primary Contact: {{primary_contact.properties.firstname}} {{primary_contact.properties.lastname}}

Onboarding Complexity: {{onboarding_plan.complexity}}
Timeline: {{onboarding_plan.timeline_days}} days

Key Stakeholders:
{{onboarding_plan.stakeholders}}

Technical Requirements:
{{onboarding_plan.technical_requirements}}

Milestones:
{{onboarding_plan.milestones}}

Risks to Watch:
{{onboarding_plan.risks}}

View in HubSpot: [link to deal]
```

**What this does:** Notifies customer success team with full onboarding plan.

***

## How It Works

**Execution flow:**

1. **Deal closes** in HubSpot → reaches "Closed Won" stage
2. **HubSpot workflow fires webhook** to Agent.AI with deal ID
3. **Lookup Deal** gets full deal details + associated contact/company IDs → `deal_data`
4. **Lookup Primary Contact** gets contact details → `primary_contact`
5. **Get Deal Engagements** retrieves sales history → `deal_engagements`
6. **Get Contact Engagements** retrieves contact history → `contact_engagements`
7. **AI Analysis** combines all context → generates onboarding plan → `onboarding_plan`
8. **Create Timeline Events** logs kickoff + milestones to deal and contact
9. **Send Email** (optional) notifies success team

**Timeline:** \~15-20 seconds from deal close to complete onboarding plan

***

## Example Output

### What the AI Generates

**For "Acme Corp - Enterprise License" deal:**

```json  theme={null}
{
  "complexity": "High",

  "stakeholders": "VP of Engineering (John Doe - primary), CTO (mentioned in demo call), IT Manager (security discussions), 3 engineering team members attended technical deep-dive",

  "technical_requirements": "SSO integration required, custom API endpoints for internal tools, data migration from legacy system, dedicated environment for testing, compliance review for data handling",

  "timeline_days": 90,

  "milestones": [
    "Week 1-2: Kickoff call, technical discovery, SSO setup",
    "Week 3-6: Core implementation, API integration, data migration planning",
    "Week 7-12: Testing, training sessions, compliance review, go-live preparation"
  ],

  "risks": "Complex SSO requirements may delay timeline. Data migration complexity not fully scoped. Multiple stakeholders need alignment. Customer mentioned tight deadline for Q1 launch.",

  "welcome_message": "Welcome to Acme Corp! This is a high-value enterprise customer with sophisticated technical requirements. VP of Engineering John Doe is your primary contact and has been very engaged throughout the sales process. Key focus: deliver SSO and API integration within 90 days to meet their Q1 launch deadline. Multiple stakeholders need coordination - schedule kickoff call with all parties ASAP."
}
```

### What Appears in HubSpot

**On the Deal timeline:**

* **Event:** "Onboarding Plan Generated"
* **Description:** "Welcome to Acme Corp! This is a high-value enterprise customer..."
* **Properties:** complexity=High, timeline\_days=90

**Three milestone events:**

* "Milestone 1: Week 1-2: Kickoff call, technical discovery, SSO setup"
* "Milestone 2: Week 3-6: Core implementation, API integration..."
* "Milestone 3: Week 7-12: Testing, training sessions..."

**On the Contact timeline:**

* **Event:** "Customer Onboarding Started"
* **Description:** "Onboarding kickoff for Acme Corp - Enterprise License"

**Email to success team:**
Subject: "New Customer Onboarding: Acme Corp - Enterprise License"
Body contains full onboarding plan with all details

***

## Customization Ideas

### Different Trigger Conditions

**In HubSpot workflow:**

* Trigger on specific deal types only (enterprise vs. standard)
* Trigger when ticket type = "New Customer Onboarding"
* Trigger when deal reaches "Implementation" stage

### Conditional Onboarding Paths

**Add If Condition after AI analysis:**

* If complexity = "High" → Assign to senior success manager
* If complexity = "Low" → Use automated onboarding sequence
* If deal amount > \$100k → Create dedicated Slack channel

### Company-Level Analysis

**Add step to lookup company:**

* Get company details from `deal_data.associations.companies[0].id`
* Include company size, industry, tech stack in AI analysis
* Adjust onboarding based on company profile

### Integration with Other Systems

**After onboarding plan:**

* Create Jira tickets for technical milestones
* Add tasks to project management tool
* Create Slack channel for customer
* Send calendar invites for milestone meetings

### Multi-Contact Analysis

**Instead of just primary contact:**

* Loop through all associated contacts
* Get engagements for each
* Identify decision makers, technical champions, end users
* Create onboarding plan for each role

***

## Troubleshooting

### No Associated Contacts

**Deal has no contacts associated**

**Causes:**

1. Deal created without contact association
2. Contact association removed

**Fix:**

1. Add If Condition after Step 3 to check if `deal_data.associations.contacts` exists
2. If empty, skip contact lookup and use deal-only onboarding
3. Or create timeline event flagging missing contact

### Engagement History Empty

**No engagements returned**

**Causes:**

1. Deal/contact has no logged engagements
2. Permissions issue

**Fix:**

1. Check "Read Engagements" permission
2. Add fallback message: "No engagement history available"
3. AI can still create onboarding plan without history
4. Log note to manually research customer

### AI Response Too Generic

**Onboarding plan lacks specifics**

**Causes:**

1. Limited engagement history
2. Prompt not specific enough
3. Missing key context

**Fix:**

1. Add more specific prompts about what to look for
2. Include additional data sources (timeline events, notes)
3. Ask AI to highlight unknowns or gaps
4. Request specific questions for kickoff call

### Timeline Events Not Creating

**Events fail to create**

**Causes:**

1. Missing permissions
2. Event type name invalid
3. Target object ID wrong

**Fix:**

1. Verify "Write Timeline Events" permission
2. Use lowercase with underscores for event type
3. Check execution log for exact error
4. Verify object IDs are correct

***

## Tips & Best Practices

**✅ Do:**

* Test with closed-won test deals first
* Include engagement limit (50 is reasonable)
* Create distinct event types for each milestone
* Log events to both deal and contact
* Include complexity assessment
* Provide success team with full context
* Track which engagements matter most (demos, technical calls)

**❌ Don't:**

* Assume primary contact is always first in array (add validation)
* Skip error handling for missing associations
* Create generic onboarding plans (use specific context)
* Forget to notify success team
* Overwhelm with too many timeline events
* Include sensitive sales notes in onboarding plan

**Performance tips:**

* Engagement retrieval is fast (under 2 seconds)
* LLM analysis takes 5-10 seconds with full context
* Consider limiting engagement count for very old deals
* Cache onboarding templates for common scenarios

**Success metrics to track:**

* Time from deal close to onboarding kickoff
* Onboarding completion rate by complexity level
* Accuracy of AI timeline predictions
* Success team satisfaction with plan quality

***

## Related Resources

**Actions used:**

* [Lookup HubSpot Object (V2)](../actions/hubspot-v2-lookup-object)
* [Get Engagements (V2)](../actions/hubspot-v2-get-engagements)
* [Create Timeline Event (V2)](../actions/hubspot-v2-create-timeline-event)

**Related workflows:**

* [HubSpot Deal Analysis](./hubspot-deal-analysis) - Similar AI analysis with loops
* [HubSpot Contact Enrichment](./hubspot-contact-enrichment) - Webhook-triggered automation

***

**Last Updated:** 2025-10-01


# HubSpot Deal Analysis
Source: https://docs.agent.ai/recipes/hubspot-deal-analysis

Automatically analyze deals using AI, review timeline history, and update records with health scores and next-step recommendations

Automatically analyze deals using AI, review timeline history, and update records with health scores and next-step recommendations.

**What it does:** Finds deals in a specific stage, analyzes each one using AI and historical data, then updates the deal with insights.

**Common uses:**

* Daily deal health checks
* Pipeline review automation
* Identify at-risk deals
* Generate AI-powered next steps
* Scale deal analysis across entire pipeline

**Complexity:** Intermediate - Uses search, loops, AI analysis, and updates

***

## Overview

This workflow combines HubSpot data with AI analysis to automatically assess deal health. For each deal in your target stage, it:

1. Searches for deals in a specific stage
2. Loops through each deal
3. Gets timeline events for historical context
4. Sends deal data + timeline to AI for analysis
5. Updates the deal with AI-generated insights

**Result:** Every deal gets a health score, risk assessment, and recommended next steps automatically.

***

## What You'll Need

### HubSpot Setup

**Custom Properties** (create these in HubSpot → Settings → Properties → Deals):

* `ai_health_score` (Number) - Stores 1-10 health rating
* `ai_risks` (Multi-line text) - Stores identified risks
* `ai_next_steps` (Multi-line text) - Stores recommended actions
* `ai_close_likelihood` (Single-line text) - Stores probability assessment

**Permissions:**

* Read Deals
* Write Deals
* Read Timeline Events

### Agent.AI Setup

**Actions needed:**

* Search HubSpot (V2)
* For Loop
* Get Timeline Events (V2)
* Invoke LLM (or Generate Content)
* Update HubSpot Object (V2)
* End Loop

**LLM Access:**

* OpenAI, Anthropic, or other LLM provider configured

***

## Step-by-Step Setup

### Step 1: Add a Trigger

Choose how to run this workflow:

**Option A: Scheduled (Recommended)**

* Trigger: Schedule
* Frequency: Daily at 9:00 AM
* Use for: Regular pipeline health checks

**Option B: Manual**

* Trigger: Manual
* Use for: On-demand analysis

### Step 2: Search for Target Deals

**Add action:** Search HubSpot (V2)

**Configuration:**

* **Object Type:** Deals
* **Search Filters:** Click "+ Add Property"
  * Property: Deal Stage
  * Operator: Equals
  * Value: "presentationscheduled" (or your target stage)
* **Retrieve Properties:** Click "+ Add Property" and select:
  * `dealname`
  * `dealstage`
  * `amount`
  * `closedate`
  * `hs_object_id`
  * `pipeline`
  * `hubspot_owner_id`
* **Sort:** `-createdate` (newest first)
* **Limit:** 50 (adjust based on your needs)
* **Output Variable:** `target_deals`

**What this does:** Finds all deals in "Presentation Scheduled" stage (or whatever stage you chose), gets their key details.

### Step 3: Start Loop

**Add action:** For Loop

**Configuration:**

* **Loop through:** Click `{}` → select `target_deals`
* **Current item variable:** `current_deal`

**What this does:** Processes each deal one at a time.

### Step 4: Get Timeline Events

**Add action:** Get Timeline Events (V2)

**Configuration:**

* **Object Type:** Deals
* **Object ID:** Click `{}` → `current_deal` → `hs_object_id`
* **Event Type Filter:** Leave blank (get all events)
* **Output Variable:** `deal_timeline`

**What this does:** Gets the complete timeline history for the current deal (emails, calls, meetings, notes, custom events).

### Step 5: AI Analysis

**Add action:** Invoke LLM (or Generate Content)

**Configuration:**

* **Prompt:**

```
Analyze this deal and provide insights:

Deal Name: {{current_deal.dealname}}
Stage: {{current_deal.dealstage}}
Amount: ${{current_deal.amount}}
Close Date: {{current_deal.closedate}}

Timeline History:
{{deal_timeline}}

Please provide:
1. Deal health score (1-10, where 10 is healthiest)
2. Key risks or concerns
3. Recommended next steps (3-5 specific actions)
4. Likelihood to close (percentage or descriptive)

Return as JSON with keys: health_score, risks, next_steps, close_likelihood
```

* **Model:** gpt-4 (or your preferred LLM)
* **Output Variable:** `deal_insights`

**What this does:** AI analyzes the deal using all available context and generates actionable insights.

**Tip:** Adjust the prompt to match your sales process. Ask about specific things that matter to your team.

### Step 6: Update Deal with Insights

**Add action:** Update HubSpot Object (V2)

**Configuration:**

* **Object Type:** Deals
* **Identify by:** Lookup by Object ID
* **Identifier:** Click `{}` → `current_deal` → `hs_object_id`
* **Update Properties:** Click "+ Add Property" and select your custom properties:
  * `ai_health_score`: Click `{}` → `deal_insights` → `health_score`
  * `ai_risks`: Click `{}` → `deal_insights` → `risks`
  * `ai_next_steps`: Click `{}` → `deal_insights` → `next_steps`
  * `ai_close_likelihood`: Click `{}` → `deal_insights` → `close_likelihood`
* **Output Variable:** `updated_deal`

**What this does:** Saves AI insights back to the deal record so your team can see them in HubSpot.

### Step 7: Close the Loop

**Add action:** End Loop

**What this does:** Marks the end of the loop. Workflow jumps back to Step 3 and processes the next deal.

### Step 8 (Optional): Send Summary

**Add action:** Send Email (after the loop)

**Configuration:**

* **To:** Your email or sales team email
* **Subject:** "Deal Analysis Complete"
* **Body:** "Analyzed and updated insights for all deals in Presentation Scheduled stage."

**What this does:** Notifies you when the workflow finishes.

***

## How It Works

**Execution flow:**

1. **Search** finds 50 deals in "Presentation Scheduled" stage → saves to `target_deals`
2. **For Loop** starts with first deal → `current_deal` = Deal #1
3. **Get Timeline Events** retrieves history for Deal #1 → saves to `deal_timeline`
4. **Invoke LLM** analyzes Deal #1 + timeline → saves insights to `deal_insights`
5. **Update** writes insights back to Deal #1 in HubSpot
6. **End Loop** → Jump back to step 2, `current_deal` = Deal #2
7. Repeat until all 50 deals are analyzed
8. **Send Email** (optional) notifies team

**Example timeline:** 50 deals × \~5 seconds per deal = \~4 minutes total

***

## Example Output

### What the AI Generates

**For a deal named "Acme Corp - Enterprise License":**

```json  theme={null}
{
  "health_score": 7,
  "risks": "Customer has not responded to follow-up in 5 days. Technical questions from demo suggest potential integration concerns. Close date is 30 days away but no next meeting scheduled.",
  "next_steps": "1. Send follow-up email addressing technical questions\n2. Offer integration consultation call with solutions engineer\n3. Share case study from similar customer in manufacturing industry\n4. Schedule technical deep-dive meeting\n5. Create custom proposal addressing integration concerns",
  "close_likelihood": "Medium-High (65%)"
}
```

### What Appears in HubSpot

In the deal record, you'll see:

* **AI Health Score:** 7
* **AI Risks:** "Customer has not responded to follow-up in 5 days..."
* **AI Next Steps:** "1. Send follow-up email... 2. Offer integration consultation..."
* **AI Close Likelihood:** "Medium-High (65%)"

Sales reps can see these insights directly on the deal record and take action.

***

## Customization Ideas

### Different Target Stages

Change which stage to analyze:

* **Search Filter Value:** Change from "presentationscheduled" to:
  * "qualifiedtobuy" - Recently qualified deals
  * "decisionmakerboughtin" - Deals nearing close
  * "contractsent" - Contracts waiting for signature

### Multiple Stages

Run separate workflows for different stages, or add an If Condition inside the loop to handle different stages differently.

### Different AI Focus

Customize the LLM prompt for different analysis types:

**For early-stage deals:**

```
Focus on: qualification quality, budget alignment, decision maker access
```

**For late-stage deals:**

```
Focus on: contract negotiation status, closing risks, urgency signals
```

**For stalled deals:**

```
Focus on: reasons for stall, re-engagement strategies, win-back probability
```

### Add Filters

Only analyze deals meeting certain criteria:

**After Get Timeline Events, add If Condition:**

* Condition: Check if timeline has any events in last 7 days
* If no recent activity → Tag as "stalled"
* If has activity → Run AI analysis

### Segment by Owner

**After Search, add another loop:**

* Group deals by `hubspot_owner_id`
* Send each owner a summary of their deals

***

## Troubleshooting

### No Deals Found

**Search returns empty array**

**Causes:**

1. No deals in that stage
2. Wrong stage name (check exact value in HubSpot)
3. Missing permissions

**Fix:**

1. Check HubSpot - do deals exist in that stage?
2. Get exact stage value: Go to HubSpot → Deal → Check "Deal Stage" property
3. Verify "Read Deals" permission

### AI Insights Not Formatted Correctly

**Deal properties contain raw JSON or malformed text**

**Causes:**

1. LLM didn't follow JSON format instruction
2. Template variable rendering issue

**Fix:**

1. Make prompt more explicit: "Return ONLY valid JSON, nothing else"
2. Test with a single deal first
3. Try different LLM model (GPT-4 better at structured output than GPT-3.5)
4. Parse JSON in a Set Variable action before updating

### Custom Properties Not Found

**Error: "Property 'ai\_health\_score' does not exist"**

**Causes:**

1. Custom properties not created in HubSpot
2. Properties created but not for Deals object

**Fix:**

1. Go to HubSpot → Settings → Properties → Deals
2. Create custom properties:
   * `ai_health_score` (Number, 0-10)
   * `ai_risks` (Multi-line text)
   * `ai_next_steps` (Multi-line text)
   * `ai_close_likelihood` (Single-line text)
3. Save and try again

### Timeline Too Long

**LLM times out or returns incomplete response**

**Causes:**

1. Timeline has hundreds of events
2. Exceeding token limit

**Fix:**

1. Add result limit to Get Timeline Events action
2. Filter by date range (last 30 days)
3. Filter by event type (only important events)
4. Use LLM with larger context window

### Loop Takes Too Long

**Workflow times out**

**Causes:**

1. Too many deals (1000+)
2. LLM calls are slow

**Fix:**

1. Reduce search limit to 50-100 deals
2. Run multiple smaller workflows instead of one large one
3. Filter deals by date (only deals from last 30 days)

***

## Tips & Best Practices

**✅ Do:**

* Start with small search limit (10-20 deals) to test
* Review AI-generated insights for a few deals before scaling
* Adjust prompt based on what your team actually needs
* Create custom properties in HubSpot before running workflow
* Use scheduled trigger for daily automated analysis
* Monitor execution logs to see how long each deal takes

**❌ Don't:**

* Analyze thousands of deals at once (splits into batches)
* Forget to create custom properties in HubSpot first
* Use vague prompts (be specific about what you want)
* Skip testing with a few deals first
* Analyze the same stage multiple times a day (redundant)

**Cost optimization:**

* LLM calls cost money - monitor usage
* Use cheaper models (GPT-3.5) for simple analysis
* Limit timeline events to reduce tokens
* Only analyze deals that changed recently (add date filter)

***

## Related Resources

**Actions used:**

* [Search HubSpot (V2)](../actions/hubspot-v2-search-objects)
* [For Loop](../actions/for_loop)
* [Get Timeline Events (V2)](../actions/hubspot-v2-get-timeline-events)
* [Update HubSpot Object (V2)](../actions/hubspot-v2-update-object)
* [End Loop](../actions/end_statement)

**Related workflows:**

* [HubSpot Contact Enrichment](./hubspot-contact-enrichment) - Similar pattern for contacts
* [HubSpot Customer Onboarding](./hubspot-customer-onboarding) - Multi-stage workflow example

***

**Last Updated:** 2025-10-01


# LinkedIn Research Agent
Source: https://docs.agent.ai/recipes/linkedin-research-agent

How to build a LinkedIn Research agent

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


# Community-Led Recipes
Source: https://docs.agent.ai/recipes/overview



This section features a mix of agent recipes shared by the [Agent.ai](http://Agent.ai) community. Some are straightforward walkthroughs to help you build useful agents fast. Others take a more unconventional route — creative workarounds that push the platform in unexpected ways.

These recipes aren’t official product guides. They’re built by users, for users — showcasing how real people are solving problems with [Agent.ai](http://Agent.ai).

## What You’ll Find

* **Quick-start tutorials** for building useful agents
* **Creative logic chains** that stretch what agents can do
* **Ideas to customize and remix** for your own workflows

Use them as-is or as a jumping-off point. Want to share one? [Join the community](https://community.agent.ai) and tell us what you’ve built.


# Calling Agents from Salesforce (SFDC)
Source: https://docs.agent.ai/recipes/salesforce



This guide walks you through integrating [Agent.ai](http://Agent.ai)'s intelligent agents directly within Salesforce without requiring external code. By setting up Named Credentials and creating a Flow with HTTP callouts, you'll enable your Salesforce instance to seamlessly communicate with [Agent.ai](http://Agent.ai)'s services. This integration allows your agents to respond to record creation events, process data from your Salesforce objects, and write results back to your records—all while maintaining the security and governance controls of your Salesforce environment. Follow these step-by-step instructions to set up this powerful integration in under 30 minutes.

## Before You Begin

Before setting up the Salesforce integration with [Agent.ai](http://Agent.ai), ensure you have:

**Tested Your Agent with cURL:**

Verify your [Agent.ai](http://Agent.ai) webhook is functional by testing it with cURL first. This confirms the endpoint is working and helps you understand the expected request/response format:

```bash  theme={null}
curl -L -X POST -H 'Content-Type: application/json' \
'https://api-lr.agent.ai/v1/agent/YOUR_AGENT_ID/webhook/YOUR_WEBHOOK_ID' \
-d '{"input_name":"Test User"}'
```

Save this cURL command and response for reference during setup.

1. **API Access in Salesforce**: Ensure the Salesforce users who will be configuring and using this integration have:
   * "API Enabled" permission
   * "Modify All Data" or appropriate object-level permissions
   * Access to create and modify Flows
   * Permission to create Named Credentials
2. **Required Information**:
   * Your complete [Agent.ai](http://Agent.ai) webhook URL
   * The expected request payload structure
   * The response format from your agent
   * Salesforce fields you want to use for input/output
3. **Salesforce Edition**: Confirm you're using a Salesforce edition that supports Named Credentials and Flows (Enterprise, Unlimited, Developer, or Performance).

Taking these preparatory steps will significantly streamline the integration process and help avoid common setup issues.

## Creating Credentials

### **1. Create External Credentials**

1. Navigate to Setup → Named Credentials → External Credentials (Tab) → New
2. Fill in the required fields (remember: Name must NOT contain spaces)
3. Select **No Authentication** from the dropdown
4. Save your settings

### **2. Create Named Credentials**

1. Navigate to **Setup → Named Credentials → Named Credentials (Tab) → New**
2. Complete the form with:
   * Label: A descriptive name (e.g., "AgentAI Named Credential")
   * Name: Same as label without spaces
   * URL: Your [Agent.ai](http://Agent.ai) endpoint (e.g., "[<u>https://api-lr.agent.ai</u>](https://api-lr.agent.ai)")
   * Enable "Enabled for Callouts"
   * Select your External Credential from the dropdown
   * Check "Generate Authorization Header"
   * Set Outbound Network Connection to "--None--"
   * Save your settings

### **3. Create Principal for Named Credentials**

1. Navigate to **Setup → Named Credentials → "AgentAI External Credential" → Principals → New**
2. Complete the form:
   * Parameter Name: A descriptive name
   * Sequence Number: 1
   * Identity Type: "Named Principal"
   * Save your settings

### **4. Create a Permission Set for External Credentials**

1. Navigate to **Setup → Permission Sets → New**
2. Enter permission set details:
   * Label: "AgentAI External Credentials Permissions"
   * API Name: Should auto-populate
   * Save your settings

### **5. Assign Permissions**

1. Navigate to Setup → Permission Sets → "AgentAI External Credentials Permissions" → Manage Assignments
2. Click **Add Assignment**
3. Select users who need access
4. Click **Next** (no expiration date needed)
5. Click **Assign**

### **6. Manage Permissions in Permission Set**

1. Navigate to **Setup → Permission Sets → "AgentAI External Credentials Permissions" → External Credential Principal Access**
2. Click **Edit**
3. Enable the Credential Principal
4. Save your settings
5. *Verify your configuration*

## Creating The Flow

### **1. Create Record Triggered Flow**

1. Navigate to **Setup → Flows → New Flow**
2. Select **Record Triggered Flow**
3. Choose **When A Record Is Created**
4. Set to optimize for "Action and Related Records"
5. Check "Include a Run Asynchronously path to access an external system after the original transaction for the triggering record is successfully committed"

### **2. Create HTTP Callout Action**

1. Click **Add Element**
2. Select **Action**
3. Find and select **Create HTTP Callout** (scroll to the bottom of the list)

### **3. Create External Service**

* Give your service a name (alphanumeric values only)

  **Note:** Use version names if creating multiple services
* Select your Named Credential from the dropdown
* Save your settings

### **4. Create Invokable Action**

1. Set Method to **POST**
2. Enter URL Path to your Agent webhook endpoint
   * Example: /v1/agent/kkmiv48izo6wo7fk/webhook/b45b7a8e
3. For Sample JSON Request, copy from your webhook example:
   * Example: `{"input_name":"REPLACE_ME"}`
4. Ignore any error that appears
5. Click **Review**
6. Confirm data structure is detected (input\_name as String)
7. Click **Connect for Schema**
8. Click **Connect**
9. Review return types match what your Agent returns
10. Name the Action for your external service

### **6. Assign Body Payload Parameters**

1. Click **Assign → Set Variable Values**
2. Select data to pass to agent:
   * Variable: agentRequestBody > input\_name
   * Operator: Equals
   * Value: Choose your field (e.g., Triggering Lead > First Name)
3. Save your settings

### **7. Save and Refresh The Page**

1. Save your flow to update the UI with new values

### **8. Set Up Response Handling**

1. Select the **Flow Action → Show Advanced Options → Store Output Values**
2. For 2XX responses, create a new resource
3. For Default Exception, create a new resource (Text type)
4. For Response Code, create a new resource (Number, 0 decimal places)
5. Save to finalize resource names

### **9. Assign Values from API Call to Objects**

1. After the HTTP Request Action, create an Assignment
2. Update the triggering record:
   * **Field:** The field you want to update (e.g., Greeting\_Phrase\_\_c)
   * **Value:** responseBodyOut2XX > response
3. **Note:** responseBodyOut2XX contains all output objects from your Agent

### **10. Test Your Flow**

1. Save your flow
2. Click **Debug**
3. Select **Run Asynchronously**
4. Select a record to test with
5. Run the flow and verify the results

## Debug Checklist

Use this checklist to troubleshoot if your [Agent.ai](http://Agent.ai) integration isn't working properly:

* **External Credentials**: Verify name contains no spaces and "No Authentication" is selected
* **Named Credentials**: Confirm URL is correct and "Enabled for Callouts" is checked
* **Principal**: Check that Principal is created with correct sequence number
* **Permission Set**: Ensure External Credential Principal is enabled
* **User Assignments**: Confirm relevant users have the permission set assigned
* **Flow Trigger**: Verify flow is set to trigger on the correct object and event
* **HTTP Callout**: Check that the webhook URL path is correct
* **Request Body**: Confirm input parameters match what your Agent expects (e.g., "input\_name")
* **Response Handling**: Ensure output variables are correctly mapped
* **Field Updates**: Verify targeted fields exist and are accessible for updates
* **Asynchronous Execution**: Confirm "Include to Run Asynchronously" is checked
* **External Service**: Check Named Credential is properly selected in External Service
* **Flow Activation**: Make sure the flow is activated after testing
* **Agent Webhook**: Verify your [Agent.ai](http://Agent.ai) webhook endpoint is active and responding
* **SFDC Logs**: Review debug logs for any callout errors

If issues persist, check your SFDC debug logs for specific error messages and verify that your [Agent.ai](http://Agent.ai) webhook is responding as expected with proper formatting.

## Conclusion

Congratulations! You've successfully integrated [Agent.ai](http://Agent.ai) with Salesforce using native SFDC capabilities, eliminating the need for middleware or custom code. This integration creates a powerful automation pipeline that leverages AI agents to enhance your Salesforce experience. As records are created in your system, they now automatically trigger intelligent processing through your [Agent.ai](http://Agent.ai) webhooks, with results flowing seamlessly back into your Salesforce records. This approach maintains Salesforce's security model while expanding its capabilities with [Agent.ai](http://Agent.ai)'s intelligence.

Consider extending this implementation by creating additional flows for different record types, implementing decision branches based on agent responses, or adding more complex data transformations. As you grow comfortable with this integration, you can enhance it to support increasingly sophisticated business processes, bringing the power of [Agent.ai](http://Agent.ai) to all aspects of your Salesforce implementation. Remember to monitor your usage and performance to ensure optimal operation as your integration scales.


# Data Security & Privacy at Agent.ai
Source: https://docs.agent.ai/security-privacy

Agent.ai prioritizes your data security and privacy with full encryption, no data reselling, and transparent handling practices. Find out how we protect your information while providing AI agent services and our current compliance status.

## **Does Agent.ai store information submitted to agents?**

Yes, Agent.ai stores the inputs you submit and the outputs you get when interacting with our agents. This is necessary to provide you with a seamless experience and to ensure continuity in your conversations with our AI assistants.

## **How we handle your data**

* **We store inputs and outputs**: Your conversations and data submissions are stored to maintain context and conversation history.

* **We don't share or resell your data**: Your information remains yours—we do not sell, trade, or otherwise transfer your data to outside parties.

* **No secondary use**: The data you share is not used to train our models or for any purpose beyond providing you with the service you requested.

* **Comprehensive encryption**: All user data—both inputs and outputs—is fully encrypted in transit using industry-standard encryption protocols.

## **Third-party LLM providers and your data**

When you interact with agents on Agent.ai, your information may be processed by third-party Large Language Model (LLM) providers, depending on which AI model powers the agent you're using.

* **API-based processing**: Agent.ai connects to third-party LLMs via their APIs. When you submit data to an agent, that information is transmitted to the relevant LLM provider for processing.

* **Varying privacy policies**: Different LLM providers have different approaches to data privacy, retention, and usage. The handling of your data once it reaches these providers is governed by their individual privacy policies.

* **Considerations for sensitive data**: When building or using agents that process personally identifiable information (PII), financial data, health information, or company-sensitive information, we recommend:

  * Reviewing the specific LLM provider's privacy policy

  * Understanding their data retention practices

  * Confirming their compliance with relevant regulations (HIPAA, GDPR, etc.)

  * Considering data minimization approaches where possible

Agent.ai ensures secure transmission of your data to these providers through encryption, but we encourage users to be mindful of the types of information shared with agents, especially for sensitive use cases.

## **Our commitment to your privacy**

At Agent.ai, we believe that privacy isn't just a feature—it's a fundamental right. Our approach to data security reflects our core company values:

**Trust**: We understand that meaningful AI assistance requires sharing information that may be sensitive or confidential. We honor that trust by implementing rigorous security measures and transparent data practices.

**Respect**: Your data belongs to you. Our business model doesn't rely on monetizing your information—it's built on providing value through our services.

**Integrity**: We're straightforward about what we do with your data. We collect only what's necessary to provide our services and use it only for the purposes you expect.

## **Intellectual Property Rights for Agent Builders**

When you create an agent on Agent.ai, you retain full ownership of the intellectual property (IP) associated with that agent. Similar to sellers on marketplace platforms (Amazon, Etsy), Agent.ai serves as the venue where your creation is hosted and discovered, but the underlying IP remains your own. This applies to the agent's concept, design, functionality, and unique implementation characteristics.

* **Builder ownership**: You maintain ownership rights to the agents you build, including their functionality, design, and purpose

* **Platform hosting**: Agent.ai provides the infrastructure and marketplace for your agent but does not claim ownership of your creative work

* **Content responsibility**: As the owner, you're responsible for ensuring your agent doesn't infringe on others' intellectual property

For complete details regarding intellectual property rights, licensing terms, and usage guidelines, please review our [Terms of Service](https://www.agent.ai/terms). Our approach to IP ownership aligns with our broader commitment to respecting your rights and fostering an ecosystem where builders can confidently innovate.

## **Compliance and certifications**

Agent.ai does not currently hold specific industry certifications such as SOC 2, HIPAA compliance, ISO 27001, or other specialized security and privacy certifications. While our security practices are robust and our encryption protocols are industry-standard, organizations with specific regulatory requirements should carefully evaluate whether our current security posture meets their compliance needs. If your organization requires specific certifications for data handling, we recommend reviewing our security documentation or contacting our team to discuss whether our platform aligns with your requirements.

## **Security measures**

Our encryption and security protocols are regularly audited and updated to maintain the highest standards of data protection. We implement multiple layers of technical safeguards to ensure your information remains secure throughout its lifecycle on our platform.

If you have specific concerns about data security or would like more information about our privacy practices, please contact our support team who can provide additional details about our security infrastructure.


# Agent Run History
Source: https://docs.agent.ai/user/agent-runs



The [**Agent Runs**](https://agent.ai/user/agent-runs) page shows a history of your agent executions—past and scheduled—so you can review when agents were triggered, what they responded with, and optionally leave feedback.

### Past Runs

In this tab, you can see:

* The **execution date** (timestamp in GMT)
* The **agent name**
* A preview of the response
* Any feedback you’ve left on the run

<Tip>
  Click any agent response to view the full output.
</Tip>

<img src="https://mintcdn.com/agentai/124P12t85CIi-2hH/images/agent-runs1.png?fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=5f549de1c7bd0f608eb8fa299b52fb33" alt="Agent Runs1 Pn" data-og-width="2522" width="2522" data-og-height="1092" height="1092" data-path="images/agent-runs1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/124P12t85CIi-2hH/images/agent-runs1.png?w=280&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=80066cba665093eb6e62236823c8d61a 280w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/agent-runs1.png?w=560&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=570bf4c6c217e767a147145c0505c481 560w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/agent-runs1.png?w=840&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=ffb57bdea1507fd29d0917f8c62471e7 840w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/agent-runs1.png?w=1100&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=21df924ab6d004d2976128ff87979ed4 1100w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/agent-runs1.png?w=1650&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=323dff85aaa532d4b77e2c7e346ade6b 1650w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/agent-runs1.png?w=2500&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=603f483a07d66bac5ef6c481808db590 2500w" />

### Scheduled Runs

The **Scheduled Runs** tab shows agents that are set to run on a recurring schedule. You can **update how often they run** or **delete the scheduled run** if it’s no longer needed.

<img src="https://mintcdn.com/agentai/124P12t85CIi-2hH/images/agent-runs2.png?fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=2ab16bc41debdf87e7a077f0217e7406" alt="Agent Runs2 Pn" data-og-width="2522" width="2522" data-og-height="804" height="804" data-path="images/agent-runs2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/124P12t85CIi-2hH/images/agent-runs2.png?w=280&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=6197df544fee87cf14be4bbffaacf573 280w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/agent-runs2.png?w=560&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=4c5789bf6eef39f6864a0b28f2e18a8f 560w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/agent-runs2.png?w=840&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=0045e4db423b7766b8c60ba3050bafa9 840w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/agent-runs2.png?w=1100&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=d7c81180fb6e49bd4a6caa6662bb9c78 1100w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/agent-runs2.png?w=1650&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=c892d8135d017663688d5923d7f2ec3c 1650w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/agent-runs2.png?w=2500&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=fe43e8f7a680b783b154e2b581f8ad9d 2500w" />

Questions about a recent agent run? Reach out to our [support team](https://agent.ai/feedback).


# Adding Agents to Your Team
Source: https://docs.agent.ai/user/agent-team



The [**Agents Team**](https://agent.ai/user/team) page shows agents you’ve added to your team—this functions like a **bookmark list** for quick access to agents you use frequently.

When you mark an agent as part of your team, it’s saved to this view for easy access. Click **Go** to run any agent on your team.

To **remove** an agent from your team, just click the **Team** button again to uncheck it.

<Tip>
  Think of an agent team as your saved agent library.
</Tip>

<img src="https://mintcdn.com/agentai/124P12t85CIi-2hH/images/agent-team.png?fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=a565bc9c7138ca0a3746ed9d9ffa2287" alt="Agent Team Pn" data-og-width="2304" width="2304" data-og-height="1250" height="1250" data-path="images/agent-team.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/124P12t85CIi-2hH/images/agent-team.png?w=280&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=dad03112f23e11ec735ac56f7bc8aa5f 280w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/agent-team.png?w=560&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=ed5e47fe02ab7c1f107c5570c6c64427 560w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/agent-team.png?w=840&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=8752f7260cbf662870f423cc14574088 840w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/agent-team.png?w=1100&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=c184942e03dbd5eb94380d36d72ea0e2 1100w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/agent-team.png?w=1650&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=38b3dde3d0a19d1f1026135ff7128fb9 1650w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/agent-team.png?w=2500&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=2a52212967eddf58e2d00907b728ec46 2500w" />

Reach out to our [support team](https://agent.ai/feedback) if you need any help with your agent team.


# Integrations
Source: https://docs.agent.ai/user/integrations

Manage your third-party integrations, API credentials, and MCP settings.

## Vendors

Connect third-party services like X, Google, and HubSpot to unlock agent actions powered by your own data.

From [**this page**](https://agent.ai/user/integrations#vendors), you can:

* Add, reconnect, or disconnect integrations
* Set a default account (for email or portal use)
* View agent-specific access when applicable

### **X Connection**

Connect your X (formerly Twitter) account to create a public **builder profile** and enable agents to perform X-specific actions like retrieving X accounts or posts.

* Your builder email alias will be based on your handle (e.g. [**yourhandle@agent.ai**](mailto:yourhandle@agent.ai))
* Click **Reconnect** or **Disconnect** to manage access

### **Google Connections**

Connect your Google account to enable agents to perform actions like creating Google Docs.

* Add multiple accounts and set a **default email**
* Click **Connect More Accounts** to add others
* Use **Reconnect** or **Disconnect** as needed

### **HubSpot Connections**

Connect your HubSpot portal to enable agents to perform CRM-related actions, including working with contacts and companies. You can connect to multiple HubSpot portals and:

* Set a **default portal**
* View which agents have private access to your portal
* Click **Connect More Portals** to add additional HubSpot accounts

<img src="https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/vendors.png?fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=2e65c0653329251f9d7a42b68ea474c1" alt="Vendors Pn" data-og-width="2764" width="2764" data-og-height="1238" height="1238" data-path="images/vendors.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/vendors.png?w=280&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=f2664fca599ac591a1e177bdc9917fb8 280w, https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/vendors.png?w=560&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=051a205b4264c410082759e6a646170a 560w, https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/vendors.png?w=840&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=57d7d2c3cfd9bd73b3067de1916b20d7 840w, https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/vendors.png?w=1100&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=9f58518be4e24edf47d96a5532a8c3ef 1100w, https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/vendors.png?w=1650&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=4607fcf44e58e6d244e467b04593eae6 1650w, https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/vendors.png?w=2500&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=d3ef7f5496629f5aa1dec2c9bd50f74a 2500w" />

## API

Your [API key](https://agent.ai/user/integrations#api) allows you to integrate [**Agent.ai**](http://Agent.ai) features directly into your own tools and workflows. You’ll find:

* Your **API key**
* Sample curl requests
* A link to the [**Agent.ai** API documentation](https://docs.agent.ai/welcome)

<Warning>
  Keep your API key private. It grants access to your [**Agent.ai**](http://Agent.ai) account and credit usage—treat it like a password. Don’t share it or commit it to public repositories.
</Warning>

<img src="https://mintcdn.com/agentai/124P12t85CIi-2hH/images/apiupdated.png?fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=2adb245de837217018a0024e7c8df61b" alt="Apiupdated Pn" data-og-width="2654" width="2654" data-og-height="1118" height="1118" data-path="images/apiupdated.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/124P12t85CIi-2hH/images/apiupdated.png?w=280&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=eca580cc811a4fe5e71f2846830b2d87 280w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/apiupdated.png?w=560&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=8d8ca7c01c634748b457361493503dde 560w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/apiupdated.png?w=840&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=d4faa246df333349164646276cc9efaf 840w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/apiupdated.png?w=1100&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=fe365d98d9165dce10ad6f4e303496ae 1100w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/apiupdated.png?w=1650&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=3a393a547e1af5eb8cc61a06db09a920 1650w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/apiupdated.png?w=2500&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=e7274bc7dc7359455c1adc3967402d85 2500w" />

## MCP

Use the [MCP tab](https://agent.ai/user/integrations#mcp) to configure your [Agent.ai](http://Agent.ai) MCP server and manage which agents are available to external tools that support MCP, like Claude Desktop. You can also add additional MCP servers from this page and use [Agent.ai](http://Agent.ai) as an MCP client.

### [Agent.ai](http://Agent.ai) MCP Tools Listing Settings

Choose which agents you’d like to expose to your MCP environment:

* **Action Agents** (default)
* My Team Agents
* Private Agents
* Top Public Agents (rating > 4.2, reviews > 3)

Check the boxes you want, then click **Save**.

<img src="https://mintcdn.com/agentai/124P12t85CIi-2hH/images/mcp1updated.png?fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=681ac51e8ce7b8a122399d065d58f4cd" alt="Mcp1updated Pn" data-og-width="2642" width="2642" data-og-height="1042" height="1042" data-path="images/mcp1updated.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/124P12t85CIi-2hH/images/mcp1updated.png?w=280&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=03a33bd678540b9929dc8ebae7ecb0e7 280w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/mcp1updated.png?w=560&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=697eb94179f1bf3bd4041310f0ae980d 560w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/mcp1updated.png?w=840&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=515cf141dac3a1d91bac51e975c419ae 840w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/mcp1updated.png?w=1100&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=ad0d5d18759362d45dbd5c49b4f91e33 1100w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/mcp1updated.png?w=1650&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=a598635a70eea9e2f9652740b1de2192 1650w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/mcp1updated.png?w=2500&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=82b72aeeb65df30324f1b2d4d02de8cc 2500w" />

### Connection Methods

Use simple URL-based configuration to connect [Agent.ai](http://Agent.ai) to MCP clients (recommended) or use the provided config block to your MCP configuration file.

You can also add external MCP servers to use within Agent.ai (more below).

For full setup instructions, see the [**MCP Integration Guide**](https://docs.agent.ai/mcp-server).

<img src="https://mintcdn.com/agentai/124P12t85CIi-2hH/images/mcp2updated.png?fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=dd7d1034b7941de4720773ed0e7c39a9" alt="Mcp2updated Pn" data-og-width="2650" width="2650" data-og-height="1492" height="1492" data-path="images/mcp2updated.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/124P12t85CIi-2hH/images/mcp2updated.png?w=280&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=f5f4f66706d5f420e5d74975273850f6 280w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/mcp2updated.png?w=560&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=1c04e3a71b7c1b2f61fead98ffe7d2d6 560w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/mcp2updated.png?w=840&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=1d64986d976f1128ca2b4523ea770925 840w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/mcp2updated.png?w=1100&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=3ce8982b2248b5a07eb1fdbf394deb9d 1100w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/mcp2updated.png?w=1650&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=bcae47c5a8127835661ea0529c724438 1650w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/mcp2updated.png?w=2500&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=86f5e1e96a444702b9e38c87e927c6a6 2500w" />

## MCP Chat

After adding MCP servers to Agent.ai, you can select them and chat with them in [MCP Chat](https://agent.ai/user/integrations#mcpchat).

<img src="https://mintcdn.com/agentai/124P12t85CIi-2hH/images/mcpchat.png?fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=2b529b859c06a866cb9ce8ae0659a6a6" alt="Mcpchat Pn" data-og-width="2672" width="2672" data-og-height="1090" height="1090" data-path="images/mcpchat.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/124P12t85CIi-2hH/images/mcpchat.png?w=280&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=df07fe1f3d9c535f174d21825dedf31a 280w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/mcpchat.png?w=560&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=0ad2c261b9a76cd57d2dd0d59ab675a3 560w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/mcpchat.png?w=840&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=5e99e2a210d18a7c4b199d73a13b0fcd 840w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/mcpchat.png?w=1100&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=b2c21db68ca4713a731ebfc021b2cdd1 1100w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/mcpchat.png?w=1650&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=a9b09a4bca45bf55899d40c5a7a57c6f 1650w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/mcpchat.png?w=2500&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=94b9e4208633b19de79ea1551c0a5f8b 2500w" />

Reach out to our [**support team**](https://agent.ai/feedback) if you have any questions about integrations or navigating [Agent.ai](http://Agent.ai).


# Profile Management
Source: https://docs.agent.ai/user/profile

Create a builder profile to join the Agent.ai builder network or edit your existing profile details.

To create your builer profile:

1. Click the profile icon in the top-right corner of [Agent.ai](http://Agent.ai)
2. Select **Create Public Profile**
3. Click **Create profile** or **Connect to X**

<img src="https://mintcdn.com/agentai/124P12t85CIi-2hH/images/profile1.png?fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=07259003eb0e9ceec0ee736aa9dcc0ea" alt="Profile1 Pn" data-og-width="2404" width="2404" data-og-height="1342" height="1342" data-path="images/profile1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/124P12t85CIi-2hH/images/profile1.png?w=280&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=40480058bb14dac7f6764cfdd07f45f8 280w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/profile1.png?w=560&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=b1b1a3d87d920699c63064555712b98d 560w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/profile1.png?w=840&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=1710a7352d6b12db25c43d4633f5c2dc 840w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/profile1.png?w=1100&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=e5a31075fe963de3a2102f404e38f0b5 1100w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/profile1.png?w=1650&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=b65f97fbbeb332fb305f4947f38089f9 1650w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/profile1.png?w=2500&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=0084a94175dddedc8a732ce28046fa55 2500w" />

Your builder profile includes:

* Profile picture
* Username (required)
  * This will be your [Agent.ai](http://Agent.ai) handle
* Display name (required)
* About you
* Twitter handle

After updating these details, click **Save** to create your profile.

<img src="https://mintcdn.com/agentai/124P12t85CIi-2hH/images/profile2.png?fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=44420fca82299aa493c9c09d783eeffd" alt="Profile2 Pn" data-og-width="2350" width="2350" data-og-height="1506" height="1506" data-path="images/profile2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/124P12t85CIi-2hH/images/profile2.png?w=280&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=3891fa087644501d3eba2484d7dfdb4e 280w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/profile2.png?w=560&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=6172135fc42762403e13ce6b4cc66aa5 560w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/profile2.png?w=840&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=bc919bdc2b0a0967fd9bd9a1f90a3664 840w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/profile2.png?w=1100&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=d2d3b1c10a37852ff408d8f88d48e685 1100w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/profile2.png?w=1650&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=d9dc97324382d6726757f8c00bda3ac5 1650w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/profile2.png?w=2500&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=633a12f708820b3c5c919f8aa9389429 2500w" />

To edit an existing profile:

1. Click the profile icon in the top-right corner of [Agent.ai](http://Agent.ai)
2. Select **Profile**
3. Click **Edit Profile**

Reach out to our [**support team**](https://agent.ai/feedback) if you have any questions about your profile or navigating [Agent.ai](http://Agent.ai).


# Submit Agent Requests in Agent.ai
Source: https://docs.agent.ai/user/request-an-agent



Have an idea for a new agent? Head to the [Request an Agent](https://agent.ai/suggest-an-agent) page to suggest it. You can also get there from the profile navigation menu.

On this page, you can:

* Submit your own agent ideas
* Search and browse requests from other users
* Upvote ideas you support to help them get prioritized

<Tip>
  Clear, specific requests are more likely to get picked up by builders.
</Tip>

<img src="https://mintcdn.com/agentai/124P12t85CIi-2hH/images/request-agent-1.png?fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=ac0df4637c2c1963f77465702cb01b9e" alt="Request Agent 1 Pn" data-og-width="2870" width="2870" data-og-height="1504" height="1504" data-path="images/request-agent-1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/124P12t85CIi-2hH/images/request-agent-1.png?w=280&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=0fbec53c5dd651237d0af3aafaa0748f 280w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/request-agent-1.png?w=560&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=bfc20f20abc0186d8ce7e5b6a73b17db 560w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/request-agent-1.png?w=840&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=e3d03d763f680672fbdec06204973d47 840w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/request-agent-1.png?w=1100&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=bfe5dcb9da736b780ad93e99c2d94a36 1100w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/request-agent-1.png?w=1650&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=a7286fd70a3443b352d79b6c4a482012 1650w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/request-agent-1.png?w=2500&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=3a4cb14634c88f05102201e0126f342a 2500w" />

## How to Submit a Request

Click **Add a Request** to open the submission form. Then:

1. Give your idea a clear title
2. Describe what the agent should do (include examples if helpful)
3. Optionally select a category to help others find it
4. Click **Submit Post**

<img src="https://mintcdn.com/agentai/124P12t85CIi-2hH/images/request-agent-2.png?fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=3b697120098a5e3c2e4dca52978b960b" alt="Request Agent 2 Pn" data-og-width="2872" width="2872" data-og-height="1202" height="1202" data-path="images/request-agent-2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/124P12t85CIi-2hH/images/request-agent-2.png?w=280&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=01c4f70b9ca56f40ae1e0a6857aee9b0 280w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/request-agent-2.png?w=560&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=ad6bb03dcc074409de386bd87c058eb8 560w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/request-agent-2.png?w=840&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=f40f75a5dd3bdea6f062935a6250ab17 840w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/request-agent-2.png?w=1100&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=668437b86d4ac3f293f9099200d059d7 1100w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/request-agent-2.png?w=1650&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=921e27dfab41d1f1f0e1b03c4b90c428 1650w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/request-agent-2.png?w=2500&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=16d00d9303878abef5ba908f2c18bdd7 2500w" />

## What happens after you submit?

The [Agent.ai](http://Agent.ai) team regularly reviews top-voted requests and shares the most popular ideas with the builder community to help bring them to life.

Questions about submitting an agent request? Reach out to our [support team](https://agent.ai/feedback).


# User Settings in Agent.ai
Source: https://docs.agent.ai/user/settings



The User Settings page lets you manage your profile details, preferences, and integrations. From notifications to API credits, this is where you control how [Agent.ai](http://Agent.ai) works for you.

## User Context

Add basic info like your name, location, title, and role so agents can tailor their responses to your background and communication style.

To update your user context:

1. Go to **User Context** in your [profile settings](https://agent.ai/user/settings)
2. Fill out any fields you’d like agents to reference in their responses

<img src="https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/usercontextupdated.png?fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=c41220f9523d7af6d3c6ad1688286ff7" alt="Usercontextupdated Pn" data-og-width="2624" width="2624" data-og-height="944" height="944" data-path="images/usercontextupdated.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/usercontextupdated.png?w=280&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=accf261423ac4546c800b68df5598b23 280w, https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/usercontextupdated.png?w=560&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=7a33c19a9a12be26323e9a744089837d 560w, https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/usercontextupdated.png?w=840&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=262bb7037ba26c3e82cafeb62f224143 840w, https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/usercontextupdated.png?w=1100&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=739e716f98c1194de2a782fedbdbc0f5 1100w, https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/usercontextupdated.png?w=1650&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=5d8519a4ccbb6391fc9d8909d9b389e3 1650w, https://mintcdn.com/agentai/aY3WeNa_RVWXvaNU/images/usercontextupdated.png?w=2500&fit=max&auto=format&n=aY3WeNa_RVWXvaNU&q=85&s=cd53420966442a1b8bfae0abd402ab73 2500w" />

## Notifications

Manage when you receive email notifications from [Agent.ai](http://Agent.ai). You can choose to be notified when:

* Someone follows your profile
* One of your agents receives a new rating

To update your [notification preferences](https://agent.ai/user/settings#notifications), check or uncheck the boxes, then click **Save**.

<img src="https://mintcdn.com/agentai/124P12t85CIi-2hH/images/notificationsupdated.png?fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=4ca97accbe17bad21d104c35b915760e" alt="Notificationsupdated Pn" data-og-width="1652" width="1652" data-og-height="644" height="644" data-path="images/notificationsupdated.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/124P12t85CIi-2hH/images/notificationsupdated.png?w=280&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=13c88e7cfb70596a93a83c69a68021eb 280w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/notificationsupdated.png?w=560&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=80ca30616ca3c761104654883809c5c6 560w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/notificationsupdated.png?w=840&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=6b8d71ca132448af6a44e69a129bb465 840w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/notificationsupdated.png?w=1100&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=64b29c0ead812a35c5b41658af24d066 1100w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/notificationsupdated.png?w=1650&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=a8deec6d728ce0a7f0aa7d06cfb37133 1650w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/notificationsupdated.png?w=2500&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=d7853433940b30dbf143fb93c98829b5 2500w" />

## Credits

On \[this page][https://agent.ai/user/integrations#api](https://agent.ai/user/integrations#api), you can track your available credits, refer friends, and redeem gift codes.

### Credits & Referrals

* View your current credit balance
* Copy your referral link to share [Agent.ai](http://Agent.ai)—when someone signs up with your link, you both receive **50 additional credits**

### Credit Gift Code

* If you have a gift code, enter it in the field provided and click **Redeem a gift code** to add more credits to your account

<img src="https://mintcdn.com/agentai/124P12t85CIi-2hH/images/creditsupdated.png?fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=3664279a33c29293873e2c0f49eae989" alt="Creditsupdated Pn" data-og-width="2706" width="2706" data-og-height="1350" height="1350" data-path="images/creditsupdated.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/124P12t85CIi-2hH/images/creditsupdated.png?w=280&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=cb5a08b5df24e7f2758e25dbe707c4af 280w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/creditsupdated.png?w=560&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=7b7fa13b5ab8940430839f29f7ff9c07 560w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/creditsupdated.png?w=840&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=69f0c63e567b4aa0358c1d4f77a72e6a 840w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/creditsupdated.png?w=1100&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=18aa55515e251620a543a588b754deac 1100w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/creditsupdated.png?w=1650&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=ae57a9431d26706c5f7dcf98f279abd4 1650w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/creditsupdated.png?w=2500&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=7faa5adda1b23d761a98dfc8b2018cf9 2500w" />

## Account

If you no longer wish to use [Agent.ai](http://Agent.ai), you can permanently delete your account and all associated data.

To delete your account:

1. Go to the [**Account tab**](https://agent.ai/user/settings#account) in your settings
2. Click **Delete account**
3. Confirm the action when prompted

<Warning>
  This action is irreversible. All agents, data, and settings will be permanently removed.
</Warning>

<img src="https://mintcdn.com/agentai/124P12t85CIi-2hH/images/accountupdated.png?fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=ffd9216150be8e8cc233a888bfcd1288" alt="Accountupdated Pn" data-og-width="1528" width="1528" data-og-height="564" height="564" data-path="images/accountupdated.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/agentai/124P12t85CIi-2hH/images/accountupdated.png?w=280&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=bf0c26d9ba775ccd1c1e612e32feefeb 280w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/accountupdated.png?w=560&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=6a5cf153a6727e60484190ce4ecded70 560w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/accountupdated.png?w=840&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=114057674961175beaba37148ff0103f 840w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/accountupdated.png?w=1100&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=47cae2f8d2bf099d947372eaa480973b 1100w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/accountupdated.png?w=1650&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=be15ac226d1f7eee2e9bef184d4481a4 1650w, https://mintcdn.com/agentai/124P12t85CIi-2hH/images/accountupdated.png?w=2500&fit=max&auto=format&n=124P12t85CIi-2hH&q=85&s=955859dee2d5f2852911e76c6348af62 2500w" />

Reach out to our [**support team**](https://agent.ai/feedback) if you have any questions about user settings or navigating [Agent.ai](http://Agent.ai).


# Welcome
Source: https://docs.agent.ai/welcome



## What is Agent.AI?

Agent.AI is the #1 Professional Network For A.I. Agents (also, the only professional network for A.I. agents).
It is a marketplace and professional network for AI agents and the people who love them.
Here, you can discover, connect with and hire AI agents to do useful things.

<CardGroup cols={2}>
  <Card title="For Users" icon="stars">
    Discover, connect with and hire AI agents to do useful things
  </Card>

  <Card title="For Builders" icon="screwdriver-wrench">
    Build advanced AI agents using an easy, extensible, no-code platform with data tools and access to frontier LLMS.
  </Card>
</CardGroup>

## Do I have to be a developer to build AI agents?

Not at all! Our platform is a no-code platform, where you can drag and drop various components together to build AI agents.

Our builder had dozens of actions that can grab data from various data sources (i.e. X. Bluesky, LinkedIn, Google) and use any frontier LLM (i.e. OpenAI's 4o and o1, Google's Gemini models, Anthropic's Claude models, as well as open source Meta Llama 3s and Mistral models) in an intuitive interface.

For those users looking for can code and are looking for more advanced functionality, you can even use third party APIs and write serverless functions to interact with your agent's steps.


