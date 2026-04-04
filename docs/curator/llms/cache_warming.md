# Source: https://docs.curator.interworks.com/site_administration/performance/cache_warming.md

# Source: https://docs.curator.interworks.com/best_practices/performance/cache_warming.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.curator.interworks.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Cache Warming

> Improve initial page load times by pre-warming caches for better user experience

Sometimes the initial page load or log in flow for your users can be very slow. This is because we must perform API
calls to check if the user has permission to see each navigation item related to analytic content. Single API calls are
fast but when your menu is large and many calls must be made it can really anchor the load time.

This feature allows you to choose a select group of Curator users to warm the cache for. This improves the initial page
load and skips the long wait caused by permission checks. The affect is even greater if your menu is very large.

## Setting Up the Group

First, we need to make sure you have a Frontend Group that contains the users needing their cache warmed. This Frontend
Group needs to have less than 200 users because this process is intensive. Increasing the number of users could clog the
queue and hurt performance. We're still playing with the sweet spot for number of users so this may change in the future.

1. Navigate to your Curator backend > Settings > Users > Frontend Groups. If you already have a group with less than
   200 members that contains the users you’d like to receive the speed bump, you’re good to go and can skip to “Setting
   Up the Feature”! Otherwise, hit the “New Frontend Group” button:
2. Give your group a name:
3. Either manually select users in the “Group Members” section or choose a group from one of your analytic platforms in
   the sections below:
4. Hit “Save!”

## Enabling Cache Warming for your Group

1. Navigate to your Curator backend > Settings > Curator > Portal Settings > Features tab:
2. Enable the “Cache Warming” feature at the top of the Functionality section:
3. Choose the Frontend Group we created earlier.
4. Hit “Save!”
