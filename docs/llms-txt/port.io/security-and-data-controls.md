# Source: https://docs.port.io/ai-interfaces/port-ai/security-and-data-controls.md

# AI Security and Data Controls

Port is committed to developing AI responsibly, maintaining high standards of data privacy and security across all our AI interfaces. This page addresses common questions about security, data handling, permissions, and controls for Port's AI capabilities.

## Data Access & Permissions[â](#data-access--permissions "Direct link to Data Access & Permissions")

### How does Port AI respect my organization's access controls?[â](#how-does-port-ai-respect-my-organizations-access-controls "Direct link to How does Port AI respect my organization's access controls?")

Port AI strictly respects your organization's existing RBAC (Role-Based Access Control) settings. AI interfaces can only access data that you already have permission to view through Port's standard permissions system. No AI feature bypasses or circumvents your configured access controls.

### What if Port AI shows me data I didn't expect to have access to?[â](#what-if-port-ai-shows-me-data-i-didnt-expect-to-have-access-to "Direct link to What if Port AI shows me data I didn't expect to have access to?")

Port AI only shows data you already have access to through Port's RBAC system. If you see information you didn't expect, it usually means your organization's permissions are broader than intended, not that AI bypassed security controls.

In this case, we recommend reviewing and tightening your RBAC settings to ensure permissions align with your intended access policies.

### Can AI features access data outside of Port?[â](#can-ai-features-access-data-outside-of-port "Direct link to Can AI features access data outside of Port?")

AI can run tools you have permitted it to use. If you build tools that fetch external data outside of Port and Port AI has permission to run them, it will have access to that external data in those cases. This is a useful way to connect AI to external data sources, but should be used with caution and proper security considerations.

## Data Privacy & Retention[â](#data-privacy--retention "Direct link to Data Privacy & Retention")

### What data does Port store from AI interactions?[â](#what-data-does-port-store-from-ai-interactions "Direct link to What data does Port store from AI interactions?")

We store data from your interactions with AI features for up to 30 days. This includes:

* Your prompts and questions
* AI responses and outputs
* Tool execution logs and metadata
* Invocation details and performance metrics

### Why does Port store this interaction data?[â](#why-does-port-store-this-interaction-data "Direct link to Why does Port store this interaction data?")

We use this stored data strictly for:

* Ensuring AI features function correctly
* Identifying and preventing problematic or inappropriate AI behavior
* Performance monitoring and system optimization
* Debugging and troubleshooting issues

We limit data storage strictly to these operational purposes.

### How is my data processed by LLM providers?[â](#how-is-my-data-processed-by-llm-providers "Direct link to How is my data processed by LLM providers?")

All data processing occurs within Port's secure cloud infrastructure. We use different LLM models depending on the AI interface:

* **OpenAI GPT models** for certain AI features
* **Claude models** for enhanced reasoning capabilities

Your data is not used for model training by these providers. We ensure complete logical separation between different customers' data throughout the processing pipeline.

### Can I opt out of data storage?[â](#can-i-opt-out-of-data-storage "Direct link to Can I opt out of data storage?")

Yes, you can contact us to opt out of the 30-day interaction data storage. However, opting out may impact our ability to provide support and troubleshoot issues with AI features.

### Does Port still retain AI interaction data when using bring-your-own LLM?[â](#does-port-still-retain-ai-interaction-data-when-using-bring-your-own-llm "Direct link to Does Port still retain AI interaction data when using bring-your-own LLM?")

Yes, even when bringing your own LLM provider, Port may still retain your AI interaction data for up to 30 days. This data retention supports:

* Monitoring and troubleshooting AI functionality.
* Error analysis and system optimization.
* Improving the overall AI experience.

This data retention is used to monitor and troubleshoot Port's AI services behavior, prompt engineering, and data processing logicâregardless of which LLM provider you choose. This data is not used for model training.

You can request to opt out of this data retention if required by contacting our support team.

## Rate Limits & Usage Controls[â](#rate-limits--usage-controls "Direct link to Rate Limits & Usage Controls")

### What are the current rate limits for AI features?[â](#what-are-the-current-rate-limits-for-ai-features "Direct link to What are the current rate limits for AI features?")

Port AI operates with specific rate limits and monthly quotas to ensure fair usage across all customers.

*Note: These limits apply when using Port's managed AI infrastructure. [Bring your own LLM provider](/ai-interfaces/port-ai/llm-providers-management/overview.md) to use your provider's limits instead.*

