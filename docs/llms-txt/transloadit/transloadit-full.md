# Transloadit Documentation

Source: https://transloadit.com/llms-full.txt

---

# Transloadit

> Transloadit is a versatile file uploading and processing API that allows developers to create complex media processing workflows through declarative JSON recipes called Assembly Instructions.

## Uploading and importing (INPUT)

Transloadit handles file uploads over XHR or tus.io (our open source protocol for resumable file uploads) and can process files through various "Robots" (specialized processing steps) that can be chained together to create customized workflows.

## Encoding workflows (PROCESS)

Assembly Instructions at a glance:

```json
{
  "steps": {
    ":original": {
      "robot": "/upload/handle"
    },
    "browser720_webm_encoded": {
      "use": ":original",
      "robot": "/video/encode",
      "preset": "webm",
      "width": 1280,
      "height": 720
    },
    "browser720_h264_encoded": {
      "use": ":original",
      "robot": "/video/encode",
      "preset": "mp4",
      "width": 1280,
      "height": 720
    },
    "thumbed": {
      "use": "browser720_h264_encoded",
      "robot": "/video/thumbs",
      "width": 1280,
      "height": 720,
      "format": "jpg",
      "resize_strategy": "fit",
      "count": 1,
    },
    "exported": {
      "use": ["browser720_webm_encoded", "browser720_h264_encoded", "thumbed", ":original"],
      "robot": "/s3/store",
      "credentials": "demo_s3_credentials",
      "url_prefix": "https://demos.transloadit.com/"
    }
  }
}
```

As you can see, our features are called Robots, and each Step inside
the Assembly Instructions can refer one. Robots can pass files to each other
with the `use` keyword. This means you can create complex workflows
unique to your application.

## Exporting to cloud storage or downloading results (OUTPUT)

Transloadit can export to all the major cloud storage providers.
Customers first need to store their credentials in their Transloadit account and
then refer to them in the Assembly Instructions.

Alternatively, Transloadit keeping 24h of temporary storage, you can directly download
resulting files when an Assembly is finished.

All meta data is available on a unique Assembly URL which contains the Assembly Status JSON.

## Example integration code with Node.js

```js
// npm install transloadit
const { Transloadit } = require('transloadit')

const transloadit = new Transloadit({
  authKey: 'TRANSLOADIT_KEY',
  authSecret: 'TRANSLOADIT_SECRET',
})

const options = {
  files: {
    file1: '/PATH/TO/FILE.jpg',
  },
  params: {
    steps: {
      // You can have many Steps. In this case we will just resize any inputs (:original)
      ':original': {
        robot: '/upload/handle',
      },
      resize: {
        use: ':original',
        robot: '/image/resize',
        result: true,
        width: 75,
        height: 75,
      },
    },
    // OR if you already created a template, you can use it instead of "steps":
    // template_id: 'YOUR_TEMPLATE_ID',
  },
  waitForCompletion: true, // Wait for the Assembly (job) to finish executing before returning
}

const status = await transloadit.createAssembly(options)
console.log('✅ Success - Your resized image:', status?.results?.resize?.[0]?.ssl_url)
```

## SDKs

- [Uppy](https://uppy.io/): Our open source browser UI for uploading files
- [Node.js SDK](https://github.com/transloadit/node-sdk): Official Node.js integration
- [Python SDK](https://github.com/transloadit/python-sdk): Official Python integration
- [Ruby SDK](https://github.com/transloadit/ruby-sdk): Official Ruby integration
- [All SDKs](https://transloadit.com/docs/sdks/): Complete list of available SDKs

## Robots

### Available Robots

- `/audio/artwork` - Extract or insert audio artwork
- `/audio/concat` - Concatenate audio
- `/audio/encode` - Encode audio
- `/audio/loop` - Loop audio
- `/audio/merge` - Merge audio files into one
- `/audio/waveform` - Generate waveform images from audio
- `/azure/import` - Import files from Azure
- `/azure/store` - Export files to Microsoft Azure
- `/backblaze/import` - Import files from Backblaze
- `/backblaze/store` - Export files to Backblaze
- `/cloudfiles/import` - Import files from Rackspace Cloud Files
- `/cloudfiles/store` - Export files to Rackspace Cloud Files
- `/cloudflare/import` - Import files from Cloudflare R2
- `/cloudflare/store` - Export files to Cloudflare R2
- `/digitalocean/import` - Import files from DigitalOcean Spaces
- `/digitalocean/store` - Export files to DigitalOcean Spaces
- `/document/autorotate` - Auto-rotate documents to the correct orientation
- `/document/convert` - Convert documents into different formats
- `/document/merge` - Merge documents into one
- `/document/ocr` - Recognize text in documents
- `/document/split` - Extract pages from a document
- `/document/thumbs` - Extract thumbnail images from documents
- `/dropbox/import` - Import files from Dropbox
- `/dropbox/store` - Export files to Dropbox
- `/edgly/deliver` - Cache and deliver files globally
- `/file/compress` - Compress files
- `/file/decompress` - Decompress archives
- `/file/filter` - Filter files
- `/file/hash` - Hash Files
- `/file/preview` - Generate a preview thumbnail
- `/file/read` - Read file contents
- `/file/serve` - Serve files to web browsers
- `/file/verify` - Verify the file type
- `/file/virusscan` - Scan files for viruses
- `/ftp/import` - Import files from FTP servers
- `/ftp/store` - Export files to FTP servers
- `/google/import` - Import files from Google Storage
- `/google/store` - Export files to Google Storage
- `/html/convert` - Take screenshots of webpages or uploaded HTML files
- `/http/import` - Import files from web servers
- `/image/bgremove` - Remove the background from images
- `/image/describe` - Recognize objects in images
- `/image/facedetect` - Detect faces in images
- `/image/generate` - Generate images from text prompts
- `/image/merge` - Merge several images into a single image
- `/image/ocr` - Recognize text in images
- `/image/optimize` - Optimize images without quality loss
- `/image/resize` - Convert, resize, or watermark images
- `/meta/write` - Write metadata to media
- `/minio/import` - Import files from MinIO
- `/minio/store` - Export files to MinIO
- `/s3/import` - Import files from Amazon S3
- `/s3/store` - Export files to Amazon S3
- `/script/run` - Run Scripts
- `/sftp/import` - Import files from SFTP servers
- `/sftp/store` - Export files to SFTP servers
- `/speech/transcribe` - Transcribe speech in audio or video files
- `/supabase/import` - Import files from Supabase
- `/supabase/store` - Export files to Supabase
- `/swift/import` - Import files from Openstack/Swift
- `/swift/store` - Export files to OpenStack Swift Spaces
- `/text/speak` - Speak text
- `/text/translate` - Translate text
- `/tigris/import` - No description available
- `/tigris/store` - No description available
- `/tlcdn/deliver` - Cache and deliver files globally
- `/tus/store` - Export files to Tus-compatible servers
- `/upload/handle` - Handle uploads
- `/video/adaptive` - Convert videos to HLS and MPEG-Dash
- `/video/concat` - Concatenate videos
- `/video/encode` - Transcode, resize, or watermark videos
- `/video/merge` - Merge video, audio, images into one video
- `/video/ondemand` - Stream videos with on-demand encoding
- `/video/subtitle` - Add subtitles to videos
- `/video/thumbs` - Extract thumbnails from videos
- `/vimeo/import` - Import videos from Vimeo
- `/vimeo/store` - Export files to Vimeo
- `/wasabi/import` - Import files from Wasabi
- `/wasabi/store` - Export files to Wasabi
- `/youtube/store` - Export files to YouTube

### Robot Parameter Schemas

#### Common Schemas

These schema definitions are shared across multiple robots:

```ts
const FfmpegSchema = z.object({
  ffmpeg: z
    .union([
      z.any(),
      z
        .object({
          af: z.union([z.any(), z.string()]).optional(),
          'b:a': z
            .union([
              z.any(),
              z.union([z.any(), z.string()]),
              z.union([
                z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                z.any(),
                z.number(),
              ]),
            ])
            .optional(),
          'b:v': z
            .union([
              z.any(),
              z.union([z.any(), z.string()]),
              z.union([
                z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                z.any(),
                z.number(),
              ]),
            ])
            .optional(),
          'c:a': z.union([z.any(), z.string()]).optional(),
          'c:v': z.union([z.any(), z.string()]).optional(),
          'codec:a': z.union([z.any(), z.string()]).optional(),
          'codec:v': z.union([z.any(), z.string()]).optional(),
          'filter:v': z.union([z.any(), z.string()]).optional(),
          'filter:a': z.union([z.any(), z.string()]).optional(),
          bits_per_mb: z
            .union([
              z.any(),
              z.union([z.any(), z.string()]),
              z.union([
                z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                z.any(),
                z.number(),
              ]),
            ])
            .optional(),
          ss: z
            .union([
              z.any(),
              z.union([z.any(), z.string()]),
              z.union([
                z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                z.any(),
                z.number(),
              ]),
            ])
            .optional(),
          t: z
            .union([
              z.any(),
              z.union([z.any(), z.string()]),
              z.union([
                z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                z.any(),
                z.number(),
              ]),
            ])
            .optional(),
          to: z
            .union([
              z.any(),
              z.union([z.any(), z.string()]),
              z.union([
                z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                z.any(),
                z.number(),
              ]),
            ])
            .optional(),
          vendor: z.union([z.any(), z.string()]).optional(),
          shortest: z
            .union([
              z.union([z.any(), z.union([z.boolean(), z.any()])]),
              z.null(),
            ])
            .optional(),
          filter_complex: z
            .union([
              z.any(),
              z.union([z.any(), z.string()]),
              z.record(z.union([z.any(), z.string()])),
            ])
            .optional(),
          'level:v': z
            .union([
              z.any(),
              z.union([z.any(), z.string()]),
              z.union([
                z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                z.any(),
                z.number(),
              ]),
            ])
            .optional(),
          'profile:v': z
            .union([
              z.any(),
              z.union([
                z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                z.any(),
                z.number(),
              ]),
              z.union([
                z.any(),
                z.enum(['baseline', 'main', 'high', 'main10']),
              ]),
            ])
            .optional(),
          'qscale:a': z
            .union([
              z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
              z.any(),
              z.number(),
            ])
            .optional(),
          'qscale:v': z
            .union([
              z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
              z.any(),
              z.number(),
            ])
            .optional(),
          'x264-params': z.union([z.any(), z.string()]).optional(),
          'overshoot-pct': z
            .union([
              z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
              z.any(),
              z.number(),
            ])
            .optional(),
          deadline: z.union([z.any(), z.string()]).optional(),
          'cpu-used': z.union([z.any(), z.string()]).optional(),
          'undershoot-pct': z
            .union([
              z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
              z.any(),
              z.number(),
            ])
            .optional(),
          'row-mt': z
            .union([
              z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
              z.any(),
              z.number(),
            ])
            .optional(),
          'x265-params': z
            .union([
              z.any(),
              z
                .object({
                  'vbv-maxrate': z
                    .union([
                      z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                      z.any(),
                      z.number(),
                    ])
                    .optional(),
                  'vbv-bufsize': z
                    .union([
                      z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                      z.any(),
                      z.number(),
                    ])
                    .optional(),
                  'rc-lookahead': z
                    .union([
                      z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                      z.any(),
                      z.number(),
                    ])
                    .optional(),
                  'b-adapt': z
                    .union([
                      z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                      z.any(),
                      z.number(),
                    ])
                    .optional(),
                })
                .strict(),
            ])
            .optional(),
          'svtav1-params': z
            .union([
              z.any(),
              z
                .object({
                  tune: z
                    .union([
                      z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                      z.any(),
                      z.number(),
                    ])
                    .optional(),
                  'enable-qm': z
                    .union([
                      z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                      z.any(),
                      z.number(),
                    ])
                    .optional(),
                  'fast-decode': z
                    .union([
                      z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                      z.any(),
                      z.number(),
                    ])
                    .optional(),
                  'film-grain-denoise': z
                    .union([
                      z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                      z.any(),
                      z.number(),
                    ])
                    .optional(),
                })
                .strict(),
            ])
            .optional(),
          ac: z
            .union([
              z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
              z.any(),
              z.number(),
            ])
            .optional(),
          an: z.union([z.any(), z.union([z.boolean(), z.any()])]).optional(),
          ar: z
            .union([
              z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
              z.any(),
              z.number(),
            ])
            .optional(),
          async: z
            .union([
              z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
              z.any(),
              z.number(),
            ])
            .optional(),
          b: z
            .union([
              z.any(),
              z.union([
                z.any(),
                z
                  .object({
                    v: z
                      .union([
                        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                        z.any(),
                        z.number(),
                      ])
                      .optional(),
                    a: z
                      .union([
                        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                        z.any(),
                        z.number(),
                      ])
                      .optional(),
                  })
                  .strict(),
              ]),
              z.union([z.any(), z.string()]),
            ])
            .optional(),
          bt: z
            .union([
              z.any(),
              z.union([
                z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                z.any(),
                z.number(),
              ]),
              z.union([z.any(), z.string()]),
            ])
            .optional(),
          bufsize: z
            .union([
              z.any(),
              z.union([z.any(), z.string()]),
              z.union([
                z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                z.any(),
                z.number(),
              ]),
            ])
            .optional(),
          c: z.union([z.any(), z.string()]).optional(),
          codec: z
            .union([
              z.any(),
              z
                .object({
                  v: z.union([z.any(), z.string()]).optional(),
                  a: z.union([z.any(), z.string()]).optional(),
                })
                .strict(),
            ])
            .optional(),
          coder: z
            .union([
              z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
              z.any(),
              z.number(),
            ])
            .optional(),
          crf: z
            .union([
              z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
              z.any(),
              z.number(),
            ])
            .optional(),
          f: z.union([z.any(), z.string()]).optional(),
          flags: z.union([z.any(), z.string()]).optional(),
          g: z
            .union([
              z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
              z.any(),
              z.number(),
            ])
            .optional(),
          i_qfactor: z
            .union([
              z.any(),
              z.union([z.any(), z.string()]),
              z.union([
                z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                z.any(),
                z.number(),
              ]),
            ])
            .optional(),
          keyint_min: z
            .union([
              z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
              z.any(),
              z.number(),
            ])
            .optional(),
          level: z
            .union([
              z.any(),
              z.union([z.any(), z.string()]),
              z.union([
                z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                z.any(),
                z.number(),
              ]),
            ])
            .optional(),
          map: z
            .union([
              z.any(),
              z.union([z.any(), z.string()]),
              z.union([z.any(), z.array(z.union([z.any(), z.string()]))]),
            ])
            .optional(),
          maxrate: z
            .union([
              z.any(),
              z.union([z.any(), z.string()]),
              z.union([
                z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                z.any(),
                z.number(),
              ]),
            ])
            .optional(),
          me_range: z
            .union([
              z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
              z.any(),
              z.number(),
            ])
            .optional(),
          movflags: z.union([z.any(), z.string()]).optional(),
          partitions: z.union([z.any(), z.string()]).optional(),
          pix_fmt: z.union([z.any(), z.string()]).optional(),
          preset: z
            .union([
              z.any(),
              z.union([z.any(), z.string()]),
              z.union([
                z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                z.any(),
                z.number(),
              ]),
            ])
            .optional(),
          profile: z.union([z.any(), z.string()]).optional(),
          'q:a': z
            .union([
              z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
              z.any(),
              z.number(),
            ])
            .optional(),
          qcomp: z
            .union([
              z.any(),
              z.union([z.any(), z.string()]),
              z.union([
                z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                z.any(),
                z.number(),
              ]),
            ])
            .optional(),
          qdiff: z
            .union([
              z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
              z.any(),
              z.number(),
            ])
            .optional(),
          qmax: z
            .union([
              z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
              z.any(),
              z.number(),
            ])
            .optional(),
          qmin: z
            .union([
              z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
              z.any(),
              z.number(),
            ])
            .optional(),
          r: z
            .union([
              z.union([
                z.any(),
                z.union([
                  z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                  z.any(),
                  z.number(),
                ]),
                z.union([z.any(), z.string()]),
              ]),
              z.null(),
            ])
            .optional(),
          rc_eq: z.union([z.any(), z.string()]).optional(),
          refs: z
            .union([
              z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
              z.any(),
              z.number(),
            ])
            .optional(),
          s: z.union([z.any(), z.string()]).optional(),
          sc_threshold: z
            .union([
              z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
              z.any(),
              z.number(),
            ])
            .optional(),
          sws_flags: z.union([z.any(), z.string()]).optional(),
          threads: z
            .union([
              z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
              z.any(),
              z.number(),
            ])
            .optional(),
          trellis: z
            .union([
              z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
              z.any(),
              z.number(),
            ])
            .optional(),
          transloaditffpreset: z
            .union([z.any(), z.literal('empty')])
            .optional(),
          vn: z.union([z.any(), z.union([z.boolean(), z.any()])]).optional(),
          vf: z.union([z.any(), z.string()]).optional(),
          x264opts: z.union([z.any(), z.string()]).optional(),
          vbr: z
            .union([
              z.any(),
              z.union([z.any(), z.string()]),
              z.union([
                z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                z.any(),
                z.number(),
              ]),
            ])
            .optional(),
        })
        .catchall(z.any()),
    ])
    .describe(
      '\nA parameter object to be passed to FFmpeg. If a preset is used, the options specified are merged on top of the ones from the preset. For available options, see the [FFmpeg documentation](https://ffmpeg.org/ffmpeg-doc.html). Options specified here take precedence over the preset options.\n',
    ),
})


const UseSchema = z.object({
  use: z
    .union([
      z.union([
        z.string(),
        z.array(z.any()),
        z.array(
          z
            .object({
              name: z.string(),
              fields: z.string().optional(),
              as: z.string().optional(),
            })
            .strict(),
        ),
      ]),
      z
        .object({
          steps: z.any(),
          bundle_steps: z.boolean().optional(),
          group_by_original: z.boolean().optional(),
          fields: z
            .array(z.string())
            .describe(
              '\nArray of field names to filter input files by when using steps.\n',
            )
            .optional(),
        })
        .strict(),
    ])
    .describe(
      '\nSpecifies which Step(s) to use as input.\n\n- You can pick any names for Steps except `":original"` (reserved for user uploads handled by Transloadit)\n- You can provide several Steps as input with arrays:\n  ```json\n  {\n    "use": [\n      ":original",\n      "encoded",\n      "resized"\n    ]\n  }\n  ```\n\n> [!Tip]\n> That\'s likely all you need to know about `use`, but you can view [Advanced use cases](https://transloadit.com/docs/topics/use-parameter/).\n',
    ),
})


const FfmpegStackSchema = z.object({
  ffmpeg_stack: z
    .union([
      z.any(),
      z.union([z.any(), z.enum(['v5', 'v6', 'v7'])]),
      z.union([
        z.any(),
        z.string().regex(new RegExp('^v?[567](\\.\\d+)?(\\.\\d+)?$')),
      ]),
    ])
    .describe(
      '\nSelects the FFmpeg stack version to use for encoding. These versions reflect real FFmpeg versions. We currently recommend to use "v6.0.0".\n',
    )
    .default('v5.0.0'),
})


const ResultSchema = z.object({
  result: z
    .union([z.any(), z.union([z.boolean(), z.any()])])
    .describe(
      'Whether the results of this Step should be present in the Assembly Status JSON',
    )
    .default(false),
})


const OutputMetaSchema = z.object({
  output_meta: z
    .union([
      z.any(),
      z.record(
        z.union([z.any(), z.union([z.boolean(), z.enum(['true', 'false'])])]),
      ),
      z.union([z.any(), z.union([z.boolean(), z.any()])]),
      z.union([z.any(), z.array(z.union([z.any(), z.string()]))]),
    ])
    .describe(
      '\nAllows you to specify a set of metadata that is more expensive on CPU power to calculate, and thus is disabled by default to keep your Assemblies processing fast.\n\nFor images, you can add `"has_transparency": true` in this object to extract if the image contains transparent parts and `"dominant_colors": true` to extract an array of hexadecimal color codes from the image.\n\nFor videos, you can add the `"colorspace: true"` parameter to extract the colorspace of the output video.\n\nFor audio, you can add `"mean_volume": true` to get a single value representing the mean average volume of the audio file.\n\nYou can also set this to `false` to skip metadata extraction and speed up transcoding.\n',
    ),
})


const IgnoreErrorsSchema = z.object({
  ignore_errors: z
    .union([
      z.any(),
      z.union([z.boolean(), z.array(z.enum(['meta', 'import']))]),
    ])
    .default([]),
})


const CredentialsSchema = z.object({
  credentials: z
    .union([z.any(), z.string()])
    .describe(
      '\nPlease create your associated <dfn>Template Credentials</dfn> in your Transloadit account and use the name of your [Template Credentials](https://transloadit.com/c/template-credentials/) as this parameter\'s value. They will contain the values for your Azure Container, Account and Key.\n\nWhile we recommend to use <dfn>Template Credentials</dfn> at all times, some use cases demand dynamic credentials for which using <dfn>Template Credentials</dfn> is too unwieldy because of their static nature. If you have this requirement, feel free to use the following parameters instead: `"account"`, `"key"`, `"container"`.\n',
    ),
})


const AudioPresetSchema = z.object({
  preset: z
    .union([
      z.any(),
      z.enum([
        'aac',
        'alac',
        'audio/aac',
        'audio/alac',
        'audio/flac',
        'audio/mp3',
        'audio/ogg',
        'dash-128k-audio',
        'dash-128k_audio',
        'dash-256k-audio',
        'dash-256k_audio',
        'dash-32k-audio',
        'dash-32k_audio',
        'dash-64k-audio',
        'dash-64k_audio',
        'dash/128k-audio',
        'dash/128k_audio',
        'dash/256k-audio',
        'dash/256k_audio',
        'dash/32k-audio',
        'dash/32k_audio',
        'dash/64k-audio',
        'dash/64k_audio',
        'dash_128k-audio',
        'dash_128k_audio',
        'dash_256k-audio',
        'dash_256k_audio',
        'dash_32k-audio',
        'dash_32k_audio',
        'dash_64k-audio',
        'dash_64k_audio',
        'empty',
        'flac',
        'hg-transformers-audio',
        'hg-transformers_audio',
        'hg_transformers-audio',
        'hg_transformers_audio',
        'mp3',
        'ogg',
        'opus',
        'speech',
        'wav',
      ]),
    ])
    .describe(
      "\nPerforms conversion using pre-configured settings.\n\nIf you specify your own FFmpeg parameters using the <dfn>Robot</dfn>'s `ffmpeg` parameter and you have not specified a preset, then the default `mp3` preset is not applied. This is to prevent you from having to override each of the MP3 preset's values manually.\n\nFor a list of audio presets, see [audio presets](https://transloadit.com/docs/presets/audio/).\n",
    ),
})


const VideoPresetSchema = z.object({
  preset: z
    .union([
      z.any(),
      z.enum([
        'android',
        'android-high',
        'android-low',
        'android_high',
        'android_low',
        'dash-1080p-video',
        'dash-1080p_video',
        'dash-270p-video',
        'dash-270p_video',
        'dash-360p-video',
        'dash-360p_video',
        'dash-480p-video',
        'dash-480p_video',
        'dash-540p-video',
        'dash-540p_video',
        'dash-576p-video',
        'dash-576p_video',
        'dash-720p-video',
        'dash-720p_video',
        'dash/1080p-video',
        'dash/1080p_video',
        'dash/270p-video',
        'dash/270p_video',
        'dash/360p-video',
        'dash/360p_video',
        'dash/480p-video',
        'dash/480p_video',
        'dash/540p-video',
        'dash/540p_video',
        'dash/576p-video',
        'dash/576p_video',
        'dash/720p-video',
        'dash/720p_video',
        'dash_1080p-video',
        'dash_1080p_video',
        'dash_270p-video',
        'dash_270p_video',
        'dash_360p-video',
        'dash_360p_video',
        'dash_480p-video',
        'dash_480p_video',
        'dash_540p-video',
        'dash_540p_video',
        'dash_576p-video',
        'dash_576p_video',
        'dash_720p-video',
        'dash_720p_video',
        'flash',
        'gif',
        'hevc',
        'hls-1080p',
        'hls-270p',
        'hls-360p',
        'hls-480p',
        'hls-540p',
        'hls-576p',
        'hls-720p',
        'hls/1080p',
        'hls/270p',
        'hls/360p',
        'hls/480p',
        'hls/4k',
        'hls/540p',
        'hls/720p',
        'hls_1080p',
        'hls_270p',
        'hls_360p',
        'hls_480p',
        'hls_540p',
        'hls_576p',
        'hls_720p',
        'ipad',
        'ipad-high',
        'ipad-low',
        'ipad_high',
        'ipad_low',
        'iphone',
        'iphone-high',
        'iphone-low',
        'iphone_high',
        'iphone_low',
        'ogv',
        'vod/1080p',
        'vod/270p',
        'vod/480p',
        'vod/720p',
        'vp9',
        'vp9-1080p',
        'vp9-270p',
        'vp9-360p',
        'vp9-480p',
        'vp9-540p',
        'vp9-576p',
        'vp9-720p',
        'vp9_1080p',
        'vp9_270p',
        'vp9_360p',
        'vp9_480p',
        'vp9_540p',
        'vp9_576p',
        'vp9_720p',
        'web/mp4-x265/1080p',
        'web/mp4-x265/240p',
        'web/mp4-x265/360p',
        'web/mp4-x265/480p',
        'web/mp4-x265/4k',
        'web/mp4-x265/720p',
        'web/mp4-x265/8k',
        'web/mp4/1080p',
        'web/mp4/240p',
        'web/mp4/360p',
        'web/mp4/480p',
        'web/mp4/4k',
        'web/mp4/540p',
        'web/mp4/720p',
        'web/mp4/8k',
        'web/mp4_x265/1080p',
        'web/mp4_x265/240p',
        'web/mp4_x265/360p',
        'web/mp4_x265/480p',
        'web/mp4_x265/4k',
        'web/mp4_x265/720p',
        'web/mp4_x265/8k',
        'web/webm-av1/1080p',
        'web/webm-av1/240p',
        'web/webm-av1/360p',
        'web/webm-av1/480p',
        'web/webm-av1/4k',
        'web/webm-av1/720p',
        'web/webm-av1/8k',
        'web/webm/1080p',
        'web/webm/240p',
        'web/webm/360p',
        'web/webm/480p',
        'web/webm/4k',
        'web/webm/720p',
        'web/webm/8k',
        'web/webm_av1/1080p',
        'web/webm_av1/240p',
        'web/webm_av1/360p',
        'web/webm_av1/480p',
        'web/webm_av1/4k',
        'web/webm_av1/720p',
        'web/webm_av1/8k',
        'webm',
        'webm-1080p',
        'webm-270p',
        'webm-360p',
        'webm-480p',
        'webm-540p',
        'webm-576p',
        'webm-720p',
        'webm_1080p',
        'webm_270p',
        'webm_360p',
        'webm_480p',
        'webm_540p',
        'webm_576p',
        'webm_720p',
        'wmv',
        'aac',
        'alac',
        'audio/aac',
        'audio/alac',
        'audio/flac',
        'audio/mp3',
        'audio/ogg',
        'dash-128k-audio',
        'dash-128k_audio',
        'dash-256k-audio',
        'dash-256k_audio',
        'dash-32k-audio',
        'dash-32k_audio',
        'dash-64k-audio',
        'dash-64k_audio',
        'dash/128k-audio',
        'dash/128k_audio',
        'dash/256k-audio',
        'dash/256k_audio',
        'dash/32k-audio',
        'dash/32k_audio',
        'dash/64k-audio',
        'dash/64k_audio',
        'dash_128k-audio',
        'dash_128k_audio',
        'dash_256k-audio',
        'dash_256k_audio',
        'dash_32k-audio',
        'dash_32k_audio',
        'dash_64k-audio',
        'dash_64k_audio',
        'empty',
        'flac',
        'hg-transformers-audio',
        'hg-transformers_audio',
        'hg_transformers-audio',
        'hg_transformers_audio',
        'mp3',
        'ogg',
        'opus',
        'speech',
        'wav',
      ]),
    ])
    .describe(
      "\nConverts a video according to [pre-configured settings](https://transloadit.com/docs/presets/video/).\n\nIf you specify your own FFmpeg parameters using the <dfn>Robot</dfn>'s and/or do not not want Transloadit to set any encoding setting, starting `ffmpeg_stack: \"v6\"`,  you can use the value `'empty'` here.\n",
    ),
})

```

#### `/audio/artwork`

[/audio/artwork docs](https://transloadit.com/docs/robots/audio-artwork/)

Robot Parameter Zod Schema:

```ts
const audioArtworkSchema = z
  .object({
    preset: AudioPresetSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    ffmpeg_stack: FfmpegStackSchema,
    use: UseSchema,
    ffmpeg: FfmpegSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    robot: z
      .literal('/audio/artwork')
      .describe(
        '\nFor extraction, this <dfn>Robot</dfn> uses the image format embedded within the audio file — most often, this is JPEG.\n\nIf you need the image in a different format, pipe the result of this <dfn>Robot</dfn> into [🤖/image/resize](https://transloadit.com/docs/robots/image-resize/).\n\nThe `method` parameter determines whether to extract or insert.\n',
      ),
    method: z
      .union([z.any(), z.enum(['extract', 'insert'])])
      .describe(
        '\nWhat should be done with the audio file. A value of `"extract"` means audio artwork will be extracted. A value of `"insert"` means the provided image will be inserted as audio artwork.\n',
      )
      .default('extract'),
    change_format_if_necessary: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nWhether the original file should be transcoded into a new format if there is an issue with the original file.\n',
      )
      .default(false),
  })
  .strict()

```

#### `/audio/concat`

[/audio/concat docs](https://transloadit.com/docs/robots/audio-concat/)

Robot Parameter Zod Schema:

```ts
const audioConcatSchema = z
  .object({
    preset: AudioPresetSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    ffmpeg_stack: FfmpegStackSchema,
    use: UseSchema,
    ffmpeg: FfmpegSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    robot: z
      .literal('/audio/concat')
      .describe(
        '\nThis Robot can concatenate an almost infinite number of audio files.\n',
      ),
    bitrate: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gte(1),
      ])
      .describe(
        '\nBit rate of the resulting audio file, in bits per second. If not specified will default to the bit rate of the input audio file.\n',
      )
      .optional(),
    sample_rate: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gte(1),
      ])
      .describe(
        '\nSample rate of the resulting audio file, in Hertz. If not specified will default to the sample rate of the input audio file.\n',
      )
      .optional(),
    audio_fade_seconds: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number(),
      ])
      .describe(
        '\nWhen used this adds an audio fade in and out effect between each section of your concatenated audio file. The float value is used, so if you want an audio delay effect of 500 milliseconds between each video section, you would select 0.5. Integer values can also be represented.\n\nThis parameter does not add an audio fade effect at the beginning or end of your result audio file. If you want to do so, create an additional [🤖/audio/encode](https://transloadit.com/docs/robots/audio-encode/) <dfn>Step</dfn> and use our `ffmpeg` parameter as shown in this [demo](https://transloadit.com/demos/audio-encoding/ffmpeg-fade-in-and-out/).\n',
      )
      .default(1),
    crossfade: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        "\nWhen set to `true`, this parameter enables crossfading between concatenated audio files using FFmpeg's `acrossfade` filter. This creates a smooth transition where the end of one audio file overlaps and blends with the beginning of the next file.\n\nThe duration of the crossfade is controlled by the `audio_fade_seconds` parameter (defaults to 1 second if `audio_fade_seconds` is 0).\n\nNote: This parameter requires at least 2 audio files to concatenate and only works with audio files, not video files.\n",
      )
      .default(false),
  })
  .strict()

```

#### `/audio/encode`

[/audio/encode docs](https://transloadit.com/docs/robots/audio-encode/)

Robot Parameter Zod Schema:

```ts
const audioEncodeSchema = z
  .object({
    preset: AudioPresetSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    ffmpeg_stack: FfmpegStackSchema,
    use: UseSchema,
    ffmpeg: FfmpegSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    robot: z.literal('/audio/encode'),
    bitrate: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gte(1),
      ])
      .describe(
        '\nBit rate of the resulting audio file, in bits per second. If not specified will default to the bit rate of the input audio file.\n',
      )
      .optional(),
    sample_rate: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gte(1),
      ])
      .describe(
        '\nSample rate of the resulting audio file, in Hertz. If not specified will default to the sample rate of the input audio file.\n',
      )
      .optional(),
  })
  .strict()

```

#### `/audio/loop`

[/audio/loop docs](https://transloadit.com/docs/robots/audio-loop/)

Robot Parameter Zod Schema:

```ts
const audioLoopSchema = z
  .object({
    preset: AudioPresetSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    ffmpeg_stack: FfmpegStackSchema,
    use: UseSchema,
    ffmpeg: FfmpegSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    robot: z.literal('/audio/loop'),
    bitrate: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gte(1),
      ])
      .describe(
        '\nBit rate of the resulting audio file, in bits per second. If not specified will default to the bit rate of the input audio file.\n',
      )
      .optional(),
    sample_rate: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gte(1),
      ])
      .describe(
        '\nSample rate of the resulting audio file, in Hertz. If not specified will default to the sample rate of the input audio file.\n',
      )
      .optional(),
    duration: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number(),
      ])
      .describe(
        '\nTarget duration for the whole process in seconds. The <dfn>Robot</dfn> will loop the input audio file for as long as this target duration is not reached yet.\n',
      )
      .default(60),
  })
  .strict()

```

#### `/audio/merge`

[/audio/merge docs](https://transloadit.com/docs/robots/audio-merge/)

Robot Parameter Zod Schema:

```ts
const audioMergeSchema = z
  .object({
    preset: AudioPresetSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    ffmpeg_stack: FfmpegStackSchema,
    use: UseSchema,
    ffmpeg: FfmpegSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    robot: z.literal('/audio/merge'),
    bitrate: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gte(1),
      ])
      .describe(
        '\nBit rate of the resulting audio file, in bits per second. If not specified will default to the bit rate of the input audio file.\n',
      )
      .optional(),
    sample_rate: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gte(1),
      ])
      .describe(
        '\nSample rate of the resulting audio file, in Hertz. If not specified will default to the sample rate of the input audio file.\n',
      )
      .optional(),
    duration: z
      .union([z.any(), z.enum(['first', 'longest', 'shortest'])])
      .describe(
        '\nDuration of the output file compared to the duration of all merged audio files. Can be `"first"` (duration of the first input file), `"shortest"` (duration of the shortest audio file) or `"longest"` for the duration of the longest input file.\n',
      )
      .default('longest'),
    loop: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nSpecifies if any input files that do not match the target duration should be looped to match it. Useful for audio merging where your overlay file is typically much shorter than the main audio file.\n',
      )
      .default(false),
    volume: z
      .union([z.any(), z.enum(['average', 'sum'])])
      .describe(
        '\nValid values are `"average"` and `"sum"` here. `"average"` means each input is scaled 1/n (n is the number of inputs) or `"sum"` which means each individual audio stays on the same volume, but since we merge tracks \'on top\' of each other, this could result in very loud output.\n',
      )
      .default('average'),
  })
  .strict()

```

#### `/audio/waveform`

[/audio/waveform docs](https://transloadit.com/docs/robots/audio-waveform/)

Robot Parameter Zod Schema:

```ts
const audioWaveformSchema = z
  .object({
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    ffmpeg_stack: FfmpegStackSchema,
    use: UseSchema,
    ffmpeg: FfmpegSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    robot: z
      .literal('/audio/waveform')
      .describe(
        '\nWe recommend that you use an [🤖/audio/encode](https://transloadit.com/docs/robots/audio-encode/) <dfn>Step</dfn> prior to your waveform <dfn>Step</dfn> to convert audio files to MP3. This way it is guaranteed that [🤖/audio/waveform](https://transloadit.com/docs/robots/audio-waveform/) accepts your audio file and you can also down-sample large audio files and save some money.\n\nSimilarly, if you need the output image in a different format, please pipe the result of this <dfn>Robot</dfn> into [🤖/image/resize](https://transloadit.com/docs/robots/image-resize/).\n',
      ),
    format: z
      .union([z.any(), z.enum(['image', 'json'])])
      .describe(
        '\nThe format of the result file. Can be `"image"` or `"json"`. If `"image"` is supplied, a PNG image will be created, otherwise a JSON file.\n',
      )
      .default('image'),
    width: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gte(1),
      ])
      .describe(
        '\nThe width of the resulting image if the format `"image"` was selected.\n',
      )
      .default(256),
    height: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gte(1),
      ])
      .describe(
        '\nThe height of the resulting image if the format `"image"` was selected.\n',
      )
      .default(64),
    style: z
      .union([
        z.any(),
        z.union([z.any(), z.literal(0)]),
        z.union([z.any(), z.literal(1)]),
      ])
      .describe(
        '\nEither a value of `0` or `1`, corresponding to using either the legacy waveform tool, or the new tool respectively, with the new tool offering an improved style. Other Robot parameters still function as described, with either tool.\n',
      )
      .default(0),
    antialiasing: z
      .union([
        z.any(),
        z.union([z.any(), z.literal(0)]),
        z.union([z.any(), z.literal(1)]),
        z.union([z.any(), z.union([z.boolean(), z.any()])]),
      ])
      .describe(
        '\nEither a value of `0` or `1`, or `true`/`false`, corresponding to if you want to enable antialiasing to achieve smoother edges in the waveform graph or not.\n',
      )
      .default(0),
    background_color: z
      .union([
        z.any(),
        z.string().regex(new RegExp('^#?[0-9a-fA-F]{6}([0-9a-fA-F]{2})?$')),
      ])
      .describe(
        '\nThe background color of the resulting image in the "rrggbbaa" format (red, green, blue, alpha), if the format `"image"` was selected.\n',
      )
      .default('#00000000'),
    center_color: z
      .union([z.any(), z.any()])
      .describe(
        '\nThe color used in the center of the gradient. The format is "rrggbbaa" (red, green, blue, alpha).\n',
      )
      .default('000000ff'),
    outer_color: z
      .union([z.any(), z.any()])
      .describe(
        '\nThe color used in the outer parts of the gradient. The format is "rrggbbaa" (red, green, blue, alpha).\n',
      )
      .default('000000ff'),
  })
  .strict()

