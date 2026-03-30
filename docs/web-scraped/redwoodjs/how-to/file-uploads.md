# Source: https://docs.redwoodjs.com/docs/how-to/file-uploads

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [How To](/docs/how-to/index)
-   [File Uploads]

[Version: 8.8]

On this page

<div>

# File Uploads

</div>

As you\'ve probably heard, Redwood thinks the future is serverless. This concept introduces some interesting problems you might not have had to worry about in the past. For example, where do files go when you upload them? There\'s no server! Like many tasks you may have done [yourself](/docs/tutorial/chapter4/authentication) in the past, this is another job that we can farm out to a third-party service.

## The Service[​](#the-service "Direct link to The Service") 

There are many services out there that handle uploading files and serving them from a CDN. Two of the big ones are [Cloudinary](https://cloudinary.com) and [Filestack](https://filestack.com). We\'re going to demo a Filestack integration here because we\'ve found it easy to integrate. In addition to storing your uploads and making them available via a CDN, they also offer on-the-fly image transformations so that even if someone uploads a Retina-ready 5000px wide headshot, you can shrink it down and only serve a 100px version for their avatar in the upper right corner of your site. You save bandwidth and transfer costs.

We\'re going to sign up for a free plan which gives us 100 uploads a month, 1000 transformations (like resizing an image), 1GB of bandwidth, and 0.5GB of storage. That\'s more than enough for this demo. (And maybe even a low-traffic production site!)

Head over to [https://dev.filestack.com/signup/free/](https://dev.filestack.com/signup/free/) and sign up. Be sure to use a real email address because they\'re going to send you a confirmation email before they let you log in. Once you verify your email, you\'ll be dropped on your dashboard where your API key will be shown in the upper right:

![New image scaffold](https://user-images.githubusercontent.com/300/82616735-ec41a400-9b82-11ea-9566-f96089e35e52.png)

Copy that (or at least keep the tab open) because we\'re going to need it in a minute. (I already changed that key so don\'t bother trying to steal it!)

That\'s it on the Filestack side; on to the application.

## The App[​](#the-app "Direct link to The App") 

Let\'s create a very simple DAM (Digital Asset Manager) that lets users upload and catalogue images. They\'ll be able to click the thumbnail to open a full-size version.

Create a new Redwood app:

``` 
yarn create redwood-app uploader
cd uploader
```

The first thing we\'ll do is create an environment variable to hold our Filestack API key. This is a best practice so that the key isn\'t living in our repository for prying eyes to see. Add the key to the `.env` file in the root of our app:

``` 
REDWOOD_ENV_FILESTACK_API_KEY=AM18i8xV4QpoiGwetoTWd
```

> We\'re prefixing with `REDWOOD_ENV_` here to tell Vite that we want it to replace this variables with its actual value as it\'s processing pages and statically generating them. Otherwise our generated pages would still contain something like `process.env.FILESTACK_API_KEY`, which wouldn\'t exist when the pages are static and being served from a CDN.

Now we can start our development server:

``` 
yarn rw dev
```

### The Database[​](#the-database "Direct link to The Database") 

We\'ll create a single model to store our image data:

api/db/schema.prisma

``` 
model Image 
```

`title` will be the user-supplied name for this asset and `url` will contain the public URL that Filestack creates after an upload.

Create a migration to update the database; when prompted, name it \"add image\":

``` 
yarn rw prisma migrate dev
```

To make our lives easier, let\'s scaffold the screens necessary to create/update/delete an image, then we\'ll worry about adding the uploader:

``` 
yarn rw generate scaffold image
```

Now head to [http://localhost:8910/images/new](http://localhost:8910/images/new) and let\'s figure this out!

![New image scaffold](https://user-images.githubusercontent.com/300/82694608-653f0b00-9c18-11ea-8003-4dc4aeac7b86.png)

## The Uploader[​](#the-uploader "Direct link to The Uploader") 

Filestack has a couple of [React components](https://github.com/filestack/filestack-react) that handle all the uploading for us. Let\'s add the package:

``` 
yarn workspace web add filestack-react
```

We want the uploader on our scaffolded form, so let\'s head over to `ImageForm`, import Filestack\'s inline picker, and try replacing the **Url** input with it:

web/src/components/ImageForm/ImageForm.js

``` 
import  from '@redwoodjs/forms'
import  from 'filestack-react'

const formatDatetime = (value) => \.\d\w/, '')
  }
}

const ImageForm = (props) => 

  return (
    <div className="rw-form-wrapper">
      <Form onSubmit= error=>
        <FormError
          error=
          wrapperClassName="rw-form-error-wrapper"
          titleClassName="rw-form-error-title"
          listClassName="rw-form-error-list"
        />

        <Label
          name="title"
          className="rw-label"
          errorClassName="rw-label rw-label-error"
        >
          Title
        </Label>
        <TextField
          name="title"
          defaultValue=
          className="rw-input"
          errorClassName="rw-input rw-input-error"
          validation=}
        />

        <FieldError name="title" className="rw-field-error" />

        <PickerInline apikey= />

        <div className="rw-button-group">
          <Submit disabled= className="rw-button rw-button-blue">
            Save
          </Submit>
        </div>
      </Form>
    </div>
  )
}

export default ImageForm
```

We now have a picker with all kinds of options, like picking a local file, providing a URL, and even grabbing a file from Facebook, Instagram, or Google Drive. Not bad!

![Filestack picker](https://user-images.githubusercontent.com/32992335/133859676-4086a4b9-8112-4a19-a4fe-5663388aafc0.png)

You can even try uploading an image to make sure it works:

![Upload](https://user-images.githubusercontent.com/300/82618035-bb636e00-9b86-11ea-9401-61b8c989f43c.png)

> Make sure you click the **Upload** button that appears after picking your file.

If you go over to the Filestack dashboard, you\'ll see that we\'ve uploaded an image:

![Filestack dashboard](https://user-images.githubusercontent.com/300/82618057-ccac7a80-9b86-11ea-9cd8-7a9e80a5a20f.png)

But that doesn\'t help us attach anything to our database record. Let\'s do that.

## The Data[​](#the-data "Direct link to The Data") 

Let\'s see what\'s going on when an upload completes. The Filestack picker takes an `onSuccess` prop with a function to call when complete:

web/src/components/ImageForm/ImageForm.js

``` 
// imports and stuff...

const ImageForm = (props) => 

  const onFileUpload = (response) => 

  // form stuff...

  <PickerInline
    apikey=
    onSuccess=
  />
```

Well lookie here:

![Uploader response](https://user-images.githubusercontent.com/300/82618071-ddf58700-9b86-11ea-9626-e093b4c8d853.png)

`filesUploaded[0].url` seems to be exactly what we need---the public URL to the image that was just uploaded. Excellent! How about we use a little state to track that for us so it\'s available when we submit our form:

web/src/components/ImageForm/ImageForm.js

``` 
import  from '@redwoodjs/forms'
import  from 'filestack-react'
import  from 'react'

const formatDatetime = (value) => \.\d\w/, '')
  }
}

const ImageForm = (props) => 

  const onFileUpload = (response) => 

  return (
    // component stuff...
```

So we\'ll use `setState` to store the URL for the image. We default it to the existing `url` value, if it exists---remember that scaffolds use this same form for editing of existing records, where we\'ll already have a value for `url`. If we didn\'t store that url value somewhere then it would be overridden with `null` if we started editing an existing record!

The last thing we need to do is set the value of `url` in the `data` object before it gets passed to the `onSave` handler:

web/src/components/ImageForm/ImageForm.js

``` 
const onSubmit = (data) => )
  props.onSave(dataWithUrl, props?.image?.id)
}
```

Now try uploading a file and saving the form:

![Upload done](https://user-images.githubusercontent.com/300/82702493-f5844c80-9c26-11ea-8fc4-0273b92034e4.png)

It worked! Next let\'s update the display here to actually show the image as a thumbnail and make it clickable to see the full version:

web/src/components/Images/Images.js

``` 
import  from '@redwoodjs/web'
import  from '@redwoodjs/web/toast'
import  from '@redwoodjs/router'

import  from 'src/components/Image/ImagesCell'

const DELETE_IMAGE_MUTATION = gql`
  mutation DeleteImageMutation($id: Int!) 
  }
`

const MAX_STRING_LENGTH = 150

const truncate = (text) => 
  return output
}

const jsonTruncate = (obj) => 

const timeTag = (datetime) =>  title=>
      
    </time>
  )
}

const checkboxInputTag = (checked) =>  disabled />
}

const ImagesList = () => ,
    // This refetches the query on the list page. Read more about other ways to
    // update the cache over here:
    // https://www.apollographql.com/docs/react/data/mutations/#making-all-other-cache-updates
    refetchQueries: [],
    awaitRefetchQueries: true,
  })

  const onDeleteClick = (id) =>  })
    }
  }

  return (
    <div className="rw-segment rw-table-wrapper-responsive">
      <table className="rw-table">
        <thead>
          <tr>
            <th>Id</th>
            <th>Title</th>
            <th>Url</th>
            <th>&nbsp;</th>
          </tr>
        </thead>
        <tbody>
          >
              <td></td>
              <td></td>
              <td>
                <a href= target="_blank">
                  <img src= style=} />
                </a>
              </td>
              <td>
                <nav className="rw-table-actions">
                  <Link
                    to=)}
                    title=
                    className="rw-button rw-button-small"
                  >
                    Show
                  </Link>
                  <Link
                    to=)}
                    title=
                    className="rw-button rw-button-small rw-button-blue"
                  >
                    Edit
                  </Link>
                  <button
                    type="button"
                    title=
                    className="rw-button rw-button-small rw-button-red"
                    onClick=
                  >
                    Delete
                  </button>
                </nav>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  )
}

export default ImagesList
```

![Image](https://user-images.githubusercontent.com/300/82702575-1fd60a00-9c27-11ea-8d2f-047bcf4e9cae.png)

## The Transform[​](#the-transform "Direct link to The Transform") 

Remember when we mentioned that Filestack can save you bandwidth by transforming images on the fly? This page is a perfect example---the image is never bigger than 50px, why pull down the full resolution just for that tiny display? Here\'s how we can tell Filestack that whenever we grab this instance of the image, it only needs to be 100px.

Why 100px? Most phones and many laptops and desktop displays are now 4k or larger. Images are actually displayed at at least double resolution on these displays, so even though it\'s \"50px\", it\'s really 100px when shown on these displays. So you\'ll usually want to bring down all images at twice their intended display resolution.

We need to add a special indicator to the URL itself to trigger the transform so let\'s add a function that does that for a given image URL (this can go either inside or outside of the component definition):

web/src/components/Images/Images.js

``` 
const thumbnail = (url) => 
```

What this does is turn a URL like

``` 
https://cdn.filestackcontent.com/81m7qIrURxSp7WHcft9a
```

into

``` 
https://cdn.filestackcontent.com/resize=width:100/81m7qIrURxSp7WHcft9a
```

Now we\'ll use the result of that function in the `<img>` tag:

web/src/components/Images/Images.js

``` 
<img src= style=} />
```

Starting with an uploaded image of 157kB, the 100px thumbnail clocks in at only 6.5kB! Optimizing image delivery is almost always worth the extra effort!

You can read more about the available transforms at [Filestack\'s API reference](https://www.filestack.com/docs/api/processing/).

## The Improvements[​](#the-improvements "Direct link to The Improvements") 

It\'d be nice if, after uploading, you could see the image you uploaded. Likewise, when editing an image, it\'d be helpful to see what\'s already attached. Let\'s make those improvements now.

We\'re already storing the attached image URL in state, so let\'s use the existence of that state to show the attached image. In fact, let\'s also hide the uploader and assume you\'re done (you\'ll be able to show it again if needed):

web/src/components/ImageForm/ImageForm.js

``` 
<PickerInline
  apikey=
  onSuccess=
>
  <div style=}></div>
</PickerInline>

 style=} />}
```

Now if you create a new image record, you\'ll see the picker, and as soon as the upload is complete, the uploaded image will pop into place. If you go to edit an image, you\'ll see the file that\'s already attached.

> You should probably use the same resize-URL trick here to make sure it doesn\'t try to display a 10MB image immediately after uploading it. A max width of 500px may be good\...

Now let\'s add the ability to bring back the uploader if you decide you want to change the image. We can do that by clearing the image that\'s in state:

web/src/components/ImageForm/ImageForm.js

``` 
<PickerInline
  apikey=
  onSuccess=
>
  <div style=}></div>
</PickerInline>

 style=} />
    <button
      onClick=
      className="rw-button rw-button-blue"
    >
      Replace Image
    </button>
  </div>
)}
```

![Replace image button](https://user-images.githubusercontent.com/300/82719274-e7055780-9c5d-11ea-9a8a-8c1c72185983.png)

We\'re borrowing the styles from the submit button and making sure that the image has both a top and bottom margin so it doesn\'t crash into the new button.

## The Delete[​](#the-delete "Direct link to The Delete") 

Having a free plan is great, but if you just load images and never actually remove the unnecessary ones, you\'ll be in trouble.

To avoid this, we\'d better implement the `deleteImage` mutation. It will enable you to make a call to the Filestack API to remove your resources and, on success, remove the row in the `Image` model.

You are going to need a new ENV var called `REDWOOD_ENV_FILESTACK_SECRET`, which you can find in **Filestack \> Security \> Policy & Signature:** App Secret. Put this into your `.env` file (don\'t use this one of course, paste your own in there):

.env

``` 
REDWOOD_ENV_FILESTACK_SECRET= PWRWGEKFZ2HJMXWSBP3YYI5ERZ
```

Filestack\'s library will provide a `getSecurity` method that will allow us to delete a resource, but only if executed on a **nodejs** environment. Hence, we need to execute the `delete` operation on the `api` side.

Let\'s add the proper package:

``` 
yarn workspace api add filestack-js
```

Great. Now we can modify our service accordingly:

api/src/services/image/image.ts

``` 
import * as Filestack from 'filestack-js'

export const deleteImage = async () =>  })

  // The `security.handle` is the unique part of the Filestack file's url.
  const handle = image.url.split('/').pop()

  const security = Filestack.getSecurity(
    ,
    process.env.REDWOOD_ENV_FILESTACK_SECRET
  )

  await client.remove(handle, security)

  return db.image.delete( })
}
```

Great! Now when you click the button in the frontend, the service will make a call to Filestack to remove the image from the service first. We set `expiry` to 20 seconds so that our policy expires 20 seconds after its generation, this is more than enough to protect your access while executing such operation.

Assuming the request to `remove()` the image succeeded, we then delete it locally. If you wanted to be extra safe you could surround the `remove()` call with a try/catch block and then throw your own error if Filestack ends up throwing an error.

## The Wrap-up[​](#the-wrap-up "Direct link to The Wrap-up") 

Files uploaded!

There\'s plenty of ways to integrate a file picker. This is just one, but we think it\'s simple, yet flexible. We use the same technique on the [example-blog](https://github.com/redwoodjs/example-blog).

Have fun and get uploading!

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/how-to/file-uploads.md)