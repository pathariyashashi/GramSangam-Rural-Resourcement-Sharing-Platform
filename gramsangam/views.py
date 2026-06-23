from django.shortcuts import render
from .models import (
    Equipment,
    EquipmentBooking,
    UserProfile,
    Worker,
    WorkerBooking,
    Transport,
    TransportBooking
)
from django.shortcuts import render, get_object_or_404, redirect
import requests
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from .models import WorkerHireRequest
from .models import UserProfile
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import (
    FarmingGuide,
    GovernmentScheme,
    DailyTip,
    EducationVideo,
    MandiPrice,
    AgricultureNews
    
)

def home(request):
    return render(request, 'home.html')


def equipment(request):

    equipments = Equipment.objects.all()

    return render(
        request,
        'equipment.html',
        {
            'equipments': equipments
        }
    )


def workers(request):

    workers = Worker.objects.all()

    skill = request.GET.get("skill")

    if skill:
        workers = workers.filter(skill=skill)

    return render(
        request,
        "workers.html",
        {
            "workers": workers
        }
    )


#def transport(request):
   # return render(request, 'transport.html')


def education(request):
    return render(request, 'education.html')

def login_page(request):

    if request.method == "POST":

        email = request.POST.get('email')
        password = request.POST.get('password')
        login_type = request.POST.get('login_type')

        user = authenticate(
            username=email,
            password=password
        )

        if user is not None:

            try:

                profile = UserProfile.objects.get(
                    user=user
                )

                # Owner Login
                if (
                    login_type == "Owner"
                    and profile.profession == "Owner"
                ):

                    login(request, user)

                    return redirect(
                        'owner_dashboard'
                    )

                # Customer Login
                elif (
                    login_type == "Customer"
                    and profile.profession == "Customer"
                ):

                    login(request, user)

                    return redirect(
                        'home'
                    )

                else:

                    return render(
                        request,
                        'login.html',
                        {
                            'error':
                            'Wrong Account Type Selected'
                        }
                    )

            except UserProfile.DoesNotExist:

                return render(
                    request,
                    'login.html',
                    {
                        'error':
                        'Profile Not Found'
                    }
                )

        return render(
            request,
            'login.html',
            {
                'error':
                'Invalid Email or Password'
            }
        )

    return render(
        request,
        'login.html'
    )



def register_page(request):

    if request.method == "POST":

        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')

        profession = request.POST.get('role')
        address = request.POST.get('address')

        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')

        if password != confirm_password:

            return render(
                request,
                'register.html',
                {
                    'error': 'Passwords do not match'
                }
            )

        if User.objects.filter(username=email).exists():

            return render(
                request,
                'register.html',
                {
                    'error': 'Email already registered'
                }
            )

        user = User.objects.create_user(
            username=email,
            email=email,
            first_name=name,
            password=password
        )

        UserProfile.objects.create(
    user=user,
    mobile=mobile,
    profession=profession,
    address=address
    )

        return redirect('login')

    return render(
        request,
        'register.html'
    )

def equipment_detail(request, id):

    equipment = get_object_or_404(
        Equipment,
        id=id
    )

    return render(
        request,
        'equipment_detail.html',
        {
            'equipment': equipment
        }
    )


def book_equipment(request, id):

    equipment = get_object_or_404(
        Equipment,
        id=id
    )

    if request.method == "POST":

        renter_name = request.POST['renter_name']
        mobile = request.POST['mobile']
        aadhaar_number = request.POST['aadhaar_number']
        start_date = request.POST['start_date']
        end_date = request.POST['end_date']

        EquipmentBooking.objects.create(
            equipment=equipment,
            renter_name=renter_name,
            mobile=mobile,
            aadhaar_number=aadhaar_number,
            start_date=start_date,
            end_date=end_date,
            total_days=1,
            total_amount=equipment.rent_per_day,
        )

        return redirect('/equipment/')

    return render(
        request,
        'booking_form.html',
        {
            'equipment': equipment
        }
    )
def workers(request):

    workers = Worker.objects.all()

    return render(
        request,
        'workers.html',
        {
            'workers': workers
        }
    )    
