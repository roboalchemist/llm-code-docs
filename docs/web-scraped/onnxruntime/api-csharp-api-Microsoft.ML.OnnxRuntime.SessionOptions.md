# Source: https://onnxruntime.ai/docs/api/csharp/api/Microsoft.ML.OnnxRuntime.SessionOptions.html

[Show / Hide Table of Contents](#sidetoggle)

# Class SessionOptions 

Holds the options for creating an InferenceSession It forces the instantiation of the OrtEnv singleton.

##### Inheritance

[object](https://learn.microsoft.com/dotnet/api/system.object)

[CriticalFinalizerObject](https://learn.microsoft.com/dotnet/api/system.runtime.constrainedexecution.criticalfinalizerobject)

[SafeHandle](https://learn.microsoft.com/dotnet/api/system.runtime.interopservices.safehandle)

[SessionOptions]

##### Implements

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

##### Inherited Members

[SafeHandle.handle](https://learn.microsoft.com/dotnet/api/system.runtime.interopservices.safehandle.handle)

[SafeHandle.Close()](https://learn.microsoft.com/dotnet/api/system.runtime.interopservices.safehandle.close)

[SafeHandle.DangerousAddRef(ref bool)](https://learn.microsoft.com/dotnet/api/system.runtime.interopservices.safehandle.dangerousaddref)

[SafeHandle.DangerousGetHandle()](https://learn.microsoft.com/dotnet/api/system.runtime.interopservices.safehandle.dangerousgethandle)

[SafeHandle.DangerousRelease()](https://learn.microsoft.com/dotnet/api/system.runtime.interopservices.safehandle.dangerousrelease)

[SafeHandle.Dispose()](https://learn.microsoft.com/dotnet/api/system.runtime.interopservices.safehandle.dispose#system-runtime-interopservices-safehandle-dispose)

[SafeHandle.Dispose(bool)](https://learn.microsoft.com/dotnet/api/system.runtime.interopservices.safehandle.dispose#system-runtime-interopservices-safehandle-dispose(system-boolean))

[SafeHandle.SetHandle(nint)](https://learn.microsoft.com/dotnet/api/system.runtime.interopservices.safehandle.sethandle)

[SafeHandle.SetHandleAsInvalid()](https://learn.microsoft.com/dotnet/api/system.runtime.interopservices.safehandle.sethandleasinvalid)

[SafeHandle.IsClosed](https://learn.microsoft.com/dotnet/api/system.runtime.interopservices.safehandle.isclosed)

[object.Equals(object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals(system-object))

[object.Equals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.equals#system-object-equals(system-object-system-object))

[object.GetHashCode()](https://learn.microsoft.com/dotnet/api/system.object.gethashcode)

[object.GetType()](https://learn.microsoft.com/dotnet/api/system.object.gettype)

[object.MemberwiseClone()](https://learn.microsoft.com/dotnet/api/system.object.memberwiseclone)

[object.ReferenceEquals(object, object)](https://learn.microsoft.com/dotnet/api/system.object.referenceequals)

[object.ToString()](https://learn.microsoft.com/dotnet/api/system.object.tostring)

###### **Namespace**: [Microsoft](Microsoft.html).[ML](Microsoft.ML.html).[OnnxRuntime](Microsoft.ML.OnnxRuntime.html)

###### **Assembly**: Microsoft.ML.OnnxRuntime.dll

##### Syntax 

``` 
public class SessionOptions : SafeHandle, IDisposable
```

### Constructors

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions__ctor.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.%23ctor%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L66) ] []

#### SessionOptions() 

Constructs an empty SessionOptions

##### Declaration 

``` 
public SessionOptions()
```

### Properties

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_EnableCpuMemArena.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.EnableCpuMemArena%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L768) ] []

#### EnableCpuMemArena 

Enables Arena allocator for the CPU memory allocations. Default is true.

##### Declaration 

``` 
public bool EnableCpuMemArena 
```

##### Property Value 

  Type                                                                   Description
  ---------------------------------------------------------------------- ----------------------------------------
  [bool](https://learn.microsoft.com/dotnet/api/system.boolean)   returns \_enableCpuMemArena flag value

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_EnableMemoryPattern.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.EnableMemoryPattern%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L687) ] []

#### EnableMemoryPattern 

Enables the use of the memory allocation patterns in the first Run() call for subsequent runs. Default = true.

##### Declaration 

``` 
public bool EnableMemoryPattern 
```

##### Property Value 

  Type                                                                   Description
  ---------------------------------------------------------------------- ----------------------------------------
  [bool](https://learn.microsoft.com/dotnet/api/system.boolean)   returns enableMemoryPattern flag value

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_EnableProfiling.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.EnableProfiling%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L721) ] []

#### EnableProfiling 

Enables profiling of InferenceSession.Run() calls. Default is false

##### Declaration 

``` 
public bool EnableProfiling 
```

##### Property Value 

  Type                                                                   Description
  ---------------------------------------------------------------------- --------------------------------------
  [bool](https://learn.microsoft.com/dotnet/api/system.boolean)   returns \_enableProfiling flag value

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_ExecutionMode.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.ExecutionMode%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L918) ] []

#### ExecutionMode 

Sets the execution mode for the session. Default is set to ORT_SEQUENTIAL. See \[ONNX_Runtime_Perf_Tuning.md\] for more details.

##### Declaration 

``` 
public ExecutionMode ExecutionMode 
```

##### Property Value 

  Type                                                                  Description
  --------------------------------------------------------------------- -------------------------------
  [ExecutionMode](Microsoft.ML.OnnxRuntime.ExecutionMode.html)   returns \_executionMode value

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_GraphOptimizationLevel.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.GraphOptimizationLevel%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L899) ] []

#### GraphOptimizationLevel 

Sets the graph optimization level for the session. Default is set to ORT_ENABLE_ALL.

##### Declaration 

``` 
public GraphOptimizationLevel GraphOptimizationLevel 
```

##### Property Value 

  Type                                                                                    Description
  --------------------------------------------------------------------------------------- ----------------------------------------
  [GraphOptimizationLevel](Microsoft.ML.OnnxRuntime.GraphOptimizationLevel.html)   returns \_graphOptimizationLevel value

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_InterOpNumThreads.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.InterOpNumThreads%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L881) ] []

#### InterOpNumThreads 

Sets the number of threads used to parallelize the execution of the graph (across nodes) If sequential execution is enabled this value is ignored A value of 0 means ORT will pick a default

##### Declaration 

``` 
public int InterOpNumThreads 
```

##### Property Value 

  Type                                                                Description
  ------------------------------------------------------------------- -----------------------------------
  [int](https://learn.microsoft.com/dotnet/api/system.int32)   returns \_interOpNumThreads value

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_IntraOpNumThreads.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.IntraOpNumThreads%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L861) ] []

#### IntraOpNumThreads 

Sets the number of threads used to parallelize the execution within nodes A value of 0 means ORT will pick a default

##### Declaration 

``` 
public int IntraOpNumThreads 
```

##### Property Value 

  Type                                                                Description
  ------------------------------------------------------------------- -----------------------------------
  [int](https://learn.microsoft.com/dotnet/api/system.int32)   returns \_intraOpNumThreads value

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_IsInvalid.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.IsInvalid%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L681) ] []

#### IsInvalid 

Overrides SafeHandle.IsInvalid

##### Declaration 

``` 
public override bool IsInvalid 
```

##### Property Value 

  Type                                                                   Description
  ---------------------------------------------------------------------- -----------------------------------------
  [bool](https://learn.microsoft.com/dotnet/api/system.boolean)   returns true if handle is equal to Zero

##### Overrides 

[SafeHandle.IsInvalid](https://learn.microsoft.com/dotnet/api/system.runtime.interopservices.safehandle.isinvalid)

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_LogId.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.LogId%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L803) ] []

#### LogId 

Log Id to be used for the session. Default is empty string.

##### Declaration 

``` 
public string LogId 
```

##### Property Value 

  Type                                                                    Description
  ----------------------------------------------------------------------- -----------------------
  [string](https://learn.microsoft.com/dotnet/api/system.string)   returns \_logId value

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_LogSeverityLevel.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.LogSeverityLevel%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L823) ] []

#### LogSeverityLevel 

Log Severity Level for the session logs. Default = ORT_LOGGING_LEVEL_WARNING

##### Declaration 

``` 
public OrtLoggingLevel LogSeverityLevel 
```

##### Property Value 

  Type                                                                      Description
  ------------------------------------------------------------------------- ----------------------------------
  [OrtLoggingLevel](Microsoft.ML.OnnxRuntime.OrtLoggingLevel.html)   returns \_logSeverityLevel value

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_LogVerbosityLevel.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.LogVerbosityLevel%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L842) ] []

#### LogVerbosityLevel 

Log Verbosity Level for the session logs. Default = 0. Valid values are \>=0. This takes into effect only when the LogSeverityLevel is set to ORT_LOGGING_LEVEL_VERBOSE.

##### Declaration 

``` 
public int LogVerbosityLevel 
```

##### Property Value 

  Type                                                                Description
  ------------------------------------------------------------------- -----------------------------------
  [int](https://learn.microsoft.com/dotnet/api/system.int32)   returns \_logVerbosityLevel value

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_OptimizedModelFilePath.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.OptimizedModelFilePath%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L747) ] []

#### OptimizedModelFilePath 

Set filepath to save optimized model after graph level transformations. Default is empty, which implies saving is disabled.

##### Declaration 

``` 
public string OptimizedModelFilePath 
```

##### Property Value 

  Type                                                                    Description
  ----------------------------------------------------------------------- ---------------------------------------------
  [string](https://learn.microsoft.com/dotnet/api/system.string)   returns \_optimizedModelFilePath flag value

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_ProfileOutputPathPrefix.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.ProfileOutputPathPrefix%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L712) ] []

#### ProfileOutputPathPrefix 

Path prefix to use for output of profiling data

##### Declaration 

``` 
public string ProfileOutputPathPrefix 
```

##### Property Value 

  Type                                                                    Description
  ----------------------------------------------------------------------- -------------
  [string](https://learn.microsoft.com/dotnet/api/system.string)   

### Methods

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_AddFreeDimensionOverride_System_String_System_Int64_.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.AddFreeDimensionOverride(System.String%2CSystem.Int64)%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L614) ] []

#### AddFreeDimensionOverride(string, long) 

Override symbolic dimensions (by specific denotation strings) with actual values if known at session initialization time to enable optimizations that can take advantage of fixed values (such as memory planning, etc)

##### Declaration 

``` 
public void AddFreeDimensionOverride(string dimDenotation, long dimValue)
```

##### Parameters 

  Type                                                                    Name                              Description
  ----------------------------------------------------------------------- --------------------------------- ------------------
  [string](https://learn.microsoft.com/dotnet/api/system.string)   [dimDenotation]   denotation name
  [long](https://learn.microsoft.com/dotnet/api/system.int64)      [dimValue]        denotation value

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_AddFreeDimensionOverrideByName_System_String_System_Int64_.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.AddFreeDimensionOverrideByName(System.String%2CSystem.Int64)%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L626) ] []

#### AddFreeDimensionOverrideByName(string, long) 

Override symbolic dimensions (by specific name strings) with actual values if known at session initialization time to enable optimizations that can take advantage of fixed values (such as memory planning, etc)

##### Declaration 

``` 
public void AddFreeDimensionOverrideByName(string dimName, long dimValue)
```

##### Parameters 

  Type                                                                    Name                         Description
  ----------------------------------------------------------------------- ---------------------------- -----------------
  [string](https://learn.microsoft.com/dotnet/api/system.string)   [dimName]    dimension name
  [long](https://learn.microsoft.com/dotnet/api/system.int64)      [dimValue]   dimension value

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_AddInitializer_System_String_Microsoft_ML_OnnxRuntime_OrtValue_.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.AddInitializer(System.String%2CMicrosoft.ML.OnnxRuntime.OrtValue)%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L589) ] []

#### AddInitializer(string, OrtValue) 

Add a pre-allocated initializer to a session. If a model contains an initializer with a name that is same as the name passed to this API call, ORT will use this initializer instance instead of deserializing one from the model file. This is useful when you want to share the same initializer across sessions.

##### Declaration 

``` 
public void AddInitializer(string name, OrtValue ortValue)
```

##### Parameters 

  Type                                                                    Name                         Description
  ----------------------------------------------------------------------- ---------------------------- --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
  [string](https://learn.microsoft.com/dotnet/api/system.string)   [name]       name of the initializer
  [OrtValue](Microsoft.ML.OnnxRuntime.OrtValue.html)               [ortValue]   OrtValue containing the initializer. Lifetime of \'val\' and the underlying initializer buffer must be managed by the user (created using the CreateTensorWithDataAsOrtValue API) and it must outlive the session object

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_AddSessionConfigEntry_System_String_System_String_.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.AddSessionConfigEntry(System.String%2CSystem.String)%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L601) ] []

#### AddSessionConfigEntry(string, string) 

Set a single session configuration entry as a pair of strings If a configuration with same key exists, this will overwrite the configuration with the given configValue

##### Declaration 

``` 
public void AddSessionConfigEntry(string configKey, string configValue)
```

##### Parameters 

  Type                                                                    Name                            Description
  ----------------------------------------------------------------------- ------------------------------- ------------------
  [string](https://learn.microsoft.com/dotnet/api/system.string)   [configKey]     config key name
  [string](https://learn.microsoft.com/dotnet/api/system.string)   [configValue]   config key value

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_AppendExecutionProvider_Microsoft_ML_OnnxRuntime_OrtEnv_System_Collections_Generic_IReadOnlyList_Microsoft_ML_OnnxRuntime_OrtEpDevice__System_Collections_Generic_IReadOnlyDictionary_System_String_System_String__.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.AppendExecutionProvider(Microsoft.ML.OnnxRuntime.OrtEnv%2CSystem.Collections.Generic.IReadOnlyList%7BMicrosoft.ML.OnnxRuntime.OrtEpDevice%7D%2CSystem.Collections.Generic.IReadOnlyDictionary%7BSystem.String%2CSystem.String%7D)%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L452) ] []

#### AppendExecutionProvider(OrtEnv, IReadOnlyList\<OrtEpDevice\>, IReadOnlyDictionary\<string, string\>) ,System.Collections.Generic.IReadOnlyDictionary)"}

Select execution providers from the list of available execution providers and devices returned by GetEpDevices.

One or more OrtEpDevice instances may be provided in epDevices, but must all be for the same execution provider.

Make multiple calls to AppendExecutionProvider if you wish to use multiple execution providers.

e.g.

- if execution provider \'A\' has an OrtEpDevice for NPU and one for GPU and you wish to use it for both devices, pass the two OrtEpDevice instances in the epDevices list in one call.
- if you wish to use execution provider \'B\' for GPU and execution provider \'C\' for CPU, make two calls to AppendExecutionProvider, with one OrtEpDevice in the epDevices list in each call.

The priority of the execution providers is set by the order in which they are appended. Highest priority is first.

##### Declaration 

``` 
public void AppendExecutionProvider(OrtEnv env, IReadOnlyList<OrtEpDevice> epDevices, IReadOnlyDictionary<string, string> epOptions)
```

##### Parameters 

  Type                                                                                                                                                                                                                                                                    Name                          Description
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------- -----------------------------------------------------------------------------------------
  [OrtEnv](Microsoft.ML.OnnxRuntime.OrtEnv.html)                                                                                                                                                                                                                   [env]         OrtEnv that provided the OrtEpDevice instances via a call to GetEpDevices.
  [IReadOnlyList](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlylist-1)\<[OrtEpDevice](Microsoft.ML.OnnxRuntime.OrtEpDevice.html)\>                                                                                            [epDevices]   One or more OrtEpDevice instances to append. These must all have the save EpName value.
  [IReadOnlyDictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.ireadonlydictionary-2)\<[string](https://learn.microsoft.com/dotnet/api/system.string), [string](https://learn.microsoft.com/dotnet/api/system.string)\>   [epOptions]   Optional options to configure the execution provider. May be null.

##### Exceptions 

  Type                                                                                          Condition
  --------------------------------------------------------------------------------------------- ----------------------
  [ArgumentException](https://learn.microsoft.com/dotnet/api/system.argumentexception)   epDevices was empty.

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_AppendExecutionProvider_System_String_System_Collections_Generic_Dictionary_System_String_System_String__.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.AppendExecutionProvider(System.String%2CSystem.Collections.Generic.Dictionary%7BSystem.String%2CSystem.String%7D)%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L416) ] []

#### AppendExecutionProvider(string, Dictionary\<string, string\>) )"}

Append QNN, SNPE or XNNPACK execution provider

##### Declaration 

``` 
public void AppendExecutionProvider(string providerName, Dictionary<string, string> providerOptions = null)
```

##### Parameters 

  Type                                                                                                                                                                                                                                                  Name                                Description
  ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- ----------------------------------- ---------------------------------------------------------------------------------------------------------
  [string](https://learn.microsoft.com/dotnet/api/system.string)                                                                                                                                                                                 [providerName]      Execution provider to add. \'QNN\', \'SNPE\' \'XNNPACK\', \'CoreML and \'AZURE are currently supported.
  [Dictionary](https://learn.microsoft.com/dotnet/api/system.collections.generic.dictionary-2)\<[string](https://learn.microsoft.com/dotnet/api/system.string), [string](https://learn.microsoft.com/dotnet/api/system.string)\>   [providerOptions]   Optional key/value pairs to specify execution provider options.

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_AppendExecutionProvider_CPU_System_Int32_.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.AppendExecutionProvider_CPU(System.Int32)%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L215) ] []

#### AppendExecutionProvider_CPU(int) 

Appends CPU EP to a list of available execution providers for the session.

##### Declaration 

``` 
public void AppendExecutionProvider_CPU(int useArena = 1)
```

##### Parameters 

  Type                                                                Name                         Description
  ------------------------------------------------------------------- ---------------------------- -------------------------------------
  [int](https://learn.microsoft.com/dotnet/api/system.int32)   [useArena]   1 - use arena, 0 - do not use arena

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_AppendExecutionProvider_CUDA_Microsoft_ML_OnnxRuntime_OrtCUDAProviderOptions_.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.AppendExecutionProvider_CUDA(Microsoft.ML.OnnxRuntime.OrtCUDAProviderOptions)%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L251) ] []

