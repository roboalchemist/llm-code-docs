# Source: https://upstash.com/docs/qstash/howto/delete-schedule.md

# Delete Schedules

Deleting schedules can be done using the [schedules api](/qstash/api/schedules/remove).

<CodeGroup>
  ```shell cURL theme={"system"}
  curl -XDELETE \
      -H 'Authorization: Bearer XXX' \
      'https://qstash.upstash.io/v2/schedules/<schedule_id>'
  ```

  ```typescript Typescript theme={"system"}
  import { Client } from "@upstash/qstash";

  const client = new Client({ token: "<QSTASH_TOKEN>" });
  await client.schedules.delete("<scheduleId>");
  ```

  ```python Python theme={"system"}
  from qstash import QStash

  client = QStash("<QSTASH_TOKEN>")
  client.schedule.delete("<scheduleId>")
  ```
</CodeGroup>

Deleting a schedule does not stop existing messages from being delivered. It
only stops the schedule from creating new messages.

## Schedule ID

If you don't know the schedule ID, you can get a list of all of your schedules
from [here](/qstash/api/schedules/list).

<CodeGroup>
  ```shell cURL theme={"system"}
  curl \
      -H 'Authorization: Bearer XXX' \
      'https://qstash.upstash.io/v2/schedules'
  ```

  ```typescript Typescript theme={"system"}
  import { Client } from "@upstash/qstash";

  const client = new Client({ token: "<QSTASH_TOKEN>" });
  const allSchedules = await client.schedules.list();
  ```

  ```python Python theme={"system"}
  from qstash import QStash

  client = QStash("<QSTASH_TOKEN>")
  client.schedule.list()
  ```
</CodeGroup>