def worker_booking(request, id):

    worker = get_object_or_404(
        Worker,
        id=id
    )

    if request.method == "POST":

        customer_name = request.POST.get("customer_name")
        mobile = request.POST.get("mobile")
        village = request.POST.get("village")
        work_date = request.POST.get("work_date")

        days_required = request.POST.get("days_required")

        WorkerBooking.objects.create(
            worker=worker,
            customer_name=customer_name,
            mobile=mobile,
            village=village,
            work_date=work_date,
            days_required=days_required,
            total_amount=int(days_required) * worker.wage_per_day
        )
        return redirect('/workers/')
    
    return render(
        request,
        "worker_booking.html",
        {
            "worker": worker
        }
    )
def worker_detail(request, id):

    worker = get_object_or_404(
        Worker,
        id=id
    )

    return render(
        request,
        'worker_detail.html',
        {
            'worker': worker
        }
    )
    
    
@login_required
def owner_dashboard(request):

    return render(
        request,
        'owner_dashboard.html'
    )    
    


@login_required
def add_equipment(request):

    if request.method == "POST":

        Equipment.objects.create(
            owner=request.user,
            name=request.POST.get('name'),
            category=request.POST.get('category'),
            owner_name=request.user.first_name,
            owner_mobile=request.POST.get('mobile'),
            location=request.POST.get('location'),
            rent_per_day=request.POST.get('rent'),
            security_deposit=request.POST.get('deposit'),
            description=request.POST.get('description'),
            rules=request.POST.get('rules'),
            image=request.FILES.get('image')
        )

        return redirect('owner_dashboard')

    return render(
        request,
        'add_equipment.html'
    )    
    
@login_required
def my_equipments(request):

    equipments = Equipment.objects.filter(
        owner=request.user
    )

    return render(
        request,
        'my_equipments.html',
        {
            'equipments': equipments
        }
    )    
    
@login_required
def equipment_requests(request):

    requests = EquipmentBooking.objects.filter(
        equipment__owner=request.user
    )

    return render(
        request,
        'equipment_requests.html',
        {
            'requests': requests
        }
    )    
    
@login_required
def approve_booking(request, id):

    booking = EquipmentBooking.objects.get(id=id)

    booking.booking_status = "Approved"
    booking.save()

    equipment = booking.equipment

    equipment.available = False
    equipment.save()

    return redirect('equipment_requests')

@login_required
def reject_booking(request, id):

    booking = EquipmentBooking.objects.get(id=id)

    booking.booking_status = "Rejected"

    booking.save()

    return redirect('equipment_requests')    

@login_required
def add_worker(request):

    if request.method == "POST":

        Worker.objects.create(
            owner=request.user,
            name=request.POST.get('name'),
            skill=request.POST.get('skill'),
            mobile=request.POST.get('mobile'),
            location=request.POST.get('location'),
            experience=request.POST.get('experience'),
            wage_per_day=request.POST.get('wage_per_day'),
            description=request.POST.get('description'),
            image=request.FILES.get('image')
        )

        return redirect('owner_dashboard')

    return render(
        request,
        'add_worker.html'
    )
@login_required
def my_workers(request):

    workers = Worker.objects.filter(
        owner=request.user
    )

    return render(
        request,
        'my_workers.html',
        {
            'workers': workers
        }
    )    
@login_required
def worker_requests(request):

    requests = WorkerBooking.objects.filter(
        worker__owner=request.user
    ).order_by('-id')

    return render(
        request,
        'worker_requests.html',
        {
            'requests': requests
        }
    )
    
@login_required
def accept_worker_request(request, id):

    req = get_object_or_404(
        WorkerBooking,
        id=id
    )

    req.booking_status = "Accepted"
    req.save()

    return redirect('worker_requests')


@login_required
def reject_worker_request(request, id):

    req = get_object_or_404(
        WorkerBooking,
        id=id
    )

    req.booking_status = "Rejected"
    req.save()

    return redirect('worker_requests')

from django.contrib.auth.decorators import login_required