```

#### `/azure/import`

[/azure/import docs](https://transloadit.com/docs/robots/azure-import/)

Robot Parameter Zod Schema:

```ts
const azureImportSchema = z
  .object({
    credentials: CredentialsSchema,
    ignore_errors: IgnoreErrorsSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    force_name: z
      .union([
        z.union([
          z.any(),
          z.union([z.any(), z.string()]),
          z.union([z.any(), z.array(z.union([z.any(), z.string()]))]),
        ]),
        z.null(),
      ])
      .describe(
        'Custom name for the imported file(s). By default file names are derived from the source.',
      )
      .default(null),
    account: z.union([z.any(), z.string()]).optional(),
    container: z.union([z.any(), z.string()]).optional(),
    key: z.union([z.any(), z.string()]).optional(),
    robot: z.literal('/azure/import'),
    path: z
      .union([
        z.any(),
        z.union([z.any(), z.string()]),
        z.union([z.any(), z.array(z.union([z.any(), z.string()]))]),
      ])
      .describe(
        "\nThe path in your container to the specific file or directory. If the path points to a file, only this file will be imported. For example: `images/avatar.jpg`.\n\nIf it points to a directory, indicated by a trailing slash (`/`), then all files that are descendants of this directory are recursively imported. For example: `images/`.\n\nIf you want to import all files from the root directory, please use `/` as the value here.\n\nYou can also use an array of path strings here to import multiple paths in the same <dfn>Robot</dfn>'s <dfn>Step</dfn>.\n",
      ),
    recursive: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\n  Setting this to `true` will enable importing files from subdirectories and sub-subdirectories (etc.) of the given path.\n  ',
      )
      .default(false),
    next_page_token: z
      .union([z.any(), z.string()])
      .describe(
        '\nA string token used for pagination. The returned files of one paginated call have the next page token inside of their meta data, which needs to be used for the subsequent paging call.\n',
      )
      .default(''),
    files_per_page: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int(),
      ])
      .describe('\nThe pagination page size.\n')
      .default(1000),
  })
  .strict()

```

#### `/azure/store`

[/azure/store docs](https://transloadit.com/docs/robots/azure-store/)

Robot Parameter Zod Schema:

```ts
const azureStoreSchema = z
  .object({
    credentials: CredentialsSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    account: z.union([z.any(), z.string()]).optional(),
    container: z.union([z.any(), z.string()]).optional(),
    key: z.union([z.any(), z.string()]).optional(),
    robot: z.literal('/azure/store'),
    path: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe path at which the file is to be stored. This may include any available [Assembly variables](https://transloadit.com/docs/topics/assembly-instructions/#assembly-variables).\n',
      )
      .default('${unique_prefix}/${file.url_name}'),
    content_type: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe content type with which to store the file. By default this will be guessed by Azure.\n',
      )
      .optional(),
    content_encoding: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe content encoding with which to store the file. By default this will be guessed by Azure.\n',
      )
      .optional(),
    content_language: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe content language with which to store the file. By default this will be guessed by Azure.\n',
      )
      .optional(),
    content_disposition: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe content disposition with which to store the file. By default this will be guessed by Azure.\n',
      )
      .optional(),
    cache_control: z
      .union([z.any(), z.string()])
      .describe('\nThe cache control header with which to store the file.\n')
      .optional(),
    metadata: z
      .record(z.union([z.any(), z.string()]))
      .describe(
        '\nA JavaScript object containing a list of metadata to be set for this file on Azure, such as `{ FileURL: "${file.url_name}" }`. This can also include any available [Assembly variables](https://transloadit.com/docs/topics/assembly-instructions/#assembly-variables).\n',
      )
      .default({}),
    sas_expires_in: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gte(0),
      ])
      .describe(
        '\nSet this to a number to enable shared access signatures for your stored object. This reflects the number of seconds that the signature will be valid for once the object is stored. Enabling this will attach the shared access signature (SAS) to the result URL of your object.\n',
      )
      .optional(),
    sas_permissions: z
      .union([z.any(), z.string().regex(new RegExp('^[rdw]+$')).min(0).max(3)])
      .describe(
        '\nSet this to a combination of `r` (read), `w` (write) and `d` (delete) for your shared access signatures (SAS) permissions.\n',
      )
      .optional(),
  })
  .strict()

```

#### `/backblaze/import`

[/backblaze/import docs](https://transloadit.com/docs/robots/backblaze-import/)

Robot Parameter Zod Schema:

```ts
const backblazeImportSchema = z
  .object({
    credentials: CredentialsSchema,
    ignore_errors: IgnoreErrorsSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    force_name: z
      .union([
        z.union([
          z.any(),
          z.union([z.any(), z.string()]),
          z.union([z.any(), z.array(z.union([z.any(), z.string()]))]),
        ]),
        z.null(),
      ])
      .describe(
        'Custom name for the imported file(s). By default file names are derived from the source.',
      )
      .default(null),
    bucket: z.union([z.any(), z.string()]).optional(),
    app_key_id: z.union([z.any(), z.string()]).optional(),
    app_key: z.union([z.any(), z.string()]).optional(),
    robot: z.literal('/backblaze/import'),
    path: z
      .union([
        z.any(),
        z.union([z.any(), z.string()]),
        z.union([z.any(), z.array(z.union([z.any(), z.string()]))]),
      ])
      .describe(
        "\nThe path in your bucket to the specific file or directory. If the path points to a file, only this file will be imported. For example: `images/avatar.jpg`.\n\nIf it points to a directory, indicated by a trailing slash (`/`), then all files that are direct descendants of this directory will be imported. For example: `images/`.\n\nDirectories are **not** imported recursively. If you want to import files from subdirectories and sub-subdirectories, enable the `recursive` parameter.\n\nIf you want to import all files from the root directory, please use `/` as the value here. In this case, make sure all your objects belong to a path. If you have objects in the root of your bucket that aren't prefixed with `/`, you'll receive a 404 `BACKBLAZE_IMPORT_NOT_FOUND` error.\n\nYou can also use an array of path strings here to import multiple paths in the same <dfn>Robot</dfn>'s <dfn>Step</dfn>.\n",
      ),
    recursive: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nSetting this to `true` will enable importing files from subdirectories and sub-subdirectories (etc.) of the given path.\n\nPlease use the pagination parameters `start_file_name` and `files_per_page` wisely here.\n',
      )
      .default(false),
    start_file_name: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe name of the last file from the previous paging call. This tells the <dfn>Robot</dfn> to ignore all files up to and including this file.\n',
      )
      .default(''),
    files_per_page: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int(),
      ])
      .describe(
        '\nThe pagination page size. This only works when recursive is `true` for now, in order to not break backwards compatibility in non-recursive imports.\n',
      )
      .default(1000),
  })
  .strict()

```

#### `/backblaze/store`

[/backblaze/store docs](https://transloadit.com/docs/robots/backblaze-store/)

Robot Parameter Zod Schema:

```ts
const backblazeStoreSchema = z
  .object({
    credentials: CredentialsSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    bucket: z.union([z.any(), z.string()]).optional(),
    app_key_id: z.union([z.any(), z.string()]).optional(),
    app_key: z.union([z.any(), z.string()]).optional(),
    robot: z.literal('/backblaze/store'),
    path: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe path at which the file is to be stored. This may include any available [Assembly variables](https://transloadit.com/docs/topics/assembly-instructions/#assembly-variables).\n',
      )
      .default('${unique_prefix}/${file.url_name}'),
    headers: z
      .record(z.union([z.any(), z.string()]))
      .describe(
        '\nAn object containing a list of headers to be set for this file on backblaze, such as `{ FileURL: "${file.url_name}" }`. This can also include any available [Assembly Variables](https://transloadit.com/docs/topics/assembly-instructions/#assembly-variables).\n\n[Here](https://www.backblaze.com/b2/docs/b2_upload_file.html) you can find a list of available headers.\n\nObject Metadata can be specified using `X-Bz-Info-*` headers.\n',
      )
      .default({}),
  })
  .strict()

```

#### `/cloudfiles/import`

[/cloudfiles/import docs](https://transloadit.com/docs/robots/cloudfiles-import/)

Robot Parameter Zod Schema:

```ts
const cloudfilesImportSchema = z
  .object({
    credentials: CredentialsSchema,
    ignore_errors: IgnoreErrorsSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    force_name: z
      .union([
        z.union([
          z.any(),
          z.union([z.any(), z.string()]),
          z.union([z.any(), z.array(z.union([z.any(), z.string()]))]),
        ]),
        z.null(),
      ])
      .describe(
        'Custom name for the imported file(s). By default file names are derived from the source.',
      )
      .default(null),
    account_type: z.union([z.any(), z.enum(['uk', 'us'])]).optional(),
    data_center: z.union([z.any(), z.string()]).optional(),
    user: z.union([z.any(), z.string()]).optional(),
    key: z.union([z.any(), z.string()]).optional(),
    container: z.union([z.any(), z.string()]).optional(),
    robot: z.literal('/cloudfiles/import'),
    path: z
      .union([
        z.any(),
        z.union([z.any(), z.string()]),
        z.union([z.any(), z.array(z.union([z.any(), z.string()]))]),
      ])
      .describe(
        "\nThe path in your bucket to the specific file or directory. If the path points to a file, only this file will be imported. For example: `images/avatar.jpg`.\n\nIf it points to a directory, indicated by a trailing slash (`/`), then all files that are direct descendants of this directory will be imported. For example: `images/`.\n\nDirectories are **not** imported recursively. If you want to import files from subdirectories and sub-subdirectories, enable the `recursive` parameter.\n\nYou can also use an array of path strings here to import multiple paths in the same <dfn>Robot</dfn>'s <dfn>Step</dfn>.\n",
      ),
    recursive: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nSetting this to `true` will enable importing files from subdirectories and sub-subdirectories (etc.) of the given path.\n\nPlease use the pagination parameters `page_number` and `files_per_page`wisely here.\n',
      )
      .default(false),
    page_number: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int(),
      ])
      .describe(
        '\nThe pagination page number. For now, in order to not break backwards compatibility in non-recursive imports, this only works when recursive is set to `true`.\n\nWhen doing big imports, make sure no files are added or removed from other scripts within your path, otherwise you might get weird results with the pagination.\n',
      )
      .default(1),
    files_per_page: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int(),
      ])
      .describe(
        '\nThe pagination page size. This only works when recursive is `true` for now, in order to not break backwards compatibility in non-recursive imports.\n',
      )
      .default(1000),
  })
  .strict()

```

#### `/cloudfiles/store`

[/cloudfiles/store docs](https://transloadit.com/docs/robots/cloudfiles-store/)

Robot Parameter Zod Schema:

```ts
const cloudfilesStoreSchema = z
  .object({
    credentials: CredentialsSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    account_type: z.union([z.any(), z.enum(['uk', 'us'])]).optional(),
    data_center: z.union([z.any(), z.string()]).optional(),
    user: z.union([z.any(), z.string()]).optional(),
    key: z.union([z.any(), z.string()]).optional(),
    container: z.union([z.any(), z.string()]).optional(),
    robot: z.literal('/cloudfiles/store'),
    path: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe path at which to store the file. This value can also contain [Assembly variables](https://transloadit.com/docs/topics/assembly-instructions/#assembly-variables).\n',
      )
      .default('${unique_prefix}/${file.url_name}'),
  })
  .strict()

```

#### `/cloudflare/import`

[/cloudflare/import docs](https://transloadit.com/docs/robots/cloudflare-import/)

Robot Parameter Zod Schema:

```ts
const cloudflareImportSchema = z
  .object({
    credentials: CredentialsSchema,
    ignore_errors: IgnoreErrorsSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    force_name: z
      .union([
        z.union([
          z.any(),
          z.union([z.any(), z.string()]),
          z.union([z.any(), z.array(z.union([z.any(), z.string()]))]),
        ]),
        z.null(),
      ])
      .describe(
        'Custom name for the imported file(s). By default file names are derived from the source.',
      )
      .default(null),
    bucket: z.union([z.any(), z.string()]).optional(),
    host: z.union([z.any(), z.string()]).optional(),
    key: z.union([z.any(), z.string()]).optional(),
    secret: z.union([z.any(), z.string()]).optional(),
    robot: z.literal('/cloudflare/import'),
    path: z
      .union([
        z.any(),
        z.union([z.any(), z.string()]),
        z.union([z.any(), z.array(z.union([z.any(), z.string()]))]),
      ])
      .describe(
        "\nThe path in your bucket to the specific file or directory. If the path points to a file, only this file will be imported. For example: `images/avatar.jpg`.\n\nIf it points to a directory, indicated by a trailing slash (`/`), then all files that are direct descendants of this directory will be imported. For example: `images/`.\n\nDirectories are **not** imported recursively. If you want to import files from subdirectories and sub-subdirectories, enable the `recursive` parameter.\n\nIf you want to import all files from the root directory, please use `/` as the value here. In this case, make sure all your objects belong to a path. If you have objects in the root of your bucket that aren't prefixed with `/`, you'll receive an error: `A client error (NoSuchKey) occurred when calling the GetObject operation: The specified key does not exist.`\n\nYou can also use an array of path strings here to import multiple paths in the same <dfn>Robot</dfn>'s <dfn>Step</dfn>.\n",
      ),
    recursive: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nSetting this to `true` will enable importing files from subfolders and sub-subfolders, etc. of the given path.\n\nPlease use the pagination parameters `page_number` and `files_per_page` wisely here.\n',
      )
      .default(false),
    page_number: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int(),
      ])
      .describe(
        '\nThe pagination page number. For now, in order to not break backwards compatibility in non-recursive imports, this only works when recursive is set to `true`.\n\nWhen doing big imports, make sure no files are added or removed from other scripts within your path, otherwise you might get weird results with the pagination.\n',
      )
      .default(1),
    files_per_page: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int(),
      ])
      .describe(
        '\nThe pagination page size. This only works when recursive is `true` for now, in order to not break backwards compatibility in non-recursive imports.\n',
      )
      .default(1000),
    return_file_stubs: z
      .union([
        z.any(),
        z.union([
          z
            .boolean()
            .describe(
              '\nIf set to `true`, the Robot will not yet import the actual files but instead return an empty file stub that includes a URL from where the file can be imported by subsequent Robots. This is useful for cases where subsequent Steps need more control over the import process, such as with 🤖/video/ondemand. This parameter should only be set if all subsequent Steps use Robots that support file stubs.\n',
            ),
          z.any(),
        ]),
      ])
      .describe(
        '\nIf set to `true`, the Robot will not yet import the actual files but instead return an empty file stub that includes a URL from where the file can be imported by subsequent Robots. This is useful for cases where subsequent Steps need more control over the import process, such as with 🤖/video/ondemand. This parameter should only be set if all subsequent Steps use Robots that support file stubs.\n',
      )
      .default(false),
  })
  .strict()

```

#### `/cloudflare/store`

[/cloudflare/store docs](https://transloadit.com/docs/robots/cloudflare-store/)

Robot Parameter Zod Schema:

```ts
const cloudflareStoreSchema = z
  .object({
    credentials: CredentialsSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    bucket: z.union([z.any(), z.string()]).optional(),
    host: z.union([z.any(), z.string()]).optional(),
    key: z.union([z.any(), z.string()]).optional(),
    secret: z.union([z.any(), z.string()]).optional(),
    robot: z.literal('/cloudflare/store'),
    path: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe path at which the file is to be stored. This may include any available [Assembly variables](https://transloadit.com/docs/topics/assembly-instructions/#assembly-variables). The path must not be a directory.\n',
      )
      .default('${unique_prefix}/${file.url_name}'),
    headers: z
      .record(z.union([z.any(), z.string()]))
      .describe(
        '\nAn object containing a list of headers to be set for this file on cloudflare Spaces, such as `{ FileURL: "${file.url_name}" }`. This can also include any available [Assembly Variables](https://transloadit.com/docs/topics/assembly-instructions/#assembly-variables).\n\nObject Metadata can be specified using `x-amz-meta-*` headers. Note that these headers [do not support non-ASCII metadata values](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#UserMetadata).\n',
      )
      .default({ 'Content-Type': '${file.mime}' }),
    sign_urls_for: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gte(0),
      ])
      .describe(
        '\nThis parameter provides signed URLs in the result JSON (in the `signed_ssl_url` property). The number that you set this parameter to is the URL expiry time in seconds. If this parameter is not used, no URL signing is done.\n',
      )
      .optional(),
    url_prefix: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe URL prefix used for accessing files from your Cloudflare R2 bucket. This is typically the custom public URL access host set up in your Cloudflare account.\n',
      )
      .optional(),
  })
  .strict()

```

#### `/digitalocean/import`

[/digitalocean/import docs](https://transloadit.com/docs/robots/digitalocean-import/)

Robot Parameter Zod Schema:

```ts
const digitaloceanImportSchema = z
  .object({
    credentials: CredentialsSchema,
    ignore_errors: IgnoreErrorsSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    force_name: z
      .union([
        z.union([
          z.any(),
          z.union([z.any(), z.string()]),
          z.union([z.any(), z.array(z.union([z.any(), z.string()]))]),
        ]),
        z.null(),
      ])
      .describe(
        'Custom name for the imported file(s). By default file names are derived from the source.',
      )
      .default(null),
    space: z.union([z.any(), z.string()]).optional(),
    region: z.union([z.any(), z.string()]).optional(),
    key: z.union([z.any(), z.string()]).optional(),
    secret: z.union([z.any(), z.string()]).optional(),
    robot: z.literal('/digitalocean/import'),
    path: z
      .union([
        z.any(),
        z.union([z.any(), z.string()]),
        z.union([z.any(), z.array(z.union([z.any(), z.string()]))]),
      ])
      .describe(
        "\nThe path in your bucket to the specific file or directory. If the path points to a file, only this file will be imported. For example: `images/avatar.jpg`.\n\nIf it points to a directory, indicated by a trailing slash (`/`), then all files that are direct descendants of this directory will be imported. For example: `images/`.\n\nDirectories are **not** imported recursively. If you want to import files from subdirectories and sub-subdirectories, enable the `recursive` parameter.\n\nYou can also use an array of path strings here to import multiple paths in the same <dfn>Robot</dfn>'s <dfn>Step</dfn>.\n",
      ),
    recursive: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nSetting this to `true` will enable importing files from subdirectories and sub-subdirectories (etc.) of the given path.\n\nPlease use the pagination parameters `page_number` and `files_per_page` wisely here.\n',
      )
      .default(false),
    page_number: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int(),
      ])
      .describe(
        '\nThe pagination page number. For now, in order to not break backwards compatibility in non-recursive imports, this only works when recursive is set to `true`.\n\nWhen doing big imports, make sure no files are added or removed from other scripts within your path, otherwise you might get weird results with the pagination.\n',
      )
      .default(1),
    files_per_page: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int(),
      ])
      .describe(
        '\nThe pagination page size. This only works when recursive is `true` for now, in order to not break backwards compatibility in non-recursive imports.\n',
      )
      .default(1000),
    return_file_stubs: z
      .union([
        z.any(),
        z.union([
          z
            .boolean()
            .describe(
              '\nIf set to `true`, the Robot will not yet import the actual files but instead return an empty file stub that includes a URL from where the file can be imported by subsequent Robots. This is useful for cases where subsequent Steps need more control over the import process, such as with 🤖/video/ondemand. This parameter should only be set if all subsequent Steps use Robots that support file stubs.\n',
            ),
          z.any(),
        ]),
      ])
      .describe(
        '\nIf set to `true`, the Robot will not yet import the actual files but instead return an empty file stub that includes a URL from where the file can be imported by subsequent Robots. This is useful for cases where subsequent Steps need more control over the import process, such as with 🤖/video/ondemand. This parameter should only be set if all subsequent Steps use Robots that support file stubs.\n',
      )
      .default(false),
  })
  .strict()

```

#### `/digitalocean/store`

[/digitalocean/store docs](https://transloadit.com/docs/robots/digitalocean-store/)

Robot Parameter Zod Schema:

```ts
const digitaloceanStoreSchema = z
  .object({
    credentials: CredentialsSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    space: z.union([z.any(), z.string()]).optional(),
    region: z.union([z.any(), z.string()]).optional(),
    key: z.union([z.any(), z.string()]).optional(),
    secret: z.union([z.any(), z.string()]).optional(),
    robot: z.literal('/digitalocean/store'),
    path: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe path at which the file is to be stored. This may include any available [Assembly variables](https://transloadit.com/docs/topics/assembly-instructions/#assembly-variables). The path must not be a directory.\n',
      )
      .default('${unique_prefix}/${file.url_name}'),
    url_prefix: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe URL prefix used for the returned URL, such as `"https://my.cdn.com/some/path"`.\n',
      )
      .default('https://{space}.{region}.digitaloceanspaces.com/'),
    acl: z
      .union([z.any(), z.enum(['private', 'public-read'])])
      .describe('\nThe permissions used for this file.\n')
      .default('public-read'),
    headers: z
      .record(z.union([z.any(), z.string()]))
      .describe(
        '\nAn object containing a list of headers to be set for this file on DigitalOcean Spaces, such as `{ FileURL: "${file.url_name}" }`. This can also include any available [Assembly Variables](https://transloadit.com/docs/topics/assembly-instructions/#assembly-variables).\n\n[Here](https://developers.digitalocean.com/documentation/spaces/#object) you can find a list of available headers.\n\nObject Metadata can be specified using `x-amz-meta-*` headers. Note that these headers [do not support non-ASCII metadata values](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#UserMetadata).\n',
      )
      .default({ 'Content-Type': '${file.mime}' }),
    sign_urls_for: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gte(0),
      ])
      .describe(
        '\nThis parameter provides signed URLs in the result JSON (in the `signed_ssl_url` property). The number that you set this parameter to is the URL expiry time in seconds. If this parameter is not used, no URL signing is done.\n',
      )
      .optional(),
  })
  .strict()

```

#### `/document/autorotate`

[/document/autorotate docs](https://transloadit.com/docs/robots/document-autorotate/)

Robot Parameter Zod Schema:

```ts
const documentAutorotateSchema = z
  .object({
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    robot: z.literal('/document/autorotate'),
  })
  .strict()

```

#### `/document/convert`

[/document/convert docs](https://transloadit.com/docs/robots/document-convert/)

Robot Parameter Zod Schema:

```ts
const documentConvertSchema = z
  .object({
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    robot: z
      .literal('/document/convert')
      .describe(
        '\n> [!Note]\n> This Robot can convert files to PDF, but cannot convert PDFs to different formats. If you want to convert PDFs to say, JPEG or TIFF, use [🤖/image/resize](https://transloadit.com/docs/robots/image-resize/). If you want to turn them into text files or recognize (OCR) them to make them searchable, reach out, as we have a new Robot in the works for this.\n\nSometimes, a certain file type might not support what you are trying to accomplish. Perhaps your company is trying to automate document formatting, but it only works with docx, so all your docs need to be converted. Or maybe your stored jpg files are taking up too much space and you want a lighter format. Whatever the case, we have you covered.\n\nUsing this Robot, you can bypass the issues that certain file types may bring, by converting your file into the most suitable format. This also works in conjunction with our other Robots, allowing for even greater versatility when using our services.\n\n> [!Warning]\n> A general rule of this Robot is that converting files into an alien format category will result in an error. For example, SRT files can be converted into the VTT format, but not to an image.\n\nThe following file formats can be converted from:\n\n- `ai`\n- `csv`\n- `doc`\n- `docx`\n- `eps`\n- `gif`\n- `html`\n- `jpg`\n- `latex`\n- `md`\n- `oda`\n- `odd`\n- `odt`\n- `ott`\n- `png`\n- `pot`\n- `pps`\n- `ppt`\n- `pptx`\n- `ppz`\n- `ps`\n- `rtf`\n- `rtx`\n- `svg`\n- `text`\n- `txt`\n- `xhtml`\n- `xla`\n- `xls`\n- `xlsx`\n- `xml`\n',
      ),
    format: z
      .union([
        z.any(),
        z
          .enum([
            'ai',
            'csv',
            'doc',
            'docx',
            'eps',
            'gif',
            'html',
            'jpeg',
            'jpg',
            'latex',
            'oda',
            'odd',
            'odt',
            'ott',
            'pdf',
            'png',
            'pot',
            'pps',
            'ppt',
            'pptx',
            'ppz',
            'ps',
            'rtf',
            'rtx',
            'srt',
            'svg',
            'text',
            'txt',
            'vtt',
            'xhtml',
            'xla',
            'xls',
            'xlsx',
            'xml',
          ])
          .describe('\nThe desired format for document conversion.\n'),
      ])
      .describe('\nThe desired format for document conversion.\n'),
    markdown_format: z
      .union([z.any(), z.enum(['commonmark', 'gfm'])])
      .describe(
        '\nMarkdown can be represented in several [variants](https://www.iana.org/assignments/markdown-variants/markdown-variants.xhtml), so when using this Robot to transform Markdown into HTML please specify which revision is being used.\n',
      )
      .default('gfm'),
    markdown_theme: z
      .union([z.any(), z.enum(['bare', 'github'])])
      .describe(
        '\nThis parameter overhauls your Markdown files styling based on several canned presets.\n',
      )
      .default('github'),
    pdf_margin: z
      .union([z.any(), z.string()])
      .describe(
        '\nPDF Paper margins, separated by `,` and with units.\n\nWe support the following unit values: `px`, `in`, `cm`, `mm`.\n\nCurrently this parameter is only supported when converting from `html`.\n',
      )
      .default('6.25mm,6.25mm,14.11mm,6.25mm'),
    pdf_print_background: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nPrint PDF background graphics.\n\nCurrently this parameter is only supported when converting from `html`.\n',
      )
      .default(true),
    pdf_format: z
      .union([
        z.any(),
        z.enum([
          'A0',
          'A1',
          'A2',
          'A3',
          'A4',
          'A5',
          'A6',
          'Ledger',
          'Legal',
          'Letter',
          'Tabloid',
        ]),
      ])
      .describe(
        '\nPDF paper format.\n\nCurrently this parameter is only supported when converting from `html`.\n',
      )
      .default('Letter'),
    pdf_display_header_footer: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nDisplay PDF header and footer.\n\nCurrently this parameter is only supported when converting from `html`.\n',
      )
      .default(false),
    pdf_header_template: z
      .union([z.any(), z.string()])
      .describe(
        '\nHTML template for the PDF print header.\n\nShould be valid HTML markup with following classes used to inject printing values into them:\n- `date` formatted print date\n- `title` document title\n- `url` document location\n- `pageNumber` current page number\n- `totalPages` total pages in the document\n\nCurrently this parameter is only supported when converting from `html`, and requires `pdf_display_header_footer` to be enabled.\n\nTo change the formatting of the HTML element, the `font-size` must be specified in a wrapper. For example, to center the page number at the top of a page you\'d use the following HTML for the header template:\n\n```html\n<div style="font-size: 15px; width: 100%; text-align: center;"><span class="pageNumber"></span></div>\n```\n',
      )
      .optional(),
    pdf_footer_template: z
      .union([z.any(), z.string()])
      .describe(
        '\nHTML template for the PDF print footer.\n\nShould use the same format as the `pdf_header_template`.\n\nCurrently this parameter is only supported when converting from `html`, and requires `pdf_display_header_footer` to be enabled.\n\nTo change the formatting of the HTML element, the `font-size` must be specified in a wrapper. For example, to center the page number in the footer you\'d use the following HTML for the footer template:\n\n```html\n<div style="font-size: 15px; width: 100%; text-align: center;"><span class="pageNumber"></span></div>\n```\n',
      )
      .optional(),
  })
  .strict()

```

#### `/document/merge`

[/document/merge docs](https://transloadit.com/docs/robots/document-merge/)

Robot Parameter Zod Schema:

```ts
const documentMergeSchema = z
  .object({
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    robot: z.literal('/document/merge'),
    input_passwords: z
      .union([z.any(), z.array(z.union([z.any(), z.string()]))])
      .describe(
        '\nAn array of passwords for the input documents, in case they are encrypted. The order of passwords must match the order of the documents as they are passed to the /document/merge step.\n\nThis can be achieved via our as-syntax using "document_1", "document_2", etc if provided. See the demos below.\n\nIf the as-syntax is not used in the "use" parameter, the documents are sorted alphanumerically based on their filename, and in that order input passwords should be provided.\n',
      )
      .default([]),
    output_password: z
      .union([z.any(), z.string()])
      .describe(
        '\nIf not empty, encrypts the output file and makes it accessible only by typing in this password.\n',
      )
      .optional(),
  })
  .strict()

```

#### `/document/ocr`

[/document/ocr docs](https://transloadit.com/docs/robots/document-ocr/)

Robot Parameter Zod Schema:

```ts
const documentOcrSchema = z
  .object({
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    robot: z
      .literal('/document/ocr')
      .describe(
        '\nWith this <dfn>Robot</dfn>, you can detect and extract text from PDFs using optical character recognition (OCR).\n\nFor example, you can use the results to obtain the content of invoices, legal documents or restaurant menus. You can also pass the text down to other <dfn>Robots</dfn> to filter documents that contain (or do not contain) certain phrases.\n',
      ),
    provider: z
      .union([
        z.any(),
        z
          .enum(['aws', 'gcp', 'replicate', 'fal', 'transloadit'])
          .describe(
            '\nWhich AI provider to leverage. Valid values are `"aws"` and `"gcp"`.\n\nTransloadit outsources this task and abstracts the interface so you can expect the same data structures, but different latencies and information being returned. Different cloud vendors have different areas they shine in, and we recommend to try out and see what yields the best results for your use case.\n\nAWS supports detection for the following languages: English, Arabic, Russian, German, French, Italian, Portuguese and Spanish. GCP allows for a wider range of languages, with varying levels of support which can be found on the [official documentation](https://cloud.google.com/vision/docs/languages/).\n',
          ),
      ])
      .describe(
        '\nWhich AI provider to leverage. Valid values are `"aws"` and `"gcp"`.\n\nTransloadit outsources this task and abstracts the interface so you can expect the same data structures, but different latencies and information being returned. Different cloud vendors have different areas they shine in, and we recommend to try out and see what yields the best results for your use case.\n\nAWS supports detection for the following languages: English, Arabic, Russian, German, French, Italian, Portuguese and Spanish. GCP allows for a wider range of languages, with varying levels of support which can be found on the [official documentation](https://cloud.google.com/vision/docs/languages/).\n',
      ),
    granularity: z
      .union([z.any(), z.enum(['full', 'list'])])
      .describe(
        '\nWhether to return a full response including coordinates for the text (`"full"`), or a flat list of the extracted phrases (`"list"`). This parameter has no effect if the `format` parameter is set to `"text"`.\n',
      )
      .default('full'),
    format: z
      .union([z.any(), z.enum(['json', 'meta', 'text'])])
      .describe(
        '\nIn what format to return the extracted text.\n- `"json"` returns a JSON file.\n- `"meta"` does not return a file, but stores the data inside Transloadit\'s file object (under `${file.meta.recognized_text}`, which is an array of strings) that\'s passed around between encoding <dfn>Steps</dfn>, so that you can use the values to burn the data into videos, filter on them, etc.\n- `"text"` returns the recognized text as a plain UTF-8 encoded text file.\n',
      )
      .default('json'),
  })
  .strict()

```

#### `/document/split`

[/document/split docs](https://transloadit.com/docs/robots/document-split/)

Robot Parameter Zod Schema:

```ts
const documentSplitSchema = z
  .object({
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    robot: z.literal('/document/split'),
    pages: z
      .union([
        z.any(),
        z.union([z.any(), z.string()]),
        z.union([z.any(), z.array(z.union([z.any(), z.string()]))]),
      ])
      .describe(
        'The pages to select from the input PDF and to be included in the output PDF. Each entry can be a single page number (e.g. 5), or a range (e.g. `5-10`). Page numbers start at 1. By default all pages are extracted.',
      )
      .optional(),
  })
  .strict()

```

#### `/document/thumbs`

[/document/thumbs docs](https://transloadit.com/docs/robots/document-thumbs/)

Robot Parameter Zod Schema:

```ts
const documentThumbsSchema = z
  .object({
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    imagemagick_stack: z
      .union([
        z.any(),
        z.union([z.any(), z.literal('v3')]),
        z.union([
          z.any(),
          z.string().regex(new RegExp('^v?[23](\\.\\d+)?(\\.\\d+)?$')),
        ]),
      ])
      .default('v3'),
    robot: z
      .literal('/document/thumbs')
      .describe(
        '\n## Things to keep in mind\n\n- If you convert a multi-page PDF file into several images, all result images will be sorted with the first image being the thumbnail of the first document page, etc.\n- You can also check the `meta.thumb_index` key of each result image to find out which page it corresponds to. Keep in mind that these thumb indices **start at 0,** not at 1.\n',
      ),
    page: z
      .union([
        z.union([
          z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
          z.any(),
          z.number().int(),
        ]),
        z.null(),
      ])
      .describe(
        '\nThe PDF page that you want to convert to an image. By default the value is `null` which means that all pages will be converted into images.\n',
      )
      .default(null),
    format: z
      .union([z.any(), z.enum(['gif', 'jpeg', 'jpg', 'png'])])
      .describe(
        '\nThe format of the extracted image(s).\n\nIf you specify the value `"gif"`, then an animated gif cycling through all pages is created. Please check out [this demo](https://transloadit.com/demos/document-processing/convert-all-pages-of-a-document-into-an-animated-gif/) to learn more about this.\n',
      )
      .default('png'),
    delay: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gte(0),
      ])
      .describe(
        '\nIf your output format is `"gif"` then this parameter sets the number of 100th seconds to pass before the next frame is shown in the animation. Set this to `100` for example to allow 1 second to pass between the frames of the animated gif.\n\nIf your output format is not `"gif"`, then this parameter does not have any effect.\n',
      )
      .optional(),
    width: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gte(1).lte(5000),
      ])
      .describe(
        '\nWidth of the new image, in pixels. If not specified, will default to the width of the input image\n',
      )
      .optional(),
    height: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gte(1).lte(5000),
      ])
      .describe(
        '\nHeight of the new image, in pixels. If not specified, will default to the height of the input image\n',
      )
      .optional(),
    resize_strategy: z
      .union([
        z.any(),
        z.enum(['crop', 'fillcrop', 'fit', 'min_fit', 'pad', 'stretch']),
      ])
      .describe(
        '\nOne of the [available resize strategies](https://transloadit.com/docs/topics/resize-strategies/).\n',
      )
      .default('pad'),
    background: z
      .union([z.any(), z.string()])
      .describe(
        '\nEither the hexadecimal code or [name](https://www.imagemagick.org/script/color.php#color_names) of the color used to fill the background (only used for the pad resize strategy).\n\nBy default, the background of transparent images is changed to white. For details about how to preserve transparency across all image types, see [this demo](https://transloadit.com/demos/image-manipulation/properly-preserve-transparency-across-all-image-types/).\n',
      )
      .default('#FFFFFF'),
    alpha: z
      .union([z.any(), z.enum(['Remove', 'Set'])])
      .describe(
        '\nChange how the alpha channel of the resulting image should work. Valid values are `"Set"` to enable transparency and `"Remove"` to remove transparency.\n\nFor a list of all valid values please check the ImageMagick documentation [here](http://www.imagemagick.org/script/command-line-options.php#alpha).\n',
      )
      .optional(),
    density: z
      .union([z.any(), z.string().regex(new RegExp('\\d+(x\\d+)?'))])
      .describe(
        '\nWhile in-memory quality and file format depth specifies the color resolution, the density of an image is the spatial (space) resolution of the image. That is the density (in pixels per inch) of an image and defines how far apart (or how big) the individual pixels are. It defines the size of the image in real world terms when displayed on devices or printed.\n\nYou can set this value to a specific `width` or in the format `width`x`height`.\n\nIf your converted image has a low resolution, please try using the density parameter to resolve that.\n',
      )
      .optional(),
    antialiasing: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nControls whether or not antialiasing is used to remove jagged edges from text or images in a document.\n',
      )
      .default(false),
    colorspace: z
      .union([
        z.any(),
        z.enum([
          'CMY',
          'CMYK',
          'Gray',
          'HCL',
          'HCLp',
          'HSB',
          'HSI',
          'HSL',
          'HSV',
          'HWB',
          'Jzazbz',
          'Lab',
          'LCHab',
          'LCHuv',
          'LMS',
          'Log',
          'Luv',
          'OHTA',
          'OkLab',
          'OkLCH',
          'Rec601YCbCr',
          'Rec709YCbCr',
          'RGB',
          'scRGB',
          'sRGB',
          'Transparent',
          'Undefined',
          'xyY',
          'XYZ',
          'YCbCr',
          'YCC',
          'YDbDr',
          'YIQ',
          'YPbPr',
          'YUV',
        ]),
      ])
      .describe(
        '\nSets the image colorspace. For details about the available values, see the [ImageMagick documentation](https://www.imagemagick.org/script/command-line-options.php#colorspace).\n\nPlease note that if you were using `"RGB"`, we recommend using `"sRGB"`. ImageMagick might try to find the most efficient `colorspace` based on the color of an image, and default to e.g. `"Gray"`. To force colors, you might then have to use this parameter.\n',
      )
      .optional(),
    trim_whitespace: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        "\nThis determines if additional whitespace around the PDF should first be trimmed away before it is converted to an image. If you set this to `true` only the real PDF page contents will be shown in the image.\n\nIf you need to reflect the PDF's dimensions in your image, it is generally a good idea to set this to `false`.\n",
      )
      .default(true),
    pdf_use_cropbox: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        "\nSome PDF documents lie about their dimensions. For instance they'll say they are landscape, but when opened in decent Desktop readers, it's really in portrait mode. This can happen if the document has a cropbox defined. When this option is enabled (by default), the cropbox is leading in determining the dimensions of the resulting thumbnails.\n",
      )
      .default(true),
    turbo: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        "\nIf you set this to `false`, the robot will not emit files as they become available. This is useful if you are only interested in the final result and not in the intermediate steps.\n\nAlso, extracted pages will be resized a lot faster as they are sent off to other machines for the resizing. This is especially useful for large documents with many pages to get up to 20 times faster processing.\n\nTurbo Mode increases pricing, though, in that the input document's file size is added for every extracted page. There are no performance benefits nor increased charges for single-page documents.\n",
      )
      .default(true),
  })
  .strict()

```

#### `/dropbox/import`

[/dropbox/import docs](https://transloadit.com/docs/robots/dropbox-import/)

Robot Parameter Zod Schema:

```ts
const dropboxImportSchema = z
  .object({
    credentials: CredentialsSchema,
    ignore_errors: IgnoreErrorsSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    force_name: z
      .union([
        z.union([
          z.any(),
          z.union([z.any(), z.string()]),
          z.union([z.any(), z.array(z.union([z.any(), z.string()]))]),
        ]),
        z.null(),
      ])
      .describe(
        'Custom name for the imported file(s). By default file names are derived from the source.',
      )
      .default(null),
    robot: z.literal('/dropbox/import'),
    path: z
      .union([
        z.any(),
        z.union([z.any(), z.string()]),
        z.union([z.any(), z.array(z.union([z.any(), z.string()]))]),
      ])
      .describe(
        "\nThe path in your Dropbox to the specific file or directory. If the path points to a file, only this file will be imported. For example: `images/avatar.jpg`.\n\nIf it points to a directory, indicated by a trailing slash (`/`), then all files that are descendants of this directory are recursively imported. For example: `images/`.\n\nIf you want to import all files from the root directory, please use `/` as the value here.\n\nYou can also use an array of path strings here to import multiple paths in the same <dfn>Robot</dfn>'s <dfn>Step</dfn>.\n",
      ),
  })
  .strict()

```

#### `/dropbox/store`

[/dropbox/store docs](https://transloadit.com/docs/robots/dropbox-store/)

Robot Parameter Zod Schema:

```ts
const dropboxStoreSchema = z
  .object({
    credentials: CredentialsSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    robot: z.literal('/dropbox/store'),
    path: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe path at which the file is to be stored. This may include any available [Assembly variables](https://transloadit.com/docs/topics/assembly-instructions/#assembly-variables).\n',
      )
      .default('${unique_prefix}/${file.url_name}'),
    create_sharing_link: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nWhether to create a URL to this file for sharing with other people. This will overwrite the file\'s `"url"` property.\n',
      )
      .default(false),
  })
  .strict()

