# Nomic Documentation

Source: https://docs.nomic.ai/platform/datasets/data-maps/guides/mapping-github-commits-with-atlas

In this cookbook, we show how to automate the extraction, processing, and mapping of GitHub commits using Python and Nomic Atlas. You can also view this cookbook on our github.

We'll clone a GitHub repository, extract commit messages, and leverage Nomic Atlas to produce map of metadata, including the author, email, and timestamp of each commit message.

## Getting Started​

The above data map represents the history of the Linux Kernel, one of the largest GitHub repositories known with over one million commits (as of June 2024).

Exploring the dataset you can discover trends and patterns in the commit history. Filtering by timestamp, you can view commit messages from the designated timeframe, even as far back as 2005. This allows you to see how the type of kernel work being worked on changed semantically over time. Surprisingly, there are very few mentions of bug fixes but quite a few about legal compliance.

### Mapping your own Github repository​

On a high level, this cookbook code works as follows:

- Input any GitHub repository as directed by the terminal formatted https://github.com/USER/REPONAME
- It clones the repository to retrieve the commit history locally
- Either create a CSV file from it or directly load the commit history into an AtlasDataset
- Finally, use the Nomic Atlas python sdk to create a data map over the commit message column of the dataset.
### Cloning repository​

The first step is to clone the GitHub repository locally.

```
import osimport subprocessdef clone_repo(repo_url, repo_path):  #Ensures that the repository has not been cloned previously    if not os.path.exists(repo_path):        subprocess.run(['git', 'clone', '--mirror', repo_url, repo_path])    else:        subprocess.run(['git', '-C', repo_path, 'fetch', '--all'])
```

### Extracting commit messages​

The next step is to extract the commit messages and metadata from the cloned repo. In this step the datetime library will be use to format the timestamp so it can be filtered when the map is created on Atlas. To extract the commit details "git log" is used

```
from datetime import datetimeimport subprocessdef fetch_commits_from_local_repo(repo_path):    commit_list = []    result = subprocess.run(        ['git', '-C', repo_path, 'log', '--format=%H;%an;%ae;%ad;%s'],        capture_output=True,        text=True,        encoding='utf8',        errors='replace'    )    #Splits commit messages    commits = result.stdout.strip().split('\n')    for i, commit in enumerate(commits, start=1):        try:            hash, author, email, date, message = commit.split(';', 4)            date_obj = datetime.strptime(date, '%a %b %d %H:%M:%S %Y %z')            formatted_date = date_obj.strftime('%Y-%m-%d')            #Appends the formatted data to the list            commit_list.append({                'id': i,                'hash': hash,                'author': author,                'email': email,                'date': formatted_date,                'message': message            })        except ValueError as e:          #Skips any commits that may have an error            print(f"ValueError occurred on commit {i}: {e}. Skipping this commit.")    return commit_list
```

### Saving repository as CSV​

This part saves the commits extracted into a csv (comma-separated-values) file to be able to see the data in case there is a problem communicating the data between the code and Atlas

```
import csvdef save_commits_to_csv(commits, csv_filename):    #Opens csv file    with open(csv_filename, 'w', newline='', encoding='utf-8') as csvfile:        #Defines column names in the csv file        fieldnames = ['id', 'hash', 'author', 'email', 'date', 'message']        #Creates a DictWriter object with the csv file and the field names        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)        #Writes the column names to the csv file        writer.writeheader()        #Writes each commit to the csv file        for commit in commits:            writer.writerow(commit)
```

## Creating a map using atlas​

Now, it is time to make the map on Nomic Atlas. However, before that it is necessary to set up your Nomic Atlas API Token by first getting it and then logging in with it

```
# --upgrade updates the nomic library specifically to ensure it is up-to-datepip install --upgrade nomic
```

```
# Get your API tokennomic login
```

```
# Login with your API tokennomic login MY_API_TOKEN_HERE
```

Two functions are provided to create an Atlas map. The first function creates a map directly from the csv file and then the second function creates a csv file along with the map for debugging.

