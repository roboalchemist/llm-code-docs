# Source: https://crawlee.dev/blog/scraping-dynamic-websites-using-python.md

# Web scraping of a dynamic website using Python with HTTP Client

September 12, 2024 ·

<!-- -->

15 min read

[![Max](https://avatars.githubusercontent.com/u/34358312?v=4)](https://github.com/Mantisus)

[Max](https://github.com/Mantisus)

Community Member of Crawlee and web scraping expert

Dynamic websites that use JavaScript for content rendering and backend interaction often create challenges for web scraping. The traditional approach to solving this problem is browser emulation, but it's not very efficient in terms of resource consumption.

note

One of our community members wrote this blog as a contribution to Crawlee Blog. If you want to contribute blogs like these to Crawlee Blog, please reach out to us on our [discord channel](https://apify.com/discord).

In this article, we'll explore an alternative method based on in-depth site analysis and the use of an HTTP client. We'll go through the entire process from analyzing a dynamic website to implementing an efficient web crawler using the [`Crawlee for Python`](https://www.crawlee.dev/python/) framework.

![How to scrape dynamic websites in Python](/assets/images/dynamic-websites-d9a83deff0729330b2d3de2d1481cd6a.webp)

## What you'll learn in this tutorial[​](#what-youll-learn-in-this-tutorial "Direct link to What you'll learn in this tutorial")

Our subject of study is the [Accommodation for Students](https://www.accommodationforstudents.com) website. Using this example, we'll examine the specifics of analyzing sites built with the Next.js framework and implement a crawler capable of efficiently extracting data without using browser emulation.

By the end of this article, you will have:

* A clear understanding of how to analyze sites with dynamic content rendered using JavaScript.
* How to implement a crawler based on Crawlee for Python.
* Insight into some of the details of working with sites that use [`Next.js`](https://nextjs.org/).
* A link to a GitHub repository with the full crawler implementation code.

## Website analysis[​](#website-analysis "Direct link to Website analysis")

To track all requests, open your Dev Tools and the `network` tab before entering the site. Some data may be transmitted only once the site is first opened.

As the site is intended for students in the UK, let's go to London. We'll start the analysis from the [search page](https://www.accommodationforstudents.com/search-results?location=London\&beds=0\&occupancy=min\&minPrice=0\&maxPrice=500\&latitude=51.509865\&longitude=-0.118092\&geo=false\&page=1)

Interacting with elements on the site page, you'll quickly notice a request of this type:

```
https://www.accommodationforstudents.com/search?limit=22&skip=0&random=false&mode=text&numberOfBedrooms=0&occupancy=min&countryCode=gb&location=London&sortBy=price&order=asc
```

![Request type](/assets/images/request-185e9cf4845c0b0f07c004d155563ea7.webp)

If we look at the format of the received response, we'll immediately notice that it comes in [`JSON`](https://www.json.org/json-en.html) format.

![JSON reposonse](/assets/images/json-a85571ceba8b80c314af9a159db15511.webp)

Great, we're getting data in a structured format that's very convenient to work with. We see the total number of results links to listings are in the `url` attribute for each `properties` element

Let's also take a look at the server response headers.

![server response](data:image/webp;base64,UklGRtYhAABXRUJQVlA4IMohAACQgACdASpzAsMAPpFGnUslo6KhpTU5sLASCWVu/HyZjugB159PE/+GG39eku2dXh+QHbh9BX/T6e3oP/9nRJ+iD/G9Lb/6vYG/u3/n9gDzt/VF/1PSAf/31AP//1v/R7+I/jd3xf1f+1/sb5s/jfxT9a/UX/Yf3X1yP7Lwa8xf8L0H/j32e/O/2fyc/vX27+gvt6/gvtp+QL8f/in97/r35E++h7F/n+0KAB+X/zv/Xf3b8pvbH8n/xX9I/GL4F/IP53/o/7J+UH2Afxv+af6j+9fjx8O/3D/JeIN8y/w/68fAD/Lf53/uv73/o/2R+jv9h/5v95/wn7r+yD8y/tf/U/w3+m+QT+Zf0//f/3b/K++D///bt+2H//9179of///zAz0RHd6I/5A4Rh8ndm/Y1S59TB7Us0tq5QYGbSdMM9X6dk9N/jRMmT8W2VF0tPnwDa/knroHOydjn+QiIiHqsaatZI8dG9PTu0ZUaxbJUy8rWPSUTopp1wA87PAsLEBC2xm683GRd25pu08RIrVGIzPhsz4bM+GzPhskbKZUmlxNW7nhAwHT+g41APt8a1+JtLhD3GfMy6ZbsnX273JQ9qrLT6Pdmchf7mSgSeZUfLeEOqgKJ+zHcZWL+Seugc7J2OpS+KGxpEwmNwGxtOIdAuUD8qjp0XNDx9JvPcAXMwIaebnC0kdhveRhHBmJBzmhmoyBJon5GoG1/JPXQOdlADyMHJw9SVw02TRTdska074IKu3dmw0HCYGG28dbmrUnaa6bx5cvlv335VnTxJtfmdk7HP8hERERWPtwUCgWt5kGs96v+b0imC7jjD0D8o3XeRpOcRMfr+8cAeu+WPb/EAvW6BtY7hJrstZVnqjro390FyBwdQdQfr+kbwtl+VVVVVVVV0OPjBgsLFCymAj2tCer+SZPJix6KBhuyfFetCKPU8/UschSrlw1ipn2ffwPNvo9UYabXs6rSHuXcNcjfia9WQiIiIiIiIrHfT8uBgw34l1idjn+Pdm3/YBtP4ofOk2y4atiWiAFnL+MwQlf6nBLEWfMaPZcZr0sAbwL8cG6UYBQvjdAU8CtkSK9S/8VzQLkFkmoG1/JPYqXA0cFcJlfaBpDxNBmFJbkIiHb0nqQ+lfjiBmY3gCZHAKKBYLflpLz10DnZO2rRXhCS8NdY8UhCUD8qqQDXP/GpBElzXhMoOdk7HP8hERERERWPxpqON4I8GkC4BbnJH3yERDyKFJCobh6iOVyGjkRERERERERERERWPx4r1k2Z5Bqvjuk1emn2RVQi3Wv32kvgazVHXKGdhf2011r+Seugc7J2Of5LHzF/AY9B2W3ZNbDdsEhye82EKn3ZckOT325BU+7Lkhye+3IKmWxxOKkAAD8iVwV6FM8oPeFAAkF3G6dTjvULyCJHNxEp4viEx2xwk8efiS3rScf9NBdtKzhSkZyQ6dm67BccUM2aaR9dGml4yXoVlEllg3+ntsMAkU+2s5X1QCInTto1IO1gkXFuc7dG5gzZOGdmEtbpEhRHBmpjot0gmD9iUsrc7eRU9rsDYXVgju1C4ks62K1QlMrz3b5wV33kiQkyolwXrcNskZMhjG6gPJ7k8hPm/wXxpeR10foq+FukWMZo3DOAxl78rzF97SGnqh32/a3P6ItaMMNuk6xW/FBp+WjUyLvw4Pd77JG04QTW/VbMANfsHnQrfYMWzI6jKZOcjwWU7vw6cBzM5YPE+rVYlp6iJziQUg5v2qMN5L5Xks6rbhC9p9uUA3GOsfY9DXLpj9fhs7CBr37G68AYjeSoTTRd+86/3q5XDzHfTHOw/yfQ87ZVORqPaWLuPogk84E4OPjJggIr79vwgXr418nNbrHNdefgIiP6uECOi9byNzrjFVhUUcVkiVFihpbM0jF8BmMrZ8n31dcBxW9nFGzBlsABGVwD/ywDCLL0v/aqCerxpdKHQKTZrikGP6etfAwSzl5S1Atsohz9NzMNSN9bru+gRL1IKRxSGqgmsWdqpGpfts1+Y+8qWXwyg03r0pujVmdjU1HccQKWLx8pgA+PNm0W3rUwaM80RBepefKRsjDAerUeyBy9YFdhDcg0TZVJi6qxdE6nHQ47fxYYrhOVOJRwMSN05DXXZdSn8v5qIcCZYifz1x9l38ATW/fxMoyfOxoc4seZrAQAM8XXe/msU54uIU7g0++Z8qKYVDG4ljFBDbHRFl4NIZaKkdokocsKmdPKFJENwPtrfqYKZj4++DgizXoU80Xel/GUuDJ1o4+DaGZsWMAwqYvFMPEhwO4hBOL4W/dPc2Pi+lcKNlL9S4NLSmIH0GOENmzrSgQw6B0Cc7xKibh4lFkK+lUOrvl+m9vD11g68Y48Y4ha+HeZ2DziOXORj21mVULwvoizCQjETMPHGSMVvMCm1aWQHFQFz6hdFGMfpOV5Ec8Q9CZSqEp2aemIqMpzpCOS2tQ77KMOrZ20L0+GanZVCzIHQxeNAvtQCguWGfWwmLHfM13y7jhc1eQwnsnfa3C1Cd3YA5Kye4Eq1/FNhwD0UD1Nq8jSTIuvlCoaQL0mkjBZ74qGVK5h+AIeUQmaLTEh1ItKOj00Hx3vUC9ed5mOFigqu1aRWozgJlPw4LUOZdCyyd/aAdOgqceGx0uXGXfwPdCeieVyHem2KgZkRaisK8khH/aO0cuGbEpet7r4xZQDCljUll2jhgcaBuM7FrGmx/j9yjW+3xuyD6si063qPjU44YOksdp9vf+CzJLOlH4+wRGgPsUssp54isUlOhyOck0FTnAatXAvtSmLrh7C4TcChzowVLcKPDjHevX+sXC1ymQ7ppUvWheSbgal087V1wcVmxRiuxsY0pWrZZfIMs49WAUwKgs+kCRq5sEciauphVQqqUTxLAP1zmEy/r5zVJOSr/euDuOKnkaDZq5NWgPqmAh078aVPtKT0vnAoveM/mfjqMUkID9qjWlMhAPowX8Z16SzwVkwOwOpYjtVHHA3yjOlITOXyxIfynsLy3iSD3Bm4vlWjwM3lMGIwluBaZkKyKJsRzIaQwc9X1pddeUELx7GMU9z1BJs3MohIwOObNlGAmKAT9QsGI6c4YDjTKd2+/pqRXKYxxUInGweF7HXc8rzimvHU/By/SqKVtiUgPZpem0d6w4GOJpunov2VrL0YH1Crwn1wTwXLyWWXQwtmQ258yzADzZrgqJ9WDf66waAImP3Da35tzaRIM+p968rAy/tm6M8ZQyA4tQAraFWMrEny3uOXg6WaL2yL544Hlin4Rmq+hAx0wy+yubqTyPtgqn0n8EHQ+2wH/redI/1kr7RW6wRUGDXFtZ77XBO02F6PumAOKmJZz99YH82MycdUhr0/IMuRzXF2X/vhCpCHSy+byjdQMOne9NwB9NG49cPDsTL/Id1/YWiiB8kDguazgBpY5WrdmNflxBnN6Ivad5yjykBaH3+v2lR3sz9n87jSldZpCU/GkADqlhmxxuSWgnjtatIbO1RUc8sDM2OZlcZ1X5DnMM/PMfFky5yZIIOY6DRNKuixYkm1TFiQdkmb6nfAgTTLpkO2AQcj+NVwXzOuZt2enEMeYE+0zlfQnfZkXEMGWaEEZqZ+/a1gl75Z0r6qcHq/loNcFXEF5BVjbE/QDE4NYVeDZLkmW09DZxnUpjXpFA04WGiQfrWyHzBQSqjpeqGcXXtb0CDy2aqPqwLBk4UKySNwc+nuG1yUFVVhZNt/HR++O9ZvH8d6m2F4ziGeokEaUGep1fSO8dgK0CLBovRIfdgDQn12USruyIHg0YmuH3ZtVpSIhJp+GxAHGuJQ/yQM0tqagCe6Nt9LYCuDMyxgjIDF2n1Xyr3NCDlq9hh7G8VtpkocZ/0rFDWFXmykzyJZ7jiSbq58ZLMtwaWCH9edXlZ40JLFtoVy1d+CbO+1Afk3k5bkT5qf9xlUr2X76xmyJXyeiAvJpzkam0KX4DCMW5romH6o72Wk687WJq/6MZfvOb8Sud0Tb309MaIS4cpjCvKgPuq9pYV/2PvYFhtSMdcEeYjySnx1oUQlAAminZ8ByTWs2bWKtrpf/czL8hoZNKuHf+8e/+r+KaRAOucqZ1fNFRjrye3MAzo31NtVh+dnxx771o7Gl4RYeQWKP5PLa3RzVlEabW20JahvQgEpRBSddN4LiAiyOebiN5OdorDJYKyB2jCrAAffznb6hxXbmio0hBIQWFidvVIhG9bl6OkDFmyb9FHCOqCBdmzenJUF5b/Gjh7DjDTGzznHPek8Q48wdcsv1WnOD44smFmmO8PRCCc0UQFxXVxNtLdQOFhgWgdae/WMwmoXV1UKo90c4gRongtUMWJalAV5x3givUEg3KSDDm+JfuNXASsYReyVZor5Ti06RLAAv6dhYRRFRHFnGBwi+L0pAS/w+FA4dvxhhck9wiCS64l9lPAWEjRQCJW+IKskw7vdkvCZCxSQop2FbR0PZNQfBzhc+nMKjLJuTSm7zDzUzNynQTDv+MHdHnLU3ZQoY9V9dSiHEzKIA+//VlLJuI7wNVNCB3iSTNHK2CFKufbCPMhdqcUdHhNtVbqtAZYTMZ9LtXS+uMWWIivzf0+T4UaGggjuksh/6OYNIRRwvWKhlH4T80MFX2X8EXqWx2z4VZtPqZRsRu82kTosIy/HbMyWDJk72h7oisUWSGKS7bMa3btadxEQ9UD1cCiPCWO9mFVNMbs0EmWHHJMMeXxkoeRlDzcAXKsxGSQ07LGApOIzvlNd00b80O57HiTe1mnmBy0knQvORjtNjJbn9LIs9GDQJdzP8L+91z+mmS6E6VWnfB6gCZWzqUZvfDQYcUfyEdKASD6t1f2v0Rs/DlCcd/l0n0LxSfyq8iRSOsbUxgOE+lgX3LCPtIXXUQKVL0ostdt5nFeLN0bcOuKrkl2BwTT2A/Dk2QRQeIqJt5SIjo/NgFZqlD18Z2Evnu/JRIS3Mn111YfpBhGKnODhrIfr/sSI3Of8y8fKJ585AiNikV4+ZSwgBMCNgNGtPrMq8MwMn9foX2gM+HQQmlZiGqcsYEydPcUCcU6PmR2eYZSnAuLAZ5rZxKJruLuqy4gDiSLqAlaVSIVgwcDqJFKjPr0iqSK7XDuVY8JCpSor8TgABXrQ6dmrxSOaLzl13w3cdjDn3/tZsj+Hw2ByiBoBvc1+H7N22wrHFtYf3AhTs6NT54szLITMSvkWX06gbyMO7kwWHBdTChNoqytm5mRkNuNd+BOGp70jxWUFmTFUXvbG9IR2Myrj+oSsO0ca+sQtrHQKg2N3vtws2LZjDjYePrsEgZLLmj5WIw7CuHoCOLED/ebJ2RzM0BvddBzHt54oi3BHoUgAvOxVbh3TI+v4PxVIiscGN4KvzdK23CnwFPPBlgjHTPl1Ym4/0xFcnHOnV7mH9CJ1AyEQoDLWmQ03Nn9qTEnDAgnfAIWz9Nq01SmMuC8qDoAm9zLAtwy3pls/LguQTg/3OSLij6LS5hLLaL3mbQVNf1dRwOTzQI0V2VTdZFy5GAZjpPHzUL6k49HgCzrk04Nsasl/HHq+Igm9xhhNonEbCtIAGz6zz26EJvJ6pP6TC90wUbd5r2IAosIyk0coOYTwkEUtI1bg+p1QsQqMK+Q2d+KO24crHnX1+mPIklcLDudyZT53fyXRx1nDpgYfxSlJgJjv7UXbB7mq2aBhACZvAHRRwjqd3+WT50o3kVxx/DK/WItp83bXMRqDbD9lX0yOV0zLvC1grTy8fwyRhbm2EyMOEJhiC1xjbVGzXieUXhj63TbqDl7xlVALiuK9F8ruBS+N4gthlGWuf4qabMdpRPjINyto4Y7xJA4zpBUt9EpSBsG616TIlKKfjL3OUM5QKDkozw8CXnXsDbG5XVfOdzzyi+coamQyrYMuj5QqWN04oS/EjrU6x4BrSC2Tkm1sW6i6xcVaVUbwqwLk6yMd4CwNH6rQhjo0jVI+H59P4bFCk0Sx9IbiwlLZiVcfKzzLfgVCms5Ap07Cq2YiBqBhWF05S23jWqbR76nZy6/ijjQv7g5QzvReSZ0N2d1dQG9VZ+FokG0VUzVE0quOM23RUERELUSgdOEjeUgU4tjVkH4IsduaBf+mOOmy/AgnXlFrYuBKdsoSn10i19zTTFyyL75CqK0GgXXDvw/QiN9NZPE/AXhqsej6XL8WWmBKiLOXfTGOTjSxJUh4AdB+OOxP7iJ47o9SzvOyt6hYZtkDBHoBXii3qFyuz6KMHeFuihPEM2VXV1643BdEc2xefzs411YeK3wJemGrs09M9j6Ix6r7AhplBc/tdrMnQqRrUZtebXb92Fc+psxGwkyyYeU21ZNZquU1onpJcekWUBIAaFt8WqK4CEjtTXmgccLrOjT9y+VlYwq+ruuHhkwYqr4XK9pB3dk1XbLl5qLiz3D3Wluh0fqxAaFy4cGOv6jsuh6ajlW2fONprj7MvwQrWFI/U8oaJCHS83X+G2OznoHYogdmG+isXTGJkds7T+6Yc7JOGa1CixzF4Z8u8ZcdJ/cyNAxCD7yObXkQBmJmrnDatTbEdGCOc/qTrx5Kodwt4VE5QH0u4ecZk9EwWmCq3KMMpAhgeRjz+wRb5Fse0MQqzZzkoXq2dtEm3z7Fp6M1JkNdUb7DIik4qpWaJGRMv6erXaSvd0q6Oa7nm8TlSPgGW7Gd7z6MikJhys/IaJvVHIzPQPeuoWfYkRS+xK0PwN70VFvmDulya7nmgqCrUal0tbiIfZLuaSpeMwOAkRfvPCTO5hQA8Dn3kbUJ9d9FyelugnxbpgMMjIkdZ4cFzcziBbtsclQz7ObTYxHmvbn3SKZVrjcWjUX/bh+yvrlRoo6UgHL+9D2Ffk1kFUNfLLdNz+zmPjHImBcHTRK5Xkm0nTFD90m8iwYqj7HN6KZG6r/Czq5ToMFMS6S399MgxAy4aL+HjXF8a5POfbOf7hRLr0qX2Q1urKiJHpksbvRXI90jF/s+TgwFETpVaKzvC4YllPuO/MGZ6Q3+ybddwbdfk8DtSx924urg8P8dLifZccD3CGQmnlqkAp4oyAiJP9zAnCHrRSoNYW+tHMnWT7syw36lNXweQtrCGiy/7gwz3Q89YtbEFaCACt0gxe6Vl+Q5EGwBt78F8u04q2CB0zW34jIj+ZYPvzFbRGd2FOyDfeAjy+JgdYjJqpmUUlB1uXVwupQPvcKn/Y+Pur+ajiQSx4wKUVsS8LIY2+yBhfpR1W2iBG56y373PWXzlqLfeLo4ux/K/zVGkX+tnCtsbZdgLImwSE5CKV0z1CrRl/8L30mpPj0iBquaKlxHc1yJarSEWRntzT72/c0oC/2pr9cYeOdI0srhtSvBKiU8VRkBsRrMWHaKVIgQUH73Q3fl2n1h0H/w+pblNUf55ysTPk3xT5E2zQpZDbGs6N03ybNZxEQYdIZCmFP06wgqZ3DM+2gm8aRZgN+2uswo7/aN98dsaeU9Tx9AogJL6FP+ADr9hO/N+MQK1qXXYxWDBxJJr0DdVWAApe9WHPzFxbB2nH8iwtxpqlos4lAUFHzg7F/nBOD8/VUNP4fRYOOYz7dnsbgOIhZI0fuAXP13a2vmNuodlok+871sUHzKWaHBsCXbgyBD3C2F7n8R18icF6SyU7qHyl8nwSy3UFY/WC3avSExt5CDfmj91fFSMPsNBkJDd+6n7VgZVSUnlbQb9/2pHQ++B5cB7p6spgf7mco9mVm5gih/oLBCKm0dUCcJNNMGDZ/LheyVPLpYcnNIRZDBVhIkVJsprIvKWzHa3BCxbgrlu980BTGRYTWOwDGFiFNFVkw/8DEAKWqnDgS7mI9DiAuQ5NF9sNqu4QYMdIM4XRIX4SZzJltfVlGFwOpVQRyoBTT/MVD0zvfxCdAmLRfUS+9FJvEfOi8tZkuNa9JxPNTNIFpN6KrFwLTVHlaO0+O3eLNcKHxbtvuFJYCqeAZevfFvINOFFGDT9uny3ZR6lVYDcDtKHgpdCCe3s0+9OoF2k5hEyUljqoIIdIlpC5Ve0gtsl6fjZOn841p6ucQAOueEf2+KIUM4hdJQcxYhOz+ZSWlIEMB3JzwXaRnjzlZrQGMaIkIEJeHXjJYx9j0OqdyfckUcPfioT4DT3hURjXvlMzC7OtrhQqNZu59Vmex8NIJd5kWmREPnwrCMLGM2yQpkQx572TEMtkwgnQ5D9K9YcRQwEnJNe67ssX38fUbvjflVDqliXDDLTDg7NFBNBpClgxjBjSuaUiVNnJ6JyWkkn6UZxKmR7GxLB/aEMBdwsRWsMGzRnr2IEey47lZcnAsR8ejc9FFq1ayjb8ecAbKdfKpzEs3Y46rs2KXeF/BSNzCf3PNuDIjJPTT89m6tuEwHrSc6YuH/oCLDN7IvbBzALxxKRSse06ac/EeXt+h2OyvZj8h4e1EF6s5AtNU4gx/CdkUWB1QgRVOA8784rpHHR0WuNk0H8z6uU8nutO9lsDehgfHovDnFGw02d+YJt4rUW3iTEf7RLw8ZlzDd9X5h1iEtHQZJEazr1rzaRJd4CZMn7X9/gYZvPUqc4m0svU6JzSUKsuUFmcWuVoEkcQwk8svJ2L2R50i7DR6WhRf+TAcs2EN7efXdkBSkal4KOZRVO4FLz11wezTfO1Mq3AaZkkNV55yh18MehkzmJ0ptF+LXvtqsYnPLJSYL0e/47NXqTGqB1U+f7EjdqAlV9WtUPU+H9UmoJ1BVj5I+5W8ukGu33yICzNzz5iq9V/MYgwfvgw9HmJPjSX2Mq9V3Bs+updBzZUpMiWYGNTlzDbVfBzCiTYVI82kS6F1GDhyb6q49kZE2EbMDcyfjPsY5HZIYYsZfD/0gntEAGvTo/Ks6J4q/SrgVwA8WVLVhwxB2RKHG8J402Lf34XF15uWKdqc6rPVKRp3dniAN5pvA4gTkBFzf13h58lvRgu6XTJ0swNn0mndDWa4bs5oYa1InaM4UW2fh1KszptJfYRA9XINzRIvF8UpL8qEKedZzc8ySov7NBM09hoF6wTYXxOaZ/taI87y2eApFkL4s+z1xAwi0duxgY7ow21WQ7aWCl1KSB7UuxoeL/rhYFlQe6Aa0U9zk1mH4W98H0BQwnYFfLWxeEOu+HlkpkaATPupjUb6aqBnjboFYXXnd4ycIK1COlyP5JlCaBY5cHbihIOyyFXVk7fH0ppPztv/7BXK1ovsFTmRUDZCnyrypUHTIKzYFwcb0pLt3UN2S4ZTFg5s2B+hEKRPr2vZdAbXiK5eiS6U5bP9Z6mrw4soNdzQ978mviyF4GDL2ZcyTL82okXzVg8CIrGyXe2FiyNSohpy3d8yjMcgRI1zWaL/fMY9DiRkW/SjEcYozIBNFzJW37uKCa18WPsZqg6zoJ9pqiO5+TOBEgiFpgmx9/1Fi9avW/sUbeo/YYHSO1as/iMuw2jVLr2zjLsHO2tRobc+5jSLUwleaP2Pt4TecQlLZFZMgbi2brn10stGBQPrULHQ7y/ML3wnX/wRPtpr5hebHQS+OuoiC0NreVZeBzH9RelRe0VZA6TrNqOlO3yX36JhpXc44gbw1wQGLDn/70pcpyIjTP6gr1iadcosFI8WwPMQTxJRS5qQEuEDELIx1xJo88maFEm41xqJOPCwKeaLI7X5a9odcRDKNvkOWeglKcCssKUZX9Oi4/kANQbNP5l+6Gd+mUHRwB9beN8jAa+nGDkwrpfzJ2qvpV5Wn0eSc/euNxlL7emh3P4PYLoiUdz07+cpvzOqUtwau7dreNDO4j93YE49j/SPh3ssfotVq+bpT2DP4vNVOyrABsA3kzS6JMRyrJ/KPNqEV82X94FSC969CKUGOqtgr/dxorMwrZPRAojHUopBZTs0MfAFMquUnxKFsKLMYRM327L6tkTV31YkDRBTBfO5BwBaZbZ1YSq3DlpF36JjCpn19mzRq00Zyo1pT3YA0EOBXYnsrwjf6fLl3qLJM/B2aqvSrvWDVHAlwLeEN4juD0L3tDf/srsKkEiidA+m3gaciL5WkkoyOd6bf0upN9EgxxVRkNom0DTK5vNZM45VKNcw9y3OlOJKKlmzIMflikoYrbdjpRfQuDev1gPJa/AM+hNAydDIRuhpQpWuTUJPRGuwLsISVCJZ6zRZ1CFGsHFLiqvAT3NIfPXtf03e+tX2ZLO1H6UOlt5YWE5ynuKFsaY5abJ56G2awpIWQwEPXpqVMFK7pM8c5YvowyTBVs1A54EvL3m/+/V//WC13a4PAI0IPHO3KW3AyMnoYoqUSOHPwL6W7KwrMREylahhndK8x0dufG9+V3ZZSOXuCleiz504Gw6x1U8foRMdsR+eM0X7mmtroX4VT7jKfIAAAAAAWAixWvTN8hHfqjaFHDZ53VcY2OjVt92q5R12m/6WHcUiXszd2SVQ9wL1cONblBwWunZJ4qKFQ1cFvmL47L9hGtK9/NX5fH2RlaJkDlPQguWZS43jEAFRRR5Nyce23psI+gPXG7WX6vzGLqzzRu8U7lHtRi8bNujQai8+0gxMWvF4QzsRgTSraz9OkgEqUMCbLcBuepqSnzIhXUmF1SUazWVH7EiGIMtohcB9eZz2xvKbyMnAFbRgvVulxWEjPIBjMLTOpXyNMxghu9eihoaQIpKzKYDEADvD1Hi4XeaSsOoMZq3qRjLsv/v1yb3CQ26WLPVdQ9/E2VwxbdpEXYKmaO/YTfe/gjvJYSSzwMDf363VQkX7AAAkN6uWYbEONss22RdQW3Hbv1O2aj8dtsgrKrlH5ABD+GBYDKtGDJWbucEqvjmE0qiNod6NyUkwyJkDDPqlk75q0ejqXFwpfZwziykrne0mQXxHwBLHMGHQn4yHYOWGEEJRPvXRQ2HxpOqa6utjEIlQclaZ4o/XSrtpdDwijjiflryKib3fcYZpE7hm402MJTNqtMHesv9BoEVbdr5vIn7BhUYG6Jkusi/xSMhjtSX8cQj8Fc3dD8RSr8zXct55AYOrz71IK2RTKy9+pZBzSXOEVjS/XoKKK4E139pIRu0wqcqp8Yg9ItG3Ji3Q1N8C8aoEMcFDD3Y8hDsJAtgHCaeXM3JsUVyIRswn9dAROk1DAdxVhcjIQ85DDG3KRPEe6B1145UCTNo6HBkgEtWBTvz8W05YQAJi5VhrAYKZtq6dMU5cvLn4FOKt7UZGsrwY9AtV3ZKgUbYR51O0bTVtanI5RrxJgtp73zd0OAG5/yW31BEiEbLHJ97W91VBUjzPKWmgKlh5p+6msLybwvdYzxFKWto54IISmvCXN36Vr9HKbGITU/Eayt8E1ym3GGz17LY2hDNHKSPWIPJBg5U1MoLxT2S1QkmbJYBHvO7TadyRDeWm7u9YrbG/q8FcTPHo5OFKRk2qtxLv7HgzNzs3BJMnzKfLQs1YYMF9Ci2gpGNGRrm7jJmu5Mm+1lFWAXI6ouTuHF8vuZfmHS54I4Q5qt1ZmodC7BWAVXlPf7wthBOKqxAW3ANZvoYUG1Tnrs/MjxT/3jwz2SrCxX5QBrQvAj1IcQ/oEQrZ2gBynGMDQEclry+nFeEgAACuaBSnvWb8nuDAAAA)

* `content-type: application/json; charset=utf-8` - It tells us that the server response comes in JSON format, which we've already confirmed visually.
* `content-encoding: gzip` - It tells us that the response was compressed using [`gzip`](https://www.gnu.org/software/gzip/), and therefore we should use appropriate decompression in our crawler.
* `server: cloudflare` - The site is hosted on [Сloudflare](https://www.cloudflare.com/) servers and uses their protection. We should consider this when creating our crawler.

Great, let's also look at the parameters used in the search API request and make hypotheses about what they're responsible for:

* `limit: 22` - The number of elements we get per request.
* `skip: 0` - The element from which we'll start getting important data for pagination.
* `random: false` - We don't change the random sorting as we benefit from strict sorting.
* `mode: text` - An unusual parameter. If you decide to conduct several experiments, you'll find that it can take the following values: text, fallback, geo. - Interestingly, the geo parameter completely changes the output, returning about 5400 options. I assume it's necessary to search by coordinates, and if we don't pass any coordinates, we get all the available results.
* `numberOfBedrooms: 0 `- filter by bedrooms.
* `occupancy: min` - filter by occupancy.
* `countryCode: gb` - country code, in our case it's Great Britain
* `location: London` - search location
* `sortBy: price` - the field by which sorting is performed
* `order: asc` - type of sorting

But there's another important point to pay attention to. Let's look at our link in the browser bar, which looks like this:

```
https://www.accommodationforstudents.com/search-results?location=London&beds=0&occupancy=min&minPrice=0&maxPrice=500&latitude=51.509865&longitude=-0.118092&geo=false&page=1
```

In it, we see the coordinate parameters `latitude` and `longitude`, which don't participate in any way when interacting with the backend, and the `geo` parameter with a false value. This also confirms our hypothesis regarding the mode parameter. This is quite useful if you want to extract all data from the site.

Great. We can get the site's search data in a convenient JSON format. We also have flexible parameters to guarantee data extraction, whether all are available on the site or for a specific city.

Let's move on to analyzing the property page.

Since after clicking on the listing it opens in a new window, make sure you have `Auto-open DevTools for popups` option set in Dev Tools

Unfortunately, we don't see any interesting interaction with the backend after analyzing all requests. All listing data is obtained in one request containing HTML code and JSON elements.

![Listing data contained in HTML code and JSON elements](/assets/images/listing-d32f6a4dabca952c5150d3e4705028fb.webp)

After carefully studying the page's source code, we can say that all the data we're interested in is in the JSON located in the `script` tag, which has an `id` attribute with the value `__NEXT_DATA__`. We can easily extract this JSON using a regular expression or HTML parser.

We already have everything necessary to build the crawler at this analysis stage. We know how to get data from the search, how pagination works, how to go from the search to the listing page, and where to extract the data we're interested in on the listing page.

But there's one obvious inconvenience: we get search data in JSON, and listing data we get in HTML inside, which is JSON. This isn't a problem but rather an inconvenience and higher traffic consumption, as such an HTML page will weigh much more than just JSON.

Let's continue our analysis.

The data in `__NEXT_DATA__` signals that the site uses the Next.js framework. Each framework has its own established internal patterns, parameters, and features.

Let's analyze the listing page again by refreshing it and analyzing the `.js` files we receive.

![Javascript files](/assets/images/javascript-52ed58b7cb5fca440f94193ff7687de3.webp)

We're interested in the file containing `_buildManifest.js` in its name, the link to it will regularly change, so I'll provide an example:

```
https://www.accommodationforstudents.com/_next/static/B5yLvSqNOvFysuIu10hQ5/_buildManifest.js
```

This file contains all possible routes available on the site. After careful study, we can see a link format like `/property/[id]`, which is clearly related to the property page. After reading more about Next.js, we can get the final link—`https://www.accommodationforstudents.com/_next/data/[build_id]/property/[id].json`.

This link has two variables:

1. `build_id` - the current build of the `Next.js` application, it can be obtained from `__NEXT_DATA__` on any application page. In the example link for `_buildManifest.js`, its value is `B5yLvSqNOvFysuIu10hQ5`
2. `id` - the identifier for the property object whose data we're interested in.

Let's form a link and study the result in the browser.

![Study the result in browser](/assets/images/result-64a7188999fd127f0b6e26bf94a4a7e5.webp)

As you can see, now we get the listing results in JSON format. But after all, `Next.js` works for search, so let's get a link for it, so that our future crawler interacts with only one API. It transforms from the link you see in the browser bar and will look like this:

```
https://www.accommodationforstudents.com/_next/data/[build_id]/search-results.json?location=[location]&page=[page]
```

I think you immediately noticed that I excluded part of the search parameters, I did this because we simply don't need them. Coordinates aren't used in basic interaction with the backend. I plan that the crawler will search by location, so I keep the location and pagination parameters.

Let's summarize our analysis.

1. For search pages, we'll use links of the format - `https://www.accommodationforstudents.com/_next/data/[build_id]/search-results.json?location=[location]&page=[page]`
2. For listing pages, we'll use links of the format - `https://www.accommodationforstudents.com/_next/data/[build_id]/property/[id].json`
3. We need to get the `build_id`, let's use the main page of the site and a simple regular expression for this.
4. We need an HTTP client that allows bypassing Cloudflare, and we don't need any HTML parsers, as we'll get all target data from JSON.

## Crawler implementation[​](#crawler-implementation "Direct link to Crawler implementation")

I'm using Crawlee for Python version `0.3.5`, this is important, as the library is developing actively and will have more capabilities in higher versions. But this is an ideal moment to show how we can work with it for complex projects.

The library already has support for an HTTP client that allows bypassing Cloudflare - [`CurlImpersonateHttpClient`](https://github.com/apify/crawlee-python/blob/v0.3.6/src/crawlee/http_clients/curl_impersonate.py). Since we have to work with JSON responses we could use [`parsel_crawler`](https://github.com/apify/crawlee-python/tree/v0.3.5/src/crawlee/parsel_crawler) added in version `0.3.0`, but I think this is excessive for such tasks, besides I like the high speed of [`orjson`](https://github.com/ijl/orjson).. Therefore, we'll need to implement our crawler rather than using one of the ready-made ones.

As a sample crawler, we'll use [beautifulsoup\_crawler](https://github.com/apify/crawlee-python/tree/v0.3.5/src/crawlee/beautifulsoup_crawler)

Let's install the necessary dependencies.

```
pip install crawlee[curl-impersonate]==0.3.5
pip install orjson>=3.10.7,<4.0.0"
```

I'm using [`orjson`](https://pypi.org/project/orjson/) instead of the standard [`json`](https://docs.python.org/3/library/json.html) module due to its high performance, which is especially noticeable in asynchronous applications.

Well, let's implement our custom\_crawler. Let's define the `CustomContext` class with the necessary attributes.

```
# custom_context.py

from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING

from crawlee.basic_crawler import BasicCrawlingContext
from crawlee.http_crawler import HttpCrawlingResult

if TYPE_CHECKING:

    from collections.abc import Callable


@dataclass(frozen=True)
class CustomContext(HttpCrawlingResult, BasicCrawlingContext):
    """Crawling context used by CustomCrawler."""

    page_data: dict | None
    # not `EnqueueLinksFunction`` because we are breaking protocol since we are not working with HTML
    # and we are not using selectors
    enqueue_links: Callable
```

Note that in my context, `enqueue_links` is just `Callable`, not [`EnqueueLinksFunction`](https://github.com/apify/crawlee-python/blob/v0.3.5/src/crawlee/_types.py#L162). This is because we won't be using selectors and extracting links from HTML, which violate the agreed protocol. Still, I want the syntax in my crawler to be as close to standardized as possible.

Let's move on to the crawler functionality in the `CustomCrawler` class.

```
# custom_crawler.py

from __future__ import annotations

import logging
from re import search
from typing import TYPE_CHECKING, Any, Unpack

from crawlee import Request
from crawlee.basic_crawler import (
    BasicCrawler,
    BasicCrawlerOptions,
    BasicCrawlingContext,
    ContextPipeline,
)
from crawlee.errors import SessionError
from crawlee.http_clients.curl_impersonate import CurlImpersonateHttpClient
from crawlee.http_crawler import HttpCrawlingContext
from orjson import loads

from afs_crawlee.constants import BASE_TEMPLATE, HEADERS

from .custom_context import CustomContext

if TYPE_CHECKING:
    from collections.abc import AsyncGenerator, Iterable


class CustomCrawler(BasicCrawler[CustomContext]):
    """A crawler that fetches the request URL using `curl_impersonate` and parses the result with `orjson` and `re`."""

    def __init__(
        self,
        *,
        impersonate: str = 'chrome124',
        additional_http_error_status_codes: Iterable[int] = (),
        ignore_http_error_status_codes: Iterable[int] = (),
        **kwargs: Unpack[BasicCrawlerOptions[CustomContext]],
    ) -> None:

        self._build_id = None
        self._base_url = BASE_TEMPLATE

        kwargs['_context_pipeline'] = (
            ContextPipeline()
            .compose(self._make_http_request)
            .compose(self._handle_blocked_request)
            .compose(self._parse_http_response)
        )

        # Initialize curl_impersonate http client using TLS preset and necessary headers
        kwargs.setdefault(
            'http_client',
            CurlImpersonateHttpClient(
                additional_http_error_status_codes=additional_http_error_status_codes,
                ignore_http_error_status_codes=ignore_http_error_status_codes,
                impersonate=impersonate,
                headers=HEADERS,
            ),
        )

        kwargs.setdefault('_logger', logging.getLogger(__name__))

        super().__init__(**kwargs)
```

In `__init__`, we define that we'll use `CurlImpersonateHttpClient` as the `http_client`. Another important element is `_context_pipeline`, which defines the sequence of methods through which our context passes.

`_make_http_request` - is completely identical to `BeautifulSoupCrawler` `_handle_blocked_request` - since we get all data through the API, only the server response status will signal about blocking.

```
    async def _handle_blocked_request(self, crawling_context: CustomContext) -> AsyncGenerator[CustomContext, None]:
        if self._retry_on_blocked:
            status_code = crawling_context.http_response.status_code

            if crawling_context.session and crawling_context.session.is_blocked_status_code(status_code=status_code):
                raise SessionError(f'Assuming the session is blocked based on HTTP status code {status_code}')

        yield crawling_context
```

`_parse_http_response` - a function that encapsulates the main logic of parsing responses

```
    async def _parse_http_response(self, context: HttpCrawlingContext) -> AsyncGenerator[CustomContext, None]:

        page_data = None

        if context.http_response.headers['content-type'] == 'text/html; charset=utf-8':
            # Get Build ID for Next js from the start page of the site, form a link to next.js endpoints
            build_id = search(rb'"buildId":"(.{21})"', context.http_response.read()).group(1)
            self._build_id = build_id.decode('UTF-8')
            self._base_url = self._base_url.format(build_id=self._build_id)
        else:
            # Convert json to python dictionary
            page_data = context.http_response.read()
            page_data = page_data.decode('ISO-8859-1').encode('utf-8')
            page_data = loads(page_data)

        async def enqueue_links(
            *, path_template: str, items: list[str], user_data: dict[str, Any] | None = None, label: str | None = None
        ) -> None:

            requests = list[Request]()
            user_data = user_data if user_data else {}

            for item in items:
                link_user_data = user_data.copy()

                if label is not None:
                    link_user_data.setdefault('label', label)

                if link_user_data.get('label') == 'SEARCH':
                    link_user_data['location'] = item

                url = self._base_url + path_template.format(item=item, **user_data)
                requests.append(Request.from_url(url, user_data=link_user_data))

            await context.add_requests(requests)

        yield CustomContext(
            request=context.request,
            session=context.session,
            proxy_info=context.proxy_info,
            enqueue_links=enqueue_links,
            add_requests=context.add_requests,
            send_request=context.send_request,
            push_data=context.push_data,
            log=context.log,
            http_response=context.http_response,
            page_data=page_data,
        )
```

As you can see, if the server response comes in HTML, we get the `build_id` using a simple regular expression. This condition should be executed once for the first link and is necessary to interact further with the Next.js API. In all other cases, we simply convert JSON to a Python `dict` and save it in the context.

In `enqueue_links`, I create logic for generating links based on string templates and input parameters.

That's it: our custom Crawler Class for Crawlee for Python is ready, it's based on the `CurlImpersonateHttpClient` client, works with JSON responses instead of HTML, and implements the link generation logic we need.

Let's finalize it by defining public classes for import.

```
# init.py

from .custom_crawler import CustomCrawler
from .types import CustomContext

__all__ = ['CustomCrawler', 'CustomContext']
```

Now that we have the crawler functionality, let's implement routing and data extraction from the site. We'll use the [`official documentation`](https://www.crawlee.dev/python/docs/introduction/refactoring) as a template.

```
# router.py

from crawlee.router import Router

from .constants import LISTING_PATH, SEARCH_PATH, TARGET_LOCATIONS
from .custom_crawler import CustomContext

router = Router[CustomContext]()


@router.default_handler
async def default_handler(context: CustomContext) -> None:
    """Handle the start URL to get the Build ID and create search links."""
    context.log.info(f'default_handler is processing {context.request.url}')

    await context.enqueue_links(
        path_template=SEARCH_PATH, items=TARGET_LOCATIONS, label='SEARCH', user_data={'page': 1}
    )


@router.handler('SEARCH')
async def search_handler(context: CustomContext) -> None:
    """Handle the SEARCH URL generates links to listings and to the next search page."""
    context.log.info(f'search_handler is processing {context.request.url}')

    max_pages = context.page_data['pageProps']['initialPageCount']
    current_page = context.request.user_data['page']
    if current_page < max_pages:

        await context.enqueue_links(
            path_template=SEARCH_PATH,
            items=[context.request.user_data['location']],
            label='SEARCH',
            user_data={'page': current_page + 1},
        )
    else:
        context.log.info(f'Last page for {context.request.user_data["location"]} location')

    listing_ids = [
        listing['property']['id']
        for group in context.page_data['pageProps']['initialListings']['groups']
        for listing in group['results']
        if listing.get('property')
    ]

    await context.enqueue_links(path_template=LISTING_PATH, items=listing_ids, label='LISTING')


@router.handler('LISTING')
async def listing_handler(context: CustomContext) -> None:
    """Handle the LISTING URL extracts data from the listings and saving it to a dataset."""
    context.log.info(f'listing_handler is processing {context.request.url}')

    listing_data = context.page_data['pageProps']['viewModel']['propertyDetails']
    if not listing_data['exists']:
        context.log.info(f'listing_handler, data is not available for url {context.request.url}')
        return
    property_data = {
        'property_id': listing_data['id'],
        'property_type': listing_data['propertyType'],
        'location_latitude': listing_data['coordinates']['lat'],
        'location_longitude': listing_data['coordinates']['lng'],
        'address1': listing_data['address']['address1'],
        'address2': listing_data['address']['address2'],
        'city': listing_data['address']['city'],
        'postcode': listing_data['address']['postcode'],
        'bills_included': listing_data.get('terms', {}).get('billsIncluded'),
        'description': listing_data.get('description'),
        'bathrooms': listing_data.get('numberOfBathrooms'),
        'number_rooms': len(listing_data['rooms']) if listing_data.get('rooms') else None,
        'rent_ppw': listing_data.get('terms', {}).get('rentPpw', {}).get('value', None),
    }

    await context.push_data(property_data)
```

Let's define our `main` function, which will launch the crawler.

```
# main.py

from .custom_crawler import CustomCrawler
from .router import router


async def main() -> None:
    """The main function that starts crawling."""
    crawler = CustomCrawler(max_requests_per_crawl=50, request_handler=router)

    # Run the crawler with the initial list of URLs.
    await crawler.run(['https://www.accommodationforstudents.com/'])

    await crawler.export_data('results.json')
```

Let's look at the results.

![Final results file](/assets/images/final-results-f14b378f9aa0cbd5d1185301c49a222e.webp)

As I prefer to manage my projects as packages and use `pyproject.toml` according to [PEP 518](https://peps.python.org/pep-0518/), the final structure of our project will look like this.

![PEP 518 file structure](data:image/webp;base64,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)

## Conclusion[​](#conclusion "Direct link to Conclusion")

In this project, we went through the entire cycle of crawler development, from analyzing a rather interesting dynamic site to full implementation of a crawler using `Crawlee for Python`. You can view the full project code on [GitHub](https://github.com/Mantisus/crawlee_python_example)

I would also like to hear your comments and thoughts on the web scraping topic you'd like to see in the next article. Feel free to comment here in the article or contact me in the [Crawlee developer community](https://apify.com/discord) on Discord.

If you are looking out to how to start scraping using Crawlee for Python, check out our [latest tutorial here](https://blog.apify.com/crawlee-for-python-tutorial/).

You can find me on the following platforms: [Github](https://github.com/Mantisus), [Linkedin](https://www.linkedin.com/in/max-bohomolov/), [Apify](https://apify.com/mantisus), [Upwork](https://www.upwork.com/freelancers/mantisus), [Contra](https://contra.com/mantisus).

Thank you for your attention. I hope you found this information useful.

**Tags:**

* [community](https://crawlee.dev/blog/tags/community.md)
