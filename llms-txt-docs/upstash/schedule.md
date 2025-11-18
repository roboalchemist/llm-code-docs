# Source: https://upstash.com/docs/workflow/howto/schedule.md

# Schedule a Workflow

You can schedule a workflow to run periodically using a cron definition.

For this feature, you would need to use Upstash QStash's Schedules feature.

## Scheduling a workflow

For example, let's suppose that you have a workflow that creates a backup of some important data daily. Our workflow endpoint might look like this:

To run this endpoint on a schedule, navigate to `Schedules` in your QStash dashboard and click `Create Schedule`:

<Frame>
  <img src="https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-workflow/create_schedule.png?fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=6d93a7f91194bb013c613851db9e61cc" data-og-width="1530" width="1530" data-og-height="966" height="966" data-path="img/qstash-workflow/create_schedule.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-workflow/create_schedule.png?w=280&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=20784884de574336a15e7d418e0fc98a 280w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-workflow/create_schedule.png?w=560&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=d5e5d841b361464f7bcedfbb6a392ad8 560w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-workflow/create_schedule.png?w=840&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=4100cc81590f13296aaea95467ee5062 840w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-workflow/create_schedule.png?w=1100&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=8bf11d6cb765329928c561e09bda95f5 1100w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-workflow/create_schedule.png?w=1650&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=0569a12089d58337dfc537018dc11d21 1650w, https://mintcdn.com/upstash/pqZtv0gXFMQuy8rU/img/qstash-workflow/create_schedule.png?w=2500&fit=max&auto=format&n=pqZtv0gXFMQuy8rU&q=85&s=94a307e3eda756d3832c4502f6447a7b 2500w" />
</Frame>

Enter your live endpoint URL, add a CRON expression to define the interval at which your endpoint is called (i.e. every day, every 15 minutes, ...) and click `Schedule`:

<Frame>
  <img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/schedule_workflow.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=00802afbcc6a04e305cc95de995684fb" data-og-width="1285" width="1285" data-og-height="679" height="679" data-path="img/qstash-workflow/schedule_workflow.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/schedule_workflow.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=645c89f282743a30adeefd8a6a170d16 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/schedule_workflow.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=f94c72be12071cdf6f8997433294c99f 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/schedule_workflow.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=3cb250be15eea6a10c447a58f79ab77b 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/schedule_workflow.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=f9cd84255e31bd3acfe7a3ee1a386f1e 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/schedule_workflow.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=9576c03397775a4c93330905aa2d7dbd 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash-workflow/schedule_workflow.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=06e7b0fa0e0a8fa9ed103c335024e5e4 2500w" />
</Frame>

Your workflow will now run repeatedly at the interval you have defined. For more details on CRON expressions, see our [QStash scheduling documentation](/qstash/features/schedules).

## Programmatically Schedule

In order to massively improve the user experience, many applications send weekly summary reports to their users. These could be weekly analytics summaries or SEO statistics to keep users engaged with the platform.

Let's create a user-specific schedule, sending a first report to each user exactly 7 days after they signed up:

<CodeGroup>
  ```typescript api/sign-up/route.ts theme={"system"}
  import { signUp } from "@/utils/auth-utils";
  import { Client } from "@upstash/qstash";

  const client = new Client({ token: process.env.QSTASH_TOKEN! });

  export async function POST(request: Request) {
    const userData: UserData = await request.json();

    // Schedule weekly account summary
    await client.schedules.create({
      scheduleId: `user-summary-${user.email}`,
      destination: "https://<YOUR_APP_URL>/api/send-weekly-summary",
      body: { userId: user.id },
      cron: cron,
    });

    return NextResponse.json(
      { success: true, message: "User registered and summary scheduled" },
      { status: 201 }
    );
  }
  ```

  ```python main.py theme={"system"}
  from fastapi import FastAPI, Request
  from fastapi.responses import JSONResponse
  from qstash import AsyncQStash
  from datetime import datetime, timedelta

  app = FastAPI()

  client = AsyncQStash("<QSTACK_TOKEN>")


  @app.post("/api/sign-up")
  async def sign_up(request: Request):
      user_data = await request.json()

      # Simulate user registration
      user = await sign_up(user_data)

      # Calculate the date for the first summary (7 days from now)
      first_summary_date = datetime.now() + timedelta(days=7)

      # Create cron expression for weekly summaries starting 7 days from signup
      cron = f"{first_summary_date.minute} {first_summary_date.hour} * * {first_summary_date.day}"

      # Schedule weekly account summary
      await client.schedule.create_json(
          schedule_id=f"user-summary-{user.email}",
          destination="https://<YOUR_APP_URL>/api/send-weekly-summary",
          body={"userId": user.id},
          cron=cron,
      )

      return JSONResponse(
          content={"success": True, "message": "User registered and summary scheduled"},
          status_code=201,
      )

  ```
</CodeGroup>

This code will call our workflow every week, starting exactly seven days after a user signs up. Each call to our workflow will contain the respective user's ID.

<Note>
  When creating a per-user schedule, pass a unique `scheduleId` to identify the schedule for better management and observability.
</Note>
