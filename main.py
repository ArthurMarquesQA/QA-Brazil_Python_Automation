#Tarefa 3
import data
import helpers

class TestUrbanRoutes:
    @classmethod

    def setup_class(cls): #Tarefa 4 
        if helpers.is_url_reachable(data.URBAN_ROUTES_URL) == True: #Verifica se retorna True, como conectado no servidor
            print("Conectado ao servidor Urban Routes")
        else: # Se retorna False não está conectado
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução.")
    pass

    def test_set_route(self):

    # Adicionar em S8
    print("função criada para definir a rota")
    pass

    def test_select_plan(self):

    # Adicionar em S8
    print("função criada para selecionar o plano")
    pass

    def test_fill_phone_number(self):

    # Adicionar em S8
    print("função criada para verificar o numero de telefone")
    pass

    def test_fill_card(self):

    # Adicionar em S8
    print("função criada para verificar o card do usuario")
    pass

    def test_comment_for_driver(self):

    # Adicionar em S8
    print("função criada para comentario para o motorista")
    pass

    def test_order_blanket_and_handkerchiefs(self):

    # Adicionar em S8
    print("função criada para o pedir um lenço")
    pass

    def test_order_2_ice_creams(self): #Tarefa 5
    for test_order_2_ice_creams in range(2): #Intera o ciclo 2 vezes
    # Adicionar em S8
    print("função criada para pedir sorvetes")
    pass

    def test_car_search_model_appears(self):

    # Adicionar em S8
    print("função criada para os modelos de carros disponiveis")
    pass
