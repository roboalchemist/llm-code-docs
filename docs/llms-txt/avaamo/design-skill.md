# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/design-skill.md

# Design skills

Skill is part of an agent that is specialized to understand and handle a specific task in the user conversation flow. **Example**: **Order Pizza skill** in a **Pizza agent** is responsible for taking the user through a conversation for capturing the required data to order a pizza. &#x20;

Training the skill with a set of quality intents and each intent with the right number of training data/training phrases/training utterances determines the quality of the agent's accuracy in understanding the user queries. Creating the right number of intents with the right number of training data samples for each intent is essential to provide a good user experience. &#x20;

This article describes the recommended best practices for designing a skill.

## Identify the purpose of skill

* When you start designing an agent, consider defining the functionality of the agent in well-defined tasks.&#x20;
* For each specific task, you can build skills and later choose to publish the skill to your company skill store, for re-usability.&#x20;
* Modularizing and building skills also help to troubleshoot and debug skills in an agent.
* Provide an appropriate name and description for each skill you build, as this name is used to identify the skill when publishes to the skill store.&#x20;

## Intent and training phrases(training utterances or training data)

Creating the right number of intents with the right number of training data samples for each intent is essential to provide a good user experience.  5 to 10 training phrases is a good number to start with.

{% hint style="info" %}
**Notes**:

* This document is for reference only and the actual intent to be created varies for each use case.
* It is not required for you to be a linguist. However, it is expected that the creator has good written communication skills.
* "Importing" is a reserved keyword and hence it is recommended to not use in the training data.
  {% endhint %}

### 1. **Avoid intent overlap**

* Avoid combining multiple goals in one intent
* Read the intent to identify overlaps

**Use Case**: To find a hospital or a specialist

| Recommended                                                                                                                                                          | Not Recommended                                                                                  |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ |
| <ul><li>Can you help me find a hospital?</li><li>Where is the nearest hospital?</li><li>Find a specialist for me.</li><li>I am looking for a pediatrician.</li></ul> | <ul><li>Find a hospital or specialist.</li><li>Search Something</li><li>Manage account</li></ul> |

### **2. Combine intents separated by entities**

Avoid creating separate intents when they mean the same with the difference only in entitie&#x73;**.**

**Use Case**: To find a tyre

| Recommended                | Not Recommended                                                       |
| -------------------------- | --------------------------------------------------------------------- |
| I am looking for X2 tyres. | <ul><li>I am looking for X2 </li><li>I am looking for tyres</li></ul> |

### **3. Write full sentences**

Writing full sentences helps the system comprehend the true intent of training data.

**Use Case**: To transfer money

| Recommended                        | Not Recommended |
| ---------------------------------- | --------------- |
| I want to transfer money to India. | Transfer Money  |

### 4. **Avoid providing duplicate training data for a single intent**&#x20;

* Do not overtrain
* Avoid including sentences in the training data that differ only by an alternate word

**Use Case**: To find a hospital or a specialist

| Recommended                                                                                      | Not Recommended                                                                                                                                                                                                                       |
| ------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| <p></p><ul><li>Can you help me find a hospital?</li><li>Where is the nearest hospital?</li></ul> | <p>Here, the following two training phrases are duplicate </p><p>for the same intent, since they differ only</p><p>by an alternate word:</p><ul><li>Can you help me find a hospital?</li><li>Can you search for a hospital?</li></ul> |

### **5.** Avoid using the same or similar training data in different intents

Avoid using the same or similar training data that differ only by an alternate word in different intents. In such cases, different responses may be displayed to the user based on the closest match to the user's intent and it often results in confusion.

**Use Case**: Outlook email policy

| Recommended                                                                                                                       | Not Recommended                                                                                                                                                                                                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Have a clearly defined intent with proper training data based on your use case. Avoid similar training data in different intents. | <p>Intent 1: Outlook Email Policy </p><p>Training Data: Older emails are missing from Outlook </p><p></p><p>Intent 2: Outlook Missing Email </p><p>Training Data: Older emails are missing on Outlook </p><p></p><p>Here, both are different intents but the training data is similar and differs only by an alternative word</p> |

### **6. Use slots for alternatives**

Create custom entity types that is generic.

**Use Case**: To open a bank account

**Recommended**:&#x20;

* I want to open a \[savings] account.
* I want to open a \[checking] account.

### **7. Use minimal words to convey meaning**

Leave out unnecessary and irrelevant words that do not contribute to the meaning of the sentence.

**Use Case**: To find a hospital or a specialist

| Recommended                      | Not Recommended                                                |
| -------------------------------- | -------------------------------------------------------------- |
| Can you help me find a hospital? | Can you help me find a gigantic, sophisticated, huge hospital? |

### **8. Avoid spelling mistakes**

Spelling mistakes in the training data cause the system to make wrong spelling corrections for user queries.

**Use Case**: Quote status

| Recommended                             | Not Recommended                        |
| --------------------------------------- | -------------------------------------- |
| Can you give me the status of my quote? | Can you give me the status of my quot? |

### **9. Use proper case for all words**

The most common mistake is writing a full sentence in lowercase.

**Use Case:** Car service center in Bangalor&#x65;**.**

| Recommended                                                                                                           | Not Recommended                                 |
| --------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------- |
| <p>Where is the Lexus service center in Bangalore?</p><p>Here, “L” in Lexus helps to identify a proper car brand.</p> | Where is the lexus service center in bangalore? |

### 10. **Ensure proper punctuation marks**

* It helps to identify the sentence type (declaration, question) and boundary.
* Missed or incorrect punctuation marks may make the training data completely unusable in some circumstances.
* Include punctuation marks such as period ( . ), comma ( , ), question mark ( ? ), exclamation point ( ! ), apostrophe( ' ), quotation mark ( "" ), and hyphen ( - ) as required.

**Use Case:** To transfer money

| Recommended                                                                                               | Not Recommended                                                                                         |
| --------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| <ul><li>What is the status of the transfer?</li><li>I transferred money to my mother last week.</li></ul> | <ul><li>What is the status of the transfer</li><li>I transferred money to my mother last week</li></ul> |

### **11. Readable intent name**

* In cases of disambiguation, the intent name is used as a button label. Hence, the intent names must be human-readable.
* Note that intent names can be longer with a full sentence

**Recommended**:

* Open a savings account
* Find a specialist for me.
* Get warranty information.

### 12. Generic vs specific training phrases

If you want training data that must match specific and generic queries, then it is recommended to provide generic training data. **Example**: If you wish to match "I want my fund value" and "I want fund value", then it is recommended to use "I want fund value" in the training data.
