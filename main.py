import pyautogui
import time

pyautogui.alert('O código será executado!')
pyautogui.PAUSE = 0.1
listApp = ['google', 'vscode', 'terminal', 'spotify']

listSite = ['https://odoo.kamico.com.br/web#action=169&model=project.task&view_type=list&cids=&menu_id=102',
            'https://web.whatsapp.com/',
            'localhost:14069/web/database/selector']

def clickSuper():
    pyautogui.moveTo(1980, 1)
    pyautogui.click()

def openAPP(listApp, listSite):
    for app in listApp:
        if app == 'google':
            pyautogui.press('win')
            pyautogui.write(app)
            pyautogui.press('enter')
            time.sleep(1)

            for site in listSite:
                pyautogui.write(site)
                pyautogui.press('enter')
                pyautogui.hotkey('ctrl', 't')
                time.sleep(1)
        else:
            pyautogui.press('win')
            pyautogui.write(app)
            pyautogui.press('enter')

openAPP(listApp, listSite)