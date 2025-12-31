# Source: https://firebase.google.com/docs/ml-kit/ios/use-custom-tflite.md.txt

# Source: https://firebase.google.com/docs/ml-kit/android/use-custom-tflite.md.txt

<br />

| This page describes an old version ofFirebase ML. In the newest version, you can use any version of TensorFlow Lite that works with your custom models, so the procedure below is unnecessary.

If you're an experienced ML developer and the pre-built TensorFlow Lite library doesn't meet your needs, you can use a custom[TensorFlow Lite](https://www.tensorflow.org/mobile/tflite/)build with ML Kit. For example, you may want to add custom ops.

## Prerequisites

- A working[TensorFlow Lite](https://github.com/tensorflow/tensorflow/blob/master/tensorflow/lite/README.md#building-tensorflow-lite-and-the-demo-app-from-source)build environment

## Bundling a custom TensorFlow Lite for Android

Build the Tensorflow Lite AAR:  

```
bazel build --cxxopt='--std=c++11' -c opt        \
  --fat_apk_cpu=x86,x86_64,arm64-v8a,armeabi-v7a   \
  //tensorflow/lite/java:tensorflow-lite
```

This will generate an AAR file in`bazel-genfiles/tensorflow/lite/java/`. Publish the custom Tensorflow Lite AAR to your local[Maven](https://maven.apache.org/download.cgi)repository:  

```
mvn install:install-file -Dfile=bazel-genfiles/tensorflow/lite/java/tensorflow-lite.aar -DgroupId=org.tensorflow \
  -DartifactId=tensorflow-lite -Dversion=0.1.100 -Dpackaging=aar
```

Finally, in your app`build.gradle`, override Tensorflow Lite with your custom version:  

    implementation 'org.tensorflow:tensorflow-lite:0.1.100'