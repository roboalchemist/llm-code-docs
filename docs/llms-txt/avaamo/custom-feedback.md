# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/custom-feedback.md

# Custom feedback

In the **Agent -> Configuration -> Custom feedback** page, you can customize the user feedback form as per your requirement using Javascript (JS) code. This feature helps to:

* Build user feedback forms that are robust and intuitive. You can now create a custom feedback form by leveraging the rich set of objects and functions in the Avaamo Platform.&#x20;
* Enhance how you can collect feedback from the users. Since the feedback form can now be tailored to suit your business requirements, it enables you to collect relevant and effective feedback from users. The collected feedback can be used to significantly enhance the user's experience when interacting with your agent.&#x20;
* Create different custom feedback forms for both positive and negative feedback.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2Ffz7IiS6fAcQkUjLiT764%2F6.1-custom-feedback-example-new.png?alt=media\&token=40528613-9ab1-4e5a-9355-d3a9a16a8c0e)

See [Collect feedback](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/collect-feedback), for more information on understanding the concept and various ways in which you can collect feedback from the users.

### Add custom user feedback

{% hint style="info" %}
**Notes**:

* Ensure you have met all the [pre-requisites](https://docs.avaamo.com/user-guide/quick-start-tutorials/pre-requisites).

* You can configure custom feedback to the agent immediately after creating an agent. See [Create agent](https://docs.avaamo.com/user-guide/how-to/build-agents/add-skills), for more information.

* If you wish to edit an agent, then:
  * In the **Avaamo Platform UI**, navigate to the **Agents** tab in the top menu. Search and open the required agent. See [Search agents](https://docs.avaamo.com/user-guide/how-to/manage-agents#search-agents), for more information.&#x20;
  * Click **Edit** to unlock the agent before editing.
    {% endhint %}

* In the Agent page, navigate to the **Configuration -> Custom feedback** option in the left navigation menu.

* By default, the custom user feedback toggle is disabled. Toggle the slider to enable this option.

* In the **Positive feedback** tab, specify the custom JS feedback form you wish to invoke when the user clicks the thumbs-up option in feedback.

* In the **Negative feedback** tab, specify the custom JS feedback form you wish to invoke when the user clicks the thumbs-down option in feedback.

* Click **Save** to save the details. To invoke the custom feedback form, you must enable collecting user feedback option at the skill or intent level as per your requirements. See [Example](#example) section, for a sample end-to-end illustration.

### Key points

Note the following important points about custom feedback:

* By default, the Custom user feedback option is disabled.
* Custom user feedback option when enabled&#x20;
  * Overrides the default feedback form provided by the platform. This implies that if you enable the toggle and do not provide any custom feedback form, then no form is displayed to the user.
  * Shows syntax errors(if any) in the JS code for custom feedback on the feedback pop-up form.
  * Is applicable wherever the user feedback is displayed to the user throughout the agent.
* Currently, you can only use Card elements to create a custom user feedback form. See [Card](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response/card), for more information.
  * In the Custom feedback, the Card returned must be a single object and not an array.&#x20;
  * If you are using [Polls](https://docs.avaamo.com/user-guide/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response/card/polls#example-2-polls-with-default-values), [Checklist](https://docs.avaamo.com/user-guide/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response/card/checklist#example-2-checklist-with-default-value), or [Picklist](https://docs.avaamo.com/user-guide/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response/card/select-picklist#example-2-picklist-with-a-default-value) in Cards, then for each option in the card element you must specify the UUID. Currently, in the Custom feedback JS form, it is recommended to use user-friendly identifiers for UUIDs instead of a random-generated number in the "Options" object as it helps you to identify the message in the [User feedback](https://docs.avaamo.com/user-guide/how-to/build-agents/learning-continuous-improvement/feedback) page.
  * Currently, in the custom feedback, the post\_message type is not supported in Card links. See [Card links](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response/card/card-links), for more information.
  * Currently, any media content including images is not supported in Custom feedback.
* Use `CTRL+ENTER` key to toggle between fullscreen mode. You can view the complete list of built-in functions with syntax and examples in the Built-in functions window available in the JS editor. See [Built-in functions window](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/built-in-functions-window), for more information.
* All the feedback provided via the custom feedback form is recorded in the Analytics and can be viewed in the **User feedback** page for further analysis. See [User feedback](https://docs.avaamo.com/user-guide/how-to/build-agents/learning-continuous-improvement/feedback), for more information.
* If you have any error in the custom feedback JS code template, then&#x20;
  * An appropriate template error message is displayed when you are in debug mode, say when you are testing the custom feedback using the Agent simulator. This helps you to troubleshoot and correct the error as a developer of the agent.
  * If you are in a non-debug mode, say, testing the same scenario using the Test button in the Web channel, then since you are viewing as a user, an error message that something went wrong is displayed.

### Example

Consider in your agent that you wish to collect feedback on how the service was helpful to the users for all the questions and responses in the Q\&A skill.

* In the **Agent ->** **Configuration -> Custom feedback** page, enable **Custom user feedback** toggle.
* In the **Positive feedback** tab, specify the custom form as per your requirement. Currently, you can only use Card elements to create a custom user feedback form. See [Card](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/how-to/build-dynamic-skill-response/card), for more information. The following code is a sample illustration of the custom feedback form:

```javascript
return {
    "notification_message": "Thank you for your valuable feedback. We appreciate your time and response.",
    "card": {
        "inputs": [{
                "type": "single_line_text",
                "title": "First Name",
                "uuid": "firstName",
                "default_value": "John"
            },
            {
                "type": "single_line_text",
                "title": "Last Name",
                "uuid": "lastName",
                "default_value": "Creek"
            },
            {
                "type": "data_capture",
                "title": "Anything you would like us to improve on?",
                "uuid": "a4615857-c2f7-4586-b4b0-f771683fcb1a"
            },
            {
                "title": "Rate our service",
                "type": "rating",
                "uuid": "784cc8d5-b3d0-4cbc-89c4-4ef3c2fa43ea"
            }
        ]
    }
}
```

* Enable the **Collect feedback** option for the Q\&A skill. See [Collect feedback](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/collect-feedback#enabling-feedback), for more information.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FWffI8KODeJ5KXpkylhAe%2Fcollect-feedback-qa.png?alt=media\&token=198f48b2-a2f9-441d-beec-3e1b7cfec516)

* You can now test the agent. Click the agent icon at the bottom-right corner to invoke the agent simulator. Specify the intent to invoke the Q\&A skill where feedback is enabled. After the Q\&A  response, a thumbs-up and thumbs-down icon is displayed in the agent.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FKGPeQnEEdfI155knxksn%2Fuser-feedback-thumbs-up-down.png?alt=media\&token=332ab9cf-a8f7-4027-b753-d573a5fd0015)

* Click the thumbs-up option in the feedback. The following pop-up is displayed as configured in the Agent -> Configuration -> Custom feedback -> Positive feedback tab.

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FSw6Fevr7PuKVqVseKa26%2Fpositive-feedback-example.png?alt=media\&token=b848eeea-8dc4-41c7-afee-192a19d346b8)

* Provide the feedback and click **Submit**. Note the message displayed in the agent after providing feedback is from the "notification\_message" attribute.&#x20;

![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2F-LpXFTiTgns4Ml77XGi3%2Fuploads%2FCfPwmdjcKWCpSZCBaMfh%2Fpositive-feedback-example-message.png?alt=media\&token=e9644337-5643-41d2-8732-5f399bf1ad45)

* You can view the submitted feedback in the [User feedback](https://docs.avaamo.com/user-guide/how-to/build-agents/learning-continuous-improvement/feedback) page for further monitoring and analysis.
