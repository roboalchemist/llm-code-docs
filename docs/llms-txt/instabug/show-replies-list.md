# Source: https://docs.instabug.com/references/in-app-replies/show-replies-list.md

# Source: https://docs.instabug.com/kmp/setup-luciq-for-kmp/setup-in-app-replies/show-replies-list.md

# Source: https://docs.instabug.com/flutter/setup-luciq-for-flutter/setup-in-app-replies/show-replies-list.md

# Source: https://docs.instabug.com/react-native/setup-luciq-for-react-native/in-app-replies/show-replies-list.md

# Show Replies List

### Show Replies

The below API can be used to display the replies page. This page contains a list of any previous chats that were opened for this customer.

JavaScript

{% code title="Example" %}

```javascript
Replies.show();
```

{% endcode %}

![Conversations List](https://content.gitbook.com/content/6lIBifTCHAMDxXnztiBK/blobs/zU3ub5fS0qa0DKwy2L4k/c315f5857fcc9b6731ddcdf86c2f6a3f578dcbe38f47a311387e1b6333c94768%20react%20native%20show%20replies%20list%201.png)

### Check if User Has Chats

If a user has no pre-existing chats, the previous API won't show the replies page. You can check whether the user has any available chats or not using the below API.

{% code title="JavaScript" %}

```javascript
const hasChats = await Replies.hasChats();
```

{% endcode %}
