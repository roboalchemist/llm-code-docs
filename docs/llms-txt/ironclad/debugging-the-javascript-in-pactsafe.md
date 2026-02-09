# Source: https://clickwrap-developer.ironcladapp.com/docs/debugging-the-javascript-in-pactsafe.md

# Debugging with PS.js

You can optionally enable debugging in our JavaScript library by adding a flag right after you load your `_ps('create')` call in our [JavaScript library](https://developer.pactsafe.com/docs/get-to-know-our-javascript-library):

```javascript
(function(w,d,s,c,f,n,t,g,a,b,l){w['PactSafeObject']=n;w[n]=w[n]||function(){(w[n].q=w[n].q||[]).push(arguments)},w[n].on=function(){(w[n].e=w[n].e||[]).push(arguments)},w[n].once=function(){(w[n].eo=w[n].eo||[]).push(arguments)},w[n].off=function(){(w[n].o=w[n].o||[]).push(arguments)},w[n].t=1*new Date(),w[n].l=0;a=d.createElement(s);b=d.getElementsByTagName(s)[0];a.async=1;a.src=c;a.onload=a.onreadystatechange=function(){w[n].l=1};a.onerror=a.onabort=function(){w[n].l=0};b.parentNode.insertBefore(a,b);setTimeout(function(){if(!w[n].l&&!w[n].loaded){w[n].error=1;a=d.createElement(s);a.async=1;a.src=f;a.onload=a.onreadystatechange=function(){w[n].l=1};a.onerror=a.onabort=function(){w[n].l=0};b.parentNode.insertBefore(a,b);l=function(u,e){try{e=d.createElement('img');e.src='https://d3r8bdci515tjv.cloudfront.net/error.gif?t='+w[n].t+'&u='+encodeURIComponent(u);d.getElementsByTagName('body')[0].appendChild(e)}catch(x){}};l(c);setTimeout(function(){if(!w[n].l&&!w[n].loaded){w[n].error=1;if(g&&'function'==typeof g){g.call(this);}l(f)}},t)}},t)})(window,document,'script','//vault.pactsafe.io/ps.min.js','//d3l1mqnl5xpsuc.cloudfront.net/ps.min.js','_ps',4000);

_ps('create', 'YOUR_ACCESS_ID');

_ps.debug = true;

_ps.on('all', function(eventName, allArguments) {
  console.log('The ' + eventName + ' was just triggered.');
  console.log(allArguments);
});
```

By enabling this flag, you'll start seeing all sorts of events in your console and be able to track various events and triggers from our library as you are coding!