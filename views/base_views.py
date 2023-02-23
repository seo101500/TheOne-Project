from operator import truth
from django.shortcuts import redirect, render, get_object_or_404
from theone.models import Seoul


def index(request):
    gu_list = Seoul.objects.order_by('create_Date')
    context = {'gu_list': gu_list}
    if request.user.is_authenticated:
        return render(request, 'theone/search.html',context)
    else:
        return render(request, 'common/login.html')
    
def detail(request, gu_id):
    gu = get_object_or_404(Seoul, pk=gu_id)
    context = {'gu': gu}
    return render(request, 'theone/gu_detail.html',context)