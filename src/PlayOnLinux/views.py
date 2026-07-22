from django.shortcuts import render
from django.http import HttpResponse
import os

def home(request):
    return render(request, "index.html")

def custom_page_not_found_view(request, exception):
    print('\n***** ERRO 404')
    return render(request, "errors/404.html", {})

def custom_error_view(request, exception=None):
    print('\n***** ERRO 500')
    return render(request, "errors/500.html", {})

def custom_permission_denied_view(request, exception=None):
    print('\n***** ERRO 403')
    return render(request, "errors/403.html", {})

def custom_bad_request_view(request, exception=None):
    print('\n***** ERRO 400')
    return render(request, "errors/400.html", {})

def version2(request):
    print("\n***** '4.3.4\n', content_type='text/plain'")
    return HttpResponse('4.3.4\n', content_type="text/plain")

def update_mark(request):
    print("\n'1673042197', content_type='text/plain'")
    return HttpResponse('1673042197', content_type="text/plain")

def get_packages(request):
    print("\n'get_packages', request, content_type='text/plain'")
    return sendFile('get_packages', request, content_type='text/plain')

def screenshot(request):
    return HttpResponse('1181', content_type="text/plain")

def get_description(request):
    return sendFile('get_description', request, content_type='text/html')

def get_file(request):
    version = request.GET.get('version')
    if(version.lower()!='playonlinux-4.3.4' and version.lower()!='playonlinux-4.4'):
        print('\n*****[get_file] version não cadastrada:', version)
        return HttpResponse(None)
    id = request.GET.get('id')
    return sendFile(id, request, content_type='text/plain')

def get_list_v4(request):
    return sendFile('get_list_v4', request, content_type='text/plain')

def get_md5_list(request):
    if(request.GET.get('playonlinux')=='1'):
        return HttpResponse('', content_type='text/plain')
    else:
        print('\n*****[get_md5_list] Valor de playonlinux inválido:', request.GET.get('playonlinux'))

def download(request, filename):
    return (sendFile(filename, request, content_type='application/octet-stream'))

def sendFile(filename, request, content_type='text/html'):
    BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    achou = False
    while(not achou):
        try:
            arq = open(BASE_DIR + '/resources/' + filename, 'rb')
        except:
            print('\n*****[sendFile] Arquivo %s não encontrado: ' % (BASE_DIR + '/resources/' + filename))
            print(f'Pedido: {request.build_absolute_uri()}')
            input("Press <Enter> to try again...")
        else:
            achou = True
    print(f"\n*****[sendFile] Enviando arquivo {BASE_DIR + '/resources/' + filename}")
    conteudo = arq.read()
    arq.close()
    return HttpResponse(conteudo, content_type=content_type)

def stars(request):
    return HttpResponse('0', content_type='text/plain')
