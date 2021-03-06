
ICON CLI tool
========

 ICON supports Command Line Interface(CLI interface) for 3rd party or user services development. With this single tool, you can control all ICON functions and automate them using scripts.

<!-- TOC depthFrom:1 depthTo:3 withLinks:1 updateOnSave:1 orderedList:0 -->

- [Prerequisite](#prerequisite)
- [Version](#version)
- [Glossary](#glossary)
- [Technical information](#technical-information)
- [Getting started](#getting-started)
	- [Installation](#installation)
	- [Run CLI](#run-cli)
	- [Console instructions](#console-instructions)
	- [Wallet operation](#wallet-operation)
		- [Create wallet file](#create-wallet-file)
		- [Show wallet information](#show-wallet-information)
		- [List up all assets in current wallet](#list-up-all-assets-in-current-wallet)
		- [Transfer the value to the specific address with the fee.](#transfer-the-value-to-the-specific-address-with-the-fee)

<!-- /TOC -->


# Prerequisite

You need Python 3.6 or later to run icxcli. You can have multiple Python versions (2.x and 3.x) installed on the same system without problems.

On macOS(Sierra and after) and Ubuntu 16.04, for example, the necessary packages are:

- automake
- pkg-config
- virtualenv
- autoconf
- libtool

In Ubuntu 16.04, you can install Python 3.6.

    $ sudo add-apt-repository ppa:jonathonf/python-3.6
    $ sudo apt update
    $ sudo apt install python3.6
    $ sudo apt install python3.6-dev
    $ sudo apt install virtualenv
    $ virtualenv -p python3.6 .venv

You can install pip3 for python 3.6 like this:

    $ wget https://bootstrap.pypa.io/get-pip.py
    $ sudo python3.6 get-pip.py

You can install autoconf, libtool and automake for python3.6.

    $ sudo apt install autoconf libtool automake



# Version

- 0.0.4



# Glossary

- Address of wallet: Unique string to identify the address to transfer value. It prefixed with 'hx'.
- Private key: A tiny bit of code that is paired with a public key to set off algorithms to encrypt and decrypt a text for the specific address.
- Public key: Long alphanumeric characters that is used to encrypt data (message).



# Technical information

## Private key, public key and wallet address

There are five steps to get from  private->public -> address:

1. Generate a private key.
2. Derive a public key from the private key.
3. H1 = sha3_256( Public key)  => 32 byte
4. BitAddress = last 20 bytes of H1
5. Address = hx || HexString(BitAddress)
ex) hxaa688d74eb5f98b577883ca203535d2aa4f0838c

## Tested platform

We tested on window and macOS. If you find some problems on window, please send the report of the problems.



# Getting started

## Installation

The easiest way to install icxcli* is to use pip:

    $ pip install icxcli

or, if you are not installing in a virtualenv:

    $ sudo pip install icxcli

If you have the aws-cli installed and want to upgrade to the latest version you can run:

    $ pip install --upgrade icxcli

## Run CLI

Run command icli in the command line.  There are many sub commands like wallet create, wallet show, asset list, transfer for ICX service. You can get the help page by adding the command help.

    $ icli  --help
    usage:
            Normal commands:
                version
                help

            Wallet Commands:

                wallet create <file path> -p <password>
                wallet show <file path> -p <password>    | -n <network : mainnet | testnet | IP or domain>
                asset list <file path> -p <password>     | -n <network : mainnet | testnet | IP or domain>
                transfer <to> <amount> <file path> -p <password> -f <fee=10000000000000000> | -n  <network : mainnet | testnet | IP or domain>

            WARNING:

                Fee feature is the experimental feature; fee is fixed to 10000000000000000 loop for now so if you
                try to make a transaction with the modified fee, which is not 10000000000000000 loop, then you would
                not be able to make the transaction. you will be notified
                when it is possible to make a transaction with the modified fee.

            IF YOU MISS -n, icli WILL USE TESTNET.


    positional arguments:
      command           wallet create, wallet show, asset list, transfer

    optional arguments:
      -h, --help		show this help message and exit
      -p PASSWORD		password
      -f FEE		transaction fee
      -n NETWORK		mainnet or testnet or other IP or domain


## Console instructions

<table>
  <tr>
    <td>Command</td>
    <td>Function description</td>
  </tr>
  <tr>
    <td>version</td>
    <td>Shows the current software version. </td>
  </tr>
  <tr>
    <td>help</td>
    <td>Shows Help menu</td>
  </tr>
</table>



## Wallet operation

<table>
  <tr>
    <td>Command</td>
    <td>Function description</td>
  </tr>
  <tr>
    <td>wallet create &lt;file path&gt; -p &lt;password&gt;</td>
    <td>Create a wallet file.</td>
  </tr>
  <tr>
    <td>wallet show &lt;file path&gt; -p &lt;password&gt; -n &lt;network&gt;
</td>
    <td>Show current wallet information.</td>
  </tr>
  <tr>
    <td>asset list &lt;file path&gt; -p &lt;password&gt; -n &lt;network&gt;</td>
    <td>Enumerate the asset in the wallet. (ICX, ICX token) </td>
  </tr>
  <tr>
    <td>transfer &lt;to&gt; &lt;amount&gt; &lt;file path&gt; -p &lt;password&gt; -f &lt;fee&gt; -n &lt;network&gt;
</td>
    <td>Transfer the value to the specific address with the fee. </td>
  </tr>
</table>

### WARNING

Fee feature is the experimental feature; **fee is fixed to 10000000000000000 loop for now** so if you try to make a transaction with the modified fee, which is not 10000000000000000 loop, then you would not be able to make the transaction. you will be notified when it is possible to make a transaction with the modified fee.



## Create wallet file

    $ icli wallet create <file path> -p <password>

Create a wallet file with given wallet name, password and file path.

### Arguments

- file path : File path for the keystore file of the wallet.
- password: Password including alphabet character, number, and  special character. If the user doesn’t give password with -p, then CLI will show the prompt and user need to type the password.

### Output

#### Successful case

Return 0 : Succeed to generate the keystore file for the wallet.

#### Error cases

**icli** will return following error code and message.

- Return 121: The file path is without a file name.
- Return 122: The file path is wrong.
- Return 123: The password is wrong.
- Return 124: The keystore file has already existed.
- Return 136: User doesn't have a permission to write the file.



## Show wallet information

    $ icli wallet show <file path> -p <password> -n <network>

Show wallet information.

### Arguments

- file path: File path for the keystore file of the wallet.
- password: Password including alphabet character, number, and  special character. If the user doesn’t give password with -p, then CLI will show the prompt and user need to type the password.
- network: 'testnet' or 'mainnet' or other IP or domain address.

### Output

Shows the all information of wallet.

- Wallet address
- Current balance
- Keystore file contents

#### Successful case

Return 0 : Print out wallet information including asset list.

#### Error cases

- Return 122: The file path is wrong.
- Return 123: The password is wrong.
- Return 126: The network is invalid.
- Return 133: The file is not a key store file.



## List up all assets in current wallet

    $ icli asset list <file path> -p <password> -n <network>

 Enumerate the list of all the assets of the wallet.

### Arguments

- file path : File path for the keystore file of the wallet.
- password: Password including alphabet character, number, and  special character. If the user doesn’t give password with -p, then CLI will show the prompt and user need to type the password.
- network: 'testnet' or 'mainnet' or other IP or domain address.

### Output

- List of all assets in current wallet.

#### Successful case

- Return 0 : Succeed to display.

#### Error cases

- Return 122: The file path is wrong.
- Return 123: The password is wrong.
- Return 126: The network is invalid.
- Return 133: The file is not a key store file.



## Transfer the value to the specific address with the fee.

    $ icli transfer <to> <amount> <file path> -p <password> -f <fee> -n <network>

Transfer the value from  A address to B address with the fee.

### Arguments

- to: Address of wallet to receive the asset.
- file path : File path for the keystore file of the wallet.
- password:  Password including alphabet character, number, and  special character. If the user doesn’t give password with -p, then CLI will show the prompt and user need to type the password.
- amount : Amount of money. (Unit:loop)
- fee : Transfer fee (Unit:loop)
    - **YOU SHOULD CHANGE BOTH THE UNIT OF AMOUNT AND FEE TO LOOP, ENTERING INTEGER VALUES FOR AMOUNT AND FEE NOT FLOATING NUMBERS.**
        - Unit: loop
            - Ex) 1 icx = 10<sup>18</sup> loop
- network: 'testnet' or 'mainnet' or other IP or domain address.

### Output

#### Successful case

Return 0 : Succeed to transfer

#### Error cases

**icli** will return following error code and message.

- Return 122: The file path is wrong.
- Return 123: The password is wrong.
- Return 126: The network is invalid.
- Return 127: The wallet doesn't have enough balance.
- Return 128: The fee is invalid.
- Return 130: The wallet address is wrong.
- Return 133: The file is not a key store file.
- Return 135: The amount is not integer values.


