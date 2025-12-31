# Source: https://docs.ideogram.ai/using-ideogram/generation-settings/negative-prompt.md

# Negative Prompt

The Negative Prompt feature guides the AI away from generating specific types of images or content. It instructs the AI on what to avoid or exclude in the generated images.

For example, if you’re using an AI to create landscape images but want to avoid beaches, you could use a negative prompt like "beach" or "beach, sand, water, ocean." This helps the AI understand your preferences and constraints so it can generate images that more closely match your intended outcome.

To access the Negative Prompt feature:

1. Select the [Prompt Box](https://docs.ideogram.ai/using-ideogram/ui-overview/ui-components/prompt-box) to reveal the generation settings (if not already visible).
2. Select the **More** button <picture><source srcset="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FsULvZOcJ9KEtw0cwW7Em%2FPB%20-%20More%20Button%20-%20Dark.png?alt=media&#x26;token=ee8e8a50-c3b7-42de-bdb3-31b87a7c336e" media="(prefers-color-scheme: dark)"><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FQMg6DKTYV1xcFS8gwDal%2FPB%20-%20More%20Button%20-%20Light.png?alt=media&#x26;token=883b737c-c2c6-4c15-86cc-378824550c3c" alt="More button in the Prompt Box." data-size="line"></picture> to open a dropdown menu where you can enter the terms or concepts you want the AI to avoid.
3. In the **Negative prompt** field, enter the terms or concepts you want the AI to avoid. Separate multiple items with commas (for example: green, green candies, cheese, cheddar.)

<figure><picture><source srcset="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FwfZVVlo6qx1FfTqkOc4J%2FPB%20-%20Negative%20Prompt%20Field%20-%20Dark.png?alt=media&#x26;token=9773e15f-d85a-4cc0-bd50-1b7c95bc5dac" media="(prefers-color-scheme: dark)"><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FXHpHxRfhdZhP4pAdr09a%2FPB%20-%20Negative%20Prompt%20Field%20-%20Light.png?alt=media&#x26;token=70c4c358-82aa-4573-852e-b634d9cedb10" alt="Negative Prompt input field inside the Prompt Box." width="375"></picture><figcaption><p>The Negative prompt field in the More menu of the Prompt Box</p></figcaption></figure>

Here are examples showing how *Negative Prompt* changes image results:

<table data-card-size="large" data-view="cards"><thead><tr><th></th><th></th><th></th></tr></thead><tbody><tr><td><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2F1JbUNnLkmvBsMCDrzDIA%2Fimage.png?alt=media&#x26;token=4a3d8c99-d5c4-464e-935e-c6165f289643" alt="Colorful candies including all colors, generated without a negative prompt." data-size="original"></td><td><strong>Prompt</strong>:<br>An assortment of colorful candies like Smarties or M&#x26;Ms, neatly arranged on a rustic wooden table.</td><td><strong>Negative prompt</strong>:<br>–</td></tr><tr><td><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FWXmqqXYiFB49UZLekUkB%2Fimage.png?alt=media&#x26;token=8efb2b98-5163-499f-a1dc-bef7aa636728" alt="Colorful candies with green candies removed using a negative prompt." data-size="original"></td><td><strong>Prompt</strong>:<br>An assortment of colorful candies like Smarties or M&#x26;Ms, neatly arranged on a rustic wooden table.</td><td><strong>Negative prompt</strong>:<br>green, green color, green candies</td></tr><tr><td><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FESmTA1pDWlGLqtpzUiSw%2Fimage.png?alt=media&#x26;token=d1139e8e-97a9-4e17-8eb9-cf40bfc1a295" alt="Gourmet burger with cheese and fries, generated without a negative prompt." data-size="original"></td><td><strong>Prompt</strong>:<br>Food photography picture of a delicious gourmet burger with a side of french fries and a beverage in the background.</td><td><strong>Negative prompt</strong>:<br>–</td></tr><tr><td><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FQkiMjXQUkL7Ifkk513o7%2Fimage.png?alt=media&#x26;token=11f3bbc2-f6fe-4c16-b86f-53b3e1198aff" alt="Gourmet burger without cheese, generated using a negative prompt for cheese." data-size="original"></td><td><strong>Prompt</strong>:<br>Food photography picture of a delicious gourmet burger with a side of french fries and a beverage in the background.</td><td><strong>Negative prompt</strong>:<br>cheese, cheeseburger, cheddar cheese</td></tr></tbody></table>

{% hint style="info" %}

#### Tips:

Here are some tips to get the most out of the feature:

* Use multiple keywords to describe what you don't want.
* Be as precise as possible without providing excessive detail.
* It is often simpler and more effective to write prompts that naturally exclude unwanted elements instead of relying heavily on negative prompts. See the [Handling Negatives](https://docs.ideogram.ai/using-ideogram/prompting-guide/4-handling-negatives) section of the *Prompting Guide* for more details.
  {% endhint %}

{% hint style="warning" %}
**Important tip:** If your negative prompt does not seem to work, check whether something in your main prompt interferes with or contradicts it. The content of the regular prompt will always be favored over the negative prompt. For example, a prompt asking for a classical guitar will almost always imply a guitar with strings. Trying to generate a guitar without strings may be difficult because the model usually interprets “guitar” as an object with strings.
{% endhint %}
