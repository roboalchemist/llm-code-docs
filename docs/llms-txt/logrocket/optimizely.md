# Source: https://docs.logrocket.com/docs/optimizely.md

# Optimizely

Integrating LogRocket with [Optimizely](https://www.optimizely.com/)

If you are using Optimizely to run A/B tests, you can use LogRocket to gain deeper insights into the differences between your experiment groups.

Set up your experiments and variations in Optimizely as normal. Take note of the experiment and variation IDs. See [here](https://docs.developers.optimizely.com/web-experimentation/docs/locate-ids-used-for-apis) for more information about locating the IDs. You can also access information about the experiments and variations selected for a user using Optimizely's JavaScript API, which is available on the global `window.optimizely` object once the Optimizely snippet has loaded. For more details, see [here](https://docs.developers.optimizely.com/web-experimentation/reference/state).

Pass information about the experiments and variations selected for a user to LogRocket using [`LogRocket.track()`](https://docs.logrocket.com/reference/track) . For example:

```javascript
LogRocket.track(EXPERIMENT_NAME, {
  variantName: VARIANT_NAME,
});
```

Then, within LogRocket, you can search for custom events and save filters to create buckets of sessions within a particular group based on experiment and variation:

![](https://files.readme.io/07922e5-Image_2022-08-12_at_1.09.21_PM.jpg "Image 2022-08-12 at 1.09.21 PM.jpg")