# Source: https://docs.together.ai/docs/how-to-build-real-time-audio-transcription-app.md

# How to build an AI audio transcription app with Whisper

> Learn how to build a real-time AI audio transcription app with Whisper, Next.js, and Together AI.

In this guide, we're going to go over how we built [UseWhisper.io](https://usewhisper.io), an open source audio transcription app that converts speech to text almost instantly & can transform it into summaries. It's built using the [Whisper Large v3 API](https://www.together.ai/models/openai-whisper-large-v3) on Together AI and supports both live recording and file uploads.

<img src="https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/cover.jpg?fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=07a613b09568c0726911221011dbf694" alt="usewhisper.io" data-og-width="2400" width="2400" data-og-height="1260" height="1260" data-path="images/guides/whisper/cover.jpg" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/cover.jpg?w=280&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=435f9e2add5d9864345b457d2031b96d 280w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/cover.jpg?w=560&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=98c58ab6d675cb5a4157f3fb718fb391 560w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/cover.jpg?w=840&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=580d414399cbf99b0c389e7586e001b5 840w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/cover.jpg?w=1100&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=925e8c16fce481e7d876a609b538a52a 1100w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/cover.jpg?w=1650&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=1b8d6614de2665aceff547559b9c7e5c 1650w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/cover.jpg?w=2500&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=d3a58a13e57e1785423af5a19fd5e5eb 2500w" />

In this post, you'll learn how to build the core parts of UseWhisper.io. The app is open-source and built with Next.js, tRPC for type safety, and Together AI's API, but the concepts can be applied to any language or framework.

## Building the audio recording interface

<img src="https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/recording-modal.png?fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=56a54a41ccd4f317e72f7046cf3aaee0" alt="Recording modal UI" data-og-width="699" width="699" data-og-height="384" height="384" data-path="images/guides/whisper/recording-modal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/recording-modal.png?w=280&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=f08d68857caa9d4155de1ee64ea8213c 280w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/recording-modal.png?w=560&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=ab8b211d7ffb16cff04aaadc37eb1207 560w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/recording-modal.png?w=840&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=92778c223fed6d1e7fe9f67928ded434 840w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/recording-modal.png?w=1100&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=bc84a97166e1c8d7c5b8ed2eaabf37f1 1100w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/recording-modal.png?w=1650&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=67878551dfe6fdb7b029545c64e085aa 1650w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/recording-modal.png?w=2500&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=96a49d291ecfa1cbf99bed6a01ca3ed4 2500w" />

Whisper's core interaction is a recording modal where users can capture audio directly in the browser:

```tsx  theme={null}
function RecordingModal({ onClose }: { onClose: () => void }) {
  const { recording, audioBlob, startRecording, stopRecording } =
    useAudioRecording();

  const handleRecordingToggle = async () => {
    if (recording) {
      stopRecording();
    } else {
      await startRecording();
    }
  };

  // Auto-process when we get an audio blob
  useEffect(() => {
    if (audioBlob) {
      handleSaveRecording();
    }
  }, [audioBlob]);

  return (
    <Dialog open onOpenChange={onClose}>
      <DialogContent>
        <Button onClick={handleRecordingToggle}>
          {recording ? "Stop Recording" : "Start Recording"}
        </Button>
      </DialogContent>
    </Dialog>
  );
}
```

The magic happens in our custom `useAudioRecording` hook, which handles all the browser audio recording logic.

## Recording audio in the browser

To capture audio, we use the MediaRecorder API with a simple hook:

```tsx  theme={null}
function useAudioRecording() {
  const [recording, setRecording] = useState(false);
  const [audioBlob, setAudioBlob] = useState<Blob | null>(null);

  const mediaRecorderRef = useRef<MediaRecorder | null>(null);
  const chunksRef = useRef<Blob[]>([]);

  const startRecording = async () => {
    try {
      // Request microphone access
      const stream = await navigator.mediaDevices.getUserMedia({ audio: true });

      // Create MediaRecorder
      const mediaRecorder = new MediaRecorder(stream);
      mediaRecorderRef.current = mediaRecorder;
      chunksRef.current = [];

      // Collect audio data
      mediaRecorder.ondataavailable = (e) => {
        chunksRef.current.push(e.data);
      };

      // Create blob when recording stops
      mediaRecorder.onstop = () => {
        const blob = new Blob(chunksRef.current, { type: "audio/webm" });
        setAudioBlob(blob);
        // Stop all tracks to release microphone
        stream.getTracks().forEach((track) => track.stop());
      };

      mediaRecorder.start();
      setRecording(true);
    } catch (err) {
      console.error("Microphone access denied:", err);
    }
  };

  const stopRecording = () => {
    if (mediaRecorderRef.current && recording) {
      mediaRecorderRef.current.stop();
      setRecording(false);
    }
  };

  return { recording, audioBlob, startRecording, stopRecording };
}
```

This simplified version focuses on the core functionality: start recording, stop recording, and get the audio blob.

## Uploading and transcribing audio

Once we have our audio blob (from recording) or file (from upload), we need to send it to Together AI's Whisper model. We use S3 for temporary storage and tRPC for type-safe API calls:

```tsx  theme={null}
const handleSaveRecording = async () => {
  if (!audioBlob) return;

  try {
    // Upload to S3
    const file = new File([audioBlob], `recording-${Date.now()}.webm`, {
      type: "audio/webm",
    });
    const { url } = await uploadToS3(file);

    // Call our tRPC endpoint
    const { id } = await transcribeMutation.mutateAsync({
      audioUrl: url,
      language: selectedLanguage,
      durationSeconds: duration,
    });

    // Navigate to transcription page
    router.push(`/whispers/${id}`);
  } catch (err) {
    toast.error("Failed to transcribe audio. Please try again.");
  }
};
```

## Creating the transcription API with tRPC

Our backend uses tRPC to provide end-to-end type safety. Here's our transcription endpoint:

```tsx  theme={null}
import { Together } from "together-ai";
import { createTogetherAI } from "@ai-sdk/togetherai";
import { generateText } from "ai";

export const whisperRouter = t.router({
  transcribeFromS3: protectedProcedure
    .input(
      z.object({
        audioUrl: z.string(),
        language: z.string().optional(),
        durationSeconds: z.number().min(1),
      })
    )
    .mutation(async ({ input, ctx }) => {
      // Call Together AI's Whisper model
      const togetherClient = new Together({
        apiKey: process.env.TOGETHER_API_KEY,
      });

      const res = await togetherClient.audio.transcriptions.create({
        file: input.audioUrl,
        model: "openai/whisper-large-v3",
        language: input.language || "en",
      });

      const transcription = res.text as string;

      // Generate a title using LLM
      const togetherAI = createTogetherAI({
        apiKey: process.env.TOGETHER_API_KEY,
      });

      const { text: title } = await generateText({
        prompt: `Generate a title for the following transcription with max of 10 words: ${transcription}`,
        model: togetherAI("meta-llama/Llama-3.3-70B-Instruct-Turbo"),
        maxTokens: 10,
      });

      // Save to database
      const whisperId = uuidv4();
      await prisma.whisper.create({
        data: {
          id: whisperId,
          title: title.slice(0, 80),
          userId: ctx.auth.userId,
          fullTranscription: transcription,
          audioTracks: {
            create: [
              {
                fileUrl: input.audioUrl,
                partialTranscription: transcription,
                language: input.language,
              },
            ],
          },
        },
      });

      return { id: whisperId };
    }),
});
```

The beauty of tRPC is that our frontend gets full TypeScript intellisense and type checking for this API call.

## Supporting file uploads

<img src="https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/upload-modal.png?fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=469a391f117228a11de74c751b49996c" alt="Upload modal UI" data-og-width="664" width="664" data-og-height="408" height="408" data-path="images/guides/whisper/upload-modal.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/upload-modal.png?w=280&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=db453b15f4720d9fe62b6363a3667fc9 280w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/upload-modal.png?w=560&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=1dddb61895e556c1a755541932cbd7a8 560w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/upload-modal.png?w=840&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=645f34df69928a02dbe627f36a05d464 840w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/upload-modal.png?w=1100&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=bddc420aecbd3b49437ab7a833f80c3b 1100w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/upload-modal.png?w=1650&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=25dc288c6b3a79e9dc3a5ae570ad0699 1650w, https://mintcdn.com/togetherai-52386018/Wza_C-RhVTrquKqp/images/guides/whisper/upload-modal.png?w=2500&fit=max&auto=format&n=Wza_C-RhVTrquKqp&q=85&s=231d74b13ade1d1e94df0a37d1b79517 2500w" />

For users who want to upload existing audio files, we use react-dropzone and next-s3-upload.

Next-s3-upload handles the S3 upload in the backend and fully integrates with Next.js API routes in a simple 5 minute setup you can read more here: [https://next-s3-upload.codingvalue.com/](https://next-s3-upload.codingvalue.com/)
:

```tsx  theme={null}
import Dropzone from "react-dropzone";
import { useS3Upload } from "next-s3-upload";

function UploadModal({ onClose }: { onClose: () => void }) {
  const { uploadToS3 } = useS3Upload();

  const handleDrop = useCallback(async (acceptedFiles: File[]) => {
    const file = acceptedFiles[0];
    if (!file) return;

    try {
      // Get audio duration and upload in parallel
      const [duration, { url }] = await Promise.all([
        getDuration(file),
        uploadToS3(file),
      ]);

      // Transcribe using the same endpoint
      const { id } = await transcribeMutation.mutateAsync({
        audioUrl: url,
        language,
        durationSeconds: Math.round(duration),
      });

      router.push(`/whispers/${id}`);
    } catch (err) {
      toast.error("Failed to transcribe audio. Please try again.");
    }
  }, []);

  return (
    <Dropzone
      accept={{
        "audio/mpeg3": [".mp3"],
        "audio/wav": [".wav"],
        "audio/mp4": [".m4a"],
      }}
      onDrop={handleDrop}
    >
      {({ getRootProps, getInputProps }) => (
        <div {...getRootProps()}>
          <input {...getInputProps()} />
          <p>Drop audio files here or click to upload</p>
        </div>
      )}
    </Dropzone>
  );
}
```

## Adding audio transformations

Once we have a transcription, users can transform it using LLMs. We support summarization, extraction, and custom transformations:

```tsx  theme={null}
import { createTogetherAI } from "@ai-sdk/togetherai";
import { generateText } from "ai";

const transformText = async (prompt: string, transcription: string) => {
  const togetherAI = createTogetherAI({
    apiKey: process.env.TOGETHER_API_KEY,
  });

  const { text } = await generateText({
    prompt: `${prompt}\n\nTranscription: ${transcription}`,
    model: togetherAI("meta-llama/Llama-3.3-70B-Instruct-Turbo"),
  });

  return text;
};
```

## Type safety with tRPC

One of the key benefits of using tRPC is the end-to-end type safety. When we call our API from the frontend:

```tsx  theme={null}
const transcribeMutation = useMutation(
  trpc.whisper.transcribeFromS3.mutationOptions()
);

// TypeScript knows the exact shape of the input and output
const result = await transcribeMutation.mutateAsync({
  audioUrl: "...",
  language: "en", // TypeScript validates this
  durationSeconds: 120,
});

// result.id is properly typed
router.push(`/whispers/${result.id}`);
```

This eliminates runtime errors and provides excellent developer experience with autocomplete and type checking.

## Going beyond basic transcription

Whisper is open-source, so check out the [full code](https://github.com/nutlope/whisper) to learn more and get inspired to build your own audio transcription apps.

When you're ready to start transcribing audio in your own apps, sign up for [Together AI](https://togetherai.link) today and make your first API call in minutes!


---

> To find navigation and other pages in this documentation, fetch the llms.txt file at: https://docs.together.ai/llms.txt