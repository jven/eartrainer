from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting

import librosa
import os
import vamp

# Create your views here.
def index(request):
    os.environ["VAMP_PATH"] = "/app/hello"
    n = librosa.time_to_samples(3)
    return HttpResponse(str(n) + ' [' + ' '.join(vamp.list_plugins()) +
        '] path=' + (os.environ["PATH"] if "PATH" in os.environ else "none") +
        ' vamp_path=' + (os.environ["VAMP_PATH"] if "VAMP_PATH" in os.environ else "none") +
        ' dirname=' + os.path.dirname(os.path.abspath(__file__)) +
        ' cwd=' + os.getcwd())


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})
