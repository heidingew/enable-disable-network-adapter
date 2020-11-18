# enable-disable-network-adapter
 Enable and/or disable Wi-Fi and Ethernet network adapters on Windows 10 with python

## Explanation
The goal of this is to change between network adapters easily without having to
do it manually every time

The [subprocess module](https://docs.python.org/3/library/subprocess.html) is used
to check whether the network adapters are enabled or disabled by allowing us to run
command prompt(cmd) commands inside the program

## Commands
1. To identify the name of the adapters you want to enable or disabled
    `netsh interfce show interface`
2. To disable the Wi-Fi or Ethernet adapter
    `netsh interface set interface "ADAPTER-NAME" disable`
    - replace `disable` with `enable` if you want to enable the adapter


## Steps
1. Fork the directory and change the adapter names in the `main.py` file
    - If you happen to have the same adapter name and our intensions match,
        you just need to run the main.exe file
2. You can run this using command `python main.py`
3. Alternatively, you may want to convert the python script to .exe file

    **a.** Install the `pyinstaller` library using command `pip install pyinstaller`

    **b.** Go into the directory where the `main.py` file is located

    **c.** Right click on any empty space and click on `Open PowerShell window here`

    **d.** Type `pyinstaller --onefile main.py` in the PowerShell Window and press Enter

    **e.** In the same directory, you can find your main.exe file in the `dist` folder

    **f.** To run the file, right-click `main.exe` and Run as Administrator



  > **Note:** Steps above requires you to have Python installed on your machine
