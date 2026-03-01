# Source: https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm

Title: chasm package - go.temporal.io/server/chasm - Go Packages

URL Source: https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm

Markdown Content:
Package chasm is a generated GoMock package.

Package chasm is a generated GoMock package.

Package chasm is a generated GoMock package.

Package chasm is a generated GoMock package.

Package chasm is a generated GoMock package.

*   [Constants](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#pkg-constants)
*   [Variables](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#pkg-variables)
*   [func ExecutionStateChanged(c Component, ctx Context, refBytes []byte) (bool, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ExecutionStateChanged)
*   [func GenerateNexusCallback(ctx Context, component NexusCompletionHandlerComponent) (*commonpb.Callback, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#GenerateNexusCallback)
*   [func GetValue[T any](m SearchAttributesMap, sa typedSearchAttribute[T]) (val T, ok bool)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#GetValue)
*   [func NewEngineContext(ctx context.Context, engine Engine) context.Context](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewEngineContext)
*   [func NewVisibilityManagerContext(ctx context.Context, engine VisibilityManager) context.Context](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewVisibilityManagerContext)
*   [func PollComponent[C any, R []byte | ComponentRef, I any, O any](ctx context.Context, r R, ...) (O, []byte, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#PollComponent)
*   [func ReadComponent[C any, R []byte | ComponentRef, I any, O any](ctx context.Context, r R, readFn func(C, Context, I) (O, error), input I, ...) (O, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ReadComponent)
*   [func UpdateComponent[C any, R []byte | ComponentRef, I any, O any](ctx context.Context, r R, updateFn func(C, MutableContext, I) (O, error), ...) (O, []byte, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#UpdateComponent)
*   [type Archetype](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Archetype)
*   [type ArchetypeID](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ArchetypeID)
*   [type BusinessIDConflictPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#BusinessIDConflictPolicy)
*   [type BusinessIDReusePolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#BusinessIDReusePolicy)
*   [type ChasmEngineInterceptor](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ChasmEngineInterceptor)
*       *   [func ChasmEngineInterceptorProvider(engine Engine, logger log.Logger, metricsHandler metrics.Handler) *ChasmEngineInterceptor](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ChasmEngineInterceptorProvider)

*       *   [func (i *ChasmEngineInterceptor) Intercept(ctx context.Context, req interface{}, info *grpc.UnaryServerInfo, ...) (resp interface{}, retError error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ChasmEngineInterceptor.Intercept)

*   [type ChasmVisibilityInterceptor](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ChasmVisibilityInterceptor)
*       *   [func ChasmVisibilityInterceptorProvider(visibilityMgr VisibilityManager) *ChasmVisibilityInterceptor](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ChasmVisibilityInterceptorProvider)

*       *   [func (i *ChasmVisibilityInterceptor) Intercept(ctx context.Context, req interface{}, info *grpc.UnaryServerInfo, ...) (resp interface{}, retError error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ChasmVisibilityInterceptor.Intercept)

*   [type Component](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Component)
*   [type ComponentFieldOption](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ComponentFieldOption)
*       *   [func ComponentFieldDetached() ComponentFieldOption](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ComponentFieldDetached)

*   [type ComponentRef](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ComponentRef)
*       *   [func DeserializeComponentRef(data []byte) (ComponentRef, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#DeserializeComponentRef)
    *   [func NewComponentRef[C Component](executionKey ExecutionKey) ComponentRef](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewComponentRef)
    *   [func ProtoRefToComponentRef(pRef *persistencespb.ChasmComponentRef) ComponentRef](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ProtoRefToComponentRef)

*       *   [func (r *ComponentRef) ArchetypeID(registry *Registry) (ArchetypeID, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ComponentRef.ArchetypeID)
    *   [func (r *ComponentRef) Serialize(registry *Registry) ([]byte, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ComponentRef.Serialize)
    *   [func (r *ComponentRef) ShardingKey(registry *Registry) (string, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ComponentRef.ShardingKey)

*   [type Context](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Context)
*       *   [func NewContext(ctx context.Context, node *Node) Context](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewContext)

*   [type CoreLibrary](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#CoreLibrary)
*       *   [func (b *CoreLibrary) Components() []*RegistrableComponent](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#CoreLibrary.Components)
    *   [func (b *CoreLibrary) Name() string](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#CoreLibrary.Name)
    *   [func (b *CoreLibrary) Tasks() []*RegistrableTask](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#CoreLibrary.Tasks)

*   [type CountExecutionsRequest](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#CountExecutionsRequest)
*   [type CountExecutionsResponse](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#CountExecutionsResponse)
*       *   [func CountExecutions[C Component](ctx context.Context, request *CountExecutionsRequest) (*CountExecutionsResponse, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#CountExecutions)

*   [type Engine](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Engine)
*   [type EngineNewExecutionResult](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#EngineNewExecutionResult)
*   [type ExecutionAlreadyStartedError](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ExecutionAlreadyStartedError)
*       *   [func NewExecutionAlreadyStartedErr(message, currentRequestID, currentRunID string) *ExecutionAlreadyStartedError](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewExecutionAlreadyStartedErr)

*       *   [func (e *ExecutionAlreadyStartedError) Error() string](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ExecutionAlreadyStartedError.Error)

*   [type ExecutionInfo](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ExecutionInfo)
*   [type ExecutionKey](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ExecutionKey)
*       *   [func UpdateWithNewExecution[C Component, I any, O1 any, O2 any](ctx context.Context, key ExecutionKey, ...) (O1, O2, ExecutionKey, []byte, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#UpdateWithNewExecution)

*   [type Field](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Field)
*       *   [func ComponentPointerTo[C Component](ctx MutableContext, c C) Field[C]](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ComponentPointerTo)
    *   [func DataPointerTo[D proto.Message](ctx MutableContext, d D) Field[D]](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#DataPointerTo)
    *   [func NewComponentField[C Component](ctx MutableContext, c C, options ...ComponentFieldOption) Field[C]](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewComponentField)
    *   [func NewDataField[D proto.Message](ctx MutableContext, d D) Field[D]](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewDataField)
    *   [func NewEmptyField[T any]() Field[T]](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewEmptyField)

*       *   [func (f Field[T]) Get(chasmContext Context) T](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Field.Get)
    *   [func (f Field[T]) TryGet(chasmContext Context) (T, bool)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Field.TryGet)

*   [type Group](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Group)
*   [type Library](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Library)
*   [type LifecycleState](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#LifecycleState)
*       *   [func (s LifecycleState) IsClosed() bool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#LifecycleState.IsClosed)
    *   [func (s LifecycleState) String() string](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#LifecycleState.String)

*   [type ListExecutionsRequest](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ListExecutionsRequest)
*   [type ListExecutionsResponse](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ListExecutionsResponse)
*       *   [func ListExecutions[C Component, M proto.Message](ctx context.Context, request *ListExecutionsRequest) (*ListExecutionsResponse[M], error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ListExecutions)

*   [type MSPointer](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MSPointer)
*       *   [func NewMSPointer(backend NodeBackend) MSPointer](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewMSPointer)

*       *   [func (m MSPointer) GetNexusCompletion(ctx Context, requestID string) (nexusrpc.OperationCompletion, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MSPointer.GetNexusCompletion)

*   [type Map](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Map)
*   [type MockComponent](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockComponent)
*       *   [func NewMockComponent(ctrl *gomock.Controller) *MockComponent](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewMockComponent)

*       *   [func (m *MockComponent) EXPECT() *MockComponentMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockComponent.EXPECT)
    *   [func (m *MockComponent) LifecycleState(arg0 Context) LifecycleState](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockComponent.LifecycleState)
    *   [func (m *MockComponent) Terminate(arg0 MutableContext, arg1 TerminateComponentRequest) (TerminateComponentResponse, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockComponent.Terminate)

*   [type MockComponentMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockComponentMockRecorder)
*       *   [func (mr *MockComponentMockRecorder) LifecycleState(arg0 any) *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockComponentMockRecorder.LifecycleState)
    *   [func (mr *MockComponentMockRecorder) Terminate(arg0, arg1 any) *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockComponentMockRecorder.Terminate)

*   [type MockContext](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockContext)
*       *   [func (c *MockContext) ExecutionCloseTime() time.Time](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockContext.ExecutionCloseTime)
    *   [func (c *MockContext) ExecutionKey() ExecutionKey](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockContext.ExecutionKey)
    *   [func (c *MockContext) Now(cmp Component) time.Time](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockContext.Now)
    *   [func (c *MockContext) Ref(cmp Component) ([]byte, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockContext.Ref)

*   [type MockEngine](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockEngine)
*       *   [func NewMockEngine(ctrl *gomock.Controller) *MockEngine](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewMockEngine)

*       *   [func (m *MockEngine) EXPECT() *MockEngineMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockEngine.EXPECT)
    *   [func (m *MockEngine) NewExecution(arg0 context.Context, arg1 ComponentRef, ...) (EngineNewExecutionResult, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockEngine.NewExecution)
    *   [func (m *MockEngine) NotifyExecution(arg0 ExecutionKey)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockEngine.NotifyExecution)
    *   [func (m *MockEngine) PollComponent(arg0 context.Context, arg1 ComponentRef, ...) ([]byte, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockEngine.PollComponent)
    *   [func (m *MockEngine) ReadComponent(arg0 context.Context, arg1 ComponentRef, arg2 func(Context, Component) error, ...) error](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockEngine.ReadComponent)
    *   [func (m *MockEngine) UpdateComponent(arg0 context.Context, arg1 ComponentRef, ...) ([]byte, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockEngine.UpdateComponent)
    *   [func (m *MockEngine) UpdateWithNewExecution(arg0 context.Context, arg1 ComponentRef, ...) (ExecutionKey, []byte, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockEngine.UpdateWithNewExecution)

*   [type MockEngineMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockEngineMockRecorder)
*       *   [func (mr *MockEngineMockRecorder) NewExecution(arg0, arg1, arg2 any, arg3 ...any) *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockEngineMockRecorder.NewExecution)
    *   [func (mr *MockEngineMockRecorder) NotifyExecution(arg0 any) *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockEngineMockRecorder.NotifyExecution)
    *   [func (mr *MockEngineMockRecorder) PollComponent(arg0, arg1, arg2 any, arg3 ...any) *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockEngineMockRecorder.PollComponent)
    *   [func (mr *MockEngineMockRecorder) ReadComponent(arg0, arg1, arg2 any, arg3 ...any) *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockEngineMockRecorder.ReadComponent)
    *   [func (mr *MockEngineMockRecorder) UpdateComponent(arg0, arg1, arg2 any, arg3 ...any) *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockEngineMockRecorder.UpdateComponent)
    *   [func (mr *MockEngineMockRecorder) UpdateWithNewExecution(arg0, arg1, arg2, arg3 any, arg4 ...any) *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockEngineMockRecorder.UpdateWithNewExecution)

*   [type MockLibrary](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockLibrary)
*       *   [func NewMockLibrary(ctrl *gomock.Controller) *MockLibrary](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewMockLibrary)

*       *   [func (m *MockLibrary) Components() []*RegistrableComponent](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockLibrary.Components)
    *   [func (m *MockLibrary) EXPECT() *MockLibraryMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockLibrary.EXPECT)
    *   [func (m *MockLibrary) Name() string](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockLibrary.Name)
    *   [func (m *MockLibrary) RegisterServices(server *grpc.Server)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockLibrary.RegisterServices)
    *   [func (m *MockLibrary) Tasks() []*RegistrableTask](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockLibrary.Tasks)

*   [type MockLibraryMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockLibraryMockRecorder)
*       *   [func (mr *MockLibraryMockRecorder) Components() *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockLibraryMockRecorder.Components)
    *   [func (mr *MockLibraryMockRecorder) Name() *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockLibraryMockRecorder.Name)
    *   [func (mr *MockLibraryMockRecorder) RegisterServices(server any) *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockLibraryMockRecorder.RegisterServices)
    *   [func (mr *MockLibraryMockRecorder) Tasks() *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockLibraryMockRecorder.Tasks)

*   [type MockMutableContext](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockMutableContext)
*       *   [func (c *MockMutableContext) AddTask(component Component, attributes TaskAttributes, payload any)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockMutableContext.AddTask)

*   [type MockNodeBackend](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockNodeBackend)
*       *   [func (m *MockNodeBackend) AddTasks(ts ...tasks.Task)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockNodeBackend.AddTasks)
    *   [func (m *MockNodeBackend) CurrentVersionedTransition() *persistencespb.VersionedTransition](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockNodeBackend.CurrentVersionedTransition)
    *   [func (m *MockNodeBackend) DeleteCHASMPureTasks(maxScheduledTime time.Time)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockNodeBackend.DeleteCHASMPureTasks)
    *   [func (m *MockNodeBackend) GetCurrentVersion() int64](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockNodeBackend.GetCurrentVersion)
    *   [func (m *MockNodeBackend) GetExecutionInfo() *persistencespb.WorkflowExecutionInfo](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockNodeBackend.GetExecutionInfo)
    *   [func (m *MockNodeBackend) GetExecutionState() *persistencespb.WorkflowExecutionState](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockNodeBackend.GetExecutionState)
    *   [func (m *MockNodeBackend) GetNexusCompletion(ctx context.Context, requestID string) (nexusrpc.OperationCompletion, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockNodeBackend.GetNexusCompletion)
    *   [func (m *MockNodeBackend) GetWorkflowKey() definition.WorkflowKey](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockNodeBackend.GetWorkflowKey)
    *   [func (m *MockNodeBackend) IsWorkflow() bool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockNodeBackend.IsWorkflow)
    *   [func (m *MockNodeBackend) LastDeletePureTaskCall() time.Time](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockNodeBackend.LastDeletePureTaskCall)
    *   [func (m *MockNodeBackend) LastUpdateWorkflowState() enumsspb.WorkflowExecutionState](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockNodeBackend.LastUpdateWorkflowState)
    *   [func (m *MockNodeBackend) LastUpdateWorkflowStatus() enumspb.WorkflowExecutionStatus](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockNodeBackend.LastUpdateWorkflowStatus)
    *   [func (m *MockNodeBackend) NextTransitionCount() int64](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockNodeBackend.NextTransitionCount)
    *   [func (m *MockNodeBackend) NumTasksAdded() int](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockNodeBackend.NumTasksAdded)
    *   [func (m *MockNodeBackend) UpdateWorkflowStateStatus(state enumsspb.WorkflowExecutionState, status enumspb.WorkflowExecutionStatus) (bool, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockNodeBackend.UpdateWorkflowStateStatus)

*   [type MockNodePureTask](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockNodePureTask)
*       *   [func (m *MockNodePureTask) ExecutePureTask(baseCtx context.Context, taskAttributes TaskAttributes, taskInstance any) (bool, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockNodePureTask.ExecutePureTask)
    *   [func (m *MockNodePureTask) ValidatePureTask(baseCtx context.Context, taskAttributes TaskAttributes, taskInstance any) (bool, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockNodePureTask.ValidatePureTask)

*   [type MockPureTaskExecutor](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockPureTaskExecutor)
*       *   [func NewMockPureTaskExecutor[C any, T any](ctrl *gomock.Controller) *MockPureTaskExecutor[C, T]](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewMockPureTaskExecutor)

*       *   [func (m *MockPureTaskExecutor[C, T]) EXPECT() *MockPureTaskExecutorMockRecorder[C, T]](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockPureTaskExecutor.EXPECT)
    *   [func (m *MockPureTaskExecutor[C, T]) Execute(arg0 MutableContext, arg1 C, arg2 TaskAttributes, arg3 T) error](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockPureTaskExecutor.Execute)

*   [type MockPureTaskExecutorMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockPureTaskExecutorMockRecorder)
*       *   [func (mr *MockPureTaskExecutorMockRecorder[C, T]) Execute(arg0, arg1, arg2, arg3 any) *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockPureTaskExecutorMockRecorder.Execute)

*   [type MockSideEffectTaskExecutor](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockSideEffectTaskExecutor)
*       *   [func NewMockSideEffectTaskExecutor[C any, T any](ctrl *gomock.Controller) *MockSideEffectTaskExecutor[C, T]](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewMockSideEffectTaskExecutor)

*       *   [func (m *MockSideEffectTaskExecutor[C, T]) EXPECT() *MockSideEffectTaskExecutorMockRecorder[C, T]](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockSideEffectTaskExecutor.EXPECT)
    *   [func (m *MockSideEffectTaskExecutor[C, T]) Execute(arg0 context.Context, arg1 ComponentRef, arg2 TaskAttributes, arg3 T) error](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockSideEffectTaskExecutor.Execute)

*   [type MockSideEffectTaskExecutorMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockSideEffectTaskExecutorMockRecorder)
*       *   [func (mr *MockSideEffectTaskExecutorMockRecorder[C, T]) Execute(arg0, arg1, arg2, arg3 any) *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockSideEffectTaskExecutorMockRecorder.Execute)

*   [type MockTask](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockTask)
*   [type MockTaskValidator](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockTaskValidator)
*       *   [func NewMockTaskValidator[C any, T any](ctrl *gomock.Controller) *MockTaskValidator[C, T]](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewMockTaskValidator)

*       *   [func (m *MockTaskValidator[C, T]) EXPECT() *MockTaskValidatorMockRecorder[C, T]](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockTaskValidator.EXPECT)
    *   [func (m *MockTaskValidator[C, T]) Validate(arg0 Context, arg1 C, arg2 TaskAttributes, arg3 T) (bool, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockTaskValidator.Validate)

*   [type MockTaskValidatorMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockTaskValidatorMockRecorder)
*       *   [func (mr *MockTaskValidatorMockRecorder[C, T]) Validate(arg0, arg1, arg2, arg3 any) *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockTaskValidatorMockRecorder.Validate)

*   [type MockVisibilityManager](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockVisibilityManager)
*       *   [func NewMockVisibilityManager(ctrl *gomock.Controller) *MockVisibilityManager](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewMockVisibilityManager)

*       *   [func (m *MockVisibilityManager) CountExecutions(arg0 context.Context, arg1 reflect.Type, arg2 *CountExecutionsRequest) (*CountExecutionsResponse, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockVisibilityManager.CountExecutions)
    *   [func (m *MockVisibilityManager) EXPECT() *MockVisibilityManagerMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockVisibilityManager.EXPECT)
    *   [func (m *MockVisibilityManager) ListExecutions(arg0 context.Context, arg1 reflect.Type, arg2 *ListExecutionsRequest) (*ListExecutionsResponse[*common.Payload], error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockVisibilityManager.ListExecutions)

*   [type MockVisibilityManagerMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockVisibilityManagerMockRecorder)
*       *   [func (mr *MockVisibilityManagerMockRecorder) CountExecutions(arg0, arg1, arg2 any) *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockVisibilityManagerMockRecorder.CountExecutions)
    *   [func (mr *MockVisibilityManagerMockRecorder) ListExecutions(arg0, arg1, arg2 any) *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockVisibilityManagerMockRecorder.ListExecutions)

*   [type Mocknamer](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Mocknamer)
*       *   [func NewMocknamer(ctrl *gomock.Controller) *Mocknamer](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewMocknamer)

*       *   [func (m *Mocknamer) EXPECT() *MocknamerMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Mocknamer.EXPECT)
    *   [func (m *Mocknamer) Name() string](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Mocknamer.Name)

*   [type MocknamerMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MocknamerMockRecorder)
*       *   [func (mr *MocknamerMockRecorder) Name() *gomock.Call](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MocknamerMockRecorder.Name)

*   [type MutableContext](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MutableContext)
*       *   [func NewMutableContext(ctx context.Context, root *Node) MutableContext](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewMutableContext)

*   [type NewExecutionResult](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewExecutionResult)
*       *   [func NewExecution[C Component, I any, O any](ctx context.Context, key ExecutionKey, ...) (NewExecutionResult[O], error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewExecution)

*   [type NexusCompletionHandler](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NexusCompletionHandler)
*   [type NexusCompletionHandlerComponent](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NexusCompletionHandlerComponent)
*   [type NoValue](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NoValue)
*   [type Node](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Node)
*       *   [func NewEmptyTree(registry *Registry, timeSource clock.TimeSource, backend NodeBackend, ...) *Node](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewEmptyTree)
    *   [func NewTreeFromDB(serializedNodes map[string]*persistencespb.ChasmNode, registry *Registry, ...) (*Node, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewTreeFromDB)

*       *   [func (n *Node) AddTask(component Component, taskAttributes TaskAttributes, task any)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Node.AddTask)
    *   [func (n *Node) ApplyMutation(mutation NodesMutation) error](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Node.ApplyMutation)
    *   [func (n *Node) ApplySnapshot(incomingSnapshot NodesSnapshot) error](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Node.ApplySnapshot)
    *   [func (n *Node) Archetype() (Archetype, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Node.Archetype)
    *   [func (n *Node) ArchetypeID() ArchetypeID](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Node.ArchetypeID)
    *   [func (n *Node) CloseTransaction() (NodesMutation, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Node.CloseTransaction)
    *   [func (n *Node) Component(chasmContext Context, ref ComponentRef) (Component, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Node.Component)
    *   [func (n *Node) ComponentByPath(chasmContext Context, path []string) (Component, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Node.ComponentByPath)
    *   [func (n *Node) EachPureTask(referenceTime time.Time, ...) error](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Node.EachPureTask)
    *   [func (n *Node) ExecutePureTask(baseCtx context.Context, taskAttributes TaskAttributes, taskInstance any) (bool, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Node.ExecutePureTask)
    *   [func (n *Node) ExecuteSideEffectTask(ctx context.Context, registry *Registry, executionKey ExecutionKey, ...) (retErr error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Node.ExecuteSideEffectTask)
    *   [func (n *Node) IsDirty() bool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Node.IsDirty)
    *   [func (n *Node) IsStale(ref ComponentRef) error](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Node.IsStale)
    *   [func (n *Node) IsStateDirty() bool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Node.IsStateDirty)
    *   [func (n *Node) Now(_ Component) time.Time](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Node.Now)
    *   [func (n *Node) Ref(component Component) ([]byte, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Node.Ref)
    *   [func (n *Node) RefreshTasks() error](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Node.RefreshTasks)
    *   [func (n *Node) SetRootComponent(rootComponent Component)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Node.SetRootComponent)
    *   [func (n *Node) Snapshot(exclusiveMinVT *persistencespb.VersionedTransition) NodesSnapshot](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Node.Snapshot)
    *   [func (n *Node) Terminate(request TerminateComponentRequest) error](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Node.Terminate)
    *   [func (n *Node) ValidatePureTask(ctx context.Context, taskAttributes TaskAttributes, taskInstance any) (bool, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Node.ValidatePureTask)
    *   [func (n *Node) ValidateSideEffectTask(ctx context.Context, chasmTask *tasks.ChasmTask) (isValid bool, retErr error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Node.ValidateSideEffectTask)

*   [type NodeBackend](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NodeBackend)
*   [type NodePathEncoder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NodePathEncoder)
*   [type NodePureTask](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NodePureTask)
*   [type NodesMutation](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NodesMutation)
*   [type NodesSnapshot](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NodesSnapshot)
*   [type OperationIntent](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#OperationIntent)
*   [type ParentPtr](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ParentPtr)
*       *   [func (p ParentPtr[T]) Get(chasmContext Context) T](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ParentPtr.Get)
    *   [func (p ParentPtr[T]) TryGet(chasmContext Context) (T, bool)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ParentPtr.TryGet)

*   [type PureTaskExecutor](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#PureTaskExecutor)
*   [type RegistrableComponent](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#RegistrableComponent)
*       *   [func NewRegistrableComponent[C Component](componentType string, opts ...RegistrableComponentOption) *RegistrableComponent](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewRegistrableComponent)

*       *   [func (rc *RegistrableComponent) SearchAttributesMapper() *VisibilitySearchAttributesMapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#RegistrableComponent.SearchAttributesMapper)

*   [type RegistrableComponentOption](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#RegistrableComponentOption)
*       *   [func WithBusinessIDAlias(alias string) RegistrableComponentOption](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#WithBusinessIDAlias)
    *   [func WithEphemeral() RegistrableComponentOption](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#WithEphemeral)
    *   [func WithSearchAttributes(searchAttributes ...SearchAttribute) RegistrableComponentOption](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#WithSearchAttributes)
    *   [func WithShardingFn(shardingFn func(ExecutionKey) string) RegistrableComponentOption](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#WithShardingFn)
    *   [func WithSingleCluster() RegistrableComponentOption](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#WithSingleCluster)

*   [type RegistrableTask](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#RegistrableTask)
*       *   [func NewRegistrablePureTask[C any, T any](taskType string, validator TaskValidator[C, T], ...) *RegistrableTask](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewRegistrablePureTask)
    *   [func NewRegistrableSideEffectTask[C any, T any](taskType string, validator TaskValidator[C, T], ...) *RegistrableTask](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewRegistrableSideEffectTask)

*   [type RegistrableTaskOption](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#RegistrableTaskOption)
*   [type Registry](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Registry)
*       *   [func NewRegistry(logger log.Logger) *Registry](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewRegistry)

*       *   [func (r *Registry) ArchetypeIDOf(componentGoType reflect.Type) (ArchetypeID, bool)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Registry.ArchetypeIDOf)
    *   [func (r *Registry) ComponentByID(id uint32) (*RegistrableComponent, bool)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Registry.ComponentByID)
    *   [func (r *Registry) ComponentFqnByID(id uint32) (string, bool)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Registry.ComponentFqnByID)
    *   [func (r *Registry) ComponentIDByFqn(fqn string) (uint32, bool)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Registry.ComponentIDByFqn)
    *   [func (r *Registry) ComponentIDFor(componentInstance any) (uint32, bool)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Registry.ComponentIDFor)
    *   [func (r *Registry) Register(lib Library) error](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Registry.Register)
    *   [func (r *Registry) RegisterServices(server *grpc.Server)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Registry.RegisterServices)
    *   [func (r *Registry) TaskFqnByID(id uint32) (string, bool)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Registry.TaskFqnByID)
    *   [func (r *Registry) TaskIDFor(taskInstance any) (uint32, bool)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Registry.TaskIDFor)

*   [type SearchAttribute](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SearchAttribute)
*   [type SearchAttributeBool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SearchAttributeBool)
*       *   [func NewSearchAttributeBool(alias string, boolField SearchAttributeFieldBool) SearchAttributeBool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewSearchAttributeBool)

*       *   [func (s SearchAttributeBool) Value(value bool) SearchAttributeKeyValue](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SearchAttributeBool.Value)

*   [type SearchAttributeDateTime](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SearchAttributeDateTime)
*       *   [func NewSearchAttributeDateTime(alias string, datetimeField SearchAttributeFieldDateTime) SearchAttributeDateTime](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewSearchAttributeDateTime)

*       *   [func (s SearchAttributeDateTime) Value(value time.Time) SearchAttributeKeyValue](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SearchAttributeDateTime.Value)

*   [type SearchAttributeDouble](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SearchAttributeDouble)
*       *   [func NewSearchAttributeDouble(alias string, doubleField SearchAttributeFieldDouble) SearchAttributeDouble](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewSearchAttributeDouble)

*       *   [func (s SearchAttributeDouble) Value(value float64) SearchAttributeKeyValue](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SearchAttributeDouble.Value)

*   [type SearchAttributeFieldBool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SearchAttributeFieldBool)
*   [type SearchAttributeFieldDateTime](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SearchAttributeFieldDateTime)
*   [type SearchAttributeFieldDouble](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SearchAttributeFieldDouble)
*   [type SearchAttributeFieldInt](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SearchAttributeFieldInt)
*   [type SearchAttributeFieldKeyword](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SearchAttributeFieldKeyword)
*   [type SearchAttributeFieldKeywordList](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SearchAttributeFieldKeywordList)
*   [type SearchAttributeInt](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SearchAttributeInt)
*       *   [func NewSearchAttributeInt(alias string, intField SearchAttributeFieldInt) SearchAttributeInt](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewSearchAttributeInt)

*       *   [func (s SearchAttributeInt) Value(value int64) SearchAttributeKeyValue](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SearchAttributeInt.Value)

*   [type SearchAttributeKeyValue](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SearchAttributeKeyValue)
*   [type SearchAttributeKeyword](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SearchAttributeKeyword)
*       *   [func NewSearchAttributeKeyword(alias string, keywordField SearchAttributeFieldKeyword) SearchAttributeKeyword](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewSearchAttributeKeyword)

*       *   [func (s SearchAttributeKeyword) Value(value string) SearchAttributeKeyValue](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SearchAttributeKeyword.Value)

*   [type SearchAttributeKeywordList](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SearchAttributeKeywordList)
*       *   [func NewSearchAttributeKeywordList(alias string, keywordListField SearchAttributeFieldKeywordList) SearchAttributeKeywordList](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewSearchAttributeKeywordList)

*       *   [func (s SearchAttributeKeywordList) Value(value []string) SearchAttributeKeyValue](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SearchAttributeKeywordList.Value)

*   [type SearchAttributesMap](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SearchAttributesMap)
*       *   [func NewSearchAttributesMap(values map[string]VisibilityValue) SearchAttributesMap](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewSearchAttributesMap)

*   [type SideEffectTaskExecutor](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SideEffectTaskExecutor)
*   [type StateMachine](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#StateMachine)
*   [type TaskAttributes](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#TaskAttributes)
*       *   [func (a *TaskAttributes) IsImmediate() bool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#TaskAttributes.IsImmediate)
    *   [func (a *TaskAttributes) IsValid() bool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#TaskAttributes.IsValid)

*   [type TaskValidator](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#TaskValidator)
*   [type TerminateComponentRequest](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#TerminateComponentRequest)
*   [type TerminateComponentResponse](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#TerminateComponentResponse)
*   [type Transition](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Transition)
*       *   [func NewTransition[S comparable, SM StateMachine[S], E any](src []S, dst S, apply func(SM, MutableContext, E) error) Transition[S, SM, E]](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewTransition)

*       *   [func (t Transition[S, SM, E]) Apply(sm SM, ctx MutableContext, event E) error](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Transition.Apply)
    *   [func (t Transition[S, SM, E]) Possible(sm SM) bool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Transition.Possible)

*   [type TransitionOption](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#TransitionOption)
*       *   [func WithBusinessIDPolicy(reusePolicy BusinessIDReusePolicy, conflictPolicy BusinessIDConflictPolicy) TransitionOption](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#WithBusinessIDPolicy)
    *   [func WithRequestID(requestID string) TransitionOption](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#WithRequestID)
    *   [func WithSpeculative() TransitionOption](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#WithSpeculative)

*   [type TransitionOptions](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#TransitionOptions)
*   [type UnimplementedComponent](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#UnimplementedComponent)
*       *   [func (UnimplementedComponent) Terminate(MutableContext, TerminateComponentRequest) (TerminateComponentResponse, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#UnimplementedComponent.Terminate)

*   [type UnimplementedLibrary](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#UnimplementedLibrary)
*       *   [func (UnimplementedLibrary) Components() []*RegistrableComponent](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#UnimplementedLibrary.Components)
    *   [func (UnimplementedLibrary) RegisterServices(_ *grpc.Server)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#UnimplementedLibrary.RegisterServices)
    *   [func (UnimplementedLibrary) Tasks() []*RegistrableTask](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#UnimplementedLibrary.Tasks)

*   [type Visibility](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Visibility)
*       *   [func NewVisibility(mutableContext MutableContext) *Visibility](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewVisibility)
    *   [func NewVisibilityWithData(mutableContext MutableContext, ...) *Visibility](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewVisibilityWithData)

*       *   [func (v *Visibility) CustomMemo(chasmContext Context) map[string]*commonpb.Payload](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Visibility.CustomMemo)
    *   [func (v *Visibility) CustomSearchAttributes(chasmContext Context) map[string]*commonpb.Payload](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Visibility.CustomSearchAttributes)
    *   [func (v *Visibility) LifecycleState(_ Context) LifecycleState](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Visibility.LifecycleState)
    *   [func (v *Visibility) MergeCustomMemo(mutableContext MutableContext, customMemo map[string]*commonpb.Payload)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Visibility.MergeCustomMemo)
    *   [func (v *Visibility) MergeCustomSearchAttributes(mutableContext MutableContext, ...)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Visibility.MergeCustomSearchAttributes)
    *   [func (v *Visibility) ReplaceCustomMemo(mutableContext MutableContext, customMemo map[string]*commonpb.Payload)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Visibility.ReplaceCustomMemo)
    *   [func (v *Visibility) ReplaceCustomSearchAttributes(mutableContext MutableContext, ...)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Visibility.ReplaceCustomSearchAttributes)

*   [type VisibilityManager](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilityManager)
*   [type VisibilityMemoProvider](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilityMemoProvider)
*   [type VisibilitySearchAttributesMapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilitySearchAttributesMapper)
*       *   [func NewTestVisibilitySearchAttributesMapper(fieldToAlias map[string]string, saTypeMap map[string]enumspb.IndexedValueType) *VisibilitySearchAttributesMapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewTestVisibilitySearchAttributesMapper)

*       *   [func (v *VisibilitySearchAttributesMapper) Alias(field string) (string, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilitySearchAttributesMapper.Alias)
    *   [func (v *VisibilitySearchAttributesMapper) Field(alias string) (string, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilitySearchAttributesMapper.Field)
    *   [func (v *VisibilitySearchAttributesMapper) SATypeMap() map[string]enumspb.IndexedValueType](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilitySearchAttributesMapper.SATypeMap)
    *   [func (v *VisibilitySearchAttributesMapper) ValueType(fieldName string) (enumspb.IndexedValueType, error)](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilitySearchAttributesMapper.ValueType)

*   [type VisibilitySearchAttributesProvider](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilitySearchAttributesProvider)
*   [type VisibilityValue](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilityValue)
*   [type VisibilityValueBool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilityValueBool)
*       *   [func (v VisibilityValueBool) Equal(other VisibilityValue) bool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilityValueBool.Equal)
    *   [func (v VisibilityValueBool) MustEncode() *commonpb.Payload](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilityValueBool.MustEncode)
    *   [func (v VisibilityValueBool) Value() any](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilityValueBool.Value)

*   [type VisibilityValueByteSlice](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilityValueByteSlice)
*       *   [func (v VisibilityValueByteSlice) Equal(other VisibilityValue) bool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilityValueByteSlice.Equal)
    *   [func (v VisibilityValueByteSlice) MustEncode() *commonpb.Payload](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilityValueByteSlice.MustEncode)
    *   [func (v VisibilityValueByteSlice) Value() any](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilityValueByteSlice.Value)

*   [type VisibilityValueFloat64](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilityValueFloat64)
*       *   [func (v VisibilityValueFloat64) Equal(other VisibilityValue) bool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilityValueFloat64.Equal)
    *   [func (v VisibilityValueFloat64) MustEncode() *commonpb.Payload](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilityValueFloat64.MustEncode)
    *   [func (v VisibilityValueFloat64) Value() any](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilityValueFloat64.Value)

*   [type VisibilityValueInt](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilityValueInt)
*       *   [func (v VisibilityValueInt) Equal(other VisibilityValue) bool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilityValueInt.Equal)
    *   [func (v VisibilityValueInt) MustEncode() *commonpb.Payload](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilityValueInt.MustEncode)
    *   [func (v VisibilityValueInt) Value() any](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilityValueInt.Value)

*   [type VisibilityValueInt32](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilityValueInt32)
*       *   [func (v VisibilityValueInt32) Equal(other VisibilityValue) bool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilityValueInt32.Equal)
    *   [func (v VisibilityValueInt32) MustEncode() *commonpb.Payload](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilityValueInt32.MustEncode)
    *   [func (v VisibilityValueInt32) Value() any](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilityValueInt32.Value)

*   [type VisibilityValueInt64](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilityValueInt64)
*       *   [func (v VisibilityValueInt64) Equal(other VisibilityValue) bool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilityValueInt64.Equal)
    *   [func (v VisibilityValueInt64) MustEncode() *commonpb.Payload](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilityValueInt64.MustEncode)
    *   [func (v VisibilityValueInt64) Value() any](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilityValueInt64.Value)

*   [type VisibilityValueString](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilityValueString)
*       *   [func (v VisibilityValueString) Equal(other VisibilityValue) bool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilityValueString.Equal)
    *   [func (v VisibilityValueString) MustEncode() *commonpb.Payload](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilityValueString.MustEncode)
    *   [func (v VisibilityValueString) Value() any](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilityValueString.Value)

*   [type VisibilityValueStringSlice](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilityValueStringSlice)
*       *   [func (v VisibilityValueStringSlice) Equal(other VisibilityValue) bool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilityValueStringSlice.Equal)
    *   [func (v VisibilityValueStringSlice) MustEncode() *commonpb.Payload](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilityValueStringSlice.MustEncode)
    *   [func (v VisibilityValueStringSlice) Value() any](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilityValueStringSlice.Value)

*   [type VisibilityValueTime](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilityValueTime)
*       *   [func (v VisibilityValueTime) Equal(other VisibilityValue) bool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilityValueTime.Equal)
    *   [func (v VisibilityValueTime) MustEncode() *commonpb.Payload](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilityValueTime.MustEncode)
    *   [func (v VisibilityValueTime) Value() any](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilityValueTime.Value)

[View Source](https://github.com/temporalio/temporal/blob/v1.30.0/chasm/scheduler.go#L6)

const (
 SchedulerLibraryName = "scheduler"  SchedulerComponentName = "scheduler" )

[View Source](https://github.com/temporalio/temporal/blob/v1.30.0/chasm/visibility.go#L17)

const (
 UserMemoKey = "__user__"  ChasmMemoKey = "__chasm__" )

[View Source](https://github.com/temporalio/temporal/blob/v1.30.0/chasm/workflow.go#L3)

const (
 WorkflowLibraryName = "workflow"  WorkflowComponentName = "workflow" )

[View Source](https://github.com/temporalio/temporal/blob/v1.30.0/chasm/nexus_completion.go#L11)

const NexusCompletionHandlerURL = "temporal://internal"

NexusCompletionHandlerURL is the user-visible URL for Nexus->CHASM callbacks.

[View Source](https://github.com/temporalio/temporal/blob/v1.30.0/chasm/scheduler.go#L11)

var (
 SchedulerArchetype = [Archetype](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Archetype)(fullyQualifiedName([SchedulerLibraryName](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SchedulerLibraryName), [SchedulerComponentName](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SchedulerComponentName)))  SchedulerArchetypeID = [ArchetypeID](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ArchetypeID)(generateTypeID([SchedulerArchetype](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SchedulerArchetype))) )

[View Source](https://github.com/temporalio/temporal/blob/v1.30.0/chasm/search_attribute.go#L34)

var (
 SearchAttributeFieldBool01 = newSearchAttributeFieldBool(1)  SearchAttributeFieldBool02 = newSearchAttributeFieldBool(2) 
 SearchAttributeFieldDateTime01 = newSearchAttributeFieldDateTime(1)  SearchAttributeFieldDateTime02 = newSearchAttributeFieldDateTime(2) 
 SearchAttributeFieldInt01 = newSearchAttributeFieldInt(1)  SearchAttributeFieldInt02 = newSearchAttributeFieldInt(2) 
 SearchAttributeFieldDouble01 = newSearchAttributeFieldDouble(1)  SearchAttributeFieldDouble02 = newSearchAttributeFieldDouble(2) 
 SearchAttributeFieldKeyword01 = newSearchAttributeFieldKeyword(1)  SearchAttributeFieldKeyword02 = newSearchAttributeFieldKeyword(2)  SearchAttributeFieldKeyword03 = newSearchAttributeFieldKeyword(3)  SearchAttributeFieldKeyword04 = newSearchAttributeFieldKeyword(4) 
	
	SearchAttributeFieldLowCardinalityKeyword01 = newSearchAttributeFieldLowCardinalityKeyword(1)

 SearchAttributeFieldKeywordList01 = newSearchAttributeFieldKeywordList(1)  SearchAttributeFieldKeywordList02 = newSearchAttributeFieldKeywordList(2) 
 SearchAttributeTemporalChangeVersion = newSearchAttributeKeywordListByField([sadefs](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/searchattribute/sadefs).[TemporalChangeVersion](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/searchattribute/sadefs#TemporalChangeVersion))  SearchAttributeBinaryChecksums = newSearchAttributeKeywordListByField([sadefs](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/searchattribute/sadefs).[BinaryChecksums](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/searchattribute/sadefs#BinaryChecksums))  SearchAttributeBuildIds = newSearchAttributeKeywordListByField([sadefs](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/searchattribute/sadefs).[BuildIds](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/searchattribute/sadefs#BuildIds))  SearchAttributeBatcherNamespace = newSearchAttributeKeywordByField([sadefs](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/searchattribute/sadefs).[BatcherNamespace](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/searchattribute/sadefs#BatcherNamespace))  SearchAttributeBatcherUser = newSearchAttributeKeywordByField([sadefs](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/searchattribute/sadefs).[BatcherUser](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/searchattribute/sadefs#BatcherUser))  SearchAttributeTemporalScheduledStartTime = newSearchAttributeDateTimeByField([sadefs](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/searchattribute/sadefs).[TemporalScheduledStartTime](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/searchattribute/sadefs#TemporalScheduledStartTime))  SearchAttributeTemporalScheduledByID = newSearchAttributeKeywordByField([sadefs](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/searchattribute/sadefs).[TemporalScheduledById](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/searchattribute/sadefs#TemporalScheduledById))  SearchAttributeTemporalSchedulePaused = newSearchAttributeBoolByField([sadefs](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/searchattribute/sadefs).[TemporalSchedulePaused](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/searchattribute/sadefs#TemporalSchedulePaused))  SearchAttributeTemporalNamespaceDivision = newSearchAttributeKeywordByField([sadefs](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/searchattribute/sadefs).[TemporalNamespaceDivision](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/searchattribute/sadefs#TemporalNamespaceDivision))  SearchAttributeTemporalPauseInfo = newSearchAttributeKeywordListByField([sadefs](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/searchattribute/sadefs).[TemporalPauseInfo](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/searchattribute/sadefs#TemporalPauseInfo))  SearchAttributeTemporalReportedProblems = newSearchAttributeKeywordListByField([sadefs](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/searchattribute/sadefs).[TemporalReportedProblems](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/searchattribute/sadefs#TemporalReportedProblems))  SearchAttributeTemporalWorkerDeploymentVersion = newSearchAttributeKeywordByField([sadefs](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/searchattribute/sadefs).[TemporalWorkerDeploymentVersion](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/searchattribute/sadefs#TemporalWorkerDeploymentVersion))  SearchAttributeTemporalWorkflowVersioningBehavior = newSearchAttributeKeywordByField([sadefs](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/searchattribute/sadefs).[TemporalWorkflowVersioningBehavior](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/searchattribute/sadefs#TemporalWorkflowVersioningBehavior))  SearchAttributeTemporalWorkerDeployment = newSearchAttributeKeywordByField([sadefs](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/searchattribute/sadefs).[TemporalWorkerDeployment](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/searchattribute/sadefs#TemporalWorkerDeployment))  SearchAttributeTemporalUsedWorkerDeploymentVersions = newSearchAttributeKeywordListByField([sadefs](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/searchattribute/sadefs).[TemporalUsedWorkerDeploymentVersions](https://pkg.go.dev/go.temporal.io/server@v1.30.0/common/searchattribute/sadefs#TemporalUsedWorkerDeploymentVersions)) )

CHASM Search Attribute User Guide:

This contains CHASM search attribute field constants. These predefined fields correspond to the exact column name in Visibility storage. For each root component, search attributes can be mapped from a user defined alias to these fields. Each component must register its search attributes with the CHASM Registry.

To define a CHASM search attribute, create this as a package/global scoped variable. Below is an example: var testComponentCompletedSearchAttribute = NewSearchAttributeBool("Completed", SearchAttributeFieldBool01) var testComponentFailedSearchAttribute = NewSearchAttributeBool("Failed", SearchAttributeFieldBool02) var testComponentStartTimeSearchAttribute = NewSearchAttributeTime("StartTime", SearchAttributeFieldDateTime01) var testComponentCategorySearchAttribute = NewSearchAttributeLowCardinalityKeyword("Category", SearchAttributeFieldLowCardinalityKeyword01)

Each CHASM search attribute field is associated with a specific indexed value type. The Value() method of a search attribute specifies the supported value type to set at compile time. eg. DateTime values must be set with a time.Time typed value.

Low Cardinality Keyword Fields: used for categorical data that support GROUP BY aggregations. Values must be limited to a small number of dimensions.

Each root component can only use a predefined search attribute field once. Developers should not reassign aliases to different fields. Reassiging aliases to different fields will result in incorrect visibility query results.

To register these search attributes with the CHASM Registry, use the WithSearchAttributes() option when creating the component in the library. eg. NewRegistrableComponent[T]("testcomponent", WithSearchAttributes(testComponentCompletedSearchAttribute, testComponentStartTimeSearchAttribute))

[View Source](https://github.com/temporalio/temporal/blob/v1.30.0/chasm/workflow.go#L8)

var (
 WorkflowArchetype = [Archetype](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Archetype)(fullyQualifiedName([WorkflowLibraryName](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#WorkflowLibraryName), [WorkflowComponentName](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#WorkflowComponentName)))  WorkflowArchetypeID = [ArchetypeID](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ArchetypeID)(generateTypeID([WorkflowArchetype](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#WorkflowArchetype))) )

ErrInvalidComponentRef is returned when component ref bytes deserialize to an invalid component ref.

ErrInvalidTransition is returned from [Transition.Apply](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Transition.Apply) on an invalid state transition.

ErrMalformedComponentRef is returned when component ref bytes cannot be deserialized.

ExecutionStateChanged returns true if execution state has advanced beyond the state encoded in refBytes. It may return ErrInvalidComponentRef or ErrMalformedComponentRef. Callers should consider converting these to serviceerror.NewInvalidArgument.

GenerateNexusCallback generates a Callback message indicating a CHASM component to receive Nexus operation completion callbacks. Particularly useful for components that want to track a workflow start with StartWorkflowExecution.

func GetValue[T [any](https://pkg.go.dev/builtin#any)](m [SearchAttributesMap](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SearchAttributesMap), sa typedSearchAttribute[T]) (val T, ok [bool](https://pkg.go.dev/builtin#bool))

GetValue returns the value for a given SearchAttribute with compile-time type safety. The return type T is inferred from the SearchAttribute's type parameter. For example, SearchAttributeBool will return a bool value. If the value is not found or the type does not match, the zero value for the type T is returned and the second return value is false.

this will be done by the nexus handler? alternatively the engine can be a global variable, but not a good practice in fx.

func PollComponent[C [any](https://pkg.go.dev/builtin#any), R [][byte](https://pkg.go.dev/builtin#byte) | [ComponentRef](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ComponentRef), I [any](https://pkg.go.dev/builtin#any), O [any](https://pkg.go.dev/builtin#any)](
	ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context),
	r R,
	monotonicPredicate func(C, [Context](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Context), I) (O, [bool](https://pkg.go.dev/builtin#bool), [error](https://pkg.go.dev/builtin#error)),
	input I,
	opts ...[TransitionOption](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#TransitionOption),
) (O, [][byte](https://pkg.go.dev/builtin#byte), [error](https://pkg.go.dev/builtin#error))

PollComponent waits until the predicate is true when evaluated against the component identified by the supplied component reference. If this times out due to a server-imposed long-poll timeout then it returns (nil, nil, nil), as an indication that the caller should continue long-polling. Otherwise it returns (output, ref, err), where output is the output of the predicate function, and ref is a component reference identifying the state at which the predicate was satisfied. The predicate must be monotonic: if it returns true at execution state transition s then it must return true at all transitions t > s. If the predicate is true at the outset then PollComponent returns immediately. opts are currently ignored.

func ReadComponent[C [any](https://pkg.go.dev/builtin#any), R [][byte](https://pkg.go.dev/builtin#byte) | [ComponentRef](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ComponentRef), I [any](https://pkg.go.dev/builtin#any), O [any](https://pkg.go.dev/builtin#any)](
	ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context),
	r R,
	readFn func(C, [Context](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Context), I) (O, [error](https://pkg.go.dev/builtin#error)),
	input I,
	opts ...[TransitionOption](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#TransitionOption),
) (O, [error](https://pkg.go.dev/builtin#error))

ReadComponent returns the result of evaluating readFn against the component identified by the component reference. opts are currently ignored.

func UpdateComponent[C [any](https://pkg.go.dev/builtin#any), R [][byte](https://pkg.go.dev/builtin#byte) | [ComponentRef](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ComponentRef), I [any](https://pkg.go.dev/builtin#any), O [any](https://pkg.go.dev/builtin#any)](
	ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context),
	r R,
	updateFn func(C, [MutableContext](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MutableContext), I) (O, [error](https://pkg.go.dev/builtin#error)),
	input I,
	opts ...[TransitionOption](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#TransitionOption),
) (O, [][byte](https://pkg.go.dev/builtin#byte), [error](https://pkg.go.dev/builtin#error))

TODO:

*   consider merge with ReadComponent
*   consider remove ComponentRef from the return value and allow components to get the ref in the transition function. There are some caveats there, check the comment of the NewRef method in MutableContext.

UpdateComponent applies updateFn to the component identified by the supplied component reference. It returns the result, along with the new component reference. opts are currently ignored.

Archetype is the fully qualified name of the root component of a CHASM execution.

ArchetypeID is CHASM framework's internal ID for an Archetype.

const (
	
	
	
	
	
	UnspecifiedArchetypeID [ArchetypeID](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ArchetypeID) = 0
)

type BusinessIDConflictPolicy [int](https://pkg.go.dev/builtin#int)

const (
 BusinessIDConflictPolicyFail [BusinessIDConflictPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#BusinessIDConflictPolicy) = [iota](https://pkg.go.dev/builtin#iota) BusinessIDConflictPolicyTerminateExisting  BusinessIDConflictPolicyUseExisting )

type BusinessIDReusePolicy [int](https://pkg.go.dev/builtin#int)

const (
 BusinessIDReusePolicyAllowDuplicate [BusinessIDReusePolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#BusinessIDReusePolicy) = [iota](https://pkg.go.dev/builtin#iota) BusinessIDReusePolicyAllowDuplicateFailedOnly  BusinessIDReusePolicyRejectDuplicate )

type ChasmEngineInterceptor struct {
	
}

ChasmEngineInterceptor Interceptor that intercepts RPC requests, detects CHASM-specific calls and does additional boilerplate processing before handing off. Visibility is injected separately with ChasmVisibilityInterceptor.

type ChasmVisibilityInterceptor struct {
	
}

ChasmVisibilityInterceptor intercepts RPC requests and adds the CHASM VisibilityManager to their context.

func ChasmVisibilityInterceptorProvider(visibilityMgr [VisibilityManager](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilityManager)) *[ChasmVisibilityInterceptor](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ChasmVisibilityInterceptor)

type Component interface {
 LifecycleState([Context](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Context)) [LifecycleState](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#LifecycleState)
 Terminate([MutableContext](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MutableContext), [TerminateComponentRequest](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#TerminateComponentRequest)) ([TerminateComponentResponse](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#TerminateComponentResponse), [error](https://pkg.go.dev/builtin#error)) 	
}

type ComponentFieldOption func(*componentFieldOptions)

func ComponentFieldDetached() [ComponentFieldOption](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ComponentFieldOption)

type ComponentRef struct {
[ExecutionKey](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ExecutionKey)	
}

func DeserializeComponentRef(data [][byte](https://pkg.go.dev/builtin#byte)) ([ComponentRef](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ComponentRef), [error](https://pkg.go.dev/builtin#error))

DeserializeComponentRef deserializes a byte slice into a ComponentRef. Provides caller the access to information including ExecutionKey, Archetype, and ShardingKey.

func NewComponentRef[C [Component](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Component)](
	executionKey [ExecutionKey](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ExecutionKey),
) [ComponentRef](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ComponentRef)

NewComponentRef creates a new ComponentRef with a registered root component go type.

In V1, if you don't have a ref, then you can only interact with the (top level) execution.

ProtoRefToComponentRef converts a persistence ChasmComponentRef reference to a ComponentRef. This is useful for situations where the protobuf ComponentRef has already been deserialized as part of an enclosing message.

func (r *[ComponentRef](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ComponentRef)) ArchetypeID(
	registry *[Registry](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Registry),
) ([ArchetypeID](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ArchetypeID), [error](https://pkg.go.dev/builtin#error))

ShardingKey returns the sharding key used for determining the shardID of the run that contains the referenced component. TODO: remove this method and ShardingKey concept, we don't need this functionality.

NewContext creates a new Context from an existing Context and root Node.

NOTE: Library authors should not invoke this constructor directly, and instead use [ReadComponent](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ReadComponent).

type CoreLibrary struct {
[UnimplementedLibrary](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#UnimplementedLibrary)}

CoreLibrary contains built-in components maintained as part of the CHASM framework.

func (b *[CoreLibrary](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#CoreLibrary)) Components() []*[RegistrableComponent](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#RegistrableComponent)

func (b *[CoreLibrary](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#CoreLibrary)) Tasks() []*[RegistrableTask](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#RegistrableTask)

type CountExecutionsRequest struct {
 NamespaceID [string](https://pkg.go.dev/builtin#string) NamespaceName [string](https://pkg.go.dev/builtin#string) Query [string](https://pkg.go.dev/builtin#string)}

type CountExecutionsResponse struct {
 Count [int64](https://pkg.go.dev/builtin#int64) Groups [][Group](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Group)}

CountExecutions counts the executions of a CHASM archetype given an initial query. The generic parameter C is the CHASM component type used for executions and search attribute filtering. The query string can specify any combination of CHASM, custom, and predefined/system search attributes. Note: For CHASM executions, TemporalNamespaceDivision is the predefined search attribute that is used to identify the archetype of the execution. If the query string does not specify TemporalNamespaceDivision, the archetype C of the request will be used to count the executions. If the initial query already specifies TemporalNamespaceDivision, the archetype C of the request will only be used to get the registered SearchAttributes.

type Engine interface {
 NewExecution( 		[context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context),
		[ComponentRef](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ComponentRef),
		func([MutableContext](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MutableContext)) ([Component](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Component), [error](https://pkg.go.dev/builtin#error)),
		...[TransitionOption](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#TransitionOption),
	) ([EngineNewExecutionResult](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#EngineNewExecutionResult), [error](https://pkg.go.dev/builtin#error))
 UpdateWithNewExecution( 		[context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context),
		[ComponentRef](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ComponentRef),
		func([MutableContext](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MutableContext)) ([Component](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Component), [error](https://pkg.go.dev/builtin#error)),
		func([MutableContext](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MutableContext), [Component](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Component)) [error](https://pkg.go.dev/builtin#error),
		...[TransitionOption](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#TransitionOption),
	) ([ExecutionKey](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ExecutionKey), [][byte](https://pkg.go.dev/builtin#byte), [error](https://pkg.go.dev/builtin#error))

 UpdateComponent( 		[context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context),
		[ComponentRef](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ComponentRef),
		func([MutableContext](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MutableContext), [Component](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Component)) [error](https://pkg.go.dev/builtin#error),
		...[TransitionOption](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#TransitionOption),
	) ([][byte](https://pkg.go.dev/builtin#byte), [error](https://pkg.go.dev/builtin#error))
 ReadComponent( 		[context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context),
		[ComponentRef](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ComponentRef),
		func([Context](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Context), [Component](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Component)) [error](https://pkg.go.dev/builtin#error),
		...[TransitionOption](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#TransitionOption),
	) [error](https://pkg.go.dev/builtin#error)

 PollComponent( 		[context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context),
		[ComponentRef](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ComponentRef),
		func([Context](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Context), [Component](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Component)) ([bool](https://pkg.go.dev/builtin#bool), [error](https://pkg.go.dev/builtin#error)),
		...[TransitionOption](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#TransitionOption),
	) ([][byte](https://pkg.go.dev/builtin#byte), [error](https://pkg.go.dev/builtin#error))

	NotifyExecution([ExecutionKey](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ExecutionKey))
}

type EngineNewExecutionResult = [NewExecutionResult](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewExecutionResult)[struct{}]

EngineNewExecutionResult is a type alias for the result type returned by the Engine implementation. This avoids repeating [struct{}] everywhere in the engine implementation.

type ExecutionAlreadyStartedError struct {
 Message [string](https://pkg.go.dev/builtin#string) CurrentRequestID [string](https://pkg.go.dev/builtin#string) CurrentRunID [string](https://pkg.go.dev/builtin#string)}

func NewExecutionAlreadyStartedErr(
	message, currentRequestID, currentRunID [string](https://pkg.go.dev/builtin#string),
) *[ExecutionAlreadyStartedError](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ExecutionAlreadyStartedError)

ExecutionKey uniquely identifies a CHASM execution in the system.

func UpdateWithNewExecution[C [Component](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Component), I [any](https://pkg.go.dev/builtin#any), O1 [any](https://pkg.go.dev/builtin#any), O2 [any](https://pkg.go.dev/builtin#any)](
	ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context),
	key [ExecutionKey](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ExecutionKey),
	newFn func([MutableContext](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MutableContext), I) (C, O1, [error](https://pkg.go.dev/builtin#error)),
	updateFn func(C, [MutableContext](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MutableContext), I) (O2, [error](https://pkg.go.dev/builtin#error)),
	input I,
	opts ...[TransitionOption](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#TransitionOption),
) (O1, O2, [ExecutionKey](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ExecutionKey), [][byte](https://pkg.go.dev/builtin#byte), [error](https://pkg.go.dev/builtin#error))

type Field[T [any](https://pkg.go.dev/builtin#any)] struct {
	Internal fieldInternal
}

func ComponentPointerTo[C [Component](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Component)](
	ctx [MutableContext](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MutableContext),
	c C,
) [Field](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Field)[C]

ComponentPointerTo returns a CHASM field populated with a pointer to the given component. Pointers are resolved at the time the transaction is closed, and the transaction will fail if any pointers cannot be resolved.

DataPointerTo returns a CHASM field populated with a pointer to the given message. Pointers are resolved at the time the transaction is closed, and the transaction will fail if any pointers cannot be resolved.

func NewComponentField[C [Component](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Component)](
	ctx [MutableContext](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MutableContext),
	c C,
	options ...[ComponentFieldOption](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ComponentFieldOption),
) [Field](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Field)[C]

re. Data v.s. Component. Components have behavior and has a lifecycle. while Data doesn't and must be attached to a component.

You can define a component just for storing the data, that may contain other information like ref count etc. most importantly, the framework needs to know when it's safe to delete the data. i.e. the lifecycle of that data component reaches completed.

func NewEmptyField[T [any](https://pkg.go.dev/builtin#any)]() [Field](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Field)[T]

func (f [Field](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Field)[T]) Get(chasmContext [Context](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Context)) T

Get returns the value of the field, deserializing it if necessary. Panics rather than returning an error, as errors are supposed to be handled by the framework as opposed to the application, even if the error is an application bug.

func (f [Field](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Field)[T]) TryGet(chasmContext [Context](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Context)) (T, [bool](https://pkg.go.dev/builtin#bool))

TryGet returns the value of the field and a boolean indicating if the value was found, deserializing if necessary. Panics rather than returning an error, as errors are supposed to be handled by the framework as opposed to the application, even if the error is an application bug.

type Library interface {
 Name() [string](https://pkg.go.dev/builtin#string) Components() []*[RegistrableComponent](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#RegistrableComponent) Tasks() []*[RegistrableTask](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#RegistrableTask) RegisterServices(server *[grpc](https://pkg.go.dev/google.golang.org/grpc).[Server](https://pkg.go.dev/google.golang.org/grpc#Server)) 	
}

Shall it be named ComponentLifecycleState?

const (
	
	
	LifecycleStateRunning [LifecycleState](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#LifecycleState) = 2 << [iota](https://pkg.go.dev/builtin#iota)

	
	
 LifecycleStateCompleted  LifecycleStateFailed )

type ListExecutionsResponse[M [proto](https://pkg.go.dev/google.golang.org/protobuf/proto).[Message](https://pkg.go.dev/google.golang.org/protobuf/proto#Message)] struct {
 Executions []*[ExecutionInfo](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ExecutionInfo)[M]  NextPageToken [][byte](https://pkg.go.dev/builtin#byte)}

ListExecutions lists the executions of a CHASM archetype given an initial query. The query string can specify any combination of CHASM, custom, and predefined/system search attributes. The generic parameter C is the CHASM component type used for executions and search attribute filtering. The generic parameter M is the type of the memo payload to be unmarshaled from the execution. PageSize is required, must be greater than 0. NextPageToken is optional, set on subsequent requests to continue listing the next page of executions. Note: For CHASM executions, TemporalNamespaceDivision is the predefined search attribute that is used to identify the archetype of the execution. If the query string does not specify TemporalNamespaceDivision, the archetype C of the request will be used to filter the executions. If the initial query already specifies TemporalNamespaceDivision, the archetype C of the request will only be used to get the registered SearchAttributes.

type MSPointer struct {
	
}

MSPointer is a special CHASM type which components can use to access their Node's underlying backend (i.e. mutable state). It is used to expose methods needed from the mutable state without polluting the chasm.Context interface. When deserializing components with fields of this type, the CHASM engine will set the value to its NodeBackend. This should only be used by the Workflow component.

func NewMSPointer(backend [NodeBackend](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NodeBackend)) [MSPointer](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MSPointer)

NewMSPointer creates a new MSPointer instance.

GetNexusCompletion retrieves the Nexus operation completion data for the given request ID from the underlying mutable state.

type MockComponent struct {
	
}

MockComponent is a mock of Component interface.

NewMockComponent creates a new mock instance.

func (m *[MockComponent](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockComponent)) EXPECT() *[MockComponentMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockComponentMockRecorder)

EXPECT returns an object that allows the caller to indicate expected use.

func (m *[MockComponent](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockComponent)) LifecycleState(arg0 [Context](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Context)) [LifecycleState](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#LifecycleState)

LifecycleState mocks base method.

Terminate mocks base method.

type MockComponentMockRecorder struct {
	
}

MockComponentMockRecorder is the mock recorder for MockComponent.

LifecycleState indicates an expected call of LifecycleState.

Terminate indicates an expected call of Terminate.

type MockContext struct {
 HandleExecutionKey func() [ExecutionKey](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ExecutionKey) HandleNow func(component [Component](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Component)) [time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time) HandleRef func(component [Component](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Component)) ([][byte](https://pkg.go.dev/builtin#byte), [error](https://pkg.go.dev/builtin#error))  HandleExecutionCloseTime func() [time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time)}

MockContext is a mock implementation of [Context](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Context).

func (c *[MockContext](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockContext)) ExecutionKey() [ExecutionKey](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ExecutionKey)

type MockEngine struct {
	
}

MockEngine is a mock of Engine interface.

NewMockEngine creates a new mock instance.

func (m *[MockEngine](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockEngine)) EXPECT() *[MockEngineMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockEngineMockRecorder)

EXPECT returns an object that allows the caller to indicate expected use.

NewExecution mocks base method.

func (m *[MockEngine](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockEngine)) NotifyExecution(arg0 [ExecutionKey](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ExecutionKey))

NotifyExecution mocks base method.

PollComponent mocks base method.

ReadComponent mocks base method.

UpdateComponent mocks base method.

UpdateWithNewExecution mocks base method.

type MockEngineMockRecorder struct {
	
}

MockEngineMockRecorder is the mock recorder for MockEngine.

NewExecution indicates an expected call of NewExecution.

NotifyExecution indicates an expected call of NotifyExecution.

PollComponent indicates an expected call of PollComponent.

ReadComponent indicates an expected call of ReadComponent.

UpdateComponent indicates an expected call of UpdateComponent.

UpdateWithNewExecution indicates an expected call of UpdateWithNewExecution.

type MockLibrary struct {
	
}

MockLibrary is a mock of Library interface.

NewMockLibrary creates a new mock instance.

func (m *[MockLibrary](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockLibrary)) Components() []*[RegistrableComponent](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#RegistrableComponent)

Components mocks base method.

func (m *[MockLibrary](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockLibrary)) EXPECT() *[MockLibraryMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockLibraryMockRecorder)

EXPECT returns an object that allows the caller to indicate expected use.

Name mocks base method.

RegisterServices mocks base method.

func (m *[MockLibrary](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockLibrary)) Tasks() []*[RegistrableTask](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#RegistrableTask)

Tasks mocks base method.

type MockLibraryMockRecorder struct {
	
}

MockLibraryMockRecorder is the mock recorder for MockLibrary.

Components indicates an expected call of Components.

Name indicates an expected call of Name.

RegisterServices indicates an expected call of RegisterServices.

Tasks indicates an expected call of Tasks.

type MockMutableContext struct {
[MockContext](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockContext)
 Tasks [][MockTask](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockTask)	
}

MockMutableContext is a mock implementation of [MutableContext](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MutableContext) that records added tasks for inspection in tests.

func (c *[MockMutableContext](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockMutableContext)) AddTask(component [Component](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Component), attributes [TaskAttributes](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#TaskAttributes), payload [any](https://pkg.go.dev/builtin#any))

MockNodeBackend is a lightweight manual mock for the NodeBackend interface. Methods may be stubbed by assigning the corresponding Handle fields. Update call history is recorded in the struct fields (thread-safe).

func (m *[MockNodeBackend](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockNodeBackend)) DeleteCHASMPureTasks(maxScheduledTime [time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time))

func (m *[MockNodeBackend](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockNodeBackend)) GetCurrentVersion() [int64](https://pkg.go.dev/builtin#int64)

func (m *[MockNodeBackend](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockNodeBackend)) IsWorkflow() [bool](https://pkg.go.dev/builtin#bool)

func (m *[MockNodeBackend](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockNodeBackend)) NextTransitionCount() [int64](https://pkg.go.dev/builtin#int64)

func (m *[MockNodeBackend](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockNodeBackend)) NumTasksAdded() [int](https://pkg.go.dev/builtin#int)

MockNodePureTask is a lightweight manual mock for the NodePureTask interface. Methods may be stubbed by assigning the corresponding Handle fields. Call history is recorded in the struct fields (thread-safe).

type MockPureTaskExecutor[C [any](https://pkg.go.dev/builtin#any), T [any](https://pkg.go.dev/builtin#any)] struct {
	
}

MockPureTaskExecutor is a mock of PureTaskExecutor interface.

NewMockPureTaskExecutor creates a new mock instance.

func (m *[MockPureTaskExecutor](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockPureTaskExecutor)[C, T]) EXPECT() *[MockPureTaskExecutorMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockPureTaskExecutorMockRecorder)[C, T]

EXPECT returns an object that allows the caller to indicate expected use.

func (m *[MockPureTaskExecutor](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockPureTaskExecutor)[C, T]) Execute(arg0 [MutableContext](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MutableContext), arg1 C, arg2 [TaskAttributes](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#TaskAttributes), arg3 T) [error](https://pkg.go.dev/builtin#error)

Execute mocks base method.

type MockPureTaskExecutorMockRecorder[C [any](https://pkg.go.dev/builtin#any), T [any](https://pkg.go.dev/builtin#any)] struct {
	
}

MockPureTaskExecutorMockRecorder is the mock recorder for MockPureTaskExecutor.

Execute indicates an expected call of Execute.

type MockSideEffectTaskExecutor[C [any](https://pkg.go.dev/builtin#any), T [any](https://pkg.go.dev/builtin#any)] struct {
	
}

MockSideEffectTaskExecutor is a mock of SideEffectTaskExecutor interface.

NewMockSideEffectTaskExecutor creates a new mock instance.

func (m *[MockSideEffectTaskExecutor](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockSideEffectTaskExecutor)[C, T]) EXPECT() *[MockSideEffectTaskExecutorMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockSideEffectTaskExecutorMockRecorder)[C, T]

EXPECT returns an object that allows the caller to indicate expected use.

Execute mocks base method.

type MockSideEffectTaskExecutorMockRecorder[C [any](https://pkg.go.dev/builtin#any), T [any](https://pkg.go.dev/builtin#any)] struct {
	
}

MockSideEffectTaskExecutorMockRecorder is the mock recorder for MockSideEffectTaskExecutor.

Execute indicates an expected call of Execute.

type MockTask struct {
 Component [Component](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Component) Attributes [TaskAttributes](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#TaskAttributes) Payload [any](https://pkg.go.dev/builtin#any)}

type MockTaskValidator[C [any](https://pkg.go.dev/builtin#any), T [any](https://pkg.go.dev/builtin#any)] struct {
	
}

MockTaskValidator is a mock of TaskValidator interface.

NewMockTaskValidator creates a new mock instance.

func (m *[MockTaskValidator](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockTaskValidator)[C, T]) EXPECT() *[MockTaskValidatorMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockTaskValidatorMockRecorder)[C, T]

EXPECT returns an object that allows the caller to indicate expected use.

func (m *[MockTaskValidator](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MockTaskValidator)[C, T]) Validate(arg0 [Context](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Context), arg1 C, arg2 [TaskAttributes](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#TaskAttributes), arg3 T) ([bool](https://pkg.go.dev/builtin#bool), [error](https://pkg.go.dev/builtin#error))

Validate mocks base method.

type MockTaskValidatorMockRecorder[C [any](https://pkg.go.dev/builtin#any), T [any](https://pkg.go.dev/builtin#any)] struct {
	
}

MockTaskValidatorMockRecorder is the mock recorder for MockTaskValidator.

Validate indicates an expected call of Validate.

type MockVisibilityManager struct {
	
}

MockVisibilityManager is a mock of VisibilityManager interface.

NewMockVisibilityManager creates a new mock instance.

CountExecutions mocks base method.

EXPECT returns an object that allows the caller to indicate expected use.

ListExecutions mocks base method.

type MockVisibilityManagerMockRecorder struct {
	
}

MockVisibilityManagerMockRecorder is the mock recorder for MockVisibilityManager.

CountExecutions indicates an expected call of CountExecutions.

ListExecutions indicates an expected call of ListExecutions.

type Mocknamer struct {
	
}

Mocknamer is a mock of namer interface.

NewMocknamer creates a new mock instance.

func (m *[Mocknamer](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Mocknamer)) EXPECT() *[MocknamerMockRecorder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MocknamerMockRecorder)

EXPECT returns an object that allows the caller to indicate expected use.

Name mocks base method.

type MocknamerMockRecorder struct {
	
}

MocknamerMockRecorder is the mock recorder for Mocknamer.

Name indicates an expected call of Name.

type MutableContext interface {
	[Context](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Context)

	
	
	AddTask([Component](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Component), [TaskAttributes](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#TaskAttributes), [any](https://pkg.go.dev/builtin#any))
}

NewMutableContext creates a new MutableContext from an existing Context and root Node.

NOTE: Library authors should not invoke this constructor directly, and instead use the [UpdateComponent](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#UpdateComponent), [UpdateWithNewExecution](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#UpdateWithNewExecution), or [NewExecution](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewExecution) APIs.

type NewExecutionResult[O [any](https://pkg.go.dev/builtin#any)] struct {
 ExecutionKey [ExecutionKey](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ExecutionKey) NewExecutionRef [][byte](https://pkg.go.dev/builtin#byte) Created [bool](https://pkg.go.dev/builtin#bool) Output O }

NewExecutionResult contains the outcome of creating a new execution via [NewExecution](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewExecution) or [UpdateWithNewExecution](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#UpdateWithNewExecution).

This struct provides information about whether a new execution was actually created, along with identifiers needed to reference the execution in subsequent operations.

Fields:

*   ExecutionKey: The unique identifier for the execution. This key can be used to look up or reference the execution in future operations.
*   NewExecutionRef: A serialized reference to the newly created root component. This can be passed to [UpdateComponent](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#UpdateComponent), [ReadComponent](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ReadComponent), or [PollComponent](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#PollComponent) to interact with the component. Use [DeserializeComponentRef](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#DeserializeComponentRef) to convert this back to a [ComponentRef](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ComponentRef) if needed.
*   Created: Indicates whether a new execution was actually created. When false, the execution already existed (based on the [BusinessIDReusePolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#BusinessIDReusePolicy) and [BusinessIDConflictPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#BusinessIDConflictPolicy) configured via [WithBusinessIDPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#WithBusinessIDPolicy)), and the existing execution was returned instead.
*   Output: The output value returned by the factory function.

func NewExecution[C [Component](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Component), I [any](https://pkg.go.dev/builtin#any), O [any](https://pkg.go.dev/builtin#any)](
	ctx [context](https://pkg.go.dev/context).[Context](https://pkg.go.dev/context#Context),
	key [ExecutionKey](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ExecutionKey),
	newFn func([MutableContext](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MutableContext), I) (C, O, [error](https://pkg.go.dev/builtin#error)),
	input I,
	opts ...[TransitionOption](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#TransitionOption),
) ([NewExecutionResult](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewExecutionResult)[O], [error](https://pkg.go.dev/builtin#error))

NewExecution creates a new execution with a component initialized by the provided factory function.

This is the primary entry point for starting a new execution in the CHASM engine. It handles the lifecycle of creating and persisting a new component within an execution context.

Type Parameters:

*   C: The component type to create, must implement [Component](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Component)
*   I: The input type passed to the factory function
*   O: The output type returned by the factory function

Parameters:

*   ctx: Context containing the CHASM engine (must be created via [NewEngineContext](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewEngineContext))
*   key: Unique identifier for the execution, used for deduplication and lookup
*   newFn: Factory function that creates the component and produces output. Receives a [MutableContext](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MutableContext) for accessing engine capabilities and the input value.
*   input: Application-specific data passed to newFn
*   opts: Optional [TransitionOption](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#TransitionOption) functions to configure creation behavior:
*   [WithBusinessIDPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#WithBusinessIDPolicy): Controls duplicate handling and conflict resolution
*   [WithRequestID](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#WithRequestID): Sets a request ID for idempotency
*   [WithSpeculative](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#WithSpeculative): Defers persistence until the next non-speculative transition

Returns:

*   O: The output value produced by newFn
*   [NewExecutionResult](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NewExecutionResult): Contains the execution key, serialized ref, and whether a new execution was created
*   error: Non-nil if creation failed or policy constraints were violated

#### type [NexusCompletionHandler](https://github.com/temporalio/temporal/blob/v1.30.0/chasm/nexus_completion.go#L14)[¶](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NexusCompletionHandler "Go to NexusCompletionHandler")added in v1.30.0

NexusCompletionHandler is implemented by CHASM components that want to handle Nexus operation completion callbacks.

type NoValue = *struct{}

NoValue is a sentinel type representing no value. Useful for accessing components using the engine methods (e.g., [GetComponent]) with a function that does not need to return any information.

type Node struct {
	
}

Node is the in-memory representation of a persisted CHASM node.

Node and all its methods are NOT meant to be used by CHASM component authors. They are exported for use by the CHASM engine and underlying MutableState implementation only.

NewEmptyTree creates a new empty in-memory CHASM tree.

NewTreeFromDB creates a new in-memory CHASM tree from a collection of flattened persistence CHASM nodes. This method should only be used when loading an existing CHASM tree from database. If serializedNodes is empty, the tree will be considered as a legacy Workflow execution without any CHASM nodes.

func (n *[Node](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Node)) AddTask(
	component [Component](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Component),
	taskAttributes [TaskAttributes](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#TaskAttributes),
	task [any](https://pkg.go.dev/builtin#any),
)

AddTask implements the CHASM MutableContext interface

func (n *[Node](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Node)) ApplyMutation(
	mutation [NodesMutation](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NodesMutation),
) [error](https://pkg.go.dev/builtin#error)

ApplyMutation is used by replication stack to apply node mutations from the source cluster.

NOTE: It will be an error if UpdatedNodes and DeletedNodes have overlapping keys, as the CHASM tree does not have enough information to tell if the deletion happens before or after the update.

func (n *[Node](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Node)) ApplySnapshot(
	incomingSnapshot [NodesSnapshot](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NodesSnapshot),
) [error](https://pkg.go.dev/builtin#error)

ApplySnapshot is used by replication stack to apply node snapshot from the source cluster.

If we simply substituting the entire CHASM tree, we will be forced to close the transaction as snapshot and potentially write extra data to persistence. This method will instead figure out the mutations needed to bring the current tree to the be the same as the snapshot, thus allowing us to close the transaction as mutation.

func (n *[Node](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Node)) Archetype() ([Archetype](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Archetype), [error](https://pkg.go.dev/builtin#error))

Archetype returns the root component's fully qualified name. Deprecated: use ArchetypeID() instead, this method will be removed.

func (n *[Node](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Node)) ArchetypeID() [ArchetypeID](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ArchetypeID)

ArchetypeID returns the framework's internal ID for the root component's fully qualified name.

func (n *[Node](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Node)) CloseTransaction() ([NodesMutation](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NodesMutation), [error](https://pkg.go.dev/builtin#error))

CloseTransaction is used by MutableState to close the transaction and track changes made in the current transaction.

func (n *[Node](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Node)) Component(
	chasmContext [Context](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Context),
	ref [ComponentRef](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ComponentRef),
) ([Component](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Component), [error](https://pkg.go.dev/builtin#error))

Component retrieves a component from the tree rooted at node n using the provided component reference It also performs access rule, and task validation checks (for task processing requests) before returning the component.

func (n *[Node](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Node)) ComponentByPath(
	chasmContext [Context](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Context),
	path [][string](https://pkg.go.dev/builtin#string),
) ([Component](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Component), [error](https://pkg.go.dev/builtin#error))

EachPureTask runs the callback for all expired/runnable pure tasks within the CHASM tree (including invalid tasks). The CHASM tree is left untouched, even if invalid tasks are detected (these are cleaned up as part of transaction close).

ExecutePureTask validates and then executes the given taskInstance against the node's component. Executing an invalid task is a no-op (no error returned).

ExecuteSideEffectTask executes the given ChasmTask on its associated node without holding the execution lock.

WARNING: This method *must not* access the node's properties without first locking the execution.

ctx should have a CHASM engine already set.

func (n *[Node](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Node)) IsDirty() [bool](https://pkg.go.dev/builtin#bool)

IsDirty returns true if any node in the tree has been modified, and need to be persisted in DB. The result will be reset to false after a call to CloseTransaction().

func (n *[Node](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Node)) IsStale(
	ref [ComponentRef](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ComponentRef),
) [error](https://pkg.go.dev/builtin#error)

func (n *[Node](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Node)) IsStateDirty() [bool](https://pkg.go.dev/builtin#bool)

IsStateDirty returns true if any node in the tree has USER DATA modified, which need to be persisted to DB AND replicated to other clusters. The result will be reset to false after a call to CloseTransaction().

Now implements the CHASM Context interface

Ref implements the CHASM Context interface

func (n *[Node](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Node)) RefreshTasks() [error](https://pkg.go.dev/builtin#error)

func (n *[Node](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Node)) SetRootComponent(
	rootComponent [Component](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Component),
)

Snapshot returns all nodes in the tree that have been modified after the given min versioned transition. A nil exclusiveMinVT will be treated as the same as the zero versioned transition and returns all nodes in the tree. This method should only be invoked on root CHASM node when IsDirty() is false.

ValidatePureTask runs a pure task's associated validator, returning true if the task is valid. Intended for use by standby executors as part of EachPureTask's callback. This method assumes the node's value has already been prepared (hydrated).

ValidateSideEffectTask runs a side effect task's associated validator, returning the deserialized task instance if the task is valid. Intended for use by standby executors.

If validation succeeds but the task is invalid, nil is returned to signify the task can be skipped/deleted.

If validation fails, that error is returned.

NodeBackend is a set of methods needed from MutableState

This is for breaking cycle dependency between this package and service/history/workflow package where MutableState is defined.

NodePathEncoder is an interface for encoding and decoding node paths. Logic outside the chasm package should only work with encoded paths.

var DefaultPathEncoder [NodePathEncoder](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#NodePathEncoder) = &defaultPathEncoder{}

NodePureTask is intended to be implemented and used within the CHASM framework only.

NodesMutation is a set of mutations for all nodes rooted at a given node n, including the node n itself.

NodesSnapshot is a snapshot for all nodes rooted at a given node n, including the node n itself.

const (
 OperationIntentProgress [OperationIntent](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#OperationIntent) = 1 << [iota](https://pkg.go.dev/builtin#iota) OperationIntentObserve 
 OperationIntentUnspecified = [OperationIntent](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#OperationIntent)(0) )

type ParentPtr[T [any](https://pkg.go.dev/builtin#any)] struct {
	
	Internal parentPtrInternal
}

ParentPtr is a in-memory pointer to the parent component of a CHASM component.

CHASM map is not a component, so if a component is inside a map, its ParentPtr will point to the nearest ancestor component that is not a map.

ParentPtr is only initialized and available for use **after** the transition that creates the component using ParentPtr is completed.

func (p [ParentPtr](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ParentPtr)[T]) Get(chasmContext [Context](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Context)) T

Get returns the parent component, deserializing it if necessary. Panics rather than returning an error, as errors are supposed to be handled by the framework as opposed to the application.

func (p [ParentPtr](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ParentPtr)[T]) TryGet(chasmContext [Context](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Context)) (T, [bool](https://pkg.go.dev/builtin#bool))

TryGet returns the parent component and a boolean indicating if the value was found, deserializing if necessary. Panics rather than returning an error, as errors are supposed to be handled by the framework as opposed to the application.

type PureTaskExecutor[C [any](https://pkg.go.dev/builtin#any), T [any](https://pkg.go.dev/builtin#any)] interface {
 Execute([MutableContext](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MutableContext), C, [TaskAttributes](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#TaskAttributes), T) [error](https://pkg.go.dev/builtin#error)}

type RegistrableComponent struct {
	
}

func NewRegistrableComponent[C [Component](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Component)](
	componentType [string](https://pkg.go.dev/builtin#string),
	opts ...[RegistrableComponentOption](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#RegistrableComponentOption),
) *[RegistrableComponent](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#RegistrableComponent)

func (rc *[RegistrableComponent](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#RegistrableComponent)) SearchAttributesMapper() *[VisibilitySearchAttributesMapper](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilitySearchAttributesMapper)

SearchAttributesMapper returns the search attributes mapper for this component.

type RegistrableComponentOption func(*[RegistrableComponent](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#RegistrableComponent))

WithBusinessIDAlias allows specifying the business ID alias of the component. This option must be specified if the archetype uses the Visibility component.

func WithEphemeral() [RegistrableComponentOption](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#RegistrableComponentOption)

func WithSearchAttributes(
	searchAttributes ...[SearchAttribute](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SearchAttribute),
) [RegistrableComponentOption](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#RegistrableComponentOption)

func WithShardingFn(
	shardingFn func([ExecutionKey](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#ExecutionKey)) [string](https://pkg.go.dev/builtin#string),
) [RegistrableComponentOption](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#RegistrableComponentOption)

WithShardingFn allows specifying a custom sharding key function for the component. TODO: remove WithShardingFn, we don't need this functionality.

func WithSingleCluster() [RegistrableComponentOption](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#RegistrableComponentOption)

Is there any use case where we don't want to replicate certain instances of a archetype?

type RegistrableTask struct {
	
}

func NewRegistrablePureTask[C [any](https://pkg.go.dev/builtin#any), T [any](https://pkg.go.dev/builtin#any)](
	taskType [string](https://pkg.go.dev/builtin#string),
	validator TaskValidator[C, T],
	executor PureTaskExecutor[C, T],
	opts ...[RegistrableTaskOption](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#RegistrableTaskOption),
) *[RegistrableTask](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#RegistrableTask)

func NewRegistrableSideEffectTask[C [any](https://pkg.go.dev/builtin#any), T [any](https://pkg.go.dev/builtin#any)](
	taskType [string](https://pkg.go.dev/builtin#string),
	validator TaskValidator[C, T],
	executor [SideEffectTaskExecutor](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SideEffectTaskExecutor)[C, T],
	opts ...[RegistrableTaskOption](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#RegistrableTaskOption),
) *[RegistrableTask](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#RegistrableTask)

NOTE: C is not Component but any.

type RegistrableTaskOption func(*[RegistrableTask](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#RegistrableTask))

type Registry struct {
	
}

ArchetypeIDOf returns the ArchetypeID for the given component Go type. This method should only be used by CHASM framework internal, NOT CHASM library developers.

ComponentByID returns the registrable component for a given archetype ID.

ComponentFqnByID converts component type ID to fully qualified component type name. This method should only be used by CHASM framework internal code, NOT CHASM library developers.

ComponentIDByFqn converts fully qualified component type name to component type ID. This method should only be used by CHASM framework internal code, NOT CHASM library developers.

ComponentIDFor converts registered component instance to component type ID. This method should only be used by CHASM framework internal code, NOT CHASM library developers.

RegisterServices registers all gRPC services from all registered libraries.

TaskFqnByID converts task type ID to fully qualified task type name. This method should only be used by CHASM framework internal code, NOT CHASM library developers.

TaskIDFor converts registered task instance to task type ID. This method should only be used by CHASM framework internal code, NOT CHASM library developers.

type SearchAttribute interface {
	
}

SearchAttribute is a shared interface for all search attribute types. Each type must embed searchAttributeDefinition.

type SearchAttributeBool struct {
	
}

SearchAttributeBool is a search attribute for a boolean value.

func NewSearchAttributeBool(alias [string](https://pkg.go.dev/builtin#string), boolField [SearchAttributeFieldBool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SearchAttributeFieldBool)) [SearchAttributeBool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SearchAttributeBool)

NewSearchAttributeBool creates a new boolean search attribute given a predefined chasm field

func (s [SearchAttributeBool](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SearchAttributeBool)) Value(value [bool](https://pkg.go.dev/builtin#bool)) SearchAttributeKeyValue

Value sets the boolean value of the search attribute.

type SearchAttributeDateTime struct {
	
}

SearchAttributeDateTime is a search attribute for a datetime value.

func NewSearchAttributeDateTime(alias [string](https://pkg.go.dev/builtin#string), datetimeField [SearchAttributeFieldDateTime](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SearchAttributeFieldDateTime)) [SearchAttributeDateTime](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SearchAttributeDateTime)

NewSearchAttributeDateTime creates a new date time search attribute given a predefined chasm field

func (s [SearchAttributeDateTime](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SearchAttributeDateTime)) Value(value [time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time)) SearchAttributeKeyValue

Value sets the date time value of the search attribute.

type SearchAttributeDouble struct {
	
}

SearchAttributeDouble is a search attribute for a double value.

func NewSearchAttributeDouble(alias [string](https://pkg.go.dev/builtin#string), doubleField [SearchAttributeFieldDouble](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SearchAttributeFieldDouble)) [SearchAttributeDouble](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SearchAttributeDouble)

NewSearchAttributeDouble creates a new double search attribute given a predefined chasm field

func (s [SearchAttributeDouble](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SearchAttributeDouble)) Value(value [float64](https://pkg.go.dev/builtin#float64)) SearchAttributeKeyValue

Value sets the double value of the search attribute.

type SearchAttributeFieldBool struct {
	
}

SearchAttributeFieldBool is a search attribute field for a boolean value.

type SearchAttributeFieldDateTime struct {
	
}

SearchAttributeFieldDateTime is a search attribute field for a datetime value.

type SearchAttributeFieldDouble struct {
	
}

SearchAttributeFieldDouble is a search attribute field for a double value.

type SearchAttributeFieldInt struct {
	
}

SearchAttributeFieldInt is a search attribute field for an integer value.

type SearchAttributeFieldKeyword struct {
	
}

SearchAttributeFieldKeyword is a search attribute field for a keyword value.

type SearchAttributeFieldKeywordList struct {
	
}

SearchAttributeFieldKeywordList is a search attribute field for a keyword list value.

type SearchAttributeInt struct {
	
}

SearchAttributeInt is a search attribute for an integer value.

func NewSearchAttributeInt(alias [string](https://pkg.go.dev/builtin#string), intField [SearchAttributeFieldInt](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SearchAttributeFieldInt)) [SearchAttributeInt](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SearchAttributeInt)

NewSearchAttributeInt creates a new integer search attribute given a predefined chasm field

func (s [SearchAttributeInt](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SearchAttributeInt)) Value(value [int64](https://pkg.go.dev/builtin#int64)) SearchAttributeKeyValue

Value sets the integer value of the search attribute.

type SearchAttributeKeyValue struct {
	Alias [string](https://pkg.go.dev/builtin#string)
	Field [string](https://pkg.go.dev/builtin#string)
	Value [VisibilityValue](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilityValue)
}

SearchAttributeKeyValue is a key value pair of a search attribute. Represents the current value of a search attribute in a CHASM Component during a transaction.

type SearchAttributeKeyword struct {
	
}

SearchAttributeKeyword is a search attribute for a keyword value.

func NewSearchAttributeKeyword(alias [string](https://pkg.go.dev/builtin#string), keywordField [SearchAttributeFieldKeyword](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SearchAttributeFieldKeyword)) [SearchAttributeKeyword](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SearchAttributeKeyword)

NewSearchAttributeKeyword creates a new keyword search attribute given a predefined chasm field

func (s [SearchAttributeKeyword](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SearchAttributeKeyword)) Value(value [string](https://pkg.go.dev/builtin#string)) SearchAttributeKeyValue

Value sets the string value of the search attribute.

type SearchAttributeKeywordList struct {
	
}

SearchAttributeKeywordList is a search attribute for a keyword list value.

func NewSearchAttributeKeywordList(alias [string](https://pkg.go.dev/builtin#string), keywordListField [SearchAttributeFieldKeywordList](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SearchAttributeFieldKeywordList)) [SearchAttributeKeywordList](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SearchAttributeKeywordList)

NewSearchAttributeKeywordList creates a new keyword list search attribute given a predefined chasm field

func (s [SearchAttributeKeywordList](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SearchAttributeKeywordList)) Value(value [][string](https://pkg.go.dev/builtin#string)) SearchAttributeKeyValue

Value sets the string list value of the search attribute.

type SearchAttributesMap struct {
	
}

SearchAttributesMap wraps search attribute values with type-safe access.

func NewSearchAttributesMap(values map[[string](https://pkg.go.dev/builtin#string)][VisibilityValue](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#VisibilityValue)) [SearchAttributesMap](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#SearchAttributesMap)

NewSearchAttributesMap creates a new SearchAttributeMap from raw values.

type StateMachine[S [comparable](https://pkg.go.dev/builtin#comparable)] interface {
 StateMachineState() S  SetStateMachineState(S) }

A StateMachine is anything that can get and set a comparable state S and re-generate tasks based on current state. It is meant to be used with [Transition](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Transition) objects to safely transition their state on a given event.

type TaskAttributes struct {
 ScheduledTime [time](https://pkg.go.dev/time).[Time](https://pkg.go.dev/time#Time) Destination [string](https://pkg.go.dev/builtin#string)}

func (a *[TaskAttributes](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#TaskAttributes)) IsImmediate() [bool](https://pkg.go.dev/builtin#bool)

type TerminateComponentResponse struct{}

type Transition[S [comparable](https://pkg.go.dev/builtin#comparable), SM [StateMachine](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#StateMachine)[S], E [any](https://pkg.go.dev/builtin#any)] struct {
	Sources []S
	Destination S
	
}

Transition represents a state machine transition for a machine of type SM with state S and event E.

NewTransition creates a new [Transition](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Transition) from the given source states to a destination state for a given event. The apply function is called after verifying the transition is possible and setting the destination state.

func (t [Transition](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Transition)[S, SM, E]) Apply(sm SM, ctx [MutableContext](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MutableContext), event E) [error](https://pkg.go.dev/builtin#error)

Apply applies a transition event to the given state machine changing the state machine's state to the transition's Destination on success.

func (t [Transition](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Transition)[S, SM, E]) Possible(sm SM) [bool](https://pkg.go.dev/builtin#bool)

Possible returns a boolean indicating whether the transition is possible for the current state.

type TransitionOption func(*[TransitionOptions](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#TransitionOptions))

func WithBusinessIDPolicy(
	reusePolicy [BusinessIDReusePolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#BusinessIDReusePolicy),
	conflictPolicy [BusinessIDConflictPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#BusinessIDConflictPolicy),
) [TransitionOption](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#TransitionOption)

WithBusinessIDPolicy sets the businessID reuse and conflict policy used in the transition when creating a new execution. This option only applies to NewExecution() and UpdateWithNewExecution().

func WithRequestID(
	requestID [string](https://pkg.go.dev/builtin#string),
) [TransitionOption](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#TransitionOption)

WithRequestID sets the requestID used when creating a new execution. This option only applies to NewExecution() and UpdateWithNewExecution().

func WithSpeculative() [TransitionOption](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#TransitionOption)

(only) this transition will not be persisted The next non-speculative transition will persist this transition as well. Compared to the ExecutionEphemeral() operation on RegistrableComponent, the scope of this operation is limited to a certain transition, while the ExecutionEphemeral() applies to all transitions. TODO: we need to figure out a way to run the tasks generated in a speculative transition

type TransitionOptions struct {
 ReusePolicy [BusinessIDReusePolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#BusinessIDReusePolicy) ConflictPolicy [BusinessIDConflictPolicy](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#BusinessIDConflictPolicy) RequestID [string](https://pkg.go.dev/builtin#string) Speculative [bool](https://pkg.go.dev/builtin#bool)}

type UnimplementedComponent struct{}

Embed UnimplementedComponent to get forward compatibility

type UnimplementedLibrary struct{}

func ([UnimplementedLibrary](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#UnimplementedLibrary)) Components() []*[RegistrableComponent](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#RegistrableComponent)

RegisterServices Registers the gRPC calls to the handlers of the library.

func ([UnimplementedLibrary](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#UnimplementedLibrary)) Tasks() []*[RegistrableTask](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#RegistrableTask)

func NewVisibility(
	mutableContext [MutableContext](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#MutableContext),
) *[Visibility](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Visibility)

CustomMemo returns the stored custom memo fields. Nil is returned if there are none.

Returned map is NOT a deep copy of the underlying data, so do NOT modify it directly, use Merge/ReplaceCustomMemo methods instead.

CustomSearchAttributes returns the stored custom search attribute fields. Nil is returned if there are none.

Returned map is NOT a deep copy of the underlying data, so do NOT modify it directly, use Merge/ReplaceCustomSearchAttributes methods instead.

func (v *[Visibility](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Visibility)) LifecycleState(_ [Context](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Context)) [LifecycleState](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#LifecycleState)

MergeCustomMemo merges the provided custom memo fields into the existing ones.

*   If a key in `customMemo` already exists, the value in `customMemo` replaces the existing value.
*   If a key in `customMemo` has nil or empty slice payload value, the key is deleted from the existing memo if it exists. If all memo fields are removed, the underlying memo node is deleted.
*   If `customMemo` is empty, this is a no-op.

MergeCustomSearchAttributes merges the provided custom search attribute fields into the existing ones.

*   If a key in `customSearchAttributes` already exists, the value in `customSearchAttributes` replaces the existing value.
*   If a key in `customSearchAttributes` has nil or empty slice payload value, the key is deleted from the existing search attributes if it exists. If all search attributes are removed, the underlying search attributes node is deleted.
*   If `customSearchAttributes` is empty, this is a no-op.

ReplaceCustomMemo replaces the existing custom memo fields with the provided ones. If `customMemo` is empty, the underlying memo node is deleted.

ReplaceCustomSearchAttributes replaces the existing custom search attribute fields with the provided ones. If `customSearchAttributes` is empty, the underlying search attributes node is deleted.

VisibilityMemoProvider if implemented by the root Component, allows the CHASM framework to automatically determine, at the end of a transaction, if a visibility task needs to be generated to update the visibility record with the returned memo.

type VisibilitySearchAttributesMapper struct {
	
}

VisibilitySearchAttributesMapper is a mapper for CHASM search attributes.

NewTestVisibilitySearchAttributesMapper creates a new VisibilitySearchAttributesMapper. For testing only.

Alias returns the alias for a given field.

Field returns the field for a given alias.

SATypeMap returns the type map for the CHASM search attributes.

ValueType returns the type of a CHASM search attribute field. Returns an error if the field is not found in the type map.

type VisibilitySearchAttributesProvider interface {
 SearchAttributes([Context](https://pkg.go.dev/go.temporal.io/server@v1.30.0/chasm#Context)) []SearchAttributeKeyValue }

VisibilitySearchAttributesProvider if implemented by the root Component, allows the CHASM framework to automatically determine, at the end of a transaction, if a visibility task needs to be generated to update the visibility record with the returned search attributes.

type VisibilityValueBool [bool](https://pkg.go.dev/builtin#bool)

type VisibilityValueByteSlice [][byte](https://pkg.go.dev/builtin#byte)

type VisibilityValueFloat64 [float64](https://pkg.go.dev/builtin#float64)

type VisibilityValueInt [int](https://pkg.go.dev/builtin#int)

type VisibilityValueInt32 [int32](https://pkg.go.dev/builtin#int32)

type VisibilityValueInt64 [int64](https://pkg.go.dev/builtin#int64)

type VisibilityValueString [string](https://pkg.go.dev/builtin#string)

type VisibilityValueStringSlice [][string](https://pkg.go.dev/builtin#string)
