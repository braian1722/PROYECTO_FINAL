from django.shortcuts import render,redirect 
from local_de_ropa.models import *
from local_de_ropa.forms import *
from django.contrib.admin.views.decorators import staff_member_required

from django.contrib.auth.forms import AuthenticationForm,UserChangeForm #formularios prefabricados
from django.contrib.auth import login,logout,authenticate ,update_session_auth_hash  # inicio de seciones y cierre
from django.contrib.auth.decorators import login_required # requisito para aceder a un parte del codigo
from django.contrib.auth.models import User

# Create your views here.
@login_required
def index(request):
        avatar = Avatar.objects.filter(user = request.user.id)
        try:
            avatar = avatar[0].image.url
        except:
            avatar = None   
        return render (request,"index.html",{"avatar":avatar})

def load(request):
    return render(request,"load.html")

def compra(request): 
    return render(request,"compra.html")

def productos(request):
    return render(request,"productos.html")

#usuario

def registro(request):
    formulario = UserRegisterForm (request.POST) 
    if request.method == "POST":
        
        
        if formulario.is_valid():
          
            formulario.save()
            return redirect("/local_de_ropa/login")

    #formulario = UserCreationForm()
        else:
            return render (request,"user_templates/registro.html",{"formulario": formulario})    

    formulario = UserRegisterForm()
    return render (request,"user_templates/registro.html",{"formulario": formulario}) 




def login_request(request):
    if request.method == "POST":
        formulario = AuthenticationForm(request, data =request.POST)
        if formulario.is_valid():
            user = formulario.cleaned_data.get("username") #obtienen el formuario
            pwd = formulario.cleaned_data.get("password")

            user = authenticate ( username = user, password = pwd) #indentifica si hay un usuario

            if user is not None:   #si user no esta vacio login crea un usuario
                login(request,user)
                avatar = Avatar.objects.filter(user = request.user.id)
                try:
                    avatar = avatar[0].image.url
                except:
                    avatar = None   
                return render (request,"index.html",{"avatar":avatar})
            else:
                return render(request,"user_templates/login.html", {"formulario":formulario})  #en caso de que no ingresemos datos nos devuelve a login  

        else:
            return render(request,"user_templates/login.html", {"formulario":formulario})

    formulario = AuthenticationForm() #mandamos el formulario vacion en caso de que no halla un post
    return render(request,"user_templates/login.html", {"formulario":formulario} )

@login_required
def perfilview(request):
   
    return render (request,"user_templates/perfil.html")  



@login_required
def editar_perfil(request):
    usuario = request.user    
    usuario_basic_info = User.objects.get(id = usuario.id)
    
    if request.method == "POST":
        formulario = UserChangeForm(request.POST, instance = usuario)
        if formulario.is_valid():

            usuario_basic_info.username = formulario.cleaned_data.get("username")
            usuario_basic_info.email = formulario.cleaned_data.get("email")
            usuario_basic_info.first_name = formulario.cleaned_data.get("first_name") 
            usuario_basic_info.last_name = formulario.cleaned_data.get("last_name")
            usuario_basic_info.save()

            avatar = Avatar.objects.filter(user = request.user.id)
            try:
               avatar = avatar[0].image.url
            except:
               avatar = None   
            return render (request,"index.html",{"avatar":avatar})

        else:
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
               avatar = avatar[0].image.url
            except:
               avatar = None   
            return render (request,"index.html",{"avatar":avatar,"formulario":formulario})

    else: 
        formulario = UserChangeForm(initial = { "email": usuario.email ,"username": usuario.username , "first_name": usuario.first_name, "last_name":usuario.last_name})       
    return render(request,"user_templates/editar_perfil.html",{"formulario":formulario,"usuario":usuario})


def chance_pass(request):
    usuario = request.user  
    if request.method == "POST":
        #formulario = PasswordChangeForm(data = request.POST, user = usuario)
        formulario = ChancePasswordChangeForm(data = request.POST, user = usuario)
        if formulario.is_valid():
            user = formulario.save()
            update_session_auth_hash(request,user)
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
               avatar = avatar[0].image.url
            except:
               avatar = None   
            return render (request,"index.html",{"avatar":avatar})
    else:
        #formulario = PasswordChangeForm(request.user)
        formulario = ChancePasswordChangeForm(user = request.user)
    return render (request,"user_templates/chancepass.html",{"formulario":formulario,"usuario":usuario}) 
    
    







