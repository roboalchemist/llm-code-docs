# Source: https://docs.asapp.com/messaging-platform/digital-agent-desk/knowledge-base.md

# Knowledge Base

> Learn how to integrate your Knowledge Base with the Digital Agent Desk.

Knowledge Base (KB) is a technology used to store structured and unstructured information useful for Agents to reference while servicing Customer enquiries.

You can integrate KB data into ASAPP Desk by manually uploading articles in an offline process or by integrating with a digital system which exposes the content via REST APIs.

Knowledge Base helps Agents access information without the Agent needing to navigate any external systems by surfacing KB content directly within Agent Desk's Right Hand Panel view.

This helps lower the Average Handle Time and increases Concurrency. KB also learns from Agent interactions and suggests articles and helps in Agent Augmentation.

<Frame>
  <img src="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9066885a-0903-fe42-8192-31ea376b8937.png?fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=09714c3f2dd9245bbefb66c885808ba7" data-og-width="1740" width="1740" data-og-height="1000" height="1000" data-path="image/uuid-9066885a-0903-fe42-8192-31ea376b8937.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9066885a-0903-fe42-8192-31ea376b8937.png?w=280&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=c50e2d19929f9725913025622b73343a 280w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9066885a-0903-fe42-8192-31ea376b8937.png?w=560&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=2e400b24f56118c49f79d7d0ad153c51 560w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9066885a-0903-fe42-8192-31ea376b8937.png?w=840&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=a44e84da12df06176ce0ae5d03e6b093 840w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9066885a-0903-fe42-8192-31ea376b8937.png?w=1100&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=04f8b0b1ac31ad1af9098755063bbd4c 1100w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9066885a-0903-fe42-8192-31ea376b8937.png?w=1650&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=94edc81296a6d6ac6f7962f72a699c89 1650w, https://mintcdn.com/asapp/COy3KdZUtsAnzs_4/image/uuid-9066885a-0903-fe42-8192-31ea376b8937.png?w=2500&fit=max&auto=format&n=COy3KdZUtsAnzs_4&q=85&s=fa614b39a68d3c6bc9fa0c704af529b3 2500w" />
</Frame>

## Integration

ASAPP can integrate with customer Knowledge Base systems or CRMs to pull data and make it available to Agent Desk. This is accomplished by a dedicated service, which can consume data from external systems that support standard REST APIs. The service layer is flexible enough to integrate with various industry standard Knowledge Base systems as well as in-house developed proprietary ones. The service programmatically retrieves new and updated articles on a regular basis to surface fresh and accurate content to agents in real-time.

Data pulled from external systems is transformed into ASAPP's standard format, and securely stored in S3 and in a database. Refer to the [Data Storage](#data-storage) section below for more details.

### Configuration

The service that integrates with customers is configuration driven so it can interface with different systems supporting different data formats/structures.

ASAPP requires the following information to integrate with APIs:

* REST endpoints and API definitions, data schemas and SLAs
  * URLs, Connection info, and Test Accounts for each environment
  * Authentication and Authorization requirements
  * JSON schema defining requests and responses, preferably Swagger
  * API Host that can handle HTTPS/TLS traffic
  * Resource
  * HTTP Method(s) supported
  * Content Type(s) supported and other Request Headers
  * Error handling documentation
  * Response sizes to expect
  * API Call Rate limits, if any
  * Response time SLAs
* API Response Requirements
  * Every 'article' should contain at least a unique identifier and last updated date timestamp.
  * Hierarchical data needs to clearly define the parent-child relationships
  * Content should not contain any PII/PCI related information
* Refreshing Data
  * On a set cadence as determined and agreed upon by both parties
* Size of data to help in capacity planning and scaling

## Data Storage

Once the service receives KB content, it stores the data in a secure S3 bucket that serves as the source of truth for all Knowledge Base articles. It then structures and packages the data into standard Knowledge Base types: Category, Folder and Article. The service then cleans, processes, and stores the packaged data in a database for further usage.

## Data Processing

ASAPP runs all the Knowledge Base articles stored in the database through a Knowledge Base Ranker service, which ranks articles and feeds Agent Augmentation. Given a set of user utterances, KB Ranker service assigns a score to every article of the Knowledge Base based on how relevant those articles are for that agent at that moment in the conversation. ASAPP determines relevance by taking into account the frequency of words in an article within the corpus of articles, and words of a given subset of utterances.

## Data Refresh

ASAPP can refresh data periodically and schedule it to meet customer needs. ASAPP uses a Unix cron style scheduler to run the refresh job, which allows flexible configuration.

Data Refresh replaces all of the current folders/articles with the new ones received.The refresh does not affect the ranking of articles, as their state is maintained separately.
