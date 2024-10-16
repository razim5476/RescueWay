from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages

# Create your views here.

def gallery_view(request):
    category = request.GET.get('category', None)  # Get the selected category from the request
    if category:
        images = GalleryImage.objects.filter(category=category)  # Filter images by category
    else:
        images = GalleryImage.objects.all()  # Show all images if no category is selected

    return render(request, 'gallery/view_images.html', {'images': images})

def upload_image(request):
    if request.method == 'POST':
        title = request.POST.get('title', '')
        description = request.POST.get('description', '')
        category = request.POST.get('category', '')  
        image = request.FILES.get('image')

        # Check if all required fields are present
        if not title or not description or not category or not image:
            # Handle the error, e.g., render the template with an error message
            return render(request, 'gallery/upload_image.html', {
                'error': 'All fields are required.',
            })

        # Save the image data to the database
        new_image = GalleryImage(title=title, description=description, category=category, image=image)
        new_image.save()

        return redirect('gallery_view')  # Redirect to the gallery view after successful upload

    return render(request, 'gallery/upload_image.html')
     
        
        
        