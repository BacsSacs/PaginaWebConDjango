from django.shortcuts import render, HttpResponse

# html_base = """
# <h1>Mi web personal</h1>
# <ul>
#     <li><a href="/">Portada</a></li>
#     <li><a href="/about-me/">about-me</a></li>
#     <li><a href="/portfolio/">Portafolio</a></li>
#     <li><a href="/contact/">Contacto</a></li>
# """

def home(request):
    return render(request,"core/home.html")

def About(request):
    return render(request,"core/about.html")

def Portafolio(request):
    return render(request,"core/portafolio.html")
def Contacto(request):
    return render(request,"core/contacto.html")