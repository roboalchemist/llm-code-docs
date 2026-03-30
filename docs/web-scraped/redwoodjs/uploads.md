# Source: https://docs.redwoodjs.com/docs/uploads

-   [![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMjQgMjQiIGNsYXNzPSJicmVhZGNydW1iSG9tZUljb25fWU5GVCI+PHBhdGggZD0iTTEwIDE5di01aDR2NWMwIC41NS40NSAxIDEgMWgzYy41NSAwIDEtLjQ1IDEtMXYtN2gxLjdjLjQ2IDAgLjY4LS41Ny4zMy0uODdMMTIuNjcgMy42Yy0uMzgtLjM0LS45Ni0uMzQtMS4zNCAwbC04LjM2IDcuNTNjLS4zNC4zLS4xMy44Ny4zMy44N0g1djdjMCAuNTUuNDUgMSAxIDFoM2MuNTUgMCAxLS40NSAxLTF6IiBmaWxsPSJjdXJyZW50Q29sb3IiPjwvcGF0aD48L3N2Zz4=)](/)
-   [Reference](/docs/index)
-   [Uploads & Storage]

[Version: 8.8]

On this page

<div>

# Uploads & Storage

</div>

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTYgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTguODkzIDEuNWMtLjE4My0uMzEtLjUyLS41LS44ODctLjVzLS43MDMuMTktLjg4Ni41TC4xMzggMTMuNDk5YS45OC45OCAwIDAgMCAwIDEuMDAxYy4xOTMuMzEuNTMuNTAxLjg4Ni41MDFoMTMuOTY0Yy4zNjcgMCAuNzA0LS4xOS44NzctLjVhMS4wMyAxLjAzIDAgMCAwIC4wMS0xLjAwMkw4Ljg5MyAxLjV6bS4xMzMgMTEuNDk3SDYuOTg3di0yLjAwM2gyLjAzOXYyLjAwM3ptMC0zLjAwNEg2Ljk4N1Y1Ljk4N2gyLjAzOXY0LjAwNnoiPjwvcGF0aD48L3N2Zz4=)]Experimental

The storage and upload functionality is currently experimental.

While we believe this feature will be included in the framework the interface is currently subject to significant change. Breaking changes will be made in minor and patch releases until the feature is released as stable after which normal SemVer rules will apply.

We\'d love to hear any feedback you might have on our [community forum](https://community.redwoodjs.com/).

Getting started with file uploads can open up a world of possibilities for your application. Whether you\'re enhancing user profiles with custom avatars, allowing document sharing, or enabling image galleries - Redwood has an integrated way of uploading files and storing them.

There are two parts to this:

1.  Setting up the frontend and GraphQL schema to send and receive files - Uploads
2.  Manipulate the data inside services, and pass it to Prisma, for persistence - Storage

We can roughly breakdown the flow as follows

![Redwood Uploads Flow Diagram](/assets/images/uploads-flow-292740e9b9ccb448c6d2d9654080d50e.png)

## Uploading Files[​](#uploading-files "Direct link to Uploading Files") 

### 1. Setting up the File scalar[​](#1-setting-up-the-file-scalar "Direct link to 1. Setting up the File scalar") 

Before we start sending files via GraphQL we need to tell Redwood how to handle them. Redwood and GraphQL Yoga are pre-configured to handle the `File` scalar.

In your mutations, use the `File` scalar for the fields where you are submitting an upload

api/src/graphql/profiles.sdl.ts

``` 
input UpdateProfileInput 
```

You\'re now ready to receive files!

### 2. Configuring the UI[​](#2-configuring-the-ui "Direct link to 2. Configuring the UI") 

Assuming you\'ve built a [Form](/docs/forms) for your profile let\'s add a `FileField` to it.

web/src/components/ProfileForm.tsx

``` 
import  from '@redwoodjs/forms'

export const ProfileForm = () => >
      <Label name="firstName" /*...*/ >
        First name
      </Label>
      <TextField name="firstName" /*...*/ />
      <FieldError name="firstName"  />

      <Label name="lastName" /*...*/ >
        Last name
      </Label>
      <TextField name="lastName" /*...*/ />
      <FieldError name="lastName"  />

      <FileField name="avatar" /*...*/ />
    </Form>
  }
}
```

A `FileField` is just a standard `<input type="file">` - that\'s integrated with your Form context - it just makes it easier to extract the data for submission.

