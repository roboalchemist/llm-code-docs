# Source: https://dateparser.readthedocs.io/en/latest/custom_language_detection.html

Title: Custom language detection — DateParser 1.3.0 documentation

URL Source: https://dateparser.readthedocs.io/en/latest/custom_language_detection.html

Markdown Content:
dateparser allows to customize the language detection behavior by using the `detect_languages_function` parameter. It currently supports two language detection libraries out of the box: [fastText](https://github.com/facebookresearch/fastText) and [langdetect](https://github.com/Mimino666/langdetect), and allows you to implement your own custom language detection.

Warning

For short strings the language detection could fail, so it’s highly recommended to use `detect_languages_function` along with `DEFAULT_LANGUAGES`.

Built-in implementations[](https://dateparser.readthedocs.io/en/latest/custom_language_detection.html#built-in-implementations "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------------

### fastText[](https://dateparser.readthedocs.io/en/latest/custom_language_detection.html#id1 "Link to this heading")

Language detection with fastText.

Import the fastText wrapper and pass it as `detect_languages_function` parameter. Example:

>>> from dateparser.custom_language_detection.fasttext import detect_languages
>>> dateparser.parse('12/12/12', detect_languages_function=detect_languages)

The fastText integration currently supports the large and the small models. Find more information about [fasttext](https://fasttext.cc/blog/2017/10/02/blog-post.html) models. You can download your model of choice using `dateparser-download`.

Downloading small model:

>>> dateparser-download --fasttext small

Downloading large model:

>>> dateparser-download --fasttext large

Deleting all cached models:

>>> dateparser-download --clear_cache

Note

If no model has been downloaded, the fastText wrapper downloads and uses the small model by default.

### langdetect[](https://dateparser.readthedocs.io/en/latest/custom_language_detection.html#id2 "Link to this heading")

Language detection with langdetect.

Import the langdetect wrapper and pass it as `detect_languages_function` parameter. Example:

>>> from dateparser.custom_language_detection.langdetect import detect_languages
>>> dateparser.parse('12/12/12', detect_languages_function=detect_languages)

Note

From some tests we did, we recommend to use `fastText` for faster and more accurate results.

Custom implementation[](https://dateparser.readthedocs.io/en/latest/custom_language_detection.html#custom-implementation "Link to this heading")
-------------------------------------------------------------------------------------------------------------------------------------------------

`dateparser` allows the integration of any library to detect languages by wrapping that library in a function that accepts 2 parameters, `text` and `confidence_threshold`, and returns a list of the detected language codes in ISO 639 standards.

Wrapper for boilerplate for implementing custom language detections:

def detect_languages(text, confidence_threshold):
 """
 Takes 2 parameters, `text` and `confidence_threshold`, and returns
 a list of `languages codes`.

* `text` is the input string whose language needs to be detected.

* `confidence_threshold` is a number between 0 and 1 that indicates the
 minimum confidence required for language matches.

 For language detection libraries that, for each language, indicate how
 confident they are that the language matches the input text, you should
 filter out languages with a confidence lower than this value (adjusted,
 if needed, to the confidence range of the target library).

 This value comes from the dateparser setting
 `LANGUAGE_DETECTION_CONFIDENCE_THRESHOLD`.

 The result must be a list of languages codes (strings).
 """
    # here you can apply your own logic
    return language_codes
