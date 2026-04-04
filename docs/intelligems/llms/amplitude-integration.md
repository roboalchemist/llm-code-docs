# Source: https://docs.intelligems.io/integrations/amplitude-integration.md

# Amplitude Integration

Intelligems can send an event to Amplitude when a visitor first enters into an experiment. The event has the name `ig_impression` , and parameters `variation` (which includes both the experiment and test group name) and `experiment` (which has the experiment name).

### Additional settings

By default, Intelligems will send an event to Amplitude only once per visitor per experiment. You can change this by choosing a `trackMode` in a `window.igSettings` object. For example:

```html
<script>
window.igSettings = {
    integrations: {
        amplitude: {
            trackMode: "assignment" // default, track on assignment
        }
    }
}
</script>
```

Track mode options are:

* `impression` (send event on every page view for each experiment)
* `assignment` (default, send event only once per visitor per experiment, on assignment)
* `timed` (send event once per visitor per experiment, re-sending after a specified amount of time has passed)
  * `timeSinceAssignment` additional setting, in seconds, that controls the time threshold, defaults to 1800 (30 minutes)

For example, to send the event once per visitor per experiment, and re-send it after at least 60 minutes has passed:

```html
<script>
window.igSettings = {
    integrations: {
        amplitude: {
            trackMode: "timed",
            timeSinceAssignment: 3600// re-send after an hour has passed
        }
    }
}
</script>
```
