# Sourcegraph Documentation


## Documentation

Search docs...LatestThemeDocumentationSourcegraph allows developers to rapidly search, write, and understand code by bringing insights from their entire codebase right into the editor.Sourcegraph is a Code Intelligence platform that deeply understands your code, no matter how large or where it&#x27;s hosted, to power modern developer experiences.

Code Search: Search through all of your repositories across all branches and all code hosts
Deep Search: Ask natural language questions and get detailed answers from our AI agent
Code Intelligence: Navigate code, find references, see code owners, trace history, and more
Fix and Refactor: Roll out and track large-scale changes and migrations across repos at once
AI Assistant: Use Cody, our AI code assistant to read, write, and understand your entire codebase faster

Quickstart
Code SearchSearch all of your repositories across all branches and all code hosts.CodyWrite, fix, and maintain code with Sourcegraph&#x27;s AI coding assistant, Cody.Deep SearchGet comprehensive answers to complex code questions using an AI agent that explores your codebase.Sourcegraph 101Learn how to use Sourcegraph.Sourcegraph TourTake a tour of Sourcegraph&#x27;s features using real-world examples and use cases.
Main Features
Some of the main Sourcegraph features include:
FeatureDescriptionDeep SearchNatural language code search with a dedicated AI agent that explores your codebaseCodyCody is and AI coding assistant that writes, fixes, and maintains your codeCode NavigationJump-to-definition, find references, and other IDE-like code browsing features on any branch, commit, or PR/code reviewCode InsightsReveal high-level information about your codebase at its current state and over time, to track migrations, version usage, vulnerability remediation, ownership, and moreBatch ChangesMake large-scale code changes across many repositories and codehostsIntegrationsWith code hosts, code review tools, editors, web browsers, etc.
What&#x27;s New
Stay in sync and get the latest news on Sourcegraph products, technologies, and culture. Read the blog →
Join our Community
If you have questions about anything related to Sourcegraph, you&#x27;re always welcome to ask in in our Discord, and X.

Search docs...LatestThemeDocsgetting-startedGetting Started
This page will help you learn and understand about Sourcegraph and how to
use it.
What is Sourcegraph?
Sourcegraph is a Code Intelligence platform that deeply understands your code, no matter how large or where it&#x27;s hosted, to power modern developer experiences.
Who should use Sourcegraph?
In addition to the companies listed on about.sourcegraph.com, companies with a few hundred developers up to those with more than 40,000 use Sourcegraph daily.
More specifically, Sourcegraph is great for all developers except:

those on smaller teams with a small amount of code
those who rarely search, read, or review code

