from time import time

from InnerLayers.DomainLayer.DomainSpecificLanguage.Body import Body
from InnerLayers.DomainLayer.DomainSpecificLanguage.CommentStatus import CommentStatus
from InnerLayers.DomainLayer.DomainSpecificLanguage.Time import Time
from InnerLayers.DomainLayer.DomainSpecificLanguage.UUID import UUID
from InnerLayers.UsecaseLayer.services.Serializable import Serializable


class CommentDTO(Serializable):
    def __init__(self):
        self.commentID: UUID = None
        self.body: Body = None
        self.createdAt: Time = None
        self.status: CommentStatus = None

    def toMap(self) -> dict:
        result = {}

        if self.commentID: result[f'{self.commentID=}'.split('=')[0].split('.')[1]] = self.commentID.toRepresent()
        if self.body: result[f'{self.body=}'.split('=')[0].split('.')[1]] = self.body.toRepresent()
        if self.createdAt: result[f'{self.createdAt=}'.split('=')[0].split('.')[1]] = self.createdAt.toRepresent()
        if self.status: result[f'{self.status=}'.split('=')[0].split('.')[1]] = self.status.toRepresent()

        return result
