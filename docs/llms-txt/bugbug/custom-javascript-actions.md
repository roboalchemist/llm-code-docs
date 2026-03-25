# Source: https://docs.bugbug.io/editing-tests/custom-javascript-actions.md

# Custom JavaScript actions

## JavaScript Steps

If you know how to code in JavaScript, you can overcome any limitations of BugBug features. With the power and flexibility of custom code actions, you can run any function during your tests.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2FWuBVtMLXu5qAAzmZXlN8%2Fadd%20step%20js.png?alt=media&#x26;token=7752a161-5eea-4dcc-9be4-8903b46fa6b4" alt=""><figcaption></figcaption></figure>

![](https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2Fw9x0527Xs1N6FC1HJtL1%2FScreenshot%202022-04-11%20at%2014.16.17.png?alt=media\&token=137aa5b5-02dc-490f-ac13-ff4c39c099df)

{% hint style="info" %}
**Hint!** You can call native JS functions, ex. you can request data via `XMLHttpRequest`, or store values in `localStorage`, etc.&#x20;
{% endhint %}

{% hint style="info" %}
**Remember!** You can also use [variables](https://docs.bugbug.io/variables#use-the-variables-argument-in-your-javascript-function) in your custom code
{% endhint %}

### Advanced JavaScript assertions

Use JS code to add complex assertions. Run any function and if it returns `true` the assertions will pass.

<figure><img src="https://3168433179-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-MKixgeBPbLvnD0l1eiV%2Fuploads%2F0oEE681NfPegM7oGuVdG%2FAssertion%20JS.png?alt=media&#x26;token=464972a4-0ee9-4b47-85ac-56caddb6311a" alt=""><figcaption></figcaption></figure>

**Example: assert if an input element has a specific placeholder text.**

1. Record a regular assertion to the input.&#x20;
2. Change its type to "Custom Javascript assertion"&#x20;
3. Enter custom JS code that checks the placeholder of the element, for example \
   `if (element.placeholder === 'Username') { return true } else {return false}`

{% embed url="<https://youtu.be/g7CsE-WHrwQ>" %}

### Make an API request from a custom Javascript code

Using the custom JS you can really do anything. For example, you can request some data from your API and use this data in a [custom javascript variable](https://docs.bugbug.io/variables#javascript-variables) or in an assertion.&#x20;

Here's an example of how to make a server-side request from Javascript.&#x20;

```
const response = await fetch('https://reqres.in/api/users', { 
    cors: 'no-cors'
});
const json = await response.json();
return json.data[0].email; //return the first user email
```

{% hint style="info" %}
**Note!** This is coding, so it adds complexity and more problems to solve. If you encounter cookie complications or  "Access-Control-Allow-Origin” ask a developer for help or contact BugBug support. We recommend keeping things simple and finding another solution to achieve a similar goal.&#x20;
{% endhint %}

{% hint style="info" %}
**Learn more** in the full [Fetch Web API documentation](https://developer.mozilla.org/en-US/docs/Web/API/Fetch_API/Using_Fetch)&#x20;
{% endhint %}

We listed several ideas on what you can achieve with API requests via code:

| Use API request to                                                                 | Example use case                                                                      |
| ---------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| Compare the data displayed in your app with the data returned from the server      | Check if your currency exchange is up-to-date                                         |
| Get a list of test users and their parameters from a centralized testing data file | Get a login and password for your random test user, skipping the registration process |
| Get the latest item from a server and its ID                                       | Check if the most recently added product is shown on the list of search results       |
