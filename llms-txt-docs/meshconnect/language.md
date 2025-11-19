# Source: https://docs.meshconnect.com/advanced/language.md

# Enabling Multi-Language Support for Link

> This guide explains how to configure Mesh Link to support multiple languages, allowing you to provide a localized experience for your users.

This guide explains how to configure Mesh Link to support multiple languages, allowing you to provide a localized experience for your users.

# Understanding Language Configuration with `language`

The `language` parameter, which you set during Mesh Link initialization, is the key to displaying Link in your user's preferred language. This parameter allows you to:

* **Automatically match the user's device/browser language**, or
* **Specify a particular language.**

# Key Parameter: `language`

You'll use the `language` parameter when initializing Mesh Link via your SDK (Web, iOS, Android, or React Native).

## **Possible Values:**

* **`<BCP 47 code>`**: A specific language code enumerated as the 2 digit language identifier (eg. “**`fr-`**” for French) and the 2 digit region identifier (eg. “**`-CA`**” for Canada), combined as “**`fr-CA`**".  Alternatively, the SDK will accept an input of only the language (eg. “**`fr`**”).
* If the indicated language (eg. “**`fr-`**”) is followed by a region code (eg. “**`-CA`**”) that is not recognized or supported for that language, Link will fall back to the default translation for that language, if available (eg. “**`fr-FR`**”). If no translation for the language is available, Link will default to "**`en-US`**" (English, US).
* If you do not provide a value for the parameter, or if you provide a value for a language that is not supported, Link will default to "**`en-US`**" (English, US).
* **`system`**: Link will detect the default language on the user’s browser and/or device and display Link in that language. If it is an unsupported value, it will fallback to another locale for that language, or it will fallback to the global default of **`en-US`**.

# Implementation

## **Initialize Link with `language`**

When you initialize Link in your application, use the **`language`** parameter to specify the desired language behavior.

### **Web SDK**

```jsx  theme={null}
const connection = createLink({
        ...
        language: 'en-US'
        ...
      })
```

### **Android SDK**

```kotlin  theme={null}
val configuration = LinkConfiguration(
    token = "linkToken",
    language = "en-US")
```

### **iOS SDK**

```swift  theme={null}
let settings = LinkSettings(language: "en-US")
let configuration = LinkConfiguration(
    linkToken: linkToken,
    settings: settings,
    ...
    )
```

### **React native SDK**

```jsx  theme={null}
<LinkConnect settings={{language: 'en-US'}} ... />
```

# Testing Your Implementation

Thoroughly test your implementation to ensure a seamless experience for your users:

* Verify that Link displays correctly in the languages you intend to support.
* Please notify your Mesh support person if you see any words or phrases that you believe are incorrectly translated if you see any layout issues (for example with right-to-left languages or character-based languages).

# Currently supported languages

<aside>
  🤝🏽

  **If you need a language that is not shown as supported below, please notify your Mesh team member to request it be added.**
</aside>

