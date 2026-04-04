# Source: https://docs.mulesoft.com/studio/change-jdk-config-in-projects

Title: Selecting a Different Java Version to Run the Embedded Mule Runtime

URL Source: https://docs.mulesoft.com/studio/change-jdk-config-in-projects

Markdown Content:
Selecting a Different Java Version to Run the Embedded Mule Runtime | MuleSoft Documentation
===============

Skip to left navigation Skip to main content Skip to page navigation

[](https://www.mulesoft.com/)

* Products For IT Teams[Anypoint Platform World’s #1 integration and API platform](https://www.mulesoft.com/platform/enterprise-integration)Integration[Code Builder](https://www.mulesoft.com/platform/api/anypoint-code-builder)[Exchange](https://www.mulesoft.com/platform/exchange)[Connectors](https://www.mulesoft.com/platform/cloud-connectors)[MCP Support](https://www.mulesoft.com/platform/ai/model-context-protocol)API management[Flex Gateway](https://www.mulesoft.com/platform/api/flex-api-gateway)[API Governance](https://www.mulesoft.com/platform/api/governance-anypoint)[Monitoring](https://www.mulesoft.com/platform/api/monitoring-anypoint)[API Manager](https://www.mulesoft.com/platform/api/manager)[See all](https://www.mulesoft.com/platform/anypoint-platform-features)  Try for free[Sign up to Anypoint Platform](https://anypoint.mulesoft.com/login/#/signup?apintent=generic)[Download Anypoint Code Builder, Studio, Mule](https://www.mulesoft.com/lp/dl/anypoint-mule-studio)  For Business Teams[MuleSoft for Flow: Integration Point to point integration with clicks, not code](https://www.mulesoft.com/platform/flow-integration)[MuleSoft IDP Extract unstructured data from documents with AI](https://www.mulesoft.com/platform/intelligent-document-processing)[MuleSoft RPA Automate tasks with bots](https://www.mulesoft.com/platform/rpa)[Dataloader.io Securely import and export unlimited Salesforce data](https://dataloader.io/)For AI[MuleSoft for Agentforce Power Agentforce with APIs and actions](https://www.mulesoft.com/platform/agentforce)[Einstein for MuleSoft Build integrations and automations faster using natural language](https://www.mulesoft.com/ai/einstein-for-mulesoft)     [![Image 7: A graphic of MuleSoft MCP Support](https://mulesoftd8.www.msit.io/sites/default/files/cmm_files/hero_image--3-.png) MuleSoft MCP Support is now available Learn how to transform your APIs to agent ready assets in minutes. Learn more](https://www.mulesoft.com/platform/ai/model-context-protocol)
* Solutions Featured Solutions[API Management Manage and secure any API, built and deployed anywhere](https://www.mulesoft.com/api/management)[Integration Connect any system, data, or API to integrate at scale](https://www.mulesoft.com/integration)[Automation Automate processes and tasks for every team](https://www.mulesoft.com/automation)[MuleSoft AI Connect data and automate workflows with AI](https://www.mulesoft.com/platform/ai)Featured Integration[Salesforce Power connected experiences with Salesforce integration](https://www.mulesoft.com/integration/salesforce)[SAP Unlock SAP and connect your IT landscape](https://www.mulesoft.com/integration/sap)[AWS Get the most out of AWS with integration and APIs](https://www.mulesoft.com/integration-solutions/soa/aws)[Small business Unlock AI-powered success for your small business](https://www.mulesoft.com/small-business)   By Industry[Financial services](https://www.mulesoft.com/solutions/financial-services)[Government](https://www.mulesoft.com/integration-solutions/soa/government)[Healthcare and life sciences](https://www.mulesoft.com/integration-solutions/soa/healthcare)[Higher education](https://www.mulesoft.com/integration-solutions/soa/higher-education)[Insurance](https://www.mulesoft.com/integration-solutions/soa/insurance)[Manufacturing](https://www.mulesoft.com/integration-solutions/api/manufacturing-edi-erp)[Media and telecom](https://www.mulesoft.com/integration-solutions/soa/digital-media)[Retail](https://www.mulesoft.com/integration-solutions/saas/retail)[Consumer goods](https://www.mulesoft.com/integration-solutions/soa/consumer-goods)By Initiative[B2B EDI integration](https://www.mulesoft.com/integration/b2b-edi-platform)[DevOps](https://www.mulesoft.com/integration-solutions/api/devops)[eCommerce](https://www.mulesoft.com/integration-solutions/api/ecommerce)[Event-Driven Architecture](https://www.mulesoft.com/event-driven-architecture)[iPaaS](https://www.mulesoft.com/integration-solutions/api/ipaas)[Legacy system modernization](https://www.mulesoft.com/legacy-system-modernization/legacy-system-modernization-solution)[Microservices](https://www.mulesoft.com/api/microservices)[Move to the cloud](https://www.mulesoft.com/integration/move-to-the-cloud)[Omnichannel](https://www.mulesoft.com/integration-solutions/api/omnichannel)[SaaS integration](https://www.mulesoft.com/integration-solutions/api/saas)[Single view of customer](https://www.mulesoft.com/integration-solutions/api/360-degree-view-customer)[See all solutions](https://www.mulesoft.com/integration-solutions)      [![Image 8: An image of the ebook cover: Create Connected Experiences with MuleSoft + AI](https://www.mulesoft.com/sites/default/files/cmm_files/image-mulesoft-solutions-create-connected-experiences-with-ai.png) Create connected experiences with AI Learn the critical steps to developing an AI strategy and foundation. Read more](https://www.mulesoft.com/lp/ebook/api/salesforce-integration-customer-360)
* Services Training[Courses](https://trailheadacademy.salesforce.com/products/mulesoft#f-products=Mulesoft)[Certifications](https://trailheadacademy.salesforce.com/products/mulesoft#f-products=MuleSoft%E2%80%9D%20target=%E2%80%9D_blank%E2%80%9D%20role=)[Training credits](https://trailhead.salesforce.com/help?article=Salesforce-Learning-Credits-FAQ-and-Redemption-Process)Customer success[MuleSoft Catalyst](https://www.mulesoft.com/support-and-services/consulting)[Business Value Services](https://www.mulesoft.com/support-and-services/mobilize-consulting-solutions)Support[Help Center](https://help.mulesoft.com/s/)[Community Forums](https://trailhead.salesforce.com/trailblazer-community/neighborhoods/mulesoft)      [![Image 9: An image of the ebook cover: 3 Predictions for the Future of Connected AI Agents](https://www.mulesoft.com/sites/default/files/cmm_files/image-mulesoft-services-future-of-connected-ai-agents.png) Future of connected AI agents Discover how to prepare for the future of autonomous AI agents. Read more](https://www.mulesoft.com/lp/whitepaper/3-predictions-future-of-connected-ai-agents)
* Resources Featured Resources[Customer stories](https://www.mulesoft.com/case-studies)[Newsroom](https://www.salesforce.com/news/products/mulesoft/)[Newsletter sign-up](https://www.linkedin.com/newsletters/technically-speaking-7140068811264651264/) Explore[Webinars](https://www.mulesoft.com/webinars)[Demos](https://www.mulesoft.com/integration-resources?type%5B0%5D=demo)[Videos](https://videos.mulesoft.com/)[Analyst reports](https://www.mulesoft.com/reports)[eBooks](https://www.mulesoft.com/ebook)[Whitepapers](https://www.mulesoft.com/whitepaper/integration-use-cases)[Infographics](https://www.mulesoft.com/infographics)[Articles](https://www.mulesoft.com/resources/articles)[Blog](https://blogs.mulesoft.com/bloghome/)[API University](https://www.mulesoft.com/api-university/what-are-apis-and-how-do-they-work) [See all resources](https://www.mulesoft.com/integration-resources)  Events[MuleSoft Connect:AI](https://mulesoft.com/connect-ai)[MuleSoft at Dreamforce](https://www.mulesoft.com/dreamforce)[MuleSoft at TrailblazerDX](https://www.salesforce.com/trailblazerdx)[Community Meetups](https://meetups.mulesoft.com/)[All events](https://www.mulesoft.com/events)     [![Image 10: A graphic showing the keynote presentation at Connect:AI](https://mulesoftd8.www.msit.io/sites/default/files/cmm_files/keynote-opt02_11zon.jpg) Go from composability to agent actionability Relive the best moments from Connect:AI with our on-demand sessions. Start watching](https://www.mulesoft.com/connect-ai)

* Developers [Getting started](https://developer.mulesoft.com/)[Community](https://www.mulesoft.com/community)[Training](https://trailheadacademy.salesforce.com/products/mulesoft#f-products=Mulesoft)[Tutorials](https://developer.mulesoft.com/tutorials-and-howtos)[Documentation](https://docs.mulesoft.com/general/)
* Partners For customers[Find a partner](https://www.mulesoft.com/integration-partner/finder)For partners[Become a partner](https://www.mulesoft.com/integration-partner/become-partner)

[Contact Us](https://www.mulesoft.com/contact)1-800-596-4880

* [English (Full site)](https://docs.mulesoft.com/)[日本語](https://docs.mulesoft.com/jp)
* Login [Anypoint Platform](https://anypoint.mulesoft.com/login/#/signin?apintent=generic)[Composer](https://composer.mulesoft.com/login/sign-in)[Help Center](https://help.mulesoft.com/s/login/)
* [Free trial](https://anypoint.mulesoft.com/login/#/signup?apintent=generic)

[](https://www.mulesoft.com/)

* Products For IT Teams[Anypoint Platform World’s #1 integration and API platform](https://www.mulesoft.com/platform/enterprise-integration)Integration[Code Builder](https://www.mulesoft.com/platform/api/anypoint-code-builder)[Exchange](https://www.mulesoft.com/platform/exchange)[Connectors](https://www.mulesoft.com/platform/cloud-connectors)[MCP Support](https://www.mulesoft.com/platform/ai/model-context-protocol)API management[Flex Gateway](https://www.mulesoft.com/platform/api/flex-api-gateway)[API Governance](https://www.mulesoft.com/platform/api/governance-anypoint)[Monitoring](https://www.mulesoft.com/platform/api/monitoring-anypoint)[API Manager](https://www.mulesoft.com/platform/api/manager)[See all](https://www.mulesoft.com/platform/anypoint-platform-features)  Try for free[Sign up to Anypoint Platform](https://anypoint.mulesoft.com/login/#/signup?apintent=generic)[Download Anypoint Code Builder, Studio, Mule](https://www.mulesoft.com/lp/dl/anypoint-mule-studio)  For Business Teams[MuleSoft for Flow: Integration Point to point integration with clicks, not code](https://www.mulesoft.com/platform/flow-integration)[MuleSoft IDP Extract unstructured data from documents with AI](https://www.mulesoft.com/platform/intelligent-document-processing)[MuleSoft RPA Automate tasks with bots](https://www.mulesoft.com/platform/rpa)[Dataloader.io Securely import and export unlimited Salesforce data](https://dataloader.io/)For AI[MuleSoft for Agentforce Power Agentforce with APIs and actions](https://www.mulesoft.com/platform/agentforce)[Einstein for MuleSoft Build integrations and automations faster using natural language](https://www.mulesoft.com/ai/einstein-for-mulesoft)     [![Image 11: A graphic of MuleSoft MCP Support](https://mulesoftd8.www.msit.io/sites/default/files/cmm_files/hero_image--3-.png) MuleSoft MCP Support is now available Learn how to transform your APIs to agent ready assets in minutes. Learn more](https://www.mulesoft.com/platform/ai/model-context-protocol)
* Solutions Featured Solutions[API Management Manage and secure any API, built and deployed anywhere](https://www.mulesoft.com/api/management)[Integration Connect any system, data, or API to integrate at scale](https://www.mulesoft.com/integration)[Automation Automate processes and tasks for every team](https://www.mulesoft.com/automation)[MuleSoft AI Connect data and automate workflows with AI](https://www.mulesoft.com/platform/ai)Featured Integration[Salesforce Power connected experiences with Salesforce integration](https://www.mulesoft.com/integration/salesforce)[SAP Unlock SAP and connect your IT landscape](https://www.mulesoft.com/integration/sap)[AWS Get the most out of AWS with integration and APIs](https://www.mulesoft.com/integration-solutions/soa/aws)[Small business Unlock AI-powered success for your small business](https://www.mulesoft.com/small-business)   By Industry[Financial services](https://www.mulesoft.com/solutions/financial-services)[Government](https://www.mulesoft.com/integration-solutions/soa/government)[Healthcare and life sciences](https://www.mulesoft.com/integration-solutions/soa/healthcare)[Higher education](https://www.mulesoft.com/integration-solutions/soa/higher-education)[Insurance](https://www.mulesoft.com/integration-solutions/soa/insurance)[Manufacturing](https://www.mulesoft.com/integration-solutions/api/manufacturing-edi-erp)[Media and telecom](https://www.mulesoft.com/integration-solutions/soa/digital-media)[Retail](https://www.mulesoft.com/integration-solutions/saas/retail)[Consumer goods](https://www.mulesoft.com/integration-solutions/soa/consumer-goods)By Initiative[B2B EDI integration](https://www.mulesoft.com/integration/b2b-edi-platform)[DevOps](https://www.mulesoft.com/integration-solutions/api/devops)[eCommerce](https://www.mulesoft.com/integration-solutions/api/ecommerce)[Event-Driven Architecture](https://www.mulesoft.com/event-driven-architecture)[iPaaS](https://www.mulesoft.com/integration-solutions/api/ipaas)[Legacy system modernization](https://www.mulesoft.com/legacy-system-modernization/legacy-system-modernization-solution)[Microservices](https://www.mulesoft.com/api/microservices)[Move to the cloud](https://www.mulesoft.com/integration/move-to-the-cloud)[Omnichannel](https://www.mulesoft.com/integration-solutions/api/omnichannel)[SaaS integration](https://www.mulesoft.com/integration-solutions/api/saas)[Single view of customer](https://www.mulesoft.com/integration-solutions/api/360-degree-view-customer)[See all solutions](https://www.mulesoft.com/integration-solutions)      [![Image 12: An image of the ebook cover: Create Connected Experiences with MuleSoft + AI](https://www.mulesoft.com/sites/default/files/cmm_files/image-mulesoft-solutions-create-connected-experiences-with-ai.png) Create connected experiences with AI Learn the critical steps to developing an AI strategy and foundation. Read more](https://www.mulesoft.com/lp/ebook/api/salesforce-integration-customer-360)
* Services Training[Courses](https://trailheadacademy.salesforce.com/products/mulesoft#f-products=Mulesoft)[Certifications](https://trailheadacademy.salesforce.com/products/mulesoft#f-products=MuleSoft%E2%80%9D%20target=%E2%80%9D_blank%E2%80%9D%20role=)[Training credits](https://trailhead.salesforce.com/help?article=Salesforce-Learning-Credits-FAQ-and-Redemption-Process)Customer success[MuleSoft Catalyst](https://www.mulesoft.com/support-and-services/consulting)[Business Value Services](https://www.mulesoft.com/support-and-services/mobilize-consulting-solutions)Support[Help Center](https://help.mulesoft.com/s/)[Community Forums](https://trailhead.salesforce.com/trailblazer-community/neighborhoods/mulesoft)      [![Image 13: An image of the ebook cover: 3 Predictions for the Future of Connected AI Agents](https://www.mulesoft.com/sites/default/files/cmm_files/image-mulesoft-services-future-of-connected-ai-agents.png) Future of connected AI agents Discover how to prepare for the future of autonomous AI agents. Read more](https://www.mulesoft.com/lp/whitepaper/3-predictions-future-of-connected-ai-agents)
* Resources Featured Resources[Customer stories](https://www.mulesoft.com/case-studies)[Newsroom](https://www.salesforce.com/news/products/mulesoft/)[Newsletter sign-up](https://www.linkedin.com/newsletters/technically-speaking-7140068811264651264/) Explore[Webinars](https://www.mulesoft.com/webinars)[Demos](https://www.mulesoft.com/integration-resources?type%5B0%5D=demo)[Videos](https://videos.mulesoft.com/)[Analyst reports](https://www.mulesoft.com/reports)[eBooks](https://www.mulesoft.com/ebook)[Whitepapers](https://www.mulesoft.com/whitepaper/integration-use-cases)[Infographics](https://www.mulesoft.com/infographics)[Articles](https://www.mulesoft.com/resources/articles)[Blog](https://blogs.mulesoft.com/bloghome/)[API University](https://www.mulesoft.com/api-university/what-are-apis-and-how-do-they-work) [See all resources](https://www.mulesoft.com/integration-resources)  Events[MuleSoft Connect:AI](https://mulesoft.com/connect-ai)[MuleSoft at Dreamforce](https://www.mulesoft.com/dreamforce)[MuleSoft at TrailblazerDX](https://www.salesforce.com/trailblazerdx)[Community Meetups](https://meetups.mulesoft.com/)[All events](https://www.mulesoft.com/events)     [![Image 14: A graphic showing the keynote presentation at Connect:AI](https://mulesoftd8.www.msit.io/sites/default/files/cmm_files/keynote-opt02_11zon.jpg) Go from composability to agent actionability Relive the best moments from Connect:AI with our on-demand sessions. Start watching](https://www.mulesoft.com/connect-ai)

* Developers [Getting started](https://developer.mulesoft.com/)[Community](https://www.mulesoft.com/community)[Training](https://trailheadacademy.salesforce.com/products/mulesoft#f-products=Mulesoft)[Tutorials](https://developer.mulesoft.com/tutorials-and-howtos)[Documentation](https://docs.mulesoft.com/general/)
* Partners For customers[Find a partner](https://www.mulesoft.com/integration-partner/finder)For partners[Become a partner](https://www.mulesoft.com/integration-partner/become-partner)

* Language [English (Full site)](https://docs.mulesoft.com/)[日本語](https://docs.mulesoft.com/jp)
* Contact By phone[1-800-596-4880](tel:1-800-596-4880) Online[Contact Us](https://www.mulesoft.com/contact)

* Login [Anypoint Platform](https://anypoint.mulesoft.com/login/#/signin?apintent=generic)[Composer](https://composer.mulesoft.com/login/sign-in)[Help Center](https://help.mulesoft.com/s/login/)

[Free trial](https://anypoint.mulesoft.com/login/#/signup?apintent=generic)

[Link to MuleSoft Twitter profile](https://twitter.com/MuleSoft)[Link to MuleSoft Linkedin profile](https://www.linkedin.com/company/mulesoft)[Link to MuleSoft Facebook page](https://www.facebook.com/MuleSoft)[Link to MuleSoft Instagram profile](https://www.instagram.com/mulesoft/)[Link to MuleSoft Videos platform](https://videos.mulesoft.com/)[Link to MuleSoft Twitch profile](https://www.twitch.tv/mulesoft_community)
© Copyright 2025 Salesforce, Inc. [All rights reserved](https://www.salesforce.com/company/legal/intellectual/).

Search Docs

![Image 15](https://docs.mulesoft.com/_/img/icons/arrow-down.svg)

* [Home](https://docs.mulesoft.com/general/)
* Release Notes
* [Archived Documentation![Image 16: Leaving the Site](https://docs.mulesoft.com/_/img/icons/external-link.svg)](https://archive.docs.mulesoft.com/)![Image 17: Archived Documentation information](https://docs.mulesoft.com/_/img/icons/tooltip-gray.svg)  

### Getting Started

* [MuleSoft AI](https://docs.mulesoft.com/general/learning-map-mulesoft-ai)
* [Agent Fabric](https://docs.mulesoft.com/general/learning-map-agent-fabric)
  * [Agent Fabric Release Notes](https://docs.mulesoft.com/general/agent-fabric-release-notes)
  * [Get Started with Agent Networks](https://docs.mulesoft.com/general/agent-networks-get-started)

* [API Management](https://docs.mulesoft.com/general/learning-map-api-management)
* [Usage Reports](https://docs.mulesoft.com/general/usage-reports)
  * [Release Notes](https://docs.mulesoft.com/general/usage-reports-release-notes)
  * [Usage and Pricing Metrics Reference](https://docs.mulesoft.com/general/usage-metrics)
  * [Pricing](https://docs.mulesoft.com/general/pricing)
  * [Troubleshooting Usage Reports](https://docs.mulesoft.com/general/troubleshooting-usage-reports)

* [Java Support](https://docs.mulesoft.com/general/java-support)
  * [Upgrading Java for Custom Connectors (Partners)](https://docs.mulesoft.com/general/partner-connector-upgrade)
  * [Upgrading Java for Custom Connectors (Customers)](https://docs.mulesoft.com/general/customer-connector-upgrade)
  * [Upgrading Java for Policies and API Proxies](https://docs.mulesoft.com/general/upgrade-policies-proxies)

* [Browser Support](https://docs.mulesoft.com/general/browser-support)
* [Glossary](https://docs.mulesoft.com/general/glossary)
* [Build an API from Start to Finish](https://docs.mulesoft.com/general/api-led-overview)
  * [Step 1. Prerequisites](https://docs.mulesoft.com/general/api-led-prerequisites)
  * [Step 2. Design an API Specification](https://docs.mulesoft.com/general/api-led-design)
  * [Step 3. Develop the API](https://docs.mulesoft.com/general/api-led-develop)
  * [Step 4. Add Validation and Error Handling](https://docs.mulesoft.com/general/api-led-test)
  * [Step 5. Deploy the API to CloudHub](https://docs.mulesoft.com/general/api-led-deploy)
  * [Step 6. Operate the API](https://docs.mulesoft.com/general/api-led-operate)

* [Contribute to MuleSoft Documentation](https://docs.mulesoft.com/general/contribute)

### Hosting

* Hosting Options
* CloudHub 2.0
* CloudHub
* Runtime Fabric 3.0  Current version 3.0  Previous versions 2.11 2.10 2.9 2.8 2.7 2.6 2.5
* Anypoint Platform Private Cloud Edition 4.1  Current version 4.1  Previous versions 4.0 3.2
* Government Cloud
* EU Control Plane
* Hyperforce
* Hybrid Standalone

### Docs by Product

* Accelerators
* Access Management
* Agent Visualizer
* Anypoint CLI 4.x  Current version 4.x  Previous versions 3.x
* Anypoint Code Builder
* API Community Manager
* API Experience Hub
* API Functional Monitoring
* API Governance
* API Manager 2.x

* APIkit Mule 4

* Composer
* Composer for Salesforce
* Connector Builder
* Connectors
* DataGraph
* DataWeave 2.11 (Mule 4.11)  Current version 2.11 (Mule 4.11)  Previous versions 2.10 (Mule 4.10) 2.9 (Mule 4.9) 2.8 (Mule 4.8) 2.7 (Mule 4.7) 2.6 (Mule 4.6) 2.5 (Mule 4.5) 2.4 (Mule 4.4) 2.3 (Mule 4.3)
* Design Center
* Exchange
* Gateway
* IDP
* Monitoring
* MQ
* Mule Runtime 4.11  Current version 4.11  Previous versions 4.10 4.9 4.8 4.7 4.6 4.5 4.4 4.3
* Mule SDK 1.11

* MuleSoft MCP Server
* MUnit 3.7  Current version 3.7  Previous versions 3.6 2.3
* Object Store
* Partner Manager 2.x

* RPA
* Runtime Manager
* Security
* Studio
  * [Overview](https://docs.mulesoft.com/studio/)
  * [Release Notes](https://docs.mulesoft.com/studio/studio-release-notes)
  * [Downloading and Installing Studio](https://docs.mulesoft.com/studio/to-download-and-install-studio)
    * [Windows](https://docs.mulesoft.com/studio/to-download-and-install-studio-wx)
    * [Linux](https://docs.mulesoft.com/studio/to-download-and-install-studio-lx)
    * [MacOS](https://docs.mulesoft.com/studio/to-download-and-install-studio-ox)

  * [Updating Workspaces](https://docs.mulesoft.com/studio/update-workspace)
  * [Exporting and Importing Studio Preferences](https://docs.mulesoft.com/studio/import-and-export-preferences-studio)
  * [Installing Mule Runtime Engine in Studio](https://docs.mulesoft.com/studio/install-mule-runtime-versions)
  * [Importing API Specifications](https://docs.mulesoft.com/studio/import-api-specification)
    * [From Exchange](https://docs.mulesoft.com/studio/import-api-specification-exchange)
    * [From Maven](https://docs.mulesoft.com/studio/import-api-specification-maven)
    * [From a Local File](https://docs.mulesoft.com/studio/import-api-specification-local-file)
    * [From MuleSoft VCS](https://docs.mulesoft.com/studio/import-api-specification-design-center)

  * [API Development in Studio](https://docs.mulesoft.com/studio/api-development-studio)
    * [Creating an API Specification Project in Studio](https://docs.mulesoft.com/studio/create-api-specification-studio)
    * [Tracking the Number of Billable Flows in Studio](https://docs.mulesoft.com/studio/flow-counting-studio)
    * [Testing your API Specification Using the API Console](https://docs.mulesoft.com/studio/test-specification-api-console)

  * [Sync Your API Projects with API Sync](https://docs.mulesoft.com/studio/api-sync)
    * [Syncing API Specifications with MuleSoft VCS](https://docs.mulesoft.com/studio/sync-api-projects-design-center)
    * [Updating the API Specification in Your Project](https://docs.mulesoft.com/studio/sync-update-api-spec)
    * [Editing Imported API Specifications in Your Projects in Studio](https://docs.mulesoft.com/studio/sync-imported-api-specifications-design-center)
    * [Solving Conflicts](https://docs.mulesoft.com/studio/solving-conflicts-api-projects)
    * [Git Staging View Reference](https://docs.mulesoft.com/studio/git-staging-view-reference)
    * [Publishing an API Project to Exchange](https://docs.mulesoft.com/studio/publish-api-project-to-exchange)
    * [Editing Your API Project Exchange File](https://docs.mulesoft.com/studio/edit-exchange-json-file)

  * [Importing and Export Projects](https://docs.mulesoft.com/studio/import-export-packages)
    * [Importing a Mule Project from Exchange](https://docs.mulesoft.com/studio/import-project-exchange)
    * [Publishing a Project to Exchange](https://docs.mulesoft.com/studio/export-to-exchange-task)

  * [Adding Modules to Your Project](https://docs.mulesoft.com/studio/add-modules-in-studio-to)
    * [Updating your Modules](https://docs.mulesoft.com/studio/update-modules)
    * [Adding Custom Modules to Your Project](https://docs.mulesoft.com/studio/add-custom-modules-in-studio-to)

  * [Search Inside Your API Specification Dependencies](https://docs.mulesoft.com/studio/api-search)
  * [Studio Debugger](https://docs.mulesoft.com/studio/visual-debugger-concept)
    * [Breakpoints](https://docs.mulesoft.com/studio/breakpoints-concepts)
    * [Breakpoints View Reference](https://docs.mulesoft.com/studio/breakpoint-view-reference)
    * [DataWeave Expression Watches](https://docs.mulesoft.com/studio/evaluate-dw-expressions)
    * [Evaluating DataWeave Expression View Reference](https://docs.mulesoft.com/studio/dw-expression-watches-view-reference)
    * [Mule Debugger View Reference](https://docs.mulesoft.com/studio/mule-debugger-view-reference)
    * [Starting the Mule Server In Debug Mode](https://docs.mulesoft.com/studio/to-start-server-debug-mode)
    * [Connecting the Java Debugger](https://docs.mulesoft.com/studio/java-debugger-preference)
    * [Handling Inaccessible Fields](https://docs.mulesoft.com/studio/setting-inaccessible-fields)

  * [Testing Your Mule Project with MUnit](https://docs.mulesoft.com/studio/test-with-munit-in-studio)
    * [Using MUnit Coverage in Studio](https://docs.mulesoft.com/studio/coverage-studio-concept)

  * [DataSense](https://docs.mulesoft.com/studio/datasense-concept)
    * [DataSense Explorer](https://docs.mulesoft.com/studio/datasense-explorer)

  * [Metadata Editor](https://docs.mulesoft.com/studio/metadata-editor-concept)
    * [Accessing the Metadata Editor](https://docs.mulesoft.com/studio/access-metadata-editor-task)
    * [Creating a Metadata Class](https://docs.mulesoft.com/studio/create-metadata-class-task)
    * [Metadata Propagation Between Flows](https://docs.mulesoft.com/studio/metadata-propagation-between-flows)
    * [Propagate Metadata to Other Flows](https://docs.mulesoft.com/studio/propagate-metadata-studio)

  * [Transform Message Component](https://docs.mulesoft.com/studio/transform-message-component-concept-studio)
    * [Workflow: Create a Mapping](https://docs.mulesoft.com/studio/workflow-create-mapping-ui-studio)
      * [Define Input and Output Structure of a Transformation](https://docs.mulesoft.com/studio/input-output-structure-transformation-studio-task)
      * [Graphically Construct a Mapping](https://docs.mulesoft.com/studio/graphically-construct-mapping-studio-task)
      * [Previewing the Output of a Transformation](https://docs.mulesoft.com/studio/preview-transformation-output-studio-task)

    * [Changing the Target Output of a Transformation](https://docs.mulesoft.com/studio/change-target-output-transformation-studio-task)
    * [Adding Another Output Target](https://docs.mulesoft.com/studio/add-another-output-transform-studio-task)
    * [Moving Transformations to Separate Files](https://docs.mulesoft.com/studio/move-transformations-separate-file-studio-task)

  * [Sign in to Anypoint Platform from Studio](https://docs.mulesoft.com/studio/login-platform-from-studio)
    * [Adding Anypoint Platform User Accounts](https://docs.mulesoft.com/studio/set-credentials-in-studio-to)

  * [Configure Anypoint Platform Cloud in Studio](https://docs.mulesoft.com/studio/set-anypoint-platform-cloud)
    * [Deploying Mule Apps to CloudHub](https://docs.mulesoft.com/studio/deploy-mule-application-task)
    * [Configuring Domains](https://docs.mulesoft.com/studio/domain-support-concept)
      * [Designing Mule Domains](https://docs.mulesoft.com/studio/domain-studio-tasks)

    * [Configuring Private Cloud Edition in Studio](https://docs.mulesoft.com/studio/pce-configuration)
      * [Configuring PCE 4 in Studio](https://docs.mulesoft.com/studio/pce4-configuration)
      * [Configuring PCE 3 in Studio](https://docs.mulesoft.com/studio/pce3-configuration)
        * [Configure Private Cloud Edition in Studio (macOS)](https://docs.mulesoft.com/studio/pce-configuration-macos)
        * [Configure Private Cloud Edition in Studio (Windows)](https://docs.mulesoft.com/studio/pce-configuration-windows)

    * [Configuring MuleSoft Government Cloud from Studio](https://docs.mulesoft.com/studio/govcloud-config)
    * [Configuring Anypoint Studio for Control Planes](https://docs.mulesoft.com/studio/hyperforce-configuration)

  * [Securing Storage](https://docs.mulesoft.com/studio/secure-storage)
  * [Configuring Proxy Settings](https://docs.mulesoft.com/studio/proxy-settings-task)
  * [Configuring Studio Browser Settings](https://docs.mulesoft.com/studio/browser-settings)
  * [Selecting a Different JRE to Run the Embedded Mule Runtime Engine](https://docs.mulesoft.com/studio/change-jdk-config-in-projects)
  * [Studio Update Sites](https://docs.mulesoft.com/studio/studio-update-sites)
  * [Using Maven in Studio](https://docs.mulesoft.com/studio/use-maven-in-studio)
    * [Configuring Studio to Use Your Own Maven](https://docs.mulesoft.com/studio/configure-studio-to-use-your-own-maven)
    * [Maven Preferences Reference](https://docs.mulesoft.com/studio/maven-preferences-reference)

  * [Starting Studio Using Your Own JDK](https://docs.mulesoft.com/studio/change-jdk-for-studio)
    * [Windows](https://docs.mulesoft.com/studio/change-jdk-for-studio-wx)
    * [Linux](https://docs.mulesoft.com/studio/change-jdk-for-studio-lx)
    * [MacOS](https://docs.mulesoft.com/studio/change-jdk-for-studio-ox)

  * [Troubleshooting](https://docs.mulesoft.com/studio/troubleshooting-studio)
    * [Troubleshooting Issues with Platform Content in Studio](https://docs.mulesoft.com/studio/faq-default-browser-config)
      * [Windows](https://docs.mulesoft.com/studio/studio-xulrunner-wx-task)
      * [Linux](https://docs.mulesoft.com/studio/studio-xulrunner-lnx-task)
      * [MacOS](https://docs.mulesoft.com/studio/studio-xulrunner-unx-task)

    * [Compatibility Issues](https://docs.mulesoft.com/studio/compatibility-issues-runtime-java)

* Visualizer

Skip to main content

[View on GitHub](https://github.com/mulesoft/docs-studio/blob/latest/modules/ROOT/pages/change-jdk-config-in-projects.adoc)
On this page
=============

1. [Mule Runtime and Java Compatibility in Studio](https://docs.mulesoft.com/studio/change-jdk-config-in-projects#mule-runtime-and-java-compatibility-in-studio)
2. [Select the Java Version for All Your Studio Projects](https://docs.mulesoft.com/studio/change-jdk-config-in-projects#select-the-java-version-for-all-your-studio-projects)
3. [Migrate Your Project to a Different Java Version](https://docs.mulesoft.com/studio/change-jdk-config-in-projects#migrate-your-project-to-a-different-java-version)
4. [Verify Java 17 Tooling](https://docs.mulesoft.com/studio/change-jdk-config-in-projects#verify-java-17-tooling)
5. [Verify Java 17 Module Compatibility](https://docs.mulesoft.com/studio/change-jdk-config-in-projects#verify-java-17-module-compatibility)
6. [Configure FIPS 140-2 in Studio](https://docs.mulesoft.com/studio/change-jdk-config-in-projects#configure-fips-140-2-in-studio)
7. [See Also](https://docs.mulesoft.com/studio/change-jdk-config-in-projects#see-also)

Menu

1. [](https://docs.mulesoft.com/general/)
2. [Studio](https://docs.mulesoft.com/studio/)
3. Selecting a Different JRE to Run the Embedded Mule Runtime Engine

![Image 18](https://docs.mulesoft.com/_/img/icons/arrow-down.svg)![Image 19: Search Docs](https://docs.mulesoft.com/_/img/icons/search.svg)

1. [](https://docs.mulesoft.com/general/)
2. [Studio](https://docs.mulesoft.com/studio/)
3. Selecting a Different JRE to Run the Embedded Mule Runtime Engine

Selecting a Different Java Version to Run the Embedded Mule Runtime
===================================================================

![Image 20](https://docs.mulesoft.com/_/img/icons/dropdown-arrow.svg)

You can select any of your installed JREs as the default Java runtime environment that Studio uses to run your Mule project.

You can select the version of the JDK to use for the project that is compatible with the Mule runtime version the project runs on.

If you change the Java or Mule runtime versions in your project, consider these facts:

* Mule runtime 4.4 and earlier works with Java 8 and 11.

* Mule runtime 4.6 works with Java 8, 11, and 17.

* Standard support for Java 8 and 11 ends in March 2025 for Mule 4.8 Edge and August 2025 for 4.6 LTS, so plan your upgrade path for apps that are running on Java 8 or 11 accordingly.

* Studio 7.21 and later builds and runs projects on Java 17 by default. To use Mule 4.9 and later, upgrade your apps to run on Java 17.

![Image 21: Copy link to clipboard](https://docs.mulesoft.com/_/img/icons/anchor.svg)Mule Runtime and Java Compatibility in Studio
----------------------------------------------------------------------------------------------------------------------------------

This table shows the compatibility between Mule runtime and Java versions in Studio:

Show

![Image 22](https://docs.mulesoft.com/_/img/icons/arrow-down.svg)| Studio Version | Mule Runtime Version | Java 8 | Java 11 | Java 17 |
| --- | --- | --- | --- | --- |
| 7.22 and later | *4.10.x* 4.9.x (LTS) and later *4.8.x* 4.6.x (LTS) | No | No | Yes |
| 7.20 | *4.8.x* 4.6.x (LTS) | Yes | Yes | Yes |
| * 4.4.x | Yes | Yes | No |

See the [Studio release notes](https://docs.mulesoft.com/studio/studio-release-notes) for the latest information about compatibility.

![Image 23: Copy link to clipboard](https://docs.mulesoft.com/_/img/icons/anchor.svg)Select the Java Version for All Your Studio Projects
-----------------------------------------------------------------------------------------------------------------------------------------

1. In Studio, click **Anypoint Studio**, and **Preferences**.

2. Under **Java**, **Installed JREs**, select the JRE version to use.

![Image 24: A table listing installed Java runtime environments with names, locations, and types](https://docs.mulesoft.com/studio/_images/installed-jres.png)  If your installed JRE version doesn’t appear, you must configure it:

    1.   Go to **Add** and select your installed JRE type:

        *   `MacOS X VM` for macOS.

        *   `Standard VM` for macOS, Windows, and Linux.

    2.   Click **Next**.

    3.   In **JRE Home**, click **Directory** and select the folder where you have installed JRE.

 For example, `/Library/Java/JavaVirtualMachines/jdk-11.0.3.jdk/Contents/Home`

    4.   In **JRE Name** type in a descriptive name for the JRE.

 For example, `Java SE 11`.

    5.   Click **Finish**.

![Image 25: Copy link to clipboard](https://docs.mulesoft.com/_/img/icons/anchor.svg)Migrate Your Project to a Different Java Version
-------------------------------------------------------------------------------------------------------------------------------------

Studio 7.17.0 and later are compatible with Java 17. Upgrade modules and apps in your projects to obtain its latest features.

1. Right-click your Studio project.

2. Go to **Build Path**, and click **Configure Build Path**.

3. In the **Libraries** tab, select your **JRE System Library** and click **Edit**.

4. Select the **Alternate JRE** option, and select your desired JRE from the dropdown menu.

![Image 26: Edit Library window displaying the alternate JRE options.](https://docs.mulesoft.com/studio/_images/change-jdk-project.png)  

If you select Java 17 for your project, Studio automatically searches Exchange and suggests [the modules and connectors to upgrade](https://docs.mulesoft.com/studio/update-modules) to make your app compatible with Java 17.

If you find issues, you can [troubleshoot them](https://docs.mulesoft.com/studio/compatibility-issues-runtime-java) and then [deploy your project to the appropriate environment](https://docs.mulesoft.com/studio/deploy-mule-application-task) with Java compatibility checks.

![Image 27: Copy link to clipboard](https://docs.mulesoft.com/_/img/icons/anchor.svg)Verify Java 17 Tooling
-----------------------------------------------------------------------------------------------------------

In Studio 7.19.0 and later, your new Mule projects use JDK 17 by default and the bundled modules in your Mule projects must be Java 17 compatible. If you have issues with the modules that use previous versions of Java:

1. Go to **Settings**>**Anypoint Studio**>**Tooling**.

2. In the **Life cycle** section, select Java 17 as the Java virtual machine for Studio services.

3. Click **Apply and Close**.

The Studio services restart and the tooling instance restarts using Java 17.

Use the [Java 17 module compatibility tool](https://docs.mulesoft.com/studio/change-jdk-config-in-projects#verify-java-17-module-compatibility) to verify the modules in your Mule project are Java 17 compatible.

![Image 28: Copy link to clipboard](https://docs.mulesoft.com/_/img/icons/anchor.svg)Verify Java 17 Module Compatibility
------------------------------------------------------------------------------------------------------------------------

In Studio 7.19.0 and later, you can check if the modules in your Mule project are Java 17 compatible:

1. Right-click the name of your project.

2. Select **Mule**>**Java 17 Module Compatibility**.

Studio analyzes the modules in your Mule project and shows the modules that aren’t Java 17 compatible in the **Problems** tab.
3.   [Update the modules](https://docs.mulesoft.com/studio/update-modules) that aren’t Java 17 compatible.

![Image 29: The problems tab is open, with one warning and three Java module compatibility notifications](https://docs.mulesoft.com/studio/_images/java-17-tooling.png)

![Image 30: Copy link to clipboard](https://docs.mulesoft.com/_/img/icons/anchor.svg)Configure FIPS 140-2 in Studio
-------------------------------------------------------------------------------------------------------------------

Studio supports FIPS 140-2 security model for Java 8, 11, and 17.

### ![Image 31: Copy link to clipboard](https://docs.mulesoft.com/_/img/icons/anchor.svg)Configure FIPS 140-2 in Java 8

1. Download the provider files from the [BouncyCastle![Image 32: Leaving the Site](https://docs.mulesoft.com/_/img/icons/external-link.svg)](https://www.bouncycastle.org/download/bouncy-castle-java-fips/) website.

    *   Provider: bc-fips-1.0.2.4

    *   TLS: bctls-fips-1.0.19.jar

    *   PKIX: bcpkix-fips-1.0.7.jar

2.   Install the required JAR files into your Studio embedded JDK 8. This example shows the command for a default macOS installation. The path to the `…​/jre/lib/ext/` directory can be different depending on your operating system and Studio version.

```bash
cp bc-fips-1.0.2.4.jar bctls-fips-1.0.19.jar bcpkix-fips-1.0.7.jar /Applications/AnypointStudio.app/Contents/Eclipse/plugins/org.mule.tooling.jdk.v8.macosx.x86_64_1.3.4/Contents/Home/jre/lib/ext/
```

bash![Image 33: copy icon](https://docs.mulesoft.com/_/img/icons/copy-default.svg)✓ Copied   The default path on Windows is `C:\AnypointStudio\plugins\org.mule.tooling.jdk.v8.win32.x86_1.3.4\jre\lib\ext`.
3.   Register the security providers in the `java.security` properties file, located in your JDK 8 `…​/lib/security/` folder. Bouncy Castle must be the only provider.

```java
#
# List of providers and their preference orders:
#
security.provider.1=org.bouncycastle.jcajce.provider.BouncyCastleFipsProvider
security.provider.2=org.bouncycastle.jsse.provider.BouncyCastleJsseProvider fips:BCFIPS
# ...
```

java![Image 34: copy icon](https://docs.mulesoft.com/_/img/icons/copy-default.svg)✓ Copied
4.   Save your changes.

1. In Studio, go to your project, right click its folder, and select **Run configuration**.

2. Go to the **Arguments** tab. In **VM arguments**, add:

```text
-Dmule.security.model=fips140-2
-Dorg.bouncycastle.fips.approved_only=true
```

text![Image 35: copy icon](https://docs.mulesoft.com/_/img/icons/copy-default.svg)✓ Copied
7.   Run your application. The startup readout shows FIPS security model enabled.

```text
* Mule Runtime and Integration Platform
* Version: 4.6.21 Build: adffffac
* MuleSoft, Inc.
* For more information go to
* https://www.mulesoft.com/platform/soa/mule-esb-enterprise
*
* Server started: 6/4/18 4:06 PM
* JDK: 1.8.0_172 (mixed mode)
* JDK properties:
  - java.vendor = Oracle Corporation
  - java.vm.name = Java HotSpot(TM) 64-Bit Server VM
  - java.home = /Library/Java/JavaVirtualMachines/jdk1.8.0_172.jdk/Contents/Home/jre
* OS: Mac OS X (10.11, x86_64)
* Host: your-hostname.local (10.250.0.81)
* Security model: fips140-2 (1)
* Mule services:
  - api-gateway-contract-service-1.0.0-mule-service.jar
  - mule-service-http-ee-1.1.1-mule-service.jar
  - mule-service-oauth-1.1.1-mule-service.jar
  - mule-service-scheduler-1.1.4-mule-service.jar
  - mule-service-soap-1.1.2-mule-service.jar
  - mule-service-weave-ee-2.1.2-mule-service.jar
* Mule system properties:
  - mule.security.model = fips140-2
  - mule.base = /Users/your-user/AnypointStudio/studio-workspace/.mule
  - mule.home = /Users/your-user/AnypointStudio/studio-workspace/.mule
```

text![Image 36: copy icon](https://docs.mulesoft.com/_/img/icons/copy-default.svg)✓ Copied Expand content   **1**FIPS 140-2 security model is enabled.

### ![Image 37: Copy link to clipboard](https://docs.mulesoft.com/_/img/icons/anchor.svg)Configure FIPS 140-2 in Java 11 and Later

1. Download the provider files from the [BouncyCastle![Image 38: Leaving the Site](https://docs.mulesoft.com/_/img/icons/external-link.svg)](https://www.bouncycastle.org/download/bouncy-castle-java-fips/) website:

    *   Provider: bc-fips-1.0.2.4

    *   TLS: bctls-fips-1.0.19.jar

    *   PKIX: bcpkix-fips-1.0.7.jar

2.   Copy the downloaded files to the embedded Mule runtime `…​/lib/boot` directory. The path to this directory can vary depending on your Studio and Mule runtime versions.

```bash
cp bc-fips-1.0.2.4.jar bctls-fips-1.0.19.jar bcpkix-fips-1.0.7.jar /Applications/AnypointStudio.app/Contents/Eclipse/plugins/org.mule.tooling.server.4.9.ee_7.21.0.202508051502/mule/lib/boot
```

bash![Image 39: copy icon](https://docs.mulesoft.com/_/img/icons/copy-default.svg)✓ Copied   The default path on Windows is `C:\AnypointStudio\plugins\org.mule.tooling.server.4.9.ee_7.21.0.202508051502\mule\lib\boot`.
3.   Delete the **wrapper.conf** file at `AnypointStudio\plugins\org.mule.tooling.server.4.9.ee_7.21.0.202508051502\mule\conf`.

1. Edit `AnypointStudio\plugins\org.mule.tooling.server.4.9.ee_7.21.0.202508051502\mule\conf\wrapper.conf.template` and uncomment this line by deleting the starting **#** character:

```text
wrapper.java.additional.21=--add-opens=java.base/sun.security.provider=org.bouncycastle.fips.core
```

text![Image 40: copy icon](https://docs.mulesoft.com/_/img/icons/copy-default.svg)✓ Copied
5.   Edit `/Applications/AnypointStudio.app/Contents/Eclipse/plugins/org.mule.tooling.jdk.macosx.aarch64_1.4.1/Contents/Home/conf/security/java.security` to list only the BouncyCastle security providers.

```java
security.provider.1=org.bouncycastle.jcajce.provider.BouncyCastleFipsProvider
security.provider.2=org.bouncycastle.jsse.provider.BouncyCastleJsseProvider fips:BCFIPS
```

java![Image 41: copy icon](https://docs.mulesoft.com/_/img/icons/copy-default.svg)✓ Copied
6.   In Studio, go to your project, right click its folder, and select **Run configuration**.

1. Go to the **Arguments** tab. In **VM arguments**, add:

```text
-Dmule.security.model=fips140-2
-Dorg.bouncycastle.fips.approved_only=true
```

text![Image 42: copy icon](https://docs.mulesoft.com/_/img/icons/copy-default.svg)✓ Copied
8.   Run your application. The startup readout shows FIPS security model enabled.

```text
* Mule Runtime and Integration Platform
* Version: 4.9.8 Build: adffffac
* MuleSoft, Inc.
* For more information go to
* https://www.mulesoft.com/platform/soa/mule-esb-enterprise
*
* Server started: 8/10/21 5:12 PM
* JDK: 11.0.11 (mixed mode)
* JDK properties:
  - java.vendor = AdoptOpenJDK
  - java.vm.name = OpenJDK 64-Bit Server VM
  - java.home = /Library/Java/JavaVirtualMachines/adoptopenjdk-11.jdk/Contents/Home
* OS: Mac OS X (11.5, x86_64)
* Host: your-hostname.local (192.168.1.10)
* Security model: fips140-2 (1)
* Mule services:
  - ...
* Mule system properties:
  - mule.security.model = fips140-2
  - mule.base = /Users/your-user/AnypointStudio/studio-workspace/.mule
  - mule.home = /Users/your-user/AnypointStudio/studio-workspace/.mule
```

text![Image 43: copy icon](https://docs.mulesoft.com/_/img/icons/copy-default.svg)✓ Copied Expand content   **1**FIPS 140-2 security model is enabled.

![Image 44: Copy link to clipboard](https://docs.mulesoft.com/_/img/icons/anchor.svg)See Also
---------------------------------------------------------------------------------------------

* [Java Support](https://docs.mulesoft.com/general/java-support)

* [Troubleshooting Issues with Mule Runtime and Java](https://docs.mulesoft.com/studio/compatibility-issues-runtime-java)

* [FIPS 140-2 Compliance Support](https://docs.mulesoft.com/mule-runtime/latest/fips-140-2-compliance-support)

[Back to top](https://docs.mulesoft.com/studio/change-jdk-config-in-projects#)

Did this article solve your issue?

Let us know so we can improve!

Yes

![Image 45](https://docs.mulesoft.com/_/img/icons/like.svg)

No

![Image 46](https://docs.mulesoft.com/_/img/icons/dislike.svg)

Please check at least 1 checkbox.
Would you like to share any additional feedback? (Optional)

800 / 800

![Image 47](https://docs.mulesoft.com/_/img/icons/success.svg) Your feedback has been successfully submitted. Thank you! [View on GitHub](https://github.com/mulesoft/docs-studio/blob/latest/modules/ROOT/pages/change-jdk-config-in-projects.adoc)

* Products
  * [Anypoint Platform](https://www.mulesoft.com/platform/enterprise-integration)
  * [MuleSoft Composer](https://www.mulesoft.com/platform/composer)
  * [MuleSoft RPA](https://www.mulesoft.com/platform/rpa)
  * [MuleSoft IDP](https://www.mulesoft.com/platform/intelligent-document-processing)
  * [Start a free trial](https://anypoint.mulesoft.com/login/signup?apintent=generic)
  * [Download Studio](https://www.mulesoft.com/lp/dl/studio)

* Solutions
  * [API management](https://www.mulesoft.com/api/management)
  * [Integration](https://www.mulesoft.com/integration)
  * [Automation](https://www.mulesoft.com/integration-solutions/api/business-automation)
  * [Artificial Intelligence](https://www.mulesoft.com/platform/ai)
  * [See all solutions](https://www.mulesoft.com/integration-solutions)

* Services
  * [Training](https://trailheadacademy.salesforce.com/products/mulesoft#f-products=Mulesoft)
  * [Certification](https://trailhead.salesforce.com/en/credentials/administratoroverview/)
  * [MuleSoft Catalyst](https://www.mulesoft.com/support-and-services/consulting)
  * [Business Value Services](https://www.mulesoft.com/support-and-services/business-value-services)

* Support
  * [Help Center](https://help.mulesoft.com/)
  * [Community](https://www.mulesoft.com/community)
  * [Tutorials](https://developer.mulesoft.com/tutorials-and-howtos)
  * [Documentation](https://docs.mulesoft.com/)
  * [Quick start guides](https://www.mulesoft.com/lp/ebook/api/integration-quick-start-guide)
  * [Contact us](https://www.mulesoft.com/contact)

* Resources
  * [Webinars](https://www.mulesoft.com/integration-resources?type%5B0%5D=Webinar)
  * [Demos](https://www.mulesoft.com/integration-resources?type%5B0%5D=Demo)
  * [Videos](https://videos.mulesoft.com/)
  * [Analyst reports](https://www.mulesoft.com/integration-resources?type%5B0%5D=Report)
  * [eBooks](https://www.mulesoft.com/integration-resources?type%5B0%5D=eBook)
  * [Whitepapers](https://www.mulesoft.com/integration-resources?type%5B0%5D=Whitepaper)
  * [Infographics](https://www.mulesoft.com/integration-resources?type%5B0%5D=Infographic)
  * [Articles](https://www.mulesoft.com/resources/articles)
  * [Blog](https://blogs.mulesoft.com/bloghome/)

* Explore more
  * [New release features](https://www.mulesoft.com/platform/new-product-features)
  * [Customer stories](https://www.mulesoft.com/case-studies)
  * [Events](https://www.mulesoft.com/events)
  * [Partners](https://www.mulesoft.com/integration-partner)
  * [Newsroom](https://www.salesforce.com/news/products/mulesoft/)
  * [Newsletter sign-up](https://www.linkedin.com/newsletters/technically-speaking-7140068811264651264/)
  * [Careers](https://careers.salesforce.com/en/jobs/?search=MuleSoft)

[](https://www.mulesoft.com/)

[Legal](https://www.salesforce.com/company/legal/)[Terms of Service](https://www.salesforce.com/company/legal/sfdc-website-terms-of-service/)[Privacy](https://www.salesforce.com/company/privacy/)[Trust](https://trust.salesforce.com/)[Contact](https://www.salesforce.com/company/contact-us/?d=cta-glob-footer-11)[Responsible Disclosure](https://www.salesforce.com/company/legal/disclosure/)Cookies Settings

[Your Privacy Choices](https://www.salesforce.com/form/other/privacy-request/)

© Copyright 2025 Salesforce, Inc. [All rights reserved.](https://www.salesforce.com/company/legal/tmcusageguidelines/) Various trademarks held by their respective owners. Salesforce, Inc. Salesforce Tower, 415 Mission Street, 3rd Floor, San Francisco, CA 94105, United States[Link to MuleSoft Linkedin profile](https://www.linkedin.com/company/mulesoft/)[Link to MuleSoft Twitter profile](https://twitter.com/MuleSoft)[Link to MuleSoft Instagram profile](https://www.instagram.com/mulesoft)[Link to MuleSoft Facebook profile](https://www.facebook.com/MuleSoft/)[Link to MuleSoft Videos platform](https://www.youtube.com/user/mulesoftvids)[Link to MuleSoft Twitch profile](https://www.twitch.tv/mulesoft_community)

![Image 48: Salesforce](https://www.mulesoft.com/oneTrust/consent/fc594183-7384-4f03-8c43-1f81571521b7/01938ba0-2bc1-7129-9a4c-e70d4380975d/logos/ddb906c9-f57b-40fc-85a1-c8bcbc371b0d/6a33a761-886e-4860-8e17-abc0832f7a62/corporate_logo_big.png)

Cookie Consent Manager
----------------------

* ### General Information

* ### Required Cookies

* ### Functional Cookies

* ### Advertising Cookies

#### General Information

We use three kinds of cookies on our websites: required, functional, and advertising. You can choose whether functional and advertising cookies apply. Click on the different cookie categories to find out more about each category and to change the default settings.

[Privacy Statement](https://www.salesforce.com/company/privacy/full_privacy/)

#### Required Cookies

Always Active

Required cookies are necessary for basic website functionality. Some examples include: session cookies needed to transmit the website, authentication cookies, and security cookies.

Cookies Details‎

#### Functional Cookies

* [x] Functional Cookies

Functional cookies enhance functions, performance, and services on the website. Some examples include: cookies used to analyze site traffic, cookies used for market research, and cookies used to display advertising that is not directed to a particular individual.

Cookies Details‎

#### Advertising Cookies

* [x] Advertising Cookies

Advertising cookies track activity across websites in order to understand a viewer’s interests, and direct them specific marketing. Some examples include: cookies used for remarketing, or interest-based advertising.

Cookies Details‎

### Cookie List

Consent Leg.Interest

* [x] checkbox label label

* [x] checkbox label label

* [x] checkbox label label

Clear

* [x] checkbox label label

Apply Cancel

Save Settings

Accept All Cookies

[![Image 49: Powered by Onetrust](https://www.mulesoft.com/oneTrust/consent/fc594183-7384-4f03-8c43-1f81571521b7/01938ba0-2bc1-7129-9a4c-e70d4380975d/logos/static/powered_by_logo.svg)](https://www.onetrust.com/products/cookie-consent/)

![Image 50](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%26800%26600%268%2624%26800%26600%260%26na&eci=3&event=%7B%7D&event_id=bf51adf2-4fb8-4f7c-a4b8-cdff6dec0042&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=f27afe31-f878-4e81-86cc-24a7b3d7dda0&pt=Selecting%20a%20Different%20Java%20Version%20to%20Run%20the%20Embedded%20Mule%20Runtime%20%7C%20MuleSoft%20Documentation&tw_document_href=https%3A%2F%2Fdocs.mulesoft.com%2Fstudio%2Fchange-jdk-config-in-projects&tw_iframe_status=0&tw_pid_src=1&twpid=tw.1773222512498.770601118563381140&txn_id=nuq81&type=javascript&version=2.3.44)![Image 51](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%26800%26600%268%2624%26800%26600%260%26na&eci=3&event=%7B%7D&event_id=bf51adf2-4fb8-4f7c-a4b8-cdff6dec0042&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=f27afe31-f878-4e81-86cc-24a7b3d7dda0&pt=Selecting%20a%20Different%20Java%20Version%20to%20Run%20the%20Embedded%20Mule%20Runtime%20%7C%20MuleSoft%20Documentation&tw_document_href=https%3A%2F%2Fdocs.mulesoft.com%2Fstudio%2Fchange-jdk-config-in-projects&tw_iframe_status=0&tw_pid_src=1&twpid=tw.1773222512498.770601118563381140&txn_id=nuq81&type=javascript&version=2.3.44)![Image 52](https://id.rlcdn.com/464526.gif)
