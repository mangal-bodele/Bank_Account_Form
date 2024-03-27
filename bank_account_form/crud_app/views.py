from django.shortcuts import render,redirect
from .forms import AccountForm
from .models import Account
from django.contrib.auth.decorators import login_required
@login_required(login_url='login_url')
def create_account(request):
    template_name = 'crud_app/create.html'
    form = AccountForm()
    if request.method == "POST":
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form':form}
    return render(request, template_name, context)
@login_required(login_url='login_url')
def show_account(request):
    template_name = 'crud_app/show.html'
    accounts = Account.objects.all()
    context = {'accounts': accounts}
    return render(request, template_name, context)

def update_account(request, pk):
    template_name = 'crud_app/create.html'
    obj = Account.objects.get(id=pk)
    form = AccountForm(instance=obj)
    if request.method == "POST":
        form = AccountForm(request.POST,instance=obj)
        if form.is_valid():
            form.save()
            return redirect('show_url')
    context = {'form': form}
    return render(request, template_name, context)

def delete_account(request,pk):
    template_name= 'crud_app/confirm.html'
    obj = Account.objects.get(id=pk)
    if request.method == "POST":
        obj.delete()
        return redirect("show_url")
    return render(request, template_name)