```

#### `/edgly/deliver`

[/edgly/deliver docs](https://transloadit.com/docs/robots/edgly-deliver/)

Robot Parameter Zod Schema:

```ts
const edglyDeliverSchema = z
  .object({
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    robot: z
      .literal('/edgly/deliver')
      .describe(
        '\nWhen you want Transloadit to tranform files on the fly, this <dfn>Robot</dfn> can cache and deliver the results close to your end-user, saving on latency and encoding volume. The use of this <dfn>Robot</dfn> is implicit when you use the <code>edgly.net</code> domain.\n',
      ),
  })
  .strict()

```

#### `/file/compress`

[/file/compress docs](https://transloadit.com/docs/robots/file-compress/)

Robot Parameter Zod Schema:

```ts
const fileCompressSchema = z
  .object({
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    robot: z.literal('/file/compress'),
    format: z
      .union([z.any(), z.enum(['tar', 'zip'])])
      .describe(
        '\nThe format of the archive to be created. Supported values are `"tar"` and `"zip"`.\n\nNote that `"tar"` without setting `gzip` to `true` results in an archive that\'s not compressed in any way.\n',
      )
      .default('tar'),
    gzip: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nDetermines if the result archive should also be gzipped. Gzip compression is only applied if you use the `"tar"` format.\n',
      )
      .default(false),
    password: z
      .union([z.union([z.any(), z.string()]), z.null()])
      .describe(
        '\nThis allows you to encrypt all archive contents with a password and thereby protect it against unauthorized use. To unzip the archive, the user will need to provide the password in a text input field prompt.\n\nThis parameter has no effect if the format parameter is anything other than `"zip"`.\n',
      )
      .default(null),
    compression_level: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gte(-9).lte(0),
      ])
      .describe(
        '\nDetermines how fiercely to try to compress the archive. `-0` is compressionless, which is suitable for media that is already compressed. `-1` is fastest with lowest compression. `-9` is slowest with the highest compression.\n\nIf you are using `-0` in combination with the `tar` format with `gzip` enabled, consider setting `gzip: false` instead. This results in a plain Tar archive, meaning it already has no compression.\n',
      )
      .default(-6),
    file_layout: z
      .union([z.any(), z.enum(['advanced', 'simple', 'relative-path'])])
      .describe(
        '\nDetermines if the result archive should contain all files in one directory (value for this is `"simple"`) or in subfolders according to the explanation below (value for this is `"advanced"`). The `"relative-path"` option preserves the relative directory structure of the input files.\n\nFiles with same names are numbered in the `"simple"` file layout to avoid naming collisions.\n',
      )
      .default('advanced'),
    archive_name: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe name of the archive file to be created (without the file extension).\n',
      )
      .optional(),
  })
  .strict()

```

#### `/file/decompress`

[/file/decompress docs](https://transloadit.com/docs/robots/file-decompress/)

Robot Parameter Zod Schema:

```ts
const fileDecompressSchema = z
  .object({
    ignore_errors: IgnoreErrorsSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    robot: z
      .literal('/file/decompress')
      .describe(
        '\nThis Robot supports the following archive formats:\n\n- ZIP archives (with uncompressed or "deflate"-compressed entries)\n- 7-Zip archives\n- RAR archives\n- GNU tar format (including GNU long filenames, long link names, and sparse files)\n- Solaris 9 extended tar format (including ACLs)\n- Old V7 tar archives\n- POSIX ustar\n- POSIX pax interchange format\n- POSIX octet-oriented cpio\n- SVR4 ASCII cpio\n- POSIX octet-oriented cpio\n- Binary cpio (big-endian or little-endian)\n- ISO9660 CD-ROM images (with optional Rockridge or Joliet extensions)\n- GNU and BSD "ar" archives\n- "mtree" format\n- Microsoft CAB format\n- LHA and LZH archives\n- XAR archives\n\nThis <dfn>Robot</dfn> also detects and handles any of the following before evaluating the archive file:\n\n- uuencoded files\n- Files with RPM wrapper\n- gzip compression\n- bzip2 compression\n- compress/LZW compression\n- lzma, lzip, and xz compression\n\nFor security reasons, archives that contain symlinks to outside the archived dir, will error out the <dfn>Assembly</dfn>. Decompressing password-protected archives (encrypted archives) is currently not fully supported but will not cause an <dfn>Assembly</dfn> to fail.\n',
      ),
  })
  .strict()

```

#### `/file/filter`

[/file/filter docs](https://transloadit.com/docs/robots/file-filter/)

Robot Parameter Zod Schema:

```ts
const fileFilterSchema = z
  .object({
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    robot: z
      .literal('/file/filter')
      .describe(
        '\nThink of this <dfn>Robot</dfn> as an `if/else` condition for building advanced file conversion workflows. With it, you can filter and direct certain uploaded files depending on their metadata.\n\nThe <dfn>Robot</dfn> has two modes of operation:\n\n- Constructing conditions out of arrays with 3 members each. For example, `["${file.size}", "<=", "720"]`\n- Writing conditions in JavaScript. For example, `${file.size <= 720}`. See also [Dynamic Evaluation](https://transloadit.com/docs/topics/dynamic-evaluation/).\n\nPassing JavaScript allows you to implement logic as complex as you wish, however it’s slower than combining arrays of conditions, and will be charged for per invocation via [🤖/script/run](https://transloadit.com/docs/robots/script-run/).\n\n### Conditions as arrays\n\nThe `accepts` and `declines` parameters can each be set to an array of arrays with three members:\n\n1. A value or job variable, such as `${file.mime}`\n2. One of the following operators: `==`, `===`, `<`, `>`, `<=`, `>=`, `!=`, `!==`, `regex`, `!regex`\n3. A value or job variable, such as `50` or `"foo"`\n\nExamples:\n\n- `[["${file.meta.width}", ">", "${file.meta.height}"]]`\n- `[["${file.size}", "<=", "720"]]`\n- `[["720", ">=", "${file.size}"]]`\n- `[["${file.mime}", "regex", "image"]]`\n\n> [!Warning]\n> If you would like to match against a `null` value or a value that is not present (like an audio file does not have a `video_codec` property in its metadata), match against `""` (an empty string) instead. We’ll support proper matching against `null` in the future, but we cannot easily do so right now without breaking backwards compatibility.\n\n### Conditions as JavaScript\n\nThe `accepts` and `declines` parameters can each be set to strings of JavaScript, which return a boolean value.\n\nExamples:\n\n- `${file.meta.width > file.meta.height}`\n- `${file.size <= 720}`\n- `${/image/.test(file.mime)}`\n- `${Math.max(file.meta.width, file.meta.height) > 100}`\n\nAs indicated, we charge for this via [🤖/script/run](https://transloadit.com/docs/robots/script-run/). See also [Dynamic Evaluation](https://transloadit.com/docs/topics/dynamic-evaluation/) for more details on allowed syntax and behavior.\n',
      ),
    accepts: z
      .union([
        z.any(),
        z.null(),
        z.union([z.any(), z.string()]),
        z.union([
          z.any(),
          z.array(
            z.union([
              z.any(),
              z.tuple([
                z.union([
                  z.any(),
                  z.union([z.any(), z.string()]),
                  z.union([
                    z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                    z.any(),
                    z.number(),
                  ]),
                  z.null(),
                  z.union([
                    z.any(),
                    z.array(
                      z.union([
                        z.any(),
                        z.union([z.any(), z.string()]),
                        z.union([
                          z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                          z.any(),
                          z.number(),
                        ]),
                        z.null(),
                      ]),
                    ),
                  ]),
                ]),
                z.union([
                  z.any(),
                  z
                    .union([
                      z.any(),
                      z.literal('=').describe('Equals without type check'),
                    ])
                    .describe('Equals without type check'),
                  z
                    .union([
                      z.any(),
                      z.literal('==').describe('Equals without type check'),
                    ])
                    .describe('Equals without type check'),
                  z
                    .union([
                      z.any(),
                      z
                        .literal('===')
                        .describe('Strict equals with type check'),
                    ])
                    .describe('Strict equals with type check'),
                  z
                    .union([z.any(), z.literal('<').describe('Less than')])
                    .describe('Less than'),
                  z
                    .union([z.any(), z.literal('>').describe('Greater than')])
                    .describe('Greater than'),
                  z
                    .union([z.any(), z.literal('<=').describe('Less or equal')])
                    .describe('Less or equal'),
                  z
                    .union([
                      z.any(),
                      z.literal('>=').describe('Greater or equal'),
                    ])
                    .describe('Greater or equal'),
                  z
                    .union([
                      z.any(),
                      z
                        .literal('!=')
                        .describe('Simple inequality check without type check'),
                    ])
                    .describe('Simple inequality check without type check'),
                  z
                    .union([
                      z.any(),
                      z
                        .literal('!==')
                        .describe('Strict inequality check with type check'),
                    ])
                    .describe('Strict inequality check with type check'),
                  z
                    .union([
                      z.any(),
                      z
                        .literal('regex')
                        .describe(
                          'Case-insensitive regular expression based on [RE2](https://github.com/google/re2) `.match()`',
                        ),
                    ])
                    .describe(
                      'Case-insensitive regular expression based on [RE2](https://github.com/google/re2) `.match()`',
                    ),
                  z
                    .union([
                      z.any(),
                      z
                        .literal('!regex')
                        .describe(
                          'Case-insensitive regular expression based on [RE2](https://github.com/google/re2) `!.match()`',
                        ),
                    ])
                    .describe(
                      'Case-insensitive regular expression based on [RE2](https://github.com/google/re2) `!.match()`',
                    ),
                  z
                    .union([
                      z.any(),
                      z
                        .literal('includes')
                        .describe(
                          'Check if the right element is included in the array, which is represented by the left element',
                        ),
                    ])
                    .describe(
                      'Check if the right element is included in the array, which is represented by the left element',
                    ),
                  z
                    .union([
                      z.any(),
                      z
                        .literal('!includes')
                        .describe(
                          'Check if the right element is not included in the array, which is represented by the left element',
                        ),
                    ])
                    .describe(
                      'Check if the right element is not included in the array, which is represented by the left element',
                    ),
                  z
                    .union([
                      z.any(),
                      z
                        .literal('empty')
                        .describe(
                          'Check if the left element is an empty array, an object without properties, an empty string, the number zero or the boolean false. Leave the third element of the array to be an empty string. It won’t be evaluated.',
                        ),
                    ])
                    .describe(
                      'Check if the left element is an empty array, an object without properties, an empty string, the number zero or the boolean false. Leave the third element of the array to be an empty string. It won’t be evaluated.',
                    ),
                  z
                    .union([
                      z.any(),
                      z
                        .literal('!empty')
                        .describe(
                          'Check if the left element is an array with members, an object with at least one property, a non-empty string, a number that does not equal zero or the boolean true. Leave the third element of the array to be an empty string. It won’t be evaluated.',
                        ),
                    ])
                    .describe(
                      'Check if the left element is an array with members, an object with at least one property, a non-empty string, a number that does not equal zero or the boolean true. Leave the third element of the array to be an empty string. It won’t be evaluated.',
                    ),
                ]),
                z.union([
                  z.any(),
                  z.union([z.any(), z.any()]),
                  z.union([
                    z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                    z.any(),
                    z.any(),
                  ]),
                  z.any(),
                  z.union([
                    z.any(),
                    z.array(
                      z.union([
                        z.any(),
                        z.union([z.any(), z.any()]),
                        z.union([
                          z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                          z.any(),
                          z.any(),
                        ]),
                        z.any(),
                      ]),
                    ),
                  ]),
                ]),
              ]),
            ]),
          ),
        ]),
      ])
      .describe(
        '\nFiles that match at least one requirement will be accepted, or declined otherwise. If the value is `null`, all files will be accepted. If the array is empty, no files will be accepted. Example:\n\n`[["${file.mime}", "==", "image/gif"]]`.\n\nIf the `condition_type` parameter is set to `"and"`, then all requirements must match for the file to be accepted.\n\nIf `accepts` and `declines` are both provided, the requirements in `accepts` will be evaluated first, before the conditions in `declines`.\n',
      )
      .optional(),
    declines: z
      .union([
        z.any(),
        z.any(),
        z.union([z.any(), z.any()]),
        z.union([
          z.any(),
          z.array(
            z.union([
              z.any(),
              z.tuple([
                z.union([
                  z.any(),
                  z.union([z.any(), z.any()]),
                  z.union([
                    z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                    z.any(),
                    z.any(),
                  ]),
                  z.any(),
                  z.union([
                    z.any(),
                    z.array(
                      z.union([
                        z.any(),
                        z.union([z.any(), z.any()]),
                        z.union([
                          z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                          z.any(),
                          z.any(),
                        ]),
                        z.any(),
                      ]),
                    ),
                  ]),
                ]),
                z.union([
                  z.any(),
                  z
                    .union([z.any(), z.any()])
                    .describe('Equals without type check'),
                  z
                    .union([z.any(), z.any()])
                    .describe('Equals without type check'),
                  z
                    .union([z.any(), z.any()])
                    .describe('Strict equals with type check'),
                  z.union([z.any(), z.any()]).describe('Less than'),
                  z.union([z.any(), z.any()]).describe('Greater than'),
                  z.union([z.any(), z.any()]).describe('Less or equal'),
                  z.union([z.any(), z.any()]).describe('Greater or equal'),
                  z
                    .union([z.any(), z.any()])
                    .describe('Simple inequality check without type check'),
                  z
                    .union([z.any(), z.any()])
                    .describe('Strict inequality check with type check'),
                  z
                    .union([z.any(), z.any()])
                    .describe(
                      'Case-insensitive regular expression based on [RE2](https://github.com/google/re2) `.match()`',
                    ),
                  z
                    .union([z.any(), z.any()])
                    .describe(
                      'Case-insensitive regular expression based on [RE2](https://github.com/google/re2) `!.match()`',
                    ),
                  z
                    .union([z.any(), z.any()])
                    .describe(
                      'Check if the right element is included in the array, which is represented by the left element',
                    ),
                  z
                    .union([z.any(), z.any()])
                    .describe(
                      'Check if the right element is not included in the array, which is represented by the left element',
                    ),
                  z
                    .union([z.any(), z.any()])
                    .describe(
                      'Check if the left element is an empty array, an object without properties, an empty string, the number zero or the boolean false. Leave the third element of the array to be an empty string. It won’t be evaluated.',
                    ),
                  z
                    .union([z.any(), z.any()])
                    .describe(
                      'Check if the left element is an array with members, an object with at least one property, a non-empty string, a number that does not equal zero or the boolean true. Leave the third element of the array to be an empty string. It won’t be evaluated.',
                    ),
                ]),
                z.union([
                  z.any(),
                  z.union([z.any(), z.any()]),
                  z.union([
                    z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                    z.any(),
                    z.any(),
                  ]),
                  z.any(),
                  z.union([
                    z.any(),
                    z.array(
                      z.union([
                        z.any(),
                        z.union([z.any(), z.any()]),
                        z.union([
                          z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                          z.any(),
                          z.any(),
                        ]),
                        z.any(),
                      ]),
                    ),
                  ]),
                ]),
              ]),
            ]),
          ),
        ]),
      ])
      .describe(
        '\nFiles that match at least one requirement will be declined, or accepted otherwise. If the value is `null` or an empty array, no files will be declined. Example:\n\n`[["${file.size}",">","1024"]]`.\n\nIf the `condition_type` parameter is set to `"and"`, then all requirements must match for the file to be declined.\n\nIf `accepts` and `declines` are both provided, the requirements in `accepts` will be evaluated first, before the conditions in `declines`.\n',
      )
      .optional(),
    condition_type: z
      .union([z.any(), z.enum(['and', 'or'])])
      .describe(
        '\nSpecifies the condition type according to which the members of the `accepts` or `declines` arrays should be evaluated. Can be `"or"` or `"and"`.\n',
      )
      .default('or'),
    error_on_decline: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nIf this is set to `true` and one or more files are declined, the Assembly will be stopped and marked with an error.\n',
      )
      .default(false),
    error_msg: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe error message shown to your users (such as by Uppy) when a file is declined and `error_on_decline` is set to `true`.\n',
      )
      .default('One of your files was declined'),
  })
  .strict()

```

#### `/file/hash`

[/file/hash docs](https://transloadit.com/docs/robots/file-hash/)

Robot Parameter Zod Schema:

```ts
const fileHashSchema = z
  .object({
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    robot: z
      .literal('/file/hash')
      .describe(
        '\nThis <dfn>Robot</dfn> allows you to hash any file as part of the <dfn>Assembly</dfn> execution process. This can be useful for verifying the integrity of a file for example.\n',
      ),
    algorithm: z
      .union([
        z.any(),
        z.enum(['b2', 'md5', 'sha1', 'sha224', 'sha256', 'sha384', 'sha512']),
      ])
      .describe(
        '\nThe hashing algorithm to use.\n\nThe file hash is exported as `file.meta.hash`.\n',
      )
      .default('sha256'),
  })
  .strict()

```

#### `/file/preview`

[/file/preview docs](https://transloadit.com/docs/robots/file-preview/)

Robot Parameter Zod Schema:

```ts
const filePreviewSchema = z
  .object({
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    robot: z
      .literal('/file/preview')
      .describe(
        "\nThis <dfn>Robot</dfn>'s purpose is to generate a meaningful preview image for any file, in such a way that the resulting thumbnail highlights the file's content. The goal is not to losslessly present the original media in a smaller way. Instead, it is to maximize the chance of a person recognizing the media at a glance, while being visually pleasing and consistent with other previews. The generation process depends on the file type. For example, the <dfn>Robot</dfn> can extract artwork from media files, frames from videos, generate a waveform for audio files, and preview the content of documents and images. The details of all available strategies are provided in the next section.\n\nIf no file-specific thumbnail can be generated because the file type is not supported, a generic icon containing the file extension will be generated.\n\nThe default parameters ensure that the <dfn>Robot</dfn> always generates a preview image with the predefined dimensions and formats, to allow an easy integration into your application's UI. In addition, the generated preview images are optimized by default to reduce their file size while keeping their quality.\n",
      ),
    format: z
      .union([z.any(), z.enum(['gif', 'jpg', 'png'])])
      .describe(
        '\nThe output format for the generated thumbnail image. If a short video clip is generated using the `clip` strategy, its format is defined by `clip_format`.\n',
      )
      .default('png'),
    width: z
      .union([z.any(), z.number().int().gte(1).lte(7680)])
      .describe('\nWidth of the thumbnail, in pixels.\n')
      .default(300),
    height: z
      .union([z.any(), z.number().int().gte(1).lte(4320)])
      .describe('\nHeight of the thumbnail, in pixels.\n')
      .default(200),
    resize_strategy: z
      .union([
        z.any(),
        z.enum(['crop', 'fit', 'fillcrop', 'min_fit', 'pad', 'stretch']),
      ])
      .describe(
        '\nTo achieve the desired dimensions of the preview thumbnail, the <dfn>Robot</dfn> might have to resize the generated image. This happens, for example, when the dimensions of a frame extracted from a video do not match the chosen `width` and `height` parameters.\n\nSee the list of available [resize strategies](https://transloadit.com/docs/topics/resize-strategies/) for more details.\n',
      )
      .default('pad'),
    background: z
      .union([
        z.any(),
        z.string().regex(new RegExp('^#?[0-9a-fA-F]{6}([0-9a-fA-F]{2})?$')),
      ])
      .describe(
        '\nThe hexadecimal code of the color used to fill the background (only used for the pad resize strategy). The format is `#rrggbb[aa]` (red, green, blue, alpha). Use `#00000000` for a transparent padding.\n',
      )
      .default('#ffffffff'),
    strategy: z
      .union([
        z.any(),
        z
          .object({
            archive: z
              .union([z.any(), z.array(z.union([z.any(), z.string()]))])
              .default(['icon']),
            audio: z
              .union([z.any(), z.array(z.union([z.any(), z.string()]))])
              .default(['artwork', 'waveform', 'icon']),
            document: z
              .union([z.any(), z.array(z.union([z.any(), z.string()]))])
              .default(['page', 'icon']),
            image: z
              .union([z.any(), z.array(z.union([z.any(), z.string()]))])
              .default(['image', 'icon']),
            unknown: z
              .union([z.any(), z.array(z.union([z.any(), z.string()]))])
              .default(['icon']),
            video: z
              .union([z.any(), z.array(z.union([z.any(), z.string()]))])
              .default(['artwork', 'frame', 'icon']),
            webpage: z
              .union([z.any(), z.array(z.union([z.any(), z.string()]))])
              .default(['render', 'icon']),
          })
          .strict(),
      ])
      .describe(
        '\nDefinition of the thumbnail generation process per file category. The parameter must be an object whose keys can be one of the file categories: `audio`, `video`, `image`, `document`, `archive`, `webpage`, and `unknown`. The corresponding value is an array of strategies for the specific file category. See the above section for a list of all available strategies.\n\nFor each file, the <dfn>Robot</dfn> will attempt to use the first strategy to generate the thumbnail. If this process fails (e.g., because no artwork is available in a video file), the next strategy is attempted. This is repeated until either a thumbnail is generated or the list is exhausted. Selecting the `icon` strategy as the last entry provides a fallback mechanism to ensure that an appropriate strategy is always available.\n\nThe parameter defaults to the following definition:\n\n```json\n{\n  "audio": ["artwork", "waveform", "icon"],\n  "video": ["artwork", "frame", "icon"],\n  "document": ["page", "icon"],\n  "image": ["image", "icon"],\n  "webpage": ["render", "icon"],\n  "archive": ["icon"],\n  "unknown": ["icon"]\n}\n```\n',
      )
      .optional(),
    artwork_outer_color: z
      .union([z.any(), z.any()])
      .describe(
        "\n  The color used in the outer parts of the artwork's gradient.\n  ",
      )
      .optional(),
    artwork_center_color: z
      .union([z.any(), z.any()])
      .describe(
        "\n  The color used in the center of the artwork's gradient.\n  ",
      )
      .optional(),
    waveform_center_color: z
      .union([z.any(), z.any()])
      .describe(
        "\nThe color used in the center of the waveform's gradient. The format is `#rrggbb[aa]` (red, green, blue, alpha). Only used if the `waveform` strategy for audio files is applied.\n",
      )
      .default('#000000ff'),
    waveform_outer_color: z
      .union([z.any(), z.any()])
      .describe(
        "\nThe color used in the outer parts of the waveform's gradient. The format is `#rrggbb[aa]` (red, green, blue, alpha). Only used if the `waveform` strategy for audio files is applied.\n",
      )
      .default('#000000ff'),
    waveform_height: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gte(1).lte(5000),
      ])
      .describe(
        '\nHeight of the waveform, in pixels. Only used if the `waveform` strategy for audio files is applied. It can be utilized to ensure that the waveform only takes up a section of the preview thumbnail.\n',
      )
      .default(100),
    waveform_width: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gte(1).lte(5000),
      ])
      .describe(
        '\nWidth of the waveform, in pixels. Only used if the `waveform` strategy for audio files is applied. It can be utilized to ensure that the waveform only takes up a section of the preview thumbnail.\n',
      )
      .default(300),
    icon_style: z
      .union([z.any(), z.enum(['square', 'with-text'])])
      .describe(
        '\nThe style of the icon generated if the `icon` strategy is applied. The default style, `with-text`, includes an icon showing the file type and a text box below it, whose content can be controlled by the `icon_text_content` parameter and defaults to the file extension (e.g. MP4, JPEG). The `square` style only includes a square variant of the icon showing the file type. Below are exemplary previews generated for a text file utilizing the different styles:\n\n<br><br> <strong>`with-text` style:</strong> <br>\n![Image with text style](/assets/images/file-preview/icon-with-text.png)\n<br><br> <strong>`square` style:</strong> <br>\n![Image with square style](/assets/images/file-preview/icon-square.png)\n',
      )
      .default('with-text'),
    icon_text_color: z
      .union([z.any(), z.any()])
      .describe(
        '\nThe color of the text used in the icon. The format is `#rrggbb[aa]`. Only used if the `icon` strategy is applied.\n',
      )
      .default('#a2a2a2'),
    icon_text_font: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe font family of the text used in the icon. Only used if the `icon` strategy is applied. [Here](https://transloadit.com/docs/supported-formats/fonts/) is a list of all supported fonts.\n',
      )
      .default('Roboto'),
    icon_text_content: z
      .union([z.any(), z.enum(['extension', 'none'])])
      .describe(
        '\nThe content of the text box in generated icons. Only used if the `icon_style` parameter is set to `with-text`. The default value, `extension`, adds the file extension (e.g. MP4, JPEG) to the icon. The value `none` can be used to render an empty text box, which is useful if no text should not be included in the raster image, but some place should be reserved in the image for later overlaying custom text over the image using HTML etc.\n',
      )
      .default('extension'),
    optimize: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        "\nSpecifies whether the generated preview image should be optimized to reduce the image's file size while keeping their quaility. If enabled, the images will be optimized using [🤖/image/optimize](https://transloadit.com/docs/robots/image-optimize/).\n",
      )
      .default(true),
    optimize_priority: z
      .union([z.any(), z.enum(['compression-ratio', 'conversion-speed'])])
      .describe(
        '\nSpecifies whether conversion speed or compression ratio is prioritized when optimizing images. Only used if `optimize` is enabled. Please see the [🤖/image/optimize documentation](https://transloadit.com/docs/robots/image-optimize/#param-priority) for more details.\n',
      )
      .default('conversion-speed'),
    optimize_progressive: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nSpecifies whether images should be interlaced, which makes the result image load progressively in browsers. Only used if `optimize` is enabled. Please see the [🤖/image/optimize documentation](https://transloadit.com/docs/robots/image-optimize/#param-progressive) for more details.\n',
      )
      .default(false),
    clip_format: z
      .union([z.any(), z.enum(['apng', 'avif', 'gif', 'webp'])])
      .describe(
        '\nThe animated image format for the generated video clip. Only used if the `clip` strategy for video files is applied.\n\nPlease consult the [MDN Web Docs](https://developer.mozilla.org/en-US/docs/Web/Media/Formats/Image_types) for detailed information about the image formats and their characteristics. GIF enjoys the broadest support in software, but only supports a limit color palette. APNG supports a variety of color depths, but its lossless compression produces large images for videos. AVIF is a modern image format that offers great compression, but proper support for animations is still lacking in some browsers. WebP on the other hand, enjoys broad support while offering a great balance between small file sizes and good visual quality, making it the default clip format.\n',
      )
      .default('webp'),
    clip_offset: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().gte(0),
      ])
      .describe(
        '\nThe start position in seconds of where the clip is cut. Only used if the `clip` strategy for video files is applied. Be aware that for larger video only the first few MBs of the file may be imported to improve speed. Larger offsets may seek to a position outside of the imported part and thus fail to generate a clip.\n',
      )
      .default(1),
    clip_duration: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().gte(0),
      ])
      .describe(
        '\nThe duration in seconds of the generated video clip. Only used if the `clip` strategy for video files is applied. Be aware that a longer clip duration also results in a larger file size, which might be undesirable for previews.\n',
      )
      .default(5),
    clip_framerate: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gte(1).lte(60),
      ])
      .describe(
        '\nThe framerate of the generated video clip. Only used if the `clip` strategy for video files is applied. Be aware that a higher framerate appears smoother but also results in a larger file size, which might be undesirable for previews.\n',
      )
      .default(5),
    clip_loop: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nSpecifies whether the generated animated image should loop forever (`true`) or stop after playing the animation once (`false`). Only used if the `clip` strategy for video files is applied.\n',
      )
      .default(true),
  })
  .strict()

```

#### `/file/read`

[/file/read docs](https://transloadit.com/docs/robots/file-read/)

Robot Parameter Zod Schema:

```ts
const fileReadSchema = z
  .object({
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    robot: z
      .literal('/file/read')
      .describe(
        '\nThis <dfn>Robot</dfn> accepts any file, and will read the file using UTF-8 encoding. The result is outputted to `file.meta.content` to be accessed in later <dfn>Steps</dfn>.\n\nThe <dfn>Robot</dfn> currently only accepts files under 500KB.\n',
      ),
  })
  .strict()

```

#### `/file/serve`

[/file/serve docs](https://transloadit.com/docs/robots/file-serve/)

Robot Parameter Zod Schema:

```ts
const fileServeSchema = z
  .object({
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    robot: z
      .literal('/file/serve')
      .describe(
        "\nWhen you want Transloadit to tranform files on the fly, you can use this <dfn>Robot</dfn> to determine which <dfn>Step</dfn> of a <dfn>Template</dfn> should be served to the end-user (via a CDN), as well as set extra information on the served files, such as headers. This way you can for instance suggest the CDN for how long to keep cached copies of the result around. By default, as you can see in the `headers` parameter, we instruct browsers to cache the result for 72h (`259200` seconds) and CDNs to cache the content for 24h (`86400` seconds). These values should be adjusted to suit your use case.\n\n🤖/file/serve merely acts as the glue layer between our <dfn>Assembly</dfn> engine and serving files over HTTP. It let's you pick the proper result of a series of <dfn>Steps</dfn> via the `use` parameter and configure headers on the original content. That is where its responsibilies end, and 🤖/tlcdn/deliver, then takes over to globally distribute this original content across the globe, and make sure that is cached close to your end-users, when they make requests such as <https://my-app.tlcdn.com/resize-img/canoe.jpg?w=500>, another. 🤖/tlcdn/deliver is not a part of your <dfn>Assembly Instructions</dfn>, but it may appear on your invoices as bandwidth charges incur when distributing the cached copies. 🤖/file/serve only charges when the CDN does not have a cached copy and requests to regenerate the original content, which depending on your caching settings could be just once a month, or year, per file/transformation.\n\nWhile theoretically possible, you could use [🤖/file/serve](https://transloadit.com/docs/robots/file-serve/) directly in HTML files, but we strongly recommend against this, because if your site gets popular and the media URL that /file/serve is handling gets hit one million times, that is one million new image resizes. Wrapping it with a CDN (and thanks to the caching that comes with it) makes sure encoding charges stay low, as well as latencies.\n\nAlso consider configuring caching headers and cache-control directives to control how content is cached and invalidated on the CDN edge servers, balancing between freshness and efficiency.\n\n## Smart CDN Security with Signature Authentication\n\nYou can leverage [Signature Authentication](https://transloadit.com/docs/api/authentication/#smart-cdn) to avoid abuse of our encoding platform. Below is a quick Node.js example using our Node SDK, but there are [examples for other languages and SDKs](https://transloadit.com/docs/api/authentication/#example-code) as well.\n\n```javascript\n// yarn add transloadit\n// or\n// npm install --save transloadit\n\nimport { Transloadit } from 'transloadit'\n\nconst transloadit = new Transloadit({\n  authKey: 'YOUR_TRANSLOADIT_KEY',\n  authSecret: 'YOUR_TRANSLOADIT_SECRET',\n})\n\nconst url = transloadit.getSignedSmartCDNUrl({\n  workspace: 'YOUR_WORKSPACE',\n  template: 'YOUR_TEMPLATE',\n  input: 'image.png',\n  urlParams: { height: 100, width: 100 },\n})\n\nconsole.log(url)\n```\n\nThis will generate a signed Smart CDN URL that includes authentication parameters, preventing unauthorized access to your transformation endpoints.\n\n## More information\n\n- [Content Delivery](https://transloadit.com/services/content-delivery/)\n- [🤖/file/serve](https://transloadit.com/docs/robots/file-serve/) pricing\n- [🤖/tlcdn/deliver](https://transloadit.com/docs/robots/tlcdn-deliver/) pricing\n- [File Preview Feature](https://transloadit.com/blog/2024/06/file-preview-with-smart-cdn/) blog post\n",
      ),
    headers: z
      .record(z.union([z.any(), z.string()]))
      .describe(
        '\nAn object containing a list of headers to be set for a file as we serve it to a CDN/web browser, such as `{ FileURL: "${file.url_name}" }` which will be merged over the defaults, and can include any available [Assembly Variable](https://transloadit.com/docs/topics/assembly-instructions/#assembly-variables).\n',
      )
      .default({
        'Access-Control-Allow-Headers':
          'X-Requested-With, Content-Type, Cache-Control, Accept, Content-Length, Transloadit-Client, Authorization',
        'Access-Control-Allow-Methods': 'POST, GET, PUT, DELETE, OPTIONS',
        'Access-Control-Allow-Origin': '*',
        'Cache-Control': 'public, max-age=259200, s-max-age=86400',
        'Content-Type': '${file.mime}; charset=utf-8',
        'Transfer-Encoding': 'chunked',
        'Transloadit-Assembly': '…',
        'Transloadit-RequestID': '…',
      }),
  })
  .strict()

```

#### `/file/verify`

[/file/verify docs](https://transloadit.com/docs/robots/file-verify/)

Robot Parameter Zod Schema:

```ts
const fileVerifySchema = z
  .object({
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    robot: z.literal('/file/verify'),
    error_on_decline: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nIf this is set to `true` and one or more files are declined, the Assembly will be stopped and marked with an error.\n',
      )
      .default(false),
    error_msg: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe error message shown to your users (such as by Uppy) when a file is declined and `error_on_decline` is set to `true`.\n',
      )
      .default('One of your files was declined'),
    verify_to_be: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe type that you want to match against to ensure your file is of this type. For example, `image` will verify whether uploaded files are images. This also works against file media types, in this case `image/png` would also work to match against specifically `png` files.\n',
      )
      .default('pdf'),
  })
  .strict()

```

#### `/file/virusscan`

[/file/virusscan docs](https://transloadit.com/docs/robots/file-virusscan/)

Robot Parameter Zod Schema:

```ts
const fileVirusscanSchema = z
  .object({
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    robot: z
      .literal('/file/virusscan')
      .describe(
        '\n      This <dfn>Robot</dfn> is built on top of [ClamAV](https://www.clamav.net/), the best open source antivirus engine available. We update its signatures on a daily basis.\n\nBy default, this <dfn>Robot</dfn> excludes all malicious files from further processing without any additional notification. This behavior can be changed by setting `error_on_decline` to `true`, which will stop <dfn>Assemblies</dfn> as soon as malicious files are found. Such <dfn>Assemblies</dfn> will then be marked with an error.\n\nWe allow the use of industry standard [EICAR files](https://www.eicar.org/download-anti-malware-testfile/) for integration testing without needing to use potentially dangerous live virus samples.\n',
      ),
    error_on_decline: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nIf this is set to `true` and one or more files are declined, the Assembly will be stopped and marked with an error.\n',
      )
      .default(false),
    error_msg: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe error message shown to your users (such as by Uppy) when a file is declined and `error_on_decline` is set to `true`.\n',
      )
      .default('One of your files was declined'),
  })
  .strict()

```

#### `/ftp/import`

[/ftp/import docs](https://transloadit.com/docs/robots/ftp-import/)

Robot Parameter Zod Schema:

```ts
const ftpImportSchema = z
  .object({
    credentials: CredentialsSchema,
    ignore_errors: IgnoreErrorsSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    force_name: z
      .union([
        z.union([
          z.any(),
          z.union([z.any(), z.string()]),
          z.union([z.any(), z.array(z.union([z.any(), z.string()]))]),
        ]),
        z.null(),
      ])
      .describe(
        'Custom name for the imported file(s). By default file names are derived from the source.',
      )
      .default(null),
    host: z.union([z.any(), z.string()]).optional(),
    port: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gte(1).lte(65535),
      ])
      .describe('The port to use for the FTP connection.')
      .default(21),
    user: z.union([z.any(), z.string()]).optional(),
    password: z.union([z.any(), z.string()]).optional(),
    robot: z.literal('/ftp/import'),
    path: z
      .union([
        z.any(),
        z.union([z.any(), z.string()]),
        z.union([z.any(), z.array(z.union([z.any(), z.string()]))]),
      ])
      .describe(
        '\nThe path on your FTP server where to search for files. Files are imported recursively from all sub-directories and sub-sub-directories (and so on) from this path.\n',
      ),
    passive_mode: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nDetermines if passive mode should be used for the FTP connection.\n',
      )
      .default(true),
  })
  .strict()

```

#### `/ftp/store`

[/ftp/store docs](https://transloadit.com/docs/robots/ftp-store/)

Robot Parameter Zod Schema:

```ts
const ftpStoreSchema = z
  .object({
    credentials: CredentialsSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    host: z.union([z.any(), z.string()]).optional(),
    port: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gte(1).lte(65535),
      ])
      .describe('The port to use for the FTP connection.')
      .default(21),
    user: z.union([z.any(), z.string()]).optional(),
    password: z.union([z.any(), z.string()]).optional(),
    robot: z.literal('/ftp/store'),
    path: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe path at which the file is to be stored. This can contain any available [Assembly variables](https://transloadit.com/docs/topics/assembly-instructions/#assembly-variables).\n\nPlease note that you might need to include your homedir at the beginning of the path.\n',
      )
      .default('${unique_prefix}/${file.url_name}'),
    url_template: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe URL of the file in the result JSON. The following [Assembly variables](https://transloadit.com/docs/topics/assembly-instructions/#assembly-variables) are supported.\n',
      )
      .default('https://{HOST}/{PATH}'),
    ssl_url_template: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe SSL URL of the file in the result JSON. The following [Assembly variables](https://transloadit.com/docs/topics/assembly-instructions/#assembly-variables) are supported.\n',
      )
      .default('https://{HOST}/{PATH}'),
    secure: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nDetermines whether to establish a secure connection to the FTP server using SSL.\n',
      )
      .default(false),
  })
  .strict()

```

#### `/google/import`

[/google/import docs](https://transloadit.com/docs/robots/google-import/)

Robot Parameter Zod Schema:

```ts
const googleImportSchema = z
  .object({
    credentials: CredentialsSchema,
    ignore_errors: IgnoreErrorsSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    force_name: z
      .union([
        z.union([
          z.any(),
          z.union([z.any(), z.string()]),
          z.union([z.any(), z.array(z.union([z.any(), z.string()]))]),
        ]),
        z.null(),
      ])
      .describe(
        'Custom name for the imported file(s). By default file names are derived from the source.',
      )
      .default(null),
    robot: z.literal('/google/import'),
    path: z
      .union([
        z.any(),
        z.union([z.any(), z.string()]),
        z.union([z.any(), z.array(z.union([z.any(), z.string()]))]),
      ])
      .describe(
        "\nThe path in your bucket to the specific file or directory. If the path points to a file, only this file will be imported. For example: `images/avatar.jpg`.\n\nIf it points to a directory, indicated by a trailing slash (`/`), then all files that are direct descendants of this directory will be imported. For example: `images/`.\n\nDirectories are **not** imported recursively. If you want to import files from subdirectories and sub-subdirectories, enable the `recursive` parameter.\n\nIf you want to import all files from the root directory, please use `/` as the value here. In this case, make sure all your objects belong to a path. If you have objects in the root of your bucket that aren't prefixed with `/`, you'll receive a 404 `GOOGLE_IMPORT_NOT_FOUND` error.\n\nYou can also use an array of path strings here to import multiple paths in the same <dfn>Robot</dfn>'s <dfn>Step</dfn>.\n",
      ),
    recursive: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nSetting this to `true` will enable importing files from subdirectories and sub-subdirectories (etc.) of the given path.\n\nPlease use the pagination parameters `start_file_name` and `files_per_page` wisely here.\n',
      )
      .default(false),
    next_page_token: z
      .union([z.any(), z.string()])
      .describe(
        '\nA string token used for pagination. The returned files of one paginated call have the next page token inside of their meta data, which needs to be used for the subsequent paging call.\n',
      )
      .default(''),
    files_per_page: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int(),
      ])
      .describe(
        '\nThe pagination page size. This only works when recursive is `true` for now, in order to not break backwards compatibility in non-recursive imports.\n',
      )
      .default(1000),
  })
  .strict()

