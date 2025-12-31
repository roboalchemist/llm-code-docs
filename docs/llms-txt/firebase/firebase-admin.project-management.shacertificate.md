# Source: https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.shacertificate.md.txt

# ShaCertificate class

A SHA-1 or SHA-256 certificate.

Do not call this constructor directly. Instead, use \[`projectManagement.shaCertificate()`\](projectManagement.ProjectManagement#shaCertificate).

**Signature:**  

    export declare class ShaCertificate 

## Properties

|                                                                       Property                                                                       | Modifiers |         Type         |        Description        |
|------------------------------------------------------------------------------------------------------------------------------------------------------|-----------|----------------------|---------------------------|
| [certType](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.shacertificate.md#shacertificatecerttype)         |           | ('sha1' \| 'sha256') | The SHA certificate type. |
| [resourceName](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.shacertificate.md#shacertificateresourcename) |           | string \| undefined  |                           |
| [shaHash](https://firebase.google.com/docs/reference/admin/node/firebase-admin.project-management.shacertificate.md#shacertificateshahash)           |           | string               |                           |

## ShaCertificate.certType

The SHA certificate type.

**Signature:**  

    readonly certType: ('sha1' | 'sha256');

### Example

    var certType = shaCertificate.certType;

## ShaCertificate.resourceName

**Signature:**  

    readonly resourceName?: string | undefined;

## ShaCertificate.shaHash

**Signature:**  

    readonly shaHash: string;