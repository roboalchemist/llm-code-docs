# Source: https://docs.avaamo.com/user-guide/ref/frequently-asked-questions-faqs.md

# General keynotes (FAQs)

The following lists a few generic keynotes about intent processing, training data, and regex entities.

### Intent processing

* If there are multiple Q\&A with the exact same query, then the response from the first matching skill is displayed.
* The Smalltalk response is displayed only when the user query (including punctuations) exactly matches the training data provided in the Smalltalk.&#x20;

See [Intent execution sequenc](https://docs.avaamo.com/user-guide/overview-and-concepts/advanced-concepts/intent-execution-sequence)e, for more information.

### Training data

* If you want training data that must match specific and generic queries, then it is recommended to provide generic training data. **Example**: If you wish to match "I want my fund value" and "I want fund value", then it is recommended to use "I want fund value" in the training data.
* Training data must not be in all caps, as caps words are considered as stop words during processing.

### Spell correction

* The platform corrects the spelling of only words where the corrected spelling is at least 4 characters.
* Spell correction is not done for System location entities and English dictionary words.
* By default, the spell correction is not done for system entities, it can be added as custom entity values if you wish to make spell correction work.
* Spell correction identifies and corrects the phrase in the user query that is closest to the training data rather than correcting it to the best match. **Example**: Consider that you have the following data in your agent:
  * Dictionary: lone
  * Entity types: Loan types -> Personal loan, Housing loan
  * Skill -> Get loan
  * Training data -> I want Axis bank personal loan

&#x20;![](https://2934665269-files.gitbook.io/~/files/v0/b/gitbook-legacy-files/o/assets%2F-LpXFTiTgns4Ml77XGi3%2F-MFiZqEoBguVBYgTgBz9%2F-MFihXbdN0judaP2WRpP%2Frn-nlu-best-phrase.png?alt=media\&token=0490c1e3-4b1e-4b88-b414-e2fe0de2ec1a)

Note that here best phrase match for "lon" is "lone". However, when the user query is "I want Axis bank personal lon" , lon gets corrected to "loan" instead of "lone", since that is closest to the training data.

* Use "Skip lemmatization" to avoid plural words of English words getting unnecessarily mapped to other entities. **Example**: AlMedia is a US City. Consider that you have pizza\_sizes entity type with Medium as one of the sizes. In the user query, "I want to order medium size pizza", both US City and pizza\_size entities are extracted, as Medium is the singular form of Media that is also a value in the US city entity type. So, if both are used in a skill and you do not want to keep deleting slots, use "Skip lemmatization" when you are creating entity type.

See [Add invocation intent](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/add-invocation-intent) and [Add user intent](https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/using-dialog-designer/create-new-skill/add-user-intent), for more information.
