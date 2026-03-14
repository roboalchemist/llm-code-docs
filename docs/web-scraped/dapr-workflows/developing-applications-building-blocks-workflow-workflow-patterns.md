# Source: https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-patterns/

Title: Workflow patterns

URL Source: https://docs.dapr.io/developing-applications/building-blocks/workflow/workflow-patterns/

Markdown Content:
Dapr Docs
Homepage
GitHub
Blog
Discord
Community
v1.17 (latest)
English
Search
Concepts
Getting started
Developing applications
Building blocks
Service invocation
Publish & subscribe
Workflow
Overview
Features and concepts
Workflow versioning
Workflow patterns
Workflow architecture
How to: Author workflows
How to: Manage workflows
Multi Application Workflows
History Retention Policy
Workflow Execution Concurrency
State management
Bindings
Actors
Secrets management
Configuration
Distributed lock
Cryptography
Jobs
Conversation
SDKs
Error codes
Local development
Debugging
Integrations
Components
Developing AI
Operations
Reference
Contributing
 Edit this page
 Create documentation issue
 Create project issue
 Print entire section
Task chaining
Fan-out/fan-in
Async HTTP APIs
Monitor
External system interaction
Compensation
Next steps
Related links
Developing applications
Building blocks
Workflow
Workflow patterns
Workflow patterns
Write different types of workflow patterns

Dapr Workflows simplify complex, stateful coordination requirements in microservice architectures. The following sections describe several application patterns that can benefit from Dapr Workflows.

Task chaining

In the task chaining pattern, multiple steps in a workflow are run in succession, and the output of one step may be passed as the input to the next step. Task chaining workflows typically involve creating a sequence of operations that need to be performed on some data, such as filtering, transforming, and reducing.

In some cases, the steps of the workflow may need to be orchestrated across multiple microservices. For increased reliability and scalability, you’re also likely to use queues to trigger the various steps.

While the pattern is simple, there are many complexities hidden in the implementation. For example:

What happens if one of the microservices are unavailable for an extended period of time?
Can failed steps be automatically retried?
If not, how do you facilitate the rollback of previously completed steps, if applicable?
Implementation details aside, is there a way to visualize the workflow so that other engineers can understand what it does and how it works?

Dapr Workflow solves these complexities by allowing you to implement the task chaining pattern concisely as a simple function in the programming language of your choice, as shown in the following example.

Python
JavaScript
.NET
Java
Go
import dapr.ext.workflow as wf





def task_chain_workflow(ctx: wf.DaprWorkflowContext, wf_input: int):

    try:

        result1 = yield ctx.call_activity(step1, input=wf_input)

        result2 = yield ctx.call_activity(step2, input=result1)

        result3 = yield ctx.call_activity(step3, input=result2)

    except Exception as e:

        yield ctx.call_activity(error_handler, input=str(e))

        raise

    return [result1, result2, result3]





def step1(ctx, activity_input):

    print(f'Step 1: Received input: {activity_input}.')

    # Do some work

    return activity_input + 1





def step2(ctx, activity_input):

    print(f'Step 2: Received input: {activity_input}.')

    # Do some work

    return activity_input * 2





def step3(ctx, activity_input):

    print(f'Step 3: Received input: {activity_input}.')

    # Do some work

    return activity_input ^ 2





def error_handler(ctx, error):

    print(f'Executing error handler: {error}.')

    # Apply some compensating work


Note Workflow retry policies will be available in a future version of the Python SDK.

As you can see, the workflow is expressed as a simple series of statements in the programming language of your choice. This allows any engineer in the organization to quickly understand the end-to-end flow without necessarily needing to understand the end-to-end system architecture.

Behind the scenes, the Dapr Workflow runtime:

Takes care of executing the workflow and ensuring that it runs to completion.
Saves progress automatically.
Automatically resumes the workflow from the last completed step if the workflow process itself fails for any reason.
Enables error handling to be expressed naturally in your target programming language, allowing you to implement compensation logic easily.
Provides built-in retry configuration primitives to simplify the process of configuring complex retry policies for individual steps in the workflow.
Fan-out/fan-in

