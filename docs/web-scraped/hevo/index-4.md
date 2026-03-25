# Source: https://hevo-edge.readme.io/

Title: Introduction

URL Source: https://hevo-edge.readme.io/

Markdown Content:
Introduction
===============

[Jump to Content](https://hevo-edge.readme.io/#content)

[![Image 1: Hevo Edge](https://files.readme.io/123a1b88a49dae175a03c049750472ff9c1c2bbfdc5787d65ef4cca28be57f62-white_bqxdpl.svg)](https://hevo-edge.readme.io/reference)[Documentation](https://docs.hevodata.com/)[Blog](https://medium.com/hevo-data-engineering)[Status](https://status.hevodata.com/)[Changelog](https://changelog.hevodata.com/)

[API Reference](https://hevo-edge.readme.io/reference)

* * *

[Documentation](https://docs.hevodata.com/)[Blog](https://medium.com/hevo-data-engineering)[Status](https://status.hevodata.com/)[Changelog](https://changelog.hevodata.com/)[![Image 2: Hevo Edge](https://files.readme.io/123a1b88a49dae175a03c049750472ff9c1c2bbfdc5787d65ef4cca28be57f62-white_bqxdpl.svg)](https://hevo-edge.readme.io/reference)

API Reference

[API Reference](https://hevo-edge.readme.io/reference)Introduction

Search

CTRL-K

All

API Reference

Pages

###### Start typing to search…

JUMP TO CTRL-/

Familiarizing with Hevo API
---------------------------

* [Introduction](https://hevo-edge.readme.io/reference/introduction)
* [Base URLs](https://hevo-edge.readme.io/reference/base-urls)
* [API Response Body](https://hevo-edge.readme.io/reference/api-response-body)

Hevo API - Edge Pipelines
-------------------------

* [Metadata](https://hevo-edge.readme.io/reference/get_api-v1-metadata-sources-connectors)
  * [List All Source Connectors get](https://hevo-edge.readme.io/reference/get_api-v1-metadata-sources-connectors)
  * [List All Destination Connectors get](https://hevo-edge.readme.io/reference/get_api-v1-metadata-destinations-connectors)

* [Destinations](https://hevo-edge.readme.io/reference/get_api-v1-destinations)
  * [List All Destinations get](https://hevo-edge.readme.io/reference/get_api-v1-destinations)
  * [Get Details of a Destination get](https://hevo-edge.readme.io/reference/get_api-v1-destinations-destination-id)
  * [Create a Destination post](https://hevo-edge.readme.io/reference/post_api-v1-destinations)
  * [Modify Destination Configuration patch](https://hevo-edge.readme.io/reference/patch_api-v1-destinations-destination-id)
  * [Delete a Destination del](https://hevo-edge.readme.io/reference/delete_api-v1-destinations-destination-id)

* [Pipelines](https://hevo-edge.readme.io/reference/get_api-v1-pipelines)
  * [List All Pipelines get](https://hevo-edge.readme.io/reference/get_api-v1-pipelines)
  * [Get Details of a Pipeline get](https://hevo-edge.readme.io/reference/get_api-v1-pipelines-pipeline-id)
  * [Create a Pipeline post](https://hevo-edge.readme.io/reference/post_api-v1-pipelines)
  * [Disable a Pipeline post](https://hevo-edge.readme.io/reference/post_api-v1-pipelines-pipeline-id-actions-disable)
  * [Enable a Pipeline post](https://hevo-edge.readme.io/reference/post_api-v1-pipelines-pipeline-id-actions-enable)
  * [Trigger Manual Sync for a Pipeline post](https://hevo-edge.readme.io/reference/post_api-v1-pipelines-pipeline-id-actions-sync-now)
  * [Resync a Pipeline post](https://hevo-edge.readme.io/reference/post_api-v1-pipelines-pipeline-id-actions-resync)
  * [Modify Pipeline Configuration patch](https://hevo-edge.readme.io/reference/patch_api-v1-pipelines-pipeline-id)
  * [Modify Source Configuration in a Pipeline patch](https://hevo-edge.readme.io/reference/patch_api-v1-pipelines-pipeline-id-sources)
  * [Delete a Pipeline del](https://hevo-edge.readme.io/reference/delete_api-v1-pipelines-pipeline-id)

* [Pipeline Objects](https://hevo-edge.readme.io/reference/get_api-v1-pipelines-pipeline-id-objects)
  * [List All Pipeline Objects get](https://hevo-edge.readme.io/reference/get_api-v1-pipelines-pipeline-id-objects)
  * [Get Details of a Pipeline Object get](https://hevo-edge.readme.io/reference/get_api-v1-pipelines-pipeline-id-objects-object-id)
  * [Trigger a Source Schema Refresh post](https://hevo-edge.readme.io/reference/post_api-v1-pipelines-pipeline-id-objects-actions-refresh-schema)
  * [Trigger Resync for a Set of Objects post](https://hevo-edge.readme.io/reference/post_api-v1-pipelines-pipeline-id-objects-actions-resync)
  * [Manage Objects in a Pipeline patch](https://hevo-edge.readme.io/reference/patch_api-v1-pipelines-pipeline-id-objects)

* [Pipeline Jobs](https://hevo-edge.readme.io/reference/get_api-v1-pipelines-pipeline-id-jobs)
  * [List All Jobs for a Pipeline get](https://hevo-edge.readme.io/reference/get_api-v1-pipelines-pipeline-id-jobs)
  * [Get Details of a Pipeline Job get](https://hevo-edge.readme.io/reference/get_api-v1-pipelines-pipeline-id-jobs-job-id)
  * [List All Objects Processed in a Pipeline Job get](https://hevo-edge.readme.io/reference/get_api-v1-pipelines-pipeline-id-jobs-job-id-objects)
  * [Cancel a Pipeline Job post](https://hevo-edge.readme.io/reference/post_api-v1-pipelines-pipeline-id-jobs-job-id-actions-cancel)

Powered by[](https://readme.com/?ref_src=hub&project=hevo-edge)

Introduction
============

Ask AI

Use the Hevo API to automate single and bulk actions that you perform in the Hevo interface. The API provides you the flexibility to act on your Pipelines based on specific data or business triggers and integrate responses from these APIs into your data management and analysis activities.

The Hevo API is organized around REST. It uses HTTP requests to access and use data, accepts JSON request bodies, returns JSON responses, and uses standard HTTP response codes, authentication, and verbs.

### What is REST API?

[](https://hevo-edge.readme.io/#what-is-rest-api)

REST stands for REpresentational State Transfer. A REST API (also known as RESTful API) is a web API that follows the REST architecture and can interact with RESTful web services. REST APIs use HTTP requests to interact with the data. For example, with a REST API, you can use HTTP requests such as Get, Post, Update, Delete to read, create, update, and delete data stored on a computer or a system. You can specify the parameters in the request body of the API that help to identify the data and the actions to be performed on it.

In API terminology, the endpoint is the URL used to make the request. The resource signifies the dataset that is returned. For example, in the endpoint

`https://us.hevodata.com/api/public/v2.0/pipelines/{id}` for fetching a Pipeline based on the ID, the resource is pipelines.

You can have multiple endpoints with the same resource based on the action you need to perform.

Refer to the API Reference section to find information about the different endpoints that are available for each resource and how to successfully use each of these. You can also try these out with sample values and review the response.

### API Breaking Changes Policy

[](https://hevo-edge.readme.io/#api-breaking-changes-policy)

Hevo will try to notify you in advance of any updates or removal of API features that may require you to update your deployed code.

Updated 20 days ago

* * *

[Base URLs](https://hevo-edge.readme.io/reference/base-urls)

Did this page help you?

Yes

No

Updated 20 days ago

* * *

[Base URLs](https://hevo-edge.readme.io/reference/base-urls)

Did this page help you?

Yes

No

* [Table of Contents](https://hevo-edge.readme.io/#)
*       *   [What is REST API?](https://hevo-edge.readme.io/#what-is-rest-api)
  * [API Breaking Changes Policy](https://hevo-edge.readme.io/#api-breaking-changes-policy)

1. Familiarizing with Hevo API
2. [Introduction](https://hevo-edge.readme.io/reference/introduction)
3. [Base URLs](https://hevo-edge.readme.io/reference/base-urls)
4. [API Response Body](https://hevo-edge.readme.io/reference/api-response-body)

5. Hevo API - Edge Pipelines
6. [Metadata](https://hevo-edge.readme.io/reference/metadata)
7. [List All Destination Connectors get](https://hevo-edge.readme.io/reference/get_api-v1-metadata-destinations-connectors)
8. [List All Source Connectors get](https://hevo-edge.readme.io/reference/get_api-v1-metadata-sources-connectors)
9. [Destinations](https://hevo-edge.readme.io/reference/destinations)
10. [Delete a Destination del](https://hevo-edge.readme.io/reference/delete_api-v1-destinations-destination-id)
11. [Modify Destination Configuration patch](https://hevo-edge.readme.io/reference/patch_api-v1-destinations-destination-id)
12. [Create a Destination post](https://hevo-edge.readme.io/reference/post_api-v1-destinations)
13. [Get Details of a Destination get](https://hevo-edge.readme.io/reference/get_api-v1-destinations-destination-id)
14. [List All Destinations get](https://hevo-edge.readme.io/reference/get_api-v1-destinations)
15. [Pipelines](https://hevo-edge.readme.io/reference/pipelines)
16. [Delete a Pipeline del](https://hevo-edge.readme.io/reference/delete_api-v1-pipelines-pipeline-id)
17. [Modify Source Configuration in a Pipeline patch](https://hevo-edge.readme.io/reference/patch_api-v1-pipelines-pipeline-id-sources)
18. [Modify Pipeline Configuration patch](https://hevo-edge.readme.io/reference/patch_api-v1-pipelines-pipeline-id)
19. [Resync a Pipeline post](https://hevo-edge.readme.io/reference/post_api-v1-pipelines-pipeline-id-actions-resync)
20. [Trigger Manual Sync for a Pipeline post](https://hevo-edge.readme.io/reference/post_api-v1-pipelines-pipeline-id-actions-sync-now)
21. [Enable a Pipeline post](https://hevo-edge.readme.io/reference/post_api-v1-pipelines-pipeline-id-actions-enable)
22. [Disable a Pipeline post](https://hevo-edge.readme.io/reference/post_api-v1-pipelines-pipeline-id-actions-disable)
23. [Create a Pipeline post](https://hevo-edge.readme.io/reference/post_api-v1-pipelines)
24. [Get Details of a Pipeline get](https://hevo-edge.readme.io/reference/get_api-v1-pipelines-pipeline-id)
25. [List All Pipelines get](https://hevo-edge.readme.io/reference/get_api-v1-pipelines)
26. [Pipeline Objects](https://hevo-edge.readme.io/reference/pipeline-objects-1)
27. [Manage Objects in a Pipeline patch](https://hevo-edge.readme.io/reference/patch_api-v1-pipelines-pipeline-id-objects)
28. [Trigger Resync for a Set of Objects post](https://hevo-edge.readme.io/reference/post_api-v1-pipelines-pipeline-id-objects-actions-resync)
29. [Trigger a Source Schema Refresh post](https://hevo-edge.readme.io/reference/post_api-v1-pipelines-pipeline-id-objects-actions-refresh-schema)
30. [Get Details of a Pipeline Object get](https://hevo-edge.readme.io/reference/get_api-v1-pipelines-pipeline-id-objects-object-id)
31. [List All Pipeline Objects get](https://hevo-edge.readme.io/reference/get_api-v1-pipelines-pipeline-id-objects)
32. [Pipeline Jobs](https://hevo-edge.readme.io/reference/pipeline-jobs-1)
33. [Cancel a Pipeline Job post](https://hevo-edge.readme.io/reference/post_api-v1-pipelines-pipeline-id-jobs-job-id-actions-cancel)
34. [List All Objects Processed in a Pipeline Job get](https://hevo-edge.readme.io/reference/get_api-v1-pipelines-pipeline-id-jobs-job-id-objects)
35. [Get Details of a Pipeline Job get](https://hevo-edge.readme.io/reference/get_api-v1-pipelines-pipeline-id-jobs-job-id)
36. [List All Jobs for a Pipeline get](https://hevo-edge.readme.io/reference/get_api-v1-pipelines-pipeline-id-jobs)
