# Source: https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/LightSettings.Builder.md.txt

# LightSettings.Builder

public static class **LightSettings.Builder** extends Object  

### Public Method Summary

|----------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| [LightSettings](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/LightSettings)                 | [build](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/LightSettings.Builder#build())() Builds a new [LightSettings](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/LightSettings) instance from the fields set on this builder.                                                                    |
| [LightSettings.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/LightSettings.Builder) | [setColor](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/LightSettings.Builder#setColor(com.google.firebase.messaging.LightSettingsColor))([LightSettingsColor](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/LightSettingsColor) color) Sets the lightSettingsColor value in the light settings. |
| [LightSettings.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/LightSettings.Builder) | [setColorFromString](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/LightSettings.Builder#setColorFromString(java.lang.String))(String color) Sets the lightSettingsColor value with a string.                                                                                                                                                     |
| [LightSettings.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/LightSettings.Builder) | [setLightOffDurationInMillis](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/LightSettings.Builder#setLightOffDurationInMillis(long))(long lightOffDurationInMillis) Sets the light off duration in milliseconds.                                                                                                                                  |
| [LightSettings.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/LightSettings.Builder) | [setLightOnDurationInMillis](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/LightSettings.Builder#setLightOnDurationInMillis(long))(long lightOnDurationInMillis) Sets the light on duration in milliseconds.                                                                                                                                      |

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

#### public [LightSettings](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/LightSettings)
**build**
()

Builds a new [LightSettings](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/LightSettings) instance from the fields set on this builder.  

##### Returns

- A non-null [LightSettings](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/LightSettings).  

##### Throws

| IllegalArgumentException | If the volume value is out of range. |
|--------------------------|--------------------------------------|

#### public [LightSettings.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/LightSettings.Builder)
**setColor**
([LightSettingsColor](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/LightSettingsColor) color)

Sets the lightSettingsColor value in the light settings.  

##### Parameters

| color | Color to be used in the light settings. |
|-------|-----------------------------------------|

##### Returns

- This builder.  

#### public [LightSettings.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/LightSettings.Builder)
**setColorFromString**
(String color)

Sets the lightSettingsColor value with a string.  

##### Parameters

| color | LightSettingsColor specified in the `#rrggbb` format. |
|-------|-------------------------------------------------------|

##### Returns

- This builder.  

#### public [LightSettings.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/LightSettings.Builder)
**setLightOffDurationInMillis**
(long lightOffDurationInMillis)

Sets the light off duration in milliseconds.  

##### Parameters

| lightOffDurationInMillis | The time duration in milliseconds for the LED light to be off. |
|--------------------------|----------------------------------------------------------------|

##### Returns

- This builder.  

#### public [LightSettings.Builder](https://firebase.google.com/docs/reference/admin/java/reference/com/google/firebase/messaging/LightSettings.Builder)
**setLightOnDurationInMillis**
(long lightOnDurationInMillis)

Sets the light on duration in milliseconds.  

##### Parameters

| lightOnDurationInMillis | The time duration in milliseconds for the LED light to be on. |
|-------------------------|---------------------------------------------------------------|

##### Returns

- This builder.