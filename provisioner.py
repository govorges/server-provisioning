from hcloud import Client
from hcloud.floating_ips.client import BoundFloatingIP

from hcloud.locations.client import BoundLocation
from hcloud.locations.domain import Location

from hcloud.datacenters.domain import Datacenter
from hcloud.datacenters.client import BoundDatacenter



from dotenv import load_dotenv
from os import environ

from configurations._loading import ListServerConfigurations, GetConfigurationByName, Configuration

load_dotenv()
assert environ.get('CLIENT_TOKEN') is not None, \
    "CLIENT_TOKEN was not set in the environment."
CLIENT_TOKEN = environ['CLIENT_TOKEN']

client = Client(token = CLIENT_TOKEN, application_name = "server-provisioning.provisioner")

def DeployInstance(name: str, location: Location, configuration: Configuration, labels: dict = None):
    """Deploys a Hetzner VM instance with the provided configuration."""
    configuration_data = configuration.__dict__.copy()
    configuration_data.pop('_name')

    creation_response = client.servers.create(
        name=name, **configuration_data, location=location, labels=labels
    )
    return creation_response

if __name__ == "__main__":
    locations: list[BoundLocation] = client.locations.get_all()
    print([f"{loc.id}: {loc.name}" for loc in locations])

    config = GetConfigurationByName("configurations.example")
    assert config is not None, \
        "No configuration with the provided name was found."
    
    response = DeployInstance(
        name = "cpx11-docker-ce-test-0",
        location = Location(id=4),
        configuration = config
    )
    print(response.server)
    