# Source: https://docs.xano.com/updates.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# What's New

> What's new in Xano -- Release Notes, Announcements, and Documentation Updates

<Update label="v2.02.2 - Patch" description="March 2, 2026">
  * **Tenant Center:** Added a tenant list to the workspace overview page, making it easy to see which tenants are associated with each workspace. This view respects existing access controls, filtering out workspaces you don't have permission to view — consistent with how Audit Logs work.
  * **XanoScript:**
    * Improved performance when processing large base64-encoded inline images within XanoScript.
    * Object value settings now handle plus signs (+) as expected, ensuring configurations save and execute reliably.
  * **Reliability & Quality:**
    * Column visibility settings now persist as expected after editing a table's schema via XanoScript, ensuring Hidden columns remain hidden.
    * Improved the Tenant Impersonation experience: the exit button is now correctly labeled "Stop Impersonating" and returns users cleanly without errors.
    * Environment variables can now be created and updated via the API, in addition to being read.
    * Tenant Swagger API endpoints now return results reliably when valid data is present.
    * Metadata tokens scoped to tenantcenter:backup now grant access to the backup endpoint as expected.
</Update>

<Update label="v2.02.1 - Patch" description="February 26, 2026">
  * **Tasks:** Improvements to task debugging with new support for task process PID and memory usage.
  * **Metadata API:** Resolved scenarios where Metadata API tokens were unable to grant proper access to backup resources.
  * **RBAC:**
    * Resolved an issue that could cause users with update, read, and create permissions to be unable to perform bulk edits on environment variables in workspace settings and tenant environment variable panels.
    * Resolved an inconsistency with new permissions on Activate Run & Debug from Request History.
  * **Run & Debug:** Improved handling of sensitive fields in logging.
  * **Database:** Resolved an issue where a failed unique index creation was still being applied to the table.
  * **Tenant Center:** Resolved an issue where changing a function to async was not being reflected when comparing two releases in the Tenant Center.
  * **Webflow Plugin:** Improved stability for the Webflow Plugin.
</Update>

