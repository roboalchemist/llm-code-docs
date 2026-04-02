Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/PlainTextOption

[@slack/types](/tools/node-slack-sdk/reference/types/) / PlainTextOption

# Interface: PlainTextOption

Defined in: [block-kit/composition-objects.ts:96](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/composition-objects.ts#L96)

## Extends {#extends}

* `OptionDescriptor`

## Properties {#properties}

### description? {#description}

```
optional description: PlainTextElement;
```

Defined in: [block-kit/composition-objects.ts:85](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/composition-objects.ts#L85)

#### Description {#description-1}

A [PlainTextElement](/tools/node-slack-sdk/reference/types/interfaces/PlainTextElement) that defines a line of descriptive text shown below the `text` field. Maximum length for the `text` within this field is 75 characters.

#### Inherited from {#inherited-from}

```
OptionDescriptor.description
```

* * *

### text {#text}

```
text: PlainTextElement;
```

Defined in: [block-kit/composition-objects.ts:101](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/composition-objects.ts#L101)

#### Description {#description-2}

A [PlainTextElement](/tools/node-slack-sdk/reference/types/interfaces/PlainTextElement) that defines the text shown in the option on the menu. To be used with overflow, select and multi-select menus. Maximum length for the `text` in this field is 75 characters.

* * *

### url? {#url}

```
optional url: string;
```

Defined in: [block-kit/composition-objects.ts:80](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/composition-objects.ts#L80)

#### Description {#description-3}

Only available in overflow menus! A URL to load in the user's browser when the option is clicked. Maximum length for this field is 3000 characters.

#### Inherited from {#inherited-from-1}

```
OptionDescriptor.url
```

* * *

### value? {#value}

```
optional value: string;
```

Defined in: [block-kit/composition-objects.ts:75](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/composition-objects.ts#L75)

#### Description {#description-4}

A unique string value that will be passed to your app when this option is chosen. Maximum length for this field is 75 characters.

#### Inherited from {#inherited-from-2}

```
OptionDescriptor.value
```
