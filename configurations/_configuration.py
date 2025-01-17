from hcloud.server_types import ServerType
from hcloud.server_types.client import BoundServerType

from hcloud.images import Image

from hcloud.ssh_keys.domain import SSHKey
from hcloud.ssh_keys.client import BoundSSHKey

from hcloud.volumes.domain import Volume
from hcloud.volumes.client import BoundVolume

from hcloud.firewalls.domain import Firewall
from hcloud.firewalls.client import BoundFirewall

from hcloud.networks.domain import Network
from hcloud.networks.client import BoundNetwork

from hcloud.locations.domain import Location
from hcloud.locations.client import BoundLocation

from hcloud.datacenters.domain import Datacenter
from hcloud.datacenters.client import BoundDatacenter

from hcloud.placement_groups.domain import PlacementGroup
from hcloud.placement_groups.client import BoundPlacementGroup

from hcloud.servers.domain import ServerCreatePublicNetwork


configuration_map = {
    "name": {
        "valid_types": [str],
        "nullable": False,
        "default": None
    },
    "server_type": {
        "valid_types": [ServerType, BoundServerType],
        "nullable": False,
        "default": None
    },
    "image": {
        "valid_types": [Image],
        "nullable": False,
        "default": None
    },
    "ssh_keys": {
        "valid_types": {
            list: (SSHKey, BoundSSHKey)
        },
        "nullable": True,
        "default": None
    },
    "volumes": {
        "valid_types": {
            list: (Volume, BoundVolume)
        },
        "nullable": True,
        "default": None
    },
    "firewalls": {
        "valid_types": {
            list: (Firewall, BoundFirewall)
        },
        "nullable": True,
        "default": None
    },
    "networks": {
        "valid_types": {
            list: (Network, BoundNetwork)
        },
        "nullable": True,
        "default": None
    },
    "user_data": {
        "valid_types": [ str ],
        "nullable": True,
        "default": None
    },
    "labels": {
        "valid_types": [dict],
        "nullable": True,
        "default": None
    },
    "location": {
        "valid_types": [Location, BoundLocation],
        "nullable": True,
        "default": None
    },
    "datacenter": {
        "valid_types": [Datacenter, BoundDatacenter],
        "nullable": True,
        "default": None
    },
    "start_after_create": {
        "valid_types": [bool],
        "nullable": True,
        "default": True
    },
    "automount": {
        "valid_types": [bool],
        "nullable": True,
        "default": None
    },
    "placement_group": {
        "valid_types": [PlacementGroup, BoundPlacementGroup],
        "nullable": True,
        "default": None
    },
    "public_net": {
        "valid_types": [ServerCreatePublicNetwork],
        "nullable": True,
        "default": None
    }
}

class Configuration:
    """Object definition of server configurations."""
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            if key not in configuration_map.keys():
                continue
            valid, message = self.keyIsValid(key, value)
            if not valid:
                raise ValueError(message)
            self.__dict__[key] = value
        for key, value in configuration_map.items():
            if key not in self.__dict__.keys():
                if not value['nullable']:
                    raise ValueError(f"configuration missing non-nullable key: `{key}`")
        if self.name is not None:
            self._name = self.name
            del self.name

    def keyIsValid(self, key: str, data):
        if data is None: # not nullable & data is None returns False
            if configuration_map[key].get('default') is not None:
                data = configuration_map[key]['default']
            else:
                return (configuration_map[key]['nullable'], f"Key `{key}` is None")
        valid_types = configuration_map[key]['valid_types']
        if isinstance(valid_types, dict):
            check_type = valid_types.get(type(data), None)
        else:
            check_type = valid_types
        
        def checker(check_item):
            if type(check_type) in [tuple, list]:
                if type(check_item) not in check_type:
                    return (False, f"{type(check_item)} not in {check_type}")
            else:
                if type(check_item) != check_type:
                    return (False, f"{type(check_item)} != {check_type}")
            return (True, "Valid!")
        if type(data) in [tuple, list]:
            for item in data:
                result, message = checker(item)
                if not result:
                    return (result, message)
        else:
            return checker(data)
        return (True, "Valid!")

if __name__ == "__main__":
    config = Configuration(
        name = None,
        server_type = ServerType(name="test"),
        image = Image(name="ubuntu-22.04"),
        ssh_keys = None
    )
    print(config.__dict__)