Now we need to send the file as a mutation!

web/src/components/EditProfile.tsx

``` 
import  from '@redwoodjs/web'

const UPDATE_PROFILE_MUTATION = gql`
  // This is the Input type we setup with File earlier!
  mutation UpdateProfileMutation($input: UpdateProfileInput!) 
  }
`

const EditProfile = () => ] = useMutation(
    UPDATE_PROFILE_MUTATION,
    
  )

  const onSave = (formData: UpdateProfileInput) => 

    updateProfile( })
  }

  return (
    <ProfileForm
      profile=
      onSave=
      error=
      loading=
    />
  )
}
```

While [multi-file uploads are possible](#saving-file-lists---savefilesinlist), when our example form is submitted we process the data to ensure the avatar field contains a single file instead of an array (because that\'s how we setup the UpdateProfileInput). The onSave function then calls the updateProfile mutation. The mutation automatically handles the file upload because we\'ve set up the File scalar and configured our backend to process file inputs.

### 3. Logging the Item Details[​](#3-logging-the-item-details "Direct link to 3. Logging the Item Details") 

Try uploading your avatar photo now, and if you log the `avatar` field in your service:

api/src/services/profiles/profiles.ts

``` 
export const updateProfile = async () => 

  // Example without using the built-in helpers
  await fs.writeFile(
    '/test/profile.jpg',
    Buffer.from(await input.avatar.arrayBuffer())
  )
}
```

You\'ll see that you are receiving an instance of [File](https://developer.mozilla.org/en-US/docs/Web/API/File).

That\'s part 1 done - you can receive uploaded files. In the next steps, we\'ll talk about some tooling and a Prisma client extension that Redwood gives you, to help you persist and manage your uploads.

**What\'s happening behind the scenes?**

<div>

Once you send the request, and open up your Network Inspect Panel, you\'ll notice that the graphql request looks slightly different - it has a different Content-Type (instead of the regular `application/json`).

That\'s because when you send a [File](https://developer.mozilla.org/en-US/docs/Web/API/File) - the Redwood Apollo client will switch the request to a multipart form request, using [GraphQL Multipart Request Spec](https://github.com/jaydenseric/graphql-multipart-request-spec). This is the case whether you send a `File`, `FileList` or `Blob` (which is a less specialized File).

On the backend, GraphQL Yoga is pre-configured to handle multipart form requests, *as long as* you specify the `File` scalar in your SDL.

</div>

## Storage[​](#storage "Direct link to Storage") 

Great, now you can receive Files from GraphQL - but how do you go about saving them to disk, while also tracking them in your database? Well, Redwood has the answers for you! Keep going to find out how!

### 1. Configuring the Prisma schema[​](#1-configuring-the-prisma-schema "Direct link to 1. Configuring the Prisma schema") 

In your Prisma schema, the `avatar` field should be defined as a string:

api/db/schema.prisma

``` 
model Profile 
```

This is because Prisma doesn\'t have a native File type. Instead, we store the file path or URL as a string in the database. The actual file processing and storage will be handled in your service layer, and then the path to the uploaded file is passed to Prisma to save.

### 2. Configuring the Upload savers and Uploads extension[​](#2-configuring-the-upload-savers-and-uploads-extension "Direct link to 2. Configuring the Upload savers and Uploads extension") 

To make it easier (and more consistent) dealing with file uploads, Redwood gives you a standardized way of saving your uploads (i.e. write to storage) by using what we call \"savers,\" along with our custom Uploads extension that will handle deletion and updates automatically for you.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

The rest of the doc assumes you are running a \"Serverful\" configuration for your deployments, as it involves the file system.

Let\'s first run the setup command:

``` 
yarn rw setup uploads
```

This will do three things:

1.  Generate a configuration file in `api/src/lib/uploads.ts`
2.  Configure your Prisma client with the storage extension
3.  Generate a `signedUrl` function

Let\'s break down the key components of the configuration.

api/src/lib/uploads.ts

``` 
import  from '@redwoodjs/storage'
import  from '@redwoodjs/storage/FileSystemStorage'
import  from '@redwoodjs/storage/signedUrl'

// ⭐ (1)
const uploadConfig = createUploadsConfig(,
})

// ⭐ (2)
export const fsStorage = new FileSystemStorage()

// ⭐ (3) Optional
export const urlSigner = new UrlSigner()

// ⭐ (4)
const  = setupStorage()

export 
```

**1. Upload Configuration** This is where you configure the fields that will receive uploads. In our case, it\'s the `profile.avatar` field.

The shape of the config looks like this:

``` 
[prismaModel] : 
```

**2. Storage Adapter** We create a storage adapter, in this case `FileSystemStorage`, that will save your uploads to the `./uploads` folder.

This just sets the base path. The actual filenames and folders are determined by the saveFiles utility functions, but [can be overridden!](#customizing-save-file-name-or-save-path)

**3. Url Signer instance** This is an optional class that will help you generate signed urls for your files, so you can limit access to these files. Generate a secret with `yarn rw g secret` and add to your .env as `UPLOADS_SECRET`.

**4. Utility Functions** We provide utility functions that can be exported from this file to be used elsewhere, such as services.

-   `saveFiles` - object containing functions to save File objects to storage, and return a path. For example:

``` 
saveFiles.forProfile(gqlInput)
```

-   `storagePrismaExtension` - The Prisma client extension we\'ll use in `api/src/lib/db.ts` to automatically handle updates, deletion of uploaded files (including when the Prisma operation fails). It also configures [Result extensions](https://www.prisma.io/docs/orm/prisma-client/client-extensions/result), to give you utilities like `profile.withSignedUrl()`.

### 3. Attaching the Uploads extension[​](#3-attaching-the-uploads-extension "Direct link to 3. Attaching the Uploads extension") 

Now we need to extend our db client in `api/src/lib/db.ts` to use the configured prisma client.

api/src/lib/db.ts

``` 
import  from '@prisma/client'

import  from '@redwoodjs/api/logger'

import  from './logger'
import  from './uploads'

// 👇 Notice here we create prisma client, but don't export it yet
const prismaClient = new PrismaClient()

handlePrismaLogging()

// 👇 Export db after adding uploads extension
export const db = prismaClient.$extends(storagePrismaExtension)
```

The `$extends` method is used to extend the functionality of your Prisma client by adding

-   [Query extensions](https://www.prisma.io/docs/orm/prisma-client/client-extensions/query) which will intercept your `create`, `update`, `delete` operations\
-   [Result extensions](https://www.prisma.io/docs/orm/prisma-client/client-extensions/result) for your stored files - which gives you helper methods on the result of your prisma query

More details on these extensions can be found [here](#storage-prisma-extension).

**Why Export This Way**

<div>

The `$extends` method returns a new instance of the Prisma client with the extensions applied. By exporting this new instance as `db`, you ensure that any additional functionality provided by the uploads extension is available throughout your application, without needing to change where you import. Note one of the [limitations](https://www.prisma.io/docs/orm/prisma-client/client-extensions#limitations) of using extensions is if you have to use `$on` on your prisma client (as we do in handlePrismaLogging), it needs to happen before you use `$extends`

</div>

### 4. Implementing Upload savers[​](#4-implementing-upload-savers "Direct link to 4. Implementing Upload savers") 

You\'ll also need a way to actually save the incoming `File` object to a file persisted on storage. In your services, you can use the pre-configured \"savers\" to write your `File` objects to storage. Prisma will automatically save the path into the database. The savers and storage adapters, configured in `api/src/lib/uploads`, determine where the file is saved.

api/src/services/profiles/profiles.ts

``` 
import  from 'src/lib/uploads'

export const updateProfile: MutationResolvers['updateProfile'] = async () => ,
  })
}
```

For each of the models you configured when you setup uploads (in `UploadConfig`) - you have savers for them.

So if you passed:

``` 
const uploadConfig = createUploadsConfig(,
  anotherModel: ,
})

const  = setupStorage(uploadConfig)

// Available methods 👇
saveFiles.forProfile(profileGqlInput)
saveFiles.forAnotherModel(anotherModelGqlInput)

// Special case - not mapped to prisma model
saveFiles.inList(arrayOfFiles)
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTcgMi4zYzMuMTQgMCA1LjcgMi41NiA1LjcgNS43cy0yLjU2IDUuNy01LjcgNS43QTUuNzEgNS43MSAwIDAgMSAxLjMgOGMwLTMuMTQgMi41Ni01LjcgNS43LTUuN3pNNyAxQzMuMTQgMSAwIDQuMTQgMCA4czMuMTQgNyA3IDcgNy0zLjE0IDctNy0zLjE0LTctNy03em0xIDNINnY1aDJWNHptMCA2SDZ2Mmgydi0yeiI+PC9wYXRoPjwvc3ZnPg==)]info

You might have already noticed that the saver functions sort-of tie your GraphQL inputs to your Prisma model.

In essence, these utility functions expect to take an object very similar to the Prisma data argument (the data you\'re passing to your `create`, `update`), but with File objects at fields `avatar`, and `document` instead of strings.

If your `File` is in a different key (or a key you did not configure in the upload config), it will be ignored and left as-is.

## Informational/Utilities[​](#informationalutilities "Direct link to Informational/Utilities") 

## Storage Prisma Extension[​](#storage-prisma-extension "Direct link to Storage Prisma Extension") 

This Prisma extension is designed to handle file uploads and deletions in conjunction with database operations. The goal here is for you as the developer to not have to think too much in terms of files, rather just as Prisma operations. The extension ensures that file uploads are properly managed alongside database operations, preventing orphaned files and maintaining consistency between the database and the storage.

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiI+PC9wYXRoPjwvc3ZnPg==)]note

The extension will *only* operate on fields and models configured in your `UploadConfig` which you configure in [`api/src/lib/uploads.ts`](#2-configuring-the-upload-savers-and-uploads-extension).

What this configures is:

**A) CRUD operations**

-   when the record is deleted, the associated upload is removed from storage
-   when a record is updated, the associated upload file is also replaced

\...and negative cases such as:

-   saved uploads are removed if creation fails
-   saved uploads are removed if update fails (while keeping the original)

### `create` & `createMany` operations[​](#create--createmany-operations "Direct link to create--createmany-operations") 

If your create operation fails, it removes any uploaded files to avoid orphaned files (so you can retry the request)

### `update` & `updateMany` operations[​](#update--updatemany-operations "Direct link to update--updatemany-operations") 

1.  If update operation is successful, removes the old uploaded files
2.  If it fails, removes any newly uploaded files (so you can retry the request)

### `delete` operations[​](#delete-operations "Direct link to delete-operations") 

Removes any associated uploaded files, once delete operation completes.

### `upsert` operations[​](#upsert-operations "Direct link to upsert-operations") 

Depending on whether it\'s updating or creating, performs the same actions as create or update.

## Result Extensions[​](#result-extensions "Direct link to Result Extensions") 

When you add the storage prisma extension, it also configures your prisma objects to have special helper methods.

These will only appear on fields that you configure in your `UploadConfig`.

``` 
const profile = await db.profile.update(/*...*/)

// The result of your prisma query contains the helpers
profile?.withSignedUrl() // ✅

// Incorrect: you need to await the result of your prisma query first!
db.profile.update(/*...*/).withSignedUrl() // 🛑

// Assuming the comment model does not have an upload field
// the helper won't appear
db.comment.findMany(/*..*/).withSignedUrl() // 🛑
```

**B) Result extensions**

api/src/services/profiles/profiles.ts

``` 
export const profile = async () => ,
  })

  // Convert the avatar field (which was persisted as a path) to data uri string
  return profile?.withDataUri()
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6Ij48L3BhdGg+PC9zdmc+)]tip

It\'s very important to note limitations around what Prisma extensions can do:

**a) The CRUD operation extensions will not run on nested read and write operations**\
For example:

``` 
const savedFiles = saveFiles.inList(input.files)

db.folder.update(,
    },
  },
  where: ,
})
```

**b) Result extensions are not available on relations.**

