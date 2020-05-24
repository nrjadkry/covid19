import requests,json
from django.shortcuts import render
from django.http import JsonResponse

from .forms import CovidForm


from rest_framework.views import APIView
from rest_framework.response import Response


# Create your views here.
def home(request):
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

	context={
	'country':cov['country'],
	'all':cov['cases']['total'],
	'recovered': cov['cases']['recovered'],
	'deaths': cov['deaths']['total'],
	'new': cov['cases']['new'],
	'serious': cov['cases']['critical'],
	}
	# print(cov)

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
			
				labels=['Red', 'Blue', 'Yellow', 'Green', 'Purple', 'Orange']
				default_items=[159,145,123,17]
				data={
				"labels":labels,
				"default":default_items,
				
				}
				return Response(data)
