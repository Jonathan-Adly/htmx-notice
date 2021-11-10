from django.shortcuts import render
from django.views.decorators.http import require_POST


def home(request):
    return render(request, "pages/home.html")


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
