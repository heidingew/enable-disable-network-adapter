# enable-disable-network-adapter
 Enable and/or disable Wi-Fi and Ethernet network adapters on Windows 10 with python

## Explanation
The goal of this is to change between network adapters easily without having to
do it manually every time

The [subprocess module](https://docs.python.org/3/library/subprocess.html) is used
to check whether the network adapters are enabled or disabled by allowing us to run
command prompt(cmd) commands inside the program

The [click module](https://click.palletsprojects.com/en/5.x/) is used to create the command line interface

## Commands using CMD
1. To identify the name of the adapters you want to enable or disabled
    `netsh interfce show interface`
2. To disable the Wi-Fi or Ethernet adapter
    `netsh interface set interface "ADAPTER-NAME" disable`
    - replace `disable` with `enable` if you want to enable the adapter


## Steps
1. Clone the repository and run `pip install .` to make the script callable from your command-line and run `enable-disable-network-adapter` to on check how to run
2. Alternatively, you can run this using command `python main.py`


  > **Note:** Steps above requires [run program as Administrator](https://www.howtogeek.com/194041/how-to-open-the-command-prompt-as-administrator-in-windows-8.1/)
