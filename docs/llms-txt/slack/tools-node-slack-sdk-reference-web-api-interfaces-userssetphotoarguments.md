Source: https://docs.slack.dev/tools/node-slack-sdk/reference/web-api/interfaces/UsersSetPhotoArguments

[@slack/web-api](/tools/node-slack-sdk/reference/web-api/) / UsersSetPhotoArguments

# Interface: UsersSetPhotoArguments

Defined in: [packages/web-api/src/types/request/users.ts:50](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/users.ts#L50)

## Extends {#extends}

* `TokenOverridable`

## Properties {#properties}

### crop_w? {#crop_w}

```text
optional crop_w: number;
```text

Defined in: [packages/web-api/src/types/request/users.ts:54](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/users.ts#L54)

#### Description {#description}

Width/height of crop box (always square).

* * *

### crop_x? {#crop_x}

```text
optional crop_x: number;
```text

Defined in: [packages/web-api/src/types/request/users.ts:56](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/users.ts#L56)

#### Description {#description-1}

X coordinate of top-left corner of crop box.

* * *

### crop_y? {#crop_y}

```text
optional crop_y: number;
```text

Defined in: [packages/web-api/src/types/request/users.ts:58](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/users.ts#L58)

#### Description {#description-2}

Y coordinate of top-left corner of crop box.

* * *

### image {#image}

```text
image: Buffer<ArrayBufferLike> | Stream;
```text

Defined in: [packages/web-api/src/types/request/users.ts:52](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/users.ts#L52)

#### Description {#description-3}

Image file contents.

* * *

### token? {#token}

```text
optional token: string;
```text

Defined in: [packages/web-api/src/types/request/common.ts:43](https://github.com/slackapi/node-slack-sdk/blob/main/packages/web-api/src/types/request/common.ts#L43)

#### Description {#description-4}

Overridable authentication token bearing required scopes.

#### Inherited from {#inherited-from}

```text
TokenOverridable.token
```text
