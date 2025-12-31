# Source: https://docs.intelligems.io/integrations/segment-integration.md

# Segment Integration

Intelligems can send an event to Segment when a visitor first enters into an experiment. The event has the name `Experiment Viewed` , and parameters `variation` (which includes both the experiment and test group name), `variationId`, `experiment` (which has the experiment name) and `experimentId`.

By default, Intelligems will send an event to Segment on every page view for each live experiment.

### Additional settings

By default, Intelligems will send an event to Segment on every page view for each live experiment. You can change this by choosing a `trackMode` in a `window.igSettings` object. For example:

```html
<script>
window.igSettings = {
    integrations: {
        segment: {
            trackMode: "impression" // default, track on every page view
        }
    }
}
</script>
```

Track mode options are:

* `impression` (default, send event on every page view for each experiment)
* `assignment` (send event only once per visitor per experiment, on assignment)
* `timed` (send event once per visitor per experiment, re-sending after a specified amount of time has passed)
  * `timeSinceAssignment` additional setting, in seconds, that controls the time threshold, defaults to 1800 (30 minutes)

For example, to send the event once per visitor per experiment, and re-send it after at least 60 minutes has passed:

```html
<script>
window.igSettings = {
    integrations: {
        segment: {
            trackMode: "timed",
            timeSinceAssignment: 3600 // re-send after an hour has passed
        }
    }
}
</script>
```
