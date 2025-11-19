# Source: https://docs.apify.com/platform/integrations/make/facebook.md

# Make - Facebook Actor integration

## Apify Scraper for Facebook Data

The Facebook Scraper modules from https://apify.com/ allow you to extract posts, comments, and profile data from Facebook.

To use these modules, you need an https://console.apify.com and an https://docs.apify.com/platform/integrations/api#api-token. You can find your token in the https://console.apify.com/ under **Settings > Integrations**. After connecting, you can automate data extraction and incorporate the results into your workflows.

## Connect Apify Scraper for Facebook Data modules to Make

1. Create an account at https://console.apify.com/. You can sign up using your email, Gmail, or GitHub account.

   ![Sign up page](/assets/images/signup-9708d31d8ee3eee598de711064f649f3.png)

2. To connect your Apify account to Make, you can use an OAuth connection (recommended) or an Apify API token. To get the Apify API token, navigate to **https://console.apify.com/settings/integrations** in the Apify Console.

   ![Apify Actor rental](/assets/images/actor-rental-f376d02ecb872d8399a7f664c8be2278.png)

3. Review the trial details. You won't be charged during the trial unless you actively switch to a paid plan. Click **Rent Actor** to activate your trial.

   ![Start Actor rental](/assets/images/start-rental-67a43c22c84cb3cb1d71c199909dc354.png)

4. Connect your Apify account with Make, you need to get the Apify API token. In the Apify Console, navigate to **https://console.apify.com/settings/integrations**.

   ![Apify Console token for Make.png](/assets/images/apify-console-token-for-make-cf75dbeb5effdcab9bc204cee94cdb6a.png)

5. Find your token under **Personal API tokens** section. You can also create a new API token with multiple customizable permissions by clicking on **+ Create a new token**.

6. Click the **Copy** icon next to your API token to copy it to your clipboard. Then, return to your Make scenario interface.

   ![Apify token on Make.png](/assets/images/Apify_token_on_Make-78f67b559503d92cffb17e5abffd18d2.png)

7. In Make, click **Add** to open the **Create a connection** dialog of the chosen Apify Scraper module.

8. In the **API token** field, paste the API token you copied from Apify. Provide a clear **Connection name**, and click **Save**.

   ![Make API token](/assets/images/make-api-token-0fa647a34cecf9027b22ab2ad6db7c27.png)

Once connected, you can build workflows to automate Facebook data extraction and integrate results into your applications.

## Apify Scraper for Facebook Data modules

After connecting the app, you can use one of the three existing Search modules as native scrapers to extract public data from Facebook.

### Extract Facebook groups

Get data via Apify's Facebook Groups Scraper. Just add one or multiple URLs of public groups you want to extract data from, then indicate a number of posts, and optionally, choose a sorting order and date filter.

For each given Facebook group URL, you will extract:

* *Post details*: post ID, legacy ID, Facebook group URL, direct post URL, post text, timestamp, and Facebook feedback ID.
* *Engagement metrics*: likes, shares, comments, top reactions, and breakdown by type (like, love, wow, care, haha).
* *User (post author)*: user ID and name.
* *Attachments*: media set URL, image thumbnail, full image URL, dimensions, OCR text (if any), media ID, and owner ID.
* *Top comments*: comment ID, comment URL, timestamp, text, feedback ID, commenter ID and name, profile picture, likes count, and threading depth.

Profile data, shortened sample


