# Source: https://upstash.com/docs/common/account/costexplorer.md

# Cost Explorer

The Cost Explorer pages allow you to view your current and previous months’ costs. To access the Cost Explorer, navigate to the left menu and select Account > Cost Explorer. Below is an example report:

<Frame>
  <img src="https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/costexplorer/costexplorer.png?fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=334bd9ff88b617ad2ff32b20a3a61dfd" data-og-width="2096" width="2096" data-og-height="1118" height="1118" data-path="img/costexplorer/costexplorer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/costexplorer/costexplorer.png?w=280&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=ac8adc206a255dcc4ad82a8c587b8e0e 280w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/costexplorer/costexplorer.png?w=560&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=684c64dddffae9a5bd894d447114c9e0 560w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/costexplorer/costexplorer.png?w=840&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=2eb1b8f3a8e3a263eb0e70aa3da4f601 840w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/costexplorer/costexplorer.png?w=1100&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=aba07654a32cfedacf05456c6875a20c 1100w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/costexplorer/costexplorer.png?w=1650&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=f11730619209988320c08c52fc6a9a11 1650w, https://mintcdn.com/upstash/ZVIIe-nWA4-ORRYS/img/costexplorer/costexplorer.png?w=2500&fit=max&auto=format&n=ZVIIe-nWA4-ORRYS&q=85&s=5384167a9557b39c2db10a8976967298 2500w" />
</Frame>

You can select a specific month to view the cost breakdown for that period. Here's the explanation of the fields in the report:

**Request:** This represents the total number of requests sent to the database.

**Storage:** This indicates the average size of the total storage consumed. Upstash database includes a persistence layer for data durability. For example, if you have 1 GB of data in your database throughout the entire month, this value will be 1 GB. Even if your database is empty for the first 29 days of the month and then expands to 30 GB on the last day, this value will still be 1 GB.

**Cost:** This field represents the total cost of your database in US Dollars.

> The values for the current month is updated hourly, so values can be stale up
> to 1 hour.
