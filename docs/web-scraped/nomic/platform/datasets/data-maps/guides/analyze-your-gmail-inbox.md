# Nomic Documentation

Source: https://docs.nomic.ai/platform/datasets/data-maps/guides/analyze-your-gmail-inbox

Atlas makes it easy to organize and understand all the emails in your inbox. With Atlas, you have an interactive data map of your emails grouped into labeled clusters for you to explore. You can also ask the Analyst questions and have it query your data to give you an explainable answer.

Your browser does not support the video tag.

In this guide, we show you how to make a map like this of your Gmail inbox.

For data privacy and security, we recommend only uploading email data to Atlas on Business or Enterprise plans which include private datasets. This ensures your email data remains private and accessible only to authorized users in your organization.

## Download Gmail Inbox​

We recommend exporting your Gmail inbox using Google Takeout. Google Takeout can export your Gmail inbox data as an .mbox file which we can preprocess and send to Atlas.

```
.mbox
```

To download your inbox, go to Google Takeout, create a new export for Mail, and configure your download link to send your export to your preferred destination (e.g. Gmail, Google Drive, etc).

You should receive a .zip or .tgz file which, when unzipped, contains an .mbox file.

```
.zip
```

```
.tgz
```

```
.mbox
```

## Parse Inbox Data​

We use the email and mailbox native Python libraries to parse the .mbox file into text, as well as the BeautifulSoup and pandas libraries for converting the extracted text into a DataFrame.

```
email
```

```
mailbox
```

```
.mbox
```

```
BeautifulSoup
```

```
pandas
```

```
!pip install -q beautifulsoup4 pandas
```

```
from bs4 import BeautifulSoupfrom datetime import datetimeimport emailfrom email.header import decode_headerimport mailboximport pandas as pdimport redef decode_field(field):    """Decode email header field."""    if field is None:        return ""    decoded_parts = []    for part, encoding in decode_header(field):        if isinstance(part, bytes):            if encoding:                try:                    decoded_parts.append(part.decode(encoding))                except:                    decoded_parts.append(part.decode('utf-8', errors='replace'))            else:                decoded_parts.append(part.decode('utf-8', errors='replace'))        else:            decoded_parts.append(part)    return ' '.join(decoded_parts)def extract_body(message):    """Extract the body from the email message."""    body = ""    if message.is_multipart():        for part in message.walk():            content_type = part.get_content_type()            content_disposition = str(part.get("Content-Disposition"))            if "attachment" in content_disposition:                continue            if content_type == "text/plain":                try:                    payload = part.get_payload(decode=True)                    charset = part.get_content_charset() or 'utf-8'                    body = payload.decode(charset, errors='replace')                    break  # Use first text/plain part                except:                    continue            elif content_type == "text/html" and not body:                try:                    payload = part.get_payload(decode=True)                    charset = part.get_content_charset() or 'utf-8'                    html_body = payload.decode(charset, errors='replace')                    soup = BeautifulSoup(html_body, 'html.parser')                    body = soup.get_text(separator=' ', strip=True)                except:                    continue    else:        content_type = message.get_content_type()        if content_type == "text/plain":            try:                payload = message.get_payload(decode=True)                charset = message.get_content_charset() or 'utf-8'                body = payload.decode(charset, errors='replace')            except:                body = message.get_payload()        elif content_type == "text/html":            try:                payload = message.get_payload(decode=True)                charset = message.get_content_charset() or 'utf-8'                html_body = payload.decode(charset, errors='replace')                soup = BeautifulSoup(html_body, 'html.parser')                body = soup.get_text(separator=' ', strip=True)            except:                body = message.get_payload()    return bodydef parse_mbox(mbox_file):    """Parse mbox file and return a DataFrame of emails."""    data = []    mbox = mailbox.mbox(mbox_file)    for message in mbox:        subject = decode_field(message['subject'])        from_address = decode_field(message['from'])        to_address = decode_field(message['to'])        date_str = message['date']        date = None        if date_str:            try:                date = email.utils.parsedate_to_datetime(date_str).isoformat()            except:                if message['received']:                    try:                        received = message['received']                        date_match = re.search(r'\d+\s+\w+\s+\d{4}\s+\d{2}:\d{2}:\d{2}', received)                        if date_match:                            date = datetime.strptime(date_match.group(0), '%d %b %Y %H:%M:%S').isoformat()                    except:                        pass        message_id = message['message-id']        thread_id = message.get('X-GM-THRID', None)        if not thread_id: # As a fallback, use References or In-Reply-To            thread_id = message.get('References', message.get('In-Reply-To', message_id))        body = extract_body(message)        labels_str = message.get('X-Gmail-Labels', '')        label_dict = {            'Inbox': False,             'Important': False,             'Opened': False,             'Unread': False,             'Archived': False,             'Trash': False,             'Spam': False,            'Category_Updates': False,            'Category_Personal': False,            'Category_Promotions': False,            'Category_Forums': False,            'Category_Purchases': False,            'IMAP_Forwarded': False        }        if labels_str:            labels = labels_str.split(',')            for label in labels:                label = label.strip()                if 'Category' in label:                    category = label.replace('Category ', 'Category_').strip()                    if category in label_dict:                        label_dict[category] = True                elif 'IMAP_$Forwarded' in label or 'IMAP_Forwarded' in label:                    label_dict['IMAP_Forwarded'] = True                elif label in label_dict:                    label_dict[label] = True        data.append({            'message_id': message_id,            'thread_id': thread_id,            'date': date,            'from': from_address,            'to': to_address,            'subject': subject,            'body': body,            **label_dict        })    return pd.DataFrame(data)
```

Now parse the .mbox file into a dataframe using the helper function defined above, and prepare the dataframe for Nomic Atlas.

```
.mbox
```

```
mbox_filepath = "/path/to/your/Takeout/Mail/gmail.mbox"email_df = parse_mbox(mbox_filepath)for c in email_df.columns:    if email_df[c].dtype == bool:        email_df[c] = email_df[c].astype(str)
```

```
email_df
```

## Upload Data to Nomic Atlas​

Once you have your emails in a dataframe with the features you want to include, you can create a new dataset in Atlas and upload your data to the platform for visualization and analysis. Make sure you have the Nomic Python SDK installed and that you login with your Nomic API Key.

```
!pip install -q nomic
```

```
!nomic login nk-...
```

Create Atlas Dataset

```
from nomic import AtlasDatasetdataset_identifier = "gmail-inbox" # to create the dataset in the organization connected to your Nomic API key# dataset_identifier = "<ORG_NAME>/gmail-inbox" # to create the dataset in other organizations you are a member ofatlas_dataset = AtlasDataset(dataset_identifier)
```

Add Data

```
add_data_result = atlas_dataset.add_data(email_df)
```

Build Data Map

We use the body column from email_df to create embeddings for Atlas. This means that emails with similar text language in the body will cluster together in your map. Additionally, you can perform vector search over the text you choose as your indexed_field.

```
body
```

```
email_df
```

```
body
```

```
indexed_field
```

```
atlas_map = atlas_dataset.create_index(indexed_field="body")
```

## Visit Your Map​

Your map will live in your Platform Dashboard. Once it is done building, you can open it and explore it using the Analyst and the data map controls.

- Download Gmail Inbox
- Parse Inbox Data
- Upload Data to Nomic Atlas
- Visit Your Map
