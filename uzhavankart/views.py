import os
import cloudinary
cloudinary.config(
    cloud_name=os.environ.get('CLOUDINARY_CLOUD_NAME'),
    api_key=os.environ.get('CLOUDINARY_API_KEY'),
    api_secret=os.environ.get('CLOUDINARY_API_SECRET'),
)
from django.shortcuts import render,get_object_or_404, redirect

# Create your views here.
# uzhavankart/views.py

from django.shortcuts import render


def home(request):
    return render(request, 'uk/home.html')

def admin_dashboard(request):
    return render(request, 'uk/admin.html')

def farmer_dashboard_man(request):
    return render(request, 'uk/farmer.html')

def employee_dashboard(request):
    return render(request, 'uk/employee.html')

def farmer_register(request):
    return render(request, 'uk/register.html')

def farmer_update(request):
    return render(request, 'uk/update.html')

def farmer_delete(request):
    return render(request, 'uk/delete.html')

def market_price_add(request):
    return render(request, 'uk/add.html')

def market_price_update(request):
    return render(request, 'uk/update.html')

def market_price_view(request):
    return render(request, 'uk/view.html')


from django.shortcuts import render, redirect
from .forms import FarmerForm, PriceUpdateForm

def farmer_register(request):
    if request.method == 'POST':
        form = FarmerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('farmer-view')
    else:
        form = FarmerForm()
    return render(request, 'uk/register.html', {'form': form})


from django.shortcuts import render
from .models import Farmer

def farmer_view(request):
    query = request.GET.get('farmer_id')
    if query:
        farmers = Farmer.objects.filter(farmer_id__icontains=query)
    else:
        farmers = Farmer.objects.all()
        
    return render(request, 'uk/farmer_view.html', {'farmers': farmers})

def farmer_view_agent(request):
    query = request.GET.get('farmer_id')
    if query:
        farmers = Farmer.objects.filter(farmer_id__icontains=query)
    else:
        farmers = Farmer.objects.all()
        
    return render(request, 'uk/farmer_view_agent.html', {'farmers': farmers})

from django.shortcuts import render, get_object_or_404
from .models import Farmer
from .forms import FarmerUpdateForm

def update_farmer_view(request):
    farmer = None
    form = None
    updated = False
    error = None

    if request.method == 'POST':
        farmer_id = request.POST.get('farmer_id')

        if 'fetch' in request.POST:
            try:
                farmer = Farmer.objects.get(farmer_id=farmer_id)
                form = FarmerUpdateForm(instance=farmer)
            except Farmer.DoesNotExist:
                error = "Farmer ID not found."

        elif 'update' in request.POST:
            farmer = get_object_or_404(Farmer, farmer_id=farmer_id)
            form = FarmerUpdateForm(request.POST, request.FILES, instance=farmer)
            if form.is_valid():
                form.save()
                updated = True
            else:
                error = "Form is invalid."

    return render(request, 'uk/update_farmer.html', {
        'form': form,
        'farmer': farmer,
        'updated': updated,
        'error': error
    })

from django.shortcuts import render, get_object_or_404, redirect
from .models import Farmer

def delete_farmer_view(request):
    farmer = None
    deleted = False
    error = None

    if request.method == 'POST':
        farmer_id = request.POST.get('farmer_id')

        if 'fetch' in request.POST:
            try:
                farmer = Farmer.objects.get(farmer_id=farmer_id)
            except Farmer.DoesNotExist:
                error = "Farmer ID not found."

        elif 'delete' in request.POST:
            try:
                farmer = Farmer.objects.get(farmer_id=farmer_id)
                farmer.delete()
                deleted = True
                farmer = None
            except Farmer.DoesNotExist:
                error = "Farmer already deleted or not found."

    return render(request, 'uk/delete_farmer.html', {
        'farmer': farmer,
        'deleted': deleted,
        'error': error,
    })


from django.shortcuts import render, redirect
from .forms import ProductForm

def add_product(request):
    if request.method == "POST":
        form = ProductForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, 'uk/product_add.html', {'form': ProductForm(), 'success': True})
    else:
        form = ProductForm()
    return render(request, 'uk/product_add.html', {'form': form})


from django.shortcuts import render, get_object_or_404, redirect
from .models import Product


def product_list(request):
     products = Product.objects.all()
     return render(request, 'uk/product_list.html', {'products': products})

def update_price(request, pk):
    product = get_object_or_404(Product, pk=pk)
    if request.method == 'POST':
        form = PriceUpdateForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('product_list')
    else:
        form = PriceUpdateForm(instance=product)
    return render(request, 'uk/update_price.html', {'form': form, 'product': product})


from django.shortcuts import render
from .models import Product  # adjust this based on your actual model name

def market_price_view(request):
    categories = ['Vegetables', 'Fruits', 'Oils', 'Seeds']
    selected_category = request.GET.get('category', 'All')

    if selected_category == 'All':
        products = Product.objects.all()
    else:
        products = Product.objects.filter(category=selected_category)

    context = {
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
    }
    return render(request, 'uk/market_price.html', context)

from django.shortcuts import render
from .models import Product  # adjust this based on your actual model name

def footer_market_price_view(request):
    categories = ['Vegetables', 'Fruits', 'Oils', 'Seeds']
    selected_category = request.GET.get('category', 'All')

    if selected_category == 'All':
        products = Product.objects.all()
    else:
        products = Product.objects.filter(category=selected_category)

    context = {
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
    }
    return render(request, 'uk/footer_market_price.html', context)


