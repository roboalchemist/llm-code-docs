# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Action.md.txt

# WebpushNotification.Action

public static class **WebpushNotification.Action** extends Object  
Represents an action available to users when the notification is presented.  

### Public Constructor Summary

|---|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
|   | [Action](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Action#Action(java.lang.String, java.lang.String))(String action, String title) Creates a new Action with the given action string and title.                                          |
|   | [Action](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/WebpushNotification.Action#Action(java.lang.String, java.lang.String, java.lang.String))(String action, String title, String icon) Creates a new Action with the given action string, title and icon URL. |

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

## Public Constructors

#### public
**Action**
(String action, String title)

Creates a new Action with the given action string and title.  

##### Parameters

| action | Action string. |
| title  |  Title text.   |
|--------|----------------|

#### public
**Action**
(String action, String title, String icon)

Creates a new Action with the given action string, title and icon URL.  

##### Parameters

| action |  Action string.   |
| title  |    Title text.    |
|  icon  | Icon URL or null. |
|--------|-------------------|