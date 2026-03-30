# Source: https://docs.temporal.io/develop/go/cancellation

Title: Interrupt a Workflow - Go SDK | Temporal Platform Documentation

URL Source: https://docs.temporal.io/develop/go/cancellation

Published Time: Fri, 27 Feb 2026 22:38:01 GMT

Markdown Content:
This pages shows the following:

*   How to handle a Cancellation request within a Workflow.
*   How to set an Activity Heartbeat Timeout.
*   How to listen for and handle a Cancellation request within an Activity.
*   How to send a Cancellation request from a Temporal Client.
*   Heartbeating after a Cancellation.

Handle Cancellation in Workflow[​](https://docs.temporal.io/develop/go/cancellation#handle-cancellation-in-workflow "Direct link to Handle Cancellation in Workflow")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------

**How to handle a Cancellation in a Workflow in Go.**

Workflow Definitions can be written to handle execution cancellation requests with Go's `defer` and the `workflow.NewDisconnectedContext` API. In the Workflow Definition, there is a special Activity that handles clean up should the execution be cancelled.

If the Workflow receives a Cancellation Request, but all Activities gracefully handle the Cancellation, and/or no Activities are skipped then the Workflow status will be Complete. It is completely up to the needs of the business process and your use case which determines whether you want to return the Cancellation error to show a Canceled status or Complete status regardless of whether a Cancellation has propagated to and/or skipped Activities.

[sample-apps/go/features/cancellation/workflow.go](https://github.com/temporalio/documentation/blob/main/sample-apps/go/features/cancellation/workflow.go)

`// ...// YourWorkflow is a Workflow Definition that shows how it can be canceled.func YourWorkflow(ctx workflow.Context) error {// ...	activityOptions := workflow.ActivityOptions{// ...		HeartbeatTimeout:    5 * time.Second,		// Set WaitForCancellation to true to have the Workflow wait to return		// until all in progress Activities have completed, failed, or accepted the Cancellation.		WaitForCancellation: true,	}	defer func() {		// This logic ensures cleanup only happens if there is a Cancelation error		if !errors.Is(ctx.Err(), workflow.ErrCanceled) {			return		}		// For the Workflow to execute an Activity after it receives a Cancellation Request		// It has to get a new disconnected context		newCtx, _ := workflow.NewDisconnectedContext(ctx)		// This Activity is only executed if		err := workflow.ExecuteActivity(newCtx, a.CleanupActivity).Get(ctx, nil)		if err != nil {			logger.Error("CleanupActivity failed", "Error", err)		}	}()// ...	err := workflow.ExecuteActivity(ctx, a.ActivityToBeCanceled).Get(ctx, &result)// ...	// This call to execute the Activity is expected to return an error "canceled".	// And the Activity Execution is skipped.	err = workflow.ExecuteActivity(ctx, a.ActivityToBeSkipped).Get(ctx, nil)// ...	// Return any errors.	// If a CanceledError is returned, the Workflow changes to a Canceled state.	return err}`

Handle Cancellation in an Activity[​](https://docs.temporal.io/develop/go/cancellation#handle-cancellation-in-an-activity "Direct link to Handle Cancellation in an Activity")
------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

**How to handle a Cancellation in an Activity in Go.**

Ensure that the Activity is Heartbeating to receive the Cancellation request and stop execution.

`// ActivityToBeCanceled is the Activity that will respond to the Cancellation Requestfunc (a *Activities) ActivityToBeCanceled(ctx context.Context) (string, error) {// ...	// A for select statement is a common approach to listening for a Cancellation is an Activity	for {		select {		case <-time.After(1 * time.Second):			logger.Info("Heartbeating...")			activity.RecordHeartbeat(ctx, "")		// Listen for ctx.Done() to know if a Cancellation Request has propagated to the Activity.		case <-ctx.Done():			logger.Info("This Activity is canceled!")			return "I am canceled by Done", nil		}	}}// ...`

Request Cancellation[​](https://docs.temporal.io/develop/go/cancellation#request-cancellation "Direct link to Request Cancellation")
------------------------------------------------------------------------------------------------------------------------------------

**How to request Cancellation of a Workflow and Activities in Go.**

Use the `CancelWorkflow` API to cancel a Workflow Execution using its Id.

`func main() {// ...	// Call the CancelWorkflow API to cancel a Workflow	// In this call we are relying on the Workflow Id only.	// But a Run Id can also be supplied to ensure the correct Workflow is Canceled.	err = temporalClient.CancelWorkflow(context.Background(), cancellation.WorkflowId, "")	if err != nil {		log.Fatalln("Unable to cancel Workflow Execution", err)	}// ...}`

Heartbeating after a Cancellation[​](https://docs.temporal.io/develop/go/cancellation#heartbeating-after-a-cancellation "Direct link to Heartbeating after a Cancellation")
---------------------------------------------------------------------------------------------------------------------------------------------------------------------------

Sometimes you may want to continue running your Activity, even after a Cancellation has been issued. You may want to completely ignore the cancellation and continue Activity execution, including Heartbeating, or you may want to send one final Heartbeat after Cancellation. Even though the context is cancelled when the Workflow is Cancelled, you are still able to send Activity Heartbeats.

When you call `activity.RecordHeartbeat` after Cancellation has occurred, a `WARN RecordActivityHeartbeat with error Error context canceled` message will be logged, and a `context canceled` error will be returned from the call. However, the Heartbeat **has** still been sent.

Reset a Workflow Execution[​](https://docs.temporal.io/develop/go/cancellation#reset "Direct link to Reset a Workflow Execution")
---------------------------------------------------------------------------------------------------------------------------------

Resetting a Workflow Execution terminates the current Workflow Execution and starts a new Workflow Execution from a point you specify in its Event History. Use reset when a Workflow is blocked due to a non-deterministic error or other issues that prevent it from completing.

When you reset a Workflow, the Event History up to the reset point is copied to the new Workflow Execution, and the Workflow resumes from that point with the current code. Reset only works if you've fixed the underlying issue, such as removing non-deterministic code. Any progress made after the reset point will be discarded. Provide a reason when resetting, as it will be recorded in the Event History.

*   Web UI
*   Temporal CLI

1.   Navigate to the Workflow Execution details page,
2.   Click the **Reset** button in the top right dropdown menu,
3.   Select the Event ID to reset to,
4.   Provide a reason for the reset,
5.   Confirm the reset.

The Web UI shows available reset points and creates a link to the new Workflow Execution after the reset completes.