from django.shortcuts import render
from .models import Product  # adjust this based on your actual model name

def agent_market_price_view(request):
    categories = ['Vegetables', 'Fruits', 'Oils', 'Seeds']
    selected_category = request.GET.get('category', 'All')

    if selected_category == 'All':
        products = Product.objects.all()
    else:
        products = Product.objects.filter(category=selected_category)

    context = {
        'products': products,
        'categories': categories,
        'selected_category': selected_category,
    }
    return render(request, 'uk/agent_market_price.html', context)

from django.shortcuts import render
from .forms import EmployeeForm

def employee_register(request):
    success_message = None
    if request.method == "POST":
        form = EmployeeForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            success_message = "Employee registered successfully!"
            form = EmployeeForm()  # reset form after success
    else:
        form = EmployeeForm()

    return render(request, "uk/employee_register.html", {
        "form": form,
        "success_message": success_message
    })


from django.shortcuts import render, get_object_or_404
from .models import Employee

def employee_search(request):
    employee = None
    emp_id = None
    error = None

    if request.method == "POST":
        emp_id = request.POST.get("emp_id")
        try:
            employee = Employee.objects.get(emp_id=emp_id)
        except Employee.DoesNotExist:
            error = "No employee found with this ID."

    return render(request, "uk/employee_search.html", {
        "employee": employee,
        "emp_id": emp_id,
        "error": error
    })


from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee
from .forms import EmployeeUpdateForm

def employee_update(request):
    employee = None
    form = None
    emp_id = None
    error = None

    if request.method == "POST":
        emp_id = request.POST.get("emp_id")

        # If emp_id is entered
        if emp_id and not request.POST.get("name"):
            try:
                employee = Employee.objects.get(emp_id=emp_id)
                form = EmployeeUpdateForm(instance=employee)
            except Employee.DoesNotExist:
                error = "Employee ID not found."

        # If form is submitted with updated data
        elif request.POST.get("name"):
            employee = get_object_or_404(Employee, emp_id=request.POST.get("emp_id_hidden"))
            form = EmployeeUpdateForm(request.POST, request.FILES, instance=employee)
            if form.is_valid():
                form.save()
                return render(request, "uk/employee_update.html", {
                    "form": form,
                    "employee": employee,
                    "success": "Employee details updated successfully!"
                })
    return render(request, "uk/employee_update.html", {
        "form": form,
        "employee": employee,
        "error": error,
        "emp_id": emp_id
    })


from django.shortcuts import render, get_object_or_404, redirect
from .models import Employee

def employee_delete(request):
    employee = None
    success = None
    error = None

    if request.method == "POST":
        # Step 1: Fetch employee
        emp_id = request.POST.get("emp_id")
        emp_id_hidden = request.POST.get("emp_id_hidden")

        if emp_id:  
            try:
                employee = Employee.objects.get(emp_id=emp_id)
            except Employee.DoesNotExist:
                error = "Employee not found!"
        
        # Step 2: Confirm delete
        elif emp_id_hidden and "confirm_delete" in request.POST:
            try:
                employee = Employee.objects.get(emp_id=emp_id_hidden)
                employee.delete()
                success = f"Employee {emp_id_hidden} deleted successfully!"
                employee = None
            except Employee.DoesNotExist:
                error = "Employee not found!"

    return render(request, "uk/employee_delete.html", {
        "employee": employee,
        "success": success,
        "error": error,
    })



from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Employee
from .forms import EmployeeLoginForm

def employee_login(request):
    if request.method == "POST":
        form = EmployeeLoginForm(request.POST)
        if form.is_valid():
            emp_id = form.cleaned_data['emp_id']

            try:
                employee = Employee.objects.get(emp_id=emp_id)

                # Save session
                request.session['employee_id'] = employee.emp_id
                request.session['employee_role'] = employee.job_role.lower()

                # Redirect based on role
                role = employee.job_role.lower()
                if role == "admin":
                    return redirect("admin-dashboard")
                elif role == "hub":
                    return redirect("hub-dashboard")
                elif role == "agent":
                    return redirect("agent-dashboard")
                elif role == "transport":
                    return redirect("transport-dashboard")
                elif role == "delivery":
                    return redirect("delivery-dashboard")
                elif role == "farmer":
                    return redirect("farmer-dashboard")
                else:
                    messages.error(request, "Unknown role assigned to this employee!")
                    return redirect("employee-login")

            except Employee.DoesNotExist:
                messages.error(request, "Employee ID not found!")

    else:
        form = EmployeeLoginForm()

    return render(request, "uk/employee_login.html", {"form": form})

def agent_dashboard(request):
    return render(request, "uk/agent.html")


def admin_dashboard(request):
    return render(request, "uk/admin.html")

def market_dashboard(request):
    return render(request, "uk/market.html")


def hub_dashboard(request):
    return render(request, "uk/hub_dashboard.html")
from django.shortcuts import render, redirect
from django.db.models import Sum
from .models import Employee, Farmer, Stock,Order
from django.db.models import Sum
from django.db.models.functions import TruncMonth, TruncDate
from django.shortcuts import render
from .models import Order

