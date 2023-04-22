from .models import Company, Sneakers
from django.shortcuts import render, get_object_or_404
from cart.forms import CartAddSneakersForm


def support(request):
    return render(request, 'support.html')


def sneakers_list(request, company_slug=None):
    company = None
    companies = Company.objects.all()
    sneakers = Sneakers.objects.filter(available=True)
    if company_slug:
        company = get_object_or_404(Company, slug=company_slug)
        sneakers = sneakers.filter(company=company)
    return render(request, 'list.html',
                  {
                      'company': company,
                      'companies': companies,
                      'sneakers': sneakers,
                  })


def sneakers_detail(request, id, slug):
    sneakers = get_object_or_404(Sneakers, id=id, slug=slug, available=True)
    cart_sneakers_form = CartAddSneakersForm()
    return render(request, 'detail.html',
                  {'sneakers': sneakers,
                   'cart_sneakers_form': cart_sneakers_form})
