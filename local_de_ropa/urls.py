from proyecto_final.urls import path
from local_de_ropa.views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
               path('', load),
               path('inicio', index),
               ####### USUARIOS
               path('login/', login_request ),
               path('registro/', registro ),
               path('logout/', LogoutView.as_view (template_name = "load.html"), name ="logout"),#funcion salir
               path('perfil/', perfilview ),
               path('perfil/editarPerfil/', editar_perfil ),
               path('perfil/chance_pass/', chance_pass ),
               path('perfil/chanceavatar/', agregarAvatar ),
               path('compra/', compra ),
               path('productos/', productos ), 
               



               ####### REMERAS
               path('read_remeras/', read_remeras ),
               path('create_remeras/', create_remera ),
               path('update_remera/<remera_id>', update_remera ),
               path('delete_remera/<remera_id>', delete_remera ),

               ####### BUZOS
               path('read_buzos/', read_buzos ),
               path('create_buzo/', create_buzo ),
               path('update_buzo/<buzo_id>', update_buzo ),
               path('delete_buzo/<buzo_id>', delete_buzo ),

               ####### JEANS
               path('read_jeans/', read_jeans ),
               path('create_jeans/', create_jeans ),
               path('update_jean/<jean_id>', update_jean ),
               path('delete_jean/<jean_id>', delete_jean ),


               ####### CAMPERAS
               path('read_camperas/', read_camperas ),
               path('create_campera/', create_campera ),
               path('update_campera/<campera_id>', update_campera ),
               path('delete_campera/<campera_id>', delete_campera ),




]