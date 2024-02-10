from django.shortcuts import render
from django.shortcuts import HttpResponse
from lyyf.models import UserInfo, Site, Restaurant,City
from django.http import JsonResponse
from django.db.models import Q
import json
from django.core.serializers import serialize

# Create your views here.
#用户界面
def index(request):
    user_data_list = UserInfo.objects.all()
    json_data = serialize('json', UserInfo.objects.all())
    return JsonResponse(json_data)
def site(request):
    if (request.method == 'GET'):
        json_data = serialize('json', Site.objects.all())
        return JsonResponse(json_data)
    request.session['site'] = request.POST.get('site')  #这里是html中城市的名字
    return None
def restaurant(request):
    json_data = serialize('json', Restaurant.objects.all())
    return JsonResponse(json_data)
def search(request):
    if (request.method == 'POST'):
        data_get = request.POST.get("city")
        json_data = serialize('json',City.objects.filter(Q(Province=data_get) | Q(PLAD=data_get)|Q(CLAD=data_get)|Q(TLAD=data_get)))
        return JsonResponse(json_data)
#由于要给ai投喂行程的日期，景点，城市，所以要用到下面的方法传递数据
def days_choose(request):
    if (request.method == 'POST'):
        data_get = request.POST.get("day")
        request.session['day'] = data_get
    return None
def preferences(request):
    if request.method == "POST":
        json_data = json.loads(request.body)
        request.session['preferences'] = json_data
    return None
def choice(request):
    preferences = request.session.get('preferences')
    days = request.session.get('day')
    if days is not None:
        pass
    return None
def mapping(request):
    keyword = request.POST.get()
    city = request.session.get('site')
    list = {'address': keyword, 'city': city}
    json.dumps(list)
    return JsonResponse(list)


"""def login(request):
    if request.method == 'POST':
        user_data_list = UserInfo.objects.all()"""




