import requests,json
from django.shortcuts import render
from django.http import JsonResponse

from .forms import CovidForm

from datetime import datetime

import requests
from rest_framework.views import APIView
from rest_framework.response import Response


today=datetime.today()

# Create your views here.
def home(request):

	url1 = "https://covid-193.p.rapidapi.com/statistics"

	headers1 = {
	    'x-rapidapi-host': "covid-193.p.rapidapi.com",
	    'x-rapidapi-key': "a37f2cca17msh79bff66e7a04eaap1de657jsn42fb0aaff772"
	    }

	response = requests.request("GET", url1, headers=headers1).json()

	data=response['response']
	lst=[]

	for x in range(226):


		d=data[x]

		# print(d)

		temp={
		'country':d['country'],
		'all':d['cases']['total'],
		'deaths': d['deaths']['total']
		}
		if not (d['country']=='All' or d['country']=='Europe' or d['country']=='North-America' or d['country']=='Asia' or d['country']=='South-America' or d['country']=='Africa'):
			lst.append(temp)
	
	def myFunc(e):
		return e['all']

	lst.sort(reverse=True, key=myFunc)
	# print(lst)

	form=CovidForm(request.POST)
	if request.method == 'POST':
		if form.is_valid:
			country=request.POST.get('country','')

		
	else:
		country='Nepal'

	url = "https://covid-193.p.rapidapi.com/statistics"

	querystring = {"country":country}


	headers = {
	'x-rapidapi-host': "covid-193.p.rapidapi.com",
	'x-rapidapi-key': "be7f37114bmsh38c0486c35a5050p1bc1e5jsnf574155ad041"
	}
	response = requests.request("GET", url, headers=headers, params=querystring).json()

	data=response['response']

	cov=data[0]



	url5 = "https://nepalcorona.info/api/v1/news"


	response = requests.request("GET", url5).json()

	data1=response['data']

	d=data1[25]

	# print(d)


	# print(data)

	allnews=[]

	# countNews=d.count()

	for news in range(25):
		d=data1[news]


		newsdata={
		'title':d['title'],
		'summary':d['summary'],
		'url':d['url']

		}
		allnews.append(newsdata)

	# print(allnews)





	context={
	'data':lst,
	'country':cov['country'],
	'all':cov['cases']['total'],
	'recovered': cov['cases']['recovered'],
	'deaths': cov['deaths']['total'],
	'new': cov['cases']['new'],
	'serious': cov['cases']['critical'],
	'today':today,
	'allnews':allnews
	}


	return render(request, 'livedata/index.html',context)

def get_data(request,*args,**kwargs):
		data={
		"sales":100,
		"customer":10,
		}
		return JsonResponse(data)


class ChartData(APIView):

			authentication_classes = []
			permission_classes = []

			def get(self, request, format=None):

				# url = "https://data.nepalcorona.info/api/v1/covid/timeline"

				# headers = {
				# 	'x-rapidapi-host': "covid-193.p.rapidapi.com",
				# 	'x-rapidapi-key': "be7f37114bmsh38c0486c35a5050p1bc1e5jsnf574155ad041"
				# 	}
				# response = requests.request("GET", url).json()

				# data=response['result']

				# d=data[0]

				# print(data)

				# data=response['response']

				# print(data[0])








			
				labels=['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
				default_items=[159,145,123,17]
				data={
				"labels":labels,
				"default":default_items,
				
				}
				return Response(data)
