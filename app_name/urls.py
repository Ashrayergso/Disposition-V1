```python
from django.urls import path
from . import views

urlpatterns = [
    path('ship_sailing_schedules/', views.ship_sailing_schedule_list, name='ship_sailing_schedule_list'),
    path('assignments/automatic/', views.automatic_assignment, name='automatic_assignment'),
]
```