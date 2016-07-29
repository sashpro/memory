#-%-coding: utf8

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, FormMixin
from two_digits.models import DigitAssoc
from django.core.urlresolvers import reverse_lazy
from django.contrib import messages
import random

# Create your views here.
def index(request):
    success = False 
    if request.method == 'POST':
        dig = request.POST.get('digit')
        word = request.POST.get('word').lower()
        if DigitAssoc.objects.get(digit=int(dig)).word.lower() == word:
            success = True
 
    digit = random.randrange(0,99,1)	
    #print('digit',digit)
    #messages.success(request, DigitAssoc.objects.get(digit=int(dig)).word+' '+str(success))		
    return render(request,"mem_digit/learning.html",{'digit':digit, 'succ':success})
    
    
def learning(request):
    print('Count =',DigitAssoc.objects.count())
    DigitAssoc.objects.create(digit=20, word='',photo='photo')

    if True:#DigitAssoc.objects.count() == 0:
        for n in range(0,100):
            DigitAssoc.objects.create(digit=n, word='',photo='photo')
    digit = DigitAssoc.objects.all()
    #print('digit',digit)
    return render(request,"two_digit/learning.html",{'digit':digit})
	

def digit_edit(request):
    if True:
        if  request.method == 'POST':
            full = DigitAssoc.objects.all()
            for f in full:
                if f.word != request.POST.get(str(f.digit)):  			    
                    f.word = request.POST.get(str(f.digit),'')
                    f.save()
            messages.success(request, "Ассоциации сохранены")#str(list(request.POST.items())))
            return HttpResponseRedirect(reverse_lazy('mem_digit:main'))#render(request,"mem_digit/learning.html")

        if DigitAssoc.objects.count() == 0:
            for n in range(0,100):
                DigitAssoc.objects.create(digit=n, word='')
        digit = DigitAssoc.objects.all()
        return render(request,"two_digits/digitassoc_list.html",{'digits':digit})
			
	
	
	
#class Digit_Form(FormView):
    
	
class List_Digits(ListView, FormMixin):
    model = DigitAssoc
    #template_name ='digitview_list.html'
    success_url=''
	
    def get_context_data(self):
        if DigitAssoc.objects.count() == 0:
            for n in range(0,100):
                DigitAssoc.objects.create(digit=n, word='')
        context = super(List_Digits, self).get_context_data()
        context["digits"] = DigitAssoc.objects.all()
        #context["page_obj"] = self.get_paginator(self.get_queryset(), 2)        
        return context
		
    def form_invalid(self,form):
	     
        return HttpResponseRedirect('mem_digit:main')


	   
    def form_valid(self,form):
        std = form.save()
        messages.success(self.request, u'Info on the student has been sucessfully changed.')
        #return 
        super(StudentUpdateView, self).form_valid(form)
        return HttpResponseRedirect('mem_digit:main')
