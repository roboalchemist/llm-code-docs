# Source: https://docs.lunary.ai/docs/features/prompt-playground.md

# Prompt Playground

The Prompt Playground is an interactive environment for testing and refining your prompts. It provides a powerful interface to experiment with different prompt variations, test against various models, and even run prompts against custom API endpoints.

## Overview

The Prompt Playground allows you to:

* Test prompts with different LLM providers (OpenAI, Anthropic, etc.)
* Compare outputs across multiple models
* Experiment with parameters like temperature and max tokens
* Test prompts against your own custom API endpoints
* Save and collaborate on prompt experiments with team members
* Create draft versions without affecting production (RBAC ensures only authorized users can deploy)

<img src="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/1.png?fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=06c8964263612f54c373da2d7faac05c" alt="Image 1" data-og-width="3054" width="3054" data-og-height="1982" height="1982" data-path="media/docs/prompt-playground/1.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/1.png?w=280&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=332600b3c150836e02da4f6a060a057d 280w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/1.png?w=560&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=df7e3ded9643512c262ab9ef1f9a77a4 560w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/1.png?w=840&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=46e0b943de4e2c04b7cbfa5daa617455 840w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/1.png?w=1100&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=dec491fecf6d7853657b0a1a6f6bb8b4 1100w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/1.png?w=1650&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=44e4fcff12c456267fa93a1b234ecb94 1650w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/1.png?w=2500&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=974b970ba4b8e788c3ca5ea769f98b4a 2500w" />

## Variables and Dynamic Content

The Playground supports dynamic variables in your prompts:

1. Define variables using double curly braces: `{{variable_name}}`
2. Enter test values in the Variables section
3. See how different variable values affect the output

<img src="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/variables.png?fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=5975e0dd9e1cc314fd2b664a62c86b47" alt="Screenshot: Using variables in prompts" data-og-width="1698" width="1698" data-og-height="426" height="426" data-path="media/docs/prompt-playground/variables.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/variables.png?w=280&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=eb57b5746e4bd7b8f7d10fe5114f0c8e 280w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/variables.png?w=560&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=fe63c7ee001116b038831e79aae9a9de 560w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/variables.png?w=840&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=5dbf641249bd1c456faeb469f9759a82 840w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/variables.png?w=1100&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=037c401154b0664d32f90d9fffa1cbc8 1100w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/variables.png?w=1650&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=9b50613e9a7d7a0fea13089dddf484ba 1650w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/variables.png?w=2500&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=a90e06c9418dedf860f0fced270bf183 2500w" />

## Saving and Collaboration

The Playground supports team collaboration with built-in versioning and role-based access control:

### Creating Draft Versions

1. Click "Save as Draft" to save your experiments without affecting production
2. Add version notes to document your changes and findings
3. Share the draft with team members for review and feedback

### Collaboration Features

* **Draft Sharing**: Team members can view and test your draft prompts
* **Notepad**: Leave feedback on specific prompt versions via the notepad
* **Role-Based Access**:
  * Developers and prompt engineers can create and edit drafts
  * Only authorized users (with deployment permissions) can promote drafts to production
  * Viewers can test prompts but cannot modify them

## Testing with Custom Endpoints

One of the most powerful features of the Prompt Playground is the ability to test prompts against your own custom API endpoints. This is particularly useful for:

* **RAG (Retrieval-Augmented Generation) systems**
* **Custom AI applications** with proprietary logic
* **API wrappers** that combine multiple AI services
* **Complex systems** that include more components than just an LLM

### Setting Up Custom Endpoints

To configure a custom endpoint:

1. Toggle the **Run Mode** from "Model Provider" to "Custom Endpoint"
2. Click "Configure Endpoints" to set up your API endpoints

<img src="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/2.png?fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=b9cd07cf9cc7d003edd0636eb3a7a3f9" alt="Screenshot: Switching to Custom Endpoint mode" data-og-width="794" width="794" data-og-height="1058" height="1058" data-path="media/docs/prompt-playground/2.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/2.png?w=280&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=5e0340b924f3b973e52a2e96bc5e47e7 280w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/2.png?w=560&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=5612f00f6c49c579460f9959718d0b85 560w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/2.png?w=840&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=cd6cde89445f9d0943b3fbe06b9e11b4 840w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/2.png?w=1100&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=da4d4eede109529edda519dfd8a61073 1100w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/2.png?w=1650&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=043567f03424f31eabf38cfd04726ffb 1650w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/2.png?w=2500&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=cc3f31de711296e4de9e9e66df647913 2500w" />

### Endpoint Configuration

When creating an endpoint, you'll need to provide:

