from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
import subprocess

from .models import Command


def test(request):
    if request.method == 'POST':
        command = request.POST.get('command')
        command = str(command)
        p = subprocess.Popen(command, stdout=subprocess.PIPE, shell=True)

        (output, err) = p.communicate()

        p_status = p.wait()

        if p.returncode == 1:
                output = output
        else:
                output = output
        context = {
                'output': output,
            }
        return render(request, 'badcommand/results.html', context)

    else:
        context = {
        }
        return render(request, 'badcommand/test.html', context )

def index(request):
    context = {
        }
    return render(request, 'badcommand/index.html', context )