For detailed information about current limits, quotas, and monitoring your usage, see the [Limits and Usage section](/ai-interfaces/port-ai/overview.md#limits-and-usage) in the Port AI Overview.

### How can I monitor my current usage?[â](#how-can-i-monitor-my-current-usage "Direct link to How can I monitor my current usage?")

For detailed information about monitoring your AI usage, including API response headers, quota endpoints, and AI invocation records, see the [Limits and Usage section](/ai-interfaces/port-ai/overview.md#limits-and-usage) in the Port AI Overview.

### What happens when I reach a usage limit?[â](#what-happens-when-i-reach-a-usage-limit "Direct link to What happens when I reach a usage limit?")

For detailed information about what happens when you reach usage limits and how to handle them, see the [Frequently Asked Questions](/ai-interfaces/port-ai/overview.md#frequently-asked-questions) in the Port AI Overview.

## Admin Controls & Organization Policies[â](#admin-controls--organization-policies "Direct link to Admin Controls & Organization Policies")

### What controls do administrators have over AI usage?[â](#what-controls-do-administrators-have-over-ai-usage "Direct link to What controls do administrators have over AI usage?")

Organization administrators can:

* Control access to AI features through existing Port RBAC settings
* Monitor AI usage through audit logs and invocation records
* Review all AI interactions through the AI invocations catalog
* Export audit logs for compliance and analysis
* Configure organization-wide policies for AI feature access

### Can we control which users have access to AI features?[â](#can-we-control-which-users-have-access-to-ai-features "Direct link to Can we control which users have access to AI features?")

Yes, AI feature access is controlled through Port's standard RBAC system. Administrators can manage access by configuring permissions for the AI invocation blueprint, which determines which users can interact with Port AI. For more details, see the [Security and Permissions section](/ai-interfaces/port-ai/overview.md#security-and-permissions) in the Port AI Overview.

### Are there organization-level vs user-level controls?[â](#are-there-organization-level-vs-user-level-controls "Direct link to Are there organization-level vs user-level controls?")

AI access controls operate at both levels:

* **Organization-level:** Overall AI feature enablement and policy settings
* **User-level:** Individual access permissions based on roles and configured RBAC rules

## Human Oversight & Autonomy[â](#human-oversight--autonomy "Direct link to Human Oversight & Autonomy")

### Do AI features act autonomously without human oversight?[â](#do-ai-features-act-autonomously-without-human-oversight "Direct link to Do AI features act autonomously without human oversight?")

AI features in Port operate with different levels of autonomy depending on configuration:

**Query responses:** AI can autonomously read and analyze your Port data to answer questions **Action execution:** You can configure whether AI can execute actions automatically or requires human approval before execution

For actions with significant impact, we recommend requiring human approval.

### What human oversight exists for AI actions?[â](#what-human-oversight-exists-for-ai-actions "Direct link to What human oversight exists for AI actions?")

* All AI interactions create detailed audit trails
* Action execution can be configured to require human approval
* Organization administrators can monitor all AI activity
* Users can review AI reasoning and tool usage for each interaction

### What visibility do customers have into AI usage?[â](#what-visibility-do-customers-have-into-ai-usage "Direct link to What visibility do customers have into AI usage?")

Comprehensive visibility is provided through:

* **AI invocation records:** Every interaction creates a detailed log
* **Audit trails:** Complete history of AI usage across your organization
* **Tool execution logs:** See exactly which tools AI used and why
* **Performance metrics:** Token usage, response times, and error rates
* **Admin dashboards:** Organization-wide usage monitoring

## Opt-out & User Controls[â](#opt-out--user-controls "Direct link to Opt-out & User Controls")

### Can we opt out of AI features entirely?[â](#can-we-opt-out-of-ai-features-entirely "Direct link to Can we opt out of AI features entirely?")

Yes, you can contact our support team to opt out of AI features for your organization.

### Can individual users opt out of specific AI features?[â](#can-individual-users-opt-out-of-specific-ai-features "Direct link to Can individual users opt out of specific AI features?")

Users cannot individually opt out of AI features that are enabled organization-wide, but administrators can use RBAC controls to restrict access for specific users or roles.

### Can we opt out of data storage while keeping AI functionality?[â](#can-we-opt-out-of-data-storage-while-keeping-ai-functionality "Direct link to Can we opt out of data storage while keeping AI functionality?")

You can opt out of the 30-day interaction data storage by contacting our support team. However, this may impact our ability to provide support and troubleshoot issues with AI features.

## Performance & Expectations[â](#performance--expectations "Direct link to Performance & Expectations")

### What are normal response times for AI features?[â](#what-are-normal-response-times-for-ai-features "Direct link to What are normal response times for AI features?")

AI features typically start streaming responses within 5 seconds and complete within 30 seconds, depending on:

* Complexity of the query or request
* Amount of data being analyzed
* Current system load
* Which AI interface is being used

Response times may occasionally be longer as we optimize performance. This is expected behavior and will improve over time.

### What should I do if AI responses seem slow?[â](#what-should-i-do-if-ai-responses-seem-slow "Direct link to What should I do if AI responses seem slow?")

Response times up to 30 seconds are normal and expected for AI processing. If you experience consistently longer response times:

* Check the AI invocation details for any errors
* Verify your usage hasn't hit rate limits
* Contact support if problems persist

## Compliance & Security Standards[â](#compliance--security-standards "Direct link to Compliance & Security Standards")

### How does this integrate with our existing compliance requirements?[â](#how-does-this-integrate-with-our-existing-compliance-requirements "Direct link to How does this integrate with our existing compliance requirements?")

Port AI features respect your existing data governance and compliance policies:

* All interactions are logged for audit purposes
* RBAC controls ensure data access follows your defined policies
* Data retention policies can be configured to meet your compliance needs
* Export capabilities support compliance reporting requirements

For detailed information about Port's security standards, certifications, and compliance frameworks (SOC2, GDPR, ISO 27001, etc.), see [Port's Security page](https://www.port.io/security).

## Troubleshooting & Support[â](#troubleshooting--support "Direct link to Troubleshooting & Support")

### What if AI gives incorrect answers?[â](#what-if-ai-gives-incorrect-answers "Direct link to What if AI gives incorrect answers?")

AI can make mistakes. If you receive incorrect answers:

1. Review the AI invocation details to see which tools were used
2. Check if the AI used incorrect field names or properties
3. Try rephrasing your question or breaking it into smaller queries
4. Provide feedback through the AI invocation record
5. Contact support if problems persist

Remember that AI features are continuously improving, but they are not infallible.

### How can I provide feedback on AI responses?[â](#how-can-i-provide-feedback-on-ai-responses "Direct link to How can I provide feedback on AI responses?")

For feedback on AI responses or to report issues, contact our support team directly.

### Who should I contact for AI-related security concerns?[â](#who-should-i-contact-for-ai-related-security-concerns "Direct link to Who should I contact for AI-related security concerns?")

For any security-related questions or concerns about AI features, contact our support team directly. We take security concerns seriously and will respond promptly to address any issues.
