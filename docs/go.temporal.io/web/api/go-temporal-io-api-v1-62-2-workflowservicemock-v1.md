# Source: https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1

Title: workflowservicemock package - go.temporal.io/api/workflowservicemock/v1 - Go Packages

URL Source: https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1

Markdown Content:
Package workflowservicemock is a generated GoMock package.

*   [type MockUnsafeWorkflowServiceServer](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockUnsafeWorkflowServiceServer)
*       *   [func NewMockUnsafeWorkflowServiceServer(ctrl *gomock.Controller) *MockUnsafeWorkflowServiceServer](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#NewMockUnsafeWorkflowServiceServer)

*       *   [func (m *MockUnsafeWorkflowServiceServer) EXPECT() *MockUnsafeWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockUnsafeWorkflowServiceServer.EXPECT)

*   [type MockUnsafeWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockUnsafeWorkflowServiceServerMockRecorder)
*   [type MockWorkflowServiceClient](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient)
*       *   [func NewMockWorkflowServiceClient(ctrl *gomock.Controller) *MockWorkflowServiceClient](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#NewMockWorkflowServiceClient)

*       *   [func (m *MockWorkflowServiceClient) CountActivityExecutions(ctx context.Context, in *workflowservice.CountActivityExecutionsRequest, ...) (*workflowservice.CountActivityExecutionsResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.CountActivityExecutions)
    *   [func (m *MockWorkflowServiceClient) CountSchedules(ctx context.Context, in *workflowservice.CountSchedulesRequest, ...) (*workflowservice.CountSchedulesResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.CountSchedules)
    *   [func (m *MockWorkflowServiceClient) CountWorkflowExecutions(ctx context.Context, in *workflowservice.CountWorkflowExecutionsRequest, ...) (*workflowservice.CountWorkflowExecutionsResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.CountWorkflowExecutions)
    *   [func (m *MockWorkflowServiceClient) CreateSchedule(ctx context.Context, in *workflowservice.CreateScheduleRequest, ...) (*workflowservice.CreateScheduleResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.CreateSchedule)
    *   [func (m *MockWorkflowServiceClient) CreateWorkflowRule(ctx context.Context, in *workflowservice.CreateWorkflowRuleRequest, ...) (*workflowservice.CreateWorkflowRuleResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.CreateWorkflowRule)
    *   [func (m *MockWorkflowServiceClient) DeleteActivityExecution(ctx context.Context, in *workflowservice.DeleteActivityExecutionRequest, ...) (*workflowservice.DeleteActivityExecutionResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.DeleteActivityExecution)
    *   [func (m *MockWorkflowServiceClient) DeleteSchedule(ctx context.Context, in *workflowservice.DeleteScheduleRequest, ...) (*workflowservice.DeleteScheduleResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.DeleteSchedule)
    *   [func (m *MockWorkflowServiceClient) DeleteWorkerDeployment(ctx context.Context, in *workflowservice.DeleteWorkerDeploymentRequest, ...) (*workflowservice.DeleteWorkerDeploymentResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.DeleteWorkerDeployment)
    *   [func (m *MockWorkflowServiceClient) DeleteWorkerDeploymentVersion(ctx context.Context, in *workflowservice.DeleteWorkerDeploymentVersionRequest, ...) (*workflowservice.DeleteWorkerDeploymentVersionResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.DeleteWorkerDeploymentVersion)
    *   [func (m *MockWorkflowServiceClient) DeleteWorkflowExecution(ctx context.Context, in *workflowservice.DeleteWorkflowExecutionRequest, ...) (*workflowservice.DeleteWorkflowExecutionResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.DeleteWorkflowExecution)
    *   [func (m *MockWorkflowServiceClient) DeleteWorkflowRule(ctx context.Context, in *workflowservice.DeleteWorkflowRuleRequest, ...) (*workflowservice.DeleteWorkflowRuleResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.DeleteWorkflowRule)
    *   [func (m *MockWorkflowServiceClient) DeprecateNamespace(ctx context.Context, in *workflowservice.DeprecateNamespaceRequest, ...) (*workflowservice.DeprecateNamespaceResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.DeprecateNamespace)
    *   [func (m *MockWorkflowServiceClient) DescribeActivityExecution(ctx context.Context, in *workflowservice.DescribeActivityExecutionRequest, ...) (*workflowservice.DescribeActivityExecutionResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.DescribeActivityExecution)
    *   [func (m *MockWorkflowServiceClient) DescribeBatchOperation(ctx context.Context, in *workflowservice.DescribeBatchOperationRequest, ...) (*workflowservice.DescribeBatchOperationResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.DescribeBatchOperation)
    *   [func (m *MockWorkflowServiceClient) DescribeDeployment(ctx context.Context, in *workflowservice.DescribeDeploymentRequest, ...) (*workflowservice.DescribeDeploymentResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.DescribeDeployment)
    *   [func (m *MockWorkflowServiceClient) DescribeNamespace(ctx context.Context, in *workflowservice.DescribeNamespaceRequest, ...) (*workflowservice.DescribeNamespaceResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.DescribeNamespace)
    *   [func (m *MockWorkflowServiceClient) DescribeSchedule(ctx context.Context, in *workflowservice.DescribeScheduleRequest, ...) (*workflowservice.DescribeScheduleResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.DescribeSchedule)
    *   [func (m *MockWorkflowServiceClient) DescribeTaskQueue(ctx context.Context, in *workflowservice.DescribeTaskQueueRequest, ...) (*workflowservice.DescribeTaskQueueResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.DescribeTaskQueue)
    *   [func (m *MockWorkflowServiceClient) DescribeWorker(ctx context.Context, in *workflowservice.DescribeWorkerRequest, ...) (*workflowservice.DescribeWorkerResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.DescribeWorker)
    *   [func (m *MockWorkflowServiceClient) DescribeWorkerDeployment(ctx context.Context, in *workflowservice.DescribeWorkerDeploymentRequest, ...) (*workflowservice.DescribeWorkerDeploymentResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.DescribeWorkerDeployment)
    *   [func (m *MockWorkflowServiceClient) DescribeWorkerDeploymentVersion(ctx context.Context, ...) (*workflowservice.DescribeWorkerDeploymentVersionResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.DescribeWorkerDeploymentVersion)
    *   [func (m *MockWorkflowServiceClient) DescribeWorkflowExecution(ctx context.Context, in *workflowservice.DescribeWorkflowExecutionRequest, ...) (*workflowservice.DescribeWorkflowExecutionResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.DescribeWorkflowExecution)
    *   [func (m *MockWorkflowServiceClient) DescribeWorkflowRule(ctx context.Context, in *workflowservice.DescribeWorkflowRuleRequest, ...) (*workflowservice.DescribeWorkflowRuleResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.DescribeWorkflowRule)
    *   [func (m *MockWorkflowServiceClient) EXPECT() *MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.EXPECT)
    *   [func (m *MockWorkflowServiceClient) ExecuteMultiOperation(ctx context.Context, in *workflowservice.ExecuteMultiOperationRequest, ...) (*workflowservice.ExecuteMultiOperationResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.ExecuteMultiOperation)
    *   [func (m *MockWorkflowServiceClient) FetchWorkerConfig(ctx context.Context, in *workflowservice.FetchWorkerConfigRequest, ...) (*workflowservice.FetchWorkerConfigResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.FetchWorkerConfig)
    *   [func (m *MockWorkflowServiceClient) GetClusterInfo(ctx context.Context, in *workflowservice.GetClusterInfoRequest, ...) (*workflowservice.GetClusterInfoResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.GetClusterInfo)
    *   [func (m *MockWorkflowServiceClient) GetCurrentDeployment(ctx context.Context, in *workflowservice.GetCurrentDeploymentRequest, ...) (*workflowservice.GetCurrentDeploymentResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.GetCurrentDeployment)
    *   [func (m *MockWorkflowServiceClient) GetDeploymentReachability(ctx context.Context, in *workflowservice.GetDeploymentReachabilityRequest, ...) (*workflowservice.GetDeploymentReachabilityResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.GetDeploymentReachability)
    *   [func (m *MockWorkflowServiceClient) GetSearchAttributes(ctx context.Context, in *workflowservice.GetSearchAttributesRequest, ...) (*workflowservice.GetSearchAttributesResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.GetSearchAttributes)
    *   [func (m *MockWorkflowServiceClient) GetSystemInfo(ctx context.Context, in *workflowservice.GetSystemInfoRequest, ...) (*workflowservice.GetSystemInfoResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.GetSystemInfo)
    *   [func (m *MockWorkflowServiceClient) GetWorkerBuildIdCompatibility(ctx context.Context, in *workflowservice.GetWorkerBuildIdCompatibilityRequest, ...) (*workflowservice.GetWorkerBuildIdCompatibilityResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.GetWorkerBuildIdCompatibility)
    *   [func (m *MockWorkflowServiceClient) GetWorkerTaskReachability(ctx context.Context, in *workflowservice.GetWorkerTaskReachabilityRequest, ...) (*workflowservice.GetWorkerTaskReachabilityResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.GetWorkerTaskReachability)
    *   [func (m *MockWorkflowServiceClient) GetWorkerVersioningRules(ctx context.Context, in *workflowservice.GetWorkerVersioningRulesRequest, ...) (*workflowservice.GetWorkerVersioningRulesResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.GetWorkerVersioningRules)
    *   [func (m *MockWorkflowServiceClient) GetWorkflowExecutionHistory(ctx context.Context, in *workflowservice.GetWorkflowExecutionHistoryRequest, ...) (*workflowservice.GetWorkflowExecutionHistoryResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.GetWorkflowExecutionHistory)
    *   [func (m *MockWorkflowServiceClient) GetWorkflowExecutionHistoryReverse(ctx context.Context, ...) (*workflowservice.GetWorkflowExecutionHistoryReverseResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.GetWorkflowExecutionHistoryReverse)
    *   [func (m *MockWorkflowServiceClient) ListActivityExecutions(ctx context.Context, in *workflowservice.ListActivityExecutionsRequest, ...) (*workflowservice.ListActivityExecutionsResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.ListActivityExecutions)
    *   [func (m *MockWorkflowServiceClient) ListArchivedWorkflowExecutions(ctx context.Context, in *workflowservice.ListArchivedWorkflowExecutionsRequest, ...) (*workflowservice.ListArchivedWorkflowExecutionsResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.ListArchivedWorkflowExecutions)
    *   [func (m *MockWorkflowServiceClient) ListBatchOperations(ctx context.Context, in *workflowservice.ListBatchOperationsRequest, ...) (*workflowservice.ListBatchOperationsResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.ListBatchOperations)
    *   [func (m *MockWorkflowServiceClient) ListClosedWorkflowExecutions(ctx context.Context, in *workflowservice.ListClosedWorkflowExecutionsRequest, ...) (*workflowservice.ListClosedWorkflowExecutionsResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.ListClosedWorkflowExecutions)
    *   [func (m *MockWorkflowServiceClient) ListDeployments(ctx context.Context, in *workflowservice.ListDeploymentsRequest, ...) (*workflowservice.ListDeploymentsResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.ListDeployments)
    *   [func (m *MockWorkflowServiceClient) ListNamespaces(ctx context.Context, in *workflowservice.ListNamespacesRequest, ...) (*workflowservice.ListNamespacesResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.ListNamespaces)
    *   [func (m *MockWorkflowServiceClient) ListOpenWorkflowExecutions(ctx context.Context, in *workflowservice.ListOpenWorkflowExecutionsRequest, ...) (*workflowservice.ListOpenWorkflowExecutionsResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.ListOpenWorkflowExecutions)
    *   [func (m *MockWorkflowServiceClient) ListScheduleMatchingTimes(ctx context.Context, in *workflowservice.ListScheduleMatchingTimesRequest, ...) (*workflowservice.ListScheduleMatchingTimesResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.ListScheduleMatchingTimes)
    *   [func (m *MockWorkflowServiceClient) ListSchedules(ctx context.Context, in *workflowservice.ListSchedulesRequest, ...) (*workflowservice.ListSchedulesResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.ListSchedules)
    *   [func (m *MockWorkflowServiceClient) ListTaskQueuePartitions(ctx context.Context, in *workflowservice.ListTaskQueuePartitionsRequest, ...) (*workflowservice.ListTaskQueuePartitionsResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.ListTaskQueuePartitions)
    *   [func (m *MockWorkflowServiceClient) ListWorkerDeployments(ctx context.Context, in *workflowservice.ListWorkerDeploymentsRequest, ...) (*workflowservice.ListWorkerDeploymentsResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.ListWorkerDeployments)
    *   [func (m *MockWorkflowServiceClient) ListWorkers(ctx context.Context, in *workflowservice.ListWorkersRequest, ...) (*workflowservice.ListWorkersResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.ListWorkers)
    *   [func (m *MockWorkflowServiceClient) ListWorkflowExecutions(ctx context.Context, in *workflowservice.ListWorkflowExecutionsRequest, ...) (*workflowservice.ListWorkflowExecutionsResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.ListWorkflowExecutions)
    *   [func (m *MockWorkflowServiceClient) ListWorkflowRules(ctx context.Context, in *workflowservice.ListWorkflowRulesRequest, ...) (*workflowservice.ListWorkflowRulesResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.ListWorkflowRules)
    *   [func (m *MockWorkflowServiceClient) PatchSchedule(ctx context.Context, in *workflowservice.PatchScheduleRequest, ...) (*workflowservice.PatchScheduleResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.PatchSchedule)
    *   [func (m *MockWorkflowServiceClient) PauseActivity(ctx context.Context, in *workflowservice.PauseActivityRequest, ...) (*workflowservice.PauseActivityResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.PauseActivity)
    *   [func (m *MockWorkflowServiceClient) PauseWorkflowExecution(ctx context.Context, in *workflowservice.PauseWorkflowExecutionRequest, ...) (*workflowservice.PauseWorkflowExecutionResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.PauseWorkflowExecution)
    *   [func (m *MockWorkflowServiceClient) PollActivityExecution(ctx context.Context, in *workflowservice.PollActivityExecutionRequest, ...) (*workflowservice.PollActivityExecutionResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.PollActivityExecution)
    *   [func (m *MockWorkflowServiceClient) PollActivityTaskQueue(ctx context.Context, in *workflowservice.PollActivityTaskQueueRequest, ...) (*workflowservice.PollActivityTaskQueueResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.PollActivityTaskQueue)
    *   [func (m *MockWorkflowServiceClient) PollNexusTaskQueue(ctx context.Context, in *workflowservice.PollNexusTaskQueueRequest, ...) (*workflowservice.PollNexusTaskQueueResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.PollNexusTaskQueue)
    *   [func (m *MockWorkflowServiceClient) PollWorkflowExecutionUpdate(ctx context.Context, in *workflowservice.PollWorkflowExecutionUpdateRequest, ...) (*workflowservice.PollWorkflowExecutionUpdateResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.PollWorkflowExecutionUpdate)
    *   [func (m *MockWorkflowServiceClient) PollWorkflowTaskQueue(ctx context.Context, in *workflowservice.PollWorkflowTaskQueueRequest, ...) (*workflowservice.PollWorkflowTaskQueueResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.PollWorkflowTaskQueue)
    *   [func (m *MockWorkflowServiceClient) QueryWorkflow(ctx context.Context, in *workflowservice.QueryWorkflowRequest, ...) (*workflowservice.QueryWorkflowResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.QueryWorkflow)
    *   [func (m *MockWorkflowServiceClient) RecordActivityTaskHeartbeat(ctx context.Context, in *workflowservice.RecordActivityTaskHeartbeatRequest, ...) (*workflowservice.RecordActivityTaskHeartbeatResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.RecordActivityTaskHeartbeat)
    *   [func (m *MockWorkflowServiceClient) RecordActivityTaskHeartbeatById(ctx context.Context, ...) (*workflowservice.RecordActivityTaskHeartbeatByIdResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.RecordActivityTaskHeartbeatById)
    *   [func (m *MockWorkflowServiceClient) RecordWorkerHeartbeat(ctx context.Context, in *workflowservice.RecordWorkerHeartbeatRequest, ...) (*workflowservice.RecordWorkerHeartbeatResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.RecordWorkerHeartbeat)
    *   [func (m *MockWorkflowServiceClient) RegisterNamespace(ctx context.Context, in *workflowservice.RegisterNamespaceRequest, ...) (*workflowservice.RegisterNamespaceResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.RegisterNamespace)
    *   [func (m *MockWorkflowServiceClient) RequestCancelActivityExecution(ctx context.Context, in *workflowservice.RequestCancelActivityExecutionRequest, ...) (*workflowservice.RequestCancelActivityExecutionResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.RequestCancelActivityExecution)
    *   [func (m *MockWorkflowServiceClient) RequestCancelWorkflowExecution(ctx context.Context, in *workflowservice.RequestCancelWorkflowExecutionRequest, ...) (*workflowservice.RequestCancelWorkflowExecutionResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.RequestCancelWorkflowExecution)
    *   [func (m *MockWorkflowServiceClient) ResetActivity(ctx context.Context, in *workflowservice.ResetActivityRequest, ...) (*workflowservice.ResetActivityResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.ResetActivity)
    *   [func (m *MockWorkflowServiceClient) ResetStickyTaskQueue(ctx context.Context, in *workflowservice.ResetStickyTaskQueueRequest, ...) (*workflowservice.ResetStickyTaskQueueResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.ResetStickyTaskQueue)
    *   [func (m *MockWorkflowServiceClient) ResetWorkflowExecution(ctx context.Context, in *workflowservice.ResetWorkflowExecutionRequest, ...) (*workflowservice.ResetWorkflowExecutionResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.ResetWorkflowExecution)
    *   [func (m *MockWorkflowServiceClient) RespondActivityTaskCanceled(ctx context.Context, in *workflowservice.RespondActivityTaskCanceledRequest, ...) (*workflowservice.RespondActivityTaskCanceledResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.RespondActivityTaskCanceled)
    *   [func (m *MockWorkflowServiceClient) RespondActivityTaskCanceledById(ctx context.Context, ...) (*workflowservice.RespondActivityTaskCanceledByIdResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.RespondActivityTaskCanceledById)
    *   [func (m *MockWorkflowServiceClient) RespondActivityTaskCompleted(ctx context.Context, in *workflowservice.RespondActivityTaskCompletedRequest, ...) (*workflowservice.RespondActivityTaskCompletedResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.RespondActivityTaskCompleted)
    *   [func (m *MockWorkflowServiceClient) RespondActivityTaskCompletedById(ctx context.Context, ...) (*workflowservice.RespondActivityTaskCompletedByIdResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.RespondActivityTaskCompletedById)
    *   [func (m *MockWorkflowServiceClient) RespondActivityTaskFailed(ctx context.Context, in *workflowservice.RespondActivityTaskFailedRequest, ...) (*workflowservice.RespondActivityTaskFailedResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.RespondActivityTaskFailed)
    *   [func (m *MockWorkflowServiceClient) RespondActivityTaskFailedById(ctx context.Context, in *workflowservice.RespondActivityTaskFailedByIdRequest, ...) (*workflowservice.RespondActivityTaskFailedByIdResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.RespondActivityTaskFailedById)
    *   [func (m *MockWorkflowServiceClient) RespondNexusTaskCompleted(ctx context.Context, in *workflowservice.RespondNexusTaskCompletedRequest, ...) (*workflowservice.RespondNexusTaskCompletedResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.RespondNexusTaskCompleted)
    *   [func (m *MockWorkflowServiceClient) RespondNexusTaskFailed(ctx context.Context, in *workflowservice.RespondNexusTaskFailedRequest, ...) (*workflowservice.RespondNexusTaskFailedResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.RespondNexusTaskFailed)
    *   [func (m *MockWorkflowServiceClient) RespondQueryTaskCompleted(ctx context.Context, in *workflowservice.RespondQueryTaskCompletedRequest, ...) (*workflowservice.RespondQueryTaskCompletedResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.RespondQueryTaskCompleted)
    *   [func (m *MockWorkflowServiceClient) RespondWorkflowTaskCompleted(ctx context.Context, in *workflowservice.RespondWorkflowTaskCompletedRequest, ...) (*workflowservice.RespondWorkflowTaskCompletedResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.RespondWorkflowTaskCompleted)
    *   [func (m *MockWorkflowServiceClient) RespondWorkflowTaskFailed(ctx context.Context, in *workflowservice.RespondWorkflowTaskFailedRequest, ...) (*workflowservice.RespondWorkflowTaskFailedResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.RespondWorkflowTaskFailed)
    *   [func (m *MockWorkflowServiceClient) ScanWorkflowExecutions(ctx context.Context, in *workflowservice.ScanWorkflowExecutionsRequest, ...) (*workflowservice.ScanWorkflowExecutionsResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.ScanWorkflowExecutions)
    *   [func (m *MockWorkflowServiceClient) SetCurrentDeployment(ctx context.Context, in *workflowservice.SetCurrentDeploymentRequest, ...) (*workflowservice.SetCurrentDeploymentResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.SetCurrentDeployment)
    *   [func (m *MockWorkflowServiceClient) SetWorkerDeploymentCurrentVersion(ctx context.Context, ...) (*workflowservice.SetWorkerDeploymentCurrentVersionResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.SetWorkerDeploymentCurrentVersion)
    *   [func (m *MockWorkflowServiceClient) SetWorkerDeploymentManager(ctx context.Context, in *workflowservice.SetWorkerDeploymentManagerRequest, ...) (*workflowservice.SetWorkerDeploymentManagerResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.SetWorkerDeploymentManager)
    *   [func (m *MockWorkflowServiceClient) SetWorkerDeploymentRampingVersion(ctx context.Context, ...) (*workflowservice.SetWorkerDeploymentRampingVersionResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.SetWorkerDeploymentRampingVersion)
    *   [func (m *MockWorkflowServiceClient) ShutdownWorker(ctx context.Context, in *workflowservice.ShutdownWorkerRequest, ...) (*workflowservice.ShutdownWorkerResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.ShutdownWorker)
    *   [func (m *MockWorkflowServiceClient) SignalWithStartWorkflowExecution(ctx context.Context, ...) (*workflowservice.SignalWithStartWorkflowExecutionResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.SignalWithStartWorkflowExecution)
    *   [func (m *MockWorkflowServiceClient) SignalWorkflowExecution(ctx context.Context, in *workflowservice.SignalWorkflowExecutionRequest, ...) (*workflowservice.SignalWorkflowExecutionResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.SignalWorkflowExecution)
    *   [func (m *MockWorkflowServiceClient) StartActivityExecution(ctx context.Context, in *workflowservice.StartActivityExecutionRequest, ...) (*workflowservice.StartActivityExecutionResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.StartActivityExecution)
    *   [func (m *MockWorkflowServiceClient) StartBatchOperation(ctx context.Context, in *workflowservice.StartBatchOperationRequest, ...) (*workflowservice.StartBatchOperationResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.StartBatchOperation)
    *   [func (m *MockWorkflowServiceClient) StartWorkflowExecution(ctx context.Context, in *workflowservice.StartWorkflowExecutionRequest, ...) (*workflowservice.StartWorkflowExecutionResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.StartWorkflowExecution)
    *   [func (m *MockWorkflowServiceClient) StopBatchOperation(ctx context.Context, in *workflowservice.StopBatchOperationRequest, ...) (*workflowservice.StopBatchOperationResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.StopBatchOperation)
    *   [func (m *MockWorkflowServiceClient) TerminateActivityExecution(ctx context.Context, in *workflowservice.TerminateActivityExecutionRequest, ...) (*workflowservice.TerminateActivityExecutionResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.TerminateActivityExecution)
    *   [func (m *MockWorkflowServiceClient) TerminateWorkflowExecution(ctx context.Context, in *workflowservice.TerminateWorkflowExecutionRequest, ...) (*workflowservice.TerminateWorkflowExecutionResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.TerminateWorkflowExecution)
    *   [func (m *MockWorkflowServiceClient) TriggerWorkflowRule(ctx context.Context, in *workflowservice.TriggerWorkflowRuleRequest, ...) (*workflowservice.TriggerWorkflowRuleResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.TriggerWorkflowRule)
    *   [func (m *MockWorkflowServiceClient) UnpauseActivity(ctx context.Context, in *workflowservice.UnpauseActivityRequest, ...) (*workflowservice.UnpauseActivityResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.UnpauseActivity)
    *   [func (m *MockWorkflowServiceClient) UnpauseWorkflowExecution(ctx context.Context, in *workflowservice.UnpauseWorkflowExecutionRequest, ...) (*workflowservice.UnpauseWorkflowExecutionResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.UnpauseWorkflowExecution)
    *   [func (m *MockWorkflowServiceClient) UpdateActivityOptions(ctx context.Context, in *workflowservice.UpdateActivityOptionsRequest, ...) (*workflowservice.UpdateActivityOptionsResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.UpdateActivityOptions)
    *   [func (m *MockWorkflowServiceClient) UpdateNamespace(ctx context.Context, in *workflowservice.UpdateNamespaceRequest, ...) (*workflowservice.UpdateNamespaceResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.UpdateNamespace)
    *   [func (m *MockWorkflowServiceClient) UpdateSchedule(ctx context.Context, in *workflowservice.UpdateScheduleRequest, ...) (*workflowservice.UpdateScheduleResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.UpdateSchedule)
    *   [func (m *MockWorkflowServiceClient) UpdateTaskQueueConfig(ctx context.Context, in *workflowservice.UpdateTaskQueueConfigRequest, ...) (*workflowservice.UpdateTaskQueueConfigResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.UpdateTaskQueueConfig)
    *   [func (m *MockWorkflowServiceClient) UpdateWorkerBuildIdCompatibility(ctx context.Context, ...) (*workflowservice.UpdateWorkerBuildIdCompatibilityResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.UpdateWorkerBuildIdCompatibility)
    *   [func (m *MockWorkflowServiceClient) UpdateWorkerConfig(ctx context.Context, in *workflowservice.UpdateWorkerConfigRequest, ...) (*workflowservice.UpdateWorkerConfigResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.UpdateWorkerConfig)
    *   [func (m *MockWorkflowServiceClient) UpdateWorkerDeploymentVersionMetadata(ctx context.Context, ...) (*workflowservice.UpdateWorkerDeploymentVersionMetadataResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.UpdateWorkerDeploymentVersionMetadata)
    *   [func (m *MockWorkflowServiceClient) UpdateWorkerVersioningRules(ctx context.Context, in *workflowservice.UpdateWorkerVersioningRulesRequest, ...) (*workflowservice.UpdateWorkerVersioningRulesResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.UpdateWorkerVersioningRules)
    *   [func (m *MockWorkflowServiceClient) UpdateWorkflowExecution(ctx context.Context, in *workflowservice.UpdateWorkflowExecutionRequest, ...) (*workflowservice.UpdateWorkflowExecutionResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.UpdateWorkflowExecution)
    *   [func (m *MockWorkflowServiceClient) UpdateWorkflowExecutionOptions(ctx context.Context, in *workflowservice.UpdateWorkflowExecutionOptionsRequest, ...) (*workflowservice.UpdateWorkflowExecutionOptionsResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClient.UpdateWorkflowExecutionOptions)

*   [type MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)
*       *   [func (mr *MockWorkflowServiceClientMockRecorder) CountActivityExecutions(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.CountActivityExecutions)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) CountSchedules(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.CountSchedules)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) CountWorkflowExecutions(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.CountWorkflowExecutions)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) CreateSchedule(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.CreateSchedule)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) CreateWorkflowRule(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.CreateWorkflowRule)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) DeleteActivityExecution(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.DeleteActivityExecution)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) DeleteSchedule(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.DeleteSchedule)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) DeleteWorkerDeployment(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.DeleteWorkerDeployment)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) DeleteWorkerDeploymentVersion(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.DeleteWorkerDeploymentVersion)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) DeleteWorkflowExecution(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.DeleteWorkflowExecution)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) DeleteWorkflowRule(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.DeleteWorkflowRule)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) DeprecateNamespace(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.DeprecateNamespace)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) DescribeActivityExecution(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.DescribeActivityExecution)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) DescribeBatchOperation(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.DescribeBatchOperation)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) DescribeDeployment(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.DescribeDeployment)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) DescribeNamespace(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.DescribeNamespace)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) DescribeSchedule(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.DescribeSchedule)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) DescribeTaskQueue(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.DescribeTaskQueue)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) DescribeWorker(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.DescribeWorker)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) DescribeWorkerDeployment(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.DescribeWorkerDeployment)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) DescribeWorkerDeploymentVersion(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.DescribeWorkerDeploymentVersion)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) DescribeWorkflowExecution(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.DescribeWorkflowExecution)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) DescribeWorkflowRule(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.DescribeWorkflowRule)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) ExecuteMultiOperation(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.ExecuteMultiOperation)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) FetchWorkerConfig(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.FetchWorkerConfig)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) GetClusterInfo(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.GetClusterInfo)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) GetCurrentDeployment(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.GetCurrentDeployment)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) GetDeploymentReachability(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.GetDeploymentReachability)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) GetSearchAttributes(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.GetSearchAttributes)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) GetSystemInfo(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.GetSystemInfo)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) GetWorkerBuildIdCompatibility(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.GetWorkerBuildIdCompatibility)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) GetWorkerTaskReachability(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.GetWorkerTaskReachability)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) GetWorkerVersioningRules(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.GetWorkerVersioningRules)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) GetWorkflowExecutionHistory(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.GetWorkflowExecutionHistory)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) GetWorkflowExecutionHistoryReverse(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.GetWorkflowExecutionHistoryReverse)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) ListActivityExecutions(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.ListActivityExecutions)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) ListArchivedWorkflowExecutions(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.ListArchivedWorkflowExecutions)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) ListBatchOperations(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.ListBatchOperations)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) ListClosedWorkflowExecutions(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.ListClosedWorkflowExecutions)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) ListDeployments(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.ListDeployments)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) ListNamespaces(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.ListNamespaces)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) ListOpenWorkflowExecutions(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.ListOpenWorkflowExecutions)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) ListScheduleMatchingTimes(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.ListScheduleMatchingTimes)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) ListSchedules(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.ListSchedules)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) ListTaskQueuePartitions(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.ListTaskQueuePartitions)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) ListWorkerDeployments(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.ListWorkerDeployments)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) ListWorkers(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.ListWorkers)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) ListWorkflowExecutions(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.ListWorkflowExecutions)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) ListWorkflowRules(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.ListWorkflowRules)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) PatchSchedule(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.PatchSchedule)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) PauseActivity(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.PauseActivity)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) PauseWorkflowExecution(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.PauseWorkflowExecution)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) PollActivityExecution(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.PollActivityExecution)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) PollActivityTaskQueue(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.PollActivityTaskQueue)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) PollNexusTaskQueue(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.PollNexusTaskQueue)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) PollWorkflowExecutionUpdate(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.PollWorkflowExecutionUpdate)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) PollWorkflowTaskQueue(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.PollWorkflowTaskQueue)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) QueryWorkflow(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.QueryWorkflow)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) RecordActivityTaskHeartbeat(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.RecordActivityTaskHeartbeat)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) RecordActivityTaskHeartbeatById(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.RecordActivityTaskHeartbeatById)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) RecordWorkerHeartbeat(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.RecordWorkerHeartbeat)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) RegisterNamespace(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.RegisterNamespace)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) RequestCancelActivityExecution(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.RequestCancelActivityExecution)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) RequestCancelWorkflowExecution(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.RequestCancelWorkflowExecution)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) ResetActivity(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.ResetActivity)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) ResetStickyTaskQueue(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.ResetStickyTaskQueue)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) ResetWorkflowExecution(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.ResetWorkflowExecution)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) RespondActivityTaskCanceled(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.RespondActivityTaskCanceled)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) RespondActivityTaskCanceledById(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.RespondActivityTaskCanceledById)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) RespondActivityTaskCompleted(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.RespondActivityTaskCompleted)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) RespondActivityTaskCompletedById(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.RespondActivityTaskCompletedById)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) RespondActivityTaskFailed(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.RespondActivityTaskFailed)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) RespondActivityTaskFailedById(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.RespondActivityTaskFailedById)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) RespondNexusTaskCompleted(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.RespondNexusTaskCompleted)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) RespondNexusTaskFailed(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.RespondNexusTaskFailed)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) RespondQueryTaskCompleted(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.RespondQueryTaskCompleted)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) RespondWorkflowTaskCompleted(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.RespondWorkflowTaskCompleted)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) RespondWorkflowTaskFailed(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.RespondWorkflowTaskFailed)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) ScanWorkflowExecutions(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.ScanWorkflowExecutions)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) SetCurrentDeployment(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.SetCurrentDeployment)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) SetWorkerDeploymentCurrentVersion(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.SetWorkerDeploymentCurrentVersion)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) SetWorkerDeploymentManager(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.SetWorkerDeploymentManager)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) SetWorkerDeploymentRampingVersion(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.SetWorkerDeploymentRampingVersion)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) ShutdownWorker(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.ShutdownWorker)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) SignalWithStartWorkflowExecution(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.SignalWithStartWorkflowExecution)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) SignalWorkflowExecution(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.SignalWorkflowExecution)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) StartActivityExecution(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.StartActivityExecution)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) StartBatchOperation(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.StartBatchOperation)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) StartWorkflowExecution(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.StartWorkflowExecution)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) StopBatchOperation(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.StopBatchOperation)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) TerminateActivityExecution(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.TerminateActivityExecution)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) TerminateWorkflowExecution(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.TerminateWorkflowExecution)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) TriggerWorkflowRule(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.TriggerWorkflowRule)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) UnpauseActivity(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.UnpauseActivity)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) UnpauseWorkflowExecution(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.UnpauseWorkflowExecution)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) UpdateActivityOptions(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.UpdateActivityOptions)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) UpdateNamespace(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.UpdateNamespace)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) UpdateSchedule(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.UpdateSchedule)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) UpdateTaskQueueConfig(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.UpdateTaskQueueConfig)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) UpdateWorkerBuildIdCompatibility(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.UpdateWorkerBuildIdCompatibility)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) UpdateWorkerConfig(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.UpdateWorkerConfig)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) UpdateWorkerDeploymentVersionMetadata(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.UpdateWorkerDeploymentVersionMetadata)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) UpdateWorkerVersioningRules(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.UpdateWorkerVersioningRules)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) UpdateWorkflowExecution(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.UpdateWorkflowExecution)
    *   [func (mr *MockWorkflowServiceClientMockRecorder) UpdateWorkflowExecutionOptions(ctx, in interface{}, opts ...interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder.UpdateWorkflowExecutionOptions)

*   [type MockWorkflowServiceServer](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer)
*       *   [func NewMockWorkflowServiceServer(ctrl *gomock.Controller) *MockWorkflowServiceServer](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#NewMockWorkflowServiceServer)

*       *   [func (m *MockWorkflowServiceServer) CountActivityExecutions(arg0 context.Context, arg1 *workflowservice.CountActivityExecutionsRequest) (*workflowservice.CountActivityExecutionsResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.CountActivityExecutions)
    *   [func (m *MockWorkflowServiceServer) CountSchedules(arg0 context.Context, arg1 *workflowservice.CountSchedulesRequest) (*workflowservice.CountSchedulesResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.CountSchedules)
    *   [func (m *MockWorkflowServiceServer) CountWorkflowExecutions(arg0 context.Context, arg1 *workflowservice.CountWorkflowExecutionsRequest) (*workflowservice.CountWorkflowExecutionsResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.CountWorkflowExecutions)
    *   [func (m *MockWorkflowServiceServer) CreateSchedule(arg0 context.Context, arg1 *workflowservice.CreateScheduleRequest) (*workflowservice.CreateScheduleResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.CreateSchedule)
    *   [func (m *MockWorkflowServiceServer) CreateWorkflowRule(arg0 context.Context, arg1 *workflowservice.CreateWorkflowRuleRequest) (*workflowservice.CreateWorkflowRuleResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.CreateWorkflowRule)
    *   [func (m *MockWorkflowServiceServer) DeleteActivityExecution(arg0 context.Context, arg1 *workflowservice.DeleteActivityExecutionRequest) (*workflowservice.DeleteActivityExecutionResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.DeleteActivityExecution)
    *   [func (m *MockWorkflowServiceServer) DeleteSchedule(arg0 context.Context, arg1 *workflowservice.DeleteScheduleRequest) (*workflowservice.DeleteScheduleResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.DeleteSchedule)
    *   [func (m *MockWorkflowServiceServer) DeleteWorkerDeployment(arg0 context.Context, arg1 *workflowservice.DeleteWorkerDeploymentRequest) (*workflowservice.DeleteWorkerDeploymentResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.DeleteWorkerDeployment)
    *   [func (m *MockWorkflowServiceServer) DeleteWorkerDeploymentVersion(arg0 context.Context, ...) (*workflowservice.DeleteWorkerDeploymentVersionResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.DeleteWorkerDeploymentVersion)
    *   [func (m *MockWorkflowServiceServer) DeleteWorkflowExecution(arg0 context.Context, arg1 *workflowservice.DeleteWorkflowExecutionRequest) (*workflowservice.DeleteWorkflowExecutionResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.DeleteWorkflowExecution)
    *   [func (m *MockWorkflowServiceServer) DeleteWorkflowRule(arg0 context.Context, arg1 *workflowservice.DeleteWorkflowRuleRequest) (*workflowservice.DeleteWorkflowRuleResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.DeleteWorkflowRule)
    *   [func (m *MockWorkflowServiceServer) DeprecateNamespace(arg0 context.Context, arg1 *workflowservice.DeprecateNamespaceRequest) (*workflowservice.DeprecateNamespaceResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.DeprecateNamespace)
    *   [func (m *MockWorkflowServiceServer) DescribeActivityExecution(arg0 context.Context, arg1 *workflowservice.DescribeActivityExecutionRequest) (*workflowservice.DescribeActivityExecutionResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.DescribeActivityExecution)
    *   [func (m *MockWorkflowServiceServer) DescribeBatchOperation(arg0 context.Context, arg1 *workflowservice.DescribeBatchOperationRequest) (*workflowservice.DescribeBatchOperationResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.DescribeBatchOperation)
    *   [func (m *MockWorkflowServiceServer) DescribeDeployment(arg0 context.Context, arg1 *workflowservice.DescribeDeploymentRequest) (*workflowservice.DescribeDeploymentResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.DescribeDeployment)
    *   [func (m *MockWorkflowServiceServer) DescribeNamespace(arg0 context.Context, arg1 *workflowservice.DescribeNamespaceRequest) (*workflowservice.DescribeNamespaceResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.DescribeNamespace)
    *   [func (m *MockWorkflowServiceServer) DescribeSchedule(arg0 context.Context, arg1 *workflowservice.DescribeScheduleRequest) (*workflowservice.DescribeScheduleResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.DescribeSchedule)
    *   [func (m *MockWorkflowServiceServer) DescribeTaskQueue(arg0 context.Context, arg1 *workflowservice.DescribeTaskQueueRequest) (*workflowservice.DescribeTaskQueueResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.DescribeTaskQueue)
    *   [func (m *MockWorkflowServiceServer) DescribeWorker(arg0 context.Context, arg1 *workflowservice.DescribeWorkerRequest) (*workflowservice.DescribeWorkerResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.DescribeWorker)
    *   [func (m *MockWorkflowServiceServer) DescribeWorkerDeployment(arg0 context.Context, arg1 *workflowservice.DescribeWorkerDeploymentRequest) (*workflowservice.DescribeWorkerDeploymentResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.DescribeWorkerDeployment)
    *   [func (m *MockWorkflowServiceServer) DescribeWorkerDeploymentVersion(arg0 context.Context, ...) (*workflowservice.DescribeWorkerDeploymentVersionResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.DescribeWorkerDeploymentVersion)
    *   [func (m *MockWorkflowServiceServer) DescribeWorkflowExecution(arg0 context.Context, arg1 *workflowservice.DescribeWorkflowExecutionRequest) (*workflowservice.DescribeWorkflowExecutionResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.DescribeWorkflowExecution)
    *   [func (m *MockWorkflowServiceServer) DescribeWorkflowRule(arg0 context.Context, arg1 *workflowservice.DescribeWorkflowRuleRequest) (*workflowservice.DescribeWorkflowRuleResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.DescribeWorkflowRule)
    *   [func (m *MockWorkflowServiceServer) EXPECT() *MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.EXPECT)
    *   [func (m *MockWorkflowServiceServer) ExecuteMultiOperation(arg0 context.Context, arg1 *workflowservice.ExecuteMultiOperationRequest) (*workflowservice.ExecuteMultiOperationResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.ExecuteMultiOperation)
    *   [func (m *MockWorkflowServiceServer) FetchWorkerConfig(arg0 context.Context, arg1 *workflowservice.FetchWorkerConfigRequest) (*workflowservice.FetchWorkerConfigResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.FetchWorkerConfig)
    *   [func (m *MockWorkflowServiceServer) GetClusterInfo(arg0 context.Context, arg1 *workflowservice.GetClusterInfoRequest) (*workflowservice.GetClusterInfoResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.GetClusterInfo)
    *   [func (m *MockWorkflowServiceServer) GetCurrentDeployment(arg0 context.Context, arg1 *workflowservice.GetCurrentDeploymentRequest) (*workflowservice.GetCurrentDeploymentResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.GetCurrentDeployment)
    *   [func (m *MockWorkflowServiceServer) GetDeploymentReachability(arg0 context.Context, arg1 *workflowservice.GetDeploymentReachabilityRequest) (*workflowservice.GetDeploymentReachabilityResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.GetDeploymentReachability)
    *   [func (m *MockWorkflowServiceServer) GetSearchAttributes(arg0 context.Context, arg1 *workflowservice.GetSearchAttributesRequest) (*workflowservice.GetSearchAttributesResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.GetSearchAttributes)
    *   [func (m *MockWorkflowServiceServer) GetSystemInfo(arg0 context.Context, arg1 *workflowservice.GetSystemInfoRequest) (*workflowservice.GetSystemInfoResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.GetSystemInfo)
    *   [func (m *MockWorkflowServiceServer) GetWorkerBuildIdCompatibility(arg0 context.Context, ...) (*workflowservice.GetWorkerBuildIdCompatibilityResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.GetWorkerBuildIdCompatibility)
    *   [func (m *MockWorkflowServiceServer) GetWorkerTaskReachability(arg0 context.Context, arg1 *workflowservice.GetWorkerTaskReachabilityRequest) (*workflowservice.GetWorkerTaskReachabilityResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.GetWorkerTaskReachability)
    *   [func (m *MockWorkflowServiceServer) GetWorkerVersioningRules(arg0 context.Context, arg1 *workflowservice.GetWorkerVersioningRulesRequest) (*workflowservice.GetWorkerVersioningRulesResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.GetWorkerVersioningRules)
    *   [func (m *MockWorkflowServiceServer) GetWorkflowExecutionHistory(arg0 context.Context, arg1 *workflowservice.GetWorkflowExecutionHistoryRequest) (*workflowservice.GetWorkflowExecutionHistoryResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.GetWorkflowExecutionHistory)
    *   [func (m *MockWorkflowServiceServer) GetWorkflowExecutionHistoryReverse(arg0 context.Context, ...) (*workflowservice.GetWorkflowExecutionHistoryReverseResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.GetWorkflowExecutionHistoryReverse)
    *   [func (m *MockWorkflowServiceServer) ListActivityExecutions(arg0 context.Context, arg1 *workflowservice.ListActivityExecutionsRequest) (*workflowservice.ListActivityExecutionsResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.ListActivityExecutions)
    *   [func (m *MockWorkflowServiceServer) ListArchivedWorkflowExecutions(arg0 context.Context, ...) (*workflowservice.ListArchivedWorkflowExecutionsResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.ListArchivedWorkflowExecutions)
    *   [func (m *MockWorkflowServiceServer) ListBatchOperations(arg0 context.Context, arg1 *workflowservice.ListBatchOperationsRequest) (*workflowservice.ListBatchOperationsResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.ListBatchOperations)
    *   [func (m *MockWorkflowServiceServer) ListClosedWorkflowExecutions(arg0 context.Context, ...) (*workflowservice.ListClosedWorkflowExecutionsResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.ListClosedWorkflowExecutions)
    *   [func (m *MockWorkflowServiceServer) ListDeployments(arg0 context.Context, arg1 *workflowservice.ListDeploymentsRequest) (*workflowservice.ListDeploymentsResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.ListDeployments)
    *   [func (m *MockWorkflowServiceServer) ListNamespaces(arg0 context.Context, arg1 *workflowservice.ListNamespacesRequest) (*workflowservice.ListNamespacesResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.ListNamespaces)
    *   [func (m *MockWorkflowServiceServer) ListOpenWorkflowExecutions(arg0 context.Context, arg1 *workflowservice.ListOpenWorkflowExecutionsRequest) (*workflowservice.ListOpenWorkflowExecutionsResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.ListOpenWorkflowExecutions)
    *   [func (m *MockWorkflowServiceServer) ListScheduleMatchingTimes(arg0 context.Context, arg1 *workflowservice.ListScheduleMatchingTimesRequest) (*workflowservice.ListScheduleMatchingTimesResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.ListScheduleMatchingTimes)
    *   [func (m *MockWorkflowServiceServer) ListSchedules(arg0 context.Context, arg1 *workflowservice.ListSchedulesRequest) (*workflowservice.ListSchedulesResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.ListSchedules)
    *   [func (m *MockWorkflowServiceServer) ListTaskQueuePartitions(arg0 context.Context, arg1 *workflowservice.ListTaskQueuePartitionsRequest) (*workflowservice.ListTaskQueuePartitionsResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.ListTaskQueuePartitions)
    *   [func (m *MockWorkflowServiceServer) ListWorkerDeployments(arg0 context.Context, arg1 *workflowservice.ListWorkerDeploymentsRequest) (*workflowservice.ListWorkerDeploymentsResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.ListWorkerDeployments)
    *   [func (m *MockWorkflowServiceServer) ListWorkers(arg0 context.Context, arg1 *workflowservice.ListWorkersRequest) (*workflowservice.ListWorkersResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.ListWorkers)
    *   [func (m *MockWorkflowServiceServer) ListWorkflowExecutions(arg0 context.Context, arg1 *workflowservice.ListWorkflowExecutionsRequest) (*workflowservice.ListWorkflowExecutionsResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.ListWorkflowExecutions)
    *   [func (m *MockWorkflowServiceServer) ListWorkflowRules(arg0 context.Context, arg1 *workflowservice.ListWorkflowRulesRequest) (*workflowservice.ListWorkflowRulesResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.ListWorkflowRules)
    *   [func (m *MockWorkflowServiceServer) PatchSchedule(arg0 context.Context, arg1 *workflowservice.PatchScheduleRequest) (*workflowservice.PatchScheduleResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.PatchSchedule)
    *   [func (m *MockWorkflowServiceServer) PauseActivity(arg0 context.Context, arg1 *workflowservice.PauseActivityRequest) (*workflowservice.PauseActivityResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.PauseActivity)
    *   [func (m *MockWorkflowServiceServer) PauseWorkflowExecution(arg0 context.Context, arg1 *workflowservice.PauseWorkflowExecutionRequest) (*workflowservice.PauseWorkflowExecutionResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.PauseWorkflowExecution)
    *   [func (m *MockWorkflowServiceServer) PollActivityExecution(arg0 context.Context, arg1 *workflowservice.PollActivityExecutionRequest) (*workflowservice.PollActivityExecutionResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.PollActivityExecution)
    *   [func (m *MockWorkflowServiceServer) PollActivityTaskQueue(arg0 context.Context, arg1 *workflowservice.PollActivityTaskQueueRequest) (*workflowservice.PollActivityTaskQueueResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.PollActivityTaskQueue)
    *   [func (m *MockWorkflowServiceServer) PollNexusTaskQueue(arg0 context.Context, arg1 *workflowservice.PollNexusTaskQueueRequest) (*workflowservice.PollNexusTaskQueueResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.PollNexusTaskQueue)
    *   [func (m *MockWorkflowServiceServer) PollWorkflowExecutionUpdate(arg0 context.Context, arg1 *workflowservice.PollWorkflowExecutionUpdateRequest) (*workflowservice.PollWorkflowExecutionUpdateResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.PollWorkflowExecutionUpdate)
    *   [func (m *MockWorkflowServiceServer) PollWorkflowTaskQueue(arg0 context.Context, arg1 *workflowservice.PollWorkflowTaskQueueRequest) (*workflowservice.PollWorkflowTaskQueueResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.PollWorkflowTaskQueue)
    *   [func (m *MockWorkflowServiceServer) QueryWorkflow(arg0 context.Context, arg1 *workflowservice.QueryWorkflowRequest) (*workflowservice.QueryWorkflowResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.QueryWorkflow)
    *   [func (m *MockWorkflowServiceServer) RecordActivityTaskHeartbeat(arg0 context.Context, arg1 *workflowservice.RecordActivityTaskHeartbeatRequest) (*workflowservice.RecordActivityTaskHeartbeatResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.RecordActivityTaskHeartbeat)
    *   [func (m *MockWorkflowServiceServer) RecordActivityTaskHeartbeatById(arg0 context.Context, ...) (*workflowservice.RecordActivityTaskHeartbeatByIdResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.RecordActivityTaskHeartbeatById)
    *   [func (m *MockWorkflowServiceServer) RecordWorkerHeartbeat(arg0 context.Context, arg1 *workflowservice.RecordWorkerHeartbeatRequest) (*workflowservice.RecordWorkerHeartbeatResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.RecordWorkerHeartbeat)
    *   [func (m *MockWorkflowServiceServer) RegisterNamespace(arg0 context.Context, arg1 *workflowservice.RegisterNamespaceRequest) (*workflowservice.RegisterNamespaceResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.RegisterNamespace)
    *   [func (m *MockWorkflowServiceServer) RequestCancelActivityExecution(arg0 context.Context, ...) (*workflowservice.RequestCancelActivityExecutionResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.RequestCancelActivityExecution)
    *   [func (m *MockWorkflowServiceServer) RequestCancelWorkflowExecution(arg0 context.Context, ...) (*workflowservice.RequestCancelWorkflowExecutionResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.RequestCancelWorkflowExecution)
    *   [func (m *MockWorkflowServiceServer) ResetActivity(arg0 context.Context, arg1 *workflowservice.ResetActivityRequest) (*workflowservice.ResetActivityResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.ResetActivity)
    *   [func (m *MockWorkflowServiceServer) ResetStickyTaskQueue(arg0 context.Context, arg1 *workflowservice.ResetStickyTaskQueueRequest) (*workflowservice.ResetStickyTaskQueueResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.ResetStickyTaskQueue)
    *   [func (m *MockWorkflowServiceServer) ResetWorkflowExecution(arg0 context.Context, arg1 *workflowservice.ResetWorkflowExecutionRequest) (*workflowservice.ResetWorkflowExecutionResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.ResetWorkflowExecution)
    *   [func (m *MockWorkflowServiceServer) RespondActivityTaskCanceled(arg0 context.Context, arg1 *workflowservice.RespondActivityTaskCanceledRequest) (*workflowservice.RespondActivityTaskCanceledResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.RespondActivityTaskCanceled)
    *   [func (m *MockWorkflowServiceServer) RespondActivityTaskCanceledById(arg0 context.Context, ...) (*workflowservice.RespondActivityTaskCanceledByIdResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.RespondActivityTaskCanceledById)
    *   [func (m *MockWorkflowServiceServer) RespondActivityTaskCompleted(arg0 context.Context, ...) (*workflowservice.RespondActivityTaskCompletedResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.RespondActivityTaskCompleted)
    *   [func (m *MockWorkflowServiceServer) RespondActivityTaskCompletedById(arg0 context.Context, ...) (*workflowservice.RespondActivityTaskCompletedByIdResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.RespondActivityTaskCompletedById)
    *   [func (m *MockWorkflowServiceServer) RespondActivityTaskFailed(arg0 context.Context, arg1 *workflowservice.RespondActivityTaskFailedRequest) (*workflowservice.RespondActivityTaskFailedResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.RespondActivityTaskFailed)
    *   [func (m *MockWorkflowServiceServer) RespondActivityTaskFailedById(arg0 context.Context, ...) (*workflowservice.RespondActivityTaskFailedByIdResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.RespondActivityTaskFailedById)
    *   [func (m *MockWorkflowServiceServer) RespondNexusTaskCompleted(arg0 context.Context, arg1 *workflowservice.RespondNexusTaskCompletedRequest) (*workflowservice.RespondNexusTaskCompletedResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.RespondNexusTaskCompleted)
    *   [func (m *MockWorkflowServiceServer) RespondNexusTaskFailed(arg0 context.Context, arg1 *workflowservice.RespondNexusTaskFailedRequest) (*workflowservice.RespondNexusTaskFailedResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.RespondNexusTaskFailed)
    *   [func (m *MockWorkflowServiceServer) RespondQueryTaskCompleted(arg0 context.Context, arg1 *workflowservice.RespondQueryTaskCompletedRequest) (*workflowservice.RespondQueryTaskCompletedResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.RespondQueryTaskCompleted)
    *   [func (m *MockWorkflowServiceServer) RespondWorkflowTaskCompleted(arg0 context.Context, ...) (*workflowservice.RespondWorkflowTaskCompletedResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.RespondWorkflowTaskCompleted)
    *   [func (m *MockWorkflowServiceServer) RespondWorkflowTaskFailed(arg0 context.Context, arg1 *workflowservice.RespondWorkflowTaskFailedRequest) (*workflowservice.RespondWorkflowTaskFailedResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.RespondWorkflowTaskFailed)
    *   [func (m *MockWorkflowServiceServer) ScanWorkflowExecutions(arg0 context.Context, arg1 *workflowservice.ScanWorkflowExecutionsRequest) (*workflowservice.ScanWorkflowExecutionsResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.ScanWorkflowExecutions)
    *   [func (m *MockWorkflowServiceServer) SetCurrentDeployment(arg0 context.Context, arg1 *workflowservice.SetCurrentDeploymentRequest) (*workflowservice.SetCurrentDeploymentResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.SetCurrentDeployment)
    *   [func (m *MockWorkflowServiceServer) SetWorkerDeploymentCurrentVersion(arg0 context.Context, ...) (*workflowservice.SetWorkerDeploymentCurrentVersionResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.SetWorkerDeploymentCurrentVersion)
    *   [func (m *MockWorkflowServiceServer) SetWorkerDeploymentManager(arg0 context.Context, arg1 *workflowservice.SetWorkerDeploymentManagerRequest) (*workflowservice.SetWorkerDeploymentManagerResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.SetWorkerDeploymentManager)
    *   [func (m *MockWorkflowServiceServer) SetWorkerDeploymentRampingVersion(arg0 context.Context, ...) (*workflowservice.SetWorkerDeploymentRampingVersionResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.SetWorkerDeploymentRampingVersion)
    *   [func (m *MockWorkflowServiceServer) ShutdownWorker(arg0 context.Context, arg1 *workflowservice.ShutdownWorkerRequest) (*workflowservice.ShutdownWorkerResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.ShutdownWorker)
    *   [func (m *MockWorkflowServiceServer) SignalWithStartWorkflowExecution(arg0 context.Context, ...) (*workflowservice.SignalWithStartWorkflowExecutionResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.SignalWithStartWorkflowExecution)
    *   [func (m *MockWorkflowServiceServer) SignalWorkflowExecution(arg0 context.Context, arg1 *workflowservice.SignalWorkflowExecutionRequest) (*workflowservice.SignalWorkflowExecutionResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.SignalWorkflowExecution)
    *   [func (m *MockWorkflowServiceServer) StartActivityExecution(arg0 context.Context, arg1 *workflowservice.StartActivityExecutionRequest) (*workflowservice.StartActivityExecutionResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.StartActivityExecution)
    *   [func (m *MockWorkflowServiceServer) StartBatchOperation(arg0 context.Context, arg1 *workflowservice.StartBatchOperationRequest) (*workflowservice.StartBatchOperationResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.StartBatchOperation)
    *   [func (m *MockWorkflowServiceServer) StartWorkflowExecution(arg0 context.Context, arg1 *workflowservice.StartWorkflowExecutionRequest) (*workflowservice.StartWorkflowExecutionResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.StartWorkflowExecution)
    *   [func (m *MockWorkflowServiceServer) StopBatchOperation(arg0 context.Context, arg1 *workflowservice.StopBatchOperationRequest) (*workflowservice.StopBatchOperationResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.StopBatchOperation)
    *   [func (m *MockWorkflowServiceServer) TerminateActivityExecution(arg0 context.Context, arg1 *workflowservice.TerminateActivityExecutionRequest) (*workflowservice.TerminateActivityExecutionResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.TerminateActivityExecution)
    *   [func (m *MockWorkflowServiceServer) TerminateWorkflowExecution(arg0 context.Context, arg1 *workflowservice.TerminateWorkflowExecutionRequest) (*workflowservice.TerminateWorkflowExecutionResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.TerminateWorkflowExecution)
    *   [func (m *MockWorkflowServiceServer) TriggerWorkflowRule(arg0 context.Context, arg1 *workflowservice.TriggerWorkflowRuleRequest) (*workflowservice.TriggerWorkflowRuleResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.TriggerWorkflowRule)
    *   [func (m *MockWorkflowServiceServer) UnpauseActivity(arg0 context.Context, arg1 *workflowservice.UnpauseActivityRequest) (*workflowservice.UnpauseActivityResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.UnpauseActivity)
    *   [func (m *MockWorkflowServiceServer) UnpauseWorkflowExecution(arg0 context.Context, arg1 *workflowservice.UnpauseWorkflowExecutionRequest) (*workflowservice.UnpauseWorkflowExecutionResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.UnpauseWorkflowExecution)
    *   [func (m *MockWorkflowServiceServer) UpdateActivityOptions(arg0 context.Context, arg1 *workflowservice.UpdateActivityOptionsRequest) (*workflowservice.UpdateActivityOptionsResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.UpdateActivityOptions)
    *   [func (m *MockWorkflowServiceServer) UpdateNamespace(arg0 context.Context, arg1 *workflowservice.UpdateNamespaceRequest) (*workflowservice.UpdateNamespaceResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.UpdateNamespace)
    *   [func (m *MockWorkflowServiceServer) UpdateSchedule(arg0 context.Context, arg1 *workflowservice.UpdateScheduleRequest) (*workflowservice.UpdateScheduleResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.UpdateSchedule)
    *   [func (m *MockWorkflowServiceServer) UpdateTaskQueueConfig(arg0 context.Context, arg1 *workflowservice.UpdateTaskQueueConfigRequest) (*workflowservice.UpdateTaskQueueConfigResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.UpdateTaskQueueConfig)
    *   [func (m *MockWorkflowServiceServer) UpdateWorkerBuildIdCompatibility(arg0 context.Context, ...) (*workflowservice.UpdateWorkerBuildIdCompatibilityResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.UpdateWorkerBuildIdCompatibility)
    *   [func (m *MockWorkflowServiceServer) UpdateWorkerConfig(arg0 context.Context, arg1 *workflowservice.UpdateWorkerConfigRequest) (*workflowservice.UpdateWorkerConfigResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.UpdateWorkerConfig)
    *   [func (m *MockWorkflowServiceServer) UpdateWorkerDeploymentVersionMetadata(arg0 context.Context, ...) (*workflowservice.UpdateWorkerDeploymentVersionMetadataResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.UpdateWorkerDeploymentVersionMetadata)
    *   [func (m *MockWorkflowServiceServer) UpdateWorkerVersioningRules(arg0 context.Context, arg1 *workflowservice.UpdateWorkerVersioningRulesRequest) (*workflowservice.UpdateWorkerVersioningRulesResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.UpdateWorkerVersioningRules)
    *   [func (m *MockWorkflowServiceServer) UpdateWorkflowExecution(arg0 context.Context, arg1 *workflowservice.UpdateWorkflowExecutionRequest) (*workflowservice.UpdateWorkflowExecutionResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.UpdateWorkflowExecution)
    *   [func (m *MockWorkflowServiceServer) UpdateWorkflowExecutionOptions(arg0 context.Context, ...) (*workflowservice.UpdateWorkflowExecutionOptionsResponse, error)](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServer.UpdateWorkflowExecutionOptions)

*   [type MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)
*       *   [func (mr *MockWorkflowServiceServerMockRecorder) CountActivityExecutions(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.CountActivityExecutions)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) CountSchedules(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.CountSchedules)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) CountWorkflowExecutions(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.CountWorkflowExecutions)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) CreateSchedule(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.CreateSchedule)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) CreateWorkflowRule(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.CreateWorkflowRule)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) DeleteActivityExecution(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.DeleteActivityExecution)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) DeleteSchedule(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.DeleteSchedule)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) DeleteWorkerDeployment(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.DeleteWorkerDeployment)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) DeleteWorkerDeploymentVersion(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.DeleteWorkerDeploymentVersion)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) DeleteWorkflowExecution(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.DeleteWorkflowExecution)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) DeleteWorkflowRule(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.DeleteWorkflowRule)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) DeprecateNamespace(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.DeprecateNamespace)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) DescribeActivityExecution(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.DescribeActivityExecution)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) DescribeBatchOperation(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.DescribeBatchOperation)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) DescribeDeployment(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.DescribeDeployment)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) DescribeNamespace(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.DescribeNamespace)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) DescribeSchedule(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.DescribeSchedule)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) DescribeTaskQueue(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.DescribeTaskQueue)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) DescribeWorker(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.DescribeWorker)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) DescribeWorkerDeployment(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.DescribeWorkerDeployment)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) DescribeWorkerDeploymentVersion(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.DescribeWorkerDeploymentVersion)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) DescribeWorkflowExecution(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.DescribeWorkflowExecution)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) DescribeWorkflowRule(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.DescribeWorkflowRule)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) ExecuteMultiOperation(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.ExecuteMultiOperation)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) FetchWorkerConfig(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.FetchWorkerConfig)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) GetClusterInfo(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.GetClusterInfo)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) GetCurrentDeployment(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.GetCurrentDeployment)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) GetDeploymentReachability(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.GetDeploymentReachability)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) GetSearchAttributes(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.GetSearchAttributes)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) GetSystemInfo(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.GetSystemInfo)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) GetWorkerBuildIdCompatibility(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.GetWorkerBuildIdCompatibility)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) GetWorkerTaskReachability(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.GetWorkerTaskReachability)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) GetWorkerVersioningRules(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.GetWorkerVersioningRules)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) GetWorkflowExecutionHistory(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.GetWorkflowExecutionHistory)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) GetWorkflowExecutionHistoryReverse(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.GetWorkflowExecutionHistoryReverse)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) ListActivityExecutions(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.ListActivityExecutions)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) ListArchivedWorkflowExecutions(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.ListArchivedWorkflowExecutions)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) ListBatchOperations(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.ListBatchOperations)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) ListClosedWorkflowExecutions(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.ListClosedWorkflowExecutions)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) ListDeployments(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.ListDeployments)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) ListNamespaces(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.ListNamespaces)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) ListOpenWorkflowExecutions(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.ListOpenWorkflowExecutions)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) ListScheduleMatchingTimes(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.ListScheduleMatchingTimes)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) ListSchedules(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.ListSchedules)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) ListTaskQueuePartitions(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.ListTaskQueuePartitions)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) ListWorkerDeployments(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.ListWorkerDeployments)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) ListWorkers(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.ListWorkers)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) ListWorkflowExecutions(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.ListWorkflowExecutions)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) ListWorkflowRules(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.ListWorkflowRules)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) PatchSchedule(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.PatchSchedule)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) PauseActivity(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.PauseActivity)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) PauseWorkflowExecution(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.PauseWorkflowExecution)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) PollActivityExecution(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.PollActivityExecution)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) PollActivityTaskQueue(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.PollActivityTaskQueue)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) PollNexusTaskQueue(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.PollNexusTaskQueue)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) PollWorkflowExecutionUpdate(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.PollWorkflowExecutionUpdate)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) PollWorkflowTaskQueue(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.PollWorkflowTaskQueue)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) QueryWorkflow(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.QueryWorkflow)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) RecordActivityTaskHeartbeat(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.RecordActivityTaskHeartbeat)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) RecordActivityTaskHeartbeatById(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.RecordActivityTaskHeartbeatById)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) RecordWorkerHeartbeat(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.RecordWorkerHeartbeat)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) RegisterNamespace(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.RegisterNamespace)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) RequestCancelActivityExecution(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.RequestCancelActivityExecution)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) RequestCancelWorkflowExecution(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.RequestCancelWorkflowExecution)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) ResetActivity(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.ResetActivity)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) ResetStickyTaskQueue(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.ResetStickyTaskQueue)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) ResetWorkflowExecution(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.ResetWorkflowExecution)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) RespondActivityTaskCanceled(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.RespondActivityTaskCanceled)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) RespondActivityTaskCanceledById(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.RespondActivityTaskCanceledById)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) RespondActivityTaskCompleted(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.RespondActivityTaskCompleted)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) RespondActivityTaskCompletedById(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.RespondActivityTaskCompletedById)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) RespondActivityTaskFailed(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.RespondActivityTaskFailed)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) RespondActivityTaskFailedById(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.RespondActivityTaskFailedById)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) RespondNexusTaskCompleted(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.RespondNexusTaskCompleted)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) RespondNexusTaskFailed(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.RespondNexusTaskFailed)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) RespondQueryTaskCompleted(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.RespondQueryTaskCompleted)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) RespondWorkflowTaskCompleted(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.RespondWorkflowTaskCompleted)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) RespondWorkflowTaskFailed(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.RespondWorkflowTaskFailed)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) ScanWorkflowExecutions(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.ScanWorkflowExecutions)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) SetCurrentDeployment(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.SetCurrentDeployment)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) SetWorkerDeploymentCurrentVersion(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.SetWorkerDeploymentCurrentVersion)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) SetWorkerDeploymentManager(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.SetWorkerDeploymentManager)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) SetWorkerDeploymentRampingVersion(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.SetWorkerDeploymentRampingVersion)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) ShutdownWorker(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.ShutdownWorker)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) SignalWithStartWorkflowExecution(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.SignalWithStartWorkflowExecution)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) SignalWorkflowExecution(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.SignalWorkflowExecution)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) StartActivityExecution(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.StartActivityExecution)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) StartBatchOperation(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.StartBatchOperation)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) StartWorkflowExecution(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.StartWorkflowExecution)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) StopBatchOperation(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.StopBatchOperation)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) TerminateActivityExecution(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.TerminateActivityExecution)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) TerminateWorkflowExecution(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.TerminateWorkflowExecution)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) TriggerWorkflowRule(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.TriggerWorkflowRule)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) UnpauseActivity(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.UnpauseActivity)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) UnpauseWorkflowExecution(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.UnpauseWorkflowExecution)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) UpdateActivityOptions(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.UpdateActivityOptions)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) UpdateNamespace(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.UpdateNamespace)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) UpdateSchedule(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.UpdateSchedule)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) UpdateTaskQueueConfig(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.UpdateTaskQueueConfig)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) UpdateWorkerBuildIdCompatibility(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.UpdateWorkerBuildIdCompatibility)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) UpdateWorkerConfig(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.UpdateWorkerConfig)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) UpdateWorkerDeploymentVersionMetadata(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.UpdateWorkerDeploymentVersionMetadata)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) UpdateWorkerVersioningRules(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.UpdateWorkerVersioningRules)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) UpdateWorkflowExecution(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.UpdateWorkflowExecution)
    *   [func (mr *MockWorkflowServiceServerMockRecorder) UpdateWorkflowExecutionOptions(arg0, arg1 interface{}) *gomock.Call](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder.UpdateWorkflowExecutionOptions)

This section is empty.

This section is empty.

This section is empty.

type MockUnsafeWorkflowServiceServer struct {
	
}

MockUnsafeWorkflowServiceServer is a mock of UnsafeWorkflowServiceServer interface.

NewMockUnsafeWorkflowServiceServer creates a new mock instance.

EXPECT returns an object that allows the caller to indicate expected use.

type MockUnsafeWorkflowServiceServerMockRecorder struct {
	
}

MockUnsafeWorkflowServiceServerMockRecorder is the mock recorder for MockUnsafeWorkflowServiceServer.

type MockWorkflowServiceClient struct {
	
}

MockWorkflowServiceClient is a mock of WorkflowServiceClient interface.

NewMockWorkflowServiceClient creates a new mock instance.

CountActivityExecutions mocks base method.

CountSchedules mocks base method.

CountWorkflowExecutions mocks base method.

CreateSchedule mocks base method.

CreateWorkflowRule mocks base method.

DeleteActivityExecution mocks base method.

DeleteSchedule mocks base method.

DeleteWorkerDeployment mocks base method.

DeleteWorkerDeploymentVersion mocks base method.

DeleteWorkflowExecution mocks base method.

DeleteWorkflowRule mocks base method.

DeprecateNamespace mocks base method.

DescribeActivityExecution mocks base method.

DescribeBatchOperation mocks base method.

DescribeDeployment mocks base method.

DescribeNamespace mocks base method.

DescribeSchedule mocks base method.

DescribeTaskQueue mocks base method.

DescribeWorker mocks base method.

DescribeWorkerDeployment mocks base method.

DescribeWorkerDeploymentVersion mocks base method.

DescribeWorkflowExecution mocks base method.

DescribeWorkflowRule mocks base method.

EXPECT returns an object that allows the caller to indicate expected use.

ExecuteMultiOperation mocks base method.

FetchWorkerConfig mocks base method.

GetClusterInfo mocks base method.

GetCurrentDeployment mocks base method.

GetDeploymentReachability mocks base method.

GetSearchAttributes mocks base method.

GetSystemInfo mocks base method.

GetWorkerBuildIdCompatibility mocks base method.

GetWorkerTaskReachability mocks base method.

GetWorkerVersioningRules mocks base method.

GetWorkflowExecutionHistory mocks base method.

GetWorkflowExecutionHistoryReverse mocks base method.

ListActivityExecutions mocks base method.

ListArchivedWorkflowExecutions mocks base method.

ListBatchOperations mocks base method.

ListClosedWorkflowExecutions mocks base method.

ListDeployments mocks base method.

ListNamespaces mocks base method.

ListOpenWorkflowExecutions mocks base method.

ListScheduleMatchingTimes mocks base method.

ListSchedules mocks base method.

ListTaskQueuePartitions mocks base method.

ListWorkerDeployments mocks base method.

ListWorkers mocks base method.

ListWorkflowExecutions mocks base method.

ListWorkflowRules mocks base method.

PatchSchedule mocks base method.

PauseActivity mocks base method.

PauseWorkflowExecution mocks base method.

PollActivityExecution mocks base method.

PollActivityTaskQueue mocks base method.

PollNexusTaskQueue mocks base method.

PollWorkflowExecutionUpdate mocks base method.

PollWorkflowTaskQueue mocks base method.

QueryWorkflow mocks base method.

RecordActivityTaskHeartbeat mocks base method.

RecordActivityTaskHeartbeatById mocks base method.

RecordWorkerHeartbeat mocks base method.

RegisterNamespace mocks base method.

RequestCancelActivityExecution mocks base method.

RequestCancelWorkflowExecution mocks base method.

ResetActivity mocks base method.

ResetStickyTaskQueue mocks base method.

ResetWorkflowExecution mocks base method.

RespondActivityTaskCanceled mocks base method.

RespondActivityTaskCanceledById mocks base method.

RespondActivityTaskCompleted mocks base method.

RespondActivityTaskCompletedById mocks base method.

RespondActivityTaskFailed mocks base method.

RespondActivityTaskFailedById mocks base method.

RespondNexusTaskCompleted mocks base method.

RespondNexusTaskFailed mocks base method.

RespondQueryTaskCompleted mocks base method.

RespondWorkflowTaskCompleted mocks base method.

RespondWorkflowTaskFailed mocks base method.

ScanWorkflowExecutions mocks base method.

SetCurrentDeployment mocks base method.

SetWorkerDeploymentCurrentVersion mocks base method.

SetWorkerDeploymentManager mocks base method.

SetWorkerDeploymentRampingVersion mocks base method.

ShutdownWorker mocks base method.

SignalWithStartWorkflowExecution mocks base method.

SignalWorkflowExecution mocks base method.

StartActivityExecution mocks base method.

StartBatchOperation mocks base method.

StartWorkflowExecution mocks base method.

StopBatchOperation mocks base method.

TerminateActivityExecution mocks base method.

TerminateWorkflowExecution mocks base method.

TriggerWorkflowRule mocks base method.

UnpauseActivity mocks base method.

UnpauseWorkflowExecution mocks base method.

UpdateActivityOptions mocks base method.

UpdateNamespace mocks base method.

UpdateSchedule mocks base method.

UpdateTaskQueueConfig mocks base method.

UpdateWorkerBuildIdCompatibility mocks base method.

UpdateWorkerConfig mocks base method.

UpdateWorkerDeploymentVersionMetadata mocks base method.

UpdateWorkerVersioningRules mocks base method.

UpdateWorkflowExecution mocks base method.

UpdateWorkflowExecutionOptions mocks base method.

type MockWorkflowServiceClientMockRecorder struct {
	
}

MockWorkflowServiceClientMockRecorder is the mock recorder for MockWorkflowServiceClient.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) CountActivityExecutions(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

CountActivityExecutions indicates an expected call of CountActivityExecutions.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) CountSchedules(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

CountSchedules indicates an expected call of CountSchedules.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) CountWorkflowExecutions(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

CountWorkflowExecutions indicates an expected call of CountWorkflowExecutions.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) CreateSchedule(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

CreateSchedule indicates an expected call of CreateSchedule.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) CreateWorkflowRule(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

CreateWorkflowRule indicates an expected call of CreateWorkflowRule.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) DeleteActivityExecution(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

DeleteActivityExecution indicates an expected call of DeleteActivityExecution.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) DeleteSchedule(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

DeleteSchedule indicates an expected call of DeleteSchedule.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) DeleteWorkerDeployment(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

DeleteWorkerDeployment indicates an expected call of DeleteWorkerDeployment.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) DeleteWorkerDeploymentVersion(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

DeleteWorkerDeploymentVersion indicates an expected call of DeleteWorkerDeploymentVersion.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) DeleteWorkflowExecution(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

DeleteWorkflowExecution indicates an expected call of DeleteWorkflowExecution.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) DeleteWorkflowRule(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

DeleteWorkflowRule indicates an expected call of DeleteWorkflowRule.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) DeprecateNamespace(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

DeprecateNamespace indicates an expected call of DeprecateNamespace.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) DescribeActivityExecution(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

DescribeActivityExecution indicates an expected call of DescribeActivityExecution.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) DescribeBatchOperation(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

DescribeBatchOperation indicates an expected call of DescribeBatchOperation.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) DescribeDeployment(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

DescribeDeployment indicates an expected call of DescribeDeployment.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) DescribeNamespace(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

DescribeNamespace indicates an expected call of DescribeNamespace.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) DescribeSchedule(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

DescribeSchedule indicates an expected call of DescribeSchedule.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) DescribeTaskQueue(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

DescribeTaskQueue indicates an expected call of DescribeTaskQueue.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) DescribeWorker(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

DescribeWorker indicates an expected call of DescribeWorker.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) DescribeWorkerDeployment(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

DescribeWorkerDeployment indicates an expected call of DescribeWorkerDeployment.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) DescribeWorkerDeploymentVersion(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

DescribeWorkerDeploymentVersion indicates an expected call of DescribeWorkerDeploymentVersion.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) DescribeWorkflowExecution(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

DescribeWorkflowExecution indicates an expected call of DescribeWorkflowExecution.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) DescribeWorkflowRule(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

DescribeWorkflowRule indicates an expected call of DescribeWorkflowRule.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) ExecuteMultiOperation(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

ExecuteMultiOperation indicates an expected call of ExecuteMultiOperation.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) FetchWorkerConfig(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

FetchWorkerConfig indicates an expected call of FetchWorkerConfig.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) GetClusterInfo(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

GetClusterInfo indicates an expected call of GetClusterInfo.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) GetCurrentDeployment(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

GetCurrentDeployment indicates an expected call of GetCurrentDeployment.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) GetDeploymentReachability(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

GetDeploymentReachability indicates an expected call of GetDeploymentReachability.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) GetSearchAttributes(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

GetSearchAttributes indicates an expected call of GetSearchAttributes.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) GetSystemInfo(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

GetSystemInfo indicates an expected call of GetSystemInfo.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) GetWorkerBuildIdCompatibility(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

GetWorkerBuildIdCompatibility indicates an expected call of GetWorkerBuildIdCompatibility.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) GetWorkerTaskReachability(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

GetWorkerTaskReachability indicates an expected call of GetWorkerTaskReachability.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) GetWorkerVersioningRules(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

GetWorkerVersioningRules indicates an expected call of GetWorkerVersioningRules.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) GetWorkflowExecutionHistory(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

GetWorkflowExecutionHistory indicates an expected call of GetWorkflowExecutionHistory.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) GetWorkflowExecutionHistoryReverse(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

GetWorkflowExecutionHistoryReverse indicates an expected call of GetWorkflowExecutionHistoryReverse.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) ListActivityExecutions(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

ListActivityExecutions indicates an expected call of ListActivityExecutions.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) ListArchivedWorkflowExecutions(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

ListArchivedWorkflowExecutions indicates an expected call of ListArchivedWorkflowExecutions.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) ListBatchOperations(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

ListBatchOperations indicates an expected call of ListBatchOperations.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) ListClosedWorkflowExecutions(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

ListClosedWorkflowExecutions indicates an expected call of ListClosedWorkflowExecutions.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) ListDeployments(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

ListDeployments indicates an expected call of ListDeployments.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) ListNamespaces(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

ListNamespaces indicates an expected call of ListNamespaces.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) ListOpenWorkflowExecutions(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

ListOpenWorkflowExecutions indicates an expected call of ListOpenWorkflowExecutions.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) ListScheduleMatchingTimes(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

ListScheduleMatchingTimes indicates an expected call of ListScheduleMatchingTimes.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) ListSchedules(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

ListSchedules indicates an expected call of ListSchedules.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) ListTaskQueuePartitions(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

ListTaskQueuePartitions indicates an expected call of ListTaskQueuePartitions.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) ListWorkerDeployments(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

ListWorkerDeployments indicates an expected call of ListWorkerDeployments.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) ListWorkers(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

ListWorkers indicates an expected call of ListWorkers.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) ListWorkflowExecutions(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

ListWorkflowExecutions indicates an expected call of ListWorkflowExecutions.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) ListWorkflowRules(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

ListWorkflowRules indicates an expected call of ListWorkflowRules.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) PatchSchedule(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

PatchSchedule indicates an expected call of PatchSchedule.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) PauseActivity(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

PauseActivity indicates an expected call of PauseActivity.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) PauseWorkflowExecution(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

PauseWorkflowExecution indicates an expected call of PauseWorkflowExecution.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) PollActivityExecution(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

PollActivityExecution indicates an expected call of PollActivityExecution.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) PollActivityTaskQueue(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

PollActivityTaskQueue indicates an expected call of PollActivityTaskQueue.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) PollNexusTaskQueue(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

PollNexusTaskQueue indicates an expected call of PollNexusTaskQueue.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) PollWorkflowExecutionUpdate(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

PollWorkflowExecutionUpdate indicates an expected call of PollWorkflowExecutionUpdate.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) PollWorkflowTaskQueue(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

PollWorkflowTaskQueue indicates an expected call of PollWorkflowTaskQueue.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) QueryWorkflow(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

QueryWorkflow indicates an expected call of QueryWorkflow.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) RecordActivityTaskHeartbeat(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

RecordActivityTaskHeartbeat indicates an expected call of RecordActivityTaskHeartbeat.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) RecordActivityTaskHeartbeatById(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

RecordActivityTaskHeartbeatById indicates an expected call of RecordActivityTaskHeartbeatById.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) RecordWorkerHeartbeat(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

RecordWorkerHeartbeat indicates an expected call of RecordWorkerHeartbeat.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) RegisterNamespace(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

RegisterNamespace indicates an expected call of RegisterNamespace.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) RequestCancelActivityExecution(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

RequestCancelActivityExecution indicates an expected call of RequestCancelActivityExecution.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) RequestCancelWorkflowExecution(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

RequestCancelWorkflowExecution indicates an expected call of RequestCancelWorkflowExecution.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) ResetActivity(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

ResetActivity indicates an expected call of ResetActivity.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) ResetStickyTaskQueue(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

ResetStickyTaskQueue indicates an expected call of ResetStickyTaskQueue.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) ResetWorkflowExecution(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

ResetWorkflowExecution indicates an expected call of ResetWorkflowExecution.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) RespondActivityTaskCanceled(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

RespondActivityTaskCanceled indicates an expected call of RespondActivityTaskCanceled.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) RespondActivityTaskCanceledById(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

RespondActivityTaskCanceledById indicates an expected call of RespondActivityTaskCanceledById.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) RespondActivityTaskCompleted(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

RespondActivityTaskCompleted indicates an expected call of RespondActivityTaskCompleted.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) RespondActivityTaskCompletedById(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

RespondActivityTaskCompletedById indicates an expected call of RespondActivityTaskCompletedById.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) RespondActivityTaskFailed(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

RespondActivityTaskFailed indicates an expected call of RespondActivityTaskFailed.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) RespondActivityTaskFailedById(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

RespondActivityTaskFailedById indicates an expected call of RespondActivityTaskFailedById.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) RespondNexusTaskCompleted(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

RespondNexusTaskCompleted indicates an expected call of RespondNexusTaskCompleted.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) RespondNexusTaskFailed(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

RespondNexusTaskFailed indicates an expected call of RespondNexusTaskFailed.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) RespondQueryTaskCompleted(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

RespondQueryTaskCompleted indicates an expected call of RespondQueryTaskCompleted.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) RespondWorkflowTaskCompleted(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

RespondWorkflowTaskCompleted indicates an expected call of RespondWorkflowTaskCompleted.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) RespondWorkflowTaskFailed(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

RespondWorkflowTaskFailed indicates an expected call of RespondWorkflowTaskFailed.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) ScanWorkflowExecutions(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

ScanWorkflowExecutions indicates an expected call of ScanWorkflowExecutions.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) SetCurrentDeployment(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

SetCurrentDeployment indicates an expected call of SetCurrentDeployment.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) SetWorkerDeploymentCurrentVersion(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

SetWorkerDeploymentCurrentVersion indicates an expected call of SetWorkerDeploymentCurrentVersion.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) SetWorkerDeploymentManager(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

SetWorkerDeploymentManager indicates an expected call of SetWorkerDeploymentManager.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) SetWorkerDeploymentRampingVersion(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

SetWorkerDeploymentRampingVersion indicates an expected call of SetWorkerDeploymentRampingVersion.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) ShutdownWorker(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

ShutdownWorker indicates an expected call of ShutdownWorker.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) SignalWithStartWorkflowExecution(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

SignalWithStartWorkflowExecution indicates an expected call of SignalWithStartWorkflowExecution.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) SignalWorkflowExecution(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

SignalWorkflowExecution indicates an expected call of SignalWorkflowExecution.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) StartActivityExecution(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

StartActivityExecution indicates an expected call of StartActivityExecution.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) StartBatchOperation(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

StartBatchOperation indicates an expected call of StartBatchOperation.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) StartWorkflowExecution(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

StartWorkflowExecution indicates an expected call of StartWorkflowExecution.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) StopBatchOperation(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

StopBatchOperation indicates an expected call of StopBatchOperation.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) TerminateActivityExecution(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

TerminateActivityExecution indicates an expected call of TerminateActivityExecution.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) TerminateWorkflowExecution(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

TerminateWorkflowExecution indicates an expected call of TerminateWorkflowExecution.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) TriggerWorkflowRule(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

TriggerWorkflowRule indicates an expected call of TriggerWorkflowRule.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) UnpauseActivity(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

UnpauseActivity indicates an expected call of UnpauseActivity.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) UnpauseWorkflowExecution(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

UnpauseWorkflowExecution indicates an expected call of UnpauseWorkflowExecution.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) UpdateActivityOptions(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

UpdateActivityOptions indicates an expected call of UpdateActivityOptions.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) UpdateNamespace(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

UpdateNamespace indicates an expected call of UpdateNamespace.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) UpdateSchedule(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

UpdateSchedule indicates an expected call of UpdateSchedule.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) UpdateTaskQueueConfig(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

UpdateTaskQueueConfig indicates an expected call of UpdateTaskQueueConfig.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) UpdateWorkerBuildIdCompatibility(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

UpdateWorkerBuildIdCompatibility indicates an expected call of UpdateWorkerBuildIdCompatibility.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) UpdateWorkerConfig(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

UpdateWorkerConfig indicates an expected call of UpdateWorkerConfig.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) UpdateWorkerDeploymentVersionMetadata(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

UpdateWorkerDeploymentVersionMetadata indicates an expected call of UpdateWorkerDeploymentVersionMetadata.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) UpdateWorkerVersioningRules(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

UpdateWorkerVersioningRules indicates an expected call of UpdateWorkerVersioningRules.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) UpdateWorkflowExecution(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

UpdateWorkflowExecution indicates an expected call of UpdateWorkflowExecution.

func (mr *[MockWorkflowServiceClientMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceClientMockRecorder)) UpdateWorkflowExecutionOptions(ctx, in interface{}, opts ...interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

UpdateWorkflowExecutionOptions indicates an expected call of UpdateWorkflowExecutionOptions.

MockWorkflowServiceServer is a mock of WorkflowServiceServer interface.

NewMockWorkflowServiceServer creates a new mock instance.

CountActivityExecutions mocks base method.

CountSchedules mocks base method.

CountWorkflowExecutions mocks base method.

CreateSchedule mocks base method.

CreateWorkflowRule mocks base method.

DeleteActivityExecution mocks base method.

DeleteSchedule mocks base method.

DeleteWorkerDeployment mocks base method.

DeleteWorkerDeploymentVersion mocks base method.

DeleteWorkflowExecution mocks base method.

DeleteWorkflowRule mocks base method.

DeprecateNamespace mocks base method.

DescribeActivityExecution mocks base method.

DescribeBatchOperation mocks base method.

DescribeDeployment mocks base method.

DescribeNamespace mocks base method.

DescribeSchedule mocks base method.

DescribeTaskQueue mocks base method.

DescribeWorker mocks base method.

DescribeWorkerDeployment mocks base method.

DescribeWorkerDeploymentVersion mocks base method.

DescribeWorkflowExecution mocks base method.

DescribeWorkflowRule mocks base method.

EXPECT returns an object that allows the caller to indicate expected use.

ExecuteMultiOperation mocks base method.

FetchWorkerConfig mocks base method.

GetClusterInfo mocks base method.

GetCurrentDeployment mocks base method.

GetDeploymentReachability mocks base method.

GetSearchAttributes mocks base method.

GetSystemInfo mocks base method.

GetWorkerBuildIdCompatibility mocks base method.

GetWorkerTaskReachability mocks base method.

GetWorkerVersioningRules mocks base method.

GetWorkflowExecutionHistory mocks base method.

GetWorkflowExecutionHistoryReverse mocks base method.

ListActivityExecutions mocks base method.

ListArchivedWorkflowExecutions mocks base method.

ListBatchOperations mocks base method.

ListClosedWorkflowExecutions mocks base method.

ListDeployments mocks base method.

ListNamespaces mocks base method.

ListOpenWorkflowExecutions mocks base method.

ListScheduleMatchingTimes mocks base method.

ListSchedules mocks base method.

ListTaskQueuePartitions mocks base method.

ListWorkerDeployments mocks base method.

ListWorkers mocks base method.

ListWorkflowExecutions mocks base method.

ListWorkflowRules mocks base method.

PatchSchedule mocks base method.

PauseActivity mocks base method.

PauseWorkflowExecution mocks base method.

PollActivityExecution mocks base method.

PollActivityTaskQueue mocks base method.

PollNexusTaskQueue mocks base method.

PollWorkflowExecutionUpdate mocks base method.

PollWorkflowTaskQueue mocks base method.

QueryWorkflow mocks base method.

RecordActivityTaskHeartbeat mocks base method.

RecordActivityTaskHeartbeatById mocks base method.

RecordWorkerHeartbeat mocks base method.

RegisterNamespace mocks base method.

RequestCancelActivityExecution mocks base method.

RequestCancelWorkflowExecution mocks base method.

ResetActivity mocks base method.

ResetStickyTaskQueue mocks base method.

ResetWorkflowExecution mocks base method.

RespondActivityTaskCanceled mocks base method.

RespondActivityTaskCanceledById mocks base method.

RespondActivityTaskCompleted mocks base method.

RespondActivityTaskCompletedById mocks base method.

RespondActivityTaskFailed mocks base method.

RespondActivityTaskFailedById mocks base method.

RespondNexusTaskCompleted mocks base method.

RespondNexusTaskFailed mocks base method.

RespondQueryTaskCompleted mocks base method.

RespondWorkflowTaskCompleted mocks base method.

RespondWorkflowTaskFailed mocks base method.

ScanWorkflowExecutions mocks base method.

SetCurrentDeployment mocks base method.

SetWorkerDeploymentCurrentVersion mocks base method.

SetWorkerDeploymentManager mocks base method.

SetWorkerDeploymentRampingVersion mocks base method.

ShutdownWorker mocks base method.

SignalWithStartWorkflowExecution mocks base method.

SignalWorkflowExecution mocks base method.

StartActivityExecution mocks base method.

StartBatchOperation mocks base method.

StartWorkflowExecution mocks base method.

StopBatchOperation mocks base method.

TerminateActivityExecution mocks base method.

TerminateWorkflowExecution mocks base method.

TriggerWorkflowRule mocks base method.

UnpauseActivity mocks base method.

UnpauseWorkflowExecution mocks base method.

UpdateActivityOptions mocks base method.

UpdateNamespace mocks base method.

UpdateSchedule mocks base method.

UpdateTaskQueueConfig mocks base method.

UpdateWorkerBuildIdCompatibility mocks base method.

UpdateWorkerConfig mocks base method.

UpdateWorkerDeploymentVersionMetadata mocks base method.

UpdateWorkerVersioningRules mocks base method.

UpdateWorkflowExecution mocks base method.

UpdateWorkflowExecutionOptions mocks base method.

type MockWorkflowServiceServerMockRecorder struct {
	
}

MockWorkflowServiceServerMockRecorder is the mock recorder for MockWorkflowServiceServer.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) CountActivityExecutions(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

CountActivityExecutions indicates an expected call of CountActivityExecutions.

CountSchedules indicates an expected call of CountSchedules.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) CountWorkflowExecutions(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

CountWorkflowExecutions indicates an expected call of CountWorkflowExecutions.

CreateSchedule indicates an expected call of CreateSchedule.

CreateWorkflowRule indicates an expected call of CreateWorkflowRule.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) DeleteActivityExecution(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

DeleteActivityExecution indicates an expected call of DeleteActivityExecution.

DeleteSchedule indicates an expected call of DeleteSchedule.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) DeleteWorkerDeployment(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

DeleteWorkerDeployment indicates an expected call of DeleteWorkerDeployment.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) DeleteWorkerDeploymentVersion(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

DeleteWorkerDeploymentVersion indicates an expected call of DeleteWorkerDeploymentVersion.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) DeleteWorkflowExecution(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

DeleteWorkflowExecution indicates an expected call of DeleteWorkflowExecution.

DeleteWorkflowRule indicates an expected call of DeleteWorkflowRule.

DeprecateNamespace indicates an expected call of DeprecateNamespace.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) DescribeActivityExecution(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

DescribeActivityExecution indicates an expected call of DescribeActivityExecution.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) DescribeBatchOperation(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

DescribeBatchOperation indicates an expected call of DescribeBatchOperation.

DescribeDeployment indicates an expected call of DescribeDeployment.

DescribeNamespace indicates an expected call of DescribeNamespace.

DescribeSchedule indicates an expected call of DescribeSchedule.

DescribeTaskQueue indicates an expected call of DescribeTaskQueue.

DescribeWorker indicates an expected call of DescribeWorker.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) DescribeWorkerDeployment(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

DescribeWorkerDeployment indicates an expected call of DescribeWorkerDeployment.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) DescribeWorkerDeploymentVersion(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

DescribeWorkerDeploymentVersion indicates an expected call of DescribeWorkerDeploymentVersion.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) DescribeWorkflowExecution(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

DescribeWorkflowExecution indicates an expected call of DescribeWorkflowExecution.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) DescribeWorkflowRule(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

DescribeWorkflowRule indicates an expected call of DescribeWorkflowRule.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) ExecuteMultiOperation(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

ExecuteMultiOperation indicates an expected call of ExecuteMultiOperation.

FetchWorkerConfig indicates an expected call of FetchWorkerConfig.

GetClusterInfo indicates an expected call of GetClusterInfo.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) GetCurrentDeployment(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

GetCurrentDeployment indicates an expected call of GetCurrentDeployment.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) GetDeploymentReachability(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

GetDeploymentReachability indicates an expected call of GetDeploymentReachability.

GetSearchAttributes indicates an expected call of GetSearchAttributes.

GetSystemInfo indicates an expected call of GetSystemInfo.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) GetWorkerBuildIdCompatibility(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

GetWorkerBuildIdCompatibility indicates an expected call of GetWorkerBuildIdCompatibility.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) GetWorkerTaskReachability(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

GetWorkerTaskReachability indicates an expected call of GetWorkerTaskReachability.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) GetWorkerVersioningRules(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

GetWorkerVersioningRules indicates an expected call of GetWorkerVersioningRules.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) GetWorkflowExecutionHistory(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

GetWorkflowExecutionHistory indicates an expected call of GetWorkflowExecutionHistory.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) GetWorkflowExecutionHistoryReverse(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

GetWorkflowExecutionHistoryReverse indicates an expected call of GetWorkflowExecutionHistoryReverse.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) ListActivityExecutions(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

ListActivityExecutions indicates an expected call of ListActivityExecutions.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) ListArchivedWorkflowExecutions(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

ListArchivedWorkflowExecutions indicates an expected call of ListArchivedWorkflowExecutions.

ListBatchOperations indicates an expected call of ListBatchOperations.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) ListClosedWorkflowExecutions(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

ListClosedWorkflowExecutions indicates an expected call of ListClosedWorkflowExecutions.

ListDeployments indicates an expected call of ListDeployments.

ListNamespaces indicates an expected call of ListNamespaces.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) ListOpenWorkflowExecutions(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

ListOpenWorkflowExecutions indicates an expected call of ListOpenWorkflowExecutions.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) ListScheduleMatchingTimes(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

ListScheduleMatchingTimes indicates an expected call of ListScheduleMatchingTimes.

ListSchedules indicates an expected call of ListSchedules.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) ListTaskQueuePartitions(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

ListTaskQueuePartitions indicates an expected call of ListTaskQueuePartitions.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) ListWorkerDeployments(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

ListWorkerDeployments indicates an expected call of ListWorkerDeployments.

ListWorkers indicates an expected call of ListWorkers.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) ListWorkflowExecutions(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

ListWorkflowExecutions indicates an expected call of ListWorkflowExecutions.

ListWorkflowRules indicates an expected call of ListWorkflowRules.

PatchSchedule indicates an expected call of PatchSchedule.

PauseActivity indicates an expected call of PauseActivity.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) PauseWorkflowExecution(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

PauseWorkflowExecution indicates an expected call of PauseWorkflowExecution.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) PollActivityExecution(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

PollActivityExecution indicates an expected call of PollActivityExecution.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) PollActivityTaskQueue(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

PollActivityTaskQueue indicates an expected call of PollActivityTaskQueue.

PollNexusTaskQueue indicates an expected call of PollNexusTaskQueue.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) PollWorkflowExecutionUpdate(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

PollWorkflowExecutionUpdate indicates an expected call of PollWorkflowExecutionUpdate.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) PollWorkflowTaskQueue(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

PollWorkflowTaskQueue indicates an expected call of PollWorkflowTaskQueue.

QueryWorkflow indicates an expected call of QueryWorkflow.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) RecordActivityTaskHeartbeat(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

RecordActivityTaskHeartbeat indicates an expected call of RecordActivityTaskHeartbeat.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) RecordActivityTaskHeartbeatById(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

RecordActivityTaskHeartbeatById indicates an expected call of RecordActivityTaskHeartbeatById.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) RecordWorkerHeartbeat(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

RecordWorkerHeartbeat indicates an expected call of RecordWorkerHeartbeat.

RegisterNamespace indicates an expected call of RegisterNamespace.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) RequestCancelActivityExecution(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

RequestCancelActivityExecution indicates an expected call of RequestCancelActivityExecution.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) RequestCancelWorkflowExecution(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

RequestCancelWorkflowExecution indicates an expected call of RequestCancelWorkflowExecution.

ResetActivity indicates an expected call of ResetActivity.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) ResetStickyTaskQueue(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

ResetStickyTaskQueue indicates an expected call of ResetStickyTaskQueue.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) ResetWorkflowExecution(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

ResetWorkflowExecution indicates an expected call of ResetWorkflowExecution.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) RespondActivityTaskCanceled(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

RespondActivityTaskCanceled indicates an expected call of RespondActivityTaskCanceled.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) RespondActivityTaskCanceledById(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

RespondActivityTaskCanceledById indicates an expected call of RespondActivityTaskCanceledById.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) RespondActivityTaskCompleted(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

RespondActivityTaskCompleted indicates an expected call of RespondActivityTaskCompleted.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) RespondActivityTaskCompletedById(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

RespondActivityTaskCompletedById indicates an expected call of RespondActivityTaskCompletedById.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) RespondActivityTaskFailed(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

RespondActivityTaskFailed indicates an expected call of RespondActivityTaskFailed.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) RespondActivityTaskFailedById(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

RespondActivityTaskFailedById indicates an expected call of RespondActivityTaskFailedById.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) RespondNexusTaskCompleted(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

RespondNexusTaskCompleted indicates an expected call of RespondNexusTaskCompleted.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) RespondNexusTaskFailed(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

RespondNexusTaskFailed indicates an expected call of RespondNexusTaskFailed.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) RespondQueryTaskCompleted(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

RespondQueryTaskCompleted indicates an expected call of RespondQueryTaskCompleted.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) RespondWorkflowTaskCompleted(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

RespondWorkflowTaskCompleted indicates an expected call of RespondWorkflowTaskCompleted.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) RespondWorkflowTaskFailed(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

RespondWorkflowTaskFailed indicates an expected call of RespondWorkflowTaskFailed.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) ScanWorkflowExecutions(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

ScanWorkflowExecutions indicates an expected call of ScanWorkflowExecutions.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) SetCurrentDeployment(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

SetCurrentDeployment indicates an expected call of SetCurrentDeployment.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) SetWorkerDeploymentCurrentVersion(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

SetWorkerDeploymentCurrentVersion indicates an expected call of SetWorkerDeploymentCurrentVersion.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) SetWorkerDeploymentManager(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

SetWorkerDeploymentManager indicates an expected call of SetWorkerDeploymentManager.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) SetWorkerDeploymentRampingVersion(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

SetWorkerDeploymentRampingVersion indicates an expected call of SetWorkerDeploymentRampingVersion.

ShutdownWorker indicates an expected call of ShutdownWorker.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) SignalWithStartWorkflowExecution(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

SignalWithStartWorkflowExecution indicates an expected call of SignalWithStartWorkflowExecution.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) SignalWorkflowExecution(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

SignalWorkflowExecution indicates an expected call of SignalWorkflowExecution.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) StartActivityExecution(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

StartActivityExecution indicates an expected call of StartActivityExecution.

StartBatchOperation indicates an expected call of StartBatchOperation.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) StartWorkflowExecution(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

StartWorkflowExecution indicates an expected call of StartWorkflowExecution.

StopBatchOperation indicates an expected call of StopBatchOperation.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) TerminateActivityExecution(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

TerminateActivityExecution indicates an expected call of TerminateActivityExecution.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) TerminateWorkflowExecution(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

TerminateWorkflowExecution indicates an expected call of TerminateWorkflowExecution.

TriggerWorkflowRule indicates an expected call of TriggerWorkflowRule.

UnpauseActivity indicates an expected call of UnpauseActivity.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) UnpauseWorkflowExecution(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

UnpauseWorkflowExecution indicates an expected call of UnpauseWorkflowExecution.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) UpdateActivityOptions(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

UpdateActivityOptions indicates an expected call of UpdateActivityOptions.

UpdateNamespace indicates an expected call of UpdateNamespace.

UpdateSchedule indicates an expected call of UpdateSchedule.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) UpdateTaskQueueConfig(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

UpdateTaskQueueConfig indicates an expected call of UpdateTaskQueueConfig.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) UpdateWorkerBuildIdCompatibility(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

UpdateWorkerBuildIdCompatibility indicates an expected call of UpdateWorkerBuildIdCompatibility.

UpdateWorkerConfig indicates an expected call of UpdateWorkerConfig.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) UpdateWorkerDeploymentVersionMetadata(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

UpdateWorkerDeploymentVersionMetadata indicates an expected call of UpdateWorkerDeploymentVersionMetadata.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) UpdateWorkerVersioningRules(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

UpdateWorkerVersioningRules indicates an expected call of UpdateWorkerVersioningRules.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) UpdateWorkflowExecution(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

UpdateWorkflowExecution indicates an expected call of UpdateWorkflowExecution.

func (mr *[MockWorkflowServiceServerMockRecorder](https://pkg.go.dev/go.temporal.io/api@v1.62.2/workflowservicemock/v1#MockWorkflowServiceServerMockRecorder)) UpdateWorkflowExecutionOptions(arg0, arg1 interface{}) *[gomock](https://pkg.go.dev/github.com/golang/mock/gomock).[Call](https://pkg.go.dev/github.com/golang/mock/gomock#Call)

UpdateWorkflowExecutionOptions indicates an expected call of UpdateWorkflowExecutionOptions.