```
# Creates map from a list of commitsdef create_commit_map_from_commits(commits, map_name):        # Checks if there are any commits    if not commits:        raise ValueError("No commits found.")        # Create an AtlasDataset with the given map name    dataset = AtlasDataset(map_name)        # Adds the commit data to the dataset    dataset.add_data(commits)        # Create a map for the dataset    atlas_map = dataset.create_index(        indexed_field='message',    )    return atlas_map#Creates map from a CSV filedef create_commit_map_from_csv(csv_filename, map_name):    data = []    #Opens the CSV file for reading    with open(csv_filename, newline='', encoding='utf-8') as csvfile:        reader = csv.DictReader(csvfile)        #Read each row of the CSV file into the data list        for row in reader:            data.append(row)    #Check if there is any data in the CSV file    if not data:        raise ValueError("No data found in CSV file.")    #Create an AtlasDataset with the given map name    dataset = AtlasDataset(map_name)    #Add the data from the CSV file to the dataset    dataset.add_data(data)    #Create a map for the dataset    atlas_map = dataset.create_index(        indexed_field='message',    )    return atlas_map
```

## Bringing it all together​

Finally, the driver code. This prompts the user to enter the GitHub repository URL and decide whether to save commits to a CSV file. It then processes the repositories, fetches commits, and creates a commit map. It combines everything done in the previous sections to ultimately create the dataset and map.

```
if __name__ == "__main__":    #Prompts the user to enter GitHub repository URLs    repo_urls = input("Enter GitHub Repository URLs separated by commas: ").split(',')    #Prompts the user to decide whether to save commits to a CSV file    save_to_csv = input("Do you want to save commits to CSV? (yes/no): ").strip().lower() == 'yes'    all_commits = []    repo_names = []    #Creates a temporary directory    with tempfile.TemporaryDirectory() as temp_dir:        for repo_url in repo_urls:            #Extracts the repository name from the URL            repo_name = repo_url.rstrip('/').split('/')[-1].strip()            repo_names.append(repo_name)            repo_path = os.path.join(temp_dir, repo_name)            #Clones the repository and fetchs commits            clone_repo(repo_url.strip(), repo_path)            commits = fetch_commits_from_local_repo(repo_path)            #Appends fetched commits to the list            if commits:                all_commits.extend(commits)        #Checks if there are any commits        if all_commits:            #Combines repository names for the map name            combined_repo_names = '_'.join(repo_names)            if save_to_csv:                #Saves the commits to a CSV file                csv_filename = os.path.join(temp_dir, f"{combined_repo_names}_commits.csv")                save_commits_to_csv(all_commits, csv_filename)                print(f"Combined commits have been saved to {csv_filename}")                map_name = os.path.splitext(os.path.basename(csv_filename))[0]                try:                    #Creates a commit map from the CSV file                    commit_map = create_commit_map_from_csv(csv_filename, map_name)                    print(f"Commit map '{map_name}' has been created")                except ValueError as e:                    print(f"Error creating commit map: {e}")            else:                #Creates a commit map from the list of commits                map_name = combined_repo_names                try:                    commit_map = create_commit_map_from_commits(all_commits, map_name)                    print(f"Commit map '{map_name}' has been created")                except ValueError as e:                    print(f"Error creating commit map: {e}")        else:            print("No commits were found for the provided repositories.")
```

## Exploring your map​

After running the script, your commit map will be created in your Nomic Atlas account with the name of the GitHub Repository name that was inputted. Additionally, there is a link that will be outputted in the terminal which directs you to the created map.

Note: Maps for larger amounts of data rows (commits) take more time. Anticipate ~15 minutes for a repository with around 100k commits and ~40 minutes for the Linux Kernel. You will get an email once the map has been built over your dataset!

- Getting StartedMapping your own Github repositoryCloning repositoryExtracting commit messagesSaving repository as CSV
- Mapping your own Github repository
- Cloning repository
- Extracting commit messages
- Saving repository as CSV
- Creating a map using atlas
- Bringing it all together
- Exploring your map