In the fan-out/fan-in design pattern, you execute multiple tasks simultaneously across potentially multiple workers, wait for them to finish, and perform some aggregation on the result.

In addition to the challenges mentioned in the previous pattern, there are several important questions to consider when implementing the fan-out/fan-in pattern manually:

How do you control the degree of parallelism?
How do you know when to trigger subsequent aggregation steps?
What if the number of parallel steps is dynamic?

Dapr Workflows provides a way to express the fan-out/fan-in pattern as a simple function, as shown in the following example:

# Start the workflow

dapr workflow run DataProcessingWorkflow \

  --app-id processor \

  --input '{"items": ["item1", "item2", "item3"]}'



# Monitor parallel execution

dapr workflow history <instance-id> --app-id processor --output json

Python
JavaScript
.NET
Java
Go
import time

from typing import List

import dapr.ext.workflow as wf





def batch_processing_workflow(ctx: wf.DaprWorkflowContext, wf_input: int):

    # get a batch of N work items to process in parallel

    work_batch = yield ctx.call_activity(get_work_batch, input=wf_input)



    # schedule N parallel tasks to process the work items and wait for all to complete

    parallel_tasks = [ctx.call_activity(process_work_item, input=work_item) for work_item in work_batch]

    outputs = yield wf.when_all(parallel_tasks)



    # aggregate the results and send them to another activity

    total = sum(outputs)

    yield ctx.call_activity(process_results, input=total)





def get_work_batch(ctx, batch_size: int) -> List[int]:

    return [i + 1 for i in range(batch_size)]





def process_work_item(ctx, work_item: int) -> int:

    print(f'Processing work item: {work_item}.')

    time.sleep(5)

    result = work_item * 2

    print(f'Work item {work_item} processed. Result: {result}.')

    return result





def process_results(ctx, final_result: int):

    print(f'Final result: {final_result}.')


The key takeaways from this example are:

The fan-out/fan-in pattern can be expressed as a simple function using ordinary programming constructs
The number of parallel tasks can be static or dynamic
The workflow itself is capable of aggregating the results of parallel executions

Furthermore, the execution of the workflow is durable. If a workflow starts 100 parallel task executions and only 40 complete before the process crashes, the workflow restarts itself automatically and only schedules the remaining 60 tasks.

It’s possible to go further and limit the degree of concurrency using simple, language-specific constructs. The sample code below illustrates how to restrict the degree of fan-out to just 5 concurrent activity executions:

.NET


//Revisiting the earlier example...

// Get a list of N work items to process in parallel.

object[] workBatch = await context.CallActivityAsync<object[]>("GetWorkBatch", null);



const int MaxParallelism = 5;

var results = new List<int>();

var inFlightTasks = new HashSet<Task<int>>();

foreach(var workItem in workBatch)

{

  if (inFlightTasks.Count >= MaxParallelism)

  {

    var finishedTask = await Task.WhenAny(inFlightTasks);

    results.Add(finishedTask.Result);

    inFlightTasks.Remove(finishedTask);

  }



  inFlightTasks.Add(context.CallActivityAsync<int>("ProcessWorkItem", workItem));

}

results.AddRange(await Task.WhenAll(inFlightTasks));



var sum = results.Sum(t => t);

await context.CallActivityAsync("PostResults", sum);


You can process workflow activities in parallel while putting an upper cap on concurrency by using the following extension methods on the WorkflowContext:

.NET
//Revisiting the earlier example...

// Get a list of work items to process

var workBatch = await context.CallActivityAsync<object[]>("GetWorkBatch", null);



// Process deterministically in parallel with an upper cap of 5 activities at a time

var results = await context.ProcessInParallelAsync(workBatch, workItem => context.CallActivityAsync<int>("ProcessWorkItem", workItem), maxConcurrency: 5);



var sum = results.Sum(t => t);

await context.CallActivityAsync("PostResults", sum);


Limiting the degree of concurrency in this way can be useful for limiting contention against shared resources. For example, if the activities need to call into external resources that have their own concurrency limits, like a databases or external APIs, it can be useful to ensure that no more than a specified number of activities call that resource concurrently.

