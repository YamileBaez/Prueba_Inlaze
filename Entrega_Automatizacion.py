from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import pandas as pd
import time


chrome_driver_path ="C:\Selenium\chromedriver.exe"

service = Service(executable_path=chrome_driver_path)
driver = webdriver.Chrome(service=service)


#username = "yam.baez@hotmail.com"
#password = "JuliJuli2023*"
#url = "https://test-qa.inlaze.com/auth/sign-in"
#Registro = "https://test-qa.inlaze.com/auth/sign-up"
#Accesok = "https://test-qa.inlaze.com/panel"

#Nombre = "Gi Yamiz"
#Email = "Giset.jimenez@gmail.com"
#NewPass = "JuliJuli2023*"
#RNewPass = "JuliJuli2023*"


data = pd.read_excel("Casos_de_Uso_Final.xlsx")




for index, row in data.iterrows():
	ID = row['ID']
username = row['username']
password = row['password']
url = row['url']
Registro = row['Registro']
Accesok = row['Accesok']
Nombre = row['Nombre']
Email = row['Email']
NewPass = row['NewPass']
RNewPass = row['RNewPass']

driver.get(url)

try:#PE05
	print("SC00 -- Inicia el proceso con el identificador: ",ID)
	elemento_inicial = WebDriverWait(driver, 10).until(
		EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-sign-in/main/section[1]/app-sign-in-form/h1"))
	)
	print("SC05 -- La pantalla inicial se ha cargado completamente, continua con el flujo")

	try:#PE10
		time.sleep(3)
		username_field = WebDriverWait(driver, 10).until(
    	EC.presence_of_element_located((By.XPATH, "//*[@id='email']"))
	)
		username_field.clear()
		username_field.send_keys(username)


		time.sleep(1)
		contrasena_field = WebDriverWait(driver, 10).until(
    	EC.visibility_of_element_located((By.XPATH, "/html/body/app-root/app-sign-in/main/section[1]/app-sign-in-form/form/div[2]/app-password/div/input"))
	)
		contrasena_field.clear()
		contrasena_field.send_keys(password)

		#print("VAL01 -- ingresa a validar si se habilito o no el boton")
		login_button = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.XPATH, "/html/body/app-root/app-sign-in/main/section[1]/app-sign-in-form/form/button"))
    )
		if login_button.is_enabled():
			print("SC15 -- El botón está habilitado, Formatos correctos en usuario y contraseña")
		
			login_button.click()
			time.sleep(1)

			try:#SC25

				success_message = driver.find_element(By.XPATH,"/html/body/app-root/app-toasts-container/div/app-toast/div/div[2]")
				if "Password doesn't match" in success_message.text:
					print("PE20 -- Contraseña Incorrecta.")
				else:
					#raise Exception("Login exitoso.")
					if "User not found" in success_message.text:
						print("PE25 -- Usuario no existe, Avanza a la pantalla de registro")
						driver.execute_script("window.open('');")
						driver.switch_to.window(driver.window_handles[1])
						driver.get(Registro)
						time.sleep(4)

						try:#SC30

							elemento_inicial = WebDriverWait(driver, 10).until(
							EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-sign-up/main/section[2]/app-sign-up-form/form/div[1]/input"))
						)
							print("SC30 -- La pantalla de registro se ha cargado completamente, continua con el flujo")
							
							if driver.current_url == Registro:
								print("SC35 -- Redirección exitosa a la URL esperada.")
							
								username2_field = WebDriverWait(driver, 10).until(
    							EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-sign-up/main/section[2]/app-sign-up-form/form/div[1]/input"))
							)
								username2_field.clear()
								username2_field.send_keys(Nombre)
								time.sleep(1)

								Email_field = WebDriverWait(driver, 10).until(
    							EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-sign-up/main/section[2]/app-sign-up-form/form/div[2]/input"))
							)
								Email_field.clear()
								Email_field.send_keys(Email)
								time.sleep(1)

								Contrasena2_field = WebDriverWait(driver, 10).until(
    							EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-sign-up/main/section[2]/app-sign-up-form/form/div[3]/app-password/div/input"))
							)
								Contrasena2_field.clear()
								Contrasena2_field.send_keys(NewPass)
								time.sleep(1)

								RContrasena2_field = WebDriverWait(driver, 10).until(
    							EC.presence_of_element_located((By.XPATH, "/html/body/app-root/app-sign-up/main/section[2]/app-sign-up-form/form/div[4]/app-password/div/input"))
							)
								RContrasena2_field.clear()
								RContrasena2_field.send_keys(RNewPass)
								time.sleep(1)

								login_button = WebDriverWait(driver, 10).until(
        						EC.visibility_of_element_located((By.XPATH, "/html/body/app-root/app-sign-up/main/section[2]/app-sign-up-form/form/button"))
        					)
								
								if login_button.is_enabled():
									print("SC40 -- El botón está habilitado, Formatos correctos en nombres, correo, contraseña, rcontraseña")
									
									login_button.click()
									time.sleep(2)
									try:#PE45
										success_message = driver.find_element(By.XPATH,"/html/body/app-root/app-toasts-container/div/app-toast/div/div[2]")
										if "Successful registration!" in success_message.text:
											print("SE45 -- Registro Exitoso")

											username_field = WebDriverWait(driver, 10).until(
    										EC.presence_of_element_located((By.XPATH, "//*[@id='email']"))
										)
											username_field.clear()
											username_field.send_keys(Email)


											time.sleep(1)
											contrasena_field = WebDriverWait(driver, 10).until(
    										EC.visibility_of_element_located((By.XPATH, "/html/body/app-root/app-sign-in/main/section[1]/app-sign-in-form/form/div[2]/app-password/div/input"))
										)
											contrasena_field.clear()
											contrasena_field.send_keys(NewPass)

											login_button = WebDriverWait(driver, 10).until(
        									EC.visibility_of_element_located((By.XPATH, "/html/body/app-root/app-sign-in/main/section[1]/app-sign-in-form/form/button"))
    									)

											login_button.click()
											time.sleep(1)

											if driver.current_url == Accesok:
												print("SC35 -- Redirección exitosa a la URL esperada.")
												print("SC99 -- Proceso finalizado con:  ", Email,"FIN.")
												time.sleep(3)
												driver.execute_script("window.open('');")
												driver.switch_to.window(driver.window_handles[1])
												driver.get(url)
											else:
												print("PE35 -- Redirección NO exitosa la URL no es la esperada.")




										else:
											print("PE45 -- Registro NO Exitoso.")
									except Exception as e:
										print("PE45 -- ERROR INESPERADO CONTROLADO, FALLO EN EL PROCESO DE REGISTRO:	", e)





								else:
									print("PE40 -- El botón no está habilitado, Formatos incorrectos en nombres, correo, contraseña o rcontraseña.")





							else:
								print("PE35 -- Redirección NO exitosa la URL no es la esperada.")

						




						except Exception as e:
							print("PE30 -- ERROR INESPERADO CONTROLADO, FALLO EN PANTALLA DE REGISTRO	", e)


				

					











					else:
						print("SC25,01 -- Usuario Correcto, se loguea")
			except Exception as e:
				print("SC25 -- Usuario y contraseña Correcta, se loguea	")

		

		else:
			print("PE15 -- No se habilita el boton de SIGN IN, Formatos incorrectos en usuario o contraseña")

		




	except Exception as e:
		print("PE10 -- Campo correo no cumple con el formato:", e)









except Exception as e:
    print("PEO5 -- Pagina no encontrada o no carga los componentes:", e)



finally:
    # Esperar algunos segundos para ver el resultado y luego cerrar el navegador
    time.sleep(10)
    driver.quit()