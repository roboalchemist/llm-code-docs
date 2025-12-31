# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/define-matching-rules-using-custom-intents.md

# Define custom intents

You can define your own matching rules using custom intents in nodes using JS. See [Build skill Response](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/build-skill-responses), for more information on creating user intents while building skill response.

Consider that you allow users to register in the MacPizza agent.  You can create a Register skill to handle all registration-related user conversations. In the Register skill, you start by asking the name under which the user wishes to register. In order to match the name entered by the user in the skill, you can define a custom intent with matching rules. &#x20;

The following is a sample JS that validates if the user has entered only a single word (assuming name in this case) using regex in [context.last\_message](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/context):

```javascript
var regex = /^[a-zA-Z]+$/;
if(regex.test(context.last_message.trim())){
  return true;
}
```
