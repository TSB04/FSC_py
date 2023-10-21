from rest_framework.permissions import BasePermission


class IsGetRequest(BasePermission):
    # GET request is allowed for Library hall
    def has_permission(self, request, view):
        return request.method == 'GET'
    

class IsPostRequest(BasePermission):
    # POST request is allowed for creating an account
    def has_permission(self, request, view):
        return request.method == 'POST'
