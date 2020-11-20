# Python Enable/Disable network adapter

# Import Useful modules
import subprocess
import click
from user_admin import is_user_admin


@click.command(no_args_is_help=True)
@click.option('--adapters', is_flag=True, help='View list of WLAN profiles stored on the PC.')
@click.option('-e', '--enable', help='Adapter name to be enabled.')
@click.option('-d', '--disable', help='Adapter name to be disabled.')


# type: (bool, str, str) -> None
def change_adapter_options(adapters, enable, disable):
    if adapters:
        show_adapters()
    if enable:
        if not is_user_admin():
            click.echo(click.style("The requested operation requires elevation (Run as administrator).", fg='red'))
        else:
            toggle_network_adapter(enable, "enable")
            click.echo("Enabled %s" % enable)
    if disable:
        if not is_user_admin():
            click.echo(click.style("The requested operation requires elevation (Run as administrator).", fg='red'))
        else:
            toggle_network_adapter(disable, "disable")
            click.echo("Disabled %s" % disable)

# @change_adapter_options()

# Function to list WLAN profiles store on the PC
# type: () -> None
def show_adapters():
    data = subprocess.check_output(['netsh', 'interface', 'show', 'interface']).decode('utf-8').split('\n')
    for i in data:
        click.echo(i)


# Function to enable/disable the network adapter
# type: (str, str) -> None
def toggle_network_adapter(adapter, toggle):
    subprocess.call(["netsh", "interface", "set", "interface", adapter, toggle])


# Driver Program
if __name__ == "__main__":
    change_adapter_options()