Async HTTP APIs

Asynchronous HTTP APIs are typically implemented using the Asynchronous Request-Reply pattern. Implementing this pattern traditionally involves the following:

A client sends a request to an HTTP API endpoint (the start API)
The start API writes a message to a backend queue, which triggers the start of a long-running operation
Immediately after scheduling the backend operation, the start API returns an HTTP 202 response to the client with an identifier that can be used to poll for status
The status API queries a database that contains the status of the long-running operation
The client repeatedly polls the status API either until some timeout expires or it receives a “completion” response

The end-to-end flow is illustrated in the following diagram.

The challenge with implementing the asynchronous request-reply pattern is that it involves the use of multiple APIs and state stores. It also involves implementing the protocol correctly so that the client knows how to automatically poll for status and know when the operation is complete.

The Dapr workflow HTTP API supports the asynchronous request-reply pattern out-of-the box, without requiring you to write any code or do any state management.

The following curl commands illustrate how the workflow APIs support this pattern.

curl -X POST http://localhost:3500/v1.0/workflows/dapr/OrderProcessingWorkflow/start?instanceID=12345678 -d '{"Name":"Paperclips","Quantity":1,"TotalCost":9.95}'


The previous command will result in the following response JSON:

{"instanceID":"12345678"}


The HTTP client can then construct the status query URL using the workflow instance ID and poll it repeatedly until it sees the “COMPLETE”, “FAILURE”, or “TERMINATED” status in the payload.

curl http://localhost:3500/v1.0/workflows/dapr/12345678


The following is an example of what an in-progress workflow status might look like.

{

  "instanceID": "12345678",

  "workflowName": "OrderProcessingWorkflow",

  "createdAt": "2023-05-03T23:22:11.143069826Z",

  "lastUpdatedAt": "2023-05-03T23:22:22.460025267Z",

  "runtimeStatus": "RUNNING",

  "properties": {

    "dapr.workflow.custom_status": "",

    "dapr.workflow.input": "{\"Name\":\"Paperclips\",\"Quantity\":1,\"TotalCost\":9.95}"

  }

}


As you can see from the previous example, the workflow’s runtime status is RUNNING, which lets the client know that it should continue polling.

If the workflow has completed, the status might look as follows.

{

  "instanceID": "12345678",

  "workflowName": "OrderProcessingWorkflow",

  "createdAt": "2023-05-03T23:30:11.381146313Z",

  "lastUpdatedAt": "2023-05-03T23:30:52.923870615Z",

  "runtimeStatus": "COMPLETED",

  "properties": {

    "dapr.workflow.custom_status": "",

    "dapr.workflow.input": "{\"Name\":\"Paperclips\",\"Quantity\":1,\"TotalCost\":9.95}",

    "dapr.workflow.output": "{\"Processed\":true}"

  }

}


As you can see from the previous example, the runtime status of the workflow is now COMPLETED, which means the client can stop polling for updates.

Monitor

The monitor pattern is recurring process that typically:

Checks the status of a system
Takes some action based on that status - e.g. send a notification
Sleeps for some period of time
Repeat

The following diagram provides a rough illustration of this pattern.

Depending on the business needs, there may be a single monitor or there may be multiple monitors, one for each business entity (for example, a stock). Furthermore, the amount of time to sleep may need to change, depending on the circumstances. These requirements make using cron-based scheduling systems impractical.

Dapr Workflow supports this pattern natively by allowing you to implement eternal workflows. Rather than writing infinite while-loops (which is an anti-pattern), Dapr Workflow exposes a continue-as-new API that workflow authors can use to restart a workflow function from the beginning with a new input.

Python
JavaScript
.NET
Java
Go
from dataclasses import dataclass

from datetime import timedelta

import random

import dapr.ext.workflow as wf





@dataclass

class JobStatus:

    job_id: str

    is_healthy: bool





