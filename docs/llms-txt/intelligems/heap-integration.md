# Source: https://docs.intelligems.io/integrations/heap-integration.md

# Heap Integration

Intelligems can send a custom event to Heap for each experiment impression, with the user's test group ID. The event is sent on each page view, with information about each experiment that's live.

The custom event is called `Intelligems Impression` and has two properties for each experiment:

* `Exp <experiment name>` with value `<test group name>`
* `Var <test group name>` with value `true`

To enable the Heap integration, simple click "Enable" on the integrations page.

### Additional settings

By default, Intelligems will send an event to Heap on every page view for every live experience. You can change this by choosing a `trackMode` in a `window.igSettings` object. For example:

```html
<script>
window.igSettings = {
    integrations: {
        heap: {
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
        heap: {
            trackMode: "timed",
            timeSinceAssignment: 3600 // re-send after an hour has passed
        }
    }
}
</script>
```