* **Name**: A descriptive name for your endpoint
* **URL**: The full URL of your API endpoint
* **Authentication**: Choose from:
  * Bearer Token (for OAuth/JWT)
  * API Key (with custom header name)
  * Basic Authentication
  * No authentication
* **Custom Headers**: Additional headers to include in requests
* **Default Payload**: Base payload that will be merged with prompt data

<img src="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/3.png?fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=9be1c88bc63d566f2a8fe17feca3d471" alt="Screenshot: Endpoint configuration dialog" data-og-width="3056" width="3056" data-og-height="1972" height="1972" data-path="media/docs/prompt-playground/3.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/3.png?w=280&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=e22b3fe3e7b2af5bc8208512413a0937 280w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/3.png?w=560&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=cdf7ae8c4d0706f29f8aadb9b6f3d575 560w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/3.png?w=840&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=f3f746f4663c0ea0e1bd1e540ac4a1bd 840w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/3.png?w=1100&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=65984dd0e940dc53573fb88e48f97925 1100w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/3.png?w=1650&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=a8268e4505b65af33f1742d372be1c55 1650w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/3.png?w=2500&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=66e4b842d71abfb7e786b44e69d37981 2500w" />

### Request Format

When you run a prompt against a custom endpoint, Lunary sends an HTTP POST request with the following JSON payload:

```json  theme={null}
{
  "messages": [
    {"role": "system", "content": "You are a helpful assistant"},
    {"role": "user", "content": "What is the weather like?"}
  ],
  "model_params": {
    "temperature": 0.7,
    "max_tokens": 1000,
    "model": "gpt-4"
  },
  "variables": {
    "location": "San Francisco",
    "user_id": "12345"
  }
  // custom payload data will be merged here 
  "custom_data": {
    "example_key": "example_value"
  }
}
```

Your endpoint should process this request and return a response. Lunary supports various response formats:

* Simple text responses
* OpenAI-compatible message arrays
* Custom JSON structures

<img src="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/4.png?fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=d42513dccca9c8ad838bb7bc28308273" alt="Screenshot: Example request payload" data-og-width="3058" width="3058" data-og-height="1984" height="1984" data-path="media/docs/prompt-playground/4.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/4.png?w=280&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=d742a7196cd9d21d178c98d9ccf1c12d 280w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/4.png?w=560&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=ee5a62949e57777db83e66299a732f35 560w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/4.png?w=840&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=d0de4c59bea4bc819112ce9465ee541d 840w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/4.png?w=1100&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=f59f56fe7b082a317f66413f66d55259 1100w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/4.png?w=1650&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=990ac01bde2869b2bc2a73625c8afd2f 1650w, https://mintcdn.com/lunary/vczTtzy07XKKcaZn/media/docs/prompt-playground/4.png?w=2500&fit=max&auto=format&n=vczTtzy07XKKcaZn&q=85&s=e5f21f5e86f9b288fe10780c48d451c3 2500w" />

### Use Case Examples

#### RAG System Integration

Test how your prompts work with your retrieval-augmented generation system:

```javascript  theme={null}
// Example RAG endpoint that enriches prompts with context
app.post('/api/rag-chat', async (req, res) => {
  const { content, variables } = req.body;
  
  // Extract the user's query
  const userQuery = content[content.length - 1].content;
  
  // Search your knowledge base
  const relevantDocs = await vectorDB.search(userQuery, {
    filter: { user_id: variables.user_id },
    limit: 5
  });
  
  // Augment the prompt with retrieved context
  const augmentedContent = [
    ...content.slice(0, -1),
    {
      role: "system",
      content: `Relevant context:\n${relevantDocs.map(d => d.text).join('\n\n')}`
    },
    content[content.length - 1]
  ];
  
  // Generate response with your LLM
  const response = await llm.generate({
    ...req.body,
    content: augmentedContent
  });
  
  res.json({ content: response.text });
});
```

#### Custom Agent Testing

Test prompts against AI agents with tool access or custom logic:

```python  theme={null}
# Example agent endpoint with tool usage
@app.post("/api/agent")
async def agent_endpoint(request: dict):
    prompt = request["content"]
    variables = request["variables"]
    
    # Parse intent and determine required tools
    intent = parse_intent(prompt[-1]["content"])
    
    if intent.requires_search:
        search_results = await web_search(intent.query)
        context = format_search_results(search_results)
        prompt.append({"role": "system", "content": f"Search results: {context}"})
    
    if intent.requires_calculation:
        calc_result = await calculator(intent.expression)
        prompt.append({"role": "system", "content": f"Calculation: {calc_result}"})
    
    # Generate final response
    response = await generate_response(prompt, variables)
    
    return {"content": response, "tools_used": intent.tools}
```


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.lunary.ai/llms.txt