def admin_dashboard(request):
    emp_id = request.session.get("employee_id")
    employee = None

    total_employee = Employee.objects.count()
    total_farmers = Farmer.objects.count()
    total_orders = Order.objects.count()  

    if emp_id:
        try:
            employee = Employee.objects.get(emp_id=emp_id)
        except Employee.DoesNotExist:
            return redirect("employee-login")

    # --- STOCK DATA for donut graph ---
    stock_data = (
        Stock.objects.values("stock_type")
        .annotate(total_qty=Sum("quantity_kg"))
        .order_by("stock_type")
    )

    stock_labels = [item["stock_type"] for item in stock_data]
    stock_values = [float(item["total_qty"]) for item in stock_data]

    context = {
        "employee": employee,
        "total_employee": total_employee,
        "total_farmers": total_farmers,
        "total_orders": total_orders,
        "stock_labels": stock_labels,   # pass to template
        "stock_values": stock_values,   # pass to template
    }
    return render(request, "uk/admin.html", context)



def hub_dashboard(request):
    emp_id = request.session.get("employee_id")
    employee = None

    total_employee = Employee.objects.count()
    total_farmers = Farmer.objects.count()
    total_orders = Order.objects.count() 

    if emp_id:
        try:
            employee = Employee.objects.get(emp_id=emp_id)
        except Employee.DoesNotExist:
            return redirect("employee-login")

    # --- STOCK DATA for donut graph ---
    stock_data = (
        Stock.objects.values("stock_type")
        .annotate(total_qty=Sum("quantity_kg"))
        .order_by("stock_type")
    )

    stock_labels = [item["stock_type"] for item in stock_data]
    stock_values = [float(item["total_qty"]) for item in stock_data]

    context = {
        "employee": employee,
        "total_employee": total_employee,
        "total_farmers": total_farmers,
        "total_orders": total_orders,
        "stock_labels": stock_labels,   # pass to template
        "stock_values": stock_values,   # pass to template
    }
    return render(request, "uk/hub_dashboard.html", context)

def agent_dashboard(request):
   emp_id = request.session.get("employee_id")
   employee = None

   total_employee = Employee.objects.count()
   total_farmers = Farmer.objects.count()
   total_orders = Order.objects.count()   

   if emp_id:
        try:
            employee = Employee.objects.get(emp_id=emp_id)
        except Employee.DoesNotExist:
            return redirect("employee-login")

    # --- STOCK DATA for donut graph ---
   stock_data = (
        Stock.objects.values("stock_type")
        .annotate(total_qty=Sum("quantity_kg"))
        .order_by("stock_type")
    )

   stock_labels = [item["stock_type"] for item in stock_data]
   stock_values = [float(item["total_qty"]) for item in stock_data]

   context = {
        "employee": employee,
        "total_employee": total_employee,
        "total_farmers": total_farmers,
        "total_orders": total_orders,
        "stock_labels": stock_labels,   # pass to template
        "stock_values": stock_values,   # pass to template
    }
   return render(request, "uk/agent.html", context)




from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage

def contact_view(request):
    if request.method == "POST":
        name = request.POST.get("name")
        mobileno = request.POST.get("mobileno")
        message_text = request.POST.get("message")

        if name and mobileno and message_text:
            ContactMessage.objects.create(
                name=name,
                mobileno=mobileno,
                message=message_text
            )
            messages.success(request, "Your message has been sent successfully!")
            return redirect('contact')
        else:
            messages.error(request, "Please fill in all fields.")

    return render(request, "uk/contact.html")


from django.shortcuts import render, redirect, get_object_or_404
from .models import ContactMessage
from django.contrib import messages

# Admin view all messages
def admin_contact_messages(request):
    messages_list = ContactMessage.objects.all().order_by('-created_at')
    return render(request, 'uk/admin_messages.html', {'messages_list': messages_list})

# Mark query as resolved
def mark_query_over(request, message_id):
    msg = get_object_or_404(ContactMessage, id=message_id)
    msg.is_resolved = True
    msg.save()
    messages.success(request, f"Query from {msg.name} marked as resolved!")
    return redirect('admin_messages')


from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import CropProductForm
from .models import CropProduct, Farmer   # ✅ import Farmer model

def add_crop_product(request):
    if request.method == "POST":
        form = CropProductForm(request.POST)
        if form.is_valid():
            crop = form.save(commit=False)

            farmer_id = request.POST.get("farmer_id")

            if farmer_id:
                try:
                    # ✅ Check if Farmer exists
                    farmer = Farmer.objects.get(farmer_id=farmer_id)
                    crop.farmer_id = farmer.farmer_id  # assign valid farmer_id
                    crop.save()
                    messages.success(request, f"Crop product added successfully for Farmer {farmer.name}!")
                    return redirect('crop_view')  # change to your crop list page
                except Farmer.DoesNotExist:
                    messages.error(request, "Invalid Farmer ID! Please check again.")
            else:
                messages.error(request, "Farmer ID is required!")
    else:
        form = CropProductForm()

    return render(request, 'uk/add_product.html', {'form': form})



from django.shortcuts import render
from .models import CropProduct
from .forms import FarmerSearchForm

def crop_view(request):
    products = None
    if request.method == "POST":
        form = FarmerSearchForm(request.POST)
        if form.is_valid():
            farmer_id = form.cleaned_data['farmer_id']
            products = CropProduct.objects.filter(farmer_id=farmer_id)
    else:
        form = FarmerSearchForm()

    return render(request, "uk/crop_view.html", {"form": form, "products": products})

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import CropProduct
from .forms import FarmerSearchForm, CropProductForm

