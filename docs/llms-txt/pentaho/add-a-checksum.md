# Source: https://docs.pentaho.com/pdia-data-integration/pdi-transformation-steps-reference-overview/add-a-checksum.md

# Source: https://docs.pentaho.com/pdia-data-integration/9.3-data-integration/pdi-transformation-steps-reference-overview/add-a-checksum.md

# Source: https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/add-a-checksum.md

# Add a Checksum

This step calculates checksums for one or more fields in the input stream and adds the checksum to the output as a new field.

![Add a Checksum step dialog](https://2745965000-files.gitbook.io/~/files/v0/b/gitbook-x-prod.appspot.com/o/spaces%2FvZoINBz5C5WnDZQlbOJQ%2Fuploads%2Fgit-blob-7be6283249aadff6e9f20d93e09ef7697a2f15fb%2FPDI_TransStep_AddChecksum_Dialog.png?alt=media)

### Options

#### Step name

Specify the unique name of the Add a Checksum step on the canvas. You can customize the name or leave it as the default.

#### Type

Specify the checksum type to calculate:

* CRC32 — [32-bit cyclic redundancy check](https://en.wikipedia.org/wiki/Cyclic_redundancy_check)
* ADLER 32 — [Adler-32 checksum algorithm](https://en.wikipedia.org/wiki/Adler-32)
* MD5 — [Message Digest Algorithm 5](https://en.wikipedia.org/wiki/MD5)
* SHA-1 — [Secure Hash Algorithm 1](https://en.wikipedia.org/wiki/SHA-1)
* SHA-256 — [Secure Hash Algorithm 2](https://en.wikipedia.org/wiki/SHA-256)

#### Result type

If you select **MD5**, **SHA-1**, or **SHA-256** for **Type**, you can select one of these result types:

* **String**
* **Hexadecimal**
* **Binary**

#### Result field

Specify the name of the field that contains the checksum.

#### Compatibility Mode

Select this option to provide backward compatibility with transformations created before PDI version 4.2.0 and its hexadecimal encoding issue.

#### Old Checksum Behaviour Mode

If selected, incoming fields are treated as strings.

{% hint style="info" %}
A binary field type produces the string representation of a byte array.
{% endhint %}

If cleared, all incoming fields are treated as byte arrays.

#### Field

In the table, specify which fields to include in the checksum calculation.

#### Get Fields

Select **Get Fields** to populate the fields table with fields derived from the input.

### Example

Your Pentaho distribution includes a CRC32 sample transformation at:

```
design-tools/data-integration/samples/transformations/Add a checksum - Basic CRC32 example.ktr
```

### Metadata injection support

All fields in this step support metadata injection. You can use this step with [ETL metadata injection](https://docs.pentaho.com/pdia-data-integration/10.2-data-integration/pdi-transformation-steps-reference-overview/etl-metadata-injection) to pass metadata to your transformation at runtime.
