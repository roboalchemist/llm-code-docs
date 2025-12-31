# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context/switch-users-language.md

# Switch user's language

You can use [Language.switch](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/language.switch) to switch to a different language in the conversation. To detect the language used in the agent, you can use **context.insights.detected\_language**. See [insights](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/context/insights), for more information.

{% hint style="info" %}
**Note**: You can switch to only those languages that are added to the skill.
{% endhint %}

Consider that in MacPizza agent, English and French languages are supported and you wish to switch based on user preference. You can use **Language.switch('fr-FR')** to achieve this functionality.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FDyUA9U30RMChwvrWzBh8%2Fimage.png?alt=media\&token=c5d369b0-bf83-4f9d-9764-81ca91e6d567)

{% content-ref url="" %}
[](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context)
{% endcontent-ref %}

{% content-ref url=".." %}
[..](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to)
{% endcontent-ref %}