# 🔎 Search by Farmer ID
def crop_search(request):
    products = None
    if request.method == "POST":
        form = FarmerSearchForm(request.POST)
        if form.is_valid():
            farmer_id = form.cleaned_data["farmer_id"]
            products = CropProduct.objects.filter(farmer_id=farmer_id)
    else:
        form = FarmerSearchForm()

    return render(request, "uk/crop_search.html", {"form": form, "products": products})

# ✏️ Update Crop Product
def crop_update(request, pk):
    product = get_object_or_404(CropProduct, pk=pk)
    if request.method == "POST":
        form = CropProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            messages.success(request, "Crop Product updated successfully.")
            return redirect("crop_search")
    else:
        form = CropProductForm(instance=product)

    return render(request, "uk/crop_update.html", {"form": form})

# ❌ Delete Crop Product
def crop_delete(request, pk):
    product = get_object_or_404(CropProduct, pk=pk)
    if request.method == "POST":
        product.delete()
        messages.success(request, "Crop Product deleted successfully.")
        return redirect("crop_search")

    return render(request, "uk/crop_delete.html", {"product": product})


from django.shortcuts import render
from .models import CropProduct
from .forms import FarmerSearchForm

def farmer_crop_view(request):
    products = None
    if request.method == "POST":
        form = FarmerSearchForm(request.POST)
        if form.is_valid():
            farmer_id = form.cleaned_data['farmer_id']
            products = CropProduct.objects.filter(farmer_id=farmer_id)
    else:
        form = FarmerSearchForm()

    return render(request, "uk/farmer_crop_view.html", {"form": form, "products": products})


def hub_farmer_dashboard(request):
    return render(request, 'uk/hub_farmer.html')


from django.shortcuts import render, redirect
from .forms import FarmerForm, PriceUpdateForm

def hub_farmer_register(request):
    if request.method == 'POST':
        form = FarmerForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('hub-farmer-view')
    else:
        form = FarmerForm()
    return render(request, 'uk/hub_farmer_register.html', {'form': form})


from django.shortcuts import render
from .models import Farmer

def hub_farmer_view(request):
    query = request.GET.get('farmer_id')
    if query:
        farmers = Farmer.objects.filter(farmer_id__icontains=query)
    else:
        farmers = Farmer.objects.all()
        
    return render(request, 'uk/hub_farmer_view.html', {'farmers': farmers})



from django.shortcuts import render, get_object_or_404
from .models import Farmer
from .forms import FarmerUpdateForm

def hub_farmer_update(request):
    farmer = None
    form = None
    updated = False
    error = None

    if request.method == 'POST':
        farmer_id = request.POST.get('farmer_id')

        if 'fetch' in request.POST:
            try:
                farmer = Farmer.objects.get(farmer_id=farmer_id)
                form = FarmerUpdateForm(instance=farmer)
            except Farmer.DoesNotExist:
                error = "Farmer ID not found."

        elif 'update' in request.POST:
            farmer = get_object_or_404(Farmer, farmer_id=farmer_id)
            form = FarmerUpdateForm(request.POST, request.FILES, instance=farmer)
            if form.is_valid():
                form.save()
                updated = True
            else:
                error = "Form is invalid."

    return render(request, 'uk/hub_farmer_update.html', {
        'form': form,
        'farmer': farmer,
        'updated': updated,
        'error': error
    })

from django.shortcuts import render, get_object_or_404, redirect
from .models import Farmer

def hub_farmer_delete(request):
    farmer = None
    deleted = False
    error = None

    if request.method == 'POST':
        farmer_id = request.POST.get('farmer_id')

        if 'fetch' in request.POST:
            try:
                farmer = Farmer.objects.get(farmer_id=farmer_id)
            except Farmer.DoesNotExist:
                error = "Farmer ID not found."

        elif 'delete' in request.POST:
            try:
                farmer = Farmer.objects.get(farmer_id=farmer_id)
                farmer.delete()
                deleted = True
                farmer = None
            except Farmer.DoesNotExist:
                error = "Farmer already deleted or not found."

    return render(request, 'uk/hub_farmer_delete.html', {
        'farmer': farmer,
        'deleted': deleted,
        'error': error,
    })


from django.shortcuts import render
from .models import CropProduct
from .forms import FarmerSearchForm

def hub_farmer_crop_view(request):
    products = None
    if request.method == "POST":
        form = FarmerSearchForm(request.POST)
        if form.is_valid():
            farmer_id = form.cleaned_data['farmer_id']
            products = CropProduct.objects.filter(farmer_id=farmer_id)
    else:
        form = FarmerSearchForm()

    return render(request, "uk/hub_crop_view.html", {"form": form, "products": products})


from django.shortcuts import render, redirect
from .forms import StockForm
from django.contrib import messages

def add_stock(request):
    if request.method == "POST":
        form = StockForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Stock entry added successfully!")
            return redirect('add_stock')
    else:
        form = StockForm()
    return render(request, 'uk/add_stock.html', {'form': form})


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Stock
from .forms import StockForm

