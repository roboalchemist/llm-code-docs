# Source: https://applitools.gitbook.io/docs/benefits.md

# Benefits and Features

## Day-to-day Benefits:

Applitools is meant to immediately make a difference in your life as a QA automation engineer from day-one and everyday after. Let's look a simple scenario to understand it better.

***Scenario: Imagine you are testing a complex page that has 50 different artifacts such as buttons, menus, fields, images and so on. Now let's look at the benefits***

| Issue                                                   | Work involved before using Applitools                                                                                                                                                                                                                                             | With Applitools                                                                                                          |
| ------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------ |
| Verify all 50 items                                     | <ol><li>Figure out identifiers for the an item. </li><li>Figure out XPath or classnames if there are no IDs</li><li>Repeat the above step 50 times</li><li>Write at least 50 lines of code to verify them</li></ol>                                                               | Just a couple of lines of code to verify all of them!                                                                    |
| Let's say, two artifacts out of 50 items change/removed | <ol><li>Two test fails</li><li>Figure out exactly which ones failed</li><li>Figure out why it failed (e.g. change in "id", "label")</li><li>Update the test code locally</li><li>Locally test if the updates work properly</li><li>Check-in the update for future tests</li></ol> | <ol><li>Test fails. </li><li>Visually inspect what failed.</li><li>Click a button to update the baseline image</li></ol> |
| Two New items are **added** to that page                | <ol><li>False positive! 👎</li><li>Because you don't have tests for these new items</li><li>If you realize it, then you'll have to manually write two additional tests</li><li>If you don't realize it, then you may not find bugs in those new items.🐛</li></ol>                | Test fails if the new items are added or removed. 👍🏻                                                                   |
| Items are not aligned properly, or layout changes       | <ol><li>False positive!👎</li><li>Because your tests only validate for mere "existence" and not for alignment or layout</li><li>You'll depend on manual testing to find these issues.</li></ol>                                                                                   | <ol><li>Test fails!👍🏻 </li><li>Applitools uses advanced AI to compare layouts (not pixel-by-pixel)</li></ol>           |
| You are using image comparison in your tests            | <ol><li>False positives!👎 </li><li>Basic pixel-by-pixel image comparison is known to break for even minute changes. </li><li>So, you may get so many false positives</li></ol>                                                                                                   | Applitools uses advanced AI to compare layouts.                                                                          |

That's just a sample list. There are plenty of other benefits. But as you can imagine, Applitools is will help your productivity starting from day-one. Let's look at some of the main features.

## Features:

### 1. Leverage your existing tests

Applitools automatically validates the look and feel and user experience of your apps and sites. It is designed to integrate with your existing tests rather than requiring you to create new tests or learn a new test automation language. Validate entire application pages at a time with a single line of code. We support all major test automation frameworks and programming languages covering web, mobile, and desktop apps.

*In the below video is showing a C# test where we are simply adding* *`eyes.checkWindow(home.Name)`* *to upload a picture to Applitools. Everytime this test is run a new picture is captured and compared against the previous one. The A.I. tool then determines if there are enough changes to mark the test as Pass or Fail or Undecided.*

![](https://blobscdn.gitbook.com/v0/b/gitbook-28427.appspot.com/o/assets%2F-LKyn5-TPBSSSy8ZqPvE%2F-LKz7GIlWOjTaaIEyQ21%2F-LKz7LpZLKNuJZJurFfI%2Fezgif-4-188dfaeb93.gif?alt=media\&token=da7f1dbb-f3e8-467a-a8b3-3b24fc78da86)

### 2. AI-powered cognitive vision

By emulating the human eye and brain, our AI-powered image comparison technology only reports differences that are perceptible to users and reliably ignore invisible rendering, size and position differences. Our algorithms can instantly validate entire application pages, detect layout issues, and process the most complex and dynamic pages. No calibration, training, tweaking or thresholding required on your part. It just works perfectly.

The video below is showing the differences Applitools AI has found in the latest run. You can use buttons such as "before and after", "zoom", "pixel compare", "layout compare" and so on to compare the differences.

![(Please click to Zoom and see)](https://blobscdn.gitbook.com/v0/b/gitbook-28427.appspot.com/o/assets%2F-LKyn5-TPBSSSy8ZqPvE%2F-LKzA9brcoYqKHrXFIjG%2F-LKzADYmEPBY4AuyY3tK%2Ffile.gif?alt=media\&token=dbf802ca-81c0-4de0-96eb-01ca8571ee72)

### 3. Automate your test maintenance

Resolve thousands of differences in minutes by leveraging sophisticated algorithms that automatically analyze the differences detected across all your tests and generate a concise report showing only distinct ones. Approve or reject a change and automatically apply the same decision to all similar changes across all your tests. Indicate elements that are allowed to move or to be ignored and automatically detect them across all screens in all your tests.

![(Please click to Zoom and read)](https://blobscdn.gitbook.com/v0/b/gitbook-28427.appspot.com/o/assets%2F-LKyn5-TPBSSSy8ZqPvE%2F-LKzB4g7RTTf1MtgDwlf%2F-LKzBRIaZ78Bm-0Fq0ft%2Ffile%20\(1\).gif?alt=media\&token=7e8f56dd-5d36-4588-bde7-6df54bfbb0c9)

​
