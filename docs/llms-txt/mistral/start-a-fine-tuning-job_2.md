# start a fine-tuning job
client.fine_tuning.jobs.start(job_id = created_jobs.id)

created_jobs
```
  </TabItem>

  <TabItem value="typescript" label="typescript">

```typescript
await client.fineTuning.jobs.start({jobId: createdJob.id})
```
  </TabItem>

  <TabItem value="curl" label="curl">

```bash
curl -X POST https://api.mistral.ai/v1/fine_tuning/jobs/<jobid>/start \
--header "Authorization: Bearer $MISTRAL_API_KEY"
```
  </TabItem>

</Tabs>

## List/retrieve/cancel jobs
You can also list jobs, retrieve a job, or cancel a job.

You can filter and view a list of jobs using various parameters such as
`page`, `page_size`, `model`, `created_after`, `created_by_me`, `status`, `wandb_project`, `wandb_name`, and `suffix`. Check out our [API specs](https://docs.mistral.ai/api/#tag/fine-tuning) for details.

<Tabs groupId="code">
  <TabItem value="python" label="python" default>

```python