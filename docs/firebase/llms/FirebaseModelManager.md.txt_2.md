# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelManager.md.txt

# FirebaseModelManager

public class **FirebaseModelManager** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Manages the registration of cloud and local models.

A model should be registered with `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelManager`
first before being used by `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelInterpreter`.
The model name is the key for a model, and a model name can only be registered once.

For cloud model, the model name should be the same name as that uploaded in Firebase
Console.

This class is thread safe.

### Public Method Summary

|---|---|
| synchronized [FirebaseCloudModelSource](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/model/FirebaseCloudModelSource) | [getCloudModelSource](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelManager#getCloudModelSource(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) modelName) Gets the registered cloud model source based on the model name. |
| synchronized static [FirebaseModelManager](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelManager) | [getInstance](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelManager#getInstance())() Gets an instance of a `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelManager` corresponding to the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp` instance. |
| synchronized [FirebaseLocalModelSource](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/model/FirebaseLocalModelSource) | [getLocalModelSource](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelManager#getLocalModelSource(java.lang.String))([String](https://developer.android.com/reference/java/lang/String.html) modelName) Gets the registered local model source based on the model name. |
| synchronized boolean | [registerCloudModelSource](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelManager#registerCloudModelSource(com.google.firebase.ml.custom.model.FirebaseCloudModelSource))([FirebaseCloudModelSource](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/model/FirebaseCloudModelSource) cloudModelSource) Registers a cloud model for model interpreter to use later. |
| synchronized boolean | [registerLocalModelSource](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelManager#registerLocalModelSource(com.google.firebase.ml.custom.model.FirebaseLocalModelSource))([FirebaseLocalModelSource](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/model/FirebaseLocalModelSource) localModelSource) Registers a local model for model interpreter to use later. |

### Inherited Method Summary

From class java.lang.Object

|---|---|
| [Object](https://developer.android.com/reference/java/lang/Object.html) | clone() |
| boolean | equals([Object](https://developer.android.com/reference/java/lang/Object.html) arg0) |
| void | finalize() |
| final [Class](https://developer.android.com/reference/java/lang/Class.html)\<?\> | getClass() |
| int | hashCode() |
| final void | notify() |
| final void | notifyAll() |
| [String](https://developer.android.com/reference/java/lang/String.html) | toString() |
| final void | wait(long arg0, int arg1) |
| final void | wait(long arg0) |
| final void | wait() |

## Public Methods

#### public synchronized [FirebaseCloudModelSource](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/model/FirebaseCloudModelSource) **getCloudModelSource** ([String](https://developer.android.com/reference/java/lang/String.html) modelName)

Gets the registered cloud model source based on the model name. Returns null if the
model name is not registered.

#### public static synchronized [FirebaseModelManager](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelManager)
**getInstance** ()

Gets an instance of a `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelManager`
corresponding to the default `https://firebase.google.com/docs/reference/android/com/google/firebase/FirebaseApp`
instance.

#### public synchronized [FirebaseLocalModelSource](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/model/FirebaseLocalModelSource) **getLocalModelSource** ([String](https://developer.android.com/reference/java/lang/String.html) modelName)

Gets the registered local model source based on the model name. Returns null if the
model name is not registered.

#### public synchronized boolean
**registerCloudModelSource** ([FirebaseCloudModelSource](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/model/FirebaseCloudModelSource) cloudModelSource)

Registers a cloud model for model interpreter to use later. Cloud models are keyed
by model names, and each model name can be registered at most once.

The model name should have the same model name when uploaded to the Firebase
Console.

##### Returns

- false if the model name is already registered, in which case you could use {`https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelManager#getCloudModelSource(java.lang.String)`} to get the registered cloud model source. True if registration succeeds.

##### Throws

| [NullPointerException](https://developer.android.com/reference/java/lang/NullPointerException.html) | if cloudModelSource is null. |
|---|---|

#### public synchronized boolean
**registerLocalModelSource** ([FirebaseLocalModelSource](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/model/FirebaseLocalModelSource) localModelSource)

Registers a local model for model interpreter to use later. Local models are keyed
by model names, and each model name can be registered at most once.

##### Returns

- false if the model name is already registered, and you could use {`https://firebase.google.com/docs/reference/android/com/google/firebase/ml/custom/FirebaseModelManager#getLocalModelSource(java.lang.String)`} to get the registered local model source. True if registration succeeds.

##### Throws

| [NullPointerException](https://developer.android.com/reference/java/lang/NullPointerException.html) | if localModelSource is null. |
|---|---|