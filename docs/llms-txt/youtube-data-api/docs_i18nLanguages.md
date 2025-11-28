# Source: https://developers.google.com/youtube/v3/docs/i18nLanguages.md.txt

# I18nLanguages

An **i18nLanguage** resource identifies an application language that the YouTube website supports. The application language can also be referred to as a UI language. For the YouTube website, an application language could be automatically selected based on Google Account settings, browser language, or IP location. A user could also manually select the desired UI language from the YouTube site footer.  

Each `i18nLanguage` resource identifies a language code and a name. The language code can be used as the value of the `hl` parameter when calling API methods like `videoCategories.list` and `guideCategories.list`.

## Methods

The API supports the following methods for `i18nLanguages` resources:

[list](https://developers.google.com/youtube/v3/docs/i18nLanguages/list)
:   Returns a list of application languages that the YouTube website supports.
    [Try it now](https://developers.google.com/youtube/v3/docs/i18nLanguages/list#usage).

## Resource representation

The following JSON structure shows the format of a `i18nLanguages` resource:  

```text
{
  "kind": "youtube#i18nLanguage",
  "etag": etag,
  "id": string,
  "snippet": {
    "hl": string,
    "name": string
  }
}
```

### Properties

The following table defines the properties that appear in this resource:

|                                                                                                        Properties                                                                                                        ||
|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| `kind`         | `string` Identifies the API resource's type. The value will be `youtube#i18nLanguage`.                                                                                                                   |
| `etag`         | `etag` The Etag of this resource.                                                                                                                                                                        |
| `id`           | `string` The ID that YouTube uses to uniquely identify the i18n language.                                                                                                                                |
| `snippet`      | `object` The `snippet` object contains basic details about the i18n language, such as its language code and name.                                                                                        |
| snippet.`hl`   | `string` A BCP-47 code that uniquely identifies a language.                                                                                                                                              |
| snippet.`name` | `string` The name of the language as it is written in the language specified using the `i18nLanguage.list` method's [hl](https://developers.google.com/youtube/v3/docs/i18nLanguages/list#hl) parameter. |