```

#### `/google/store`

[/google/store docs](https://transloadit.com/docs/robots/google-store/)

Robot Parameter Zod Schema:

```ts
const googleStoreSchema = z
  .object({
    credentials: CredentialsSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    robot: z
      .literal('/google/store')
      .describe(
        "\nThe URL to the exported file in your Google bucket will be presented in the Transloadit <dfn>Assembly Status</dfn> JSON. This <dfn>Robot</dfn> can also be used to export encoded files to Google's Firebase as demonstrated in [this blogpost](https://transloadit.com/blog/2018/12/2h-youtube-clone/).\n",
      ),
    path: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe path at which the file is to be stored. This may include any available [Assembly Variables](https://transloadit.com/docs/topics/assembly-instructions/#assembly-variables).\n',
      )
      .default('${unique_prefix}/${file.url_name}'),
    acl: z
      .union([
        z.union([
          z.any(),
          z.enum([
            'authenticated-read',
            'bucket-owner-full-control',
            'private',
            'project-private',
            'public-read',
          ]),
        ]),
        z.null(),
      ])
      .describe('\nThe permissions used for this file.\n')
      .default('public-read'),
    cache_control: z
      .union([z.any(), z.string()])
      .describe(
        "\nThe `Cache-Control` header determines how long browsers are allowed to cache your object for. Values specified with this parameter will be added to the object's metadata under the `Cache-Control` header. For more information on valid values, take a look at the [official Google documentation](https://cloud.google.com/storage/docs/metadata#cache-control).\n",
      )
      .optional(),
    url_template: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe URL of the file in the result JSON. This may include any of the following supported [Assembly variables](https://transloadit.com/docs/topics/assembly-instructions/#assembly-variables).\n',
      )
      .default('https://{HOST}/{PATH}'),
    ssl_url_template: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe SSL URL of the file in the result JSON. The following [Assembly variables](https://transloadit.com/docs/topics/assembly-instructions/#assembly-variables) are supported.\n',
      )
      .default('https://{HOST}/{PATH}'),
  })
  .strict()

```

#### `/html/convert`

[/html/convert docs](https://transloadit.com/docs/robots/html-convert/)

Robot Parameter Zod Schema:

```ts
const htmlConvertSchema = z
  .object({
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    robot: z
      .literal('/html/convert')
      .describe(
        '\nA URL can be provided instead of an input HTML file, to capture a screenshot from the website referenced by the URL.\n\nUse [🤖/image/resize](https://transloadit.com/docs/robots/image-resize/) to resize or crop the screenshot as needed.\n',
      ),
    url: z
      .union([z.union([z.any(), z.string()]), z.null()])
      .describe(
        '\nThe URL of the web page to be converted. Optional, as you can also upload/import HTML files and pass it to this <dfn>Robot</dfn>.\n',
      )
      .default(null),
    format: z
      .union([z.any(), z.enum(['jpeg', 'jpg', 'pdf', 'png'])])
      .describe('\nThe format of the resulting image.\n')
      .default('png'),
    fullpage: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nDetermines if a screenshot of the full page should be taken or not.\n\nIf set to `true`, the `height` parameter will not have any effect, as heights of websites vary. You can control the size of the resulting image somewhat, though, by setting the `width` parameter.\n\nIf set to `false`, an image will be cropped from the top of the webpage according to your `width` and `height` parameters.\n',
      )
      .default(true),
    omit_background: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        "\nDetermines whether to preserve a transparent background in HTML pages. Useful if you're generating artwork in HTML that you want to overlay on e.g. a video.\n\nThe default of `false` fills transparent areas with a white background, for easier reading/printing.\n\nThis parameter is only used when `format` is not `pdf`.\n",
      )
      .default(false),
    width: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gte(1),
      ])
      .describe(
        '\nThe screen width that will be used, in pixels. Change this to change the  dimensions of the resulting image.\n',
      )
      .default(1024),
    height: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gte(1),
      ])
      .describe(
        '\nThe screen height that will be used, in pixels. By default this equals the length of the web page in pixels if `fullpage` is set to `true`. If `fullpage` is set to `false`, the height parameter takes effect and defaults to the value `768`.\n',
      )
      .optional(),
    delay: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gte(0),
      ])
      .describe(
        '\nThe delay (in milliseconds) applied to allow the page and all of its JavaScript to render before taking the screenshot.\n',
      )
      .default(0),
    headers: z
      .record(z.union([z.any(), z.string()]))
      .describe(
        '\nAn object containing optional headers that will be passed along with the original request to the website. For example, this parameter can be used to pass along an authorization token along with the request.\n',
      )
      .optional(),
    wait_until: z
      .union([
        z.any(),
        z.enum(['domcontentloaded', 'load', 'networkidle', 'commit']),
      ])
      .describe(
        "\nThe event to wait for before taking the screenshot. Used for loading Javascript, and images.\n\nSee [Playwright's documentation](https://playwright.dev/docs/api/class-page#page-wait-for-load-state) for more information.\n",
      )
      .default('networkidle'),
  })
  .strict()

```

#### `/http/import`

[/http/import docs](https://transloadit.com/docs/robots/http-import/)

Robot Parameter Zod Schema:

```ts
const httpImportSchema = z
  .object({
    ignore_errors: IgnoreErrorsSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    force_name: z
      .union([
        z.union([
          z.any(),
          z.union([z.any(), z.string()]),
          z.union([z.any(), z.array(z.union([z.any(), z.string()]))]),
        ]),
        z.null(),
      ])
      .describe(
        'Custom name for the imported file(s). By default file names are derived from the source.',
      )
      .default(null),
    robot: z
      .literal('/http/import')
      .describe(
        '\nThe result of this <dfn>Robot</dfn> will carry a field `import_url` in their metadata, which references the URL from which they were imported. Further conversion results that use this file will also carry this `import_url` field. This allows you to to match conversion results with the original import URL that you used.\n\nThis <dfn>Robot</dfn> knows to interpret links to files on these services:\n\n- Dropbox\n- Google Drive\n- Google Docs\n- OneDrive\n\nInstead of downloading the HTML page previewing the file, the actual file itself will be imported.\n',
      ),
    url: z
      .union([
        z.any(),
        z.union([z.any(), z.string().url()]),
        z.union([z.any(), z.array(z.union([z.any(), z.string().url()]))]),
      ])
      .describe(
        '\nThe URL from which the file to be imported can be retrieved.\n\nYou can also specify an array of URLs or a string of `|` delimited URLs to import several files at once. Please also check the `url_delimiter` parameter for that.\n',
      ),
    url_delimiter: z
      .union([z.any(), z.string()])
      .describe(
        '\nProvides the delimiter that is used to split the URLs in your `url` parameter value.\n',
      )
      .default('|'),
    headers: z
      .union([
        z.any(),
        z.union([z.any(), z.array(z.union([z.any(), z.string()]))]),
        z.union([z.any(), z.array(z.record(z.union([z.any(), z.string()])))]),
        z.union([z.any(), z.string()]),
      ])
      .describe(
        '\nCustom headers to be sent for file import.\n\nThis is an empty array by default, such that no additional headers except the necessary ones (e.g. Host) are sent.\n\nHeaders can be specified as:\n- An array of strings in the format "Header-Name: value"\n- An array of objects with header names as keys and values as values\n- A JSON string that will be parsed into an object\n',
      )
      .default([]),
    import_on_errors: z
      .union([z.any(), z.array(z.union([z.any(), z.string()]))])
      .describe(
        '\nSetting this to `"meta"` will still import the file on metadata extraction errors. `ignore_errors` is similar, it also ignores the error and makes sure the Robot doesn\'t stop, but it doesn\'t import the file.\n',
      )
      .default([]),
    fail_fast: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        "\nDisable the internal retry mechanism, and fail immediately if a resource can't be imported. This can be useful for performance critical applications.\n",
      )
      .default(false),
    return_file_stubs: z
      .union([
        z.any(),
        z.union([
          z
            .boolean()
            .describe(
              '\nIf set to `true`, the Robot will not yet import the actual files but instead return an empty file stub that includes a URL from where the file can be imported by subsequent Robots. This is useful for cases where subsequent Steps need more control over the import process, such as with 🤖/video/ondemand. This parameter should only be set if all subsequent Steps use Robots that support file stubs.\n',
            ),
          z.any(),
        ]),
      ])
      .describe(
        '\nIf set to `true`, the Robot will not yet import the actual files but instead return an empty file stub that includes a URL from where the file can be imported by subsequent Robots. This is useful for cases where subsequent Steps need more control over the import process, such as with 🤖/video/ondemand. This parameter should only be set if all subsequent Steps use Robots that support file stubs.\n',
      )
      .default(false),
    range: z
      .union([
        z.any(),
        z.union([z.any(), z.string()]),
        z.union([z.any(), z.array(z.union([z.any(), z.string()]))]),
      ])
      .describe(
        '\nAllows you to specify one or more byte ranges to import from the file. The server must support range requests for this to work.\n\n**Single range**: Use a string like `"0-99"` to import bytes 0-99 (the first 100 bytes).\n\n**Multiple ranges**: Use an array like `["0-99", "200-299"]` to import multiple separate ranges. The resulting file will contain all requested ranges concatenated together, with zero bytes (\\0) filling any gaps between non-contiguous ranges.\n\n**Range formats**:\n- `"0-99"`: Bytes 0 through 99 (inclusive)\n- `"100-199"`: Bytes 100 through 199 (inclusive)\n- `"-100"`: The last 100 bytes of the file\n\n**Important notes**:\n- The server must support HTTP range requests (respond with 206 Partial Content)\n- If the server doesn\'t support range requests, the entire file will be imported instead\n- Overlapping ranges are allowed and will be included as requested\n- The resulting file size will be the highest byte position requested, with gaps filled with zero bytes\n',
      )
      .optional(),
  })
  .strict()

```

#### `/image/bgremove`

[/image/bgremove docs](https://transloadit.com/docs/robots/image-bgremove/)

Robot Parameter Zod Schema:

```ts
const imageBgremoveSchema = z
  .object({
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    robot: z.literal('/image/bgremove'),
    select: z
      .union([z.any(), z.enum(['foreground', 'background'])])
      .describe(
        'Region to select and keep in the image. The other region is removed.',
      )
      .optional(),
    format: z
      .union([z.any(), z.enum(['png', 'gif', 'webp'])])
      .describe('Format of the generated image.')
      .optional(),
    provider: z
      .union([z.any(), z.enum(['transloadit', 'replicate', 'fal'])])
      .describe('Provider to use for removing the background.')
      .optional(),
  })
  .strict()

```

#### `/image/describe`

[/image/describe docs](https://transloadit.com/docs/robots/image-describe/)

Robot Parameter Zod Schema:

```ts
const imageDescribeSchema = z
  .object({
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    robot: z
      .literal('/image/describe')
      .describe(
        '\nYou can use the labels that we return in your application to automatically classify images. You can also pass the labels down to other <dfn>Robots</dfn> to filter images that contain (or do not contain) certain content.\n',
      ),
    provider: z
      .union([
        z.any(),
        z.enum(['aws', 'gcp', 'replicate', 'fal', 'transloadit']),
      ])
      .describe(
        '\nWhich AI provider to leverage.\n\nTransloadit outsources this task and abstracts the interface so you can expect the same data structures, but different latencies and information being returned. Different cloud vendors have different areas they shine in, and we recommend to try out and see what yields the best results for your use case.\n',
      )
      .optional(),
    granularity: z
      .union([z.any(), z.enum(['full', 'list'])])
      .describe(
        '\nWhether to return a full response (`"full"`) including confidence percentages for each found label, or just a flat list of labels (`"list"`).\n',
      )
      .default('full'),
    format: z
      .union([z.any(), z.enum(['json', 'meta', 'text'])])
      .describe(
        '\nIn what format to return the descriptions.\n\n- `"json"` returns a JSON file.\n- `"meta"` does not return a file, but stores the data inside Transloadit\'s file object (under `${file.meta.descriptions}`) that\'s passed around between encoding <dfn>Steps</dfn>, so that you can use the values to burn the data into videos, filter on them, etc.\n',
      )
      .default('json'),
    explicit_descriptions: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nWhether to return only explicit or only non-explicit descriptions of the provided image. Explicit descriptions include labels for NSFW content (nudity, violence, etc). If set to `false`, only non-explicit descriptions (such as human or chair) will be returned. If set to `true`, only explicit descriptions will be returned.\n\nThe possible descriptions depend on the chosen provider. The list of labels from AWS can be found [in their documentation](https://docs.aws.amazon.com/rekognition/latest/dg/moderation.html#moderation-api). GCP labels the image based on five categories, as described [in their documentation](https://cloud.google.com/vision/docs/detecting-safe-search).\n\nFor an example of how to automatically reject NSFW content and malware, please check out this [blog post](https://transloadit.com/blog/2022/07/deny-image-uploads/).\n',
      )
      .default(false),
  })
  .strict()

```

#### `/image/facedetect`

[/image/facedetect docs](https://transloadit.com/docs/robots/image-facedetect/)

Robot Parameter Zod Schema:

```ts
const imageFacedetectSchema = z
  .object({
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    robot: z
      .literal('/image/facedetect')
      .describe(
        '\nYou can specify padding around the extracted faces, tailoring the output for your needs.\n\nThis <dfn>Robot</dfn> works well together with [🤖/image/resize](https://transloadit.com/docs/robots/image-resize/) to bring the full power of resized and optimized images to your website or app.\n\n<div class="alert alert-note">\n\n**How to improve the accuracy:**\n\n- Ensure that your pictures have the correct orientation. This <dfn>Robot</dfn> achieves the best performance when the faces in the image are oriented upright and not rotated.\n- If the <dfn>Robot</dfn> detects objects other than a face, you can use `"faces": "max-confidence"` within your <dfn>Template</dfn> for selecting only the detection with the highest confidence.\n- The number of returned detections can also be controlled using the `min_confidence` parameter. Increasing its value will yield less results but each with a higher confidence. Decreasing the value, on the other hand, will provide more results but may also include objects other than faces.\n\n</div>\n',
      ),
    provider: z
      .union([
        z.any(),
        z.enum(['aws', 'gcp', 'replicate', 'fal', 'transloadit']),
      ])
      .describe(
        '\nWhich AI provider to leverage.\n\nTransloadit outsources this task and abstracts the interface so you can expect the same data structures, but different latencies and information being returned. Different cloud vendors have different areas they shine in, and we recommend to try out and see what yields the best results for your use case.\n',
      )
      .optional(),
    crop: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nDetermine if the detected faces should be extracted. If this option is set to `false`, then the <dfn>Robot</dfn> returns the input image again, but with the coordinates of all detected faces attached to `file.meta.faces` in the result JSON. If this parameter is set to `true`, the <dfn>Robot</dfn> will output all detected faces as images.\n',
      )
      .default(false),
    crop_padding: z
      .union([z.any(), z.string().regex(new RegExp('^\\d+(px|%)$'))])
      .describe(
        '\nSpecifies how much padding is added to the extracted face images if `crop` is set to `true`. Values can be in `px` (pixels) or `%` (percentage of the width and height of the particular face image).\n',
      )
      .default('5px'),
    format: z
      .union([z.any(), z.enum(['jpg', 'png', 'preserve', 'tiff'])])
      .describe(
        '\nDetermines the output format of the extracted face images if `crop` is set to `true`.\n\nThe default value `"preserve"` means that the input image format is re-used.\n',
      )
      .default('preserve'),
    min_confidence: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gte(0).lte(100),
      ])
      .describe(
        '\nSpecifies the minimum confidence that a detected face must have. Only faces which have a higher confidence value than this threshold will be included in the result.\n',
      )
      .default(70),
    faces: z
      .union([
        z.any(),
        z.union([
          z.any(),
          z.enum(['each', 'group', 'max-confidence', 'max-size']),
        ]),
        z.union([
          z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
          z.any(),
          z.number().int(),
        ]),
      ])
      .describe(
        '\nDetermines which of the detected faces should be returned. Valid values are:\n\n- `"each"` — each face is returned individually.\n- `"max-confidence"` — only the face with the highest confidence value is returned.\n- `"max-size"` — only the face with the largest area is returned.\n- `"group"` — all detected faces are grouped together into one rectangle that contains all faces.\n- any integer — the faces are sorted by their top-left corner and the integer determines the index of the returned face. Be aware the values are zero-indexed, meaning that `faces: 0` will return the first face. If no face for a given index exists, no output is produced.\n\nFor the following examples, the input image is:\n\n![](https://transloadit.com/assets/images/abbas-malek-hosseini-22NnY93qaOk-unsplash.jpg)\n\n<br>\n\n`faces: "each"` applied:\n\n![](https://transloadit.com/assets/images/abbas-malek-hosseini-22NnY93qaOk-face-0.jpg)\n![](https://transloadit.com/assets/images/abbas-malek-hosseini-22NnY93qaOk-face-1.jpg)\n\n<br>\n\n`faces: "max-confidence"` applied:\n\n![](https://transloadit.com/assets/images/abbas-malek-hosseini-22NnY93qaOk-face-1.jpg)\n\n<br>\n\n`faces: "max-size"` applied:\n\n![](https://transloadit.com/assets/images/abbas-malek-hosseini-22NnY93qaOk-face-1.jpg)\n\n<br>\n\n`faces: "group"` applied:\n\n![](https://transloadit.com/assets/images/abbas-malek-hosseini-22NnY93qaOk-face-group.jpg)\n\n<br>\n\n`faces: 0` applied:\n\n![](https://transloadit.com/assets/images/abbas-malek-hosseini-22NnY93qaOk-face-0.jpg)\n',
      )
      .default('each'),
  })
  .strict()

```

#### `/image/generate`

[/image/generate docs](https://transloadit.com/docs/robots/image-generate/)

Robot Parameter Zod Schema:

```ts
const imageGenerateSchema = z
  .object({
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    robot: z.literal('/image/generate'),
    model: z.union([z.any(), z.string()]),
    prompt: z
      .union([
        z.any(),
        z.string().describe('The prompt describing the desired image content.'),
      ])
      .describe('The prompt describing the desired image content.'),
    format: z
      .union([z.any(), z.enum(['jpeg', 'png', 'gif', 'webp', 'svg'])])
      .describe('Format of the generated image.')
      .optional(),
    seed: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number(),
      ])
      .describe('Seed for the random number generator.')
      .optional(),
    aspect_ratio: z
      .union([z.any(), z.string()])
      .describe('Aspect ratio of the generated image.')
      .optional(),
    height: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number(),
      ])
      .describe('Height of the generated image.')
      .optional(),
    width: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number(),
      ])
      .describe('Width of the generated image.')
      .optional(),
    style: z
      .union([z.any(), z.string()])
      .describe('Style of the generated image.')
      .optional(),
    num_outputs: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gte(1).lte(10),
      ])
      .describe('Number of image variants to generate.')
      .optional(),
  })
  .strict()

```

#### `/image/merge`

[/image/merge docs](https://transloadit.com/docs/robots/image-merge/)

Robot Parameter Zod Schema:

```ts
const imageMergeSchema = z
  .object({
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    robot: z
      .literal('/image/merge')
      .describe(
        "\nThe final result will be a spritesheet, with the images displayed horizontally or vertically.\n\nIt's recommended to use this Robot with\n[🤖/image/resize](https://transloadit.com/docs/robots/image-resize/) so your images are of a\nsimilar size before merging them.\n",
      ),
    format: z
      .union([z.any(), z.enum(['jpg', 'png'])])
      .describe('The output format for the modified image.')
      .default('png'),
    direction: z
      .union([z.any(), z.enum(['horizontal', 'vertical'])])
      .describe('Specifies the direction which the images are displayed.')
      .default('horizontal'),
    border: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int(),
      ])
      .describe(
        '\nAn integer value which defines the gap between images on the spritesheet.\n\nA value of `10` would cause the images to have the largest gap between them, while a value of `1` would place the images side-by-side.\n',
      )
      .default(0),
    background: z
      .union([
        z.any(),
        z.string().regex(new RegExp('^#?[0-9a-fA-F]{3}([0-9a-fA-F]{3})?$')),
      ])
      .describe(
        '\nEither the hexadecimal code or [name](https://www.imagemagick.org/script/color.php#color_names) of the color used to fill the background (only shown with a border > 1).\n\nBy default, the background of transparent images is changed to white.\n\nFor details about how to preserve transparency across all image types, see [this demo](https://transloadit.com/demos/image-manipulation/properly-preserve-transparency-across-all-image-types/).\n',
      )
      .default('#FFFFFF'),
    adaptive_filtering: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nControls the image compression for PNG images. Setting to `true` results in smaller file size, while increasing processing time. It is encouraged to keep this option disabled.\n',
      )
      .default(false),
    quality: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gte(1).lte(100),
      ])
      .describe(
        '\nControls the image compression for JPG and PNG images. Please also take a look at [🤖/image/optimize](https://transloadit.com/docs/robots/image-optimize/).\n',
      )
      .default(92),
  })
  .strict()

```

#### `/image/ocr`

[/image/ocr docs](https://transloadit.com/docs/robots/image-ocr/)

Robot Parameter Zod Schema:

```ts
const imageOcrSchema = z
  .object({
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    robot: z
      .literal('/image/ocr')
      .describe(
        '\nWith this <dfn>Robot</dfn> you can detect and extract text from images using optical character recognition (OCR).\n\nFor example, you can use the results to obtain the content of traffic signs, name tags, package labels and many more. You can also pass the text down to other <dfn>Robots</dfn> to filter images that contain (or do not contain) certain phrases. For images of dense documents, results may vary and be less accurate than for small pieces of text in photos.\n',
      ),
    provider: z
      .union([
        z.any(),
        z
          .enum(['aws', 'gcp', 'replicate', 'fal', 'transloadit'])
          .describe(
            '\nWhich AI provider to leverage.\n\nTransloadit outsources this task and abstracts the interface so you can expect the same data structures, but different latencies and information being returned. Different cloud vendors have different areas they shine in, and we recommend to try out and see what yields the best results for your use case.\n\nAWS supports detection for the following languages: English, Arabic, Russian, German, French, Italian, Portuguese and Spanish. GCP allows for a wider range of languages, with varying levels of support which can be found on the [official documentation](https://cloud.google.com/vision/docs/languages/).\n',
          ),
      ])
      .describe(
        '\nWhich AI provider to leverage.\n\nTransloadit outsources this task and abstracts the interface so you can expect the same data structures, but different latencies and information being returned. Different cloud vendors have different areas they shine in, and we recommend to try out and see what yields the best results for your use case.\n\nAWS supports detection for the following languages: English, Arabic, Russian, German, French, Italian, Portuguese and Spanish. GCP allows for a wider range of languages, with varying levels of support which can be found on the [official documentation](https://cloud.google.com/vision/docs/languages/).\n',
      ),
    granularity: z
      .union([z.any(), z.enum(['full', 'list'])])
      .describe(
        '\nWhether to return a full response including coordinates for the text (`"full"`), or a flat list of the extracted phrases (`"list"`). This parameter has no effect if the `format` parameter is set to `"text"`.\n',
      )
      .default('full'),
    format: z
      .union([z.any(), z.enum(['json', 'meta', 'text'])])
      .describe(
        '\nIn what format to return the extracted text.\n- `"json"` returns a JSON file.\n- `"meta"` does not return a file, but stores the data inside Transloadit\'s file object (under `${file.meta.recognized_text}`, which is an array of strings) that\'s passed around between encoding <dfn>Steps</dfn>, so that you can use the values to burn the data into videos, filter on them, etc.\n- `"text"` returns the recognized text as a plain UTF-8 encoded text file.\n',
      )
      .default('json'),
  })
  .strict()

```

#### `/image/optimize`

[/image/optimize docs](https://transloadit.com/docs/robots/image-optimize/)

Robot Parameter Zod Schema:

```ts
const imageOptimizeSchema = z
  .object({
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    robot: z
      .literal('/image/optimize')
      .describe(
        "\nWith this <dfn>Robot</dfn> it's possible to reduce the file size of your JPEG, PNG, GIF, WEBP and SVG images by up to 80% for big images and 65% for small to medium sized ones — while keeping their original quality!\n\nThis <dfn>Robot</dfn> enables you to lower your storage and bandwidth costs, and improves your user experience and monetization by reducing the load time of image-intensive web pages.\n\nIt works well together with [🤖/image/resize](https://transloadit.com/docs/robots/image-resize/) to bring the full power of resized and optimized images to your website or app.\n\n> [!Note]\n> This <dfn>Robot</dfn> accepts all image types and will just pass on unsupported image types unoptimized. Hence, there is no need to set up [🤖/file/filter](https://transloadit.com/docs/robots/file-filter/) workflows for this.\n",
      ),
    priority: z
      .union([z.any(), z.enum(['compression-ratio', 'conversion-speed'])])
      .describe(
        '\nProvides different algorithms for better or worse compression for your images, but that run slower or faster. The value `"conversion-speed"` will result in an average compression ratio of 18%. `"compression-ratio"` will result in an average compression ratio of 31%.\n',
      )
      .default('conversion-speed'),
    progressive: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nInterlaces the image if set to `true`, which makes the result image load progressively in browsers. Instead of rendering the image from top to bottom, the browser will first show a low-res blurry version of the image which is then quickly replaced with the actual image as the data arrives. This greatly increases the user experience, but comes at a loss of about 10% of the file size reduction.\n',
      )
      .default(false),
    preserve_meta_data: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        "\nSpecifies if the image's metadata should be preserved during the optimization, or not. If it is not preserved, the file size is even further reduced. But be aware that this could strip a photographer's copyright information, which for obvious reasons can be frowned upon.\n",
      )
      .default(true),
    fix_breaking_images: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nIf set to `true` this parameter tries to fix images that would otherwise make the underlying tool error out and thereby break your <dfn>Assemblies</dfn>. This can sometimes result in a larger file size, though.\n',
      )
      .default(true),
  })
  .strict()

