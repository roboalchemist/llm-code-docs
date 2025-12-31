# Source: https://docs.ideogram.ai/using-ideogram/prompting-guide/4-handling-negatives.md

# 4- Handling Negatives

## Why Negative Phrasing Often Fails

Ideogram, like many text-to-image AIs, struggles with understanding negation. When you describe something in terms of what it shouldn't include, the AI often misinterprets or ignores the negation. Instead, it focuses on the keywords themselves. For example, prompting *“a man without a beard”* may result in an image of a man with a beard, as the AI emphasizes the word *“beard”* without processing the *“without”* modifier.

This issue arises because these models are trained to associate words with visual elements, but they don't inherently grasp the concept of absence or exclusion. Therefore, using negative terms like *“no,”* *“without,”* or *“not”* can lead to unintended results.

***

## Turn Negatives Into Positives

When people want to exclude something from the image, they usually write the prompt using negative concept and phrasing of what they don't want—*“no people,” “without clouds,” “not dark.”* That’s completely natural in everyday language, but it doesn’t work well with text-to-image AI like Ideogram.

Instead, try to shift your thinking: describe the *positive visual opposite* of the thing you want to exclude.

Ask yourself: *“If this thing wasn’t there, what would I see instead?”*

For example:

* Don't write *“no people in the room”* but write *“an empty room with chairs neatly arranged”*
* Avoid *“without hair”* and replace it by “a bald figure with smooth skin”
* Instead of *“a beach without people”* use *“an empty beach at sunrise”*
* Rather than *“a robot with no eyes”* try *“a robot with a smooth, featureless face”*
* Don't write *“no cars on the street”* but opt for *“a quiet pedestrian-only street”*

This might feel less intuitive at first, but it gets easier with practice and is far more effective. If you're unsure how to flip your idea into a positive phrase, turn on Magic Prompt—it will often converts the sentence to a positive phrase—or use a Large Language Models AI (LLM) like ChatGPT to suggest an affirmative rewrite.

***
