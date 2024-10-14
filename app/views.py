from django.shortcuts import render,redirect, reverse
from app.models import Blog,Comment
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.contrib import messages

# Create your views here.
def homepage(request):
    products=["tote bag", "shoes", "jewelries"]
    context={"product":products}
    return render(request, 'app/index.html',context)

def about(request):
    return render(request,'app/about.html')
""" def hello(request,cap):
    context={"person": cap}
  
    return render(request,'app/hello.html',context) """
def hello(request,cap):
    context={"person": cap}
  
    return render(request,'app/hello.html',context)

@login_required
def blogs(request):
    user=request.user
    my_blogs= Blog.objects.filter(owner=user).order_by("-created_at")[:2]
    other_blogs= Blog.objects.all().exclude(owner=user).order_by("-created_at")[:2]
    
    context={"my_blogs" :my_blogs,"other_blogs":other_blogs}
    return render(request, 'app/blogs.html',context)
def read(request, id):
    user=request.user
    single_blog=Blog.objects.filter(id=id).first()
    if not single_blog:
        
    
        messages.error(request, 'invalid blog')
        return redirect(blogs)
    if request.method =="POST":
        body=request.POST.get('comment')
        if not body:
            messages.error(request,"cannot be empty")
            return redirect(reverse("read",kwargs={'id':id}))
            
        Comment.objects.create(
            owner=user,
            blog=single_blog,
            body=body
            )
        return redirect(reverse("read",kwargs={'id':id}))
    blogs_comments=Comment.objects.filter(blog=single_blog).order_by('-created_at')
    context={'blog': single_blog, 'comments':blogs_comments}
    return render(request,'app/read.html',context)

def delete(request, id):
    single_blog=Blog.objects.filter(id=id).first()
    user = request.user
    if not single_blog:
        messages.error(request, 'invalid blog')
        return redirect(blogs)
    if single_blog.owner != user:
        messages.error(request,"only the authorize owner can edit")
        return redirect(blogs)
    single_blog.delete()
    return redirect(blogs)
@login_required   
def create(request):
    user=request.user#new shiit 7 of october
   
   
    if request.method=="POST":
        title=request.POST.get("title") #do the same     
        #title=request.POST["titl"] do the same as the above
        body=request.POST.get("body")
        files=request.FILES.get("img")
        print(title, body, files)
        if not title or not body or not files:
            messages.error(request,"these are required steps to take")
            return redirect(homepage)
        Blog.objects.create(
            title=title,
            body=body,
            image=files,
            owner=user #new shit 7 of october
        )
        messages.success(request,"Blog created sucessfully")
        return redirect(about)
    return render(request,"app/new.html")

@login_required
def edit(request, id):
    user=request.user #new shit 7 octo
    single_blog=Blog.objects.filter(id=id).first()
    if not single_blog:
        messages.error(request, 'invalid blog')
        return redirect(blogs)
    if single_blog.owner != user:
        messages.error(request,"only the authorize owner can edit")
        return redirect(blogs)
    
    context={'blog': single_blog}
    if request.method=="POST":#
        title=request.POST.get('title')
        body=request.POST.get('body')
        description=request.POST.get('description')
        img = request.FILES.get('image')
        if not title or not body:
            messages.error(request,"it is update successfully")
            return redirect(homepage )
        single_blog.title = title
        single_blog.body = body
        single_blog.descrition = description
        if img:
            single_blog.image = img
        single_blog.save()
        messages.success(request,"sucessfully done")
        return redirect(homepage)
    return render(request,'app/edit.html',context)
def signup(request):
    
    if request.method == 'POST':
        username=request.POST.get("username")
        Email=request.POST.get("email")
        firstname=request.POST.get("firstname")
        lastname=request.POST.get("lastname")
        password=request.POST.get("password")
        cpassword=request.POST.get("cpassword")
        if not username or not Email or not firstname or not lastname or not password or not cpassword:
            messages.error(request,"all fields are required")
            return redirect(signup)
        if password !=cpassword:
            messages.error(request,"password does not ,match")
            return redirect(signup)
        if len("password")<8:
            messages.error(request,"password must be up to eight characters")
            return redirect(signup)
        if len("username")<5:
            messages.error(request,"username must be atleast five characters")
            return redirect(signup)
        username_exists=User.objects.filter(username=username).exists()
        if username_exists:
            messages.error(request,"the user name already exist")
            return redirect(signup)
        email_exists=User.objects.filter(email=Email).exists()
        if email_exists:
            messages.error(request,"the email already exist")
            return redirect(signup)
        user=User.objects.create(
            username=username,
            email=Email,
            first_name=firstname,
            last_name=lastname,
        )
        user.set_password(password)
        user.save()
        messages.success(request,"done")
        return redirect(homepage)

       
    return render(request,"app/caccount.html")
def login(request):
    next=request.GET.get("next")#lets get you baby
    if request.user.is_authenticated:
        return redirect(homepage)
    if request.method == 'POST':
        username=request.POST.get("username")
        password=request.POST.get("password")
        if not username or not password:
            messages.error(request, "invalid username or password")
            return redirect(login)
        user=auth.authenticate(username=username,password=password)
        if not user:
            messages.error(request,"invalid login credential")
            return redirect(login)
        auth.login(request,user)
        return redirect(next or homepage)# lets get the variable

    return render(request,"app/login.html")

def logout(request):
    auth.logout(request)
    return redirect(login)
     