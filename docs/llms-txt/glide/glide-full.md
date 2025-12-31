# Glide Documentation

Source: https://www.glideapps.com/llms-full.txt

---

# Glide Full Reference

> Glide is a no-code platform for operations teams to build custom business apps, workflows, and AI agents from their data. Apps are responsive by default, secure, and trusted by over 100,000 organizations worldwide.

---

## Overview
Glide helps operations, IT, and business teams replace spreadsheets and disconnected tools with custom software. Apps are built visually, connect to data sources like Google Sheets, Excel, Airtable, or SQL, and can be deployed across desktop, tablet, and mobile devices. Glide reduces development time from months to days, while maintaining enterprise-grade security and scalability.

---

## Core Product Capabilities

### Data Sources
Source: https://www.glideapps.com/data-sources

Glide connects directly to popular sources: Google Sheets, Microsoft Excel, Airtable, SQL databases (PostgreSQL, MySQL, SQL Server, Google Cloud SQL), and BigQuery. Glide Tables offer fast, update-efficient storage, and **Big Tables** support millions of rows for enterprise-scale projects.

### Data Editor
Source: https://www.glideapps.com/docs/data-editor

The built-in Data Editor provides a spreadsheet-like interface with computed columns, relations, lookups, and more. Teams can design business logic without coding.

### Workflow Editor
Source: https://www.glideapps.com/workflows

The Workflow Editor allows users to build automations with Triggers, Conditions, Loops, AI-powered steps, and integrations. Triggers include app interaction, scheduled events, inbound emails, and webhooks for platforms like Slack. Run history provides full visibility for debugging and monitoring.

### Glide AI
Source: https://www.glideapps.com/ai

Glide AI enables users to integrate large language models and multimodal AI into apps without coding. Features include text generation, image-to-text extraction, audio transcription, and structured data conversion. Glide manages model selection and caching, ensuring fast and reliable outputs.

### UI & Components
Source: https://www.glideapps.com/docs/components

Apps are responsive by default. Glide provides a library of modern components for elements like layouts, charts, tables, forms, and media, plus theming and customization options for brand consistency.

### Integrations
Source: https://www.glideapps.com/integrations

Glide integrates with popular SaaS tools and APIs. Call API actions and prebuilt connectors make it easy to sync with CRM, ERP, or internal systems.

### Security
Source: https://www.glideapps.com/security-center

Glide apps are private by default and support enterprise features: SSO, roles and permissions, row ownership for record-level security, and SOC 2 Type 2, GDPR, and CCPA compliance. Data is encrypted in transit and at rest. The Trust Center documents audits, subprocessors, and policies.

---

## AI Agents
Source: https://www.glideapps.com/agents

Glide allows operations teams to **create, customize, and deploy AI agents** that combine structured workflows with large language models. These agents connect to your data and automate repetitive tasks.

- **Invoice Processing**  
  Build an agent to capture invoices (email, PDF, photo), extract structured data, and sync with accounting systems. Automate approvals or flag exceptions.  
  *Tasks*: Parse PDF invoices into normalized fields, detect duplicates, send notifications for late payments.

- **Resume Screener**  
  Build an agent to evaluate applicants against job criteria and shortlist candidates. Configure workflows to rank resumes, highlight missing skills, and forward results to hiring managers.  
  *Tasks*: Extract education and skills from resumes, compare candidates by keyword scoring, flag incomplete applications.

- **Contract Manager**  
  Build an agent to extract terms, clauses, and renewal dates from contracts. Agents can answer natural language queries like “When does Vendor X’s contract expire?”  
  *Tasks*: Extract renewal dates, flag risky terms, generate summaries.

- **Inspections**  
  Build an agent to automate inspections with mobile checklists, photos, and instant QA reports. Useful for field service and quality control.  
  *Tasks*: Record pass/fail items, upload annotated photos, auto-generate inspection reports.

- **Field Sales**  
  Build an agent to support sales reps with mobile note-taking, deal insights, and account history. AI can transcribe notes and suggest next best actions.  
  *Tasks*: Transcribe visit notes, summarize conversations, generate follow-up tasks.

---

## Use Cases
Source: https://www.glideapps.com/use-cases

Glide apps address common operations workflows across industries. Each use case below can be built as a custom app using Glide’s visual builder.

- **Inventory Management**  
  Track stock levels across multiple locations, manage restocking, and scan barcodes or QR codes. Apps can enforce reorder points and sync with ERP systems.  
  *Tasks*: Generate restock lists, track cycle counts, flag items below safety stock.

