from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.responses import JSONResponse

from rbac.config import RESOURCES_FOR_ROLES, EXCLUDED_PATHS

# Sample user data (can be fetched from a database)
USERS = {
    'user1': {'username': 'user1', 'password': 'password', 'role': 'user'},
    'admin1': {'username': 'admin1', 'password': 'adminpassword', 'role': 'admin'}
}


def translate_method_to_action(method: str) -> str:
    method_permission_mapping = {
        'GET': 'read',
        'POST': 'write',
        'PUT': 'update',
        'DELETE': 'delete',
    }
    return method_permission_mapping.get(method.upper(), 'read')


# CHeck if permission granted or not
def has_permission(user_role, resource_name, required_permission):
    if user_role in RESOURCES_FOR_ROLES and resource_name in RESOURCES_FOR_ROLES[user_role]:
        return required_permission in RESOURCES_FOR_ROLES[user_role][resource_name]
    return False


# Define a custom Middleware for handling RBAC
class RBACMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        request_method = str(request.method).upper()
        action = translate_method_to_action(request_method)
        resource = request.url.path[1:]
        if resource not in EXCLUDED_PATHS:
            user1 = USERS['admin1']
            # user1 = USERS['user1']
            if not has_permission(user1['role'], resource, action):
                return JSONResponse(status_code=403, content={"details": "Insufficient permissions"})
        response = await call_next(request)
        return response
