# Source: https://docs.deepconverse.com/product-docs/conversational-flow-builder/assign-parameters-in-conversations/predefined-parameters.md

# Predefined Parameters

The system will prepopulate common parameters to help make decisions in the flows. Below is a list of the predefined parameters.

<table><thead><tr><th>Parameter Name</th><th></th></tr></thead><tbody><tr><td><pre><code>__sys_userIp
</code></pre></td><td>IP Address of the customer</td></tr><tr><td><pre><code>__sys_userAgent
</code></pre></td><td>User agent of the browser </td></tr><tr><td><pre><code>__sys_userAgentParsed
</code></pre></td><td>Parsed representation of the user agent <br><br>Example:<br><code>{"device": {"brand": "Apple", "family": "Mac", "model": "Mac"}, "os": {"family": "Mac OS X", "major": "10", "minor": "9", "patch": "4", "patch_minor": null}, "string": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2272.104 Safari/537.36", "user_agent": {"family": "Chrome", "major": "41", "minor": "0", "patch": "2272"}}</code></td></tr><tr><td><pre><code>__sys_userCountry
</code></pre></td><td>Country identified by Cloudflare<br><a href="https://developers.cloudflare.com/support/network/configuring-ip-geolocation/">https://developers.cloudflare.com/support/network/configuring-ip-geolocation/</a></td></tr><tr><td><pre><code>__sys_conversationId
</code></pre></td><td>Conversation Id </td></tr><tr><td><pre><code>__sys_userAction
</code></pre></td><td><p>Last Action taken by the customer</p><pre><code>{"type": "action_userInput", "text": button_text}
</code></pre><pre><code>{"type": "action_userQuickReply", "text": "Order Return"}
</code></pre></td></tr><tr><td><pre><code>__sys_channel
</code></pre></td><td>Channel being used for the conversation</td></tr><tr><td><pre><code>__sys_activeIntent
</code></pre></td><td>Currently active intent</td></tr><tr><td><pre><code>browser_path
</code></pre></td><td>URL Path the chatbot was loaded on</td></tr><tr><td><pre><code>browser_hostname
</code></pre></td><td>Browser hostname </td></tr><tr><td><pre><code>browser_referrer
</code></pre></td><td>Referrer of the webpage where bot was loaded</td></tr><tr><td><pre><code>browser_isMobile
</code></pre></td><td>If the user is on a mobile device</td></tr></tbody></table>
