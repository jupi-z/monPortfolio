from django.shortcuts import render
from .models import Article
from .models import ContactForm
from .models import Project


# Create your views here.
# request permet d envoyer ou de recuperer les donnee via le http
# context permet d envoyer le code python vers le  html


def accueilVenteView(request, template_name="meuble/pages/index.html"):
    # declaration de notre context
    context = {}
    bonjour = "Bonjour tout le monde"
    # affectation de la clef dans notre context
    # recuperation de la clef
    #       clef     VALEUR

    # instance Article
    # a1 = Article("Chaise", "Meuble de salon ")
    # a2 = Article("Table", "Meuble de salon ")
    # a3 = Article("Fauteuil", "Meuble de salon ")
    # a4 = Article("Vitrine", "Meuble de salon ")
    # a5 = Article("Tabouret", "Meuble de salon ")
    # a6 = Article("Table_Télévisur", "Meuble de salon ")
    # a7 = Article("Mini-Bar", "Meuble de salon ")
    # a8 = Article("Armoir", "Meuble de salon ")
    # list_article = [a1, a2, a3, a4, a5, a6, a7, a8]
    # SELECT * FROM Article; avec SQL
    # AVEC L'ORM :

    list_article = Article.objects.all()

    context['name'] = bonjour
    context['article'] = list_article

    return render(request, template_name, context)


def aboutView(request, template_name="meuble/pages/about.html"):
    # declaration de notre context

    context = {}
    bonjour = "Bonjour tout le monde"

    # affectation de la clef dans notre context
    # recuperation de la clef
    #       clef     VALEUR
    context['name'] = bonjour
    return render(request, template_name, context)


def contactView(request, template_name="meuble/pages/contact.html"):
    context = {}
    contacts = ContactForm.objects.all()
    context["contacts"] = contacts
    # On vérifie si la methode  http de la requette est POST
    if request.method == "POST":
        # On recupère les valeur entrées par l'utilisateur !

        name = request.POST['name']
        email = request.POST['email']
        sujet = request.POST['sujet']
        message = request.POST['message']

        # On appelle la classe ContactForm / on créé notre objet Contact
        obj_contact = ContactForm(
            name=name,
            email=email,
            sujet=sujet,
            message=message
        )

        obj_contact.save()

    return render(request, template_name, context)


def portfolio(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'portfolio.html', context)


def portfolio(request):
    projects = Project.objects.all()
    context = {
        'projects': projects
    }
    return render(request, 'portfolio.html', context)
