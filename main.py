# Python Enable/Disable network adapter

# Import Useful modules
import subprocess


# to list WLAN profiles store on the PC, type the following command in CMD
# netsh interface show interface


# Function to enable/disable the network adapter
def toggle_network_adapter(adapter, toggle):
    subprocess.call(["netsh", "interface", "set", "interface", adapter, toggle])


# Driver Program
if __name__ == "__main__":
    data = subprocess.check_output(['netsh', 'interface', 'show', 'interface']).decode('utf-8').split('\n')
    for i in data:
        if "Disabled" in i and "Wi-Fi 2" in i:
            toggle_network_adapter("Wi-Fi 2", "enable")
            print("Enabled Wi-Fi 2 network\n")
        elif "Enabled" in i and "Wi-Fi" in i and "Wi-Fi 2" not in i:
            toggle_network_adapter("Wi-Fi", "disable")
            print("Disabled Wi-Fi network\n")
