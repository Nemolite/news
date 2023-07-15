from django.forms import model_to_dict
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect

# Create your views here.
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from .forms import PersonForm
from .models import *
from django.db.models import Q
from django.db.models import Subquery

from .serializers import NewsSerializer


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
    context = {
        'post_one': post_one
    }
    return render(request, 'articles/post.html', context=context)

def dbtrening(request):
    result = Post.objects.all()
    context = {
        'result': result
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
def manytomany(request):
    students = Student.objects.all()
    curses = Curse.objects.all()
    contex= {
        'students': students,
        'curses':curses
    }
    return render(request, 'articles/tomany.html', context=contex)

def stud(request,id):
    students = Student.objects.all()
    curses = Curse.objects.all()
    stud = Student.objects.get(id=id)
    courforstud = Student.objects.get(id=id).curses.all()
    print(courforstud)
    contex = {
        'students': students,
        'curses': curses,
        'courforstud': courforstud,
        'stud': stud,
    }
    return render(request, 'articles/tomany.html', context=contex)

def curs(request,id):
    students = Student.objects.all()
    curses = Curse.objects.all()
    curs = Curse.objects.get(id=id)
    studforcurs = Student.objects.filter(curses__name=curs.name)
    print(studforcurs)
    contex = {
        'students': students,
        'curses': curses,
        'studforcurs': studforcurs,
        'curs': curs,
    }
    return render(request, 'articles/tomany.html', context=contex)

def formtest(request):
    if request.method == "POST":
        inpname = request.POST.get("inpname")
        print(str(inpname))

    #return render(request, 'articles/test.html')
    return HttpResponse('good')


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

def shop(request):
    return render(request, 'shop/catalog.html')

# class NewsAPIView(generics.ListAPIView):
#    queryset = Post.objects.all()
#    serializer_class = NewsSerializer

class NewsAPIList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = NewsSerializer

class NewsAPIUpdate(generics.UpdateAPIView):
    queryset = Post.objects.all()
    serializer_class = NewsSerializer

class NewsAPIDelete(generics.DestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = NewsSerializer

class NewsAPIDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = NewsSerializer
# class NewsAPIView(APIView):
#     def get(self,request):
#         p = Post.objects.all().values()
#         return Response({'post':NewsSerializer(p, many=True).data})
#
#     def post(self,request):
#         serializer = NewsSerializer(data= request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#
#         return Response({'post': serializer.data})
#
#     def put(self, request, *srgs,**kwargs):
#         pk = kwargs.get("pk",None)
#         if not pk:
#             return Response({"error":"Method PUT not allowed"})
#         try:
#             instance = Post.objects.get(pk=pk)
#         except:
#             return Response({"error":"Oject does not exists"})
#
#         serializer = NewsSerializer(data = request.data, instance=instance)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response({"post":serializer.data})
#
#     def delete(self, request, *srgs,**kwargs):
#         pk = kwargs.get("pk", None)
#         if not pk:
#             return Response({"error": "Method DELETE not allowed"})
#
#         return Response({"post":"delete post" + str(pk)})