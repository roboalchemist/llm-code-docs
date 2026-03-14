# Source: https://docs.airbyte.com/platform/using-airbyte/tagging.md

# Source: https://docs.airbyte.com/platform/2.0/using-airbyte/tagging.md

# Source: https://docs.airbyte.com/platform/1.8/using-airbyte/tagging.md

# Source: https://docs.airbyte.com/platform/1.7/using-airbyte/tagging.md

# Source: https://docs.airbyte.com/platform/1.6/using-airbyte/tagging.md

# Tagging Connections

Copy Page

CoreStandardPlusProEnterprise FlexSelf-Managed Enterprise[ Compare](https://airbyte.com/product/features)

As time goes on, the number of connections in your workspace tends to increase. Use tags to organize connections based on any set of criteria you like, then filter your connections based on the tags you want to see.

![A workspace with tagged connections](/assets/images/tagging-f9e07936efa28a8366b3a183bcbe96d2.png)

## Strategies for managing tags[​](#strategies-for-managing-tags "Direct link to Strategies for managing tags")

Tags are flexible, so make sure you create a system that works for you. Here are a few classification schemes to get you started.

* **Data owner**: Which department or team owns the source data?

* **Engineering owner**: Who is responsible for keeping this connection running smoothly?

* **Criticality**: Is a connection powering critical business systems? Are there SLAs you need to meet?

* **Purpose**: What functions is the data powering, and who is using this data?

* **Readiness**: Is the connection in testing, or is it production-ready?

* **Origin**: Is this connection managed by the Airbyte UI, Python, Terraform, or something else?

Regardless of your tag choices, it's always good practice to observe these guidelines.

* Use a standardized set of tags that everyone understands

* Use clear, descriptive tags that accurately represent your connections

* Stick to a manageable number of tags

* Review and update tags to ensure they stay relevant

* Combine similar tags, like 'Prod' and 'Production'

* Customize colors to visually represent a tag's importance

## Create a new tag[​](#create-a-new-tag "Direct link to Create a new tag")

Create a new tag and add it to one of your connections.

1. Open Airbyte and click **Connections**.

2. In the **Tags** column, find the connection you want to tag and hover on it.

3. If the connection has no tags, click **Add a tag** . If the connection already has tags, click **Edit tags** .

4. Type a name for your tag and click **Create `tag name`**.

Airbyte creates the tag and applies it to that connection. Tag colors are defined automatically, but you can [change them](#change-tag-properties).

## Add or remove a tag on a connection[​](#add-or-remove-a-tag-on-a-connection "Direct link to Add or remove a tag on a connection")

Modify a connection to add or remove a tag that already exists.

1. Open Airbyte and click **Connections**.

2. In the **Tags** column, find the connection you want to tag and hover on it.

3. Click **Edit tags** .

4. Click on tags to add and remove them for that connection.

Airbyte applies and removes tags and you select and deselect them.

## Change a tag's name and color[​](#change-tag-properties "Direct link to Change a tag's name and color")

Rename and recolor a tag.

1. Open Airbyte and click **Settings** > **General**.

2. Under **Workspace Tags**, click the pencil icon .

3. Rename the tag and update the color as you prefer. The color must be a valid hexadecimal code. Click the color sample and use the color picker to generate this for you.

4. Click **Save changes**.

Airbyte updates your tag. Next time you view the Connections page, your tags will reflect these changes.

## Delete a tag[​](#delete-a-tag "Direct link to Delete a tag")

Delete a tag from Airbyte and remove it from any connections that use it.

1. Open Airbyte and click **Settings** > **General**.

2. Under **Workspace Tags**, click the trash icon .

3. Click **Delete**.

Airbyte deletes the tag and removes it from any connections that use it.

## Limitations[​](#limitations "Direct link to Limitations")

Tags have the following maximums.

* 30 characters per tag name

* 10 tags per connection

* 100 tags per workspace
