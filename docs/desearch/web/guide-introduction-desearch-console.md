<!--
source: https://desearch.ai/docs/guide/introduction/desearch-console
title: Desearch Console - Introduction Documentation | Desearch
captured: 2026-04-04
-->
# Desearch Console - Introduction Documentation | Desearch

Source: https://desearch.ai/docs/guide/introduction/desearch-console

---

Home
Guide
API Reference
SDKs
API Console
API Status
GitHub
Discord
Blog
Search guides...
⌘K
INTRODUCTION
Desearch AI
Desearch Console
Glossary
APIS
Desearch API
Desearch x Bittensor
API Keys
Authorization
Pricing and Billing
SDK
Desearch API SDK
Python SDK Specification
JavaScript SDK Specification
INTEGRATIONS
MCP
OpenAI Wrapper
Function Calling with GPT
Function Calling with Claude
RAG with LangChain x Desearch
RAG with LlmaIndex x Desearch
ElizaOs Agents with Desearch
CrewAI Agents with Desearch
Browser Use x Desearch
OpenClaw Agent with Desearch
Numinous SN6 × Desearch Integration
USE CASES
Search Engine Use Cases
AI-Driven Chat Use Cases
Intelligent Agent Task Automation
CAPABILITIES
X (Twitter) Queries
Desearch Console

Desearch Console is a platform designed to simplify AI integration for developers and businesses, providing comprehensive access to the Bittensor network through a single API key. The dashboard also enables users to directly consume the Bittensor network’s AI models and utilize its capabilities to perform a wide range of search-based operations

Key Features

Desearch: An AI-driven search tool that offers contextual, multi-perspective results by processing queries through a decentralized community of AI models. This approach ensures the accuracy and relevance of information, minimizing noise and irrelevant data.

API Integration: The platform offers a user-friendly API with comprehensive documentation, enabling quick and efficient incorporation of AI features into applications, thereby enhancing user experience and operational efficiency.

Real-Time Monitoring and Analytics: Users have access to a detailed API console that provides real-time error logs and request metrics, ensuring smooth application performance.

Playground: Desearch console provides a playground for users to experience AI models firsthand, allowing them to test features, evaluate performance, and envision potential enhancements for their applications.

Desearch Console

By leveraging the Desearch Dashboard, developers can seamlessly integrate advanced AI capabilities into their projects, benefiting from the decentralized and secure nature of the Bittensor network.

​Console

The Console is user-friendly and provides real-time monitoring of API usage, errors, and billing, helping users track and optimize their AI-based integrations. The overview provides general insights into API usage and account details.

Desearch Console

**API Keys:** Manages API keys for accessing Desearch services.

Logs: Tracks API request logs and error logs.

Billing: Provides financial details, including balance and spending.

​Error Trends & Logs

Requests: Displays the total number of API requests.

Graph: Shows request trends over time.

Latest Error Logs: Indicates whether there are any recent errors.

Balance & Spending

Balance: Shows the current account balance.

**Spent:** Displays the total spending for the selected time period.

Graph: Represents spending trends over time.

​Activity Summary

**Subnets Used:** Lists the subnets.

Requests: Number of API requests per subnet.

Errors: Tracks errors encountered.

Spent: Displays the cost associated with API calls.

​API Keys

This is the API Keys Management page of the Desearch Console, where users can manage their API keys for accessing Desearch services.

Create Key is used to define a new API key, while Delete Key removes an existing key. Edit allows the user to change the key name and description, but not the key itself. The primary grid displays existing API keys with details such as:

Name: Identifier for the key.

Token: The actual API key, partially masked for security.

Description: A user-defined description.

Timestamp: The date and time when the key was created.

Logs

This is the Logs page of the Desearch Console, where users can monitor API requests and responses.

The Log Entries Table contains the following information. Upon clicking the Subnet, additional details are displayed with request and response details.

Subnet: The service making the request .

Method: The HTTP method used.

URL: The endpoint being accessed.

Timestamp: The date and time of the request.

Status: The HTTP response code.

​Billing

This is the Billing page of the Desearch Console, where users can manage their account balance, top-ups, and spending.

Balance Management

Current Balance: Displays the available balance.

Payment Method: Shows available payment methods (TAO and Card). User can use either method to top up the balance

Top-Up Option: Users can manually enter an amount and click “Top up balance” to add funds. On this, the user will be redirected to Stripe Payment Gateway for further payment. w

Auto Top-Up: Users can enable automatic billing when their balance is low. The current threshold by default is set to 10, and the default auto top−up amount is 25. There is also an option to update the threshold.

​Spending Overview

Spent Amount: Displays the total amount paid.

Spending Graph: Visual representation of spending over time.

​Transaction Explorer

This grid enlists recent transactions along with the payment deducted for the relevant transaction.

Subnet: The service used for a particular transaction.

Date: Timestamp of the transaction.

Amount: The cost of the request.

Status: Payment success status.

​Playground

This is the Playground page for the Desearch Console, specifically for the Desearch AI-powered search tool.

​Tool Selection & Filters

Desearch: The selected AI search tool, which allows developers and AI builders to integrate AI search capabilities into their applications.

Customization Button: Users can configure Desearch for their needs. This allows users to pass on custom instructions to the AI model, which helps in better responses.

Filters: Filters under this streamline the AI Model based on search tools, date filters, response order sorting, and available models.

​Search & Results

New Chat: Initiates a new AI-powered search.

Search Results: Displays news and search results related to the provided query. The results are generated by the AI model.

📘 Behind the Scene

The playground behind the scenes uses Desearch API's AI Search endpoint which can be accessed through here .

🍪 We value your privacy

We use cookies to enhance your browsing experience, serve personalized ads or content, and analyze our traffic. By clicking "Accept All", you consent to our use of cookies. Read our Privacy Policy

Reject All
Accept All
