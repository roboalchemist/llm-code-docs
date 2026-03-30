# Source: https://www.comet.com/docs/opik/integrations/flowise.mdx

***

description: >-
Start here to integrate Opik into your Flowise-based genai application for
end-to-end LLM observability, unit testing, and optimization.
headline: Flowise | Opik Documentation
'og:description': >-
Create AI agents using Flowise's drag-and-drop interface. Leverage Opik to
analyze chatflows and enhance user experiences effectively.
'og:site\_name': Opik Documentation
'og:title': Build AI Workflows with Opik - Flowise
title: Observability for Flowise with Opik
------------------------------------------

Flowise AI is a visual LLM builder that allows you to create AI agents and workflows through a drag-and-drop interface. With Opik integration, you can analyze and troubleshoot your chatflows and agentflows to improve performance and user experience.

<Tip>
  This is a native UI integration that works directly within the Flowise AI interface. No Python code is required to set
  up the integration.
</Tip>

## Overview

Flowise AI provides a visual interface for building AI applications, and Opik integration enables comprehensive analytics and monitoring of your AI workflows. This integration allows you to track performance metrics, monitor user interactions, and analyze conversation flows directly from the Flowise AI interface.

## Setup Instructions

### 1. Access Configuration

1. At the top right corner of your Chatflow or Agentflow, click **Settings** > **Configuration**

2. Navigate to the **Analyse Chatflow** section

   ![Flowise Analytics Section](https://files.buildwithfern.com/https://opik.docs.buildwithfern.com/docs/opik/df28318f32a8a398c59ac54fe0f347092a365a8e52a1f7409d4ac3eee065b841/img/tracing/flowise/analytic-2.png)

3. You will see a list of analytics providers, including Opik

### 2. Configure Opik Integration

1. Click on **Opik** from the list of analytics providers

2. Create credentials for Opik:

   * **API Key**: Your Opik API key (obtain from your Opik workspace)
   * **Workspace**: Your Opik workspace name
   * **Project**: Your Opik project name
   * **Server URL**: Your Opik server URL (if using self-hosted)

   ![Opik Configuration Fields](https://files.buildwithfern.com/https://opik.docs.buildwithfern.com/docs/opik/54987f34d1278623a695806e470751d29eff4b90e785c2787492336c2938960a/img/tracing/flowise/opik-1.png)

3. Fill in other configuration details as required

4. Turn the provider **ON**

   ![Analytics Providers Enabled](https://files.buildwithfern.com/https://opik.docs.buildwithfern.com/docs/opik/9d2ba0290375fa2c5dd1c23e22518cdc95c045d7f6ef70bb88da831aaaa73957/img/tracing/flowise/opik-2.png)

   ![Analytics Configuration Complete](https://files.buildwithfern.com/https://opik.docs.buildwithfern.com/docs/opik/dea749bbd679caecc2180fe32fe33d7c9bfb8b9d53a76c7028c53473fb3579b2/img/tracing/flowise/opik-3.png)

### 3. Verify Integration

Once configured, you can analyze your chatflows and agentflows using the Opik UI dashboard. The integration will automatically start tracking:

* User interactions
* Agent responses
* Performance metrics
* Error rates
* Conversation flows

![Opik UI Dashboard](https://files.buildwithfern.com/https://opik.docs.buildwithfern.com/docs/opik/746369a804e37f5b9f9b93398d31a2cab6f3ea89e35f23d6b7fce5287dfe9479/img/tracing/flowise/opik-4.png)

## What Gets Tracked

When you enable the Opik integration in Flowise AI, the following data is automatically captured:

* **Chatflow/Agentflow executions**: Complete workflow runs with inputs and outputs
* **User interactions**: All user messages and system responses
* **Performance metrics**: Response times and execution durations
* **Error tracking**: Any failures or exceptions during execution
* **Conversation context**: Full conversation history and flow state

## Viewing Data in Opik

After setting up the integration, you can view your Flowise AI data in the Opik dashboard:

1. **Traces**: Each chatflow or agentflow execution creates a trace
2. **Spans**: Individual steps and interactions within workflows
3. **Metrics**: Performance and usage statistics
4. **Feedback**: Manual annotations and evaluations

## Next Steps

After setting up the Flowise AI integration:

1. **Test the Integration**: Run a few test chatflows to verify data is being captured
2. **Explore Analytics**: Use the Opik dashboard to analyze your workflow performance
3. **Set Up Monitoring**: Configure alerts for performance issues or errors
4. **Optimize Workflows**: Use insights to improve your AI applications

## Getting Help

If you encounter issues with the Flowise AI integration:

1. Check the [Opik documentation](/tracing/concepts)
2. Review [Flowise AI documentation](https://docs.flowiseai.com)
3. Contact Opik support for technical assistance

The Flowise AI integration with Opik provides powerful analytics capabilities to help you build, monitor, and optimize your AI applications effectively.
