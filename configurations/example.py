from hcloud.images import Image
from hcloud.server_types import ServerType

from ._configuration import Configuration

SERVER_CONFIGURATION = Configuration(
    name = __name__,
    server_type = ServerType(name="cpx11"),
    image = Image(name="docker-ce")
)