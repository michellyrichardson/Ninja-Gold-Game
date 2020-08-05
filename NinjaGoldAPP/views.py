from django.shortcuts import render, redirect
import random

# Create your views here.
def ninjagold(request):
    if 'gold' not in request.session:
        request.session['gold'] = 0
    
    print(request.session['gold'])
    return render(request, 'ninjagold.html')

def farm(request):
    rand_num = random.randint(10,20)
    request.session['gold'] = request.session['gold'] + rand_num
    print(f'Earned {rand_num} golds from the farm')
    return redirect('/')

def cave(request):
    rand_num = random.randint(5,10)
    request.session['gold'] = request.session['gold'] + rand_num
    print(f'Earned {rand_num} golds from the cave')
    return redirect('/')

def house(request):
    rand_num = random.randint(2,5)
    request.session['gold'] = request.session['gold'] + rand_num
    print(f'Earned {rand_num} golds from the house')
    return redirect('/')

def casino(request):
    rand_num = random.randint(-50,50)
    request.session['gold'] = request.session['gold'] + rand_num
    print(f'Earned/Lost {rand_num} golds from the casino')
    return redirect('/')