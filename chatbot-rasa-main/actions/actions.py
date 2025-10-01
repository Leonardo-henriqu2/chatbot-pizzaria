from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import random

class ActionCheckPizzaPrice(Action):
    def name(self):
        return "action_check_pizza_price"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict):
        
        # Cardápio fictício
        menu = {
            "pequena": 25,
            "média": 40,
            "grande": 55
        }

        tamanho = tracker.get_slot("tamanho")
        if tamanho in menu:
            preco = menu[tamanho]
            dispatcher.utter_message(text=f"A pizza {tamanho} custa R$ {preco},00.")
        else:
            dispatcher.utter_message(text="Desculpe, não temos esse tamanho. Temos pequena, média e grande.")
        
        return []

class ActionSimularEntrega(Action):
    def name(self):
        return "action_simular_entrega"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: dict):
        
        endereco = tracker.get_slot("endereco")
        tempo = random.randint(20, 50)  # tempo estimado de entrega em minutos

        if endereco:
            dispatcher.utter_message(text=f"Sua pizza será entregue em {endereco} dentro de aproximadamente {tempo} minutos.")
        else:
            dispatcher.utter_message(text="Para simular a entrega, preciso do seu endereço.")
        
        return []