def status_monitor_workflow(ctx: wf.DaprWorkflowContext, job: JobStatus):

    # poll a status endpoint associated with this job

    status = yield ctx.call_activity(check_status, input=job)

    if not ctx.is_replaying:

        print(f"Job '{job.job_id}' is {status}.")



    if status == "healthy":

        job.is_healthy = True

        next_sleep_interval = 60  # check less frequently when healthy

    else:

        if job.is_healthy:

            job.is_healthy = False

            ctx.call_activity(send_alert, input=f"Job '{job.job_id}' is unhealthy!")

        next_sleep_interval = 5  # check more frequently when unhealthy



    yield ctx.create_timer(fire_at=ctx.current_utc_datetime + timedelta(minutes=next_sleep_interval))



    # restart from the beginning with a new JobStatus input

    ctx.continue_as_new(job)





def check_status(ctx, _) -> str:

    return random.choice(["healthy", "unhealthy"])





def send_alert(ctx, message: str):

    print(f'*** Alert: {message}')


A workflow implementing the monitor pattern can loop forever or it can terminate itself gracefully by not calling continue-as-new.

Note
This pattern can also be expressed using actors and reminders. The difference is that this workflow is expressed as a single function with inputs and state stored in local variables. Workflows can also execute a sequence of actions with stronger reliability guarantees, if necessary.
External system interaction

In some cases, a workflow may need to pause and wait for an external system to perform some action. For example, a workflow may need to pause and wait for a payment to be received. In this case, a payment system might publish an event to a pub/sub topic on receipt of a payment, and a listener on that topic can raise an event to the workflow using the raise event workflow API.

Another very common scenario is when a workflow needs to pause and wait for a human, for example when approving a purchase order. Dapr Workflow supports this event pattern via the external events feature.

Here’s an example workflow for a purchase order involving a human:

A workflow is triggered when a purchase order is received.
A rule in the workflow determines that a human needs to perform some action. For example, the purchase order cost exceeds a certain auto-approval threshold.
The workflow sends a notification requesting a human action. For example, it sends an email with an approval link to a designated approver.
The workflow pauses and waits for the human to either approve or reject the order by clicking on a link.
If the approval isn’t received within the specified time, the workflow resumes and performs some compensation logic, such as canceling the order.

The following diagram illustrates this flow.

The following example code shows how this pattern can be implemented using Dapr Workflow.

Python
JavaScript
.NET
Java
Go
from dataclasses import dataclass

from datetime import timedelta

import dapr.ext.workflow as wf





@dataclass

class Order:

    cost: float

    product: str

    quantity: int



    def __str__(self):

        return f'{self.product} ({self.quantity})'





@dataclass

class Approval:

    approver: str



    @staticmethod

    def from_dict(dict):

        return Approval(**dict)





def purchase_order_workflow(ctx: wf.DaprWorkflowContext, order: Order):

    # Orders under $1000 are auto-approved

    if order.cost < 1000:

        return "Auto-approved"



    # Orders of $1000 or more require manager approval

    yield ctx.call_activity(send_approval_request, input=order)



    # Approvals must be received within 24 hours or they will be canceled.

    approval_event = ctx.wait_for_external_event("approval_received")

    timeout_event = ctx.create_timer(timedelta(hours=24))

    winner = yield wf.when_any([approval_event, timeout_event])

    if winner == timeout_event:

        return "Cancelled"



    # The order was approved

    yield ctx.call_activity(place_order, input=order)

    approval_details = Approval.from_dict(approval_event.get_result())

    return f"Approved by '{approval_details.approver}'"





def send_approval_request(_, order: Order) -> None:

    print(f'*** Sending approval request for order: {order}')





def place_order(_, order: Order) -> None:

    print(f'*** Placing order: {order}')


The code that delivers the event to resume the workflow execution is external to the workflow. Workflow events can be delivered to a waiting workflow instance using the raise event workflow management API, as shown in the following example:

Python
JavaScript
.NET
Java
Go
from dapr.clients import DaprClient

from dataclasses import asdict



with DaprClient() as d:

    d.raise_workflow_event(

        instance_id=instance_id,

        workflow_component="dapr",

        event_name="approval_received",

        event_data=asdict(Approval("Jane Doe")))


