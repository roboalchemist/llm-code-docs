# Source: https://firebase.google.com/docs/reference/js/auth.reactnativeasyncstorage.md.txt

# ReactNativeAsyncStorage interface

Interface for a supplied `AsyncStorage`.

**Signature:**  

    export interface ReactNativeAsyncStorage 

## Methods

|                                                               Method                                                                |          Description           |
|-------------------------------------------------------------------------------------------------------------------------------------|--------------------------------|
| [getItem(key)](https://firebase.google.com/docs/reference/js/auth.reactnativeasyncstorage.md#reactnativeasyncstoragegetitem)        | Retrieve an item from storage. |
| [removeItem(key)](https://firebase.google.com/docs/reference/js/auth.reactnativeasyncstorage.md#reactnativeasyncstorageremoveitem)  | Remove an item from storage.   |
| [setItem(key, value)](https://firebase.google.com/docs/reference/js/auth.reactnativeasyncstorage.md#reactnativeasyncstoragesetitem) | Persist an item in storage.    |

## ReactNativeAsyncStorage.getItem()

Retrieve an item from storage.

**Signature:**  

    getItem(key: string): Promise<string | null>;

#### Parameters

| Parameter |  Type  | Description  |
|-----------|--------|--------------|
| key       | string | storage key. |

**Returns:**

Promise\<string \| null\>

## ReactNativeAsyncStorage.removeItem()

Remove an item from storage.

**Signature:**  

    removeItem(key: string): Promise<void>;

#### Parameters

| Parameter |  Type  | Description  |
|-----------|--------|--------------|
| key       | string | storage key. |

**Returns:**

Promise\<void\>

## ReactNativeAsyncStorage.setItem()

Persist an item in storage.

**Signature:**  

    setItem(key: string, value: string): Promise<void>;

#### Parameters

| Parameter |  Type  |  Description   |
|-----------|--------|----------------|
| key       | string | storage key.   |
| value     | string | storage value. |

**Returns:**

Promise\<void\>