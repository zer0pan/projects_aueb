import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
df = pd.read_csv("weather_data.csv")



# zhthma 1
df.update(df['HIGH'].replace(' ',''))
df.update(df['LOW'].replace(' ',''))

df["LOW"]=pd.to_numeric(df["LOW"])
df["HIGH"]=pd.to_numeric(df["HIGH"])

#pd.set_option('display.max_rows',None)

dfh = df["HIGH"].interpolate(method="cubic")
dfl = df["LOW"].interpolate(method="cubic")


leh = [] # list of indexes in the col HIGH containing nan
lel = [] # list of indexes in the col LOW  containing nan

for i in range(365):
    if pd.isna(df.loc[i].at["HIGH"]):
        leh.append(i)
    if pd.isna(df.loc[i].at["LOW"]):   
        lel.append(i)
        
print("Κυβικη παρεμβολη των ελλειπων μεγιστων θερμοκρασιων")
for k in leh:
  print("index ",k,dfh[k])
print()
print("Κυβικη παρεμβολη των ελλειπων ελαχιστων θερμοκρασιων")
for k in lel:
  print("index ",k,dfl[k])                  
print()
del i,k,leh,lel,dfl,dfh

df.update(df['MONTH'].replace(' ','DEC'))
df.update(df['MONTH'].replace('  ','DEC'))

# zhthma 2
df.loc[365] = [None,None,df["TEMP"].mean(),df["HIGH"].max(),None,df["LOW"].min(),None,df["HDD"].sum(),df["CDD"].sum(),df["RAIN"].sum(),None,df["WINDHIGH"].max(),None,None]

# zhthma 3
print("Η διάμεσος των μέσων θεμοκρασιών ειναι : ",df["TEMP"].median())
print("Η τυπική απόκλιση των μέσων θερμοκρασιών ειναι : ",df["TEMP"].std())
print()

# zhthma 4

dirs =list(df["DIR"].unique()) # directions
dirs.pop()

dirn = [0 for i in range(len(dirs))] # λιστα παραλληλη της dirs με τον αριθμο των ημερων που φυσουσε στην διευθυνση της αντιστοιχης κατευθυνσης
for i in range(365):
    dirn[dirs.index(df["DIR"][i])]+=1

for i in range(len(dirs)):
    print("Από την κατεύθυνση ",dirs[i],"φύσιξε",dirn[i],"μέρες")


plt.pie(dirn,labels=dirs,shadow=True)
plt.savefig("my_plot2.png", bbox_inches="tight")

# zhthma 5
htt =list(df["TIME"].unique()) # highest temperature time
htt.pop()

httn= [0 for i in range(len(htt))] # λιστα παραλληλη με με την htt με το συνολο των μεγιστων θερμοκρασιων που συνεβησαν στην αντιστοιχη ωρα
for i in range(365):
    httn[htt.index(df["TIME"][i])]+=1

ltt =list(df["TIME.1"].unique()) # lowest temperature time
ltt.pop()

lttn= [0 for i in range(len(ltt))] # λιστα παραλληλη με με την htt με το συνολο των μεγιστων θερμοκρασιων που συνεβησαν στην αντιστοιχη ωρα
for i in range(365):
    lttn[ltt.index(df["TIME.1"][i])]+=1

print("\n\nΗ ώρα που συνέβησαν οι περισσότερες μέγιστες θερμοκρασίες ηταν: ",htt[httn.index(max(httn))],)
print("Η ώρα που συνέβησαν οι περισσότερες ελάχιστες θερμοκρασίες ηταν: ",ltt[lttn.index(max(lttn))],)

# zhthma 6
print()
df2 = pd.DataFrame({"TEMP":df["TEMP"],"HIGH":df["HIGH"],"LOW":df["LOW"]})
df2 = df2.T

th = -1 
maxvar = -1
for i in range(365):
    if df2[i].var() > maxvar:
        maxvar = df2[i].var()
        th = i

print("Η μέρα του έτους με την μεγαλύτερη διακύμανση ειναι την : ",int(df["DAY"][th]),"of",df["MONTH"][th])

# zhthma 7
print()
print("Η διεύθυνση που φυσούσε τις περισσότερες μέρες του χρόνου είναι η : ",dirs[dirn.index(max(dirn))])

# zhthma 8
print()
maxw = -1
th = -1
for i in range(365):
    if df["WINDHIGH"][i] > maxw:
        maxw = df["WINDHIGH"][i]
        th = i
