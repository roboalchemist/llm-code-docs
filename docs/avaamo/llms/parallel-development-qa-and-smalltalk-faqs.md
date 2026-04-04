# Source: https://docs.avaamo.com/user-guide/ref/parallel-development-qa-and-smalltalk-faqs.md

# Parallel development (QA & Smalltalk) FAQs

The following lists a few frequently asked questions about parallel development in Q\&A and Smalltalk skills.

### 1. What are some of the recommended best practices?

The following lists a few best practices to consider:

* **Adding and editing Q\&A** - Multiple developers can add or edit questions and answers simultaneously in the same Q\&A or Smalltalk skill, encouraging faster development of the skill. As a best design practice, it is recommended to distribute a set of intents among developers, so that it is easy to maintain and manage and results in seamless collaboration.
* **Adding languages** - Multiple developers can add and save language packs simultaneously in the Q\&A skill.  Each language pack can be saved independently. As a best practice, it is recommended that individual developers work on a single language pack independently. It helps to easily manage and maintain language packs.

### 2. Can I edit Dialog skill, when another user is editing a Q\&A skill simultaneously?

Yes, they can. One developer can unlock the agent and edit the Dialog skill, while the other developer works on the Q\&A. Editing Q\&A skills required lock only at each intent level.

### 3. Can I import Q\&A using CSV, when another user is editing a Q\&A intent in the same skill?

No, you cannot. You can import only when all of the existing questions and answers in the Q\&A skill are unlocked.&#x20;

### 4. Can I delete all (Clear) Q\&A, when another user is editing a Q\&A intent in the same skill?

No, you cannot. You can clear all the Q\&A only when all of the existing questions and answers in the Q\&A skill are unlocked

### 5. Can I publish a Q\&A skill, when another user is editing a Q\&A intent of the same skill?

Yes, you can. At the point of publishing, whatever is saved in the Q\&A skill, is published to the Skill store.

### 6. Can I import/re-import other skills from the skill store, when another user is editing a Q\&A intent?&#x20;

Yes, you can. One developer can unlock the agent and import other skills, while the other developer works on the Q\&A. Editing Q\&A skills required lock only at each intent level. The same holds good for publish/re-publish as well.&#x20;
