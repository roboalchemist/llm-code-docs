# Source: https://docs.roboflow.com/changelog/explore-by-month/september-2025/auto-label-now-supports-images-greater-than-4096px.md

# Auto Label now supports images > 4096px

<figure><img src="https://2667452268-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMR3m936tBXGm5QsAcPwe%2Fuploads%2FrJgI2api8WctkztT6vB8%2FScreenshot%202025-09-29%20at%2010.31.53.png?alt=media&#x26;token=cb6ecba4-7d56-40c8-a6de-d9f962485997" alt=""><figcaption></figcaption></figure>

When you upload images greater than 4096x4096px into Roboflow and use them with our Auto Label assistant, the images will be temporarily resized so that they work with Auto Label. The resulting annotations are then scaled back to be the original dimensions of the image.

This feature lets you upload images greater than 4096x4096px into Auto Label and receive annotations that are scaled to the size of your inptu image.
