Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/PlainTextOption

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / PlainTextOption

# Interface: PlainTextOption

Defined in: packages/types/dist/block-kit/composition-objects.d.ts:87

## Extends {#extends}

* `OptionDescriptor`

## Properties {#properties}

### description? {#description}

```text
optional description: PlainTextElement;
```text

Defined in: packages/types/dist/block-kit/composition-objects.d.ts:78

#### Description {#description-1}

A [PlainTextElement](/tools/node-slack-sdk/reference/web-api/interfaces/PlainTextElement) that defines a line of descriptive text shown below the `text` field. Maximum length for the `text` within this field is 75 characters.

#### Inherited from {#inherited-from}

```text
OptionDescriptor.description
```text

* * *

### text {#text}

```text
text: PlainTextElement;
```text

Defined in: packages/types/dist/block-kit/composition-objects.d.ts:92

#### Description {#description-2}

A [PlainTextElement](/tools/node-slack-sdk/reference/web-api/interfaces/PlainTextElement) that defines the text shown in the option on the menu. To be used with overflow, select and multi-select menus. Maximum length for the `text` in this field is 75 characters.

* * *

### url? {#url}

```text
optional url: string;
```text

Defined in: packages/types/dist/block-kit/composition-objects.d.ts:73

#### Description {#description-3}

Only available in overflow menus! A URL to load in the user's browser when the option is clicked. Maximum length for this field is 3000 characters.

#### Inherited from {#inherited-from-1}

```text
OptionDescriptor.url
```text

* * *

### value? {#value}

```text
optional value: string;
```text

Defined in: packages/types/dist/block-kit/composition-objects.d.ts:68

#### Description {#description-4}

A unique string value that will be passed to your app when this option is chosen. Maximum length for this field is 75 characters.

#### Inherited from {#inherited-from-2}

```text
OptionDescriptor.value
```text
