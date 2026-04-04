# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/ShaCertificate.md.txt

# ShaCertificate

public class **ShaCertificate** extends Object  
Information about an SHA certificate associated with an Android app.  

### Public Method Summary

|------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| static [ShaCertificate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/ShaCertificate)  | [create](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/ShaCertificate#create(java.lang.String))(String shaHash) Creates an [ShaCertificate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/ShaCertificate) from the given certificate hash. |
| boolean                                                                                                                                        | [equals](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/ShaCertificate#equals(java.lang.Object))(Object o)                                                                                                                                                                                          |
| [ShaCertificateType](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/ShaCertificateType) | [getCertType](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/ShaCertificate#getCertType())() Returns the type of this SHA certificate.                                                                                                                                                              |
| String                                                                                                                                         | [getName](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/ShaCertificate#getName())() Returns the fully qualified resource name of this SHA certificate.                                                                                                                                             |
| String                                                                                                                                         | [getShaHash](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/ShaCertificate#getShaHash())() Returns the hash of this SHA certificate.                                                                                                                                                                |
| int                                                                                                                                            | [hashCode](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/ShaCertificate#hashCode())()                                                                                                                                                                                                              |
| String                                                                                                                                         | [toString](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/ShaCertificate#toString())()                                                                                                                                                                                                              |

### Inherited Method Summary

From class java.lang.Object  

|------------------|---------------------------|
| Object           | clone()                   |
| boolean          | equals(Object arg0)       |
| void             | finalize()                |
| final Class\<?\> | getClass()                |
| int              | hashCode()                |
| final void       | notify()                  |
| final void       | notifyAll()               |
| String           | toString()                |
| final void       | wait(long arg0, int arg1) |
| final void       | wait(long arg0)           |
| final void       | wait()                    |

## Public Methods

#### public static [ShaCertificate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/ShaCertificate)
**create**
(String shaHash)

Creates an [ShaCertificate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/ShaCertificate) from the given certificate hash.

The fully qualified resource name of this certificate will be set to the empty string since
it has not been generated yet.  

##### Parameters

| shaHash | SHA hash of the certificate |
|---------|-----------------------------|

##### Returns

- a new [ShaCertificate](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/ShaCertificate) instance  

#### public boolean
**equals**
(Object o)

<br />

#### public [ShaCertificateType](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/projectmanagement/ShaCertificateType)
**getCertType**
()

Returns the type of this SHA certificate.  

#### public String
**getName**
()

Returns the fully qualified resource name of this SHA certificate.  

#### public String
**getShaHash**
()

Returns the hash of this SHA certificate.  

#### public int
**hashCode**
()

<br />

#### public String
**toString**
()

<br />