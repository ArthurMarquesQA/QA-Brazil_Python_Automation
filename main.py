#Imports
from pages import UrbanRoutesPage
from selenium.webdriver import Chrome
import data
import helpers
import time


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls): #não modifique, pois precisamos do registro adicional habilitado para recuperar o código de confirmação do telefone
        # não modifique, pois precisamos do registro adicional habilitado para recuperar o código de confirmação do telefone
        from selenium.webdriver import DesiredCapabilities
        capabilities = DesiredCapabilities.CHROME
        capabilities["goog:loggingPrefs"] = {'performance': 'ALL'}
        cls.driver = Chrome()
        cls.driver.implicitly_wait(5)

        if helpers.is_url_reachable(data.URBAN_ROUTES_URL): #Verifica se retorna True, como conectado no servidor
            print("Conectado ao servidor Urban Routes")
        else: # Se retorna False não está conectado
            print("Não foi possível conectar ao Urban Routes. Verifique se o servidor está ligado e ainda em execução.")

    def test_set_route(self):  #Teste 1 - Preencher as Rotas De e Para
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        WebDriverWait(self.driver, 1).until(lambda d: True)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        WebDriverWait(self.driver, 1).until(lambda d: True)
        assert routes_page.get_from_location_value() == data.ADDRESS_FROM
        assert routes_page.get_to_location_value() == data.ADDRESS_TO


    def test_select_plan(self): #Teste 2 - Preencher as Rotas e Selecionar o Plano Comfort
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        WebDriverWait(self.driver, 1).until(lambda d: True)
        routes_page.click_taxi_option()
        routes_page.click_comfort_icon()
        WebDriverWait(self.driver, 1).until(lambda d: True)
        assert routes_page.click_comfort_active()

    def test_fill_phone_number(self): #Teste 3 - Preencher Numero de telefone
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_taxi_option()
        routes_page.click_comfort_icon()
        routes_page.click_number_text(data.PHONE_NUMBER)
        assert data.PHONE_NUMBER in routes_page.numero_confirmado()

    def test_fill_card(self): #Teste 4 - Adicionar forma de pagamento como cartão
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        WebDriverWait(self.driver, 1).until(lambda d: True)
        routes_page.click_taxi_option()
        routes_page.click_comfort_icon()
        WebDriverWait(self.driver, 1).until(lambda d: True)
        routes_page.click_add_cartao(data.CARD_NUMBER,data.CARD_CODE)
        assert "Cartão" in routes_page.confirm_cartao() #Acresentado o assert para confirmar o cartão


    def test_comment_for_driver(self): #Teste 5 - Adicionar um comentário para o motorista
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_taxi_option()
        routes_page.click_comfort_icon()
        routes_page.add_comentario(data.MESSAGE_FOR_DRIVER)
        assert data.MESSAGE_FOR_DRIVER in routes_page.coment_confirm()



    def test_order_blanket_and_handkerchiefs(self): #Teste 6 - Adicionar o cobertor para a viagem
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_taxi_option()
        routes_page.click_comfort_icon()
        routes_page.switch_cobertor()
        WebDriverWait(self.driver, 1).until(lambda d: True)
        assert routes_page.switch_cobertor_active() is True


    def test_order_2_ice_creams(self):  # Teste 7 - Adicionar 2 sorvetes
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_taxi_option()
        routes_page.click_comfort_icon()

        for _ in range(2):  # Loop dentro do método
            routes_page.add_ice()  # Chamada correta do método de instância

        assert int(routes_page.qnt_sorvete()) == 2  # Verificação correta do atributo

    def test_car_search_model_appears(self): # Teste 8 - Solicitar um taxi 
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_taxi_option()
        routes_page.click_comfort_icon()
        routes_page.click_number_text(data.PHONE_NUMBER)
        WebDriverWait(self.driver, 1).until(lambda d: True)
        routes_page.click_add_cartao(data.CARD_NUMBER, data.CARD_CODE)
        routes_page.add_comentario(data.MESSAGE_FOR_DRIVER)
        WebDriverWait(self.driver, 1).until(lambda d: True)
        routes_page.call_taxi()
        assert "Buscar carro" in routes_page.pop_up_show()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()