```

#### `/image/resize`

[/image/resize docs](https://transloadit.com/docs/robots/image-resize/)

Robot Parameter Zod Schema:

```ts
const imageResizeSchema = z
  .object({
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    imagemagick_stack: z
      .union([
        z.any(),
        z.union([z.any(), z.literal('v3')]),
        z.union([
          z.any(),
          z.string().regex(new RegExp('^v?[23](\\.\\d+)?(\\.\\d+)?$')),
        ]),
      ])
      .default('v3'),
    robot: z.literal('/image/resize'),
    format: z
      .union([z.union([z.any(), z.string()]), z.null()])
      .describe(
        '\nThe output format for the modified image.\n\nSome of the most important available formats are `"jpg"`, `"png"`, `"gif"`, and `"tiff"`. For a complete lists of all formats that we can write to please check [our supported image formats list](https://transloadit.com/docs/supported-formats/image-formats/).\n\nIf `null` (default), then the input image\'s format will be used as the output format.\n\nIf you wish to convert to `"pdf"`, please consider [🤖/document/convert](https://transloadit.com/docs/robots/document-convert/) instead.\n',
      )
      .default(null),
    width: z
      .union([z.any(), z.number().int().gte(1).lte(7680)])
      .describe(
        '\nWidth of the result in pixels. If not specified, will default to the width of the original.\n',
      )
      .optional(),
    height: z
      .union([z.any(), z.number().int().gte(1).lte(4320)])
      .describe(
        '\nHeight of the new image, in pixels. If not specified, will default to the height of the input image.\n',
      )
      .optional(),
    resize_strategy: z
      .union([
        z.any(),
        z
          .union([
            z.any(),
            z
              .literal('crop')
              .describe(
                'Cuts an area out of an image, discarding any overlapping parts. If the source image is smaller than the crop frame, it will be zoomed. This strategy is implied when you specify coordinates in the `crop` parameter, and cannot be used without it.\n\nTo crop around human faces, see [🤖/image/facedetect](https://transloadit.com/docs/robots/image-facedetect/) instead.',
              ),
          ])
          .describe(
            'Cuts an area out of an image, discarding any overlapping parts. If the source image is smaller than the crop frame, it will be zoomed. This strategy is implied when you specify coordinates in the `crop` parameter, and cannot be used without it.\n\nTo crop around human faces, see [🤖/image/facedetect](https://transloadit.com/docs/robots/image-facedetect/) instead.',
          ),
        z
          .union([
            z.any(),
            z
              .literal('fillcrop')
              .describe(
                'Scales the image to fit into our 100×100 target while preserving aspect ratio, while trimming away any excess surface. This means both sides will become exactly 100 pixels, at the tradeoff of destroying parts of the image.\n\nBy default the resulting image is horizontally/vertically centered to fill the target rectangle. Use the `gravity` parameter to change where to crop the image, such as `"bottom`" or `"left`".',
              ),
          ])
          .describe(
            'Scales the image to fit into our 100×100 target while preserving aspect ratio, while trimming away any excess surface. This means both sides will become exactly 100 pixels, at the tradeoff of destroying parts of the image.\n\nBy default the resulting image is horizontally/vertically centered to fill the target rectangle. Use the `gravity` parameter to change where to crop the image, such as `"bottom`" or `"left`".',
          ),
        z
          .union([
            z.any(),
            z
              .literal('fit')
              .describe(
                'Uses the larger side of the original image as a base for the resize. Aspect ratio is preserved. Either side will become at most 100 pixels.\n\nFor example: resizing a 400×300 image into 100×100, would produce a 100×75 image.',
              ),
          ])
          .describe(
            'Uses the larger side of the original image as a base for the resize. Aspect ratio is preserved. Either side will become at most 100 pixels.\n\nFor example: resizing a 400×300 image into 100×100, would produce a 100×75 image.',
          ),
        z
          .union([
            z.any(),
            z
              .literal('min_fit')
              .describe(
                'Uses the **smaller** side of the original image as a base for the resize. After resizing, the larger side will have a larger value than specified. Aspect ratio is preserved. Either side will become at least 100 pixels.\n\nFor example: resizing a 400×300 image into 100×100, would produce a 133×100 image.',
              ),
          ])
          .describe(
            'Uses the **smaller** side of the original image as a base for the resize. After resizing, the larger side will have a larger value than specified. Aspect ratio is preserved. Either side will become at least 100 pixels.\n\nFor example: resizing a 400×300 image into 100×100, would produce a 133×100 image.',
          ),
        z
          .union([
            z.any(),
            z
              .literal('pad')
              .describe(
                'Scales the image to fit while preserving aspect ratio. Both sides of the resized image become exactly 100 pixels, and any remaining surface is filled with a background color.\n\nIn this example, the background color is determined by the [Assembly Variable](https://transloadit.com/docs/topics/assembly-instructions/#assembly-variables) `${file.meta.average_color}`. If you set `zoom` to `false` (default is `true`), smaller images will be centered horizontally and vertically, and have the background padding all around them.',
              ),
          ])
          .describe(
            'Scales the image to fit while preserving aspect ratio. Both sides of the resized image become exactly 100 pixels, and any remaining surface is filled with a background color.\n\nIn this example, the background color is determined by the [Assembly Variable](https://transloadit.com/docs/topics/assembly-instructions/#assembly-variables) `${file.meta.average_color}`. If you set `zoom` to `false` (default is `true`), smaller images will be centered horizontally and vertically, and have the background padding all around them.',
          ),
        z
          .union([
            z.any(),
            z
              .literal('stretch')
              .describe(
                'Ignores aspect ratio, resizing the image to the exact width and height specified. This may result in a stretched or distorted image.',
              ),
          ])
          .describe(
            'Ignores aspect ratio, resizing the image to the exact width and height specified. This may result in a stretched or distorted image.',
          ),
      ])
      .describe(
        '\nSee the list of available [resize strategies](https://transloadit.com/docs/topics/resize-strategies/).\n',
      )
      .default('fit'),
    zoom: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nIf this is set to `false`, smaller images will not be stretched to the desired width and height. For details about the impact of zooming for your preferred resize strategy, see the list of available [resize strategies](https://transloadit.com/docs/topics/resize-strategies/).\n',
      )
      .default(true),
    crop: z
      .union([
        z.any(),
        z.union([
          z.any(),
          z
            .object({
              x1: z
                .union([
                  z.union([
                    z.any(),
                    z.union([z.any(), z.string()]),
                    z.union([
                      z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                      z.any(),
                      z.number(),
                    ]),
                  ]),
                  z.null(),
                ])
                .optional(),
              y1: z
                .union([
                  z.union([
                    z.any(),
                    z.union([z.any(), z.string()]),
                    z.union([
                      z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                      z.any(),
                      z.number(),
                    ]),
                  ]),
                  z.null(),
                ])
                .optional(),
              x2: z
                .union([
                  z.union([
                    z.any(),
                    z.union([z.any(), z.string()]),
                    z.union([
                      z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                      z.any(),
                      z.number(),
                    ]),
                  ]),
                  z.null(),
                ])
                .optional(),
              y2: z
                .union([
                  z.union([
                    z.any(),
                    z.union([z.any(), z.string()]),
                    z.union([
                      z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                      z.any(),
                      z.number(),
                    ]),
                  ]),
                  z.null(),
                ])
                .optional(),
            })
            .strict(),
        ]),
        z.union([z.any(), z.string()]),
      ])
      .describe(
        '\nSpecify an object containing coordinates for the top left and bottom right corners of the rectangle to be cropped from the original image(s). The coordinate system is rooted in the top left corner of the image. Values can be integers for absolute pixel values or strings for percentage based values.\n\nFor example:\n\n```json\n{\n  "x1": 80,\n  "y1": 100,\n  "x2": "60%",\n  "y2": "80%"\n}\n```\n\nThis will crop the area from `(80, 100)` to `(600, 800)` from a 1000×1000 pixels image, which is a square whose width is 520px and height is 700px. If `crop` is set, the width and height parameters are ignored, and the `resize_strategy` is set to `crop` automatically.\n\nYou can also use a JSON string of such an object with coordinates in similar fashion:\n\n```json\n"{\\"x1\\": <Integer>, \\"y1\\": <Integer>, \\"x2\\": <Integer>, \\"y2\\": <Integer>}"\n```\n\nTo crop around human faces, see [🤖/image/facedetect](https://transloadit.com/docs/robots/image-facedetect/).\n',
      )
      .optional(),
    gravity: z
      .union([
        z.any(),
        z.enum([
          'bottom',
          'bottom-left',
          'bottom-right',
          'center',
          'left',
          'right',
          'top',
          'top-left',
          'top-right',
        ]),
      ])
      .describe(
        '\nThe direction from which the image is to be cropped, when `"resize_strategy"` is set to `"crop"`, but no crop coordinates are defined.\n',
      )
      .default('center'),
    strip: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nStrips all metadata from the image. This is useful to keep thumbnails as small as possible.\n',
      )
      .default(false),
    alpha: z
      .union([
        z.any(),
        z.enum([
          'Activate',
          'Background',
          'Copy',
          'Deactivate',
          'Extract',
          'Off',
          'On',
          'Opaque',
          'Remove',
          'Set',
          'Shape',
          'Transparent',
        ]),
      ])
      .describe('\nGives control of the alpha/matte channel of an image.\n')
      .optional(),
    preclip_alpha: z
      .union([
        z.any(),
        z.enum([
          'Activate',
          'Background',
          'Copy',
          'Deactivate',
          'Extract',
          'Off',
          'On',
          'Opaque',
          'Remove',
          'Set',
          'Shape',
          'Transparent',
        ]),
      ])
      .describe(
        '\nGives control of the alpha/matte channel of an image before applying the clipping path via `clip: true`.\n',
      )
      .optional(),
    flatten: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nFlattens all layers onto the specified background to achieve better results from transparent formats to non-transparent formats, as explained in the [ImageMagick documentation](https://www.imagemagick.org/script/command-line-options.php#layers).\n\nTo preserve animations, GIF files are not flattened when this is set to `true`. To flatten GIF animations, use the `frame` parameter.\n',
      )
      .default(true),
    correct_gamma: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nPrevents gamma errors [common in many image scaling algorithms](https://www.4p8.com/eric.brasseur/gamma.html).\n',
      )
      .default(false),
    quality: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gte(1).lte(100),
      ])
      .describe(
        '\nControls the image compression for JPG and PNG images. Please also take a look at [🤖/image/optimize](https://transloadit.com/docs/robots/image-optimize/).\n',
      )
      .default(92),
    adaptive_filtering: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nControls the image compression for PNG images. Setting to `true` results in smaller file size, while increasing processing time. It is encouraged to keep this option disabled.\n',
      )
      .default(false),
    background: z
      .union([
        z.any(),
        z.union([
          z.any(),
          z.string().regex(new RegExp('^#?[0-9a-fA-F]{3}([0-9a-fA-F]{3})?$')),
        ]),
        z.union([
          z.any(),
          z.enum([
            'transparent',
            'none',
            'black',
            'white',
            'red',
            'green',
            'blue',
            'yellow',
            'cyan',
            'magenta',
            'gray',
            'grey',
            'opaque',
          ]),
        ]),
      ])
      .describe(
        '\nEither the hexadecimal code or [name](https://www.imagemagick.org/script/color.php#color_names) of the color used to fill the background (used for the `pad` resize strategy).\n\n**Note:** By default, the background of transparent images is changed to white. To preserve transparency, set `"background"` to `"none"`.\n',
      )
      .default('#FFFFFF'),
    frame: z
      .union([
        z.union([
          z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
          z.any(),
          z.number().int().gte(1),
        ]),
        z.null(),
      ])
      .describe(
        '\nUse this parameter when dealing with animated GIF files to specify which frame of the GIF is used for the operation. Specify `1` to use the first frame, `2` to use the second, and so on. `null` means all frames.\n',
      )
      .default(null),
    colorspace: z
      .union([
        z.any(),
        z.enum([
          'CMY',
          'CMYK',
          'Gray',
          'HCL',
          'HCLp',
          'HSB',
          'HSI',
          'HSL',
          'HSV',
          'HWB',
          'Jzazbz',
          'Lab',
          'LCHab',
          'LCHuv',
          'LMS',
          'Log',
          'Luv',
          'OHTA',
          'OkLab',
          'OkLCH',
          'Rec601YCbCr',
          'Rec709YCbCr',
          'RGB',
          'scRGB',
          'sRGB',
          'Transparent',
          'Undefined',
          'xyY',
          'XYZ',
          'YCbCr',
          'YCC',
          'YDbDr',
          'YIQ',
          'YPbPr',
          'YUV',
        ]),
      ])
      .describe(
        '\nSets the image colorspace. For details about the available values, see the [ImageMagick documentation](https://www.imagemagick.org/script/command-line-options.php#colorspace). Please note that if you were using `"RGB"`, we recommend using `"sRGB"` instead as of 2014-02-04. ImageMagick might try to find the most efficient `colorspace` based on the color of an image, and default to e.g. `"Gray"`. To force colors, you might have to use this parameter in combination with `type: "TrueColor"`.\n',
      )
      .optional(),
    type: z
      .union([
        z.any(),
        z.enum([
          'Bilevel',
          'ColorSeparation',
          'ColorSeparationAlpha',
          'Grayscale',
          'GrayscaleAlpha',
          'Palette',
          'PaletteAlpha',
          'TrueColor',
          'TrueColorAlpha',
        ]),
      ])
      .describe(
        '\nSets the image color type. For details about the available values, see the [ImageMagick documentation](https://www.imagemagick.org/script/command-line-options.php#type). If you\'re using `colorspace`, ImageMagick might try to find the most efficient based on the color of an image, and default to e.g. `"Gray"`. To force colors, you could e.g. set this parameter to `"TrueColor"`\n',
      )
      .optional(),
    sepia: z
      .union([
        z.union([
          z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
          z.any(),
          z.number().int().gte(0).lte(99),
        ]),
        z.null(),
      ])
      .describe('\nApplies a sepia tone effect in percent.\n')
      .default(null),
    rotation: z
      .union([
        z.any(),
        z.union([
          z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
          z.any(),
          z.number(),
        ]),
        z.union([z.any(), z.union([z.boolean(), z.any()])]),
        z.union([z.any(), z.literal('auto')]),
      ])
      .describe(
        '\nDetermines whether the image should be rotated. Use any number to specify the rotation angle in degrees (e.g., `90`, `180`, `270`, `360`, or precise values like `2.9`). Use the value `true` or `"auto"` to auto-rotate images that are rotated incorrectly or depend on EXIF rotation settings. Otherwise, use `false` to disable auto-fixing altogether.\n',
      )
      .default(true),
    compress: z
      .union([
        z.union([
          z.any(),
          z.enum([
            'BZip',
            'Fax',
            'Group4',
            'JPEG',
            'JPEG2000',
            'Lossless',
            'LZW',
            'None',
            'RLE',
            'Zip',
          ]),
        ]),
        z.null(),
      ])
      .describe(
        '\nSpecifies pixel compression for when the image is written. Compression is disabled by default.\n\nPlease also take a look at [🤖/image/optimize](https://transloadit.com/docs/robots/image-optimize/).\n',
      )
      .default(null),
    blur: z
      .union([
        z.union([
          z.any(),
          z.string().regex(new RegExp('^\\d+(\\.\\d+)?x\\d+(\\.\\d+)?$')),
        ]),
        z.null(),
      ])
      .describe(
        '\nSpecifies gaussian blur, using a value with the form `{radius}x{sigma}`. The radius value specifies the size of area the operator should look at when spreading pixels, and should typically be either `"0"` or at least two times the sigma value. The sigma value is an approximation of how many pixels the image is "spread"; think of it as the size of the brush used to blur the image. This number is a floating point value, enabling small values like `"0.5"` to be used.\n',
      )
      .default(null),
    blur_regions: z
      .union([
        z.union([
          z.any(),
          z.array(
            z.union([
              z.any(),
              z
                .object({
                  x: z.union([z.any(), z.any()]),
                  y: z.union([z.any(), z.any()]),
                  width: z.union([z.any(), z.any()]),
                  height: z.union([z.any(), z.any()]),
                })
                .strict(),
            ]),
          ),
        ]),
        z.null(),
      ])
      .describe(
        '\nSpecifies an array of ellipse objects that should be blurred on the image. Each object has the following keys: `x`, `y`, `width`, `height`.  If `blur_regions` has a value, then the `blur` parameter is used as the strength of the blur for each region.\n',
      )
      .default(null),
    brightness: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().gte(0),
      ])
      .describe(
        '\nIncreases or decreases the brightness of the image by using a multiplier. For example `1.5` would increase the brightness by 50%, and `0.75` would decrease the brightness by 25%.\n',
      )
      .default(1),
    saturation: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().gte(0),
      ])
      .describe(
        '\nIncreases or decreases the saturation of the image by using a multiplier. For example `1.5` would increase the saturation by 50%, and `0.75` would decrease the saturation by 25%.\n',
      )
      .default(1),
    hue: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().gte(0),
      ])
      .describe(
        '\nChanges the hue by rotating the color of the image. The value `100` would produce no change whereas `0` and `200` will negate the colors in the image.\n',
      )
      .default(100),
    contrast: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().gte(0).lte(2),
      ])
      .describe(
        '\nAdjusts the contrast of the image. A value of `1` produces no change. Values below `1` decrease contrast (with `0` being minimum contrast), and values above `1` increase contrast (with `2` being maximum contrast). This works like the `brightness` parameter.\n',
      )
      .default(1),
    watermark_url: z
      .union([z.any(), z.string()])
      .describe(
        '\nA URL indicating a PNG image to be overlaid above this image. Please note that you can also  [supply the watermark via another Assembly Step](https://transloadit.com/docs/topics/use-parameter/#supplying-the-watermark-via-an-assembly-step). With watermarking you can add an image onto another image. This is usually used for logos.\n',
      )
      .optional(),
    watermark_position: z
      .union([
        z.any(),
        z.union([z.any(), z.any()]),
        z.union([z.any(), z.array(z.union([z.any(), z.any()]))]),
      ])
      .describe(
        '\nThe position at which the watermark is placed. The available options are `"center"`, `"top"`, `"bottom"`, `"left"`, and `"right"`. You can also combine options, such as `"bottom-right"`.\n\nAn array of possible values can also be specified, in which case one value will be selected at random, such as `[ "center", "left", "bottom-left", "bottom-right" ]`.\n\nThis setting puts the watermark in the specified corner. To use a specific pixel offset for the watermark, you will need to add the padding to the image itself.\n',
      )
      .default('center'),
    watermark_x_offset: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int(),
      ])
      .describe(
        "\nThe x-offset in number of pixels at which the watermark will be placed in relation to the position it has due to `watermark_position`.\n\nValues can be both positive and negative and yield different results depending on the `watermark_position` parameter. Positive values move the watermark closer to the image's center point, whereas negative values move the watermark further away from the image's center point.\n",
      )
      .default(0),
    watermark_y_offset: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int(),
      ])
      .describe(
        "\nThe y-offset in number of pixels at which the watermark will be placed in relation to the position it has due to `watermark_position`.\n\nValues can be both positive and negative and yield different results depending on the `watermark_position` parameter. Positive values move the watermark closer to the image's center point, whereas negative values move the watermark further away from the image's center point.\n",
      )
      .default(0),
    watermark_size: z
      .union([z.any(), z.string().regex(new RegExp('^\\d+%$'))])
      .describe(
        '\nThe size of the watermark, as a percentage.\n\nFor example, a value of `"50%"` means that size of the watermark will be 50% of the size of image on which it is placed. The exact sizing depends on `watermark_resize_strategy`, too.\n',
      )
      .optional(),
    watermark_resize_strategy: z
      .union([z.any(), z.enum(['area', 'fit', 'min_fit', 'stretch'])])
      .describe(
        '\nAvailable values are `"fit"`, `"min_fit"`, `"stretch"` and `"area"`.\n\nTo explain how the resize strategies work, let\'s assume our target image size is 800×800 pixels and our watermark image is 400×300 pixels. Let\'s also assume, the `watermark_size` parameter is set to `"25%"`.\n\nFor the `"fit"` resize strategy, the watermark is scaled so that the longer side of the watermark takes up 25% of the corresponding image side. And the other side is scaled according to the aspect ratio of the watermark image. So with our watermark, the width is the longer side, and 25% of the image size would be 200px. Hence, the watermark would be resized to 200×150 pixels. If the `watermark_size` was set to `"50%"`, it would be resized to 400×300 pixels (so just left at its original size).\n\nFor the `"min_fit"` resize strategy, the watermark is scaled so that the shorter side of the watermark takes up 25% of the corresponding image side. And the other side is scaled according to the aspect ratio of the watermark image. So with our watermark, the height is the shorter side, and 25% of the image size would be 200px. Hence, the watermark would be resized to 267×200 pixels. If the `watermark_size` was set to `"50%"`, it would be resized to 533×400 pixels (so larger than its original size).\n\nFor the `"stretch"` resize strategy, the watermark is stretched (meaning, it is resized without keeping its aspect ratio in mind) so that both sides take up 25% of the corresponding image side. Since our image is 800×800 pixels, for a watermark size of 25% the watermark would be resized to 200×200 pixels. Its height would appear stretched, because keeping the aspect ratio in mind it would be resized to 200×150 pixels instead.\n\nFor the `"area"` resize strategy, the watermark is resized (keeping its aspect ratio in check) so that it covers `"xx%"` of the image\'s surface area. The value from `watermark_size` is used for the percentage area size.\n',
      )
      .default('fit'),
    watermark_opacity: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().gte(0).lte(1),
      ])
      .describe(
        '\nThe opacity of the watermark, where `0.0` is fully transparent and `1.0` is fully opaque.\n\nFor example, a value of `0.5` means the watermark will be 50% transparent, allowing the underlying image to show through. This is useful for subtle branding or when you want the watermark to be less obtrusive.\n',
      )
      .default(1),
    watermark_repeat_x: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nWhen set to `true`, the watermark will be repeated horizontally across the entire width of the image.\n\nThis is useful for creating tiled watermark patterns that cover the full image and make it more difficult to crop out the watermark.\n',
      )
      .default(false),
    watermark_repeat_y: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nWhen set to `true`, the watermark will be repeated vertically across the entire height of the image.\n\nThis is useful for creating tiled watermark patterns that cover the full image. Can be combined with `watermark_repeat_x` to tile in both directions.\n',
      )
      .default(false),
    text: z
      .union([
        z.any(),
        z.union([
          z.any(),
          z
            .object({
              text: z.union([z.any(), z.string()]),
              font: z
                .union([z.any(), z.string()])
                .describe(
                  '\nThe font family to use. Also includes boldness and style of the font.\n\n[Here](https://transloadit.com/docs/supported-formats/fonts/) is a list of all\nsupported fonts.\n',
                )
                .default('Arial'),
              size: z
                .union([
                  z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                  z.any(),
                  z.number().int().gte(1),
                ])
                .describe('\nThe text size in pixels.\n')
                .default(12),
              rotate: z
                .union([
                  z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                  z.any(),
                  z.number().int(),
                ])
                .describe('\nThe rotation angle in degrees.\n')
                .default(0),
              color: z
                .union([
                  z.any(),
                  z.union([z.any(), z.any()]),
                  z.union([z.any(), z.any()]),
                ])
                .describe(
                  '\nThe text color. All hex colors in the form `"#xxxxxx"` are supported, where each x can be `0-9` or `a-f`. Named colors like `"black"`, `"white"`, `"transparent"` etc. are also supported. If you want a transparent text color, use "stroke" instead, otherwise your text will not be visible.\n',
                )
                .default('#000000'),
              background_color: z
                .union([
                  z.any(),
                  z.union([z.any(), z.any()]),
                  z.union([z.any(), z.any()]),
                ])
                .describe(
                  '\nThe background color behind the text. All hex colors in the form `"#xxxxxx"` are supported, where each x can be `0-9` or `a-f`. Named colors like `"black"`, `"white"`, `"transparent"` etc. are also supported.\n',
                )
                .default('transparent'),
              stroke_width: z
                .union([
                  z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                  z.any(),
                  z.number().int().gte(0),
                ])
                .describe("\nThe stroke's width in pixels.\n")
                .default(0),
              stroke_color: z
                .union([
                  z.any(),
                  z.union([z.any(), z.any()]),
                  z.union([z.any(), z.any()]),
                ])
                .describe(
                  '\nThe stroke\'s color. All hex colors in the form `"#xxxxxx"` are supported, where each x can be `0-9` or `a-f`. Named colors like `"black"`, `"white"`, `"transparent"` etc. are also supported.\n',
                )
                .default('transparent'),
              align: z
                .union([z.any(), z.enum(['center', 'left', 'right'])])
                .describe(
                  '\nThe horizontal text alignment. Can be `"left"`, `"center"` and `"right"`.\n',
                )
                .default('center'),
              valign: z
                .union([z.any(), z.enum(['bottom', 'center', 'top'])])
                .describe(
                  '\nThe vertical text alignment. Can be `"top"`, `"center"` and `"bottom"`.\n',
                )
                .default('center'),
              x_offset: z
                .union([
                  z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                  z.any(),
                  z.number().int(),
                ])
                .describe(
                  '\nThe horizontal offset for the text in pixels that is added (positive integer) or removed (negative integer) from the horizontal alignment.\n',
                )
                .default(0),
              y_offset: z
                .union([
                  z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                  z.any(),
                  z.number().int(),
                ])
                .describe(
                  '\nThe vertical offset for the text in pixels that is added (positive integer) or removed (negative integer) from the vertical alignment.\n',
                )
                .default(0),
            })
            .strict(),
        ]),
        z.union([
          z.any(),
          z.array(
            z.union([
              z.any(),
              z
                .object({
                  text: z.union([z.any(), z.any()]),
                  font: z
                    .union([z.any(), z.any()])
                    .describe(
                      '\nThe font family to use. Also includes boldness and style of the font.\n\n[Here](https://transloadit.com/docs/supported-formats/fonts/) is a list of all\nsupported fonts.\n',
                    )
                    .default('Arial'),
                  size: z
                    .union([
                      z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                      z.any(),
                      z.any(),
                    ])
                    .describe('\nThe text size in pixels.\n')
                    .default(12),
                  rotate: z
                    .union([
                      z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                      z.any(),
                      z.any(),
                    ])
                    .describe('\nThe rotation angle in degrees.\n')
                    .default(0),
                  color: z
                    .union([
                      z.any(),
                      z.union([z.any(), z.any()]),
                      z.union([z.any(), z.any()]),
                    ])
                    .describe(
                      '\nThe text color. All hex colors in the form `"#xxxxxx"` are supported, where each x can be `0-9` or `a-f`. Named colors like `"black"`, `"white"`, `"transparent"` etc. are also supported. If you want a transparent text color, use "stroke" instead, otherwise your text will not be visible.\n',
                    )
                    .default('#000000'),
                  background_color: z
                    .union([
                      z.any(),
                      z.union([z.any(), z.any()]),
                      z.union([z.any(), z.any()]),
                    ])
                    .describe(
                      '\nThe background color behind the text. All hex colors in the form `"#xxxxxx"` are supported, where each x can be `0-9` or `a-f`. Named colors like `"black"`, `"white"`, `"transparent"` etc. are also supported.\n',
                    )
                    .default('transparent'),
                  stroke_width: z
                    .union([
                      z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                      z.any(),
                      z.any(),
                    ])
                    .describe("\nThe stroke's width in pixels.\n")
                    .default(0),
                  stroke_color: z
                    .union([
                      z.any(),
                      z.union([z.any(), z.any()]),
                      z.union([z.any(), z.any()]),
                    ])
                    .describe(
                      '\nThe stroke\'s color. All hex colors in the form `"#xxxxxx"` are supported, where each x can be `0-9` or `a-f`. Named colors like `"black"`, `"white"`, `"transparent"` etc. are also supported.\n',
                    )
                    .default('transparent'),
                  align: z
                    .union([z.any(), z.any()])
                    .describe(
                      '\nThe horizontal text alignment. Can be `"left"`, `"center"` and `"right"`.\n',
                    )
                    .default('center'),
                  valign: z
                    .union([z.any(), z.any()])
                    .describe(
                      '\nThe vertical text alignment. Can be `"top"`, `"center"` and `"bottom"`.\n',
                    )
                    .default('center'),
                  x_offset: z
                    .union([
                      z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                      z.any(),
                      z.any(),
                    ])
                    .describe(
                      '\nThe horizontal offset for the text in pixels that is added (positive integer) or removed (negative integer) from the horizontal alignment.\n',
                    )
                    .default(0),
                  y_offset: z
                    .union([
                      z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                      z.any(),
                      z.any(),
                    ])
                    .describe(
                      '\nThe vertical offset for the text in pixels that is added (positive integer) or removed (negative integer) from the vertical alignment.\n',
                    )
                    .default(0),
                })
                .strict(),
            ]),
          ),
        ]),
      ])
      .describe(
        '\nText overlays to be applied to the image. Can be either a single text object or an array of text objects. Each text object contains text rules. The following text parameters are intended to be used as properties for your text overlays. Here is an example:\n\n```json\n"watermarked": {\n  "use": "resized",\n  "robot": "/image/resize",\n  "text": [\n    {\n      "text": "© 2018 Transloadit.com",\n      "size": 12,\n      "font": "Ubuntu",\n      "color": "#eeeeee",\n      "valign": "bottom",\n      "align": "right",\n      "x_offset": 16,\n      "y_offset": -10\n    }\n  ]\n}\n```',
      )
      .optional(),
    progressive: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nInterlaces the image if set to `true`, which makes the image load progressively in browsers. Instead of rendering the image from top to bottom, the browser will first show a low-res blurry version of the images which is then quickly replaced with the actual image as the data arrives. This greatly increases the user experience, but comes at a cost of a file size increase by around 10%.\n',
      )
      .default(false),
    transparent: z
      .union([
        z.any(),
        z.union([
          z.any(),
          z.union([z.any(), z.any()]),
          z.union([z.any(), z.any()]),
        ]),
        z.union([z.any(), z.string().regex(new RegExp('^\\d+,\\d+,\\d+$'))]),
      ])
      .describe(
        '\nMake this color transparent within the image. Example: `"255,255,255"`.\n',
      )
      .optional(),
    trim_whitespace: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nThis determines if additional whitespace around the image should first be trimmed away. If you set this to `true` this parameter removes any edges that are exactly the same color as the corner pixels.\n',
      )
      .default(false),
    clip: z
      .union([
        z.any(),
        z.union([z.any(), z.string()]),
        z.union([z.any(), z.union([z.boolean(), z.any()])]),
      ])
      .describe(
        '\nApply the clipping path to other operations in the resize job, if one is present. If set to `true`, it will automatically take the first clipping path. If set to a String it finds a clipping path by that name.\n',
      )
      .default(false),
    negate: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nReplace each pixel with its complementary color, effectively negating the image. Especially useful when testing clipping.\n',
      )
      .default(false),
    density: z
      .union([
        z.union([z.any(), z.string().regex(new RegExp('\\d+(x\\d+)?'))]),
        z.null(),
      ])
      .describe(
        '\nWhile in-memory quality and file format depth specifies the color resolution, the density of an image is the spatial (space) resolution of the image. That is the density (in pixels per inch) of an image and defines how far apart (or how big) the individual pixels are. It defines the size of the image in real world terms when displayed on devices or printed.\n\nYou can set this value to a specific `width` or in the format `width`x`height`.\n\nIf your converted image is unsharp, please try increasing density.\n',
      )
      .default(null),
    monochrome: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nTransform the image to black and white. This is a shortcut for setting the colorspace to Gray and type to Bilevel.\n',
      )
      .default(false),
    shave: z
      .union([
        z.any(),
        z.union([z.any(), z.string().regex(new RegExp('^\\d+(x\\d+)?$'))]),
        z.union([z.any(), z.number().int().gte(0)]),
      ])
      .describe(
        '\nShave pixels from the image edges. The value should be in the format `width` or `width`x`height` to specify the number of pixels to remove from each side.\n',
      )
      .optional(),
  })
  .strict()

```

#### `/meta/write`

[/meta/write docs](https://transloadit.com/docs/robots/meta-write/)

Robot Parameter Zod Schema:

```ts
const metaWriteSchema = z
  .object({
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    ffmpeg_stack: FfmpegStackSchema,
    use: UseSchema,
    ffmpeg: FfmpegSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    robot: z
      .literal('/meta/write')
      .describe(
        '\n**Note:** This <dfn>Robot</dfn> currently accepts images, videos and audio files.\n',
      ),
    data_to_write: z
      .union([z.any(), z.object({}).catchall(z.any())])
      .describe(
        '\nA key/value map defining the metadata to write into the file.\n\nValid metadata keys can be found [here](https://exiftool.org/TagNames/EXIF.html). For example: `ProcessingSoftware`.\n',
      )
      .default({}),
  })
  .strict()

```

#### `/minio/import`

[/minio/import docs](https://transloadit.com/docs/robots/minio-import/)

Robot Parameter Zod Schema:

```ts
const minioImportSchema = z
  .object({
    credentials: CredentialsSchema,
    ignore_errors: IgnoreErrorsSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    force_name: z
      .union([
        z.union([
          z.any(),
          z.union([z.any(), z.string()]),
          z.union([z.any(), z.array(z.union([z.any(), z.string()]))]),
        ]),
        z.null(),
      ])
      .describe(
        'Custom name for the imported file(s). By default file names are derived from the source.',
      )
      .default(null),
    bucket: z.union([z.any(), z.string()]).optional(),
    host: z.union([z.any(), z.string()]).optional(),
    key: z.union([z.any(), z.string()]).optional(),
    secret: z.union([z.any(), z.string()]).optional(),
    robot: z.literal('/minio/import'),
    path: z
      .union([
        z.any(),
        z.union([z.any(), z.string()]),
        z.union([z.any(), z.array(z.union([z.any(), z.string()]))]),
      ])
      .describe(
        "\nThe path in your bucket to the specific file or directory. If the path points to a file, only this file will be imported. For example: `images/avatar.jpg`.\n\nIf it points to a directory, indicated by a trailing slash (`/`), then all files that are direct descendants of this directory will be imported. For example: `images/`.\n\nDirectories are **not** imported recursively. If you want to import files from subdirectories and sub-subdirectories, enable the `recursive` parameter.\n\nIf you want to import all files from the root directory, please use `/` as the value here. In this case, make sure all your objects belong to a path. If you have objects in the root of your bucket that aren't prefixed with `/`, you'll receive an error: `A client error (NoSuchKey) occurred when calling the GetObject operation: The specified key does not exist.`\n\nYou can also use an array of path strings here to import multiple paths in the same <dfn>Robot</dfn>'s <dfn>Step</dfn>.\n",
      ),
    recursive: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nSetting this to `true` will enable importing files from subdirectories and sub-subdirectories (etc.) of the given path.\n\nPlease use the pagination parameters `page_number` and `files_per_page` wisely here.\n',
      )
      .default(false),
    page_number: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int(),
      ])
      .describe(
        '\nThe pagination page number. For now, in order to not break backwards compatibility in non-recursive imports, this only works when recursive is set to `true`.\n\nWhen doing big imports, make sure no files are added or removed from other scripts within your path, otherwise you might get weird results with the pagination.\n',
      )
      .default(1),
    files_per_page: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int(),
      ])
      .describe(
        '\nThe pagination page size. This only works when recursive is `true` for now, in order to not break backwards compatibility in non-recursive imports.\n',
      )
      .default(1000),
    return_file_stubs: z
      .union([
        z.any(),
        z.union([
          z
            .boolean()
            .describe(
              '\nIf set to `true`, the Robot will not yet import the actual files but instead return an empty file stub that includes a URL from where the file can be imported by subsequent Robots. This is useful for cases where subsequent Steps need more control over the import process, such as with 🤖/video/ondemand. This parameter should only be set if all subsequent Steps use Robots that support file stubs.\n',
            ),
          z.any(),
        ]),
      ])
      .describe(
        '\nIf set to `true`, the Robot will not yet import the actual files but instead return an empty file stub that includes a URL from where the file can be imported by subsequent Robots. This is useful for cases where subsequent Steps need more control over the import process, such as with 🤖/video/ondemand. This parameter should only be set if all subsequent Steps use Robots that support file stubs.\n',
      )
      .default(false),
  })
  .strict()

```

#### `/minio/store`

[/minio/store docs](https://transloadit.com/docs/robots/minio-store/)

Robot Parameter Zod Schema:

```ts
const minioStoreSchema = z
  .object({
    credentials: CredentialsSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    bucket: z.union([z.any(), z.string()]).optional(),
    host: z.union([z.any(), z.string()]).optional(),
    key: z.union([z.any(), z.string()]).optional(),
    secret: z.union([z.any(), z.string()]).optional(),
    robot: z
      .literal('/minio/store')
      .describe(
        '\nThe URL to the result file will be returned in the <dfn>Assembly Status JSON</dfn>.\n',
      ),
    path: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe path at which the file is to be stored. This may include any available [Assembly variables](https://transloadit.com/docs/topics/assembly-instructions/#assembly-variables). The path must not be a directory.\n',
      )
      .default('${unique_prefix}/${file.url_name}'),
    acl: z
      .union([z.any(), z.enum(['private', 'public-read'])])
      .describe('\nThe permissions used for this file.\n')
      .default('public-read'),
    headers: z
      .record(z.union([z.any(), z.string()]))
      .describe(
        '\nAn object containing a list of headers to be set for this file on MinIO Spaces, such as `{ FileURL: "${file.url_name}" }`. This can also include any available [Assembly Variables](https://transloadit.com/docs/topics/assembly-instructions/#assembly-variables).\n\nObject Metadata can be specified using `x-amz-meta-*` headers. Note that these headers [do not support non-ASCII metadata values](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#UserMetadata).\n',
      )
      .default({ 'Content-Type': '${file.mime}' }),
    sign_urls_for: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gte(0),
      ])
      .describe(
        '\nThis parameter provides signed URLs in the result JSON (in the `signed_ssl_url` property). The number that you set this parameter to is the URL expiry time in seconds.\n\nIf this parameter is not used, no URL signing is done.\n',
      )
      .optional(),
  })
  .strict()

```

#### `/s3/import`

[/s3/import docs](https://transloadit.com/docs/robots/s3-import/)

Robot Parameter Zod Schema:

```ts
const s3ImportSchema = z
  .object({
    credentials: CredentialsSchema,
    ignore_errors: IgnoreErrorsSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    force_name: z
      .union([
        z.union([
          z.any(),
          z.union([z.any(), z.string()]),
          z.union([z.any(), z.array(z.union([z.any(), z.string()]))]),
        ]),
        z.null(),
      ])
      .describe(
        'Custom name for the imported file(s). By default file names are derived from the source.',
      )
      .default(null),
    bucket: z.union([z.any(), z.string()]).optional(),
    bucket_region: z.union([z.any(), z.string()]).optional(),
    key: z.union([z.any(), z.string()]).optional(),
    secret: z.union([z.any(), z.string()]).optional(),
    robot: z
      .literal('/s3/import')
      .describe(
        '\nIf you are new to Amazon S3, see our tutorial on [using your own S3 bucket](https://transloadit.com/docs/faq/how-to-set-up-an-amazon-s3-bucket/).\n\nThe URL to the result file in your S3 bucket will be returned in the <dfn>Assembly Status JSON</dfn>.\n\n> [!Warning]\n> **Use DNS-compliant bucket names**. Your bucket name [must be DNS-compliant](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html) and must not contain uppercase letters. Any non-alphanumeric characters in the file names will be replaced with an underscore, and spaces will be replaced with dashes. If your existing S3 bucket contains uppercase letters or is otherwise not DNS-compliant, rewrite the result URLs using the <dfn>Robot</dfn>’s `url_prefix` parameter.\n\n<span id="minimum-s3-iam-permissions" aria-hidden="true"></span>\n\n## Limit access\n\nYou will also need to add permissions to your bucket so that Transloadit can access it properly. Here is an example IAM policy that you can use. Following the [principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege), it contains the **minimum required permissions** to export a file to your S3 bucket using Transloadit. You may require more permissions (especially viewing permissions) depending on your application.\n\nPlease change `{BUCKET_NAME}` in the values for `Sid` and `Resource` accordingly. Also, this policy will grant the minimum required permissions to all your users. We advise you to create a separate Amazon IAM user, and use its User ARN (can be found in the "Summary" tab of a user [here](https://console.aws.amazon.com/iam/home#users)) for the `Principal` value. More information about this can be found [here](https://docs.aws.amazon.com/AmazonS3/latest/dev/AccessPolicyLanguage_UseCases_s3_a.html).\n\n```json\n{\n  "Version": "2012-10-17",\n  "Statement": [\n    {\n      "Sid": "AllowTransloaditToImportFilesIn{BUCKET_NAME}Bucket",\n      "Effect": "Allow",\n      "Action": ["s3:GetBucketLocation", "s3:ListBucket"],\n      "Resource": ["arn:aws:s3:::{BUCKET_NAME}", "arn:aws:s3:::{BUCKET_NAME}/*"]\n    }\n  ]\n}\n```\n\nThe `Sid` value is just an identifier for you to recognize the rule later. You can name it anything you like.\n\nThe policy needs to be separated into two parts, because the `ListBucket` action requires permissions on the bucket while the other actions require permissions on the objects in the bucket. When targeting the objects there\'s a trailing slash and an asterisk in the `Resource` parameter, whereas when the policy targets the bucket, the slash and the asterisk are omitted.\n\nIn order to build proper result URLs we need to know the region in which your S3 bucket resides. For this we require the `GetBucketLocation` permission. Figuring out your bucket\'s region this way will also slow down your Assemblies. To make this much faster and to also not require the `GetBucketLocation` permission, we have added the `bucket_region` parameter to the /s3/store and /s3/import Robots. We recommend using them at all times.\n\nPlease keep in mind that if you use bucket encryption you may also need to add `"sts:*"` and `"kms:*"` to the bucket policy. Please read [here](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) and [here](https://aws.amazon.com/blogs/security/how-to-restrict-amazon-s3-bucket-access-to-a-specific-iam-role/) in case you run into trouble with our example bucket policy.\n',
      ),
    path: z
      .union([
        z.any(),
        z.union([z.any(), z.string()]),
        z.union([z.any(), z.array(z.union([z.any(), z.string()]))]),
      ])
      .describe(
        "\nThe path in your bucket to the specific file or directory. If the path points to a file, only this file will be imported. For example: `images/avatar.jpg`.\n\nIf it points to a directory, indicated by a trailing slash (`/`), then all files that are direct descendants to this directory will be imported. For example: `images/`.\n\nDirectories are **not** imported recursively. If you want to import files from subdirectories and sub-subdirectories, enable the `recursive` parameter.\n\nIf you want to import all files from the root directory, please use `/` as the value here. In this case, make sure all your objects belong to a path. If you have objects in the root of your bucket that aren't prefixed with `/`, you'll receive an error: `A client error (NoSuchKey) occurred when calling the GetObject operation: The specified key does not exist.`\n\nYou can also use an array of path strings here to import multiple paths in the same <dfn>Robot</dfn>'s <dfn>Step</dfn>.\n",
      ),
    recursive: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nSetting this to `true` will enable importing files from subdirectories and sub-subdirectories (etc.) of the given path.\n\nPlease use the pagination parameters `page_number` and `files_per_page` wisely here.\n',
      )
      .default(false),
    page_number: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int(),
      ])
      .describe(
        '\nThe pagination page number. For now, in order to not break backwards compatibility in non-recursive imports, this only works when recursive is set to `true`.\n\nWhen doing big imports, make sure no files are added or removed from other scripts within your path, otherwise you might get weird results with the pagination.\n',
      )
      .default(1),
    files_per_page: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int(),
      ])
      .describe(
        '\nThe pagination page size. This only works when recursive is `true` for now, in order to not break backwards compatibility in non-recursive imports.\n',
      )
      .default(1000),
    return_file_stubs: z
      .union([
        z.any(),
        z.union([
          z
            .boolean()
            .describe(
              '\nIf set to `true`, the Robot will not yet import the actual files but instead return an empty file stub that includes a URL from where the file can be imported by subsequent Robots. This is useful for cases where subsequent Steps need more control over the import process, such as with 🤖/video/ondemand. This parameter should only be set if all subsequent Steps use Robots that support file stubs.\n',
            ),
          z.any(),
        ]),
      ])
      .describe(
        '\nIf set to `true`, the Robot will not yet import the actual files but instead return an empty file stub that includes a URL from where the file can be imported by subsequent Robots. This is useful for cases where subsequent Steps need more control over the import process, such as with 🤖/video/ondemand. This parameter should only be set if all subsequent Steps use Robots that support file stubs.\n',
      )
      .default(false),
    range: z
      .union([
        z.any(),
        z.union([z.any(), z.string()]),
        z.union([z.any(), z.array(z.union([z.any(), z.string()]))]),
      ])
      .describe(
        '\nAllows you to specify one or more byte ranges to import from the file. S3 must support range requests for this to work.\n\n**Single range**: Use a string like `"0-99"` to import bytes 0-99 (the first 100 bytes).\n\n**Multiple ranges**: Use an array like `["0-99", "200-299"]` to import multiple separate ranges. The resulting file will contain all requested ranges concatenated together, with zero bytes (\\0) filling any gaps between non-contiguous ranges.\n\n**Range formats**:\n- `"0-99"`: Bytes 0 through 99 (inclusive)\n- `"100-199"`: Bytes 100 through 199 (inclusive)\n- `"-100"`: The last 100 bytes of the file\n\n**Important notes**:\n- S3 supports range requests by default\n- Overlapping ranges are allowed and will be included as requested\n- The resulting file size will be the highest byte position requested, with gaps filled with zero bytes\n- Each range is fetched in a separate request to ensure compatibility with S3\n',
      )
      .optional(),
  })
  .strict()

```

#### `/s3/store`

[/s3/store docs](https://transloadit.com/docs/robots/s3-store/)

Robot Parameter Zod Schema:

```ts
const s3StoreSchema = z
  .object({
    credentials: CredentialsSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    bucket: z.union([z.any(), z.string()]).optional(),
    bucket_region: z.union([z.any(), z.string()]).optional(),
    key: z.union([z.any(), z.string()]).optional(),
    secret: z.union([z.any(), z.string()]).optional(),
    robot: z
      .literal('/s3/store')
      .describe(
        '\nIf you are new to Amazon S3, see our tutorial on [using your own S3 bucket](https://transloadit.com/docs/faq/how-to-set-up-an-amazon-s3-bucket/).\n\nThe URL to the result file in your S3 bucket will be returned in the <dfn>Assembly Status JSON</dfn>. If your S3 bucket has versioning enabled, the version ID of the file will be returned within `meta.version_id`\n\n> [!Warning]\n> **Avoid permission errors.** By default, `acl` is set to `"public"`. AWS S3 has a bucket setting called "Block new public ACLs and uploading public objects". Set this to <strong>False</strong> in your bucket if you intend to leave `acl` as `"public"`. Otherwise, you’ll receive permission errors in your Assemblies despite your S3 credentials being configured correctly.\n\n> [!Warning]\n> **Use DNS-compliant bucket names.** Your bucket name [must be DNS-compliant](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucketnamingrules.html) and must not contain uppercase letters. Any non-alphanumeric characters in the file names will be replaced with an underscore, and spaces will be replaced with dashes. If your existing S3 bucket contains uppercase letters or is otherwise not DNS-compliant, rewrite the result URLs using the <dfn>Robot</dfn>’s `url_prefix` parameter.\n\n<span id="minimum-s3-iam-permissions" aria-hidden="true"></span>\n\n## Limit access\n\nYou will also need to add permissions to your bucket so that Transloadit can access it properly. Here is an example IAM policy that you can use. Following the [principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege), it contains the **minimum required permissions** to export a file to your S3 bucket using Transloadit. You may require more permissions (especially viewing permissions) depending on your application.\n\nPlease change `{BUCKET_NAME}` in the values for `Sid` and `Resource` accordingly. Also, this policy will grant the minimum required permissions to all your users. We advise you to create a separate Amazon IAM user, and use its User ARN (can be found in the "Summary" tab of a user [here](https://console.aws.amazon.com/iam/home#users)) for the `Principal` value. More information about this can be found [here](https://docs.aws.amazon.com/AmazonS3/latest/dev/AccessPolicyLanguage_UseCases_s3_a.html).\n\n```json\n{\n  "Version": "2012-10-17",\n  "Statement": [\n    {\n      "Sid": "AllowTransloaditToStoreFilesIn{BUCKET_NAME}Bucket",\n      "Effect": "Allow",\n      "Action": ["s3:GetBucketLocation", "s3:ListBucket", "s3:PutObject", "s3:PutObjectAcl"],\n      "Resource": ["arn:aws:s3:::{BUCKET_NAME}", "arn:aws:s3:::{BUCKET_NAME}/*"]\n    }\n  ]\n}\n```\n\nThe `Sid` value is just an identifier for you to recognize the rule later. You can name it anything you like.\n\nThe policy needs to be separated into two parts, because the `ListBucket` action requires permissions on the bucket while the other actions require permissions on the objects in the bucket. When targeting the objects there\'s a trailing slash and an asterisk in the `Resource` parameter, whereas when the policy targets the bucket, the slash and the asterisk are omitted.\n\nPlease note that if you give the <dfn>Robot</dfn>\'s `acl` parameter a value of `"bucket-default"`, then you do not need the `"s3:PutObjectAcl"` permission in your bucket policy.\n\nIn order to build proper result URLs we need to know the region in which your S3 bucket resides. For this we require the `GetBucketLocation` permission. Figuring out your bucket\'s region this way will also slow down your Assemblies. To make this much faster and to also not require the `GetBucketLocation` permission, we have added the `bucket_region` parameter to the /s3/store and /s3/import Robots. We recommend using them at all times.\n\nPlease keep in mind that if you use bucket encryption you may also need to add `"sts:*"` and `"kms:*"` to the bucket policy. Please read [here](https://docs.aws.amazon.com/kms/latest/developerguide/kms-api-permissions-reference.html) and [here](https://aws.amazon.com/blogs/security/how-to-restrict-amazon-s3-bucket-access-to-a-specific-iam-role/) in case you run into trouble with our example bucket policy.\n',
      ),
    path: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe path at which the file is to be stored. This may include any available [Assembly variables](https://transloadit.com/docs/topics/assembly-instructions/#assembly-variables). The path must not be a directory.\n',
      )
      .default('${unique_prefix}/${file.url_name}'),
    url_prefix: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe URL prefix used for the returned URL, such as `"http://my.cdn.com/some/path/"`.\n',
      )
      .default('http://{bucket}.s3.amazonaws.com/'),
    acl: z
      .union([
        z.any(),
        z.enum(['bucket-default', 'private', 'public', 'public-read']),
      ])
      .describe(
        '\nThe permissions used for this file.\n\nPlease keep in mind that the default value `"public-read"` can lead to permission errors due to the `"Block all public access"` checkbox that is checked by default when creating a new Amazon S3 Bucket in the AWS console.\n',
      )
      .default('public-read'),
    check_integrity: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        "\nCalculate and submit the file's checksum in order for S3 to verify its integrity after uploading, which can help with occasional file corruption issues.\n\nEnabling this option adds to the overall execution time, as integrity checking can be CPU intensive, especially for larger files.\n",
      )
      .default(false),
    headers: z
      .record(z.union([z.any(), z.string()]))
      .describe(
        '\nAn object containing a list of headers to be set for this file on S3, such as `{ FileURL: "${file.url_name}" }`. This can also include any available [Assembly Variables](https://transloadit.com/docs/topics/assembly-instructions/#assembly-variables). You can find a list of available headers [here](https://docs.aws.amazon.com/AmazonS3/latest/API/RESTObjectPUT.html).\n\nObject Metadata can be specified using `x-amz-meta-*` headers. Note that these headers [do not support non-ASCII metadata values](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#UserMetadata).\n',
      )
      .default({ 'Content-Type': '${file.mime}' }),
    tags: z
      .record(z.union([z.any(), z.string()]))
      .describe(
        '\nObject tagging allows you to categorize storage. You can associate up to 10 tags with an object. Tags that are associated with an object must have unique tag keys.\n',
      )
      .default({}),
    host: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe host of the storage service used. This only needs to be set when the storage service used is not Amazon S3, but has a compatible API (such as hosteurope.de). The default protocol used is HTTP, for anything else the protocol needs to be explicitly specified. For example, prefix the host with `https://` or `s3://` to use either respective protocol.\n',
      )
      .default('s3.amazonaws.com'),
    no_vhost: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nSet to `true` if you use a custom host and run into access denied errors.\n',
      )
      .default(false),
    sign_urls_for: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gte(0),
      ])
      .describe(
        '\nThis parameter provides signed URLs in the result JSON (in the `signed_url` and `signed_ssl_url` properties). The number that you set this parameter to is the URL expiry time in seconds. If this parameter is not used, no URL signing is done.\n',
      )
      .optional(),
    session_token: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe session token to use for the S3 store. This is only used if the credentials are from an IAM user with the `sts:AssumeRole` permission.\n',
      )
      .optional(),
  })
  .strict()