#### AppendExecutionProvider_CUDA(OrtCUDAProviderOptions) 

Append a CUDA EP instance (based on specified configuration) to the SessionOptions instance. Use only if you have the onnxruntime package specific to this Execution Provider.

##### Declaration 

``` 
public void AppendExecutionProvider_CUDA(OrtCUDAProviderOptions cudaProviderOptions)
```

##### Parameters 

  Type                                                                                    Name                                    Description
  --------------------------------------------------------------------------------------- --------------------------------------- --------------------------
  [OrtCUDAProviderOptions](Microsoft.ML.OnnxRuntime.OrtCUDAProviderOptions.html)   [cudaProviderOptions]   CUDA EP provider options

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_AppendExecutionProvider_CUDA_System_Int32_.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.AppendExecutionProvider_CUDA(System.Int32)%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L237) ] []

#### AppendExecutionProvider_CUDA(int) 

Use only if you have the onnxruntime package specific to this Execution Provider.

##### Declaration 

``` 
public void AppendExecutionProvider_CUDA(int deviceId = 0)
```

##### Parameters 

  Type                                                                Name                         Description
  ------------------------------------------------------------------- ---------------------------- -------------------
  [int](https://learn.microsoft.com/dotnet/api/system.int32)   [deviceId]   integer device ID

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_AppendExecutionProvider_CoreML_Microsoft_ML_OnnxRuntime_CoreMLFlags_.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.AppendExecutionProvider_CoreML(Microsoft.ML.OnnxRuntime.CoreMLFlags)%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L374) ] []

