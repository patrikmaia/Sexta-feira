from _ast import Import
import pyautogui
import webbrowser
import time
import selenium
import datetime

pyautogui.PAUSE = 0.5
edge = pyautogui.locateCenterOnScreen ( "edge.PNG", confidence=0.7 )
if edge:
    pyautogui.click (edge)

while True:
    try:
        img = pyautogui.locateCenterOnScreen ( "clicarnocampoanexo.PNG", confidence=0.7 )
        if img:
            pyautogui.click ( img )
    except:
        time.sleep(1)
    else:
        break

while True:
    try:
        baixaranexo = pyautogui.locateCenterOnScreen ( "baixaranexo.PNG", confidence=0.7 )
        if baixaranexo:
            pyautogui.click ( baixaranexo )
    except:
        time.sleep(1)
    else:
        break

while True:
    try:
        donwload = pyautogui.locateCenterOnScreen ( "donwload.PNG", confidence=0.7 )
        if donwload:
            pyautogui.click (donwload)
    except:
        time.sleep(1)
    else:
        break

while True:
    try:
        abrirnota = pyautogui.locateCenterOnScreen ( "abrirnota.PNG", confidence=0.7 )
        if abrirnota:
            pyautogui.doubleClick ( abrirnota )
    except:
        time.sleep(1)
    else:
       break

while True:
    try:
        chavedeacesso = pyautogui.locateCenterOnScreen ( "chavedeacesso.PNG", confidence=0.7 )
        if chavedeacesso:
            pyautogui.tripleClick(chavedeacesso)
            pyautogui.hotkey('ctrl', 'c')
    except:
        time.sleep(1)
    else:
        break
while True:
    try:
        fsist = pyautogui.locateCenterOnScreen ( "fsist.PNG", confidence=0.7 )
        if fsist:
            pyautogui.click (fsist)
    except:
        time.sleep(1)
    else:
        break
try:
    time.sleep (2)
    anuncio = pyautogui.locateCenterOnScreen ( "anuncio.PNG", confidence=0.7 )
except:
    # continua normal
    print ( 'ok' )
else:
    pyautogui.click(anuncio)
try:
    time.sleep(1)
    anuncio2 = pyautogui.locateCenterOnScreen( "anuncio2.PNG", confidence=0.7 )
except:
    print('ok')
else:
    pyautogui.click(anuncio2)

while True:
    try:
        digiteachave = pyautogui.locateCenterOnScreen ( "digiteachave.PNG", confidence=0.7 )
        if digiteachave:
            pyautogui.tripleClick( digiteachave )
            pyautogui.hotkey ( 'ctrl', 'v' )
            pyautogui.press ( 'enter' )
    except:
        time.sleep(1)
    else:
        break
while True:
    try:
        captcha = pyautogui.locateCenterOnScreen ( "captcha.PNG", confidence=0.7 )
        if captcha:
            pyautogui.click(captcha)
    except:
        time.sleep(1)
    else:
        break

while True:
    try:
        baixarxml = pyautogui.locateCenterOnScreen ( "baixarxml.PNG", confidence=0.7 )
        if baixarxml:
            pyautogui.click ( baixarxml )
    except:
        time.sleep(1)
    else:
        break
while True:
    try:
        pastaD = pyautogui.locateCenterOnScreen ( "pastaD.PNG", confidence=0.7 )
        if pastaD:
            pyautogui.click ( pastaD )
    except:
        time.sleep(1)
    else:
        break
while True:
    try:
        copiarxml = pyautogui.locateCenterOnScreen ( "copiarxml.PNG", confidence=0.7 )
        if copiarxml:
            pyautogui.click ( copiarxml )
            pyautogui.hotkey ( 'ctrl', 'c' )
    except:
        time.sleep(1)
    else:
        break

# Abre o siagri
siagri2 = pyautogui.locateCenterOnScreen ( "siagri2.PNG", confidence=0.7 )
if siagri2:
        pyautogui.click(siagri2)
try:
    #segunda imagem do siagri
    time.sleep(2)
    siagri = pyautogui.locateCenterOnScreen ( "siagri.PNG", confidence=0.7 )
except:
    #continua normal
    print('ok')
else:
    pyautogui.click(siagri)

pyautogui.click(489,177)
while True:
    try:
        pastasiagri = pyautogui.locateCenterOnScreen ( "pastasiagri.PNG", confidence=0.7 )
        if pastasiagri:
            pyautogui.click ( pastasiagri )
            pyautogui.hotkey ( 'ctrl', 'v' )
            time.sleep(3)
            pyautogui.press ( 'enter' )
    except:
        time.sleep(1)
    else:
        break
time.sleep(2)
#Confirma a inclusão do ct-e
pyautogui.click(1015,610)
time.sleep(1)
pyautogui.click(827, 316)
pyautogui.press ( 't' )
pyautogui.press ( 'enter' )
pyautogui.press ( 'enter' )
pyautogui.press ( 'enter' )
pyautogui.press ( 'enter' )
pyautogui.press ( 'enter' )
pyautogui.press ( 'enter' )
pyautogui.write ( '5' )
pyautogui.press ( 'enter' )
pyautogui.press ( 'enter' )
#If para descobrir o cfop correto
pyautogui.write ( '135329' )
pyautogui.press ( 'enter' )
try:
    #capturar o aviso na tela
    time.sleep ( 2 )
    janeladeerro = pyautogui.locateCenterOnScreen ( "janeladeerro.PNG", confidence=0.7 )
