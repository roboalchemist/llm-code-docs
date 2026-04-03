# Source: https://docs.8base.com/introduction/built-application-architecture

Built Application Architecture
Cloud Infrastructure
â
8base utilizes Amazon Web Services (AWS) for hosting both backend and frontend applications.
Data Layer
â
8base employs a fully redundant and fault-tolerant Aurora MySQL relational database within AWS. For scalability and performance, automatic load-balancing is implemented across these redundant databases.
Logic Layer
â
8base uses Amazon Lambda for serverless functions. The supported functions include:
Custom Resolvers: Custom logic for queries and mutations.
Triggers: Responses to database events.
Scheduled and On-demand Tasks: Tasks that run based on a schedule or manual triggering.
Web Hooks: For external integrations.
API Layer
â
8base offers a GraphQL API that provides:
Auto-generated CRUD commands
Pagination
Filtering
Sorting
Full-text search
Groupings
Aggregations
Documentation
The API can be extended using custom resolvers through serverless JavaScript and Typescript functions.
Frontend
â
Applications constructed with 8base's frontend tools produce a React application hosted on AWS S3. For optimized delivery, CDN services are facilitated by Amazon CloudFront.
Alternative Frontends
â
8baseâs backend and GraphQL API support frontends built using developersâ framework of choice or even other low-code tools. In these cases, frontend applications can be hosted using Netlify, Vercel or any other hosting provider.
Mobile Applications
â
8baseâs backend and GraphQL API support native mobile applications built using any of the prevailing frameworks and/or tools.