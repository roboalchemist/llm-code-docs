# Source: https://docs.sinch.com/ia-conversational/untitled-8/input-validation.md

# Input Validation

An `input validation` dialog state can be used to get information from the user. When the user gives information, the bot will first check if the info corresponds to an already known variable. Variables can be known already for various reasons:

* The user has answered this question before
* A previous entity was detected with the same variable name
* The user is authenticated and the variable was automatically set

If the `variable` has a `value` already, the bot will automatically go to the next bot dialog specified in the `Next bot dialog` dropdown list.

If the `variable` does not have a `value` yet, the bot will ask the question written in the input validation dialog.

## Invalid input

When a user gives an answer that's invalid (for example, when the bot asks for an email address and the user replies with 'chicken') the bot needs to let the user know their answer was invalid. To do so, you can create a message to be displayed for when input validation fails once, and another message for when the input fails 3 times.&#x20;

For example: the first time an input fails, the error message could simply be "Sorry, I didn't get that. Can you try again?" or "Sorry, that doesn't seem to be a valid date. Can you try the DD-MM-YYYY format?". When the user fails to give valid input 3 times in a row, the error message could be "Sorry, I can't seem to understand. Please contact our support team at \[tel number]". Another option is for your bot to redirect the user to a live agent.

## Settings

### Disable NLP

Users are able to leave the input validation if an intent is recognized. For bots with a very small NLP model, this might trigger a false positive. The 'disable NLP' checkbox allows you to disable the NLP model while in the input validation, which makes sure that whatever the user says gets saved as input.

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FMFmd3L5uZ6YGwe4pJBag%2Fimage.png?alt=media\&token=a7e6b906-39ef-49bd-ac1a-35d164b89bce)

### Always past - always future

Our platform parses user's expressions to match a default date format. If the date you ask should always be in the present or future, you can use these options. A user saying “Thursday” for example will be either mapped to last or next Thursday.

### Input types

Input plugins automatically validate and extract different input types based on the type setting. The type parser is responsible for extracting the data from the user's input. For example: if the input-plugin has a type of **date** and the user's input-sentence was 'I need to be in Paris *in two days*' the input plugin parser will extract the date definition from this input which results in 'in two days'. The parser will convert this into a date representation, DD-MM-YYYY, and the result will be stored in the user session.

#### Any

The 'Any' input type will accept all string values as an input. It is important to know that intents and entities are processed before parsers. This can be useful for automatically extracting certain pieces of a sentence as an answer to a question. We've got a great example of this in our tutorial [here](https://docs-latam.messaging.sinch.com/ia-conversational/untitled-8/broken-reference).

#### Date

The Date input parser type will try to parse the response as a date. Sentences like 'next week Monday' are automatically converted to a DD-MM-YYYY date object. Supported formats (also in other supported NLP languages) are:

* 22-04-2018
* 22-04
* 22 apr
* 22 april 18
* twenty two April 2018
* yesterday
* today
* now
* last night
* tomorrow, tmr
* in two weeks
* in 3 days
* next Monday
* next week Friday
* last/past Monday
* last/past week
* within/in 5/five days
* Friday/Fri

#### Location

The location parser will send the user's input to a Google Geocoding API service. When a correct address or location is recognized, the Chatlayer platform will automatically create an object that contains all relevant geo-data.&#x20;

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FLBgmTCYDt63nQiAHRC6G%2Fimage.png?alt=media\&token=d2d6d7f6-9e9d-4565-aa8d-0060d7859b23)

Look at the bot dialog above. When the user answers the question "Where do you work?" with a valid location, this information will be stored as a `user_work_location` variable (you can rename this variable if needed).&#x20;

Below is an example that shows how the `user_work_location` variable would be stored when the user responds with 'Chatlayer.ai':

```javascript
{
    fullAddress: "Oudeleeuwenrui 39, 2000 Antwerpen, Belgium",
    latitude: 51.227317,
    longitude: 4.409155999999999,
    streetNumber: "39",
    streetName: "Oudeleeuwenrui",
    city: "Antwerpen",
    country: "Belgium",
    zipcode: "2000",
}
```

{% hint style="info" %}
To show the address as a full address (street, street number, zipcode and city) you need to add some extra information to the variable: `.fullAddress`

So in the example above, the bot can display the entire location by using the following variable:`{user_work_location.fullAddress}`
{% endhint %}

A bot message containing the following info:

`Thank you, shall I send your package to {user_work_location.fullAddress}?`

Will display the following message to the user:

`Thank you, shall I send your package to Oudeleeuwenrui 39, 2000 Antwerpen, Belgium?`

#### Number

Number will parse any number the user has given.

#### Hours

This input type will parse and validate timestamps.

#### Currency

This input type will parse and validate currencies.

#### E-mail

This input type will parse and validate email addresses.

#### Postal code

This input type will parse and validate zip codes. Note: currently we only support Belgian zip codes.

#### **Image**

The image format type allows you to check if a user has uploaded an image or other file (such as pdf). Currently, this is only possible in the Facebook Messenger, WhatsApp, Instagram, RCS, MMS, Telegram and Instagram channels. If the bot user uploads a file, the URL to that file will be saved under the variable you save the response to.

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2FfIXahKBnQ4KxFImK9H1D%2Fimage.png?alt=media\&token=9a0ab99b-3e26-4762-828d-9a68e5089ebb)

The image will be saved as an array. If you chose {img} as variable, this means that you should use {img\[0]} to retrieve the URL for the first saved image.&#x20;

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2Fi7HoJBOzklHVugh3KfDh%2Fimage.png?alt=media\&token=1a4eded6-a0af-4c37-87df-c3f80c264863)

For the chat widget (web channel), we recommend using the [file upload](https://docs-latam.messaging.sinch.com/ia-conversational/untitled-8/broken-reference) template.

#### Language

This input type will parse and validate NLP supported languages.

* English: (en-us): 'engels', 'English', 'en', 'anglais'
* Dutch (nl-nl): 'nederlands', 'Dutch', 'ned', 'nl', 'vlaams', 'hollands', 'be', 'ned', 'néerlandais', 'belgisch'
* French (fr-fr): 'French', 'français', 'frans', 'fr', 'francais'
* Chinese (zh-cn): 'Chinese', 'cn', 'zh', 'chinees'
* Spanish (es-es): 'Spanish', 'español', 'es', 'spaans'
* Italian (it-it): 'Italian', 'italiaans', 'italiano', 'it
* German (de-de): 'German', 'duits', 'de', 'deutsch
* Japanese (ja-jp): 'Japanese', 'japans', 'jp', '日本の
* Brazil Portugese (pt-br): 'Brazil Portugese', 'Portugese', 'portugees', 'braziliaans portugees', 'português'

#### **Voice message**

![](https://1892724945-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-Mkmx3dQNmGgjdXVGQoB%2Fuploads%2Fly84J1rWoAhefWWEYLEk%2Fimage.png?alt=media\&token=2290f213-b384-4f53-9b54-60dcdfd303c7)

Use the Voice message input type to save whatever is said to the bot in a voice channel as text. You can configure the maximum duration of this voice message, and how long it takes for the bot to regard the message as "complete".
