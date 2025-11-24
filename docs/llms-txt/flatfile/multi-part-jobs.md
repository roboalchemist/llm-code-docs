# Source: https://flatfile.com/docs/guides/multi-part-jobs.md

# Multi-Part Jobs

> Split up Jobs into Parts

A Job can be split up into multiple parts depending on the intended functionality. This can help spread out large data sets or long tasks across many separate listeners. When a job is split up into parts, the original part is considered the "parent" part and it's children are considered "parts". Each Part is considered it's own separate Job and has the full ecosystem of events attached to it. When all Job Parts have been completed, a new event `job:parts-completed` is emitted, so that you can listen for that event to complete the Parent Job. This event has a payload that has summary statistics about the parts.

```json
{
  "payload": {
    "parts": {
      "total": 10,
      "completed": 10,
      "failed": 0,
      "canceled": 0
    }
  }
}
```

By inspecting this payload, you can determine if the all have completed successfully or not. Based on that information, you are expected to complete or fail the parent Job.

Here's an example of a listener that creates parts and waits for the `job:parts-completed` event:

```typescript
import api from "@flatfile/api";
import { FlatfileListener } from "@flatfile/listener";

export default function (listener: FlatfileListener) {
  // Parent and Part Jobs have the same operation name.
  // Filtering by isPart: false, ensures that the Job is the Parent
  // The job operation name is an example, you can define your own.
  listener.filter(
    { job: "sheet:submitLargeSheet", isPart: false },
    (submitLargeSheet) => {
      submitLargeSheet.on("job:ready", async (event) => {
        const {
          context: { jobId, sheetId },
        } = event;
        console.log("job:ready [PARENT]", { jobId: event.context.jobId });

        const { data: counts } = await api.sheets.getRecordCounts(sheetId);
        const { total } = counts.counts;
        await api.jobs.ack(jobId, {
          info: `Splitting Job`,
          progress: 10,
        });
        console.log("splitting job: ", { jobId, total });

        const batchSize = 1000;
        const totalParts = Math.ceil(total / batchSize);
        const splitjob = await api.jobs.split(jobId, { parts: totalParts });
        console.log("splitjob: ", { splitjob });

        await api.jobs.ack(jobId, {
          info: `Job Split into ${total} parts.`,
          progress: 20,
        });
      });

      // Listen for all parts to finish and then complete the parent Job
      submitLargeSheet.on("job:parts-completed", async (event) => {
        const {
          context: { jobId },
        } = event;

        console.log("job:parts-completed: ", jobId);

        await api.jobs.complete(jobId, {
          outcome: {
            message: "This job is now complete.",
          },
        });
      });
    }
  );
}
```

Here's an example of a listener that does logic on each Part:

```typescript
import api from "@flatfile/api";
import { FlatfileListener } from "@flatfile/listener";

export default function (listener: FlatfileListener) {
  // Parent and Part Jobs have the same operation name.
  // Filtering by isPart: true, ensures that the Job is a Part
  // The job operation name is an example, you can define your own.
  listener.filter(
    { job: "sheet:submitLargeSheet", isPart: true },
    (submitLargeSheet) => {
      submitLargeSheet.on("job:ready", async (event) => {
        const {
          context: { jobId },
        } = event;
        await api.jobs.ack(jobId);
        const job = await api.jobs.get(jobId);
        console.dir({ job }, { depth: 10 });
        const { partData, parentId } = job.data;
        const { records } = await event.data({
          pageSize: 1,
          pageNumber: partData.part + 1,
        });

        console.log({ record: records[0].values });
        console.log("submitting part: ", jobId, partData);

        await new Promise((r) => setTimeout(r, 1000));

        await api.jobs.complete(jobId, {
          outcome: {
            message: "This job is now complete.",
          },
        });
      });
    }
  );
}
```
