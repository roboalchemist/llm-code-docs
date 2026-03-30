# Source: https://docs.luciq.ai/references/report-data/attachments/add-extra-attachment.md

# Add Extra Attachment

It's possible to manually add an extra attachment to the report by passing a file URL to this method.

{% tabs fullWidth="true" %}
{% tab title="iOS - Swift" %}

```swift
let url = URL(fileURLWithPath: "filePath")
Luciq.addFileAttachmentWithURL(filePath, fileName)
//OR
Luciq.addFileAttachment(with: data, andName: "attachment_1.log")
//Name field is optional
```

{% endtab %}

{% tab title="iOS - ObjC" %}

```objectivec
NSURL *url = [NSURL fileURLWithPath:@"filePath"];
[Luciq addFileAttachmentWithURL:url];
//OR
NSData *data = [[NSData alloc] init];
[Luciq addFileAttachmentWithData:data andName:@"attachment_1.log"];
//Name field is optional
```

{% endtab %}

{% tab title="And - Java" %}

```java
Luciq.addFileAttachment(Uri.fromFile(file), "file_name.txt");
```

{% endtab %}

{% tab title="And - Kotlin" %}

```kotlin
Luciq.addFileAttachment(Uri.fromFile(file), "file_name.txt")
```

{% endtab %}

{% tab title="RN" %}

```javascript
//iOS
Luciq.addFileAttachment(filePath)

//Android
Luciq.addFileAttachment(filePath, fileName)
```

{% endtab %}

{% tab title="Flutter" %}

```dart
Luciq.addFileAttachment(filePath, fileName)
```

{% endtab %}
{% endtabs %}
