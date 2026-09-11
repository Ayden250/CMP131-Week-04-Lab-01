#Ayden Suarez
#CMP_131
#Week_4
#9/16/2026
movie=input("enter movie name")
child_ticket=int(input("number of child ticket"))
adult_ticket=int(input("number of adult tickets"))
Gross_box= adult_ticket*10 + child_ticket*6
Net_box= Gross_box*0.2 
Amount=Gross_box-Net_box
print("Movie name:", movie)
