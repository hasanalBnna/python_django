from django.http import HttpResponse

def test_view(request):
    html = """
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>Document</title>
        </head>
        <body>
            <h2>This is a test page2</h2>
        </body>
        </html>
    """
    return HttpResponse(html)