#### AppendExecutionProvider_CoreML(CoreMLFlags) 

Use only if you have the onnxruntime package specific to this Execution Provider.

##### Declaration 

``` 
public void AppendExecutionProvider_CoreML(CoreMLFlags coremlFlags = CoreMLFlags.COREML_FLAG_USE_NONE)
```

##### Parameters 

  Type                                                              Name                            Description
  ----------------------------------------------------------------- ------------------------------- -----------------------
  [CoreMLFlags](Microsoft.ML.OnnxRuntime.CoreMLFlags.html)   [coremlFlags]   CoreML specific flags

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_AppendExecutionProvider_DML_System_Int32_.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.AppendExecutionProvider_DML(System.Int32)%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L264) ] []

#### AppendExecutionProvider_DML(int) 

Use only if you have the onnxruntime package specific to this Execution Provider.

##### Declaration 

``` 
public void AppendExecutionProvider_DML(int deviceId = 0)
```

##### Parameters 

  Type                                                                Name                         Description
  ------------------------------------------------------------------- ---------------------------- -----------------------
  [int](https://learn.microsoft.com/dotnet/api/system.int32)   [deviceId]   device identification

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_AppendExecutionProvider_Dnnl_System_Int32_.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.AppendExecutionProvider_Dnnl(System.Int32)%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L224) ] []

