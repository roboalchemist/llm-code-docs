# Source: https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity

Title: activity package - go.temporal.io/server/chasm/lib/activity - Go Packages

URL Source: https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity

Markdown Content:
*   [Constants](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#pkg-constants)
*   [Variables](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#pkg-variables)
*   [func InternalStatusToAPIStatus(status activitypb.ActivityExecutionStatus) enumspb.ActivityExecutionStatus](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#InternalStatusToAPIStatus)
*   [func NewEmbeddedActivity(ctx chasm.MutableContext, state *activitypb.ActivityState, ...)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#NewEmbeddedActivity)
*   [func ValidateActivityTaskToken(ctx chasm.Context, a *Activity, token *tokenspb.Task) error](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#ValidateActivityTaskToken)
*   [func ValidateAndNormalizeActivityAttributes(activityID string, activityType string, ...) error](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#ValidateAndNormalizeActivityAttributes)
*   [func ValidateDescribeActivityExecutionRequest(req *workflowservice.DescribeActivityExecutionRequest, maxIDLengthLimit int) error](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#ValidateDescribeActivityExecutionRequest)
*   [func ValidatePollActivityExecutionRequest(req *workflowservice.PollActivityExecutionRequest, maxIDLengthLimit int) error](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#ValidatePollActivityExecutionRequest)
*   [type Activity](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#Activity)
*       *   [func NewStandaloneActivity(ctx chasm.MutableContext, ...) (*Activity, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#NewStandaloneActivity)

*       *   [func (a *Activity) HandleCanceled(ctx chasm.MutableContext, event RespondCancelledEvent) (*historyservice.RespondActivityTaskCanceledResponse, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#Activity.HandleCanceled)
    *   [func (a *Activity) HandleCompleted(ctx chasm.MutableContext, event RespondCompletedEvent) (*historyservice.RespondActivityTaskCompletedResponse, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#Activity.HandleCompleted)
    *   [func (a *Activity) HandleFailed(ctx chasm.MutableContext, event RespondFailedEvent) (*historyservice.RespondActivityTaskFailedResponse, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#Activity.HandleFailed)
    *   [func (a *Activity) HandleStarted(ctx chasm.MutableContext, ...) (*historyservice.RecordActivityTaskStartedResponse, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#Activity.HandleStarted)
    *   [func (a *Activity) LifecycleState(_ chasm.Context) chasm.LifecycleState](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#Activity.LifecycleState)
    *   [func (a *Activity) PopulateRecordStartedResponse(ctx chasm.Context, key chasm.ExecutionKey, ...) error](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#Activity.PopulateRecordStartedResponse)
    *   [func (a *Activity) RecordCompleted(ctx chasm.MutableContext, applyFn func(ctx chasm.MutableContext) error) error](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#Activity.RecordCompleted)
    *   [func (a *Activity) RecordHeartbeat(ctx chasm.MutableContext, ...) (*historyservice.RecordActivityTaskHeartbeatResponse, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#Activity.RecordHeartbeat)
    *   [func (a *Activity) SearchAttributes(_ chasm.Context) []chasm.SearchAttributeKeyValue](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#Activity.SearchAttributes)
    *   [func (a *Activity) SetStateMachineState(state activitypb.ActivityExecutionStatus)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#Activity.SetStateMachineState)
    *   [func (a *Activity) StateMachineState() activitypb.ActivityExecutionStatus](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#Activity.StateMachineState)
    *   [func (a *Activity) StoreOrSelf(ctx chasm.Context) ActivityStore](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#Activity.StoreOrSelf)

*   [type ActivityStore](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#ActivityStore)
*   [type Config](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#Config)
*       *   [func ConfigProvider(dc *dynamicconfig.Collection) *Config](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#ConfigProvider)

*   [type FrontendHandler](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#FrontendHandler)
*       *   [func NewFrontendHandler(client activitypb.ActivityServiceClient, config *Config, logger log.Logger, ...) FrontendHandler](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#NewFrontendHandler)

*   [type MetricsHandlerBuilderParams](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#MetricsHandlerBuilderParams)
*   [type RespondCancelledEvent](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#RespondCancelledEvent)
*   [type RespondCompletedEvent](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#RespondCompletedEvent)
*   [type RespondFailedEvent](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#RespondFailedEvent)
*   [type WithToken](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#WithToken)

[View Source](https://github.com/temporalio/temporal/blob/v1.30.0/chasm/lib/activity/activity.go#L30)

const (
	
	WorkflowTypeTag = "__temporal_standalone_activity__"

 TypeSAAlias = "ActivityType"  StatusSAAlias = "ActivityStatus"  TaskQueueSAAlias = "ActivityTaskQueue" )

[View Source](https://github.com/temporalio/temporal/blob/v1.30.0/chasm/lib/activity/frontend.go#L24)

const StandaloneActivityDisabledError = "Standalone activity is disabled"

[View Source](https://github.com/temporalio/temporal/blob/v1.30.0/chasm/lib/activity/config.go#L10)

var (
 Enabled = [dynamicconfig](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/dynamicconfig).[NewNamespaceBoolSetting](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/dynamicconfig#NewNamespaceBoolSetting)( 		"activity.enableStandalone",
		[false](https://pkg.go.dev/builtin#false),
		`Toggles standalone activity functionality on the server.`,
	)

 LongPollTimeout = [dynamicconfig](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/dynamicconfig).[NewNamespaceDurationSetting](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/dynamicconfig#NewNamespaceDurationSetting)( 		"activity.longPollTimeout",
		20*[time](https://pkg.go.dev/time).[Second](https://pkg.go.dev/time#Second),
		`Timeout for activity long-poll requests.`,
	)

 LongPollBuffer = [dynamicconfig](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/dynamicconfig).[NewNamespaceDurationSetting](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/dynamicconfig#NewNamespaceDurationSetting)( 		"activity.longPollBuffer",
		[time](https://pkg.go.dev/time).[Second](https://pkg.go.dev/time#Second),
		`A buffer used to adjust the activity long-poll timeouts.
 Specifically, activity long-poll requests are timed out at a time which leaves at least the buffer's duration
 remaining before the caller's deadline, if permitted by the caller's deadline.`,
	)
)

[View Source](https://github.com/temporalio/temporal/blob/v1.30.0/chasm/lib/activity/fx.go#L10)

var HistoryModule = [fx](https://pkg.go.dev/go.uber.org/fx).[Module](https://pkg.go.dev/go.uber.org/fx#Module)( 	"activity-history",
	[fx](https://pkg.go.dev/go.uber.org/fx).[Provide](https://pkg.go.dev/go.uber.org/fx#Provide)(
		[ConfigProvider](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#ConfigProvider),
		newActivityDispatchTaskExecutor,
		newScheduleToStartTimeoutTaskExecutor,
		newScheduleToCloseTimeoutTaskExecutor,
		newStartToCloseTimeoutTaskExecutor,
		newHeartbeatTimeoutTaskExecutor,
		newHandler,
		newLibrary,
	),
	[fx](https://pkg.go.dev/go.uber.org/fx).[Invoke](https://pkg.go.dev/go.uber.org/fx#Invoke)(func(l *library, registry *[chasm](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm).[Registry](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Registry)) [error](https://pkg.go.dev/builtin#error) {
		return registry.Register(l)
	}),
)

[View Source](https://github.com/temporalio/temporal/blob/v1.30.0/chasm/lib/activity/statemachine.go#L276)

var TransitionCancelRequested = [chasm](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm).[NewTransition](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewTransition)( 	[][activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ActivityExecutionStatus](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ActivityExecutionStatus){
		[activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ACTIVITY_EXECUTION_STATUS_STARTED](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ACTIVITY_EXECUTION_STATUS_STARTED),
		[activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ACTIVITY_EXECUTION_STATUS_SCHEDULED](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ACTIVITY_EXECUTION_STATUS_SCHEDULED),
		[activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ACTIVITY_EXECUTION_STATUS_CANCEL_REQUESTED](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ACTIVITY_EXECUTION_STATUS_CANCEL_REQUESTED),
	},
	[activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ACTIVITY_EXECUTION_STATUS_CANCEL_REQUESTED](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ACTIVITY_EXECUTION_STATUS_CANCEL_REQUESTED),
	func(a *[Activity](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#Activity), ctx [chasm](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm).[MutableContext](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MutableContext), req *[workflowservice](https://pkg.go.dev/go.temporal.io/api/workflowservice/v1).[RequestCancelActivityExecutionRequest](https://pkg.go.dev/go.temporal.io/api/workflowservice/v1#RequestCancelActivityExecutionRequest)) [error](https://pkg.go.dev/builtin#error) {
		a.CancelState = &[activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ActivityCancelState](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ActivityCancelState){
			Identity:    req.GetIdentity(),
			RequestId:   req.GetRequestId(),
			Reason:      req.GetReason(),
			RequestTime: [timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[New](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#New)(ctx.Now(a)),
		}

		return [nil](https://pkg.go.dev/builtin#nil)
	},
)

TransitionCancelRequested transitions to CancelRequested status.

[View Source](https://github.com/temporalio/temporal/blob/v1.30.0/chasm/lib/activity/statemachine.go#L302)

var TransitionCanceled = [chasm](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm).[NewTransition](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewTransition)( 	[][activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ActivityExecutionStatus](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ActivityExecutionStatus){
		[activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ACTIVITY_EXECUTION_STATUS_CANCEL_REQUESTED](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ACTIVITY_EXECUTION_STATUS_CANCEL_REQUESTED),
	},
	[activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ACTIVITY_EXECUTION_STATUS_CANCELED](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ACTIVITY_EXECUTION_STATUS_CANCELED),
	func(a *[Activity](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#Activity), ctx [chasm](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm).[MutableContext](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MutableContext), event cancelEvent) [error](https://pkg.go.dev/builtin#error) {
		return a.StoreOrSelf(ctx).RecordCompleted(ctx, func(ctx [chasm](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm).[MutableContext](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MutableContext)) [error](https://pkg.go.dev/builtin#error) {
			outcome := a.Outcome.Get(ctx)
			failure := &[failurepb](https://pkg.go.dev/go.temporal.io/api/failure/v1).[Failure](https://pkg.go.dev/go.temporal.io/api/failure/v1#Failure){
				Message: "Activity canceled",
				FailureInfo: &[failurepb](https://pkg.go.dev/go.temporal.io/api/failure/v1).[Failure_CanceledFailureInfo](https://pkg.go.dev/go.temporal.io/api/failure/v1#Failure_CanceledFailureInfo){
					CanceledFailureInfo: &[failurepb](https://pkg.go.dev/go.temporal.io/api/failure/v1).[CanceledFailureInfo](https://pkg.go.dev/go.temporal.io/api/failure/v1#CanceledFailureInfo){
						Details: event.details,
					},
				},
			}
			outcome.Variant = &[activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ActivityOutcome_Failed_](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ActivityOutcome_Failed_){
				Failed: &[activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ActivityOutcome_Failed](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ActivityOutcome_Failed){
					Failure: failure,
				},
			}

			a.emitOnCanceledMetrics(ctx, event.handler, event.fromStatus)

			return [nil](https://pkg.go.dev/builtin#nil)
		})
	},
)

TransitionCanceled transitions to Canceled status.

[View Source](https://github.com/temporalio/temporal/blob/v1.30.0/chasm/lib/activity/statemachine.go#L172)

var TransitionCompleted = [chasm](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm).[NewTransition](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewTransition)( 	[][activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ActivityExecutionStatus](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ActivityExecutionStatus){
		[activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ACTIVITY_EXECUTION_STATUS_STARTED](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ACTIVITY_EXECUTION_STATUS_STARTED),
		[activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ACTIVITY_EXECUTION_STATUS_CANCEL_REQUESTED](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ACTIVITY_EXECUTION_STATUS_CANCEL_REQUESTED),
	},
	[activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ACTIVITY_EXECUTION_STATUS_COMPLETED](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ACTIVITY_EXECUTION_STATUS_COMPLETED),
	func(a *[Activity](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#Activity), ctx [chasm](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm).[MutableContext](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MutableContext), event completeEvent) [error](https://pkg.go.dev/builtin#error) {
		return a.StoreOrSelf(ctx).RecordCompleted(ctx, func(ctx [chasm](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm).[MutableContext](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MutableContext)) [error](https://pkg.go.dev/builtin#error) {
			req := event.req.GetCompleteRequest()

			attempt := a.LastAttempt.Get(ctx)
			attempt.CompleteTime = [timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[New](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#New)(ctx.Now(a))
			attempt.LastWorkerIdentity = req.GetIdentity()
			outcome := a.Outcome.Get(ctx)
			outcome.Variant = &[activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ActivityOutcome_Successful_](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ActivityOutcome_Successful_){
				Successful: &[activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ActivityOutcome_Successful](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ActivityOutcome_Successful){
					Output: req.GetResult(),
				},
			}

			a.emitOnCompletedMetrics(ctx, event.metricsHandler)

			return [nil](https://pkg.go.dev/builtin#nil)
		})
	},
)

TransitionCompleted transitions to Completed status.

[View Source](https://github.com/temporalio/temporal/blob/v1.30.0/chasm/lib/activity/statemachine.go#L205)

var TransitionFailed = [chasm](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm).[NewTransition](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewTransition)( 	[][activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ActivityExecutionStatus](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ActivityExecutionStatus){
		[activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ACTIVITY_EXECUTION_STATUS_STARTED](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ACTIVITY_EXECUTION_STATUS_STARTED),
		[activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ACTIVITY_EXECUTION_STATUS_CANCEL_REQUESTED](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ACTIVITY_EXECUTION_STATUS_CANCEL_REQUESTED),
	},
	[activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ACTIVITY_EXECUTION_STATUS_FAILED](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ACTIVITY_EXECUTION_STATUS_FAILED),
	func(a *[Activity](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#Activity), ctx [chasm](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm).[MutableContext](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MutableContext), event failedEvent) [error](https://pkg.go.dev/builtin#error) {
		return a.StoreOrSelf(ctx).RecordCompleted(ctx, func(ctx [chasm](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm).[MutableContext](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MutableContext)) [error](https://pkg.go.dev/builtin#error) {
			req := event.req.GetFailedRequest()

			if details := req.GetLastHeartbeatDetails(); details != [nil](https://pkg.go.dev/builtin#nil) {
				heartbeat := a.getOrCreateLastHeartbeat(ctx)
				heartbeat.Details = details
				heartbeat.RecordedTime = [timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[New](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#New)(ctx.Now(a))
			}
			attempt := a.LastAttempt.Get(ctx)
			attempt.LastWorkerIdentity = req.GetIdentity()

			if err := a.recordFailedAttempt(ctx, 0, req.GetFailure(), ctx.Now(a), [true](https://pkg.go.dev/builtin#true)); err != [nil](https://pkg.go.dev/builtin#nil) {
				return err
			}

			a.emitOnFailedMetrics(ctx, event.metricsHandler)

			return [nil](https://pkg.go.dev/builtin#nil)
		})
	},
)

TransitionFailed transitions to Failed status.

[View Source](https://github.com/temporalio/temporal/blob/v1.30.0/chasm/lib/activity/statemachine.go#L86)

var TransitionRescheduled = [chasm](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm).[NewTransition](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewTransition)( 	[][activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ActivityExecutionStatus](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ActivityExecutionStatus){
		[activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ACTIVITY_EXECUTION_STATUS_STARTED](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ACTIVITY_EXECUTION_STATUS_STARTED),
	},
	[activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ACTIVITY_EXECUTION_STATUS_SCHEDULED](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ACTIVITY_EXECUTION_STATUS_SCHEDULED),
	func(a *[Activity](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#Activity), ctx [chasm](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm).[MutableContext](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MutableContext), event rescheduleEvent) [error](https://pkg.go.dev/builtin#error) {
		attempt := a.LastAttempt.Get(ctx)
		currentTime := ctx.Now(a)
		attempt.Count += 1

		err := a.recordFailedAttempt(ctx, event.retryInterval, event.failure, currentTime, [false](https://pkg.go.dev/builtin#false))
		if err != [nil](https://pkg.go.dev/builtin#nil) {
			return err
		}

		if timeout := a.GetScheduleToStartTimeout().AsDuration(); timeout > 0 {
			ctx.AddTask(
				a,
				[chasm](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm).[TaskAttributes](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#TaskAttributes){
					ScheduledTime: currentTime.Add(timeout).Add(event.retryInterval),
				},
				&[activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ScheduleToStartTimeoutTask](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ScheduleToStartTimeoutTask){
					Attempt: attempt.GetCount(),
				})
		}

		ctx.AddTask(
			a,
			[chasm](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm).[TaskAttributes](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#TaskAttributes){
				ScheduledTime: currentTime.Add(event.retryInterval),
			},
			&[activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ActivityDispatchTask](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ActivityDispatchTask){
				Attempt: attempt.GetCount(),
			})

		return [nil](https://pkg.go.dev/builtin#nil)
	},
)

TransitionRescheduled transitions to Scheduled from Started, which happens on retries. The event to pass in is the failure to be recorded from the previously failed attempt.

[View Source](https://github.com/temporalio/temporal/blob/v1.30.0/chasm/lib/activity/statemachine.go#L37)

var TransitionScheduled = [chasm](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm).[NewTransition](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewTransition)( 	[][activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ActivityExecutionStatus](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ActivityExecutionStatus){
		[activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ACTIVITY_EXECUTION_STATUS_UNSPECIFIED](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ACTIVITY_EXECUTION_STATUS_UNSPECIFIED),
	},
	[activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ACTIVITY_EXECUTION_STATUS_SCHEDULED](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ACTIVITY_EXECUTION_STATUS_SCHEDULED),
	func(a *[Activity](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#Activity), ctx [chasm](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm).[MutableContext](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MutableContext), _ [any](https://pkg.go.dev/builtin#any)) [error](https://pkg.go.dev/builtin#error) {
		attempt := a.LastAttempt.Get(ctx)
		currentTime := ctx.Now(a)
		attempt.Count += 1

		if timeout := a.GetScheduleToStartTimeout().AsDuration(); timeout > 0 {
			ctx.AddTask(
				a,
				[chasm](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm).[TaskAttributes](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#TaskAttributes){
					ScheduledTime: currentTime.Add(timeout),
				},
				&[activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ScheduleToStartTimeoutTask](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ScheduleToStartTimeoutTask){
					Attempt: attempt.GetCount(),
				})
		}

		if timeout := a.GetScheduleToCloseTimeout().AsDuration(); timeout > 0 {
			ctx.AddTask(
				a,
				[chasm](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm).[TaskAttributes](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#TaskAttributes){
					ScheduledTime: currentTime.Add(timeout),
				},
				&[activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ScheduleToCloseTimeoutTask](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ScheduleToCloseTimeoutTask){})
		}

		ctx.AddTask(
			a,
			[chasm](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm).[TaskAttributes](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#TaskAttributes){},
			&[activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ActivityDispatchTask](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ActivityDispatchTask){
				Attempt: attempt.GetCount(),
			})

		return [nil](https://pkg.go.dev/builtin#nil)
	},
)

TransitionScheduled transitions to Scheduled status. This is only called on the initial scheduling of the activity.

[View Source](https://github.com/temporalio/temporal/blob/v1.30.0/chasm/lib/activity/statemachine.go#L126)

var TransitionStarted = [chasm](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm).[NewTransition](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewTransition)( 	[][activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ActivityExecutionStatus](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ActivityExecutionStatus){
		[activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ACTIVITY_EXECUTION_STATUS_SCHEDULED](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ACTIVITY_EXECUTION_STATUS_SCHEDULED),
	},
	[activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ACTIVITY_EXECUTION_STATUS_STARTED](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ACTIVITY_EXECUTION_STATUS_STARTED),
	func(a *[Activity](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#Activity), ctx [chasm](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm).[MutableContext](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MutableContext), request *[historyservice](https://pkg.go.dev/go.temporal.io/server@v1.30.0/api/historyservice/v1).[RecordActivityTaskStartedRequest](https://pkg.go.dev/go.temporal.io/server@v1.30.0/api/historyservice/v1#RecordActivityTaskStartedRequest)) [error](https://pkg.go.dev/builtin#error) {
		attempt := a.LastAttempt.Get(ctx)
		attempt.StartedTime = [timestamppb](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb).[New](https://pkg.go.dev/google.golang.org/protobuf/types/known/timestamppb#New)(ctx.Now(a))
		attempt.LastWorkerIdentity = request.GetPollRequest().GetIdentity()
		if versionDirective := request.GetVersionDirective().GetDeploymentVersion(); versionDirective != [nil](https://pkg.go.dev/builtin#nil) {
			attempt.LastDeploymentVersion = &[deploymentpb](https://pkg.go.dev/go.temporal.io/api/deployment/v1).[WorkerDeploymentVersion](https://pkg.go.dev/go.temporal.io/api/deployment/v1#WorkerDeploymentVersion){
				BuildId:        versionDirective.GetBuildId(),
				DeploymentName: versionDirective.GetDeploymentName(),
			}
		}
		startTime := attempt.GetStartedTime().AsTime()
		ctx.AddTask(
			a,
			[chasm](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm).[TaskAttributes](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#TaskAttributes){
				ScheduledTime: startTime.Add(a.GetStartToCloseTimeout().AsDuration()),
			},
			&[activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[StartToCloseTimeoutTask](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#StartToCloseTimeoutTask){
				Attempt: a.LastAttempt.Get(ctx).GetCount(),
			})

		if heartbeatTimeout := a.GetHeartbeatTimeout().AsDuration(); heartbeatTimeout > 0 {
			ctx.AddTask(
				a,
				[chasm](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm).[TaskAttributes](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#TaskAttributes){
					ScheduledTime: startTime.Add(heartbeatTimeout),
				},
				&[activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[HeartbeatTimeoutTask](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#HeartbeatTimeoutTask){
					Attempt: attempt.GetCount(),
				})
		}

		return [nil](https://pkg.go.dev/builtin#nil)
	},
)

TransitionStarted transitions to Started status.

[View Source](https://github.com/temporalio/temporal/blob/v1.30.0/chasm/lib/activity/statemachine.go#L235)

var TransitionTerminated = [chasm](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm).[NewTransition](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewTransition)( 	[][activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ActivityExecutionStatus](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ActivityExecutionStatus){
		[activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ACTIVITY_EXECUTION_STATUS_SCHEDULED](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ACTIVITY_EXECUTION_STATUS_SCHEDULED),
		[activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ACTIVITY_EXECUTION_STATUS_STARTED](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ACTIVITY_EXECUTION_STATUS_STARTED),
		[activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ACTIVITY_EXECUTION_STATUS_CANCEL_REQUESTED](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ACTIVITY_EXECUTION_STATUS_CANCEL_REQUESTED),
	},
	[activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ACTIVITY_EXECUTION_STATUS_TERMINATED](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ACTIVITY_EXECUTION_STATUS_TERMINATED),
	func(a *[Activity](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#Activity), ctx [chasm](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm).[MutableContext](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MutableContext), event terminateEvent) [error](https://pkg.go.dev/builtin#error) {
		return a.StoreOrSelf(ctx).RecordCompleted(ctx, func(ctx [chasm](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm).[MutableContext](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MutableContext)) [error](https://pkg.go.dev/builtin#error) {
			req := event.request.GetFrontendRequest()

			a.TerminateState = &[activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ActivityTerminateState](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ActivityTerminateState){
				RequestId: req.GetRequestId(),
			}
			outcome := a.Outcome.Get(ctx)
			failure := &[failurepb](https://pkg.go.dev/go.temporal.io/api/failure/v1).[Failure](https://pkg.go.dev/go.temporal.io/api/failure/v1#Failure){

				Message:     req.GetReason(),
				FailureInfo: &[failurepb](https://pkg.go.dev/go.temporal.io/api/failure/v1).[Failure_TerminatedFailureInfo](https://pkg.go.dev/go.temporal.io/api/failure/v1#Failure_TerminatedFailureInfo){},
			}
			outcome.Variant = &[activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ActivityOutcome_Failed_](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ActivityOutcome_Failed_){
				Failed: &[activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ActivityOutcome_Failed](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ActivityOutcome_Failed){
					Failure: failure,
				},
			}

			metricsHandler := enrichMetricsHandler(
				a,
				event.MetricsHandlerBuilderParams.Handler,
				event.MetricsHandlerBuilderParams.NamespaceName,
				[metrics](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/metrics).[ActivityTerminatedScope](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/metrics#ActivityTerminatedScope),
				event.MetricsHandlerBuilderParams.BreakdownMetricsByTaskQueue)

			[metrics](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/metrics).[ActivityTerminate](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/metrics#ActivityTerminate).With(metricsHandler).Record(1)

			return [nil](https://pkg.go.dev/builtin#nil)
		})
	},
)

TransitionTerminated transitions to Terminated status.

[View Source](https://github.com/temporalio/temporal/blob/v1.30.0/chasm/lib/activity/statemachine.go#L338)

var TransitionTimedOut = [chasm](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm).[NewTransition](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewTransition)( 	[][activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ActivityExecutionStatus](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ActivityExecutionStatus){
		[activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ACTIVITY_EXECUTION_STATUS_SCHEDULED](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ACTIVITY_EXECUTION_STATUS_SCHEDULED),
		[activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ACTIVITY_EXECUTION_STATUS_STARTED](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ACTIVITY_EXECUTION_STATUS_STARTED),
		[activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ACTIVITY_EXECUTION_STATUS_CANCEL_REQUESTED](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ACTIVITY_EXECUTION_STATUS_CANCEL_REQUESTED),
	},
	[activitypb](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1).[ACTIVITY_EXECUTION_STATUS_TIMED_OUT](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity/gen/activitypb/v1#ACTIVITY_EXECUTION_STATUS_TIMED_OUT),
	func(a *[Activity](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#Activity), ctx [chasm](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm).[MutableContext](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MutableContext), event timeoutEvent) [error](https://pkg.go.dev/builtin#error) {
		timeoutType := event.timeoutType

		return a.StoreOrSelf(ctx).RecordCompleted(ctx, func(ctx [chasm](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm).[MutableContext](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MutableContext)) [error](https://pkg.go.dev/builtin#error) {
			var err [error](https://pkg.go.dev/builtin#error)
			switch timeoutType {
			case [enumspb](https://pkg.go.dev/go.temporal.io/api/enums/v1).[TIMEOUT_TYPE_SCHEDULE_TO_START](https://pkg.go.dev/go.temporal.io/api/enums/v1#TIMEOUT_TYPE_SCHEDULE_TO_START),
				[enumspb](https://pkg.go.dev/go.temporal.io/api/enums/v1).[TIMEOUT_TYPE_SCHEDULE_TO_CLOSE](https://pkg.go.dev/go.temporal.io/api/enums/v1#TIMEOUT_TYPE_SCHEDULE_TO_CLOSE):
				err = a.recordScheduleToStartOrCloseTimeoutFailure(ctx, timeoutType)
			case [enumspb](https://pkg.go.dev/go.temporal.io/api/enums/v1).[TIMEOUT_TYPE_START_TO_CLOSE](https://pkg.go.dev/go.temporal.io/api/enums/v1#TIMEOUT_TYPE_START_TO_CLOSE):
				failure := createStartToCloseTimeoutFailure()
				err = a.recordFailedAttempt(ctx, 0, failure, ctx.Now(a), [true](https://pkg.go.dev/builtin#true))
			case [enumspb](https://pkg.go.dev/go.temporal.io/api/enums/v1).[TIMEOUT_TYPE_HEARTBEAT](https://pkg.go.dev/go.temporal.io/api/enums/v1#TIMEOUT_TYPE_HEARTBEAT):
				failure := createHeartbeatTimeoutFailure()
				err = a.recordFailedAttempt(ctx, 0, failure, ctx.Now(a), [true](https://pkg.go.dev/builtin#true))
			default:
				err = [fmt](https://pkg.go.dev/fmt).[Errorf](https://pkg.go.dev/fmt#Errorf)("unhandled activity timeout: %v", timeoutType)
			}
			if err != [nil](https://pkg.go.dev/builtin#nil) {
				return err
			}

			a.emitOnTimedOutMetrics(ctx, event.metricsHandler, timeoutType, event.fromStatus)

			return [nil](https://pkg.go.dev/builtin#nil)
		})
	},
)

TransitionTimedOut transitions to TimedOut status.

InternalStatusToAPIStatus converts internal activity execution status to API status.

ValidateActivityTaskToken validates a task token against the current activity state.

#### func [ValidateAndNormalizeActivityAttributes](https://github.com/temporalio/temporal/blob/v1.30.0/chasm/lib/activity/validator.go#L37)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#ValidateAndNormalizeActivityAttributes "Go to ValidateAndNormalizeActivityAttributes")

ValidateAndNormalizeActivityAttributes validates and normalizes the common activity request attributes. This validation is shared by both standalone and embedded activities. IMPORTANT: this method mutates the input params; in cases where it's critical to maintain immutability (i.e., when incoming request can potentially be retried), clone the params first before passing it in.

The timeout normalization logic is as follows: 1. If ScheduleToClose is set, fill in missing ScheduleToStart and StartToClose from ScheduleToClose 2. If StartToClose is set but ScheduleToClose is not set, set ScheduleToClose to runTimeout, and fill in missing ScheduleToStart from runTimeout 3. If neither ScheduleToClose nor StartToClose is set, return error 4. Ensure all timeouts do not exceed runTimeout if runTimeout is set (>0) 5. Ensure HeartbeatTimeout does not exceed StartToClose

ValidateDescribeActivityExecutionRequest validates DescribeActivityExecutionRequest.

ValidatePollActivityExecutionRequest validates PollActivityExecutionRequest.

Activity component represents an activity execution persistence object and can be either standalone activity or one embedded within a workflow.

#### func [NewStandaloneActivity](https://github.com/temporalio/temporal/blob/v1.30.0/chasm/lib/activity/activity.go#L138)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#NewStandaloneActivity "Go to NewStandaloneActivity")

NewStandaloneActivity creates a new activity component and adds associated tasks to start execution.

#### func (*Activity) [HandleCanceled](https://github.com/temporalio/temporal/blob/v1.30.0/chasm/lib/activity/activity.go#L322)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#Activity.HandleCanceled "Go to Activity.HandleCanceled")

HandleCanceled updates the activity on activity canceled.

#### func (*Activity) [HandleCompleted](https://github.com/temporalio/temporal/blob/v1.30.0/chasm/lib/activity/activity.go#L248)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#Activity.HandleCompleted "Go to Activity.HandleCompleted")

HandleCompleted updates the activity on activity completion.

#### func (*Activity) [HandleFailed](https://github.com/temporalio/temporal/blob/v1.30.0/chasm/lib/activity/activity.go#L276)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#Activity.HandleFailed "Go to Activity.HandleFailed")

HandleFailed updates the activity on activity failure. if the activity is retryable, it will be rescheduled for retry instead.

#### func (*Activity) [HandleStarted](https://github.com/temporalio/temporal/blob/v1.30.0/chasm/lib/activity/activity.go#L200)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#Activity.HandleStarted "Go to Activity.HandleStarted")

HandleStarted updates the activity on recording activity task started and populates the response.

PopulateRecordStartedResponse populates the response for HandleStarted.

RecordCompleted applies the provided function to record activity completion.

RecordHeartbeat records a heartbeat for the activity.

SearchAttributes implements chasm.VisibilitySearchAttributesProvider interface. Returns the current search attribute values for this activity execution.

SetStateMachineState sets the status of the activity.

StateMachineState returns the current status of the activity.

StoreOrSelf returns the store for the activity. If the store is not set as a field (e.g. standalone activities), it returns the activity itself.

#### type [FrontendHandler](https://github.com/temporalio/temporal/blob/v1.30.0/chasm/lib/activity/frontend.go#L26)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#FrontendHandler "Go to FrontendHandler")

type FrontendHandler interface {
 StartActivityExecution(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[workflowservice](https://pkg.go.dev/go.temporal.io/api/workflowservice/v1).[StartActivityExecutionRequest](https://pkg.go.dev/go.temporal.io/api/workflowservice/v1#StartActivityExecutionRequest)) (*[workflowservice](https://pkg.go.dev/go.temporal.io/api/workflowservice/v1).[StartActivityExecutionResponse](https://pkg.go.dev/go.temporal.io/api/workflowservice/v1#StartActivityExecutionResponse), [error](https://pkg.go.dev/builtin#error))  DescribeActivityExecution(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[workflowservice](https://pkg.go.dev/go.temporal.io/api/workflowservice/v1).[DescribeActivityExecutionRequest](https://pkg.go.dev/go.temporal.io/api/workflowservice/v1#DescribeActivityExecutionRequest)) (*[workflowservice](https://pkg.go.dev/go.temporal.io/api/workflowservice/v1).[DescribeActivityExecutionResponse](https://pkg.go.dev/go.temporal.io/api/workflowservice/v1#DescribeActivityExecutionResponse), [error](https://pkg.go.dev/builtin#error))  PollActivityExecution(ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), req *[workflowservice](https://pkg.go.dev/go.temporal.io/api/workflowservice/v1).[PollActivityExecutionRequest](https://pkg.go.dev/go.temporal.io/api/workflowservice/v1#PollActivityExecutionRequest)) (*[workflowservice](https://pkg.go.dev/go.temporal.io/api/workflowservice/v1).[PollActivityExecutionResponse](https://pkg.go.dev/go.temporal.io/api/workflowservice/v1#PollActivityExecutionResponse), [error](https://pkg.go.dev/builtin#error))  CountActivityExecutions([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *[workflowservice](https://pkg.go.dev/go.temporal.io/api/workflowservice/v1).[CountActivityExecutionsRequest](https://pkg.go.dev/go.temporal.io/api/workflowservice/v1#CountActivityExecutionsRequest)) (*[workflowservice](https://pkg.go.dev/go.temporal.io/api/workflowservice/v1).[CountActivityExecutionsResponse](https://pkg.go.dev/go.temporal.io/api/workflowservice/v1#CountActivityExecutionsResponse), [error](https://pkg.go.dev/builtin#error))  DeleteActivityExecution([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *[workflowservice](https://pkg.go.dev/go.temporal.io/api/workflowservice/v1).[DeleteActivityExecutionRequest](https://pkg.go.dev/go.temporal.io/api/workflowservice/v1#DeleteActivityExecutionRequest)) (*[workflowservice](https://pkg.go.dev/go.temporal.io/api/workflowservice/v1).[DeleteActivityExecutionResponse](https://pkg.go.dev/go.temporal.io/api/workflowservice/v1#DeleteActivityExecutionResponse), [error](https://pkg.go.dev/builtin#error))  ListActivityExecutions([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *[workflowservice](https://pkg.go.dev/go.temporal.io/api/workflowservice/v1).[ListActivityExecutionsRequest](https://pkg.go.dev/go.temporal.io/api/workflowservice/v1#ListActivityExecutionsRequest)) (*[workflowservice](https://pkg.go.dev/go.temporal.io/api/workflowservice/v1).[ListActivityExecutionsResponse](https://pkg.go.dev/go.temporal.io/api/workflowservice/v1#ListActivityExecutionsResponse), [error](https://pkg.go.dev/builtin#error))  RequestCancelActivityExecution([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *[workflowservice](https://pkg.go.dev/go.temporal.io/api/workflowservice/v1).[RequestCancelActivityExecutionRequest](https://pkg.go.dev/go.temporal.io/api/workflowservice/v1#RequestCancelActivityExecutionRequest)) (*[workflowservice](https://pkg.go.dev/go.temporal.io/api/workflowservice/v1).[RequestCancelActivityExecutionResponse](https://pkg.go.dev/go.temporal.io/api/workflowservice/v1#RequestCancelActivityExecutionResponse), [error](https://pkg.go.dev/builtin#error))  TerminateActivityExecution([context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context), *[workflowservice](https://pkg.go.dev/go.temporal.io/api/workflowservice/v1).[TerminateActivityExecutionRequest](https://pkg.go.dev/go.temporal.io/api/workflowservice/v1#TerminateActivityExecutionRequest)) (*[workflowservice](https://pkg.go.dev/go.temporal.io/api/workflowservice/v1).[TerminateActivityExecutionResponse](https://pkg.go.dev/go.temporal.io/api/workflowservice/v1#TerminateActivityExecutionResponse), [error](https://pkg.go.dev/builtin#error))  IsStandaloneActivityEnabled(namespaceName [string](https://pkg.go.dev/builtin#string)) [bool](https://pkg.go.dev/builtin#bool)}

#### func [NewFrontendHandler](https://github.com/temporalio/temporal/blob/v1.30.0/chasm/lib/activity/frontend.go#L50)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#NewFrontendHandler "Go to NewFrontendHandler")

NewFrontendHandler creates a new FrontendHandler instance for processing activity frontend requests.

#### type [MetricsHandlerBuilderParams](https://github.com/temporalio/temporal/blob/v1.30.0/chasm/lib/activity/activity.go#L84)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm/lib/activity#MetricsHandlerBuilderParams "Go to MetricsHandlerBuilderParams")

MetricsHandlerBuilderParams contains parameters for building/enriching a metrics handler for activity operations

RespondCancelledEvent wraps the RespondActivityTaskCanceledRequest with context-specific data.

RespondCompletedEvent wraps the RespondActivityTaskCompletedRequest with context-specific data.

RespondFailedEvent wraps the RespondActivityTaskFailedRequest with context-specific data.

WithToken wraps a request with its deserialized task token.
