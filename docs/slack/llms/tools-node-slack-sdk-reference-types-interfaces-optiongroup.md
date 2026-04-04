Source: https://docs.slack.dev/tools/node-slack-sdk/reference/types/interfaces/OptionGroup

[@slack/types](/tools/node-slack-sdk/reference/types/) / OptionGroup

# Interface: OptionGroup

Defined in: [block-kit/composition-objects.ts:115](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/composition-objects.ts#L115)

## Description {#description}

Defines a way to group options in a select or multi-select menu.

## See {#see}

[Option group object reference](https://docs.slack.dev/reference/block-kit/composition-objects/option-group-object).

## Properties {#properties}

### label {#label}

```
label: PlainTextElement;
```

Defined in: [block-kit/composition-objects.ts:120](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/composition-objects.ts#L120)

#### Description {#description-1}

A [PlainTextElement](/tools/node-slack-sdk/reference/types/interfaces/PlainTextElement) text object that defines the label shown above this group of options. Maximum length for the `text` in this field is 75 characters.

* * *

### options {#options}

```
options: Option[];
```

Defined in: [block-kit/composition-objects.ts:124](https://github.com/slackapi/node-slack-sdk/blob/main/packages/types/src/block-kit/composition-objects.ts#L124)

#### Description {#description-2}

An array of [Option](/tools/node-slack-sdk/reference/types/type-aliases/Option) that belong to this specific group. Maximum of 100 items.
