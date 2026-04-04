# Source: https://docs.8base.com/introduction/using-8base-at-scale

Using 8base at Scale
Introduction
â
As businesses grow, so do their technological needs. Scalability isn't just about handling more users; it's about ensuring consistent performance, security, and cost-effectiveness at every level of growth. Unlike most no- and low-code tools, 8base was built to operate large applications at scale and offers a variety of cloud instance types to cater to different scalability requirements.
8baseâs Standard Multi-Tenant Infrastructure
â
This is the default offering from 8base and a great way to get started. It provides a shared environment where resources are distributed among multiple clients. It's designed for quick setup and is most suitable for small to mid-sized applications.
Dedicated Instances
â
8base offers the ability to host backend and frontend applications in dedicated instances, which  allocate exclusive and isolated cloud resources. This ensures more consistent performance and offers a higher degree of configuration flexibility such as the size and memory of the database server, global clustering, more replicas and tunable parameters, while remaining a fully-managed service.
Self-Hosted Instances
â
For businesses that require complete control over their computing environment, 8base offers self-hosted instances. This option allows businesses to run 8base inside of their own AWS account, ensuring full customization, data sovereignty, and the ability to integrate any tool or service. It's the most hands-on option and requires a comprehensive understanding of both infrastructure management and 8base.
Tips to Realize Better Performance at Scale
â
As applications grow and user bases expand, the need for scalable infrastructure becomes paramount. 8base, with its robust architecture built on top of Amazon Web Services (AWS), is designed to handle scale. However, leveraging its full potential requires understanding and strategic implementation. This article delves into best practices and considerations for using 8base at scale.
Data Layer Optimization
â
Database Indexing
â
Ensure that your Aurora MySQL database tables are properly indexed using 8baseâs indexing functions. Indexing accelerates data retrieval speeds by providing quicker paths to data. Regularly review and optimize indexes based on query patterns.
Data Partitioning
â
For large datasets, consider partitioning your tables. This divides your table into smaller, more manageable pieces and can improve query performance.
Efficient Use of Serverless Functions
â
Stateless Design
â
Design your Lambda functions to be stateless. This ensures they can be quickly initiated and terminated, allowing for efficient scaling.
Concurrency Management
â
Monitor and adjust the concurrency settings for your Lambda functions. While AWS Lambda scales automatically, setting appropriate concurrency limits can prevent unexpected spikes and associated costs.
GraphQL API Considerations
â
Batch Operations
â
Instead of making multiple individual requests, batch operations where possible. This reduces the number of API calls and the associated overhead.
Optimize Queries
â
Avoid fetching unnecessary data. Use GraphQL's flexibility to request only the data needed, reducing the payload and improving performance.
Frontend Performance
â
Content Delivery Network (CDN)
â
Leverage 8baseâs built-in CDN capabilities enabled by Amazon CloudFront. CDNs cache content closer to users, reducing latency and improving load times.
Asynchronous Operations
â
For operations that don't need immediate feedback, consider implementing them asynchronously. This can offload heavy tasks from the main thread, ensuring a smoother user experience.
Performance Optimization
â
Developers using 8base in their own dedicated environment have the option to tune their database instance to better match the requirements of their applications.
Conclusion
â
Scaling with 8base is a combination of leveraging its built-in capabilities and implementing best practices. By staying proactive, monitoring performance, and optimizing regularly, you can ensure that your 8base application remains robust and efficient, even as it handles a growing number of users and operations.