#### AppendExecutionProvider_Dnnl(int) 

Use only if you have the onnxruntime package specific to this Execution Provider.

##### Declaration 

``` 
public void AppendExecutionProvider_Dnnl(int useArena = 1)
```

##### Parameters 

  Type                                                                Name                         Description
  ------------------------------------------------------------------- ---------------------------- -----------------------------------------
  [int](https://learn.microsoft.com/dotnet/api/system.int32)   [useArena]   1 - use allocation arena, 0 - otherwise

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_AppendExecutionProvider_MIGraphX_System_Int32_.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.AppendExecutionProvider_MIGraphX(System.Int32)%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L347) ] []

#### AppendExecutionProvider_MIGraphX(int) 

Use only if you have the onnxruntime package specific to this Execution Provider.

##### Declaration 

``` 
public void AppendExecutionProvider_MIGraphX(int deviceId = 0)
```

##### Parameters 

  Type                                                                Name                         Description
  ------------------------------------------------------------------- ---------------------------- -----------------------
  [int](https://learn.microsoft.com/dotnet/api/system.int32)   [deviceId]   device identification

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_AppendExecutionProvider_Nnapi_Microsoft_ML_OnnxRuntime_NnapiFlags_.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.AppendExecutionProvider_Nnapi(Microsoft.ML.OnnxRuntime.NnapiFlags)%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L360) ] []

