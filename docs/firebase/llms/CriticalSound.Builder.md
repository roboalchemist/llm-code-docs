# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/CriticalSound.Builder.md.txt

# CriticalSound.Builder

public static final class **CriticalSound.Builder** extends Object  

### Public Method Summary

|----------------------------------------------------------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [CriticalSound](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/CriticalSound)                 | [build](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/CriticalSound.Builder#build())() Builds a new [CriticalSound](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/CriticalSound) instance from the fields set on this builder. |
| [CriticalSound.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/CriticalSound.Builder) | [setCritical](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/CriticalSound.Builder#setCritical(boolean))(boolean critical) Sets the critical alert flag on the sound configuration.                                                                                             |
| [CriticalSound.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/CriticalSound.Builder) | [setName](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/CriticalSound.Builder#setName(java.lang.String))(String name) The name of a sound file in your app's main bundle or in the `Library/Sounds` folder of your app's container directory.                                  |
| [CriticalSound.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/CriticalSound.Builder) | [setVolume](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/CriticalSound.Builder#setVolume(double))(double volume) The volume for the critical alert's sound.                                                                                                                   |

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

#### public [CriticalSound](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/CriticalSound)
**build**
()

Builds a new [CriticalSound](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/CriticalSound) instance from the fields set on this builder.  

##### Returns

- A non-null [CriticalSound](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/CriticalSound).  

##### Throws

| IllegalArgumentException | If the volume value is out of range. |
|--------------------------|--------------------------------------|

#### public [CriticalSound.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/CriticalSound.Builder)
**setCritical**
(boolean critical)

Sets the critical alert flag on the sound configuration.  

##### Parameters

| critical | True to set the critical alert flag. |
|----------|--------------------------------------|

##### Returns

- This builder.  

#### public [CriticalSound.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/CriticalSound.Builder)
**setName**
(String name)

The name of a sound file in your app's main bundle or in the `Library/Sounds` folder
of your app's container directory. Specify the string `default` to play the system
sound.  

##### Parameters

| name | Sound file name. |
|------|------------------|

##### Returns

- This builder.  

#### public [CriticalSound.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/CriticalSound.Builder)
**setVolume**
(double volume)

The volume for the critical alert's sound. Must be a value between 0.0 (silent) and 1.0
(full volume).  

##### Parameters

| volume | A volume between 0.0 (inclusive) and 1.0 (inclusive). |
|--------|-------------------------------------------------------|

##### Returns

- This builder.