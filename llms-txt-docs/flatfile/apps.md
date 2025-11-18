# Source: https://flatfile.com/docs/core-concepts/apps.md

# Apps

> The anatomy of an App

## Apps

Apps are an organizational unit in Flatfile, designed to manage and coordinate data import workflows across different environments. They serve as containers for organizing related Spaces and provide a consistent configuration that can be deployed across your development pipeline.

Apps can be given [namespaces](/guides/namespaces-and-filters#app-namespaces) to isolate different parts of your application and control which [listeners](/core-concepts/listeners) receive events from which spaces.

<Frame caption="App settings modal">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/flatfileinc/core-concepts/assets/app-settings.png" width="400" />
</Frame>

Apps are available across Development-level environments by default, and optionally available across Production environments with a configuration option:

<Frame caption="Production Environment checkbox">
  <img src="https://mintlify.s3.us-west-1.amazonaws.com/flatfileinc/getting-started/quickstart/assets/apps_show_in_production_environments.png" width="275" />
</Frame>
