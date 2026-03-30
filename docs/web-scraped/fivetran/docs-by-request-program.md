# Source: https://fivetran.com/docs/by-request-program

Title: Fivetran By Request program

URL Source: https://fivetran.com/docs/by-request-program

Markdown Content:
Our By Request program is a simple [six-step program](https://fivetran.com/docs/by-request-program#whatarethestepsinthebyrequestprogram) where you can [collaborate with our Product team to build a Lite connector](https://fivetran.com/docs/by-request-program#whyshouldicollaboratewithfivetrantobuildaconnector) for a SaaS application source you need. The program enables you to centralize essential data from your business-critical SaaS applications whenever you need it.

The [By Request program streamlines accessing data](https://fivetran.com/docs/by-request-program#whyshouldiusethebyrequestprogram) from unsupported sources in your backlog. The program reduces the effort it takes for your teams to get data from these sources while placing a spotlight on use cases that yield immediate value. As the requester, you and your team are the ones to verify that the connector aligns with your requirements and data objectives.

Once we build the connector, it’s added to Fivetran’s catalog of connectors. We provide support, maintenance, and also consider enhancement requests. Once the new connector development is complete, you can request enhancements using our Feedback portal.

* * *

When should I use the By Request program?[](https://fivetran.com/docs/by-request-program#whenshouldiusethebyrequestprogram)
---------------------------------------------------------------------------------------------------------------------------

The By Request program is suitable for Fivetran users who are looking for:

*   A SaaS application connector that Fivetran doesn't currently support
*   A connector for a service that uses HTTP APIs (REST APIs, GraphQL)
*   Fivetran's support to build and maintain the connector

* * *

Why should I use the By Request program?[](https://fivetran.com/docs/by-request-program#whyshouldiusethebyrequestprogram)
-------------------------------------------------------------------------------------------------------------------------

Building data pipelines is complex and involves the following major elements:

*   Connection
*   Extraction
*   Data cleansing
*   Load or write
*   Transformation

With the By Request Program, you can work with Fivetran to build a data pipeline for your use case.

* * *

Why should I collaborate with Fivetran to build a connector?[](https://fivetran.com/docs/by-request-program#whyshouldicollaboratewithfivetrantobuildaconnector)
---------------------------------------------------------------------------------------------------------------------------------------------------------------

Fivetran connectors are built on the following principles:

*   Reliability: You don't have to think about your connector - you can set it and forget it.
*   Security: We provide enterprise-grade security and data governance.
*   Performance: Our connectors have a quick setup process, fast historical syncs, and provide end-to-end updates with low latency.
*   Extensibility: Product extensions are built on top of our connectors (for example, Transformations and Fivetran REST API).
*   Simplicity: Our connectors are easy to use. We only provide advanced configuration to work around unavoidable system and environment complexity.

* * *

How does the requesting user contribute to the program?[](https://fivetran.com/docs/by-request-program#howdoestherequestingusercontributetotheprogram)
------------------------------------------------------------------------------------------------------------------------------------------------------

The requesting user has a major role to play in the connector design and development.

In the request, the user must provide the following:

*   Service name and URLs
*   API docs
*   Use case clarification
*   Information about the data needed from the service

During the technical consultation, the user must:

*   Meet with Fivetran Technical Product Specialist
*   Grant Fivetran access to source systems and test data
*   Demonstrate how they use the service
*   Provide data requirement information
*   Provide use case information

During the Private Preview phase, the user must:

*   Review the data delivered into their destination to ensure its completeness
*   Verify that the connector meets the requirements

* * *

What are the steps in the By Request program?[](https://fivetran.com/docs/by-request-program#whatarethestepsinthebyrequestprogram)
----------------------------------------------------------------------------------------------------------------------------------

Our By Request program can be summarized into the following high-level steps. Fivetran uses these six phases that involves submission, validation, consultation, and development to build the connector for your source.

1.   **Request Submission**: You [submit a request](https://fivetran.com/dashboard/by-request) to build a connector for a specific source.
2.   **Request Validation**: We review the request.
3.   **Technical Consultation**: Our Technical Product Specialist team meets you and discusses the requirements and use cases.
4.   **Connector Development**: We build and test the connector.
5.   **Private Preview release**: The connector development reaches the Private Preview phase.
6.   **Generally Available release**: The connector development reaches the Generally Available phase.

For more information, expand the following section.

**What to expect?** The following steps outline the By Request program and what our users can expect from each step: 
**Request Submission**

A Fivetran user submits a Request for a Connector service to be prioritized. Complete the request using the [Fivetran Lite Connector Request form](https://fivetran.com/dashboard/by-request).

In the request, the user needs to provide information about the service to help us assess suitability for the program, including:

*   The name and URLs for the business page
*   API docs
*   Clarification on the use cases and data needed from the service

**Request Validation**

Fivetran reviews the request. In this step:

*   Fivetran de-duplicate the requests and combines it with any similar requests.
    *   Fivetran communicates the status of any duplicates.

*   Fivetran accepts the submitted viable request for connector development.
    *   Fivetran completes a detailed analysis of the available API documentation for the requested API(s) to confirm the service matches the program.
        *   If the source is not a great candidate, we let you know, and the process stops.

    *   Fivetran then prepares a Starter Connector to enable the access partnership.

We expect to take around two to eight weeks for the request validation phase.

**Technical Consultation**

Fivetran Technical Product Specialist meets with the [requesting user](https://fivetran.com/docs/by-request-program#whatuserroleshouldihaveinfivetrantobeabletosetupaconnector) and does three key things:

*   Set up the Starter Connector and grant Fivetran access to enable the build to continue. While the production environment is readily accessible, Fivetran can also connect to the sandbox or test environment that has the representative test data.
*   Review the service being requested. The user takes the Technical Product Specialist through the service being requested and demonstrates how their business uses the service and what data is needed from it.
*   Discuss about the use cases planned for the data once it is available in the user’s destination (data warehouse).

**Connector Development**

Fivetran builds the connector. This includes:

*   Building and testing the connector.
*   Creating documentation for the connector.
*   Finalizing the connector and promoting to the Private Preview phase.

After we receive the source access, we expect to take around six to eight weeks to develop the connector.

**Private Preview release**

The connector joins Fivetran's Private Preview program. In the Private Preview phase:

*   The Starter Connector starts syncing data. Fivetran identifies and fixes issues.
*   The users trying the connector review the data delivered into their destination to ensure its completeness.
*   The user who requested the connector verifies that the connector meets the requirements.

**Generally Available release**

Fivetran promotes the connector to General Availability. The By Request program is complete.

When Lite connectors are Generally Available, users can request enhancements to the connector by submitting to the [Feedback portal](https://support.fivetran.com/hc/en-us/community/topics/360001909373-Feature-Requests).

* * *

Source considerations[](https://fivetran.com/docs/by-request-program#sourceconsiderations)
------------------------------------------------------------------------------------------

Fivetran considers the following characteristics of the source service before designing and building the connector:

*   Good API documentation
*   Structured and reasonably-sized API responses
*   No custom data
*   Good use cases for the data
*   API key-based authentication (preferably)

For more information, expand the following section.

**What makes a good candidate application?**
The By Request process allows you to request that Fivetran prioritize a new Lite connector that delivers an immediate business impact. Some services are better candidates than others due to the technology behind Lite connectors.

If you submit a detailed and well-researched request, we can build and deliver the Lite connector more quickly and ultimately get your data moving faster.

A service that is ideal for a Lite connector has the following characteristics:

*   Well-documented APIs:

    *   Publicly accessible documentation is better
    *   A document you can send us can work in some cases

*   A service where a distinct set of data can deliver value through only a reasonable number of API calls with well-structured and reasonably-sized API responses:

    *   ~40 endpoints is a great number
    *   2 or 3 levels of nesting in the data response only. Nesting is when we call one endpoint in order to get a list that we then need to iterate through to make additional API calls before getting the actual data

You can submit the request even if your service doesn't meet the above criteria. We will try to build a connector for your service, although it might take us a little longer than our [usual timelines](https://fivetran.com/docs/by-request-program#whattimelineshouldiexpectforabyrequestbuild).

*   A service with not too much custom data

    *   Our Lite connector build process can support many examples of custom data. However, it does not work well for services where the entire schema is custom - that is, defined by the end user and therefore different for each user

*   Clear use case with APIs related to that use case

    *   Would you find it easy to get the data you are asking for?
    *   Can you share code or examples of the data you want?
    *   Two great resources on this topic:
        *   [Blog](https://fivetran.com/blog/fivetran-protocol) about what makes a great API for syncing data to a destination
        *   [E-book](https://resources.fivetran.com/ebooks/fivetran-protocol-ebook) available on the blog is a more detailed source of information

*   Currently, API key access is preferred over OAuth 2.0

    *   Our framework supports OAuth 2.0 however a lot more coordination and involvement from the requesting user and/or the source application is needed.

* * *

Security[](https://fivetran.com/docs/by-request-program#security)
-----------------------------------------------------------------

Lite connectors are built on a framework and principles that ensure enterprise-grade security.

For more information, expand the following section.

**Key questions that your InfoSec team may ask (and some possible answers)**
The Lite building process creates a starter connector meaning that all credential information is stored in Fivetran’s secure systems.Throughout the connector build process, Fivetran uses state-of-the-art security measures to keep your data safe:

*   Our single sign-on provider controls data access by enforcing permission validation, deny by default, separation of duties and Defense-in-Depth.
*   We mandate multi-factor authentication to access production networks for securing consumer identities and preventing authentication bypass.
*   We securely log and monitor all access to correlate and investigate relevant security events like unhandled exceptions, authentication or authorization failures, brute force attempts, etc.
*   The environment is ephemeral and all data is deleted after seven days.
*   We follow the principle of least access control. Only engineers working on building this connector have access to your data.
*   We use strong cryptographic standards to preserve confidentiality and integrity of data at rest, in transit and in memory.
*   Our employees are unable to copy data out of this environment.
*   We only use this access to verify how data is returned from the source and confirm if we are writing it correctly to your destination.

* * *

Frequently asked questions[](https://fivetran.com/docs/by-request-program#frequentlyaskedquestions)
---------------------------------------------------------------------------------------------------

For frequently asked questions and their answers, expand the following section.

**FAQs**
#### What timeline should I expect for a By Request build?[](https://fivetran.com/docs/by-request-program#whattimelineshouldiexpectforabyrequestbuild)

*   We aim to take two to eight weeks to review the initial request.
*   We aim to take six to eight weeks from the starter connector being setup with access granted to kick off the initial sync of the first build of the connector.

This timeline is an estimate and is based on the assumption that the request submitted is detailed and well-researched. Requests that need additional scoping may delay the delivery of the Lite connector.

#### Do I need to be a Fivetran user to request a connector?[](https://fivetran.com/docs/by-request-program#doineedtobeafivetranusertorequestaconnector)

Yes. Fivetran is limiting this program to our users. However, it is easy to become a Fivetran user by signing up for one of our plans.

#### What user role should I have in Fivetran to be able to set up a connector?[](https://fivetran.com/docs/by-request-program#whatuserroleshouldihaveinfivetrantobeabletosetupaconnector)

To set up a connector, you must have one of the following [user roles](https://fivetran.com/docs/using-fivetran/fivetran-dashboard/account-settings/role-based-access-control#standardrolesinourrbacmodel) in Fivetran:

*   Account Administrator
*   Account Analyst
*   Manage Connection
*   Create Connection
*   Manage Destination
*   Edit Destination
*   Destination Creator

#### When will I know if Fivetran is able to build a Lite connector for the service I requested?[](https://fivetran.com/docs/by-request-program#whenwilliknowiffivetranisabletobuildaliteconnectorfortheserviceirequested)

Our Technical Product Specialist contacts you as soon as we have enough information to determine if the requested service is a good candidate. We aim to take two to eight weeks for this initial review.

#### What do I do if my source isn’t a good fit for a Lite connector?[](https://fivetran.com/docs/by-request-program#whatdoidoifmysourceisntagoodfitforaliteconnector)

If the source you request turns out not to be a good candidate then you can consider our [Connector SDK](https://fivetran.com/docs/connector-sdk) or if necessary a [File connector](https://fivetran.com/docs/connectors/files) to sync an export of the source's information.

#### What if I want to withdraw from the program?[](https://fivetran.com/docs/by-request-program#whatifiwanttowithdrawfromtheprogram)

You can withdraw at any time. You can delete the Starter Connector through Fivetran’s dashboard. You can also reach out to the assigned Technical Product Specialist for the build to let them know. The Lite connector you requested may still continue to get built if Fivetran works with other users or partners with the same request.

#### What is the difference between a Lite connector and other Fivetran connectors?[](https://fivetran.com/docs/by-request-program#whatisthedifferencebetweenaliteconnectorandotherfivetranconnectors)

See our [Lite connector documentation](https://fivetran.com/docs/connectors/applications/lite-connectors#whatarethekeydifferencesbetweenconnectorsdkandliteconnectors).

#### What SLA and support does Lite connectors have?[](https://fivetran.com/docs/by-request-program#whatslaandsupportdoesliteconnectorshave)

Fivetran’s SLA is part of the agreement that comes with signing up for a pricing plan, including the Free Plan, becoming a Fivetran user. Lite connectors are covered in the same way that our Standard connectors are.

#### What if the connector Fivetran builds is missing critical data I need?[](https://fivetran.com/docs/by-request-program#whatiftheconnectorfivetranbuildsismissingcriticaldataineed)

Fivetran focuses on building connectors our users need to get the data they want. We will always be limited by the APIs made available to us by the source. In some cases, we may need to build a connector in multiple phases. If you need more data to be added to a connector, submit a Feature Request through our [Support Portal](https://support.fivetran.com/hc/en-us/community/topics/360001909373-Feature-Requests).

Thanks for your feedback!

Was this page helpful?