#### AppendExecutionProvider_Nnapi(NnapiFlags) 

Use only if you have the onnxruntime package specific to this Execution Provider.

##### Declaration 

``` 
public void AppendExecutionProvider_Nnapi(NnapiFlags nnapiFlags = NnapiFlags.NNAPI_FLAG_USE_NONE)
```

##### Parameters 

  Type                                                            Name                           Description
  --------------------------------------------------------------- ------------------------------ --------------------------
  [NnapiFlags](Microsoft.ML.OnnxRuntime.NnapiFlags.html)   [nnapiFlags]   NNAPI specific flag mask

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_AppendExecutionProvider_OpenVINO_System_String_.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.AppendExecutionProvider_OpenVINO(System.String)%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L278) ] []

#### AppendExecutionProvider_OpenVINO(string) 

Use only if you have the onnxruntime package specific to this Execution Provider.

##### Declaration 

``` 
public void AppendExecutionProvider_OpenVINO(string deviceId = "")
```

##### Parameters 

  Type                                                                    Name                         Description
  ----------------------------------------------------------------------- ---------------------------- ---------------------------------------------
  [string](https://learn.microsoft.com/dotnet/api/system.string)   [deviceId]   device identification, default empty string

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_AppendExecutionProvider_ROCm_Microsoft_ML_OnnxRuntime_OrtROCMProviderOptions_.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.AppendExecutionProvider_ROCm(Microsoft.ML.OnnxRuntime.OrtROCMProviderOptions)%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L334) ] []

#### AppendExecutionProvider_ROCm(OrtROCMProviderOptions) 

Append a ROCm EP instance (based on specified configuration) to the SessionOptions instance. Use only if you have the onnxruntime package specific to this Execution Provider.

##### Declaration 

``` 
public void AppendExecutionProvider_ROCm(OrtROCMProviderOptions rocmProviderOptions)
```

##### Parameters 

  Type                                                                                    Name                                    Description
  --------------------------------------------------------------------------------------- --------------------------------------- --------------------------
  [OrtROCMProviderOptions](Microsoft.ML.OnnxRuntime.OrtROCMProviderOptions.html)   [rocmProviderOptions]   ROCm EP provider options

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_AppendExecutionProvider_ROCm_System_Int32_.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.AppendExecutionProvider_ROCm(System.Int32)%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L319) ] []

#### AppendExecutionProvider_ROCm(int) 

Use only if you have the onnxruntime package specific to this Execution Provider.

##### Declaration 

``` 
public void AppendExecutionProvider_ROCm(int deviceId = 0)
```

##### Parameters 

  Type                                                                Name                         Description
  ------------------------------------------------------------------- ---------------------------- -------------
  [int](https://learn.microsoft.com/dotnet/api/system.int32)   [deviceId]   Device Id

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_AppendExecutionProvider_Tensorrt_Microsoft_ML_OnnxRuntime_OrtTensorRTProviderOptions_.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.AppendExecutionProvider_Tensorrt(Microsoft.ML.OnnxRuntime.OrtTensorRTProviderOptions)%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L306) ] []

