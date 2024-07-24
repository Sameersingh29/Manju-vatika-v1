from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_protect
from .forms import EnquiryForm
import logging
from django.core.cache import cache
import hashlib

logger = logging.getLogger(__name__)

def index(request):
    form = EnquiryForm()
    return render(request, 'index.html', {'form': form})

def gallery(request):
    return render(request, 'gallery.html')

def hash_request_data(data):
    """
    Generate a hash of the form data to detect duplicates.
    """
    data_string = '|'.join([str(data[key]) for key in sorted(data.keys())])
    return hashlib.md5(data_string.encode('utf-8')).hexdigest()

@csrf_protect
def submit_enquiry(request):
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form_hash = hash_request_data(request.POST)
            cache_key = f'enquiry_{form_hash}'
            if cache.get(cache_key):
                logger.warning('Duplicate form submission detected')
                return JsonResponse({'success': False, 'error': 'Duplicate submission detected'})
            else:
                form.save()
                cache.set(cache_key, True, timeout=60)  # Prevent duplicates for 1 minute
                logger.info('Form submitted successfully')
                return JsonResponse({'success': True})
        else:
            logger.warning('Form submission failed with errors: %s', form.errors)
            return JsonResponse({'success': False, 'errors': form.errors})
    logger.error('Invalid request method: %s', request.method)
    return JsonResponse({'success': False, 'error': 'Invalid request method'})
