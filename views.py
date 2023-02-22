#views.py

from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from .models import ChatMessage

@login_required
def send_message(request):
    message = request.POST.get('message')
    ChatMessage.objects.create(sender=request.user, message=message)
    return JsonResponse({'success': True})

@login_required
def get_messages(request):
    messages = ChatMessage.objects.order_by('-timestamp')[:10]
    messages = [{'sender': message.sender.username, 'message': message.message} for message in messages]
    return JsonResponse({'messages': messages})