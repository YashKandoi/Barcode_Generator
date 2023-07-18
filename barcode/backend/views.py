import os
from django.shortcuts import render

from Main import execute_code
from .serializer import formSerializer


def my_view(request):
    if request.method == 'POST':
        form = formSerializer(request.POST, request.FILES)
        if form.is_valid():
            my_model = form.save(commit=False)
            
            output_file_name = process_inputs_and_generate_name(my_model)            
            output_file_path = os.path.join('output_files', output_file_name)
            my_model.output_file.save(output_file_path, request.FILES['input_file1'])
            
            context = {'file_output_path': my_model.output_file.url}
            return render(request, 'result.html', context)
    else:
        form = formSerializer()
    
    return render(request, 'form.html', {'form': form})


def process_inputs_and_generate_name(form_instance):
    text_input1 = form_instance.text_input1
    text_input2 = form_instance.text_input2
    text_input3 = form_instance.text_input3
    text_input4 = form_instance.text_input4
    file_path="../media/input_files/abcd.pdf"
    execute_code(file_path, text_input1, text_input2)

    output_file_name = "./output_files/temp.csv"
    return output_file_name


