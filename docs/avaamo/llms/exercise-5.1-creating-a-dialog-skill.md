# Source: https://docs.avaamo.com/user-guide/tutorials-and-exercises/part-1-creating-my-agent/chapter-5-building-a-dialog-skill/exercise-5.1-creating-a-dialog-skill.md

# Exercise 5.1: Creating a Dialog skill

Let us build a skill to create an incident using ServiceNow integration. Here are some ways people can ask the agent to create a ticket:

```
I want to create a support ticket
My printer is not working, create a ticket
My Desktop is laggy, raise an incident
```

For the purpose of this exercise, we are limiting the training to these 3 phrases, you can go in and add more training data.

**To create a new Dialog skill**:

* In the Agent page, click on the Skills option in the left navigation menu to display the Skills page. Click on the *Add skill* button.
* In the Skill builder page, select Dialog skill and click *Create*.
* Specify the following details and click the *Create* button:

![](https://lh6.googleusercontent.com/__j6m94HAGy2V3NDm3TNeCqf3c3iev0ZI2aX_c7Dy_SYBncHqFTq3DCT7Bq2uybecxCWP33KE3U97b-t9pYsEHRTilFrnHOubgYpylkDwZpaM-gWlpmJNCZmhAxae53IWBrwL-Y4)

* Now, let us add some some training data to our invocation intent. After adding the training data, we can see that entities are automatically identified and slotted by the platform:

![](https://lh3.googleusercontent.com/KJyqcBxs3k4DZ2xA2FEhTi7Kr8Fgx7aY5M74wvjMfFlz5w4AIc_LVZ7eCz3VV7vyFLU1DFY_exlyufoiC28Kd6JQ7fXcIfLhBzui0XAPHaZhHAw6ZuzMVzATBNYVTdifYcSC1P8Q)

Let us create a conversation flow for this skill.
