from django.urls import path,include
from rest_framework.routers import DefaultRouter
from humanhealth.views import Foodview
from humanhealth.views import Sleepview
from humanhealth.views import Waterview
from humanhealth.views import WalkView
from humanhealth.views import LocationView,Mobileview

router = DefaultRouter()
router.register("food",Foodview,basename="Food")
router.register("sleep",Sleepview,basename="Sleep" )
router.register("water",Waterview, basename="Water")
router.register("walk",WalkView,basename="walk")
router.register("Mobile",Mobileview,basename="Mobile")
router.register("location",LocationView,basename="Location")

urlpatterns=[
    path("", include(router.urls))
]