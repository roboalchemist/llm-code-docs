# Source: https://docs.agent.ai/actions-available.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.agent.ai/llms.txt
> Use this file to discover all available pages before exploring further.

# Action Availability

> Agent.ai provides actions across the builder and SDKs.

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
