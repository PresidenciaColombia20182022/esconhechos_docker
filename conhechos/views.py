from django.shortcuts import render
from conhechos.models import Eje, Descripcion, CumplimosLoPrometidoVideo, SliderVideo
from django.db.models import Q


def handler404(request, exception):
    return render(request, '404.html',  status=404)
   

def handler403(request, exception):
    return render(request, '404.html',  status=404)

def handler500(request):
    return render(request, '500.html',  status=404)

def home(request):
    ejelista = Eje.objects.all()
    listaDes = Descripcion.objects.all()
    ListacumplimosLoPrometidoVideo = CumplimosLoPrometidoVideo.objects.all()
    sliderVideos = SliderVideo.objects.all()
    listaDescripcion = []
    fecha1 = 0
    selectid = []
    for eje in ejelista:
        if Descripcion.objects.filter(eje=eje).exists():
            descripcion = Descripcion.objects.filter(eje=eje)
            contador = 0
            if descripcion.count() >=2:
                for des in descripcion:
                    if contador == 0:
                        fecha1 = des.fecha
                        contador = 1
                    else:
                        if fecha1 >= des.fecha:   
                            fecha1 = fecha1
                        else:
                            fecha1 = des.fecha
                    selectid = Descripcion.objects.get(eje=eje.id,fecha=fecha1)
                listaDescripcion.append(selectid.id)
            else:
                for des in descripcion:
                    listaDescripcion.append(des.id)
    return render(request,'index.html',{"sliderVideos":sliderVideos,"videoscumplimos":ListacumplimosLoPrometidoVideo,"listaDescripcionSelect":listaDescripcion,"listaDescripcion":listaDes})

def interna(request,eje):
    ejes = Eje.objects.get(eje=eje) 
    palabra = request.POST.get("palabra")
    validar = 0
    if palabra:
        descripciones = Descripcion.objects.filter(
                Q(titulo__icontains = palabra) & 
                Q(descripcion__icontains = palabra),
                eje=ejes
            ).distinct()
        if descripciones:
            validar=1
        else:
            validar=2
    else:       
        descripciones = Descripcion.objects.filter(eje=ejes)
    return render(request,"interna.html",{"listadescripciones":descripciones,"eje":ejes,"validar":validar})  

    


  