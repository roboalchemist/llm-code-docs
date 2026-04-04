# Cancel a jobs
canceled_jobs = client.fine_tuning.jobs.cancel(job_id = created_jobs.id)
print(canceled_jobs)
```
  </TabItem>

  <TabItem value="typescript" label="typescript">

```typescript
// List jobs
const jobs = await client.fineTuning.jobs.list();

// Retrieve a job
const retrievedJob = await client.fineTuning.jobs.get({ jobId: createdJob.id })

// Cancel a job
const canceledJob = await client.fineTuning.jobs.cancel({
  jobId: createdJob.id,
});
```
  </TabItem>

  <TabItem value="curl" label="curl">

```bash