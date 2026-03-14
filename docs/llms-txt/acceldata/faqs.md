# Source: https://docs.acceldata.io/documentation/faqs.md

# FAQs

**Q: How do I get started with ADM?** 

A: Navigate to your organization's ADM URL, log in, and type a simple question in the chat window. Try asking "Show me my data quality policies" or use the recommended questions in the starter pane.

**Q: Can ADM modify my data?** 

A: No. ADM primarily reads and analyzes data. It can create policies and configurations but requires your approval before making any changes to your data systems.

**Q: How does ADM maintain context in conversations?** 

A: ADM maintains context using conversation history, user profile, knowledge base documents, and current system state. Each message builds on previous exchanges in the same conversation.

**Q: What happens to my conversation history?** 

A: Conversations are stored securely and can be accessed anytime from your history. You can delete conversations, and they're retained according to your organization's data retention policy.

**Q: Can I use ADM offline?** 

A: No. ADM requires an internet connection to function as it relies on cloud-based AI services and access to your data catalog.

**Q: How do I share a conversation with my team?** 

A: Click the "Share" button in any conversation, search for users, select permission levels, and click "Share". Recipients will see the conversation in their history.

**Q: What file formats can I upload to the Knowledge Base?** 

A: Fully supported: PDF, Word (doc/docx), Text (txt), Markdown (md), Excel (xls/xlsx). Partially supported: PowerPoint (pptx), JSON, XML.

**Q: How long does document indexing take?** 

A: Small documents (&lt; 10 pages): 30-60 seconds. Medium (10-50 pages): 1-3 minutes. Large (50+ pages): 3-10 minutes.

**Q: Can I schedule notebooks to run automatically?** 

A: Yes. Open any notebook, click "Schedule", configure frequency and time, select notification group, and enable the schedule.

**Q: What's the difference between a conversation and a notebook?** 

A: Conversations are interactive Q&A sessions. Notebooks are collections of fixed queries that can be scheduled for regular execution and produce structured results.

**Q: How do I connect Google Drive to ADM?** 

A: Go to Settings &gt; Integrations &gt; MCP Servers, find "Google Drive MCP", click "Enable", authenticate with your Google account, and grant permissions.

**Q: Can I use my own LLM instead of the default?** 

A: Yes, if your organization enables BYO LLM. Go to Settings &gt; LLM Configuration, add your provider, enter connection details, and test the connection.

**Q: How do I create a data quality policy?** 

A: Use the Data Quality Policy Creation workflow. Type your requirements (e.g., "Create a policy to validate customer emails"), review AI-generated rules, modify as needed, and save.

**Q: What does a policy score mean?** 

A: Policy score = (Passed Rules / Total Rules) × 100. Scores above 95% are excellent, 85-94% are good, and below 85% need attention.

**Q: How do I troubleshoot a failed workflow?** 

A: Open the workflow run, identify the failed step, review error messages, check step details, and retry with modifications or contact support.

**Q: Can multiple people work on the same conversation?** 

A: Yes. Share the conversation with team members, and all can view and contribute. Use @adm to query the AI in group conversations.

**Q: How secure is my data in ADM?** 

A: ADM uses multi-tenant architecture with row-level security, AES-256 encryption, TLS 1.3 for transit, and complies with SOC 2, GDPR, and optionally HIPAA.

**Q: Can I export conversations?** 

A: Yes. Click "Download as PDF" in any conversation to export the complete conversation with formatting, timestamps, and thought processes.

**Q: How do I get help if I'm stuck?** 

A: Type 'help' or Check this documentation, search the Knowledge Base, ask CS team members, or contact support at [support@acceldata.io](mailto:support@acceldata.io).