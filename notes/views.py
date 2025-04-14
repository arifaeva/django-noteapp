from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import get_object_or_404, redirect, render
from django.views import View
from .tasks import task_do_something

from .models import Note


class IndexView(LoginRequiredMixin, View):
    login_url = "/login"

    def get(self, request):
        notes = Note.objects.filter(actor=request.user)
        return render(request, "index.html", {"notes": notes})

    def post(self, request):
        title = request.POST.get("title")
        content = request.POST.get("content")

        if not title and not content:
            messages.error(request, "Title and content are required")
        else:
            task_do_something()
            Note.objects.create(title=title, content=content, actor=request.user)

        return redirect("index")


class DetailView(LoginRequiredMixin, View):
    login_url = "/login"

    def get(self, request, id):
        note = Note.objects.get(id=id)
        get_object_or_404(Note, id=id)

        return render(request, "detail.html", {"note": note})


class DeleteView(LoginRequiredMixin, View):
    login_url = "/login"

    def post(self, request, id):
        note = Note.objects.get(id=id)
        note.delete()

        return redirect("index")


class EditView(LoginRequiredMixin, View):
    login_url = "/login"

    def get(self, request, id):
        note = Note.objects.get(id=id)

        return render(request, "edit.html", {"note": note})

    def post(self, request, id):
        title = request.POST.get("title")
        content = request.POST.get("content")

        note = Note.objects.get(id=id)

        note.title = title
        note.content = content
        note.save()

        return redirect("index")
