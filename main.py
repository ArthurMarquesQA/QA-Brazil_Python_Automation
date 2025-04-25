#Tarefa 3
from pages import UrbanRoutesPage
from selenium.webdriver import Chrome
import data
import helpers
import time


class TestUrbanRoutes:
    @classmethod
    def setup_class(cls): #Tarefa 4     # não modifique, pois precisamos do registro adicional habilitado para recuperar o código de confirmação do telefone
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

    def test_set_route(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        time.sleep(2)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(2)
        assert routes_page.get_from_location_value() == data.ADDRESS_FROM
        assert routes_page.get_to_location_value() == data.ADDRESS_TO


    def test_select_plan(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(2)
        routes_page.click_taxi_option()
        routes_page.click_comfort_icon()
        time.sleep(2)


    def test_fill_phone_number(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_taxi_option()
        routes_page.click_comfort_icon()
        routes_page.click_number_text(data.PHONE_NUMBER)


    def test_fill_card(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        time.sleep(1)
        routes_page.click_taxi_option()
        routes_page.click_comfort_icon()
        time.sleep(1)
        routes_page.click_add_cartao(data.CARD_NUMBER,data.CARD_CODE)



    def test_comment_for_driver(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_taxi_option()
        routes_page.click_comfort_icon()
        routes_page.add_comentario(data.MESSAGE_FOR_DRIVER)



    def test_order_blanket_and_handkerchiefs(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_taxi_option()
        routes_page.click_comfort_icon()
        routes_page.switch_cobertor()


    def test_order_2_ice_creams(self):  # Tarefa 5
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_taxi_option()
        routes_page.click_comfort_icon()

        for _ in range(2):  # Loop dentro do método
            routes_page.add_ice()  # Chamada correta do método de instância

        assert int(routes_page.qnt_sorvete()) == 2  # Verificação correta do atributo

    def test_car_search_model_appears(self):
        self.driver.get(data.URBAN_ROUTES_URL)
        routes_page = UrbanRoutesPage(self.driver)
        routes_page.enter_locations(data.ADDRESS_FROM, data.ADDRESS_TO)
        routes_page.click_taxi_option()
        routes_page.click_comfort_icon()
        routes_page.click_number_text(data.PHONE_NUMBER)
        time.sleep(1)
        routes_page.click_add_cartao(data.CARD_NUMBER, data.CARD_CODE)
        time.sleep(1)
        routes_page.call_taxi()

    @classmethod
    def teardown_class(cls):
        cls.driver.quit()