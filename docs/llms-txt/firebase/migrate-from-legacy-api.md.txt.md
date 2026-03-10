# Source: https://firebase.google.com/docs/ml/android/migrate-from-legacy-api.md.txt

Version 22.0.2 of the `firebase-ml-model-interpreter` library introduces a new
`getLatestModelFile()` method, which gets the location on the device of custom
models. You can use this method to directly instantiate a TensorFlow Lite
`Interpreter` object, which you can use instead of the
`FirebaseModelInterpreter` wrapper.

Going forward, this is the preferred approach. Because the TensorFlow Lite
interpreter version is no longer coupled with the Firebase library version, you
have more flexibility to upgrade to new versions of TensorFlow Lite when you
want, or more easily use custom TensorFlow Lite builds.

This page shows how you can migrate from using `FirebaseModelInterpreter` to the
TensorFlow Lite `Interpreter`.

## 1. Update project dependencies

Update your project's dependencies to include version 22.0.2 of the
`firebase-ml-model-interpreter` library (or newer) and the `tensorflow-lite`
library:

#### Before

    implementation("com.google.firebase:firebase-ml-model-interpreter:22.0.1")

#### After

    implementation("com.google.firebase:firebase-ml-model-interpreter:22.0.2")
    implementation("org.tensorflow:tensorflow-lite:2.0.0")

## 2. Create a TensorFlow Lite interpreter instead of a FirebaseModelInterpreter

Instead of creating a `FirebaseModelInterpreter`, get the model's location on
device with `getLatestModelFile()` and use it to create a TensorFlow Lite
`Interpreter`.

#### Before

### Kotlin

    val remoteModel = FirebaseCustomRemoteModel.Builder("your_model").build()
    val options = FirebaseModelInterpreterOptions.Builder(remoteModel).build()
    val interpreter = FirebaseModelInterpreter.getInstance(options)

### Java

    FirebaseCustomRemoteModel remoteModel =
            new FirebaseCustomRemoteModel.Builder("your_model").build();
    FirebaseModelInterpreterOptions options =
            new FirebaseModelInterpreterOptions.Builder(remoteModel).build();
    FirebaseModelInterpreter interpreter = FirebaseModelInterpreter.getInstance(options);

#### After

### Kotlin

    val remoteModel = FirebaseCustomRemoteModel.Builder("your_model").build()
    FirebaseModelManager.getInstance().getLatestModelFile(remoteModel)
        .addOnCompleteListener { task ->
            val modelFile = task.getResult()
            if (modelFile != null) {
                // Instantiate an org.tensorflow.lite.Interpreter object.
                interpreter = Interpreter(modelFile)
            }
        }

### Java

    FirebaseCustomRemoteModel remoteModel =
            new FirebaseCustomRemoteModel.Builder("your_model").build();
    FirebaseModelManager.getInstance().getLatestModelFile(remoteModel)
            .addOnCompleteListener(new OnCompleteListener<File>() {
                @Override
                public void onComplete(@NonNull Task<File> task) {
                    File modelFile = task.getResult();
                    if (modelFile != null) {
                        // Instantiate an org.tensorflow.lite.Interpreter object.
                        Interpreter interpreter = new Interpreter(modelFile);
                    }
                }
            });

## 3. Update input and output preparation code

With `FirebaseModelInterpreter`, you specify the model's input and output shapes
by passing a `FirebaseModelInputOutputOptions` object to the interpreter when
you run it.

For the TensorFlow Lite interpreter, you instead allocate `ByteBuffer` objects
with the right size for your model's input and output.

For example, if your model has an input shape of \[1 224 224 3\] `float` values
and an output shape of \[1 1000\] `float` values, make these changes:

#### Before

### Kotlin

    val inputOutputOptions = FirebaseModelInputOutputOptions.Builder()
        .setInputFormat(0, FirebaseModelDataType.FLOAT32, intArrayOf(1, 224, 224, 3))
        .setOutputFormat(0, FirebaseModelDataType.FLOAT32, intArrayOf(1, 1000))
        .build()

    val input = ByteBuffer.allocateDirect(224*224*3*4).order(ByteOrder.nativeOrder())
    // Then populate with input data.

    val inputs = FirebaseModelInputs.Builder()
        .add(input)
        .build()

    interpreter.run(inputs, inputOutputOptions)
        .addOnSuccessListener { outputs ->
            // ...
        }
        .addOnFailureListener {
            // Task failed with an exception.
            // ...
        }

