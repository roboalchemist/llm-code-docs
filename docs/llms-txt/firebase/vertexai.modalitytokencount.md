# Source: https://firebase.google.com/docs/reference/js/vertexai.modalitytokencount.md.txt

# ModalityTokenCount interface

Represents token counting info for a single modality.

**Signature:**  

    export interface ModalityTokenCount 

## Properties

|                                                        Property                                                         |                                      Type                                      |                  Description                   |
|-------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------|------------------------------------------------|
| [modality](https://firebase.google.com/docs/reference/js/vertexai.modalitytokencount.md#modalitytokencountmodality)     | [Modality](https://firebase.google.com/docs/reference/js/vertexai.md#modality) | The modality associated with this token count. |
| [tokenCount](https://firebase.google.com/docs/reference/js/vertexai.modalitytokencount.md#modalitytokencounttokencount) | number                                                                         | The number of tokens counted.                  |

## ModalityTokenCount.modality

The modality associated with this token count.

**Signature:**  

    modality: Modality;

## ModalityTokenCount.tokenCount

The number of tokens counted.

**Signature:**  

    tokenCount: number;