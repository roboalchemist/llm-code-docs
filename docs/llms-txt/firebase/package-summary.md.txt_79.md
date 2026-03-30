# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/package-summary.md.txt

# com.google.firebase.ml.vision.document

### Annotations

|---|---|
| [FirebaseVisionDocumentText.RecognizedBreak.BreakType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.RecognizedBreak.BreakType) | Detected start or end of a structural component type: `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.RecognizedBreak#UNKNOWN`, `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.RecognizedBreak#SPACE` `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.RecognizedBreak#SURE_SPACE`, `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.RecognizedBreak#EOL_SURE_SPACE`, `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.RecognizedBreak#HYPHEN`, `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.RecognizedBreak#LINE_BREAK`. |

### Classes

|---|---|
| [FirebaseVisionCloudDocumentRecognizerOptions](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionCloudDocumentRecognizerOptions) | Represents the cloud document recognizer options. |
| [FirebaseVisionCloudDocumentRecognizerOptions.Builder](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionCloudDocumentRecognizerOptions.Builder) | Builder of `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionCloudDocumentRecognizerOptions`. |
| [FirebaseVisionDocumentText](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText) | Represents detected text by `https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentTextRecognizer`. |
| [FirebaseVisionDocumentText.Block](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.Block) | A logical element on the page. |
| [FirebaseVisionDocumentText.Paragraph](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.Paragraph) | A structural unit of text representing a number of words in certain order. |
| [FirebaseVisionDocumentText.RecognizedBreak](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.RecognizedBreak) | Detected start or end of a structural component. |
| [FirebaseVisionDocumentText.Symbol](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.Symbol) | A single symbol representation. |
| [FirebaseVisionDocumentText.Word](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.Word) | A single word representation. |
| [FirebaseVisionDocumentTextRecognizer](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentTextRecognizer) | Detector for performing optical character recognition(OCR) on an input image by sending the image to Google cloud ML backend. |