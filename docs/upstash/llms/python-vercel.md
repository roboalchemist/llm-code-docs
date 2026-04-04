# Source: https://upstash.com/docs/qstash/quickstarts/python-vercel.md

> ## Documentation Index
> Fetch the complete documentation index at: https://upstash.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Python on Vercel

## Introduction

This quickstart will guide you through setting up QStash to run a daily script
to clean up your database. This is useful for testing and development environments
where you want to reset the database every day.

## Prerequisites

* Create an Upstash account and get your [QStash token](https://console.upstash.com/qstash)

<Steps>
  <Step titleSize="h3" title="Create Python app">
    First, we'll create a new directory for our Python app. We'll call it `clean-db-cron`.

    The database we'll be using is Redis, so we'll need to install the `upstash_redis` package.

    ```bash  theme={"system"}
    mkdir clean-db-cron
    ```

    ```bash  theme={"system"}
    cd clean-db-cron
    ```

    ```bash  theme={"system"}
    pip install upstash-redis
    ```
  </Step>

  <Step titleSize="h3" title="Cleanup logic">
    Let's write the Python code to clean up the database. We'll use the `upstash_redis`
    package to connect to the database and delete all keys.

    ```python index.py theme={"system"}
    from upstash_redis import Redis

    redis = Redis(url="https://YOUR_REDIS_URL", token="YOUR_TOKEN")

    def delete_all_entries():
      keys = redis.keys("*") # Match all keys
      redis.delete(*keys)


    delete_all_entries()
    ```

    Try running the code to see if it works. Your database keys should be deleted!
  </Step>

  <Step titleSize="h3" title="Make the Python code into a public endpoint">
    In order to use QStash, we need to make the Python code into a public endpoint. There
    are many ways to do this such as using Flask, FastAPI, or Django. In this example, we'll
    use the Python `http.server` module to create a simple HTTP server.

    ```python api/index.py theme={"system"}
    from http.server import BaseHTTPRequestHandler
    from upstash_redis import Redis

    redis = Redis(url="https://YOUR_REDIS_URL", token="YOUR_TOKEN")

    def delete_all_entries():
      keys = redis.keys("*") # Match all keys
      redis.delete(*keys)


    class handler(BaseHTTPRequestHandler):
      def do_POST(self):
        delete_all_entries()
        self.send_response(200)
        self.end_headers()
    ```

    For the purpose of this tutorial, I'll deploy the application to Vercel using the
    [Python Runtime](https://vercel.com/docs/functions/runtimes/python), but feel free to
    use any other hosting provider.

    <Accordion title="Deploying to Vercel">
      There are many ways to [deploy to Vercel](https://vercel.com/docs/deployments/overview), but
      I'm going to use the Vercel CLI.

      ```bash  theme={"system"}
      npm install -g vercel
      ```

      ```bash  theme={"system"}
      vercel
      ```
    </Accordion>

    Once deployed, you can find the public URL in the dashboard.
  </Step>

  <Step titleSize="h3" title="Have QStash invoke the endpoint">
    There are two ways we can go about configuring QStash. We can either use the QStash dashboard
    or the QStash API. In this example, it makes more sense to utilize the dashboard since we
    only need to set up a singular cronjob.

    However, you can imagine a scenario where you have a large number of cronjobs and you'd
    want to automate the process. In that case, you'd want to use the QStash Python SDK.

    To create the schedule, go to the [QStash dashboard](https://console.upstash.com/qstash) and enter
    the URL of the public endpoint you created. Then, set the type to schedule and change the
    `Upstash-Cron` header to run daily at a time of your choosing.

    ```
    URL: https://your-vercel-app.vercel.app/api
    Type: Schedule
    Every: every day at midnight (feel free to customize)
    ```

    <Frame>
      <img src="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/python-quickstart-schedule.png?fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=8173b32d110478738d2c7f4713b69593" alt="QStash console scheduling" data-og-width="2002" width="2002" data-og-height="1282" height="1282" data-path="img/qstash/python-quickstart-schedule.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/python-quickstart-schedule.png?w=280&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=de2601e51052910ae56c321912d0568d 280w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/python-quickstart-schedule.png?w=560&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=6c4e7261a126990b151704a03b912929 560w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/python-quickstart-schedule.png?w=840&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=b874129a02d901bcf4d4308598a855f0 840w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/python-quickstart-schedule.png?w=1100&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=41748daa51aef9cc8e0c02c67562658d 1100w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/python-quickstart-schedule.png?w=1650&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=87c08f2d42bc1f39d9634b05a7a5ebf1 1650w, https://mintcdn.com/upstash/V1WwT580M-elE8rq/img/qstash/python-quickstart-schedule.png?w=2500&fit=max&auto=format&n=V1WwT580M-elE8rq&q=85&s=72343d62d71b8b046ddf6700065489b8 2500w" />
    </Frame>

    Once you start the schedule, QStash will invoke the endpoint at the specified time. You can
    scroll down and verify the job has been created!

    <Accordion title="Using the SDK">
      If you have a use case where you need to automate the creation of jobs, you can use the SDK instead.

      ```python  theme={"system"}
      from qstash import QStash

      client = QStash("<QSTASH_TOKEN>")
      client.schedule.create(
          destination="https://YOUR_URL.vercel.app/api",
          cron="0 12 * * *",
      )
      ```
    </Accordion>
  </Step>
</Steps>

Now, go ahead and try it out for yourself! Try using some of the other features of QStash, such as
[callbacks](/qstash/features/callbacks) and [URL Groups](/qstash/features/url-groups).
