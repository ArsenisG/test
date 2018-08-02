from django.shortcuts import render, redirect
from ABCquestionnaire.forms import ValueForm
from ABCquestionnaire.models import Value
from django.http import HttpResponse
from django.contrib.auth.models import User
from ABCquestionnaire.singlestudent import graphs
import matplotlib
matplotlib.use('Agg')
from io import BytesIO, StringIO
import six
from django.template import loader
from ABCquestionnaire.utils import render_to_pdf
from django.template.loader import get_template


def question_values(request):
    form = ValueForm()
    ABCQuestions = {'Q1':'1. Study effectively on your own in independent private study',
        'Q2':'2. Produce your best work under examination conditions',
	    'Q3':'3. Respond to questions asked by a lecturer in front of a full lecture theatre',
	    'Q4':'4. Manage your workload to meet coursework deadlines',
	    'Q5':'5. Give a presentation to a small group of fellow students',
	    'Q6':'6. Attend most taught sessions',
	    'Q7':'7. Attain good grades in your work',
	    'Q8':'8. Engage in profitable academic debate with your peers',
	    'Q9':'9. Ask lecturers questions about the material they are teaching, during a lecture',
	    'Q10':'10. Produce coursework at the required standard',
	    'Q11':'11. Write in an appropriate academic style',
	    'Q12':'12. Be on time for lectures',
	    'Q13':'13. Pass assessments at the first attempt',
	    'Q14':'14. Plan appropriate revision schedules',
	    'Q15':'15. Remain adequately motivated throughout',
	    'Q16':'16. Produce your best work in coursework assignments',
	    'Q17':'17. Attend tutorials',
      }
    return render(request,'ABCquestionnaire/index.html', {'form':form, 'ABCQuestions':ABCQuestions})


from django.core.files.base import ContentFile
def create_survey(request):
    global datas
    # value=Value(user=request.user)
    if request.method=='POST':
        form=ValueForm(request.POST)
        if form.is_valid():
            # request.session['Q1'] = request.POST.get('choice1')                
            answers=form.save(commit=False)
            # answers.user=request.user
            # answers.save()
            datas=[answers.choice1,answers.choice2,answers.choice3,answers.choice4,answers.choice5,answers.choice6,
                answers.choice7,answers.choice8,answers.choice9,answers.choice10,answers.choice11,answers.choice12,
                answers.choice13,answers.choice14,answers.choice15,answers.choice16,answers.choice17,
            ]
            return redirect('/result')
    # for answer in datas:
    #     f=open('data.txt', 'a')
    #     f.write(answer+",")
    # f.write("\n")
    # f.close()
    return render(request,'ABCquestionnaire/result.html',{"datas":datas})
        

def submitted_info(request):
    if 'count' not in request.session:
        request.session['count'] = 0
    request.session['count'] += 1
    return render (request, 'ABCquestionnaire/result.html')
	

def python_code(request):   
	global datas
	global fig5
	global Xfinal
	global ABCX  
	fig1,fig2,fig3,fig4,fig5,Xfinal,ABCX=graphs.python(datas)
	Xfinal=[('Grd',float("{0:.3f}".format(Xfinal[0]))),('Vrb',float("{0:.3f}".format(Xfinal[1]))),('Att',float("{0:.3f}".format(Xfinal[2]))),('Std',float("{0:.3f}".format(Xfinal[3])))]
	Xfinal=sorted(Xfinal,key=lambda x:(-x[1],x[0]))
	template=loader.get_template('ABCquestionnaire/final.html')
	tmp1=six.StringIO()
	fig1.savefig(tmp1, format='svg', bbox_inches='tight')    
	# c1={'svg1':tmp1.getvalue()}
	tmp2=six.StringIO()
	fig2.savefig(tmp2, format='svg', bbox_inches='tight')
	# c2={'svg2':tmp2.getvalue()}
	tmp3=six.StringIO()
	fig3.savefig(tmp3, format='svg', bbox_inches='tight')
	# c3={'svg3':tmp3.getvalue()}
	tmp4=six.StringIO()
	fig4.savefig(tmp4, format='svg', bbox_inches='tight')
	# c4={'svg4':tmp4.getvalue()}
	tmp5=six.StringIO()
	fig5.savefig(tmp5, format='svg', bbox_inches='tight')
	# c5={'svg5':tmp5.getvalue()}
	global c
	c={'svg1':tmp1.getvalue(),'svg2':tmp2.getvalue(),'svg3':tmp3.getvalue(),'svg4':tmp4.getvalue(),'svg5':tmp5.getvalue(),'Xfinal':Xfinal,'ABCX':ABCX}
	return render(request, 'ABCquestionnaire/final.html', c)

def download_figs(request):
    global fig5
    tmp5=six.StringIO()
    fig5.savefig(tmp5, format='svg', bbox_inches='tight')
    return render(request, "ABCquestionnaire/download.html", {"svg5":tmp5.getvalue()})

import base64
import numpy as np
from matplotlib import pyplot as plt
def generate_view(request, *args, **kwargs):
    template=get_template('download.html')
    global fig5
    global Xfinal
    global ABCX
    tmp5=six.BytesIO()
    fig5.savefig(tmp5, format='png', bbox_inches='tight')
    image_base64 = base64.b64encode(tmp5.getvalue()).decode('utf-8').replace('\n', '')
    context= {
        'Xfinal':Xfinal,
        'ABCX':ABCX,
        "svg5":image_base64,
    }
    html=template.render(context)
    pdf=render_to_pdf('download.html',context)
    # figure=download_figs(request)
    if pdf:
        response=HttpResponse(pdf, content_type='application/pdf')
        filename="Information.pdf"
        content="inline; filename='%s'" %(filename)
        response['Content-Dispotition']=content
        # download=request.GET.get("download")
        # if download:
        #     content="attachment; filename='%s'" %(filename)
        return response
    return HttpResponse("Not found")













