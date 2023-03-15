from dataclasses import dataclass


@dataclass
class GetUserRequest:
    user_id: int


class GetUserController:
    def get(self) -> None:
        pass


@dataclass
class AddUserRequest:
    user: dict


class AddUserController:
    def add(self, request: AddUserRequest) -> None:
        print(request.user)


@dataclass
class PatchUserRequest:
    user_id: int
    user: dict


class PatchUserController:
    def patch(self, request: PatchUserRequest) -> None:
        print(request.user)


@dataclass
class DeleteUserRequest:
    user_id: int


class DeleteUserController:
    def delete(self, request: DeleteUserRequest) -> None:
        print(request.user_id)


@dataclass
class PutUserRequest:
    user: dict


class PutUserController:
    def put(self, request: PutUserRequest) -> None:
        print(request.user)
