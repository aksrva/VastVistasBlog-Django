from django.urls import path
from compiler.views import compile_code, input_form, process_input
urlpatterns = [
    path('', compile_code, name="compile_code"),
    path('input-form/', input_form, name='input_form'),
    path('process-input/', process_input, name='process_input'),
]
