import requests
import json
import os
from PIL import Image
from io import BytesIO

class Lox:
    def twirl(self, forest):
        # modify forest state
        pass

    def leap(self, forest):
        # modify forest state
        pass

    def spin(self, forest):
        # modify forest state
        pass

class Drako:
    def twirl(self, forest):
        # modify forest state
        pass

    def leap(self, forest):
        # modify forest state
        pass

    def spin(self, forest):
        # modify forest state
        pass

class Forest:
    def __init__(self):
        self.state = {
            'fireflies': False,
            'rain': False,
            'rainbow': False,
            'butterflies': False,
            'wind': False,
            'fog': False,
            'flowers': False,
            'stars': False,
            'moonlight': False
        }

    def fireflies(self):
        self.state['fireflies'] = True

    def rain(self):
        self.state['rain'] = True

    def rainbow(self):
        self.state['rainbow'] = True

    def butterflies(self):
        self.state['butterflies'] = True

    def wind(self):
        self.state['wind'] = True

    def fog(self):
        self.state['fog'] = True

    def flowers(self):
        self.state['flowers'] = True

    def stars(self):
        self.state['stars'] = True

    def moonlight(self):
        self.state['moonlight'] = True

def simulate_dance(lox_moves, drako_moves):
    forest = Forest()
    lox = Lox()
    drako = Drako()

    for lox_move, drako_move in zip(lox_moves, drako_moves):
        if lox_move == 'twirl' and drako_move == 'twirl':
            forest.fireflies()
        elif lox_move == 'leap' and drako_move == 'spin':
            forest.rain()
        elif lox_move == 'spin' and drako_move == 'leap':
            forest.rainbow()
        elif lox_move == 'twirl' and drako_move == 'leap':
            forest.butterflies()
        elif lox_move == 'leap' and drako_move == 'leap':
            forest.wind()
        elif lox_move == 'spin' and drako_move == 'spin':
            forest.fog()
        elif lox_move == 'leap' and drako_move == 'twirl':
            forest.flowers()
        elif lox_move == 'spin' and drako_move == 'twirl':
            forest.stars()
        elif lox_move == 'twirl' and drako_move == 'spin':
            forest.moonlight()

        print(f"After sequence {lox_move} + {drako_move}, the forest state is: {forest.state}")

    return forest.state


# def simulate_dance(lox_moves, drako_moves):
#     forest = Forest()
#     lox = Lox()
#     drako = Drako()

#     url = "https://sbp-gctfs-offsite24-oai.openai.azure.com/openai/deployments/dalle3/images/generations?api-version=2023-12-01-preview"
#     headers = {
#         "Authorization": "Bearer c6793551a72640a6957c02df798df68e",
#         "Content-Type": "application/json"
#     }

#     for i, (lox_move, drako_move) in enumerate(zip(lox_moves, drako_moves), 1):
#         getattr(lox, lox_move)(forest)
#         getattr(drako, drako_move)(forest)

#         prompt = f"After sequence {lox_move} + {drako_move}, the forest state is: {forest.state}"
#         print(prompt)

#         data = {
#             "prompt": prompt
#         }

#         response = requests.post(url, headers=headers, data=json.dumps(data))

#         if response.status_code == 200:
#             print("Request was successful.")
#             image_data = response.json()['imageData']
#             image = Image.open(BytesIO(base64.b64decode(image_data)))
#             image.save(os.path.join('download', f'sequence_{i}.png'))
#         else:
#             print(f"Request failed with status code {response.status_code}.")

#     return forest.state




lox_moves = ['twirl', 'leap', 'spin', 'twirl', 'leap']
drako_moves = ['spin', 'twirl', 'leap', 'leap', 'spin']

simulate_dance(lox_moves, drako_moves)