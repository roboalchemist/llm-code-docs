# Source: https://clickwrap-developer.ironcladapp.com/docs/setting-up-the-javascript-snippet.md

# Setting up the JavaScript Snippet

This reference documents the JavaScript Snippet used to include the Ironclad Clickwrap Library on a website.

**Note**: This snippet includes the option to include a backup copy of `ps.min.js` on your own server or one you specify should our snippet fail to load on the page. If our snippet does not load successfully after 4 seconds (notice the configurable timeout in the last parameter), then it will load the backup. Notice the `cloudfront.net` URL which you can replace with `ps.min.js` hosted on your own servers.

# Minified

```javascript
(function(w,d,s,c,f,n,t,g,a,b,l){w['PactSafeObject']=n;w[n]=w[n]||function(){(w[n].q=w[n].q||[]).push(arguments)},w[n].on=function(){(w[n].e=w[n].e||[]).push(arguments)},w[n].once=function(){(w[n].eo=w[n].eo||[]).push(arguments)},w[n].off=function(){(w[n].o=w[n].o||[]).push(arguments)},w[n].t=1*new Date(),w[n].l=0;a=d.createElement(s);b=d.getElementsByTagName(s)[0];a.async=1;a.src=c;a.onload=a.onreadystatechange=function(){w[n].l=1};a.onerror=a.onabort=function(){w[n].l=0};b.parentNode.insertBefore(a,b);setTimeout(function(){if(!w[n].l&&!w[n].loaded){w[n].error=1;a=d.createElement(s);a.async=1;a.src=f;a.onload=a.onreadystatechange=function(){w[n].l=1};a.onerror=a.onabort=function(){w[n].l=0};b.parentNode.insertBefore(a,b);l=function(u,e){try{e=d.createElement('img');e.src='https://d3r8bdci515tjv.cloudfront.net/error.gif?t='+w[n].t+'&u='+encodeURIComponent(u);d.getElementsByTagName('body')[0].appendChild(e)}catch(x){}};l(c);setTimeout(function(){if(!w[n].l&&!w[n].loaded){w[n].error=1;if(g&&'function'==typeof g){g.call(this);}l(f)}},t)}},t)})(window,document,'script','//vault.pactsafe.io/ps.min.js','//d3l1mqnl5xpsuc.cloudfront.net/ps.min.js','_ps',4000);

// Creates a Site object with the default configuration.
_ps('create', '25b2b173-632a-4227-9877-31d2109d8c98');
```

# Unminified

```javascript
(function(w, d, s, c, f, n, t, g, a, b, l) {
    // Defines the global _ps object and initializes the _ps() function
    // that will queue commands until the Ironclad Clickwrap Library is ready.
    w['PactSafeObject'] = n;
    w[n] = w[n] || function() {
      (w[n].q = w[n].q || []).push(arguments)
    },
  
    // Defines the event functions for the global _ps object.
    w[n].on = function() {
      (w[n].e = w[n].e || []).push(arguments)
    },
    w[n].once = function() {
      (w[n].eo = w[n].eo || []).push(arguments)
    },
    w[n].off = function() {
      (w[n].o = w[n].o || []).push(arguments)
    },
  
    // Marks the time that the script is inserted.
    w[n].t = 1 * new Date(),
    w[n].l = 0;
    
    // Inserts a new script element to load the Ironclad Clickwrap Library JS file (ps.js).
    a = d.createElement(s);
    b = d.getElementsByTagName(s)[0];
    a.async = 1;
    a.src = c;
    
    // Marks that the script has started loading or failed to load.
    a.onload = a.onreadystatechange = function() { w[n].l = 1 };
    a.onerror = a.onabort = function() { w[n].l = 0 };
    b.parentNode.insertBefore(a, b);
    
    // Retry loading the script from a fallback location after 4 seconds.
    setTimeout(function() {
      if (!w[n].l && !w[n].loaded) {
        w[n].error = 1;
        a = d.createElement(s);
        a.async = 1;
        a.src = f;
        a.onload = a.onreadystatechange = function() { w[n].l = 1 };
        a.onerror = a.onabort = function() { w[n].l = 0 };
        b.parentNode.insertBefore(a, b);
        
        // Log the loading error via beacon.
        l = function(u, e) {
          try {
            e = d.createElement('img');
            e.src = 'https://d3r8bdci515tjv.cloudfront.net/error.gif?t=' + w[n].t + '&u=' + encodeURIComponent(u);
            d.getElementsByTagName('body')[0].appendChild(e);
          }
          catch(x) {}
        };
        l(c);
        
        // Call the optional error callback function after a second failed attempt.
        setTimeout(function() {
          if (!w[n].l && !w[n].loaded) {
            w[n].error = 1;
            if (g && 'function' == typeof g) {
              g.call(this);
            }
            l(f);
          }
        }, t);
      }
    }, t);
  })(window, document, 'script', '//vault.pactsafe.io/ps.min.js', '//d3l1mqnl5xpsuc.cloudfront.net/ps.min.js', '_ps', 4000, function optionalErrorCallback() { alert('Unable to load the JS Library.') });
  
// Creates a Site object with the default configuration.
_ps('create', '25b2b173-632a-4227-9877-31d2109d8c98');
```