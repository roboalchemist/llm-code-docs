# Source: https://docs.port.io/guides/all/find-internal-documentation-with-ai.md

# Find internal documentation with AI

This guide demonstrates how to find internal documentation with AI. By storing documentation as entities, you can ask questions like "When was this document last updated?", "Who owns this document?", or "What are all the product-related docs?" and get intelligent responses.

![](/img/guides/internal-docs-ai-context-1.png)

## Common use cases[â](#common-use-cases "Direct link to Common use cases")

* **Document discovery**: Find relevant documentation quickly through natural language queries
* **Ownership tracking**: Identify document owners and maintainers
* **Version control**: Track document updates and changes over time
* **Categorization**: Organize docs by product, team, or topic for better searchability
* **Knowledge sharing**: Enable team members to find information without knowing exact document names

## Prerequisites[â](#prerequisites "Direct link to Prerequisites")

This guide assumes you have:

* A Port account with the [AI agents feature enabled](/ai-interfaces/ai-agents/overview.md#access-to-the-feature)

## Set up data model[â](#set-up-data-model "Direct link to Set up data model")

We'll create an enhanced blueprint to store internal documentation with rich metadata for better AI context.

### Create Internal Documentation blueprint

1. Go to the [Builder](https://app.getport.io/settings/data-model) page of your portal.

2. Click on `+ Blueprint`.

3. Click on `{...} Edit JSON`.

4. Copy and paste the following JSON schema:

   Internal documentation blueprint (Click to expand)

   This blueprint stores internal documentation with rich metadata for AI context.

   Create in Port

   ```
   {
   "identifier": "internal_docs",
   "description": "Represent internal documentation with instructions, guides, and organizational knowledge",
   "title": "Internal Documentation",
   "icon": "FileText",
   "schema": {
       "properties": {
       "content": {
           "type": "string",
           "title": "Content",
           "description": "The main document content",
           "format": "markdown"
       },
       "documentType": {
           "type": "string",
           "title": "Document Type",
           "description": "Type of document",
           "enum": ["Guide", "Policy", "Procedure", "FAQ", "Architecture", "Runbook", "API Documentation", "Onboarding", "Troubleshooting", "Best Practices"],
           "enumColors": {
           "Guide": "blue",
           "Policy": "red",
           "Procedure": "green",
           "FAQ": "yellow",
           "Architecture": "purple",
           "Runbook": "orange",
           "API Documentation": "cyan",
           "Onboarding": "pink",
           "Troubleshooting": "red",
           "Best Practices": "green"
           }
       },
       "product": {
           "type": "string",
           "title": "Product",
           "description": "Product or service this document relates to"
       },
       "team": {
           "type": "string",
           "title": "Team",
           "description": "Team responsible for this document"
       },
       "owner": {
           "type": "string",
           "title": "Owner",
           "description": "Primary owner/maintainer of this document"
       },
       "lastUpdated": {
           "type": "string",
           "format": "date-time",
           "title": "Last Updated",
           "description": "When this document was last modified"
       },
       "version": {
           "type": "string",
           "title": "Version",
           "description": "Document version number"
       },
       "status": {
           "type": "string",
           "title": "Status",
           "description": "Document status",
           "enum": ["Draft", "Review", "Approved", "Deprecated", "Archived"],
           "enumColors": {
           "Draft": "yellow",
           "Review": "orange",
           "Approved": "green",
           "Deprecated": "red",
           "Archived": "gray"
           }
       },
       "tags": {
           "type": "array",
           "title": "Tags",
           "description": "Tags for categorizing and searching documents"
       },
       "summary": {
           "type": "string",
           "title": "Summary",
           "description": "Brief summary of what this document covers"
       },
       "relatedDocs": {
           "type": "array",
           "title": "Related Documents",
           "description": "Identifiers of related documents"
       },
       "audience": {
           "type": "string",
           "title": "Audience",
           "description": "Target audience for this document",
           "enum": ["All Teams", "Engineering", "Product", "Operations", "Security", "New Hires", "Leadership"]
       },
       "priority": {
           "type": "string",
           "title": "Priority",
           "description": "Document priority level",
           "enum": ["Critical", "High", "Medium", "Low"],
           "enumColors": {
           "Critical": "red",
           "High": "orange",
           "Medium": "yellow",
           "Low": "green"
           }
       }
       },
       "required": ["content", "documentType", "summary"]
   },
   "mirrorProperties": {},
   "calculationProperties": {},
   "aggregationProperties": {},
   "relations": {}
   }
   ```

5. Click `Create` to save the blueprint.

## Populate with sample documentation[â](#populate-with-sample-documentation "Direct link to Populate with sample documentation")

Let's add some sample internal documentation to demonstrate the AI capabilities:

* Port UI
* API
* Webhook
* Integration

### API Documentation Example

1. Go to your [software catalog](https://app.getport.io/organization).

2. Find the "Internal Documentation" tab and click `+ Internal Documentation`.

3. Toggle JSON mode and copy the following:

   API Documentation example

   ````
   {
     "properties": {
       "content": "# User Authentication API\n\n## Overview\nThis API handles user authentication and authorization for our platform.\n\n## Endpoints\n\n### POST /auth/login\nAuthenticates a user and returns a JWT token.\n\n**Request Body:**\n```json\n{\n  \"email\": \"user@example.com\",\n  \"password\": \"password123\"\n}\n```\n\n**Response:**\n```json\n{\n  \"token\": \"eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...\",\n  \"expires_in\": 3600\n}\n```\n\n### GET /auth/me\nReturns current user information.\n\n**Headers:**\n- `Authorization: Bearer <token>`\n\n**Response:**\n```json\n{\n  \"id\": \"user123\",\n  \"email\": \"user@example.com\",\n  \"name\": \"John Doe\"\n}\n```\n\n## Error Codes\n- `400`: Invalid credentials\n- `401`: Unauthorized\n- `429`: Rate limit exceeded",
       "documentType": "API Documentation",
       "product": "Authentication Service",
       "team": "Backend Engineering",
        "owner": "john.doe@company.com",
       "lastUpdated": "2024-01-15T10:30:00.000Z",
       "version": "2.1.0",
       "status": "Approved",
       "tags": ["api", "authentication", "jwt", "backend"],
       "summary": "Complete API documentation for user authentication endpoints",
       "audience": "Engineering",
       "priority": "High"
       },
     "relations": {},
     "icon": "FileText",
     "identifier": "auth-api-docs-v2",
     "title": "User Authentication API Documentation"
   }
   ````

4. Click `Create` to save the document.

### Troubleshooting Guide Example

1. Click `+ Internal Documentation` again.

2. Toggle JSON mode and copy the following:

   Troubleshooting guide example

   ```
   {
     "properties": {
       "content": "# Database Connection Issues Troubleshooting\n\n## Common Issues\n\n### Connection Timeout\n**Symptoms:**\n- API requests timing out\n- Database connection errors in logs\n- High response times\n\n**Diagnosis:**\n1. Check database connection pool status\n2. Review connection timeout settings\n3. Monitor database server resources\n\n**Solutions:**\n1. Increase connection pool size\n2. Adjust timeout values\n3. Scale database resources\n\n### Connection Pool Exhaustion\n**Symptoms:**\n- \"No available connections\" errors\n- Application hangs\n- Database locks\n\n**Diagnosis:**\n1. Check active connections\n2. Review connection leak patterns\n3. Analyze connection usage\n\n**Solutions:**\n1. Fix connection leaks in code\n2. Implement connection monitoring\n3. Add connection pool alerts\n\n## Prevention\n- Regular connection pool monitoring\n- Code reviews for connection management\n- Load testing with realistic scenarios",
       "documentType": "Troubleshooting",
       "product": "Database Infrastructure",
       "team": "Platform Engineering",
       "owner": "jane.smith@company.com",
       "lastUpdated": "2024-01-20T14:15:00.000Z",
       "version": "1.3.0",
       "status": "Approved",
       "tags": ["database", "troubleshooting", "connections", "performance"],
       "summary": "Comprehensive guide for diagnosing and resolving database connection issues",
       "audience": "Engineering",
       "priority": "Critical"
     },
    "relations": {},
    "icon": "FileText",
    "identifier": "db-connection-troubleshooting",
    "title": "Database Connection Issues Troubleshooting Guide"
   }
   ```

3. Click `Create` to save the document.

### Onboarding Guide Example

1. Click `+ Internal Documentation` again.

2. Toggle JSON mode and copy the following:

   Onboarding guide example

   ```
   {
     "properties": {
       "content": "# New Developer Onboarding Guide\n\n## Week 1: Environment Setup\n\n### Day 1-2: Development Environment\n1. **Access Setup**\n   - Request VPN access\n   - Set up development machine\n   - Install required tools (Docker, Git, IDE)\n\n2. **Repository Access**\n   - Clone main repositories\n   - Set up SSH keys\n   - Configure Git settings\n\n### Day 3-5: First Project\n1. **Choose Starter Task**\n   - Pick from \"good first issue\" list\n   - Set up local development environment\n   - Make first contribution\n\n## Week 2: Team Integration\n\n### Meetings and Processes\n1. **Team Meetings**\n   - Daily standups (9:30 AM)\n   - Weekly planning (Monday 2 PM)\n   - Retrospectives (Friday 4 PM)\n\n2. **Development Process**\n   - Code review process\n   - Testing requirements\n   - Deployment procedures\n\n## Resources\n- [Internal Wiki](https://wiki.company.com)\n- [API Documentation](/docs/api)\n- [Architecture Overview](/docs/architecture)\n- [Team Slack Channel](#dev-team)",
       "documentType": "Onboarding",
       "product": "Engineering",
       "team": "Engineering",
       "owner": "hr@company.com",
       "lastUpdated": "2024-01-10T09:00:00.000Z",
       "version": "3.0.0",
       "status": "Approved",
       "tags": ["onboarding", "new-hires", "development", "process"],
       "summary": "Complete onboarding guide for new developers joining the engineering team",
       "audience": "New Hires",
       "priority": "High"
     },
     "relations": {},
     "icon": "FileText",
     "identifier": "dev-onboarding-guide",
     "title": "New Developer Onboarding Guide"
   }
   ```

3. Click `Create` to save the document.

### API Integration for Bulk Import

You can programmatically create documentation entities using Port's API:

Create documentation via API

```
import requests
from datetime import datetime

# Get API token
CLIENT_ID = 'YOUR_CLIENT_ID'
CLIENT_SECRET = 'YOUR_CLIENT_SECRET'
API_URL = 'https://api.port.io/v1'

credentials = {'clientId': CLIENT_ID, 'clientSecret': CLIENT_SECRET}
token_response = requests.post(f'{API_URL}/auth/access_token', json=credentials)
access_token = token_response.json()['accessToken']

headers = {'Authorization': f'Bearer {access_token}'}

# Create API documentation entity
api_doc = {
    "properties": {
        "content": "# User Authentication API\n\n## Overview\nThis API handles user authentication...",
        "documentType": "API Documentation",
        "product": "Authentication Service",
        "team": "Backend Engineering",
        "owner": "john.doe@company.com",
        "lastUpdated": datetime.now().isoformat(),
        "version": "2.1.0",
        "status": "Approved",
        "tags": ["api", "authentication", "jwt"],
        "summary": "Complete API documentation for user authentication endpoints",
        "audience": "Engineering",
        "priority": "High"
    },
    "relations": {},
    "icon": "FileText",
    "identifier": "auth-api-docs-v2",
    "title": "User Authentication API Documentation"
}

# Create the entity
response = requests.post(
    f'{API_URL}/blueprints/internal_docs/entities', 
    json=api_doc, 
    headers=headers
)

if response.status_code == 201:
    print("Documentation entity created successfully!")
else:
    print(f"Error: {response.status_code} - {response.text}")
```

### Webhook Integration for Automatic Updates

Set up a webhook to automatically sync documentation from external systems:

1. Go to [data sources](https://app.getport.io/settings/data-sources).

2. Click `+ Data source` â `Webhook` â `Custom integration`.

3. Configure the webhook mapping:

Documentation Webhook Mapping

```
[
  {
    "blueprint": "internal_docs",
    "operation": "upsert",
    "filter": ".body.event_type == \"document_updated\"",
    "entity": {
      "identifier": ".body.doc_id",
      "title": ".body.title",
      "properties": {
        "content": ".body.content",
        "documentType": ".body.document_type",
        "product": ".body.product",
        "team": ".body.team",
        "owner": ".body.owner",
        "lastUpdated": ".body.updated_at",
        "version": ".body.version",
        "status": ".body.status",
        "tags": ".body.tags",
        "summary": ".body.summary",
        "audience": ".body.audience",
        "priority": ".body.priority"
      }
    }
  }
]
```

### GitHub Integration for markdown files

Another popular use case is documentation being markdown files in a GitHub repo.<br /><!-- -->You can set up a GitHub integration to automatically sync markdown files (excluding README files):

1. Install the [Port GitHub App](https://github.com/apps/getport-io) in your organization.

2. Go to [data sources](https://app.getport.io/settings/data-sources).

3. Under `Exporters`, click on your GitHub organization.

4. Add a file mapping to sync markdown files:

   GitHub integration configuration

   ```
   resources:
   - kind: file
       selector:
       query: '.file.name | contains("README") | not'
       files:
           - path: '**/*.md'
           skipParsing: true
       port:
       entity:
           mappings:
           identifier: .file.path | split("/") | last | split(".") | first
           title: .file.name | split(".") | first | replace("-", " ") | title
           blueprint: '"internal_docs"'
           properties:
               content: .file.content
               documentType: .file.path | split("/") | first | title
               product: .repo.name
               team: .repo.owner.login
               owner: .repo.owner.login + "@company.com"
               lastUpdated: .file.lastModified
               version: .file.sha[0:7]
               status: "Approved"
               tags: 
               - (.file.path | split("/") | first | downcase)
               - "github"
               - "markdown"
               summary: .file.content | split("\n") | first | replace("#", "") | strip
               audience: "All Teams"
               priority: "Medium"
   ```

   Advanced Filtering

   You can customize the `query` field to filter files more specifically:

   * `'.file.name | contains("README") | not'` - Exclude README files
   * `'.file.path | startswith("docs/")'` - Only sync files from docs/ directory
   * `'.file.name | contains("draft") | not'` - Exclude draft files

## Test AI-powered documentation queries[â](#test-ai-powered-documentation-queries "Direct link to Test AI-powered documentation queries")

You can toggle the AI assistant on and off by pressing `Ctrl + I` (or `Command + I` on Mac).

![](/img/guides/port-ai-assistant-interface.png)

Try these example queries to test your AI-powered documentation search:

* "What API documentation do we have in our catalog?"
* "Who owns the authentication API documentation?"
* "What documentation was updated in the last month in our catalog?"
* "Show me all documentation related to the authentication service in our catalog"
* "What critical documentation needs review in our catalog?"

AI Response Behavior

Sometimes, the AI might think you want to query Port technical documentation. In that case, you can instruct it to focus on your internal documentation by adding "in our catalog" or "from our internal documentation" to your prompt to clarify that you're asking about your cataloged entities rather than Port's general documentation.

## Conclusion[â](#conclusion "Direct link to Conclusion")

You've successfully set up a centralized documentation system with AI-powered question answering! Your internal documentation is now searchable through natural language queries, making it easier for team members to find the information they need.

The enhanced blueprint provides rich metadata that enables sophisticated queries about document ownership, updates, categorization, and relationships. This approach can be extended to other types of organizational knowledge and integrated with your existing workflows.

## Next steps[â](#next-steps "Direct link to Next steps")

* **Expand content**: Add more documentation types and examples
* **Integrate workflows**: Connect with your existing documentation tools
* **Monitor usage**: Track which documents are accessed most frequently
* **Iterate**: Refine metadata and content based on AI query patterns
* **Scale**: Consider adding more specialized blueprints for different document types
