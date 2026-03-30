# Source: https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-decode-encode

Title: Decode and Encode Base64 | MuleSoft Documentation

URL Source: https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-decode-encode

Published Time: Wed, 11 Mar 2026 09:30:46 GMT

Markdown Content:
Decode and Encode Base64 | MuleSoft Documentation
===============

Skip to left navigation Skip to main content Skip to page navigation

[](https://www.mulesoft.com/)

*   Products For IT Teams[Anypoint Platform World’s #1 integration and API platform](https://www.mulesoft.com/platform/enterprise-integration)Integration[Code Builder](https://www.mulesoft.com/platform/api/anypoint-code-builder)[Exchange](https://www.mulesoft.com/platform/exchange)[Connectors](https://www.mulesoft.com/platform/cloud-connectors)[MCP Support](https://www.mulesoft.com/platform/ai/model-context-protocol)API management[Flex Gateway](https://www.mulesoft.com/platform/api/flex-api-gateway)[API Governance](https://www.mulesoft.com/platform/api/governance-anypoint)[Monitoring](https://www.mulesoft.com/platform/api/monitoring-anypoint)[API Manager](https://www.mulesoft.com/platform/api/manager)[See all](https://www.mulesoft.com/platform/anypoint-platform-features)  Try for free[Sign up to Anypoint Platform](https://anypoint.mulesoft.com/login/#/signup?apintent=generic)[Download Anypoint Code Builder, Studio, Mule](https://www.mulesoft.com/lp/dl/anypoint-mule-studio)  For Business Teams[MuleSoft for Flow: Integration Point to point integration with clicks, not code](https://www.mulesoft.com/platform/flow-integration)[MuleSoft IDP Extract unstructured data from documents with AI](https://www.mulesoft.com/platform/intelligent-document-processing)[MuleSoft RPA Automate tasks with bots](https://www.mulesoft.com/platform/rpa)[Dataloader.io Securely import and export unlimited Salesforce data](https://dataloader.io/)For AI[MuleSoft for Agentforce Power Agentforce with APIs and actions](https://www.mulesoft.com/platform/agentforce)[Einstein for MuleSoft Build integrations and automations faster using natural language](https://www.mulesoft.com/ai/einstein-for-mulesoft)     [![Image 3: A graphic of MuleSoft MCP Support](https://mulesoftd8.www.msit.io/sites/default/files/cmm_files/hero_image--3-.png) MuleSoft MCP Support is now available Learn how to transform your APIs to agent ready assets in minutes. Learn more](https://www.mulesoft.com/platform/ai/model-context-protocol)   
*   Solutions Featured Solutions[API Management Manage and secure any API, built and deployed anywhere](https://www.mulesoft.com/api/management)[Integration Connect any system, data, or API to integrate at scale](https://www.mulesoft.com/integration)[Automation Automate processes and tasks for every team](https://www.mulesoft.com/automation)[MuleSoft AI Connect data and automate workflows with AI](https://www.mulesoft.com/platform/ai)Featured Integration[Salesforce Power connected experiences with Salesforce integration](https://www.mulesoft.com/integration/salesforce)[SAP Unlock SAP and connect your IT landscape](https://www.mulesoft.com/integration/sap)[AWS Get the most out of AWS with integration and APIs](https://www.mulesoft.com/integration-solutions/soa/aws)[Small business Unlock AI-powered success for your small business](https://www.mulesoft.com/small-business)   By Industry[Financial services](https://www.mulesoft.com/solutions/financial-services)[Government](https://www.mulesoft.com/integration-solutions/soa/government)[Healthcare and life sciences](https://www.mulesoft.com/integration-solutions/soa/healthcare)[Higher education](https://www.mulesoft.com/integration-solutions/soa/higher-education)[Insurance](https://www.mulesoft.com/integration-solutions/soa/insurance)[Manufacturing](https://www.mulesoft.com/integration-solutions/api/manufacturing-edi-erp)[Media and telecom](https://www.mulesoft.com/integration-solutions/soa/digital-media)[Retail](https://www.mulesoft.com/integration-solutions/saas/retail)[Consumer goods](https://www.mulesoft.com/integration-solutions/soa/consumer-goods)By Initiative[B2B EDI integration](https://www.mulesoft.com/integration/b2b-edi-platform)[DevOps](https://www.mulesoft.com/integration-solutions/api/devops)[eCommerce](https://www.mulesoft.com/integration-solutions/api/ecommerce)[Event-Driven Architecture](https://www.mulesoft.com/event-driven-architecture)[iPaaS](https://www.mulesoft.com/integration-solutions/api/ipaas)[Legacy system modernization](https://www.mulesoft.com/legacy-system-modernization/legacy-system-modernization-solution)[Microservices](https://www.mulesoft.com/api/microservices)[Move to the cloud](https://www.mulesoft.com/integration/move-to-the-cloud)[Omnichannel](https://www.mulesoft.com/integration-solutions/api/omnichannel)[SaaS integration](https://www.mulesoft.com/integration-solutions/api/saas)[Single view of customer](https://www.mulesoft.com/integration-solutions/api/360-degree-view-customer)[See all solutions](https://www.mulesoft.com/integration-solutions)      [![Image 4: An image of the ebook cover: Create Connected Experiences with MuleSoft + AI](https://www.mulesoft.com/sites/default/files/cmm_files/image-mulesoft-solutions-create-connected-experiences-with-ai.png) Create connected experiences with AI Learn the critical steps to developing an AI strategy and foundation. Read more](https://www.mulesoft.com/lp/ebook/api/salesforce-integration-customer-360)   
*   Services Training[Courses](https://trailheadacademy.salesforce.com/products/mulesoft#f-products=Mulesoft)[Certifications](https://trailheadacademy.salesforce.com/products/mulesoft#f-products=MuleSoft%E2%80%9D%20target=%E2%80%9D_blank%E2%80%9D%20role=)[Training credits](https://trailhead.salesforce.com/help?article=Salesforce-Learning-Credits-FAQ-and-Redemption-Process)Customer success[MuleSoft Catalyst](https://www.mulesoft.com/support-and-services/consulting)[Business Value Services](https://www.mulesoft.com/support-and-services/mobilize-consulting-solutions)Support[Help Center](https://help.mulesoft.com/s/)[Community Forums](https://trailhead.salesforce.com/trailblazer-community/neighborhoods/mulesoft)      [![Image 5: An image of the ebook cover: 3 Predictions for the Future of Connected AI Agents](https://www.mulesoft.com/sites/default/files/cmm_files/image-mulesoft-services-future-of-connected-ai-agents.png) Future of connected AI agents Discover how to prepare for the future of autonomous AI agents. Read more](https://www.mulesoft.com/lp/whitepaper/3-predictions-future-of-connected-ai-agents)   
*   Resources Featured Resources[Customer stories](https://www.mulesoft.com/case-studies)[Newsroom](https://www.salesforce.com/news/products/mulesoft/)[Newsletter sign-up](https://www.linkedin.com/newsletters/technically-speaking-7140068811264651264/) Explore[Webinars](https://www.mulesoft.com/webinars)[Demos](https://www.mulesoft.com/integration-resources?type%5B0%5D=demo)[Videos](https://videos.mulesoft.com/)[Analyst reports](https://www.mulesoft.com/reports)[eBooks](https://www.mulesoft.com/ebook)[Whitepapers](https://www.mulesoft.com/whitepaper/integration-use-cases)[Infographics](https://www.mulesoft.com/infographics)[Articles](https://www.mulesoft.com/resources/articles)[Blog](https://blogs.mulesoft.com/bloghome/)[API University](https://www.mulesoft.com/api-university/what-are-apis-and-how-do-they-work) [See all resources](https://www.mulesoft.com/integration-resources)  Events[MuleSoft Connect:AI](https://mulesoft.com/connect-ai)[MuleSoft at Dreamforce](https://www.mulesoft.com/dreamforce)[MuleSoft at TrailblazerDX](https://www.salesforce.com/trailblazerdx)[Community Meetups](https://meetups.mulesoft.com/)[All events](https://www.mulesoft.com/events)     [![Image 6: A graphic showing the keynote presentation at Connect:AI](https://mulesoftd8.www.msit.io/sites/default/files/cmm_files/keynote-opt02_11zon.jpg) Go from composability to agent actionability Relive the best moments from Connect:AI with our on-demand sessions. Start watching](https://www.mulesoft.com/connect-ai)   

*   Developers [Getting started](https://developer.mulesoft.com/)[Community](https://www.mulesoft.com/community)[Training](https://trailheadacademy.salesforce.com/products/mulesoft#f-products=Mulesoft)[Tutorials](https://developer.mulesoft.com/tutorials-and-howtos)[Documentation](https://docs.mulesoft.com/general/)   
*   Partners For customers[Find a partner](https://www.mulesoft.com/integration-partner/finder)For partners[Become a partner](https://www.mulesoft.com/integration-partner/become-partner)   

[Contact Us](https://www.mulesoft.com/contact)1-800-596-4880

*    [English (Full site)](https://docs.mulesoft.com/)[日本語](https://docs.mulesoft.com/jp)      
*   Login [Anypoint Platform](https://anypoint.mulesoft.com/login/#/signin?apintent=generic)[Composer](https://composer.mulesoft.com/login/sign-in)[Help Center](https://help.mulesoft.com/s/login/)      
*   [Free trial](https://anypoint.mulesoft.com/login/#/signup?apintent=generic)

[](https://www.mulesoft.com/)

*   Products For IT Teams[Anypoint Platform World’s #1 integration and API platform](https://www.mulesoft.com/platform/enterprise-integration)Integration[Code Builder](https://www.mulesoft.com/platform/api/anypoint-code-builder)[Exchange](https://www.mulesoft.com/platform/exchange)[Connectors](https://www.mulesoft.com/platform/cloud-connectors)[MCP Support](https://www.mulesoft.com/platform/ai/model-context-protocol)API management[Flex Gateway](https://www.mulesoft.com/platform/api/flex-api-gateway)[API Governance](https://www.mulesoft.com/platform/api/governance-anypoint)[Monitoring](https://www.mulesoft.com/platform/api/monitoring-anypoint)[API Manager](https://www.mulesoft.com/platform/api/manager)[See all](https://www.mulesoft.com/platform/anypoint-platform-features)  Try for free[Sign up to Anypoint Platform](https://anypoint.mulesoft.com/login/#/signup?apintent=generic)[Download Anypoint Code Builder, Studio, Mule](https://www.mulesoft.com/lp/dl/anypoint-mule-studio)  For Business Teams[MuleSoft for Flow: Integration Point to point integration with clicks, not code](https://www.mulesoft.com/platform/flow-integration)[MuleSoft IDP Extract unstructured data from documents with AI](https://www.mulesoft.com/platform/intelligent-document-processing)[MuleSoft RPA Automate tasks with bots](https://www.mulesoft.com/platform/rpa)[Dataloader.io Securely import and export unlimited Salesforce data](https://dataloader.io/)For AI[MuleSoft for Agentforce Power Agentforce with APIs and actions](https://www.mulesoft.com/platform/agentforce)[Einstein for MuleSoft Build integrations and automations faster using natural language](https://www.mulesoft.com/ai/einstein-for-mulesoft)     [![Image 7: A graphic of MuleSoft MCP Support](https://mulesoftd8.www.msit.io/sites/default/files/cmm_files/hero_image--3-.png) MuleSoft MCP Support is now available Learn how to transform your APIs to agent ready assets in minutes. Learn more](https://www.mulesoft.com/platform/ai/model-context-protocol)   
*   Solutions Featured Solutions[API Management Manage and secure any API, built and deployed anywhere](https://www.mulesoft.com/api/management)[Integration Connect any system, data, or API to integrate at scale](https://www.mulesoft.com/integration)[Automation Automate processes and tasks for every team](https://www.mulesoft.com/automation)[MuleSoft AI Connect data and automate workflows with AI](https://www.mulesoft.com/platform/ai)Featured Integration[Salesforce Power connected experiences with Salesforce integration](https://www.mulesoft.com/integration/salesforce)[SAP Unlock SAP and connect your IT landscape](https://www.mulesoft.com/integration/sap)[AWS Get the most out of AWS with integration and APIs](https://www.mulesoft.com/integration-solutions/soa/aws)[Small business Unlock AI-powered success for your small business](https://www.mulesoft.com/small-business)   By Industry[Financial services](https://www.mulesoft.com/solutions/financial-services)[Government](https://www.mulesoft.com/integration-solutions/soa/government)[Healthcare and life sciences](https://www.mulesoft.com/integration-solutions/soa/healthcare)[Higher education](https://www.mulesoft.com/integration-solutions/soa/higher-education)[Insurance](https://www.mulesoft.com/integration-solutions/soa/insurance)[Manufacturing](https://www.mulesoft.com/integration-solutions/api/manufacturing-edi-erp)[Media and telecom](https://www.mulesoft.com/integration-solutions/soa/digital-media)[Retail](https://www.mulesoft.com/integration-solutions/saas/retail)[Consumer goods](https://www.mulesoft.com/integration-solutions/soa/consumer-goods)By Initiative[B2B EDI integration](https://www.mulesoft.com/integration/b2b-edi-platform)[DevOps](https://www.mulesoft.com/integration-solutions/api/devops)[eCommerce](https://www.mulesoft.com/integration-solutions/api/ecommerce)[Event-Driven Architecture](https://www.mulesoft.com/event-driven-architecture)[iPaaS](https://www.mulesoft.com/integration-solutions/api/ipaas)[Legacy system modernization](https://www.mulesoft.com/legacy-system-modernization/legacy-system-modernization-solution)[Microservices](https://www.mulesoft.com/api/microservices)[Move to the cloud](https://www.mulesoft.com/integration/move-to-the-cloud)[Omnichannel](https://www.mulesoft.com/integration-solutions/api/omnichannel)[SaaS integration](https://www.mulesoft.com/integration-solutions/api/saas)[Single view of customer](https://www.mulesoft.com/integration-solutions/api/360-degree-view-customer)[See all solutions](https://www.mulesoft.com/integration-solutions)      [![Image 8: An image of the ebook cover: Create Connected Experiences with MuleSoft + AI](https://www.mulesoft.com/sites/default/files/cmm_files/image-mulesoft-solutions-create-connected-experiences-with-ai.png) Create connected experiences with AI Learn the critical steps to developing an AI strategy and foundation. Read more](https://www.mulesoft.com/lp/ebook/api/salesforce-integration-customer-360)   
*   Services Training[Courses](https://trailheadacademy.salesforce.com/products/mulesoft#f-products=Mulesoft)[Certifications](https://trailheadacademy.salesforce.com/products/mulesoft#f-products=MuleSoft%E2%80%9D%20target=%E2%80%9D_blank%E2%80%9D%20role=)[Training credits](https://trailhead.salesforce.com/help?article=Salesforce-Learning-Credits-FAQ-and-Redemption-Process)Customer success[MuleSoft Catalyst](https://www.mulesoft.com/support-and-services/consulting)[Business Value Services](https://www.mulesoft.com/support-and-services/mobilize-consulting-solutions)Support[Help Center](https://help.mulesoft.com/s/)[Community Forums](https://trailhead.salesforce.com/trailblazer-community/neighborhoods/mulesoft)      [![Image 9: An image of the ebook cover: 3 Predictions for the Future of Connected AI Agents](https://www.mulesoft.com/sites/default/files/cmm_files/image-mulesoft-services-future-of-connected-ai-agents.png) Future of connected AI agents Discover how to prepare for the future of autonomous AI agents. Read more](https://www.mulesoft.com/lp/whitepaper/3-predictions-future-of-connected-ai-agents)   
*   Resources Featured Resources[Customer stories](https://www.mulesoft.com/case-studies)[Newsroom](https://www.salesforce.com/news/products/mulesoft/)[Newsletter sign-up](https://www.linkedin.com/newsletters/technically-speaking-7140068811264651264/) Explore[Webinars](https://www.mulesoft.com/webinars)[Demos](https://www.mulesoft.com/integration-resources?type%5B0%5D=demo)[Videos](https://videos.mulesoft.com/)[Analyst reports](https://www.mulesoft.com/reports)[eBooks](https://www.mulesoft.com/ebook)[Whitepapers](https://www.mulesoft.com/whitepaper/integration-use-cases)[Infographics](https://www.mulesoft.com/infographics)[Articles](https://www.mulesoft.com/resources/articles)[Blog](https://blogs.mulesoft.com/bloghome/)[API University](https://www.mulesoft.com/api-university/what-are-apis-and-how-do-they-work) [See all resources](https://www.mulesoft.com/integration-resources)  Events[MuleSoft Connect:AI](https://mulesoft.com/connect-ai)[MuleSoft at Dreamforce](https://www.mulesoft.com/dreamforce)[MuleSoft at TrailblazerDX](https://www.salesforce.com/trailblazerdx)[Community Meetups](https://meetups.mulesoft.com/)[All events](https://www.mulesoft.com/events)     [![Image 10: A graphic showing the keynote presentation at Connect:AI](https://mulesoftd8.www.msit.io/sites/default/files/cmm_files/keynote-opt02_11zon.jpg) Go from composability to agent actionability Relive the best moments from Connect:AI with our on-demand sessions. Start watching](https://www.mulesoft.com/connect-ai)   

*   Developers [Getting started](https://developer.mulesoft.com/)[Community](https://www.mulesoft.com/community)[Training](https://trailheadacademy.salesforce.com/products/mulesoft#f-products=Mulesoft)[Tutorials](https://developer.mulesoft.com/tutorials-and-howtos)[Documentation](https://docs.mulesoft.com/general/)   
*   Partners For customers[Find a partner](https://www.mulesoft.com/integration-partner/finder)For partners[Become a partner](https://www.mulesoft.com/integration-partner/become-partner)   

*   Language [English (Full site)](https://docs.mulesoft.com/)[日本語](https://docs.mulesoft.com/jp)      
*   Contact By phone[1-800-596-4880](tel:1-800-596-4880) Online[Contact Us](https://www.mulesoft.com/contact)       

*   Login [Anypoint Platform](https://anypoint.mulesoft.com/login/#/signin?apintent=generic)[Composer](https://composer.mulesoft.com/login/sign-in)[Help Center](https://help.mulesoft.com/s/login/)      

[Free trial](https://anypoint.mulesoft.com/login/#/signup?apintent=generic)

[Link to MuleSoft Twitter profile](https://twitter.com/MuleSoft)[Link to MuleSoft Linkedin profile](https://www.linkedin.com/company/mulesoft)[Link to MuleSoft Facebook page](https://www.facebook.com/MuleSoft)[Link to MuleSoft Instagram profile](https://www.instagram.com/mulesoft/)[Link to MuleSoft Videos platform](https://videos.mulesoft.com/)[Link to MuleSoft Twitch profile](https://www.twitch.tv/mulesoft_community)
© Copyright 2025 Salesforce, Inc. [All rights reserved](https://www.salesforce.com/company/legal/intellectual/).

Search Docs

![Image 11](https://docs.mulesoft.com/_/img/icons/arrow-down.svg)

*   [Home](https://docs.mulesoft.com/general/) 
*   Release Notes 
*   [Archived Documentation![Image 12: Leaving the Site](https://docs.mulesoft.com/_/img/icons/external-link.svg)](https://archive.docs.mulesoft.com/)![Image 13: Archived Documentation information](https://docs.mulesoft.com/_/img/icons/tooltip-gray.svg)  

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

[View on GitHub](https://github.com/mulesoft/docs-dataweave/blob/v2.11/modules/ROOT/pages/dataweave-cookbook-decode-encode.adoc)
On this page:
=============

1.   [Encode a PDF File to Base64](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-decode-encode#ex01)
2.   [Decode Base64](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-decode-encode#ex02)
3.   [XML Configuration Example](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-decode-encode#xml_config)
4.   [See Also](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-decode-encode#see-also)

Menu
1.   [](https://docs.mulesoft.com/general/)
2.   [DataWeave (2.11)](https://docs.mulesoft.com/dataweave/latest/)
3.   [DataWeave Examples](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook)
4.   Decode and Encode Base64 (Mule)

![Image 14](https://docs.mulesoft.com/_/img/icons/arrow-down.svg)![Image 15](https://docs.mulesoft.com/_/img/icons/search.svg)

1.   [](https://docs.mulesoft.com/general/)
2.   [DataWeave (2.11)](https://docs.mulesoft.com/dataweave/latest/)
3.   [DataWeave Examples](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook)
4.   Decode and Encode Base64 (Mule)

Decode and Encode Base64
========================

![Image 16](https://docs.mulesoft.com/_/img/icons/dropdown-arrow.svg)

The following DataWeave examples show how to convert a file stream into Base64 and to convert a Base64 string into a file stream. They use a PDF file as the input and output.

MuleSoft uses the standard Base64 encoding as defined in [RFC 4648, section 4![Image 17: Leaving the Site](https://docs.mulesoft.com/_/img/icons/external-link.svg)](https://www.rfc-editor.org/rfc/rfc4648#section-4). This standard includes the `+` and `/` characters and uses `=` for padding. The encoding isn’t URL safe. To use Base64 encoding in a URL, you must first encode the URL separately.

![Image 18: Copy link to clipboard](https://docs.mulesoft.com/_/img/icons/anchor.svg)Encode a PDF File to Base64
----------------------------------------------------------------------------------------------------------------

This example performs Base64 encoding on a PDF file. It simulates the transformation in the Read operation from the [XML configuration](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-decode-encode#xml_config) by converting a Base64 file stream (`application/octet-stream`) to Binary and outputting the Binary in the `text/plain` format.

The example uses the following functions:

*   `toBase64` from the `dw::core::Binaries` module to transform a binary value to a Base64 string.

*   `readUrl` from the `Core (dw::Core)` module to input a PDF file.

The example assumes that the PDF file is in the `src/main/resources` directory of a Mule project in Anypoint Studio. It provides the name of the PDF file and specifies the MIME type as `"application/octet-stream"`. Using `"binary"` as the second `readUrl` argument is also valid for this example. 

DataWeave Script:

```dataweave
%dw 2.0
import * from dw::core::Binaries
var myPDF = readUrl("classpath://pdf-test.pdf", "application/octet-stream")
output text/plain
---
toBase64(myPDF as Binary)
```

dataweave![Image 19: copy icon](https://docs.mulesoft.com/_/img/icons/copy-default.svg)✓ Copied

Output (partial results):

```json
JVBERi0xLjYNJeLjz9MNCjM3IDAgb2JqIDw8L0xpbmVhcml6ZWQgMS9MIDIwNTk3L08gNDAvRSAx
...
```

json![Image 20: copy icon](https://docs.mulesoft.com/_/img/icons/copy-default.svg)✓ Copied

![Image 21: Copy link to clipboard](https://docs.mulesoft.com/_/img/icons/anchor.svg)Decode Base64
--------------------------------------------------------------------------------------------------

This example simulates the transformation in the Write operation from the [XML configuration](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-decode-encode#xml_config) by converting a Base64 file stream (`application/octet-stream`) to Binary and outputting the Binary in the `application/PDF with binary` format. The example does not generate a PDF file; a Write operation is required to generate such a file.

The examples use the following functions:

*   `fromBase64` in the `dw::core::Binaries` module to transform a Base64 string to a binary value.

*   `readUrl` to input a PDF file.

The example assumes that the PDF file is in the `src/main/resources` directory of a Mule project in Anypoint Studio. The function reads the input PDF as an octet-stream MIME type. Using the MIME type `"binary"` as the second `readUrl` argument is also valid for this example. 

DataWeave Script:

```dataweave
%dw 2.0
import * from dw::core::Binaries
var myPDF = readUrl("classpath://pdf-test.pdf", "application/octet-stream")
var myPDFasBinary = toBase64(myPDF as Binary)
output application/PDF with binary
---
fromBase64(myPDFasBinary as String) as Binary
```

dataweave![Image 22: copy icon](https://docs.mulesoft.com/_/img/icons/copy-default.svg)✓ Copied

The output is the text representation of the PDF.

Output (partial results):

```json
%PDF-1.6
%����
37 0 obj <</Linearized 1/L 20597/O 40/E 14115/N 1/T 19795/H [ 1005 215]>>
endobj

xref
37 34
0000000016 00000 n
...
```

json![Image 23: copy icon](https://docs.mulesoft.com/_/img/icons/copy-default.svg)✓ Copied

![Image 24: Copy link to clipboard](https://docs.mulesoft.com/_/img/icons/anchor.svg)XML Configuration Example
--------------------------------------------------------------------------------------------------------------

In Anypoint Studio, you can create and run a Mule flow that encodes and decodes a PDF file. After you complete the procedure, the example reads the file from the specified local directory using the File Connector Read operation. It writes the PDF to the specified directory by using the File Connector Write operation, and it uses Transform Message components to encode the file to Base64 and to decode that output from Base64.

1.   Create a Mule project in Anypoint Studio:

    1.   Select **File > New > Mule Project**.

    2.   Enter a name for your Mule project.

    3.   Click **Finish**.

2.   Use **Add Module** in the Mule Palette to add the File Connector:

    1.   In the **Mule Palette** view, click **(X) Search in Exchange**.

    2.   In the **Add Dependencies to Project** window, type `file` in the search field.

    3.   Click **File Connector** in Available modules.

    4.   Click **Add**.

    5.   Click **Finish**.

3.   In the Studio canvas, navigate to the **Configuration XML** tab.

4.   Copy and paste the following example between the `<mule/>` elements of a Mule flow in Anypoint Studio:

```XML
<http:listener-config name="HTTP_Listener_config"
                      doc:name="HTTP Listener config" >
    <http:listener-connection
                            host="0.0.0.0"
                            port="8081" />
</http:listener-config>
<file:config name="File_Config"
             doc:name="File Config" >
    <file:connection workingDir="/Users/me/Downloads" />
</file:config>
<flow name="encode-decode-base64">
    <http:listener doc:name="Listener"
                 path="/transform"
                 config-ref="HTTP_Listener_config"/>
    <file:read doc:name="Read"
             config-ref="File_Config"
             path="pdf-test.pdf" />
    <ee:transform doc:name="Transform Message">
        <ee:message>
          <ee:set-payload><![CDATA[%dw 2.0
import * from dw::core::Binaries
output text/plain
---
toBase64(payload as Binary)]]></ee:set-payload>
        </ee:message>
    </ee:transform>
    <ee:transform doc:name="Transform Message" >
        <ee:message >
          <ee:set-payload ><![CDATA[%dw 2.0
import * from dw::core::Binaries
output application/pdf with binary
---
fromBase64(payload as String) as Binary]]></ee:set-payload>
        </ee:message>
    </ee:transform>
    <file:write doc:name="Write"
              path="/Users/me/pdf-test-result.pdf"/>
    <set-payload
              value='#["PDF file created in the directory specified in the Write operation."]'
              doc:name="Set Payload" />
</flow>
```
XML![Image 25: copy icon](https://docs.mulesoft.com/_/img/icons/copy-default.svg)✓ Copied Expand content   Note that it is valid to replace the directive `output application/pdf with binary` in the second Transform Message component with `output application/octet-stream`. 
5.   Place a PDF file of your choice into a local directory on your machine.

6.   Correct the input and output directories of the **Read** and **Write** operations:

    *   In the **Read** operation, change the **File Path** value `/Users/me/Downloads" to the location of your PDF file.

    *   In the **Write** operation, change the **Path** value `/Users/me/pdf-test.pdf"` to the location and file name that you want to output the file.

7.   Run the project in Studio.

8.   Load the `0.0.0.0:8081/transform` into a browser.

This action creates a PDF file in the specified location and generates a separate `transform` file with the message in the Set Payload component, `PDF file created in the directory specified in the Write operation.` 

![Image 26: Copy link to clipboard](https://docs.mulesoft.com/_/img/icons/anchor.svg)See Also
---------------------------------------------------------------------------------------------

*   [Binaries (dw::core::Binaries)](https://docs.mulesoft.com/dataweave/latest/dw-binaries)

*   [DataWeave Selectors](https://docs.mulesoft.com/dataweave/latest/dataweave-selectors)

*   [DataWeave Cookbook](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook)

[Back to top](https://docs.mulesoft.com/dataweave/latest/dataweave-cookbook-decode-encode#)

Did this article solve your issue?

Let us know so we can improve!

Yes

![Image 27](https://docs.mulesoft.com/_/img/icons/like.svg)

No

![Image 28](https://docs.mulesoft.com/_/img/icons/dislike.svg)

Please check at least 1 checkbox.
Would you like to share any additional feedback? (Optional)

800 / 800

![Image 29](https://docs.mulesoft.com/_/img/icons/success.svg) Your feedback has been successfully submitted. Thank you! [View on GitHub](https://github.com/mulesoft/docs-dataweave/blob/v2.11/modules/ROOT/pages/dataweave-cookbook-decode-encode.adoc)

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

[Legal](https://www.salesforce.com/company/legal/)[Terms of Service](https://www.salesforce.com/company/legal/sfdc-website-terms-of-service/)[Privacy](https://www.salesforce.com/company/privacy/)[Trust](https://trust.salesforce.com/)[Contact](https://www.salesforce.com/company/contact-us/?d=cta-glob-footer-11)[Responsible Disclosure](https://www.salesforce.com/company/legal/disclosure/)Cookie Settings

[Your Privacy Choices](https://www.salesforce.com/form/other/privacy-request/)

© Copyright 2025 Salesforce, Inc. [All rights reserved.](https://www.salesforce.com/company/legal/tmcusageguidelines/) Various trademarks held by their respective owners. Salesforce, Inc. Salesforce Tower, 415 Mission Street, 3rd Floor, San Francisco, CA 94105, United States[Link to MuleSoft Linkedin profile](https://www.linkedin.com/company/mulesoft/)[Link to MuleSoft Twitter profile](https://twitter.com/MuleSoft)[Link to MuleSoft Instagram profile](https://www.instagram.com/mulesoft)[Link to MuleSoft Facebook profile](https://www.facebook.com/MuleSoft/)[Link to MuleSoft Videos platform](https://www.youtube.com/user/mulesoftvids)[Link to MuleSoft Twitch profile](https://www.twitch.tv/mulesoft_community)
