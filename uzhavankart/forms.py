from django import forms
from .models import Farmer, Product

class FarmerForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = '__all__'
class PriceUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['price']

from django import forms
from .models import Farmer

class FarmerUpdateForm(forms.ModelForm):
    class Meta:
        model = Farmer
        fields = [
            'name', 'village', 'district', 'address',
            'land_sqft', 'crop', 'mobile_no', 'photo'
        ]
        widgets = {
            'address': forms.Textarea(attrs={'rows': 2}),
        }



from django import forms
from .models import Product  # Ensure Product model is defined in models.py

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'category', 'price', 'image']  # Add/remove fields as needed



from django import forms
from .models import Employee

class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['emp_id', 'name', 'dob', 'gender', 'mobile_no', 'address', 'job_role', 'photo']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
            'gender': forms.RadioSelect,
        }


from django import forms
from .models import Employee

class EmployeeUpdateForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ['name', 'dob', 'gender', 'mobile_no', 'address', 'job_role', 'photo']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }




class EmployeeLoginForm(forms.Form):
    emp_id = forms.CharField(max_length=20, label="Employee ID")

from django import forms
from .models import CropProduct

class CropProductForm(forms.ModelForm):
    class Meta:
        model = CropProduct
        fields = ['name_of_crop', 'total_kg', 'price_per_kg']  # farmer_id excluded




from django import forms

class FarmerSearchForm(forms.Form):
    farmer_id = forms.CharField(label="Enter Farmer ID", max_length=20)


from django import forms
from .models import CropProduct

class FarmerSearchForm(forms.Form):
    farmer_id = forms.CharField(max_length=20, label="Enter Farmer ID")

class CropProductForm(forms.ModelForm):
    class Meta:
        model = CropProduct
        fields = ["name_of_crop", "total_kg", "price_per_kg"]


from django import forms
from .models import Stock

class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = ['crop_name', 'stock_type', 'quantity_kg', 'price_per_kg', 'stock_image']
        widgets = {
            'crop_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Crop Name'}),
            'stock_type': forms.Select(attrs={'class': 'form-select'}),
            'quantity_kg': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Quantity (kg)'}),
            'price_per_kg': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Enter Price per Kg'}),
            'stock_image': forms.ClearableFileInput(attrs={'class': 'form-control'}),
        }



from django import forms
from .models import Vehicle


class VehicleForm(forms.ModelForm):
    class Meta:
        model = Vehicle
        fields = "__all__"   # include all fields
        widgets = {
            "vehicle_id": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Vehicle ID"}),
            "driver_id": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Driver ID"}),
            "owner_name": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Owner Name"}),
            "vehicle_type": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Vehicle Type"}),
            "vehicle_company": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Company Name"}),
            "registration_number": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter Registration Number"}),
            "vehicle_img": forms.ClearableFileInput(attrs={"class": "form-control"}),
        }



from django import forms

class FarmerLoginForm(forms.Form):
    farmer_id = forms.CharField(
        max_length=20, 
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Enter Farmer ID'
        })
    )


from django import forms
from .models import Customer


# ---------------------------
# Signup Form
# ---------------------------
class CustomerSignupForm(forms.ModelForm):
    password1 = forms.CharField(
        widget=forms.PasswordInput,
        label="Password",
        strip=False
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput,
        label="Confirm Password",
        strip=False
    )

    class Meta:
        model = Customer
        fields = ["name", "dob", "mobile", "email"]

    def clean_password2(self):
        p1 = self.cleaned_data.get("password1")
        p2 = self.cleaned_data.get("password2")
        if p1 and p2 and p1 != p2:
            raise forms.ValidationError("Passwords don’t match")
        return p2

    def save(self, commit=True):
        user = super().save(commit=False)
        # ✅ hash password using model method
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


# ---------------------------
# Login Form
# ---------------------------
class CustomerLoginForm(forms.Form):
    email = forms.EmailField(label="Email")
    password = forms.CharField(widget=forms.PasswordInput, label="Password")


# ---------------------------
# Forgot Password (OTP request)
# ---------------------------
class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(label="Registered Email")


# ---------------------------
# Reset Password (OTP verify)
# ---------------------------
class ResetPasswordForm(forms.Form):
    otp = forms.CharField(max_length=6, label="OTP")
    new_password1 = forms.CharField(widget=forms.PasswordInput, label="New Password")
    new_password2 = forms.CharField(widget=forms.PasswordInput, label="Confirm New Password")

    def clean(self):
        cleaned = super().clean()
        if cleaned.get("new_password1") != cleaned.get("new_password2"):
            raise forms.ValidationError("Passwords do not match")
        return cleaned

