from django.shortcuts import render
from django.views.decorators.http import require_POST
from datetime import date

from .forms import Form0, Form1, Form2, Form3, Form4, Form5, Form6, Form7, Form8


FORM_LIST = [
    {"The Violation": Form0},
    {"Landlord's Name": Form1},
    {"Landlord's Mailing Address": Form2},
    {"Landlord's Contact Info": Form3},
    {"The Tentant(s)": Form4},
    {"Property Address": Form5},
    {"Lease Start Date": Form6},
    {"Non-Payment of Rent": Form7},
    {"Notice Date": Form8},
    {"Signature Page": ""},
]


def home(request):
    request.session.clear()
    request.session["form_0"] = {"document_type": "rent"}
    form_num = 0
    form = list(FORM_LIST[form_num].values())[0](initial={"document_type": "rent"})
    title = list(FORM_LIST[form_num])[0]
    title_list = []
    for i in FORM_LIST:
        title_list.append([*i][0])

    return render(
        request,
        "pages/home.html",
        {
            "form": form,
            "title_list": title_list,
            "title": title,
            "form_num": form_num,
            "previous_form": form_num,
        },
    )


def form(request, form_num):
    form = list(FORM_LIST[form_num].values())[0]  # FORM0
    title = list(FORM_LIST[form_num])[0]  # Violation
    next_form = form_num + 1  # 1

    if request.method == "POST":  # posting against 0
        form = form(request.POST)  # FORM0(request.POST)
        if form.is_valid():
            if form_num == 6:
                form.cleaned_data["lease_begin_date"] = form.cleaned_data[
                    "lease_begin_date"
                ].strftime("%B %d %Y")
                if request.session["form_0"]["document_type"] == "non_compliance":
                    next_form = next_form + 1
            if form_num == 8:
                form.cleaned_data["notice_date"] = form.cleaned_data[
                    "notice_date"
                ].strftime("%B %d %Y")
                if request.session["form_0"]["document_type"] == "non_compliance":
                    form_num = form_num - 1
            request.session[f"form_{str(form_num)}"] = form.cleaned_data  # form_0
            return render(
                request,
                "components/form.html",
                {
                    "form": list(FORM_LIST[next_form].values())[0],  # FORM1
                    "title": list(FORM_LIST[next_form])[0],  # LandLord Name
                    "form_num": next_form,  # 2
                    "previous_form": form_num,  # 0
                },
            )
        else:
            errors = form.errors
            return render(
                request,
                "components/form.html",  # form-1
                {
                    "errors": errors,
                    "form": form,
                    "title": title,
                    "form_num": form_num,
                    "previous_form": form_num - 1,
                },  # FORM1(request.POST)
            )
    form = form(initial=request.session[f"form_{str(form_num)}"])
    return render(
        request,
        "components/form.html",
        {
            "form": form,
            "title": title,
            "form_num": form_num,
            "previous_form": form_num - 1,
        },
    )


def update_table(request, form_num):
    title_list = []

    for i in FORM_LIST:
        title_list.append([*i][0])

    if request.session["form_0"]["document_type"] == "rent":
        title_list[7] = "Non-Payment of Rent"
    else:
        title_list[7] = "Non-Compliance with The Lease"

    return render(
        request,
        "components/title_list.html",
        {
            "title_list": title_list,
            "selected_title": title_list[form_num],
        },
    )
