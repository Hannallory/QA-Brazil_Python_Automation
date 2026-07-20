from data import *
from helpers import *

class TestUrbanRoutes:
    @classmethod
    def setup_class(cls):
        if is_url_reachable(URBAN_ROUTES_URL):
            return True
        else:
            return False

    def  test_set_route(self):
         # Adicionar em S8
         print ("função criada para definir a rota")
         pass
    def test_select_plan (self):
         # Adicionar em S8
         print ("função criada para definir a plan")
         pass
    def test_fill_phone_number (self):
         # Adicionar em S8
         print("função criada para definir o telefone")
         pass
    def test_fill_card (self):
         # Adicionar em S8
         print("função criada para definir o cartao de credito")
         pass
    def test_comment_for_driver (self):
         # Adicionar em S8
         print("função criada para definir comentario do motorista")
         pass
    def test_order_blanket_and_handkerchiefs (self):
         # Adicionar em S8
         print("função criada para pedir cobertor")
         pass
    def test_order_2_ice_creams (self):
         # Adicionar em S8
         print("função criada para pedir 2 sorvetes")
         for i in range (2):
             # Adicionar em S8
             pass
    def test_car_search_model_appears (self):
         # Adicionar em S8
         print("função criada para buscar modelos de carro")
         pass