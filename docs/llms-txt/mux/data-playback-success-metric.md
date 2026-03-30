# Source: https://www.mux.com/docs/guides/data-playback-success-metric.md

# Playback Success
Playback Success for a single view is a score of 0, 50, or 100 that measures if the user was able to successfully begin playback.
<Image alt="Playback Success" width={1189} height={881} src="/docs/images/playback-success-dashboard.png" />

````md
## Playback Success Score

Playback Success Score focuses on whether a video played back successfully.

Successful playback includes two components:

* Did the video play without an error?
* Did the user actually get to playback, or did they exit before playback started?

### Formula
**Playback Success Score** is fairly simple. A failure that ends playback is a `0`, while a video that plays through without failure is `100`. A view that is terminated by the viewer before playback starts (an “Exit Before Video Start,” or EBVS) is given a score of `50`.  EBVS views that occur in less than 1 second are given no score.

```
100: successful playback
50: exit before video start
0: playback failure
N/A: exit before video start <1 second
```

Why are EBVS views given a score of 50? The reason is that while exits can often point to streaming problems (e.g. the video took too long to load), some percentage of exits before video start are normal. A user might click the wrong video or see a link to a different video they want to watch more. If a view is abandoned in less than one second, we assume the video start was unintentional or programmatic and exclude those play attempts from the score.

### Use this metric to:
* Understand how playback failures impact the overall viewer experience
* Compare playback success performance to other areas of viewer experience
* Find areas where playback success can be optimized and improved


## Exits Before Video Start

Viewers will sometimes abandon a video (e.g. close the page/app or click the back button) because it is taking too long to load. The Exits Before Video Start Percentage metric captures how frequently this happens.

For this metric we count the number of video views where the viewer clicked play (or the player began to autoplay) but the video never began to play back (Video Startup Time was never recorded), excluding playback failures.  We then divide that number by the total number of video views.

### Use this metric to:
* Watch how changes in Video Startup Time directly impact viewers abandoning the video
* Compare players and understand if factors other than startup time may be causing viewers to leave, for example visual cues like loading indicators and poster frames.

Note: Viewers may leave for reasons other than long startup times, for example deciding that they clicked the wrong video or clicking on a related video. Before becoming concerned with your platform’s specific percentage you should attempt to improve your Video Startup Time and see how that impacts your Exits Before Video Start.


## Playback Failure Percentage

The Playback Failure Percentage metric gives the percentage of video views that failed to play due to a fatal error. Playback failures can happen at any point during video playback, causing the playback to end prematurely.

An error is considered a Playback Failure if it has a severity of fatal and it is not due to a business rule exception.

### Use this metric to:
* Understand where playback failures are happening most frequently
* Watch for spikes in playback failures due to new errors

Visit the Errors section to see which specific errors are happening the most frequently.


## Video Startup Failure Percentage

The Video Start Failure Percentage metric is the percentage of video views that experienced an error that prevents the user from seeing the first frame of video, which could be either ads or content.

An error is considered a Startup Failure if it occurs before the first frame of video is shown, has a severity of fatal, and the error is not due to a business rule exception.

### Use this metric to:
* Understand where video startup failures are happening most frequently
* Watch for spikes in startup failures due to new errors

Visit the Errors section to see which specific errors are happening the most frequently when start failures occur.

## Business Exception Percentage

  The Business Exception Percentage metric gives the percentage of video views that failed to play due to a fatal business rule exception.   Business Rule Exceptions can happen at any point during video playback, causing the playback to end prematurely.

  An error is considered a Business Rule Exception if it has a severity of fatal and it is specified as due to a business rule exception.


  ### Use this metric to:
  * Understand where playback failures are happening most frequently
  * Watch for spikes in playback failures due to new errors

  Visit the Errors section to see which specific business rule exceptions are happening the most frequently.
  

