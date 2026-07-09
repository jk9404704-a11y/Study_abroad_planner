
# Register your models here.
from django.contrib import admin
from .models import Country, University, Scholarship,IELTS,Budget,DocumentChecklist,Application,Timeline,Contact

admin.site.register(Country)
admin.site.register(University)
admin.site.register(Scholarship)
admin.site.register(IELTS)
admin.site.register(Budget)
admin.site.register(DocumentChecklist)
admin.site.register(Application)
admin.site.register(Timeline)
admin.site.register(Contact)
