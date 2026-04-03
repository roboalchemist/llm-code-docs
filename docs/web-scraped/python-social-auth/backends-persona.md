# Backends/Persona

Source: https://python-social-auth.readthedocs.io/en/latest/backends/persona.html

Mozilla Persona
¶

Support for 
Mozilla Persona
 is possible by posting the 

assertion

 code to

/complete/persona/

 URL.

The setup doesn’t need any setting, just the usual 
Mozilla Persona

javascript include in your document and the needed mechanism to trigger the
POST to 
python-social-auth
:

&lt;!-- Include BrowserID JavaScript --&gt;
&lt;script src=&quot;https://login.persona.org/include.js&quot; type=&quot;text/javascript&quot;&gt;&lt;/script&gt;

&lt;!-- Define a form to send the POST data --&gt;
&lt;form method=&quot;post&quot; action=&quot;/complete/persona/&quot;&gt;
    &lt;input type=&quot;hidden&quot; name=&quot;assertion&quot; value=&quot;&quot; /&gt;
    &lt;a rel=&quot;nofollow&quot; id=&quot;persona&quot; href=&quot;#&quot;&gt;Mozilla Persona&lt;/a&gt;
&lt;/form&gt;

&lt;!-- Setup click handler that retrieves Persona assertion code and sends POST data --&gt;
&lt;script type=&quot;text/javascript&quot;&gt;
    $(function () {
        $(&#39;#persona&#39;).click(function (e) {
            e.preventDefault();
            var self = $(this);

            navigator.id.get(function (assertion) {
                if (assertion) {
                    self.parent(&#39;form&#39;)
                            .find(&#39;input[type=hidden]&#39;)
                                .attr(&#39;value&#39;, assertion)
                                .end()
                            .submit();
                } else {
                    alert(&#39;Some error occurred&#39;);
                }
            });
        });
    });
&lt;/script&gt;