Why do I need Code Search?
Facebook and Google provide their employees with an in-house Sourcegraph-like code search and intelligence tool. A published research paper from Google and a Google developer survey showed that 98% of developers surveyed consider their Sourcegraph-like internal tool to be critical. Developers use it on average for 5.3 sessions each day. (Facebook&#x27;s and Google&#x27;s in-house tools are unavailable to other companies; use Sourcegraph instead.)
What do I use Sourcegraph for?
Sourcegraph helps you:

Find example code
Explore/read code (including during a code review)
Debug issues
Locate a specific piece of code
Determine the impact of changes
And more!

Sourcegraph makes it easier for you and everyone else in your organization to perform these tasks.
What does Sourcegraph do?
Sourcegraph&#x27;s main features are:

Deep Search: Ask questions in natural language and get comprehensive, sourced answers about your codebase using AI-powered agentic search
Code Search: fast, up-to-date, and scalable, with regexp support on any branch or commit without an indexing delay (and diff search)
Code navigation: jump-to-definition, find references, and other smart, IDE-like code browsing features on any branch, commit, or PR/code review
Code Insights: reveal high-level information about your codebase at its current state and over time to track migrations, version usage, vulnerability remediation, ownership, and anything else you can search in Sourcegraph
Batch Changes: make large-scale code changes across many repositories and code hosts
Integrations with code hosts, code review tools, editors, web browsers, etc.
MCP Server: Connect AI tools and IDEs to Sourcegraph&#x27;s code intelligence capabilities through the Model Context Protocol

How do I start using Sourcegraph?

Deploy and Configure Sourcegraph inside your organization on your internal code if nobody else has yet
Install and configure the web browser code host integrations (recommended)
Start searching and browsing code on Sourcegraph by visiting the URL of your organization&#x27;s internal Sourcegraph instance
Personalize Sourcegraph with themes, quick links, and badges!

You can also try Sourcegraph.com, a public Sourcegraph instance for use on open-source code only.
How is Sourcegraph licensed?
Sourcegraph Enterprise is Sourcegraph&#x27;s primary offering and includes all code intelligence platform features. Sourcegraph Enterprise is the best solution for enterprises who want to use Sourcegraph with their organization&#x27;s code.
How is Sourcegraph different from the GitHub code search?

See how GitHub code search compares to Sourcegraph

Code Search
Sourcegraph code search is fast, works across all your repositories at any commit, and has minimal indexing delay. Code search also includes advanced features, including:

Powerful, flexible query syntax
Commit diff search
Commit message search
Saved search scopes
Search contexts to search across a set of repositories at specific revisions
Saved search monitoring

Read the code search documentation to learn more and discover the complete feature set. Here&#x27;s a video to help you get started:

How to Search commits and diffs with Sourcegraph
Search Examples

Code Navigation
Sourcegraph gives your development team cross-repository IDE-like features on your code:

Hover tooltips
Go-to-definition
Find references
Symbol search

Sourcegraph gives you code navigation in:

code files in Sourcegraph&#x27;s web UI



diffs in your code review tool, via integrations



code files on your code host, via integrations


Please read the code navigation documentation to learn more and to set it up.
Deep Search
Deep Search is an agentic code search tool that understands natural language questions about your codebase. Unlike traditional search, Deep Search uses AI to intelligently explore your code, following leads and synthesizing information to provide comprehensive, conversational answers.
Key capabilities

Ask questions in natural language and get detailed, sourced answers about architecture, implementations, and code patterns
Use @-mentions to scope searches to specific repositories, files, directories, or symbols for faster, more focused results
Follow up with additional questions to dive deeper into specific aspects of your codebase
View all sources - see exactly which searches were performed and which files were analyzed for full transparency

Deep Search works across your entire codebase, no matter how large, and is available on Enterprise Starter and Enterprise plans.
Learn more about Deep Search
Batch Changes
Automate changes to your codebase. Reduce effort, reduce errors, and enable developers to focus on high-value work.
Read the batch changes documentation to learn more, including helpful how-to guides. Want a video tutorial? Check out this batch change tutorial
Code Insights
Sourcegraph lets you understand and analyze code trends by visualizing how the codebase changes. Measure and act on engineering goals such as migration and component deprecation.
Read the code insights documentation to learn more, including helpful how-to guides.
Integrations
Sourcegraph allows you to get code navigation and code search on code files and code review diffs in your code host and review tool or from your IDE, and also provides an MCP server for additional integrations.
MCP Server
Sourcegraph provides a Model Context Protocol (MCP) Server that connects AI tools and IDEs directly to your code intelligence platform. The MCP Server enables you to integrate Sourcegraph&#x27;s search, navigation, and analysis capabilities into your favorite development tools.
Learn more about the MCP Server
IDE integration
Sourcegraph&#x27;s editor integrations allow you to search and navigate across all of your repositories without ever leaving your IDE or checking them out locally. Learn more about how to set them up here.
Browser extension
Our browser extension directly adds code navigation within your code hosts (GitHub, GitLab, Bitbucket, and Phabricator) via Chrome, Safari, and Firefox browsers. Learn more about how to set up the browser extension here.

Search docs...LatestThemeDocscode-searchCode Search
Supported on Enterprise Starter and
Enterprise plans.Available via VS Code and JetBrains editor extensions and the Web.
Learn how to search code across all your repositories and code hosts.
Code Search allows you to find, fix, and navigate code with any code host or language across multiple repositories with real-time updates. It deeply understands your code, prioritizing the most relevant results for an enhanced search experience.

Sourcegraph&#x27;s Code Search empowers you to:

Utilize regular expressions, boolean operations, and keyboard shortcuts to help you unleash the full potential of your searches
With the symbol, commit, and diff search capabilities, it identifies code vulnerabilities in milliseconds and quickly helps you resolve issues and incidents
Offers innovative code view with seamless code navigation for a comprehensive coding experience

Getting started
Get single-tenant instance managed by Sourcegraph.Sign up and get a 30 day free trial for your team.
Search Query SyntaxLearn about the search pattern syntax and filters available for Code Search.Search ExamplesLearn about some common search use cases and examples.FeaturesLearn about the core search features.Advanced FeaturesLearn about advanced features like saved searches and search contexts.
Features
Code Search main features include:

Use query assist to search with natural language
Use regular expressions and keyword queries to perform full-text searches
Search any branch and commit, with no indexing required
Search commit diffs and commit messages to see how code has changed
Narrow your search by repository and file pattern
Use search contexts to search across a set of repositories at specific revisions
Curate saved searches for yourself or your org
Use code monitoring to set up notifications for code changes that match a query
View language statistics for search results

 Read more in detail about the Code Search features here →
Check out the Code Search FAQs here →
Architecture
Learn about how Code Search fits into Sourcegraph in the architecture overview.

Search docs...LatestThemeDocscodyCody
Supported on Sourcegraph
Enterprise.Available on VS Code, JetBrains, Visual Studio, and the Web app.
Cody is an AI coding assistant that uses all the latest LLMs and your development context to help you understand, write, and fix code faster. It uses the powerful Sourcegraph&#x27;s advanced Search API to pull context from both local and remote codebases so that you can use context about APIs, symbols, and usage patterns from across your entire codebase.

Cody connects seamlessly with codehosts like GitHub, GitLab and IDEs like VS Code, JetBrains, and Visual Studio. Once connected, Cody acts as your personal AI coding assistant, equipped with the following capabilities:

Developer chat with the most powerful models and context
Code completions, code edits, and customizable prompts
Extensive context to deliver the most accurate results

Getting started
You can start using Cody with the following options:
Cody for VS CodeInstall Cody&#x27;s extension for VS Code. Cody for JetBrainsInstall Cody&#x27;s extension for JetBrains.Cody for Visual Studio (Experimental)Install Cody&#x27;s extension for Visual Studio.Cody for WebUse Cody in the Sourcegraph web app.Cody CLIRun Cody from the command line.Cody EnterpriseGet in touch with our team to try Cody for Sourcegraph Enterprise.
Main features
Cody&#x27;s main features include:
FeatureDescriptionChatChat directly with AI to ask questions about your code, generate code, and edit code. Cody has the context of your open file and repository by default, and you can use @ to add context on specific files, symbols, remote repositories, or other non-code artifacts.Auto-editSuggests code changes by analyzing cursor movements and typing. After you&#x27;ve made at least one character edit in your codebase, it begins proposing contextual modifications based on your cursor position and recent changes.PromptsAutomate key tasks in your workflow with premade and customizable prompts. Any common query or task can be built into a prompt to save and share with your team.ContextCody provides the best LLM models and context to power chat. It uses the powerful Sourcegraph&#x27;s advanced Search API to pull context from both local and remote codebases.Debug codeCody is optimized to identify and fix errors in your code. Its debugging capability and autocomplete suggestions can significantly accelerate your debugging process, increasing developer productivity.Context FiltersCody can ignore selected repositories from chat and autocomplete results, which helps you control and manage what context your codebase uses.
What data is collected, and how is it used?
Cody collects and uses data in the following ways:

Prompts and responses: When you use Cody, Sourcegraph collects your prompts and responses to provide the service. For individuals using Cody via Sourcegraph.com, Sourcegraph may use your prompts and responses to enhance the user experience, but Sourcegraph does not use any of your data to train models.
Usage data and feedback: Sourcegraph also collects usage data and feedback to improve the user experience.

Read more about Cody Usage and Privacy policy here →
Compatible with Sourcegraph products
Cody is compatible with other Sourcegraph products, like Code Search. You can use Cody&#x27;s chat to ask questions about your codebase. When you run any search query and open a repository or file, you’ll find the Cody button that takes you to Cody’s chat interface, which you can use to ask questions about the codebase.
Read more in the Cody FAQs to learn more about such queries →
Join our community
If you have any questions regarding Cody, you can always ask in Discord, or create a post on X.

