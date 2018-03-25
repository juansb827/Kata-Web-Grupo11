import random
import sys

import os

__author__ = 'asistente'
from unittest import TestCase
from selenium import webdriver
from selenium.webdriver.common.by import By

class FunctionalTest(TestCase):

    randomId=str(random.randrange(1000))

    def setUp(self):
        self.browser = webdriver.Chrome(executable_path=r"files/chromedriver.exe")
        self.browser.implicitly_wait(2)

    def tearDown(self):
        self.browser.quit()

    def test_title(self):
        self.browser.get('http://localhost:8000')
        self.assertIn('Busco Ayuda', self.browser.title)


    def test_registro(self):
        self.browser.get('http://localhost:8000')
        link = self.browser.find_element_by_id('id_register')
        link.click()

        nombre = self.browser.find_element_by_id('id_nombre')
        nombre.send_keys('Juan Daniel')

        apellidos = self.browser.find_element_by_id('id_apellidos')
        apellidos.send_keys('Arevalo')

        experiencia = self.browser.find_element_by_id('id_aniosExperiencia')
        experiencia.send_keys('5')

        self.browser.find_element_by_xpath("//select[@id='id_tiposDeServicio']/option[text()='Desarrollador Web']").click()
        telefono = self.browser.find_element_by_id('id_telefono')
        telefono.send_keys('3173024578')

        correo = self.browser.find_element_by_id('id_correo')
        correo.send_keys('jd.patino1'+FunctionalTest.randomId+'@uniandes.edu.co')

        imagen = self.browser.find_element_by_id('id_imagen')
        ruta= os.path.join(sys.path[0], "polls/files", 'daisy.jpg')
        imagen.send_keys(ruta)

        nombreUsuario = self.browser.find_element_by_id('id_username')
        nombreUsuario.send_keys('juan645'+FunctionalTest.randomId)

        clave = self.browser.find_element_by_id('id_password')
        clave.send_keys('clave123')

        botonGrabar = self.browser.find_element_by_id('id_grabar')
        botonGrabar.click()
        self.browser.implicitly_wait(3)
        span=self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')

        self.assertIn('Juan Daniel Arevalo', span.text)


    def test_verDetalle(self):
        self.browser.get('http://localhost:8000')
        span=self.browser.find_element(By.XPATH, '//span[text()="Juan Daniel Arevalo"]')
        span.click()

        h2=self.browser.find_element(By.XPATH, '//h2[text()="Juan Daniel Arevalo"]')

        self.assertIn('Juan Daniel Arevalo', h2.text)


    def test_login_independiente(self):
        self.browser.get('http://localhost:8000/login')
        campoUsuario = self.browser.find_element_by_id('usrname')
        campoUsuario.send_keys('juan645')
        campoClave = self.browser.find_element_by_id('psw')
        campoClave.send_keys('clave123')
        botonLogin = self.browser.find_element_by_id('id_login')
        botonLogin.click()
        self.browser.implicitly_wait(3)
        self.assertIn('Login exitoso juan645', self.browser.title)



    def test_edit_user(self):
        self.browser.get('http://localhost:8000/login')
        campoUsuario = self.browser.find_element_by_id('usrname')
        campoUsuario.send_keys('juan645')
        campoClave = self.browser.find_element_by_id('psw')
        campoClave.send_keys('clave123')
        botonLogin = self.browser.find_element_by_id('id_login')
        botonLogin.click()

        self.browser.implicitly_wait(3)

        self.browser.get('http://localhost:8000/')


        self.browser.execute_script('document.getElementById("id_editar").click()')

        self.browser.implicitly_wait(3)

        new_correo="js.bedoya170@uniandes.edu.co"
        correo = self.browser.find_element_by_id('id_correo')
        correo.clear()
        correo.send_keys(new_correo)

        self.browser.implicitly_wait(5)

        self.browser.find_element_by_id('id_update').click()

        self.browser.execute_script('document.getElementById("id_editar").click()')
        self.browser.implicitly_wait(3)

        self.assertEqual( self.browser.find_element_by_id('id_correo').get_attribute("value") , new_correo )


