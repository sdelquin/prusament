# prusament

Available stock of prusament filaments at tinermaq.com

![Prusament Galaxy Silver](galaxy.jpg)

## Motivation

I love [Prusament](https://prusament.com/) filaments but it's not easy to find them in physical shops here in Tenerife (Canary Islands). There is one shop which brings some of them from time to time though: [Tinermaq](<[https://](https://tinermaq.com/blog/categoria-producto/filamento/prusament/)>).

I developed this project in order to be notified when new filaments are available.

## Setup

Create a Python virtualenv and install requirements:

```console
$ python3.10 -m venv venv
$ source venv/bin/activate
$ pip install -r requirements.txt
```

Optionally, you can create a `.env` file in the working directory to overwrite settings from [settings.py](settings.py).

## Usage

```console
$ python main.py --help
Usage: main.py [OPTIONS] COMMAND [ARGS]...

Options:
  --help  Show this message and exit.

Commands:
  list    List available prusament filaments at Tinermaq.
  notify  Notify available prusament filaments at Tinermaq.
  save    Save available prusament filaments at Tinermaq.
```

### List

List available prusament filaments at Tinermaq.

```console
$ python main.py list --help
Usage: main.py list [OPTIONS]

  List available prusament filaments at Tinermaq.

Options:
  -q, --quiet    Run in quite mode.
  -u, --updates  List filament updates.
  --help         Show this message and exit.
```

### Notify

Notify available prusament filaments at Tinermaq.

```console
$ python main.py notify --help
Usage: main.py notify [OPTIONS]

  Notify available prusament filaments at Tinermaq.

Options:
  -u, --updates  Notify filament updates.
  --help         Show this message and exit.
```

### Save

Save available prusament filaments at Tinermaq.

```console
$ python main.py save --help
Usage: main.py save [OPTIONS]

  Save available prusament filaments at Tinermaq.

Options:
  --help  Show this message and exit.
```