External events don’t have to be directly triggered by humans. They can also be triggered by other systems. For example, a workflow may need to pause and wait for a payment to be received. In this case, a payment system might publish an event to a pub/sub topic on receipt of a payment, and a listener on that topic can raise an event to the workflow using the raise event workflow API.

Compensation

The compensation pattern (also known as the saga pattern) provides a mechanism for rolling back or undoing operations that have already been executed when a workflow fails partway through. This pattern is particularly important for long-running workflows that span multiple microservices where traditional database transactions are not feasible.

In distributed microservice architectures, you often need to coordinate operations across multiple services. When these operations cannot be wrapped in a single transaction, the compensation pattern provides a way to maintain consistency by defining compensating actions for each step in the workflow.

The compensation pattern addresses several critical challenges:

Distributed Transaction Management: When a workflow spans multiple microservices, each with their own data stores, traditional ACID transactions are not possible. The compensation pattern provides transactional consistency by ensuring operations are either all completed successfully or all undone through compensation.
Partial Failure Recovery: If a workflow fails after some steps have completed successfully, the compensation pattern allows you to undo those completed steps gracefully.
Business Process Integrity: Ensures that business processes can be properly rolled back in case of failures, maintaining the integrity of your business operations.
Long-Running Processes: For workflows that may run for hours, days, or longer, traditional locking mechanisms are impractical. Compensation provides a way to handle failures in these scenarios.

Common use cases for the compensation pattern include:

E-commerce Order Processing: Reserve inventory, charge payment, and ship orders. If shipping fails, you need to release the inventory and refund the payment.
Financial Transactions: In a money transfer, if crediting the destination account fails, you need to rollback the debit from the source account.
Resource Provisioning: When provisioning cloud resources across multiple providers, if one step fails, you need to clean up all previously provisioned resources.
Multi-Step Business Processes: Any business process that involves multiple irreversible steps that may need to be undone in case of later failures.

Dapr Workflow provides support for the compensation pattern, allowing you to register compensation activities for each step and execute them in reverse order when needed.

Here’s an example workflow for an e-commerce process:

A workflow is triggered when an order is received.
A reservation is made for the order in the inventory.
The payment is processed.
The order is shipped.
If any of the above actions results in an error, the actions are compensated with another action:
The shipment is cancelled.
The payment is refunded.
The inventory reservation is released.

The following diagram illustrates this flow.

Java
public class PaymentProcessingWorkflow implements Workflow {



    @Override

    public WorkflowStub create() {

        return ctx -> {

            ctx.getLogger().info("Starting Workflow: " + ctx.getName());

            var orderId = ctx.getInput(String.class);

            List<String> compensations = new ArrayList<>();



            try {

                // Step 1: Reserve inventory

                String reservationId = ctx.callActivity(ReserveInventoryActivity.class.getName(), orderId, String.class).await();

                ctx.getLogger().info("Inventory reserved: {}", reservationId);

                compensations.add("ReleaseInventory");



                // Step 2: Process payment

                String paymentId = ctx.callActivity(ProcessPaymentActivity.class.getName(), orderId, String.class).await();

                ctx.getLogger().info("Payment processed: {}", paymentId);

                compensations.add("RefundPayment");



                // Step 3: Ship order

                String shipmentId = ctx.callActivity(ShipOrderActivity.class.getName(), orderId, String.class).await();

                ctx.getLogger().info("Order shipped: {}", shipmentId);

                compensations.add("CancelShipment");



            } catch (TaskFailedException e) {

                ctx.getLogger().error("Activity failed: {}", e.getMessage());



                // Execute compensations in reverse order

                Collections.reverse(compensations);

                for (String compensation : compensations) {

                    try {

                        switch (compensation) {

                            case "CancelShipment":

                                String shipmentCancelResult = ctx.callActivity(

                                    CancelShipmentActivity.class.getName(),

                                    orderId,

                                    String.class).await();

                                ctx.getLogger().info("Shipment cancellation completed: {}", shipmentCancelResult);

                                break;



                            case "RefundPayment":

                                String refundResult = ctx.callActivity(

                                    RefundPaymentActivity.class.getName(),

                                    orderId,

                                    String.class).await();

                                ctx.getLogger().info("Payment refund completed: {}", refundResult);

                                break;



                            case "ReleaseInventory":

                                String releaseResult = ctx.callActivity(

                                    ReleaseInventoryActivity.class.getName(),

                                    orderId,

                                    String.class).await();

                                ctx.getLogger().info("Inventory release completed: {}", releaseResult);

                                break;

                        }

                    } catch (TaskFailedException ex) {

                        ctx.getLogger().error("Compensation activity failed: {}", ex.getMessage());

                    }

                }

                ctx.complete("Order processing failed, compensation applied");

            }



			// Step 4: Send confirmation

			ctx.callActivity(SendConfirmationActivity.class.getName(), orderId, Void.class).await();

            ctx.getLogger().info("Confirmation sent for order: {}", orderId);



            ctx.complete("Order processed successfully: " + orderId);

        };

    }

}



