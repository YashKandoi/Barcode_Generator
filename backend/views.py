import os
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse
from .form import DataInputForm
from .API.Main import execute_code

def process_data(request):
    if request.method == 'POST':
        form = DataInputForm(request.POST, request.FILES)
        if form.is_valid():
            # Get the form data
            file_input = request.FILES['file_input']  # Get the file object

            # Save the uploaded file to the 'media/input_files' directory
            file_path = os.path.join(settings.MEDIA_ROOT, 'input_files', file_input.name)
            with open(file_path, 'wb') as destination:
                for chunk in file_input.chunks():
                    destination.write(chunk)

            text_input1 = form.cleaned_data['Tax_Percentage']
            text_input2 = form.cleaned_data['Profit_Percentage']
            # open_ai_input = form.cleaned_data['Open_Ai_input']

            # Save the open_ai_input to openAi.txt
            # open_ai_file_path = os.path.join(settings.KEY_ROOT, 'openAi.txt')
            # with open(open_ai_file_path, 'w') as open_ai_file:
            #     open_ai_file.write(open_ai_input)   


            # Call the execute_code function with the appropriate arguments, passing the file_path
            execute_code(file_path, text_input1, text_input2)

            # Redirect the user to the success page
            return render(request, 'success.html')
    else:
        form = DataInputForm()

    return render(request, 'data_form.html', {'form': form})    

def download_output_csv(request):
    # The code for this view remains unchanged
    output_file_path = request.GET.get('output_file_path')
    if output_file_path:
        with open(output_file_path, 'rb') as output_file:
            response = HttpResponse(output_file.read(), content_type='text/csv')
            response['Content-Disposition'] = 'attachment; filename="output.csv"'
            return response
    else:
        return render(request, 'error.html', {'error_message': 'Output file path not provided.'})