#### AppendExecutionProvider_Tensorrt(OrtTensorRTProviderOptions) 

Append a TensorRT EP instance (based on specified configuration) to the SessionOptions instance. Use only if you have the onnxruntime package specific to this Execution Provider.

##### Declaration 

``` 
public void AppendExecutionProvider_Tensorrt(OrtTensorRTProviderOptions trtProviderOptions)
```

##### Parameters 

  Type                                                                                            Name                                   Description
  ----------------------------------------------------------------------------------------------- -------------------------------------- ------------------------------
  [OrtTensorRTProviderOptions](Microsoft.ML.OnnxRuntime.OrtTensorRTProviderOptions.html)   [trtProviderOptions]   TensorRT EP provider options

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_AppendExecutionProvider_Tensorrt_System_Int32_.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.AppendExecutionProvider_Tensorrt(System.Int32)%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L292) ] []

#### AppendExecutionProvider_Tensorrt(int) 

Use only if you have the onnxruntime package specific to this Execution Provider.

##### Declaration 

``` 
public void AppendExecutionProvider_Tensorrt(int deviceId = 0)
```

##### Parameters 

  Type                                                                Name                         Description
  ------------------------------------------------------------------- ---------------------------- -----------------------
  [int](https://learn.microsoft.com/dotnet/api/system.int32)   [deviceId]   device identification

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_DisablePerSessionThreads.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.DisablePerSessionThreads%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L794) ] []

#### DisablePerSessionThreads() 

Disables the per session threads. Default is true. This makes all sessions in the process use a global TP.

##### Declaration 

``` 
public void DisablePerSessionThreads()
```

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_MakeSessionOptionWithCudaProvider_Microsoft_ML_OnnxRuntime_OrtCUDAProviderOptions_.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.MakeSessionOptionWithCudaProvider(Microsoft.ML.OnnxRuntime.OrtCUDAProviderOptions)%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L102) ] []

#### MakeSessionOptionWithCudaProvider(OrtCUDAProviderOptions) 

A helper method to construct a SessionOptions object for CUDA execution provider. Use only if CUDA is installed and you have the onnxruntime package specific to this Execution Provider.

##### Declaration 

``` 
public static SessionOptions MakeSessionOptionWithCudaProvider(OrtCUDAProviderOptions cudaProviderOptions)
```

##### Parameters 

  Type                                                                                    Name                                    Description
  --------------------------------------------------------------------------------------- --------------------------------------- --------------------------
  [OrtCUDAProviderOptions](Microsoft.ML.OnnxRuntime.OrtCUDAProviderOptions.html)   [cudaProviderOptions]   CUDA EP provider options

##### Returns 

  Type                                                                    Description
  ----------------------------------------------------------------------- -------------------------------------------------------------------------
  [SessionOptions](Microsoft.ML.OnnxRuntime.SessionOptions.html)   A SessionsOptions() object configured for execution on provider options

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_MakeSessionOptionWithCudaProvider_System_Int32_.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.MakeSessionOptionWithCudaProvider(System.Int32)%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L80) ] []

#### MakeSessionOptionWithCudaProvider(int) 

A helper method to construct a SessionOptions object for CUDA execution. Use only if CUDA is installed and you have the onnxruntime package specific to this Execution Provider.

##### Declaration 

``` 
public static SessionOptions MakeSessionOptionWithCudaProvider(int deviceId = 0)
```

##### Parameters 

  Type                                                                Name                         Description
  ------------------------------------------------------------------- ---------------------------- -------------
  [int](https://learn.microsoft.com/dotnet/api/system.int32)   [deviceId]   

##### Returns 

  Type                                                                    Description
  ----------------------------------------------------------------------- -----------------------------------------------------------------
  [SessionOptions](Microsoft.ML.OnnxRuntime.SessionOptions.html)   A SessionsOptions() object configured for execution on deviceId

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_MakeSessionOptionWithRocmProvider_Microsoft_ML_OnnxRuntime_OrtROCMProviderOptions_.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.MakeSessionOptionWithRocmProvider(Microsoft.ML.OnnxRuntime.OrtROCMProviderOptions)%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L193) ] []

#### MakeSessionOptionWithRocmProvider(OrtROCMProviderOptions) 

A helper method to construct a SessionOptions object for ROCm execution provider. Use only if ROCm is installed and you have the onnxruntime package specific to this Execution Provider.

##### Declaration 

``` 
public static SessionOptions MakeSessionOptionWithRocmProvider(OrtROCMProviderOptions rocmProviderOptions)
```

##### Parameters 

  Type                                                                                    Name                                    Description
  --------------------------------------------------------------------------------------- --------------------------------------- --------------------------
  [OrtROCMProviderOptions](Microsoft.ML.OnnxRuntime.OrtROCMProviderOptions.html)   [rocmProviderOptions]   ROCm EP provider options

##### Returns 

  Type                                                                    Description
  ----------------------------------------------------------------------- -------------------------------------------------------------------------
  [SessionOptions](Microsoft.ML.OnnxRuntime.SessionOptions.html)   A SessionsOptions() object configured for execution on provider options

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_MakeSessionOptionWithRocmProvider_System_Int32_.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.MakeSessionOptionWithRocmProvider(System.Int32)%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L171) ] []

