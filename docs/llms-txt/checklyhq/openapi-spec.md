# Source: https://checklyhq.com/docs/quickstarts/openapi-spec.md

> ## Documentation Index
> Fetch the complete documentation index at: https://checklyhq.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Creating Checks from an OpenAPI Spec

> Step-by-step guide to creating your first API check in Checkly using the web UI and CLI.

If your API implements the Swagger 2.0 or OpenAPI spec, you can import the `swagger.json` spec. The importer
parses your spec and prompts you to make some decisions about which requests are to be imported and how.

Navigate to the Create API Check page and select the Import from Swagger / OpenAPI button.

<Frame>
  <img className="block dark:hidden" src="https://mintcdn.com/checkly-422f444a/jpJy3Q8mT2HKDQv1/images/next/swagger-import-light.png?fit=max&auto=format&n=jpJy3Q8mT2HKDQv1&q=85&s=37c135774489ccb0e3598f29b0351e53" alt="Light mode interface" width="2506" height="1228" data-path="images/next/swagger-import-light.png" />

  <img className="hidden dark:block" src="https://mintcdn.com/checkly-422f444a/jpJy3Q8mT2HKDQv1/images/next/swagger-import-dark.png?fit=max&auto=format&n=jpJy3Q8mT2HKDQv1&q=85&s=b623a96b906ed4d3e423c1572992e57d" alt="Dark mode interface" width="2508" height="1218" data-path="images/next/swagger-import-dark.png" />
</Frame>

Add a valid URL to the Swagger / OpenAPI specification and click the Import Specfication button.

## Configuring Your Checks

### Groups & Tagging

You can add your OpenAPI endpoints checks to a group to help you manage them.

<Frame>
  <img className="block dark:hidden" src="https://mintcdn.com/checkly-422f444a/jpJy3Q8mT2HKDQv1/images/next/swagger-import-choice-light.png?fit=max&auto=format&n=jpJy3Q8mT2HKDQv1&q=85&s=c4cbe00288d29180c40a749e18fe72e7" alt="Light mode interface" width="2480" height="1166" data-path="images/next/swagger-import-choice-light.png" />

  <img className="hidden dark:block" src="https://mintcdn.com/checkly-422f444a/jpJy3Q8mT2HKDQv1/images/next/swagger-import-choice-dark.png?fit=max&auto=format&n=jpJy3Q8mT2HKDQv1&q=85&s=a0f5d0dcad8650364bfded8afd19a6c3" alt="Dark mode interface" width="2466" height="1150" data-path="images/next/swagger-import-choice-dark.png" />
</Frame>

A tag will be added to each imported check.

### Name

The name of the check will be the name of the OpenAPI endpoint.

### Response time limits

Sometimes APIs can be slow, but not broken. We call this degraded. You can set [response time limits](/detect/synthetic-monitoring/api-checks/response-limits) to specify when an API check should be marked as degraded and when it should be marked as failed.

### Assertions

This is where you determine whether the response of the HTTP request is correct or not.
You can assert on different sources. These could be:

* The HTTP status code returned from the API
* Something missing or required within the response body
* A specific response header
* A specific response time

[Read more about assertions](assertions)

### Scheduling & locations

You can configure your checks to run from our [public](/concepts/locations) locations, or use a Checkly Agent to host your own [private](/platform/private-locations/overview) locations. If you don't select more than one location and you've disabled retrying checks from the same location, we will pick a random location when retrying checks.

Checkly runs your API checks based on an interval you set. The shortest interval you can run is every 10 seconds and the longest is every 24 hours.

<Info>
  A 1-second interval is available upon request — [contact us](mailto:support@checklyhq.com) if you'd like to learn more.
</Info>

### Retries & alerting

Select your preferred [retry strategy](/communicate/alerts/retries) for failed checks.

Choose which [alert channels](/communicate/alerts/channels) to get notified through when your check runs into issues. If we don't have your preferred alert method, why not try out our [webhooks](/integrations/alerts/webhooks)?

### Testing

You can run your check as an [E2E test](/testing/overview) locally or from your CI/CD pipeline to validate your freshly deployed application. Use the Checkly CLI, or configure integrations with Vercel and GitHub.


Built with [Mintlify](https://mintlify.com).