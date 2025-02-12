
# Define role-based access control (RBAC) structure
RESOURCES_FOR_ROLES = {
    'admin': {
        'resource1': ['read', 'write', 'delete'],
        'resource2': ['read', 'write', 'delete'],
        '': ['read']
    },
    'user': {
        'resource1': ['read'],
        'resource2': ['read', 'write'],
    }
}

# Optionally, define paths to be excluded from checking for permissions
EXCLUDED_PATHS = ['docs', 'openapi.json']

