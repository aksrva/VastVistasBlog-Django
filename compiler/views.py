# compiler/views.py
import subprocess
from django.shortcuts import render, redirect
from .forms import CodeSubmissionForm
from django.http import HttpResponse


def compile_code(request):
    if request.method == 'POST':
        form = CodeSubmissionForm(request.POST)
        if form.is_valid():
            process = subprocess.run(
                ['python', '-c', form.cleaned_data['source_code']],
                capture_output=True, text=True, timeout=5)
            return render(request, 'compiler/output.html',
                          {'stdout': process.stdout, 'stderr': process.stderr})
    else:
        form = CodeSubmissionForm()
    return render(request, 'compiler/index.html', {'form': form})


def input_form(request):
    return render(request, 'compiler/input_form.html')


def process_input(request):
    if request.method == 'POST':
        user_input = request.POST.get('user_input')
        return HttpResponse(f"You entered: {user_input}")
    else:
        return redirect('input_form')
