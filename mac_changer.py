#!/usr/bin/env python

import subprocess
import click
import re


@click.command()
@click.option('-i', '--interface', prompt='Interface')
@click.option('-m', '--mac', prompt='MAC address')
def current_mac(interface, mac):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)

    if mac_address_search_result:
        print(mac_address_search_result.group(0))
        change_mac(interface, mac)
    else:
        print("Could not read MAC")


def change_mac(interface, new_mac):
    print("Changing MAC for " + interface + " to " + new_mac)
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])


if __name__ == '__main__':
    current_mac()
