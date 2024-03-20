from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework import mixins, viewsets, status
from vastvistas_web.models import (Configuration, Navbar, Post, PostComment,
                                   User)
from vastvistas_web.serializers import (ConfigurationSerializer,
                                        NavbarSerializer, UserSerializer)
from django.core.paginator import Paginator
from rest_framework.decorators import api_view
from django.db import IntegrityError
from django.db.models import Q
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


def home(request):
    config = Configuration.objects.last()
    posts = Post.objects.filter(
        is_active=True, is_approved=True, status=1).order_by("priority")
    paginator = Paginator(posts, config.post_count)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'homepage.html', {"posts": page_obj})


def post(request, slug):
    comments = None
    post = Post.objects.filter(
        slug=slug, is_active=True, is_approved=True, status=1).last()
    if post:
        if 'viewed_posts' not in request.session:
            request.session['viewed_posts'] = []
        viewed_posts = request.session.get('viewed_posts', [])
        if post.id not in viewed_posts:
            post.views += 1
            post.save()
            viewed_posts.append(post.id)
            request.session['viewed_posts'] = viewed_posts
            request.session.modified = True
        saved_user_info = None
        user = None
        if 'save_user' in request.session:
            saved_user_info = request.session.get("save_user")
            user = User.objects.filter(
                email=saved_user_info.get("email")).last()
        if not request.user.is_superuser:
            comments = PostComment.objects.filter(Q(user=user) |
                                                  Q(is_approved=True))
        else:
            comments = PostComment.objects.all()
    return render(request, 'post.html',
                  {"post": post,
                   "saved_user_info": saved_user_info,
                   "comments": comments})


@api_view(['POST'])
def create_comment(request):
    post_id = request.POST.get("postId")
    comment = request.POST.get("comment")
    user_name_ = request.POST.get("username").lower()
    user_name = user_name_.split(" ")
    if len(user_name) == 1:
        return JsonResponse(
            {"message": "Please Enter First name and last name."},
            status=status.HTTP_400_BAD_REQUEST)
    else:
        first_name = user_name[0]
        last_name = user_name[1]
    email = request.POST.get("email")
    website = request.POST.get("website")
    save_user = request.POST.get("save-user", None)
    if save_user is not None:
        request.session['save_user'] = {
            "user_name": user_name_,
            "email": email,
            "website": website}
    user_name = first_name + "-" + last_name if last_name else first_name
    try:
        user, created = User.objects.get_or_create(
            email=email, username=user_name, defaults={
                'username': user_name,
                'first_name': first_name,
                'last_name': last_name
            })
        if user:
            post = Post.objects.filter(pk=post_id).last()
            PostComment.objects.create(
                post=post, user=user, website=website, comment=comment)
            return JsonResponse({"message": "Successfully commented"},
                                status=status.HTTP_200_OK)
    except IntegrityError:
        return JsonResponse(
            {"message": (
                "Username or Email Id already exists. "
                "Please choose a different username.")},
            status=status.HTTP_400_BAD_REQUEST)


class NavbarViewSet(viewsets.ModelViewSet):
    serializer_class = NavbarSerializer

    def get_queryset(self):
        return Navbar.objects.filter(is_active=True)


class ConfigurationViewset(mixins.ListModelMixin,
                           viewsets.GenericViewSet):
    serializer_class = ConfigurationSerializer

    def get_queryset(self):
        return Configuration.objects.all()[:1]