You can often rewrite the query in a different way though. For example, when looking up files :

``` 
const filesViaRelation = await db.folder
  .findUnique( })
  .files()

const filesWhereQuery = await db.file.findMany(,
})

// 🛑 Will not work, because files accessed via relation
return filesViaRelation.map((file) => file.withSignedUrl())

// ✅ OK, because direct lookup
return filesWhereQuery.map((file) => file.withSignedUrl())
```

### Saving File lists - `saveFiles.inList()`[​](#saving-file-lists---savefilesinlist "Direct link to saving-file-lists---savefilesinlist") 

If you would like to upload FileLists (or an arrays of Files), use this special utility to persist your Files to storage. This is necessary because String arrays aren\'t supported on databases - you probably want to save them to a different table, or specific fields.

Let\'s say you define in your SDL, a way to send an Array of files.

``` 
input UpdateAlbumInput 
```

You can use the `.inList` function like this:

api/src/services/albums.ts

``` 
export const updateAlbum = async () => ))
  /* Will make `mappedPhotos` be an array of objects like this:
  [
    ,
    ,
  ]
  */

  return db.album.update(,
      },
    },
    where: ,
  })
```

### Customizing save file name or save path[​](#customizing-save-file-name-or-save-path "Direct link to Customizing save file name or save path") 

