# Source: https://docs.roboflow.com/changelog/explore-by-month/september-2025/upgrades-to-the-ocr-model-workflow-block.md

# Upgrades to the OCR Model Workflow Block

<figure><img src="https://2667452268-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FMR3m936tBXGm5QsAcPwe%2Fuploads%2FNAoF73kvqVvpO69VeyBR%2Fimage%20(15).png?alt=media&#x26;token=df524557-bcd1-4464-a6ce-2fdce12fbd19" alt=""><figcaption></figcaption></figure>

The "OCR Model" block in Roboflow Workflows now returns the bounding boxes associated with the text that has been identified by the block. This means that you can now write logic that uses the box coordinates from an OCR prediction. You can also connect the OCR Model block to a bounding box and label visualization to display predictions from an OCR Model on the original input image.
