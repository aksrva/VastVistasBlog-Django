from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework import status
from vastvistas_web.serializers import UserSerializer
from django.contrib.auth import login, authenticate, logout
from rest_framework.authtoken.models import Token
from rest_framework.response import Response
from rest_framework.views import APIView


def logout_view(request):
    logout(request)
    return redirect("/")


def login_view(request):
    if request.method == "POST":
        user = authenticate(
            request,
            username=request.POST.get("email"),
            password=request.POST.get("password"))
        print(user)
        if user is not None:
            login(request, user)
            return redirect("/")
        else:
            return JsonResponse({"message": "Email or Password Incorrect!"})
    return render(request, 'login.html')


class RegisterUser(APIView):
    template_name = "register.html"

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name)

    def post(self, request, *args, **kwargs):
        print(request.data)
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            if user:
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                return redirect("/")
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