| **Status**                                             | **Language**                   | **Region**                                                                  | **Locale code** |
| ------------------------------------------------------ | ------------------------------ | --------------------------------------------------------------------------- | --------------- |
| <span class="sdk-badge sdk-live">**live**</span>       | English                        | United States <span class="sdk-badge sdk-default">**global default**</span> | **`en-US`**     |
| <span class="sdk-badge sdk-live">**live**</span>       | Spanish                        | United States <span class="sdk-badge sdk-default">**es default**</span>     | **`es-US`**     |
| <span class="sdk-badge sdk-live">**live**</span>       | Russian                        | Russia                                                                      | **`ru-RU`**     |
| <span class="sdk-badge sdk-live">**live**</span>       | French                         | France <span class="sdk-badge sdk-default">**fr default**</span>            | **`fr-FR`**     |
| <span class="sdk-badge sdk-live">**live**</span>       | Chinese/Mandarin (Simplified)  | China <span class="sdk-badge sdk-default">**zh default**</span>             | **`zh-CN`**     |
| <span class="sdk-badge sdk-live">**live**</span>       | Turkish                        | Turkey                                                                      | **`tr-TR`**     |
| <span class="sdk-badge sdk-live">**live**</span>       | Polish                         | Poland                                                                      | **`pl-PL`**     |
| <span class="sdk-badge sdk-live">**live**</span>       | Japanese                       | Japan                                                                       | **`ja-JP`**     |
| <span class="sdk-badge sdk-live">**live**</span>       | German                         | Germany                                                                     | **`de-DE`**     |
| <span class="sdk-badge sdk-live">**live**</span>       | Finnish                        | Finland                                                                     | **`fi-FI`**     |
| <span class="sdk-badge sdk-live">**live**</span>       | Hindi                          | India                                                                       | **`hi-IN`**     |
| <span class="sdk-badge sdk-live">**live**</span>       | Portuguese                     | Portugal <span class="sdk-badge sdk-default">**pt default**</span>          | **`pt-PT`**     |
| <span class="sdk-badge sdk-live">**live**</span>       | Vietnamese                     | Vietnam                                                                     | **`vi-VN`**     |
| <span class="sdk-badge sdk-live">**live**</span>       | system                         |                                                                             | **`system`**    |
| <span class="sdk-badge sdk-backlog">**backlog**</span> | Arabic                         | Egypt                                                                       | **`ar-EG`**     |
| <span class="sdk-badge sdk-backlog">**backlog**</span> | Chinese/Mandarin (Traditional) | United States                                                               | **`zh-US`**     |
| <span class="sdk-badge sdk-backlog">**backlog**</span> | Chinese                        | Hong Kong                                                                   | **`zh-HK`**     |
| <span class="sdk-badge sdk-backlog">**backlog**</span> | Chinese                        | Taiwan                                                                      | **`zh-TW`**     |
| <span class="sdk-badge sdk-backlog">**backlog**</span> | Czech                          | Czech Republic                                                              | **`cs-CZ`**     |
| <span class="sdk-badge sdk-backlog">**backlog**</span> | Danish                         | Denmark                                                                     | **`da-DK`**     |
| <span class="sdk-badge sdk-backlog">**backlog**</span> | Dutch, Flemish                 | Belgium                                                                     | **`nl-NL`**     |
| <span class="sdk-badge sdk-backlog">**backlog**</span> | English                        | Australia                                                                   | **`en-AU`**     |
| <span class="sdk-badge sdk-backlog">**backlog**</span> | English                        | India                                                                       | **`en-IN`**     |
| <span class="sdk-badge sdk-backlog">**backlog**</span> | English                        | United Kingdom                                                              | **`en-GB`**     |
| <span class="sdk-badge sdk-backlog">**backlog**</span> | French                         | Canada                                                                      | **`fr-CA`**     |
| <span class="sdk-badge sdk-backlog">**backlog**</span> | Greek, Modern (1453–)          | Greece                                                                      | **`el-GR`**     |
| <span class="sdk-badge sdk-backlog">**backlog**</span> | Hebrew                         | Israel                                                                      | **`he-IL`**     |
| <span class="sdk-badge sdk-backlog">**backlog**</span> | Hungarian                      | Hungary                                                                     | **`hu-HU`**     |
| <span class="sdk-badge sdk-backlog">**backlog**</span> | Indonesian                     | Indonesia                                                                   | **`id-ID`**     |
| <span class="sdk-badge sdk-backlog">**backlog**</span> | Italian                        | Italy                                                                       | **`it-IT`**     |
| <span class="sdk-badge sdk-backlog">**backlog**</span> | Korean                         | South Korea                                                                 | **`ko-KR`**     |
| <span class="sdk-badge sdk-backlog">**backlog**</span> | Norwegian                      | Norway                                                                      | **`no-NO`**     |
| <span class="sdk-badge sdk-backlog">**backlog**</span> | Portuguese                     | Brazil                                                                      | **`pt-BR`**     |
| <span class="sdk-badge sdk-backlog">**backlog**</span> | Slovak                         | Slovakia                                                                    | **`sk-SK`**     |
| <span class="sdk-badge sdk-backlog">**backlog**</span> | Spanish, Castilian             | Spain                                                                       | **`es-ES`**     |
| <span class="sdk-badge sdk-backlog">**backlog**</span> | Swedish                        | Sweden                                                                      | **`sv-SE`**     |
| <span class="sdk-badge sdk-backlog">**backlog**</span> | Thai                           | Thailand                                                                    | **`th-TH`**     |
