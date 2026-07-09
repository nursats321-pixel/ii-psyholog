from django.shortcuts import render
from .ai import ask_ai

def chat(request):

    answer = ""

    if request.method == "POST":
        message = request.POST.get("message")
        mood = request.POST.get("mood")

        answer = ask_ai(message, mood)

    return render(request, "chat.html", {
        "answer": answer
    })