# Source: https://firebase.google.com/docs/ml-kit/ios/use-custom-tflite.md.txt

> [!CAUTION]
> This page describes an old version of Firebase ML. In the newest
> version, you can use any version of TensorFlow Lite that works with your
> custom models, so the procedure below is unnecessary.

If you're an experienced ML developer and the pre-built TensorFlow Lite
library doesn't meet your needs, you can use a custom
[TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/) build with ML Kit. For
example, you may want to add custom ops.

## Prerequisites

- A working [TensorFlow Lite](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/README.md#building-tensorflow-lite-and-the-demo-app-from-source) build environment
- A checkout of TensorFlow Lite 1.10.1

You can check out the correct version using Git:

    git checkout -b work
    git reset --hard tflite-v1.10.1
    git cherry-pick 4dcfddc5d12018a5a0fdca652b9221ed95e9eb23

## Building the Tensorflow Lite library

1. Build Tensorflow Lite (with your modifications) following the [standard instructions](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/g3doc/guide/build_ios.md)
2. Build the framework:

```
tensorflow/lite/lib_package/create_ios_frameworks.sh
```

The generated framework can be found at `tensorflow/lite/gen/ios_frameworks/tensorflow_lite.framework.zip`

> [!NOTE]
> **Note:** There have been [build issues
> reported](https://github.com/tensorflow/tensorflow/issues/18356) with Xcode 9.3

## Creating a local pod

1. Create a directory for your local pod
2. Run `pod lib create TensorFlowLite` in the directory you created
3. Create a `Frameworks` directory inside the `TensorFlowLite` directory
4. Unzip the `tensorflow_lite.framework.zip` file generated above
5. Copy the unzipped `tensorflow_lite.framework` to `TensorFlowLite/Frameworks`
6. Modify the generated `TensorFlowLite/TensorFlowLite.podspec` to reference the library:

        Pod::Spec.new do |s|
          s.name             = 'TensorFlowLite'
          s.version          = '0.1.7' # Version must match.
          s.ios.deployment_target = '9.0'
          
          # ... make other changes as desired
          
          internal_pod_root = Pathname.pwd
          s.frameworks = 'Accelerate'
          s.libraries = 'c++'
          s.vendored_frameworks = 'Frameworks/tensorflow_lite.framework'

          s.pod_target_xcconfig = {
            'SWIFT_VERSION' => '4.0',
            'INTERNAL_POD_ROOT' => "#{internal_pod_root}",
            'HEADER_SEARCH_PATHS' => "$(inherited) '${INTERNAL_POD_ROOT}/Frameworks/tensorflow_lite.framework/Headers'",
            'OTHER_LDFLAGS' => "-force_load '${INTERNAL_POD_ROOT}/Frameworks/tensorflow_lite.framework/tensorflow_lite'"
          }
        end

## Referencing the custom pod in your project

You can include the custom pod by referencing it directly from your app's
`Podfile`:

    pod 'Firebase/MLModelInterpreter'
    pod 'TensorFlowLite', :path => 'path/to/your/TensorflowLite'

For other options for managing private pods, see
[Private Pods](https://guides.cocoapods.org/making/private-cocoapods.html) in
the Cocoapods documentation. Note that the version must exactly match, and you
should reference this version when including the pod from your
private repository, e.g. `pod 'TensorFlowLite', "1.10.1"`.