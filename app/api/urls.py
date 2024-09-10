from django.urls import path
from ninja import NinjaAPI

api_v1 = NinjaAPI(title='SIMS API', version='v1')

urlpatterns = [
    path('v1/', api_v1.urls),
]
