# If local audio, upload and retrieve the signed url
with open("music.mp3", "rb") as f:
    uploaded_audio = client.files.upload(
      file={
          "content": f,
          "file_name": f.name
      },
      purpose="audio"
    )

signed_url = client.files.get_signed_url(file_id=uploaded_audio.id)