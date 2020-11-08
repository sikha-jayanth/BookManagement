from django.shortcuts import render, redirect
from books.models import Book
from books.forms import BookCreateForms,BookpUpdateForm

# Create your views here.
def bookCreate(request):
    template_name="bookcreate.html"
    form=BookCreateForms()
    context={}
    context["form"]=form
    queryset = Book.objects.all()
    context["books"] = queryset
    if request.method=="POST":
        form=BookCreateForms(request.POST)
        if form.is_valid():
            # book_name=form.cleaned_data.get("book_name")
            # author=form.cleaned_data.get("author")
            # price=form.cleaned_data.get("price")
            # pages=form.cleaned_data.get("pages")
            # obj=Book(book_name=book_name,author=author,price=price,pages=pages)
            # obj.save()
            form.save()
            return render(request,template_name,context)
        else:
            context["form"]=form
            return render(request, template_name, context)



    return render(request,template_name,context)



def viewBooks(request,pk):
    template_name="viewbooks.html"
    qs=Book.objects.get(id=pk)
    context={}
    context["book"]=qs
    return render(request,template_name,context)

def deleteBooks(request,pk):
    Book.objects.get(id=pk).delete()
    return redirect("create")

def updateBooks(request,pk):
    template_name="bookupdate.html"
    book=Book.objects.get(id=pk)
    form=BookpUpdateForm(instance=book)
    context={}
    context["form"]=form
    if request.method=='POST':
        form=BookpUpdateForm(instance=book,data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("create")
    return render(request,template_name,context)






