# Source: https://docs.agent.ai/actions/invoke_web_api.md

# Invoke Web API

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
