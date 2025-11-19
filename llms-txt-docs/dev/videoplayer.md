# Source: https://dev.writer.com/components/videoplayer.md

# Video Player

A Video player component that can play various video formats.

<img src="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/framework/public/components/videoplayer.png?fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=b7ac2f9091c2198a695401869f95de5d" data-og-width="1141" width="1141" data-og-height="668" height="668" data-path="framework/public/components/videoplayer.png" data-optimize="true" data-opv="3" srcset="https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/framework/public/components/videoplayer.png?w=280&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=0acd5f49b55d8d7d63facb10c1173406 280w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/framework/public/components/videoplayer.png?w=560&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=fe2a08940e0227051ac210b98ccffab8 560w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/framework/public/components/videoplayer.png?w=840&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=3397c52bc374c5039135e0c4fba7df34 840w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/framework/public/components/videoplayer.png?w=1100&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=99fb230b392722e3621ff7fc5cd674ac 1100w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/framework/public/components/videoplayer.png?w=1650&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=9a9c90e805cd599d132137eb8eede9c5 1650w, https://mintcdn.com/writer/dHnl9w_Om9ycQRLE/framework/public/components/videoplayer.png?w=2500&fit=max&auto=format&n=dHnl9w_Om9ycQRLE&q=85&s=bc27b00b8b0a3bb3f2ac72c297a8eb31 2500w" />

Use your app's static folder to serve videos directly. For example, `static/my_video.mp4`.

Alternatively, you can pack bytes or files in state:

`state[&quot;vid_b&quot;] = wf.pack_bytes(vid_bytes, &quot;video/mp4&quot;)`

`state[&quot;vid_f&quot;] = wf.pack_file(vid_file, &quot;video/mp4&quot;)`

Afterwards, you can reference the video using the syntax `@{vid_f}`.

## Fields

<table className="componentFields">
  <thead>
    <th>Name</th>
    <th>Type</th>
    <th class="desc">Description</th>
    <th>Options</th>
  </thead>

  <tbody>
    <tr>
      <td>Source</td>
      <td>Text</td>
      <td>The URL of the video file. Alternatively, you can pass a file via state.</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Enable controls</td>
      <td>Boolean</td>
      <td>Display Video player controls.</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Autoplay</td>
      <td>Boolean</td>
      <td>Autoplay the video when the component is loaded.</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Loop</td>
      <td>Boolean</td>
      <td>Loop the video when it reaches the end.</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Muted</td>
      <td>Boolean</td>
      <td>Mute the video by default.</td>

      <td>
        <span>-</span>
      </td>
    </tr>

    <tr>
      <td>Custom CSS classes</td>
      <td>Text</td>
      <td>CSS classes, separated by spaces. You can define classes in custom stylesheets.</td>

      <td>
        <span>-</span>
      </td>
    </tr>
  </tbody>
</table>
