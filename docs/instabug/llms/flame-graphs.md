# Source: https://docs.instabug.com/product-guides-and-integrations/product-guides/crash-reporting/flame-graphs.md

# Flame Graphs

Flame graphs are visualization tools that help analyze and debug performance issues, such as Application Not Responding (ANR) errors and App Hangs. The display stack traces of an ANR or an App Hang, showing how many times each function appears in the occurrences of the issue. By identifying the functions that are called the most, developers can pinpoint bottlenecks and optimize performance to resolve ANR problems.To analyze a flame graph effectively, look for functions with wide boxes that consume a significant portion of the graph. The closer these boxes are to where the ANR happened, the more likely that these functions indicate potential performance bottlenecks or areas where optimization is needed. By focusing on optimizing these critical functions, you can address ANR issues and improve the overall performance of your applicationYou can [learn about Flame Graphs here.](https://www.brendangregg.com/flamegraphs.html)​

#### How can Flame Graphs help you?

Along with the available debugging data that comes with ANRs and [App Hangs](https://docs.luciq.ai/product-guides-and-integrations/product-guides/crash-reporting/app-hangs), you can debug those frustrating experiences by seeing the visual aggregations of the stack traces. You can also find the code paths that are frequently associated with the hangs so you can debug them to improve your app’s performance and user experience.Example:Imagine you get a 100 occurrences of an app hang on a certain screen.

<figure><img src="https://images.gitbook.com/__img/dpr=2,width=760,onerror=redirect,format=auto,signature=-1754938049/https%3A%2F%2Ffiles.readme.io%2F68fede69b1cf11974ff06f9118b283151c65261dbc271dc0316085a1d16ad131-product-guides-flame-graphs-1.png" alt=""><figcaption></figcaption></figure>

* There are 100 stack traces associated with the occurrences (1 stack trace per occurrence).
* The goal of the flame graphs is to combine those 100 occurrences.
* The **width** of the bars for each frame would show the *frequency of the frame* to show up in the stack trace.
* The **depth** would show *the order* in which it appeared in the stack trace. (Refer to the below screenshot)

<figure><img src="https://images.gitbook.com/__img/dpr=2,width=760,onerror=redirect,format=auto,signature=1325516117/https%3A%2F%2Ffiles.readme.io%2F5679f6aec83674fdcf0ff0ff93dd7a01d52ff5c68151cf3873672ae0800eeef9-product-guides-flame-graphs-3.png" alt=""><figcaption></figcaption></figure>

{% hint style="warning" %}
The width of the stack trace does not show the latency of the frame, but the frequency.This is what the flame graph looks like on the Luciq Dashboard
{% endhint %}

This is what the flame graph looks like on the Luciq Dashboard

<figure><img src="https://images.gitbook.com/__img/dpr=2,width=760,onerror=redirect,format=auto,signature=-1901080956/https%3A%2F%2Ffiles.readme.io%2F671377cc119c800c9f73f7eda8b85ebca8fc089cee54595e02860b0bf04b0363-product-guides-flame-graphs-2.gif" alt=""><figcaption></figcaption></figure>
