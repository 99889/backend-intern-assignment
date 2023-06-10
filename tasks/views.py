from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from tasks.models import Task
import json

@csrf_exempt
def create_task(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        title = data.get('title')
        description = data.get('description')
        due_date = data.get('due_date')
        status = data.get('status')

        if not title or not description or not due_date or not status:
            return JsonResponse({'error': 'Invalid data'}, status=400)

        task = Task.objects.create(
            title=title,
            description=description,
            due_date=due_date,
            status=status
        )

        return JsonResponse({'task_id': task.id}, status=201)

@csrf_exempt
def retrieve_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return JsonResponse({'error': 'Task not found'}, status=404)

    task_data = {
        'id': task.id,
        'title': task.title,
        'description': task.description,
        'due_date': task.due_date,
        'status': task.status
    }

    return JsonResponse(task_data, status=200)

@csrf_exempt
def update_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return JsonResponse({'error': 'Task not found'}, status=404)

    if request.method == 'PUT':
        data = json.loads(request.body)
        title = data.get('title')
        description = data.get('description')
        due_date = data.get('due_date')
        status = data.get('status')

        if not title or not description or not due_date or not status:
            return JsonResponse({'error': 'Invalid data'}, status=400)

        task.title = title
        task.description = description
        task.due_date = due_date
        task.status = status
        task.save()

        return JsonResponse({'message': 'Task updated successfully'}, status=200)

@csrf_exempt
def delete_task(request, task_id):
    try:
        task = Task.objects.get(id=task_id)
    except Task.DoesNotExist:
        return JsonResponse({'error': 'Task not found'}, status=404)

    if request.method == 'DELETE':
        task.delete()
        return JsonResponse({'message': 'Task deleted successfully'}, status=200)

@csrf_exempt
def list_tasks(request):
    tasks = Task.objects.all()
    task_list = []
    for task in tasks:
        task_data = {
            'id': task.id,
            'title': task.title,
            'description': task.description,
            'due_date': task.due_date,
            'status': task.status
        }
        task_list.append(task_data)

    return JsonResponse({'tasks': task_list}, status=200)
