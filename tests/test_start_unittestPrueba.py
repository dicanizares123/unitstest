import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
import time # Opcional, por si necesitas ver qué pasa

class FindByIdName(unittest.TestCase):
    
    # 1. Este método se ejecuta AUTOMÁTICAMENTE antes de cada prueba
    def setUp(self):
        # Aquí inicializamos el driver (como tenías en la línea 4)
        self.driver = webdriver.Edge()
        # OJO: Verifica si debes usar la URL de tu código o la de la foto del deber.
        # En la foto del deber (Imagen 2) usan esta:
        self.driver.get("https://kfjaramillo.github.io/PaginaPruebas/")
        
    # 2. Este es tu caso de prueba real
    def testIdName(self):
        # Aquí pegas tu lógica de búsqueda, pero agregando "self." antes de driver
        
        # Buscar por ID (Tu línea 8)
        elemento = self.driver.find_element(By.ID, "noImportante")
        
        if elemento is not None:
            print("El elemento by ID fue encontrado")

        # Buscar por NAME (Tu línea 13)
        elemento2 = self.driver.find_element(By.NAME, "ultimo")
        
        if elemento2 is not None:
            print("El elemento by NAME fue encontrado")

    # 3. El tearDown se usa para cerrar, aunque en tu foto no lo piden explícitamente aún,
    # es buena práctica o puedes dejar que se cierre solo al acabar el script.
    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()