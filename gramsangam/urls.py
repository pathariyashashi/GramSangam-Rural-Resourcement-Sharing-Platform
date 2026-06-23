from django.urls import path
from . import views

urlpatterns =[

    path('', views.home, name='home'),

    path('equipment/', views.equipment, name='equipment'),


    path('workers/', views.workers, name='worker_list'),

    path('worker/<int:id>/', views.worker_detail, name='worker_detail'),

    path(
        'worker-booking/<int:id>/',
        views.worker_booking,
        name='worker_booking'
    ),

    path('education/', views.education, name='education'),

    path('login/', views.login_page, name='login'),

    path('register/', views.register_page, name='register'),

    path(
        'equipment/<int:id>/',
        views.equipment_detail,
        name='equipment_detail'
    ),

    path(
        'equipment/book/<int:id>/',
        views.book_equipment,
        name='book_equipment'
    ),
    
    path(
    'owner-dashboard/',
    views.owner_dashboard,
    name='owner_dashboard'
),
    
    path(
    'add-equipment/',
    views.add_equipment,
    name='add_equipment'
),
    
    path(
    'my-equipments/',
    views.my_equipments,
    name='my_equipments'
),
    path(
    'equipment-requests/',
    views.equipment_requests,
    name='equipment_requests'
),
    
    path(
    'approve-booking/<int:id>/',
    views.approve_booking,
    name='approve_booking'
),

path(
    'reject-booking/<int:id>/',
    views.reject_booking,
    name='reject_booking'
),
path(
    'add-worker/',
    views.add_worker,
    name='add_worker'
),
path(
    'my-workers/',
    views.my_workers,
    name='my_workers'
),

path(
    'worker-requests/',
    views.worker_requests,
    name='worker_requests'
),

path(
    'accept-worker-request/<int:id>/',
    views.accept_worker_request,
    name='accept_worker_request'
),

path(
    'reject-worker-request/<int:id>/',
    views.reject_worker_request,
    name='reject_worker_request'
),

path(
    'transport/',
    views.transport,
    name='transport'
),

path(
    'add-transport/',
    views.add_transport,
    name='add_transport'
),

path(
    'transport/<int:id>/',
    views.transport_detail,
    name='transport_detail'
),

path(
    'book-transport/<int:id>/',
    views.book_transport,
    name='book_transport'
),

path(
    'transport-requests/',
    views.transport_requests,
    name='transport_requests'
),

path(
    'accept-transport-request/<int:id>/',
    views.accept_transport_request,
    name='accept_transport_request'
),

path(
    'reject-transport-request/<int:id>/',
    views.reject_transport_request,
    name='reject_transport_request'
),

path(
    'my-transport-bookings/',
    views.my_transport_bookings,
    name='my_transport_bookings'
),

path(
    'logout/',
    views.logout_user,
    name='logout'
),

path(
    'my-bookings/',
    views.my_bookings,
    name='my_bookings'
),

path(
    'transport-payment/<int:id>/',
    views.transport_payment,
    name='transport_payment'
),
path(
    'education/',
    views.education,
    name='education'
),
]
