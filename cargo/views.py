from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Driver, Dispatcher, Client, Order


def driver_list(request):
    return render(request, 'driver_list.html', {'drivers': Driver.objects.all()})

def dispatcher_list(request):
    return render(request, 'dispatcher_list.html', {'dispatchers': Dispatcher.objects.all()})

def client_list(request):
    return render(request, 'client_list.html', {'clients': Client.objects.all()})

def order_list(request):
    return render(request, 'order_list.html', {
        'orders': Order.objects.select_related('driver', 'dispatcher', 'client')
    })



def driver_detail(request, pk):
    driver = get_object_or_404(Driver, pk=pk)
    return render(request, 'driver_detail.html', {
        'driver': driver,
        'orders': driver.Orders.all()
    })

def dispatcher_detail(request, pk):
    dispatcher = get_object_or_404(Dispatcher, pk=pk)
    return render(request, 'dispatcher_detail.html', {
        'dispatcher': dispatcher,
        'orders': dispatcher.Orders.all()
    })

def client_detail(request, pk):
    client = get_object_or_404(Client, pk=pk)
    return render(request, 'client_detail.html', {
        'client': client,
        'orders': client.Orders.all()
    })

def order_detail(request, pk):
    order = get_object_or_404(Order, pk=pk)
    return render(request, 'order_detail.html', {'order': order})



def order_create(request):
    if request.method == 'POST':
        name_order = request.POST.get('name_order')
        price = request.POST.get('price')
        delivery_address = request.POST.get('delivery_address') 

       
        if not name_order or not price or not delivery_address:
            return render(request, 'logistic/order_form.html', {
                'error': 'Заполните обязательные поля: название, цена, адрес.',
            })

        try:
            price = int(price)
        except ValueError:
            return render(request, 'logistic/order_form.html', {
                'error': 'Цена должна быть числом.',
            })

        order = Order(
            name_order=name_order,
            price=price,
            delivery_address=delivery_address,
            creation_date=timezone.now(), 
        )
        order.save()
        return redirect('order_detail', pk=order.pk)


    return render(request, 'order_form.html', {
        
    })


# Задание на дом добавить возможность для страницы диспетчера назначать заказы на себя и на свободных водителей


def operators_page(request):

    if request.method == "GET":

        new_orders = Order.objects.filter(
            driver__isnull=True,
            dispatcher__isnull=True
        )

        drivers = Driver.objects.filter(
            Orders__isnull=True
        )

        context = {
            "new_orders": new_orders,
            "drivers": drivers
        }

        return render(request, "operators.html", context)

    if request.method == "POST":

    
        order_id = request.POST.get("order_id")
        driver_id = request.POST.get("driver_id")
        dispatcher_id = request.POST.get("dispatcher_id")


        order = get_object_or_404(
            Order,
            id=order_id,
            driver__isnull=True,
            dispatcher__isnull=True
        )

       
        dispatcher = get_object_or_404(
            Dispatcher,
            id=dispatcher_id
        )

    
        order.dispatcher = dispatcher

      
        if driver_id:

            driver = get_object_or_404(
                Driver,
                id=driver_id,
                Orders__isnull=True
            )

            order.driver = driver

    
        order.save()

        return redirect("operators_page")



# Create your views here.