```
[
  {
    "facebookUrl": "https://www.facebook.com/groups/WeirdSecondhandFinds",
    "url": "https://www.facebook.com/groups/WeirdSecondhandFinds/permalink/3348022435381946/",
    "time": "2025-04-09T15:34:31.000Z",
    "user": {
      "name": "Author name"
    },
    "text": "4/9/2025 - This glass fish was found at a friend's yard sale and for some reason it had to come home with me. Any ideas on how to display it?",
    "reactionLikeCount": 704,
    "reactionLoveCount": 185,
    "reactionWowCount": 10,
    "reactionCareCount": 6,
    "reactionHahaCount": 3,
    "attachments": [
      {
        "url": "https://www.facebook.com/media/set/?set=pcb.3348022435381946&type=1",
        "thumbnail": "https://scontent.fcgh33-1.fna.fbcdn.net/v/t39.30808-6/490077910_10228674979643758_5977579619381197326_n.jpg?stp=dst-jpg_s600x600_tt6"
      }
    ],
    "likesCount": 908,
    "sharesCount": 3,
    "commentsCount": 852,
    "topComments": [
      {
        "commentUrl": "https://www.facebook.com/groups/WeirdSecondhandFinds/permalink/3348022435381946/?comment_id=3348201365364053",
        "text": "Would this work okay? Water and floating candle?",
        "profileName": "Bonnie FireUrchin Lambourn",
        "likesCount": 2
      }
    ],
    "facebookId": "650812835102933",
    "groupTitle": "Weird (and Wonderful) Secondhand Finds That Just Need To Be Shared"
  }
]
```


### Extract Facebook comments

Use the Facebook Comment Scraper to collect comments from Facebook posts. Add the post URLs, set the number of comments you want, and optionally choose comment order and whether to include replies.

You’ll get:

* *Text*: Comment text
* *Timestamp*: Date and time of the comment
* *Like count*: Number of likes on the comment
* *Commenter info*: Username, profile picture, profile URL, user ID
* *Number of replies*: Number of replies to the comment (not included in this example)
* *Post URL*: Link to the post the comment is associated with
* *Nested replies*: Nested replies to the comment (not included in this example)

Free plan limitations

Features like *replies* and *comment sorting* are limited for users on Apify's Free Plan. Consider upgrading to a https://apify.com/pricing.

Example (shortened)


```
[
  {
    "facebookUrl": "https://www.facebook.com/NASAJSC/posts/pfbid0ohxEG5cJnm3JNFodkvsehRUY3yfLx5Vis8cude7xRdmrXV9EMDxsuScPaSCtX9KNl?locale=cs_CZ",     "commentUrl": "https://www.facebook.com/NASAJSC/posts/pfbid0ohxEG5cJnm3JNFodkvsehRUY3yfLx5Vis8cude7xRdmrXV9EMDxsuScPaSCtX9KNl?comment_id=2386082985122451",
    "id": "Y29tbWVudDoxMDU1NDAzMDgzMzY4Mzk1XzIzODYwODI5ODUxMjI0NTE=",      "feedbackId": "ZmVlZGJhY2s6MTA1NTQwMzA4MzM2ODM5NV8yMzg2MDgyOTg1MTIyNDUx",     "date": "2025-04-09T18:39:23.000Z",
   "text": "Green is my favorite color. The beach my peaceful place. When I visited I was amazed at all the green and to see the beach area. Very cool",
    "profileUrl": "https://www.facebook.com/people/Elizabeth-Grindrod/pfbid022LryhRGvvGeZrrHq6SeS95doHdjDg7WHfaJHErzcEiNF8KPHiTx3drT9pw3oKMKTl/",
    "profilePicture": "https://scontent-bkk1-1.xx.fbcdn.net/v/t39.30808-1/489953042_122145581006424177_4615090019565194474_n.jpg?stp=cp0_dst-jpg_s32x32_tt6&_nc_cat=109&ccb=1-7&_nc_sid=e99d92&_nc_ohc=fJU9pA6IZpkQ7kNvwFulSHc&_nc_oc=AdldBxtJX_EilisOewldRrGT1dHWEFd690Wt6nWFTEVLY9-rlYNGHFTlMjgjB5bDsAM&_nc_zt=24&_nc_ht=scontent-bkk1-1.xx&_nc_gid=Kbf_nt_NCH2lzg1SIjTdHg&oh=00_AfGKLaCo8R4odY5OLT4esFDzvURJ46R6dxwCE0fD8jJR2A&oe=67FCA025",
    "profileId": "pfbid022LryhRGvvGeZrrHq6SeS95doHdjDg7WHfaJHErzcEiNF8KPHiTx3drT9pw3oKMKTl",
    "profileName": "Elizabeth Grindrod",
    "likesCount": "2",
    "threadingDepth": 0,
    "facebookId": "1055403083368395",
]
```


