# Source: https://firebase.google.com/docs/reference/js/ai.imagensafetysettings.md.txt

Settings for controlling the aggressiveness of filtering out sensitive content.

See the [documentation](http://firebase.google.com/docs/vertex-ai/generate-images) for more details.

**Signature:**  

    export interface ImagenSafetySettings 

## Properties

|                                                              Property                                                               |                                                  Type                                                  |                                           Description                                            |
|-------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------|
| [personFilterLevel](https://firebase.google.com/docs/reference/js/ai.imagensafetysettings.md#imagensafetysettingspersonfilterlevel) | [ImagenPersonFilterLevel](https://firebase.google.com/docs/reference/js/ai.md#imagenpersonfilterlevel) | A filter level controlling whether generation of images containing people or faces is allowed.   |
| [safetyFilterLevel](https://firebase.google.com/docs/reference/js/ai.imagensafetysettings.md#imagensafetysettingssafetyfilterlevel) | [ImagenSafetyFilterLevel](https://firebase.google.com/docs/reference/js/ai.md#imagensafetyfilterlevel) | A filter level controlling how aggressive to filter out sensitive content from generated images. |

## ImagenSafetySettings.personFilterLevel

A filter level controlling whether generation of images containing people or faces is allowed.

**Signature:**  

    personFilterLevel?: ImagenPersonFilterLevel;

## ImagenSafetySettings.safetyFilterLevel

A filter level controlling how aggressive to filter out sensitive content from generated images.

**Signature:**  

    safetyFilterLevel?: ImagenSafetyFilterLevel;