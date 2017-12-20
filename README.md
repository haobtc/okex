# Okex Python Client

A Python client for the Okex API.

Most of the unauthenticated calls have been implemented.  It is planned to
implement the remainder of the API.

## Installation

    pip install okex


## Poll The Order Book

Run the ```okex-poll-orderbook``` script in a terminal.

Press ```Ctrl-c``` to exit.

    okex-poll-orderbook

## Setup

Install the libs

    pip install -r ./requirements.txt


## Usage

See the examples directory for samples.

e.g.

    PYTHONPATH=.:$PYTHONPATH python examples/basic.py


## Compatibility

This code has been tested on

- Python 2.7.10


## TODO

- Implement all API calls that Okex make available.

## Contributing

1. Create an issue and discuss.
1. Fork it.
1. Create a feature branch containing only your fix or feature.
1. Add tests!!!! Features or fixes that don't have good tests won't be accepted.
1. Create a pull request.

## References

- [https://www.okex.com/rest_api.html](https://www.okex.com/rest_api.html)

## Licence

The MIT License (MIT)

See [LICENSE.md](LICENSE.md)