# UPDATE STOCK
def update_stock(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    if request.method == "POST":
        form = StockForm(request.POST, request.FILES, instance=stock)
        if form.is_valid():
            form.save()
            messages.success(request, "Stock updated successfully!")
            return redirect('stock_list')   # redirect to stock list page
    else:
        form = StockForm(instance=stock)
    return render(request, 'uk/update_stock.html', {'form': form, 'stock': stock})

# DELETE STOCK
def delete_stock(request, pk):
    stock = get_object_or_404(Stock, pk=pk)
    if request.method == "POST":
        stock.delete()
        messages.success(request, "Stock deleted successfully!")
        return redirect('stock_list')
    return render(request, 'uk/delete_stock.html', {'stock': stock})

# STOCK LIST PAGE (to view all stocks)
def stock_list(request):
    stocks = Stock.objects.all().order_by('-created_at')
    return render(request, 'uk/stock_list.html', {'stocks': stocks})


from django.db.models import Sum
from django.shortcuts import render
from .models import CropProduct

def crop_summary(request):
    # First: group by crop and calculate total_kg
    crops = (
        CropProduct.objects
        .values('name_of_crop', 'price_per_kg')
        .annotate(total_kg=Sum('total_kg'))
        .order_by('name_of_crop')
    )

    # Now compute total_value manually (since can't multiply aggregate directly)
    for crop in crops:
        crop['total_value'] = crop['total_kg'] * crop['price_per_kg']

    return render(request, "uk/crop_summary.html", {"crops": crops})


def admin_hub(request):
    return render(request, "uk/admin_hub.html")



def admin_hub_stock_view(request):
    stocks = Stock.objects.all().order_by('-created_at')
    return render(request, 'uk/admin_hub_stock_view.html', {'stocks': stocks})


from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Driver

# Manage + Search Driver
def driver_manage(request):
    driver = None
    search_id = request.GET.get("search_id")

    if search_id:
        try:
            driver = Driver.objects.get(driver_id=search_id)
        except Driver.DoesNotExist:
            messages.error(request, "Driver not found.")
            driver = None

    return render(request, "uk/driver_manage.html", {"driver": driver})

# Add new driver
def add_driver(request):
    if request.method == "POST":
        Driver.objects.create(
            driver_id=request.POST["driver_id"],
            name=request.POST["name"],
            phone=request.POST["phone"],
            license_number=request.POST["license_number"],
            address=request.POST["address"],
            photo=request.FILES.get("photo")
        )
        messages.success(request, "Driver added successfully!")
        return redirect("driver_manage")

# Update driver
def update_driver(request, driver_id):
    driver = get_object_or_404(Driver, driver_id=driver_id)

    if request.method == "POST":
        driver.name = request.POST["name"]
        driver.phone = request.POST["phone"]
        driver.license_number = request.POST["license_number"]
        driver.address = request.POST["address"]
        if request.FILES.get("photo"):
            driver.photo = request.FILES["photo"]
        driver.save()
        messages.success(request, "Driver updated successfully!")
        return redirect("driver_manage")

    return render(request, "uk/driver_update.html", {"driver": driver})

# Delete driver
def delete_driver(request, driver_id):
    driver = get_object_or_404(Driver, driver_id=driver_id)
    driver.delete()
    messages.success(request, "Driver deleted successfully!")
    return redirect("driver_manage")


from django.shortcuts import render, redirect, get_object_or_404
from .models import Staff
from django.contrib import messages

def staff_management(request):
    staff = None
    search_id = request.GET.get("search_id")

    if search_id:
        try:
            staff = Staff.objects.get(staff_id=search_id)
        except Staff.DoesNotExist:
            messages.error(request, "Staff not found!")

    return render(request, "uk/staff_management.html", {"staff": staff})

def add_staff(request):
    if request.method == "POST":
        staff_id = request.POST.get("staff_id")
        name = request.POST.get("name")
        phone = request.POST.get("phone")
        role = request.POST.get("role")
        address = request.POST.get("address")
        photo = request.FILES.get("photo")

        Staff.objects.create(
            staff_id=staff_id,
            name=name,
            phone=phone,
            role=role,
            address=address,
            photo=photo
        )
        messages.success(request, "Staff registered successfully!")
        return redirect("staff_management")

def update_staff(request, staff_id):
    staff = get_object_or_404(Staff, staff_id=staff_id)
    if request.method == "POST":
        staff.name = request.POST.get("name")
        staff.phone = request.POST.get("phone")
        staff.role = request.POST.get("role")
        staff.address = request.POST.get("address")
        if request.FILES.get("photo"):
            staff.photo = request.FILES.get("photo")
        staff.save()
        messages.success(request, "Staff updated successfully!")
        return redirect("staff_management")

    return render(request, "uk/update_staff.html", {"staff": staff})

def delete_staff(request, staff_id):
    staff = get_object_or_404(Staff, staff_id=staff_id)
    staff.delete()
    messages.success(request, "Staff deleted successfully!")
    return redirect("staff_management")


# uk/views.py
from django.shortcuts import render, get_object_or_404, redirect
from django.utils.timezone import now
from .models import Staff, StaffAttendance

def staff_attendance(request):
    staff = None
    attendance_marked = False

    if request.method == "POST":
        staff_id = request.POST.get("staff_id")
        status = request.POST.get("status")

        staff = get_object_or_404(Staff, staff_id=staff_id)

        # Prevent duplicate marking for the same day
        attendance, created = StaffAttendance.objects.get_or_create(
            staff=staff,
            date=now().date(),
            defaults={"status": status}
        )

        if not created:  
            attendance.status = status  
            attendance.save()

        attendance_marked = True

    return render(request, "uk/staff_attendance.html", {
        "staff": staff,
        "attendance_marked": attendance_marked,
    })



# uk/views.py
from django.shortcuts import render, get_object_or_404
from .models import Staff, StaffAttendance

def staff_attendance_view(request):
    staff = None
    attendance_records = None

    if request.method == "GET" and 'staff_id' in request.GET:
        staff_id = request.GET.get("staff_id")
        try:
            staff = Staff.objects.get(staff_id=staff_id)
            attendance_records = StaffAttendance.objects.filter(staff=staff).order_by('-date')
        except Staff.DoesNotExist:
            staff = None
            attendance_records = None

    return render(request, "uk/staff_attendance_view.html", {
        "staff": staff,
        "attendance_records": attendance_records
    })


from django.shortcuts import render, get_object_or_404, redirect
from .models import Driver, DriverAttendance
from django.contrib import messages

# Mark attendance for driver
def driver_attendance(request):
    if request.method == "POST":
        driver_id = request.POST.get("driver_id")
        status = request.POST.get("status")

        try:
            driver = Driver.objects.get(driver_id=driver_id)
            DriverAttendance.objects.create(driver=driver, status=status)
            messages.success(request, f"Attendance marked for {driver.name}")
        except Driver.DoesNotExist:
            messages.error(request, "Driver ID not found")

    return render(request, "uk/driver_attendance.html")


# View attendance records by driver_id
def driver_attendance_view(request):
    attendance_records = None
    driver = None

    if request.method == "GET" and "driver_id" in request.GET:
        driver_id = request.GET.get("driver_id")
        try:
            driver = Driver.objects.get(driver_id=driver_id)
            attendance_records = DriverAttendance.objects.filter(driver=driver).order_by("-date")
        except Driver.DoesNotExist:
            driver = None
            attendance_records = None

    return render(request, "uk/driver_attendance_view.html", {
        "driver": driver,
        "attendance_records": attendance_records,
    })


def about(request):
    return render(request, "uk/about.html")


from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Vehicle
from .forms import VehicleForm



def vehicle_register(request):
    if request.method == "POST":
        form = VehicleForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request, "Vehicle registered successfully!")
            return redirect('vehicle_register')
    else:
        form = VehicleForm()
    return render(request, 'uk/vehicle_register.html', {'form': form})
