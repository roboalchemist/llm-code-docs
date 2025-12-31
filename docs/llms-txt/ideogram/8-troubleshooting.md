# Source: https://docs.ideogram.ai/using-ideogram/prompting-guide/8-troubleshooting.md

# 8- Troubleshooting

##

Even with a well-structured prompt, the AI may not always interpret your intent exactly as expected. This section highlights common issues that can occur while prompting, along with practical fixes and links to relevant sections of the guide where you can learn more.

<details>

<summary>The AI adds something I specifically said I didn’t want.</summary>

**Possible Causes:**

* Prompt uses negative phrasing (e.g., “*no hair*,” “*no people*”).
* AI fails to process negation and focuses on the mentioned object instead.
* The unwanted object or concept is inadvertently suggested elsewhere in the prompt.
* Use of Magic Prompt.

**Fixes:**

* Rewrite using **affirmative descriptions** (e.g., “*bald*” or “*empty city*”).
* Use **visual substitution** to describe what *is* present instead of what isn’t.
* Double check you prompt for possible contradiction, even subtle.
* Turn Magic Prompt off.

→ **See:** [Handling Negatives](https://docs.ideogram.ai/using-ideogram/prompting-guide/4-handling-negatives), [Magic Prompt](https://docs.ideogram.ai/using-ideogram/7-creative-tools-in-ideogram#magic-prompt)

</details>

<details>

<summary>Text appears broken, misspelled, or missing.</summary>

**Possible Causes:**

* Text isn’t properly indicated in prompt.
* Text placed too late in the prompt.
* Too much or too complex text.
* Text in foreign language or non-Latin characters.
* Conflicts with visual complexity.

**Fixes:**

* Put the text in **quotes** (e.g., *a sign that says “Open 24 Hours”*).
* Place the text early in the prompt.
* Limit the amount of generated text.
* Break long text into chunks with placement cues.
* Use **Magic Fill** to correct errors after generation.
* For long copy, add it later in a third party editor.

→ **See:** [Generating Text in Images](https://docs.ideogram.ai/using-ideogram/2-prompting-fundamentals#generating-text-in-images)

</details>

<details>

<summary>Facial features, hands, or limbs look distorted (especially from a distance).</summary>

**Possible Causes:**

* Subject appears too small or far away in the frame for the AI to render detail properly.
* Low emphasis on face or limbs in the prompt.

**Fixes:**

* Move the subject closer by adjusting framing (“*close-up*,” “*portrait*”).
* Emphasize details explicitly (e.g., hands, eyes, facial features).
* Fix imperfections afterward using **Magic Fill**, recommended if you like the image.

*\*This isn't really a problem of wording or style, but rather the fact that most AIs struggle to handle fine detail at a distance, partly because of the lack of available pixels the AI has to work with.* [*Magic Fill*](https://docs.ideogram.ai/canvas-and-editing/canvas/magic-fill) *can help fixing this as it can work with greater pixel density over small areas.*

</details>

<details>

<summary>The subject is cropped when it should be shown fully (or vice versa).</summary>

**Possible Causes:**

* Aspect ratio doesn't match intended framing.
* The aspect ratio isn't commonly used for that type of image.
* Insufficient framing cues in prompt.

**Fixes:**

* Explicitly include framing cues like “full body,” “head and shoulders,” or “wide view.”
* Describe elements near the cropped area (feet, shoes, ground) to encourage full framing.
* Adjust the **aspect ratio** to better fit your subject and match intended composition.

→ **See:** [Aspect Ratio Influence on Framing](https://docs.ideogram.ai/using-ideogram/5-common-pitfalls-and-fixes#aspect-ratio-influence-on-framing)

</details>

<details>

<summary>Important words or concepts are not visually present in the image.</summary>

**Possible Causes:**

* Important ideas are too abstract, ambiguous, or visually unclear.
* Terms used are not visually grounded enough.

**Fixes:**

* Use alternate, more visually concrete wording or synonyms.
* Add more explicit visual cues or repetition of terms.

→ **See:** [Try Alternate Wording](https://docs.ideogram.ai/using-ideogram/6-prompt-iteration-and-refinement#try-alternate-wording), [Emphasize Important Parts of the Image](https://docs.ideogram.ai/using-ideogram/6-prompt-iteration-and-refinement#emphasize-important-parts-of-the-image)

</details>

<details>

<summary>Unwanted object, person or text appears in the image.</summary>

**Possible Causes:**

* Vague or overloaded prompt.
* Ambiguous language indirectly suggesting extra items.
* Uses of Magic Prompt.

**Fixes:**

* Simplify or clarify your prompt to remove ambiguity.
* Emphasize the desired subject and exclude unnecessary ideas.
* Use visual substitution (e.g., “empty field” instead of “no one around”).
* Turn off Magic Prompt.

→ **See:** [Prompt Length and Clarity](https://docs.ideogram.ai/using-ideogram/2-prompting-fundamentals#prompt-length-and-clarity), [Handling Negatives](https://docs.ideogram.ai/using-ideogram/prompting-guide/4-handling-negatives), [Magic Prompt](https://docs.ideogram.ai/using-ideogram/7-creative-tools-in-ideogram#magic-prompt)

</details>

<details>

<summary>Non-English or non-Latin text is incorrect or unreadable.</summary>

**Possible Causes:**

* AI has limitations rendering non-Latin alphabets (Cyrillic, Arabic, Chinese).

**Fixes:**

* Use English for best text rendering.
* Add add non-Latin text manually afterward (if necessary).
* Keep non-Latin text very short (logo-length).

→ **See:** [Prompting Uses Natural Language](https://docs.ideogram.ai/using-ideogram/2-prompting-fundamentals#prompting-uses-natural-language), [Generating Text in Images](https://docs.ideogram.ai/using-ideogram/2-prompting-fundamentals#generating-text-in-images)

</details>

<details>

<summary>A phrase isn’t giving the result I expected.</summary>

**Possible Causes:**

* Wording is too vague or abstract.
* Phrase not visually grounded.
* Uses of Magic Prompt.

**Fixes:**

* Use more **visually grounded** synonyms or phrasing.
* Try alternate wording or rephrasing of the concept.
* Turn Magic Prompt off.

→ **See:** [Try Alternate Wording](https://docs.ideogram.ai/using-ideogram/6-prompt-iteration-and-refinement#try-alternate-wording), [Visually Grounded vs Abstract Prompts](https://docs.ideogram.ai/using-ideogram/2-prompting-fundamentals#visually-grounded-vs.-abstract-prompts), [Magic Prompt](https://docs.ideogram.ai/using-ideogram/7-creative-tools-in-ideogram#magic-prompt)

</details>

<details>

<summary>The AI ignores important parts of my prompt.</summary>

**Possible Causes:**

* Important details placed too late in the prompt.
* Lack of emphasis for key features.
* Prompt length exceeds \~150 words.

**Fixes:**

* Place important elements early in the prompt.
* Repeat or describe the key elements with more detail.
* Use **descriptive emphasis** to draw attention.

→ **See:** 6.5 [Emphasize Important Parts of the Image](https://docs.ideogram.ai/using-ideogram/6-prompt-iteration-and-refinement#emphasize-important-parts-of-the-image).

</details>

<details>

<summary>Changing one word doesn’t seem to help.</summary>

**Possible Causes:**

* The new word is not visually strong or grounded.
* Other words in the prompt might conflict with it.

**Fixes:**

* Change **multiple related terms** for better alignment.
* Try synonyms that are more visual.
* Use a **thesaurus or LLM** to brainstorm variations.

→ **See:** [Try Alternate Wording](https://docs.ideogram.ai/using-ideogram/6-prompt-iteration-and-refinement#try-alternate-wording)

</details>

<details>

<summary>The style or visual mood isn’t right.</summary>

**Possible Causes:**

* Style or mood not specified or vague (*“artistic,” “modern”*).
* Contradictions between subject and style.

**Fixes:**

* Mention specific style and moods: *“watercolor,” “digital painting,” “dreamy,*” etc.
* Use a visually grounded detailed description for the style and mood you want.
* Try **Magic Prompt** to explore or **Style Reference** to better control styles and moods.

→ **See:** [Visually Grounded vs. Abstract Prompts](https://docs.ideogram.ai/using-ideogram/2-prompting-fundamentals#visually-grounded-vs.-abstract-prompts), [Creative Tools in Ideogram](https://docs.ideogram.ai/using-ideogram/prompting-guide/7-creative-tools-in-ideogram)

</details>

<details>

<summary>The image doesn’t match the emotion or concept I had in mind.</summary>

**Possible Causes:**

* Emotion or concept described too abstractly for AI recognition.
* Missing concrete visual cues.

**Fixes:**

* Translate emotional or conceptual language into visual or facial/body language cues.
* Blend abstract phrasing with visually grounded language.

→ **See:** [Visually Grounded vs. Abstract Prompts](https://docs.ideogram.ai/using-ideogram/2-prompting-fundamentals#visually-grounded-vs.-abstract-prompts), [Abstract Concepts Tied to a Subject](https://docs.ideogram.ai/using-ideogram/5-common-pitfalls-and-fixes#abstract-concepts-tied-to-a-subject)

</details>

This section doesn’t cover every possible scenario, but these are the most frequent issues users run into and most image issues can be fixed with one of these strategies. With time and a little experimentation, you’ll find the right combination of clarity and creativity to make each prompt work better. If something still isn’t working, try breaking your idea into smaller parts and building it up again, one step at a time.

***
