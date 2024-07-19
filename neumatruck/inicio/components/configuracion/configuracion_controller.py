from inicio.models import Configuracion



class ConfiguracionController:
    # 
    def get_all(self):
        first_number = self.first_number()
        second_number = self.second_number()
        facebook = self.facebook()
        instagram = self.instagram()
        email_admin = self.email_admin()
        
        data = {
            'first_number' : first_number,
            'second_number' : second_number,
            'facebook' : facebook,
            'instagram' : instagram,
            'email_admin': email_admin
        }

        return data


    # ? caputar el primer telefono
    def first_number(self):

        configuracion = Configuracion.objects.get(id_configuracion = 1)

        return configuracion.valor;

    def second_number(self):

        configuracion = Configuracion.objects.get(id_configuracion = 2)

        return configuracion.valor;


    def facebook(self):

        configuracion = Configuracion.objects.get(id_configuracion = 3)

        return configuracion.valor;


    def instagram(self):

        configuracion = Configuracion.objects.get(id_configuracion = 4)

        return configuracion.valor;


    def email_admin(self):

        configuracion = Configuracion.objects.get(id_configuracion = 5)

        return configuracion.valor;