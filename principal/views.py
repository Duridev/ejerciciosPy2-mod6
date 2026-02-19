from django.shortcuts import render

# Create your views here.
def index(request):
    data = [
        {
            'categoria': 'Estudios',
            'titulo': 'Django',
            'fecha': '15 de febrero',
            'contenido': 'This is a wider card with supporting text below as a natural lead-in to additional content.',
            'imagen': 'Thumbnail',
        },
        {
            'categoria': 'Design',
            'titulo': 'Featured post',
            'fecha': 'Nov 12',
            'contenido': 'This is a wider card with supporting text below as a natural lead-in to additional content.',
            'imagen': 'Thumbnail',
        },        {
            'categoria': 'Design',
            'titulo': 'Featured post',
            'fecha': 'Nov 12',
            'contenido': 'This is a wider card with supporting text below as a natural lead-in to additional content.',
            'imagen': 'Thumbnail',
        },
    ]
    contexto = {'data': data}
    return render(request, 'principal/index.html', contexto)
