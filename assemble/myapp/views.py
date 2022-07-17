from django.shortcuts import render, redirect
from django.contrib import auth
from .models import myUser

def index(request):
    return render(request, 'index.html')

def home(request):
    return render(request, 'home.html')

def login(request):
    #POST 요청이 들어오면 로그인 처리를 해줌
    if request.method == 'POST':
        userid = request.POST['username']
        pwd = request.POST['password']
        user = auth.authenticate(request, username=userid, password=pwd) 
        #받은 username과 password가 DB에 이미 있는건지 확인해보겠다는 의미
        #있는 계정이면 그 회원의 USER객체를 반환 없는계정이면 NONE 반환함
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render(request, 'login.html')
    #GET 요청이 들어오면 login form을 담고있는 login.html을 띄어주는 역할을 해줌
    else:
        return render(request, 'login.html')
# Create your views here.

def signup(request):
    # signup 으로 POST 요청이 왔을 때, 새로운 유저를 만드는 절차를 밟는다.
        if request.method == 'POST':
            userid = request.POST['username']
            pwd = request.POST['password']
            # pwd2 = request.POST['confirm']
            name = request.POST['name']
            email = request.POST['email']
            phone = request.POST['phone']
            gender = request.POST['gender']
            birthday = request.POST['birthday']

            user = myUser.objects.create_user(username=userid, password=pwd, name=name, email=email, phone=phone, gender=gender, birthday=birthday)
            auth.login(request, user)
            return redirect('home')

            # password와 confirm에 입력된 값이 같다면
            # if pwd == pwd2:
            #     # user 객체를 새로 생성
            #     user = myUser.objects.create_user(username=userid, password=pwd, nickname = nickname)
            #     # 로그인 한다
            #     auth.login(request, user)
            #     return redirect('home')
            # else:
            #     return render(request, 'signup.html')
            
    
        # signup으로 GET 요청이 왔을 때, 회원가입 화면을 띄워준다.
        return render(request, 'signup.html')

def logout(request):
    auth.logout(request)
    return redirect('index')