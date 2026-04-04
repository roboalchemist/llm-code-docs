# Source: https://docs.airbyte.com/platform/using-airbyte/mappings.md

# Source: https://docs.airbyte.com/platform/2.0/using-airbyte/mappings.md

# Source: https://docs.airbyte.com/platform/1.8/using-airbyte/mappings.md

# Source: https://docs.airbyte.com/platform/1.7/using-airbyte/mappings.md

# Source: https://docs.airbyte.com/platform/1.6/using-airbyte/mappings.md

# Mappings

Copy Page

CoreStandardPlusProEnterprise FlexSelf-Managed Enterprise[ Compare](https://airbyte.com/product/features)

Use mappings to hash, encrypt, and rename fields, and filter rows. You set up mappings on each stream, ensuring your source data arrives in your destination exactly as you want it.

![Screenshot of mappings feature showing several streams with mappings applied](/assets/images/mappings-ebd0c364a50935d5612a7a0f56a177b9.png)

## More about mapping in Airbyte[​](#more-about-mapping-in-airbyte "Direct link to More about mapping in Airbyte")

It’s often the case that you want to move data from a source to a destination in a non-literal way, obscuring sensitive information and improving the consistency and usability of that data in its destination. Mapping allows you to match a field from your source to your destination and sync data in a way that is still accurate, but also more meaningful and appropriate for your needs.

Several types of mapping are possible in Airbyte, and you can combine them together in meaningful ways.

### Hash[​](#hash "Direct link to Hash")

Hashing is an **irreversible** process that protects sensitive data by obscuring it. Airbyte supports MD5, SHA-256, and SHA-512 hashing methods. Support for MD2, SHA-1, and SHA-384 is only available [through the API](https://reference.airbyte.com).

![](/assets/images/mapping-hash-71d6697683c8fcc631ef8195c5db40a3.png)

There are many reasons you might want to hash data.

* **Data security**: Source datasets can contain data like passwords or credit card information. It's more secure to store a hashed version of this data.
* **Anonymity and compliance**: Source datasets can contain personally identifiable information (PII). Anonymizing PII can help you meet data privacy regulations like GDPR and HIPAA.

### Encrypt[​](#encrypt "Direct link to Encrypt")

Encryption is a **reversible** process that protects sensitive data by obscuring it. Airbyte supports RSA encryption using an encryption key you generate yourself.

![](/assets/images/mapping-encrypt-32b1c72f35a02051ee5758e6bb5cb66d.png)

There are many reasons you might want to encrypt data.

* **Data security**: Source datasets can contain data like passwords or credit card information. It's more secure to store an encrypted version of this data.
* **Anonymity and compliance**: Source datasets can contain personally identifiable information (PII). Anonymizing PII can help you meet data privacy regulations like GDPR and HIPAA.

Airbyte expects RSA keys in hex-encoded DER format. PEM isn't currently supported.

This example generates the required key format.

```
openssl genpkey -algorithm RSA -out private_key.pem -pkeyopt rsa_keygen_bits:2048
openssl rsa -pubout -outform DER -in private_key.pem -out public_key.der
xxd -p public_key.der | tr -d '\n'
```

This is an example of the public key format Airbyte expects, but make sure you generate your own.

```
30820122300d06092a864886f70d01010105000382010f003082010a0282010100ce01c1000b6712bd5f694402c82ffb7b60867130b6e3284eac39577ff0f9b12a69920af4e53f4d83843ce86ba4975bb0298e6cf0ffbb8696540426bbf2146075ac6779801cf3dac54aa21ec69b14ab78217b5be70d083d075f06443a6f84ed6a61c924a4467b76eb35b41cf0d9e88be8c98734aec87ba7e9a6e8b9bec45627edbba2ea285f4907811ff94a01b6b1a90d88d303fbb60f62c094a65f5739fc6e46e06924040cd54c2a990483aa25eb4a7a35c0b77ef42f0c06fe1b00a8ca038939d22cc136de862a3bb5ba4a14f211e31d1380cf26fa3d6b268f6a4be47e3926a5d83ca20ae0108379b0d940c0e8a5a9cf7d24a6222305520ce6b507e3f7515e2d0203010001
```

### Rename field[​](#rename-field "Direct link to Rename field")

Renaming fields helps you ensure clarity, consistency, and compatibility in your destination data.

![](/assets/images/mapping-rename-6b3368fadc62531f0009e675866330fd.png)

There are many reasons you might want to rename fields.

* **Schema alignment**: Sources and destinations can use different naming conventions, or your destination can have more stringent naming requirements.
* **Readability and understanding**: Sources won't always have descriptive field names and the purpose of a field can be lost out of context. In an HRIS system, you might guess that `emp_num` is an employee number, but that might be less obvious years later in a data warehouse. Meaningful, descriptive names help teams understand and manage their data more efficiently.
* **Avoid naming conflicts**: Prevent multiple fields from having unnecessarily similar or identical names, and avoid the use of reserved keywords as field names.

### Filter rows[​](#filter-rows "Direct link to Filter rows")

Filtering rows is how you ensure you only sync relevant, high-quality, and meaningful data to your destination.

![](/assets/images/mapping-filter-25518bec5d159493611b12244f7b1ddb.png)

There are many reasons you might want to filter rows.

* **Remove irrelevant or corrupted data**: Data sources can contain test data, incomplete transactions, null values, and other things you don't want to preserve.
* **Optimization**: Smaller datasets require less processing and storage, and you can query them faster.
* **Compliance**: You don't want to keep data longer than is needed for a defined business purpose, and you want to ensure you don't accidentally archive data from individuals who opted out of data collection.

note

You can only filter fields whose type is string and number.

## Considerations and limitations[​](#considerations-and-limitations "Direct link to Considerations and limitations")

Before you begin mapping fields, consider the following.

* Don't map a cursor or primary key field if the [sync mode](/platform/1.6/using-airbyte/core-concepts/sync-modes/.md) depends on it. Doing this disrupts Airbyte's ability to use them for incremental syncing and deduplication.

* If you set up mapping on an existing connection, Airbyte prompts you to refresh affected streams. If a given destination does not support refreshes, Airbyte prompts you to clear it, instead. You almost certainly should do this. Not doing this could result in undesirable or unexpected behavior. For example, if you set up hashing on a field that contains PII, you want all data in that column to be hashed, not just new data. In a case like this, it's critical that you [clear historical data](/platform/1.6/operator-guides/clear.md) before syncing again.

  note

  If you're dealing with an extremely large database, a complete resync might take a significant amount of time.

## Create a new mapping[​](#create-a-new-mapping "Direct link to Create a new mapping")

Follow these steps to create a new mapping. Once you add a mapping to a stream, you cannot disable that stream until you [delete that stream's mappings](#delete).

1. Click **Connections** in the sidebar.
2. Click the connection on which you want to set up mappings.
3. Click **Mappings**.
4. Click **Select stream** or **Add stream**.
5. Select the stream on which you want to set up mappings.
6. Define your mappings for that stream.
7. When you're done, click **Submit**. Airbyte may prompt you to refresh or clear your destination to avoid unexpected behavior. The mapping is applied next time you sync data.

## Modify a mapping[​](#modify-a-mapping "Direct link to Modify a mapping")

Follow these steps to change an existing mapping.

1. Click **Connections** in the sidebar.
2. Click the connection on which you want to set up mappings.
3. Click **Mappings**.
4. Find the mappings you want to modify, and adjust them.
5. When you're done, click **Submit**. Airbyte may prompt you to refresh or clear your destination to avoid unexpected behavior. The mapping is applied next time you sync data.

## Delete a mapping[​](#delete "Direct link to Delete a mapping")

Follow these steps to create a new mapping.

1. Click **Connections** in the sidebar.
2. Click the connection on which you want to set up mappings.
3. Click **Mappings**.
4. Click the trash can icon next to the mapping you want to remove.