### Java

    FirebaseModelInputOutputOptions inputOutputOptions =
            new FirebaseModelInputOutputOptions.Builder()
                    .setInputFormat(0, FirebaseModelDataType.FLOAT32, new int[]{1, 224, 224, 3})
                    .setOutputFormat(0, FirebaseModelDataType.FLOAT32, new int[]{1, 1000})
                    .build();

    float[][][][] input = new float[1][224][224][3];
    // Then populate with input data.

    FirebaseModelInputs inputs = new FirebaseModelInputs.Builder()
            .add(input)
            .build();

    interpreter.run(inputs, inputOutputOptions)
            .addOnSuccessListener(
                    new OnSuccessListener<FirebaseModelOutputs>() {
                        @Override
                        public void onSuccess(FirebaseModelOutputs result) {
                            // ...
                        }
                    })
            .addOnFailureListener(
                    new OnFailureListener() {
                        @Override
                        public void onFailure(@NonNull Exception e) {
                            // Task failed with an exception
                            // ...
                        }
                    });

#### After

### Kotlin

    val inBufferSize = 1 * 224 * 224 * 3 * java.lang.Float.SIZE / java.lang.Byte.SIZE
    val inputBuffer = ByteBuffer.allocateDirect(inBufferSize).order(ByteOrder.nativeOrder())
    // Then populate with input data.

    val outBufferSize = 1 * 1000 * java.lang.Float.SIZE / java.lang.Byte.SIZE
    val outputBuffer = ByteBuffer.allocateDirect(outBufferSize).order(ByteOrder.nativeOrder())

    interpreter.run(inputBuffer, outputBuffer)

### Java

    int inBufferSize = 1 * 224 * 224 * 3 * java.lang.Float.SIZE / java.lang.Byte.SIZE;
    ByteBuffer inputBuffer =
            ByteBuffer.allocateDirect(inBufferSize).order(ByteOrder.nativeOrder());
    // Then populate with input data.

    int outBufferSize = 1 * 1000 * java.lang.Float.SIZE / java.lang.Byte.SIZE;
    ByteBuffer outputBuffer =
            ByteBuffer.allocateDirect(outBufferSize).order(ByteOrder.nativeOrder());

    interpreter.run(inputBuffer, outputBuffer);

## 4. Update output handling code

Finally, instead of getting the model's output with the `FirebaseModelOutputs`
object's `getOutput()` method, convert the `ByteBuffer` output to whatever
structure is convenient for your use case.

For example, if you're doing classification, you might make changes like the
following:

#### Before

### Kotlin

    val output = result.getOutput(0)
    val probabilities = output[0]
    try {
        val reader = BufferedReader(InputStreamReader(assets.open("custom_labels.txt")))
        for (probability in probabilities) {
            val label: String = reader.readLine()
            println("$label: $probability")
        }
    } catch (e: IOException) {
        // File not found?
    }

### Java

    float[][] output = result.getOutput(0);
    float[] probabilities = output[0];
    try {
        BufferedReader reader = new BufferedReader(
              new InputStreamReader(getAssets().open("custom_labels.txt")));
        for (float probability : probabilities) {
            String label = reader.readLine();
            Log.i(TAG, String.format("%s: %1.4f", label, probability));
        }
    } catch (IOException e) {
        // File not found?
    }

#### After

### Kotlin

    modelOutput.rewind()
    val probabilities = modelOutput.asFloatBuffer()
    try {
        val reader = BufferedReader(
                InputStreamReader(assets.open("custom_labels.txt")))
        for (i in probabilities.capacity()) {
            val label: String = reader.readLine()
            val probability = probabilities.get(i)
            println("$label: $probability")
        }
    } catch (e: IOException) {
        // File not found?
    }

### Java

    modelOutput.rewind();
    FloatBuffer probabilities = modelOutput.asFloatBuffer();
    try {
        BufferedReader reader = new BufferedReader(
                new InputStreamReader(getAssets().open("custom_labels.txt")));
        for (int i = 0; i < probabilities.capacity(); i++) {
            String label = reader.readLine();
            float probability = probabilities.get(i);
            Log.i(TAG, String.format("%s: %1.4f", label, probability));
        }
    } catch (IOException e) {
        // File not found?
    }