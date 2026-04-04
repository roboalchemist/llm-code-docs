# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInterpreter.md.txt

# FirebaseModelInterpreter

public final class **FirebaseModelInterpreter** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
implements [Closeable](https://developer.android.com/reference/java/io/Closeable.html)  
**This class is deprecated.**   

For more information refer to the [custom model implementation
instructions](https://firebase.google.com/docs/ml/android/use-custom-models).

Interpreter to run custom models with TensorFlow Lite (requires API level 16+)

A model interpreter is created via [getInstance(FirebaseModelInterpreterOptions)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInterpreter#getInstance(com.google.firebase.ml.custom.FirebaseModelInterpreterOptions)) Follow the steps below to specify the
[FirebaseCustomRemoteModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseCustomRemoteModel)
or [FirebaseCustomLocalModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseCustomLocalModel),
create a [FirebaseModelInterpreterOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInterpreterOptions)
and then create a [FirebaseModelInterpreter](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInterpreter)
and all the way to running an inference with the model.

Firstly, create at least one of [FirebaseCustomRemoteModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseCustomRemoteModel)
and [FirebaseCustomLocalModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseCustomLocalModel).
If you want to use [FirebaseCustomRemoteModel](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseCustomRemoteModel),
you need to download it through FirebaseModelManager first.

The following code creates the model and the interpreterOptions:  



     FirebaseCustomRemoteModel remoteModel = new FirebaseCustomRemoteModel.Builder(REMOTE_MODEL_NAME)
         .build();

     FirebaseModelInterpreterOptions interpreterOptions =
          new FirebaseModelInterpreterOptions.Builder(remoteModel).build();

     Or

     FirebaseCustomLocalModel localModel = new FirebaseCustomLocalModel.Builder()
         .setFilePath(filePath).build();

     FirebaseModelInterpreterOptions interpreterOptions =
         new FirebaseModelInterpreterOptions.Builder(localModel).build();

     
Secondly, create an instance of [FirebaseModelInterpreter](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInterpreter)
with the [FirebaseModelInterpreterOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInterpreterOptions)  


     FirebaseModelInterpreter interpreter = FirebaseModelInterpreter.getInstance(interpreterOptions);
     
Thirdly, create a [FirebaseModelInputs](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputs)
and a [FirebaseModelInputOutputOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputOutputOptions).
You need to know the input and output data specifications of the model, including the data
types and input/output dimensions. The following code is an example:  


     FirebaseModelInputs modelInputs = new FirebaseModelInputs.Builder().add(...).build();

     FirebaseModelInputOutputOptions inputOutputOptions =
         new FirebaseModelInputOutputOptions.Builder()
             .setInputFormat(0, FirebaseModelDataType.FLOAT32, inputDims)
             .setOutputFormat(0, FirebaseModelDataType.FLOAT32, outputDims)
             .build();
     
Lastly, feed the inputs to [run(FirebaseModelInputs, FirebaseModelInputOutputOptions)](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInterpreter#run(com.google.firebase.ml.custom.FirebaseModelInputs, com.google.firebase.ml.custom.FirebaseModelInputOutputOptions)). The following code is
an example:  


     Task<FirebaseModelOutputs> task = interpreter.run(modelInputs, inputOutputOptions);
     task.addOnSuccessListener(...).addOnFailureListener(...);
     
### Public Method Summary

|----------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| void                                                                                                                                         | [close](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInterpreter#close())()                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| Task\<[Integer](https://developer.android.com/reference/java/lang/Integer.html)\>                                                            | [getInputIndex](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInterpreter#getInputIndex(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) name) Gets the index of an input by its name.                                                                                                                                                                                                                                                                                                           |
| static [FirebaseModelInterpreter](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInterpreter) | [getInstance](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInterpreter#getInstance(com.google.firebase.ml.custom.FirebaseModelInterpreterOptions))([FirebaseModelInterpreterOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInterpreterOptions) options) Gets an instance of the `FirebaseModelInterpreter` to support custom model specified in `FirebaseModelOptions`.                                                                                                           |
| Task\<[Integer](https://developer.android.com/reference/java/lang/Integer.html)\>                                                            | [getOutputIndex](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInterpreter#getOutputIndex(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) name) Gets the index of an output by its name.                                                                                                                                                                                                                                                                                                        |
| boolean                                                                                                                                      | [isStatsCollectionEnabled](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInterpreter#isStatsCollectionEnabled())() Determines whether stats collection in Model Interpreter is enabled.                                                                                                                                                                                                                                                                                                                                                    |
| Task\<[FirebaseModelOutputs](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelOutputs)\>        | [run](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInterpreter#run(com.google.firebase.ml.custom.FirebaseModelInputs, com.google.firebase.ml.custom.FirebaseModelInputOutputOptions))([FirebaseModelInputs](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputs) inputs, [FirebaseModelInputOutputOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputOutputOptions) options) Runs inference with input and data configurations. |
| void                                                                                                                                         | [setStatsCollectionEnabled](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInterpreter#setStatsCollectionEnabled(boolean))(boolean enable) Enables stats collection in ML Kit model interpreter.                                                                                                                                                                                                                                                                                                                                            |

### Inherited Method Summary

From class java.lang.Object  

|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [Object](https://developer.android.com/reference/java/lang/Object.html)          | clone()                                                                              |
| boolean                                                                          | equals([Object](https://developer.android.com/reference/java/lang/Object.html) arg0) |
| void                                                                             | finalize()                                                                           |
| final [Class](https://developer.android.com/reference/java/lang/Class.html)\<?\> | getClass()                                                                           |
| int                                                                              | hashCode()                                                                           |
| final void                                                                       | notify()                                                                             |
| final void                                                                       | notifyAll()                                                                          |
| [String](https://developer.android.com/reference/java/lang/String.html)          | toString()                                                                           |
| final void                                                                       | wait(long arg0, int arg1)                                                            |
| final void                                                                       | wait(long arg0)                                                                      |
| final void                                                                       | wait()                                                                               |

From interface java.io.Closeable  

|---------------|---------|
| abstract void | close() |

From interface java.lang.AutoCloseable  

|---------------|---------|
| abstract void | close() |

## Public Methods

#### public void **close** ()

#### public Task\<[Integer](https://developer.android.com/reference/java/lang/Integer.html)\>
**getInputIndex** ([String](https://developer.android.com/reference/java/lang/String.html) name)

Gets the index of an input by its name.  

##### Parameters

| name | the name of the input |
|------|-----------------------|

##### Returns

- a [Task](https://firebase.google.com/docs/reference/android/com/google/android/gms/tasks/Task) for the index of the input. The [Task](https://firebase.google.com/docs/reference/android/com/google/android/gms/tasks/Task) will fail with [FirebaseMLException](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/FirebaseMLException) if the input name does not exist in the model.  

#### public static [FirebaseModelInterpreter](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInterpreter)
**getInstance** ([FirebaseModelInterpreterOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInterpreterOptions) options)

Gets an instance of the `FirebaseModelInterpreter` to support custom
model specified in `FirebaseModelOptions`.  

##### Parameters

| options | the options for the model to use. |
|---------|-----------------------------------|

##### Returns

- an instance of `FirebaseModelInterpreter`. Note that the interpreter instance will be the same instance if the supplied options are the same.  

##### Throws

|         [IllegalArgumentException](https://developer.android.com/reference/java/lang/IllegalArgumentException.html)         | if [FirebaseModelInterpreterOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInterpreterOptions) contains no model |
| [FirebaseMLException](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/FirebaseMLException) |                                                                                                                                                                          |
|-----------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

#### public Task\<[Integer](https://developer.android.com/reference/java/lang/Integer.html)\>
**getOutputIndex** ([String](https://developer.android.com/reference/java/lang/String.html) name)

Gets the index of an output by its name.  

##### Parameters

| name | the name of the output |
|------|------------------------|

##### Returns

- a [Task](https://firebase.google.com/docs/reference/android/com/google/android/gms/tasks/Task) for the index of the output name. The [Task](https://firebase.google.com/docs/reference/android/com/google/android/gms/tasks/Task) will fail with [FirebaseMLException](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/FirebaseMLException) if the output name does not exist in the model.  

#### public boolean **isStatsCollectionEnabled** ()

Determines whether stats collection in Model Interpreter is enabled.  

##### Returns

- true if stats collection is enabled.  

#### public Task\<[FirebaseModelOutputs](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelOutputs)\>
**run** ([FirebaseModelInputs](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputs) inputs, [FirebaseModelInputOutputOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputOutputOptions) options)

Runs inference with input and data configurations.  

##### Parameters

| inputs  |                               an instance of [FirebaseModelInputs](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputs) containing input data                               |
| options | an instance of [FirebaseModelInputOutputOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInputOutputOptions) containing types and dimensions of input and output data. |
|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|

#### public void **setStatsCollectionEnabled** (boolean enable)

Enables stats collection in ML Kit model interpreter. The stats include API calls
counts, errors, API call durations, options, etc. No personally identifiable
information is logged.

The setting is per [MlKitContext](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/common/internal/MlKitContext),
and it is persistent together with app's private data. It means if the user uninstalls
the app or clears all app data, the setting will be erased. The best practice is to set
the flag in each initialization.

By default the logging is enabled. You have to specifically set it to false here to
disable logging for [FirebaseModelInterpreter](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInterpreter).