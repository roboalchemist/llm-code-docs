# Source: https://docs.flux.ai/faq/lost-connection.md

# Lost connection

## What you'll see

![](https://uploads.developerhub.io/prod/86Yw/sdxev6zxldii1dpz77ukudr2ribaucx4eaad83ik44ljt4uihhvmyuelkq9vd97o.png)

While you're working, this scary red box will appear at the top of the canvas.  While it is present, you won't be able to modify your project in any way.

## What it means

When Flux is unable to connect to the database and save your data, we will show you this error.  It can occur for several possible reasons:

- **Slow or spotty internet connection**
    - If your internet connection is slow or unstable, it may take a very long time for the application to contact and receive a response from the database.

- **Poor performance on large documents**
    - If your project is very large, Flux is busy doing a lot of work in the background - and this can cause the connection to the database to take a very long time to complete its work.

## What you can do

_No matter which solution you attempt below, be aware that this issue can mean that some data has been lost - so please check the state of your work when you're back in business!_

1. Report the issue in [Canny](https://fluxai.canny.io/bugreports) so that Flux Engineering can take a look!
2. First of all, you can try refreshing the page - if the connection issue is intermittent, it may clear right up.
3. If the issue persists and your document is very large, consider grouping some parts together into sublayouts to improve performance.
4. If none of the above work, your project may simply be beyond what Flux can handle right now - but please know we're working tirelessly to improve the performance of the product!