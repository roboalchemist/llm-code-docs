# Source: https://docs.expo.dev/versions/latest/sdk/contacts

---
title: Contacts
description: A library that provides access to the phone's system contacts.
sourceCodeUrl: 'https://github.com/expo/expo/tree/main/packages/expo-contacts'
packageName: 'expo-contacts'
iconUrl: '/static/images/packages/expo-contacts.png'
platforms: ['android', 'ios', 'expo-go']
---

# Expo Contacts

A library that provides access to the phone's system contacts.
Android, iOS, Included in Expo Go

`expo-contacts` provides access to the device's system contacts, allowing you to get contact information as well as adding, editing, or removing contacts.

On iOS, contacts have a multi-layered grouping system that you can also access through this API.

## Installation

```sh
npx expo install expo-contacts
```

If you are installing this in an [existing React Native app](/bare/overview), make sure to [install `expo`](/bare/installing-expo-modules) in your project.

## Configuration in app config

You can configure `expo-contacts` using its built-in [config plugin](/config-plugins/introduction) if you use config plugins in your project ([Continuous Native Generation (CNG)](/workflow/continuous-native-generation)). The plugin allows you to configure various properties that cannot be set at runtime and require building a new app binary to take effect. If your app does **not** use CNG, then you'll need to manually configure the library.

### Example app.json with config plugin

```json
{
  "expo": {
    "plugins": [
      [
        "expo-contacts",
        {
          "contactsPermission": "Allow $(PRODUCT_NAME) to access your contacts."
        }
      ]
    ]
  }
}
```

### Configurable properties

| Name | Default | Description |
| --- | --- | --- |
| `contactsPermission` | `"Allow $(PRODUCT_NAME) to access your contacts"` | Only for: iOS. A string to set the [`NSContactsUsageDescription`](#ios) permission message. |

Are you using this library in an existing React Native app?

If you're not using Continuous Native Generation ([CNG](/workflow/continuous-native-generation)) (you're using native **android** and **ios** projects manually), then you need to configure following permissions in your native projects:

-   For Android, add `android.permission.READ_CONTACTS` and `android.permission.WRITE_CONTACTS` permissions to your project's **android/app/src/main/AndroidManifest.xml**:
    
    ```xml
    <uses-permission android:name="android.permission.READ_CONTACTS" />
    <uses-permission android:name="android.permission.WRITE_CONTACTS" />
    ```
    
-   For iOS, add the `NSContactsUsageDescription` key to your project's **ios/[app]/Info.plist**:
    
    ```xml
    <key>NSContactsUsageDescription</key>
    <string>Allow $(PRODUCT_NAME) to access your contacts</string>
    ```

## Usage

```jsx
import { useEffect } from 'react';
import { StyleSheet, View, Text } from 'react-native';
import * as Contacts from 'expo-contacts';

export default function App() {
  useEffect(() => {
    (async () => {
      const { status } = await Contacts.requestPermissionsAsync();
      if (status === 'granted') {
        const { data } = await Contacts.getContactsAsync({
          fields: [Contacts.Fields.Emails],
        });

        if (data.length > 0) {
          const contact = data[0];
          console.log(contact);
        }
      }
    })();
  }, []);

  return (
    <View style={styles.container}>
      <Text>Contacts Module Example</Text>
    </View>
  );
}

const styles = StyleSheet.create({
  container: {
    flex: 1,
    backgroundColor: '#fff',
    alignItems: 'center',
    justifyContent: 'center',
  },
});
```

## API

```js
import * as Contacts from 'expo-contacts';
```

## Component

### `ContactAccessButton`

Supported platforms: iOS 18.0+.

