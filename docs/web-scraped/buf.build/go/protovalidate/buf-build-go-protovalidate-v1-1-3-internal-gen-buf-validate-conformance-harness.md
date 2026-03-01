# Source: https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness

Title: harness package - buf.build/go/protovalidate/internal/gen/buf/validate/conformance/harness - Go Packages

URL Source: https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness

Markdown Content:
*   [Constants](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#pkg-constants)
*   [Variables](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#pkg-variables)
*   [type CaseResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult)
*       *   [func (x *CaseResult) ClearGot()](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult.ClearGot)
    *   [func (x *CaseResult) ClearInput()](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult.ClearInput)
    *   [func (x *CaseResult) ClearWanted()](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult.ClearWanted)
    *   [func (x *CaseResult) GetExpectedFailure() bool](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult.GetExpectedFailure)
    *   [func (x *CaseResult) GetGot() *TestResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult.GetGot)
    *   [func (x *CaseResult) GetInput() *anypb.Any](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult.GetInput)
    *   [func (x *CaseResult) GetName() string](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult.GetName)
    *   [func (x *CaseResult) GetSuccess() bool](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult.GetSuccess)
    *   [func (x *CaseResult) GetWanted() *TestResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult.GetWanted)
    *   [func (x *CaseResult) HasGot() bool](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult.HasGot)
    *   [func (x *CaseResult) HasInput() bool](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult.HasInput)
    *   [func (x *CaseResult) HasWanted() bool](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult.HasWanted)
    *   [func (*CaseResult) ProtoMessage()](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult.ProtoMessage)
    *   [func (x *CaseResult) ProtoReflect() protoreflect.Message](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult.ProtoReflect)
    *   [func (x *CaseResult) Reset()](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult.Reset)
    *   [func (x *CaseResult) SetExpectedFailure(v bool)](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult.SetExpectedFailure)
    *   [func (x *CaseResult) SetGot(v *TestResult)](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult.SetGot)
    *   [func (x *CaseResult) SetInput(v *anypb.Any)](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult.SetInput)
    *   [func (x *CaseResult) SetName(v string)](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult.SetName)
    *   [func (x *CaseResult) SetSuccess(v bool)](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult.SetSuccess)
    *   [func (x *CaseResult) SetWanted(v *TestResult)](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult.SetWanted)
    *   [func (x *CaseResult) String() string](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult.String)

*   [type CaseResult_builder](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult_builder)
*       *   [func (b0 CaseResult_builder) Build() *CaseResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult_builder.Build)

*   [type ResultOptions](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultOptions)
*       *   [func (x *ResultOptions) GetCaseFilter() string](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultOptions.GetCaseFilter)
    *   [func (x *ResultOptions) GetStrictError() bool](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultOptions.GetStrictError)
    *   [func (x *ResultOptions) GetStrictMessage() bool](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultOptions.GetStrictMessage)
    *   [func (x *ResultOptions) GetSuiteFilter() string](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultOptions.GetSuiteFilter)
    *   [func (x *ResultOptions) GetVerbose() bool](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultOptions.GetVerbose)
    *   [func (*ResultOptions) ProtoMessage()](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultOptions.ProtoMessage)
    *   [func (x *ResultOptions) ProtoReflect() protoreflect.Message](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultOptions.ProtoReflect)
    *   [func (x *ResultOptions) Reset()](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultOptions.Reset)
    *   [func (x *ResultOptions) SetCaseFilter(v string)](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultOptions.SetCaseFilter)
    *   [func (x *ResultOptions) SetStrictError(v bool)](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultOptions.SetStrictError)
    *   [func (x *ResultOptions) SetStrictMessage(v bool)](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultOptions.SetStrictMessage)
    *   [func (x *ResultOptions) SetSuiteFilter(v string)](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultOptions.SetSuiteFilter)
    *   [func (x *ResultOptions) SetVerbose(v bool)](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultOptions.SetVerbose)
    *   [func (x *ResultOptions) String() string](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultOptions.String)

*   [type ResultOptions_builder](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultOptions_builder)
*       *   [func (b0 ResultOptions_builder) Build() *ResultOptions](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultOptions_builder.Build)

*   [type ResultSet](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultSet)
*       *   [func (x *ResultSet) ClearOptions()](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultSet.ClearOptions)
    *   [func (x *ResultSet) GetExpectedFailures() int32](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultSet.GetExpectedFailures)
    *   [func (x *ResultSet) GetFailures() int32](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultSet.GetFailures)
    *   [func (x *ResultSet) GetOptions() *ResultOptions](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultSet.GetOptions)
    *   [func (x *ResultSet) GetSuccesses() int32](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultSet.GetSuccesses)
    *   [func (x *ResultSet) GetSuites() []*SuiteResults](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultSet.GetSuites)
    *   [func (x *ResultSet) HasOptions() bool](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultSet.HasOptions)
    *   [func (*ResultSet) ProtoMessage()](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultSet.ProtoMessage)
    *   [func (x *ResultSet) ProtoReflect() protoreflect.Message](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultSet.ProtoReflect)
    *   [func (x *ResultSet) Reset()](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultSet.Reset)
    *   [func (x *ResultSet) SetExpectedFailures(v int32)](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultSet.SetExpectedFailures)
    *   [func (x *ResultSet) SetFailures(v int32)](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultSet.SetFailures)
    *   [func (x *ResultSet) SetOptions(v *ResultOptions)](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultSet.SetOptions)
    *   [func (x *ResultSet) SetSuccesses(v int32)](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultSet.SetSuccesses)
    *   [func (x *ResultSet) SetSuites(v []*SuiteResults)](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultSet.SetSuites)
    *   [func (x *ResultSet) String() string](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultSet.String)

*   [type ResultSet_builder](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultSet_builder)
*       *   [func (b0 ResultSet_builder) Build() *ResultSet](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultSet_builder.Build)

*   [type SuiteResults](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#SuiteResults)
*       *   [func (x *SuiteResults) ClearFdset()](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#SuiteResults.ClearFdset)
    *   [func (x *SuiteResults) GetCases() []*CaseResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#SuiteResults.GetCases)
    *   [func (x *SuiteResults) GetExpectedFailures() int32](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#SuiteResults.GetExpectedFailures)
    *   [func (x *SuiteResults) GetFailures() int32](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#SuiteResults.GetFailures)
    *   [func (x *SuiteResults) GetFdset() *descriptorpb.FileDescriptorSet](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#SuiteResults.GetFdset)
    *   [func (x *SuiteResults) GetName() string](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#SuiteResults.GetName)
    *   [func (x *SuiteResults) GetSuccesses() int32](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#SuiteResults.GetSuccesses)
    *   [func (x *SuiteResults) HasFdset() bool](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#SuiteResults.HasFdset)
    *   [func (*SuiteResults) ProtoMessage()](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#SuiteResults.ProtoMessage)
    *   [func (x *SuiteResults) ProtoReflect() protoreflect.Message](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#SuiteResults.ProtoReflect)
    *   [func (x *SuiteResults) Reset()](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#SuiteResults.Reset)
    *   [func (x *SuiteResults) SetCases(v []*CaseResult)](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#SuiteResults.SetCases)
    *   [func (x *SuiteResults) SetExpectedFailures(v int32)](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#SuiteResults.SetExpectedFailures)
    *   [func (x *SuiteResults) SetFailures(v int32)](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#SuiteResults.SetFailures)
    *   [func (x *SuiteResults) SetFdset(v *descriptorpb.FileDescriptorSet)](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#SuiteResults.SetFdset)
    *   [func (x *SuiteResults) SetName(v string)](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#SuiteResults.SetName)
    *   [func (x *SuiteResults) SetSuccesses(v int32)](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#SuiteResults.SetSuccesses)
    *   [func (x *SuiteResults) String() string](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#SuiteResults.String)

*   [type SuiteResults_builder](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#SuiteResults_builder)
*       *   [func (b0 SuiteResults_builder) Build() *SuiteResults](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#SuiteResults_builder.Build)

*   [type TestConformanceRequest](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestConformanceRequest)
*       *   [func (x *TestConformanceRequest) ClearFdset()](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestConformanceRequest.ClearFdset)
    *   [func (x *TestConformanceRequest) GetCases() map[string]*anypb.Any](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestConformanceRequest.GetCases)
    *   [func (x *TestConformanceRequest) GetFdset() *descriptorpb.FileDescriptorSet](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestConformanceRequest.GetFdset)
    *   [func (x *TestConformanceRequest) HasFdset() bool](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestConformanceRequest.HasFdset)
    *   [func (*TestConformanceRequest) ProtoMessage()](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestConformanceRequest.ProtoMessage)
    *   [func (x *TestConformanceRequest) ProtoReflect() protoreflect.Message](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestConformanceRequest.ProtoReflect)
    *   [func (x *TestConformanceRequest) Reset()](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestConformanceRequest.Reset)
    *   [func (x *TestConformanceRequest) SetCases(v map[string]*anypb.Any)](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestConformanceRequest.SetCases)
    *   [func (x *TestConformanceRequest) SetFdset(v *descriptorpb.FileDescriptorSet)](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestConformanceRequest.SetFdset)
    *   [func (x *TestConformanceRequest) String() string](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestConformanceRequest.String)

*   [type TestConformanceRequest_builder](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestConformanceRequest_builder)
*       *   [func (b0 TestConformanceRequest_builder) Build() *TestConformanceRequest](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestConformanceRequest_builder.Build)

*   [type TestConformanceResponse](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestConformanceResponse)
*       *   [func (x *TestConformanceResponse) GetResults() map[string]*TestResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestConformanceResponse.GetResults)
    *   [func (*TestConformanceResponse) ProtoMessage()](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestConformanceResponse.ProtoMessage)
    *   [func (x *TestConformanceResponse) ProtoReflect() protoreflect.Message](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestConformanceResponse.ProtoReflect)
    *   [func (x *TestConformanceResponse) Reset()](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestConformanceResponse.Reset)
    *   [func (x *TestConformanceResponse) SetResults(v map[string]*TestResult)](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestConformanceResponse.SetResults)
    *   [func (x *TestConformanceResponse) String() string](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestConformanceResponse.String)

*   [type TestConformanceResponse_builder](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestConformanceResponse_builder)
*       *   [func (b0 TestConformanceResponse_builder) Build() *TestConformanceResponse](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestConformanceResponse_builder.Build)

*   [type TestResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult)
*       *   [func (x *TestResult) ClearCompilationError()](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult.ClearCompilationError)
    *   [func (x *TestResult) ClearResult()](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult.ClearResult)
    *   [func (x *TestResult) ClearRuntimeError()](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult.ClearRuntimeError)
    *   [func (x *TestResult) ClearSuccess()](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult.ClearSuccess)
    *   [func (x *TestResult) ClearUnexpectedError()](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult.ClearUnexpectedError)
    *   [func (x *TestResult) ClearValidationError()](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult.ClearValidationError)
    *   [func (x *TestResult) GetCompilationError() string](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult.GetCompilationError)
    *   [func (x *TestResult) GetResult() isTestResult_Result](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult.GetResult)
    *   [func (x *TestResult) GetRuntimeError() string](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult.GetRuntimeError)
    *   [func (x *TestResult) GetSuccess() bool](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult.GetSuccess)
    *   [func (x *TestResult) GetUnexpectedError() string](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult.GetUnexpectedError)
    *   [func (x *TestResult) GetValidationError() *validate.Violations](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult.GetValidationError)
    *   [func (x *TestResult) HasCompilationError() bool](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult.HasCompilationError)
    *   [func (x *TestResult) HasResult() bool](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult.HasResult)
    *   [func (x *TestResult) HasRuntimeError() bool](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult.HasRuntimeError)
    *   [func (x *TestResult) HasSuccess() bool](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult.HasSuccess)
    *   [func (x *TestResult) HasUnexpectedError() bool](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult.HasUnexpectedError)
    *   [func (x *TestResult) HasValidationError() bool](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult.HasValidationError)
    *   [func (*TestResult) ProtoMessage()](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult.ProtoMessage)
    *   [func (x *TestResult) ProtoReflect() protoreflect.Message](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult.ProtoReflect)
    *   [func (x *TestResult) Reset()](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult.Reset)
    *   [func (x *TestResult) SetCompilationError(v string)](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult.SetCompilationError)
    *   [func (x *TestResult) SetRuntimeError(v string)](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult.SetRuntimeError)
    *   [func (x *TestResult) SetSuccess(v bool)](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult.SetSuccess)
    *   [func (x *TestResult) SetUnexpectedError(v string)](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult.SetUnexpectedError)
    *   [func (x *TestResult) SetValidationError(v *validate.Violations)](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult.SetValidationError)
    *   [func (x *TestResult) String() string](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult.String)
    *   [func (x *TestResult) WhichResult() case_TestResult_Result](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult.WhichResult)

*   [type TestResult_CompilationError](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult_CompilationError)
*   [type TestResult_RuntimeError](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult_RuntimeError)
*   [type TestResult_Success](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult_Success)
*   [type TestResult_UnexpectedError](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult_UnexpectedError)
*   [type TestResult_ValidationError](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult_ValidationError)
*   [type TestResult_builder](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult_builder)
*       *   [func (b0 TestResult_builder) Build() *TestResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult_builder.Build)

[View Source](https://github.com/bufbuild/protovalidate-go/blob/v1.1.3/internal/gen/buf/validate/conformance/harness/harness.pb.go#L386)

const TestResult_CompilationError_case case_TestResult_Result = 3

[View Source](https://github.com/bufbuild/protovalidate-go/blob/v1.1.3/internal/gen/buf/validate/conformance/harness/harness.pb.go#L383)

const TestResult_Result_not_set_case case_TestResult_Result = 0

[View Source](https://github.com/bufbuild/protovalidate-go/blob/v1.1.3/internal/gen/buf/validate/conformance/harness/harness.pb.go#L387)

const TestResult_RuntimeError_case case_TestResult_Result = 4

[View Source](https://github.com/bufbuild/protovalidate-go/blob/v1.1.3/internal/gen/buf/validate/conformance/harness/harness.pb.go#L384)

const TestResult_Success_case case_TestResult_Result = 1

[View Source](https://github.com/bufbuild/protovalidate-go/blob/v1.1.3/internal/gen/buf/validate/conformance/harness/harness.pb.go#L388)

const TestResult_UnexpectedError_case case_TestResult_Result = 5

[View Source](https://github.com/bufbuild/protovalidate-go/blob/v1.1.3/internal/gen/buf/validate/conformance/harness/harness.pb.go#L385)

const TestResult_ValidationError_case case_TestResult_Result = 2

This section is empty.

type CaseResult struct {

	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
	Success [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,2,opt,name=success,proto3" json:"success,omitempty"`
	Wanted *[TestResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult) `protobuf:"bytes,3,opt,name=wanted,proto3" json:"wanted,omitempty"`
	Got *[TestResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult) `protobuf:"bytes,4,opt,name=got,proto3" json:"got,omitempty"`
	Input *[anypb](https://pkg.go.dev/google.golang.org/protobuf/types/known/anypb).[Any](https://pkg.go.dev/google.golang.org/protobuf/types/known/anypb#Any) `protobuf:"bytes,5,opt,name=input,proto3" json:"input,omitempty"`
	ExpectedFailure [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,6,opt,name=expected_failure,json=expectedFailure,proto3" json:"expected_failure,omitempty"`
	
}

A case result is a single test case result.

func (x *[CaseResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult)) ClearGot()

func (x *[CaseResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult)) ClearInput()

func (x *[CaseResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult)) ClearWanted()

func (x *[CaseResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult)) GetExpectedFailure() [bool](https://pkg.go.dev/builtin#bool)

func (x *[CaseResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult)) GetGot() *[TestResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult)

func (x *[CaseResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult)) GetSuccess() [bool](https://pkg.go.dev/builtin#bool)

func (x *[CaseResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult)) GetWanted() *[TestResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult)

func (x *[CaseResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult)) HasInput() [bool](https://pkg.go.dev/builtin#bool)

func (x *[CaseResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult)) HasWanted() [bool](https://pkg.go.dev/builtin#bool)

func (*[CaseResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult)) ProtoMessage()

func (x *[CaseResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult)) Reset()

func (x *[CaseResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult)) SetExpectedFailure(v [bool](https://pkg.go.dev/builtin#bool))

func (x *[CaseResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult)) SetGot(v *[TestResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult))

func (x *[CaseResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult)) SetSuccess(v [bool](https://pkg.go.dev/builtin#bool))

func (x *[CaseResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult)) SetWanted(v *[TestResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult))

func (b0 [CaseResult_builder](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult_builder)) Build() *[CaseResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult)

type ResultOptions struct {

	SuiteFilter [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=suite_filter,json=suiteFilter,proto3" json:"suite_filter,omitempty"`
	CaseFilter [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,2,opt,name=case_filter,json=caseFilter,proto3" json:"case_filter,omitempty"`
	Verbose [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,3,opt,name=verbose,proto3" json:"verbose,omitempty"`
	StrictMessage [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,5,opt,name=strict_message,json=strictMessage,proto3" json:"strict_message,omitempty"`
	StrictError [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,6,opt,name=strict_error,json=strictError,proto3" json:"strict_error,omitempty"`
	
}

ResultOptions are the options passed to the test runner to configure the test run.

func (x *[ResultOptions](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultOptions)) GetStrictError() [bool](https://pkg.go.dev/builtin#bool)

func (x *[ResultOptions](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultOptions)) GetStrictMessage() [bool](https://pkg.go.dev/builtin#bool)

func (x *[ResultOptions](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultOptions)) GetVerbose() [bool](https://pkg.go.dev/builtin#bool)

func (*[ResultOptions](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultOptions)) ProtoMessage()

func (x *[ResultOptions](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultOptions)) Reset()

func (x *[ResultOptions](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultOptions)) SetStrictError(v [bool](https://pkg.go.dev/builtin#bool))

func (x *[ResultOptions](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultOptions)) SetStrictMessage(v [bool](https://pkg.go.dev/builtin#bool))

func (x *[ResultOptions](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultOptions)) SetVerbose(v [bool](https://pkg.go.dev/builtin#bool))

type ResultOptions_builder struct {

	SuiteFilter [string](https://pkg.go.dev/builtin#string)
	CaseFilter [string](https://pkg.go.dev/builtin#string)
	Verbose [bool](https://pkg.go.dev/builtin#bool)
	StrictMessage [bool](https://pkg.go.dev/builtin#bool)
	StrictError [bool](https://pkg.go.dev/builtin#bool)
	
}

func (b0 [ResultOptions_builder](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultOptions_builder)) Build() *[ResultOptions](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultOptions)

type ResultSet struct {

	Successes [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,1,opt,name=successes,proto3" json:"successes,omitempty"`
	Failures [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=failures,proto3" json:"failures,omitempty"`
	Suites []*[SuiteResults](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#SuiteResults) `protobuf:"bytes,3,rep,name=suites,proto3" json:"suites,omitempty"`
	Options *[ResultOptions](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultOptions) `protobuf:"bytes,4,opt,name=options,proto3" json:"options,omitempty"`
	ExpectedFailures [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,5,opt,name=expected_failures,json=expectedFailures,proto3" json:"expected_failures,omitempty"`
	
}

A result is the result of a test run.

func (x *[ResultSet](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultSet)) ClearOptions()

func (x *[ResultSet](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultSet)) GetExpectedFailures() [int32](https://pkg.go.dev/builtin#int32)

func (x *[ResultSet](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultSet)) GetFailures() [int32](https://pkg.go.dev/builtin#int32)

func (x *[ResultSet](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultSet)) GetOptions() *[ResultOptions](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultOptions)

func (x *[ResultSet](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultSet)) GetSuccesses() [int32](https://pkg.go.dev/builtin#int32)

func (x *[ResultSet](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultSet)) GetSuites() []*[SuiteResults](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#SuiteResults)

func (x *[ResultSet](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultSet)) HasOptions() [bool](https://pkg.go.dev/builtin#bool)

func (*[ResultSet](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultSet)) ProtoMessage()

func (x *[ResultSet](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultSet)) Reset()

func (x *[ResultSet](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultSet)) SetExpectedFailures(v [int32](https://pkg.go.dev/builtin#int32))

func (x *[ResultSet](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultSet)) SetFailures(v [int32](https://pkg.go.dev/builtin#int32))

func (x *[ResultSet](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultSet)) SetOptions(v *[ResultOptions](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultOptions))

func (x *[ResultSet](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultSet)) SetSuccesses(v [int32](https://pkg.go.dev/builtin#int32))

func (x *[ResultSet](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultSet)) SetSuites(v []*[SuiteResults](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#SuiteResults))

type ResultSet_builder struct {

	Successes [int32](https://pkg.go.dev/builtin#int32)
	Failures [int32](https://pkg.go.dev/builtin#int32)
	Suites []*[SuiteResults](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#SuiteResults)
	Options *[ResultOptions](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultOptions)
	ExpectedFailures [int32](https://pkg.go.dev/builtin#int32)
	
}

func (b0 [ResultSet_builder](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultSet_builder)) Build() *[ResultSet](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#ResultSet)

type SuiteResults struct {

	Name [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,1,opt,name=name,proto3" json:"name,omitempty"`
	Successes [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,2,opt,name=successes,proto3" json:"successes,omitempty"`
	Failures [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,3,opt,name=failures,proto3" json:"failures,omitempty"`
	Cases []*[CaseResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult) `protobuf:"bytes,4,rep,name=cases,proto3" json:"cases,omitempty"`
	Fdset *[descriptorpb](https://pkg.go.dev/google.golang.org/protobuf/types/descriptorpb).[FileDescriptorSet](https://pkg.go.dev/google.golang.org/protobuf/types/descriptorpb#FileDescriptorSet) `protobuf:"bytes,5,opt,name=fdset,proto3" json:"fdset,omitempty"`
	ExpectedFailures [int32](https://pkg.go.dev/builtin#int32) `protobuf:"varint,6,opt,name=expected_failures,json=expectedFailures,proto3" json:"expected_failures,omitempty"`
	
}

A suite result is a single test suite result.

func (x *[SuiteResults](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#SuiteResults)) ClearFdset()

func (x *[SuiteResults](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#SuiteResults)) GetCases() []*[CaseResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult)

func (x *[SuiteResults](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#SuiteResults)) GetExpectedFailures() [int32](https://pkg.go.dev/builtin#int32)

func (x *[SuiteResults](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#SuiteResults)) GetSuccesses() [int32](https://pkg.go.dev/builtin#int32)

func (x *[SuiteResults](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#SuiteResults)) HasFdset() [bool](https://pkg.go.dev/builtin#bool)

func (*[SuiteResults](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#SuiteResults)) ProtoMessage()

func (x *[SuiteResults](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#SuiteResults)) Reset()

func (x *[SuiteResults](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#SuiteResults)) SetCases(v []*[CaseResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#CaseResult))

func (x *[SuiteResults](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#SuiteResults)) SetExpectedFailures(v [int32](https://pkg.go.dev/builtin#int32))

func (x *[SuiteResults](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#SuiteResults)) SetFailures(v [int32](https://pkg.go.dev/builtin#int32))

func (x *[SuiteResults](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#SuiteResults)) SetSuccesses(v [int32](https://pkg.go.dev/builtin#int32))

func (b0 [SuiteResults_builder](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#SuiteResults_builder)) Build() *[SuiteResults](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#SuiteResults)

TestConformanceRequest is the request for Conformance Tests. The FileDescriptorSet is the FileDescriptorSet to test against. The cases map is a map of case name to the Any message that represents the case.

func (x *[TestConformanceRequest](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestConformanceRequest)) ClearFdset()

func (*[TestConformanceRequest](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestConformanceRequest)) ProtoMessage()

func (x *[TestConformanceRequest](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestConformanceRequest)) Reset()

type TestConformanceResponse struct {
 Results map[[string](https://pkg.go.dev/builtin#string)]*[TestResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult) `` 	
}

TestConformanceResponse is the response for Conformance Tests. The results map is a map of case name to the TestResult.

func (*[TestConformanceResponse](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestConformanceResponse)) ProtoMessage()

func (x *[TestConformanceResponse](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestConformanceResponse)) Reset()

type TestConformanceResponse_builder struct {
 Results map[[string](https://pkg.go.dev/builtin#string)]*[TestResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult)	
}

type TestResult struct {

	
	
	
	
	
	
	Result isTestResult_Result `protobuf_oneof:"result"`
	
}

TestResult is the result of a single test. Only one of the fields will be set.

func (x *[TestResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult)) ClearCompilationError()

func (x *[TestResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult)) ClearResult()

func (x *[TestResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult)) ClearRuntimeError()

func (x *[TestResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult)) ClearSuccess()

func (x *[TestResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult)) ClearUnexpectedError()

func (x *[TestResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult)) ClearValidationError()

func (x *[TestResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult)) GetCompilationError() [string](https://pkg.go.dev/builtin#string)

func (x *[TestResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult)) GetResult() isTestResult_Result

func (x *[TestResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult)) GetRuntimeError() [string](https://pkg.go.dev/builtin#string)

func (x *[TestResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult)) GetSuccess() [bool](https://pkg.go.dev/builtin#bool)

func (x *[TestResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult)) GetUnexpectedError() [string](https://pkg.go.dev/builtin#string)

func (x *[TestResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult)) HasCompilationError() [bool](https://pkg.go.dev/builtin#bool)

func (x *[TestResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult)) HasResult() [bool](https://pkg.go.dev/builtin#bool)

func (x *[TestResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult)) HasRuntimeError() [bool](https://pkg.go.dev/builtin#bool)

func (x *[TestResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult)) HasSuccess() [bool](https://pkg.go.dev/builtin#bool)

func (x *[TestResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult)) HasUnexpectedError() [bool](https://pkg.go.dev/builtin#bool)

func (x *[TestResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult)) HasValidationError() [bool](https://pkg.go.dev/builtin#bool)

func (*[TestResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult)) ProtoMessage()

func (x *[TestResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult)) Reset()

func (x *[TestResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult)) SetCompilationError(v [string](https://pkg.go.dev/builtin#string))

func (x *[TestResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult)) SetRuntimeError(v [string](https://pkg.go.dev/builtin#string))

func (x *[TestResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult)) SetSuccess(v [bool](https://pkg.go.dev/builtin#bool))

func (x *[TestResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult)) SetUnexpectedError(v [string](https://pkg.go.dev/builtin#string))

func (x *[TestResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult)) WhichResult() case_TestResult_Result

type TestResult_CompilationError struct {
	CompilationError [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,3,opt,name=compilation_error,json=compilationError,proto3,oneof"`
}

type TestResult_RuntimeError struct {
	RuntimeError [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,4,opt,name=runtime_error,json=runtimeError,proto3,oneof"`
}

type TestResult_Success struct {
	Success [bool](https://pkg.go.dev/builtin#bool) `protobuf:"varint,1,opt,name=success,proto3,oneof"`
}

type TestResult_UnexpectedError struct {
	UnexpectedError [string](https://pkg.go.dev/builtin#string) `protobuf:"bytes,5,opt,name=unexpected_error,json=unexpectedError,proto3,oneof"`
}

type TestResult_ValidationError struct {
	ValidationError *[validate](https://pkg.go.dev/buf.build/gen/go/bufbuild/protovalidate/protocolbuffers/go/buf/validate).[Violations](https://pkg.go.dev/buf.build/gen/go/bufbuild/protovalidate/protocolbuffers/go/buf/validate#Violations) `protobuf:"bytes,2,opt,name=validation_error,json=validationError,proto3,oneof"`
}

func (b0 [TestResult_builder](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult_builder)) Build() *[TestResult](https://pkg.go.dev/buf.build/go/protovalidate@v1.1.3/internal/gen/buf/validate/conformance/harness#TestResult)
