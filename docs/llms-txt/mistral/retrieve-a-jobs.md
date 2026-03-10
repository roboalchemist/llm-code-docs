# Retrieve a jobs
retrieved_jobs = client.fine_tuning.jobs.get(job_id = created_jobs.id)
print(retrieved_jobs)
```
  </TabItem>

  <TabItem value="typescript" label="typescript">

```typescript
// Retrieve a job
const retrievedJob = await client.jobs.retrieve({ jobId: createdJob.id });
```
  </TabItem>
  
  <TabItem value="curl" label="curl">

```bash