# Source: https://plivo.com/docs/voice/use-cases/download-recordings.md

> ## Documentation Index
> Fetch the complete documentation index at: https://plivo.com/docs/llms.txt
> Use this file to discover all available pages before exploring further.

# Download Recordings

> Retrieve and download call recordings to local storage from Plivo

<Tabs>
  <Tab title="Node">
    ## Overview

    This guide shows how to retrieve recordings and download them to local storage. Plivo begins charging for stored recordings after 90 days. To avoid these charges, you can download recordings and store them elsewhere.

    ## Prerequisites

    To use Plivo APIs, follow our instructions to set up a Node development environment and a web server and safely expose that server to the internet.

    ## Download recordings to local storage

    Here’s sample code you can use to retrieve recordings to a local directory.

    ```js  theme={null}
    // Example script for downloading recording files

    var plivo = require('plivo');
    var axios = require('axios');
    var fs = require('fs');
    var path = require('path');

    const AUTH_ID = "<auth_id>";
    const AUTH_TOKEN = "<auth_token>";

    (function main() {
      'use strict';

      var client = new plivo.Client(AUTH_ID,AUTH_TOKEN);

      // Directory where the recordings will be saved
      var recordingsDir = path.join(__dirname, "recordings");

      if (!fs.existsSync(recordingsDir)) {
        fs.mkdirSync(recordingsDir, { recursive: true });
      }

      client.recordings.list(
        {
          add_time__gt: "2023-04-01 00:00:00",
          add_time__lt: "2023-04-30 00:00:00",
          offset: 0,
          limit: 5,
        },
      ).then(function (response) {
        console.log("Found " + response.length + " recordings.");

        response.forEach(recording => {
          var recording_url = recording.recordingUrl;
          var recording_id = recording.recordingId;
          var format = recording.recordingFormat;
          console.log("Downloading recording: " + recording_url);

          var output_file = path.join(recordingsDir, recording_id + "." + format);

          // Download the file
          axios({
            url: recording_url,
            method: 'GET',
            responseType: 'stream',
          }).then(function (response) {
            var fileStream = fs.createWriteStream(output_file);
            response.data.pipe(fileStream);
            fileStream.on('finish', function () {
              console.log("Downloaded file to: " + output_file);
            });
          }).catch(function (error) {
            console.log("Error downloading file: " + error.message);
          });
        });
      }, function (err) {
        console.error(err);
      });
    })();
    ```

    ## Delete recordings from Plivo storage

    You can delete a recording by using the <a href="/voice/api/recording#delete-a-recording">Delete a Recording API</a> and specifying a recording ID, which you can retrieve from <a href="/voice/api/recording#list-all-recordings">list all recordings API</a> or the HTTP callback details stored in your database. You can also delete recordings from the Voice <a href="https://cx.plivo.com/logs">Recordings</a> page of the Plivo console.
  </Tab>

  <Tab title="Ruby">
    ## Overview

    This guide shows how to retrieve recordings and download them to local storage. Plivo begins charging for stored recordings after 90 days. To avoid these charges, you can download recordings and store them elsewhere.

    ## Prerequisites

    To use Plivo APIs, follow our instructions to set up a Ruby development environment and a web server and safely expose that server to the internet.

    ## Download recordings to local storage

    Here’s sample code you can use to retrieve recordings to a local directory.

    ```rb  theme={null}
    #
    # Example script for downloading recording files
    #
    require 'rubygems'
    require 'plivo'
    require 'open-uri'
    require 'fileutils'

    include Plivo
    include Plivo::Exceptions

    AUTH_ID = "<auth_id>"
    AUTH_TOKEN = "<auth_token>"

    api = RestClient.new(AUTH_ID,AUTH_TOKEN)

    begin
      response = api.recordings.list(
        add_time__gt: "2023-04-01 00:00:00",
        add_time__lt: "2023-04-30 00:00:00",
        limit: 5,
        offset: 0
      )

      puts "Found #{response[:objects].length} recordings."

      response[:objects].each do |recording|
        recording_url = recording.recording_url
        recording_id = recording.recording_id
        format = recording.recording_format
        puts "Downloading recording: #{recording_url}"

        output_file = "recordings/#{recording_id}.#{format}"

        # Directory where the recordings will be saved
        FileUtils.mkdir_p 'recordings'

        begin
          # Download the file
          open(recording_url) do |file|
            File.open(output_file, "wb") do |output|
              output.write(file.read)
            end
          end
          puts "Downloaded file to: #{output_file}"
        rescue StandardError => e
          puts "Error downloading file: #{e.message}"
        end
      end

    rescue PlivoRESTError => e
      puts 'Exception: ' + e.message
    end
    ```

    ## Delete recordings from Plivo storage

    You can delete a recording by using the <a href="/voice/api/recording#delete-a-recording">Delete a Recording API</a> and specifying a recording ID, which you can retrieve from <a href="/voice/api/recording#list-all-recordings">list all recordings API</a> or the HTTP callback details stored in your database. You can also delete recordings from the Voice <a href="https://cx.plivo.com/logs">Recordings</a> page of the Plivo console.
  </Tab>

  <Tab title="Python">
    ## Overview

    This guide shows how to retrieve recordings and download them to local storage. Plivo begins charging for stored recordings after 90 days. To avoid these charges, you can download recordings and store them elsewhere.

    ## Prerequisites

    To use Plivo APIs, follow our instructions to set up a python development environment and a web server and safely expose that server to the internet.

    ## Download recordings to local storage

    Here’s sample code you can use to retrieve recordings to a local directory.

    ```py  theme={null}
    import plivo
    import requests
    import os

    AUTH_ID = "<auth_id>"
    AUTH_TOKEN = "<auth_token>"

    client = plivo.RestClient(AUTH_ID,AUTH_TOKEN)
    response = client.recordings.list(
        add_time__gt='2023-07-01 00:00:00',
        add_time__lt='2023-07-30 00:00:00',
        offset=0,
        limit=5,
    )

    print(f"Found {len(response)} recordings.")

    # Directory where the recordings will be saved
    path = 'recordings'
    os.makedirs(path, exist_ok=True)

    for i, recording in enumerate(response):
        url = recording['recording_url']
        print(f"Downloading recording: {url}")

        # Download the file
        r = requests.get(url)

        file_path = os.path.join(path, f'{recording["recording_id"]}.{recording["recording_format"]}')

        with open(file_path, 'wb') as f:
            f.write(r.content)

        print(f"Downloaded file to: {file_path}")
    ```

    ## Delete recordings from Plivo storage

    You can delete a recording by using the <a href="/voice/api/recording#delete-a-recording">Delete a Recording API</a> and specifying a recording ID, which you can retrieve from <a href="/voice/api/recording#list-all-recordings">list all recordings API</a> or the HTTP callback details stored in your database. You can also delete recordings from the Voice <a href="https://cx.plivo.com/logs">Recordings</a> page of the Plivo console.
  </Tab>

  <Tab title="PHP">
    ## Overview

    This guide shows how to retrieve recordings and download them to local storage. Plivo begins charging for stored recordings after 90 days. To avoid these charges, you can download recordings and store them elsewhere.

    ## Prerequisites

    To use Plivo APIs, follow our instructions to set up a PHP development environment and a web server and safely expose that server to the internet.

    ## Download recordings to local storage

    Here’s sample code you can use to retrieve recordings to a local directory.

    ```php  theme={null}
    <?php
    /**
     * Example script for downloading recording files
     */
    require '../../vendor/autoload.php';
    use Plivo\RestClient;
    use Plivo\Exceptions\PlivoRestException;
    use GuzzleHttp\Client;

    $AUTH_ID = "<auth_id>";
    $AUTH_TOKEN = "<auth_token>";

    $client = new RestClient($AUTH_ID,$AUTH_TOKEN);

    try {
        $response = $client->recordings->list(
            [
                'add_time__gt' => "2023-04-01 00:00:00",
                'add_time__lt' => "2023-04-30 00:00:00",
                'limit' => 5,
                'offset' => 0
            ]
        );

        echo "Found " . count($response->resources) . " recordings." . PHP_EOL;

        // Directory where the recordings will be saved
        $dir = "./recordings";

        if (!file_exists($dir)) {
            mkdir($dir, 0777, true);
        }

        $http = new Client();

        foreach ($response as $recording) {
            $recording_url = $recording->recordingUrl;
            $recording_id = $recording->recordingId;
            $format = $recording->recordingFormat;

            echo "Downloading recording: " . $recording_url . PHP_EOL;

            $output_file = $dir . "/" . $recording_id . "." . $format;

            // Download the file
            $http->get($recording_url, ['sink' => $output_file]);

            echo "Downloaded file to: " . $output_file . PHP_EOL;
        }
    }
    catch (PlivoRestException $ex) {
        print_r($ex);
    }
    ```

    ## Delete recordings from Plivo storage

    You can delete a recording by using the <a href="/voice/api/recording#delete-a-recording">Delete a Recording API</a> and specifying a recording ID, which you can retrieve from <a href="/voice/api/recording#list-all-recordings">list all recordings API</a> or the HTTP callback details stored in your database. You can also delete recordings from the Voice <a href="https://cx.plivo.com/logs">Recordings</a> page of the Plivo console.
  </Tab>

  <Tab title=".NET">
    ## Overview

    This guide shows how to retrieve recordings and download them to local storage. Plivo begins charging for stored recordings after 90 days. To avoid these charges, you can download recordings and store them elsewhere.

    ## Prerequisites

    To use Plivo APIs, follow our instructions to set up a .NET development environment and a web server and safely expose that server to the internet.

    ## Download recordings to local storage

    Here’s sample code you can use to retrieve recordings to a local directory.

    ```cs  theme={null}
    /**
     * Example script for downloading recording files
     */
    using System;
    using System.Collections.Generic;
    using Plivo;
    using Plivo.Exception;
    using System.IO;
    using System.Net.Http;
    using System.Threading.Tasks;

    namespace PlivoExamples
    {
        internal class Program
        {
            private const string AUTH_ID = "<auth_id>";
            private const string AUTH_TOKEN = "<auth_token>";
            public static async Task Main(string[] args)
            {
                var api = new PlivoApi(AUTH_ID,AUTH_TOKEN);
                try
                {
                    var response = api.Recording.List(
                        addTime_Gt: DateTime.Parse("2023-04-01 00:00:00"),
                        addTime_Lt: DateTime.Parse("2023-04-30 00:00:00"),
                        limit:5,
                        offset:0
                    );

                    Console.WriteLine($"Found {response.Objects.Count} recordings.");

                    // Directory where the recordings will be saved
                    string dir = "./recordings";

                    if (!Directory.Exists(dir))
                    {
                        Directory.CreateDirectory(dir);
                    }

                    foreach (var recording in response.Objects)
                    {
                        string recordingUrl = recording.RecordingUrl;
                        string recordingId = recording.RecordingId;
                        string format = recording.RecordingFormat;

                        Console.WriteLine("Downloading recording: " + recordingUrl);

                        string outputFilePath = Path.Combine(dir, recordingId + "." + format);

                        // Download the file
                        using (var httpClient = new HttpClient())
                        {
                            var fileBytes = await httpClient.GetByteArrayAsync(recordingUrl);
                            await File.WriteAllBytesAsync(outputFilePath, fileBytes);
                        }

                        Console.WriteLine("Downloaded file to: " + outputFilePath);
                    }
                }
                catch (PlivoRestException e)
                {
                    Console.WriteLine("Exception: " + e.Message);
                }
            }
        }
    }
    ```

    ## Delete recordings from Plivo storage

    You can delete a recording by using the <a href="/voice/api/recording#delete-a-recording">Delete a Recording API</a> and specifying a recording ID, which you can retrieve from <a href="/voice/api/recording#list-all-recordings">list all recordings API</a> or the HTTP callback details stored in your database. You can also delete recordings from the Voice <a href="https://cx.plivo.com/logs">Recordings</a> page of the Plivo console.
  </Tab>

  <Tab title="Java">
    ## Overview

    This guide shows how to retrieve recordings and download them to local storage. Plivo begins charging for stored recordings after 90 days. To avoid these charges, you can download recordings and store them elsewhere.

    ## Prerequisites

    To use Plivo APIs, follow our instructions to set up a Java development environment and a web server and safely expose that server to the internet.

    ## Download recordings to local storage

    Here’s sample code you can use to retrieve recordings to a local directory.

    ```java  theme={null}
    package com.plivo.examples;

    import com.plivo.api.Plivo;
    import com.plivo.api.exceptions.PlivoRestException;
    import com.plivo.api.exceptions.PlivoValidationException;
    import com.plivo.api.models.base.ListResponse;
    import com.plivo.api.models.recording.Recording;
    import com.plivo.api.util.PropertyFilter;
    import org.apache.commons.io.FileUtils;

    import java.io.File;
    import java.io.IOException;
    import java.net.URL;
    import java.text.ParseException;
    import java.text.SimpleDateFormat;
    import java.util.Date;

    /**
     * Example script for downloading recording files
     */
    public class DownloadRecordings {

      private static final String AUTH_ID = "<auth_id>";
      private static final String AUTH_TOKEN = "<auth_token>";

      public static void main(String[] args) {
        Plivo.init(AUTH_ID, AUTH_TOKEN);
        try {
          String greaterThan = "2023-04-01 00:00:00";
          String lessThan = "2023-04-30 00:00:00";
          SimpleDateFormat formatter = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
          Date greaterThanDate = formatter.parse(greaterThan);
          Date lessThanDate = formatter.parse(lessThan);

          ListResponse<Recording> response = Recording.lister().addTime(new PropertyFilter<Date>().greaterThan(greaterThanDate).lessThan(lessThanDate)).offset(0).limit(5).list();

          System.out.println("Found " + response.getObjects().size() + " recordings.");

          for (Recording recording : response.getObjects()) {
            String recordingURL = recording.getRecordingUrl();
            String recordingId = recording.getRecordingId();
            String format = recording.getRecordingFormat();

            System.out.println("Downloading recording: " + recordingURL);

            // Directory where the recordings will be saved
            File outputFile = new File("recordings/" + recordingId + "." + format);
            outputFile.getParentFile().mkdirs();

            try {
              // Download the file
              FileUtils.copyURLToFile(new URL(recordingURL), outputFile);
              System.out.println("Downloaded file to: " + outputFile.getPath());
            } catch (IOException e) {
              System.out.println("Error downloading file: " + e.getMessage());
            }
          }
        } catch (PlivoRestException | IOException e) {
          e.printStackTrace();
        } catch (PlivoValidationException e) {
          throw new RuntimeException(e);
        } catch (ParseException e) {
          throw new RuntimeException(e);
        }
      }
    }
    ```

    ## Delete recordings from Plivo storage

    You can delete a recording by using the <a href="/voice/api/recording#delete-a-recording">Delete a Recording API</a> and specifying a recording ID, which you can retrieve from <a href="/voice/api/recording#list-all-recordings">list all recordings API</a> or the HTTP callback details stored in your database. You can also delete recordings from the Voice <a href="https://cx.plivo.com/logs">Recordings</a> page of the Plivo console.
  </Tab>

  <Tab title="Go">
    ## Overview

    This guide shows how to retrieve recordings and download them to local storage. Plivo begins charging for stored recordings after 90 days. To avoid these charges, you can download recordings and store them elsewhere.

    ## Prerequisites

    To use Plivo APIs, follow our instructions to set up a go development environment and a web server and safely expose that server to the internet.

    ## Download recordings to local storage

    Here’s sample code you can use to retrieve recordings to a local directory.

    ```go  theme={null}
    // Example script for downloading recording files

    package main

    import (
    	"fmt"
    	"io"
    	"net/http"
    	"os"
    	"path/filepath"

    	"github.com/plivo/plivo-go/v7"
    )

    var (
    	AuthID    = "<auth_id>"
    	AuthToken = "<auth_token>"
    )

    func main() {
    	client, err := plivo.NewClient(AuthID, AuthToken, &plivo.ClientOptions{})
    	if err != nil {
    		fmt.Println("Error", err.Error())
    		return
    	}
    	response, err := client.Recordings.List(
    		plivo.RecordingListParams{
    			AddTimeGreaterThan: "2023-04-01 00:00:00",
    			AddTimeLessThan:    "2023-04-30 00:00:00",
    			Offset:             0,
    			Limit:              5,
    		},
    	)
    	if err != nil {
    		fmt.Println("Error", err.Error())
    		return
    	}

    	fmt.Printf("Found %d recordings.\n", len(response.Objects))

    	// Directory where the recordings will be saved
    	os.MkdirAll("recordings", os.ModePerm)

    	for _, recording := range response.Objects {
    		fmt.Println("Downloading recording: ", recording.RecordingURL)
    		filePath := filepath.Join("recordings", recording.RecordingID+recording.RecordingFormat)
    		err = downloadFile(filePath, recording.RecordingURL)
    		if err != nil {
    			fmt.Println("Error downloading file: ", err)
    		} else {
    			fmt.Println("Downloaded file to: ", filePath)
    		}
    	}
    }

    func downloadFile(filepath string, url string) error {
    	out, err := os.Create(filepath)
    	if err != nil {
    		return err
    	}
    	defer out.Close()

    	resp, err := http.Get(url)
    	if err != nil {
    		return err
    	}
    	defer resp.Body.Close()

    	_, err = io.Copy(out, resp.Body)
    	return err
    }
    ```

    ## Delete recordings from Plivo storage

    You can delete a recording by using the <a href="/voice/api/recording#delete-a-recording">Delete a Recording API</a> and specifying a recording ID, which you can retrieve from <a href="/voice/api/recording#list-all-recordings">list all recordings API</a> or the HTTP callback details stored in your database. You can also delete recordings from the Voice <a href="https://cx.plivo.com/logs">Recordings</a> page of the Plivo console.
  </Tab>
</Tabs>
