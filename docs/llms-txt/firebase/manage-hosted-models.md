# Source: https://firebase.google.com/docs/ml/manage-hosted-models.md.txt

<br />

You can deploy and manage custom models and AutoML-trained models using either theFirebaseconsole or the Firebase Admin Python and Node.js SDKs. If you just want to deploy a model and occasionally update it, it's usually simplest to use theFirebaseconsole. The Admin SDK can be helpful when integrating with build pipelines, working with Colab or Jupyter notebooks, and other workflows.

## Deploy and manage models in theFirebaseconsole

### TensorFlow Lite models

To deploy a TensorFlow Lite model using theFirebaseconsole:

1. Open the[Firebase MLCustom model page](https://console.firebase.google.com/project/_/ml/custom)in theFirebaseconsole.
2. Click**Add custom model** (or**Add another model**).
3. Specify a name that will be used to identify your model in your Firebase project, then upload the TensorFlow Lite model file (usually ending in`.tflite`or`.lite`).

After you deploy your model, you can find it on the Custom page. From there, you can complete tasks such as updating the model with a new file, downloading the model, and deleting the model from your project.

## Deploy and manage models with the Firebase Admin SDK

This section shows how you can complete common model deployment and management tasks with the Admin SDK. See the SDK reference for[Python](https://firebase.google.com/docs/reference/admin/python/firebase_admin.ml)or[Node.js](https://firebase.google.com/docs/reference/admin/node/firebase-admin.machine-learning)for additional help.

For examples of the SDK in use, see the[Python quickstart sample](https://github.com/firebase/quickstart-python/tree/master/machine-learning)and[Node.js quickstart sample](https://github.com/firebase/quickstart-nodejs/tree/master/machine-learning).

### Before you begin

1. If you don't already have a Firebase project, create a new project in the[Firebaseconsole](https://console.firebase.google.com/). Then, open your project and do the following:

   1. On the[Settings](https://console.firebase.google.com/project/_/settings/serviceaccounts/adminsdk)page, create a service account and download the service account key file. Keep this file safe, since it grants administrator access to your project.

   2. On the Storage page, enableCloud Storage. Take note of your bucket name.

      You need aCloud Storagebucket to temporarily store model files while adding them to your Firebase project. If you are on the Blaze plan, you can create and use a bucket other than the default for this purpose.
   3. On theFirebase MLpage, click**Get started** if you haven't yet enabledFirebase ML.

2. In the[Google APIs console](https://console.developers.google.com/apis/library/firebaseml.googleapis.com?project=_), open your Firebase project and enable the Firebase ML API.

3. [Install and initialize the Admin SDK](https://firebase.google.com/docs/admin/setup).

   When you initialize the SDK, specify your service account credentials and theCloud Storagebucket you want to use to store your models:  

   ### Python

       import firebase_admin
       from firebase_admin import ml
       from firebase_admin import credentials

       firebase_admin.initialize_app(
         credentials.Certificate('/path/to/your/service_account_key.json'),
         options={
             'storageBucket': 'your-storage-bucket',
         })

   ### Node.js

       const admin = require('firebase-admin');
       const serviceAccount = require('/path/to/your/service_account_key.json');
       admin.initializeApp({
         credential: admin.credential.cert(serviceAccount),
         storageBucket: 'your-storage-bucket',
       });
       const ml = admin.machineLearning();

   | **Note:** InGoogle Cloudenvironments, includingCloud Functions for Firebase, the Admin SDK can automatically initialize with your service account credentials. See[the setup guide](https://firebase.google.com/docs/admin/setup).

### Deploy models

#### TensorFlow Lite files

To deploy a TensorFlow Lite model from a model file, upload it to your project and then publish it:  

### Python

    # First, import and initialize the SDK as shown above.

    # Load a tflite file and upload it to Cloud Storage
    source = ml.TFLiteGCSModelSource.from_tflite_model_file('example.tflite')

    # Create the model object
    tflite_format = ml.TFLiteFormat(model_source=source)
    model = ml.Model(
        display_name="example_model",  # This is the name you use from your app to load the model.
        tags=["examples"],             # Optional tags for easier management.
        model_format=tflite_format)

    # Add the model to your Firebase project and publish it
    new_model = ml.create_model(model)
    ml.publish_model(new_model.model_id)

### Node.js

    // First, import and initialize the SDK as shown above.

    (async () => {
      // Upload the tflite file to Cloud Storage
      const storageBucket = admin.storage().bucket('your-storage-bucket');
      const files = await storageBucket.upload('./example.tflite');

      // Create the model object and add the model to your Firebase project.
      const bucket = files[0].metadata.bucket;
      const name = files[0].metadata.name;
      const gcsUri = `gs:/â /${bucket}/${name}`;
      const model = await ml.createModel({
        displayName: 'example_model',  // This is the name you use from your app to load the model.
        tags: ['examples'],  // Optional tags for easier management.
        tfliteModel: { gcsTfliteUri: gcsUri },
      });

      // Publish the model.
      await ml.publishModel(model.modelId);

      process.exit();
    })().catch(console.error);

#### TensorFlow and Keras models

With the Python SDK, you can convert a model from TensorFlow saved model format to TensorFlow Lite and upload it to yourCloud Storagebucket in a single step. Then, deploy it the same way you deploy a TensorFlow Lite file.  

### Python

    # First, import and initialize the SDK as shown above.

    # Convert the model to TensorFlow Lite and upload it to Cloud Storage
    source = ml.TFLiteGCSModelSource.from_saved_model('./model_directory')

    # Create the model object
    tflite_format = ml.TFLiteFormat(model_source=source)
    model = ml.Model(
        display_name="example_model",  # This is the name you use from your app to load the model.
        tags=["examples"],             # Optional tags for easier management.
        model_format=tflite_format)

    # Add the model to your Firebase project and publish it
    new_model = ml.create_model(model)
    ml.publish_model(new_model.model_id)

If you have a Keras model, you can also convert it to TensorFlow Lite and upload it in a single step. You can use a Keras model saved to an HDF5 file:  

### Python

    import tensorflow as tf

    # Load a Keras model, convert it to TensorFlow Lite, and upload it to Cloud Storage
    model = tf.keras.models.load_model('your_model.h5')
    source = ml.TFLiteGCSModelSource.from_keras_model(model)

    # Create the model object, add the model to your project, and publish it. (See
    # above.)
    # ...

Or, you can convert and upload a Keras model straight from your training script:  

### Python

    import tensorflow as tf

    # Create a simple Keras model.
    x = [-1, 0, 1, 2, 3, 4]
    y = [-3, -1, 1, 3, 5, 7]

    model = tf.keras.models.Sequential(
        [tf.keras.layers.Dense(units=1, input_shape=[1])])
    model.compile(optimizer='sgd', loss='mean_squared_error')
    model.fit(x, y, epochs=3)

    # Convert the model to TensorFlow Lite and upload it to Cloud Storage
    source = ml.TFLiteGCSModelSource.from_keras_model(model)

    # Create the model object, add the model to your project, and publish it. (See
    # above.)
    # ...

#### AutoML TensorFlow Lite models

If you trained an Edge model with the[AutoML Cloud API](https://cloud.google.com/vision/automl/docs/train-edge#automl_vision_classification_create_model-python)or with theGoogle Cloudconsole UI, you can deploy the model to Firebase using the Admin SDK.
| Firebase ML's AutoML Vision Edge features are deprecated. Consider using[Vertex AI](https://cloud.google.com/vertex-ai/docs/beginner/beginners-guide)to automatically train ML models, which you can either[export as TensorFlow Lite models](https://cloud.google.com/vertex-ai/docs/export/export-edge-model)for on-device use or[deploy for cloud-based inference](https://cloud.google.com/vertex-ai/docs/predictions/overview).

You will need to specify the model's resource identifier, which is a string that looks like the following example:  

```
projects/PROJECT_NUMBER/locations/STORAGE_LOCATION/models/MODEL_ID
```

|--------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `PROJECT_NUMBER`   | The project number of theCloud Storagebucket that contains the model. This might be your Firebase project or anotherGoogle Cloudproject. You can find this value on the Settings page of theFirebaseconsole or theGoogle Cloudconsole dashboard. |
| `STORAGE_LOCATION` | The resource location of theCloud Storagebucket that contains the model. This value is always`us-central1`.                                                                                                                                      |
| `MODEL_ID`         | The model's ID, which you got from the AutoML Cloud API.                                                                                                                                                                                         |

### Python

    # First, import and initialize the SDK as shown above.

    # Get a reference to the AutoML model
    source = ml.TFLiteAutoMlSource('projects/{}/locations/{}/models/{}'.format(
        # See above for information on these values.
        project_number,
        storage_location,
        model_id
    ))

    # Create the model object
    tflite_format = ml.TFLiteFormat(model_source=source)
    model = ml.Model(
        display_name="example_model",  # This is the name you will use from your app to load the model.
        tags=["examples"],             # Optional tags for easier management.
        model_format=tflite_format)

    # Add the model to your Firebase project and publish it
    new_model = ml.create_model(model)
    new_model.wait_for_unlocked()
    ml.publish_model(new_model.model_id)

### Node.js

    // First, import and initialize the SDK as shown above.

    (async () => {
      // Get a reference to the AutoML model. See above for information on these
      // values.
      const automlModel = `projects/${projectNumber}/locations/${storageLocation}/models/${modelId}`;

      // Create the model object and add the model to your Firebase project.
      const model = await ml.createModel({
        displayName: 'example_model',  // This is the name you use from your app to load the model.
        tags: ['examples'],  // Optional tags for easier management.
        tfliteModel: { automlModel: automlModel },
      });

      // Wait for the model to be ready.
      await model.waitForUnlocked();

      // Publish the model.
      await ml.publishModel(model.modelId);

      process.exit();
    })().catch(console.error);

### List your project's models

You can list your project's models, optionally filtering the results:  

### Python

    # First, import and initialize the SDK as shown above.

    face_detectors = ml.list_models(list_filter="tags: face_detector").iterate_all()
    print("Face detection models:")
    for model in face_detectors:
      print('{} (ID: {})'.format(model.display_name, model.model_id))

### Node.js

    // First, import and initialize the SDK as shown above.

    (async () => {
      let listOptions = {filter: 'tags: face_detector'}
      let models;
      let pageToken = null;
      do {
        if (pageToken) listOptions.pageToken = pageToken;
        ({models, pageToken} = await ml.listModels(listOptions));
        for (const model of models) {
          console.log(`${model.displayName} (ID: ${model.modelId})`);
        }
      } while (pageToken != null);

      process.exit();
    })().catch(console.error);

You can filter by the following fields:

|       Field       |                                                                                           Examples                                                                                           |
|-------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `display_name`    | `display_name = example_model` `display_name != example_model` All display names with the`experimental_`prefix: `display_name : experimental_*` Note that only prefix matching is supported. |
| `tags`            | `tags: face_detector` `tags: face_detector AND tags: experimental`                                                                                                                           |
| `state.published` | `state.published = true` `state.published = false`                                                                                                                                           |

Combine filters with the`AND`,`OR`, and`NOT`operators and parentheses (`(`,`)`).

### Update models

After you've added a model to your project, you can update its display name, tags, and`tflite`model file:  

### Python

    # First, import and initialize the SDK as shown above.

    model = ...   # Model object from create_model(), get_model(), or list_models()

    # Update the model with a new tflite model. (You could also update with a
    # `TFLiteAutoMlSource`)
    source = ml.TFLiteGCSModelSource.from_tflite_model_file('example_v2.tflite')
    model.model_format = ml.TFLiteFormat(model_source=source)

    # Update the model's display name.
    model.display_name = "example_model"

    # Update the model's tags.
    model.tags = ["examples", "new_models"]

    # Add a new tag.
    model.tags += "experimental"

    # After you change the fields you want to update, save the model changes to
    # Firebase and publish it.
    updated_model = ml.update_model(model)
    ml.publish_model(updated_model.model_id)

### Node.js

    // First, import and initialize the SDK as shown above.

    (async () => {
      const model = ... // Model object from createModel(), getModel(), or listModels()

      // Upload a new tflite file to Cloud Storage.
      const files = await storageBucket.upload('./example_v2.tflite');
      const bucket = files[0].metadata.bucket;
      const name = files[0].metadata.name;

      // Update the model. Any fields you omit will be unchanged.
      await ml.updateModel(model.modelId, {
        displayName: 'example_model',  // Update the model's display name.
        tags: model.tags.concat(['new']),  // Add a tag.
        tfliteModel: {gcsTfliteUri: `gs:/â /${bucket}/${name}`},
      });

      process.exit();
    })().catch(console.error);

### Unpublish or delete models

To unpublish or delete a model, pass the model ID to the unpublish or delete methods. When you unpublish a model, it remains in your project, but isn't available for your apps to download. When you delete a model, it's completely removed from your project. (Unpublishing a model is not expected in a standard workflow, but you can use it to immediately unpublish a new model you accidentally published and isn't being used anywhere yet, or in cases where it is worse for users to download a "bad" model than to get model-not-found errors.)

If you don't still have a reference to the Model object, you'll probably need to get the model ID by listing your project's models with a filter. For example, to delete all models tagged "face_detector":  

### Python

    # First, import and initialize the SDK as shown above.

    face_detectors = ml.list_models(list_filter="tags: 'face_detector'").iterate_all()
    for model in face_detectors:
      ml.delete_model(model.model_id)

### Node.js

    // First, import and initialize the SDK as shown above.

    (async () => {
      let listOptions = {filter: 'tags: face_detector'}
      let models;
      let pageToken = null;
      do {
        if (pageToken) listOptions.pageToken = pageToken;
        ({models, pageToken} = await ml.listModels(listOptions));
        for (const model of models) {
          await ml.deleteModel(model.modelId);
        }
      } while (pageToken != null);

      process.exit();
    })().catch(console.error);