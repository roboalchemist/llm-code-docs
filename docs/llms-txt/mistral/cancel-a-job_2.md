# Cancel a job
curl -X POST https://api.mistral.ai/v1/fine_tuning/jobs/<jobid>/cancel \
--header "Authorization: Bearer $MISTRAL_API_KEY"
```
  </TabItem>

</Tabs>


## Use a fine-tuned model
When a fine-tuned job is finished, you will be able to see the fine-tuned model name via `retrieved_jobs.fine_tuned_model`. Then you can use our `chat` endpoint to chat with the fine-tuned model:

<Tabs groupId="code">
  <TabItem value="python" label="python" default>

```python
chat_response = client.chat.complete(
    model=retrieved_job.fine_tuned_model,
    messages = [{"role":'user', "content":'What is the best French cheese?'}]
)
```
  </TabItem>

  <TabItem value="typescript" label="typescript">

```typescript
const chatResponse = await client.chat.complete({
  model: retrievedJob.fine_tuned_model,
  messages: [{role: 'user', content: 'What is the best French cheese?'}],
});
```
  </TabItem>

  <TabItem value="curl" label="curl">

```bash
curl "https://api.mistral.ai/v1/chat/completions" \
     --header 'Content-Type: application/json' \
     --header 'Accept: application/json' \
     --header "Authorization: Bearer $MISTRAL_API_KEY" \
     --data '{
    "model": "ft:open-mistral-7b:daf5e488:20240430:c1bed559",
    "messages": [{"role": "user", "content": "Who is the most renowned French painter?"}]
  }'
```
  </TabItem>

</Tabs>

## Delete a fine-tuned model

<Tabs groupId="code">
  <TabItem value="python" label="python" default>

```python
client.models.delete(model_id=retrieved_job.fine_tuned_model)
```
  </TabItem>

  <TabItem value="typescript" label="typescript">

```typescript
await client.models.delete({modelId:retrieved_job.fine_tuned_model})
```

  </TabItem>

  <TabItem value="curl" label="curl">

```bash
curl --location --request DELETE 'https://api.mistral.ai/v1/models/ft:open-mistral-7b:XXX:20240531:XXX' \
     --header 'Accept: application/json' \
     --header "Authorization: Bearer $MISTRAL_API_KEY"
```
  </TabItem>

</Tabs>


<FAQ />


[Function calling]
Source: https://docs.mistral.ai/docs/capabilities/function-calling

<a target="_blank" href="https://colab.research.google.com/github/mistralai/cookbook/blob/main/mistral/function_calling/function_calling.ipynb">
  <img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/>
</a>

Function calling allows Mistral models to connect to external tools. By integrating Mistral models with external tools such as user defined functions or APIs, users can easily build applications catering to specific use cases and practical problems. In this guide, for instance, we wrote two functions for tracking payment status and payment date. We can use these two tools to provide answers for payment-related queries. 

<div style={{ textAlign: 'center' }}>
  <iframe width="560" height="315" src="https://www.youtube.com/embed/eOo4GfHj3ZE?si=-l0j8Qpi9qLNy1BA" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
</div>

### Available models
Currently, function calling is available for the following models:
- Mistral Large 
- Mistral Medium
- Mistral Small 
- Devstral Small
- Codestral 
- Ministral 8B 
- Ministral 3B 
- Pixtral 12B 
- Pixtral Large
- Mistral Nemo 


### Four steps 
At a glance, there are four steps with function calling:
- User: specify tools and query
- Model: Generate function arguments if applicable
- User: Execute function to obtain tool results
- Model: Generate final answer

<div style={{ textAlign: 'center' }}>
  <img
    src="/img/guides/functioncalling1.png"
    alt="functioncalling1"
    width="600"
    style={{ borderRadius: '15px' }}
  />
</div>

In this guide, we will walk through a simple example to demonstrate how function calling works with Mistral models in these four steps. 

Before we get started, let’s assume we have a dataframe consisting of payment transactions. When users ask questions about this dataframe, they can use certain tools to answer questions about this data. This is just an example to emulate an external database that the LLM cannot directly access.

<Tabs groupId="code">
  <TabItem value="python" label="python" default>

```python