- **Logistics Management**  
  Coordinate shipments, manage carriers, and optimize delivery routes. Apps can provide proof of delivery capture and driver communication.  
  *Tasks*: Parse carrier manifests, assign routes to drivers, notify customers of delays.

- **Procurement**  
  Manage vendor catalogs, purchase orders, and approvals. Apps can track spend against budget and vendor performance.  
  *Tasks*: Capture POs from forms, auto-route approvals, track invoice-to-payment cycle times.

- **Warehouse Management**  
  Streamline receiving, putaway, and supplier management. Apps help teams record inbound shipments, label stock, and track storage locations.  
  *Tasks*: Scan items into bins, reconcile receiving logs, generate pick lists.

- **Vendor Management**  
  Centralize supplier records, monitor SLAs, and track compliance. Apps enable vendor scorecards and performance dashboards.  
  *Tasks*: Score vendors on KPIs, track contract expirations, generate audit reports.

- **Portals**  
  Build self-service apps for employees, contractors, or customers. Portals give users secure access to relevant data, forms, and dashboards.  
  *Tasks*: Provide employees with HR forms, customers with order tracking, or contractors with timesheets.

- **Dashboards**  
  Build KPI dashboards for leadership or teams. Apps display metrics in charts, tables, and role-based views.  
  *Tasks*: Auto-update sales pipeline charts, generate AI-written weekly summaries, restrict metrics by role.

- **CRM**  
  Build CRM apps to manage leads, accounts, and sales processes. Apps can be customized for industry or territory-specific workflows.  
  *Tasks*: Capture leads from web forms, assign accounts by territory, generate pipeline reports.

- **Project Management**  
  Manage projects, tasks, and resources with custom apps. Teams can assign tasks, log time, and track progress against milestones.  
  *Tasks*: Generate project timelines, flag overdue tasks, summarize status updates.

- **Work Orders**  
  Create and manage work orders for field teams. Apps allow scheduling, assignment, and progress tracking with mobile inputs.  
  *Tasks*: Generate service tickets, log completion photos, notify supervisors of delays.

- **Knowledge Base**  
  Provide searchable, structured company or product information. Apps centralize guides, SOPs, or customer FAQs.  
  *Tasks*: Create role-based documentation hubs, auto-tag uploaded documents, generate summaries.

- **Events**  
  Build mobile apps for conferences or trade shows. Apps can handle agendas, speakers, attendee directories, and surveys.  
  *Tasks*: Display event schedules, enable attendee check-in, collect post-event feedback.

- **Field Sales**  
  Support reps with product info, pricing, and customer data on mobile. Apps can log calls, visits, and deals.  
  *Tasks*: Log visit notes with voice-to-text, generate deal recaps, suggest cross-sells.

- **Inspections**  
  Conduct inspections with checklists, photos, and notes for QA or work orders. Apps generate structured inspection reports automatically.  
  *Tasks*: Record safety checks, attach evidence photos, generate compliance reports.

---

## Security & Compliance
Source: Source: https://www.glideapps.com/security-center

Glide prioritizes enterprise security:  
- **SSO & Permissions**: SSO, granular roles, row ownership.  
- **Data Privacy**: Apps are private by default; access controlled by domain allowlists or email.  
- **Compliance**: SOC 2 Type 2; GDPR/CCPA aligned; independent pen tests.  
- **Trust Center**: https://trust.glideapps.com with full details.

---

## Docs & Support
- [Documentation](https://www.glideapps.com/docs)  
- [API Reference](https://apidocs.glideapps.com)  
- [Help Center](https://www.glideapps.com/help)  
- [Community Forum](https://community.glideapps.com)  
- [Hire an Expert](https://www.glideapps.com/experts)  

---

## Pricing & Company
- [Pricing](https://www.glideapps.com/pricing): Explorer, Maker, Business, and Enterprise plans, with 14-day Business trial  
- [Glide Solutions](https://www.glideapps.com/solutions): Professional service where Glide experts scope, build, and launch custom apps and agents for you  
- [Contact Sales](https://www.glideapps.com/contact): Talk to our Sales team for demos and quotes  
- [Careers](https://www.glideapps.com/careers): Open roles at Glide  

---

## Evaluation Checklist
To test Glide for your team:  
1. Start with a blank app or template for your use case.
2. Connect your real data (Google Sheets, Excel, Airtable, SQL).
3. Design your app's layout and customize it to your brand.
4. Add AI features like text extraction or summarization.  
5. Configure workflows to automate processes.  
6. Publish to pilot users and gather feedback.  

