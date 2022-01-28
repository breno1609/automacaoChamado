import pyautogui
import pyperclip
import time

#ABRIR O SISTEMA
pyautogui.hotkey("ctrl", "t")
pyautogui.sleep(5)
pyautogui.write("https://secportal.com.br/logon.asp")
pyautogui.press("enter")
pyautogui.sleep(4)
pyautogui.write("")#MATRICULA
pyautogui.hotkey("tab")
pyautogui.sleep(5)
pyautogui.write("")#SENHA
pyautogui.sleep(5)
pyautogui.hotkey("enter")
pyautogui.sleep(30)

#ABRIR CHAMADO
pyautogui.click(x=1154, y=170)
pyautogui.sleep(5)
pyautogui.click(x=352, y=266)
pyautogui.sleep(5)
pyautogui.click(x=501, y=252)
pyautogui.sleep(3)
pyautogui.click(x=823, y=700)
pyautogui.sleep(2)
pyautogui.click(x=492, y=257)
pyautogui.sleep(30)
pyautogui.click(x=225, y=206)
pyautogui.write("")#NOME DO ALUNO
pyautogui.sleep(1)
pyautogui.hotkey("tab")

pyautogui.write("")#MATRICULA DO ALUNO
pyautogui.sleep(1)
pyautogui.hotkey("tab")

pyautogui.write("")#CPF DO ALUNO
pyautogui.sleep(1)

pyautogui.click(x=359, y=372)#SETA DAS OPÇÕES DE SOLICITAÇÃO
pyautogui.sleep(2)

pyautogui.click(x=211, y=499)#OPÇÃO REGULARIZAÇÃO ACADEMICA
pyautogui.sleep(1)

pyautogui.click(x=257, y=373)#SETA DE OPÇÃO DE TIPO DE REGULARIZAÇÃO
pyautogui.sleep(2)

pyautogui.click(x=279, y=419)#OPÇÃO ACERTOS ACADEMICOS
pyautogui.sleep(2)

pyautogui.click(x=165, y=466)#CLICA NA BARRA DE PESQUISA DE CAMPUS
pyautogui.write("PARALELA")
pyautogui.sleep(2)

pyautogui.click(x=199, y=524)#BARRA DE PESQUISA PERIODO
pyautogui.write("2022.1")

pyautogui.click(x=253, y=569)#SETA OPÇÃO BOLSISTA
pyautogui.sleep(1)

pyautogui.click(x=87, y=632)#OPÇÃO SIM DE BOLSISTA
pyautogui.sleep(1)

pyautogui.click(x=223, y=622)#BARRA DEPESQUISA TIPO DE BOLSA
pyautogui.sleep(2)

pyautogui.write("MIGRACAO")
pyautogui.sleep(2)

pyautogui.click(x=324, y=676)#BARRA DE PESQUISA MENSAGEM
pyautogui.sleep(2)

pyautogui.write("TESTS")
pyautogui.sleep(2)

pyautogui.click(x=1229, y=707)#OPÇÃO COFIRMAR 1º PAGINA
pyautogui.sleep(25)

pyautogui.click(x=172, y=605)#OPÇÃO CANCELARº PAGINA
pyautogui.sleep(4)

pyautogui.click(x=740, y=179)

#DESCOBRIR A POSIÇÃO DO CURSOR
pyautogui.sleep(8)
pyautogui.position()
