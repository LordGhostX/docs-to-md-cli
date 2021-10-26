# Docs To MD CLI

Welcome to the codebase for the Docs TO MD CLI.

A Command Line Interface(CLI) tool that converts Google Docs files to MarkDown

## Usage

### Publish your Google Docs file to the web

* Select "Publish to the web" tab found under the file menu as seen in the image below:

![publish_step_1](docs_publish_step_1.jpg)


* Click on the "Publish" button:

![publish_step_2](docs_publish_step_2.PNG)


* Copy the Google Docs publish link under the link tab :

![publish_step_3](docs_publish_step_3.PNG)


### Convert Google Docs to Markdown

```bash
$ python dtm.py <docs URL>
$ python dtm.py <docs URL> <local|docs>
```

### Converting Google Docs to MarkDown and Saving Images Locally

```bash
$ python dtm.py <docs URL> local
```

### Converting Google Docs to MarkDown and Saving Images on Google Servers

```bash
$ python dtm.py <docs URL> docs
```

## Author

* [LordGhostX](https://twitter.com/LordGhostX) - Everyone's Friendly Neighbourhood Ghost

## License

* MIT
