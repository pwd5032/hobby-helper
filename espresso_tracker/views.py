from django.shortcuts import render
from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
from .models import Brew, Bean
import json

# Create your views here.

# List all brews
def brews(request):
    if request.method == 'GET': 
        brew_list = list(Brew.objects.values()) # Get all brews
        return JsonResponse(brews_json, safe=False) # Return as JSON

# Add a new brew
@csrf_exempt # Disable CSRF protection
def add_brew(request):
    if request.method == 'POST':
        data = json.loads(request.body) # Get the data from the request
        brew = Brew.objects.create(**data) # Create a new brew
        return JsonResponse({'id': brew.id}) # Return the ID of the new brew

# Update an existing brew
@csrf_exempt # Disable CSRF protection
def update_brew(request, brew_id):
    if request.method == 'PUT':
        data = json.loads(request.body) # Get the data from the request
        brew = get_object_or_404(Brew, id=brew_id) # Get the brew
        for key, value in data.items():
            setattr(brew, key, value)
        brew.save() # Save the changes
        return JsonResponse({'id': brew.id}) # Return success

# Delete an existing brew (TODO update with soft delete)
@csrf_exempt # Disable CSRF protection
def delete_brew(request, brew_id):
    if request.method == 'DELETE':
        brew = get_object_or_404(Brew, id=brew_id) # Get the brew
        brew.delete() # Delete the brew
        return JsonResponse({'id': brew.id}) # Return success


# Bean Views

# List all beans
def beans(request):
    if request.method == 'GET': 
        bean_list = list(Bean.objects.values()) # Get all beans
        return JsonResponse(bean_list, safe=False) # Return as JSON

# Add a new bean
@csrf_exempt # Disable CSRF protection
def add_bean(request):
    if request.method == 'POST':
        data = json.loads(request.body) # Get the data from the request
        bean = Bean.objects.create(**data) # Create a new bean
        return JsonResponse({'id': bean.id}) # Return the ID of the new bean

# Update an existing bean
@csrf_exempt # Disable CSRF protection
def update_bean(request, bean_id):
    if request.method == 'PUT':
        data = json.loads(request.body) # Get the data from the request
        bean = get_object_or_404(Bean, id=bean_id) # Get the bean
        for key, value in data.items():
            setattr(bean, key, value)
        bean.save() # Save the changes
        return JsonResponse({'id': bean.id}) # Return success

# Delete an existing bean (TODO update with soft delete)
@csrf_exempt # Disable CSRF protection
def delete_bean(request, bean_id):
    if request.method == 'DELETE':
        bean = get_object_or_404(Bean, id=bean_id)
        bean.delete() # Delete the bean
        return JsonResponse({'id': bean.id}) # Return success

