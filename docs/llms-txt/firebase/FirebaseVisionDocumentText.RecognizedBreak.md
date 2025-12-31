# Source: https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.RecognizedBreak.md.txt

# FirebaseVisionDocumentText.RecognizedBreak

public static class **FirebaseVisionDocumentText.RecognizedBreak** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
Detected start or end of a structural component.  

### Nested Class Summary

|------------|---|---|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| @interface | [FirebaseVisionDocumentText.RecognizedBreak.BreakType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.RecognizedBreak.BreakType) || Detected start or end of a structural component type: [UNKNOWN](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.RecognizedBreak#UNKNOWN), [SPACE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.RecognizedBreak#SPACE) [SURE_SPACE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.RecognizedBreak#SURE_SPACE), [EOL_SURE_SPACE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.RecognizedBreak#EOL_SURE_SPACE), [HYPHEN](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.RecognizedBreak#HYPHEN), [LINE_BREAK](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.RecognizedBreak#LINE_BREAK). |

### Constant Summary

|-----|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| int | [EOL_SURE_SPACE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.RecognizedBreak#EOL_SURE_SPACE) | Line-wrapping break.                                                                                                |
| int | [HYPHEN](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.RecognizedBreak#HYPHEN)                 | End-line hyphen that is not present in text; does not co-occur with \`SPACE\`, \`LEADER_SPACE\`, or \`LINE_BREAK\`. |
| int | [LINE_BREAK](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.RecognizedBreak#LINE_BREAK)         | Line break that ends a paragraph.                                                                                   |
| int | [SPACE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.RecognizedBreak#SPACE)                   | Regular space.                                                                                                      |
| int | [SURE_SPACE](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.RecognizedBreak#SURE_SPACE)         | Sure space (very wide).                                                                                             |
| int | [UNKNOWN](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.RecognizedBreak#UNKNOWN)               | Unknown break label type.                                                                                           |

### Public Method Summary

|---------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| int     | [getDetectedBreakType](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.RecognizedBreak#getDetectedBreakType())() Gets detected break type.  |
| boolean | [getIsPrefix](https://firebase.google.com/docs/reference/android/com/google/firebase/ml/vision/document/FirebaseVisionDocumentText.RecognizedBreak#getIsPrefix())() Returns `true` if break prepends an element. |

### Inherited Method Summary

From class java.lang.Object  

|----------------------------------------------------------------------------------|--------------------------------------------------------------------------------------|
| [Object](https://developer.android.com/reference/java/lang/Object.html)          | clone()                                                                              |
| boolean                                                                          | equals([Object](https://developer.android.com/reference/java/lang/Object.html) arg0) |
| void                                                                             | finalize()                                                                           |
| final [Class](https://developer.android.com/reference/java/lang/Class.html)\<?\> | getClass()                                                                           |
| int                                                                              | hashCode()                                                                           |
| final void                                                                       | notify()                                                                             |
| final void                                                                       | notifyAll()                                                                          |
| [String](https://developer.android.com/reference/java/lang/String.html)          | toString()                                                                           |
| final void                                                                       | wait(long arg0, int arg1)                                                            |
| final void                                                                       | wait(long arg0)                                                                      |
| final void                                                                       | wait()                                                                               |

## Constants

#### public static final int
**EOL_SURE_SPACE**

Line-wrapping break.  
Constant Value: 3  

#### public static final int
**HYPHEN**

End-line hyphen that is not present in text; does not co-occur with \`SPACE\`,
\`LEADER_SPACE\`, or \`LINE_BREAK\`.  
Constant Value: 4  

#### public static final int
**LINE_BREAK**

Line break that ends a paragraph.  
Constant Value: 5  

#### public static final int
**SPACE**

Regular space.  
Constant Value: 1  

#### public static final int
**SURE_SPACE**

Sure space (very wide).  
Constant Value: 2  

#### public static final int
**UNKNOWN**

Unknown break label type.  
Constant Value: 0

## Public Methods

#### public int **getDetectedBreakType** ()

Gets detected break type.  

#### public boolean **getIsPrefix** ()

Returns `true` if break prepends an element.