## Video Startup Business Exception Percentage

  The Video Startup Business Exception Percentage metric is the percentage of video views that experienced a business rule exception that   prevents the user from seeing the first frame of video, which could be either ads or content.

  An error is considered a Startup Business Rule Exception if it occurs before the first frame of video is shown,   has a severity of fatal, and the error is specified as due to a business rule exception.

  ### Use this metric to:
  * Understand where video startup business rule exceptions are happening most frequently
  * Watch for spikes in startup business rule exceptions due to new errors

  Visit the Errors section to see which specific errors are happening the most frequently when startup business rule exceptions occur.
  

## View Dropped Percentage

  Video views sometimes end for unknown reasons. This could be caused by a technical issue such as an   application or player crash, loss of session internet connection or browser behavior that   may restrict analytics. The View Dropped Percentage metric captures how frequently this happens.

  For this metric we count the number of video views where the viewing session ended without a clean   exit. We then divide that number by the total number of video views.

  ### Use this metric to:
  * Understand where dropped views are happening most frequently
  * Watch for spikes in dropped views due to player or application updates
  

## Ad Errors

The Ad Errors metric counts the number of times that ad errors occurred when trying to play. The number of Ad Errors helps you understand how often ads you attempt to run have problems being viewed.

An Ad Error is not necessarily a playback failure; errors often result in the ad playback ending or the ad being skipped before returning to video content playback.


## Ad Error Percentage

The Ad Error Percentage metric gives the percentage of ad attempts that failed during playback due to an ad error. Ad Errors can happen at any point during the ad playback, often causing the ad to end prematurely.

### Use this metric to:
* Understand how often errors are occurring when showing ads
* Watch for spikes in ad errors that can occur due a system issue


## Ad Breaks with Errors

The Ad Breaks with Errors metric counts the number of times that ad errors occurred during an ad break. The number of Ad Breaks with Errors helps you understand how often ad breaks have problems showing ads.

Some ad services will skip all remaining ads in the ad pod if an error happens and this metric can help you understand how often that occurs.


## Ad Breaks with Error Percentage

The Ad Breaks with Errors Percentage metric gives the percentage of ad breaks where an ad error occurred during the ad break.

### Use this metric to:
* Understand how often ad breaks have errors that occur when showing ads
* Understand if ad errors are more concentrated within a smaller number of ad breaks or spread out across ad breaks


## Ad Startup Error Percentage

The Ad Startup Error Percentage metric gives the percentage of time that an ad attempted to play but a failure occurred before the ad started and an ad impression was recorded.

### Use this metric to:
* Understand how often errors prevent ads from playing for viewers


## Ad Exits Before Start Percentage

The Ad Exits Before Start Percentage metric gives the percentage of time that an ad attempted to play but the user stopped or left the stream before the ad started playing.

The Ad Exit Before Start metric is intended to capture views where the user exits explicitly; ad start failures are not considered an exit in this metric because the user is not choosing to leave before the ad is shown when an error occurs.

### Use this metric to:
* Understand how often viewers stop the video stream before an ad started playing


## Ad Playback Failure Percentage

The Ad Playback Failure Percentage metric gives the percentage of video views that failed to play due to a fatal error during an ad break, causing ad playback to end prematurely.

An error is considered a Ad Playback Failure if it occurs during ad playback, has a severity of fatal, and is not due to a business rule exception.

### Use this metric to:
* Understand where ad playback failures are happening most frequently
* Watch for spikes in ad playback failures due to new errors

Visit the Errors section to see which specific errors are happening the most frequently.


## Content Playback Failure Percentage

The Content Playback Failure Percentage metric gives the percentage of video views that failed to play due to a fatal error during content playback. Content playback failures can happen any time during video playback outside of ad breaks, causing content playback to end prematurely.

An error is considered a Content Playback Failure if it occurs during content playback, has a severity of fatal and it is not due to a business rule exception.

### Use this metric to:
* Understand where content playback failures are happening most frequently
* Watch for spikes in content playback failures due to new errors

Visit the Errors section to see which specific errors are happening the most frequently.

````