// Example activities

class ReserveInventoryActivity implements WorkflowActivity {

    @Override

    public Object run(WorkflowActivityContext ctx) {

        String orderId = ctx.getInput(String.class);

        // Logic to reserve inventory

        String reservationId = "reservation_" + orderId;

        System.out.println("Reserved inventory for order: " + orderId);

        return reservationId;

    }

}



class ReleaseInventoryActivity implements WorkflowActivity {

    @Override

    public Object run(WorkflowActivityContext ctx) {

        String reservationId = ctx.getInput(String.class);

        // Logic to release inventory reservation

        System.out.println("Released inventory reservation: " + reservationId);

        return "Released: " + reservationId;

    }

}



class ProcessPaymentActivity implements WorkflowActivity {

    @Override

    public Object run(WorkflowActivityContext ctx) {

        String orderId = ctx.getInput(String.class);

        // Logic to process payment

        String paymentId = "payment_" + orderId;

        System.out.println("Processed payment for order: " + orderId);

        return paymentId;

    }

}



class RefundPaymentActivity implements WorkflowActivity {

    @Override

    public Object run(WorkflowActivityContext ctx) {

        String paymentId = ctx.getInput(String.class);

        // Logic to refund payment

        System.out.println("Refunded payment: " + paymentId);

        return "Refunded: " + paymentId;

    }

}



class ShipOrderActivity implements WorkflowActivity {

    @Override

    public Object run(WorkflowActivityContext ctx) {

        String orderId = ctx.getInput(String.class);

        // Logic to ship order

        String shipmentId = "shipment_" + orderId;

        System.out.println("Shipped order: " + orderId);

        return shipmentId;

    }

}



class CancelShipmentActivity implements WorkflowActivity {

    @Override

    public Object run(WorkflowActivityContext ctx) {

        String shipmentId = ctx.getInput(String.class);

        // Logic to cancel shipment

        System.out.println("Canceled shipment: " + shipmentId);

        return "Canceled: " + shipmentId;

    }

}



class SendConfirmationActivity implements WorkflowActivity {

    @Override

    public Object run(WorkflowActivityContext ctx) {

        String orderId = ctx.getInput(String.class);

        // Logic to send confirmation

        System.out.println("Sent confirmation for order: " + orderId);

        return null;

    }

}


The key benefits of using Dapr Workflow’s compensation pattern include:

Compensation Control: You have full control over when and how compensation activities are executed.
Flexible Configuration: You can implement custom logic for determining which compensations to run.
Error Handling: Handle compensation failures according to your specific business requirements.
Simple Implementation: No additional framework dependencies - just standard workflow activities and exception handling.

The compensation pattern ensures that your distributed workflows can maintain consistency and recover gracefully from failures, making it an essential tool for building reliable microservice architectures.

Next steps
Workflow architecture >>
Related links
Try out Dapr Workflows using the quickstart
Workflow overview
Workflow API reference
Try out the following examples:
Python
JavaScript
.NET
Java
Go
Last modified March 3, 2026: Merge pull request #5062 from JoshVanL/wf-versioning-cli-example (3b5020c)
© 2026 The Linux Foundation. All rights reserved. The Linux Foundation has registered trademarks and uses trademarks. For a list of trademarks of The Linux Foundation, please see our Trademark Usage page.
