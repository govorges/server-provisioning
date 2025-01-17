from hcloud import Client
from hcloud.floating_ips.client import BoundFloatingIP

from dotenv import load_dotenv
from os import environ

load_dotenv()
assert environ.get('CLIENT_TOKEN') is not None, \
    "CLIENT_TOKEN was not set in the environment."
CLIENT_TOKEN = environ['CLIENT_TOKEN']

client = Client(token = CLIENT_TOKEN, application_name = "server-provisioning.provisioner")

floating_ip_addresses: list[BoundFloatingIP] = client.floating_ips.get_all()
print([address.ip for address in floating_ip_addresses])