import getTrain
import Tkinter as tk
import timeRelated
def countdown(count,train_num,station_name,d,h,m,doj):
    # change text in label
    x=''        
    if d!=0:
    	x=x+'\n    Days  '+str(d)
    if h!=0:
    	x=x+'\n   Hours  '+str(h)
    x=x+'\n Minutes   '+str(m)
    if d==0 and h == 0 and m <=30:
        x=x+"\n\n\tGet Ready."
    label['text'] = "Train "+str(train_num)+" is arriving in"+x;
    if d<0:
        label['text'] = "Time has crossed "+station_name;
        count=100
    if count > 0:
        # call countdown again after 1000ms (1s)
        m=m-1
        if(m==-1):
        	m=59
        	h=h-1
        	if h==-1:
        		h=23
        		d=d-1
        

        root.after(1000, countdown, count-1,train_num,station_name,d,h,m,doj)
    else :
    	actarr_date,actarr=getTrain.getRunningStatus(train_number,doj,station_name)
    	s2=timeRelated.getDates(actarr_date,actarr)
    	s1=timeRelated.getcurtime()
    	d,h,m,s=timeRelated.getDiff(s1,s2)
    	count=1
    	if d>0:
    		count=10
    	elif h>0:
    		count=2  
    	root.after(0, countdown, count,train_num,station_name,d,h,m,doj)

root = tk.Tk()

label = tk.Label(root)
label.place(x=35, y=15)

train_number    = input('Enter train Number:')
stations=[]
stations        = getTrain.getroute(24369)
for i in range(len(stations)):
    print i+1,stations[i]
n=input('Enter station_number:')
station_name    = stations[int(n-1)]
print station_name
doj    = input('Enter DOJ:')


actarr_date,actarr=getTrain.getRunningStatus(train_number,doj,station_name)
s2=timeRelated.getDates(actarr_date,actarr)
s1=timeRelated.getcurtime()
d,h,m,s=timeRelated.getDiff(s1,s2)
countdown(1,train_number,station_name,d,h,m,doj)
root.title('the_simplest')
root.mainloop()


