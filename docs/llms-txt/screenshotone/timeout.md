# Source: https://screenshotone.com/docs/errors/timeout/

# Timeout Error

It is an API error returned when the API can't render screenshots or video within the specified timeout:

```json
{
  "is_successful": false,
  "error_code": "timeout_error",
  "error_message": "The screenshot couldn't be taken within the specified timeout. Either the site doesn't respond quickly, or rendering takes longer than expected. Play with the `timeout` or the `navigation_timeout` options or reach the support for the investigation.",
  "documentation_url": "https://screenshotone.com/docs/errors/"
}
```

## Reasons and how to fix

Let's quickly consider possible reasons and possible solutions.

### Timeout is too small

By default, the timeout is about 60 seconds. You must fit your rendering request within that timeout.

You can:

Either use asynchronous requests and webhooks to get the results. And set the timeout up to 300 seconds.
Or you can try to increase the timeout up to 90 seconds.

### Delay is too big

Make sure that your delay is not too big, e.g. if you set it to 30 seconds, and it takes the website to load for 30 seconds, it is better to decrease the delay.

### A website is not loading properly

Some sites just take too much time to load or they don't emit DOMContentLoaded events.

Try to play with different values of [the wait_until option]() and see if it helps.

### Long duration of the video

Often when you record a video of a long duration, the API must not respond in time. Since it takes to both record a video and stream it.

Try to decrease the video duration you are recording, it might help.

## Reach out to support

If nothing helps you, please, reach out to `support@screenshotone.com` and we will try to help you as fast as possible.