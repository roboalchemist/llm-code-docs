# Source: https://docs.luciq.ai/product-guides-and-integrations/product-guides/app-ratings-and-reviews.md

# App Ratings & Reviews

To start using App Ratings and Reviews, navigate to the App Reviews page on your dashboard from the side navigation bar and choose your app's bundle ID or package name. Luciq will then automatically fetch your existing app store reviews and detect new reviews your app receives.

{% hint style="info" %}

#### **Min Required SDK Version**

App Ratings & Reviews is supported starting iOS SDK version 12.0.
{% endhint %}

Once you confirm your bundle ID, you’ll be able to track, monitor, and debug App Reviews and Ratings.

<figure><img src="https://images.gitbook.com/__img/dpr=2,width=760,onerror=redirect,format=auto,signature=1425383440/https%3A%2F%2Ffiles.readme.io%2F2622632fd34677d07ff628f3acbff0c3f60477366b0d2382c898a7ae33f6c82d-ios-app-reviews-2.png" alt=""><figcaption></figcaption></figure>

### Track App Reviews <a href="#track-app-reviews" id="track-app-reviews"></a>

In the App Reviews page in the side navigation bar, you’ll find a list of all reviews your app received, where you'll be able to view the following metadata:

* Rating
* Title
* Review
* Date
* App Version
* Country​<br>

  <figure><img src="https://images.gitbook.com/__img/dpr=2,width=1168,onerror=redirect,format=auto,signature=1509673054/https%3A%2F%2Ffiles.readme.io%2F6db75c0518bbd4869e2146b9c4beaae81da2f8cca5977391be308bd591b9eaa3-ios-app-reviews-5.png" alt=""><figcaption></figcaption></figure>

### Monitor App Ratings <a href="#monitor-app-ratings" id="monitor-app-ratings"></a>

From the App Overview page, you’ll be able to monitor your overall app rating per country to see how your ratings are distributed and see a chart for the Rating over time.By clicking on view all reviews button, you’ll be redirected to the App Reviews page to see a list of all your reviews.

<figure><img src="https://images.gitbook.com/__img/dpr=2,width=760,onerror=redirect,format=auto,signature=-797350245/https%3A%2F%2Ffiles.readme.io%2F75ea3a504ff6f6503124c5e968297140a02ba1aa3cb1c0901ea8b3958bb2199c-ios-app-reviews-7.png" alt=""><figcaption></figcaption></figure>

<figure><img src="https://images.gitbook.com/__img/dpr=2,width=760,onerror=redirect,format=auto,signature=1934462360/https%3A%2F%2Ffiles.readme.io%2F2eaaed0ec2b3e3afeeb90add2c85b321fd3fe2b00dac826d841b7bf062632509-ios-app-reviews-4.png" alt=""><figcaption></figcaption></figure>

### Monitor App Ratings and Reviews for each Release <a href="#monitor-app-ratings-and-reviews-for-each-release" id="monitor-app-ratings-and-reviews-for-each-release"></a>

From the releases page, you'll be able to see the Average Rating for each release. This average rating is calculated based on the star rating associated with each review the user wrote on the store for this app version.

<figure><img src="https://images.gitbook.com/__img/dpr=2,width=760,onerror=redirect,format=auto,signature=1527531422/https%3A%2F%2Ffiles.readme.io%2F69a7f4484ad8e36d495da2b87aeb77bbf2cbb381ce400cc4bb812659330e465b-ios-app-reviews-9.png" alt=""><figcaption></figcaption></figure>

From the release details page, you'll be able to see a breakdown of your App Rating based on the number of stars. In the comparison table, you’ll be able to see the current version rating and compare it across different releases.

<figure><img src="https://images.gitbook.com/__img/dpr=2,width=760,onerror=redirect,format=auto,signature=-2136095986/https%3A%2F%2Ffiles.readme.io%2F2b70360f2eb43a534ead2beea6b12a34f2a293e9666699c091b47fdf173adfe9-ios-app-reviews-10.png" alt=""><figcaption></figcaption></figure>

Once you navigate to the summary tab, you'll be able to see an AI-generated summary of the reviews for this release to get an idea about the end user sentiment.

<figure><img src="https://images.gitbook.com/__img/dpr=2,width=760,onerror=redirect,format=auto,signature=-1846657529/https%3A%2F%2Ffiles.readme.io%2Ff468891c6b22a01a7fc4e503db32855a8398d3ff6338d9e1da90ef71117cc5dc-ios-app-reviews-7.png" alt=""><figcaption></figcaption></figure>

### Debug App Reviews <a href="#debug-app-reviews" id="debug-app-reviews"></a>

Tracking your app’s ratings and reviews is only the first step. Combining Ratings and Reviews with Luciq’s Session Replay allows you to view a list of the sessions related to a specific review and replay them to understand the experience that led to that review.

#### How It Works <a href="#how-it-works" id="how-it-works"></a>

**Native In-App Prompt**

If you’re using the native in-app rating API, Our SDK will automatically detect the suspected sessions that are related to the reviews you receive on the dashboard.

<figure><img src="https://images.gitbook.com/__img/dpr=2,width=760,onerror=redirect,format=auto,signature=669359351/https%3A%2F%2Ffiles.readme.io%2Fb8b0aa13f6f4dc02a0835514fb7489232d1ffea0ebc2070f87252808b7d402b3-ios-app-reviews-3.png" alt=""><figcaption></figcaption></figure>

Once you click on **“View Session“** CTA, you’ll be redirected to the list of suspected sessions we matched for this review.

<figure><img src="https://images.gitbook.com/__img/dpr=2,width=760,onerror=redirect,format=auto,signature=658194379/https%3A%2F%2Ffiles.readme.io%2F99701393b960e6c28d6136874c7f036d56c4465e974e470232b12c3a30df6951-ios-app-reviews-1.png" alt=""><figcaption></figcaption></figure>

Now when you click on session details, you will be able to replay the session associated with that review and see all the needed debugging data that would help you resolve the issue.

<figure><img src="https://images.gitbook.com/__img/dpr=2,width=760,onerror=redirect,format=auto,signature=-586801711/https%3A%2F%2Ffiles.readme.io%2F578ee15f5579fe453a62f6ca671d05e30c5aa50b4344a6013be4c9a25e7dbae1-ios-app-reviews-8.png" alt=""><figcaption></figcaption></figure>
