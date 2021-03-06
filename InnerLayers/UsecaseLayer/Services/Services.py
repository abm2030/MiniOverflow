from InnerLayers.UsecaseLayer.Services.Authentication import Authentication
from InnerLayers.UsecaseLayer.Services.UUIDGenerator import UUIDGenerator


class Services:
    uuidGenerator: UUIDGenerator = None
    authentication: Authentication = None

    @staticmethod
    def initialize(uuidGenerator: UUIDGenerator, authentication: Authentication):
        Services.uuidGenerator = uuidGenerator
        Services.authentication = authentication