## CRUD REMEARAS ##

def create_remera(request):
    if request.method == "POST":
        remera = Remeras (modelo=request.POST["modelo"],marca=request.POST["marca"],talle=request.POST["talle"],
        color=request.POST["color"],stock=request.POST["stock"])
        remera.save()

        remeras = Remeras.objects.all()
        return render(request,"RemerasCRUD/read_remeras.html", {"remeras": remeras})
        
    return render(request,"RemerasCRUD/create_remeras.html")
   

@staff_member_required
def read_remeras(request):
        remera = Remeras.objects.all() 
        return render(request,"RemerasCRUD/read_remeras.html", {"remeras": remera})

           
      
def update_remera(request,remera_id):

    remera = Remeras.objects.get(id = remera_id) #busca al estudiante por el id

    if request.method == "POST":
        formulario = form_remeras(request.POST) # si encuentra el id trae el formulario

        if formulario.is_valid():
            informacion = formulario.cleaned_data
            remera.modelo = informacion ["modelo"]
            remera.marca = informacion ["marca"]  ## modifica los parametros
            remera.talle = informacion ["talle"]
            remera.color = informacion ["color"]
            remera.stock = informacion ["stock"]
            remera.save()
            
            remeras= Remeras.objects.all()#retorna la nueva lista
            return render(request,"RemerasCRUD/read_remeras.html", {"remeras":remeras})

    else:
        formulario = form_remeras(initial={"modelo": remera.modelo,"marca": remera.marca,"talle": remera.talle, 
        "color": remera.color, "stock": remera.stock})        
    
    return render(request,"RemerasCRUD/update_remeras.html",{"formulario" : formulario})

    
    
def delete_remera(request,remera_id):
    remera = Remeras.objects.get(id = remera_id)
    remera.delete()

    remeras = Remeras.objects.all()
    return render(request,"RemerasCRUD/read_remeras.html", {"remeras": remeras})


## buzos

def create_buzo(request):
    if request.method == "POST":
        buzo = Buzos(modelo=request.POST["modelo"],marca=request.POST["marca"],talle=request.POST["talle"],
        color=request.POST["color"],stock=request.POST["stock"])
        buzo.save()

        buzos = Buzos.objects.all()
        return render(request,"Buzos CRUD/read_buzos.html", {"buzos": buzos})
        
    return render(request,"Buzos CRUD/create_buzos.html")
   

@staff_member_required
def read_buzos(request):#para que no alla un error 
    buzo = Buzos.objects.all() # trae todos los datos 
    return render(request,"Buzos CRUD/read_buzos.html", {"buzos": buzo})



def update_buzo(request,buzo_id):

    buzo = Buzos.objects.get(id = buzo_id) #busca al estudiante por el id

    if request.method == "POST":
        formulario = form_buzos(request.POST) # si encuentra el id trae el formulario
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            buzo.modelo = informacion ["modelo"]
            buzo.marca = informacion ["marca"]  ## modifica los parametros
            buzo.talle = informacion ["talle"]
            buzo.color = informacion ["color"]
            buzo.stock = informacion ["stock"]
            buzo.save()
            
            buzos= Buzos.objects.all()#retorna la nueva lista
            return render(request,"Buzos CRUD/read_buzos.html", {"buzos":buzos})

    else:
        formulario = form_buzos(initial={"modelo": buzo.modelo,"marca": buzo.marca,"talle": buzo.talle, 
        "color": buzo.color, "stock": buzo.stock})        
    
    return render(request,"Buzos CRUD/update_buzos.html",{"formulario" : formulario})

    
    
def delete_buzo(request,buzo_id):
    buzo = Buzos.objects.get(id = buzo_id)
    buzo.delete()

    buzos = Buzos.objects.all()
    return render(request,"Buzos CRUD/read_buzos.html", {"buzos": buzos})



#### JEANS


def create_jeans(request):
    if request.method == "POST":
        jean = Jeans(modelo=request.POST["modelo"],marca=request.POST["marca"],talle=request.POST["talle"],
        color=request.POST["color"],stock=request.POST["stock"])
        jean.save()

        jeans = Jeans.objects.all()
        return render(request,"jeans CRUD/read_jeans.html", {"jeans": jeans})
        
    return render(request,"Jeans CRUD/create_jeans.html")
   