```

#### `/script/run`

[/script/run docs](https://transloadit.com/docs/robots/script-run/)

Robot Parameter Zod Schema:

```ts
const scriptRunSchema = z
  .object({
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    robot: z
      .literal('/script/run')
      .describe(
        '\nThis <dfn>Robot</dfn> allows you to run arbitrary `JavaScript` as part of the <dfn>Assembly</dfn>\nexecution process. The <dfn>Robot</dfn> is invoked automatically when there are <dfn>Assembly\nInstructions</dfn> containing `${...}`:\n\n```json\n{\n  "robot": "/image/resize",\n  "width": "${Math.max(file.meta.width, file.meta.height)}"\n}\n```\n\nYou can also invoke this <dfn>Robot</dfn> directly, leaving out the `${...}`:\n\n```json\n{\n  "robot": "/script/run",\n  "script": "Math.max(file.meta.width, file.meta.height)"\n}\n```\n\nWhen accessing arrays, the syntax is the same as in any JavaScript program:\n\n```json\n{\n  "robot": "/image/resize",\n  "width": "${file.meta.faces[0].width * 2}"\n}\n```\n\nCompared to only accessing an <dfn>Assembly Variable</dfn>:\n\n```json\n{\n  "robot": "/image/resize",\n  "width": "${file.meta.faces[0].width}"\n}\n```\n\nFor more information, see [Dynamic Evaluation](https://transloadit.com/docs/topics/dynamic-evaluation/).\n',
      ),
    script: z
      .union([
        z.any(),
        z
          .string()
          .describe(
            '\nA string of JavaScript to evaluate. It has access to all JavaScript features available in a modern browser environment.\n\nThe script is expected to return a `JSON.stringify`-able value in the same tick, so no `await` or callbacks are allowed (yet).\n\nIf the script does not finish within 1000ms it times out with an error. The return value or error is exported as `file.meta.result`. If there was an error, `file.meta.isError` is `true`. Note that the <dfn>Assembly</dfn> will not crash in this case. If you need it to crash, you can check this value with a [🤖/file/filter](https://transloadit.com/docs/robots/file-filter/) <dfn>Step</dfn>, setting `error_on_decline` to `true`.\n\nYou can check whether evaluating this script was free by inspecting `file.meta.isFree`. It is recommended to do this during development as to not see sudden unexpected costs in production.\n',
          ),
      ])
      .describe(
        '\nA string of JavaScript to evaluate. It has access to all JavaScript features available in a modern browser environment.\n\nThe script is expected to return a `JSON.stringify`-able value in the same tick, so no `await` or callbacks are allowed (yet).\n\nIf the script does not finish within 1000ms it times out with an error. The return value or error is exported as `file.meta.result`. If there was an error, `file.meta.isError` is `true`. Note that the <dfn>Assembly</dfn> will not crash in this case. If you need it to crash, you can check this value with a [🤖/file/filter](https://transloadit.com/docs/robots/file-filter/) <dfn>Step</dfn>, setting `error_on_decline` to `true`.\n\nYou can check whether evaluating this script was free by inspecting `file.meta.isFree`. It is recommended to do this during development as to not see sudden unexpected costs in production.\n',
      ),
  })
  .strict()

```

#### `/sftp/import`

[/sftp/import docs](https://transloadit.com/docs/robots/sftp-import/)

Robot Parameter Zod Schema:

```ts
const sftpImportSchema = z
  .object({
    credentials: CredentialsSchema,
    ignore_errors: IgnoreErrorsSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    force_name: z
      .union([
        z.union([
          z.any(),
          z.union([z.any(), z.string()]),
          z.union([z.any(), z.array(z.union([z.any(), z.string()]))]),
        ]),
        z.null(),
      ])
      .describe(
        'Custom name for the imported file(s). By default file names are derived from the source.',
      )
      .default(null),
    host: z.union([z.any(), z.string()]).optional(),
    port: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gte(1).lte(65535),
      ])
      .describe('The port to use for the FTP connection.')
      .default(21),
    user: z.union([z.any(), z.string()]).optional(),
    public_key: z.union([z.any(), z.string()]).optional(),
    robot: z.literal('/sftp/import'),
    path: z
      .union([
        z.any(),
        z
          .string()
          .describe(
            '\nThe path on your SFTP server where to search for files.\n',
          ),
      ])
      .describe('\nThe path on your SFTP server where to search for files.\n'),
  })
  .strict()

```

#### `/sftp/store`

[/sftp/store docs](https://transloadit.com/docs/robots/sftp-store/)

Robot Parameter Zod Schema:

```ts
const sftpStoreSchema = z
  .object({
    credentials: CredentialsSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    host: z.union([z.any(), z.string()]).optional(),
    port: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gte(1).lte(65535),
      ])
      .describe('The port to use for the FTP connection.')
      .default(21),
    user: z.union([z.any(), z.string()]).optional(),
    public_key: z.union([z.any(), z.string()]).optional(),
    robot: z.literal('/sftp/store'),
    path: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe path at which the file is to be stored. This may include any available [Assembly variables](https://transloadit.com/docs/topics/assembly-instructions/#assembly-variables).\n',
      )
      .default('${unique_prefix}/${file.url_name}'),
    url_template: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe URL of the file in the result JSON. This may include any of the following supported [Assembly variables](https://transloadit.com/docs/topics/assembly-instructions/#assembly-variables).\n',
      )
      .default('http://host/path'),
    ssl_url_template: z
      .union([z.any(), z.string()])
      .describe(
        '\n  The SSL URL of the file in the result JSON. The following [Assembly variables](https://transloadit.com/docs/topics/assembly-instructions/#assembly-variables) are supported.\n',
      )
      .default('https://{HOST}/{PATH}'),
    file_chmod: z
      .union([z.any(), z.string().regex(new RegExp('([0-7]{3}|auto)'))])
      .describe(
        "\nThis optional parameter controls how an uploaded file's permission bits are set. You can use any string format that the `chmod` command would accept, such as `\"755\"`. If you don't specify this option, the file's permission bits aren't changed at all, meaning it's up to your server's configuration (e.g. umask).\n      ",
      )
      .default('auto'),
  })
  .strict()

```

#### `/speech/transcribe`

[/speech/transcribe docs](https://transloadit.com/docs/robots/speech-transcribe/)

Robot Parameter Zod Schema:

```ts
const speechTranscribeSchema = z
  .object({
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    robot: z
      .literal('/speech/transcribe')
      .describe(
        '\nYou can use the text that we return in your application, or you can pass the text down to other <dfn>Robots</dfn> to filter audio or video files that contain (or do not contain) certain content, or burn the text into images or video for example.\n\nAnother common use case is automatically subtitling videos, or making audio searchable.\n',
      ),
    provider: z
      .union([
        z.any(),
        z
          .enum(['aws', 'gcp', 'replicate', 'fal', 'transloadit'])
          .describe(
            '\nWhich AI provider to leverage.\n\nTransloadit outsources this task and abstracts the interface so you can expect the same data structures, but different latencies and information being returned. Different cloud vendors have different areas they shine in, and we recommend to try out and see what yields the best results for your use case.\n',
          ),
      ])
      .describe(
        '\nWhich AI provider to leverage.\n\nTransloadit outsources this task and abstracts the interface so you can expect the same data structures, but different latencies and information being returned. Different cloud vendors have different areas they shine in, and we recommend to try out and see what yields the best results for your use case.\n',
      ),
    granularity: z
      .union([z.any(), z.enum(['full', 'list'])])
      .describe(
        '\nWhether to return a full response (`"full"`), or a flat list of descriptions (`"list"`).\n',
      )
      .default('full'),
    format: z
      .union([
        z.any(),
        z.enum(['json', 'meta', 'srt', 'meta', 'text', 'webvtt']),
      ])
      .describe(
        '\nOutput format for the transcription.\n\n- `"text"` outputs a plain text file that you can store and process.\n- `"json"` outputs a JSON file containing timestamped words.\n- `"srt"` and `"webvtt"` output subtitle files of those respective file types, which can be stored separately or used in other encoding <dfn>Steps</dfn>.\n- `"meta"` does not return a file, but stores the data inside  Transloadit\'s file object (under `${file.meta.transcription.text}`) that\'s passed around between encoding <dfn>Steps</dfn>, so that you can use the values to burn the data into videos, filter on them, etc.\n',
      )
      .default('json'),
    source_language: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe spoken language of the audio or video. This will also be the language of the transcribed text.\n\nThe language should be specified in the [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) format, such as `"en-GB"`, `"de-DE"` or `"fr-FR"`. Please also consult the list of supported languages for [the `gcp` provider](https://cloud.google.com/speech-to-text/docs/languages) and the [the `aws` provider](https://docs.aws.amazon.com/transcribe/latest/dg/what-is-transcribe.html).\n',
      )
      .default('en-US'),
    target_language: z
      .union([z.any(), z.string()])
      .describe(
        '\n      This will also be the language of the written text.\n\n      The language should be specified in the [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) format, such as `"en-GB"`, `"de-DE"` or `"fr-FR"`. Please consult the list of supported languages and voices.\n    ',
      )
      .default('en-US'),
  })
  .strict()

```

#### `/supabase/import`

[/supabase/import docs](https://transloadit.com/docs/robots/supabase-import/)

Robot Parameter Zod Schema:

```ts
const supabaseImportSchema = z
  .object({
    credentials: CredentialsSchema,
    ignore_errors: IgnoreErrorsSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    force_name: z
      .union([
        z.union([
          z.any(),
          z.union([z.any(), z.string()]),
          z.union([z.any(), z.array(z.union([z.any(), z.string()]))]),
        ]),
        z.null(),
      ])
      .describe(
        'Custom name for the imported file(s). By default file names are derived from the source.',
      )
      .default(null),
    bucket: z.union([z.any(), z.string()]).optional(),
    bucket_region: z
      .union([z.any(), z.string()])
      .describe('\nThe region where the bucket is located.\n')
      .optional(),
    host: z.union([z.any(), z.string()]).optional(),
    key: z.union([z.any(), z.string()]).optional(),
    secret: z.union([z.any(), z.string()]).optional(),
    robot: z
      .literal('/supabase/import')
      .describe(
        '\nThe URL to the result file will be returned in the <dfn>Assembly Status JSON</dfn>.\n',
      ),
    path: z
      .union([
        z.any(),
        z.union([z.any(), z.string()]),
        z.union([z.any(), z.array(z.union([z.any(), z.string()]))]),
      ])
      .describe(
        "\nThe path in your bucket to the specific file or directory. If the path points to a file, only this file will be imported. For example: `images/avatar.jpg`.\n\nIf it points to a directory, indicated by a trailing slash (`/`), then all files that are direct descendants of this directory will be imported. For example: `images/`.\n\nDirectories are **not** imported recursively. If you want to import files from subdirectories and sub-subdirectories, enable the `recursive` parameter.\n\nIf you want to import all files from the root directory, please use `/` as the value here. In this case, make sure all your objects belong to a path. If you have objects in the root of your bucket that aren't prefixed with `/`, you'll receive an error: `A client error (NoSuchKey) occurred when calling the GetObject operation: The specified key does not exist.`\n\nYou can also use an array of path strings here to import multiple paths in the same <dfn>Robot</dfn>'s <dfn>Step</dfn>.\n",
      ),
    recursive: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nSetting this to `true` will enable importing files from subfolders and sub-subfolders, etc. of the given path.\n\nPlease use the pagination parameters `page_number` and `files_per_page` wisely here.\n',
      )
      .default(false),
    page_number: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int(),
      ])
      .describe(
        '\nThe pagination page number. For now, in order to not break backwards compatibility in non-recursive imports, this only works when recursive is set to `true`.\n\nWhen doing big imports, make sure no files are added or removed from other scripts within your path, otherwise you might get weird results with the pagination.\n',
      )
      .default(1),
    files_per_page: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int(),
      ])
      .describe(
        '\nThe pagination page size. This only works when recursive is `true` for now, in order to not break backwards compatibility in non-recursive imports.\n',
      )
      .default(1000),
    return_file_stubs: z
      .union([
        z.any(),
        z.union([
          z
            .boolean()
            .describe(
              '\nIf set to `true`, the Robot will not yet import the actual files but instead return an empty file stub that includes a URL from where the file can be imported by subsequent Robots. This is useful for cases where subsequent Steps need more control over the import process, such as with 🤖/video/ondemand. This parameter should only be set if all subsequent Steps use Robots that support file stubs.\n',
            ),
          z.any(),
        ]),
      ])
      .describe(
        '\nIf set to `true`, the Robot will not yet import the actual files but instead return an empty file stub that includes a URL from where the file can be imported by subsequent Robots. This is useful for cases where subsequent Steps need more control over the import process, such as with 🤖/video/ondemand. This parameter should only be set if all subsequent Steps use Robots that support file stubs.\n',
      )
      .default(false),
  })
  .strict()

```

#### `/supabase/store`

[/supabase/store docs](https://transloadit.com/docs/robots/supabase-store/)

Robot Parameter Zod Schema:

```ts
const supabaseStoreSchema = z
  .object({
    credentials: CredentialsSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    bucket: z.union([z.any(), z.string()]).optional(),
    bucket_region: z
      .union([z.any(), z.string()])
      .describe('\nThe region where the bucket is located.\n')
      .optional(),
    host: z.union([z.any(), z.string()]).optional(),
    key: z.union([z.any(), z.string()]).optional(),
    secret: z.union([z.any(), z.string()]).optional(),
    robot: z.literal('/supabase/store'),
    path: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe path at which the file is to be stored. This may include any available [Assembly variables](https://transloadit.com/docs/topics/assembly-instructions/#assembly-variables). The path must not be a directory.\n',
      )
      .default('${unique_prefix}/${file.url_name}'),
    headers: z
      .record(z.union([z.any(), z.string()]))
      .describe(
        '\nAn object containing a list of headers to be set for this file on supabase Spaces, such as `{ FileURL: "${file.url_name}" }`. This can also include any available [Assembly Variables](https://transloadit.com/docs/topics/assembly-instructions/#assembly-variables).\n\nObject Metadata can be specified using `x-amz-meta-*` headers. Note that these headers [do not support non-ASCII metadata values](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#UserMetadata).\n',
      )
      .default({ 'Content-Type': '${file.mime}' }),
    sign_urls_for: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gte(0),
      ])
      .describe(
        '\nThis parameter provides signed URLs in the result JSON (in the `signed_ssl_url` property). The number that you set this parameter to is the URL expiry time in seconds. If this parameter is not used, no URL signing is done.\n',
      )
      .optional(),
  })
  .strict()

```

#### `/swift/import`

[/swift/import docs](https://transloadit.com/docs/robots/swift-import/)

Robot Parameter Zod Schema:

```ts
const swiftImportSchema = z
  .object({
    credentials: CredentialsSchema,
    ignore_errors: IgnoreErrorsSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    force_name: z
      .union([
        z.union([
          z.any(),
          z.union([z.any(), z.string()]),
          z.union([z.any(), z.array(z.union([z.any(), z.string()]))]),
        ]),
        z.null(),
      ])
      .describe(
        'Custom name for the imported file(s). By default file names are derived from the source.',
      )
      .default(null),
    bucket: z.union([z.any(), z.string()]).optional(),
    bucket_region: z
      .union([z.any(), z.string()])
      .describe('\nThe region where the bucket is located.\n')
      .optional(),
    host: z.union([z.any(), z.string()]).optional(),
    key: z.union([z.any(), z.string()]).optional(),
    secret: z.union([z.any(), z.string()]).optional(),
    robot: z.literal('/swift/import'),
    path: z
      .union([
        z.any(),
        z.union([z.any(), z.string()]),
        z.union([z.any(), z.array(z.union([z.any(), z.string()]))]),
      ])
      .describe(
        "\nThe path in your bucket to the specific file or directory. If the path points to a file, only this file will be imported. For example: `images/avatar.jpg`.\n\nIf it points to a directory, indicated by a trailing slash (`/`), then all files that are direct descendants of this directory will be imported. For example: `images/`.\n\nDirectories are **not** imported recursively. If you want to import files from subdirectories and sub-subdirectories, enable the `recursive` parameter.\n\nIf you want to import all files from the root directory, please use `/` as the value here. In this case, make sure all your objects belong to a path. If you have objects in the root of your bucket that aren't prefixed with `/`, you'll receive an error: `A client error (NoSuchKey) occurred when calling the GetObject operation: The specified key does not exist.`\n\nYou can also use an array of path strings here to import multiple paths in the same <dfn>Robot</dfn>'s <dfn>Step</dfn>.\n",
      ),
    recursive: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nSetting this to `true` will enable importing files from subdirectories and sub-subdirectories (etc.) of the given path.\n\nPlease use the pagination parameters `page_number` and `files_per_page` wisely here.\n',
      )
      .default(false),
    page_number: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int(),
      ])
      .describe(
        '\nThe pagination page number. For now, in order to not break backwards compatibility in non-recursive imports, this only works when recursive is set to `true`.\n\nWhen doing big imports, make sure no files are added or removed from other scripts within your path, otherwise you might get weird results with the pagination.\n',
      )
      .default(1),
    files_per_page: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int(),
      ])
      .describe(
        '\nThe pagination page size. This only works when recursive is `true` for now, in order to not break backwards compatibility in non-recursive imports.\n',
      )
      .default(1000),
    return_file_stubs: z
      .union([
        z.any(),
        z.union([
          z
            .boolean()
            .describe(
              '\nIf set to `true`, the Robot will not yet import the actual files but instead return an empty file stub that includes a URL from where the file can be imported by subsequent Robots. This is useful for cases where subsequent Steps need more control over the import process, such as with 🤖/video/ondemand. This parameter should only be set if all subsequent Steps use Robots that support file stubs.\n',
            ),
          z.any(),
        ]),
      ])
      .describe(
        '\nIf set to `true`, the Robot will not yet import the actual files but instead return an empty file stub that includes a URL from where the file can be imported by subsequent Robots. This is useful for cases where subsequent Steps need more control over the import process, such as with 🤖/video/ondemand. This parameter should only be set if all subsequent Steps use Robots that support file stubs.\n',
      )
      .default(false),
  })
  .strict()

```

#### `/swift/store`

[/swift/store docs](https://transloadit.com/docs/robots/swift-store/)

Robot Parameter Zod Schema:

```ts
const swiftStoreSchema = z
  .object({
    credentials: CredentialsSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    bucket: z.union([z.any(), z.string()]).optional(),
    bucket_region: z
      .union([z.any(), z.string()])
      .describe('\nThe region where the bucket is located.\n')
      .optional(),
    host: z.union([z.any(), z.string()]).optional(),
    key: z.union([z.any(), z.string()]).optional(),
    secret: z.union([z.any(), z.string()]).optional(),
    robot: z
      .literal('/swift/store')
      .describe(
        '\nThe URL to the result file in your OpenStack bucket will be returned in the <dfn>Assembly Status JSON</dfn>.',
      ),
    path: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe path at which the file is to be stored. This may include any available [Assembly variables](https://transloadit.com/docs/topics/assembly-instructions/#assembly-variables). The path must not be a directory.\n',
      )
      .default('${unique_prefix}/${file.url_name}'),
    acl: z
      .union([z.any(), z.enum(['private', 'public-read'])])
      .describe('\nThe permissions used for this file.\n')
      .default('public-read'),
    headers: z
      .record(z.union([z.any(), z.string()]))
      .describe(
        '\nAn object containing a list of headers to be set for this file on swift Spaces, such as `{ FileURL: "${file.url_name}" }`. This can also include any available [Assembly Variables](https://transloadit.com/docs/topics/assembly-instructions/#assembly-variables).\n\nObject Metadata can be specified using `x-amz-meta-*` headers. Note that these headers [do not support non-ASCII metadata values](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#UserMetadata).\n',
      )
      .default({ 'Content-Type': '${file.mime}' }),
    sign_urls_for: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gte(0),
      ])
      .describe(
        '\nThis parameter provides signed URLs in the result JSON (in the `signed_ssl_url` property). The number that you set this parameter to is the URL expiry time in seconds. If this parameter is not used, no URL signing is done.\n',
      )
      .optional(),
  })
  .strict()

```

#### `/text/speak`

[/text/speak docs](https://transloadit.com/docs/robots/text-speak/)

Robot Parameter Zod Schema:

```ts
const textSpeakSchema = z
  .object({
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    robot: z
      .literal('/text/speak')
      .describe(
        '\nYou can use the audio that we return in your application, or you can pass the audio down to other <dfn>Robots</dfn> to add a voice track to a video for example.\n\nAnother common use case is making your product accessible to people with a reading disability.\n',
      ),
    prompt: z
      .union([z.union([z.any(), z.string()]), z.null()])
      .describe(
        '\nWhich text to speak. You can also set this to `null` and supply an input text file.\n',
      )
      .optional(),
    provider: z
      .union([
        z.any(),
        z
          .enum(['aws', 'gcp', 'replicate', 'fal', 'transloadit'])
          .describe(
            '\nWhich AI provider to leverage.\n\nTransloadit outsources this task and abstracts the interface so you can expect the same data structures, but different latencies and information being returned. Different cloud vendors have different areas they shine in, and we recommend to try out and see what yields the best results for your use case.\n',
          ),
      ])
      .describe(
        '\nWhich AI provider to leverage.\n\nTransloadit outsources this task and abstracts the interface so you can expect the same data structures, but different latencies and information being returned. Different cloud vendors have different areas they shine in, and we recommend to try out and see what yields the best results for your use case.\n',
      ),
    target_language: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe written language of the document. This will also be the language of the spoken text.\n\nThe language should be specified in the [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) format, such as `"en-GB"`, `"de-DE"` or `"fr-FR"`. Please consult the list of supported languages and voices.\n',
      )
      .default('en-US'),
    voice: z
      .union([
        z.any(),
        z.enum([
          'female-1',
          'female-2',
          'female-3',
          'female-child-1',
          'male-1',
          'male-child-1',
        ]),
      ])
      .describe(
        '\nThe gender to be used for voice synthesis. Please consult the list of supported languages and voices.\n      ',
      )
      .default('female-1'),
    ssml: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nSupply [Speech Synthesis Markup Language](https://en.wikipedia.org/wiki/Speech_Synthesis_Markup_Language) instead of raw text, in order to gain more control over how your text is voiced, including rests and pronounciations.\n\nPlease see the supported syntaxes for [AWS](https://docs.aws.amazon.com/polly/latest/dg/supportedtags.html) and [GCP](https://cloud.google.com/text-to-speech/docs/ssml).\n',
      )
      .default(false),
  })
  .strict()

```

#### `/text/translate`

[/text/translate docs](https://transloadit.com/docs/robots/text-translate/)

Robot Parameter Zod Schema:

```ts
const textTranslateSchema = z
  .object({
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    robot: z
      .literal('/text/translate')
      .describe(
        '\nYou can use the text that we return in your application, or you can pass the text down to other <dfn>Robots</dfn> to add a translated subtitle track to a video for example.\n\n> [!Note]\n> **This <dfn>Robot</dfn> accepts only files with a `text/*` MIME-type,** including plain text and Markdown. For documents in other formats, use [🤖/document/convert](https://transloadit.com/docs/robots/document-convert/) to first convert them into a compatible text format before proceeding.\n',
      ),
    provider: z
      .union([
        z.any(),
        z
          .enum(['aws', 'gcp', 'replicate', 'fal', 'transloadit'])
          .describe(
            '\nWhich AI provider to leverage. Valid values are `"aws"` (Amazon Web Services) and `"gcp"` (Google Cloud Platform).\n\nTransloadit outsources this task and abstracts the interface so you can expect the same data structures, but different latencies and information being returned. Different cloud vendors have different areas they shine in, and we recommend to try out and see what yields the best results for your use case.\n',
          ),
      ])
      .describe(
        '\nWhich AI provider to leverage. Valid values are `"aws"` (Amazon Web Services) and `"gcp"` (Google Cloud Platform).\n\nTransloadit outsources this task and abstracts the interface so you can expect the same data structures, but different latencies and information being returned. Different cloud vendors have different areas they shine in, and we recommend to try out and see what yields the best results for your use case.\n',
      ),
    target_language: z
      .union([
        z.any(),
        z.enum([
          'af',
          'am',
          'ar',
          'az',
          'be',
          'bg',
          'bn',
          'bs',
          'ca',
          'ceb',
          'co',
          'cs',
          'cy',
          'da',
          'de',
          'el',
          'en',
          'en-US',
          'eo',
          'es',
          'es-MX',
          'et',
          'eu',
          'fa',
          'fa-AF',
          'fi',
          'fr',
          'fr-CA',
          'fy',
          'ga',
          'gd',
          'gl',
          'gu',
          'ha',
          'haw',
          'he',
          'hi',
          'hmn',
          'hr',
          'ht',
          'hu',
          'hy',
          'id',
          'ig',
          'is',
          'it',
          'iw',
          'ja',
          'jv',
          'ka',
          'kk',
          'km',
          'kn',
          'ko',
          'ku',
          'ky',
          'la',
          'lb',
          'lo',
          'lt',
          'lv',
          'mg',
          'mi',
          'mk',
          'ml',
          'mn',
          'mr',
          'ms',
          'mt',
          'my',
          'ne',
          'nl',
          'no',
          'ny',
          'or',
          'pa',
          'pl',
          'ps',
          'pt',
          'ro',
          'ru',
          'rw',
          'sd',
          'si',
          'sk',
          'sl',
          'sm',
          'sn',
          'so',
          'sq',
          'sr',
          'st',
          'su',
          'sv',
          'sw',
          'ta',
          'te',
          'tg',
          'th',
          'tk',
          'tl',
          'tr',
          'tt',
          'ug',
          'uk',
          'ur',
          'uz',
          'vi',
          'xh',
          'yi',
          'yo',
          'zh',
          'zh-CN',
          'zh-TW',
          'zu',
        ]),
      ])
      .describe(
        '\nThe desired language to translate to.\n\nIf the exact language can\'t be found, a generic variant can be fallen back to. For example, if you specify `"en-US"`, "en" will be used instead. Please consult the list of supported languages for each provider.\n',
      )
      .default('en'),
    source_language: z
      .union([z.any(), z.any()])
      .describe(
        '\nThe desired language to translate from.\n\nBy default, both providers will detect this automatically, but there are cases where specifying the source language prevents ambiguities.\n\nIf the exact language can\'t be found, a generic variant can be fallen back to. For example, if you specify `"en-US"`, "en" will be used instead. Please consult the list of supported languages for each provider.\n',
      )
      .default('en'),
  })
  .strict()

```

#### `/tigris/import`

[/tigris/import docs](https://transloadit.com/docs/robots/tigris-import/)

Robot Parameter Zod Schema:

```ts
const tigrisImportSchema = z
  .object({
    credentials: CredentialsSchema,
    ignore_errors: IgnoreErrorsSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    force_name: z
      .union([
        z.union([
          z.any(),
          z.union([z.any(), z.string()]),
          z.union([z.any(), z.array(z.union([z.any(), z.string()]))]),
        ]),
        z.null(),
      ])
      .describe(
        'Custom name for the imported file(s). By default file names are derived from the source.',
      )
      .default(null),
    bucket: z.union([z.any(), z.string()]).optional(),
    bucket_region: z
      .union([z.any(), z.string()])
      .describe(
        'The region of your Tigris bucket. This is optional as it can often be derived.',
      )
      .optional(),
    host: z.union([z.any(), z.string()]).optional(),
    key: z.union([z.any(), z.string()]).optional(),
    secret: z.union([z.any(), z.string()]).optional(),
    robot: z.literal('/tigris/import'),
    path: z
      .union([
        z.any(),
        z.union([z.any(), z.string()]),
        z.union([z.any(), z.array(z.union([z.any(), z.string()]))]),
      ])
      .describe(
        "\nThe path in your bucket to the specific file or directory. If the path points to a file, only this file will be imported. For example: `images/avatar.jpg`.\n\nIf it points to a directory, indicated by a trailing slash (`/`), then all files that are direct descendants of this directory will be imported. For example: `images/`.\n\nDirectories are **not** imported recursively. If you want to import files from subdirectories and sub-subdirectories, enable the `recursive` parameter.\n\nIf you want to import all files from the root directory, please use `/` as the value here. In this case, make sure all your objects belong to a path. If you have objects in the root of your bucket that aren't prefixed with `/`, you'll receive an error: `A client error (NoSuchKey) occurred when calling the GetObject operation: The specified key does not exist.`\n\nYou can also use an array of path strings here to import multiple paths in the same <dfn>Robot</dfn>'s <dfn>Step</dfn>.\n",
      ),
    recursive: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nSetting this to `true` will enable importing files from subdirectories and sub-subdirectories (etc.) of the given path.\n\nPlease use the pagination parameters `page_number` and `files_per_page` wisely here.\n',
      )
      .default(false),
    page_number: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int(),
      ])
      .describe(
        '\nThe pagination page number. For now, in order to not break backwards compatibility in non-recursive imports, this only works when recursive is set to `true`.\n\nWhen doing big imports, make sure no files are added or removed from other scripts within your path, otherwise you might get weird results with the pagination.\n',
      )
      .default(1),
    files_per_page: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int(),
      ])
      .describe(
        '\nThe pagination page size. This only works when recursive is `true` for now, in order to not break backwards compatibility in non-recursive imports.\n',
      )
      .default(1000),
    return_file_stubs: z
      .union([
        z.any(),
        z.union([
          z
            .boolean()
            .describe(
              '\nIf set to `true`, the Robot will not yet import the actual files but instead return an empty file stub that includes a URL from where the file can be imported by subsequent Robots. This is useful for cases where subsequent Steps need more control over the import process, such as with 🤖/video/ondemand. This parameter should only be set if all subsequent Steps use Robots that support file stubs.\n',
            ),
          z.any(),
        ]),
      ])
      .describe(
        '\nIf set to `true`, the Robot will not yet import the actual files but instead return an empty file stub that includes a URL from where the file can be imported by subsequent Robots. This is useful for cases where subsequent Steps need more control over the import process, such as with 🤖/video/ondemand. This parameter should only be set if all subsequent Steps use Robots that support file stubs.\n',
      )
      .default(false),
  })
  .strict()

```

#### `/tigris/store`

[/tigris/store docs](https://transloadit.com/docs/robots/tigris-store/)

Robot Parameter Zod Schema:

```ts
const tigrisStoreSchema = z
  .object({
    credentials: CredentialsSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    bucket: z.union([z.any(), z.string()]).optional(),
    bucket_region: z
      .union([z.any(), z.string()])
      .describe(
        'The region of your Tigris bucket. This is optional as it can often be derived.',
      )
      .optional(),
    host: z.union([z.any(), z.string()]).optional(),
    key: z.union([z.any(), z.string()]).optional(),
    secret: z.union([z.any(), z.string()]).optional(),
    robot: z
      .literal('/tigris/store')
      .describe(
        '\nThe URL to the result file will be returned in the <dfn>Assembly Status JSON</dfn>.\n',
      ),
    path: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe path at which the file is to be stored. This may include any available [Assembly variables](https://transloadit.com/docs/topics/assembly-instructions/#assembly-variables). The path must not be a directory.\n',
      )
      .default('${unique_prefix}/${file.url_name}'),
    acl: z
      .union([z.any(), z.enum(['private', 'public-read'])])
      .describe('\nThe permissions used for this file.\n')
      .default('public-read'),
    headers: z
      .record(z.union([z.any(), z.string()]))
      .describe(
        '\nAn object containing a list of headers to be set for this file on Tigris, such as `{ FileURL: "${file.url_name}" }`. This can also include any available [Assembly Variables](https://transloadit.com/docs/topics/assembly-instructions/#assembly-variables).\n\nObject Metadata can be specified using `x-amz-meta-*` headers. Note that these headers [do not support non-ASCII metadata values](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#UserMetadata).\n',
      )
      .default({ 'Content-Type': '${file.mime}' }),
    sign_urls_for: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gte(0),
      ])
      .describe(
        '\nThis parameter provides signed URLs in the result JSON (in the `signed_ssl_url` property). The number that you set this parameter to is the URL expiry time in seconds.\n\nIf this parameter is not used, no URL signing is done.\n',
      )
      .optional(),
  })
  .strict()

```

#### `/tlcdn/deliver`

[/tlcdn/deliver docs](https://transloadit.com/docs/robots/tlcdn-deliver/)

Robot Parameter Zod Schema:

```ts
const tlcdnDeliverSchema = z
  .object({
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    robot: z
      .literal('/tlcdn/deliver')
      .describe(
        '\nWhen you want Transloadit to tranform files on the fly, this <dfn>Robot</dfn> can cache and deliver the results close to your end-user, saving on latency and encoding volume. The use of this <dfn>Robot</dfn> is implicit when you use the <code>tlcdn.com</code> domain.\n',
      ),
  })
  .strict()

```

#### `/tus/store`

[/tus/store docs](https://transloadit.com/docs/robots/tus-store/)

Robot Parameter Zod Schema:

```ts
const tusStoreSchema = z
  .object({
    credentials: CredentialsSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    robot: z
      .literal('/tus/store')
      .describe(
        "\n> [!Note]\n> This <dfn>Robot</dfn> only accepts videos.\n\n> [!Warning]\n> Vimeo's API limits the number of concurrent uploads per minute based on your Vimeo account plan. To see how many videos can be uploaded at once based on your plan, click the following [link](https://developer.vimeo.com/guidelines/rate-limiting#table-1).\n\n## Installation\n\nSince Vimeo works with OAuth, you will need to generate [Template Credentials](https://transloadit.com/c/template-credentials/) to use this <dfn>Robot</dfn>.\n\nTo change the `title` or `description` per video, we recommend to [inject variables into your Template](https://transloadit.com/docs/topics/templates/).\n",
      ),
    endpoint: z
      .union([
        z.any(),
        z
          .string()
          .url()
          .describe(
            "\nThe URL of the Tus-compatible server, which you're uploading files to.\n",
          ),
      ])
      .describe(
        "\nThe URL of the Tus-compatible server, which you're uploading files to.\n",
      ),
    headers: z
      .record(z.union([z.any(), z.string()]))
      .describe(
        "\nOptional extra headers outside of the <dfn>Template Credentials</dfn> can be passed along within this parameter.\n\nAlthough, we recommend to exclusively use <dfn>Template Credentials</dfn>, this may be necessary if you're looking to use dynamic credentials, which isn't a feature supported by <dfn>Template Credentials</dfn>.\n",
      )
      .default({}),
    metadata: z
      .record(z.union([z.any(), z.string()]))
      .describe(
        '\nMetadata to pass along to destination. Includes some file info by default.\n',
      )
      .default({
        filename: 'example.png',
        basename: 'example',
        extension: 'png',
      }),
    url_template: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe URL of the file in the <dfn>Assembly Status JSON</dfn>. The following [Assembly Variables](https://transloadit.com/docs/topics/assembly-instructions/#assembly-variables) are supported. If this is not specified, the upload URL specified by the destination server will be used instead.\n',
      )
      .optional(),
    ssl_url_template: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe SSL URL of the file in the <dfn>Assembly Status JSON</dfn>. The following [Assembly Variables](https://transloadit.com/docs/topics/assembly-instructions/#assembly-variables) are supported. If this is not specified, the upload URL specified by the destination server will be used instead, as long as it starts with `https`.\n',
      )
      .optional(),
  })
  .strict()

```

#### `/upload/handle`

[/upload/handle docs](https://transloadit.com/docs/robots/upload-handle/)

Robot Parameter Zod Schema:

```ts
const uploadHandleSchema = z
  .object({
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    robot: z
      .literal('/upload/handle')
      .describe(
        '\nTransloadit handles file uploads by default, so specifying this <dfn>Robot</dfn> is optional.\n\nIt can still be a good idea to define this <dfn>Robot</dfn>, though. It makes your <dfn>Assembly Instructions</dfn> explicit, and allows you to configure exactly how uploads should be handled. For example, you can extract specific metadata from the uploaded files.\n\nThere are **3 important constraints** when using this <dfn>Robot</dfn>:\n\n1. Don’t define a `use` parameter, unlike with other <dfn>Robots</dfn>.\n2. Use it only once in a single set of <dfn>Assembly Instructions</dfn>.\n3. Name the Step as `:original`.\n',
      ),
  })
  .strict()

