# Source: https://validator.w3.org/feedback.html

Title: Feedback - W3C Markup Validation

URL Source: https://validator.w3.org/feedback.html

Markdown Content:
How to Provide Feedback For the W3C Markup Validator
----------------------------------------------------

There are many ways to send feedback or discuss the Markup Validator:

1.   If you need [help on validation or Web authoring](https://validator.w3.org/feedback.html#needhelp)
2.   If you would like to [send a suggestion on a validation error message](https://validator.w3.org/feedback.html#errormsg)
3.   If you want to [help, participate or discuss](https://validator.w3.org/feedback.html#mailinglist)
4.   If you want to [search or report bugs](https://validator.w3.org/feedback.html#bugreport).

### Finding help on validation and Web authoring

Your page doesn't validate, and you don't know why, or you have a question about HTML, stylesheets or validation?

**First, check our [Help and FAQ document](https://validator.w3.org/docs/help.html), as well as the [Web authoring FAQ](https://www.htmlhelp.com/faq/) to see if your question has been answered there.**

The two most common problems are: [Validating pages with ampersands (&'s) in URLs](http://www.htmlhelp.com/tools/validator/problems.html#amp) and [Validating pages with JavaScript: HTML in a `SCRIPT` Element](http://www.htmlhelp.com/tools/validator/problems.html#script).

If your problem isn't covered by one of the resources above, you can send it to one of the following forums:

*   [Stack Overflow](https://stackoverflow.com/questions/tagged/html)
*   [Reddit r/webdev](https://www.reddit.com/r/webdev/)

Each of these forums have plenty of experienced HTML authors who are willing to share their expertise. If you are commenting on a specific page, be sure to provide a URL when you ask your question!

### Error message feedback

If you think the error messages in the Markup Validator's result pages could be improved, or are not comprehensible, you can send questions and suggestions to our mailing-list.

If you do not understand an error while validating a page, or if you need help on validation, **read the FAQ** and help (see the section [Finding help on validation](https://validator.w3.org/feedback.html#needhelp)) and **search the list archives** for existing mail threads on the topic **before sending any message to the mailing-list**.

Before you send any feedback on error messages, we encourage you to search the archives for existing messages on this error in case your feedback has already been sent, or answers to your query have already been given.

Once you have checked that your suggestion has not been given yet, you can send your message. To write an efficient message:

*   **Add a meaningful subject line**: summarize your feedback in a handful of words;
*   If our system added [VE][XX] at the beginning of the mail subject, keep it. Otherwise, please precise which error message you are sending feedback about;
*   **Give some context**. Generally speaking, this means **give the URL** of the page you were trying to validate. The more context you give, the easier it will be for others to understand your problem, question or feedback. 
*   **What is your feedback?**. Explain your suggestion, or question, in a clear and informative manner. Be precise and thorough.

Once you have checked all the criteria above, [send your message to the www-validator public mailing-list](mailto:www-validator@w3.org?Subject=%20Add%20Subject%20Here&body=%0D%0A%0D%0ANOTE%3A%20Whenever%20possible%2C%20give%20the%20address%20of%20the%20document%20you%20were%20checking.).

### Discuss and participate

If you are interested in helping to improve this service, by writing code or just providing ideas, you should feel free to join or send a message to our mailing-list.

The **public** mailing-list to discuss the Markup Validator, Link checker and other tools is [`www-validator`](https://lists.w3.org/Archives/Public/www-validator/).

You can [subscribe](mailto:www-validator-request@w3.org?Subject=subscribe "Send a message to the www-validator-request subscription handler") to the list (and [unsubscribe](mailto:www-validator-request@w3.org?Subject=unsubscribe "Send a message to the www-validator-request subscription handler")), or if you just have a small patch or idea and don't want to join the list, feel free to [send it directly to the list](mailto:www-validator@w3.org "Send a message to the www-validator mailing list"). But whatever you do, **always use the [mail search engine](https://www.w3.org/Search/Mail/Public/search?index-type=t;type-index=www-validator)** first to check for existing messages on a given topic.

If you just want to have an informal discussion with developers and users of the Validator, you may also join the IRC channel #validator on the [freenode](https://freenode.net/) network (irc.freenode.net). However, please keep in mind that _this is not a support channel_.

### Bug reports

W3C tracks bug reports on the validator through the GitHub repositories where the code is maintained. Developers and other technical users can log bug reports and feature suggestions directly. If you are not familiar with issue tracking systems in general, send your feedback to the [mailing list](https://validator.w3.org/feedback.html#mailinglist) and someone on the W3C Validator Team will take care of logging your issue as appropriate.

There are two distinct repositories where issues can be filed; if you're not sure which to use, pick the first one and we will take care of transferring it if necessary:

1.   the [(X)HTML validator](https://github.com/w3c/markup-validator) which is used to validate HTML4 and XHTML documents, and provides the shared front-end for markup validation;
2.   the [NU validator](https://github.com/validator/validator/) which is the most actively maintained project, used to validate HTML5 / HTML LS documents.

Before you enter a new bug, we strongly encourage you to check that it is not yet in the list of opened issues.
