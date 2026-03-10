#   ]
)
```

After creating a fine-tuning job, you can check the job status using `client.fine_tuning.jobs.get(job_id = created_jobs.id)`.
  </TabItem>

  <TabItem value="typescript" label="typescript">

```typescript
const createdJob = await client.fineTuning.jobs.create({
    model: 'ministral-3b-latest',
    jobType: 'classifier',
    trainingFiles: [{fileId: training_data.id, weight: 1}],
    validationFiles: [validation_data.id],
    hyperparameters: {
      trainingSteps: 10,
      learningRate: 0.0001,
    },
    autoStart:false,
//  integrations:[
//      {
//          project: "finetuning",
//          apiKey: "WANDB_KEY",
//      }
//  ],
});
```

After creating a fine-tuning job, you can check the job status using `client.fineTuning.jobs.get({ jobId: createdJob.id })`.
  </TabItem>

  <TabItem value="curl" label="curl">

```bash
curl https://api.mistral.ai/v1/fine_tuning/jobs \
--header "Authorization: Bearer $MISTRAL_API_KEY" \
--header 'Content-Type: application/json' \
--header 'Accept: application/json' \
--data '{
  "model": "ministral-3b-latest",
  "job_type": "classifier",
  "training_files": [
    "<uuid>"
  ],
  "validation_files": [
    "<uuid>"
  ],
  "hyperparameters": {
    "training_steps": 10,
    "learning_rate": 0.0001
  },
  "auto_start": false
}'
```

After creating a fine-tuning job, you can check the job status using:
```bash
curl https://api.mistral.ai/v1/fine_tuning/jobs/<jobid> \
--header "Authorization: Bearer $MISTRAL_API_KEY"
```

  </TabItem>

</Tabs>

Initially, the job status will be `"QUEUED"`. After a brief period, the status will update to `"VALIDATED"`. At this point, you can proceed to start the fine-tuning job:

<Tabs groupId="code">
  <TabItem value="python" label="python" default>

```python