except:
    print('ok')
else:
    pyautogui.press('enter')
    time.sleep (1)
    pyautogui.write('235329')
    pyautogui.press ('enter')
time.sleep(0.5)
pyautogui.click ( 770, 576 )
time.sleep (2)
pyautogui.click ( 708, 647 )
time.sleep(0.5)
pyautogui.click ( 980, 573 )
time.sleep (1)
pyautogui.click ( 1034, 601 )

condpgto = pyautogui.locateCenterOnScreen ( "condpgto.PNG", confidence=0.7 )
if condpgto:
     pyautogui.click ( condpgto )
     pyautogui.write ( '1' )
     pyautogui.press ( 'enter' )
     pyautogui.write ( '090' )
     pyautogui.press ( 'enter' )
valores = pyautogui.locateCenterOnScreen ( "valores.PNG", confidence=0.7 )
if valores:
     pyautogui.click ( valores )
     time.sleep ( 0.5 )
totaldofrete = pyautogui.locateCenterOnScreen ( "totaldofrete.PNG", confidence=0.7 )
if totaldofrete:
     pyautogui.click ( totaldofrete )
     pyautogui.press ( 'enter' )

apagaraliquota = pyautogui.locateCenterOnScreen ( "apagaraliquota.PNG", confidence=0.7 )
if apagaraliquota:
     pyautogui.doubleClick ( apagaraliquota )
     pyautogui.press ( 'delete' )
     pyautogui.click ( 1284, 914 )
     time.sleep ( 1 )
confirmar = pyautogui.locateCenterOnScreen ( "confirmar.PNG", confidence=0.7 )
if confirmar:
     pyautogui.doubleClick ( confirmar )
     time.sleep ( 1 )
     pyautogui.click ( 1284, 914 )
     time.sleep ( 1 )
novodoc = pyautogui.locateCenterOnScreen ( "novodoc.PNG", confidence=0.7 )
if novodoc:
     pyautogui.click ( novodoc )
     time.sleep ( 1 )
     pyautogui.write ( '11000221' )
     pyautogui.press ( 'enter' )
     pyautogui.press ( 'tab' )
     pyautogui.press ( 'enter' )

edge = pyautogui.locateCenterOnScreen ( "edge.PNG", confidence=0.7 )
if edge:
     pyautogui.click ( edge )
     time.sleep ( 1 )

numerodanota = pyautogui.locateCenterOnScreen ( "numerodanota.PNG", confidence=0.7 )
if numerodanota:
     pyautogui.doubleClick ( numerodanota )
     pyautogui.hotkey ( 'ctrl', 'c' )
     pyautogui.click (siagri2)
     #Loop para encontrar segunda imagem do icone do siagri
     try:
         time.sleep ( 2 )
         siagri = pyautogui.locateCenterOnScreen ( "siagri.PNG", confidence=0.7 )
     except:
         # continua normal
         print ( 'ok' )
     else:
       pyautogui.click(siagri)

     time.sleep ( 1 )
     pyautogui.hotkey ( 'ctrl', 'v' )
     pyautogui.press ( 'enter' )
     pyautogui.press ( 'enter' )
     pyautogui.write ( '1' )
     time.sleep ( 1 )
     pyautogui.click ( 1269, 955 )
     time.sleep ( 1 )
     pyautogui.click ( 807, 908 )

#Calcula a data de vencimento
pyautogui.click(609,329)
pyautogui.press('left')
pyautogui.press('left')
data_atual = datetime.date.today()
dia = int(data_atual.strftime('%d'))
mes = int(data_atual.strftime('%m'))
if dia <=5 and dia>0 :
    data = datetime.date(data_atual.year,data_atual.month,15)
elif dia >5 and dia<=15:
    data = datetime.date(data_atual.year,data_atual.month,25)
elif dia>15 and mes < 12:
    data = datetime.date(data_atual.year,int(data_atual.month)+1,15)
else:
    data = datetime.date(int(data_atual.year)+1,1,15)
data_em_texto = data.strftime('%d%m%Y')
pyautogui.write(data_em_texto)

#Seleciona a forma de pagamento
pyautogui.click(779,596)
pyautogui.click(728,650)
pyautogui.click ( 807, 908 )
time.sleep(1)
#Botão concluir
pyautogui.click(1280,952)

# Gravar processo
pyautogui.click(1308, 912)
time.sleep(2)
try:
    time.sleep (1)
    ctecomplementar = pyautogui.locateCenterOnScreen ( "ctecomplementar.PNG", confidence=0.7 )
except:
    pyautogui.alert(' Ct-e complementar. Verificar com o time fiscal liberação de senha para o lançamento')

pyautogui.alert('Concluído')

#Criar estrutura de repetição
#Criar diretorio para pegar o número dos cards.
