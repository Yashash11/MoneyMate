from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from .models import Category, Expense
from django.contrib import messages

# Create your views here:

def homePage(request):
    # This is the main page that will be displayed to the user.
    # The function has been exported to the 'expensesapp' 
    # project in the 'urls.py' file in order to visualize the HTML content.
    return render(request, 'moneymate/base.html')

def dashboard(request):
    # When the user logs in or registers, he/she will be taken 
    # directly to the templates/moneymate/dashboard.html file.
    return render(request, 'moneymate/dashboard.html')

def viewExpensesList(request):
    # This feature allows the user to review the expenses
    # they have previously entered in the application. 
    # By clicking on 'Expenses' in the navigation bar of 
    # the dashboard.html, users can access a list of their recorded expenses.
    categories = Category.objects.all()
    expenses = Expense.objects.filter(user = request.user)
    context = {'expenses': expenses}
    return render(request, 'moneymate/expenses/list_expenses.html', context)

def addExpense(request):
    # This feature enables users to access their expense records.
    # By clicking on the appropriate button
    categories = Category.objects.all()
    context = {
        'categories': categories,
        'values': request.POST
    }
    if request.method == 'GET':
        return render(request, 'moneymate/expenses/add_expense.html', context)

    if request.method == 'POST':
        amount = request.POST['amount']

        if not amount:
            messages.error(request, 'Amount is required.')
            return render(request, 'moneymate/expenses/add_expense.html', context)
        description = request.POST['description']
        date = request.POST['expense_date']
        category = request.POST['category']

        if not description:
            messages.error(request, 'Description is required.')
            return render(request, 'moneymate/expenses/add_expense.html', context)

        Expense.objects.create(user=request.user, amount=amount, date=date,
                               category=category, description=description)
        messages.success(request, 'Expense saved successfully.')

        return redirect('listExpenses')