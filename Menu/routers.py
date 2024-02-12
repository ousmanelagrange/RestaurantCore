#./routers.py

from rest_framework import routers
from Menu.views import MenuViewset

router = routers.SimpleRouter()
router.register(r'menu', MenuViewset, basename="menu")

urlpatterns = router.urls