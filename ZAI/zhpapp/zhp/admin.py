from django.contrib import admin
from .models import Harcerz, Druzyna, Harcerz_w_druzynie, Stopien, Stopien_harcerza
# Register your models here.
admin.site.register(Harcerz)
admin.site.register(Druzyna)
admin.site.register(Harcerz_w_druzynie)
admin.site.register(Stopien)
admin.site.register(Stopien_harcerza)