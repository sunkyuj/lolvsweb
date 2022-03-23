import os
from urllib.parse import urlparse
#from selenium.webdriver.common.desired_capabilities import DesiredCapabilities 

import chrome_auto_upgrade
import json

            
def fetch_top5_masters():


    driver = chrome_auto_upgrade.get_driver(
        show_browser=False,  # show: 웹 브라우저를 띄우지 않는 headless chrome 옵션 적용
    )
    # driver = webdriver.Chrome("chromedriver.exe", options=options)
    #driver.implicitly_wait(1)  # 로딩 완료되면 1초 기다리기
    
    champ_id ='131'
    
    url = f"http://fow.kr/champranking#{champ_id},30,cmd,p,S12"
    driver.get(url)  # op.gg <-- 여기가 엄청 오래걸림
    
    driver.execute_script('window.open("about:blank", "_blank");')  # new tab for lol.ps
    tabs = driver.window_handles  # <-- 탭 관리
    driver.switch_to.window(tabs[0])
    
    
    croll_masters = driver.find_element_by_id("r_out")
    top5 = croll_masters.find_elements_by_css_selector("a")[:5]
    
    masters = {i+1:top5[i] for i in range(len(top5))}
    

    return json.dumps(masters)



