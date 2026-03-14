# Source: https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-quick-start-guide/introduction.md

# Introduction

### Nimble API Structure

At the core of the Nimble API is the [Web API](https://docs.nimbleway.io/nimble-sdk/web-api) – a generic API that accepts any public URL and collects data from that address. The Web API is designed to be flexible and support any use case while providing fundamental and advanced tools for robust web data pipelines.

<figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/Ev9zqnR0mhyrDQA9WS8o/Nimble%20API.png" alt=""><figcaption></figcaption></figure>

The Web API also serves as the infrastructure for Nimble API Templates, which act as specialized APIs for specific use cases. Templates allow for specific goals to be met more accurately, provide an optimized workflow, or include use-case-specific functionality that wouldn’t apply outside the context of that particular implementation.

To help you get started, we created several Templates that can be used both as models for the development of your own apps, as well as in production-level data pipelines:

* [**SERP API**](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/serp-api)
* [**E-Commerce API**](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/e-commerce-api)
* [**Maps API**](https://docs.nimbleway.io/nimble-sdk/web-api/vertical-endpoints/maps-api)

The Templates are based on the Web API, and their structure, workflow, and authentication process are fundamentally the same. Therefore, for the purposes of this quick-start guide, we’ll be going over the basics of using the Web API.&#x20;

### WebAPI Overview

The Web API is mainly operated through three major endpoints, each of which serves one of the three request types supported by the API. Each of these requests provide unique benefits in different situations.

* **Real-time request** – The data request is performed immediately, and the result of the request is returned directly to the client that made the request.
* **Asynchronous request** – the data request triggers an asynchronous task, and a taskID is returned to the client. The requested data is collected and delivered to a cloud storage repository, and a callback URL is notified when the task is completed.
* **Batch request** – Batch requests are functionally identical to asynchronous requests, but can include up to 1,000 tasks (URLs) in a single batch.

<figure><img src="https://content.gitbook.com/content/ZNy4aqrBN53tR8DpTEuW/blobs/5TKUfncLYogCIVw24VNF/asynchronous-request.png" alt=""><figcaption></figcaption></figure>

Despite their differences, real-time, asynchronous, and batch requests all support the same fundamental parameters, which include:

**URL** – The address of the desired web data. The WebAPI supports any public web data, and automatically employs fingerprinting technology and other advanced countermeasures to ensure smooth access is achieved every time.

**Location** – WebAPI requests are always made through Nimble IP, our premium proxy network. Nimble IP offers granular global location targeting, and supports Country, City, and US State levels of selection. The desired locale can also be set for further accuracy when using a particular location.

**Parsing** – Instead of simply returning the HTML contents of the requested URL, Nimble API can parse the HTML into a structured JSON format that simplifies storage and expedites analysis. Additionally, Nimble API uses AI models to recognize and extract key data points, such as the price of a product, position of a listing in a SERP, and more.

**Rendering** – Controls the execution of javascript and other web technologies when loading the target URL. Some data sources will not require rendering, and in such cases disabling rendering reduces the response time for a faster request. However, many websites will require full javascript rendering to load properly and accurately.

In addition to those listed above, the WebAPI supports several additional parameters. For a complete list, see the [**Nimble API Functions Documentation**](https://docs.nimbleway.io/nimble-sdk/web-api/nimble-web-api-functions)**.**
