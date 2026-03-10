# start a fine-tuning job
client.fine_tuning.jobs.start(job_id = created_jobs.id)

created_jobs
```
  </TabItem>

  <TabItem value="typescript" label="typescript">

```typescript
const createdJob = await client.jobs.create({
  model: 'open-mistral-7b',
  trainingFiles: [ultrachat_chunk_train.id],
  validationFiles: [ultrachat_chunk_eval.id],
  hyperparameters: {
    trainingSteps: 10,
    learningRate: 0.0001,
  },
});
```
  </TabItem>
  
  <TabItem value="curl" label="curl">

```bash
curl https://api.mistral.ai/v1/fine_tuning/jobs \
--header "Authorization: Bearer $MISTRAL_API_KEY" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
  "model": "open-mistral-7b",
  "training_files": [
    "<uuid>"
  ],
  "validation_files": [
    "<uuid>"
  ],
  "hyperparameters": {
    "training_steps": 10,
    "learning_rate": 0.0001
  }
}'
```
  </TabItem>

</Tabs>

Example output:

```
{
    "id": "25d7efe6-6303-474f-9739-21fb0fccd469",
    "hyperparameters": {
        "training_steps": 10,
        "learning_rate": 0.0001
    },
    "fine_tuned_model": null,
    "model": "open-mistral-7b",
    "status": "QUEUED",
    "job_type": "FT",
    "created_at": 1717170356,
    "modified_at": 1717170357,
    "training_files": [
        "66f96d02-8b51-4c76-a5ac-a78e28b2584f"
    ],
    "validation_files": [
        "84482011-dfe9-4245-9103-d28b6aef30d4"
    ],
    "object": "job",
    "integrations": []
}
```


### Analyze and evaluate fine-tuned model

When we retrieve a model, we get the following metrics every 10% of the progress with a minimum of 10 steps in between:
- Training loss: the error of the model on the training data, indicating how well the model is learning from the training set. 
- Validation loss: the error of the model on the validation data, providing insight into how well the model is generalizing to unseen data. 
- Validation token accuracy: the percentage of tokens in the validation set that are correctly predicted by the model. 

Both validation loss and validation token accuracy serve as essential indicators of the model's overall performance, helping to assess its ability to generalize and make accurate predictions on new data.


<Tabs>
  <TabItem value="python" label="python" default>

```python