# List all vehicles
def vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'uk/vehicle_list.html', {'vehicles': vehicles})

# Update vehicle
def vehicle_update(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, vehicle_id=vehicle_id)
    if request.method == "POST":
        form = VehicleForm(request.POST, request.FILES, instance=vehicle)
        if form.is_valid():
            form.save()
            messages.success(request, "Vehicle updated successfully!")
            return redirect('vehicle_list')
    else:
        form = VehicleForm(instance=vehicle)
    return render(request, 'uk/vehicle_form.html', {'form': form})

# Delete vehicle
def vehicle_delete(request, vehicle_id):
    vehicle = get_object_or_404(Vehicle, vehicle_id=vehicle_id)
    if request.method == "POST":
        vehicle.delete()
        messages.success(request, "Vehicle deleted successfully!")
        return redirect('vehicle_list')
    return render(request, 'uk/vehicle_confirm_delete.html', {'vehicle': vehicle})


def admin_vehicle_list(request):
    vehicles = Vehicle.objects.all()
    return render(request, 'uk/admin_transport.html', {'vehicles': vehicles})


from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Farmer
from .forms import FarmerLoginForm

def farmer_login(request):
    if request.method == "POST":
        form = FarmerLoginForm(request.POST)
        if form.is_valid():
            farmer_id = form.cleaned_data['farmer_id']

            try:
                farmer = Farmer.objects.get(farmer_id=farmer_id)
                # Save farmer id in session
                request.session['farmer_id'] = farmer.farmer_id
                return redirect('farmer_dashboard')
            except Farmer.DoesNotExist:
                messages.error(request, "Invalid Farmer ID")
    else:
        form = FarmerLoginForm()
    return render(request, 'uk/farmer_login.html', {'form': form})


def farmer_dashboard(request):
    farmer_id = request.session.get('farmer_id')
    if not farmer_id:
        return redirect('farmer_login')
    
    farmer = Farmer.objects.get(farmer_id=farmer_id)
    return render(request, 'uk/farmer_dashboard.html', {'farmer': farmer})




def farmer_logout(request):
    request.session.flush()  # clear session
    return redirect('farmer_login')



def farmer_home(request):
    return render(request, "uk/farmer_home.html")

def farmer_dashboard(request):
    farmer_id = request.session.get('farmer_id')
    if not farmer_id:
        return redirect('farmer_login')

    farmer = Farmer.objects.get(farmer_id=farmer_id)

    # Get stock list (may be empty)
    stocks = CropProduct.objects.filter(farmer_id=farmer.farmer_id)

    return render(request, 'uk/farmer_dashboard.html', {
        'farmer': farmer,
        'stocks': stocks,
    })


import random
from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
from .models import Customer
from .forms import (
    CustomerSignupForm,
    CustomerLoginForm,
    ForgotPasswordForm,
    ResetPasswordForm,
)

# Store OTP temporarily (better to use cache/Redis in production)
OTP_STORE = {}


# ---------------------------
# Signup
# ---------------------------
def customer_signup(request):
    if request.method == "POST":
        form = CustomerSignupForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully. Please login.")
            return redirect("customer_login")
    else:
        form = CustomerSignupForm()
    return render(request, "uk/signup.html", {"form": form})


