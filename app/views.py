import io
import os
import shutil
import tempfile
import zipfile

from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.views.generic import TemplateView, View
from pbr.pbr import PBR

from app.models import *
from app.forms import *

class LandingPageView(TemplateView):
    template_name = "landing_page.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['generate_form'] = kwargs.get('generate_form', GenerateForm())
        return context

class GenerateView(View):
    def post(self, request, *args, **kwargs):
        response = {}
        form = GenerateForm(request.POST)
        if form.is_valid():
            seed = form.cleaned_data['seed']
            pbr_zip_data = get_pbr_zip_data(seed)
            response = HttpResponse(pbr_zip_data, content_type='application/zip')
            response['Content-Disposition'] = 'attachment; filename="pbr_{seed}.zip"'.format(seed=seed)
            return response
        else:
            return LandingPageView.as_view()(self.request, generate_form=form)


def get_pbr_zip_data(seed):
    with tempfile.TemporaryDirectory() as temp_dir:
        pbr_instance = PBR(seed)
        pbr_instance.process()
        pbr_instance.save(temp_dir)
        bytes_io = io.BytesIO()
        with zipfile.ZipFile(bytes_io, 'w') as zip_file:
            for root, directories, filenames in os.walk(temp_dir):
                for filename in filenames:
                    file_path = os.path.join(root, filename)
                    archive_name = os.path.relpath(file_path, temp_dir)
                    zip_file.write(file_path, archive_name)
        return bytes_io.getvalue()
