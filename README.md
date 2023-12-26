# Confluence Brain Dump
## Background
A simple application to add simple ideas using markdown to a Confluence page, retaining the previous information on the page. The input supports multi-line input.

**Note**: While multi-line support is provided, once moving to the next line the previous line cannot be edited.

## Authentication
The application requires an active [Atlassian personal API token](https://support.atlassian.com/atlassian-account/docs/manage-api-tokens-for-your-atlassian-account/). The token needs to be [Base64](https://en.wikipedia.org/wiki/Base64) encoded along with the username. On OSX the following step can be taken:

```shell
echo -n 'user@example.com:yourApiToken' | base64
```

More information on basic authentication headers and the Atlassian product REST APIs can be found [here](https://developer.atlassian.com/cloud/jira/platform/basic-auth-for-rest-apis/#supply-basic-auth-headers).

## Setup
Clone the repo to your environment, ensure that the modules from the `requirements.txt` file are present.

Setup the `config.json` file with the information for your own environment.

## Configuration
The file uses a JSON file called `config.json` to allow the user to provide the Atlassian Cloud URL, page id and the authorization token.

Please see the included `sample_config.json` file for examples, which currently has the following format:

```json
{
	"cloudUrl": "acme.atlassian.net",
	"pageId": "12345789",
	"token": "yourApiToken"
}
```
## Example
The script accepts markdown which is converted to HTML in order to build out the Confluence page.

An example to create a bulletpoint entry:

```shell
./confluence-brain-dump
This is an update for testing purposes:
- Don't forget to check the todo list on [Example site](https://example.com)
```

## Todo
The following are some items I'd like to improve the script with:

- [ ] Add `argparse` to be able to dynamically override config file
- [ ] Allow using text editors to create the markdown as opposed to inline editing
- [ ] When using argparse allow adding a direct comment negating the need for interactive mode
- [ ] Reconfigure the use of `Ctrl+x` to send the data
- [ ] Test the different markdown that can be transmitted in this way
- [ ] When multiple notes are added in a single day, append the existing entry as opposed to create a new one for the day
- [ ] Remove timestamp for the heading
- [ ] Consider JSON vs YAML for the config file
