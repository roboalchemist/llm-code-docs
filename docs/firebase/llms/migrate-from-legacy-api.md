# Source: https://firebase.google.com/docs/ml/android/migrate-from-legacy-api.md.txt

# Source: https://firebase.google.com/docs/ml/ios/migrate-from-legacy-api.md.txt

<br />

Version 0.20.0 of the`Firebase/MLModelInterpreter`library introduces a new`getLatestModelFilePath()`method, which gets the location on the device of custom models. You can use this method to directly instantiate a TensorFlow Lite`Interpreter`object, which you can use instead of Firebase's`ModelInterpreter`wrapper.

Going forward, this is the preferred approach. Because the TensorFlow Lite interpreter version is no longer coupled with the Firebase library version, you have more flexibility to upgrade to new versions of TensorFlow Lite when you want, or more easily use custom TensorFlow Lite builds.

This page shows how you can migrate from using`ModelInterpreter`to the TensorFlow Lite`Interpreter`.

## 1. Update project dependencies

Update your project's Podfile to include version 0.20.0 of the`Firebase/MLModelInterpreter`library (or newer) and the TensorFlow Lite library:

#### Before

### Swift

    pod 'Firebase/MLModelInterpreter', '0.19.0'

### Objective-C

    pod 'Firebase/MLModelInterpreter', '0.19.0'

#### After

### Swift

    pod 'Firebase/MLModelInterpreter', '~> 0.20.0'
    pod 'TensorFlowLiteSwift'

### Objective-C

    pod 'Firebase/MLModelInterpreter', '~> 0.20.0'
    pod 'TensorFlowLiteObjC'

## 2. Create a TensorFlow Lite interpreter instead of a Firebase ModelInterpreter

Instead of creating a Firebase`ModelInterpreter`, get the model's location on device with`getLatestModelFilePath()`and use it to create a TensorFlow Lite`Interpreter`.

#### Before

### Swift

    let remoteModel = CustomRemoteModel(
        name: "your_remote_model"  // The name you assigned in the Firebase console.
    )
    interpreter = ModelInterpreter.modelInterpreter(remoteModel: remoteModel)

### Objective-C

    // Initialize using the name you assigned in the Firebase console.
    FIRCustomRemoteModel *remoteModel =
            [[FIRCustomRemoteModel alloc] initWithName:@"your_remote_model"];
    interpreter = [FIRModelInterpreter modelInterpreterForRemoteModel:remoteModel];

#### After

### Swift

    let remoteModel = CustomRemoteModel(
        name: "your_remote_model"  // The name you assigned in the Firebase console.
    )
    ModelManager.modelManager().getLatestModelFilePath(remoteModel) { (remoteModelPath, error) in
        guard error == nil, let remoteModelPath = remoteModelPath else { return }
        do {
            interpreter = try Interpreter(modelPath: remoteModelPath)
        } catch {
            // Error?
        }
    }

### Objective-C

    FIRCustomRemoteModel *remoteModel =
            [[FIRCustomRemoteModel alloc] initWithName:@"your_remote_model"];
    [[FIRModelManager modelManager] getLatestModelFilePath:remoteModel
                                                completion:^(NSString * _Nullable filePath,
                                                             NSError * _Nullable error) {
        if (error != nil || filePath == nil) { return; }

        NSError *tfError = nil;
        interpreter = [[TFLInterpreter alloc] initWithModelPath:filePath error:&tfError];
    }];

## 3. Update input and output preparation code

With`ModelInterpreter`, you specify the model's input and output shapes by passing a`ModelInputOutputOptions`object to the interpreter when you run it.

For the TensorFlow Lite interpreter, you instead call`allocateTensors()`to allocate space for the model's input and output, then copy your input data to the input tensors.

For example, if your model has an input shape of \[1 224 224 3\]`float`values and an output shape of \[1 1000\]`float`values, make these changes:

#### Before

### Swift

    let ioOptions = ModelInputOutputOptions()
    do {
        try ioOptions.setInputFormat(
            index: 0,
            type: .float32,
            dimensions: [1, 224, 224, 3]
        )
        try ioOptions.setOutputFormat(
            index: 0,
            type: .float32,
            dimensions: [1, 1000]
        )
    } catch let error as NSError {
        print("Failed to set input or output format with error: \(error.localizedDescription)")
    }

    let inputs = ModelInputs()
    do {
        let inputData = Data()
        // Then populate with input data.

        try inputs.addInput(inputData)
    } catch let error {
        print("Failed to add input: \(error)")
    }

    interpreter.run(inputs: inputs, options: ioOptions) { outputs, error in
        guard error == nil, let outputs = outputs else { return }
        // Process outputs
        // ...
    }