@login_required
def add_transport(request):

    if request.method == "POST":

        print("FORM SUBMITTED")

        transport = Transport.objects.create(
            owner=request.user,
            vehicle_name=request.POST.get('vehicle_name'),
            vehicle_type=request.POST.get('vehicle_type'),
            owner_mobile=request.POST.get('owner_mobile'),
            location=request.POST.get('location'),
            rent_per_day=request.POST.get('rent_per_day'),
            description=request.POST.get('description'),
            image=request.FILES.get('image')
        )

        print("TRANSPORT SAVED:", transport.id)

        return redirect('owner_dashboard')

    return render(
        request,
        'add_transport.html'
    )

def transport(request):

    transports = Transport.objects.all().order_by('-id')

    print("TOTAL TRANSPORTS =", transports.count())

    return render(
        request,
        'transport.html',
        {
            'transports': transports
        }
    )
    
def transport_detail(request, id):

    transport = get_object_or_404(
        Transport,
        id=id
    )

    return render(
        request,
        'transport_detail.html',
        {
            'transport': transport
        }
    )    
    
    
@login_required
def book_transport(request, id):

    transport = get_object_or_404(
        Transport,
        id=id
    )

    if request.method == "POST":

        TransportBooking.objects.create(
            transport=transport,
            user=request.user,
            customer_name=request.POST.get('customer_name'),
            mobile=request.POST.get('mobile'),
            pickup_location=request.POST.get('pickup_location'),
            drop_location=request.POST.get('drop_location'),
            booking_date=request.POST.get('booking_date')
        )

        return redirect('transport')

    return render(
        request,
        'transport_booking.html',
        {
            'transport': transport
        }
    )


@login_required
def transport_requests(request):

    requests = TransportBooking.objects.filter(
        transport__owner=request.user
    ).order_by('-id')

    return render(
        request,
        'transport_requests.html',
        {
            'requests': requests
        }
    )


@login_required
def accept_transport_request(request, id):

    req = get_object_or_404(
        TransportBooking,
        id=id
    )

    req.booking_status = "Accepted"
    req.save()

    return redirect('transport_requests')


@login_required
def reject_transport_request(request, id):

    req = get_object_or_404(
        TransportBooking,
        id=id
    )

    req.booking_status = "Rejected"
    req.save()

    return redirect('transport_requests') 


@login_required
def my_transport_bookings(request):

    bookings = TransportBooking.objects.filter(
        user=request.user
    ).order_by('-id')

    return render(
        request,
        'my_transport_bookings.html',
        {
            'bookings': bookings
        }
    )   
    
def logout_user(request):
    logout(request)
    return redirect('home')    

from django.contrib.auth.decorators import login_required

@login_required
def my_bookings(request):

    worker_bookings = WorkerBooking.objects.filter(
        user=request.user
    ).order_by('-id')

    transport_bookings = TransportBooking.objects.filter(
        user=request.user
    ).order_by('-id')

    equipment_bookings = EquipmentBooking.objects.filter(
        user=request.user
    ).order_by('-id')

    return render(
        request,
        'my_bookings.html',
        {
            'worker_bookings': worker_bookings,
            'transport_bookings': transport_bookings,
            'equipment_bookings': equipment_bookings
        }
    )
    
@login_required
def transport_payment(request, id):

    booking = get_object_or_404(
        TransportBooking,
        id=id
    )

    booking.payment_status = "Paid"

    booking.save()

    return render(
        request,
        'payment_success.html'
    )    
    

def education(request):

    guides = FarmingGuide.objects.all().order_by('-id')

    schemes = GovernmentScheme.objects.all().order_by('-id')

    tips = DailyTip.objects.all().order_by('-id')[:5]

    videos = EducationVideo.objects.all().order_by('-id')

    mandi_prices = MandiPrice.objects.all().order_by('-id')

    news = AgricultureNews.objects.all().order_by('-id')

    weather = None

    try:

        city = "Harsud"

        api_key = "9eed842ba78ab16cabbd72a7cf72f7ab"

        url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

        response = requests.get(url)

        data = response.json()

        weather = {
            'city': city,
            'temp': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'wind': data['wind']['speed'],
            'description': data['weather'][0]['description']
        }

    except:
        weather = None

    return render(
        request,
        'education.html',
        {
            'guides': guides,
            'schemes': schemes,
            'tips': tips,
            'videos': videos,
            'weather': weather,
            'mandi_prices': mandi_prices,
            'news': news
        }
    )