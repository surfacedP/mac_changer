#!/usr/bin/env python

import subprocess
import click
import re


@click.command()
@click.option('-i', '--interface', prompt='Input Interface:', help="Interface to change MAC address for")
@click.option('-m', '--mac', prompt='Input MAC address:', help="MAC address to change to for Interface")
def begin(interface, mac):
    get_mac(interface)
    change_mac(interface, mac)


def get_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))

    if mac_address_search_result:
        print(mac_address_search_result.group(0))
    else:
        print("Could not read MAC")


def change_mac(interface, new_mac):
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac])
    subprocess.call(["ifconfig", interface, "up"])
    get_mac(interface)


if __name__ == '__main__':
    begin()
