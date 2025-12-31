# Storybook Documentation
# Source: https://storybook.js.org/docs/api
# Page: /docs/api

# API references

An overview of all available API references for Storybook.

## 

Configuration

Name| Description  
---|---  
[`main.js|ts`](./api/main-config/main-config)| Storybook's primary configuration file, which specifies your Storybook project's behavior, including the location of your stories, the addons you use, feature flags and other project-specific settings.  
[`preview.js|jsx|ts|tsx`](./configure/#configure-story-rendering)| This configuration file controls the way stories are rendered. You can also use it to run code that applies to all stories.  
[`manager.js|ts`](./configure/#configure-storybooks-ui)| This configuration file controls the behavior of Storybook's UI, the manager.  
[CLI](./api/cli-options)| Storybook is a CLI tool. You can start Storybook in development mode or build a static version of your Storybook.  
  
## 

Stories

Name| Description  
---|---  
[CSF](./api/csf)| Component Story Format (CSF) is the API for writing stories. It's an open standard based on ES6 modules that is portable beyond Storybook.  
[ArgTypes](./api/arg-types)| ArgTypes specify the behavior of [args](./writing-stories/args). By specifying the type of an arg, you constrain the values that it can accept and provide information about args that are not explicitly set.  
[Parameters](./api/parameters)| Parameters are static metadata used to configure your [stories](./get-started/whats-a-story) [addons](./addons) in Storybook. They are specified at the story, meta (component), project (global) levels.  
  
## 

Docs

Name| Description  
---|---  
[Doc blocks](./writing-docs/doc-blocks/#available-blocks)| Storybook offers several doc blocks to help document your components and other aspects of your project.  
  
Was this page useful?

👍👎

[✍️ Edit on Github](https://github.com/storybookjs/storybook/tree/next/docs/api/index.mdx)