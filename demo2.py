import pdfkit
options = {
    'page-size': 'A4',
    'margin-top': '0.75in',
    'margin-right': '0.75in',
    'margin-bottom': '0.75in',
    'margin-left': '0.75in',
}
p=pdfkit.from_url('https://en.wikipedia.org/wiki/NumPy', 'numpy.pdf', options=options)
