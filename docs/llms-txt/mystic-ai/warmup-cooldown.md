# Source: https://docs.mystic.ai/docs/warmup-cooldown.md

# Warmup & Cooldown

Notify Mystic that you either want a pipeline to start caching, or you're done with it and want it to scale to 0!

When you have predictable user behaviour in your product, or just want a model to scale up/down, you can drastically reduce costs while improving your user experience by making sure models are ready or completely down.

Mystic offers two endpoints to achieve this:

* Warmup - `/v4/pipelines/{pipeline_id}/warmup`
* Cooldown`/v4/pipelines/{pipeline_id}/cooldown`

## Warmup

The warmup endpoint overrides the minimum nodes count for a given pipeline. You can view the API reference [here](https://docs.mystic.ai/reference/pipeline_warmup_v4_pipelines__pipeline_id__warmup_post)

It takes in the following input:

```json
{
  "minimum_nodes": 1,
  "duration": 60
}
```

* `minimum_nodes: int`: The minimum number of nodes to have for the pipeline
* `duration: int` (`default=300)`: The number of seconds to have the minimum number nodes up for

*Note: This controls the minimum number of nodes, so if you start performing runs that require more nodes for a pipeline it will scale up as needed*

Example request to warmup SDXL on 2 nodes for 10minutes:

```shell
curl --request POST \
     --url https://www.mystic.ai/v4/pipelines/pipeline_8e79f00bfcbc4d00869fa3650060fb52/warmup \
     --header 'content-type: application/json' \
     --data '
{
  "minimum_nodes": 2,
  "duration": 600
}
'
```

## Cooldown

The cooldown endpoint overrides the maximum nodes count for a given pipeline. You can view the API reference [here](https://docs.mystic.ai/reference/pipeline_cooldown_v4_pipelines__pipeline_id__cooldown_post).

It takes in the following input:

```json
{
  "duration": 60
}
```

* `duration: int` (`default=1800)`: The number of seconds force no nodes

> 📘 Runs will reset cooldowns
>
> Cooldowns control the maximum number of nodes, so if you start performing runs it will scale up a pipeline as needed and default back to your set scaling configuration removing the cooldown

```shell
curl --request POST \
     --url https://www.mystic.ai/v4/pipelines/pipeline_8e79f00bfcbc4d00869fa3650060fb52/cooldown \
     --header 'content-type: application/json' \
     --data '{"duration":10}'
```