# ---------------------------
# Login
# ---------------------------
def customer_login(request):
    if request.method == "POST":
        form = CustomerLoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            password = form.cleaned_data["password"]

            try:
                user = Customer.objects.get(email=email)
                if user.check_password(password):
                    # ✅ store email in session instead of id
                    request.session["customer_email"] = user.email
                    request.session["customer_name"] = user.name
                    messages.success(request, f"Welcome {user.name}!")
                    return redirect("customer_home")
                else:
                    messages.error(request, "Invalid password")
            except Customer.DoesNotExist:
                messages.error(request, "Email not registered")
    else:
        form = CustomerLoginForm()
    return render(request, "uk/login.html", {"form": form})



# ---------------------------
# Logout
# ---------------------------
def customer_logout(request):
    request.session.flush()  # ✅ clears session data
    messages.success(request, "Logged out successfully.")
    return redirect("customer_login")


# ---------------------------
# Forgot Password - Send OTP
# ---------------------------
def forgot_password(request):
    if request.method == "POST":
        form = ForgotPasswordForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            try:
                user = Customer.objects.get(email=email)
                otp = str(random.randint(100000, 999999))
                OTP_STORE[email] = otp

                # Send OTP via Email
                send_mail(
                    "Uzhavan Kart - Password Reset OTP",
                    f"Your OTP for password reset is: {otp}",
                    settings.DEFAULT_FROM_EMAIL,
                    [email],
                    fail_silently=False,
                )
                messages.success(request, "OTP sent to your email.")
                return redirect("reset_password")
            except Customer.DoesNotExist:
                messages.error(request, "Email not registered")
    else:
        form = ForgotPasswordForm()
    return render(request, "uk/forgot_password.html", {"form": form})


# ---------------------------
# Reset Password - Verify OTP
# ---------------------------
def reset_password(request):
    if request.method == "POST":
        form = ResetPasswordForm(request.POST)
        if form.is_valid():
            otp = form.cleaned_data["otp"]
            new_password = form.cleaned_data["new_password1"]

            # Find email with OTP
            email = None
            for k, v in OTP_STORE.items():
                if v == otp:
                    email = k
                    break

            if email:
                try:
                    user = Customer.objects.get(email=email)
                    user.set_password(new_password)  # ✅ hash password
                    user.save()
                    OTP_STORE.pop(email, None)
                    messages.success(request, "Password reset successful. Please login.")
                    return redirect("customer_login")
                except Customer.DoesNotExist:
                    messages.error(request, "User not found")
            else:
                messages.error(request, "Invalid OTP")
    else:
        form = ResetPasswordForm()
    return render(request, "uk/reset_password.html", {"form": form})


# ---------------------------
# Customer Home
# ---------------------------
def customer_home(request):
    customer = None
    if "customer_email" in request.session:  # ✅ check email instead of id
        try:
            customer = Customer.objects.get(email=request.session["customer_email"])
        except Customer.DoesNotExist:
            pass
    return render(request, "uk/customer_home.html", {"customer": customer})


def customer_home_uk(request):
    customer = None
    if "customer_email" in request.session:  # ✅ keep consistent
        try:
            customer = Customer.objects.get(email=request.session["customer_email"])
        except Customer.DoesNotExist:
            pass
    return render(request, "uk/customer_home_uk.html", {"customer": customer})



# views.py
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.db import transaction
from django.db.models import F
from .models import Stock, Cart, Order
from collections import defaultdict
from decimal import Decimal

from django.db.models import Sum

def browse_products(request):
    category = request.GET.get('stock_type')
    products = Stock.objects.all()
    if category:
        products = products.filter(stock_type=category)

    cart_count = 0
    if request.user.is_authenticated:
        cart_count = Cart.objects.filter(user=request.user).aggregate(Sum('quantity'))['quantity__sum'] or 0

    stock_types = Stock.STOCK_TYPES
    return render(request, 'uk/customer_product_list.html', {
        'products': products,
        'selected_stock_type': category,
        'stock_types': stock_types,
        'cart_count': cart_count
    })



from django.http import JsonResponse

def add_to_cart(request, crop_name):
    if request.method != "GET":
        return JsonResponse({"status": "error", "message": "Invalid request"}, status=400)

    product = get_object_or_404(Stock, crop_name=crop_name)
    qty = int(request.GET.get("qty", 1))

    customer_email = request.session.get("customer_email")
    if not customer_email:
        return JsonResponse({"status": "error", "message": "Login required"}, status=403)

    cart_item, created = Cart.objects.get_or_create(
        customer_email=customer_email,
        product=product,
        defaults={"quantity": 0},
    )

    cart_item.quantity += qty
    if cart_item.quantity <= 0:
        cart_item.delete()
    else:
        cart_item.save()

    cart_count = Cart.objects.filter(customer_email=customer_email).count()

    return JsonResponse({
        "status": "success",
        "message": f"{product.crop_name} added to cart",
        "cart_count": cart_count
    })



def view_cart(request):
    customer_email = request.session.get("customer_email")
    if not customer_email:
        return redirect("customer_login")

    cart_items = Cart.objects.filter(customer_email=customer_email)
    total = sum(item.subtotal() for item in cart_items)

    return render(request, "uk/cart.html", {
        "cart_items": cart_items,
        "total": total,
    })