If you\'d like to customize the filename that a saver will write to you can override it when calling it. For example, you could name your files by the User\'s id

``` 
await saveFiles.forProfile(data, )

// Will save files to
// /base_path/profilePhoto-58xx4ruv41f8eit0y25.png
```

If you\'d like to customize where files are saved, perhaps you want to put it in a specific folder, so you can make those files [publicly available](#making-a-folder-public), you can override the folder to use too (skipping the base path of your Storage adapter):

``` 
await saveFiles.forProfile(data, )

// Will save files to
// /public_avatar/profilePhoto-58xx4ruv41f8eit0y25.png
```

The extension is determined by the name of the uploaded file.

### Signed URLs[​](#signed-urls "Direct link to Signed URLs") 

When you setup uploads, we also generate an API function (an endpoint) for you - by default at `/signedUrl`. You can use this in conjunction with the `.withSignedUrl` helper. For example:

api/src/services/profiles/profiles.ts

``` 
import  from '@redwoodjs/storage/UrlSigner'

export const profile = async () => ,
  })

  // Convert the avatar field to signed URLs
  return profile?.withSignedUrl()
}
```

The object being returned will look like:

``` 

```

This will generate a URL that will expire in 2 days (from the point of query). Let\'s breakdown the URL:

URL Component

`/.redwood/functions/signedUrl`

