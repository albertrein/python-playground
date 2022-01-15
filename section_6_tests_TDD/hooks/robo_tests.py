import unittest
from robo import Robo

class RoboTests(unittest.TestCase):

    def setUp(self) -> None:
        self.bumblee_bee = Robo('Bumblee Bee', bateria=33)
        print('Starting Tests')
        return super().setUp()
    
    def tearDown(self) -> None:
        print('Finishing Tests')
        return super().tearDown()
    
    def test_carregar(self):
        self.assertEqual(self.bumblee_bee.bateria, 33)
        self.bumblee_bee.carregar()
        self.assertEqual(self.bumblee_bee.bateria, 100)
    
    def test_speak(self):
        self.assertEqual(self.bumblee_bee.speak(), 'Olá, eu sou Bumblee Bee')
        self.assertEqual(self.bumblee_bee.bateria, 32)
        self.bumblee_bee._bateria = 0
        self.assertEqual(self.bumblee_bee.speak(), 'Bateria Fraca. Por favor recarregue')

if __name__ == '__main__':
    unittest.main()
