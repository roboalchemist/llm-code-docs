# Source: https://documentation.onesignal.com/docs/en/auto-segment-users-by-page-visit.md

> ## Documentation Index
>
> Fetch the complete documentation index at: https://documentation.onesignal.com/llms.txt
> Use this file to discover all available pages before exploring further.

# Track topic interest for smarter targeting

> Learn how to automatically track page visits by topic and use custom tags to send highly relevant Web Push notifications with OneSignal.

Most apps offer a wide range of content, but not every visitor is interested in everything. You can track what topics users explore and how often they return to those topics with OneSignal's SDK by tagging them.

Example use cases:

* On a fashion app, a user is only interested in men’s shoes—not women’s dresses.
* On a news app, a user consistently visits finance and sports articles—but never entertainment or politics.

By tracking the pages and topics users visit most, you can deliver more personalized messaging—boosting relevance, click-throughs, and satisfaction.

***

## Setup

### 1. Define and structure your topic taxonomy

Start by identifying the content categories or topics you want to track. These might be:

* Broad verticals like `sports`, `finance`, or `entertainment`
* Product types like `laptops`, `accessories`, or `premium`
* Authors or brands

<Note>
  - Start with 3–8 topics to keep management simple
  - Stay under 20 topics overall to avoid bloat
</Note>

***

### 2. Add code to track topic visits

You can tag users based on the number of times they visit a given topic. In the provided examples, we do the following:

* Track one or more topics per page or screen.
* Increment the visit count every time the topic is viewed.
* Immediately tag the user with the updated count on each view.

<CodeGroup>
  ```javascript JavaScript theme={null}
  // Set the topics you want to track for this page
  const topics = ["sports", "entertainment"]; // One or many

  if (typeof localStorage !== "undefined" && Array.isArray(topics)) {
    topics.forEach(topic => {
      let count = parseInt(localStorage.getItem(topic), 10);
      count = isNaN(count) ? 1 : count + 1;
      localStorage.setItem(topic, count);
      OneSignal.User.addTag(topic, count.toString());
    });
  }

  ```

  ```kotlin Kotlin theme={null}
  val topics = listOf("sports", "entertainment") // One or many
  val sharedPrefs = context.getSharedPreferences("TopicPrefs", Context.MODE_PRIVATE)

  topics.forEach { topic ->
      val count = sharedPrefs.getInt(topic, 0) + 1
      sharedPrefs.edit().putInt(topic, count).apply()
      val tags = mapOf(topic to count.toString())
      OneSignal.User.addTags(tags)
  }
  ```

  ```swift Swift theme={null}
  let topics = ["sports", "entertainment"] // One or many
  let defaults = UserDefaults.standard

  for topic in topics {
      let count = defaults.integer(forKey: topic) + 1
      defaults.set(count, forKey: topic)
      OneSignal.User.addTag(key: topic, value: "\(count)")
  }
  ```

</CodeGroup>

### 3. Segment and send personalized messages

Once tags are applied to users, you can target them using:

* [Segments](./segmentation) to build rule-based groups (e.g., users with `gaming >= 3`)
* [API Filters](/reference/create-message#filters) to dynamically include users in a campaign

Example use cases:

* Only message users about specific topics that have visited related pages 5+ times
* Promote posts to users who’ve read more than 3 posts from a specific author
* Offer discounts to shoppers who keep returning to a specific product category

***

## Best practices and tips

### Do

* Test your tag logic using `console.log()` before launching campaigns
* Use consistent topic naming conventions across pages

### Avoid

* Using long or overly specific tag keys (e.g., full article titles or long URLs)
* Exceeding OneSignal’s [tag limits](https://onesignal.com/pricing)
* Tagging with personally identifiable information (PII)

***

<Check>
  Congrats on enriching your user data with contextual information!
  Additional resources:

* [Data Tags](./add-user-data-tags)
* [Web SDK Reference](./web-sdk-reference)
* [Mobile SDK Reference](./mobile-sdk-reference)
* [Segments](./segmentation)
</Check>

***

Built with [Mintlify](https://mintlify.com).
