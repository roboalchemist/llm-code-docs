# Source: https://firebase.google.com/docs/reference/functions/firebase-functions.auth.useroptions.md.txt

# auth.UserOptions interface

Options for Auth blocking function.

**Signature:**  

    export interface UserOptions 

## Properties

|                                                                   Property                                                                    |                                 Type                                  |                                Description                                 |
|-----------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------|----------------------------------------------------------------------------|
| [blockingOptions](https://firebase.google.com/docs/reference/functions/firebase-functions.auth.useroptions.md#authuseroptionsblockingoptions) | { idToken?: boolean; accessToken?: boolean; refreshToken?: boolean; } | Options to set configuration at the resource level for blocking functions. |

## auth.UserOptions.blockingOptions

Options to set configuration at the resource level for blocking functions.

**Signature:**  

    blockingOptions?: {
            idToken?: boolean;
            accessToken?: boolean;
            refreshToken?: boolean;
        };