# Source: https://docs.statsig.com/statsig-warehouse-native/features/filtering-exposures.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.statsig.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Filter Exposures

## Filter Exposures by Qualifying Event

You can use Qualifying Events to filter exposures to units who did or did not trigger an event after being exposed. This is a powerful tool, especially for analysis-only experiments where the assignment tool may have over-exposed units (e.g. assigning units on page load when the intervention was only triggered when a button was clicked).

<Frame>
  <img src="https://mintcdn.com/statsig-4b2ff144/DbEV6mNxirwT8Ol0/images/statsig-warehouse-native/features/filtering-exposures/f7a5ee06-b67a-4cba-9680-fbe99c64d0fc.png?fit=max&auto=format&n=DbEV6mNxirwT8Ol0&q=85&s=5622f8fceb870770f9dcf44b4d1789db" alt="Qualifying event filter configuration interface" width="1537" height="382" data-path="images/statsig-warehouse-native/features/filtering-exposures/f7a5ee06-b67a-4cba-9680-fbe99c64d0fc.png" />
</Frame>

We recommend caution using this tool, as it's possible to introduce post-assignment data into your assignment data, biasing results. Because of this, qualifying Event filters are disabled on Assign and Analyze experiments by default, since with the Statsig SDK experiments are usually not overexposed. The Statsig team can turn this feature on by request if you have a use case for it!

There are a few settings:

* Qualifying Event: the event source to qualify exposures with. This can be filtered, so you can pick specific target events within a qualifying event source
* Exclude matching units: whether to include, or exclude units who triggered the event
* Use qualifying event timestamp for first exposures: if the actual intervention occurred when the unit triggered the qualifying event, check this so that Statsig knows to override the exposure timestamp with the qualifying event timestamp
* Filter events by time window: restrict the qualifying event matching to events that happened within X days/minutes of the unit's exposure event

## Filter Assignment Source

You can also filter exposures to units based on the columns in assignment source. You can directly use certain columns, as well as apply filters on top of that.

Similar to filtering by qualifying event, we recommend using this tool carefully because it can artificially introduce bias to the experiment results.

<img width="1169" alt="Assignment source filter selection UI" src="https://mintcdn.com/statsig-4b2ff144/DbEV6mNxirwT8Ol0/images/statsig-warehouse-native/features/filtering-exposures/36ddb74f-d9e9-4e25-8349-61077f77b863.png?fit=max&auto=format&n=DbEV6mNxirwT8Ol0&q=85&s=56ae231c1c42fc05abbf3751cb062a62" data-path="images/statsig-warehouse-native/features/filtering-exposures/36ddb74f-d9e9-4e25-8349-61077f77b863.png" />


Built with [Mintlify](https://mintlify.com).