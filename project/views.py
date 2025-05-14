from django.shortcuts import render,redirect
from project.models import userdata,contactdata 

# Create your views here.
def register(request):
    if request.method == 'POST':
        name=request.POST['name']
        email=request.POST['email']
        password=request.POST['password']
        image = request.FILES.get('image')

        if userdata.objects.filter(email=email).exists():
            return render(request, 'register.html', {
                'error': 'Email already registered. Please use a different email.'
            })
        
        data=userdata(
            name=name,
            email=email,
            password=password,
            image=image 
        )
        data.save()
        return redirect('/')
    return render(request,'register.html')

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = userdata.objects.filter(email=email, password=password).first() 
        if user:
            request.session['user_id'] = user.id  
            return redirect('/dashboard/')
        else:
            return render(request, 'login.html', {"error": "Invalid Email or Password"})

    return render(request, 'login.html' )


def logout_view(request):
    del request.session['user_id']
    return redirect('/login/')

def dashboard(request):
    if 'user_id' not in request.session:
        return redirect('/login/')
    user = userdata.objects.get(id=request.session['user_id']) 
    return render(request, 'dashboard.html', {'user':user})


def add_contact(request):
    user_id = request.session.get('user_id')

    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        gender = request.POST['gender']
        city = request.POST['city']
        contact = request.POST['contact']
        address = request.POST['address']
        image = request.FILES.get('image')
      
        user = userdata.objects.get(id=user_id)

        data = contactdata(
            user_id=user,
            name=name,
            email=email,
            gender=gender,
            city=city,
            contact=contact,
            address=address,
            image=image,
            
        )
        data.save()
        return redirect('/view/')

    return render(request, 'addcontact.html', {'user_id': user_id})


def viewdata(request):
    if 'user_id' not in request.session:
        return redirect('/login/')

    data = contactdata.objects.filter(user_id=request.session['user_id'])
    return render(request, 'view.html', {"data": data})

def editdata(request, id):
    data = contactdata.objects.filter(id=id, user_id=request.session['user_id'])

    if request.method == "POST":
       
        data.name = request.POST['name']
        data.email = request.POST['email']
        data.gender = request.POST['gender']
        data.city = request.POST['city']
        data.contact = request.POST['contact']
        data.address = request.POST['address']
        data.image  =  request.FILES.get('image')
        data.save() 

        return redirect('/view/') 

    return render(request, 'editdata.html', {'data': data}) 



def delete_contact(request, id):
    contact = contactdata.objects.get(id=id)
    contact.delete()
    return redirect('/view/')


def logout_view(request):
    request.session.flush()
    return redirect('/')

def change_password(request):
    if 'user_id' not in request.session:
        return redirect('/login/')
    
    if request.method == 'POST':
        current_password = request.POST['current_password']
        new_password = request.POST['new_password']
        confirm_password = request.POST['confirm_password']
        
        user = userdata.objects.get(id=request.session['user_id'])
        
        if user.password == current_password: 
            if new_password == confirm_password:
                user.password = new_password
                user.save()
                return redirect('/dashboard/')
            else:
                return render(request, 'change_password.html', {"error": "Passwords do not match!"})
        else:
            return render(request, 'change_password.html', {"error": "Incorrect current password!"})
    
    return render(request, 'change_password.html')

def edit_profile(request):
    if 'user_id' not in request.session:
        return redirect('/login/')

    user = userdata.objects.get(id=request.session['user_id'])

    if request.method == 'POST':
        new_name = request.POST['name']
        new_email = request.POST['email']
        new_image = request.FILES.get('image')

        if userdata.objects.exclude(id=user.id).filter(email=new_email).exists():
            return render(request, 'edit_profile.html', {
                'user': user,
                'error': 'Email already exists. Please choose a different one.'
            })

        user.name = new_name
        user.email = new_email
        user.image = new_image

        user.save()

        return render(request, 'edit_profile.html', {
            'user': user,
            'success': 'Profile updated successfully.'
        })

    return render(request, 'edit_profile.html', {'user': user})


def delete_profile(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = userdata.objects.filter(email=email, password=password).first()

        if user:
  
            contactdata.objects.filter(user_id=user).delete()

            user.delete()

            return render(request, 'delete_profile.html', {
                'success': 'Account deleted successfully.'
            })
        else:
            return render(request, 'delete_profile.html', {
                'error': 'Invalid email or password.'
            })

    return render(request, 'delete_profile.html')


