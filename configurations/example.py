from hcloud.images import Image
from hcloud.server_types import ServerType

from ._configuration import Configuration

SERVER_CONFIGURATION = Configuration( # A file's server configuration must be named SERVER_CONFIGURATION.
    name = "example-server",
    server_type = ServerType(name="example"),
    image = Image(name="ubuntu-22.04")
)