Point to the API server, and the endpoint configured

`s=s1gnatur3`

The signature that we\'ll validate

`expiry=1725190749613`

Time stamp for when it expires

`path=path.png`

The key to look up the file on your storage

How the signedUrl function validates

<div>

This function is automatically generated for you, but let\'s take a quick look at how it works:

api/src/functions/signedUrl/signedUrl.ts

``` 
import type  from '@redwoodjs/storage/UrlSigner'

// The urlSigner and fsStorage instances were configured when we setup uploads
import  from 'src/lib/uploads'

export const handler = async (event) => 
    event.queryStringParameters as SignatureValidationArgs
  )

  // Use the returned value to lookup the file in your storage
  const  = await fsStorage.read(fileToReturn)

  return ,
    // Return the contents of the file
    body: contents,
  }
}
```

We created and exported the `urlSigner` instance and `fsStorage` adapter in `src/lib/uploads`.

The details to validate come through as query parameters, which we pass to the `urlSigner.validateSignature` parameter.

If it\'s valid, you will receive a path (or key) to the file - which you can then lookup in your storage.

The `read` function also returns the mime-type of the file (based on the extension) - which you pass as a response header. This ensures that browsers know how to read your response!

</div>

### Data URIs[​](#data-uris "Direct link to Data URIs") 

When you have smaller files, you can choose instead to return a Base64 DataURI string that you can render directly into your html.

api/src/services/profiles.ts

``` 
export const profile = async () => ,
  })

  return profile?.withDataUri()
}
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTIgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuNSAwQzMuNDggMCAxIDIuMTkgMSA1YzAgLjkyLjU1IDIuMjUgMSAzIDEuMzQgMi4yNSAxLjc4IDIuNzggMiA0djFoNXYtMWMuMjItMS4yMi42Ni0xLjc1IDItNCAuNDUtLjc1IDEtMi4wOCAxLTMgMC0yLjgxLTIuNDgtNS01LjUtNXptMy42NCA3LjQ4Yy0uMjUuNDQtLjQ3LjgtLjY3IDEuMTEtLjg2IDEuNDEtMS4yNSAyLjA2LTEuNDUgMy4yMy0uMDIuMDUtLjAyLjExLS4wMi4xN0g1YzAtLjA2IDAtLjEzLS4wMi0uMTctLjItMS4xNy0uNTktMS44My0xLjQ1LTMuMjMtLjItLjMxLS40Mi0uNjctLjY3LTEuMTFDMi40NCA2Ljc4IDIgNS42NSAyIDVjMC0yLjIgMi4wMi00IDQuNS00IDEuMjIgMCAyLjM2LjQyIDMuMjIgMS4xOUMxMC41NSAyLjk0IDExIDMuOTQgMTEgNWMwIC42Ni0uNDQgMS43OC0uODYgMi40OHpNNCAxNGg1Yy0uMjMgMS4xNC0xLjMgMi0yLjUgMnMtMi4yNy0uODYtMi41LTJ6Ij48L3BhdGg+PC9zdmc+)]tip

The `withDataUri` extension is an `async` function. Remember to await, if you are doing additional manipulation before returning your result object from the service.

The output of `withDataUri` would be your profile object, with the upload fields transformed into a data uri. For example:

``` 

