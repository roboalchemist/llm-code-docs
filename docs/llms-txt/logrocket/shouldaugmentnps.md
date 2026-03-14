# Source: https://docs.logrocket.com/reference/shouldaugmentnps.md

# Add Session Links to NPS

Control whether or not LogRocket session URLs are included in NPS survey responses

## Disable inclusion of session links in Delighted and Wootric survey responses

#### `shouldAugmentNPS` - Boolean

##### optional (default - `true`)

When a user responds to a [Delighted](https://docs.logrocket.com/docs/delighted) or [Wootric](https://docs.logrocket.com/docs/wootric) survey in your application, LogRocket will append the URL for the user's current session to the survey response (feedback) text.

If you want to disable this feature, add this option to your configuration:

```javascript
LogRocket.init(YOUR_APP_ID, {
  shouldAugmentNPS: false,
});
```