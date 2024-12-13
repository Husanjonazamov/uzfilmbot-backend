from typing import Any

from drf_spectacular.utils import extend_schema
from rest_framework.permissions import AllowAny
from rest_framework.viewsets import ReadOnlyModelViewSet

from ..models import UsersModel
from ..serializers.users import CreateUsersSerializer, ListUsersSerializer, RetrieveUsersSerializer


@extend_schema(tags=["users"])
class UsersView(ReadOnlyModelViewSet):
    queryset = UsersModel.objects.all()

    def get_serializer_class(self) -> Any:
        match self.action:
            case "list":
                return ListUsersSerializer
            case "retrieve":
                return RetrieveUsersSerializer
            case "create":
                return CreateUsersSerializer
            case _:
                return ListUsersSerializer

    def get_permissions(self) -> Any:
        perms = []
        match self.action:
            case _:
                perms.extend([AllowAny])
        self.permission_classes = perms
        return super().get_permissions()
