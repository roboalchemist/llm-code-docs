# Source: https://docs.roboflow.com/changelog/explore-by-month/november-2025/run-workflows-on-camera-streams-from-the-web.md

# Run Workflows on Camera Streams from the Web

{% embed url="<https://www.loom.com/share/48b7c442a69c49e081d0dbec49e1ab57>" %}

You can now run Workflows on live camera streams from the web via WebRTC.

This feature works by opening up a streaming connection to the Roboflow Serverless API. The Roboflow Cloud will run your Workflow on frames from the stream, then return the results back to your application.

Our [Inference Sample App](https://github.com/roboflow/inferenceSampleApp), built with JavaScript has all the components you need to run a Roboflow Workflow from a web application. This includes installation steps, camera setup, and instructions on how to configure a back-end proxy through which to relay requests from your front-end application.

You can see all of the documentation for this feature in the [Roboflow Web Browser Deployment documentation](https://docs.roboflow.com/deploy/sdks/web-browser#real-time-streaming-with-roboflow-inference-sdk).
