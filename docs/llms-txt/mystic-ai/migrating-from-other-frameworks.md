# Source: https://docs.mystic.ai/docs/migrating-from-other-frameworks.md

# Migrating from other frameworks

# Running Cog (Replicate) models on Mystic

> 📘 This feature requires pipeline-ai >= 2.8.0

> 🚧 Note that this functionality is still experimental
>
> There are some limitations currently:
>
> * ~~It does not yet support Turbo Registry (coming soon!)~~
> * File inputs are only supported if the input is a URL

If you have a [Cog](https://github.com/replicate/cog) model that you want to run on Mystic, you can convert it to a Mystic pipeline by following these steps:

1. Firstly ensure you have the `cog` executable on your machine
2. Navigate to the your code's source directory (the one where your `cog.yaml` lives)
3. Use the `convert` CLI command: `pipeline container convert --type=cog -n <pipeline_name>`
4. The above command will generate a `pipeline.yaml` file. You will need to edit this file to set things such as `accelerators`.
   1. One additional config you may want to check is `extras.model_framework.save_output_files` - if this is set to `true` any file data returned by Cog will uploaded as an output file, if not, the file data will be returned directly as a base64 encoded string.
5. Assuming you have the necessary compute resources, you should be able to test out your pipeline locally using `pipeline container up`
6. Push your pipeline as usual using `pipeline container push`

## Using Turbo Registry

To use the Turbo Registry, simply update your `pipeline.yaml` file to include `  turbo_registry: true` inside the `extras` field before running `pipeline container push`. Example:

```yaml
extras:
  turbo_registry: true
  model_framework:
    framework: cog
    save_output_files: true
```

Note that you'll need to be on a plan that supports Turbo Registry to use this feature.