import datetime
import json
import markdown
import requests


# Read data from config file
with open('config.json') as config_file:
    config = json.load(config_file)

baseUrl = config['cloudUrl']
pageId = config['pageId']
auth = config['token']
apiUrl = 'https://' + baseUrl + '/wiki/api/v2/pages/'
queryParameter = '?body-format=storage'

header = {
    "Accept": "application/json",
    "Content-Type": "application/json",
    "Authorization": "Basic " + auth
    }

def getPage(url,pageid,query):
    getUrl = url + pageid + query
    response = requests.get(getUrl, headers=header)
    return json.loads(response.text)

def updatePage(url,pageid,payload):
    updateUrl = url + pageid
    response = requests.put(updateUrl, headers=header, data=payload)
    return response.status_code

# Loop to get multi line user input for payload
# Can accept markdown
print("Enter/Paste your content. Ctrl-C once done editing:")
contents = []
while True:
    try:
        line = input()
    except KeyboardInterrupt:
        break
    contents.append(markdown.markdown(line))

# Strip new line characters when user input is multiline otherwise these are submitted as
# escaped \n characters
contentsMarkdown = [x.replace('\n', '')  for x in contents]

# Get existing page content and information
getRequest = getPage(apiUrl, pageId, queryParameter)

# Store existing content as a variable
originalNotes = getRequest['body']['storage']['value'] #.split('<h1>Brain dump</h1>')
#originalNotes = originalNotes[1:-1] # Strip trailing double quote

# Set the header for the udate to the current timestamp formatted as 01-01-2023 00:00:00
now = datetime.datetime.now()
nowFormatted = now.strftime('%d-%m-%Y %H:%M:%S')
dateHeader = '<h2>' + nowFormatted + '</h2>'

contentsMarkdown.insert(0, dateHeader) # Prepend date header to list
contentsMarkdown.append(originalNotes) # Append the existing content pulled down from the page
contentsHtml = ''.join(contentsMarkdown) # Join the list

payload = json.dumps( {
    "id": getRequest['id'],
    "status": "current",
    "spaceId": getRequest['spaceId'],
    "parentId": getRequest['parentId'],
    "title": getRequest['title'],
    "version": {
        "number": getRequest['version']['number'] +1,
        "message": ""
    },
    "body": {
        "representation": "storage",
        "value": contentsHtml
        }
    } )
    
sendRequest = updatePage(apiUrl, pageId, payload)
print(sendRequest)
