from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from .forms import PersonForm
from .models import *
from django.db.models import Q
from django.db.models import Subquery


def index(request):
    posts = Post.objects.all()
    category = Category.objects.all()
    context = {
        'posts': posts,
        'category': category
    }
    return render(request,'articles/index.html',context=context)

def category(request,id):
    posts = Post.objects.filter(cat_id=id)
    category = Category.objects.all()
    context = {
        'posts': posts,
        'category': category
    }

    return render(request,'articles/index.html',context=context)

def post(request,id):
    post_one = Post.objects.filter(id=id)
    print(post_one)
    onepostmark = 'true'
    context = {
        'post_one': post_one,
        'onepostmark':onepostmark
    }
    return render(request, 'articles/post.html', context=context)

def dbtrening(request):
    result = Post.objects.all()
    onepostmark = 'true'
    context = {
        'result': result,
        'onepostmark': onepostmark
    }
    return render(request, 'articles/dbtrening.html', context=context)

def insert(request):
    Person.objects.create(name="Bruce7",
                          bron="2002-11-2",
                          locic=False,
                          age=34,
                          test=1021)
    result = Person.objects.all()
    return render(request, 'articles/dbtrening.html', context={'result':result})

def gett(request):
    result = Person.objects.all()
    getres = Person.objects.filter(age=34)
    return render(request, 'articles/dbtrening.html', context={'result': result,
                                                               'getres':getres})

def updater(request):
    upd = Person.objects.get(id=7)
    upd.name = 'Bill27'
    upd.save()
    updafter = Person.objects.get(id=7)
    counter = Person.objects.count()
    return render(request, 'articles/dbtrening.html', context={'u': updafter,
                                                               'counter':counter})

def myforms(request):
    form = PersonForm()
    return render(request, 'articles/myforms.html', context={'form': form})

def insforms(request):
    if request.method == "POST":
        klient = Person()
        klient.name = request.POST.get("name")
        klient.bron = request.POST.get("bron")
        locic = request.POST.get("locic")
        if locic=='on':
            klient.locic = True
        else:
            klient.locic = False
        klient.age = int(request.POST.get("age"))
        klient.test = int(request.POST.get("test"))
        klient.save()

    #return reverse('myforms')
    #return render(request, 'articles/myforms.html')
    return HttpResponseRedirect('/')

def spec(request):
    spec = Product.objects.get(id=1)
    marka = Product.objects.filter(company__name="Volvo")
    firma = Company.objects.get(name='Volvo')
    products = firma.product_set.all()
    count = firma.product_set.count()

    insfirma = Company.objects.create(name='Tank')
    insfirma.product_set.create(name='Tanker-2300',price='5000')
    allproduct = Product.objects.all()

    return render(request, 'articles/spec.html', context={'spec': spec,
                                                          'marka':marka,
                                                          'products':products,
                                                          'count':count,
                                                          'allproduct':allproduct})
def tomany(request):
    #st_vik = Student.objects.create(name="Виктор")
    #st_vik.curses.create(name="Информатика")
    #info = Student.objects.all()
    curs = Curse.objects.all()
    print(curs)
    contex= {
        #'info': info,
        'curs':curs
    }
    return render(request, 'articles/tomany.html', context=contex)


def test(request):
    test = Student.objects.all()
    print(str(test.query))

    am = Student.objects.filter( name__startswith='П' ).values('name')
    print(str(am.query))

    yset = Student.objects.filter(~Q(id__lt=5))

    ets = Product.objects.filter(id__in=Subquery(test.values('id')))
    print(ets)

    data={
        'wer':'12345',
        'am':am,
        'yset':yset
    }
    return render(request, 'articles/test.html', context=data)
