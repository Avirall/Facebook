from django.shortcuts import render,redirect,get_object_or_404
from .models import UserProfile,Post,Comment,Likes
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

# Create your views here.


def loginPage(request):
    page = 'login'
    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':
        username = request.POST.get('email')
        password = request.POST.get('password')
        
        try:
            user = User.objects.get(username=username)
        except:
            # messages.error(request, "The email address or mobile number you entered isn't connected to an account.")
            return render(request, 'core/login_register.html', {'page': page})

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.error(request, "Username or password is incorrect")

    context = {'page': page}
    return render(request, 'core/login_register.html', context)

def registerUser(request):
    if request.method == 'POST':
        fname = request.POST.get('firstname')
        sname = request.POST.get('surname')
        username = request.POST.get('username')
        password = request.POST.get('password')
        date_of_birth = request.POST.get('dob')
        gender = request.POST.get('gender')
        email = username
        user = User.objects.create_user(username,email,password)
        user.first_name = fname
        user.last_name = sname
        user.save()
        UserProfile.objects.create(user=user,date_of_birth=date_of_birth,gender=gender)
        return redirect('login')
    return render(request, 'core/register.html')

def loginUser(request):
    
    if request.method=='POST':
        user=request.user
        description=request.POST.get('desc')
        media_file=request.FILES.get('fileinput')
        new_post=Post.objects.create(user=user,description=description,media_file=media_file)
        new_post.save()
        return redirect('home')
        
    
    posts= Post.objects.all()
    comments = Comment.objects.all
    context = {'posts':posts,'comments':comments}
    return render(request,'core/logged_in.html',context)

def like(request, id):
    user = request.user
    post = get_object_or_404(Post, id=id)
    current_likes = post.likes
    liked = Likes.objects.filter(user=user, post=post).count()

    if not liked:
        Likes.objects.create(user=user, post=post)
        current_likes += 1
    else:
        # Delete the existing like
        Likes.objects.filter(user=user, post=post).delete()
        current_likes -= 1

    post.likes = current_likes  
    post.save() 
    return redirect('home')

def comment(request,id):
    
    if request.method=='POST':
        user=request.user
        post = Post.objects.get(id=id)
        body = request.POST.get('comment')
        Comment.objects.create(user=user,post=post,body=body)
        return redirect('home')
    posts= Post.objects.all()
    comments = Comment.objects.all
    context = {'posts':posts,'comments':comments}
    return render(request,'core/logged_in.html',context)