```

## Storage Adapters[​](#storage-adapters "Direct link to Storage Adapters") 

Storage adapters are crucial for abstracting the underlying storage mechanism, allowing for flexibility in how files are managed. The BaseStorageAdapter defines a standard interface for all storage adapters, and looks like this:

``` 
export abstract class BaseStorageAdapter 

  getAdapterOptions() 

  generateFileNameWithExtension(
    saveOpts: SaveOptionsOverride | undefined,
    file: File
  ) 

  abstract save(
    file: File,
    saveOpts?: SaveOptionsOverride
  ): Promise<AdapterResult>

  abstract remove(fileLocation: AdapterResult['location']): Promise<void>

  abstract read(fileLocation: AdapterResult['location']): Promise<>
}
```

Types of Storage Adapters MemoryStorage: This adapter stores files in memory, making it ideal for temporary storage needs or testing scenarios. It offers faster access times but does not persist data across application restarts.

We build in two storage adapters:

-   [FileSystemStorage](https://github.com/redwoodjs/redwood/blob/main/packages/storage/src/adapters/FileSystemStorage/FileSystemStorage.ts) - This adapter interacts with the file system, enabling the storage of files on disk.
-   [MemoryStorage](https://github.com/redwoodjs/redwood/blob/main/packages/storage/src/adapters/MemoryStorage/MemoryStorage.ts) - this adapter stores files in memory, making it ideal for temporary storage needs or testing scenarios. It offers faster access times but does not persist data across application restarts.

## Configuring the server further[​](#configuring-the-server-further "Direct link to Configuring the server further") 

Sometimes, you may need more control over how the Redwood API server behaves. This could include customizing the body limit for requests, redirects, or implementing additional logic - that\'s exactly what the [Server File](/docs/server-file) is for!

### Making a folder public[​](#making-a-folder-public "Direct link to Making a folder public") 

While you can always create a function to access certain files publicly, similar to the `/signedUrl` function that gets generated for you - another way could be to configure the API server with the [fastify-static](https://github.com/fastify/fastify-static) plugin to make a specific folder publicly accessible.

api/server.js

``` 
import path from 'path'
import fastifyStatic from '@fastify/static'

import  from '@redwoodjs/api-server'
import  from 'src/lib/logger'

async function main() )

  server.register(fastifyStatic, )

  await server.start()
}

main()
```

Based on the above, you\'ll be able to access your files at:

`http://localhost:8910/.redwood/functions/public_uploads/01J6AF89Y89WTWZF12DRC72Q2A.jpeg`

OR directly

`http://localhost:8911/public_uploads/01J6AF89Y89WTWZF12DRC72Q2A.jpeg`

Where you are only exposing **part** of your uploads directory publicly

In your web side code you can construct the URL like this:

``` 
const publicUrl = `$/$`
```

### Customizing the body limit for requests[​](#customizing-the-body-limit-for-requests "Direct link to Customizing the body limit for requests") 

The default body size limit for the Redwood API server is 100MB (per request). Depending on the sizes of files you\'re uploading, especially in the case of multiple files, you may receive errors like this:

``` 

```

You can configure the `bodyLimit` option to increase or decrease the default limit.

api/server.js

``` 
import  from '@redwoodjs/api-server'

import  from 'src/lib/logger'

async function main() ,
  })

  await server.start()
}

main()
```

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6Ij48L3BhdGg+PC9nPjwvc3ZnPg==)Edit the latest version of this page](https://github.com/redwoodjs/graphql/blob/main/docs/docs/uploads.md)