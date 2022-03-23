import os
from urllib.parse import urlparse

import chrome_auto_upgrade

            
def fetch_top5_masters():

    
    driver = chrome_auto_upgrade.get_driver(
        show_browser=False,  # show: 웹 브라우저를 띄우지 않는 headless chrome 옵션 적용
    )
    # driver = webdriver.Chrome("chromedriver.exe", options=options)
    #driver.implicitly_wait(1)  # 로딩 완료되면 1초 기다리기
    
    url = "https://www.op.gg/champions/diana/jungle/build"
    driver.get(url)  # op.gg
    driver.execute_script('window.open("about:blank", "_blank");')  # new tab for lol.ps
    tabs = driver.window_handles  # <-- 탭 관리
    driver.switch_to.window(tabs[0])
    
    driver.switch_to.window(tabs[0])  # op.gg 탭으로 이동
    champ ='kassadin'
    opggURL = f"https://www.op.gg/champion/{champ}/statistics"  # need vs!!!
    driver.get(opggURL)

    croll_masters = driver.find_elements_by_class_name("summoner")
    
    name_list = []
    url_list = []
    for master in croll_masters:
        name_list.append(master.text)
        master_url = master.get_attribute("href")
        url_list.append(master_url)
    print(name_list)
    print(url_list)
    
    
    return name_list


print(fetch_top5_masters())
