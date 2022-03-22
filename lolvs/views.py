from django.shortcuts import render

# Create your views here.


def base(requests):
    context = {}

    return render(requests, "lolvs/base.html", context=context)
    # return render(requests, "index.html", context=context)


def search(requests):
    myChampion = requests.POST["myChampion"]
    enemyChampion = requests.POST["enemyChampion"]

    return render(
        requests,
        "lolvs/search.html",
        {"myChampion": myChampion, "enemyChampion": enemyChampion},
    )
