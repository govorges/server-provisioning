from hcloud.images import Image
from hcloud.server_types import ServerType

from ._configuration import Configuration

CONFIGURATION_NAME = __name__ # Optional
SERVER_CONFIGURATION = Configuration( # A file's server configuration must be named SERVER_CONFIGURATION.
    name = CONFIGURATION_NAME,
    server_type = ServerType(name=CONFIGURATION_NAME),
    image = Image(name="ubuntu-22.04")
)