print("Η διεύθυνση του ανέμου με την μέγιστη ένταση ανέμου είναι η : ",df["DIR"][th])

del th,maxw,maxvar,i 

# zhthma 9
print()
pin = [[df["DIR"][i] for i in range(365)],[df["TEMP"][i] for i in range(365)]] # δισδιαστατος πινακας . 1η διασταση οι διευθυνσεις του ανεμου , 2η διασταση οι μεσες θερμοκρασιες που αντιστοιχουν σε καθε διευθυνση

print("Η διεύθυνση που έδωσε την μεγαλύτερη μέση θερμοκρασία ειναι η : ",pin[0][pin[1].index(max(pin[1]))])
print("Η διεύθυνση που έδωσε την μικρότερη μέση θερμοκρασία ειναι η : ",pin[0][pin[1].index(min(pin[1]))])

# zhthma 10 
months = list(df["MONTH"].unique())
months.pop()
rpm = [0 for i in range(len(months))] # rain per month
for i in range(365):
    rpm[months.index(df["MONTH"][i])] += df["RAIN"][i]

rpm = [round(rpm[i],2) for i in range(len(rpm))]
df3 = pd.DataFrame({"MONTH":months,"RAIN":rpm})

df3.plot(kind='bar',x="MONTH",y="RAIN")
plt.title('Βροχόπτωση ανά μήνα')
plt.savefig("my_plot3.png", bbox_inches="tight")

# zhthma 11
x1 = list(range(1,32))
y1 = list(df["TEMP"][i] for i in range(334,365))# ουσιαστικα οι τελευταιες 31 μερες του ετους

#plt.scatter(x,y)

I = np.ones(len(x1))
A = np.c_[x1,I]
a = np.linalg.lstsq(A,y1,rcond=-1)

xp = np.arange(1,32)
yp = a[0][0]*xp + a[0][1]

ax = plt.subplot(111)

plt.title('Γραμμική παλινδρόμιση\nμέσων θερμοκρασιών Δεκεμβρίου')
ax.scatter(x1,y1)
ax.plot(xp,yp)
plt.savefig("my_plot.png", bbox_inches="tight")

print("Η μεση θερμοκρασία την 25/12/2018 προβλέπεται να είναι : ",np.interp(365+24,x1,y1,right=round(a[0][0]*25+a[0][1],2)),'\n') # απο την 1η δεκεμβριου/2017 + 1 χρονος = 1/12/2018 + 24 μερες = 25/12/2018

# zhthma 12
tx = list(range(334,365)) #time xeimonas
t0 = list(range(59))
tx0 = list(range(31))
tx1 = list(range(31,90))

ta = np.arange(59,151) # anoixis
tk = np.arange(151,242) # kalokairi
tf = np.arange(242,334) # fthinoporo

plt.subplot(411)
plt.title("1.ΧΕΙΜΩΝΑΣ 2.ΑΝΟΙΞΗ 3.ΚΑΛΟΚΑΙΡΙ 4.ΦΘΙΝΟΠΩΡΟ")
plt.plot(tx0,df["TEMP"][tx],'g--',tx1,df["TEMP"][t0],'g--',tx0,df["HIGH"][tx],'r--',tx1,df["HIGH"][t0],'r--',tx0,df["LOW"][tx],'b--',tx1,df["LOW"][t0],'b--')

plt.subplot(412)
plt.plot(ta,df["TEMP"][ta],'g--',ta,df["HIGH"][ta],'r--',ta,df["LOW"][ta],'b--')


plt.subplot(413)
plt.plot(tk,df["TEMP"][tk],'g--',tk,df["HIGH"][tk],'r--',tk,df["LOW"][tk],'b--')

plt.subplot(414)
plt.plot(tf,df["TEMP"][tf],'g--',tf,df["HIGH"][tf],'r--',tf,df["LOW"][tf],'b--')

plt.savefig("my_plot1.png", bbox_inches="tight")

# zhthma 13
def vroxi(x):
    if x < 400:
        print("Λειψυδρία")
    elif x <= 600:
        print("Ικανοποιητικά ποσά βροχής")
    else:
        print("Υπερβολική βροχόπτωση")

print()
vroxi(df["RAIN"][365])
print(df["RAIN"][365])

df.to_csv("new_weather_data.csv")
