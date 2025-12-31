# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/debug-agents/insights.md

# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/context/insights.md

# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/debug-agents/insights.md

# Source: https://docs.avaamo.com/user-guide/how-to/build-skills/create-skill/customize-your-skill/reference-library/context/insights.md

# insights

Context insights indicate how the user’s intent was analyzed and matched in the agent flow. You can use this information to debug agents. The following is a sample JSON of insights details in context object:

```javascript
{
  "analyzed_document": "I am very excited today I want to order veg cheese pizza",
  "document": "I am very excited today I want to order veg cheese pizza",
  "domain_ids": [
    41948
  ],
  "entities": [
    {
      "entity": "pizza_types",
      "entity_type": "pizza_types",
      "entity_value": "veg",
      "domain_key": "bot_inline_domain_497ba7c2-5677-42f2-940d-616c688357c5",
      "value": "veg",
      "current_value": "veg",
      "index": 43,
      "derived_parent": true,
      "parent_entity_key": null,
      "custom_entity_type": true
    },
    {
      "entity": "pizza_toppings",
      "entity_type": "pizza_toppings",
      "entity_value": "cheese",
      "domain_key": "bot_inline_domain_497ba7c2-5677-42f2-940d-616c688357c5",
      "value": "cheese",
      "current_value": "cheese",
      "index": 43,
      "parent_entity_key": "pizza_types",
      "custom_entity_type": true
    }
  ],
  "featured_tokens": [
    "i",
    "am",
    "very",
    "excite",
    "today",
    "i",
    "want",
    "to",
    "order",
    "veg",
    "cheese",
    "pizza"
  ],
  "featured_tokens_lemma_map": {
    "am": "am",
    "cheese": "cheese",
    "excited": "excite",
    "i": "i",
    "order": "order",
    "pizza": "pizza",
    "to": "to",
    "today": "today",
    "veg": "veg",
    "very": "very",
    "want": "want"
  },
  "id": null,
  "lemma": "i am very excite today i want to order veg cheese pizza",
  "negation": false,
  "original_document": "I am very excited today I want to order veg cheese pizza",
  "pos": [
    [
      "i",
      "NN"
    ],
    [
      "am",
      "VBP"
    ],
    [
      "very",
      "RB"
    ],
    [
      "excited",
      "JJ"
    ],
    [
      "today",
      "NN"
    ],
    [
      "i",
      "VBP"
    ],
    [
      "want",
      "VBP"
    ],
    [
      "to",
      "TO"
    ],
    [
      "order",
      "NN"
    ],
    [
      "veg",
      "NNS"
    ],
    [
      "cheese",
      "JJ"
    ],
    [
      "pizza",
      "NN"
    ]
  ],
  "sentiment": "neutral",
  "tone": "Surprise",
  "raw_document": "I am very excited today I want to order veg cheese pizza",
  "bow_normalized_document_with_stopwords": "i very excite datetime want order veg randomA pizza",
  "bow_normalized_document": "excite datetime want order veg randomA pizza",
  "bow_words": [
    "want",
    "veg",
    "randoma",
    "pizza",
    "order",
    "excite",
    "datetime"
  ],
  "normalized_document": "excite datetime want order veg randomA pizza",
  "featured_normalized_tokens": "excite datetime want order veg randomA pizza",
  "normalized_tokens": "excite datetime want order veg randomA pizza",
  "multiIntentEligible": false,
  "bow_score": 1,
  "entities_already_processed": true,
  "intent": "node_intent_node_1",
  "intent_name": "Test",
  "skill_name": "Test",
  "score": 1,
  "es_score": 23.346571,
  "confidence_score": 0,
  "training_datum_id": 1386989,
  "intent_id": 212186,
  "intent_type": "INLINE::INTENT",
  "bot_key": "1",
  "skill_key": "1",
  "intent_key": "3",
  "matching_document": "I want to order veg cheese pizza",
  "second_best_result": null,
  "detected_language": "en-US",
  "original_text": "I am very excited today I want to order veg cheese pizza",
  "is_transaction": false
}
```