#### MakeSessionOptionWithRocmProvider(int) 

A helper method to construct a SessionOptions object for ROCM execution. Use only if ROCM is installed and you have the onnxruntime package specific to this Execution Provider.

##### Declaration 

``` 
public static SessionOptions MakeSessionOptionWithRocmProvider(int deviceId = 0)
```

##### Parameters 

  Type                                                                Name                         Description
  ------------------------------------------------------------------- ---------------------------- -------------
  [int](https://learn.microsoft.com/dotnet/api/system.int32)   [deviceId]   Device Id

##### Returns 

  Type                                                                    Description
  ----------------------------------------------------------------------- -----------------------------------------------------------------
  [SessionOptions](Microsoft.ML.OnnxRuntime.SessionOptions.html)   A SessionsOptions() object configured for execution on deviceId

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_MakeSessionOptionWithTensorrtProvider_Microsoft_ML_OnnxRuntime_OrtTensorRTProviderOptions_.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.MakeSessionOptionWithTensorrtProvider(Microsoft.ML.OnnxRuntime.OrtTensorRTProviderOptions)%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L147) ] []

#### MakeSessionOptionWithTensorrtProvider(OrtTensorRTProviderOptions) 

A helper method to construct a SessionOptions object for TensorRT execution provider. Use only if CUDA/TensorRT are installed and you have the onnxruntime package specific to this Execution Provider.

##### Declaration 

``` 
public static SessionOptions MakeSessionOptionWithTensorrtProvider(OrtTensorRTProviderOptions trtProviderOptions)
```

##### Parameters 

  Type                                                                                            Name                                   Description
  ----------------------------------------------------------------------------------------------- -------------------------------------- ------------------------------
  [OrtTensorRTProviderOptions](Microsoft.ML.OnnxRuntime.OrtTensorRTProviderOptions.html)   [trtProviderOptions]   TensorRT EP provider options

##### Returns 

  Type                                                                    Description
  ----------------------------------------------------------------------- -------------------------------------------------------------------------
  [SessionOptions](Microsoft.ML.OnnxRuntime.SessionOptions.html)   A SessionsOptions() object configured for execution on provider options

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_MakeSessionOptionWithTensorrtProvider_System_Int32_.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.MakeSessionOptionWithTensorrtProvider(System.Int32)%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L124) ] []

#### MakeSessionOptionWithTensorrtProvider(int) 

A helper method to construct a SessionOptions object for TensorRT execution. Use only if CUDA/TensorRT are installed and you have the onnxruntime package specific to this Execution Provider.

##### Declaration 

``` 
public static SessionOptions MakeSessionOptionWithTensorrtProvider(int deviceId = 0)
```

##### Parameters 

  Type                                                                Name                         Description
  ------------------------------------------------------------------- ---------------------------- -------------
  [int](https://learn.microsoft.com/dotnet/api/system.int32)   [deviceId]   

##### Returns 

  Type                                                                    Description
  ----------------------------------------------------------------------- -----------------------------------------------------------------
  [SessionOptions](Microsoft.ML.OnnxRuntime.SessionOptions.html)   A SessionsOptions() object configured for execution on deviceId

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_RegisterCustomOpLibrary_System_String_.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.RegisterCustomOpLibrary(System.String)%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L517) ] []

#### RegisterCustomOpLibrary(string) 

Loads a DLL named \'libraryPath\' and looks for this entry point: OrtStatus\* RegisterCustomOps(OrtSessionOptions\* options, const OrtApiBase\* api); It then passes in the provided session options to this function along with the api base.

Prior to v1.15 this leaked the library handle and RegisterCustomOpLibraryV2 was added to resolve that.

From v1.15 on ONNX Runtime will manage the lifetime of the handle.

##### Declaration 

``` 
public void RegisterCustomOpLibrary(string libraryPath)
```

##### Parameters 

  Type                                                                    Name                            Description
  ----------------------------------------------------------------------- ------------------------------- -------------------------------
  [string](https://learn.microsoft.com/dotnet/api/system.string)   [libraryPath]   path to the custom op library

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_RegisterCustomOpLibraryV2_System_String_System_IntPtr__.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.RegisterCustomOpLibraryV2(System.String%2CSystem.IntPtr%40)%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L536) ] []

#### RegisterCustomOpLibraryV2(string, out nint) 

Loads a DLL named \'libraryPath\' and looks for this entry point: OrtStatus\* RegisterCustomOps(OrtSessionOptions\* options, const OrtApiBase\* api); It then passes in the provided session options to this function along with the api base. The handle to the loaded library is returned in \'libraryHandle\'. It can be unloaded by the caller after all sessions using the passed in session options are destroyed, or if an error occurs and it is non null. Hint: .NET Core 3.1 has a \'NativeLibrary\' class that can be used to free the library handle

##### Declaration 

``` 
public void RegisterCustomOpLibraryV2(string libraryPath, out nint libraryHandle)
```

##### Parameters 

  Type                                                                    Name                              Description
  ----------------------------------------------------------------------- --------------------------------- -------------------------------
  [string](https://learn.microsoft.com/dotnet/api/system.string)   [libraryPath]     Custom op library path
  [nint](https://learn.microsoft.com/dotnet/api/system.intptr)     [libraryHandle]   out parameter, library handle

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_RegisterOrtExtensions.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.RegisterOrtExtensions%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L557) ] []

