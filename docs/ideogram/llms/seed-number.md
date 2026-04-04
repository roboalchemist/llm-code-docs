# Source: https://docs.ideogram.ai/using-ideogram/generation-settings/seed-number.md

# Seed Number

The Seed Number feature serves as a unique numerical identifier or starting point for image generation. Think of it as a special code that sets the initial conditions the AI uses to create an image. It’s primarily used to reproduce the same result and ensure consistency across generations.

To access Seed Number:

1. Select the [Prompt Box](https://docs.ideogram.ai/using-ideogram/ui-overview/ui-components/prompt-box) to expand it (if not already expanded) and show the available options.
2. Select the **More** button <picture><source srcset="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FsULvZOcJ9KEtw0cwW7Em%2FPB%20-%20More%20Button%20-%20Dark.png?alt=media&#x26;token=ee8e8a50-c3b7-42de-bdb3-31b87a7c336e" media="(prefers-color-scheme: dark)"><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FQMg6DKTYV1xcFS8gwDal%2FPB%20-%20More%20Button%20-%20Light.png?alt=media&#x26;token=883b737c-c2c6-4c15-86cc-378824550c3c" alt="" data-size="line"></picture> to open the dropdown menu.
3. In the **Seed number** field, enter the number you want to use for the next generation.

<figure><picture><source srcset="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FY3PP3O7UckdZyUlKaRFe%2FPB%20-%20Seed%20Number%20Field%20-%20Dark.png?alt=media&#x26;token=392fef66-ce83-4356-8d2d-d9feedff5576" media="(prefers-color-scheme: dark)"><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FGEn8NHZBeYTPJa6bXYsT%2FPB%20-%20Seed%20Number%20Field%20-%20Light.png?alt=media&#x26;token=17a53773-6c56-46c2-9682-e0ddb3f06a4e" alt="Seed number field in the More menu." width="375"></picture><figcaption><p>Seed number field in the More menu.</p></figcaption></figure>

If no Seed Number is entered, the AI will automatically assign a random value. You can enter any number to act as a seed for generation.

When viewing an image, its Seed Number appears in the [Details Panel](https://docs.ideogram.ai/using-ideogram/ui-overview/ui-components/details-panel) on the right (desktop) or below the image (mobile).

{% hint style="warning" %}
**Warning:** In Ideogram **Model v3.0**, using the same Seed Number with different [Render Speeds](https://docs.ideogram.ai/using-ideogram/generation-settings/render-speed) won’t generate identical images as in earlier versions. However, the results will remain visually similar if the same prompt is used.
{% endhint %}

## Seed Number Use Cases

One example is to keep the same Seed Number and generate the same prompt using different Render speeds, as shown below:

<table data-view="cards"><thead><tr><th></th><th></th></tr></thead><tbody><tr><td>Seed: 406220<br>Rendering: Turbo</td><td><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FYz0LcGrTj58en9FZ3CQe%2Fimage.png?alt=media&#x26;token=a3abb3de-b326-4ce9-97a7-bde06f325253" alt="Image generated with Turbo render speed using Seed 406220" data-size="original"></td></tr><tr><td>Seed: 406220<br>Rendering: Default</td><td><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2F0ZxfLbi2t3aum0amBSeN%2Fimage.png?alt=media&#x26;token=b2d4ed15-8b50-4d20-87d0-85ba83e45c44" alt="Image generated with Default render speed using Seed 406220" data-size="original"></td></tr><tr><td>Seed: 406220<br>Rendering: Quality</td><td><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2F8hugIeBdZcmhoUJlChvI%2Fimage.png?alt=media&#x26;token=57d209e3-405a-4431-8591-c4042f3d2747" alt="Image generated with Quality render speed using Seed 406220" data-size="original"></td></tr></tbody></table>

You can also use the Seed Number to make small prompt adjustments while preserving most of the original composition.

<table data-view="cards"><thead><tr><th></th><th></th><th></th></tr></thead><tbody><tr><td><strong>Prompt</strong>: <em>... The background is a dark <mark style="color:green;">blue</mark> gradient, ...</em><br><strong>Seed</strong>: 406220<br><strong>Rendering</strong>: Default</td><td><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FWxQSzpQIymJVeZEYveZF%2Fimage.png?alt=media&#x26;token=59f180f6-fd6e-4665-a80c-1775773e9b0b" alt="" data-size="original"></td><td></td></tr><tr><td><strong>Prompt</strong>: <em>... The background is a dark <mark style="color:green;">purple</mark> gradient, ...</em><br><strong>Seed</strong>: 406220<br><strong>Rendering</strong>: Default</td><td><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FiE9QLnl1TvtGYfq9ZSxb%2Fimage.png?alt=media&#x26;token=0983b08c-a332-4529-abf6-2d3488384ff4" alt="" data-size="original"></td><td></td></tr><tr><td><strong>Prompt</strong>: <em>... The background is a dark <mark style="color:green;">red</mark> gradient, ...</em><br><strong>Seed</strong>: 406220<br><strong>Rendering</strong>: Default</td><td><img src="https://1799634369-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FzjhNby3LLsIikYuvxAJP%2Fuploads%2FdoCz9dSrZ6R0nDkFIjFA%2Fimage.png?alt=media&#x26;token=6c7f08c2-077f-4bdc-a623-027b340148c2" alt="" data-size="original"></td><td></td></tr></tbody></table>

The images aren’t identical, but they maintain the same composition and overall appearance. Only the background changes as specified.

{% hint style="warning" %}
**Warning:** Even when using the same *Seed Number*, changing a key concept in the prompt — for example, replacing “photography” with “painting,” or switching to another **model** — will generate different images.
{% endhint %}