### Objective-C

    FIRModelInputOutputOptions *ioOptions = [[FIRModelInputOutputOptions alloc] init];
    NSError *error;
    [ioOptions setInputFormatForIndex:0
                                 type:FIRModelElementTypeFloat32
                           dimensions:@[@1, @224, @224, @3]
                                error:&error];
    if (error != nil) { return; }
    [ioOptions setOutputFormatForIndex:0
                                  type:FIRModelElementTypeFloat32
                            dimensions:@[@1, @1000]
                                 error:&error];
    if (error != nil) { return; }

    FIRModelInputs *inputs = [[FIRModelInputs alloc] init];
    NSMutableData *inputData = [[NSMutableData alloc] initWithCapacity:0];
    // Then populate with input data.

    [inputs addInput:inputData error:&error];
    if (error != nil) { return; }

    [interpreter runWithInputs:inputs
                       options:ioOptions
                    completion:^(FIRModelOutputs * _Nullable outputs,
                                 NSError * _Nullable error) {
      if (error != nil || outputs == nil) {
        return;
      }
      // Process outputs
      // ...
    }];

#### After

### Swift

    do {
        try interpreter.allocateTensors()

        let inputData = Data()
        // Then populate with input data.

        try interpreter.copy(inputData, toInputAt: 0)

        try interpreter.invoke()
    } catch let err {
        print(err.localizedDescription)
    }

### Objective-C

    NSError *error = nil;

    [interpreter allocateTensorsWithError:&error];
    if (error != nil) { return; }

    TFLTensor *input = [interpreter inputTensorAtIndex:0 error:&error];
    if (error != nil) { return; }

    NSMutableData *inputData = [[NSMutableData alloc] initWithCapacity:0];
    // Then populate with input data.

    [input copyData:inputData error:&error];
    if (error != nil) { return; }

    [interpreter invokeWithError:&error];
    if (error != nil) { return; }

## 4. Update output handling code

Finally, instead of getting the model's output with the`ModelOutputs`object's`output()`method, get the output tensor from the interpreter and convert its data to whatever structure is convenient for your use case.

For example, if you're doing classification, you might make changes like the following:

#### Before

### Swift

    let output = try? outputs.output(index: 0) as? [[NSNumber]]
    let probabilities = output?[0]

    guard let labelPath = Bundle.main.path(
        forResource: "custom_labels",
        ofType: "txt"
    ) else { return }
    let fileContents = try? String(contentsOfFile: labelPath)
    guard let labels = fileContents?.components(separatedBy: "\n") else { return }

    for i in 0 ..< labels.count {
        if let probability = probabilities?[i] {
            print("\(labels[i]): \(probability)")
        }
    }

### Objective-C

    // Get first and only output of inference with a batch size of 1
    NSError *error;
    NSArray *probabilites = [outputs outputAtIndex:0 error:&error][0];
    if (error != nil) { return; }

    NSString *labelPath = [NSBundle.mainBundle pathForResource:@"retrained_labels"
                                                        ofType:@"txt"];
    NSString *fileContents = [NSString stringWithContentsOfFile:labelPath
                                                       encoding:NSUTF8StringEncoding
                                                          error:&error];
    if (error != nil || fileContents == NULL) { return; }
    NSArray<NSString *> *labels = [fileContents componentsSeparatedByString:@"\n"];
    for (int i = 0; i < labels.count; i++) {
        NSString *label = labels[i];
        NSNumber *probability = probabilites[i];
        NSLog(@"%@: %f", label, probability.floatValue);
    }

#### After

### Swift

    do {
        // After calling interpreter.invoke():
        let output = try interpreter.output(at: 0)
        let probabilities =
                UnsafeMutableBufferPointer<Float32>.allocate(capacity: 1000)
        output.data.copyBytes(to: probabilities)

        guard let labelPath = Bundle.main.path(
            forResource: "custom_labels",
            ofType: "txt"
        ) else { return }
        let fileContents = try? String(contentsOfFile: labelPath)
        guard let labels = fileContents?.components(separatedBy: "\n") else { return }

        for i in labels.indices {
            print("\(labels[i]): \(probabilities[i])")
        }
    } catch let err {
        print(err.localizedDescription)
    }

### Objective-C

    NSError *error = nil;

    TFLTensor *output = [interpreter outputTensorAtIndex:0 error:&error];
    if (error != nil) { return; }

    NSData *outputData = [output dataWithError:&error];
    if (error != nil) { return; }

    Float32 probabilities[outputData.length / 4];
    [outputData getBytes:&probabilities length:outputData.length];

    NSString *labelPath = [NSBundle.mainBundle pathForResource:@"custom_labels"
                                                        ofType:@"txt"];
    NSString *fileContents = [NSString stringWithContentsOfFile:labelPath
                                                       encoding:NSUTF8StringEncoding
                                                          error:&error];
    if (error != nil || fileContents == nil) { return; }

    NSArray<NSString *> *labels = [fileContents componentsSeparatedByString:@"\n"];
    for (int i = 0; i < labels.count; i++) {
        NSLog(@"%@: %f", labels[i], probabilities[i]);
    }