@transaction.atomic
def checkout(request):
    customer_email = request.session.get("customer_email")
    if not customer_email:
        return redirect("customer_login")

    cart_items = Cart.objects.select_related("product").select_for_update().filter(
        customer_email=customer_email
    )
    if not cart_items.exists():
        messages.warning(request, "Your cart is empty!")
        return redirect("view_cart")

    total = sum(item.subtotal() for item in cart_items)

    if request.method == "POST":
        name = request.POST.get("name")
        mobile = request.POST.get("mobile")
        address = request.POST.get("address")
        payment_method = request.POST.get("payment_method")

        if not (name and mobile and address):
            messages.error(request, "Please fill all required fields.")
            return redirect("checkout")

        # Consolidate quantities
        qty_by_product = defaultdict(int)
        for item in cart_items:
            qty_by_product[item.product] += item.quantity

        # Stock check
        for product, qty in qty_by_product.items():
            if product.quantity_kg < qty:
                messages.error(request, f"Insufficient stock for {product.crop_name}")
                return redirect("view_cart")

        # Deduct stock + create orders
        for product, qty in qty_by_product.items():
            Stock.objects.filter(id=product.id).update(
                quantity_kg=F("quantity_kg") - Decimal(qty)
            )
            Order.objects.create(
                customer_email=customer_email,
                customer_name=name,
                customer_mobile=mobile,
                address=address,
                crop_name=product.crop_name,
                quantity=qty,
                total_price=product.price_per_kg * Decimal(qty),
                payment_method=payment_method,
            )

        cart_items.delete()
        messages.success(request, "✅ Order placed successfully!")
        return redirect("customer_home")

    return render(request, "uk/checkout.html", {
        "cart_items": cart_items,
        "total": total,
    })


from django.db import transaction
from django.db.models import F
from decimal import Decimal
from django.shortcuts import redirect, get_object_or_404
from django.contrib import messages
from .models import Order, Stock

@transaction.atomic
def cancel_order(request, order_id):
    customer_email = request.session.get("customer_email")
    if not customer_email:
        return redirect("customer_login")

    # Get order of the logged-in customer
    order = get_object_or_404(Order, id=order_id, customer_email=customer_email)

    # Prevent double cancellation
    if order.status == "Cancelled":
        messages.info(request, "This order is already cancelled.")
        return redirect("view_orders")

    try:
        # Lock the stock row to avoid race condition
        product = Stock.objects.select_for_update().get(crop_name=order.crop_name)

        # Restore stock
        Stock.objects.filter(id=product.id).update(
            quantity_kg=F("quantity_kg") + Decimal(order.quantity)
        )
    except Stock.DoesNotExist:
        pass  # If stock missing, just skip

    # ✅ Delete the order completely from DB
    order.delete()

    messages.success(request, "Order cancelled, stock restored, and order removed.")
    return redirect("view_orders")




from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Stock, Cart, Order

# -----------------------------
# Remove single product from cart
# -----------------------------
def remove_from_cart(request, crop_name):
    customer_email = request.session.get("customer_email")
    if not customer_email:
        return redirect("customer_login")

    product = get_object_or_404(Stock, crop_name=crop_name)
    cart_item = Cart.objects.filter(customer_email=customer_email, product=product).first()

    if cart_item:
        cart_item.delete()
        messages.success(request, f"{product.crop_name} removed from cart.")
    else:
        messages.warning(request, "Item not found in your cart.")

    return redirect("view_cart")

# -----------------------------
# Clear entire cart
# -----------------------------
def clear_cart(request):
    customer_email = request.session.get("customer_email")
    if not customer_email:
        return redirect("customer_login")

    Cart.objects.filter(customer_email=customer_email).delete()
    messages.success(request, "Your cart has been cleared.")

    return redirect("view_cart")

# -----------------------------
# Order Success page
# -----------------------------
def order_success(request):
    customer_email = request.session.get("customer_email")
    if not customer_email:
        return redirect("customer_login")

    # Get latest orders for the customer
    latest_orders = Order.objects.filter(customer_email=customer_email).order_by("-id")[:5]

    return render(request, "uk/order_success.html", {
        "orders": latest_orders
    })


from django.shortcuts import render, redirect
from .models import Order

def view_orders(request):
    customer_email = request.session.get("customer_email")
    if not customer_email:
        return redirect("customer_login")

    orders = Order.objects.filter(customer_email=customer_email).order_by("-created_at")
    return render(request, "uk/view_orders.html", {"orders": orders})



from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from .models import Order

# Hub Order Management View
def hub_order_manage(request):
    # Directly show all orders without authentication
    orders = Order.objects.all().order_by("-created_at")
    return render(request, "uk/hub_order_manage.html", {"orders": orders})


def hub_update_order_status(request, order_id, status):
    order = get_object_or_404(Order, id=order_id)

    if status == "Cancelled":
        # Restore stock
        try:
            product = Stock.objects.get(crop_name=order.crop_name)
            product.quantity_kg = F("quantity_kg") + Decimal(order.quantity)
            product.save()
        except Stock.DoesNotExist:
            pass

        order.delete()   # ❌ remove order
        messages.success(request, f"Order #{order_id} cancelled and removed.")
    elif status in ["Pending", "Completed"]:
        order.status = status
        order.save()
        messages.success(request, f"Order #{order_id} marked as {status}.")
    else:
        messages.error(request, "Invalid status update.")

    return redirect("hub_order_manage")



