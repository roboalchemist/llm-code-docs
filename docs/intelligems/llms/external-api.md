# Source: https://docs.intelligems.io/developer-resources/external-api.md

# External API

{% hint style="warning" %}
Our external API is currently in beta. To request access and get your API key, contact our support team [here](https://portal.usepylon.com/intelligems/forms/intelligems-support-request).&#x20;

\
Have thoughts on how to make our API better? Email your feature suggestions to <jerica@intelligems.io>.
{% endhint %}

### What is the External API?

The Intelligems External API provides programmatic access to your Intelligems experiences and analytics data. This RESTful API allows you to integrate Intelligems functionality into your own applications, workflows, and data pipelines.

### What can you do with the External API?

The External API enables you to:

**Retrieve Test & Experience Data**

* List all tests and experiences in your account
* Get detailed configuration for specific tests and experiences including variations, targeting rules, offer details, and content modifications
* Access test and experience metadata like status, test types, and historical actions

**Access Analytics Data**

* Pull performance metrics for any test or experience
* View results by audience segments (device type, visitor type, traffic source, geography, etc.)
* Export analytics data for custom reporting and analysis

**Automate Workflows**

* Integrate Intelligems data into your business intelligence tools
* Build custom dashboards combining Intelligems metrics with other data sources
* Automate reporting and alerting based on test performance

### Common Use Cases

* **Custom Reporting**: Build internal dashboards that combine Intelligems test results with proprietary business metrics.
* **Data Warehouse Integration**: Sync experience and analytics data to your data warehouse for unified analysis.
* **Automated Monitoring**: Create alerts when tests reach statistical significance or meet specific performance thresholds.
* **Cross-Platform Analysis**: Combine Intelligems data with other analytics platforms for comprehensive performance views.

{% hint style="info" %}
***Checkout our*** [***Automations & Guides sections***](https://docs.intelligems.io/developer-resources/external-api/automations-and-guides) ***for how-tos of common use cases.***
{% endhint %}

### Getting Started

Our External API is currently in beta. To request access and receive your API key, [contact our support team](https://portal.usepylon.com/intelligems/forms/intelligems-support-request).

Once you have your API key, you can authenticate requests by including it in the `intelligems-access-token` header.

### Available Endpoints

* **GET /v25-10-beta/experiences-list** - Retrieve a list of all experiences with optional filtering by category, status, and pagination
* **GET /v25-10-beta/experiences/{experienceId}** - Get complete details for a specific experience
* **GET /v25-10-beta/analytics/resource/{experienceId}** - Access analytics data for an experience with customizable date ranges and audience segmentation

For detailed endpoint documentation including parameters, request examples, and response schemas, see the [API Reference](https://docs.intelligems.io/developer-resources/external-api/get-experience-data).
