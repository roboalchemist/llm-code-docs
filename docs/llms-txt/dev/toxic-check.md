# Source: https://dev.writer.com/home/toxic-check.md

# Toxic check

We developed an independent system that classifies input and output textual data and predicts its level of toxicity. Our model was trained on a distinct dataset that included both toxic and nontoxic examples. Each prompt is sent through the API to one of our large language models, and the generated text is analyzed and classified by a model that predicts the text's toxicity level. This probability lies between 0 and 1, where 0 indicates toxic classes and 1 indicates nontoxic classes

The Palmyra models provide scores for several different attributes, including Toxicity. Here are some of the other attributes Palmyra can provide scores for:

* **Severe Toxicity**: A very hateful, aggressive, disrespectful comment or otherwise very likely to make a user leave a discussion or give up on sharing their perspective. This attribute is much less sensitive to more mild forms of toxicity, such as comments that include positive uses of curse words.
* **Insult**: Insulting, inflammatory, or negative comment towards a person or a group of people.
* **Profanity**: Swear words, curse words, or other obscene or profane language.
* **Identity Attack**: Negative or hateful comments targeting someone because of their identity.
* **Threat**: Describes an intention to inflict pain, injury, or violence against an individual or group.
* **Sexually explicit**: Contains references to sexual acts, body parts, or other lewd content.

The text completion API methods return a JSON response with two fields, prompt labels and completion labels, that indicate the toxicity scores for each part independently. The field class name contains a binary class label determined by score, where a value less than 0.5 indicates toxicity and a value greater than 0.5 indicates nontoxicity.

```json  theme={null}

"prompt_labels": [
   {
      "class_name": "nontoxic",
      "score": 0.995605
    }
  ],
"completion_labels": [
    {
      "class_name": "nontoxic",
      "score": 0.997559    }
  ]
```
