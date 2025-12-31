# Source: https://docs.avaamo.com/user-guide/how-to/build-agents/configure-agents/deploy/web-channel/web-channel-callback-functions.md

# Web channel callback functions

You can also perform certain customization such as open and close the agent, send messages to the agent deployed in the web channel using JS. The agents deployed on web channels have web pages with **callback functions** embedded. These callback functions help to customize the user interaction with the agent. The Avaamo platform supports the following available callback functions&#x20;

* Avaamo.onBotMessage
* Avaamo.hideEditor()
* Avaamo.showEditor()
* Avaamo.onFirstUserMessage
* Avaamo.onFirstBotMessage
* Avaamo.onChannelLoaded
* Avaamo.onChatIframeLoad
* Avaamo.onChatBoxOpen
* Avaamo.onChatBoxClose
* Avaamo.logout()
* Avaamo.openChatBox()
* Avaamo.closeChatBox()
* Avaamo.toggleChatBox()

### **Open and Close**

You can open and close the agent programmatically with the following code:

```javascript

window.Avaamo.openChatBox();


window.Avaamo.closeChatBox();


window.Avaamo.toggleChatBox();
```

Consider that you wish to keep the agent in the open state when the agent is loaded. You can pass the **openChatbox** in the **chatBox.load** function. You can view the sample code when you click **Test** in the web channel.&#x20;

The following is a sample code to keep the agent in the open state when the agent is loaded:

```javascript
var AvaamoChatBot=function(t){function o(t,o){var n=document.createElement("script");n.setAttribute("src",t),n.setAttribute("id","optimaxscript"),n.onload=o,document.body.appendChild(n)}return this.options=t||{},this.load=function(t){o(this.options.url,function(){window.Avaamo.addFrame(),t&&"function"==typeof(t)&&t(window.Avaamo)})},this};
var chatBox = new AvaamoChatBot({url: 'https://cx.avaamo.com/web_channels/93b4ffd1-5aca-44a6-bfe1-9e7dd5b254cc?action=demo&banner=true&banner_text=+&banner_title=This+is+how+chat+bot+shows+up&controller=web_channels&demo=true&theme=avm-blue'});
  
/**This is the  function which will keep on open state when the agent loads.**/             
chatBox.load(function(avaamo) {window.Avaamo.openChatBox();});
```

### **Send message**

To send a message programmatically to the agent on behalf of the user.&#x20;

```
window.Avaamo.sendMessage("hello");
```

This function also accepts an optional second parameter that can be used to send a more meaningful message to the agent. If the second param is passed, the first param is used as a display message to the user in the chat window and the second param is used by the agent as the actual message:

```
window.Avaamo.sendMessage("Savings account", "I want to open a savings account");
```

### **Avaamo.onBotMessage**

This function once configured is executed for every response received from the agent:

```javascript
<!DOCTYPE html>
  <html>
  <head>
    <title>Web Channel</title>
    <meta name="viewport" content="width=device-width, initial-scale=1, maximum-scale=1, user-scalable=0">
  </head>
  <body>
  <script type="text/javascript">
    var AvaamoChatBot=function(t){function o(t,o){var n=document.createElement("script");n.setAttribute("src",t),n.onload=o,document.body.appendChild(n)}return this.options=t||{},this.load=function(t){o(this.options.url,function(){window.Avaamo.addFrame(),t&&"function"==typeof(t)&&t(window.Avaamo)})},this};
    var chatBox = new AvaamoChatBot({url: 'https://cx.avaamo.com/web_channels/52cf2ff5-f41e-4d48-aa05-8b2d6354b6fd?banner=true&banner_text=+&banner_title=This+is+how+chat+bot+shows+up&demo=true&theme=avm-blue&debug=true'});
    chatBox.load(function(avaamo) {
      avaamo.onBotMessage = (message) => {
        console.log('Response message from agent');
      } ;
    } );
   </script>
  </body>
</html>
```

### **Avaamo.hideEditor() / Avaamo.showEditor()**

You can hide the text input box on the agent. This is useful in scenarios where the user has other input options like a select list, a dropdown list, date selection, number box, etc.

**To hide or show the text box**:

1. Right-click on the agent, click on “inspect” and then click on the console.
2. Enter <\<Avaamo.hideEditor()>> and the text box is hidden.
3. Enter <\<Avaamo.showEditor()>> to display the text box again.

If you have persistent menu, then use **Avaamo.hideEditor({hideMenu: true});** to hide persistent menu and **Avaamo.showEditor({showMenu: true});** to show the persistent menu.&#x20;

Consider that you wish to display a form when the agent is loaded and wish to proceed further only when the user submits the form. You can view the sample code when you click "**Test"** in the web channel. The following is a sample code to hide the text editor when the form card displays and show for other messages:

```javascript
var AvaamoChatBot=function(t){function o(t,o){var n=document.createElement("script");n.setAttribute("src",t),n.onload=o,document.body.appendChild(n)}return this.options=t||{},this.load=function(t){o(this.options.url,function(){window.Avaamo.addFrame(),t&&"function"==typeof(t)&&t(window.Avaamo)})},this};
var chatBox = new AvaamoChatBot({url: ''});
//Text box hide/unhide feature
chatBox.load(function(avaamo) {
Avaamo.onChatIframeLoad=()=>{
 Avaamo.hideEditor({hideMenu: true});
};
avaamo.onBotMessage = (message) => {
//console.log("This is console ",message);

      Avaamo.hideEditor({hideMenu: true});
      /** You need to identify the Form card then add the condition. 
      Below is for all the default card types the text input will be hidden**/
       if(message.content_type === 'default_card') {
         //Avaamo.hideEditor();
         Avaamo.hideEditor({hideMenu: true});
       } else {
         //Avaamo.showEditor();
         Avaamo.showEditor({showMenu : true});
       }
};
};
```

### **Avaamo.onFirstUserMessage**&#x20;

This function once configured is executed every time an end-user sends the first message to initiate the agent conversation.

### **Avaamo.onFirstBotMessage**&#x20;

This function once configured is executed every time the agent displays the greeting message.

### **Avaamo.onChannelLoaded**&#x20;

This function once configured on the client-side where the agent is embedded in the HTML page is executed every time the agent is displayed. This is applicable only for web channels.

### **Avaamo.onChatIframeLoad**&#x20;

This function once configured is executed every time the agent chat window frame loads.

### **Avaamo.onChatBoxOpen**&#x20;

This function once configured is executed every time the agent chat window loads.

### **Avaamo.onChatBoxClose**&#x20;

This function once configured is executed every time the agent chat window closes.

### **Avaamo.logout()**&#x20;

This function can be used in the agent for the user to log out of an active agent session. The user is logged out of the agent but not the deployed channel. All the conversation with the agent is lost and the users must start a new session to interact with the agent.