#### RegisterOrtExtensions() 

Register the custom operators from the Microsoft.ML.OnnxRuntime.Extensions NuGet package. A reference to Microsoft.ML.OnnxRuntime.Extensions must be manually added to your project.

##### Declaration 

``` 
public void RegisterOrtExtensions()
```

##### Exceptions 

  Type                                                                                Condition
  ----------------------------------------------------------------------------------- ------------------------------------------------
  [OnnxRuntimeException](Microsoft.ML.OnnxRuntime.OnnxRuntimeException.html)   Throws if the extensions library is not found.

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_ReleaseHandle.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.ReleaseHandle%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L1136) ] []

#### ReleaseHandle() 

Overrides SafeHandle.ReleaseHandle() to properly dispose of the native instance of SessionOptions

##### Declaration 

``` 
protected override bool ReleaseHandle()
```

##### Returns 

  Type                                                                   Description
  ---------------------------------------------------------------------- ---------------------
  [bool](https://learn.microsoft.com/dotnet/api/system.boolean)   always returns true

##### Overrides 

[SafeHandle.ReleaseHandle()](https://learn.microsoft.com/dotnet/api/system.runtime.interopservices.safehandle.releasehandle)

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_SetEpSelectionPolicy_Microsoft_ML_OnnxRuntime_ExecutionProviderDevicePolicy_.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.SetEpSelectionPolicy(Microsoft.ML.OnnxRuntime.ExecutionProviderDevicePolicy)%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L637) ] []

#### SetEpSelectionPolicy(ExecutionProviderDevicePolicy) 

Set the execution provider selection policy if using automatic execution provider selection. Execution providers must be registered with the OrtEnv to be available for selection.

##### Declaration 

``` 
public void SetEpSelectionPolicy(ExecutionProviderDevicePolicy policy)
```

##### Parameters 

  Type                                                                                                  Name                       Description
  ----------------------------------------------------------------------------------------------------- -------------------------- ----------------
  [ExecutionProviderDevicePolicy](Microsoft.ML.OnnxRuntime.ExecutionProviderDevicePolicy.html)   [policy]   Policy to use.

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_SetEpSelectionPolicyDelegate_Microsoft_ML_OnnxRuntime_SessionOptions_EpSelectionDelegate_.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.SetEpSelectionPolicyDelegate(Microsoft.ML.OnnxRuntime.SessionOptions.EpSelectionDelegate)%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L648) ] []

#### SetEpSelectionPolicyDelegate(EpSelectionDelegate) 

Set the execution provider selection policy if using automatic execution provider selection. Execution providers must be registered with the OrtEnv to be available for selection.

##### Declaration 

``` 
public void SetEpSelectionPolicyDelegate(SessionOptions.EpSelectionDelegate selectionDelegate = null)
```

##### Parameters 

  Type                                                                                                                                                                   Name                                  Description
  ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- ------------------------------------- -------------------------------------------------------
  [SessionOptions](Microsoft.ML.OnnxRuntime.SessionOptions.html).[EpSelectionDelegate](Microsoft.ML.OnnxRuntime.SessionOptions.EpSelectionDelegate.html)   [selectionDelegate]   Delegate that implements the custom selection policy.

[ [\|] [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions_SetLoadCancellationFlag_System_Boolean_.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions.SetLoadCancellationFlag(System.Boolean)%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A) ] [ [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L937) ] []

#### SetLoadCancellationFlag(bool) 

Sets the load cancellation flag for the session. Default is set to false. Provides an opportunity for the user to cancel model loading.

##### Declaration 

``` 
public void SetLoadCancellationFlag(bool value)
```

##### Parameters 

  Type                                                                   Name                      Description
  ---------------------------------------------------------------------- ------------------------- ------------------------------------------------
  [bool](https://learn.microsoft.com/dotnet/api/system.boolean)   [value]   true to request cancellation, false to proceed

### Implements 

[IDisposable](https://learn.microsoft.com/dotnet/api/system.idisposable)

### Extension Methods 

[SessionOptionsContainer.ApplyConfiguration(SessionOptions, string, bool)](Microsoft.ML.OnnxRuntime.SessionOptionsContainer.html#Microsoft_ML_OnnxRuntime_SessionOptionsContainer_ApplyConfiguration_Microsoft_ML_OnnxRuntime_SessionOptions_System_String_System_Boolean_)

- [Improve this Doc](https://github.com/microsoft/onnxruntime/new/main/apiSpec/new?filename=Microsoft_ML_OnnxRuntime_SessionOptions.md&value=---%0Auid%3A%20Microsoft.ML.OnnxRuntime.SessionOptions%0Asummary%3A%20'*You%20can%20override%20summary%20for%20the%20API%20here%20using%20*MARKDOWN*%20syntax'%0A---%0A%0A*Please%20type%20below%20more%20information%20about%20this%20API%3A*%0A%0A)
- [View Source](https://github.com/microsoft/onnxruntime/blob/main/csharp/src/Microsoft.ML.OnnxRuntime/SessionOptions.shared.cs/#L55)