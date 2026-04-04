# Source: https://docs.mulesoft.com/dataweave/latest/dataweave-troubleshoot

Title: Troubleshooting a Failing DataWeave Script

URL Source: https://docs.mulesoft.com/dataweave/latest/dataweave-troubleshoot

Markdown Content:
Troubleshooting a Failing DataWeave Script | MuleSoft Documentation
===============

Skip to left navigation Skip to main content Skip to page navigation

[](https://www.mulesoft.com/)

*   Products For IT Teams[Anypoint Platform World’s #1 integration and API platform](https://www.mulesoft.com/platform/enterprise-integration)Integration[Code Builder](https://www.mulesoft.com/platform/api/anypoint-code-builder)[Exchange](https://www.mulesoft.com/platform/exchange)[Connectors](https://www.mulesoft.com/platform/cloud-connectors)[MCP Support](https://www.mulesoft.com/platform/ai/model-context-protocol)API management[Flex Gateway](https://www.mulesoft.com/platform/api/flex-api-gateway)[API Governance](https://www.mulesoft.com/platform/api/governance-anypoint)[Monitoring](https://www.mulesoft.com/platform/api/monitoring-anypoint)[API Manager](https://www.mulesoft.com/platform/api/manager)[See all](https://www.mulesoft.com/platform/anypoint-platform-features)  Try for free[Sign up to Anypoint Platform](https://anypoint.mulesoft.com/login/#/signup?apintent=generic)[Download Anypoint Code Builder, Studio, Mule](https://www.mulesoft.com/lp/dl/anypoint-mule-studio)  For Business Teams[MuleSoft for Flow: Integration Point to point integration with clicks, not code](https://www.mulesoft.com/platform/flow-integration)[MuleSoft IDP Extract unstructured data from documents with AI](https://www.mulesoft.com/platform/intelligent-document-processing)[MuleSoft RPA Automate tasks with bots](https://www.mulesoft.com/platform/rpa)[Dataloader.io Securely import and export unlimited Salesforce data](https://dataloader.io/)For AI[MuleSoft for Agentforce Power Agentforce with APIs and actions](https://www.mulesoft.com/platform/agentforce)[Einstein for MuleSoft Build integrations and automations faster using natural language](https://www.mulesoft.com/ai/einstein-for-mulesoft)     [![Image 2: A graphic of MuleSoft MCP Support](https://mulesoftd8.www.msit.io/sites/default/files/cmm_files/hero_image--3-.png) MuleSoft MCP Support is now available Learn how to transform your APIs to agent ready assets in minutes. Learn more](https://www.mulesoft.com/platform/ai/model-context-protocol)   
*   Solutions Featured Solutions[API Management Manage and secure any API, built and deployed anywhere](https://www.mulesoft.com/api/management)[Integration Connect any system, data, or API to integrate at scale](https://www.mulesoft.com/integration)[Automation Automate processes and tasks for every team](https://www.mulesoft.com/automation)[MuleSoft AI Connect data and automate workflows with AI](https://www.mulesoft.com/platform/ai)Featured Integration[Salesforce Power connected experiences with Salesforce integration](https://www.mulesoft.com/integration/salesforce)[SAP Unlock SAP and connect your IT landscape](https://www.mulesoft.com/integration/sap)[AWS Get the most out of AWS with integration and APIs](https://www.mulesoft.com/integration-solutions/soa/aws)[Small business Unlock AI-powered success for your small business](https://www.mulesoft.com/small-business)   By Industry[Financial services](https://www.mulesoft.com/solutions/financial-services)[Government](https://www.mulesoft.com/integration-solutions/soa/government)[Healthcare and life sciences](https://www.mulesoft.com/integration-solutions/soa/healthcare)[Higher education](https://www.mulesoft.com/integration-solutions/soa/higher-education)[Insurance](https://www.mulesoft.com/integration-solutions/soa/insurance)[Manufacturing](https://www.mulesoft.com/integration-solutions/api/manufacturing-edi-erp)[Media and telecom](https://www.mulesoft.com/integration-solutions/soa/digital-media)[Retail](https://www.mulesoft.com/integration-solutions/saas/retail)[Consumer goods](https://www.mulesoft.com/integration-solutions/soa/consumer-goods)By Initiative[B2B EDI integration](https://www.mulesoft.com/integration/b2b-edi-platform)[DevOps](https://www.mulesoft.com/integration-solutions/api/devops)[eCommerce](https://www.mulesoft.com/integration-solutions/api/ecommerce)[Event-Driven Architecture](https://www.mulesoft.com/event-driven-architecture)[iPaaS](https://www.mulesoft.com/integration-solutions/api/ipaas)[Legacy system modernization](https://www.mulesoft.com/legacy-system-modernization/legacy-system-modernization-solution)[Microservices](https://www.mulesoft.com/api/microservices)[Move to the cloud](https://www.mulesoft.com/integration/move-to-the-cloud)[Omnichannel](https://www.mulesoft.com/integration-solutions/api/omnichannel)[SaaS integration](https://www.mulesoft.com/integration-solutions/api/saas)[Single view of customer](https://www.mulesoft.com/integration-solutions/api/360-degree-view-customer)[See all solutions](https://www.mulesoft.com/integration-solutions)      [![Image 3: An image of the ebook cover: Create Connected Experiences with MuleSoft + AI](https://www.mulesoft.com/sites/default/files/cmm_files/image-mulesoft-solutions-create-connected-experiences-with-ai.png) Create connected experiences with AI Learn the critical steps to developing an AI strategy and foundation. Read more](https://www.mulesoft.com/lp/ebook/api/salesforce-integration-customer-360)   
*   Services Training[Courses](https://trailheadacademy.salesforce.com/products/mulesoft#f-products=Mulesoft)[Certifications](https://trailheadacademy.salesforce.com/products/mulesoft#f-products=MuleSoft%E2%80%9D%20target=%E2%80%9D_blank%E2%80%9D%20role=)[Training credits](https://trailhead.salesforce.com/help?article=Salesforce-Learning-Credits-FAQ-and-Redemption-Process)Customer success[MuleSoft Catalyst](https://www.mulesoft.com/support-and-services/consulting)[Business Value Services](https://www.mulesoft.com/support-and-services/mobilize-consulting-solutions)Support[Help Center](https://help.mulesoft.com/s/)[Community Forums](https://trailhead.salesforce.com/trailblazer-community/neighborhoods/mulesoft)      [![Image 4: An image of the ebook cover: 3 Predictions for the Future of Connected AI Agents](https://www.mulesoft.com/sites/default/files/cmm_files/image-mulesoft-services-future-of-connected-ai-agents.png) Future of connected AI agents Discover how to prepare for the future of autonomous AI agents. Read more](https://www.mulesoft.com/lp/whitepaper/3-predictions-future-of-connected-ai-agents)   
*   Resources Featured Resources[Customer stories](https://www.mulesoft.com/case-studies)[Newsroom](https://www.salesforce.com/news/products/mulesoft/)[Newsletter sign-up](https://www.linkedin.com/newsletters/technically-speaking-7140068811264651264/) Explore[Webinars](https://www.mulesoft.com/webinars)[Demos](https://www.mulesoft.com/integration-resources?type%5B0%5D=demo)[Videos](https://videos.mulesoft.com/)[Analyst reports](https://www.mulesoft.com/reports)[eBooks](https://www.mulesoft.com/ebook)[Whitepapers](https://www.mulesoft.com/whitepaper/integration-use-cases)[Infographics](https://www.mulesoft.com/infographics)[Articles](https://www.mulesoft.com/resources/articles)[Blog](https://blogs.mulesoft.com/bloghome/)[API University](https://www.mulesoft.com/api-university/what-are-apis-and-how-do-they-work) [See all resources](https://www.mulesoft.com/integration-resources)  Events[MuleSoft Connect:AI](https://mulesoft.com/connect-ai)[MuleSoft at Dreamforce](https://www.mulesoft.com/dreamforce)[MuleSoft at TrailblazerDX](https://www.salesforce.com/trailblazerdx)[Community Meetups](https://meetups.mulesoft.com/)[All events](https://www.mulesoft.com/events)     [![Image 5: A graphic showing the keynote presentation at Connect:AI](https://mulesoftd8.www.msit.io/sites/default/files/cmm_files/keynote-opt02_11zon.jpg) Go from composability to agent actionability Relive the best moments from Connect:AI with our on-demand sessions. Start watching](https://www.mulesoft.com/connect-ai)   

*   Developers [Getting started](https://developer.mulesoft.com/)[Community](https://www.mulesoft.com/community)[Training](https://trailheadacademy.salesforce.com/products/mulesoft#f-products=Mulesoft)[Tutorials](https://developer.mulesoft.com/tutorials-and-howtos)[Documentation](https://docs.mulesoft.com/general/)   
*   Partners For customers[Find a partner](https://www.mulesoft.com/integration-partner/finder)For partners[Become a partner](https://www.mulesoft.com/integration-partner/become-partner)   

[Contact Us](https://www.mulesoft.com/contact)1-800-596-4880

*    [English (Full site)](https://docs.mulesoft.com/)[日本語](https://docs.mulesoft.com/jp)      
*   Login [Anypoint Platform](https://anypoint.mulesoft.com/login/#/signin?apintent=generic)[Composer](https://composer.mulesoft.com/login/sign-in)[Help Center](https://help.mulesoft.com/s/login/)      
*   [Free trial](https://anypoint.mulesoft.com/login/#/signup?apintent=generic)

[](https://www.mulesoft.com/)

*   Products For IT Teams[Anypoint Platform World’s #1 integration and API platform](https://www.mulesoft.com/platform/enterprise-integration)Integration[Code Builder](https://www.mulesoft.com/platform/api/anypoint-code-builder)[Exchange](https://www.mulesoft.com/platform/exchange)[Connectors](https://www.mulesoft.com/platform/cloud-connectors)[MCP Support](https://www.mulesoft.com/platform/ai/model-context-protocol)API management[Flex Gateway](https://www.mulesoft.com/platform/api/flex-api-gateway)[API Governance](https://www.mulesoft.com/platform/api/governance-anypoint)[Monitoring](https://www.mulesoft.com/platform/api/monitoring-anypoint)[API Manager](https://www.mulesoft.com/platform/api/manager)[See all](https://www.mulesoft.com/platform/anypoint-platform-features)  Try for free[Sign up to Anypoint Platform](https://anypoint.mulesoft.com/login/#/signup?apintent=generic)[Download Anypoint Code Builder, Studio, Mule](https://www.mulesoft.com/lp/dl/anypoint-mule-studio)  For Business Teams[MuleSoft for Flow: Integration Point to point integration with clicks, not code](https://www.mulesoft.com/platform/flow-integration)[MuleSoft IDP Extract unstructured data from documents with AI](https://www.mulesoft.com/platform/intelligent-document-processing)[MuleSoft RPA Automate tasks with bots](https://www.mulesoft.com/platform/rpa)[Dataloader.io Securely import and export unlimited Salesforce data](https://dataloader.io/)For AI[MuleSoft for Agentforce Power Agentforce with APIs and actions](https://www.mulesoft.com/platform/agentforce)[Einstein for MuleSoft Build integrations and automations faster using natural language](https://www.mulesoft.com/ai/einstein-for-mulesoft)     [![Image 6: A graphic of MuleSoft MCP Support](https://mulesoftd8.www.msit.io/sites/default/files/cmm_files/hero_image--3-.png) MuleSoft MCP Support is now available Learn how to transform your APIs to agent ready assets in minutes. Learn more](https://www.mulesoft.com/platform/ai/model-context-protocol)   
*   Solutions Featured Solutions[API Management Manage and secure any API, built and deployed anywhere](https://www.mulesoft.com/api/management)[Integration Connect any system, data, or API to integrate at scale](https://www.mulesoft.com/integration)[Automation Automate processes and tasks for every team](https://www.mulesoft.com/automation)[MuleSoft AI Connect data and automate workflows with AI](https://www.mulesoft.com/platform/ai)Featured Integration[Salesforce Power connected experiences with Salesforce integration](https://www.mulesoft.com/integration/salesforce)[SAP Unlock SAP and connect your IT landscape](https://www.mulesoft.com/integration/sap)[AWS Get the most out of AWS with integration and APIs](https://www.mulesoft.com/integration-solutions/soa/aws)[Small business Unlock AI-powered success for your small business](https://www.mulesoft.com/small-business)   By Industry[Financial services](https://www.mulesoft.com/solutions/financial-services)[Government](https://www.mulesoft.com/integration-solutions/soa/government)[Healthcare and life sciences](https://www.mulesoft.com/integration-solutions/soa/healthcare)[Higher education](https://www.mulesoft.com/integration-solutions/soa/higher-education)[Insurance](https://www.mulesoft.com/integration-solutions/soa/insurance)[Manufacturing](https://www.mulesoft.com/integration-solutions/api/manufacturing-edi-erp)[Media and telecom](https://www.mulesoft.com/integration-solutions/soa/digital-media)[Retail](https://www.mulesoft.com/integration-solutions/saas/retail)[Consumer goods](https://www.mulesoft.com/integration-solutions/soa/consumer-goods)By Initiative[B2B EDI integration](https://www.mulesoft.com/integration/b2b-edi-platform)[DevOps](https://www.mulesoft.com/integration-solutions/api/devops)[eCommerce](https://www.mulesoft.com/integration-solutions/api/ecommerce)[Event-Driven Architecture](https://www.mulesoft.com/event-driven-architecture)[iPaaS](https://www.mulesoft.com/integration-solutions/api/ipaas)[Legacy system modernization](https://www.mulesoft.com/legacy-system-modernization/legacy-system-modernization-solution)[Microservices](https://www.mulesoft.com/api/microservices)[Move to the cloud](https://www.mulesoft.com/integration/move-to-the-cloud)[Omnichannel](https://www.mulesoft.com/integration-solutions/api/omnichannel)[SaaS integration](https://www.mulesoft.com/integration-solutions/api/saas)[Single view of customer](https://www.mulesoft.com/integration-solutions/api/360-degree-view-customer)[See all solutions](https://www.mulesoft.com/integration-solutions)      [![Image 7: An image of the ebook cover: Create Connected Experiences with MuleSoft + AI](https://www.mulesoft.com/sites/default/files/cmm_files/image-mulesoft-solutions-create-connected-experiences-with-ai.png) Create connected experiences with AI Learn the critical steps to developing an AI strategy and foundation. Read more](https://www.mulesoft.com/lp/ebook/api/salesforce-integration-customer-360)   
*   Services Training[Courses](https://trailheadacademy.salesforce.com/products/mulesoft#f-products=Mulesoft)[Certifications](https://trailheadacademy.salesforce.com/products/mulesoft#f-products=MuleSoft%E2%80%9D%20target=%E2%80%9D_blank%E2%80%9D%20role=)[Training credits](https://trailhead.salesforce.com/help?article=Salesforce-Learning-Credits-FAQ-and-Redemption-Process)Customer success[MuleSoft Catalyst](https://www.mulesoft.com/support-and-services/consulting)[Business Value Services](https://www.mulesoft.com/support-and-services/mobilize-consulting-solutions)Support[Help Center](https://help.mulesoft.com/s/)[Community Forums](https://trailhead.salesforce.com/trailblazer-community/neighborhoods/mulesoft)      [![Image 8: An image of the ebook cover: 3 Predictions for the Future of Connected AI Agents](https://www.mulesoft.com/sites/default/files/cmm_files/image-mulesoft-services-future-of-connected-ai-agents.png) Future of connected AI agents Discover how to prepare for the future of autonomous AI agents. Read more](https://www.mulesoft.com/lp/whitepaper/3-predictions-future-of-connected-ai-agents)   
*   Resources Featured Resources[Customer stories](https://www.mulesoft.com/case-studies)[Newsroom](https://www.salesforce.com/news/products/mulesoft/)[Newsletter sign-up](https://www.linkedin.com/newsletters/technically-speaking-7140068811264651264/) Explore[Webinars](https://www.mulesoft.com/webinars)[Demos](https://www.mulesoft.com/integration-resources?type%5B0%5D=demo)[Videos](https://videos.mulesoft.com/)[Analyst reports](https://www.mulesoft.com/reports)[eBooks](https://www.mulesoft.com/ebook)[Whitepapers](https://www.mulesoft.com/whitepaper/integration-use-cases)[Infographics](https://www.mulesoft.com/infographics)[Articles](https://www.mulesoft.com/resources/articles)[Blog](https://blogs.mulesoft.com/bloghome/)[API University](https://www.mulesoft.com/api-university/what-are-apis-and-how-do-they-work) [See all resources](https://www.mulesoft.com/integration-resources)  Events[MuleSoft Connect:AI](https://mulesoft.com/connect-ai)[MuleSoft at Dreamforce](https://www.mulesoft.com/dreamforce)[MuleSoft at TrailblazerDX](https://www.salesforce.com/trailblazerdx)[Community Meetups](https://meetups.mulesoft.com/)[All events](https://www.mulesoft.com/events)     [![Image 9: A graphic showing the keynote presentation at Connect:AI](https://mulesoftd8.www.msit.io/sites/default/files/cmm_files/keynote-opt02_11zon.jpg) Go from composability to agent actionability Relive the best moments from Connect:AI with our on-demand sessions. Start watching](https://www.mulesoft.com/connect-ai)   

*   Developers [Getting started](https://developer.mulesoft.com/)[Community](https://www.mulesoft.com/community)[Training](https://trailheadacademy.salesforce.com/products/mulesoft#f-products=Mulesoft)[Tutorials](https://developer.mulesoft.com/tutorials-and-howtos)[Documentation](https://docs.mulesoft.com/general/)   
*   Partners For customers[Find a partner](https://www.mulesoft.com/integration-partner/finder)For partners[Become a partner](https://www.mulesoft.com/integration-partner/become-partner)   

*   Language [English (Full site)](https://docs.mulesoft.com/)[日本語](https://docs.mulesoft.com/jp)      
*   Contact By phone[1-800-596-4880](tel:1-800-596-4880) Online[Contact Us](https://www.mulesoft.com/contact)       

*   Login [Anypoint Platform](https://anypoint.mulesoft.com/login/#/signin?apintent=generic)[Composer](https://composer.mulesoft.com/login/sign-in)[Help Center](https://help.mulesoft.com/s/login/)      

[Free trial](https://anypoint.mulesoft.com/login/#/signup?apintent=generic)

[Link to MuleSoft Twitter profile](https://twitter.com/MuleSoft)[Link to MuleSoft Linkedin profile](https://www.linkedin.com/company/mulesoft)[Link to MuleSoft Facebook page](https://www.facebook.com/MuleSoft)[Link to MuleSoft Instagram profile](https://www.instagram.com/mulesoft/)[Link to MuleSoft Videos platform](https://videos.mulesoft.com/)[Link to MuleSoft Twitch profile](https://www.twitch.tv/mulesoft_community)
© Copyright 2025 Salesforce, Inc. [All rights reserved](https://www.salesforce.com/company/legal/intellectual/).

Search Docs

![Image 10](https://docs.mulesoft.com/_/img/icons/arrow-down.svg)

*   [Home](https://docs.mulesoft.com/general/) 
*   Release Notes 
*   [Archived Documentation![Image 11: Leaving the Site](https://docs.mulesoft.com/_/img/icons/external-link.svg)](https://archive.docs.mulesoft.com/)![Image 12: Archived Documentation information](https://docs.mulesoft.com/_/img/icons/tooltip-gray.svg)  

### Getting Started

*   [MuleSoft AI](https://docs.mulesoft.com/general/learning-map-mulesoft-ai)
*   [Agent Fabric](https://docs.mulesoft.com/general/learning-map-agent-fabric)
    *   [Agent Fabric Release Notes](https://docs.mulesoft.com/general/agent-fabric-release-notes)
    *   [Get Started with Agent Networks](https://docs.mulesoft.com/general/agent-networks-get-started)

*   [API Management](https://docs.mulesoft.com/general/learning-map-api-management)
*   [Usage Reports](https://docs.mulesoft.com/general/usage-reports)
    *   [Release Notes](https://docs.mulesoft.com/general/usage-reports-release-notes)
    *   [Usage and Pricing Metrics Reference](https://docs.mulesoft.com/general/usage-metrics)
    *   [Pricing](https://docs.mulesoft.com/general/pricing)
    *   [Troubleshooting Usage Reports](https://docs.mulesoft.com/general/troubleshooting-usage-reports)

*   [Java Support](https://docs.mulesoft.com/general/java-support)
    *   [Upgrading Java for Custom Connectors (Partners)](https://docs.mulesoft.com/general/partner-connector-upgrade)
    *   [Upgrading Java for Custom Connectors (Customers)](https://docs.mulesoft.com/general/customer-connector-upgrade)
    *   [Upgrading Java for Policies and API Proxies](https://docs.mulesoft.com/general/upgrade-policies-proxies)

*   [Browser Support](https://docs.mulesoft.com/general/browser-support)
*   [Glossary](https://docs.mulesoft.com/general/glossary)
*   [Build an API from Start to Finish](https://docs.mulesoft.com/general/api-led-overview)
    *   [Step 1. Prerequisites](https://docs.mulesoft.com/general/api-led-prerequisites)
    *   [Step 2. Design an API Specification](https://docs.mulesoft.com/general/api-led-design)
    *   [Step 3. Develop the API](https://docs.mulesoft.com/general/api-led-develop)
    *   [Step 4. Add Validation and Error Handling](https://docs.mulesoft.com/general/api-led-test)
    *   [Step 5. Deploy the API to CloudHub](https://docs.mulesoft.com/general/api-led-deploy)
    *   [Step 6. Operate the API](https://docs.mulesoft.com/general/api-led-operate)

*   [Contribute to MuleSoft Documentation](https://docs.mulesoft.com/general/contribute)

### Hosting

*   Hosting Options 
*   CloudHub 2.0 
*   CloudHub 
*   Runtime Fabric 3.0  Current version 3.0  Previous versions 2.11 2.10 2.9 2.8 2.7 2.6 2.5     
*   Anypoint Platform Private Cloud Edition 4.1  Current version 4.1  Previous versions 4.0 3.2     
*   Government Cloud 
*   EU Control Plane 
*   Hyperforce 
*   Hybrid Standalone 

### Docs by Product

*   Accelerators 
*   Access Management 
*   Agent Visualizer 
*   Anypoint CLI 4.x  Current version 4.x  Previous versions 3.x     
*   Anypoint Code Builder 
*   API Community Manager 
*   API Experience Hub 
*   API Functional Monitoring 
*   API Governance 
*   API Manager 2.x

   
*   APIkit Mule 4

   
*   Composer 
*   Composer for Salesforce 
*   Connector Builder 
*   Connectors 
*   DataGraph 
*   DataWeave 2.11 (Mule 4.11)  Current version 2.11 (Mule 4.11)  Previous versions 2.10 (Mule 4.10) 2.9 (Mule 4.9) 2.8 (Mule 4.8) 2.7 (Mule 4.7) 2.6 (Mule 4.6) 2.5 (Mule 4.5) 2.4 (Mule 4.4) 2.3 (Mule 4.3)     
    *   [Overview](https://docs.mulesoft.com/dataweave/latest/)
    *   [Release Notes](https://docs.mulesoft.com/dataweave/latest/dataweave-release-notes)
    *   [DataWeave Quickstart](https://docs.mulesoft.com/dataweave/latest/dataweave-quickstart)
    *   [Language Guide](https://docs.mulesoft.com/dataweave/latest/dataweave-language-guide)
        *   [Scripts](https://docs.mulesoft.com/dataweave/latest/dataweave-language-introduction)
        *   [Selectors](https://docs.mulesoft.com/dataweave/latest/dataweave-selectors)
            *   [Selecting Types](https://docs.mulesoft.com/dataweave/latest/dataweave-selecting-types)

        *   [Supported Data Formats](https://docs.mulesoft.com/dataweave/latest/dataweave-formats)
            *   [Avro Format](https://docs.mulesoft.com/dataweave/latest/dataweave-formats-avro)
            *   [Binary Format](https://docs.mulesoft.com/dataweave/latest/dataweave-formats-binary)
            *   [COBOL Copybook Format](https://docs.mulesoft.com/dataweave/latest/dataweave-formats-copybook)
            *   [CSV Format](https://docs.mulesoft.com/dataweave/latest/dataweave-formats-csv)
            *   [DataWeave Format (dw)](https://docs.mulesoft.com/dataweave/latest/dataweave-formats-dw)
            *   [Event Stream Format](https://docs.mulesoft.com/dataweave/latest/dataweave-formats-eventstream)
            *   [Excel Format (XLSX)](https://docs.mulesoft.com/dataweave/latest/dataweave-formats-excel)
            *   [Fixed Width Format](https://docs.mulesoft.com/dataweave/latest/dataweave-formats-fixedwidth)
            *   [Flat File Format](https://docs.mulesoft.com/dataweave/latest/dataweave-formats-flatfile)
            *   [Java Format](https://docs.mulesoft.com/dataweave/latest/dataweave-formats-java)
            *   [JSON Format](https://docs.mulesoft.com/dataweave/latest/dataweave-formats-json)
            *   [Multipart Format](https://docs.mulesoft.com/dataweave/latest/dataweave-formats-multipart)
            *   [New Line Delimited (ndjson) Format](https://docs.mulesoft.com/dataweave/latest/dataweave-formats-ndjson)
            *   [Protobuf Format](https://docs.mulesoft.com/dataweave/latest/dataweave-formats-protobuf)
            *   [Text Java Properties Format](https://docs.mulesoft.com/dataweave/latest/dataweave-formats-properties)
            *   [Text Plain Format](https://docs.mulesoft.com/dataweave/latest/dataweave-formats-text)
            *   [URL Encoded Format](https://docs.mulesoft.com/dataweave/latest/dataweave-formats-urlencoded)
            *   [XML Format](https://docs.mulesoft.com/dataweave/latest/dataweave-formats-xml)
            *   [YAML Format](https://docs.mulesoft.com/dataweave/latest/dataweave-formats-yaml)

        *   [Streaming in DataWeave](https://docs.mulesoft.com/dataweave/latest/dataweave-streaming)
        *   [Indexed Readers in DataWeave](https://docs.mulesoft.com/dataweave/latest/dataweave-indexed-readers)
        *   [Flatfile Schemas](https://docs.mulesoft.com/dataweave/latest/dataweave-flat-file-schemas)
        *   [Type System](https://docs.mulesoft.com/dataweave/latest/dataweave-type-system)
            *   [Reusing Types from DataWeave Modules](https://docs.mulesoft.com/dataweave/latest/dataweave-type-reuse-modules)
            *   [Reusing Types from a JSON Schema](https://docs.mulesoft.com/dataweave/latest/dataweave-type-reuse-json-schema)
            *   [Reusing an XML Schema](https://docs.mulesoft.com/dataweave/latest/dataweave-type-reuse-xml-schema)
            *   [Reusing Types from Java Classes](https://docs.mulesoft.com/dataweave/latest/dataweave-type-reuse-java-classes)
            *   [Reusing Types from an Avro Schema](https://docs.mulesoft.com/dataweave/latest/dataweave-type-reuse-avro-schema)

        *   [Value Constructs for Types](https://docs.mulesoft.com/dataweave/latest/dataweave-types)
        *   [Type Coercion with DataWeave](https://docs.mulesoft.com/dataweave/latest/dataweave-types-coercion)
        *   [Variables](https://docs.mulesoft.com/dataweave/latest/dataweave-variables)
        *   [Predefined Variables](https://docs.mulesoft.com/dataweave/latest/dataweave-variables-context)
        *   [Flow Control in DataWeave](https://docs.mulesoft.com/dataweave/latest/dataweave-flow-control)
        *   [Pattern Matching in DataWeave](https://docs.mulesoft.com/dataweave/latest/dataweave-pattern-matching)
        *   [External Functions Available to DataWeave](https://docs.mulesoft.com/dataweave/latest/dataweave-runtime-functions)
        *   [Troubleshooting](https://docs.mulesoft.com/dataweave/latest/dataweave-troubleshoot)
        *   [Define Functions](https://docs.mulesoft.com/dataweave/latest/dataweave-functions)
        *   [Create Custom Modules and Mappings](https://docs.mulesoft.com/dataweave/latest/dataweave-create-module)
        *   [Working with Functions and Lambdas in DataWeave](https://docs.mulesoft.com/dataweave/latest/dataweave-functions-lambdas)
        *   [Memory Management](https://docs.mulesoft.com/dataweave/latest/dataweave-memory-management)
        *   [Logging Configuration](https://docs.mulesoft.com/dataweave/latest/dataweave-logging-configuration)
        *   [Versioning Behavior in DataWeave](https://docs.mulesoft.com/dataweave/latest/dataweave-versioning-behavior)

    *   [DataWeave Examples](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook)
        *   [Extract Data](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-extract-data)
        *   [Select XML Elements](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-select-xml-elements)
        *   [Set Default Values](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-defaults)
        *   [Set Reader and Writer Configuration Properties](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-set-reader-writer-props)
        *   [Perform a Basic Transformation](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-perform-basic-transformation)
        *   [Map Data](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-map)
        *   [Map and Flatten an Array](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-map-and-flatten)
        *   [Map an Object](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-map-an-object)
        *   [Map the Objects within an Array](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-map-object-elements-as-an-array)
        *   [Map Based On an External Definition](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-map-based-on-an-external-definition)
        *   [Rename Keys](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-rename-keys)
        *   [Output a Field When Present](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-output-a-field-when-present)
        *   [Change Format According to Type](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-format-according-to-type)
        *   [Regroup Fields](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-regroup-fields)
        *   [Zip Arrays Together](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-zip-arrays-together)
        *   [Pick Top Elements](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-pick-top-elements)
        *   [Change the Value of a Field](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-change-value-of-a-field)
        *   [Exclude Fields from the Output](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-exclude-field)
        *   [Use Constant Directives](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-use-constant-directives)
        *   [Define a Custom Addition Function](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-define-a-custom-addition-function)
        *   [Define a Function that Flattens Data in a List](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-define-function-to-flatten-list)
        *   [Flatten Elements of Arrays](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-flatten-arrays)
        *   [Use Regular Expressions](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-use-regex)
        *   [Output self-closing XML tags](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-output-self-closing-xml-tags)
        *   [Insert an Attribute into an XML Tag](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-insert-attribute)
        *   [Remove Certain XML Attributes](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-remove-certain-xml-attributes)
        *   [Pass XML Attributes](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-pass-xml-attributes)
        *   [Include XML Namespaces](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-include-xml-namespaces)
        *   [Remove Objects Containing Specified Key-Value Pairs](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-remove-objects)
        *   [Reference Multiple Inputs](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-reference-multiple-inputs)
        *   [Merge Fields from Separate Objects](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-merge-multiple-payloads)
        *   [Parse Dates](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-parse-dates)
        *   [Add and Subtracting Dates](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-add-and-subtract-time)
        *   [Change a Time Zone](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-change-time-zone)
        *   [Format Dates and Times](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-format-dates)
        *   [Work with Multipart Data](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-work-with-multipart-data)
        *   [Conditionally Reduce a List Via a Function](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-conditional-list-reduction-via-function)
        *   [Pass Functions as Arguments](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-pass-functions-as-arguments)
        *   [Change a Script’s MIME Type Output (Mule)](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-change-script-output-mime)
        *   [Look Up Data in an Excel (XLSX) File (Mule)](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-xlsx-lookup)
        *   [Look Up Data in CSV File (Mule)](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-csv-lookup)
        *   [Decode and Encode Base64 (Mule)](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-decode-encode)
        *   [Call Java Methods (Mule)](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-java-methods)
        *   [Read and Write a Flat File (Mule)](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-flat-file-read-and-write)
        *   [Use a Reader Property through a Connector (Mule)](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-reader-prop-connector)
        *   [Use Dynamic Writer Properties (Mule)](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-writer-prop-mule)
        *   [Extract Key/Value Pairs with Pluck Function (Mule)](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-pluck)

    *   [DataWeave Reference](https://docs.mulesoft.com/dataweave/latest/dw-functions)
        *   [DataWeave Operators](https://docs.mulesoft.com/dataweave/latest/dw-operators)
        *   [System Properties](https://docs.mulesoft.com/dataweave/latest/dataweave-system-properties)
        *   [Precedence Rules](https://docs.mulesoft.com/dataweave/latest/dataweave-flow-control-precedence)
        *   [dw::Core](https://docs.mulesoft.com/dataweave/latest/dw-core)
            *   [++](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-plusplus)
            *   [--](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-minusminus)
            *   [abs](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-abs)
            *   [avg](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-avg)
            *   [ceil](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-ceil)
            *   [contains](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-contains)
            *   [daysBetween](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-daysbetween)
            *   [distinctBy](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-distinctby)
            *   [endsWith](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-endswith)
            *   [entriesOf](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-entriesof)
            *   [evaluateCompatibilityFlag](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-evaluatecompatibilityflag)
            *   [filter](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-filter)
            *   [filterObject](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-filterobject)
            *   [find](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-find)
            *   [flatMap](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-flatmap)
            *   [flatten](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-flatten)
            *   [floor](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-floor)
            *   [groupBy](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-groupby)
            *   [indexOf](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-indexof)
            *   [isBlank](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-isblank)
            *   [isDecimal](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-isdecimal)
            *   [isEmpty](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-isempty)
            *   [isEven](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-iseven)
            *   [isInteger](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-isinteger)
            *   [isLeapYear](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-isleapyear)
            *   [isOdd](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-isodd)
            *   [joinBy](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-joinby)
            *   [keysOf](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-keysof)
            *   [lastIndexOf](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-lastindexof)
            *   [log](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-log)
            *   [logDebug](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-logdebug)
            *   [logError](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-logerror)
            *   [logInfo](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-loginfo)
            *   [logWarn](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-logwarn)
            *   [logWith](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-logwith)
            *   [lower](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-lower)
            *   [map](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-map)
            *   [mapObject](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-mapobject)
            *   [match](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-match)
            *   [matches](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-matches)
            *   [max](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-max)
            *   [maxBy](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-maxby)
            *   [min](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-min)
            *   [minBy](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-minby)
            *   [mod](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-mod)
            *   [namesOf](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-namesof)
            *   [now](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-now)
            *   [onNull](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-onnull)
            *   [orderBy](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-orderby)
            *   [pluck](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-pluck)
            *   [pow](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-pow)
            *   [random](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-random)
            *   [randomInt](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-randomint)
            *   [read](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-read)
            *   [readUrl](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-readurl)
            *   [reduce](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-reduce)
            *   [replace](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-replace)
            *   [round](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-round)
            *   [scan](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-scan)
            *   [sizeOf](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-sizeof)
            *   [splitBy](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-splitby)
            *   [sqrt](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-sqrt)
            *   [startsWith](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-startswith)
            *   [sum](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-sum)
            *   [then](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-then)
            *   [to](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-to)
            *   [trim](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-trim)
            *   [typeOf](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-typeof)
            *   [unzip](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-unzip)
            *   [upper](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-upper)
            *   [uuid](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-uuid)
            *   [valuesOf](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-valuesof)
            *   [with](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-with)
            *   [write](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-write)
            *   [xsiType](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-xsitype)
            *   [zip](https://docs.mulesoft.com/dataweave/latest/dw-core-functions-zip)
            *   [Core Types](https://docs.mulesoft.com/dataweave/latest/dw-core-types)
            *   [Core Namespaces](https://docs.mulesoft.com/dataweave/latest/dw-core-namespaces)
            *   [Core Annotations](https://docs.mulesoft.com/dataweave/latest/dw-core-annotations)

        *   [dw::core::Arrays](https://docs.mulesoft.com/dataweave/latest/dw-arrays)
            *   [countBy](https://docs.mulesoft.com/dataweave/latest/dw-arrays-functions-countby)
            *   [divideBy](https://docs.mulesoft.com/dataweave/latest/dw-arrays-functions-divideby)
            *   [drop](https://docs.mulesoft.com/dataweave/latest/dw-arrays-functions-drop)
            *   [dropWhile](https://docs.mulesoft.com/dataweave/latest/dw-arrays-functions-dropwhile)
            *   [every](https://docs.mulesoft.com/dataweave/latest/dw-arrays-functions-every)
            *   [firstWith](https://docs.mulesoft.com/dataweave/latest/dw-arrays-functions-firstwith)
            *   [indexOf](https://docs.mulesoft.com/dataweave/latest/dw-arrays-functions-indexof)
            *   [indexWhere](https://docs.mulesoft.com/dataweave/latest/dw-arrays-functions-indexwhere)
            *   [join](https://docs.mulesoft.com/dataweave/latest/dw-arrays-functions-join)
            *   [leftJoin](https://docs.mulesoft.com/dataweave/latest/dw-arrays-functions-leftjoin)
            *   [outerJoin](https://docs.mulesoft.com/dataweave/latest/dw-arrays-functions-outerjoin)
            *   [partition](https://docs.mulesoft.com/dataweave/latest/dw-arrays-functions-partition)
            *   [slice](https://docs.mulesoft.com/dataweave/latest/dw-arrays-functions-slice)
            *   [some](https://docs.mulesoft.com/dataweave/latest/dw-arrays-functions-some)
            *   [splitAt](https://docs.mulesoft.com/dataweave/latest/dw-arrays-functions-splitat)
            *   [splitWhere](https://docs.mulesoft.com/dataweave/latest/dw-arrays-functions-splitwhere)
            *   [sumBy](https://docs.mulesoft.com/dataweave/latest/dw-arrays-functions-sumby)
            *   [take](https://docs.mulesoft.com/dataweave/latest/dw-arrays-functions-take)
            *   [takeWhile](https://docs.mulesoft.com/dataweave/latest/dw-arrays-functions-takewhile)

        *   [dw::core::Binaries](https://docs.mulesoft.com/dataweave/latest/dw-binaries)
            *   [concatWith](https://docs.mulesoft.com/dataweave/latest/dw-binaries-functions-concatwith)
            *   [fromBase64](https://docs.mulesoft.com/dataweave/latest/dw-binaries-functions-frombase64)
            *   [fromHex](https://docs.mulesoft.com/dataweave/latest/dw-binaries-functions-fromhex)
            *   [readLinesWith](https://docs.mulesoft.com/dataweave/latest/dw-binaries-functions-readlineswith)
            *   [toBase64](https://docs.mulesoft.com/dataweave/latest/dw-binaries-functions-tobase64)
            *   [toHex](https://docs.mulesoft.com/dataweave/latest/dw-binaries-functions-tohex)
            *   [writeLinesWith](https://docs.mulesoft.com/dataweave/latest/dw-binaries-functions-writelineswith)

        *   [dw::core::Dates](https://docs.mulesoft.com/dataweave/latest/dw-dates)
            *   [atBeginningOfDay](https://docs.mulesoft.com/dataweave/latest/dw-dates-functions-atbeginningofday)
            *   [atBeginningOfHour](https://docs.mulesoft.com/dataweave/latest/dw-dates-functions-atbeginningofhour)
            *   [atBeginningOfMonth](https://docs.mulesoft.com/dataweave/latest/dw-dates-functions-atbeginningofmonth)
            *   [atBeginningOfWeek](https://docs.mulesoft.com/dataweave/latest/dw-dates-functions-atbeginningofweek)
            *   [atBeginningOfYear](https://docs.mulesoft.com/dataweave/latest/dw-dates-functions-atbeginningofyear)
            *   [date](https://docs.mulesoft.com/dataweave/latest/dw-dates-functions-date)
            *   [dateTime](https://docs.mulesoft.com/dataweave/latest/dw-dates-functions-datetime)
            *   [localDateTime](https://docs.mulesoft.com/dataweave/latest/dw-dates-functions-localdatetime)
            *   [localTime](https://docs.mulesoft.com/dataweave/latest/dw-dates-functions-localtime)
            *   [time](https://docs.mulesoft.com/dataweave/latest/dw-dates-functions-time)
            *   [today](https://docs.mulesoft.com/dataweave/latest/dw-dates-functions-today)
            *   [tomorrow](https://docs.mulesoft.com/dataweave/latest/dw-dates-functions-tomorrow)
            *   [yesterday](https://docs.mulesoft.com/dataweave/latest/dw-dates-functions-yesterday)
            *   [Dates Types](https://docs.mulesoft.com/dataweave/latest/dw-dates-types)

        *   [dw::core::Numbers](https://docs.mulesoft.com/dataweave/latest/dw-numbers)
            *   [fromBinary](https://docs.mulesoft.com/dataweave/latest/dw-numbers-functions-frombinary)
            *   [fromHex](https://docs.mulesoft.com/dataweave/latest/dw-numbers-functions-fromhex)
            *   [fromRadixNumber](https://docs.mulesoft.com/dataweave/latest/dw-numbers-functions-fromradixnumber)
            *   [toBinary](https://docs.mulesoft.com/dataweave/latest/dw-numbers-functions-tobinary)
            *   [toHex](https://docs.mulesoft.com/dataweave/latest/dw-numbers-functions-tohex)
            *   [toRadixNumber](https://docs.mulesoft.com/dataweave/latest/dw-numbers-functions-toradixnumber)

        *   [dw::core::Objects](https://docs.mulesoft.com/dataweave/latest/dw-objects)
            *   [divideBy](https://docs.mulesoft.com/dataweave/latest/dw-objects-functions-divideby)
            *   [entrySet](https://docs.mulesoft.com/dataweave/latest/dw-objects-functions-entryset)
            *   [everyEntry](https://docs.mulesoft.com/dataweave/latest/dw-objects-functions-everyentry)
            *   [keySet](https://docs.mulesoft.com/dataweave/latest/dw-objects-functions-keyset)
            *   [mergeWith](https://docs.mulesoft.com/dataweave/latest/dw-objects-functions-mergewith)
            *   [nameSet](https://docs.mulesoft.com/dataweave/latest/dw-objects-functions-nameset)
            *   [someEntry](https://docs.mulesoft.com/dataweave/latest/dw-objects-functions-someentry)
            *   [takeWhile](https://docs.mulesoft.com/dataweave/latest/dw-objects-functions-takewhile)
            *   [valueSet](https://docs.mulesoft.com/dataweave/latest/dw-objects-functions-valueset)

        *   [dw::core::Periods](https://docs.mulesoft.com/dataweave/latest/dw-periods)
            *   [between](https://docs.mulesoft.com/dataweave/latest/dw-periods-functions-between)
            *   [days](https://docs.mulesoft.com/dataweave/latest/dw-periods-functions-days)
            *   [duration](https://docs.mulesoft.com/dataweave/latest/dw-periods-functions-duration)
            *   [hours](https://docs.mulesoft.com/dataweave/latest/dw-periods-functions-hours)
            *   [minutes](https://docs.mulesoft.com/dataweave/latest/dw-periods-functions-minutes)
            *   [months](https://docs.mulesoft.com/dataweave/latest/dw-periods-functions-months)
            *   [period](https://docs.mulesoft.com/dataweave/latest/dw-periods-functions-period)
            *   [seconds](https://docs.mulesoft.com/dataweave/latest/dw-periods-functions-seconds)
            *   [years](https://docs.mulesoft.com/dataweave/latest/dw-periods-functions-years)

        *   [dw::core::Strings](https://docs.mulesoft.com/dataweave/latest/dw-strings)
            *   [appendIfMissing](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-appendifmissing)
            *   [camelize](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-camelize)
            *   [capitalize](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-capitalize)
            *   [charCode](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-charcode)
            *   [charCodeAt](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-charcodeat)
            *   [collapse](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-collapse)
            *   [countCharactersBy](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-countcharactersby)
            *   [countMatches](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-countmatches)
            *   [dasherize](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-dasherize)
            *   [everyCharacter](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-everycharacter)
            *   [first](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-first)
            *   [fromCharCode](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-fromcharcode)
            *   [hammingDistance](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-hammingdistance)
            *   [isAlpha](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-isalpha)
            *   [isAlphanumeric](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-isalphanumeric)
            *   [isLowerCase](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-islowercase)
            *   [isNumeric](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-isnumeric)
            *   [isUpperCase](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-isuppercase)
            *   [isWhitespace](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-iswhitespace)
            *   [last](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-last)
            *   [leftPad](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-leftpad)
            *   [levenshteinDistance](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-levenshteindistance)
            *   [lines](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-lines)
            *   [mapString](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-mapstring)
            *   [ordinalize](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-ordinalize)
            *   [pluralize](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-pluralize)
            *   [prependIfMissing](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-prependifmissing)
            *   [remove](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-remove)
            *   [repeat](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-repeat)
            *   [replaceAll](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-replaceall)
            *   [reverse](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-reverse)
            *   [rightPad](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-rightpad)
            *   [singularize](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-singularize)
            *   [someCharacter](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-somecharacter)
            *   [substring](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-substring)
            *   [substringAfter](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-substringafter)
            *   [substringAfterLast](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-substringafterlast)
            *   [substringBefore](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-substringbefore)
            *   [substringBeforeLast](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-substringbeforelast)
            *   [substringBy](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-substringby)
            *   [substringEvery](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-substringevery)
            *   [underscore](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-underscore)
            *   [unwrap](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-unwrap)
            *   [withMaxSize](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-withmaxsize)
            *   [words](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-words)
            *   [wrapIfMissing](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-wrapifmissing)
            *   [wrapWith](https://docs.mulesoft.com/dataweave/latest/dw-strings-functions-wrapwith)

        *   [dw::core::Types](https://docs.mulesoft.com/dataweave/latest/dw-types)
            *   [arrayItem](https://docs.mulesoft.com/dataweave/latest/dw-types-functions-arrayitem)
            *   [baseTypeOf](https://docs.mulesoft.com/dataweave/latest/dw-types-functions-basetypeof)
            *   [functionParamTypes](https://docs.mulesoft.com/dataweave/latest/dw-types-functions-functionparamtypes)
            *   [functionReturnType](https://docs.mulesoft.com/dataweave/latest/dw-types-functions-functionreturntype)
            *   [intersectionItems](https://docs.mulesoft.com/dataweave/latest/dw-types-functions-intersectionitems)
            *   [isAnyType](https://docs.mulesoft.com/dataweave/latest/dw-types-functions-isanytype)
            *   [isArrayType](https://docs.mulesoft.com/dataweave/latest/dw-types-functions-isarraytype)
            *   [isBinaryType](https://docs.mulesoft.com/dataweave/latest/dw-types-functions-isbinarytype)
            *   [isBooleanType](https://docs.mulesoft.com/dataweave/latest/dw-types-functions-isbooleantype)
            *   [isDateTimeType](https://docs.mulesoft.com/dataweave/latest/dw-types-functions-isdatetimetype)
            *   [isDateType](https://docs.mulesoft.com/dataweave/latest/dw-types-functions-isdatetype)
            *   [isFunctionType](https://docs.mulesoft.com/dataweave/latest/dw-types-functions-isfunctiontype)
            *   [isIntersectionType](https://docs.mulesoft.com/dataweave/latest/dw-types-functions-isintersectiontype)
            *   [isKeyType](https://docs.mulesoft.com/dataweave/latest/dw-types-functions-iskeytype)
            *   [isLiteralType](https://docs.mulesoft.com/dataweave/latest/dw-types-functions-isliteraltype)
            *   [isLocalDateTimeType](https://docs.mulesoft.com/dataweave/latest/dw-types-functions-islocaldatetimetype)
            *   [isLocalTimeType](https://docs.mulesoft.com/dataweave/latest/dw-types-functions-islocaltimetype)
            *   [isNamespaceType](https://docs.mulesoft.com/dataweave/latest/dw-types-functions-isnamespacetype)
            *   [isNothingType](https://docs.mulesoft.com/dataweave/latest/dw-types-functions-isnothingtype)
            *   [isNullType](https://docs.mulesoft.com/dataweave/latest/dw-types-functions-isnulltype)
            *   [isNumberType](https://docs.mulesoft.com/dataweave/latest/dw-types-functions-isnumbertype)
            *   [isObjectType](https://docs.mulesoft.com/dataweave/latest/dw-types-functions-isobjecttype)
            *   [isPeriodType](https://docs.mulesoft.com/dataweave/latest/dw-types-functions-isperiodtype)
            *   [isRangeType](https://docs.mulesoft.com/dataweave/latest/dw-types-functions-israngetype)
            *   [isReferenceType](https://docs.mulesoft.com/dataweave/latest/dw-types-functions-isreferencetype)
            *   [isRegexType](https://docs.mulesoft.com/dataweave/latest/dw-types-functions-isregextype)
            *   [isStringType](https://docs.mulesoft.com/dataweave/latest/dw-types-functions-isstringtype)
            *   [isTimeType](https://docs.mulesoft.com/dataweave/latest/dw-types-functions-istimetype)
            *   [isTimeZoneType](https://docs.mulesoft.com/dataweave/latest/dw-types-functions-istimezonetype)
            *   [isTypeType](https://docs.mulesoft.com/dataweave/latest/dw-types-functions-istypetype)
            *   [isUnionType](https://docs.mulesoft.com/dataweave/latest/dw-types-functions-isuniontype)
            *   [isUriType](https://docs.mulesoft.com/dataweave/latest/dw-types-functions-isuritype)
            *   [literalValueOf](https://docs.mulesoft.com/dataweave/latest/dw-types-functions-literalvalueof)
            *   [metadataOf](https://docs.mulesoft.com/dataweave/latest/dw-types-functions-metadataof)
            *   [nameOf](https://docs.mulesoft.com/dataweave/latest/dw-types-functions-nameof)
            *   [objectFields](https://docs.mulesoft.com/dataweave/latest/dw-types-functions-objectfields)
            *   [unionItems](https://docs.mulesoft.com/dataweave/latest/dw-types-functions-unionitems)
            *   [Types Types](https://docs.mulesoft.com/dataweave/latest/dw-types-types)

        *   [dw::core::URL](https://docs.mulesoft.com/dataweave/latest/dw-url)
            *   [compose](https://docs.mulesoft.com/dataweave/latest/dw-url-functions-compose)
            *   [decodeURI](https://docs.mulesoft.com/dataweave/latest/dw-url-functions-decodeuri)
            *   [decodeURIComponent](https://docs.mulesoft.com/dataweave/latest/dw-url-functions-decodeuricomponent)
            *   [encodeURI](https://docs.mulesoft.com/dataweave/latest/dw-url-functions-encodeuri)
            *   [encodeURIComponent](https://docs.mulesoft.com/dataweave/latest/dw-url-functions-encodeuricomponent)
            *   [parseURI](https://docs.mulesoft.com/dataweave/latest/dw-url-functions-parseuri)
            *   [URL Types](https://docs.mulesoft.com/dataweave/latest/dw-url-types)

        *   [dw::Crypto](https://docs.mulesoft.com/dataweave/latest/dw-crypto)
            *   [HMACBinary](https://docs.mulesoft.com/dataweave/latest/dw-crypto-functions-hmacbinary)
            *   [HMACWith](https://docs.mulesoft.com/dataweave/latest/dw-crypto-functions-hmacwith)
            *   [MD5](https://docs.mulesoft.com/dataweave/latest/dw-crypto-functions-md5)
            *   [SHA1](https://docs.mulesoft.com/dataweave/latest/dw-crypto-functions-sha1)
            *   [hashWith](https://docs.mulesoft.com/dataweave/latest/dw-crypto-functions-hashwith)

        *   [dw::extension::DataFormat](https://docs.mulesoft.com/dataweave/latest/dw-dataformat)
            *   [DataFormat Types](https://docs.mulesoft.com/dataweave/latest/dw-dataformat-types)
            *   [DataFormat Annotations](https://docs.mulesoft.com/dataweave/latest/dw-dataformat-annotations)

        *   [dw::module::Mime](https://docs.mulesoft.com/dataweave/latest/dw-mime)
            *   [fromString](https://docs.mulesoft.com/dataweave/latest/dw-mime-functions-fromstring)
            *   [isHandledBy](https://docs.mulesoft.com/dataweave/latest/dw-mime-functions-ishandledby)
            *   [toString](https://docs.mulesoft.com/dataweave/latest/dw-mime-functions-tostring)
            *   [Mime Types](https://docs.mulesoft.com/dataweave/latest/dw-mime-types)

        *   [dw::module::Multipart](https://docs.mulesoft.com/dataweave/latest/dw-multipart)
            *   [field](https://docs.mulesoft.com/dataweave/latest/dw-multipart-functions-field)
            *   [file](https://docs.mulesoft.com/dataweave/latest/dw-multipart-functions-file)
            *   [form](https://docs.mulesoft.com/dataweave/latest/dw-multipart-functions-form)
            *   [generateBoundary](https://docs.mulesoft.com/dataweave/latest/dw-multipart-functions-generateboundary)
            *   [Multipart Types](https://docs.mulesoft.com/dataweave/latest/dw-multipart-types)

        *   [dw::Mule](https://docs.mulesoft.com/dataweave/latest/dw-mule)
            *   [causedBy](https://docs.mulesoft.com/dataweave/latest/dw-mule-functions-causedby)
            *   [lookup](https://docs.mulesoft.com/dataweave/latest/dw-mule-functions-lookup)
            *   [p](https://docs.mulesoft.com/dataweave/latest/dw-mule-functions-p)
            *   [Mule Types](https://docs.mulesoft.com/dataweave/latest/dw-mule-types)

        *   [dw::Runtime](https://docs.mulesoft.com/dataweave/latest/dw-runtime)
            *   [dataFormatsDescriptor](https://docs.mulesoft.com/dataweave/latest/dw-runtime-functions-dataformatsdescriptor)
            *   [eval](https://docs.mulesoft.com/dataweave/latest/dw-runtime-functions-eval)
            *   [evalUrl](https://docs.mulesoft.com/dataweave/latest/dw-runtime-functions-evalurl)
            *   [fail](https://docs.mulesoft.com/dataweave/latest/dw-runtime-functions-fail)
            *   [failIf](https://docs.mulesoft.com/dataweave/latest/dw-runtime-functions-failif)
            *   [findDataFormatDescriptorByMime](https://docs.mulesoft.com/dataweave/latest/dw-runtime-functions-finddataformatdescriptorbymime)
            *   [location](https://docs.mulesoft.com/dataweave/latest/dw-runtime-functions-location)
            *   [locationString](https://docs.mulesoft.com/dataweave/latest/dw-runtime-functions-locationstring)
            *   [orElse](https://docs.mulesoft.com/dataweave/latest/dw-runtime-functions-orelse)
            *   [orElseTry](https://docs.mulesoft.com/dataweave/latest/dw-runtime-functions-orelsetry)
            *   [prop](https://docs.mulesoft.com/dataweave/latest/dw-runtime-functions-prop)
            *   [props](https://docs.mulesoft.com/dataweave/latest/dw-runtime-functions-props)
            *   [run](https://docs.mulesoft.com/dataweave/latest/dw-runtime-functions-run)
            *   [runUrl](https://docs.mulesoft.com/dataweave/latest/dw-runtime-functions-runurl)
            *   [try](https://docs.mulesoft.com/dataweave/latest/dw-runtime-functions-try)
            *   [version](https://docs.mulesoft.com/dataweave/latest/dw-runtime-functions-version)
            *   [wait](https://docs.mulesoft.com/dataweave/latest/dw-runtime-functions-wait)
            *   [Runtime Types](https://docs.mulesoft.com/dataweave/latest/dw-runtime-types)

        *   [dw::System](https://docs.mulesoft.com/dataweave/latest/dw-system)
            *   [envVar](https://docs.mulesoft.com/dataweave/latest/dw-system-functions-envvar)
            *   [envVars](https://docs.mulesoft.com/dataweave/latest/dw-system-functions-envvars)

        *   [dw::util::Coercions](https://docs.mulesoft.com/dataweave/latest/dw-coercions)
            *   [toArray](https://docs.mulesoft.com/dataweave/latest/dw-coercions-functions-toarray)
            *   [toBinary](https://docs.mulesoft.com/dataweave/latest/dw-coercions-functions-tobinary)
            *   [toBoolean](https://docs.mulesoft.com/dataweave/latest/dw-coercions-functions-toboolean)
            *   [toDate](https://docs.mulesoft.com/dataweave/latest/dw-coercions-functions-todate)
            *   [toDateOrNull](https://docs.mulesoft.com/dataweave/latest/dw-coercions-functions-todateornull)
            *   [toDateTime](https://docs.mulesoft.com/dataweave/latest/dw-coercions-functions-todatetime)
            *   [toDateTimeOrNull](https://docs.mulesoft.com/dataweave/latest/dw-coercions-functions-todatetimeornull)
            *   [toLocalDateTime](https://docs.mulesoft.com/dataweave/latest/dw-coercions-functions-tolocaldatetime)
            *   [toLocalDateTimeOrNull](https://docs.mulesoft.com/dataweave/latest/dw-coercions-functions-tolocaldatetimeornull)
            *   [toLocalTime](https://docs.mulesoft.com/dataweave/latest/dw-coercions-functions-tolocaltime)
            *   [toLocalTimeOrNull](https://docs.mulesoft.com/dataweave/latest/dw-coercions-functions-tolocaltimeornull)
            *   [toNumber](https://docs.mulesoft.com/dataweave/latest/dw-coercions-functions-tonumber)
            *   [toNumberOrNull](https://docs.mulesoft.com/dataweave/latest/dw-coercions-functions-tonumberornull)
            *   [toPeriod](https://docs.mulesoft.com/dataweave/latest/dw-coercions-functions-toperiod)
            *   [toRegex](https://docs.mulesoft.com/dataweave/latest/dw-coercions-functions-toregex)
            *   [toString](https://docs.mulesoft.com/dataweave/latest/dw-coercions-functions-tostring)
            *   [toTime](https://docs.mulesoft.com/dataweave/latest/dw-coercions-functions-totime)
            *   [toTimeOrNull](https://docs.mulesoft.com/dataweave/latest/dw-coercions-functions-totimeornull)
            *   [toTimeZone](https://docs.mulesoft.com/dataweave/latest/dw-coercions-functions-totimezone)
            *   [toUri](https://docs.mulesoft.com/dataweave/latest/dw-coercions-functions-touri)
            *   [Coercions Types](https://docs.mulesoft.com/dataweave/latest/dw-coercions-types)

        *   [dw::util::Diff](https://docs.mulesoft.com/dataweave/latest/dw-diff)
            *   [diff](https://docs.mulesoft.com/dataweave/latest/dw-diff-functions-diff)
            *   [Diff Types](https://docs.mulesoft.com/dataweave/latest/dw-diff-types)

        *   [dw::util::Math](https://docs.mulesoft.com/dataweave/latest/dw-math)
            *   [acos](https://docs.mulesoft.com/dataweave/latest/dw-math-functions-acos)
            *   [asin](https://docs.mulesoft.com/dataweave/latest/dw-math-functions-asin)
            *   [atan](https://docs.mulesoft.com/dataweave/latest/dw-math-functions-atan)
            *   [cos](https://docs.mulesoft.com/dataweave/latest/dw-math-functions-cos)
            *   [decimalAdd](https://docs.mulesoft.com/dataweave/latest/dw-math-functions-decimaladd)
            *   [decimalDivide](https://docs.mulesoft.com/dataweave/latest/dw-math-functions-decimaldivide)
            *   [decimalMultiply](https://docs.mulesoft.com/dataweave/latest/dw-math-functions-decimalmultiply)
            *   [decimalPow](https://docs.mulesoft.com/dataweave/latest/dw-math-functions-decimalpow)
            *   [decimalRound](https://docs.mulesoft.com/dataweave/latest/dw-math-functions-decimalround)
            *   [decimalSqrt](https://docs.mulesoft.com/dataweave/latest/dw-math-functions-decimalsqrt)
            *   [decimalSubtract](https://docs.mulesoft.com/dataweave/latest/dw-math-functions-decimalsubtract)
            *   [log10](https://docs.mulesoft.com/dataweave/latest/dw-math-functions-log10)
            *   [logn](https://docs.mulesoft.com/dataweave/latest/dw-math-functions-logn)
            *   [sin](https://docs.mulesoft.com/dataweave/latest/dw-math-functions-sin)
            *   [tan](https://docs.mulesoft.com/dataweave/latest/dw-math-functions-tan)
            *   [toDegrees](https://docs.mulesoft.com/dataweave/latest/dw-math-functions-todegrees)
            *   [toRadians](https://docs.mulesoft.com/dataweave/latest/dw-math-functions-toradians)
            *   [Math Variables](https://docs.mulesoft.com/dataweave/latest/dw-math-variables)
            *   [Math Types](https://docs.mulesoft.com/dataweave/latest/dw-math-types)

        *   [dw::util::Timer](https://docs.mulesoft.com/dataweave/latest/dw-timer)
            *   [currentMilliseconds](https://docs.mulesoft.com/dataweave/latest/dw-timer-functions-currentmilliseconds)
            *   [duration](https://docs.mulesoft.com/dataweave/latest/dw-timer-functions-duration)
            *   [time](https://docs.mulesoft.com/dataweave/latest/dw-timer-functions-time)
            *   [toMilliseconds](https://docs.mulesoft.com/dataweave/latest/dw-timer-functions-tomilliseconds)
            *   [Timer Types](https://docs.mulesoft.com/dataweave/latest/dw-timer-types)

        *   [dw::util::Tree](https://docs.mulesoft.com/dataweave/latest/dw-tree)
            *   [asExpressionString](https://docs.mulesoft.com/dataweave/latest/dw-tree-functions-asexpressionstring)
            *   [filterArrayLeafs](https://docs.mulesoft.com/dataweave/latest/dw-tree-functions-filterarrayleafs)
            *   [filterObjectLeafs](https://docs.mulesoft.com/dataweave/latest/dw-tree-functions-filterobjectleafs)
            *   [filterTree](https://docs.mulesoft.com/dataweave/latest/dw-tree-functions-filtertree)
            *   [isArrayType](https://docs.mulesoft.com/dataweave/latest/dw-tree-functions-isarraytype)
            *   [isAttributeType](https://docs.mulesoft.com/dataweave/latest/dw-tree-functions-isattributetype)
            *   [isObjectType](https://docs.mulesoft.com/dataweave/latest/dw-tree-functions-isobjecttype)
            *   [mapLeafValues](https://docs.mulesoft.com/dataweave/latest/dw-tree-functions-mapleafvalues)
            *   [nodeExists](https://docs.mulesoft.com/dataweave/latest/dw-tree-functions-nodeexists)
            *   [Tree Variables](https://docs.mulesoft.com/dataweave/latest/dw-tree-variables)
            *   [Tree Types](https://docs.mulesoft.com/dataweave/latest/dw-tree-types)

        *   [dw::util::Values](https://docs.mulesoft.com/dataweave/latest/dw-values)
            *   [attr](https://docs.mulesoft.com/dataweave/latest/dw-values-functions-attr)
            *   [field](https://docs.mulesoft.com/dataweave/latest/dw-values-functions-field)
            *   [index](https://docs.mulesoft.com/dataweave/latest/dw-values-functions-index)
            *   [mask](https://docs.mulesoft.com/dataweave/latest/dw-values-functions-mask)
            *   [update](https://docs.mulesoft.com/dataweave/latest/dw-values-functions-update)
            *   [Values Types](https://docs.mulesoft.com/dataweave/latest/dw-values-types)

        *   [dw::xml::Dtd](https://docs.mulesoft.com/dataweave/latest/dw-dtd)
            *   [docTypeAsString](https://docs.mulesoft.com/dataweave/latest/dw-dtd-functions-doctypeasstring)
            *   [Dtd Types](https://docs.mulesoft.com/dataweave/latest/dw-dtd-types)

    *   [DataWeave Extension](https://docs.mulesoft.com/dataweave/latest/dataweave-extension)
        *   [Installing and Using the DataWeave Extension](https://docs.mulesoft.com/dataweave/latest/dataweave-extension-plugin)
        *   [Testing DataWeave Libraries and Modules](https://docs.mulesoft.com/dataweave/latest/dataweave-testing-framework)
            *   [dw::test:Asserts](https://docs.mulesoft.com/dataweave/latest/dw-test-asserts)

        *   [Packaging and Deploying DataWeave Libraries](https://docs.mulesoft.com/dataweave/latest/dataweave-maven-plugin)

*   Design Center 
*   Exchange 
*   Gateway 
*   IDP 
*   Monitoring 
*   MQ 
*   Mule Runtime 4.11  Current version 4.11  Previous versions 4.10 4.9 4.8 4.7 4.6 4.5 4.4 4.3     
*   Mule SDK 1.11

   
*   MuleSoft MCP Server 
*   MUnit 3.7  Current version 3.7  Previous versions 3.6 2.3     
*   Object Store 
*   Partner Manager 2.x

   
*   RPA 
*   Runtime Manager 
*   Security 
*   Studio 
*   Visualizer 

Skip to main content

[View on GitHub](https://github.com/mulesoft/docs-dataweave/blob/v2.11/modules/ROOT/pages/dataweave-troubleshoot.adoc)
On this page:
=============

1.   [Dump Input Context and the Script into a Folder](https://docs.mulesoft.com/dataweave/latest/dataweave-troubleshoot#dump-input-context-and-the-script-into-a-folder)
2.   [DataWeave Exceptions](https://docs.mulesoft.com/dataweave/latest/dataweave-troubleshoot#dataweave-exceptions)
3.   [DataWeave Warnings](https://docs.mulesoft.com/dataweave/latest/dataweave-troubleshoot#dataweave-warnings)
4.   [Low Performance Issues](https://docs.mulesoft.com/dataweave/latest/dataweave-troubleshoot#low-performance-issues)

Menu
1.   [](https://docs.mulesoft.com/general/)
2.   [DataWeave (2.11)](https://docs.mulesoft.com/dataweave/latest/)
3.   [Language Guide](https://docs.mulesoft.com/dataweave/latest/dataweave-language-guide)
4.   Troubleshooting

![Image 13](https://docs.mulesoft.com/_/img/icons/arrow-down.svg)![Image 14: Search Docs](https://docs.mulesoft.com/_/img/icons/search.svg)

1.   [](https://docs.mulesoft.com/general/)
2.   [DataWeave (2.11)](https://docs.mulesoft.com/dataweave/latest/)
3.   [Language Guide](https://docs.mulesoft.com/dataweave/latest/dataweave-language-guide)
4.   Troubleshooting

Troubleshooting a Failing DataWeave Script
==========================================

![Image 15](https://docs.mulesoft.com/_/img/icons/dropdown-arrow.svg)

When you troubleshoot a failing script, one challenge to reproducing an error is having the same inputs the script had when it executed, especially in production environments where inputs can change unexpectedly. Therefore, it’s important to capture the inputs going into a script debugging or using loggers. Often, the failures occur because the input coming from another component upstream is not valid. You can find here a listing of the most common DataWeave errors and how to overcome them.

![Image 16: Copy link to clipboard](https://docs.mulesoft.com/_/img/icons/anchor.svg)Dump Input Context and the Script into a Folder
------------------------------------------------------------------------------------------------------------------------------------

In Mule 4.2.1, DataWeave introduced an experimental feature that enables you to dump the input context and the failing script into a folder so that you can track the failing script along with the data that makes the script fail. This tool is particularly useful for checking that received input data is valid because incorrect scripts often fail when an upstream component generates invalid data.

To use this feature:

1.   Set the following system property to enable the dump feature:

`-M-Dcom.mulesoft.dw.dump_files=true` 
2.   [Optional] Specify the path in which to generate the dump files:

`-M-Dcom.mulesoft.dw.dump_folder=<path_to_folder>` The default directory is set in the `java.io.tmpdir` property. 

![Image 17: Copy link to clipboard](https://docs.mulesoft.com/_/img/icons/anchor.svg)DataWeave Exceptions
---------------------------------------------------------------------------------------------------------

The following are some common DataWeave exceptions that you can find in your dump file, along with some details to troubleshoot these errors.

### ![Image 18: Copy link to clipboard](https://docs.mulesoft.com/_/img/icons/anchor.svg)Incorrect Arguments

When a function is called with the incorrect kind of argument, it throws the exception, `org.mule.weave.v2.exception.UnsupportedTypeCoercionException`. Causes of this exception include:

*   [Function Does Not Accept Null Argument](https://docs.mulesoft.com/dataweave/latest/dataweave-troubleshoot#null_arg_not_accepted)

*   [MIME Type Is Not Set](https://docs.mulesoft.com/dataweave/latest/dataweave-troubleshoot#mimetype_unset)

#### ![Image 19: Copy link to clipboard](https://docs.mulesoft.com/_/img/icons/anchor.svg)Function Does Not Accept Null Argument

The most common cause of this exception occurs when one of the arguments is `Null` and the function does not accept `Null` as an argument. This issue results in an error message similar to the following:

```weave
You called the function '++' with these arguments:
  1: Null (null)
  2: String (" A text")

But it expects one of these combinations:
  (Array, Array)
  (Date, Time)
  (Date, LocalTime)
  (Date, TimeZone)
  (LocalDateTime, TimeZone)
  (LocalTime, Date)
  (LocalTime, TimeZone)
  (Object, Object)
  (String, String)
  (Time, Date)
  (TimeZone, LocalDateTime)
  (TimeZone, Date)
  (TimeZone, LocalTime)

1| payload.message ++ " A text"
   ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
Trace:
  at ++ (line: 1, column: 1)
  at main (line: 1, column: 17)
```

weave![Image 20: copy icon](https://docs.mulesoft.com/_/img/icons/copy-default.svg)✓ Copied

Expand content

One way to resolve this issue uses the `default` operator. For example, using `payload.message default "" ++ " A text"` appends empty text when the message is null.

#### ![Image 21: Copy link to clipboard](https://docs.mulesoft.com/_/img/icons/anchor.svg)MIME Type Is Not Set

When the MIME type is not set, you receive an error message similar to the following:

```weave
You called the function 'Value Selector' with these arguments:

  1: String ("{ \"message\": 123}")
  2: Name ("message")

But it expects one of these combinations:
  (Array, Name)
  (Array, String)
  (Date, Name)
  (DateTime, Name)
  (LocalDateTime, Name)
  (LocalTime, Name)
  (Object, Name)
  (Object, String)
  (Period, Name)
  (Time, Name)

1| payload.message
   ^^^^^^^^^^^^^^^
Trace:
  at main (line: 1, column: 1)
```

weave![Image 22: copy icon](https://docs.mulesoft.com/_/img/icons/copy-default.svg)✓ Copied

Expand content

When no MIME type is set on the payload, the MIME type defaults to `application/java`, and the content is handled as a `String` instead of a JSON object.

### ![Image 23: Copy link to clipboard](https://docs.mulesoft.com/_/img/icons/anchor.svg)Reader Properties Not Working In a Mule Application

In a Mule application, the `input` directive to a DataWeave script does not work. Unlike Mule runtime, a standalone DataWeave runtime, such as the one in the [DataWeave Playground+![Image 24: Leaving the Site](https://docs.mulesoft.com/_/img/icons/external-link.svg)](https://dataweave.mulesoft.com/learn/), can process a valid MIME type set through the `input` directive in the same DataWeave script. To input reader properties to a script in a Mule application, configure the `outputMimeType` attribute for the data source to produce the same results. See [Using Reader and Writer Properties](https://docs.mulesoft.com/dataweave/latest/dataweave-formats#using-reader-and-writer-properties) for further details.

### ![Image 25: Copy link to clipboard](https://docs.mulesoft.com/_/img/icons/anchor.svg)Stack Overflow

When a function recurses too deeply, an error like the following one is thrown:

```weave
Stack Overflow. Max stack is 256
```

weave![Image 26: copy icon](https://docs.mulesoft.com/_/img/icons/copy-default.svg)✓ Copied

You can configure the maximum stack size by using the property `com.mulesoft.dw.stacksize`.

### ![Image 27: Copy link to clipboard](https://docs.mulesoft.com/_/img/icons/anchor.svg)No space left on device

To handle large payloads, DataWeave generates data that is handled in memory unless the payload exceeds a configurable limit. If the payload exceeds the limit, the data is stored on disk as output, input, and buffer files in a temporary directory. See [DataWeave Memory Management](https://docs.mulesoft.com/dataweave/latest/dataweave-memory-management) for further details.

When the streams that reference the files are closed, the files are released. Closure normally occurs when flows complete their execution, so many buffer files in the temporary folder can remain in use during long-running and concurrent executions.

To avoid the exception `No space left on device`, try to provide more resources to run the application, or determine whether you can reduce the application’s resource consumption.

Sometimes bugs prevent the release of the files even after the flow has completed. If the latest Mule release does not fix this issue, please report the issue to the MuleSoft support team.

### ![Image 28: Copy link to clipboard](https://docs.mulesoft.com/_/img/icons/anchor.svg)Closed Streams

Input data that reaches DataWeave is usually a stream. Mule handles the stream and adds auto-closing and repeatable capabilities to it by generating “cursors” over the stream. Sometimes a stream closes prematurely, before it reaches the DataWeave script, and it can be difficult to understand what closed it. In these circumstances, the script fails with an error similar to `Cannot open a new cursor on a closed stream`.

If this error occurs in latest Mule update, please report it to the MuleSoft support team. It is not possible to work around the issue, but you can use the `com.mulesoft.dw.track.cursor.close` system property to determine which component closed the stream prematurely. With the property set, the error shows the stack trace from the moment that the stream was closed, which points to the component that triggered the closure.

### ![Image 29: Copy link to clipboard](https://docs.mulesoft.com/_/img/icons/anchor.svg)Output Mismatch When Undefined

Unlike transformations, DataWeave expressions do not require you to define an output format because DataWeave can infer the output based on the expression and the variables you use. Occasionally, the inference process results in a mismatch between the inferred type and the expected type. To resolve this issue, you must make the output explicit. Common examples of this situation occur when:

*   [Extract Data from XML](https://docs.mulesoft.com/dataweave/latest/dataweave-troubleshoot#xml_extraction)

*   [Handle Multipart Entries](https://docs.mulesoft.com/dataweave/latest/dataweave-troubleshoot#multipart_handling)

*   [Manipulate Text Data](https://docs.mulesoft.com/dataweave/latest/dataweave-troubleshoot#manipulating_text)

#### ![Image 30: Copy link to clipboard](https://docs.mulesoft.com/_/img/icons/anchor.svg)Extract Data from XML

When extracting a String, for example, from an XML payload with the expression `payload.order.product.model`, DataWeave infers an XML output based on the payload format. In such cases, an error similar to the following one occurs:

```weave
"Trying to output non-whitespace characters outside main element tree (in prolog or epilog), while writing Xml at ." evaluating expression: "payload.order.product.model".
```

weave![Image 31: copy icon](https://docs.mulesoft.com/_/img/icons/copy-default.svg)✓ Copied

For such an error, you must make the output format explicit, for example: `output text/plain --- payload.order.product.model`.

#### ![Image 32: Copy link to clipboard](https://docs.mulesoft.com/_/img/icons/anchor.svg)Handle Multipart Entries

A common inference error occurs with multipart data, which has a very specific structure. Consider a multipart payload and the expression `dw::core::Objects::keySet(payload.parts)`. Without an explicit output format, DataWeave must infer, based on the payload type, that you intend to output multipart content. In this case, an error similar to the following is thrown:

```weave
"Expecting type is {
  preamble?: String,
  parts: {
    _*: {
      headers: Object,
      content: Any
    }
  }
} but got Array, while writing MultiPart.
Trace:
  at main (Unknown)" evaluating expression: "dw::core::Objects::keySet(payload.parts)".
```

weave![Image 33: copy icon](https://docs.mulesoft.com/_/img/icons/copy-default.svg)✓ Copied

To resolve this issue, you must define an output format, for example: `output application/json --- dw::core::Objects::keySet(payload.parts)`

#### ![Image 34: Copy link to clipboard](https://docs.mulesoft.com/_/img/icons/anchor.svg)Manipulate Text Data

You can use text data to create a more complex object. However, if you do not define the output format for the input text data, DataWeave infers that it must use the plain text writer for the output. The expression `payload splitBy ' '`, for example, will fail with an error similar to:

```weave
"Text plain writer is unable to write Array.
Reason:
Cannot coerce Array (org.mule.weave.v2.model.values.ArrayValue$ArraySeqArrayValue@1331b353) to String
Trace:
  at main (Unknown), while writing TextPlain.
Trace:
  at main (Unknown)" evaluating expression: "payload splitBy ' '".
```

weave![Image 35: copy icon](https://docs.mulesoft.com/_/img/icons/copy-default.svg)✓ Copied

Making the output explicit solves the issue: `output application/java --- payload splitBy ' '`

### ![Image 36: Copy link to clipboard](https://docs.mulesoft.com/_/img/icons/anchor.svg)Encoding Issues

Encoding issues can occur because of a mismatch between encodings used to read and write a file or when the encoding to write some text does not support some of the characters. Common examples include the following:

*   [Incorrect Encoding for the Reader](https://docs.mulesoft.com/dataweave/latest/dataweave-troubleshoot#reader_encoding)

*   [Encoding Used by the Writer Does Not Support Some Characters](https://docs.mulesoft.com/dataweave/latest/dataweave-troubleshoot#writer_encoding)

*   [Multipart/Form-Data Reader Does Not Support UTF-8 Characters by Default](https://docs.mulesoft.com/dataweave/latest/dataweave-troubleshoot#multipart_reader)

#### ![Image 37: Copy link to clipboard](https://docs.mulesoft.com/_/img/icons/anchor.svg)Incorrect Encoding for the Reader

In Mule, when you use components or connector operations that provide a `MIME Type` configuration (such as `Set Payload`, `File Read`, `HTTP Listener`), check that the encoding you set corresponds to the encoding used to write the payload. DataWeave reads the encoding that you set in the `MIME Type` configuration.

If you do not set the MIME type, DataWeave uses the default encoding provided by Mule through the `mule.encoding` system property.

#### ![Image 38: Copy link to clipboard](https://docs.mulesoft.com/_/img/icons/anchor.svg)Encoding Used by the Writer Does Not Support Some Characters

Check that your writer encoding supports the characters that you are trying to write.

For example, writing the text `"～―－＄￠￡㈱①"` with the encoding `sjis` outputs `"???＄????"` because many of the input characters are not supported in that encoding (unlike UTF-8, for example).

```weave
%dw 2.0
output application/json encoding="sjis"
---
"～―－＄￠￡㈱①"
```

weave![Image 39: copy icon](https://docs.mulesoft.com/_/img/icons/copy-default.svg)✓ Copied

#### ![Image 40: Copy link to clipboard](https://docs.mulesoft.com/_/img/icons/anchor.svg)Multipart/Form-Data Reader Does Not Support UTF-8 Characters by Default

If you use UTF-8 characters in the multipart filenames, the non-ASCII characters in the names are corrupted.

Set the following system property to enable support for UTF-8 in multipart: `-M-Dmail.mime.allowutf8=true`

For example, posting a multipart payload with filename=`不明.txt` without setting the `allowutf8` property to `true` produces the following unreadable text for the `filename` field:

```weave
{
  "Content-Disposition": {
    name: "file",
    filename: "ä\ufffd\ufffd明.txt",
    subtype: "form-data"
  },
  "Content-Type": "text/plain"
}
```

weave![Image 41: copy icon](https://docs.mulesoft.com/_/img/icons/copy-default.svg)✓ Copied

![Image 42: Copy link to clipboard](https://docs.mulesoft.com/_/img/icons/anchor.svg)DataWeave Warnings
-------------------------------------------------------------------------------------------------------

The following are some common DataWeave warnings that appear in your dump file, along with some details to address these warnings.

### ![Image 43: Copy link to clipboard](https://docs.mulesoft.com/_/img/icons/anchor.svg)End of Input Was Reached

This warning appears because DataWeave treats the Unicode non-character `U+FFFF` as a special character that indicates the end of input.

To avoid this warning, replace the special character in the raw payload and then proceed as usual.

```weave
read(payload.^raw replace "\uFFFF" with "NonChar")
```

weave![Image 44: copy icon](https://docs.mulesoft.com/_/img/icons/copy-default.svg)✓ Copied

![Image 45: Copy link to clipboard](https://docs.mulesoft.com/_/img/icons/anchor.svg)Low Performance Issues
-----------------------------------------------------------------------------------------------------------

### ![Image 46: Copy link to clipboard](https://docs.mulesoft.com/_/img/icons/anchor.svg)application/dw Format

Using `output application/dw` format can impact the performance of transformations. This format is intended to help you debug the results of DataWeave transformations. It is significantly slower than other formats, so avoid using this format in production applications.

### ![Image 47: Copy link to clipboard](https://docs.mulesoft.com/_/img/icons/anchor.svg)multipart/form-data Content Parsing

For `multipart/form-data` inputs, accessing content of a large part can cause performance degradation, especially for high-memory formats like `application/xlsx`, because the interpreter attempts to parse the content of the part for further querying and analysis.

You can use the `^raw` selector to avoid parsing binary contents of parts.

The following example uses the `^raw` selector on specific operations over each part.

#### ![Image 48: Copy link to clipboard](https://docs.mulesoft.com/_/img/icons/anchor.svg)Input

```text
--myboundary
Content-Disposition: form-data; name="file1"; filename="a.json"
Content-Type: application/json

{
"title": "Java 8 in Action",
"author": "Mario Fusco",
"year": 2014
}
--myboundary
Content-Disposition: form-data; name="file2"; filename="a.xml"
Content-Type: application/xml

<doc>
    <title> Available for download! </title>
    <content> Really large content </content>
</doc>
--myboundary--
```

text![Image 49: copy icon](https://docs.mulesoft.com/_/img/icons/copy-default.svg)✓ Copied

#### ![Image 50: Copy link to clipboard](https://docs.mulesoft.com/_/img/icons/anchor.svg)Source

```weave
%dw 2.0
input payload multipart boundary='myboundary'
output application/json
---
payload.parts mapObject ((value, key, index) ->
{
    (key): {
	fileName: payload.parts[index].headers.'Content-Disposition'.filename,
    rawContent: payload.parts[index].content.^raw
    }
})
```

weave![Image 51: copy icon](https://docs.mulesoft.com/_/img/icons/copy-default.svg)✓ Copied

[Back to top](https://docs.mulesoft.com/dataweave/latest/dataweave-troubleshoot#)

Did this article solve your issue?

Let us know so we can improve!

Yes

![Image 52](https://docs.mulesoft.com/_/img/icons/like.svg)

No

![Image 53](https://docs.mulesoft.com/_/img/icons/dislike.svg)

Please check at least 1 checkbox.
Would you like to share any additional feedback? (Optional)

800 / 800

![Image 54](https://docs.mulesoft.com/_/img/icons/success.svg) Your feedback has been successfully submitted. Thank you! [View on GitHub](https://github.com/mulesoft/docs-dataweave/blob/v2.11/modules/ROOT/pages/dataweave-troubleshoot.adoc)

*   Products
    *   [Anypoint Platform](https://www.mulesoft.com/platform/enterprise-integration)
    *   [MuleSoft Composer](https://www.mulesoft.com/platform/composer)
    *   [MuleSoft RPA](https://www.mulesoft.com/platform/rpa)
    *   [MuleSoft IDP](https://www.mulesoft.com/platform/intelligent-document-processing)
    *   [Start a free trial](https://anypoint.mulesoft.com/login/signup?apintent=generic)
    *   [Download Studio](https://www.mulesoft.com/lp/dl/studio)

*   Solutions
    *   [API management](https://www.mulesoft.com/api/management)
    *   [Integration](https://www.mulesoft.com/integration)
    *   [Automation](https://www.mulesoft.com/integration-solutions/api/business-automation)
    *   [Artificial Intelligence](https://www.mulesoft.com/platform/ai)
    *   [See all solutions](https://www.mulesoft.com/integration-solutions)

*   Services
    *   [Training](https://trailheadacademy.salesforce.com/products/mulesoft#f-products=Mulesoft)
    *   [Certification](https://trailhead.salesforce.com/en/credentials/administratoroverview/)
    *   [MuleSoft Catalyst](https://www.mulesoft.com/support-and-services/consulting)
    *   [Business Value Services](https://www.mulesoft.com/support-and-services/business-value-services)

*   Support
    *   [Help Center](https://help.mulesoft.com/)
    *   [Community](https://www.mulesoft.com/community)
    *   [Tutorials](https://developer.mulesoft.com/tutorials-and-howtos)
    *   [Documentation](https://docs.mulesoft.com/)
    *   [Quick start guides](https://www.mulesoft.com/lp/ebook/api/integration-quick-start-guide)
    *   [Contact us](https://www.mulesoft.com/contact)

*   Resources
    *   [Webinars](https://www.mulesoft.com/integration-resources?type%5B0%5D=Webinar)
    *   [Demos](https://www.mulesoft.com/integration-resources?type%5B0%5D=Demo)
    *   [Videos](https://videos.mulesoft.com/)
    *   [Analyst reports](https://www.mulesoft.com/integration-resources?type%5B0%5D=Report)
    *   [eBooks](https://www.mulesoft.com/integration-resources?type%5B0%5D=eBook)
    *   [Whitepapers](https://www.mulesoft.com/integration-resources?type%5B0%5D=Whitepaper)
    *   [Infographics](https://www.mulesoft.com/integration-resources?type%5B0%5D=Infographic)
    *   [Articles](https://www.mulesoft.com/resources/articles)
    *   [Blog](https://blogs.mulesoft.com/bloghome/)

*   Explore more
    *   [New release features](https://www.mulesoft.com/platform/new-product-features)
    *   [Customer stories](https://www.mulesoft.com/case-studies)
    *   [Events](https://www.mulesoft.com/events)
    *   [Partners](https://www.mulesoft.com/integration-partner)
    *   [Newsroom](https://www.salesforce.com/news/products/mulesoft/)
    *   [Newsletter sign-up](https://www.linkedin.com/newsletters/technically-speaking-7140068811264651264/)
    *   [Careers](https://careers.salesforce.com/en/jobs/?search=MuleSoft)

[](https://www.mulesoft.com/)

[Legal](https://www.salesforce.com/company/legal/)[Terms of Service](https://www.salesforce.com/company/legal/sfdc-website-terms-of-service/)[Privacy](https://www.salesforce.com/company/privacy/)[Trust](https://trust.salesforce.com/)[Contact](https://www.salesforce.com/company/contact-us/?d=cta-glob-footer-11)[Responsible Disclosure](https://www.salesforce.com/company/legal/disclosure/)Cookies Settings

[Your Privacy Choices](https://www.salesforce.com/form/other/privacy-request/)

© Copyright 2025 Salesforce, Inc. [All rights reserved.](https://www.salesforce.com/company/legal/tmcusageguidelines/) Various trademarks held by their respective owners. Salesforce, Inc. Salesforce Tower, 415 Mission Street, 3rd Floor, San Francisco, CA 94105, United States[Link to MuleSoft Linkedin profile](https://www.linkedin.com/company/mulesoft/)[Link to MuleSoft Twitter profile](https://twitter.com/MuleSoft)[Link to MuleSoft Instagram profile](https://www.instagram.com/mulesoft)[Link to MuleSoft Facebook profile](https://www.facebook.com/MuleSoft/)[Link to MuleSoft Videos platform](https://www.youtube.com/user/mulesoftvids)[Link to MuleSoft Twitch profile](https://www.twitch.tv/mulesoft_community)

![Image 55](https://t.co/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%26800%26600%268%2624%26800%26600%260%26na&eci=3&event=%7B%7D&event_id=4592df2f-cf2f-4b62-9a6e-fdfe235c39d3&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=05b7b6af-bd09-4bea-8041-1817d58d6827&pt=Troubleshooting%20a%20Failing%20DataWeave%20Script%20%7C%20MuleSoft%20Documentation&tw_document_href=https%3A%2F%2Fdocs.mulesoft.com%2Fdataweave%2Flatest%2Fdataweave-troubleshoot&tw_iframe_status=0&tw_pid_src=1&twpid=tw.1773228892949.350091354838428402&txn_id=nuq81&type=javascript&version=2.3.44)![Image 56](https://analytics.twitter.com/1/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%26800%26600%268%2624%26800%26600%260%26na&eci=3&event=%7B%7D&event_id=4592df2f-cf2f-4b62-9a6e-fdfe235c39d3&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=05b7b6af-bd09-4bea-8041-1817d58d6827&pt=Troubleshooting%20a%20Failing%20DataWeave%20Script%20%7C%20MuleSoft%20Documentation&tw_document_href=https%3A%2F%2Fdocs.mulesoft.com%2Fdataweave%2Flatest%2Fdataweave-troubleshoot&tw_iframe_status=0&tw_pid_src=1&twpid=tw.1773228892949.350091354838428402&txn_id=nuq81&type=javascript&version=2.3.44)

![Image 57: Salesforce](https://www.mulesoft.com/oneTrust/consent/fc594183-7384-4f03-8c43-1f81571521b7/01938ba0-2bc1-7129-9a4c-e70d4380975d/logos/ddb906c9-f57b-40fc-85a1-c8bcbc371b0d/6a33a761-886e-4860-8e17-abc0832f7a62/corporate_logo_big.png)

Cookie Consent Manager
----------------------

*   ### General Information 
*   ### Required Cookies 
*   ### Functional Cookies 
*   ### Advertising Cookies 

#### General Information

We use three kinds of cookies on our websites: required, functional, and advertising. You can choose whether functional and advertising cookies apply. Click on the different cookie categories to find out more about each category and to change the default settings. 

[Privacy Statement](https://www.salesforce.com/company/privacy/full_privacy/)

#### Required Cookies

Always Active

Required cookies are necessary for basic website functionality. Some examples include: session cookies needed to transmit the website, authentication cookies, and security cookies.

Cookies Details‎

#### Functional Cookies

- [x] Functional Cookies 

Functional cookies enhance functions, performance, and services on the website. Some examples include: cookies used to analyze site traffic, cookies used for market research, and cookies used to display advertising that is not directed to a particular individual.

Cookies Details‎

#### Advertising Cookies

- [x] Advertising Cookies 

Advertising cookies track activity across websites in order to understand a viewer’s interests, and direct them specific marketing. Some examples include: cookies used for remarketing, or interest-based advertising.

Cookies Details‎

### Cookie List

Consent Leg.Interest

- [x] checkbox label label

- [x] checkbox label label

- [x] checkbox label label

Clear

- [x] checkbox label label

Apply Cancel

Save Settings

Accept All Cookies

[![Image 58: Powered by Onetrust](https://www.mulesoft.com/oneTrust/consent/fc594183-7384-4f03-8c43-1f81571521b7/01938ba0-2bc1-7129-9a4c-e70d4380975d/logos/static/powered_by_logo.svg)](https://www.onetrust.com/products/cookie-consent/)

![Image 59](https://id.rlcdn.com/464526.gif)![Image 60](https://t.co/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%26800%26600%268%2624%26800%26600%260%26na&eci=1&event_id=14867e58-534a-4860-8a57-67176993e191&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=05b7b6af-bd09-4bea-8041-1817d58d6827&pt=Troubleshooting%20a%20Failing%20DataWeave%20Script%20%7C%20MuleSoft%20Documentation&tw_document_href=https%3A%2F%2Fdocs.mulesoft.com%2Fdataweave%2Flatest%2Fdataweave-troubleshoot&tw_iframe_status=0&tw_order_quantity=0&tw_pid_src=1&tw_sale_amount=0&twpid=tw.1773228892949.350091354838428402&txn_id=nue0l&type=javascript&version=2.3.44)![Image 61](https://analytics.twitter.com/i/adsct?bci=4&dv=UTC%26en-US%26Google%20Inc.%26Linux%20x86_64%26255%26800%26600%268%2624%26800%26600%260%26na&eci=1&event_id=14867e58-534a-4860-8a57-67176993e191&integration=advertiser&p_id=Twitter&p_user_id=0&pl_id=05b7b6af-bd09-4bea-8041-1817d58d6827&pt=Troubleshooting%20a%20Failing%20DataWeave%20Script%20%7C%20MuleSoft%20Documentation&tw_document_href=https%3A%2F%2Fdocs.mulesoft.com%2Fdataweave%2Flatest%2Fdataweave-troubleshoot&tw_iframe_status=0&tw_order_quantity=0&tw_pid_src=1&tw_sale_amount=0&twpid=tw.1773228892949.350091354838428402&txn_id=nue0l&type=javascript&version=2.3.44)
