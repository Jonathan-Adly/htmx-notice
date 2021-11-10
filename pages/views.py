from django.shortcuts import render
from django.views.decorators.http import require_POST
from datetime import date

from .forms import Form3, Form4, Form6, Form7, Form8, Form9


def home(request):
    form_3 = Form3()
    form_4 = Form4()
    form_6 = Form6()
    form_7 = Form7()
    form_8 = Form8()
    form_9 = Form9()
    return render(
        request,
        "pages/home.html",
        {
            "form_3": form_3,
            "form_4": form_4,
            "form_6": form_6,
            "form_7": form_7,
            "form_8": form_8,
            "form_9": form_9,
        },
    )


def form_1(request):
    if request.method == "POST":
        doc_type = request.POST["radio_1"]
        request.session["doc_type"] = doc_type
        return render(request, "components/form-2.html", {"doc_type": doc_type})

    doc_type = request.session["doc_type"]
    return render(request, "components/form-1.html", {"doc_type": doc_type})


def form_2(request):
    if request.method == "POST":
        landlord_name = request.POST["landlord_name"]

        request.session["landlord_name"] = landlord_name
        return render(
            request,
            "components/form-3.html",
            {"landlord_name": landlord_name},
        )

    landlord_name = request.session["landlord_name"]
    return render(request, "components/form-2.html", {"landlord_name": landlord_name})
