# Source: https://docs.xano.com/frequently-asked-questions.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Xano — Features & Capabilities FAQ

> An overview of Xano's features, architecture, AI capabilities, security, and enterprise readiness.

<h2>Table of Contents</h2>

<h3>Platform Basics</h3>

* [What is Xano, and where does it fit in a company's technology stack?](#what-is-xano,-and-where-does-it-fit-in-a-company's-technology-stack)
* [What types of teams typically use Xano?](#what-types-of-teams-typically-use-xano)
* [What database technology does Xano use?](#what-database-technology-does-xano-use)
* [How should I structure and model my data in Xano?](#how-should-i-structure-and-model-my-data-in-xano)

<h3>APIs & Backend Logic</h3>

* [How are APIs built and managed in Xano?](#how-are-apis-built-and-managed-in-xano)
* [Can Xano support complex business logic?](#can-xano-support-complex-business-logic)
* [Can Xano be used with code as well as visual workflows?](#can-xano-be-used-with-code-as-well-as-visual-workflows)
* [Does Xano support real-time functionality?](#does-xano-support-real-time-functionality)

<h3>Authentication & Access Control</h3>

* [How does authentication and authorization work?](#how-does-authentication-and-authorization-work)
* [Does Xano support role-based access control (RBAC)?](#does-xano-support-role-based-access-control-rbac-)

<h3>AI-Assisted Development</h3>

* [How can teams generate a backend using AI?](#how-can-teams-generate-a-backend-using-ai)
* [How does Xano help manage and evolve database schemas with AI?](#how-does-xano-help-manage-and-evolve-database-schemas-with-ai)
* [Can Xano help generate advanced database queries?](#can-xano-help-generate-advanced-database-queries)
* [Can Xano be used for AI-powered or agent-based workflows?](#can-xano-be-used-for-ai-powered-or-agent-based-workflows)

<h3>Extensibility & Integrations</h3>

* [How does Xano support custom backend code and external libraries?](#how-does-xano-support-custom-backend-code-and-external-libraries)
* [Can Xano handle background jobs and asynchronous processing?](#can-xano-handle-background-jobs-and-asynchronous-processing)
* [How does Xano integrate with existing systems?](#how-does-xano-integrate-with-existing-systems)

<h3>Scaling, Security & Enterprise</h3>

* [How does Xano scale as usage grows?](#how-does-xano-scale-as-usage-grows)
* [What are best practices for performance and scaling?](#what-are-best-practices-for-performance-and-scaling)
* [Does Xano offer data and resource isolation?](#does-xano-offer-data-and-resource-isolation)
* [Can I build a multi-tenant or B2B application with Xano?](#can-i-build-a-multi-tenant-or-b2b-application-with-xano)
* [Is Xano suitable for production and enterprise use?](#is-xano-suitable-for-production-and-enterprise-use)
* [How does Xano address security requirements?](#how-does-xano-address-security-requirements)
* [How does Xano handle backups and data recovery?](#how-does-xano-handle-backups-and-data-recovery)
* [Where is my data hosted?](#where-is-my-data-hosted)
* [How can I check Xano's uptime or service status?](#how-can-i-check-xano's-uptime-or-service-status)
* [How does Xano handle AI data and privacy?](#how-does-xano-handle-ai-data-and-privacy)

<h3>Development Workflow & Portability</h3>

* [How does Xano support development and deployment workflows?](#how-does-xano-support-development-and-deployment-workflows)
* [Can we export APIs and data from Xano?](#can-we-export-apis-and-data-from-xano)
* [How do companies typically adopt Xano?](#how-do-companies-typically-adopt-xano)
* [How does Xano compare to other platforms?](#how-does-xano-compare-to-other-platforms)

<h3>Ownership, Billing & Support</h3>

* [Who owns my data and what I build on Xano?](#who-owns-my-data-and-what-i-build-on-xano)
* [What happens if I want to leave Xano?](#what-happens-if-i-want-to-leave-xano)
* [What are Xano's usage limits, and what happens if I reach them?](#what-are-xano's-usage-limits,-and-what-happens-if-i-reach-them)
* [How does pricing work, and how can I estimate costs before launching?](#how-does-pricing-work,-and-how-can-i-estimate-costs-before-launching)
* [Can I pause my Xano subscription?](#can-i-pause-my-xano-subscription)
* [What happens if I cancel my subscription?](#what-happens-if-i-cancel-my-subscription)
* [What is Xano's refund policy?](#what-is-xano's-refund-policy)
* [Can I downgrade back to a free plan?](#can-i-downgrade-back-to-a-free-plan)
* [What kind of support do I get with Xano?](#what-kind-of-support-do-i-get-with-xano)
* [How do I get help?](#how-do-i-get-help)

***

### **What is Xano, and where does it fit in a company's technology stack?**

Xano is a backend-as-a-service platform that companies use to build, run, and scale APIs, data models, and backend logic without managing servers or infrastructure. It provides a managed database, API layer, business logic, authentication, and background processing in a single system.

Xano also acts as an execution and data layer for AI agents and agent frontends via standards like MCP (Model Context Protocol), allowing tools like ChatGPT, Claude, or custom agent UIs to securely call APIs, access structured data, and trigger backend workflows. This lets organizations expose real business capabilities to AI without giving agents direct access to production systems.

### **What types of teams typically use Xano?**

Xano is used by application development teams, platform teams, and IT organizations building internal tools, customer-facing applications, or integration layers. It supports collaboration across developers, architects, and less technical contributors.

This makes it suitable for small teams through large organizations.

### **What database technology does Xano use?**

Xano is built on PostgreSQL, a widely adopted, enterprise-grade relational database, which powers Xano's native managed database. Teams can model complex schemas, enforce relationships, and maintain data integrity without operating the database themselves.

You can also [migrate your data to Xano](the-database/migrating-your-data) or connect to existing external databases, allowing organizations to keep their data where it already lives while using Xano as an API, logic, and orchestration layer on top.

**For more info:** [the-database/database](the-database/database)

### **How should I structure and model my data in Xano?**

Xano uses a [relational database](https://www.xano.com/database/) based on Postgres, allowing you to structure data using tables and relationships similar to traditional SQL-based systems. This makes it well-suited for common application patterns such as one-to-many and many-to-many relationships, while still being accessible through a visual interface.

### **How are APIs built and managed in Xano?**

Xano provides a visual API builder that allows teams to create REST APIs using configurable logic blocks, database queries, and integrations. For teams that prefer a code-first workflow, Xano also supports building and editing APIs in code using XanoScript through its IDE extension, giving developers full control when they need it.

Beyond the primary API layer, teams can extend and automate Xano itself using the Xano MCP (Model Context Protocol) server and the Metadata API, which enable programmatic management of resources, environments, and configurations. All APIs are automatically documented and can be exported using OpenAPI (Swagger), making them easy to integrate, test, and govern across teams.

**For more info:** [api](api)

### **Can Xano support complex business logic?**

Yes. Xano's Function Stack is built so that teams can implement validations, workflows, conditional logic, and data transformations directly in the backend, with no limitations based on complexity. Logic is centralized and reusable across multiple applications and clients. This reduces duplication and helps enforce consistent rules across systems.

**For more info:** [building/build-visually/function-stack](building/build-visually/function-stack)

### **Can Xano be used with code as well as visual workflows?**

Yes. Xano supports building backend logic either visually or entirely in code using XanoScript, allowing engineering teams to choose the workflow that best fits their standards and development practices. Visual and code-based logic can coexist in the same backend, giving teams flexibility without fragmenting their architecture.

For cases where teams need to run custom JavaScript or leverage existing Node.js libraries, Xano also supports Lambda functions that execute natively within the Xano environment. This allows organizations to extend their backend with custom code while keeping everything governed, secure, and integrated.

**For more info:** [the-function-stack/building-with-visual-development/custom-functions#custom-functions](the-function-stack/building-with-visual-development/custom-functions#custom-functions)

### **Does Xano support real-time functionality?**

Xano supports real-time use cases through features such as webhooks and WebSockets. For many applications, real-time-like experiences can also be achieved through efficient APIs and frontend polling strategies, depending on the requirements of your app.

### **How does authentication and authorization work?**

Xano includes built-in authentication features such as login, token management, and secure API access. Authorization rules can be customized based on roles, ownership, or custom business logic, giving teams fine-grained control over who can access what.

In addition to native auth, Xano can integrate with common OAuth providers (such as Google, GitHub, and others) as well as custom OAuth services, allowing organizations to plug Xano into existing identity and SSO systems.

This allows organizations to implement secure access controls aligned with internal policies.

**For more info:** [security/best-practices#authentication](security/best-practices#authentication)

### **How can teams generate a backend using AI?**

Xano includes an AI-powered Getting Started Assistant that can generate a database schema, user authentication, and API endpoints from a simple description of your application. This allows teams to go from idea to a working backend in minutes.

Teams can then refine, extend, and govern what the AI produces before deploying it.

**For more info**: [building/build-with-ai/getting-started-assistant](building/build-with-ai/getting-started-assistant)

### **How does Xano help manage and evolve database schemas with AI?**

Xano's Database Assistant lets teams describe schema changes in natural language and apply them safely to their database. It suggests updates to tables, fields, and relationships and allows teams to review every change before committing.

This makes it easier to evolve data models as applications grow without breaking production systems.

**For more info:** [building/build-with-ai/database-assistant](building/build-with-ai/database-assistant)

### **Can Xano help generate advanced database queries?**

Yes. Xano includes a SQL Assistant that can translate natural-language requests into SQL queries. Teams can use it to build complex joins, filters, and aggregations and immediately preview the results.

This reduces the need for manual SQL writing while maintaining full transparency and control.

**For more info:** [building/build-with-ai/sql-assistant](building/build-with-ai/sql-assistant)

### **How does Xano support custom backend code and external libraries?**

Xano supports Lambda functions that allow teams to run custom JavaScript and leverage existing NPM libraries directly inside their backend. This is commonly used for tasks such as document generation, image processing, data transformations, or specialized integrations.

In addition, on certain plans, Xano can connect to external Docker-based microservices, enabling teams to run custom workloads in their own containers while still orchestrating them from Xano's APIs and workflows. Xano's Lambda Assistant further helps teams write and iterate on functions using AI while keeping everything integrated into the broader backend.

**For more info:** [building/build-with-ai/lambda-assistant](building/build-with-ai/lambda-assistant)

### **How does Xano handle AI data and privacy?**

Xano does not store or train on your application data when processing AI requests. Data is used only to generate the requested AI output and is not retained or repurposed.

Third-party AI providers may collect limited usage metadata for billing and performance, but your application data remains yours.

**For more info:** [https://legal.xano.com/privacy-notice](https://legal.xano.com/privacy-notice)

### **Does Xano support role-based access control (RBAC)?**

Yes. Xano supports role-based access control at both the application level and the platform level. For end users of your application, you can define roles, ownership rules, and permission logic that determine which users can access or modify specific data or APIs.

For your internal teams, Xano also provides role-based access to the Xano workspace itself, allowing you to control which developers, operators, or partners can view, edit, or deploy backend logic. This makes it suitable for both secure applications and governed development teams.

**For more info:** [team-collaboration/role-based-access-control-rbac#role-based-access-control-rbac](team-collaboration/role-based-access-control-rbac#role-based-access-control-rbac)

### **Can Xano handle background jobs and asynchronous processing?**

Yes. Xano supports background tasks for long-running or asynchronous operations such as batch processing, integrations, or notifications.

This helps maintain API performance while handling operational workloads reliably.

**For more info:** [the-function-stack/building-with-visual-development/background-tasks#background-tasks](the-function-stack/building-with-visual-development/background-tasks#background-tasks)

### **How does Xano integrate with existing systems?**

Xano can call external APIs, consume webhooks, and act as an integration layer between systems. Teams use it to connect frontends, third-party services, internal tools, and automation platforms through a single, governed backend.

To speed this up, Xano also provides pre-built integration actions and templates for common services (such as auth providers, email, payments, and automation tools), allowing teams to connect systems without writing everything from scratch. This makes Xano well suited for organizations with heterogeneous technology stacks.

**For more info:** [https://www.xano.com/connect/](https://www.xano.com/connect/)

### **Can Xano be used for AI-powered or agent-based workflows?**

Yes. Xano can serve as a backend for AI-driven applications by managing data, orchestrating workflows, and exposing APIs to AI agents. It also supports observability via OpenTelemetry.

This enables teams to add AI capabilities while maintaining backend control and visibility.

**For more info:** ​[http://docs.xano.com/ai-tools/ai-agents](http://docs.xano.com/ai-tools/ai-agents)

### **How does Xano scale as usage grows?**

Xano can scale infrastructure as demand increases, without requiring teams to manage servers or databases. For organizations with advanced needs, Xano also supports isolated environments.

**For more info:** [adjust-server-performance#how-does-xano-scale-to-meet-demand](adjust-server-performance#how-does-xano-scale-to-meet-demand)

### **What are best practices for performance and scaling?**

Xano is built to scale automatically as your application grows. Performance best practices include designing efficient queries, using pagination where appropriate, and structuring data to match access patterns. Xano provides tools to help monitor and optimize performance as usage increases.

### **Does Xano offer data and resource isolation?**

Yes. On certain plans, Xano allows you to create separate tenants for the isolation of data and resources, including regional isolation. Whether you're looking to implement CI/CD workflows, offer single-tenancy to customers, customize tenant resources, control releases, or meet data residency requirements, you can easily do it with Xano.This is ideal for SaaS companies with multiple customers who need isolated environments.

**For more info:** [enterprise/enterprise-features/tenant-center#tenant-center](enterprise/enterprise-features/tenant-center#tenant-center)

### **Can I build a multi-tenant or B2B application with Xano?**

Yes. Xano supports multi-tenant architecture through the [Tenant Center](https://www.xano.com/blog/xano-tenant-center/), which is designed for applications that need clear isolation between customers or environments. With Tenant Center, you define a single backend blueprint (your APIs, database schema, and business logic) and then deploy it across multiple tenants while keeping each tenant's data and resources fully isolated. Tenants can run in different geographic regions to meet data-residency or performance requirements, and you can manage releases and versioning across tenants from one control plane. This makes it suitable for SaaS products, enterprise platforms, or any B2B application where separate customer boundaries and operational control matter.

### **Is Xano suitable for production and enterprise use?**

Yes. Xano is designed to run production workloads and is used by organizations supporting real users and business-critical applications. It includes features for security, performance, monitoring, and operational stability.

To read up on how customers are using Xano, check out our [customer case studies page](https://www.xano.com/case-studies/) and some of our real-life customer testimonials below.

"We were able to accelerate the development process without compromising on the essential elements of security and scalability." (Arthur Anouil, [Decathlon](https://www.xano.com/case-study/how-xano-helped-decathlon-get-to-market-and-develop-3x-faster/))

""Xano made it incredibly easy to go from idea → AI-generated backend → production-grade system in a very short time." (Manikant Kella, [Dev.to](https://dev.to/manikant92/promptshield-ai-an-ai-cost-risk-firewall-built-with-xano-346e))

""Xano was my first choice due to its robust logic capabilities combined with a scalable database architecture. This combination would not only facilitate a successful launch but also ensure seamless scaling without additional technical overhead." (Tom Wesołowski for [Playmore](https://www.xano.com/case-study/how-xano-helped-playmore-replace-their-legacy-system-within-three-months/))

### **How does Xano address security requirements?**

Xano provides encryption in transit and at rest, access controls, and secure authentication mechanisms. Security configurations can be tailored to meet organizational requirements. This helps teams meet internal security standards without managing infrastructure directly.

Compliance and security details are maintained in Xano's Trust Center.

**For more info:** [https://security.xano.com/](https://security.xano.com/)

### **How does Xano handle backups and data recovery?**

Xano automatically performs backups of your data to protect against data loss. These backups are managed by Xano and are designed to support recovery in the event of an incident. This allows you to focus on building your application without needing to manage your own backup infrastructure.

### **Where is my data hosted?**

Xano runs on managed [cloud infrastructure](https://www.xano.com/server/) and stores your data in secure data centers. The specific hosting region depends on your instance configuration. Xano is designed to meet common data security and residency requirements for modern applications.

### **How can I check Xano's uptime or service status?**

Xano provides a public status page where you can view current system status and historical incidents. This allows you to quickly verify whether an issue is related to Xano's infrastructure.

### **Can we export APIs and data from Xano?**

Xano provides ways to access and extract your database content, which gives you a practical path to migrate information into a different backend, data warehouse, or cloud environment. Xano also exposes your API definitions via OpenAPI (Swagger) as documentation of how your endpoints behave, which can help other tools or engineers understand how your system works if you rebuild or reimplement parts of it elsewhere. In addition, teams that have written backend logic in XanoScript may be able to reuse parts of that logic conceptually (or translate it to another language).

**For more info:** the-database/database-basics/export-and-sharing

### **How does Xano support development and deployment workflows?**

Xano supports environment management and safe iteration on backend logic, allowing teams to test changes before rolling them out. This enables structured workflows without complex DevOps tooling.

**For more info:** [ci-cd#ci-cd](ci-cd#ci-cd)

### **How do companies typically adopt Xano?**

Companies often start by using Xano for a specific application, workflow, or integration layer, then expand usage as teams see value. Xano can coexist with existing infrastructure. This makes it a low-risk way to modernize backend development incrementally.

### **How does Xano compare to other platforms?**

Xano provides a unified backend platform that combines database, APIs, business logic, authentication, and integrations in one system. This allows teams to avoid stitching together multiple tools for different backend functions. It is designed for visual and code-based development, giving teams flexibility without sacrificing governance.

**For more info:**

* [https://www.xano.com/versus/supabase](https://www.xano.com/versus/supabase)
* [https://www.xano.com/versus/airtable](https://www.xano.com/versus/airtable)
* [https://www.xano.com/versus/bubble](https://www.xano.com/versus/bubble)

### **Who owns my data and what I build on Xano?**

You do. You retain full ownership of everything you build on Xano, including your database schemas, APIs, business logic, and any data processed through your backend. Xano does not claim rights to your intellectual property, applications, or customer data.

Xano's role is to provide the platform and infrastructure that runs your backend—not to own or reuse what you create on top of it.

### **What happens if I want to leave Xano?**

If you decide to move off Xano, you can export your data and API definitions so they can be migrated to another system. Xano supports OpenAPI (Swagger) exports for your APIs and provides mechanisms to retrieve your underlying data.

In the unlikely event that Xano were ever unable to continue operating, the company maintains an exit plan designed to help customers recover their data and API specifications in a structured way.

### **What are Xano's usage limits, and what happens if I reach them?**

Xano plans include limits based on resources such as API requests, storage, and compute. These limits are designed to support applications at different stages, from prototypes to production-scale workloads. If you approach or exceed a limit, Xano provides visibility into usage so you can upgrade or adjust your architecture as needed. Visit our [pricing page](https://www.xano.com/pricing/) for more information about specific plan limits.

### **How does pricing work, and how can I estimate costs before launching?**

Xano pricing is based on the resources required to run your backend, such as compute and storage. Different plans are designed to support different stages of growth. Before launching, you can estimate costs based on your expected usage and scale, and upgrade plans as your application grows.

### **Can I pause my Xano subscription?**

Xano subscriptions cannot be paused. If you're having difficulties, please reach out to our support team for assistance.

### **What happens if I cancel my subscription?**

You will continue to retain access to Xano until the end of your subscription period.

### **What is Xano's refund policy?**

Xano does not offer refunds on monthly plans. We may offer a refund on a yearly subscription during the first thirty days depending on the circumstances. Refunds are not processed automatically upon cancellation; you need to reach out to our support team before you cancel to process your request.

### **Can I downgrade back to a free plan?**

Due to technical limitations in our current infrastructure, it is not currently possible to directly downgrade from a paid plan back to a free plan.

### **What kind of support do I get with Xano?**

All Xano users have access to documentation and community resources. Paid plans include direct support, with higher-tier plans offering faster response times and additional support options. This ensures teams can get help appropriate to the criticality of their application.

### **How do I get help?**

* **Check out the [Xano YouTube Channel](https://www.youtube.com/nocodebackend).** Our YouTube channel is always being updated with tutorials, use case examples, feature announcements, and more.
* **Visit the [Xano Community](https://community.xano.com/).** Ask or answer questions and interact directly with other Xano users.
* **Reach out to our support team.** Just click the option in the lower-left corner anywhere in Xano to be connected to our support team, 24 hours a day.


Built with [Mintlify](https://mintlify.com).