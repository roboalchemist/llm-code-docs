# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context/to-get-user-details.md

# Get user details

You can get the user details such as first name, last name, email, mobile number interacting with the agent from [context.user ](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/context/user)object.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-M14SvsuO0v4kkWc7ucP%2F-M14TSWft302y3YOMv6Y%2FJS%20-%20User%20Details.gif?alt=media\&token=a6b98e66-41db-4e78-a1c6-50ed16cc3fac)

{% hint style="info" %}
**Notes**:

* In the text, quick reply, card, or carousel, you can use **${context.user.<\<attributes>>}** to extract the user details.
* In a JS node, you can use **context.user.<\<attributes>>** to extract the user details.
  {% endhint %}

Consider that you wish to display a greeting message with the user's first name in the MacPizza agent. You can extract the user name using [context.user.first\_name](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/context/user) in the response as follows:

```markup
Hi ${context.user.first_name}, welcome to MacPizza agent. How can I help you today?
```

<div align="left"><img src="https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-LxZr4FY3FIqUlgQZGsT%2F-LxZslHIHvBgvecOxBqG%2Fjs-context-user-details.png?alt=media&#x26;token=40598593-f199-4b6d-8ab3-a6eaecd42f25" alt=""></div>

The following greeting message is displayed to the user:

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FDmfwPALyNEGIPKipy9CV%2Fimage.png?alt=media\&token=74a4b1fc-140a-4906-bad4-dc15928ebdad)

{% content-ref url="" %}
[](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/use-context)
{% endcontent-ref %}

{% content-ref url=".." %}
[..](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to)
{% endcontent-ref %}