```

#### `/video/adaptive`

[/video/adaptive docs](https://transloadit.com/docs/robots/video-adaptive/)

Robot Parameter Zod Schema:

```ts
const videoAdaptiveSchema = z
  .object({
    preset: VideoPresetSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    ffmpeg_stack: FfmpegStackSchema,
    use: UseSchema,
    ffmpeg: FfmpegSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    width: z
      .union([
        z.union([
          z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
          z.any(),
          z.number().int().gte(1),
        ]),
        z.null(),
      ])
      .describe(
        "\nWidth of the new video, in pixels.\n\nIf the value is not specified and the `preset` parameter is available, the `preset`'s [supplied width](https://transloadit.com/docs/presets/video/) will be implemented.\n",
      )
      .optional(),
    height: z
      .union([
        z.union([
          z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
          z.any(),
          z.number().int().gte(1),
        ]),
        z.null(),
      ])
      .describe(
        "\nHeight of the new video, in pixels.\n\nIf the value is not specified and the `preset` parameter is available, the `preset`'s [supplied height](https://transloadit.com/docs/presets/video/) will be implemented.\n",
      )
      .optional(),
    robot: z
      .literal('/video/adaptive')
      .describe(
        '\nThis <dfn>Robot</dfn> accepts all types of video files and audio files. Do not forget to use <dfn>Step</dfn> bundling in your `use` parameter to make the <dfn>Robot</dfn> work on several input files at once.\n\nThis <dfn>Robot</dfn> is normally used in combination with [🤖/video/encode](https://transloadit.com/docs/robots/video-encode/). We have implemented video and audio encoding presets specifically for MPEG-Dash and HTTP Live Streaming support. These presets are prefixed with `"dash/"` and `"hls/"`. [View a HTTP Live Streaming demo here](https://transloadit.com/demos/video-encoding/implement-http-live-streaming/).\n\n### Required CORS settings for MPEG-Dash and HTTP Live Streaming\n\nPlaying back MPEG-Dash Manifest or HLS playlist files requires a proper CORS setup on the server-side. The file-serving server should be configured to add the following header fields to responses:\n\n```\nAccess-Control-Allow-Origin: *\nAccess-Control-Allow-Methods: GET\nAccess-Control-Allow-Headers: *\n```\n\nIf the files are stored in an Amazon S3 Bucket, you can use the following [CORS definition](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ManageCorsUsing.html) to ensure the CORS header fields are set correctly:\n\n```json\n[\n  {\n    "AllowedHeaders": ["*"],\n    "AllowedMethods": ["GET"],\n    "AllowedOrigins": ["*"],\n    "ExposeHeaders": []\n  }\n]\n```\n\nTo set up CORS for your S3 bucket:\n\n1. Visit <https://s3.console.aws.amazon.com/s3/buckets/>\n1. Click on your bucket\n1. Click "Permissions"\n1. Edit "Cross-origin resource sharing (CORS)"\n\n### Storing Segments and Playlist files\n\nThe <dfn>Robot</dfn> gives its result files (segments, initialization segments, MPD manifest files and M3U8 playlist files) the right metadata property `relative_path`, so that you can store them easily using one of our storage <dfn>Robots</dfn>.\n\nIn the `path` parameter of the storage <dfn>Robot</dfn> of your choice, use the <dfn>Assembly Variable</dfn> `${file.meta.relative_path}` to store files in the proper paths to make the playlist files work.\n',
      ),
    technique: z
      .union([z.any(), z.enum(['dash', 'hls'])])
      .describe(
        '\nDetermines which streaming technique should be used. Currently supports `"dash"` for MPEG-Dash and `"hls"` for HTTP Live Streaming.\n',
      )
      .default('dash'),
    playlist_name: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe filename for the generated manifest/playlist file. The default is `"playlist.mpd"` if your `technique` is `"dash"`, and `"playlist.m3u8"` if your `technique` is `"hls"`.\n',
      )
      .optional(),
    segment_duration: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int(),
      ])
      .describe('\nThe duration for each segment in seconds.\n')
      .default(10),
    closed_captions: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nDetermines whether you want closed caption support when using the `"hls"` technique.\n',
      )
      .default(true),
  })
  .strict()

```

#### `/video/concat`

[/video/concat docs](https://transloadit.com/docs/robots/video-concat/)

Robot Parameter Zod Schema:

```ts
const videoConcatSchema = z
  .object({
    preset: VideoPresetSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    ffmpeg_stack: FfmpegStackSchema,
    use: UseSchema,
    ffmpeg: FfmpegSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    width: z
      .union([
        z.union([
          z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
          z.any(),
          z.number().int().gte(1),
        ]),
        z.null(),
      ])
      .describe(
        "\nWidth of the new video, in pixels.\n\nIf the value is not specified and the `preset` parameter is available, the `preset`'s [supplied width](https://transloadit.com/docs/presets/video/) will be implemented.\n",
      )
      .optional(),
    height: z
      .union([
        z.union([
          z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
          z.any(),
          z.number().int().gte(1),
        ]),
        z.null(),
      ])
      .describe(
        "\nHeight of the new video, in pixels.\n\nIf the value is not specified and the `preset` parameter is available, the `preset`'s [supplied height](https://transloadit.com/docs/presets/video/) will be implemented.\n",
      )
      .optional(),
    robot: z
      .literal('/video/concat')
      .describe(
        '\n> [!Note]\n> Input videos may have differing dimensions and streams - the Robot can handle this fine. It will pre-transcode the input videos if necessary before concatenation at no additional cost.\n\nItʼs possible to concatenate a virtually infinite number of video files using [🤖/video/concat](https://transloadit.com/docs/robots/video-concat/).\n',
      ),
    video_fade_seconds: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number(),
      ])
      .describe(
        '\nWhen used this adds a video fade in and out effect between each section of your concatenated video. The float value is used so if you want a video delay effect of 500 milliseconds between each video section you would select `0.5`, however, integer values can also be represented.\n\nThis parameter does not add a video fade effect at the beginning or end of your video. If you want to do so, create an additional [🤖/video/encode](https://transloadit.com/docs/robots/video-encode/) Step and use our `ffmpeg` parameter as shown in this [demo](https://transloadit.com/demos/video-encoding/concatenate-fade-effect/).\n\nPlease note this parameter is independent of adding audio fades between sections.\n',
      )
      .default(1),
    audio_fade_seconds: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number(),
      ])
      .describe(
        '\nWhen used this adds an audio fade in and out effect between each section of your concatenated video. The float value is used so if you want an audio delay effect of 500 milliseconds between each video section you would select `0.5`, however, integer values can also be represented.\n\nThis parameter does not add an audio fade effect at the beginning or end of your video. If you want to do so, create an additional [🤖/video/encode](https://transloadit.com/docs/robots/video-encode/] Step and use our `ffmpeg` parameter as shown in this [demo](https://transloadit.com/demos/audio-encoding/ffmpeg-fade-in-and-out/).\n\nPlease note this parameter is independent of adding video fades between sections.\n',
      )
      .default(1),
  })
  .strict()

```

#### `/video/encode`

[/video/encode docs](https://transloadit.com/docs/robots/video-encode/)

Robot Parameter Zod Schema:

```ts
const videoEncodeSchema = z
  .object({
    preset: VideoPresetSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    ffmpeg_stack: FfmpegStackSchema,
    use: UseSchema,
    ffmpeg: FfmpegSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    width: z
      .union([
        z.union([
          z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
          z.any(),
          z.number().int().gte(1),
        ]),
        z.null(),
      ])
      .describe(
        "\nWidth of the new video, in pixels.\n\nIf the value is not specified and the `preset` parameter is available, the `preset`'s [supplied width](https://transloadit.com/docs/presets/video/) will be implemented.\n",
      )
      .optional(),
    height: z
      .union([
        z.union([
          z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
          z.any(),
          z.number().int().gte(1),
        ]),
        z.null(),
      ])
      .describe(
        "\nHeight of the new video, in pixels.\n\nIf the value is not specified and the `preset` parameter is available, the `preset`'s [supplied height](https://transloadit.com/docs/presets/video/) will be implemented.\n",
      )
      .optional(),
    resize_strategy: z
      .union([
        z.any(),
        z.enum(['crop', 'fit', 'fillcrop', 'min_fit', 'pad', 'stretch']),
      ])
      .describe(
        '\nSee the [available resize strategies](https://transloadit.com/docs/topics/resize-strategies/).\n',
      )
      .default('pad'),
    zoom: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nIf this is set to `false`, smaller videos will not be stretched to the desired width and height. For details about the impact of zooming for your preferred resize strategy, see the list of available [resize strategies](https://transloadit.com/docs/topics/resize-strategies/).\n',
      )
      .default(true),
    crop: z
      .union([
        z.any(),
        z.union([
          z.any(),
          z
            .object({
              x1: z
                .union([
                  z.union([
                    z.any(),
                    z.union([z.any(), z.string()]),
                    z.union([
                      z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                      z.any(),
                      z.number(),
                    ]),
                  ]),
                  z.null(),
                ])
                .optional(),
              y1: z
                .union([
                  z.union([
                    z.any(),
                    z.union([z.any(), z.string()]),
                    z.union([
                      z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                      z.any(),
                      z.number(),
                    ]),
                  ]),
                  z.null(),
                ])
                .optional(),
              x2: z
                .union([
                  z.union([
                    z.any(),
                    z.union([z.any(), z.string()]),
                    z.union([
                      z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                      z.any(),
                      z.number(),
                    ]),
                  ]),
                  z.null(),
                ])
                .optional(),
              y2: z
                .union([
                  z.union([
                    z.any(),
                    z.union([z.any(), z.string()]),
                    z.union([
                      z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                      z.any(),
                      z.number(),
                    ]),
                  ]),
                  z.null(),
                ])
                .optional(),
            })
            .strict(),
        ]),
        z.union([z.any(), z.string()]),
      ])
      .describe(
        '\nSpecify an object containing coordinates for the top left and bottom right corners of the rectangle to be cropped from the original video(s). Values can be integers for absolute pixel values or strings for percentage based values.\n\nFor example:\n\n```json\n{\n  "x1": 80,\n  "y1": 100,\n  "x2": "60%",\n  "y2": "80%"\n}\n```\n\nThis will crop the area from `(80, 100)` to `(600, 800)` from a 1000×1000 pixels video, which is a square whose width is 520px and height is 700px. If `crop` is set, the width and height parameters are ignored, and the `resize_strategy` is set to `crop` automatically.\n\nYou can also use a JSON string of such an object with coordinates in similar fashion:\n\n```json\n"{\\"x1\\": <Integer>, \\"y1\\": <Integer>, \\"x2\\": <Integer>, \\"y2\\": <Integer>}"\n```\n',
      )
      .optional(),
    background: z
      .union([
        z.any(),
        z.string().regex(new RegExp('^#?[0-9a-fA-F]{6}([0-9a-fA-F]{2})?$')),
      ])
      .describe(
        '\nThe background color of the resulting video the `"rrggbbaa"` format (red, green, blue, alpha) when used with the `"pad"` resize strategy. The default color is black.\n',
      )
      .default('#00000000'),
    rotate: z
      .union([
        z.any(),
        z.union([z.any(), z.literal(0)]),
        z.union([z.any(), z.literal(90)]),
        z.union([z.any(), z.literal(180)]),
        z.union([z.any(), z.literal(270)]),
        z.union([z.any(), z.literal(360)]),
        z.union([z.any(), z.literal(false)]),
      ])
      .describe(
        '\nForces the video to be rotated by the specified degree integer. Currently, only multiples of `90` are supported. We automatically correct the orientation of many videos when the orientation is provided by the camera. This option is only useful for videos requiring rotation because it was not detected by the camera. If you set `rotate` to `false` no rotation is performed, even if the metadata contains such instructions.\n',
      )
      .optional(),
    hint: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe('\nEnables hinting for mp4 files, for RTP/RTSP streaming.\n')
      .default(false),
    turbo: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nSplits the video into multiple chunks so that each chunk can be encoded in parallel before all encoded chunks are stitched back together to form the result video. This comes at the expense of extra <dfn>Priority Job Slots</dfn> and may prove to be counter-productive for very small video files.\n',
      )
      .default(false),
    chunk_duration: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gte(1),
      ])
      .describe(
        '\nAllows you to specify the duration of each chunk when `turbo` is set to `true`. This means you can take advantage of that feature while using fewer <dfn>Priority Job Slots</dfn>. For instance, the longer each chunk is, the fewer <dfn>Encoding Jobs</dfn> will need to be used.\n',
      )
      .optional(),
    watermark_url: z
      .union([z.any(), z.string()])
      .describe(
        '\nA URL indicating a PNG image to be overlaid above this image. You can also [supply the watermark via another Assembly Step](https://transloadit.com/docs/topics/use-parameter/#supplying-the-watermark-via-an-assembly-step).\n',
      )
      .default(''),
    watermark_position: z
      .union([
        z.any(),
        z.union([
          z.any(),
          z.enum([
            'bottom',
            'bottom-left',
            'bottom-right',
            'center',
            'left',
            'right',
            'top',
            'top-left',
            'top-right',
          ]),
        ]),
        z.union([z.any(), z.array(z.union([z.any(), z.any()]))]),
      ])
      .describe(
        '\nThe position at which the watermark is placed.\n\nAn array of possible values can also be specified, in which case one value will be selected at random, such as `[ "center", "left", "bottom-left", "bottom-right" ]`.\n\nThis setting puts the watermark in the specified corner. To use a specific pixel offset for the watermark, you will need to add the padding to the image itself.\n',
      )
      .default('center'),
    watermark_x_offset: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int(),
      ])
      .describe(
        "\nThe x-offset in number of pixels at which the watermark will be placed in relation to the position it has due to `watermark_position`.\n\nValues can be both positive and negative and yield different results depending on the `watermark_position` parameter. Positive values move the watermark closer to the image's center point, whereas negative values move the watermark further away from the image's center point.\n",
      )
      .default(0),
    watermark_y_offset: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int(),
      ])
      .describe(
        "\nThe y-offset in number of pixels at which the watermark will be placed in relation to the position it has due to `watermark_position`.\n\nValues can be both positive and negative and yield different results depending on the `watermark_position` parameter. Positive values move the watermark closer to the image's center point, whereas negative values move the watermark further away from the image's center point.\n",
      )
      .default(0),
    watermark_size: z
      .union([z.any(), z.string().regex(new RegExp('^\\d+%$'))])
      .describe(
        '\nThe size of the watermark, as a percentage, such as `"50%"`. How the watermark is resized greatly depends on the `watermark_resize_strategy`.\n',
      )
      .optional(),
    watermark_resize_strategy: z
      .union([z.any(), z.enum(['area', 'fit', 'stretch'])])
      .describe(
        '\nTo explain how the resize strategies work, let\'s assume our target video size is 800×800 pixels and our watermark image is 400×300 pixels. Let\'s also assume, the `watermark_size` parameter is set to `"25%"`.\n\nFor the `"fit"` resize strategy, the watermark is scaled so that the longer side of the watermark takes up 25% of the corresponding video side. And the other side is scaled according to the aspect ratio of the watermark image. So with our watermark, the width is the longer side, and 25% of the video size would be 200px. Hence, the watermark would be resized to 200×150 pixels. If the `watermark_size` was set to `"50%"`", it would be resized to 400×300 pixels (so just left at its original size).\n\nFor the `"stretch"` resize strategy, the watermark image is stretched (meaning, it is resized without keeping its aspect ratio in mind) so that both sides take up 25% of the corresponding video side. Since our video is 800×800 pixels, for a watermark size of 25% the watermark would be resized to 200×200 pixels. Its height would appear stretched, because keeping the aspect ratio in mind it would be resized to 200×150 pixels instead.\n\nFor the `"area"` resize strategy, the watermark is resized (keeping its aspect ratio in check) so that it covers `"xx%"` of the video\'s surface area. The value from `watermark_size` is used for the percentage area size.\n',
      )
      .default('fit'),
    watermark_start_time: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number(),
      ])
      .describe(
        '\nThe delay in seconds from the start of the video for the watermark to appear. By default the watermark is immediately shown.\n',
      )
      .default(0),
    watermark_duration: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number(),
      ])
      .describe(
        '\nThe duration in seconds for the watermark to be shown. Can be used together with `watermark_start_time` to create nice effects. The default value is `-1.0`, which means that the watermark is shown for the entire duration of the video.\n',
      )
      .default(-1),
    watermark_opacity: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().gte(0).lte(1),
      ])
      .describe(
        '\nThe opacity of the watermark. Valid values are between `0` (invisible) and `1.0` (full visibility).\n',
      )
      .default(1),
    segment: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        "\nSplits the file into multiple parts, to be used for Apple's [HTTP Live Streaming](https://developer.apple.com/resources/http-streaming/).\n",
      )
      .default(false),
    segment_duration: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gte(1),
      ])
      .describe(
        '\nSpecifies the length of each HTTP segment. This is optional, and the default value as recommended by Apple is `10`. Do not change this value unless you have a good reason.\n',
      )
      .default(10),
    segment_prefix: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe prefix used for the naming. For example, a prefix of `"segment_"` would produce files named `"segment_0.ts"`, `"segment_1.ts"` and so on. This is optional, and defaults to the base name of the input file. Also see the related `segment_name` parameter.\n',
      )
      .default(''),
    segment_name: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe name used for the final segment. Available variables are `${segment_prefix}`, `${segment_number}` and `${segment_id}` (which is a UUIDv4 without dashes).\n',
      )
      .default(''),
    segment_time_delta: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number(),
      ])
      .describe(
        '\nDelta to apply to segment duration. This is optional and allows fine-tuning of segment boundaries.\n',
      )
      .optional(),
    robot: z
      .literal('/video/encode')
      .describe(
        '\nThe /video/encode Robot is a versatile tool for video processing that handles transcoding, resizing, and watermarking. It supports various formats including modern standards like HEVC (H.265), and provides features such as presets for common devices, custom FFmpeg parameters for powerusers, watermark positioning, and more.\n\n## Adding text overlays with FFmpeg\n\nYou can add text overlays to videos using FFmpeg\'s `drawtext` filter through this <Definition term="Robot">Robot</Definition>\'s `ffmpeg` parameter. Here are two examples — one with the default font and one with a custom font family name:\n\n```json\n{\n  "steps": {\n    ":original": {\n      "robot": "/upload/handle"\n    },\n    "text_overlay_default": {\n      "use": ":original",\n      "robot": "/video/encode",\n      "preset": "empty",\n      "ffmpeg_stack": "{{stacks.ffmpeg.recommended_version}}",\n      "ffmpeg": {\n        "codec:a": "copy",\n        "vf": "drawtext=text=\'My text overlay\':fontcolor=white:fontsize=24:box=1:boxcolor=black@0.5:boxborderw=5:x=(w-text_w)/2:y=(h-text_h)/2"\n      },\n      "result": true\n    },\n    "text_overlay_custom": {\n      "use": ":original",\n      "robot": "/video/encode",\n      "preset": "empty",\n      "ffmpeg_stack": "{{stacks.ffmpeg.recommended_version}}",\n      "ffmpeg": {\n        "codec:a": "copy",\n        "vf": "drawtext=font=\'Times New Roman\':text=\'My text overlay\':fontcolor=white:fontsize=24:box=1:boxcolor=black@0.5:boxborderw=5:x=(w-text_w)/2:y=(h-text_h)/2"\n      },\n      "result": true\n    }\n  }\n}\n```\n\n**Notes:**\n\n- Use the `font` attribute to reference a font by family name with FFmpeg\'s `drawtext`\n- FFmpeg font family names typically do not contain dashes (e.g. `Times New Roman`), while\n  ImageMagick uses dashed names (e.g. `Times-New-Roman`).\n- Preserve the source audio by setting `"codec:a": "copy"`.\n- Position text with the `x` and `y` expressions. The example above centers the text.\n\nSee the live demo [here](https://transloadit.com/demos/video-encoding/add-text-overlay/).\n',
      ),
    font_size: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number(),
      ])
      .optional(),
    font_color: z.union([z.any(), z.string()]).optional(),
    text_background_color: z.union([z.any(), z.string()]).optional(),
  })
  .strict()

```

#### `/video/merge`

[/video/merge docs](https://transloadit.com/docs/robots/video-merge/)

Robot Parameter Zod Schema:

```ts
const videoMergeSchema = z
  .object({
    preset: VideoPresetSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    ffmpeg_stack: FfmpegStackSchema,
    use: UseSchema,
    ffmpeg: FfmpegSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    width: z
      .union([
        z.union([
          z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
          z.any(),
          z.number().int().gte(1),
        ]),
        z.null(),
      ])
      .describe(
        "\nWidth of the new video, in pixels.\n\nIf the value is not specified and the `preset` parameter is available, the `preset`'s [supplied width](https://transloadit.com/docs/presets/video/) will be implemented.\n",
      )
      .optional(),
    height: z
      .union([
        z.union([
          z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
          z.any(),
          z.number().int().gte(1),
        ]),
        z.null(),
      ])
      .describe(
        "\nHeight of the new video, in pixels.\n\nIf the value is not specified and the `preset` parameter is available, the `preset`'s [supplied height](https://transloadit.com/docs/presets/video/) will be implemented.\n",
      )
      .optional(),
    robot: z.literal('/video/merge'),
    resize_strategy: z
      .union([
        z.any(),
        z.enum(['crop', 'fit', 'fillcrop', 'min_fit', 'pad', 'stretch']),
      ])
      .describe(
        "\nIf the given width/height parameters are bigger than the input image's dimensions, then the `resize_strategy` determines how the image will be resized to match the provided width/height. See the [available resize strategies](https://transloadit.com/docs/topics/resize-strategies/).\n",
      )
      .default('pad'),
    background: z
      .union([
        z.any(),
        z.string().regex(new RegExp('^#?[0-9a-fA-F]{6}([0-9a-fA-F]{2})?$')),
      ])
      .describe(
        '\nThe background color of the resulting video the `"rrggbbaa"` format (red, green, blue, alpha) when used with the `"pad"` resize strategy. The default color is black.\n',
      )
      .default('#00000000'),
    framerate: z
      .union([
        z.any(),
        z.union([
          z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
          z.any(),
          z.number().int().gte(1),
        ]),
        z.union([z.any(), z.string().regex(new RegExp('^\\d+(?:\\/\\d+)?$'))]),
      ])
      .describe(
        '\nWhen merging images to generate a video this is the input framerate. A value of "1/5" means each image is given 5 seconds before the next frame appears (the inverse of a framerate of "5"). Likewise for "1/10", "1/20", etc. A value of "5" means there are 5 frames per second.\n',
      )
      .default('1/5'),
    image_durations: z
      .union([
        z.any(),
        z.array(
          z.union([
            z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
            z.any(),
            z.number(),
          ]),
        ),
      ])
      .describe(
        '\nWhen merging images to generate a video this allows you to define how long (in seconds) each image will be shown inside of the video. So if you pass 3 images and define `[2.4, 5.6, 9]` the first image will be shown for 2.4s, the second image for 5.6s and the last one for 9s. The `duration` parameter will automatically be set to the sum of the image_durations, so `17` in our example. It can still be overwritten, though, in which case the last image will be shown until the defined duration is reached.\n',
      )
      .default([]),
    duration: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number(),
      ])
      .describe(
        '\nWhen merging images to generate a video or when merging audio and video this is the desired target duration in seconds. The float value can take one decimal digit. If you want all images to be displayed exactly once, then you can set the duration according to this formula: `duration = numberOfImages / framerate`. This also works for the inverse framerate values like `1/5`.\n\nIf you set this value to `null` (default), then the duration of the input audio file will be used when merging images with an audio file.\n\nWhen merging audio files and video files, the duration of the longest video or audio file is used by default.\n',
      )
      .default(5),
    audio_delay: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number(),
      ])
      .describe(
        '\nWhen merging a video and an audio file, and when merging images and an audio file to generate a video, this is the desired delay in seconds for the audio file to start playing. Imagine you merge a video file without sound and an audio file, but you wish the audio to start playing after 5 seconds and not immediately, then this is the parameter to use.\n',
      )
      .default(0),
    loop: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\n  Determines whether the shorter media file should be looped to match the duration of the longer one. For example, if you merge a 1-minute video with a 3-minute audio file and enable this option, the video will play three times in a row to match the audio length.',
      )
      .default(false),
    replace_audio: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nDetermines whether the audio of the video should be replaced with a provided audio file.\n',
      )
      .default(false),
    vstack: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nStacks the input media vertically. All streams need to have the same pixel format and width - so consider using a [/video/encode](https://transloadit.com/docs/robots/video-encode/) <dfn>Step</dfn> before using this parameter to enforce this.\n',
      )
      .default(false),
    image_url: z
      .union([z.any(), z.string().url()])
      .describe(
        '\nThe URL of an image to be merged with the audio or video. When this parameter is provided, the robot will download the image from the URL and merge it with the other media.\n',
      )
      .optional(),
  })
  .strict()

```

#### `/video/ondemand`

[/video/ondemand docs](https://transloadit.com/docs/robots/video-ondemand/)

Robot Parameter Zod Schema:

```ts
const videoOndemandSchema = z
  .object({
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    robot: z.literal('/video/ondemand'),
    variants: z
      .record(
        z.union([
          z.any(),
          z
            .object({
              ffmpeg: z
                .union([
                  z.any(),
                  z
                    .object({
                      af: z.union([z.any(), z.string()]).optional(),
                      'b:a': z
                        .union([
                          z.any(),
                          z.union([z.any(), z.string()]),
                          z.union([
                            z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                            z.any(),
                            z.number(),
                          ]),
                        ])
                        .optional(),
                      'b:v': z
                        .union([
                          z.any(),
                          z.union([z.any(), z.string()]),
                          z.union([
                            z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                            z.any(),
                            z.number(),
                          ]),
                        ])
                        .optional(),
                      'c:a': z.union([z.any(), z.string()]).optional(),
                      'c:v': z.union([z.any(), z.string()]).optional(),
                      'codec:a': z.union([z.any(), z.string()]).optional(),
                      'codec:v': z.union([z.any(), z.string()]).optional(),
                      'filter:v': z.union([z.any(), z.string()]).optional(),
                      'filter:a': z.union([z.any(), z.string()]).optional(),
                      bits_per_mb: z
                        .union([
                          z.any(),
                          z.union([z.any(), z.string()]),
                          z.union([
                            z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                            z.any(),
                            z.number(),
                          ]),
                        ])
                        .optional(),
                      ss: z
                        .union([
                          z.any(),
                          z.union([z.any(), z.string()]),
                          z.union([
                            z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                            z.any(),
                            z.number(),
                          ]),
                        ])
                        .optional(),
                      t: z
                        .union([
                          z.any(),
                          z.union([z.any(), z.string()]),
                          z.union([
                            z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                            z.any(),
                            z.number(),
                          ]),
                        ])
                        .optional(),
                      to: z
                        .union([
                          z.any(),
                          z.union([z.any(), z.string()]),
                          z.union([
                            z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                            z.any(),
                            z.number(),
                          ]),
                        ])
                        .optional(),
                      vendor: z.union([z.any(), z.string()]).optional(),
                      shortest: z
                        .union([
                          z.union([z.any(), z.union([z.boolean(), z.any()])]),
                          z.null(),
                        ])
                        .optional(),
                      filter_complex: z
                        .union([
                          z.any(),
                          z.union([z.any(), z.string()]),
                          z.record(z.union([z.any(), z.string()])),
                        ])
                        .optional(),
                      'level:v': z
                        .union([
                          z.any(),
                          z.union([z.any(), z.string()]),
                          z.union([
                            z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                            z.any(),
                            z.number(),
                          ]),
                        ])
                        .optional(),
                      'profile:v': z
                        .union([
                          z.any(),
                          z.union([
                            z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                            z.any(),
                            z.number(),
                          ]),
                          z.union([
                            z.any(),
                            z.enum(['baseline', 'main', 'high', 'main10']),
                          ]),
                        ])
                        .optional(),
                      'qscale:a': z
                        .union([
                          z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                          z.any(),
                          z.number(),
                        ])
                        .optional(),
                      'qscale:v': z
                        .union([
                          z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                          z.any(),
                          z.number(),
                        ])
                        .optional(),
                      'x264-params': z.union([z.any(), z.string()]).optional(),
                      'overshoot-pct': z
                        .union([
                          z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                          z.any(),
                          z.number(),
                        ])
                        .optional(),
                      deadline: z.union([z.any(), z.string()]).optional(),
                      'cpu-used': z.union([z.any(), z.string()]).optional(),
                      'undershoot-pct': z
                        .union([
                          z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                          z.any(),
                          z.number(),
                        ])
                        .optional(),
                      'row-mt': z
                        .union([
                          z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                          z.any(),
                          z.number(),
                        ])
                        .optional(),
                      'x265-params': z
                        .union([
                          z.any(),
                          z
                            .object({
                              'vbv-maxrate': z
                                .union([
                                  z
                                    .string()
                                    .regex(new RegExp('^\\d+(\\.\\d+)?$')),
                                  z.any(),
                                  z.number(),
                                ])
                                .optional(),
                              'vbv-bufsize': z
                                .union([
                                  z
                                    .string()
                                    .regex(new RegExp('^\\d+(\\.\\d+)?$')),
                                  z.any(),
                                  z.number(),
                                ])
                                .optional(),
                              'rc-lookahead': z
                                .union([
                                  z
                                    .string()
                                    .regex(new RegExp('^\\d+(\\.\\d+)?$')),
                                  z.any(),
                                  z.number(),
                                ])
                                .optional(),
                              'b-adapt': z
                                .union([
                                  z
                                    .string()
                                    .regex(new RegExp('^\\d+(\\.\\d+)?$')),
                                  z.any(),
                                  z.number(),
                                ])
                                .optional(),
                            })
                            .strict(),
                        ])
                        .optional(),
                      'svtav1-params': z
                        .union([
                          z.any(),
                          z
                            .object({
                              tune: z
                                .union([
                                  z
                                    .string()
                                    .regex(new RegExp('^\\d+(\\.\\d+)?$')),
                                  z.any(),
                                  z.number(),
                                ])
                                .optional(),
                              'enable-qm': z
                                .union([
                                  z
                                    .string()
                                    .regex(new RegExp('^\\d+(\\.\\d+)?$')),
                                  z.any(),
                                  z.number(),
                                ])
                                .optional(),
                              'fast-decode': z
                                .union([
                                  z
                                    .string()
                                    .regex(new RegExp('^\\d+(\\.\\d+)?$')),
                                  z.any(),
                                  z.number(),
                                ])
                                .optional(),
                              'film-grain-denoise': z
                                .union([
                                  z
                                    .string()
                                    .regex(new RegExp('^\\d+(\\.\\d+)?$')),
                                  z.any(),
                                  z.number(),
                                ])
                                .optional(),
                            })
                            .strict(),
                        ])
                        .optional(),
                      ac: z
                        .union([
                          z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                          z.any(),
                          z.number(),
                        ])
                        .optional(),
                      an: z
                        .union([z.any(), z.union([z.boolean(), z.any()])])
                        .optional(),
                      ar: z
                        .union([
                          z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                          z.any(),
                          z.number(),
                        ])
                        .optional(),
                      async: z
                        .union([
                          z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                          z.any(),
                          z.number(),
                        ])
                        .optional(),
                      b: z
                        .union([
                          z.any(),
                          z.union([
                            z.any(),
                            z
                              .object({
                                v: z
                                  .union([
                                    z
                                      .string()
                                      .regex(new RegExp('^\\d+(\\.\\d+)?$')),
                                    z.any(),
                                    z.number(),
                                  ])
                                  .optional(),
                                a: z
                                  .union([
                                    z
                                      .string()
                                      .regex(new RegExp('^\\d+(\\.\\d+)?$')),
                                    z.any(),
                                    z.number(),
                                  ])
                                  .optional(),
                              })
                              .strict(),
                          ]),
                          z.union([z.any(), z.string()]),
                        ])
                        .optional(),
                      bt: z
                        .union([
                          z.any(),
                          z.union([
                            z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                            z.any(),
                            z.number(),
                          ]),
                          z.union([z.any(), z.string()]),
                        ])
                        .optional(),
                      bufsize: z
                        .union([
                          z.any(),
                          z.union([z.any(), z.string()]),
                          z.union([
                            z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                            z.any(),
                            z.number(),
                          ]),
                        ])
                        .optional(),
                      c: z.union([z.any(), z.string()]).optional(),
                      codec: z
                        .union([
                          z.any(),
                          z
                            .object({
                              v: z.union([z.any(), z.string()]).optional(),
                              a: z.union([z.any(), z.string()]).optional(),
                            })
                            .strict(),
                        ])
                        .optional(),
                      coder: z
                        .union([
                          z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                          z.any(),
                          z.number(),
                        ])
                        .optional(),
                      crf: z
                        .union([
                          z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                          z.any(),
                          z.number(),
                        ])
                        .optional(),
                      f: z.union([z.any(), z.string()]).optional(),
                      flags: z.union([z.any(), z.string()]).optional(),
                      g: z
                        .union([
                          z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                          z.any(),
                          z.number(),
                        ])
                        .optional(),
                      i_qfactor: z
                        .union([
                          z.any(),
                          z.union([z.any(), z.string()]),
                          z.union([
                            z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                            z.any(),
                            z.number(),
                          ]),
                        ])
                        .optional(),
                      keyint_min: z
                        .union([
                          z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                          z.any(),
                          z.number(),
                        ])
                        .optional(),
                      level: z
                        .union([
                          z.any(),
                          z.union([z.any(), z.string()]),
                          z.union([
                            z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                            z.any(),
                            z.number(),
                          ]),
                        ])
                        .optional(),
                      map: z
                        .union([
                          z.any(),
                          z.union([z.any(), z.string()]),
                          z.union([
                            z.any(),
                            z.array(z.union([z.any(), z.string()])),
                          ]),
                        ])
                        .optional(),
                      maxrate: z
                        .union([
                          z.any(),
                          z.union([z.any(), z.string()]),
                          z.union([
                            z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                            z.any(),
                            z.number(),
                          ]),
                        ])
                        .optional(),
                      me_range: z
                        .union([
                          z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                          z.any(),
                          z.number(),
                        ])
                        .optional(),
                      movflags: z.union([z.any(), z.string()]).optional(),
                      partitions: z.union([z.any(), z.string()]).optional(),
                      pix_fmt: z.union([z.any(), z.string()]).optional(),
                      preset: z
                        .union([
                          z.any(),
                          z.union([z.any(), z.string()]),
                          z.union([
                            z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                            z.any(),
                            z.number(),
                          ]),
                        ])
                        .optional(),
                      profile: z.union([z.any(), z.string()]).optional(),
                      'q:a': z
                        .union([
                          z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                          z.any(),
                          z.number(),
                        ])
                        .optional(),
                      qcomp: z
                        .union([
                          z.any(),
                          z.union([z.any(), z.string()]),
                          z.union([
                            z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                            z.any(),
                            z.number(),
                          ]),
                        ])
                        .optional(),
                      qdiff: z
                        .union([
                          z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                          z.any(),
                          z.number(),
                        ])
                        .optional(),
                      qmax: z
                        .union([
                          z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                          z.any(),
                          z.number(),
                        ])
                        .optional(),
                      qmin: z
                        .union([
                          z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                          z.any(),
                          z.number(),
                        ])
                        .optional(),
                      r: z
                        .union([
                          z.union([
                            z.any(),
                            z.union([
                              z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                              z.any(),
                              z.number(),
                            ]),
                            z.union([z.any(), z.string()]),
                          ]),
                          z.null(),
                        ])
                        .optional(),
                      rc_eq: z.union([z.any(), z.string()]).optional(),
                      refs: z
                        .union([
                          z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                          z.any(),
                          z.number(),
                        ])
                        .optional(),
                      s: z.union([z.any(), z.string()]).optional(),
                      sc_threshold: z
                        .union([
                          z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                          z.any(),
                          z.number(),
                        ])
                        .optional(),
                      sws_flags: z.union([z.any(), z.string()]).optional(),
                      threads: z
                        .union([
                          z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                          z.any(),
                          z.number(),
                        ])
                        .optional(),
                      trellis: z
                        .union([
                          z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                          z.any(),
                          z.number(),
                        ])
                        .optional(),
                      transloaditffpreset: z
                        .union([z.any(), z.literal('empty')])
                        .optional(),
                      vn: z
                        .union([z.any(), z.union([z.boolean(), z.any()])])
                        .optional(),
                      vf: z.union([z.any(), z.string()]).optional(),
                      x264opts: z.union([z.any(), z.string()]).optional(),
                      vbr: z
                        .union([
                          z.any(),
                          z.union([z.any(), z.string()]),
                          z.union([
                            z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                            z.any(),
                            z.number(),
                          ]),
                        ])
                        .optional(),
                    })
                    .catchall(z.any()),
                ])
                .describe(
                  '\nA parameter object to be passed to FFmpeg. If a preset is used, the options specified are merged on top of the ones from the preset. For available options, see the [FFmpeg documentation](https://ffmpeg.org/ffmpeg-doc.html). Options specified here take precedence over the preset options.\n',
                )
                .optional(),
              ffmpeg_stack: z
                .union([
                  z.any(),
                  z.union([z.any(), z.enum(['v5', 'v6', 'v7'])]),
                  z.union([
                    z.any(),
                    z
                      .string()
                      .regex(new RegExp('^v?[567](\\.\\d+)?(\\.\\d+)?$')),
                  ]),
                ])
                .describe(
                  '\nSelects the FFmpeg stack version to use for encoding. These versions reflect real FFmpeg versions. We currently recommend to use "v6.0.0".\n',
                )
                .default('v5.0.0'),
              width: z
                .union([
                  z.union([
                    z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                    z.any(),
                    z.number().int().gte(1),
                  ]),
                  z.null(),
                ])
                .describe(
                  "\nWidth of the new video, in pixels.\n\nIf the value is not specified and the `preset` parameter is available, the `preset`'s [supplied width](https://transloadit.com/docs/presets/video/) will be implemented.\n",
                )
                .optional(),
              height: z
                .union([
                  z.union([
                    z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                    z.any(),
                    z.number().int().gte(1),
                  ]),
                  z.null(),
                ])
                .describe(
                  "\nHeight of the new video, in pixels.\n\nIf the value is not specified and the `preset` parameter is available, the `preset`'s [supplied height](https://transloadit.com/docs/presets/video/) will be implemented.\n",
                )
                .optional(),
              preset: z
                .union([
                  z.any(),
                  z.enum([
                    'android',
                    'android-high',
                    'android-low',
                    'android_high',
                    'android_low',
                    'dash-1080p-video',
                    'dash-1080p_video',
                    'dash-270p-video',
                    'dash-270p_video',
                    'dash-360p-video',
                    'dash-360p_video',
                    'dash-480p-video',
                    'dash-480p_video',
                    'dash-540p-video',
                    'dash-540p_video',
                    'dash-576p-video',
                    'dash-576p_video',
                    'dash-720p-video',
                    'dash-720p_video',
                    'dash/1080p-video',
                    'dash/1080p_video',
                    'dash/270p-video',
                    'dash/270p_video',
                    'dash/360p-video',
                    'dash/360p_video',
                    'dash/480p-video',
                    'dash/480p_video',
                    'dash/540p-video',
                    'dash/540p_video',
                    'dash/576p-video',
                    'dash/576p_video',
                    'dash/720p-video',
                    'dash/720p_video',
                    'dash_1080p-video',
                    'dash_1080p_video',
                    'dash_270p-video',
                    'dash_270p_video',
                    'dash_360p-video',
                    'dash_360p_video',
                    'dash_480p-video',
                    'dash_480p_video',
                    'dash_540p-video',
                    'dash_540p_video',
                    'dash_576p-video',
                    'dash_576p_video',
                    'dash_720p-video',
                    'dash_720p_video',
                    'flash',
                    'gif',
                    'hevc',
                    'hls-1080p',
                    'hls-270p',
                    'hls-360p',
                    'hls-480p',
                    'hls-540p',
                    'hls-576p',
                    'hls-720p',
                    'hls/1080p',
                    'hls/270p',
                    'hls/360p',
                    'hls/480p',
                    'hls/4k',
                    'hls/540p',
                    'hls/720p',
                    'hls_1080p',
                    'hls_270p',
                    'hls_360p',
                    'hls_480p',
                    'hls_540p',
                    'hls_576p',
                    'hls_720p',
                    'ipad',
                    'ipad-high',
                    'ipad-low',
                    'ipad_high',
                    'ipad_low',
                    'iphone',
                    'iphone-high',
                    'iphone-low',
                    'iphone_high',
                    'iphone_low',
                    'ogv',
                    'vod/1080p',
                    'vod/270p',
                    'vod/480p',
                    'vod/720p',
                    'vp9',
                    'vp9-1080p',
                    'vp9-270p',
                    'vp9-360p',
                    'vp9-480p',
                    'vp9-540p',
                    'vp9-576p',
                    'vp9-720p',
                    'vp9_1080p',
                    'vp9_270p',
                    'vp9_360p',
                    'vp9_480p',
                    'vp9_540p',
                    'vp9_576p',
                    'vp9_720p',
                    'web/mp4-x265/1080p',
                    'web/mp4-x265/240p',
                    'web/mp4-x265/360p',
                    'web/mp4-x265/480p',
                    'web/mp4-x265/4k',
                    'web/mp4-x265/720p',
                    'web/mp4-x265/8k',
                    'web/mp4/1080p',
                    'web/mp4/240p',
                    'web/mp4/360p',
                    'web/mp4/480p',
                    'web/mp4/4k',
                    'web/mp4/540p',
                    'web/mp4/720p',
                    'web/mp4/8k',
                    'web/mp4_x265/1080p',
                    'web/mp4_x265/240p',
                    'web/mp4_x265/360p',
                    'web/mp4_x265/480p',
                    'web/mp4_x265/4k',
                    'web/mp4_x265/720p',
                    'web/mp4_x265/8k',
                    'web/webm-av1/1080p',
                    'web/webm-av1/240p',
                    'web/webm-av1/360p',
                    'web/webm-av1/480p',
                    'web/webm-av1/4k',
                    'web/webm-av1/720p',
                    'web/webm-av1/8k',
                    'web/webm/1080p',
                    'web/webm/240p',
                    'web/webm/360p',
                    'web/webm/480p',
                    'web/webm/4k',
                    'web/webm/720p',
                    'web/webm/8k',
                    'web/webm_av1/1080p',
                    'web/webm_av1/240p',
                    'web/webm_av1/360p',
                    'web/webm_av1/480p',
                    'web/webm_av1/4k',
                    'web/webm_av1/720p',
                    'web/webm_av1/8k',
                    'webm',
                    'webm-1080p',
                    'webm-270p',
                    'webm-360p',
                    'webm-480p',
                    'webm-540p',
                    'webm-576p',
                    'webm-720p',
                    'webm_1080p',
                    'webm_270p',
                    'webm_360p',
                    'webm_480p',
                    'webm_540p',
                    'webm_576p',
                    'webm_720p',
                    'wmv',
                    'aac',
                    'alac',
                    'audio/aac',
                    'audio/alac',
                    'audio/flac',
                    'audio/mp3',
                    'audio/ogg',
                    'dash-128k-audio',
                    'dash-128k_audio',
                    'dash-256k-audio',
                    'dash-256k_audio',
                    'dash-32k-audio',
                    'dash-32k_audio',
                    'dash-64k-audio',
                    'dash-64k_audio',
                    'dash/128k-audio',
                    'dash/128k_audio',
                    'dash/256k-audio',
                    'dash/256k_audio',
                    'dash/32k-audio',
                    'dash/32k_audio',
                    'dash/64k-audio',
                    'dash/64k_audio',
                    'dash_128k-audio',
                    'dash_128k_audio',
                    'dash_256k-audio',
                    'dash_256k_audio',
                    'dash_32k-audio',
                    'dash_32k_audio',
                    'dash_64k-audio',
                    'dash_64k_audio',
                    'empty',
                    'flac',
                    'hg-transformers-audio',
                    'hg-transformers_audio',
                    'hg_transformers-audio',
                    'hg_transformers_audio',
                    'mp3',
                    'ogg',
                    'opus',
                    'speech',
                    'wav',
                  ]),
                ])
                .describe(
                  "\nConverts a video according to [pre-configured settings](https://transloadit.com/docs/presets/video/).\n\nIf you specify your own FFmpeg parameters using the <dfn>Robot</dfn>'s and/or do not not want Transloadit to set any encoding setting, starting `ffmpeg_stack: \"v6\"`,  you can use the value `'empty'` here.\n",
                )
                .optional(),
              resize_strategy: z
                .union([
                  z.any(),
                  z.enum([
                    'crop',
                    'fit',
                    'fillcrop',
                    'min_fit',
                    'pad',
                    'stretch',
                  ]),
                ])
                .describe(
                  '\nSee the [available resize strategies](https://transloadit.com/docs/topics/resize-strategies/).\n',
                )
                .default('pad'),
              zoom: z
                .union([z.any(), z.union([z.boolean(), z.any()])])
                .describe(
                  '\nIf this is set to `false`, smaller videos will not be stretched to the desired width and height. For details about the impact of zooming for your preferred resize strategy, see the list of available [resize strategies](https://transloadit.com/docs/topics/resize-strategies/).\n',
                )
                .default(true),
              crop: z
                .union([
                  z.any(),
                  z.union([
                    z.any(),
                    z
                      .object({
                        x1: z
                          .union([
                            z.union([
                              z.any(),
                              z.union([z.any(), z.string()]),
                              z.union([
                                z
                                  .string()
                                  .regex(new RegExp('^\\d+(\\.\\d+)?$')),
                                z.any(),
                                z.number(),
                              ]),
                            ]),
                            z.null(),
                          ])
                          .optional(),
                        y1: z
                          .union([
                            z.union([
                              z.any(),
                              z.union([z.any(), z.string()]),
                              z.union([
                                z
                                  .string()
                                  .regex(new RegExp('^\\d+(\\.\\d+)?$')),
                                z.any(),
                                z.number(),
                              ]),
                            ]),
                            z.null(),
                          ])
                          .optional(),
                        x2: z
                          .union([
                            z.union([
                              z.any(),
                              z.union([z.any(), z.string()]),
                              z.union([
                                z
                                  .string()
                                  .regex(new RegExp('^\\d+(\\.\\d+)?$')),
                                z.any(),
                                z.number(),
                              ]),
                            ]),
                            z.null(),
                          ])
                          .optional(),
                        y2: z
                          .union([
                            z.union([
                              z.any(),
                              z.union([z.any(), z.string()]),
                              z.union([
                                z
                                  .string()
                                  .regex(new RegExp('^\\d+(\\.\\d+)?$')),
                                z.any(),
                                z.number(),
                              ]),
                            ]),
                            z.null(),
                          ])
                          .optional(),
                      })
                      .strict(),
                  ]),
                  z.union([z.any(), z.string()]),
                ])
                .describe(
                  '\nSpecify an object containing coordinates for the top left and bottom right corners of the rectangle to be cropped from the original video(s). Values can be integers for absolute pixel values or strings for percentage based values.\n\nFor example:\n\n```json\n{\n  "x1": 80,\n  "y1": 100,\n  "x2": "60%",\n  "y2": "80%"\n}\n```\n\nThis will crop the area from `(80, 100)` to `(600, 800)` from a 1000×1000 pixels video, which is a square whose width is 520px and height is 700px. If `crop` is set, the width and height parameters are ignored, and the `resize_strategy` is set to `crop` automatically.\n\nYou can also use a JSON string of such an object with coordinates in similar fashion:\n\n```json\n"{\\"x1\\": <Integer>, \\"y1\\": <Integer>, \\"x2\\": <Integer>, \\"y2\\": <Integer>}"\n```\n',
                )
                .optional(),
              background: z
                .union([
                  z.any(),
                  z
                    .string()
                    .regex(new RegExp('^#?[0-9a-fA-F]{6}([0-9a-fA-F]{2})?$')),
                ])
                .describe(
                  '\nThe background color of the resulting video the `"rrggbbaa"` format (red, green, blue, alpha) when used with the `"pad"` resize strategy. The default color is black.\n',
                )
                .default('#00000000'),
              rotate: z
                .union([
                  z.any(),
                  z.union([z.any(), z.literal(0)]),
                  z.union([z.any(), z.literal(90)]),
                  z.union([z.any(), z.literal(180)]),
                  z.union([z.any(), z.literal(270)]),
                  z.union([z.any(), z.literal(360)]),
                  z.union([z.any(), z.literal(false)]),
                ])
                .describe(
                  '\nForces the video to be rotated by the specified degree integer. Currently, only multiples of `90` are supported. We automatically correct the orientation of many videos when the orientation is provided by the camera. This option is only useful for videos requiring rotation because it was not detected by the camera. If you set `rotate` to `false` no rotation is performed, even if the metadata contains such instructions.\n',
                )
                .optional(),
              hint: z
                .union([z.any(), z.union([z.boolean(), z.any()])])
                .describe(
                  '\nEnables hinting for mp4 files, for RTP/RTSP streaming.\n',
                )
                .default(false),
              turbo: z
                .union([z.any(), z.union([z.boolean(), z.any()])])
                .describe(
                  '\nSplits the video into multiple chunks so that each chunk can be encoded in parallel before all encoded chunks are stitched back together to form the result video. This comes at the expense of extra <dfn>Priority Job Slots</dfn> and may prove to be counter-productive for very small video files.\n',
                )
                .default(false),
              chunk_duration: z
                .union([
                  z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                  z.any(),
                  z.number().int().gte(1),
                ])
                .describe(
                  '\nAllows you to specify the duration of each chunk when `turbo` is set to `true`. This means you can take advantage of that feature while using fewer <dfn>Priority Job Slots</dfn>. For instance, the longer each chunk is, the fewer <dfn>Encoding Jobs</dfn> will need to be used.\n',
                )
                .optional(),
              watermark_url: z
                .union([z.any(), z.string()])
                .describe(
                  '\nA URL indicating a PNG image to be overlaid above this image. You can also [supply the watermark via another Assembly Step](https://transloadit.com/docs/topics/use-parameter/#supplying-the-watermark-via-an-assembly-step).\n',
                )
                .default(''),
              watermark_position: z
                .union([
                  z.any(),
                  z.union([
                    z.any(),
                    z.enum([
                      'bottom',
                      'bottom-left',
                      'bottom-right',
                      'center',
                      'left',
                      'right',
                      'top',
                      'top-left',
                      'top-right',
                    ]),
                  ]),
                  z.union([z.any(), z.array(z.union([z.any(), z.any()]))]),
                ])
                .describe(
                  '\nThe position at which the watermark is placed.\n\nAn array of possible values can also be specified, in which case one value will be selected at random, such as `[ "center", "left", "bottom-left", "bottom-right" ]`.\n\nThis setting puts the watermark in the specified corner. To use a specific pixel offset for the watermark, you will need to add the padding to the image itself.\n',
                )
                .default('center'),
              watermark_x_offset: z
                .union([
                  z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                  z.any(),
                  z.number().int(),
                ])
                .describe(
                  "\nThe x-offset in number of pixels at which the watermark will be placed in relation to the position it has due to `watermark_position`.\n\nValues can be both positive and negative and yield different results depending on the `watermark_position` parameter. Positive values move the watermark closer to the image's center point, whereas negative values move the watermark further away from the image's center point.\n",
                )
                .default(0),
              watermark_y_offset: z
                .union([
                  z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                  z.any(),
                  z.number().int(),
                ])
                .describe(
                  "\nThe y-offset in number of pixels at which the watermark will be placed in relation to the position it has due to `watermark_position`.\n\nValues can be both positive and negative and yield different results depending on the `watermark_position` parameter. Positive values move the watermark closer to the image's center point, whereas negative values move the watermark further away from the image's center point.\n",
                )
                .default(0),
              watermark_size: z
                .union([z.any(), z.string().regex(new RegExp('^\\d+%$'))])
                .describe(
                  '\nThe size of the watermark, as a percentage, such as `"50%"`. How the watermark is resized greatly depends on the `watermark_resize_strategy`.\n',
                )
                .optional(),
              watermark_resize_strategy: z
                .union([z.any(), z.enum(['area', 'fit', 'stretch'])])
                .describe(
                  '\nTo explain how the resize strategies work, let\'s assume our target video size is 800×800 pixels and our watermark image is 400×300 pixels. Let\'s also assume, the `watermark_size` parameter is set to `"25%"`.\n\nFor the `"fit"` resize strategy, the watermark is scaled so that the longer side of the watermark takes up 25% of the corresponding video side. And the other side is scaled according to the aspect ratio of the watermark image. So with our watermark, the width is the longer side, and 25% of the video size would be 200px. Hence, the watermark would be resized to 200×150 pixels. If the `watermark_size` was set to `"50%"`", it would be resized to 400×300 pixels (so just left at its original size).\n\nFor the `"stretch"` resize strategy, the watermark image is stretched (meaning, it is resized without keeping its aspect ratio in mind) so that both sides take up 25% of the corresponding video side. Since our video is 800×800 pixels, for a watermark size of 25% the watermark would be resized to 200×200 pixels. Its height would appear stretched, because keeping the aspect ratio in mind it would be resized to 200×150 pixels instead.\n\nFor the `"area"` resize strategy, the watermark is resized (keeping its aspect ratio in check) so that it covers `"xx%"` of the video\'s surface area. The value from `watermark_size` is used for the percentage area size.\n',
                )
                .default('fit'),
              watermark_start_time: z
                .union([
                  z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                  z.any(),
                  z.number(),
                ])
                .describe(
                  '\nThe delay in seconds from the start of the video for the watermark to appear. By default the watermark is immediately shown.\n',
                )
                .default(0),
              watermark_duration: z
                .union([
                  z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                  z.any(),
                  z.number(),
                ])
                .describe(
                  '\nThe duration in seconds for the watermark to be shown. Can be used together with `watermark_start_time` to create nice effects. The default value is `-1.0`, which means that the watermark is shown for the entire duration of the video.\n',
                )
                .default(-1),
              watermark_opacity: z
                .union([
                  z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                  z.any(),
                  z.number().gte(0).lte(1),
                ])
                .describe(
                  '\nThe opacity of the watermark. Valid values are between `0` (invisible) and `1.0` (full visibility).\n',
                )
                .default(1),
              segment: z
                .union([z.any(), z.union([z.boolean(), z.any()])])
                .describe(
                  "\nSplits the file into multiple parts, to be used for Apple's [HTTP Live Streaming](https://developer.apple.com/resources/http-streaming/).\n",
                )
                .default(false),
              segment_duration: z
                .union([
                  z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                  z.any(),
                  z.number().int().gte(1),
                ])
                .describe(
                  '\nSpecifies the length of each HTTP segment. This is optional, and the default value as recommended by Apple is `10`. Do not change this value unless you have a good reason.\n',
                )
                .default(10),
              segment_prefix: z
                .union([z.any(), z.string()])
                .describe(
                  '\nThe prefix used for the naming. For example, a prefix of `"segment_"` would produce files named `"segment_0.ts"`, `"segment_1.ts"` and so on. This is optional, and defaults to the base name of the input file. Also see the related `segment_name` parameter.\n',
                )
                .default(''),
              segment_name: z
                .union([z.any(), z.string()])
                .describe(
                  '\nThe name used for the final segment. Available variables are `${segment_prefix}`, `${segment_number}` and `${segment_id}` (which is a UUIDv4 without dashes).\n',
                )
                .default(''),
              segment_time_delta: z
                .union([
                  z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
                  z.any(),
                  z.number(),
                ])
                .describe(
                  '\nDelta to apply to segment duration. This is optional and allows fine-tuning of segment boundaries.\n',
                )
                .optional(),
            })
            .strict(),
        ]),
      )
      .describe(
        'Defines the variants the video player can choose from. The keys are the names of the variant as they will appear in the generated playlists and URLs.',
      ),
    enabled_variants: z
      .union([
        z.any(),
        z.union([z.any(), z.string()]),
        z.union([z.any(), z.array(z.union([z.any(), z.string()]))]),
      ])
      .describe(
        'Specifies which variants, defined in the variants parameter, are enabled. Non-enabled variants will not be included in the master playlist.',
      )
      .optional(),
    segment_duration: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number(),
      ])
      .describe('The duration of each segment in seconds.')
      .default(6),
    sign_urls_for: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number(),
      ])
      .describe(
        'When signing URLs is enabled, the URLs in the generated playlist files will be signed. This parameter specifies the duration (in seconds) that the signed URLs will remain valid.',
      )
      .default(0),
    asset: z
      .union([z.any(), z.string()])
      .describe(
        'Controls which file is generated. For example, if the parameter is unset, a master playlist referencing the variants is generated.',
      )
      .optional(),
    asset_param_name: z
      .union([z.any(), z.string()])
      .describe(
        'Specifies from which URL parameter the asset parameter value is taken and which URL parameter to use when generating playlist files.',
      )
      .default('asset'),
  })
  .strict()