<Update label="v2.2 - Release" description="February 24, 2026">
  * **Snowflake Integration**: Added native Snowflake [direct query](/the-function-stack/functions/database-requests/external-database-query) support, enabling users to run queries against Snowflake data warehouses directly within Xano's function stack alongside existing database connectors.
  * **[Instance Down Alerting](/troubleshooting-and-support/my-instance-is-down#instance-down-alerting):** Introduced automated email alerts to notify instance administrators when downtime is detected, including recommended resolution steps such as [hard restarts](/the-database/database-performance-and-maintenance/maintenance#server-maintenance), storage expansion, and plan upgrades.
  * **Run and Debug from [Request History](/maintenance-monitoring-and-logging/request-history):** Added the ability to open any past API call from the Request History directly in [Run & Debug](/testing-debugging/testing-and-debugging-function-stacks), with inputs pre-populated from the original request.
  * **[Tenant](/enterprise/enterprise-features/tenant-center) Proxy Support:** Introduced proxy URL configuration for tenant environments, allowing requests to be forwarded from an existing tenant URL to a new one. This simplifies tenant migrations by removing the urgency of immediate URL cutover, with minimal additional latency added during the transition period.
  * **Connection String Variable and Filter Support:** Enabled variables and filters to be used within connection string fields for [External MySQL, PostgreSQL, and Oracle Query](/the-function-stack/functions/database-requests/external-database-query) statements, replacing the previous requirement to hard-code connection strings as string literals.
  * **[XanoScript](/xanoscript/introduction):** Delivered ongoing enhancements and stability improvements across the scripting engine.
  * **[VS Code Extension](/xanoscript/vs-code):** Implemented performance improvements and resolved various bugs. [Change Logs](https://marketplace.visualstudio.com/items/xano.xanoscript/changelog)
  * **UX Enhancements:**
    * **New Onboarding Experience:** Introducing a revamped onboarding experience for new users that streamlines the process of [starting to build](/before-you-begin/where-should-i-start) in Xano.
    * **[RBAC](/team-collaboration/role-based-access-control-rbac) UI Enhancements:** Delivered comprehensive improvements to the Permissions page, including multi-select filter dropdowns for Members, Roles, and Workspaces with removable chips and a clear-all option. Wizard flows for managing team roles, cloning permissions, and bulk management now include search inputs with filter pass-through.
</Update>

<Update label="v2.1.3 - Release" description="January 21, 2026">
  * [Tenant Center](/enterprise/enterprise-features/tenant-center): A centralized way to create and manage multiple tenants with data, resource, and regional isolation as needed —making it easy to support CI/CD workflows, customer-level isolation, controlled releases, and data residency requirements. Available with Custom Plans.
  * Essential plan: A new entry plan for building and running serious, production-grade apps and agents on Xano.
  * XanoScript: Delivered ongoing enhancements and stability improvements across the scripting engine.
  * VS Code Extension: Implemented performance improvements and resolved various bugs. Change Logs
</Update>

<Update label="v2.01.2 - Patch" description="December 19, 2025">
  * Performance Fix: resolved issue with certain tasks using increased amounts of CPU resources
  * XanoScript: Bug fixes for using ternary operators within filter arguments
  * Dot Notation: Bug fix - regression with inline dot notation using asterisk characters
</Update>

<Update label="v2.01.1 - Patch" description="December 16, 2025">
  * GitHub Sync: Added support for syncing Workflow Tests to GitHub.
  * XanoScript: Delivered continued improvements and bug fixes.
  * Performance and Reliability: Bug fixes and improvements to ensure better performance and reliability for all plans.
</Update>

<Update label="v2.01 - Release" description="December 11, 2025">
  * Performance Improvements: Improved execution speed for async functions, triggers, expressions, and loops across all plans.
  * Agent OpenTelemetry Integration: Added support for connecting AI agents to Braintrust, Langfuse, and LangSmith for enhanced observability.
  * Swagger Documentation Updates: Enabled export of Swagger documentation for all API groups in a single consolidated document. Enabled export of a single endpoint’s Swagger documentation. Added an option to minify Swagger examples by removing additional examples and shortening long strings, reducing token usage for LLM workflows.
  * AI Commit Messages: Added automatic and on-demand generation of AI-powered commit messages when publishing business logic changes.
  * XanoScript: Delivered ongoing enhancements and stability improvements across the scripting engine.
  * VS Code Extension: Implemented performance improvements and resolved various bugs. Change Logs
  * UX Enhancements:
    * Added searchable field types to streamline adding input fields and table fields, including searchable subpaths and response values.
    * Improved API History performance on the Dashboard.
    * Enhanced Database Assistant to make CRUD endpoint creation and test data generation more accessible.
    * Improved Agent detail pages with easier API connection creation and refined Call AI Agent statement linking from the Function Stack and Canvas.
    * Added support for creating new Custom Functions directly from the Function Stack or Canvas.
    * Enhanced search within Performance Insights. Learn more about Performance Insights.
    * Added individual Swagger documentation links for each object.
</Update>

<Update label="v2.00.4 - Patch" description="November 11, 2025">
  * Tenant Center Enhancements: Restricted read-only user access to secrets and clusters. Updated resource management UI to conditionally show tolerations. Enabled copying environment variables from workspaces during tenant creation.
  * Database and Migration Improvements: Fixed SQL rename conflicts by scoping checks to public schema. Resolved migration failures from free to paid plans due to missing AI toolsets. Ensured nullable list children return null instead of empty arrays.
  * AI and Logic Assistant Fixes: Added UX warnings for large stacks exceeding token limits. Prevented query reference loss after updates.
  * XanoScript Improvements: Ensured AI-generated auth applies correctly without resets. Fixed lock removal on db.query saves and prevented multiline value spacing accumulation. Supported bulk add/patch/update/delete operations fully.
  * Language Server Updates: Resolved issues with filter\_zero/false, vector inputs, async agent settings, run tools, QAR sorting/output locks, and get record locks. Fixed bulk statements, action additions, and workflow expect to throw.
  * MCP and Tools Fixes: Eliminated 500 errors on simple tool executions and ensured XanoScript returns properly in update triggers. Enforced authentication for all tools. Fixed "Call AI Agent" errors if agent deleted.
  * UI Enhancements: Made function folder breadcrumbs clickable and list items new-tab compatible. Restored step numbers in function stacks and spaced horizontal scrolls from Add Record buttons.
  * Static Hosting Fixes: Resolved upload failures for filenames with spaces and Windows zip path inconsistencies (unix/path vs windows\path).
  * Swagger and Endpoint Resolutions: Fixed blueprint rows errors blocking Swagger when moving queries. Made disabled API group icons open settings with tooltips.
  * Query Wizard and Misc Fixes: Fixed TypeErrors on AWS search payload updates. Corrected table "referenced by" listings and precondition sidebar closures.
</Update>

<Update label="v2.00.3 - Patch" description="October 31, 2025">
  * RBAC Permissions Fixes: Resolved custom role permissions reverting for realtime and workflow features, plus access denied errors when adding environment variables. Restored toast notifications for all permission updates.
  * Metadata API Enhancements: Fixed errors in the mcp\_server/trigger endpoint when no triggers exist.
  * UI and Panel Improvements: Fixed panel closure for long variable values and added loading indicators for panel resizing in XanoScript. Resolved layout issues in heavy function stacks, including text wrapping in conditionals and missing step numbers.
  * XanoScript Fixes: Corrected expression changes after saving, including multiline and regex issues, plus nested objects reverting in edits. Supported multiline arrays, allowed leading underscores in variables.
  * Language Server Fixes: Resolved issues with cache increments, external API follow\_location flags, env:tenant additions, and direct\_query support.
  * Tenant Management Improvements: Enabled task history viewing in tenants. Added environment variable copying from workspaces during tenant creation. Fixed performance insights display and profiler cleanup in tenants.
  * AI and Agents Fixes: Resolved prompt parsing errors causing unknown run issues and added agent version control in XanoScript. Fixed Logic Assistant execution failures for simple commands.
  * Static Hosting Fixes: Resolved inability to save edited descriptions for static sites.
  * Function Stack and Canvas Enhancements: Improved truncation for long expressions and highlighted "Add Function" buttons in empty stacks. Auto-opened editors for new comments and reduced prominence of 'add else if' conditions. Tightened add function search to exclude irrelevant results and fixed nested property edits plus array operation errors.
  * Expression Editor Fixes: Resolved layout issues on resize. Improved error messages for variable naming and enabled Cmd+K shortcuts for search from the editor.
  * Profiler Enhancements: Fixed logging omissions in async functions.
</Update>

<Update label="v2.00.2 - Patch" description="October 27, 2025">
  * Middleware Fixes: Resolved an issue preventing middleware references from appearing in XanoScript on branches via the Metadata API. Fixed a bug where editing and saving XanoScript disrupted middleware execution, necessitating removal and re-addition to restore it. Corrected a linting error displaying a red line for get\_raw\_input in XanoScript. Addressed debugger errors in API endpoint debugging with multiple middlewares.
  * XanoScript addon Update: Updated to use an array of objects for describing query add-ons, resolving issues with add-ons applied at the root of the query output.
  * Tenant Features Enhancements: Added support for the \$tenant environment variable to enable tenant-specific configurations, and introduced the ability to disable tasks for individual tenants, offering greater operational control.
  * MCP Tools Listing Error Fix: Fixed errors in mcp\_list\_tools for SSE and stream modes, ensuring reliable tool listing.
  * Merge Branch Error Handling Improvement: Enhanced error handling during branch merges for clearer and more informative messages.
  * Publish Now Loading Indicator: Added a loading indicator to the "Publish Now" button to show progress during quick publishes.
  * Canvas Auto Layout Fix: Resolved an issue where the auto layout button in the Canvas view was not reorganizing workflow elements properly.
  * Panel Resizing Delay Fix: Resolved a delay and UI disruption when resizing panels with loaded XanoScript.
</Update>

<Update label="v2.00.1 - Patch" description="October 24, 2025">
  * Release #22540
  * Merge Dependency Option Fix: Resolved an issue where the auto-include dependency option was not visible during merges.
  * Tenant Release Field Fix: Fixed a bug causing the tenant release field to empty after editing tenant settings.
  * Billing Support Option Update: Removed the Priority Support option from Pro and Scale user plans for accurate billing representation.
  * Search and Folder Icons Display Fix: Adjusted search and folder icons to span full width on wide monitors, improving UI consistency.
  * Function Stack Performance Optimization: Addressed performance issues caused by large inline static variables in the function stack.
  * Database Backup Reliability Fix: Resolved inconsistencies in automatic database backups to ensure reliable completion.
  * AI Tool References Navigation Fix: Fixed a navigation error where clicking AI Tool References in tables led to non-existent pages.
  * Column Name Search Criteria Clarification: Clarified and fixed search criteria for column name matching to improve accuracy.
  * Static Hosts and Resources Deletion API: Introduced a new API for deleting static hosts and resources, enhancing management capabilities.
  * Compliance Center Agent Triggers Update: Added a dedicated section for agent triggers in the Compliance Center, separating them from server triggers.
  * Hover Value Display Regression Fix: Fixed a regression where hover-over values on statements were missing on the left side.
</Update>

<Update label="v2.0 - Release" description="October 22, 2025">
  * XanoScript \[Beta]: Introduced XanoScript, a scripting language for backend data and logic. Features include a text editor, UI, language server, packaged actions, and bug fixes for enhanced developer productivity.
  * Visual Canvas: Launched a node-based visual data flow editor for constructing workflows with operators, dependencies, and decision logic in a graphical interface.
  * Logic Assistant \[Beta]: Released the Logic Assistant with chatbot UX, enabling users to describe logic in plain language for AI-generated XanoScript code. Improved prompt iteration.
  * VS Code Extension: Added a native Visual Studio Code extension for direct Xano backend connection, account creation, and IDE integration (VS Code, Cursor, Windsurf). Includes instructions for leveraging IDE-integrated LLMs (Copilot, etc.) to accelerate backend development with AI guidance.
  * Metadata API & MCP Logic Layer Support: Enhanced Metadata API and MCP Server to support backend building outside Xano using preferred IDEs or AI tools.
  * XanoScript Diff Experience: Implemented a Git-style diff viewer to compare backend changes before publishing, merging, deploying, or reverting.
  * Expanded Starter Template for New Users: Upgraded onboarding with core tables, new send email statement, expanded auth API endpoints (including reset password flow), event logging APIs, and an example Agent chatbot.
  * Agents Free Credits: Provided limited free Gemini credits via a test key per workspace, allowing new users to try Agents without external API keys.
  * Frontend Static Hosting Deployment: Enabled deployment of frontend static hosting, integrated with VS Code Extension for frontend code syncing.
  * Git Sync Integration: Added one-way push to export workspace as XanoScript to a Git repository upon publish, and frontend sync to pull code from a selected Git repository and deploy to Static Hosting.
  * Lambda Functions Private NPM Support: Introduced authentication for private NPM registries via query parameters or environment variables for seamless package installation.
</Update>

<Update label="v1.70.4 - Patch" description="September 30, 2025">
  * AI Workspace Generation Fix: Resolved an issue preventing workspace generation through AI in staging and production environments.
  * Connection Pool Disable Support: Added support to disable connection pooling via license configuration for enhanced flexibility.
  * UUID Filter Error Fix: Corrected errors in the "Filter" feature when using UUID and UUIDv7 fields.
  * Action Publishing Regression Fix: Fixed a regression causing errors during action publishing.
  * Endpoint Timeout Resolution: Addressed customer endpoint timeouts triggered during horizontal pod autoscaling.
  * Workflow Test Method Display Fix: Corrected an issue where GET endpoints displayed as POST methods in workflow tests.
</Update>

<Update label="v1.70.3 - Patch" description="September 18, 2025">
  * Middleware Audit Logs Fix: Middleware creation are now properly captured in audit logs.
  * MCP Server Stability: Resolved frequent error responses from Xano MCP server.
  * Updated MCP SDK to version [1.17.5](https://www.npmjs.com/package/@modelcontextprotocol/sdk/v/1.17.5).
  * Middleware Merge Fixes: Corrected issues with branch settings and “referenced by” references.
  * Release Track Date Fix: Fixed incorrect dates displayed in the release track timeline.
  * Database Security: Addressed a potential XSS vulnerability in the database interface.
  * Branch Merge Error Fix: Resolved a `map is not a function` error during branch merges.
  * MCP Streaming Fix: Fixed SSE/Stream errors when running MCP tools.
  * Agent Prompt Editor Fix: Structured Output configurations are no longer deleted when prompts are updated.
  * API Example Response Fix: Corrected “Set Example Response” application.
  * Redis Usage Optimization: Reduced excessive Redis usage and bandwidth.
  * Performance Insights Improvement: Reduced Redis memory usage (old history deleted due to new data format).
  * Async/Await Fix: `await` statement now works properly with tenants.
  * Tenant XDO/SQL Fix: Automatic migration from XDO to SQL during tenant deploy.
  * Tenant Deployment Message: Error message now shown when tenant deploy fails.
  * Triggers Improvements: Backend fixes to improve performance and reliability.
</Update>

<Update label="v1.70.2 - Patch" description="August 28, 2025">
  * Performance Insights: Backend optimization, large loop UI tracking, console error fixes.
  * Metadata API: Added tenant-level read-safe endpoints, column fix, schema guardrails.
  * Vector Index Fix: Resolved insert errors on embedding columns.
  * Database Triggers Fix: Prevented double trigger execution.
  * Instance Activity Chart: Added 1-minute increments for charts under 24h.
  * Nullable Values Deployment Fix: Corrected issues deploying nullable values to tenant/datasource configs.
  * Database Version History Fix: Fixed “Invalid name” errors when restoring versions.
  * Downgrade Stability Fix: Prevented repeated failures during plan downgrades.
  * Middleware Input Fix: Multiple endpoint inputs now appear correctly.
</Update>

<Update label="v1.70.1 - Patch" description="August 20, 2025">
  * HDS Compliance Add-on (Paid Upgrade): Ensures confidentiality and localization of health data.
  * Tenant Management: Deploy timestamps, clearing records fix, impersonation access fixes, request history permission fixes.
  * Query/Index Fixes: Resolved errors with `rank eval`, vector index errors, and database recovery vector queries.
  * Agent System Prompt Settings: Prevented API key/model reset when updating system prompts.
  * Database Trigger Execution Fix on certain tables.
  * Database Assistant Button Fix in lower-right corner.
  * Snippets Loading Fix on home page and multi-branch workspaces.
  * Audit Logs Fix for server/agent summaries.
  * Workflow Test Error Fix (500 fatal error).
  * Performance Insights UI Flicker Fix.
  * Upgrade MCP SDK to version [1.15.1](https://www.npmjs.com/package/@modelcontextprotocol/sdk/v/1.15.1).
</Update>

<Update label="v1.70 - Release" description="August 12, 2025">
  * Performance Insights: [Identify slow operations](https://docs.xano.com/maintenance-monitoring-and-logging/performance-insights).
  * Audit Logs (GA): [Clear, searchable user-level logs](https://docs.xano.com/xano-features/workspace-settings/audit-logs).
  * Agents Improvements: Added Call Tool, triggers, context/messages, snippets support, and UX updates.
  * Data Transform Statements: Array Map, Partition, Group By, Difference, Intersection, and Union.
  * Switzerland Data Center Region added.
  * Descriptions for IF/ELSE blocks in conditional statements.
  * Default Payment Method Fix.
  * Snippet Installation Fix.
  * Environment Variable References visibility added.
</Update>

<Update label="v1.69.4 - Patch" description="July 24, 2025">
  * Task Execution with Add-ons Fix.
  * Request History Maintenance Fix for enterprise instances.
  * Playground Modals Stability Fix.
  * Bulk Add for Case Table Fix.
</Update>

<Update label="v1.69.3 - Patch" description="July 16, 2025">
  * Function Publishing Selection Fix.
  * Function Stack UI Rendering Fix.
  * Xano Expressions UI Fix with template engine statements.
</Update>

<Update label="v1.69.2 - Patch" description="July 15, 2025">
  * Run & Debug Freeze Fix.
  * Tenant Center Visual Bug Fix.
  * Storage Calculation Display Fix.
  * Query All Sorting Fix.
  * Table Content Export/Import Fix.
  * Agent Version History Fix.
  * Geo Field Query Fix.
</Update>

<Update label="v1.69.1 - Patch" description="July 2, 2025">
  * Instance Upgrade Error Fix.
  * Coupon Removal Fix.
  * Billing Page Navigation Improvement.
  * Workspace Cloning Fix.
  * Workspace Import/Export Fix.
  * MCP Trigger Navigation and Visibility Fixes.
  * Build Account Trigger Access Fix.
  * Non-Nullable Column Error Fix.
  * Query Result in Conditional Fix.
</Update>

<Update label="v1.69 - Release" description="July 1, 2025">
  * New Pricing Plans: Starter and Pro plans plus updated Launch & Scale plans.
  * AI Agents and Tools launch for reusable AI capabilities.
  * Database Setup Shortcuts for tables and sample data.
  * Global Workspace Statement Search Enhancement.
  * Autocomplete Improvements for database fields.
  * Task Frequency Display.
  * Action Search Fix.
  * Null Date Handling Fix.
  * Enterprise Multi-Tenancy Fixes.
</Update>


Built with [Mintlify](https://mintlify.com).