@staff_member_required
def read_jeans(request):#para que no alla un error 
    jean = Jeans.objects.all() # trae todos los datos 
    return render(request,"Jeans CRUD/read_jeans.html", {"jeans": jean})



def update_jean(request,jean_id):

    jean= Jeans.objects.get(id = jean_id) #busca al estudiante por el id

    if request.method == "POST":
        formulario = form_jeans(request.POST) # si encuentra el id trae el formulario
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            jean.modelo = informacion ["modelo"]
            jean.marca = informacion ["marca"]  ## modifica los parametros
            jean.talle = informacion ["talle"]
            jean.color = informacion ["color"]
            jean.stock = informacion ["stock"]
            jean.save()
            
            jeans= Jeans.objects.all()#retorna la nueva lista
            return render(request,"jeans CRUD/read_jeans.html", {"jeans":jeans})

    else:
        formulario = form_buzos(initial={"modelo": jean.modelo,"marca": jean.marca,"talle": jean.talle, 
        "color": jean.color, "stock": jean.stock})        
    
    return render(request,"Jeans CRUD/update_jeans.html",{"formulario" : formulario})

    
    
def delete_jean(request,jean_id):
    jean = Jeans.objects.get(id = jean_id)
    jean.delete()

    jeans= Jeans.objects.all()
    return render(request,"Jeans CRUD/read_jeans.html", {"jeans": jeans})


###### CAMPERAS


def create_campera(request):
    if request.method == "POST":
        campera = Camperas(modelo=request.POST["modelo"],marca=request.POST["marca"],talle=request.POST["talle"],
        color=request.POST["color"],stock=request.POST["stock"])
        campera.save()

        camperas = Camperas.objects.all()
        return render(request,"Camperas CRUD/read_camperas.html", {"camperas": camperas})
        
    return render(request,"Camperas CRUD/create_camperas.html")
   
@staff_member_required
def read_camperas(request):#para que no alla un error 
    campera = Camperas.objects.all() # trae todos los datos 
    return render(request,"Camperas CRUD/read_camperas.html", {"camperas": campera})



def update_campera(request,campera_id):

    campera= Camperas.objects.get(id = campera_id) #busca al estudiante por el id

    if request.method == "POST":
        formulario = form_camperas(request.POST) # si encuentra el id trae el formulario
        if formulario.is_valid():
            informacion = formulario.cleaned_data
            campera.modelo = informacion ["modelo"]
            campera.marca = informacion ["marca"]  ## modifica los parametros
            campera.talle = informacion ["talle"]
            campera.color = informacion ["color"]
            campera.stock = informacion ["stock"]
            campera.save()
        
            camperas= Camperas.objects.all()#retorna la nueva lista
            return render(request,"Camperas CRUD/read_camperas.html", {"camperas":camperas})

    else:
        formulario = form_camperas(initial={"modelo": campera.modelo,"marca": campera.marca,"talle": campera.talle, 
        "color": campera.color, "stock": campera.stock})        
    
    return render(request,"Camperas CRUD/update_camperas.html",{"formulario" : formulario})

    
    
def delete_campera(request,campera_id):
    campera = Camperas.objects.get(id = campera_id)
    campera.delete()

    camperas= Camperas.objects.all()
    return render(request,"Camperas CRUD/read_camperas.html", {"camperas":camperas})


#### AVATAR


def agregarAvatar(request):
    if request.method == "POST" :
        formulario = Avatarformulario(request.POST, request.FILES) #RECIVE DOS PARAMETROS
        if formulario.is_valid():
            user = User.objects.get(username= request.user)
            avatar = Avatar (user = user,image = formulario.cleaned_data["avatar"], id = request.user.id)
            avatar.save()
            avatar = Avatar.objects.filter(user = request.user.id)
            try:
               avatar = avatar[0].image.url
            except:
               avatar = None   
            return render (request,"index.html",{"avatar":avatar})
    else:
        try:
            avatar = Avatar.objects.filter(user = request.user.id)
            formulario = Avatarformulario()
            
        except:
            formulario = Avatarformulario()
    return render (request,"user_templates/agregar_avatar.html",{"formulario":formulario})
