from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Image as RLImage
from reportlab.lib.styles import getSampleStyleSheet
from django.http import HttpResponse

def generate_pdf(images):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="images.pdf"'

    doc = SimpleDocTemplate(response, pagesize=letter)
    styles = getSampleStyleSheet()

    story = []
    for image in images:
        story.append(RLImage(image.image.path))
        story.append(Paragraph(image.description, styles['Normal']))

    doc.build(story)
    return response