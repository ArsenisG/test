#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  9 15:16:05 2018

@author: arsenios
"""

import numpy as np
import pandas as pd
from . import views
import matplotlib
matplotlib.use('Agg')
from matplotlib import pyplot as plt
from matplotlib import pylab

class graphs:
    def python(datas):
        Grades,Verb,Att,St=np.zeros(6),np.zeros(4),np.zeros(3),np.zeros(4)

        q1=np.array([2,7,10,11,13,16]) #questions of the grades factor
        for i in range(0,len(q1)):
            Grades[i]=datas[q1[i]-1] #set the grade values
                
        q2=np.array([3,5,8,9])
        for i in range(0,len(q2)):
            Verb[i]=datas[q2[i]-1]
            
        q3=np.array([6,12,17])
        for i in range(0,len(q3)):  
            Att[i]=datas[q3[i]-1]

        q4=np.array([1,4,14,15])    
        for i in range(0,len(q4)):
            St[i]=datas[q4[i]-1]

        loadings=np.array([0.57471, 0.63080, 0.78801, 0.55995, 0.80258, 0.79753, 0.69789, 0.69968,
                        0.77465, 0.76411, 0.75837, 0.80312, 0.69860, 0.80645, 0.74723, 0.68176, 0.85382]) # question loadings
        pvariance=np.array([0.22376, 0.16725, 0.14112, 0.13919]) #percent of variance for each factor
        normvar=pvariance/(sum(pvariance)) #normalised variance

        import cmath
        factors=(Grades,Verb,Att,St)
        words=("Grades","Verbalising","Attendance","Studying")
        q=(q1,q2,q3,q4)


        fk=[[] for x in range(len(factors))]
        factorloadings=[[] for x in range(len(factors))]
        w=[[] for x in range(len(factors))]
        for g in range(0,len(factors)):
            for i in range(0,len(factors[g])):  
                fk[g].append((factors[g][i]-1)/(5-1))    #transformation function
                factorloadings[g].append(loadings[q[g][i]-1])   #get the loadings of the factor
            for i in range(0,len(factors[g])):
                w[g].append((factorloadings[g][i])/(sum(factorloadings[g]))) #weightings    
            z=[[] for x in range(len(factors))] #complex number
            zfinal=np.zeros(len(factors[g]),dtype=complex) #create empty array of the final position coordinates
            xco,yco=[[] for x in range(len(factors[g]))],[[] for x in range(len(factors[g]))] #x and y coordinates
            xfinal,yfinal=np.zeros(len(factors[g])),np.zeros(len(factors[g]))
        figList=["fig1","fig2","fig3","fig4"]
        for g in range(0,len(factors)):
            for i in range(0,len(factors[g])):
                z[g].append(w[g][i]*np.exp(cmath.sqrt(-1)*fk[g][i]*np.pi)) #array of imaginary numbers for each grade variable
                zfinal[g]+=w[g][i]*np.exp(cmath.sqrt(-1)*fk[g][i]*np.pi) #imaginary mumber that represents the factor
                xco[g].append((-1)*z[g][i].real) #x component array of the grade variables
                yco[g].append(z[g][i].imag)
            xfinal[g]=(-1)*zfinal[g].real #final x component
            yfinal[g]=zfinal[g].imag #final y component

            
            figList[g]=plt.figure()
            figList[g],ax=plt.subplots() #create semicircle 
            th=np.linspace( 0, np.pi, 100)
            R=1
            xc=R*np.cos(th)
            yc=R*np.sin(th)
            ax.plot(xc,yc,"k-")
            ax.plot([-1,1],(0,0),"k-")
            plt.xticks([])  #removes axis 
            plt.yticks([])
            # plt.axis("equal")
            ax.axis('square')
            plt.ylim(-0.25,1.10)
            ax.spines['right'].set_visible(False)
            ax.spines['top'].set_visible(False)
            ax.spines['bottom'].set_visible(False)
            ax.spines['left'].set_visible(False)
            plt.title("Constellation graph showing confidence in "+words[g]+" of student")# %s" %datas[0])
            #plt.show()
            
            from adjustText import adjust_text
            from matplotlib.pyplot import text    #add text around the semicircle
            ax.arrow(-0.32,-0.20,-0.63,0.0, head_width=0.05, head_length=0.05, fc='k', ec='k')
            ax.arrow(0.32,-0.20,0.63,0.0, head_width=0.05, head_length=0.05, fc='k', ec='k')
            text(-0.26,-0.225,"Confidence",fontsize=15)
            text(-0.07,-0.13,"0.5",fontsize=15)
            text(-1.07,-0.12,"0.0",fontsize=15)
            text(0.95,-0.12,"1.0",fontsize=15)
            text(-0.90,-0.17,"Low",fontsize=13)
            text(0.7,-0.17,"High",fontsize=13)
            #text(-1.07,1.0,"SG-%s" %datas[0],fontsize=18)    
            # plt.show()
            
            alltexts=[] #create a text tuple
            plt.plot(xfinal[g],yfinal[g],"ko") #plot final position
            #alltexts.append(plt.text(xfinal[g],yfinal[g]+0.03,"%s" %datas[0])) #text of studen't number at final position
            x1,y1,x2,y2=0,0,0,0
            ax.plot([0,xco[g][0]],[0,yco[g][0]],"k-") #plot the first coordinate
            alltexts.append(plt.text((xco[g][0]/2),(yco[g][0]/2),"V%d" %q[g][0],fontsize=9)) #text at the first coordinate
            for i in range (0,len(xco[g])-1):
                x1+=xco[g][i]   #x components up to that point which give the ith x coordinate
                y1+=yco[g][i]
                plt.plot([x2+xco[g][i],x1+xco[g][i+1]],[y2+yco[g][i],y1+yco[g][i+1]],"k-") #plot line from one position to the next eg for the first line beginning x is x2+xco[g][0](where both x2 and xco[g][0] are zero) and final x is the first non zero position 
                plt.plot(x1,y1,"ko",ms=4) #plot the new coordinate
                alltexts.append(plt.text(((x2+xco[g][i]+x1+xco[g][i+1])/2),((y2+yco[g][i]+y1+yco[g][i+1])/2),"V%d" %q[g][i+1],fontsize=9)) #add text between points
                x2+=xco[g][i]
                y2+=yco[g][i]
                # plt.show()
            
            plt.plot([xfinal[g],xfinal[g]],[yfinal[g],0],"k--",alpha=0.5,linewidth=1) #plot dashed line from final position to the x axis
            plt.plot(xfinal[g],0,"ko") #plot a dot where the dashed line ends 
            plt.text(xfinal[g],-0.05,"%.3f" %((xfinal[g]+1)/2),fontsize=7) #add the factor confidence value
            adjust_text(alltexts,autoalign='xy',expand_text=(1.05,1.20),expand_points=(1.05,1.20),force_text=(0.1,0.25), #stops the texts(labels) from overlapping 
                force_points=(0.2,0.5),only_move={'points':'xy', 'text':'xy'},text_from_text=True, text_from_points=True)
        #    plt.savefig("Constellation graph of confidence in "+words[g],dpi=1000)
            # plt.show()
            print("The student's confidence in " + words[g] + " is %.2f" %((xfinal[g]+1)/2))
        Xfinal=(xfinal+1)/2
        Xfinal=[round(elem,3) for elem in Xfinal]
        #
        #
        #    
        #add all factors in a graph
        colors=("m","r","g","y")
        wordsshort=("Grd","Vrb","Att","Std")

        
        fig5=plt.figure()
        ax=fig5.add_subplot(1,1,1)
        th=np.linspace( 0, np.pi, 100)
        R=1
        xc=R*np.cos(th)
        yc=R*np.sin(th)
        ax.plot(xc,yc,"k-",alpha=0.5)
        ax.plot([-1,1],(0,0),"k-",alpha=0.3)
        plt.xticks([])
        plt.yticks([])
        # plt.axis("equal")
        ax.axis('square')
        plt.ylim(-0.35,1.05)
        ax.spines['right'].set_visible(False)
        ax.spines['top'].set_visible(False)
        ax.spines['bottom'].set_visible(False)
        ax.spines['left'].set_visible(False)
        # plt.title("Constellation graph showing confidence for all factors")
        # plt.show()

        ax.arrow(-0.32,-0.20,-0.63,0.0, head_width=0.05, head_length=0.05, fc='k', ec='k')
        ax.arrow(0.32,-0.20,0.63,0.0, head_width=0.05, head_length=0.05, fc='k', ec='k')
        text(-0.26,-0.225,"Confidence",fontsize=15)
        # text(-0.07,-0.13,"0.5",fontsize=15)
        text(-1.07,-0.12,"0.0",fontsize=15)
        text(0.95,-0.12,"1.0",fontsize=15)
        text(-0.90,-0.17,"Low",fontsize=13)
        text(0.7,-0.17,"High",fontsize=13)
        #text(-1.07,1.0,"SG-%s" %(datas[0]),fontsize=18)
        # plt.show()

        
        alltexts=[]
        for g in range(0,len(factors)): 
            plt.plot(xfinal[g],yfinal[g],"ko",ms=5)  #plot the final point of each factor
            alltexts.append(plt.text(xfinal[g],yfinal[g],"%s" %wordsshort[g],color=colors[g]))  #label the end points
            x1,y1,x2,y2=0,0,0,0
            ax.plot([0,xco[g][0]],[0,yco[g][0]],color=colors[g],linestyle="-.",label=words[g],alpha=0.5) #plot the first lines going from the origin to the first coordinates
            alltexts.append(plt.text((xco[g][0]/2),(yco[g][0]/2),"V%d" %q[g][0],color=colors[g],fontsize=7))  #lebel the first lines (from the origin to the first points)
            for i in range (0,len(xco[g])-1):
                x1+=xco[g][i]   #x componetns up to that point
                y1+=yco[g][i]
                plt.plot([x2+xco[g][i],x1+xco[g][i+1]],[y2+yco[g][i],y1+yco[g][i+1]],color=colors[g],linestyle="-.",alpha=0.5)
                alltexts.append(plt.text(((x2+xco[g][i]+x1+xco[g][i+1])/2),((y2+yco[g][i]+y1+yco[g][i+1])/2),"V%d" %q[g][i+1],color=colors[g],fontsize=7)) #label the rest of the lines between points
                x2+=xco[g][i]
                y2+=yco[g][i]
                plt.plot(x2,y2,"ko",ms=2,alpha=0.5) #plot the points at the end of each line
            plt.legend(bbox_to_anchor=(0.0, -0.05, 1.0, .10), loc=1, ncol=4, mode="expand", borderaxespad=0.)
            # plt.show()

            plt.plot([xfinal[g],xfinal[g]],[yfinal[g],0],"k--",alpha=0.5,linewidth=1)
            plt.plot(xfinal[g],0,"ko",ms=4) #plot the position of the final factor value
            alltexts.append(plt.text(xfinal[g],-0.05,"%.3f" %((xfinal[g]+1)/2),fontsize=7)) #label the the confidence values of the factors  (have -0.05 as y in order to get the value under the x axis)
            # plt.show()


        ABCx=(sum(xfinal*normvar))
        ABCy=(sum(yfinal*normvar))
        plt.plot(ABCx,ABCy,"ko",ms=6)
        alltexts.append(plt.text(ABCx,ABCy,"ABC")) #label the ABC point
        plt.plot([ABCx,ABCx],[ABCy,0],"k--",alpha=0.5,linewidth=1)
        plt.plot(ABCx,0,"ko",ms=5) #plot the position of the final ABC value
        alltexts.append(plt.text(ABCx,0,"%.3f" %((ABCx+1)/2),fontsize=7,fontweight='bold')) #label the ABC value
        adjust_text(alltexts,autoalign='xy',expand_text=(1.05,1.20),expand_points=(1.05,1.20),force_text=(0.1,0.25), #stops the texts(labels) from overlapping 
            force_points=(0.2,0.5),only_move={'points':'xy', 'text':'xy'},text_from_text=True, text_from_points=True)
        # plt.show()
        # plt.savefig("ABC Constellation graph",dpi=1000)

        C=np.zeros(len(factors))
        for g in range(0,len(factors)):
            C[g]=np.sqrt(pow(xfinal[g],2)+pow(yfinal[g],2))
            #print("The consistency metric of student {0:s} for {1} is {2:.3f}".format(datas[0],words[g],C[g]))
        ABCX=(ABCx+1)/2 #change ABC to a 0 to 1 domain in order to find the final confidence
        ABCX=round(ABCX,3) #round final confidence value to 3 dp
        #print("The ABC value of student {0:s} is {1:.3f}".format(datas[0],ABCX))
        return figList[0],figList[1],figList[2],figList[3],fig5,Xfinal,ABCX
