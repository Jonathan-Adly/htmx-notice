from django.shortcuts import render
from django.views.decorators.http import require_POST
from datetime import date

from .forms import Form1, Form2, Form3, Form4, Form5, Form6, Form7, Form8, Form9


DOCUMENT_TITLE_LIST = [
    "The Violation",
    "Landlord's Name",
    "Landlord's Mailing Address",
    "Landlord's Contact Info",
    "The Tentant(s)",
    "Property Address",
    "Lease Start Date",
    "Non-Payment of Rent",
    "Notice Date",
    "Signature Page",
]


def home(request):
    form = Form1(initial={"document_type": "rent"})
    return render(
        request,
        "pages/home.html",
        {
            "form": form,
            "title_list": DOCUMENT_TITLE_LIST,
        },
    )


def update_table(request, form_num):
    if request.session["form_1"]["document_type"] == "rent":
        DOCUMENT_TITLE_LIST[7] = "Non-Payment of Rent"
    else:
        DOCUMENT_TITLE_LIST[7] = "Non-Compliance with The Lease"

    return render(
        request,
        "components/title_list.html",
        {
            "title_list": DOCUMENT_TITLE_LIST,
            "selected_title": DOCUMENT_TITLE_LIST[form_num],
        },
    )


def form_1(request):
    if request.method == "POST":
        form = Form1(request.POST)
        if form.is_valid():
            request.session["form_1"] = form.cleaned_data
            return render(request, "components/form-2.html", {"form": Form2()})
        else:
            errors = form.errors
            return render(
                request, "components/form-1.html", {"errors": errors, "form": form}
            )
    form = Form1(initial=request.session["form_1"])
    return render(request, "components/form-1.html", {"form": form})


def form_2(request):
    if request.method == "POST":
        form = Form2(request.POST)
        if form.is_valid():
            request.session["form_2"] = form.cleaned_data
            return render(request, "components/form-3.html", {"form": Form3()})
        else:
            errors = form.errors
            return render(
                request, "components/form-2.html", {"errors": errors, "form": form}
            )

    form = Form2(initial=request.session["form_2"])
    return render(request, "components/form-2.html", {"form": form})


def form_3(request):
    if request.method == "POST":
        form = Form3(request.POST)
        if form.is_valid():
            request.session["form_3"] = form.cleaned_data
            return render(request, "components/form-4.html", {"form": Form4()})
        else:
            errors = form.errors
            return render(
                request, "components/form-3.html", {"errors": errors, "form": form}
            )

    form = Form3(initial=request.session["form_3"])
    return render(request, "components/form-3.html", {"form": form})


def form_4(request):
    if request.method == "POST":
        form = Form4(request.POST)
        if form.is_valid():
            request.session["form_4"] = form.cleaned_data
            return render(request, "components/form-5.html", {"form": Form5()})  # +1
        else:
            errors = form.errors
            return render(
                request, "components/form-4.html", {"errors": errors, "form": form}
            )

    form = Form4(initial=request.session["form_4"])
    return render(request, "components/form-4.html", {"form": form})


def form_5(request):
    if request.method == "POST":
        form = Form5(request.POST)  # same
        if form.is_valid():
            request.session["form_5"] = form.cleaned_data  # same
            return render(request, "components/form-6.html", {"form": Form6()})  # +1
        else:
            errors = form.errors
            return render(
                request,
                "components/form-5.html",
                {"errors": errors, "form": form},  # same
            )

    form = Form5(initial=request.session["form_5"])  # same
    return render(request, "components/form-5.html", {"form": form})  # same


def form_6(request):
    if request.method == "POST":
        form = Form6(request.POST)  # same
        if form.is_valid():
            request.session["form_6"] = form.cleaned_data  # same
            return render(request, "components/form-7.html", {"form": Form7()})  # +1
        else:
            errors = form.errors
            return render(
                request,
                "components/form-6.html",
                {"errors": errors, "form": form},  # same
            )

    form = Form6(initial=request.session["form_6"])  # same
    return render(request, "components/form-6.html", {"form": form})  # same


def form_7(request):
    if request.method == "POST":
        form = Form7(request.POST)  # same
        if form.is_valid():
            form.cleaned_data["lease_begin_date"] = form.cleaned_data[
                "lease_begin_date"
            ].strftime("%B %d %Y")
            request.session["form_7"] = form.cleaned_data  # same
            if request.session["form_1"]["document_type"] == "rent":
                return render(
                    request, "components/form-8-optional.html", {"form": Form8()}
                )  # +1
            return render(request, "components/form-9.html", {"form": Form9()})
        else:
            errors = form.errors
            return render(
                request,
                "components/form-7.html",
                {"errors": errors, "form": form},  # same
            )

    form = Form7(initial=request.session["form_7"])  # same
    return render(request, "components/form-7.html", {"form": form})  # same


def form_8(request):
    if request.method == "POST":
        form = Form8(request.POST)  # same
        if form.is_valid():
            request.session["form_8"] = form.cleaned_data  # same
            return render(request, "components/form-9.html", {"form": Form9()})  # +1
        else:
            errors = form.errors
            return render(
                request,
                "components/form-8-optioanl.html",
                {"errors": errors, "form": form},  # same
            )

    form = Form8(initial=request.session["form_8"])  # same
    return render(request, "components/form-8-optional.html", {"form": form})  # same


def form_9(request):
    doc_type = request.session["form_1"]["document_type"]
    if request.method == "POST":
        form = Form9(request.POST)  # same
        if form.is_valid():
            form.cleaned_data["notice_date"] = form.cleaned_data[
                "notice_date"
            ].strftime("%B %d %Y")
            request.session["form_9"] = form.cleaned_data  # same
            return render(request, "components/form-10.html")  # +1
        else:
            errors = form.errors
            return render(
                request,
                "components/form-9.html",
                {"errors": errors, "form": form},  # same
            )

    form = Form9(initial=request.session["form_9"])  # same
    return render(
        request, "components/form-9.html", {"form": form, "doc_type": doc_type}
    )  # same


def form_10(request):
    if request.method == "POST":
        pass

    # same
    return render(request, "components/form-10.html")  # same
