# Source: https://docs.avaamo.com/user-guide/llamb/improve-user-experience-feedback-analytics.md

# Improve user experience - Feedback, Analytics

The best way to improve user experience with LLaMB is by collecting early user feedback from the domain experts and SMEs in the UAT stage itself. You can also leverage the Analytics board to draw some inference on the the usage of intents in your `LLaMB Content skill`.

This article covers the following topics that can help improve user experience with the `LLaMB Content skill`:&#x20;

1. [Using user feedback ](#user-feedback)
2. [Using Analytics](#insights-from-analytics)

## User Feedback

Regularly collecting and analyzing user feedback allows for ongoing improvements and adjustments, ensuring the agent evolves in response to the user's needs.

User feedback is crucial for various reasons:

* Provides valuable insights into users' expectations.&#x20;
* Highlights the areas where improvements can be made to enhance the overall user experience.
* Identifies issues, bugs, or unexpected behaviors that can be addressed promptly.

### Collecting user feedback

The suggested approach to collect feedback is to start early in the UAT phase. Gather user feedback from UAT users before deploying the agent in the live production environment. User feedback obtained during UAT varies from that collected in a production environment.

Within the UAT environment, the emphasis is on gathering detailed and accurate feedback to enhance the user experience before deploying the agent to the actual production users. The users can use the thumbs-up or thumbs-down option to provide the feedback. See [UAT](https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/uat), for more information.

The following illustration depicts the feedback collected on the thumbs-down option:

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FmIAd1OO7fG91kz4DmSU7%2Fimage.png?alt=media&#x26;token=4366e50c-1b28-4431-bcd2-fd49c16b6701" alt=""><figcaption></figcaption></figure>

After the agent is deployed in the production environment, the actual users can share the feedback using thumbs up and thumbs down options in the agent response. When the user selects the thumbs-down option, the agent collects a few details from the user that can help is fine-tuning the agent:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2F7M0K5etoqVcjcvEAoQTy%2Fimage.png?alt=media\&token=a4b6027d-c6c7-4620-9e15-debfaebb36de)

### Monitor user feedback

You can view the user feedback from the [Monitor -> Analytics](https://docs.avaamo.com/user-guide/how-to/build-agents/monitor-and-analyze/analytics#user-feedback) page and also under [Learning -> User Feedback](https://docs.avaamo.com/user-guide/how-to/build-agents/learning-continuous-improvement/feedback) section.&#x20;

Alternatively, you can also use the [User Feedback API](https://docs.avaamo.com/user-guide/ref/avaamo-platform-api-documentation/feedback-api) to collect feedback periodically to learn and analyze the user's experience when interacting with your agent.&#x20;

### Analyze feedback and improvise

When using LLaMB, the following are a few recommendations that can help incorporate user feedback and improve the overall user experience of the agent:

* Check if all the documents and URLs are ingested successfully in LLaMB without any errors. See Troubleshooting tips, for inputs on resolving errors if any.
* Isolate the problem;
  1. Check if the source from where the answer is inferred in the agent does contain the expected response from the user. If not, consider updating the source.
  2. If the source contains the expected response, but you are unable to get the expected behavior, check if updating the knowledge base on the `LLaMB Content skill`, can help. See [View and edit knowledge](https://docs.avaamo.com/user-guide/llamb/get-started/step-2-ingest-enterprise-content/view-and-edit-knowledge), for more information.
  3. If the behavior persists after #1 and #2, contact Avaamo Support for further assistance.

### Insights from Analytics

The `Top LLaMB Content intents` block in the `Monitor -> Analytics` page gives you valuable insights into the top user intents responding to the user query.

<figure><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FY1Jv6l3dpfdEPe0mVTwu%2Fimage.png?alt=media&#x26;token=79422b29-fd4e-484b-a266-a68684a6da7a" alt=""><figcaption></figcaption></figure>

It helps you learn and understand how users are interacting with your assistant. With these statistics, you can decide how and where to further improve your agent based on your business requirements.&#x20;

See [Top LLaMB Content intents](https://docs.avaamo.com/user-guide/how-to/build-agents/monitor-and-analyze/analytics#top-llamb-content-intents), for more information.
