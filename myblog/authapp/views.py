from django.contrib.auth.models import Group
from django.shortcuts import render,redirect
from authapp.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from articles.models import Articles
from books.models import Books
from articles.models import Comments
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db.models import Count



# Create your views here.
def home(request):
    #articles = Articles.objects.all().order_by('-date')[:6]
    books = Books.objects.all().order_by('-date_add')[:12]
    articles = Articles.objects.annotate(nb_comments=Count('commentaires')).order_by('-date')[:6]
    context = {
        'articles':articles,
        'books':books,
    }
    return render(request, 'authapp/home.html', context)

def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']

        #Restrictions sur mes champs de formulaires
        if User.objects.filter(username=username):
            messages.error(request,"Ce username est deja utilisé !")
            return redirect('register')
        if not username.isalpha():
            messages.error(request, "Désolé, mais le username doit etre en lettre uniquement !")
            return redirect('register')
        if User.objects.filter(email=email):
            messages.error(request,"Cet adresse email est deja utilisé !")
            return redirect('register')
        
        try : 
            validate_password(password)
        except ValidationError as errors:
            return render(request, 'authapp/register.html', {'errors':errors.messages})
        
        #Fin des restrictions sur mes champs de formulaires
        user = User.objects.create_user(username,email,password)

        #Apres la creation du compte utilisateur dans la base de données, l'ajouter au groupes 'users blog'
        group = Group.objects.get(name="users blog")
        user.groups.add(group)

        if user:
            user.save()
            messages.success(request, 'Votre compte a bien été crée !!!')
        return redirect('login_user')

    return render(request, 'authapp/register.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, f"Bienvenue {user.username} vous etes connecté !!!")
            return redirect('home')
        else:
            messages.error(request, "Mot de passe ou nom d'utilisateur incorrect !!!!")
            return redirect('login_user')

    return render(request, 'authapp/login_user.html')

def logout_user(request): 
    logout(request)
    messages.success(request, f'Vous avez bien été Déconnecté !!!')

    return redirect('login_user')

