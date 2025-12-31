# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response/delay.md

# Delay

You can programmatically include a delay in the JS response using **\_.delay** function. This can be used to provide better user experience when you are using JS to perform backend API integrations.

If you expect multiple responses to be returned from the JS block, then you can introduce a delay between the responses. This provides a better conversational experience to the user by allowing them to read responses that are verbose, instead of displaying all the responses at once.

The following is a sample usage of delay in a Promise function:

```javascript
return new Promise ((res,rej) =>{
  _.delay(function(text){
    res(text);
   }, 3000, "Response after 3 seconds");
});
```