<table><thead><tr><th width="216.85132055266237">Attribute</th><th width="320.0076575658408">Description</th><th>Type</th></tr></thead><tbody><tr><td>analyzed_document</td><td>Indicates the original user intent being analyzed.</td><td>String</td></tr><tr><td>document</td><td>Indicates the actual intent in the agent flow that is used to analyze the user query.</td><td>String</td></tr><tr><td>entities</td><td>Indicates an array of entities used to analyze the user’s intent.</td><td>An array of JSON key-value pairs.</td></tr><tr><td>featured_tokens</td><td><p>Indicates an array of lemma tokens generated from the user’s intent. </p><p></p><p>Here, <strong>tokens</strong> are characters separated by spaces that provide a convenient logical separation of phrases/sentences into words.</p></td><td>Array</td></tr><tr><td>featured_tokens_lemma_map</td><td><p>Indicates the mapping between each token and lemma token from the user’s intent. </p><p></p><p>This indicates how each token is converted to a lemma token. </p><p></p><p>Example: Ordering in lemma token is order.</p></td><td>Array</td></tr><tr><td>negation</td><td>Indicates if the user’s intent included negation words. Example: I do not want to order cheese pan pizza. In this case, negation is set to true.</td><td>Boolean</td></tr><tr><td>original_document</td><td>Indicates the original user intent being analyzed.</td><td>String</td></tr><tr><td>pos</td><td><p>Indicates parts of speech (pos) from the user’s intent. </p><p></p><p>See <a href="https://en.wikipedia.org/wiki/Part-of-speech_tagging">Part-of-speech tagging</a>, for more information.</p></td><td>Array</td></tr><tr><td>tone</td><td><p>Indicates the tone of the user query such as anger, fear, happy. </p><p></p><p>See <a href="../../../../../../overview-and-concepts/advanced-concepts/tone-and-sentiment">Tone and sentiment</a>, for more information.</p></td><td>String</td></tr><tr><td>sentiment</td><td><p>Indicates the sentiment in the user query such as Positive, Negative, Neutral. </p><p></p><p>See <a href="../../../../../../overview-and-concepts/advanced-concepts/tone-and-sentiment">Tone and sentiment</a>, for more information.</p></td><td>String</td></tr><tr><td>raw_document</td><td>Indicates the original user intent being analyzed.</td><td>String</td></tr><tr><td>new_normalized_document</td><td>Indicates the user intent after being normalized.</td><td>String</td></tr><tr><td>new_normalized_document_query</td><td>Indicates the user’s intent after removing the stopwords such as I, am, want, etc.</td><td>String</td></tr><tr><td>normalized_tokens</td><td>Indicates the list of tokens from the user’s intent after normalization.</td><td>String</td></tr><tr><td>entities_already_processed</td><td>Indicates if the entities are processed or not.</td><td>Boolean</td></tr><tr><td>intent</td><td>Indicates the name of the intent used while analyzing the user’s query.</td><td>String</td></tr><tr><td>training_datum_id</td><td>Indicates the training of the intent used while analyzing the user’s query.</td><td>Integer</td></tr><tr><td>intent_id</td><td>Indicates a unique identifier of the intent.</td><td>Integer</td></tr><tr><td>intent_name</td><td>Indicates the name of the intent used while analyzing the user’s query.</td><td>String</td></tr><tr><td>intent_type</td><td>Indicates the type of intent such as Inline, System intents, Knowledge Packs (Smalltalk and Q&#x26;A)</td><td>String</td></tr><tr><td>skill_key</td><td>Indicates unique key of the skill.</td><td>String</td></tr><tr><td>intent_key</td><td>Indicates the unique key of the intent.</td><td>String</td></tr><tr><td>second_best_result</td><td>Indicates the next best result obtained while analyzing the user’s intent, if any</td><td>String</td></tr><tr><td>detected_language</td><td>Indicates the language detected while analyzing the user’s intent.</td><td>String</td></tr><tr><td>knowledge_pack_id</td><td>Indicates the identifier of the knowledge pack, if any, used to analyze the user’s intent.</td><td>String</td></tr><tr><td>raw_utterance</td><td><p>Indicates the "as-is" utterances of the user's speech in the IVR channels. </p><p></p><p>Note that these are the exact spoken utterances without any modifications such as removing noise, filtering words, or modifying anything in the user's speech.</p></td><td>String</td></tr></tbody></table>

{% hint style="info" %}
**Note**: All the parameters in the context->insights object other than those listed in the table above are for internal usage only. For example, multiIntentEligible, es\_score, confidence\_score and other such parameters not listed above on the table are for internal usage only.
{% endhint %}
