# Source: https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/offline-apps

Title: Develop offline-capable canvas apps - Power Apps

URL Source: https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/offline-apps

Markdown Content:
Mobile users often need to be productive even when they have limited or no connectivity. When you build a canvas app, you can perform these tasks:

*   Open Power Apps Mobile and run apps when the device is not connected to the network.
*   Determine when an app is offline, online, or in a metered connection by using the [Connection](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/functions/signals#connection) signal object.
*   Synchronize data between your device and the server.

If your app connects to Dataverse, offline support is [**built-in**](https://learn.microsoft.com/en-us/power-apps/mobile/canvas-mobile-offline-overview). Power Apps will allows you to download data to your device and upload changes back to Dataverse. If your app does not use Dataverse, you can use collections and leverage the [**LoadData** and **SaveData**](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/functions/function-savedata-loaddata) functions for basic storage when offline.

Note

*   Offline capability for canvas apps is available while running the apps using the native [Power Apps Mobile](https://powerapps.microsoft.com/downloads/) players on iOS, Android, and Windows.
*   Canvas apps running in web browsers can't run offline, even when using a web browser on a mobile device.
*   Canvas apps in Teams are limited to 1 MB of data through the LoadData and SaveData functions—useful for a small number of text strings, numbers, and dates. Use of images or other media is inappropriate for this limit. More information: [**LoadData** and **SaveData** function reference](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/functions/function-savedata-loaddata)

For Microsoft Dataverse-based canvas apps, you must use the offline capability built-in with the [offline-first](https://learn.microsoft.com/en-us/power-apps/mobile/canvas-mobile-offline-overview) experience. For more information, see [Set up mobile offline for canvas apps](https://learn.microsoft.com/en-us/power-apps/mobile/canvas-mobile-offline-setup) and [Working with canvas apps offline](https://learn.microsoft.com/en-us/power-apps/mobile/canvas-mobile-offline-working). With the flip of a switch, your app can work with Dataverse data wherever you are, with or without a network connection. Just build your app with standard Power Fx formulas and the offline feature handles all the complexity for you.

This section includes an example using Twitter data. An even simpler example that doesn't require a connection is included in the [**LoadData** and **SaveData** function reference](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/functions/function-savedata-loaddata).

Watch this video to learn how to create offline enabled canvas apps which don't use Dataverse data:

**LoadData** and **SaveData** combine to form a simple mechanism to store small amounts of data on a local device. By using these functions, you can add simple offline capabilities to your app.

These functions are limited by the amount of available app memory because they operate on an in-memory collection. Available memory can vary depending on the device, the operating system, the memory that Power Apps Mobile uses, and the complexity of the app in terms of screens and controls. If you store more than a few megabytes of data, test your app with expected scenarios on the devices on which you expect it to run. You'll generally have 30-70 megabytes of available memory.

The functions also don't automatically resolve merge conflicts when a device comes online. Configuration on what data is saved and how to handle reconnection is up to the maker when writing expressions.

After using **LoadData** to populate a collection, that collection cannot be used to update Dataverse data which includes a lookup field. Doing so will result in the lookup field not being updated.

For updates on offline capabilities, return to this topic, and subscribe to the [Power Apps blog](https://powerapps.microsoft.com/blog/).

When you design offline scenarios, you should first consider how your apps work with data. Apps in Power Apps primarily access data through a set of [connectors](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/connections-list) that the platform provides, such as SharePoint, Office 365, and Microsoft Dataverse. You can also build custom connectors that enable apps to access any service that provides a RESTful endpoint. This could be a Web API or a service such as Azure Functions. All these connectors use HTTPS over the Internet, which means your users must be online for them to access data and any other capabilities that a service offers.

![Image 1: Power Apps with connectors.](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/media/offline-apps/online-app.png)

In Power Apps, you can filter, search, sort, aggregate, and manipulate data in a consistent way regardless of the data source. Sources range from in-memory collections in the app to lists created using Microsoft Lists to SQL databases and Dataverse. Because of this consistency, you can easily retarget an app to use a different data source. More importantly for offline scenarios, you can use local collections for data management with almost no changes to an app's logic. In fact, local collections are the primary mechanism for handling offline data.

To keep the focus on the offline aspects of app development, this topic illustrates a simple scenario focused around Twitter. You'll build an app that enables you to read Twitter posts and submit tweets while being offline. When the app comes online, the app posts tweets and reloads the local data.

At a high level, the app performs these tasks:

*   When the user opens the app:

    *   If the device is online, the app fetches data through the Twitter connector and populates a collection with that data.
    *   If the device is offline, the app loads the data from a local cache file by using the [**LoadData**](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/functions/function-savedata-loaddata) function.
    *   The user can submit tweets. If the app is online, it posts the tweets directly to Twitter and refreshes the local cache.

*   Every five minutes while the app is online:

    *   The app posts any tweets in the local cache.
    *   The app refreshes the local cache and saves it by using the [**SaveData**](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/functions/function-savedata-loaddata) function.

1.   Create a [blank canvas app](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/create-blank-app) with **Phone** layout.
2.   On the **View** tab, select **Data sources**.
3.   In the **Data** pane, select **Add data source**.
4.   Select **New Connection**>**Twitter**>**Create**.
5.   Enter your credentials, create the connection, and then close the **Data** pane.

1.   In the **Tree view** pane, select **App**, and then set its **OnStart** property to this formula:

```
If( Connection.Connected,
    ClearCollect( LocalTweets, Twitter.SearchTweet( "PowerApps", {maxResults: 10} ) );
        Set( statusText, "Online data" ),
    LoadData( LocalTweets, "LocalTweets", true );
        Set( statusText, "Local data" )
);
SaveData( LocalTweets, "LocalTweets" );
```

![Image 2: Formula to load tweets.](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/media/offline-apps/load-tweets.png)

2.   In the **Tree view** pane, select the ellipsis menu for the **App** object, and then select **Run OnStart** to run that formula.

![Image 3: Run formula to load tweets.](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/media/offline-apps/load-tweets-run.png)

Note

The **LoadData** and **SaveData** functions might show an error in Power Apps Studio because browsers don't support them. However, they'll perform normally after you deploy this app to a device. 

This formula checks whether the device is online:

*   If the device is online, the formula loads up to 10 tweets with the search term "PowerApps" into a **LocalTweets** collection.
*   If the device is offline, the formula loads the local cache from a file called "LocalTweets" if it's available.

1.   On the **Insert** tab, select **Gallery**>**Blank flexible height**.

2.   Set the **Items** property of the [**Gallery**](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-gallery) control to `LocalTweets`.

3.   In the gallery template, add three [**Label**](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-box) controls, and set the **Text** property of each label to one of these values:

    *   `ThisItem.UserDetails.FullName & " (@" & ThisItem.UserDetails.UserName & ")"`
    *   `Text(DateTimeValue(ThisItem.CreatedAtIso), DateTimeFormat.ShortDateTime)`
    *   `ThisItem.TweetText`

4.   Make the text in the last label bold so that the gallery resembles this example.

![Image 4: Gallery showing sample tweets.](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/media/offline-apps/tweet-gallery.png)

1.   Under the gallery, insert a label, and then set its **Color** property to **Red**.

2.   Set the newest label's **Text** property to this formula:

`If( Connection.Connected, "Connected", "Offline" )`

This formula determines whether the device is online. If it is, the label shows **Connected**; otherwise, it shows **Offline**.

1.   Under the connection-status label, insert a [**Text input**](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/controls/control-text-input) control, and rename it **NewTweetTextInput**.

2.   Set the text-input box's **Default** property to `""`.

![Image 5: Gallery over status info and text-input box.](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/media/offline-apps/status-input.png)

1.   Under the text-input box, add a **Button** control, and set its **Text** property to this value:

`"Tweet"`

2.   Set the button's **OnSelect** property to this formula:

```
If( Connection.Connected,
    Twitter.Tweet( "", {tweetText: NewTweetTextInput.Text} ),
    Collect( LocalTweetsToPost, {tweetText: NewTweetTextInput.Text} );
        SaveData( LocalTweetsToPost, "LocalTweetsToPost" )
);
Reset( NewTweetTextInput );
```
3.   In the **OnStart** property for the **App**, add a line at the end of the formula:

```
If( Connection.Connected,
    ClearCollect( LocalTweets, Twitter.SearchTweet( "PowerApps", {maxResults: 100} ) );
        Set( statusText, "Online data" ),
    LoadData( LocalTweets, "LocalTweets", true );
        Set( statusText, "Local data" )
);
SaveData( LocalTweets, "LocalTweets" );
LoadData( LocalTweetsToPost, "LocalTweetsToPost", true );  // added line
```

![Image 6: Run formula to load tweets with uncommented line.](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/media/offline-apps/load-tweets-save.png)

This formula determines whether the device is online:

*   If the device is online, it posts the tweet immediately.
*   If the device is offline, it captures the tweet in a **LocalTweetsToPost** collection and saves it to the device.

Then the formula resets the text in the text-input box.

1.   On the right side of the button, add a **Timer** control.

![Image 7: Final apps.](https://learn.microsoft.com/en-us/power-apps/maker/canvas-apps/media/offline-apps/final-app.png)

2.   Set the timer's **Duration** property to **300000**.

3.   Set the timer's **AutoStart** and **Repeat** properties to **true**.

4.   Set the timer's **OnTimerEnd** to this formula:

```
If( Connection.Connected,
    ForAll( LocalTweetsToPost, Twitter.Tweet( "", {tweetText: tweetText} ) );
    Clear( LocalTweetsToPost );
    ClearCollect( LocalTweets, Twitter.SearchTweet( "PowerApps", {maxResults: 10} ) );
    SaveData( LocalTweets, "LocalTweets" );
)
```

This formula determines whether the device is online. If it is, the app tweets all the items in the **LocalTweetsToPost** collection and then clears the collection.

1.   Open the app using [Power Apps Mobile](https://powerapps.microsoft.com/downloads/) on a mobile device that's connected to the Internet.

Existing tweets appear in the gallery, and the status shows **Connected**.

2.   Disconnect the device from the Internet by enabling the device's airplane mode and disabling wi-fi.

The status label shows that the app is **Offline**.

3.   While the device is offline, write a tweet that includes **Power Apps**, and then select the **Tweet** button.

The tweet is stored locally in the **LocalTweetsToPost** collection.

4.   Reconnect the device to the Internet by disabling the device's airplane mode and enabling wi-fi.

Within five minutes, the app posts the tweet, which appears in the gallery.

We hope this article gives you an idea of the capabilities that Power Apps has for building offline apps. As always, please provide feedback in our [forum](https://powerusers.microsoft.com/t5/PowerApps-Forum/bd-p/PowerAppsForum1) and share your examples of offline apps in the [Power Apps community blog](https://powerusers.microsoft.com/t5/PowerApps-Community-Blog/bg-p/PowerAppsBlog).
