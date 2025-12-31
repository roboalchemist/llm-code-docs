# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context/detect-user-tone-and-sentiment.md

# Detect user tone and sentiment

You can use `context.insights.tone` and `context.insights.sentiment` to detect tone and sentiment from a user query to either change flows or respond with appropriate messages as per your business requirement. See [context.insights](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/context/insights), for more information.

Consider that when you detect if a user is sad from the user query and then wish to provide a comforting response to the user. You can create a custom Smalltalk skill to capture such intents and write a JS code as follows:

```javascript
if(context.insights.tone == "Sadness" && context.insights.sentiment == "negative")
  {
    return "I am sorry to learn that. How can I cheer you up today?";
  }
  
```

In the agent, when a user query with sadness is detected, then the following response is displayed:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FS01LrIPKsB3ku1konIDk%2Fimage.png?alt=media\&token=d823d854-0239-427d-9ae9-0439d18de32e)
