# Source: https://directus.io/docs/raw/configuration/pm2.md

# PM2

> Configuration for PM2, the process manager for Directus.

<partial content="config-env-vars">



</partial>

For more information on what these options do, refer directly to the [`pm2` documentation](https://pm2.keymetrics.io/docs/usage/application-declaration/).

<table>
<thead>
  <tr>
    <th>
      Variable
    </th>
    
    <th>
      Description
    </th>
    
    <th>
      Default
    </th>
  </tr>
</thead>

<tbody>
  <tr>
    <td>
      <code>
        PM2_INSTANCES
      </code>
      
      <sup>
        <span>
          1
        </span>
      </sup>
    </td>
    
    <td>
      Number of app instance to be launched.
    </td>
    
    <td>
      <code>
        1
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        PM2_EXEC_MODE
      </code>
    </td>
    
    <td>
      One of <code>
        fork
      </code>
      
      , <code>
        cluster
      </code>
      
      .
    </td>
    
    <td>
      <code>
        'cluster'
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        PM2_MAX_MEMORY_RESTART
      </code>
    </td>
    
    <td>
      App will be restarted if it exceeds the amount of memory specified.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        PM2_MIN_UPTIME
      </code>
    </td>
    
    <td>
      Min uptime of the app to be considered started.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        PM2_LISTEN_TIMEOUT
      </code>
    </td>
    
    <td>
      Time in ms before forcing a reload if app not listening.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        PM2_KILL_TIMEOUT
      </code>
    </td>
    
    <td>
      Time in milliseconds before sending a final SIGKILL.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        PM2_MAX_RESTARTS
      </code>
    </td>
    
    <td>
      Number of failed restarts before the process is killed.
    </td>
    
    <td>
      
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        PM2_RESTART_DELAY
      </code>
    </td>
    
    <td>
      Time to wait before restarting a crashed app.
    </td>
    
    <td>
      <code>
        0
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        PM2_AUTO_RESTART
      </code>
    </td>
    
    <td>
      Automatically restart Directus if it crashes unexpectedly.
    </td>
    
    <td>
      <code>
        false
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        PM2_LOG_ERROR_FILE
      </code>
    </td>
    
    <td>
      Error file path.
    </td>
    
    <td>
      <code>
        $HOME/.pm2/logs/<app name>-error-<pid>.log
      </code>
    </td>
  </tr>
  
  <tr>
    <td>
      <code>
        PM2_LOG_OUT_FILE
      </code>
    </td>
    
    <td>
      Output file path.
    </td>
    
    <td>
      <code>
        $HOME/.pm2/logs/<app name>-out-<pid>.log
      </code>
    </td>
  </tr>
</tbody>
</table>

<sup>
<span>

1

</span>
</sup>

 Redis is required in case of multiple instances.

These environment variables only exist when you're using the official Docker Container, or are using the provided [`ecosystem.config.cjs`](https://github.com/directus/directus/blob/main/ecosystem.config.cjs) file with `pm2` directly.
