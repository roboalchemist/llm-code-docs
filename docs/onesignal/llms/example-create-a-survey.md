# Source: https://documentation.onesignal.com/docs/en/example-create-a-survey.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Create a survey to ask for feedback

> Build a multi-page in-app survey using Carousel, Button Click Actions, Outcomes, and Tags for analytics and segmentation.

Using the In-App Message Carousel and Button Click Actions, we can create a survey with up to 10 pages of questions and multiple choice answers. When users provide answers, we can collect the data as outcomes and/or group them with [Data Tags](./add-user-data-tags) for targeting with messages.

### Designing your Survey

* To get the carousel, select the **Full** Message Type.
* Add 3 Text Blocks, 1 Image Block, and 2 button blocks.

Upon duplicating cards for the carousel, all blocks will be duplicated as well to make setting up the survey much easier!

* Select "+ Create Carousel" to duplicate this card and go back to **Card 1**.

Our initial setup will look similar to this:

<Frame caption="Image showing in-app editor with preview of survey for this tutorial">
  <img src="https://mintcdn.com/onesignal/_KaXe4GQkxsEfa17/images/docs/3666fcb-Screen_Shot_2020-09-16_at_5.16.40_PM.png?fit=max&auto=format&n=_KaXe4GQkxsEfa17&q=85&s=908788418ef4eafc875bf6365e72a4cd" width="1043" height="849" data-path="images/docs/3666fcb-Screen_Shot_2020-09-16_at_5.16.40_PM.png" />
</Frame>

Inside your text and image blocks, you can add any messaging you like and catchy image to get the user's interest.

Users will read the question, select a button and swipe to the next question.

My initial question is going to ask the user if they have time to answer some questions. If they say "Yes" I am going to save that as an Outcomes to mark how many people are interested in taking my survey and if they select "No" I will set an outcome that they are not interested at this time. If I get a lot of "No" responses, I might decide to show this prompt at a different time..

* Select **Add Click Action** to "Send Outcome"

Adding Outcomes will also add tags, so I can get both - analytics on my survey and create segments for re-targeting with tags.

Here is how the "Yes" button looks, notice that "Dismiss on click" is **unchecked**. This is found in the top right menu of each block > Show Advanced Settings

<Frame caption="Image showing button block with sending outcome of question">
  <img src="https://mintcdn.com/onesignal/tNi1OgLc_p9hiq7_/images/docs/1ab478c-Screen_Shot_2020-09-16_at_5.52.40_PM.png?fit=max&auto=format&n=tNi1OgLc_p9hiq7_&q=85&s=59ddc9eff3bdd4f81b29b728b48fccd4" width="498" height="402" data-path="images/docs/1ab478c-Screen_Shot_2020-09-16_at_5.52.40_PM.png" />
</Frame>

<Frame caption="Image showing ability to clone a block">
  <img src="https://mintcdn.com/onesignal/jFWn5xzleD8du3j6/images/docs/569c28c-Screen_Shot_2020-09-16_at_5.51.56_PM.png?fit=max&auto=format&n=jFWn5xzleD8du3j6&q=85&s=f784328720544be60c01c1d219869d0a" width="502" height="189" data-path="images/docs/569c28c-Screen_Shot_2020-09-16_at_5.51.56_PM.png" />
</Frame>

The "No" button will work in the exact same way, except we will check the "Dismiss on click" button to remove the In-App Message from view.

<Frame caption="Image showing a second button block with sending outcome of question">
  <img src="https://mintcdn.com/onesignal/56ctKxZSV4m5VEkn/images/docs/bb9e975-Screen_Shot_2020-09-16_at_5.31.42_PM.png?fit=max&auto=format&n=56ctKxZSV4m5VEkn&q=85&s=0feaf726fc7a1d4873662cc8182b3b0c" width="495" height="482" data-path="images/docs/bb9e975-Screen_Shot_2020-09-16_at_5.31.42_PM.png" />
</Frame>

### More Cards and Questions

Click **Card 2** or swipe the carousel to the next page. You will see all the blocks are duplicated.

Here, we can update the text and image but let's keep the question a simply Yes or No. We can do a multiple choice next.

Make sure "Dismiss on click" is not checked on your buttons.

<Frame caption="Image showing both button blocks for survey results">
  <img src="https://mintcdn.com/onesignal/3zq1PvSaqvUE2bIx/images/docs/314db9a-Screen_Shot_2020-09-16_at_5.41.18_PM.png?fit=max&auto=format&n=3zq1PvSaqvUE2bIx&q=85&s=a78f6b104aff17e795302e1b6f849907" width="918" height="823" data-path="images/docs/314db9a-Screen_Shot_2020-09-16_at_5.41.18_PM.png" />
</Frame>

Press the **+ Add Card** button to add the next card and so forth. You can add up to 10 cards.

### Final Survey Question

Let's setup a multiple choice question and end the survey.

To get the most space, I'll remove the image and add 2 more buttons. Remember: you can clone blocks to re-use them!

<Frame caption="Image showing ability to clone block">
  <img src="https://mintcdn.com/onesignal/4HyuQPBpu-4xjmQC/images/docs/cd1cd04-Screen_Shot_2020-09-16_at_5.55.25_PM.png?fit=max&auto=format&n=4HyuQPBpu-4xjmQC&q=85&s=64ceff1af5b4164bf90d275f6f50ad76" width="504" height="406" data-path="images/docs/cd1cd04-Screen_Shot_2020-09-16_at_5.55.25_PM.png" />
</Frame>

Since this is the end of my survey, I will have whatever button they select dismiss the In-App Message.

<Frame caption="Image showing a final four button survey">
  <img src="https://mintcdn.com/onesignal/tNi1OgLc_p9hiq7_/images/docs/14c36ad-Screen_Shot_2020-09-16_at_5.58.56_PM.png?fit=max&auto=format&n=tNi1OgLc_p9hiq7_&q=85&s=e6cbd79778a99253ea1ed2ea51677f68" width="949" height="822" data-path="images/docs/14c36ad-Screen_Shot_2020-09-16_at_5.58.56_PM.png" />
</Frame>

***

Built with [Mintlify](https://mintlify.com).