### Extract Facebook posts

Use the Facebook Post Scraper to get post data by adding one or multiple page URLs and the amount of posts you want to scrape.

You’ll get:

* *Post URL*: Link to the post

* *Shortcode*: Unique identifier for the post

* *Timestamp*: Date and time of the post

* *Content type*: Whether it’s an image, video, or carousel

* *Caption*: Text content of the post

* *Hashtags*: List of hashtags used in the post

* *Mentions*: Usernames of mentioned accounts

* *Likes*: Number of likes on the post

* *Comments*: Number of comments on the post

* *Shares*: Number of times the post has been shared

* *Media info*:

  <!-- -->

  * *URLs*: Links to media files
  * *Type*: Whether it's an image or video
  * *Dimensions*: Size of the media

* *Owner info*:

  <!-- -->

  * *Username*: Account name of the post owner
  * *User ID*: Unique identifier for the owner
  * *Full name*: Full name of the account holder

* *Tags*: Hashtags used in the post

* *Location*: Geographic location tagged in the post (if available)

Example (shortened)


```
[
  {
    "facebookUrl": "https://www.facebook.com/nasa",
    "postId": "1215784396583601",
    "pageName": "NASA",
    "url": "https://www.facebook.com/NASA/posts/pfbid029aLb3sDGnXuYA5P7DK5uRT7Upf39X5fwCBFcRz9C3M4EMShwJWNwLLaXA5RdYeyKl",
    "time": "2025-04-07T19:09:00.000Z",
    "user": {
      "id": "100044561550831",
      "name": "NASA - National Aeronautics and Space Administration",
      "profileUrl": "https://www.facebook.com/NASA",
      "profilePic": "https://scontent.fbog3-2.fna.fbcdn.net/v/t39.30808-1/243095782_416661036495945_3843362260429099279_n.png?stp=cp0_dst-png_s40x40&_nc_cat=1&ccb=1-7&_nc_sid=2d3e12&_nc_ohc=pGNKYYiG82gQ7kNvwGLgqmB&_nc_oc=AdmpIOT7GNKe9qxJgFM-EEuF78UvDx97YygzhxiRXW5nXDyZmQScZzHnWAFlGmn8VBk"
    },
    "text": "It’s your time to shine! This Citizen Science Month, contribute to a NASA Citizen Science project that will help improve life on Earth and solve cosmic mysteries.",
    "link": "https://science.nasa.gov/citizen-science/",
    "likes": 2016,
    "comments": 171,
    "shares": 217,
    "media": [
      {
        "thumbnail": "https://scontent.fbog3-3.fna.fbcdn.net/v/t39.30808-6/489419147_1215784366583604_2492050236576327908_n.jpg?stp=dst-jpg_s720x720_tt6&_nc_cat=110&ccb=1-7&_nc_sid=127cfc&_nc_ohc=YI6mnyIKJmwQ7kNvwGVLR7C&_nc_oc=AdklMZgJuQZ-r924q5F9ikY0F5E_LF2gbzNnepx75qTmtJ-jDnq6Ve-VkIQ1hcaCDhA"
      }
    ]
  },
  {
    "facebookUrl": "https://www.facebook.com/nasa",
    "postId": "1215717559923618",
    "pageName": "NASA",
    "url": "https://www.facebook.com/NASA/posts/pfbid01SDwDikd344679WW4Er1F1UAB3cfpBH4Ud54RJEaTtD1Fih2xSzjtsCsYXgbh93Ll",
    "time": "2025-04-07T17:04:00.000Z",
    "user": {
      "id": "100044561550831",
      "name": "NASA - National Aeronautics and Space Administration",
      "profileUrl": "https://www.facebook.com/NASA",
      "profilePic": "https://scontent.fbog3-2.fna.fbcdn.net/v/t39.30808-1/243095782_416661036495945_3843362260429099279_n.png?stp=cp0_dst-png_s40x40&_nc_cat=1&ccb=1-7&_nc_sid=2d3e12&_nc_ohc=pGNKYYiG82gQ7kNvwGLgqmB&_nc_oc=AdmpIOT7GNKe9qxJgFM-EEuF78UvDx97YygzhxiRXW5nXDyZmQScZzHnWAFlGmn8VBk"
    },
    "text": "NASA's Hubble Space Telescope has studied Uranus for more than 20 years and is still learning more about its gas.",
    "link": "https://go.nasa.gov/3RIapAw",
    "likes": 1878,
    "comments": 144,
    "shares": 215,
    "media": [
      {
        "thumbnail": "https://scontent.fbog3-1.fna.fbcdn.net/v/t39.30808-6/489532065_1215717536590287_873488674466633974_n.jpg?stp=dst-jpg_p180x540_tt6&_nc_cat=109&ccb=1-7&_nc_sid=127cfc&_nc_ohc=kAiP3avgomkQ7kNvwGOb-YS&_nc_oc=Adn31Ca9oiQ5ieTtUtFqcr45R4jdJdVxei1kMR1kj-RLDehS-fyEVJD1fY2-5IItLe0"
      }
    ]
  },
  {
    "facebookUrl": "https://www.facebook.com/nasa",
    "postId": "1212614090233965",
    "pageName": "NASA",
    "url": "https://www.facebook.com/NASA/videos/958890849561531/",
    "time": "2025-04-03T18:06:29.000Z",
    "user": {
      "id": "100044561550831",
      "name": "NASA - National Aeronautics and Space Administration",
      "profileUrl": "https://www.facebook.com/NASA",
      "profilePic": "https://scontent.fssz1-1.fna.fbcdn.net/v/t39.30808-1/243095782_416661036495945_3843362260429099279_n.png?stp=cp0_dst-png_s40x40&_nc_cat=1&ccb=1-7&_nc_sid=2d3e12&_nc_ohc=pGNKYYiG82gQ7kNvwGLgqmB&_nc_oc=AdmpIOT7GNKe9qxJgFM-EEuF78UvDx97YygzhxiRXW5nXDyZmQScZzHnWAFlGmn8VBk"
    },
    "text": "Rocket? Stacking. Crew training? Underway. Mission patch? Ready to go.",
    "link": "https://go.nasa.gov/41ZErWJ",
    "likes": 1813,
    "comments": 190,
    "shares": 456,
    "media": [
      {
        "thumbnail": "https://scontent.fssz1-1.fna.fbcdn.net/v/t15.5256-10/488073346_1027101039315356_6805938007276905855_n.jpg?_nc_cat=109&ccb=1-7&_nc_sid=7965db&_nc_ohc=M4hIzfAIbdAQ7kNvwFnbXVw&_nc_oc=AdmJODt8am5l58TuwIbYLbEMK_w9IFb6uaUqiq7SCtNI9ouf4Xd_nZcifKpRLWSsclg"
      }
    ]
  }
]
```


## Other scrapers available

Looking for more than just Facebook? You can use other native Make apps powered by Apify:

* https://docs.apify.com/platform/integrations/make/tiktok.md
* https://docs.apify.com/platform/integrations/make/search.md
* https://docs.apify.com/platform/integrations/make/maps.md
* https://docs.apify.com/platform/integrations/make/youtube.md
* https://docs.apify.com/platform/integrations/make/ai-crawling.md
* https://docs.apify.com/platform/integrations/make/amazon.md

And more! Because you can access any of thousands of our scrapers on Apify Store by using the https://www.make.com/en/integrations/apify.