```

#### `/video/subtitle`

[/video/subtitle docs](https://transloadit.com/docs/robots/video-subtitle/)

Robot Parameter Zod Schema:

```ts
const videoSubtitleSchema = z
  .object({
    preset: VideoPresetSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    ffmpeg_stack: FfmpegStackSchema,
    use: UseSchema,
    ffmpeg: FfmpegSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    width: z
      .union([
        z.union([
          z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
          z.any(),
          z.number().int().gte(1),
        ]),
        z.null(),
      ])
      .describe(
        "\nWidth of the new video, in pixels.\n\nIf the value is not specified and the `preset` parameter is available, the `preset`'s [supplied width](https://transloadit.com/docs/presets/video/) will be implemented.\n",
      )
      .optional(),
    height: z
      .union([
        z.union([
          z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
          z.any(),
          z.number().int().gte(1),
        ]),
        z.null(),
      ])
      .describe(
        "\nHeight of the new video, in pixels.\n\nIf the value is not specified and the `preset` parameter is available, the `preset`'s [supplied height](https://transloadit.com/docs/presets/video/) will be implemented.\n",
      )
      .optional(),
    robot: z
      .literal('/video/subtitle')
      .describe(
        '\nThis <dfn>Robot</dfn> supports both SRT and VTT subtitle files.\n',
      ),
    subtitles_type: z
      .union([z.any(), z.enum(['burned', 'external', 'burn'])])
      .describe(
        '\nDetermines if subtitles are added as a separate stream to the video (value `"external"`) that then can be switched on and off in your video player, or if they should be burned directly into the video (value `"burned"` or `"burn"`) so that they become part of the video stream.\n',
      )
      .default('external'),
    border_style: z
      .union([z.any(), z.enum(['box', 'outline', 'shadow'])])
      .describe(
        '\nSpecifies the style of the subtitle. Use the `border_color` parameter to specify the color of the border.\n',
      )
      .default('outline'),
    border_color: z
      .union([
        z.any(),
        z.string().regex(new RegExp('^#?[0-9a-fA-F]{6}([0-9a-fA-F]{2})?$')),
      ])
      .describe(
        '\nThe color for the subtitle border. The first two hex digits specify the alpha value of the color.\n',
      )
      .default('40000000'),
    font: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe font family to use. Also includes boldness and style of the font.\n\n[Here](https://transloadit.com/docs/supported-formats/fonts/) is a list of all supported fonts.\n',
      )
      .default('Arial'),
    font_color: z
      .union([
        z.any(),
        z.string().regex(new RegExp('^#?[0-9a-fA-F]{3}([0-9a-fA-F]{3})?$')),
      ])
      .describe(
        '\nThe color of the subtitle text. The first two hex digits specify the alpha value of the color.\n',
      )
      .default('FFFFFF'),
    font_size: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gte(1),
      ])
      .describe('\nSpecifies the size of the text.\n')
      .default(16),
    position: z
      .union([
        z.any(),
        z.enum([
          'bottom',
          'bottom-left',
          'bottom-right',
          'center',
          'left',
          'right',
          'top',
          'top-left',
          'top-right',
        ]),
      ])
      .describe('\nSpecifies the position of the subtitles.\n')
      .default('bottom'),
    language: z
      .union([
        z.union([
          z
            .any()
            .refine(
              (value) => !z.any().safeParse(value).success,
              'Invalid input: Should NOT be valid against schema',
            ),
          z.union([z.any(), z.string()]),
        ]),
        z.null(),
      ])
      .describe(
        '\nSpecifies the language of the subtitles. Only used if the subtitles are external.\n',
      )
      .optional(),
    keep_subtitles: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nSpecifies if existing subtitles in the input file should be kept or be replaced by the new subtitle. Only used if the subtitles are external.\n',
      )
      .default(false),
  })
  .strict()

```

#### `/video/thumbs`

[/video/thumbs docs](https://transloadit.com/docs/robots/video-thumbs/)

Robot Parameter Zod Schema:

```ts
const videoThumbsSchema = z
  .object({
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    ffmpeg_stack: FfmpegStackSchema,
    use: UseSchema,
    ffmpeg: FfmpegSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    robot: z
      .literal('/video/thumbs')
      .describe(
        '\n> [!Note]\n> Even though thumbnails are extracted from videos in parallel, we sort the thumbnails before adding them to the Assembly results. So the order in which they appear there reflects the order in which they appear in the video. You can also make sure by checking the <code>thumb_index</code> meta key.\n',
      ),
    count: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gte(1).lte(999),
      ])
      .describe(
        '\nThe number of thumbnails to be extracted. As some videos have incorrect durations, the actual number of thumbnails generated may be less in rare cases. The maximum number of thumbnails we currently allow is 999.\n\nThe thumbnails are taken at regular intervals, determined by dividing the video duration by the count. For example, a count of 3 will produce thumbnails at 25%, 50% and 75% through the video.\n\nTo extract thumbnails for specific timestamps, use the `offsets` parameter.\n',
      )
      .default(8),
    offsets: z
      .union([
        z.any(),
        z.union([
          z.any(),
          z.array(
            z.union([
              z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
              z.any(),
              z.number(),
            ]),
          ),
        ]),
        z.union([
          z.any(),
          z.array(z.union([z.any(), z.string().regex(new RegExp('^\\d+%$'))])),
        ]),
      ])
      .describe(
        '\nAn array of offsets representing seconds of the file duration, such as `[ 2, 45, 120 ]`. Millisecond durations of a file can also be used by using decimal place values. For example, an offset from 1250 milliseconds would be represented with `1.25`. Offsets can also be percentage values such as `[ "2%", "50%", "75%" ]`.\n\nThis option cannot be used with the `count` parameter, and takes precedence if both are specified. Out-of-range offsets are silently ignored.\n',
      )
      .default([]),
    format: z
      .union([z.any(), z.enum(['jpeg', 'jpg', 'png'])])
      .describe(
        '\nThe format of the extracted thumbnail. Supported values are `"jpg"`, `"jpeg"` and `"png"`. Even if you specify the format to be `"jpeg"` the resulting thumbnails will have a `"jpg"` file extension.\n',
      )
      .default('jpeg'),
    width: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gte(1).lte(1920),
      ])
      .describe(
        '\nThe width of the thumbnail, in pixels. Defaults to the original width of the video.\n',
      )
      .optional(),
    height: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gte(1).lte(1080),
      ])
      .describe(
        '\nThe height of the thumbnail, in pixels. Defaults to the original height of the video.\n',
      )
      .optional(),
    resize_strategy: z
      .union([
        z.any(),
        z.enum(['crop', 'fit', 'fillcrop', 'min_fit', 'pad', 'stretch']),
      ])
      .describe(
        '\nOne of the [available resize strategies](https://transloadit.com/docs/topics/resize-strategies/).\n',
      )
      .default('pad'),
    background: z
      .union([
        z.any(),
        z.string().regex(new RegExp('^#?[0-9a-fA-F]{6}([0-9a-fA-F]{2})?$')),
      ])
      .describe(
        '\nThe background color of the resulting thumbnails in the `"rrggbbaa"` format (red, green, blue, alpha) when used with the `"pad"` resize strategy. The default color is black.\n',
      )
      .default('#00000000'),
    rotate: z
      .union([
        z.any(),
        z.union([z.any(), z.literal(0)]),
        z.union([z.any(), z.literal(90)]),
        z.union([z.any(), z.literal(180)]),
        z.union([z.any(), z.literal(270)]),
        z.union([z.any(), z.literal(360)]),
      ])
      .describe(
        '\nForces the video to be rotated by the specified degree integer. Currently, only multiples of 90 are supported. We automatically correct the orientation of many videos when the orientation is provided by the camera. This option is only useful for videos requiring rotation because it was not detected by the camera.\n',
      )
      .default(0),
    input_codec: z
      .union([z.any(), z.string()])
      .describe(
        '\nSpecifies the input codec to use when decoding the video. This is useful for videos with special codecs that require specific decoders.\n',
      )
      .optional(),
  })
  .strict()

```

#### `/vimeo/import`

[/vimeo/import docs](https://transloadit.com/docs/robots/vimeo-import/)

Robot Parameter Zod Schema:

```ts
const vimeoImportSchema = z
  .object({
    credentials: CredentialsSchema,
    ignore_errors: IgnoreErrorsSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    force_name: z
      .union([
        z.union([
          z.any(),
          z.union([z.any(), z.string()]),
          z.union([z.any(), z.array(z.union([z.any(), z.string()]))]),
        ]),
        z.null(),
      ])
      .describe(
        'Custom name for the imported file(s). By default file names are derived from the source.',
      )
      .default(null),
    robot: z.literal('/vimeo/import'),
    path: z
      .union([
        z.any(),
        z.union([z.any(), z.string()]),
        z.union([z.any(), z.array(z.union([z.any(), z.string()]))]),
      ])
      .describe(
        "\nThe Vimeo API path to import from. The most common paths are:\n- `me/videos`: Your own videos\n- `me/likes`: Videos you've liked\n- `me/albums/:album_id/videos`: Videos from a specific album\n- `me/channels/:channel_id/videos`: Videos from a specific channel\n- `me/groups/:group_id/videos`: Videos from a specific group\n- `me/portfolios/:portfolio_id/videos`: Videos from a specific portfolio\n- `me/watchlater`: Videos in your watch later queue\n\nYou can also use an array of path strings here to import multiple paths in the same <dfn>Robot</dfn>'s <dfn>Step</dfn>.\n",
      )
      .default('me/videos'),
    page_number: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gt(0),
      ])
      .describe(
        'The page number to import from. Vimeo API uses pagination for large result sets.',
      )
      .default(1),
    files_per_page: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gt(0).lte(100),
      ])
      .describe(
        'The number of files to import per page. Maximum is 100 as per Vimeo API limits.',
      )
      .default(20),
    rendition: z
      .union([
        z.any(),
        z.enum(['240p', '360p', '540p', '720p', '1080p', 'source']),
      ])
      .describe('The quality of the video to import.')
      .default('720p'),
  })
  .strict()

```

#### `/vimeo/store`

[/vimeo/store docs](https://transloadit.com/docs/robots/vimeo-store/)

Robot Parameter Zod Schema:

```ts
const vimeoStoreSchema = z
  .object({
    credentials: CredentialsSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    robot: z.literal('/vimeo/store'),
    title: z
      .union([
        z.any(),
        z
          .string()
          .describe('\nThe title of the video to be displayed on Vimeo.\n'),
      ])
      .describe('\nThe title of the video to be displayed on Vimeo.\n'),
    description: z
      .union([
        z.any(),
        z
          .string()
          .describe(
            '\nThe description of the video to be displayed on Vimeo.\n',
          ),
      ])
      .describe('\nThe description of the video to be displayed on Vimeo.\n'),
    acl: z
      .union([
        z.any(),
        z.enum([
          'anybody',
          'contacts',
          'disable',
          'nobody',
          'password',
          'unlisted',
          'users',
        ]),
      ])
      .describe(
        '\nControls access permissions for the video. Here are the valid values:\n\n- `"anybody"` — anyone can access the video.\n- `"contacts"` — only those who follow the owner on Vimeo can access the video.\n- `"disable"` — the video is embeddable, but it\'s hidden on Vimeo and can\'t be played.\n- `"nobody"` — no one except the owner can access the video.\n- `"password"` — only those with the password can access the video.\n- `"unlisted"` — only those with the private link can access the video.\n- `"users"` — only Vimeo members can access the video.\n',
      )
      .default('anybody'),
    password: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe password to access the video if `acl` is `"password"`.\n',
      )
      .optional(),
    showcases: z
      .union([z.any(), z.array(z.union([z.any(), z.string()]))])
      .describe(
        '\nAn array of string IDs of showcases that you want to add the video to. The IDs can be found when browsing Vimeo. For example `https://vimeo.com/manage/showcases/[SHOWCASE_ID]/info`.\n',
      )
      .default([]),
    downloadable: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nWhether or not the video can be downloaded from the Vimeo website.\n\nOnly set this to `true` if you have unlocked this feature in your Vimeo accounting by upgrading to their "Pro" plan. If you use it while on their Freemium plan, the Vimeo API will return an `"Invalid parameter supplied"` error.\n',
      )
      .default(false),
    folder_id: z
      .union([z.union([z.any(), z.string()]), z.null()])
      .describe(
        '\nThe ID of the folder to which the video is uploaded.\n\nWhen visiting one of your folders, the URL is similar to `https://vimeo.com/manage/folders/xxxxxxxx`. The folder_id would be `"xxxxxxxx"`.\n',
      )
      .default(null),
    folder_uri: z
      .union([z.any(), z.string()])
      .describe(
        '\nDeprecated. Please use `folder_id` instead. The URI of the folder to which the video is uploaded.\n',
      )
      .optional(),
  })
  .strict()

```

#### `/wasabi/import`

[/wasabi/import docs](https://transloadit.com/docs/robots/wasabi-import/)

Robot Parameter Zod Schema:

```ts
const wasabiImportSchema = z
  .object({
    credentials: CredentialsSchema,
    ignore_errors: IgnoreErrorsSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    force_name: z
      .union([
        z.union([
          z.any(),
          z.union([z.any(), z.string()]),
          z.union([z.any(), z.array(z.union([z.any(), z.string()]))]),
        ]),
        z.null(),
      ])
      .describe(
        'Custom name for the imported file(s). By default file names are derived from the source.',
      )
      .default(null),
    bucket: z.union([z.any(), z.string()]).optional(),
    bucket_region: z
      .union([z.any(), z.string()])
      .describe('\nThe region where the bucket is located.\n')
      .optional(),
    host: z.union([z.any(), z.string()]).optional(),
    key: z.union([z.any(), z.string()]).optional(),
    secret: z.union([z.any(), z.string()]).optional(),
    robot: z.literal('/wasabi/import'),
    path: z
      .union([
        z.any(),
        z.union([z.any(), z.string()]),
        z.union([z.any(), z.array(z.union([z.any(), z.string()]))]),
      ])
      .describe(
        "\nThe path in your bucket to the specific file or directory. If the path points to a file, only this file will be imported. For example: `images/avatar.jpg`.\n\nIf it points to a directory, indicated by a trailing slash (`/`), then all files that are direct descendants of this directory will be imported. For example: `images/`.\n\nDirectories are **not** imported recursively. If you want to import files from subdirectories and sub-subdirectories, enable the `recursive` parameter.\n\nIf you want to import all files from the root directory, please use `/` as the value here. In this case, make sure all your objects belong to a path. If you have objects in the root of your bucket that aren't prefixed with `/`, you'll receive an error: `A client error (NoSuchKey) occurred when calling the GetObject operation: The specified key does not exist.`\n\nYou can also use an array of path strings here to import multiple paths in the same <dfn>Robot</dfn>'s <dfn>Step</dfn>.\n",
      ),
    recursive: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        '\nSetting this to `true` will enable importing files from subfolders and sub-subfolders, etc. of the given path.\n\nPlease use the pagination parameters `page_number` and `files_per_page` wisely here.\n',
      )
      .default(false),
    page_number: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int(),
      ])
      .describe(
        '\nThe pagination page number. For now, in order to not break backwards compatibility in non-recursive imports, this only works when recursive is set to `true`.\n\nWhen doing big imports, make sure no files are added or removed from other scripts within your path, otherwise you might get weird results with the pagination.\n',
      )
      .default(1),
    files_per_page: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int(),
      ])
      .describe(
        '\nThe pagination page size. This only works when recursive is `true` for now, in order to not break backwards compatibility in non-recursive imports.\n',
      )
      .default(1000),
    return_file_stubs: z
      .union([
        z.any(),
        z.union([
          z
            .boolean()
            .describe(
              '\nIf set to `true`, the Robot will not yet import the actual files but instead return an empty file stub that includes a URL from where the file can be imported by subsequent Robots. This is useful for cases where subsequent Steps need more control over the import process, such as with 🤖/video/ondemand. This parameter should only be set if all subsequent Steps use Robots that support file stubs.\n',
            ),
          z.any(),
        ]),
      ])
      .describe(
        '\nIf set to `true`, the Robot will not yet import the actual files but instead return an empty file stub that includes a URL from where the file can be imported by subsequent Robots. This is useful for cases where subsequent Steps need more control over the import process, such as with 🤖/video/ondemand. This parameter should only be set if all subsequent Steps use Robots that support file stubs.\n',
      )
      .default(false),
  })
  .strict()

```

#### `/wasabi/store`

[/wasabi/store docs](https://transloadit.com/docs/robots/wasabi-store/)

Robot Parameter Zod Schema:

```ts
const wasabiStoreSchema = z
  .object({
    credentials: CredentialsSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    bucket: z.union([z.any(), z.string()]).optional(),
    bucket_region: z
      .union([z.any(), z.string()])
      .describe('\nThe region where the bucket is located.\n')
      .optional(),
    host: z.union([z.any(), z.string()]).optional(),
    key: z.union([z.any(), z.string()]).optional(),
    secret: z.union([z.any(), z.string()]).optional(),
    robot: z
      .literal('/wasabi/store')
      .describe(
        '\nThe URL to the result file will be returned in the <dfn>Assembly Status JSON</dfn>.\n',
      ),
    path: z
      .union([z.any(), z.string()])
      .describe(
        '\nThe path at which the file is to be stored. This may include any available [Assembly variables](https://transloadit.com/docs/topics/assembly-instructions/#assembly-variables). The path must not be a directory.\n',
      )
      .default('${unique_prefix}/${file.url_name}'),
    acl: z
      .union([z.any(), z.enum(['private', 'public-read'])])
      .describe('\nThe permissions used for this file.\n')
      .default('public-read'),
    headers: z
      .record(z.union([z.any(), z.string()]))
      .describe(
        '\nAn object containing a list of headers to be set for this file on Wasabi Spaces, such as `{ FileURL: "${file.url_name}" }`. This can also include any available [Assembly Variables](https://transloadit.com/docs/topics/assembly-instructions/#assembly-variables).\n\nObject Metadata can be specified using `x-amz-meta-*` headers. Note that these headers [do not support non-ASCII metadata values](https://docs.aws.amazon.com/AmazonS3/latest/dev/UsingMetadata.html#UserMetadata).\n',
      )
      .default({ 'Content-Type': '${file.mime}' }),
    sign_urls_for: z
      .union([
        z.string().regex(new RegExp('^\\d+(\\.\\d+)?$')),
        z.any(),
        z.number().int().gte(0),
      ])
      .describe(
        '\nThis parameter provides signed URLs in the result JSON (in the `signed_ssl_url` property). The number that you set this parameter to is the URL expiry time in seconds. If this parameter is not used, no URL signing is done.\n',
      )
      .optional(),
  })
  .strict()

```

#### `/youtube/store`

[/youtube/store docs](https://transloadit.com/docs/robots/youtube-store/)

Robot Parameter Zod Schema:

```ts
const youtubeStoreSchema = z
  .object({
    credentials: CredentialsSchema,
    output_meta: OutputMetaSchema,
    result: ResultSchema,
    use: UseSchema,
    queue: z
      .union([z.any(), z.literal('batch')])
      .describe(
        "Setting the queue to 'batch', manually downgrades the priority of jobs for this step to avoid consuming Priority job slots for jobs that don't need zero queue waiting times",
      )
      .optional(),
    force_accept: z
      .union([z.any(), z.union([z.boolean(), z.any()])])
      .describe(
        'Force a Robot to accept a file type it would have ignored.\n\nBy default, Robots ignore files they are not familiar with.\n[🤖/video/encode](https://transloadit.com/docs/robots/video-encode/), for\nexample, will happily ignore input images.\n\nWith the `force_accept` parameter set to `true`, you can force Robots to accept all files thrown at them.\nThis will typically lead to errors and should only be used for debugging or combatting edge cases.\n',
      )
      .default(false),
    robot: z
      .literal('/youtube/store')
      .describe(
        '\n> [!Note]\n> This <dfn>Robot</dfn> only accepts videos.\n\n## Installation\n\nSince YouTube works with OAuth, you will need to generate [Template Credentials](https://transloadit.com/c/template-credentials/) to use this <dfn>Robot</dfn>.\n\nTo change the `title`, `description`, `category`, or `keywords` per video, we recommend to [inject variables into your Template](https://transloadit.com/docs/topics/templates/).\n\n## Adding a thumbnail image to your video\n\nYou can add a custom thumbnail to your video on YouTube by using our `"as"` syntax for the `"use"` parameter to supply both a video and an image to the step:\n\n```json\n"exported": {\n  "use": [\n    { "name": "video_encode_step", "as": "video" },\n    { "name": "image_resize_step", "as": "image" },\n  ],\n  ...\n},\n```\n\nIf you encounter an error such as "The authenticated user doesnʼt have permissions to upload and set custom video thumbnails", you should go to your YouTube account and try adding a custom thumbnail to one of your existing videos. Youʼll be prompted to add your phone number. Once youʼve added it, the error should go away.\n',
      ),
    title: z
      .union([
        z.any(),
        z
          .string()
          .max(80)
          .describe(
            '\nThe title of the video to be displayed on YouTube.\n\nNote that since the YouTube API requires titles to be within 80 characters, longer titles may be truncated.\n',
          ),
      ])
      .describe(
        '\nThe title of the video to be displayed on YouTube.\n\nNote that since the YouTube API requires titles to be within 80 characters, longer titles may be truncated.\n',
      ),
    description: z
      .union([
        z.any(),
        z
          .string()
          .describe(
            '\nThe description of the video to be displayed on YouTube. This can be up to 5000 characters, including `\\n` for new-lines.\n',
          ),
      ])
      .describe(
        '\nThe description of the video to be displayed on YouTube. This can be up to 5000 characters, including `\\n` for new-lines.\n',
      ),
    category: z
      .union([
        z.any(),
        z
          .enum([
            'autos & vehicles',
            'comedy',
            'education',
            'entertainment',
            'film & animation',
            'gaming',
            'howto & style',
            'music',
            'news & politics',
            'people & blogs',
            'pets & animals',
            'science & technology',
            'sports',
            'travel & events',
          ])
          .describe('\nThe category to which this video will be assigned.\n'),
      ])
      .describe('\nThe category to which this video will be assigned.\n'),
    keywords: z
      .union([
        z.any(),
        z
          .string()
          .describe(
            '\nTags used to describe the video, separated by commas. These tags will also be displayed on YouTube.\n',
          ),
      ])
      .describe(
        '\nTags used to describe the video, separated by commas. These tags will also be displayed on YouTube.\n',
      ),
    visibility: z
      .union([
        z.any(),
        z
          .enum(['public', 'private', 'unlisted'])
          .describe('\nDefines the visibility of the uploaded video.\n'),
      ])
      .describe('\nDefines the visibility of the uploaded video.\n'),
  })
  .strict()

```


## More resources

- [Getting Started](https://transloadit.com/docs/): Introduction to Transloadit's core concepts
- [Assembly Instructions](https://transloadit.com/docs/topics/assembly-instructions/): How to create processing workflows
- [Templates](https://transloadit.com/docs/topics/templates/): Learn about reusable Assembly Instructions
- [API Reference](https://transloadit.com/docs/api/): Detailed API documentation
- [Community Forum](https://community.transloadit.com/): Get help from other Transloadit users
- [Status Page](https://status.transloadit.com/): Real-time status of our services
- [Pricing](https://transloadit.com/pricing/): Transloadit pricing plans
- [llms](https://transloadit.com/llms.txt): LLMs docs intro (13kb)
- [llms-full](https://transloadit.com/llms-full.txt): LLMs full docs (270kb)
- [Blog](https://transloadit.com/blog/): Latest news and updates

this file is 456kB