Type: React.[PureComponent](https://react.dev/reference/react/PureComponent)<[ContactAccessButtonProps](#contactaccessbuttonprops)\>

Creates a contact access button to quickly add contacts under limited-access authorization.

For more details, you can read the Apple docs about the underlying [`ContactAccessButton`](https://developer.apple.com/documentation/contactsui/contactaccessbutton) SwiftUI view.

ContactAccessButtonProps

### `backgroundColor`

Supported platforms: iOS 18.0+.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

A color of the button's background. Provided color should not be transparent, otherwise it may not satisfy platform requirements for button legibility.

### `caption`

Supported platforms: iOS 18.0+.

Optional • Literal type: `string`

When the query produces a single result, the contact access button shows the caption under the matching contact name. It can be nothing (default), email address or phone number.

Acceptable values are: `'default'` | `'email'` | `'phone'`

### `ignoredEmails`

Supported platforms: iOS 18.0+.

Optional • Type: `string[]`

An array of email addresses. The search omits contacts matching query that also match any email address in this array.

### `ignoredPhoneNumbers`

Supported platforms: iOS 18.0+.

Optional • Type: `string[]`

An array of phone numbers. The search omits contacts matching query that also match any phone number in this set.

### `query`

Supported platforms: iOS 18.0+.

Optional • Type: `string`

A string to match against contacts not yet exposed to the app. You typically get this value from a search UI that your app presents, like a text field.

### `textColor`

Supported platforms: iOS 18.0+.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

A color of the button's title. Slightly dimmed version of this color is used for the caption text. Make sure there is a good contrast between the text and the background, otherwise platform requirements for button legibility may not be satisfied.

### `tintColor`

Supported platforms: iOS 18.0+.

Optional • Type: [ColorValue](https://reactnative.dev/docs/colors)

A tint color of the button and the modal that is presented when there is more than one match.

#### Inherited Props

-   [ViewProps](https://reactnative.dev/docs/view#props)

## Static Methods

### `isAvailable()`

Supported platforms: Android, iOS.

Returns a boolean whether the `ContactAccessButton` is available on the platform. This is `true` only on iOS 18.0 and newer.

Returns: `boolean`

## Constants

### `Contacts.onContactsChangeEventName`

Supported platforms: Android, iOS.

Type: `'onContactsChange'`

## Methods

### `Contacts.addContactAsync(contact, containerId)`

Supported platforms: Android, iOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `contact` | [Contact](#contact) | A contact with the changes you wish to persist. The `id` parameter will not be used. |
| `containerId`(optional) | `string` | - |

  

Creates a new contact and adds it to the system.

> **Note**: For Android users, the Expo Go app does not have the required `WRITE_CONTACTS` permission to write to Contacts. You will need to create a [development build](/develop/development-builds/create-a-build) and add permission in there manually to use this method.

Returns: `Promise<string>`

A promise that fulfills with ID of the new system contact.

Example

```js
const contact = {
  [Contacts.Fields.FirstName]: 'Bird',
  [Contacts.Fields.LastName]: 'Man',
  [Contacts.Fields.Company]: 'Young Money',
};
const contactId = await Contacts.addContactAsync(contact);
```

### `Contacts.addExistingContactToGroupAsync(contactId, groupId)`

Supported platforms: iOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `contactId` | `string` | ID of the contact you want to edit. |
| `groupId` | `string` | ID for the group you want to add membership to. |

  

Add a contact as a member to a group. A contact can be a member of multiple groups.

Returns: `Promise<any>`

Example

```js
await Contacts.addExistingContactToGroupAsync(
  '665FDBCFAE55-D614-4A15-8DC6-161A368D',
  '161A368D-D614-4A15-8DC6-665FDBCFAE55'
);
```

### `Contacts.addExistingGroupToContainerAsync(groupId, containerId)`

Supported platforms: iOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `groupId` | `string` | The group you want to target. |
| `containerId` | `string` | The container you want to add membership to. |

  

Add a group to a container.

Returns: `Promise<any>`

Example

```js
await Contacts.addExistingGroupToContainerAsync(
  '161A368D-D614-4A15-8DC6-665FDBCFAE55',
  '665FDBCFAE55-D614-4A15-8DC6-161A368D'
);
```

### `Contacts.createGroupAsync(name, containerId)`

Supported platforms: iOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `name`(optional) | `string` | Name of the new group. |
| `containerId`(optional) | `string` | The container you to add membership to. |

  

Create a group with a name, and add it to a container. If the container is `undefined`, the default container will be targeted.

Returns: `Promise<string>`

A promise that fulfills with ID of the new group.

Example

```js
const groupId = await Contacts.createGroupAsync('Sailor Moon');
```

### `Contacts.getContactByIdAsync(id, fields)`

Supported platforms: Android, iOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `id` | `string` | The ID of a system contact. |
| `fields`(optional) | [FieldType[]](#fieldtype) | If specified, the fields defined will be returned. When skipped, all fields will be returned. |

  

Used for gathering precise data about a contact. Returns a contact matching the given `id`.

Returns: `Promise<existingcontact>`

A promise that fulfills with `Contact` object with ID matching the input ID, or `undefined` if there is no match.

Example

```js
const contact = await Contacts.getContactByIdAsync('161A368D-D614-4A15-8DC6-665FDBCFAE55');
if (contact) {
  console.log(contact);
}
```

### `Contacts.getContactsAsync(contactQuery)`

Supported platforms: Android, iOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `contactQuery`(optional) | [ContactQuery](#contactquery) | Object used to query contacts. Default: `{}` |

  

Return a list of contacts that fit a given criteria. You can get all of the contacts by passing no criteria.

Returns: `Promise<contactresponse>`

A promise that fulfills with `ContactResponse` object returned from the query.

Example

```js
const { data } = await Contacts.getContactsAsync({
  fields: [Contacts.Fields.Emails],
});

if (data.length > 0) {
  const contact = data[0];
  console.log(contact);
}
```

### `Contacts.getContainersAsync(containerQuery)`

Supported platforms: iOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `containerQuery` | [ContainerQuery](#containerquery) | Information used to gather containers. |

  

Query a list of system containers.

Returns: `Promise<container[]>`

A promise that fulfills with array of containers that fit the query.

Example

```js
const allContainers = await Contacts.getContainersAsync({
  contactId: '665FDBCFAE55-D614-4A15-8DC6-161A368D',
});
```

### `Contacts.getDefaultContainerIdAsync()`

Supported platforms: iOS.

Get the default container's ID.

Returns: `Promise<string>`

A promise that fulfills with default container ID.

Example

```js
const containerId = await Contacts.getDefaultContainerIdAsync();
```

### `Contacts.getGroupsAsync(groupQuery)`

Supported platforms: iOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `groupQuery` | [GroupQuery](#groupquery) | Information regarding which groups you want to get. |

  

Query and return a list of system groups.

Returns: `Promise<group[]>`

A promise that fulfills with array of groups that fit the query.

Example

```js
const groups = await Contacts.getGroupsAsync({ groupName: 'sailor moon' });
const allGroups = await Contacts.getGroupsAsync({});
```

### `Contacts.getPagedContactsAsync(contactQuery)`

Supported platforms: Android, iOS.

| Parameter | Type |
| --- | --- |
| `contactQuery`(optional) | [ContactQuery](#contactquery) |

  

Returns: `Promise<contactresponse>`

### `Contacts.getPermissionsAsync()`

Supported platforms: Android, iOS.

Checks user's permissions for accessing contacts data.

Returns: `Promise<contactspermissionresponse>`

A promise that resolves to a [ContactsPermissionResponse](#contactspermissionresponse) object.

### `Contacts.hasContactsAsync()`

Supported platforms: Android, iOS.

Checks if any contacts exist on the device without querying all contacts. This method requires contacts read permission.

Returns: `Promise<boolean>`

A promise that fulfills with a `boolean`, indicating whether there are any contacts on the device.

Example

```js
const hasContacts = await Contacts.hasContactsAsync();
if (hasContacts) {
  console.log('Contacts are available');
}
```

### `Contacts.isAvailableAsync()`

Supported platforms: Android, iOS.

Returns whether the Contacts API is enabled on the current device. This method does not check the app permissions.

Returns: `Promise<boolean>`

A promise that fulfills with a `boolean`, indicating whether the Contacts API is available on the current device. It always resolves to `false` on web.

### `Contacts.presentAccessPickerAsync()`

Supported platforms: iOS 18.0+.

Presents a modal which allows the user to select which contacts the app has access to. Using this function is reasonable only when the app has "limited" permissions.

Returns: `Promise<string[]>`

A promise that resolves with an array of contact identifiers that were newly granted to the app. Contacts which the app lost access to are not listed. On platforms other than iOS and below 18.0, the promise rejects immediately.

### `Contacts.presentContactPickerAsync()`

Supported platforms: Android, iOS.

Presents a native contact picker to select a single contact from the system. On Android, the `READ_CONTACTS` permission is required. You can obtain this permission by calling the [`Contacts.requestPermissionsAsync()`](#contactsrequestpermissionsasync) method. On iOS, no permissions are required to use this method.

Returns: `Promise<existingcontact>`

A promise that fulfills with a single `Contact` object if a contact is selected or `null` if no contact is selected (when selection is canceled).

### `Contacts.presentFormAsync(contactId, contact, formOptions)`

Supported platforms: Android, iOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `contactId`(optional) | `string | null` | The ID of a system contact. |
| `contact`(optional) | [Contact](#contact) | null | A contact with the changes you want to persist. |
| `formOptions`(optional) | [FormOptions](#formoptions) | Options for the native editor. Default: `{}` |

  

Present a native form for manipulating contacts.

Returns: `Promise<any>`

Example

```js
await Contacts.presentFormAsync('161A368D-D614-4A15-8DC6-665FDBCFAE55');
```

### `Contacts.removeContactAsync(contactId)`

Supported platforms: iOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `contactId` | `string` | ID of the contact you want to delete. |

  

Delete a contact from the system.

Returns: `Promise<any>`

Example

```js
await Contacts.removeContactAsync('161A368D-D614-4A15-8DC6-665FDBCFAE55');
```

### `Contacts.removeContactFromGroupAsync(contactId, groupId)`

Supported platforms: iOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `contactId` | `string` | ID of the contact you want to remove. |
| `groupId` | `string` | ID for the group you want to remove membership of. |

  

Remove a contact's membership from a given group. This will not delete the contact.

Returns: `Promise<any>`

Example

```js
await Contacts.removeContactFromGroupAsync(
  '665FDBCFAE55-D614-4A15-8DC6-161A368D',
  '161A368D-D614-4A15-8DC6-665FDBCFAE55'
);
```

### `Contacts.removeGroupAsync(groupId)`

Supported platforms: iOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `groupId` | `string` | ID of the group you want to remove. |

  

Delete a group from the device.

Returns: `Promise<any>`

Example

```js
await Contacts.removeGroupAsync('161A368D-D614-4A15-8DC6-665FDBCFAE55');
```

### `Contacts.requestPermissionsAsync()`

Supported platforms: Android, iOS.

Asks the user to grant permissions for accessing contacts data.

Returns: `Promise<contactspermissionresponse>`

A promise that resolves to a [ContactsPermissionResponse](#contactspermissionresponse) object.

### `Contacts.shareContactAsync(contactId, message, shareOptions)`

Supported platforms: Android, iOS.

| Parameter | Type |
| --- | --- |
| `contactId` | `string` |
| `message` | `string` |
| `shareOptions`(optional) | [ShareOptions](https://reactnative.dev/docs/share#share) |

  

Returns: `Promise<any>`

### `Contacts.updateContactAsync(contact)`

Supported platforms: Android, iOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `contact` | { id: string } & [Partial](https://www.typescriptlang.org/docs/handbook/utility-types.html#partialtype)<[ExistingContact](#existingcontact)\> | A contact object including the wanted changes. Contact `id` is required. |

  

Mutate the information of an existing contact. Due to an iOS bug, `nonGregorianBirthday` field cannot be modified.

Returns: `Promise<string>`

A promise that fulfills with ID of the updated system contact if mutation was successful.

Example

```js
const contact = {
  id: '161A368D-D614-4A15-8DC6-665FDBCFAE55',
  [Contacts.Fields.FirstName]: 'Drake',
  [Contacts.Fields.Company]: 'Young Money',
};
await Contacts.updateContactAsync(contact);
```

### `Contacts.updateGroupNameAsync(groupName, groupId)`

Supported platforms: iOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `groupName` | `string` | New name for an existing group. |
| `groupId` | `string` | ID of the group you want to edit. |

  

Change the name of an existing group.

Returns: `Promise<any>`

Example

```js
await Contacts.updateGroupName('Expo Friends', '161A368D-D614-4A15-8DC6-665FDBCFAE55');
```

### `Contacts.writeContactToFileAsync(contactQuery)`

Supported platforms: Android, iOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `contactQuery`(optional) | [ContactQuery](#contactquery) | Used to query contact you want to write. Default: `{}` |

  

Query a set of contacts and write them to a local URI that can be used for sharing.

Returns: `Promise<string>`

A promise that fulfills with shareable local URI, or `undefined` if there was no match.

Example

```js
const localUri = await Contacts.writeContactToFileAsync({
  id: '161A368D-D614-4A15-8DC6-665FDBCFAE55',
});
Share.share({ url: localUri, message: 'Call me!' });
```

## Event Subscriptions

### `Contacts.addContactsChangeListener(listener)`

Supported platforms: Android, iOS.

| Parameter | Type | Description |
| --- | --- | --- |
| `listener` | `() => void` | The function that will be executed when contacts change. This function accepts no arguments. |

  

Adds a listener for contact changes. The listener will be called whenever contacts are added, updated, or deleted.

**Platform differences:**

-   **Android**: 5-7 second delay - uses `ContentObserver` with inherent system delays
-   **iOS**: Immediate response - uses `CNContactStoreDidChangeNotification`

The Android delay is a system limitation that affects all apps using `ContentObserver` for contacts. This delay is by design to batch notifications for better performance and battery life. For more immediate updates, you can also listen to app state changes and refresh contacts when the app comes to the foreground. This ensures users see the latest contacts when returning from the native Contacts app.

Returns: `EventSubscription`

A subscription object with a `remove` method to stop listening.

Example

```jsx
const subscription = Contacts.addContactChangeListener(() => {
  console.log('Contacts changed - refreshing contact list');
  // Refresh your contact list when changes are detected
  loadContacts();
});

// Later, remove the listener
subscription.remove();
```

## Types

### `Address`

Supported platforms: Android, iOS.

| Property | Type | Description |
| --- | --- | --- |
| city(optional) | `string` | City name. |
| country(optional) | `string` | Country name |
| id(optional) | `string` | Unique ID. This value will be generated by the OS. |
| isoCountryCode(optional) | `string` | [Standard country code](https://www.iso.org/iso-3166-country-codes.html). |
| label | `string` | Localized display name. |
| neighborhood(optional) | `string` | Neighborhood name. |
| poBox(optional) | `string` | P.O. Box. |
| postalCode(optional) | `string` | Local post code. |
| region(optional) | `string` | Region or state name. |
| street(optional) | `string` | Street name. |

### `CalendarFormatType`

Supported platforms: Android, iOS.

Literal Type: `union`

Acceptable values are: [CalendarFormats](#calendarformats) | `{CalendarFormats}`

### `Contact`

Supported platforms: Android, iOS.

Base contact type without ID. For better type safety, consider using:

-   `Contact` when creating new contacts (no ID needed)
-   `ExistingContact` when working with contacts returned from the system (ID guaranteed)

| Property | Type | Description |
| --- | --- | --- |
| addresses(optional) | [Address[]](#address) | Locations. |
| birthday(optional) | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | Birthday information in Gregorian format. |
| company(optional) | `string` | Organization the entity belongs to. |
| contactType | [ContactType](#contacttype) | Denoting a person or company. |
| dates(optional) | [Date[]](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | A labeled list of other relevant user dates in Gregorian format. |
| department(optional) | `string` | Job department. |
| emails(optional) | [Email[]](#email) | Email addresses. |
| firstName(optional) | `string` | Given name. |
| image(optional) | [Image](#image) | Thumbnail image. On iOS it size is set to 320×320px, on Android it may vary. |
| imageAvailable(optional) | `boolean` | Used for efficient retrieval of images. |
| instantMessageAddresses(optional) | [InstantMessageAddress[]](#instantmessageaddress) | Instant messaging connections. |
| isFavorite(optional) | `boolean` | Supported platforms: Android. Whether the contact is starred. |
| jobTitle(optional) | `string` | Job description. |
| lastName(optional) | `string` | Last name. |
| maidenName(optional) | `string` | Maiden name. |
| middleName(optional) | `string` | Middle name |
| name | `string` | Full name with proper format. |
| namePrefix(optional) | `string` | Dr., Mr., Mrs., and so on. |
| nameSuffix(optional) | `string` | Jr., Sr., and so on. |
| nickname(optional) | `string` | An alias to the proper name. |
| nonGregorianBirthday(optional) | [Date](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Date) | Supported platforms: iOS. Birthday that doesn't conform to the Gregorian calendar format, interpreted based on the [calendar `format`](#date) setting. |
| note(optional) | `string` | Additional information. The note field requires your app to request additional entitlements. The Expo Go app does not contain those entitlements, so in order to test this feature you will need to request the entitlement from Apple, set the ios.accessesContactNotes field in app config to true, and create your development build. |
| phoneNumbers(optional) | [PhoneNumber[]](#phonenumber) | Phone numbers. |
| phoneticFirstName(optional) | `string` | Pronunciation of the first name. |
| phoneticLastName(optional) | `string` | Pronunciation of the last name. |
| phoneticMiddleName(optional) | `string` | Pronunciation of the middle name. |
| rawImage(optional) | [Image](#image) | Raw image without cropping, usually large. |
| relationships(optional) | [Relationship[]](#relationship) | Names of other relevant user connections. |
| socialProfiles(optional) | [SocialProfile[]](#socialprofile) | Supported platforms: iOS. Social networks. |
| urlAddresses(optional) | [UrlAddress[]](#urladdress) | Associated web URLs. |

### `ContactQuery`

Supported platforms: Android, iOS.

Used to query contacts from the user's device.

| Property | Type | Description |
| --- | --- | --- |
| containerId(optional) | `string` | Supported platforms: iOS. Get all contacts that belong to the container matching this ID. |
| fields(optional) | [FieldType[]](#fieldtype) | If specified, the defined fields will be returned. If skipped, all fields will be returned. |
| groupId(optional) | `string` | Supported platforms: iOS. Get all contacts that belong to the group matching this ID. |
| id(optional) | `string | string[]` | Get contacts with a matching ID or array of IDs. |
| name(optional) | `string` | Get all contacts whose name contains the provided string (not case-sensitive). |
| pageOffset(optional) | `number` | The number of contacts to skip before gathering contacts. |
| pageSize(optional) | `number` | The max number of contacts to return. If skipped or set to `0` all contacts will be returned. |
| rawContacts(optional) | `boolean` | Supported platforms: iOS. Prevent unification of contacts when gathering. Default: `false` |
| sort(optional) | [ContactSort](#contactsort) | Sort method used when gathering contacts. |

### `ContactResponse`

Supported platforms: Android, iOS.

The return value for queried contact operations like `getContactsAsync`.

| Property | Type | Description |
| --- | --- | --- |
| data | [ExistingContact[]](#existingcontact) | An array of contacts that match a particular query. |
| hasNextPage | `boolean` | This will be `true` if there are more contacts to retrieve beyond what is returned. |
| hasPreviousPage | `boolean` | This will be `true` if there are previous contacts that weren't retrieved due to `pageOffset` limit. |

### `ContactSort`

Supported platforms: Android, iOS.

String union of [SortTypes](#sorttypes) values.

### `ContactsPermissionResponse`

Supported platforms: Android, iOS.

Type: `PermissionResponse` extended by:

| Property | Type | Description |
| --- | --- | --- |
| accessPrivileges(optional) | `'all' | 'limited' | 'none'` | Indicates if your app has access to the whole or only part of the contact library. Possible values are:
-   `'all'` if the user granted your app access to the whole contact library
-   `'limited'` if the user granted your app access only to selected contacts (only available on iOS 18+)
-   `'none'`

 |

### `ContactType`

Supported platforms: Android, iOS.

Literal Type: `union`

Acceptable values are: [ContactTypes](#contacttypes) | `{ContactTypes}`

### `Container`

Supported platforms: Android, iOS.

| Property | Type | Description |
| --- | --- | --- |
| id | `string` | - |
| name | `string` | - |
| type | `ContainerType` | - |

### `ContainerQuery`

Supported platforms: iOS.

Used to query native contact containers.

| Property | Type | Description |
| --- | --- | --- |
| contactId(optional) | `string` | Query all the containers that parent a contact. |
| containerId(optional) | `string | string[]` | Query all the containers that matches ID or an array od IDs. |
| groupId(optional) | `string` | Query all the containers that parent a group. |

### `ContainerType`

Supported platforms: Android, iOS.

Literal Type: `union`

Acceptable values are: [ContainerTypes](#containertypes) | `{ContainerTypes}`

### `Date`

Supported platforms: Android, iOS.

| Property | Type | Description |
| --- | --- | --- |
| day | `number` | Day. |
| format(optional) | [CalendarFormatType](#calendarformattype) | Format for the date. This is provided by the OS, do not set this manually. |
| id(optional) | `string` | Unique ID. This value will be generated by the OS. |
| label(optional) | `string` | Localized display name. |
| month | `number` | Month - adjusted for JavaScript `Date` which starts at `0`. |
| year(optional) | `number` | Year. |

### `Email`

Supported platforms: Android, iOS.

| Property | Type | Description |
| --- | --- | --- |
| email(optional) | `string` | Email address. |
| id(optional) | `string` | Unique ID. This value will be generated by the OS. |
| isPrimary(optional) | `boolean` | Flag signifying if it is a primary email address. |
| label | `string` | Localized display name. |

### `ExistingContact`

Supported platforms: Android, iOS.

Type for existing contacts returned from the system - guarantees the id field is present.

Type: [Contact](#contact) extended by:

| Property | Type | Description |
| --- | --- | --- |
| id | `string` | Immutable identifier used for querying and indexing. This value will be generated by the OS when the contact is created. |

### `FieldType`

Supported platforms: Android, iOS.

Literal Type: `union`

Acceptable values are: [Fields](#fields) | `{Fields}`

### `FormOptions`

Supported platforms: iOS.

Denotes the functionality of a native contact form.

| Property | Type | Description |
| --- | --- | --- |
| allowsActions(optional) | `boolean` | Actions like share, add, create. |
| allowsEditing(optional) | `boolean` | Allows for contact mutation. |
| alternateName(optional) | `string` | Used if contact doesn't have a name defined. |
| cancelButtonTitle(optional) | `string` | The name of the left bar button. Only applies when editing an existing contact. |
| displayedPropertyKeys(optional) | [FieldType[]](#fieldtype) | The properties that will be displayed when viewing a contact. |
| groupId(optional) | `string` | The parent group for a new contact. |
| isNew(optional) | `boolean` | Present the new contact controller. If set to `false` the unknown controller will be shown. |
| message(optional) | `string` | The message displayed under the name of the contact. Only applies when editing an existing contact. |
| preventAnimation(optional) | `boolean` | Prevents the controller from animating in. |
| shouldShowLinkedContacts(optional) | `boolean` | Show or hide the similar contacts. |

### `Group`

Supported platforms: iOS.

A parent to contacts. A contact can belong to multiple groups. Here are some query operations you can perform:

-   Child Contacts: `getContactsAsync({ groupId })`
-   Groups From Container: `getGroupsAsync({ containerId })`
-   Groups Named: `getContainersAsync({ groupName })`

| Property | Type | Description |
| --- | --- | --- |
| id(optional) | `string` | The editable name of a group. |
| name(optional) | `string` | Immutable id representing the group. |

### `GroupQuery`

Supported platforms: iOS.

Used to query native contact groups.

| Property | Type | Description |
| --- | --- | --- |
| containerId(optional) | `string` | Query all groups that belong to a certain container. |
| groupId(optional) | `string` | Query the group with a matching ID. |
| groupName(optional) | `string` | Query all groups matching a name. |

### `Image`

Supported platforms: Android, iOS.

Information regarding thumbnail images.

> On Android you can get dimensions using [`Image.getSize`](https://reactnative.dev/docs/image#getsize) method.

| Property | Type | Description |
| --- | --- | --- |
| base64(optional) | `string` | Image as Base64 string. |
| height(optional) | `number` | Supported platforms: iOS. Image height |
| uri(optional) | `string` | A local image URI. Note: If you have a remote URI, download it first using FileSystem.downloadAsync. |
| width(optional) | `number` | Supported platforms: iOS. Image width. |

### `InstantMessageAddress`

Supported platforms: Android, iOS.

| Property | Type | Description |
| --- | --- | --- |
| id(optional) | `string` | Unique ID. This value will be generated by the OS. |
| label | `string` | Localized display name. |
| localizedService(optional) | `string` | Localized name of app. |
| service(optional) | `string` | Name of instant messaging app. |
| username(optional) | `string` | Username in IM app. |

### `PermissionExpiration`

Supported platforms: Android, iOS.

Literal Type: `union`

Permission expiration time. Currently, all permissions are granted permanently.

Acceptable values are: `'never'` | `number`

### `PermissionResponse`

Supported platforms: Android, iOS.

An object obtained by permissions get and request functions.

| Property | Type | Description |
| --- | --- | --- |
| canAskAgain | `boolean` | Indicates if user can be asked again for specific permission. If not, one should be directed to the Settings app in order to enable/disable the permission. |
| expires | `PermissionExpiration` | Determines time when the permission expires. |
| granted | `boolean` | A convenience boolean that indicates if the permission is granted. |
| status | `PermissionStatus` | Determines the status of the permission. |

### `PhoneNumber`

Supported platforms: Android, iOS.

| Property | Type | Description |
| --- | --- | --- |
| countryCode(optional) | `string` | Country code. . Example. `us` |
| digits(optional) | `string` | Phone number without format. . Example. `8674305` |
| id(optional) | `string` | Unique ID. This value will be generated by the OS. |
| isPrimary(optional) | `boolean` | Flag signifying if it is a primary phone number. |
| label | `string` | Localized display name. |
| number(optional) | `string` | Phone number. |

### `Relationship`

Supported platforms: Android, iOS.

| Property | Type | Description |
| --- | --- | --- |
| id(optional) | `string` | Unique ID. This value will be generated by the OS. |
| label | `string` | Localized display name. |
| name(optional) | `string` | Name of related contact. |

### `SocialProfile`

Supported platforms: iOS.

| Property | Type | Description |
| --- | --- | --- |
| id(optional) | `string` | Unique ID. This value will be generated by the OS. |
| label | `string` | Localized display name. |
| localizedProfile(optional) | `string` | Localized profile name. |
| service(optional) | `string` | Name of social app. |
| url(optional) | `string` | Web URL. |
| userId(optional) | `string` | Username ID in social app. |
| username(optional) | `string` | Username in social app. |

### `UrlAddress`

Supported platforms: Android, iOS.

| Property | Type | Description |
| --- | --- | --- |
| id(optional) | `string` | Unique ID. This value will be generated by the OS. |
| label | `string` | Localized display name. |
| url(optional) | `string` | Web URL. |

## Enums

### `CalendarFormats`

Supported platforms: Android, iOS.

This format denotes the common calendar format used to specify how a date is calculated in `nonGregorianBirthday` fields.

#### `Buddhist`

Supported platforms: iOS.

`CalendarFormats.Buddhist = "buddhist"`

#### `Chinese`

Supported platforms: iOS.

`CalendarFormats.Chinese = "chinese"`

#### `Coptic`

Supported platforms: iOS.

`CalendarFormats.Coptic = "coptic"`

#### `EthiopicAmeteAlem`

Supported platforms: iOS.

`CalendarFormats.EthiopicAmeteAlem = "ethiopicAmeteAlem"`

#### `EthiopicAmeteMihret`

Supported platforms: iOS.

`CalendarFormats.EthiopicAmeteMihret = "ethiopicAmeteMihret"`

#### `Gregorian`

`CalendarFormats.Gregorian = "gregorian"`

#### `Hebrew`

Supported platforms: iOS.

`CalendarFormats.Hebrew = "hebrew"`

#### `Indian`

Supported platforms: iOS.

`CalendarFormats.Indian = "indian"`

#### `Islamic`

Supported platforms: iOS.

`CalendarFormats.Islamic = "islamic"`

#### `IslamicCivil`

Supported platforms: iOS.

`CalendarFormats.IslamicCivil = "islamicCivil"`

#### `IslamicTabular`

Supported platforms: iOS.

`CalendarFormats.IslamicTabular = "islamicTabular"`

#### `IslamicUmmAlQura`

Supported platforms: iOS.

`CalendarFormats.IslamicUmmAlQura = "islamicUmmAlQura"`

#### `ISO8601`

Supported platforms: iOS.

`CalendarFormats.ISO8601 = "iso8601"`

#### `Japanese`

Supported platforms: iOS.

`CalendarFormats.Japanese = "japanese"`

#### `Persian`

Supported platforms: iOS.

`CalendarFormats.Persian = "persian"`

#### `RepublicOfChina`

Supported platforms: iOS.

`CalendarFormats.RepublicOfChina = "republicOfChina"`

### `ContactTypes`

Supported platforms: Android, iOS.

#### `Company`

`ContactTypes.Company = "company"`

Contact is group or company.

#### `Person`

`ContactTypes.Person = "person"`

Contact is a human.

### `ContainerTypes`

Supported platforms: iOS.

#### `CardDAV`

`ContainerTypes.CardDAV = "cardDAV"`

With cardDAV protocol used for sharing.

#### `Exchange`

`ContainerTypes.Exchange = "exchange"`

In association with email server.

#### `Local`

`ContainerTypes.Local = "local"`

A local non-iCloud container.

#### `Unassigned`

`ContainerTypes.Unassigned = "unassigned"`

Unknown container.

### `Fields`

Supported platforms: Android, iOS.

Possible fields to retrieve for a contact.

#### `Addresses`

`Fields.Addresses = "addresses"`

#### `Birthday`

`Fields.Birthday = "birthday"`

#### `Company`

`Fields.Company = "company"`

#### `ContactType`

`Fields.ContactType = "contactType"`

#### `Dates`

`Fields.Dates = "dates"`

#### `Department`

`Fields.Department = "department"`

#### `Emails`

`Fields.Emails = "emails"`

#### `ExtraNames`

`Fields.ExtraNames = "extraNames"`

#### `FirstName`

`Fields.FirstName = "firstName"`

#### `ID`

`Fields.ID = "id"`

#### `Image`

`Fields.Image = "image"`

#### `ImageAvailable`

`Fields.ImageAvailable = "imageAvailable"`

#### `InstantMessageAddresses`

`Fields.InstantMessageAddresses = "instantMessageAddresses"`

#### `IsFavorite`

Supported platforms: Android.

`Fields.IsFavorite = "isFavorite"`

#### `JobTitle`

`Fields.JobTitle = "jobTitle"`

#### `LastName`

`Fields.LastName = "lastName"`

#### `MaidenName`

`Fields.MaidenName = "maidenName"`

#### `MiddleName`

`Fields.MiddleName = "middleName"`

#### `Name`

`Fields.Name = "name"`

#### `NamePrefix`

`Fields.NamePrefix = "namePrefix"`

#### `NameSuffix`

`Fields.NameSuffix = "nameSuffix"`

#### `Nickname`

`Fields.Nickname = "nickname"`

#### `NonGregorianBirthday`

Supported platforms: iOS.

`Fields.NonGregorianBirthday = "nonGregorianBirthday"`

#### `Note`

`Fields.Note = "note"`

#### `PhoneNumbers`

`Fields.PhoneNumbers = "phoneNumbers"`

#### `PhoneticFirstName`

`Fields.PhoneticFirstName = "phoneticFirstName"`

#### `PhoneticLastName`

`Fields.PhoneticLastName = "phoneticLastName"`

#### `PhoneticMiddleName`

`Fields.PhoneticMiddleName = "phoneticMiddleName"`

#### `RawImage`

`Fields.RawImage = "rawImage"`

#### `Relationships`

`Fields.Relationships = "relationships"`

#### `SocialProfiles`

Supported platforms: iOS.

`Fields.SocialProfiles = "socialProfiles"`

#### `UrlAddresses`

`Fields.UrlAddresses = "urlAddresses"`

### `PermissionStatus`

Supported platforms: Android, iOS.

#### `DENIED`

`PermissionStatus.DENIED = "denied"`

User has denied the permission.

#### `GRANTED`

`PermissionStatus.GRANTED = "granted"`

User has granted the permission.

#### `UNDETERMINED`

`PermissionStatus.UNDETERMINED = "undetermined"`

User hasn't granted or denied the permission yet.

### `SortTypes`

Supported platforms: Android, iOS.

#### `FirstName`

`SortTypes.FirstName = "firstName"`

Sort by first name in ascending order.

#### `LastName`

`SortTypes.LastName = "lastName"`

Sort by last name in ascending order.

#### `None`

`SortTypes.None = "none"`

No sorting should be applied.

#### `UserDefault`

Supported platforms: Android.

`SortTypes.UserDefault = "userDefault"`

The user default method of sorting.

## Permissions

### Android

This library automatically adds `READ_CONTACTS` and `WRITE_CONTACTS` permissions to your app:

| Android Permission | Description |
| --- | --- |
| `READ_CONTACTS` | Allows an application to read the user's contacts data. |
| `WRITE_CONTACTS` | Allows an application to write the user's contacts data. |

### iOS

The following usage description keys are used by this library:

| Info.plist Key | Description |
| --- | --- |
| `NSContactsUsageDescription` | A message that tells the user why the app is requesting access to the user’s contacts. |
