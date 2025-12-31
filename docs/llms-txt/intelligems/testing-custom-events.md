# Source: https://docs.intelligems.io/analytics/custom-events/testing-custom-events.md

# Testing Custom Events

Once you’ve defined a user interaction custom event (like click, scroll, element visible, or custom JS events) there are a few ways you can confirm it’s working as expected. First, it’s often useful to trigger the event yourself — to do this, open an incognito window, navigate to a page where the event can be triggered, and hard refresh your browser (CMD/CTRL + Shift + R in most browsers). The hard refresh ensures that you have the latest Intelligems code running, instead of a recently cached version which may not be aware of the new custom event configuration. Then, complete the user interaction (like a click or scroll) to trigger the event. To confirm it’s working:

## Using the Events Manager

The Events Manager displays the last tracked time and number of occurrences for each custom event that has been triggered within the last 24 hours. This data is close to real-time — it should take about 30 seconds or less for activity happening on the site to be incorporated here. If the event you’re tracking is a page view, you’ll also see the data up-to-date retroactively (i.e., looking back over the last 24 hours, even before the event was defined). For user interaction events like clicks and scrolls, data will start being collected only from the moment you’ve defined the event.

## Use your browser

You can check for the event in your browser’s network traffic to see if it's firing. When a user interaction custom event is triggered, it sends an event that you can see in your browser’s network traffic (note: page view events like “Viewed Product,” “Viewed Collection,” or “Visited URL” rely on Intelligems’ built-in page view tracking and do not send separate events). You can trigger the event and then check for this event in your browser’s network traffic to confirm it’s working. To do this, follow these steps or check out [this Loom video](https://www.loom.com/share/93418eb03e2c4191a0c7e1c0ff6fcbde?sid=898d9766-3c0d-4b96-bab3-7baa1c9ce0be) demonstrating the process:

1. Open an incognito window and navigate to a page where the event can be triggered and hard refresh (CMD/CTRL + Shift + R), as described above. It’s very important to hard refresh and use an incognito window to make sure your browser is receiving the most recent Intelligems configuration.
2. Then, open your browser’s developer tools (in Chrome you can do this with View > Developer > Developer Tools)
3. Open the Network Activity tab
4. Filter to intelligems.io/v3/track
5. Trigger the custom event. If it’s working, you should see a new event pop up. Open it and confirm it looks like the correct event
