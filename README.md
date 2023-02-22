<div align="center">

# 📖 OntoGPT API

</div>

An API to extract informations from text using [OntoGPT](https://github.com/monarch-initiative/ontogpt)

## 🧑‍💻 Development setup

The final section of the README is for if you want to run the package in development, and get involved by making a code contribution.


### 📥️ Clone

Clone the repository:

```bash
git clone https://github.com/vemonet/ontogpt-api
cd ontogpt-api
```
### 🐣 Install dependencies

Install [Hatch](https://hatch.pypa.io), this will automatically handle virtual environments and make sure all dependencies are installed when you run a script in the project:

```bash
pip install --upgrade hatch
```

Install the dependencies in a local virtual environment:

```bash
hatch -v env create
```

Create a `.env` file with your BioPortal and OpenAI API keys:

```bash
BIOPORTAL_APIKEY=XXX
OPENAI_APIKEY=XXX
```

###  🚀 Run the API

```bash
hatch run dev
```

### 🧹 Code formatting

The code will be automatically formatted when you commit your changes using `pre-commit`. But you can also run the script to format the code yourself:

```
hatch run fmt
```

Check the code for errors, and if it is in accordance with the PEP8 style guide, by running `flake8` and `mypy`:

```
hatch run check
```

### ♻️ Reset the environment

In case you are facing issues with dependencies not updating properly you can easily reset the virtual environment with:

```bash
hatch env prune
```

## 🐳 Deploy in production with docker

Create a `.env` file with your BioPortal and OpenAI API keys:

```bash
BIOPORTAL_APIKEY=XXX
OPENAI_APIKEY=XXX
```

Deploy with docker-compose:

```bash
docker-compose up
```

