Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/OptionGroup

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / OptionGroup

# Interface: OptionGroup

Defined in: packages/types/dist/block-kit/composition-objects.d.ts:104

## Description {#description}

Defines a way to group options in a select or multi-select menu.

## See {#see}

[Option group object reference](https://docs.slack.dev/reference/block-kit/composition-objects/option-group-object).

## Properties {#properties}

### label {#label}

```text
label: PlainTextElement;
```text

Defined in: packages/types/dist/block-kit/composition-objects.d.ts:109

#### Description {#description-1}

A [PlainTextElement](/tools/node-slack-sdk/reference/web-api/interfaces/PlainTextElement) text object that defines the label shown above this group of options. Maximum length for the `text` in this field is 75 characters.

* * *

### options {#options}

```text
options: Option[];
```text

Defined in: packages/types/dist/block-kit/composition-objects.d.ts:113

#### Description {#description-2}

An array of [Option](/tools/node-slack-sdk/reference/web-api/type-aliases/Option) that belong to this specific group. Maximum of 100 items.
