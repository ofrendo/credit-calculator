# credit-calculator

- [credit-calculator](#credit-calculator)
  - [Preparing Python](#preparing-python)
  - [Installation](#installation)
  - [Run tests](#run-tests)
  - [Run script](#run-script)


## Preparing Python
See [documentation](https://computingforgeeks.com/how-to-install-python-on-ubuntu-linux-system/)
```
sudo apt install software-properties-common -y
sudo add-apt-repository ppa:deadsnakes/ppa
sudo apt install python3.9
sudo apt install python3.9-distutils
```

## Installation

```
poetry install
```

## Run tests
```
make test
```

## Run script

```
poetry run python credit_calculator/main.py
```
