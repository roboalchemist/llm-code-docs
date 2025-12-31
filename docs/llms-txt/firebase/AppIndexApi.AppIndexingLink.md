# Source: https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/AppIndexApi.AppIndexingLink.md.txt

# AppIndexApi.AppIndexingLink

public static final class **AppIndexApi.AppIndexingLink** extends [Object](https://developer.android.com/reference/java/lang/Object.html)  
**This class is deprecated.**   

No replacement.

An outbound link attached to viewed content.  

### Field Summary

|----------------------------------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------|
| public final [Uri](https://developer.android.com/reference/android/net/Uri.html) | [appIndexingUrl](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/AppIndexApi.AppIndexingLink#appIndexingUrl) | App URI in the [App Indexing](https://developers.google.com/app-indexing/) format. |
| public final int                                                                 | [viewId](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/AppIndexApi.AppIndexingLink#viewId)                 | View id of this link in the rendered content.                                      |
| public final [Uri](https://developer.android.com/reference/android/net/Uri.html) | [webUrl](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/AppIndexApi.AppIndexingLink#webUrl)                 | Optional equivalent web URL of this content.                                       |

### Public Constructor Summary

|---|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [AppIndexingLink](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/AppIndexApi.AppIndexingLink#AppIndexingLink(android.net.Uri,%20android.net.Uri,%20android.view.View))([Uri](https://developer.android.com/reference/android/net/Uri.html) appUri, [Uri](https://developer.android.com/reference/android/net/Uri.html) webUrl, [View](https://developer.android.com/reference/android/view/View.html) view) |
|   | [AppIndexingLink](https://firebase.google.com/docs/reference/android/com/google/android/gms/appindexing/AppIndexApi.AppIndexingLink#AppIndexingLink(android.net.Uri,%20android.view.View))([Uri](https://developer.android.com/reference/android/net/Uri.html) appUri, [View](https://developer.android.com/reference/android/view/View.html) view)                                                                                                |

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

## Fields

#### public final [Uri](https://developer.android.com/reference/android/net/Uri.html)
**appIndexingUrl**

App URI in the [App Indexing](https://developers.google.com/app-indexing/)
format.  

#### public final int
**viewId**

View id of this link in the rendered content.  

#### public final [Uri](https://developer.android.com/reference/android/net/Uri.html)
**webUrl**

Optional equivalent web URL of this content.

## Public Constructors

#### public **AppIndexingLink** ([Uri](https://developer.android.com/reference/android/net/Uri.html) appUri, [Uri](https://developer.android.com/reference/android/net/Uri.html) webUrl, [View](https://developer.android.com/reference/android/view/View.html) view)

#### public **AppIndexingLink** ([Uri](https://developer.android.com/reference/android/net/Uri.html) appUri, [View](https://developer.android.com/reference/android/view/View.html) view)