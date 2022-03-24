from django.shortcuts import render
from django.http import JsonResponse

from rest_framework.response import Response
from rest_framework.decorators import api_view
#from serializer import lolvs

import chrome_auto_upgrade
from fow_champion_id import champ_id

# show: 웹 브라우저를 띄우지 않는 headless chrome 옵션 적용
driver = chrome_auto_upgrade.get_driver(show_browser=False)
# driver = webdriver.Chrome("chromedriver.exe", options=options)
#driver.implicitly_wait(1)  # 로딩 완료되면 1초 기다리기

# Create your views here.


def index(requests):
    context = {}

    return render(requests, "lolvs/index.html", context=context)
    # return render(requests, "index.html", context=context)


def search(requests):
    myChampion = requests.POST["myChampion"]
    enemyChampion = requests.POST["enemyChampion"]

    return render(
        requests,
        "lolvs/search.html",
        {"myChampion": myChampion, "enemyChampion": enemyChampion},
    )
    
def viewJson(requests):
    return JsonResponse("REST API end point...",safe=False)

"""def crawlMaster(requests):
    myChampion = requests.GET["myChampion"] + " is my champ"
    enemyChampion = requests.GET["enemyChampion"] + " is enemy champ"
    print(myChampion,enemyChampion)
    
    return JsonResponse({"myChampion":myChampion,"enemyChampion":enemyChampion})"""

def crawlMaster(requests):

    
    myChampion = requests.GET["myChampion"]
    enemyChampion = requests.GET["enemyChampion"] # vstip 을 위해서 필요
    
    
    url = f"http://fow.kr/champranking#{champ_id[myChampion]}"
    driver.get(url)  # op.gg <-- 여기가 엄청 오래걸림
    
    driver.execute_script('window.open("about:blank", "_blank");')  # new tab for lol.ps
    tabs = driver.window_handles  # <-- 탭 관리
    driver.switch_to.window(tabs[0])
    
    
    croll_masters = driver.find_element_by_id("r_out")
    top5 = croll_masters.find_elements_by_css_selector("a")[:5]
    
    masters = {i+1:top5[i].text for i in range(len(top5))}
    print(masters)
    
    return JsonResponse(masters)
