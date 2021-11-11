from django.shortcuts import render
from django.views.decorators.http import require_POST
from datetime import date

from .forms import Form2, Form3, Form4, Form5, Form6, Form7, Form8, Form9


def home(request):
    form_2 = Form2()
    form_3 = Form3()
    form_4 = Form4()
    form_5 = Form5()
    form_6 = Form6()
    form_7 = Form7()
    form_8 = Form8(initial={"payment_method": "cash"})
    form_9 = Form9(initial={"notice_date": date.today()})
    return render(
        request,
        "pages/home.html",
        {
            "form_2": form_2,
            "form_3": form_3,
            "form_4": form_4,
            "form_5": form_5,
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
