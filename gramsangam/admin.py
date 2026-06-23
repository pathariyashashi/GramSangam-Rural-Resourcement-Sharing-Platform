from django.contrib import admin
from .models import Equipment, EquipmentBooking
from .models import Worker
from .models import WorkerHireRequest
from .models import *
from .models import (
    Worker,
    Equipment,
    EquipmentBooking,
    WorkerHireRequest,
    FarmingGuide,
    GovernmentScheme,
    DailyTip,
    EducationVideo,
)

admin.site.register(WorkerHireRequest)
admin.site.register(Worker)
admin.site.register(Equipment)
admin.site.register(EquipmentBooking)


admin.site.register(FarmingGuide)
admin.site.register(GovernmentScheme)
admin.site.register(DailyTip)
admin.site.register(EducationVideo)
admin.site.register(MandiPrice)
admin.site.register(AgricultureNews)