# Source: https://docs.xano.com/building/logic/background-tasks.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.xano.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Background Tasks in Xano

> Learn how to build and schedule background tasks (cron jobs) in Xano using the visual builder or XanoScript.

<Tip>
  Before continuing, make sure you're familiar with:

  * [Core Components](/building/logic/core-components)
  * [Working with Data](/building/logic/working-with-data)
</Tip>

## Background Tasks in Xano

Background tasks (also called scheduled tasks or cron jobs) allow you to automate operations at specific times or intervals. They are ideal for recurring jobs like data cleanup, report generation, or sending notifications.

Each background task has:

* A name (unique identifier, e.g., `daily_sales_report`)
* Logic (the actions to perform)
* A schedule (when and how often to run)

Unlike APIs, background tasks **do not** have inputs or responses. They only contain logic and a schedule block.

## Creating a Background Task

You can create background tasks visually or with XanoScript.

### Visual Builder

<Steps>
  <Step title="Add a New Task">
    From the left-hand menu, click <span class="ui-bubble"><Icon icon="clock-rotate-left" /> Tasks</span>, then click <span class="ui-bubble"><Icon icon="plus" /> Add Background Task</span>.
    <Frame>    <img src="https://mintcdn.com/xano-997cb9ee/2BfSBW9hPbKyXtF8/images/background-tasks-20251020-084325.png?fit=max&auto=format&n=2BfSBW9hPbKyXtF8&q=85&s=9fb9cca98aa3d4c381d5d9a26342f071" alt="background-tasks-20251020-084325" width="1247" height="665" data-path="images/background-tasks-20251020-084325.png" /></Frame>
  </Step>

  <Step title="Configure the Task">
    Give your task a name and description, and choose the data source that the task will run against, by default. If you don't choose a data source, scheduled runs will always use the live data source.
    <Frame>    <img src="https://mintcdn.com/xano-997cb9ee/2BfSBW9hPbKyXtF8/images/background-tasks-20251020-084540.png?fit=max&auto=format&n=2BfSBW9hPbKyXtF8&q=85&s=e6ce6e4342ad33d0a17a538ebf197a3f" alt="background-tasks-20251020-084540" width="1350" height="624" data-path="images/background-tasks-20251020-084540.png" /></Frame>
  </Step>
</Steps>

<Tabs>
  <Tab title="Build Visually">
    Add functions to your task by clicking <span class="ui-bubble"><Icon icon="plus" /> Add Function</span>. You can use any function available in Xano, just like in APIs.<br /><img src="https://mintcdn.com/xano-997cb9ee/2BfSBW9hPbKyXtF8/images/background-tasks-20251020-084713.png?fit=max&auto=format&n=2BfSBW9hPbKyXtF8&q=85&s=d2e19587a6d559d8e9f53784fb3367ab" alt="background-tasks-20251020-084713" width="2553" height="880" data-path="images/background-tasks-20251020-084713.png" />

    When you've finished building your logic, you can set up the schedule by clicking the <span class="ui-bubble"><Icon icon="plus" /> Add a schedule</span> option.

    Schedules have a start date / time, and can run once or on a repeating interval (e.g., every hour, day, week, etc.). For tasks that have a repeating schedule, you can also set an end date.<br /><img src="https://mintcdn.com/xano-997cb9ee/2BfSBW9hPbKyXtF8/images/background-tasks-20251020-084908.png?fit=max&auto=format&n=2BfSBW9hPbKyXtF8&q=85&s=6fbb3c8b51a4bfed649a30225314caef" alt="background-tasks-20251020-084908" width="658" height="695" data-path="images/background-tasks-20251020-084908.png" />

    After configuring the schedule, click <span class="ui-bubble">Save</span> to create your background task.

    You'll need to enable your task before publishing by selecting the option.

    <Frame caption="Active/Inactive toggle in the Canvas View">
            <img src="https://mintcdn.com/xano-997cb9ee/2BfSBW9hPbKyXtF8/images/background-tasks-20251020-085101.png?fit=max&auto=format&n=2BfSBW9hPbKyXtF8&q=85&s=d7bec7f2bc8bfa52a046a1b2134f848e" alt="background-tasks-20251020-085101" width="602" height="274" data-path="images/background-tasks-20251020-085101.png" />
    </Frame>

    <br />

    <Frame caption="Enable option in the Function Stack view">
            <img src="https://mintcdn.com/xano-997cb9ee/2BfSBW9hPbKyXtF8/images/background-tasks-20251020-085136.png?fit=max&auto=format&n=2BfSBW9hPbKyXtF8&q=85&s=c8cc66d19ffa888726ae84b65add0898" alt="background-tasks-20251020-085136" width="2264" height="479" data-path="images/background-tasks-20251020-085136.png" />
    </Frame>

    Once you've set your schedule and enabled the task, click <span class="ui-bubble">Publish</span> to deploy your background task.
  </Tab>

  <Tab title="XanoScript">
    ### XanoScript

    A basic background task in XanoScript has two parts — **logic** and **schedule**:

    ```javascript lines icon="code" Example of a basic background task in XanoScript theme={null}
    // This task runs every day at 11 PM UTC and generates a sales report
    task daily_sales_report {
      description = "Generate a daily sales report at 11 PM UTC"
      stack {
        db.query payment_transactions {
          description = "Get all transactions from the past 24 hours"
          where = $db.payment_transactions.transaction_date >= (now|transform_timestamp:"24 hours ago":"UTC")
        } as $daily_sales

        var $transaction_count {
          value = $daily_sales|count
          description = "Count number of transactions"
        }

        var $total_sales {
          value = ($daily_sales[$$].amount)|sum
          description = "Calculate total sales amount"
        }

        db.add reports {
          data = {
            report_type      : "daily_sales"
            report_date      : now
            total_sales      : $total_sales
            transaction_count: $transaction_count
          }
          description = "Insert daily sales report"
        } as $report_result

        debug.log {
          value = "Daily sales report generated"
          description = "Log report generation"
        }
      }
      schedule = [{starts_on: 2025-10-20 13:47:35+0000, freq: 86400}]

    }
    ```

    <Card title="Learn how to build Tasks in XanoScript" icon="code" horizontal href="/xanoscript/tasks">
      For more information on how to build background tasks in XanoScript, see the XanoScript Task documentation.
    </Card>
  </Tab>
</Tabs>


Built with [Mintlify](https://mintlify.com).