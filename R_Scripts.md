# R Scripts (Exhaustive analyses)

### R Scripts for Research Question 1

Research Question 1: What is the case load with respect to programs, job titles, and staff?

We will look for the relationship between
Program Name -> Unique Record ID
Program Name -> Job Title
Program Name -> Staff Name
And
Facility -> Job Title
Facility -> Staff Title

Our objective is to understand
-how many people are enrolled in each program? And how much do they use each program?
-how many staff members work in each program and specific facilities?
-how many job titles work in each program and specific facilities?
-how many staff members work in multiple facilities and programs?

**_Analysis 1: how many people are enrolled in each program_**
```{r}
#df1 has unique records of the columns recordID and program_name combined.
ggplot(df1, aes(x=reorder(Var1,+Freq), y=Freq)) +
  ggtitle("Total number of clients enrolled into each program")+
  xlab("Program Name") +
  ylab("Number of Records")+
  geom_bar(stat="identity", fill="steelblue")+
  geom_text(aes(label=Freq), vjust=-0.3, color="black", size=3.5)+
  theme_minimal()+theme(axis.text.x=element_text(angle=45,hjust=1))
names(df1)[1]<-"program_names"
names(df1)[2]<- "number_unique_recordID"
```
**_Summary:_** In this graph we can see how many people are enrolled in each program. This is done by finding unique record IDs for program names. Therefore, this might include people who are in more than 1 program. As we can see Mental Health is more utilized currently. There are very few people who are utilizing the Gambling programs. This may be due to the fact that the Gambling program is only offered in certain places, is less funded, or is a new program.

**_how many people are enrolled in each program_**

<p  align="middle">
  <img src="https://github.com/121107/Data/blob/master/Images/11.PNG" width="700", height="300" />
</p>

 **_Analysis 2: average number of visits for each program_**
 ```{r}
 library(tidyverse)
 df2 <- as.data.frame(table(Program_Facility_Staff12$program_name))
 df2[3]<-df1$number_unique_recordID
 df2[4]<-round(df2$Freq/df2[3],2)
 names(df2)[1]<-"program_name"
 names(df2)[2]<-"frequency_of_utilization"
 names(df2)[3]<-"number_of_unique_clients"
 names(df2)[4]<-"average_visits"
 ggplot(df2, aes(x=reorder(program_name, +average_visits), y=average_visits)) +
   ggtitle("Number of times a program is utilized")+
   xlab("Program Name") +
   ylab("Average Visits")+
   geom_bar(stat="identity", fill="steelblue")+
   geom_text(aes(label=average_visits), vjust=-0.3, color="black", size=3.5)+
   theme_minimal()+theme(axis.text.x=element_text(angle=45,hjust=1))
 ```

**_Summary:_** This graph shows the average number of visits for each program. To do this we divided the frequency of utilization by the number of clients for each program. As we can see the people who attend substance Use programs tend to come back more often than those who do not. This may be due to insurance allotments for visits or it could just be the atmosphere for the substance Use programs retain more people because the way they function.

 **_average number of visits for each program_**

 <p  align="middle">
   <img src="https://github.com/121107/Data/blob/master/Images/12.PNG" width="700", height="300" />
 </p>

**_Analysis 3: the number of therapists, specialists, and other people working for each program_**
```{r}
Program_Facility_Staff12A<-Program_Facility_Staff12 %>% filter(facility=="Heartland Family Service - Gendler")
Gendler<-as.data.frame(table(Program_Facility_Staff12A))

# Program Name -> Job Title
# This shows the frequency of jobs performed in each program offered by HFS-Gendler
ggplot(Gendler, aes(x=reorder(job_title,+Freq), y=Freq, fill=facility))+geom_col(position = "dodge", fill="steelblue")+facet_wrap(Gendler$program_name)+theme(axis.text.x=element_text(angle=45,hjust=1))+ggtitle("Employment by Programs offered by HFS-Gendler")+xlab("Program Name")+ylab("Amount of Employees")+geom_text(aes(label=Freq), vjust=-0.3, color="black", size=3.5)
```

**_Summary:_** This graph shows the number of therapists, specialists, and other people working for each program at the Gendler site. This site is one of the top visited facility. The size of this was expected due to the amount of demand for each program.

**_the number of therapists, specialists, and other people working for each program_**

<p  align="middle">
  <img src="https://github.com/121107/Data/blob/master/Images/13.PNG" width="700", height="300" />
</p>

# Employment by programs offered by different schools
In this analysis, we showed how the employment distributed for different programs (Mental Health, Substance Use and Gambling) in different facilities (specifically schools).

<table>
  <tr>
    <td> Abraam Linc. high school is covered by only one of the main cost centers.</td>
     <td>Bellevue Reporting Center there are mostly therapists but there is also 1 other employee.</td>
  </tr>
  <tr>
    <td><img src="https://github.com/121107/Data/blob/master/Images/14.PNG" width=700 height=300></td>
    <td><img src="https://github.com/121107/Data/blob/master/Images/15.PNG" width=700 height=300></td>
  </tr>
  <tr>
    <td> This is a location where more than one program is offered. As we can see a majority of the people in direct contact with clients are therapists.</td>
     <td>HFS’s Central location mental health and substance Use are both offered. The mental health program has more employees, as expected</td>
  </tr>
  <tr>
    <td><img src="https://github.com/121107/Data/blob/master/Images/16.PNG" width=700 height=300></td>
    <td><img src="https://github.com/121107/Data/blob/master/Images/17.PNG" width=700 height=300></td>
  </tr>
  <tr>
    <td> HFS Child and Family facility (HFSCFF) they have a mental health program with more other staff interacting with clients. This may be due to the clients that they serve.</td>
     <td>the previous graph (HFSCFF) this has more other employees than normal. Therefore, the other workers might be interacting more with the clients due to the type of clients</td>
  </tr>
  <tr>
    <td><img src="https://github.com/121107/Data/blob/master/Images/18.PNG" width=700 height=300></td>
    <td><img src="https://github.com/121107/Data/blob/master/Images/19.PNG" width=700 height=300></td>
  </tr>
  <tr>
    <td> they offer two different programs, which have a lot of attendance as seen in previous graphs, there are not a lot of employees at this facility.</td>
     <td>facility is an HFS called Heartland Homes. It is a transitional housing for those people who need services but are also homeless.</td>
  </tr>
  <tr>
    <td><img src="https://github.com/121107/Data/blob/master/Images/20.PNG" width=700 height=300></td>
    <td><img src="https://github.com/121107/Data/blob/master/Images/21.PNG" width=700 height=300></td>
  </tr>
  <tr>
    <td> graph shows the employees at HFS-Lakin. There are only a few employees here.</td>
     <td>graph shows the employees that work at HFS - Logan. Though it does offer two programs, Mental Health and Substance Use, there are very few Therapists doing substance use sessions here.</td>
  </tr>
  <tr>
    <td><img src="https://github.com/121107/Data/blob/master/Images/22.PNG" width=700 height=300></td>
    <td><img src="https://github.com/121107/Data/blob/master/Images/23.PNG" width=700 height=300></td>
  </tr>
  <tr>
    <td> graph shows the employees at HFS - Sarpy. Although this is one of the top used locations, it doesn’t have as many Therapists as Gendler does.</td>
     <td>graph shows that there is 1 therapist at the Kanesville Alternative Learning Center.</td>
  </tr>
  <tr>
    <td><img src="https://github.com/121107/Data/blob/master/Images/24.PNG" width=700 height=300></td>
    <td><img src="https://github.com/121107/Data/blob/master/Images/25.PNG" width=700 height=300></td>
  </tr>
  <tr>
    <td> Junior High is a school that HFS offers services at. Once again we see all schools only are offered Mental Health services and mainly have Therapists.</td>
     <td>We noticed that the schools in Lewis Central were not funded under any sc_code or were covered by the sc_code 1311-54. However, the mental health program is obviously very utilized. </td>
  </tr>
  <tr>
    <td><img src="https://github.com/121107/Data/blob/master/Images/26.PNG" width=700 height=300></td>
    <td><img src="https://github.com/121107/Data/blob/master/Images/27.PNG" width=700 height=300></td>
  </tr>
  <tr>
    <td> Terapist has significant impact.</td>
     <td>Terapist has significant impact. </td>
  </tr>
  <tr>
    <td><img src="https://github.com/121107/Data/blob/master/Images/28.PNG" width=700 height=300></td>
    <td><img src="https://github.com/121107/Data/blob/master/Images/29.PNG" width=700 height=300></td>
  </tr>
  <tr>
    <td> Terapist has significant impact.</td>
     <td>Micah house is one of the most utilized facilities. The fact that it only has therapists working with clients makes it unique. </td>
  </tr>
  <tr>
    <td><img src="https://github.com/121107/Data/blob/master/Images/30.PNG" width=700 height=300></td>
    <td><img src="https://github.com/121107/Data/blob/master/Images/31.PNG" width=700 height=300></td>
  </tr>
  <tr>
    <td> Omaha Intergenerational Campus is not in the top 5 most utilized facilities. However, the amount of employees is higher than most of the top 5 utilized facilities.</td>
     <td>the graph shows the same trends of having higher amounts of therapists in Mental Health and less in Substance Use. This is specifically looking at the Omaha Blondo Reporting Center. </td>
  </tr>
  <tr>
    <td><img src="https://github.com/121107/Data/blob/master/Images/32.PNG" width=700 height=300></td>
    <td><img src="https://github.com/121107/Data/blob/master/Images/33.PNG" width=700 height=300></td>
  </tr>
  <tr>
    <td> a graph of Omaha (Spring) Reporting Center. It has only therapists working with patients.</td>
     <td>the sanctuary house. It has only other employees working there. For this specific facility, it seems reasonable to have a small regular number of staff at these facilities.</td>
  </tr>
  <tr>
    <td><img src="https://github.com/121107/Data/blob/master/Images/34.PNG" width=700 height=300></td>
    <td><img src="https://github.com/121107/Data/blob/master/Images/35.PNG" width=700 height=300></td>
  </tr>
  <tr>
    <td> again is a school where only mental health programs are offered and only therapists are available. It is a school in the Council Bluffs District.</td>
     <td>school has a high number number of therapists compared with other schools from the Council Bluffs School District.</td>
  </tr>
  <tr>
    <td><img src="https://github.com/121107/Data/blob/master/Images/36.PNG" width=700 height=300></td>
    <td><img src="https://github.com/121107/Data/blob/master/Images/37.PNG" width=700 height=300></td>
  </tr>

 </table>


```{r}
#This shows the number of times a particular job title served in various programs
ggplot(df4, aes(x=reorder(Var1, +Freq), y=Freq)) +
  ggtitle("Number of times a particular job title served in programs")+
  xlab("Job Title") +
  ylab("Number of Records")+
  geom_bar(stat="identity", fill="steelblue")+
  geom_text(aes(label=Freq), vjust=-0.3, color="black", size=3.5)+
  theme_minimal()
```
**_the interactions between clients and employees (where a majority are therapists)_**

<p  align="middle">
  <img src="https://github.com/121107/Data/blob/master/Images/38.PNG" width="700", height="300" />
</p>

```{r}
#creating a data frame with only job_title, staff_name and program_name columns from the HFS data
staffjob<-as.data.frame(table(HFS$job_title,HFS$staff_name,HFS$program_name))

#filtering for only "Therapist" job title and "Gambling" program from the above data frame
TherapistG<-staffjob %>% filter(Var1=="Therapist"& Var3=="Gambling"&Freq!=0)

#filtering for only "Therapist" job title and "Mental Health" program from the above data frame
TherapistM<-staffjob %>% filter(Var1=="Therapist"& Var3=="Mental Health"&Freq!=0)

#filtering for only "Therapist" job title and "Substance Use" program from the above data frame
TherapistS<-staffjob %>% filter(Var1=="Therapist"& Var3=="Substance Use"& Freq!=0)

#filtering for only "Specialist" job title and "Gambling" program from the above data frame
SpecialistG<-staffjob %>% filter(Var1=="Specialist"&Var3=="Gambling"&Freq!=0)

#filtering for only "Specialist" job title and "Mental Health" program from the above data frame
SpecialistM<-staffjob %>% filter(Var1=="Specialist"&Var3=="Mental Health"&Freq!=0)

#filtering for only "Specialist" job title and "Substance Use" program from the above data frame
SpecialistS<-staffjob %>% filter(Var1=="Specialist"&Var3=="Substance Use"&Freq!=0)

#filtering for only "Other" job title and "Gambling" program from the above data frame
OtherG<-staffjob %>% filter(Var1=="Other"&Var3=="Gambling"&Freq!=0)

#filtering for only "Other" job title and "Mental Health" program from the above data frame
OtherM<-staffjob %>% filter(Var1=="Other"&Var3=="Mental Health"&Freq!=0)

#filtering for only "Other" job title and "Substance Use" program from the above data frame
OtherS<-staffjob %>% filter(Var1=="Other"&Var3=="Substance Use"&Freq!=0)
```

```{r}
# Case load 1
#This show the number of time a each therapist of HFS served for the "Gambling" Program
ggplot(TherapistG, aes(x=reorder(Var2,+Freq), y=Freq))+geom_col(position ="dodge", fill="steelblue")+theme(axis.text.x=element_text(angle=45,hjust=1))+xlab("Staff Member")+ylab("Frequency of work")+ggtitle("Therapist's case load for Programs about Gambiling")+geom_text(aes(label=Freq), vjust=-0.3, color="black", size=3.5)

# case load 2
#This show the number of time a each therapist of HFS served for the "Mental Health" Program
TherapistM<-TherapistM %>% top_n(10, Freq)
ggplot(TherapistM, aes(x=reorder(Var2,+Freq), y=Freq))+geom_col(position ="dodge", fill="steelblue")+theme(axis.text.x=element_text(angle=45,hjust=1))+xlab("Staff Member")+ylab("Frequency of work")+ggtitle("Top 10 Therapist's case load for Programs about Mental Health")+geom_text(aes(label=Freq), vjust=-0.3, color="black", size=3.5)

# case load 3
#This show the number of time a each therapist of HFS served for the "Substance Use" Program
TherapistS<-TherapistS %>% top_n(10,Freq)
ggplot(TherapistS, aes(x=reorder(Var2,+Freq), y=Freq))+geom_col(position ="dodge", fill="steelblue")+theme(axis.text.x=element_text(angle=45,hjust=1))+xlab("Staff Member")+ylab("Frequency of work")+ggtitle("Therapist's case load for Programs about Substance Use")+geom_text(aes(label=Freq), vjust=-0.3, color="black", size=3.5)

# Case load 4
#This show the number of time a each specialist of HFS served for the "Gambling" Program
ggplot(SpecialistG, aes(x=reorder(Var2,+Freq), y=Freq))+geom_col(position ="dodge", fill="steelblue")+theme(axis.text.x=element_text(angle=45,hjust=1))+xlab("Staff Member")+ylab("Frequency of work")+ggtitle("Specialist's case load for Programs about Gambiling")+geom_text(aes(label=Freq), vjust=-0.3, color="black", size=3.5)

# case load 5
#This show the number of time a each Specialist of HFS served for the "Mental Health" Program
ggplot(SpecialistM, aes(x=reorder(Var2,+Freq), y=Freq))+geom_col(position ="dodge", fill="steelblue")+theme(axis.text.x=element_text(angle=45,hjust=1))+xlab("Staff Member")+ylab("Frequency of work")+ggtitle("Specialist's case load for Programs about Mental Health")+geom_text(aes(label=Freq), vjust=-0.3, color="black", size=3.5)

# case load 6
#This show the number of time a each Specialist of HFS served for the "Substance Use" Program
ggplot(SpecialistS, aes(x=reorder(Var2,+Freq), y=Freq))+geom_col(position ="dodge", fill="steelblue")+theme(axis.text.x=element_text(angle=45,hjust=1))+xlab("Staff Member")+ylab("Frequency of work")+ggtitle("Specialist's case load for Programs about Substance Use")+geom_text(aes(label=Freq), vjust=-0.3, color="black", size=3.5)

# Case load 7
#This show the number of time other staff members of HFS served for the "Gambling" Program
ggplot(OtherG, aes(x=reorder(Var2,+Freq), y=Freq))+geom_col(position ="dodge", fill="steelblue")+theme(axis.text.x=element_text(angle=45,hjust=1))+xlab("Staff Member")+ylab("Frequency of work")+ggtitle("Other Staff's case load for Programs about Gambiling")+geom_text(aes(label=Freq), vjust=-0.3, color="black", size=3.5)

# Case load 8
#This show the number of time other staff members of HFS served for the "Mental Health" Program
OtherM<-OtherM %>% top_n(10,Freq)
ggplot(OtherM, aes(x=reorder(Var2,+Freq), y=Freq))+geom_col(position ="dodge", fill="steelblue")+theme(axis.text.x=element_text(angle=45,hjust=1))+xlab("Staff Member")+ylab("Frequency of work")+ggtitle("Top 10 Other Staff's case load for Programs about Mental Health")+geom_text(aes(label=Freq), vjust=-0.3, color="black", size=3.5)

# Case load 9
#This show the number of time other staff members of HFS served for the "Substance Use" Program
OtherS<-OtherS%>% top_n(10,Freq)
ggplot(OtherS, aes(x=reorder(Var2,+Freq), y=Freq))+geom_col(position ="dodge", fill="steelblue")+theme(axis.text.x=element_text(angle=45,hjust=1))+xlab("Staff Member")+ylab("Frequency of work")+ggtitle("Top 10 Other Staff's case load for Programs about Substance Use")+geom_text(aes(label=Freq), vjust=-0.3, color="black", size=3.5)
```

## **_Therapist and other specialists case load based on programs_**

<table>
  <tr>
    <td> Case load 1:the therapists currently working with the gambling program. As we can see three of the therapistss are doing a majority of the work </td>
     <td>Case load 2: the top 10 therapists working for the Mental Health Program. We can see a majority of the work is being done by a few therapists. Peggy Eppdito and Kiel Hansen are in all three graphs showing the top therapists.</td>
  </tr>
  <tr>
    <td><img src="https://github.com/121107/Data/blob/master/Images/39.PNG" width=700 height=300></td>
    <td><img src="https://github.com/121107/Data/blob/master/Images/40.PNG" width=700 height=300></td>
  </tr>
  <tr>
    <td> Case load 3: the top ten therapists case load in the substance use programs.</td>
     <td>Case load 4: the graph show the specialists and their case load. Courtney Winkler is in all three graphs. Christian Thomas is in the graphs and the graph for case load 5.</td>
  </tr>
  <tr>
    <td><img src="https://github.com/121107/Data/blob/master/Images/41.PNG" width=700 height=300></td>
    <td><img src="https://github.com/121107/Data/blob/master/Images/42.PNG" width=700 height=300></td>
  </tr>
  <tr>
    <td> Case load 5: the graph show the specialists and their case load. Courtney Winkler is in all three graphs. Christian Thomas is in the graphs and the graph for case load 4.</td>
     <td>Case load 6: the other employyes that work in each program. Rachel Hobza, Megan Cheney, Victoria Cassidy, Florentina Anderson, and Diane Cox are in two of the graphs.</td>
  </tr>
  <tr>
    <td><img src="https://github.com/121107/Data/blob/master/Images/43.PNG" width=700 height=300></td>
    <td><img src="https://github.com/121107/Data/blob/master/Images/44.PNG" width=700 height=300></td>
  </tr>
  <tr>
    <td> Case load 7:</td>
     <td>Case load 8:</td>
  </tr>
  <tr>
    <td><img src="https://github.com/121107/Data/blob/master/Images/45.PNG" width=700 height=300></td>
    <td><img src="https://github.com/121107/Data/blob/master/Images/46.PNG" width=700 height=300></td>
  </tr>
  <tr>
    <td> Case load 9:</td>

  </tr>
  <tr>
    <td><img src="https://github.com/121107/Data/blob/master/Images/47.PNG" width=700 height=300></td>
  </tr>
 </table>

```{r}
#Creating a data frame with facility and job_title columns from the HFS data
facilityjob<-as.data.frame(table(HFS$facility,HFS$job_title))

#filtering for records which have atleast one occurance
facilityjob<-facilityjob %>% filter(Freq!=0)

#filtering for records which have the only the HFS facilities -"Heartland Family Service - Child and Family Center" , "Heartland Family Service - Gendler", "Heartland Family Service - Heartland Homes", "NHeartland Family Service - Logan", "Heartland Family Service - Sarpy", "Heartland Family Service - Lakin", "Heartland Family Service - Glenwood", "Heartland Family Service - Family Works Nebraska",, "Heartland Family Service - Central"
facilityjobHFS<-facilityjob %>% filter(Var1=="Heartland Family Service - Child and Family Center"|Var1=="Heartland Family Service - Gendler"|Var1=="Heartland Family Service - Heartland Homes"|Var1=="NHeartland Family Service - Logan"|Var1=="Heartland Family Service - Sarpy"|Var1=="Heartland Family Service - Lakin"|Var1=="Heartland Family Service - Glenwood"|Var1=="Heartland Family Service - Family Works Nebraska"|Var1=="Heartland Family Service - Central")

# This show the frequency of each job title resource utilization at HFS facilities
ggplot(facilityjobHFS, aes(x=reorder(Var2,+Freq), y=Freq))+geom_col(position ="dodge", fill="steelblue")+theme(axis.text.x=element_text(angle=45,hjust=1))+facet_wrap(reorder(facilityjobHFS$Var1, -facilityjobHFS$Freq), labeller = labeller(label_wrap_gen(width=10)))+ggtitle("Job Type by Frequency of Use at HFS Facilities")+xlab("Job Type")+ylab("Frequency of Use")+geom_text(aes(label=Freq), vjust=-0.3, color="black", size=3.5)
```
**_the frequency of cases by job type for HFS facilities. Gendler, Central, Child and Family, and Sarpy are the most used facilitie._**
<p  align="middle">
  <img src="https://github.com/121107/Data/blob/master/Images/48.PNG" width="700", height="500" />
</p>

```{r}
#filtering for records which have the only the school facilities
facilityjobSchool<-facilityjob %>% filter(Var1=="Abraham Lincoln High School"|Var1=="Kanesville Alternative Learning Center"|Var1=="Kreft Primary School"|Var1=="Lewis Central Middle School"|Var1=="Thomas Jefferson High School"|Var1=="Wilson Middle School"|Var1=="Titan Hill Intermediate School"|Var1=="Lewis Central High School"|Var1=="Kirn Junior High  School")

# This show the frequency of each job title resource utilization at school facilities
ggplot(facilityjobSchool, aes(x=reorder(Var2,+Freq), y=Freq))+geom_col(position ="dodge", fill="steelblue")+theme(axis.text.x=element_text(angle=45,hjust=1))+facet_wrap(reorder(facilityjobSchool$Var1, -facilityjobSchool$Freq), labeller = labeller(label_wrap_gen(width=10)))+ggtitle("Job Type Frequency of Use at Schools")+xlab("Job Type")+ylab("Frequency of Use")+geom_text(aes(label=Freq), vjust=-0.3, color="black", size=3.5)
```

**_the frequency of cases by job type for Schools. Almost all the schools are in Council Bluffs or Lewis Central School Districts_**
<p  align="middle">
  <img src="https://github.com/121107/Data/blob/master/Images/49.PNG" width="700", height="500" />
</p>

```{r}
#filtering for records which have the only the other facilities  (not HFS or school)
facilityjobOther<-facilityjob %>% filter(Var1=="Center Mall Office"| Var1=="North Omaha Intergenerational Campus (Service)"| Var1=="Omaha (Spring) Reporting Center"| Var1=="Sanctuary House"| Var1=="Omaha (Blondo) Reporting Center"| Var1=="Micah House"|Var1=="Bellevue Reporting Center")

# This show the frequency of each job title resource utilization at other facilities
ggplot(facilityjobOther, aes(x=reorder(Var2,+Freq), y=Freq))+geom_col(position ="dodge", fill="steelblue")+theme(axis.text.x=element_text(angle=45,hjust=1))+facet_wrap(reorder(facilityjobOther$Var1, -facilityjobOther$Freq), labeller = labeller(label_wrap_gen(width=10)))+ggtitle("Job Type Frequency of Use at Other Facilities")+xlab("Job Type")+ylab("Frequency of Use")+geom_text(aes(label=Freq), vjust=-0.3, color="black", size=3.5)
```

**_the frequency of cases by job type for Other facilities. Most of them are reporting centers. Just like the schools this only has Therapists and Other people._**
<p  align="middle">
  <img src="https://github.com/121107/Data/blob/master/Images/50.PNG" width="700", height="500" />
</p>

```{r}
#Filtering the staff records for which the facility is any school facility
facilitystaffSchool<-facilitystaff %>% filter(Var1=="Abraham Lincoln High School"|Var1=="Kanesville Alternative Learning Center"|Var1=="Kreft Primary School"|Var1=="Lewis Central Middle School"|Var1=="Thomas Jefferson High School"|Var1=="Wilson Middle School"|Var1=="Titan Hill Intermediate School"|Var1=="Lewis Central High School"|Var1=="Kirn Junior High  School")

#This shows the frequency of utilization of each staff member at school facilities
ggplot(facilitystaffSchool, aes(x=reorder(Var1,+Freq), y=Freq,fill=Var4))+geom_col(position ="dodge")+theme(axis.text.x=element_text(angle=45,hjust=1))+facet_wrap(reorder(facilitystaffSchool$Var2, -facilitystaffSchool$Freq), labeller = labeller(label_wrap_gen(width=10)))+ggtitle("Job Type Frequency of Use at Schools")+xlab("Job Type")+ylab("Frequency of Use")+geom_text(aes(label=Freq), vjust=-0.3, color="black", size=3.5)
```

**_the frequency each therapist works at each school. From this we can see a common theme that most work at many different schools instead of specifically in one school or one district._**
<p  align="middle">
  <img src="https://github.com/121107/Data/blob/master/Images/51.PNG" width="700", height="500" />
</p>

```{r}
#Filtering the staff records for which the facility is any other facilities (not school or HFS)
facilitystaffOther<-facilitystaff %>% filter(Var1=="Center Mall Office"| Var1=="North Omaha Intergenerational Campus (Service)"| Var1=="Omaha (Spring) Reporting Center"| Var1=="Omaha (Blondo) Reporting Center"| Var1=="Micah House")

#This shows the frequency of utilization of each staff member at other facilities
facilitystaffOther<-facilitystaffOther %>% filter(Freq>=100)
ggplot(facilitystaffOther, aes(x=reorder(Var2,+Freq), y=Freq, fill=Var4))+geom_col(position ="dodge")+theme(axis.text.x=element_text(angle=45,hjust=1))+facet_wrap(facilitystaffOther$Var1, labeller = labeller(label_wrap_gen(width=10)))+ggtitle("Top 5 Other Facilities Staff Frequency of Interaction with Clients greater than 100")+xlab("Job Type")+ylab("Frequency of Use")+coord_flip()
```

**_the staff that have over 100 instances of meeting with clients_**
<p  align="middle">
  <img src="https://github.com/121107/Data/blob/master/Images/52.PNG" width="700", height="500" />
</p>

# Final Analysis for Objectives in Reserach Question 1
-How many people are enrolled in each program? And how much do they use each program?

There are currently 587 people served. 8 clients were enrolled in a gambling program, 88 clients were enrolled for a substance use program, and 482 clients were enrolled in a mental health program. There are 5 people enrolled in substance use programs and gambling programs. There are 83 people enrolled in substance use programs and mental health programs.

-How many staff members work in each program and specific facilities?

Many staff members work at various programs and facilities. We noted that a few work in many programs. The staff members working at schools tend to work at many schools and only practice mental health programs at those schools and none of them were specialists. The staff members at other facilities are therapists and other employees. The other employees were the only ones working at the sanctuary house.

-How many job titles work in each program and specific facilities?

There are many therapists in each program. There are specialists only at HFS facilities. The facilities showed a range of high use to low use. Future inquires and analysis should look into the high use and low use of facilities and cost object numbers.

-How many staff members work in multiple facilities and programs?

There are many staff working at many different schools. The graphs for the other facilities and programs were difficult to read and many staff overlapped. Future analysis should shows exactly which programs and facilities the employees work at.

# R Scripts for Research Question 2
Research Question 2: Based on the program, what demographics are currently being served?

We will look for the relationship between Program Name -> Gender Identity sorted by unique record ID Program Name -> Age sorted by unique record ID Program Name -> Race sorted by unique record ID

Our objective is to understand - What are the demographics of the most served demographics? - What are the demographics of the least served demographics?

```{r}
# Program Name -> Gender Identity sorted by unique record ID
HFS$gender_identity[HFS$gender_identity=="Female"] <- "Woman"
HFS$gender_identity[HFS$gender_identity=="Not Obtained"] <- "Queer or Not Obtained"
HFS$gender_identity[HFS$gender_identity=="Client Declined to Give"] <- "Queer or Not Obtained"
HFS$gender_identity[HFS$gender_identity=="Two-Spirit"] <- "Queer or Not Obtained"
HFS$gender_identity[HFS$gender_identity=="Non-Binary"] <- "Queer or Not Obtained"
HFS$gender_identity[HFS$gender_identity=="Other"] <- "Queer or Not Obtained"

#creating a data set with records of unique recordID, gender_identity and program_name
Program_Gender_uID21 <- unique(HFS[ , c('recordID', 'gender_identity', 'program_name')])

#Creating a data frame for gender_identity column from the above created unique data set
df12 <- as.data.frame(table(Program_Gender_uID21$gender_identity))

# This needs to be redone to show gender identity and program name
ggplot(df12, aes(x=reorder(Var1, +Freq), y=Freq)) +
  ggtitle("Number of times a particular gender was served")+
  xlab("Gender") +
  ylab("Number of Records")+
  geom_bar(stat="identity", fill="steelblue")+
  geom_text(aes(label=Freq), vjust=-0.3, color="black", size=3.5)+
  theme_minimal()+theme(axis.text.x=element_text(angle=45,hjust=1))
```
**_the gender identity of the clients. Women make up half of the population. Men and Queer or Not Obtained make up the other half_**
<p  align="middle">
  <img src="https://github.com/121107/Data/blob/master/Images/53.PNG" width="700", height="300" />
</p>

```{r}
#converting the Var1 of the data frame to numeric value
df131$Var1<-as.numeric(df131$Var1)

#This shows the Frequency of Program Use by Age
ggplot(df131, aes(x=Var1,y=Freq, color=Var2))+geom_point()+ggtitle("Frequency of Program Use by Age")+xlab("Age")+ylab("Frequency of Use")+scale_x_continuous()+geom_line(aes(colour=Var2)) + geom_smooth(aes(group=Var2))
```

**_the age diversity in each program: This graphs show a peak for those under 20 in Mental Health. There is a slow in crease starting around 10 years old for the substance use program. Similarly we see the second bump in mental health corresponding to the peak in substance use._**
<p  align="middle">
  <img src="https://github.com/121107/Data/blob/master/Images/54.PNG" width="700", height="300" />
</p>

```{r}
# removing the records which have the uncategorised simple_race code.
HFS2<-subset(HFS,recordID!=19 & recordID!=111 &recordID!=135 &recordID!=191 &recordID!=219 &recordID!=226 &recordID!=227 &recordID!=394 &recordID!=407 &recordID!=421 &recordID!=463)

#Categorising the records with gender_identity as "Woman" to "Female"
HFS2$gender_identity[HFS2$gender_identity=="Woman"] <- "Female"

#Categorising the records with gender_identity as "Not Obtained" to "NA"
HFS2$gender_identity[HFS2$gender_identity=="Not Obtained"] <- "NA"

#Categorising the records with null value in gender_identity column to "NA"
HFS2$gender_identity[is.na(HFS2$gender_identity)]<-"NA"


HFS2$simple_race[HFS2$simple_race==1] <- "Caucasian"
HFS2$simple_race[HFS2$simple_race==2] <- "Alaskan Native"
HFS2$simple_race[HFS2$simple_race==4] <- "Native American"
HFS2$simple_race[HFS2$simple_race==8] <- "Asian"
HFS2$simple_race[HFS2$simple_race==16] <- "Black"
HFS2$simple_race[HFS2$simple_race==32] <- "Hawaiian Native"
HFS2$simple_race[HFS2$simple_race==64] <- "Two or More"
HFS2$simple_race[HFS2$simple_race==128] <- "Other"
HFS2$simple_race[HFS2$simple_race==0] <- "Unknown"

# Program Name -> Race sorted by unique record ID
Program_Race_uID23 <- unique(HFS2[, c('recordID', 'simple_race', 'program_name')])

# These should be redone to show simple race and program name
#creating data frame with just the simple_race column
df14 <- as.data.frame(table(Program_Race_uID23$simple_race))

#creating data frame with just the program_name column
df15 <- as.data.frame(table(Program_Race_uID23$program_name))

#This shows the number of times a particular race was served
ggplot(df14, aes(x=reorder(Var1,+Freq), y=Freq)) +
  ggtitle("Number of times a particular race was served")+
  xlab("Race") +
  ylab("Number of Records")+
  geom_bar(stat="identity", fill="steelblue")+
  geom_text(aes(label=Freq), vjust=-0.3, color="black", size=3.5)+
  theme_minimal()+theme(axis.text.x=element_text(angle=45,hjust=1))
```

**_the initial view of the race of the clients. A majority are caucasian_**
<p  align="middle">
  <img src="https://github.com/121107/Data/blob/master/Images/55.PNG" width="700", height="300" />
</p>

```{r}
HFS3<-Program_Race_uID23

#Categorising the records with simple_race as "Caucasian" to "White"
HFS3$simple_race[HFS3$simple_race=="Caucasian"] <- "White"

#Categorising the records with simple_race as "Alaskan Native" to "Non-White"
HFS3$simple_race[HFS3$simple_race=="Alaskan Native"] <- "Non-White"

#Categorising the records with simple_race as "Native American" to "Non-White"
HFS3$simple_race[HFS3$simple_race=="Native American"] <- "Non-White"

#Categorising the records with simple_race as "Asian" to "Non-White"
HFS3$simple_race[HFS3$simple_race=="Asian"] <- "Non-White"

#Categorising the records with simple_race as "Black" to "Non-White"
HFS3$simple_race[HFS3$simple_race=="Black"] <- "Non-White"

#Categorising the records with simple_race as "Hawaiian Native" to "Non-White"
HFS3$simple_race[HFS3$simple_race=="Hawaiian Native"] <- "Non-White"

#Categorising the records with simple_race as "Two or More" to "Non-White"
HFS3$simple_race[HFS3$simple_race=="Two or More"] <- "Non-White"

#Categorising the records with simple_race as "Other" to "Non-White"
HFS3$simple_race[HFS3$simple_race=="Other"] <- "Non-White"

#Categorising the records with simple_race as "Unknown" to "Non-White"
HFS3$simple_race[HFS3$simple_race=="Unknown"] <- "Non-White"

#creating a data frame with simple_race and program_name columns from the HFS3 data set
HFS3race<-as.data.frame(table(HFS3$simple_race,HFS3$program_name))

#This shows the number of people belonging to a particular race served in the programs
ggplot(HFS3race, aes(x=Var1,fill=Var2))+geom_bar(aes(y=Freq), stat="identity",position = "dodge")+xlab("Race")+ylab("Number of people")
```

**_This is the second graph of the race with non-white people being grouped together_**
<p  align="middle">
  <img src="https://github.com/121107/Data/blob/master/Images/56.PNG" width="700", height="300" />
</p>

# R Scripts for Research Question 3

Research Question 3: Using american community survey data, are the percent of demographics of both the population served in the 680 and 681 area codes (non-telehealth and telehealth specified )  and the percent of the demographics in Douglas county with access to internet fairly similar to each other?

This is exploratory. We will look at the percents of each demographics and compare them to each other. Our objective is to try to understand if access to internet was a deterrent to those who chose to receive care via telehealth.

**_Most of the analysis (comparison with ACS dataset) of this research question has been done on data cleaning section (refer to that parts of the projects in addition analysis of here)_**

```{r}
#Renaming the data in HFS for which the general_location values are "Telehealth - Phone" or "Telehealth - Video" with the new value "Telehealth"
HFS$general_location[HFS$general_location=="Telehealth - Phone" | HFS$general_location=="Telehealth - Video"] <- "Telehealth"

#Renaming the data in HFS for which the general_location value is not "Telehealth" with "Not Telehealth"
HFS$general_location[HFS$general_location!="Telehealth"] <- "Not Telehealth"

#creating a data frame with just "general_location" column from the HFS data set
df16 <- as.data.frame(table(HFS$general_location))

#This shows the number of times telehealth and non-telehealth was the general location
ggplot(df16, aes(x=Var1, y=Freq)) +
  ggtitle("Number of times telehealth and non-telehealth")+
  xlab("General Location") +
  ylab("Number of Records")+
  geom_bar(stat="identity", fill="steelblue")+
  geom_text(aes(label=Freq), vjust=-0.3, color="black", size=3.5)+
  theme_minimal()
```

**_the frequency of telehealth and non telehealth_**
<p  align="middle">
  <img src="https://github.com/121107/Data/blob/master/Images/57.PNG" width="700", height="300" />
</p>

Our objective was to try to understand if access to internet was a deterrent to those who chose to receive care via telehealth. We predicted with the ACS data that people who are black and older would have participated in telehealth less. However our data shows that half of the patients used telehealth and the other half did not. The demographics did not seem to be a factor. We should look into other aspects such as facilities or events.

# R Scripts for Research Question 4

Research Question 4: What care comes from which facilities based on job title, Sc code, zip, and state?

We will look for the relationship between
Job Title -> SC code
Job Title -> Zip
Job Title -> State
Job Title filtered by Event Name -> SC code
Job Title filtered by Event Name -> Zip
Job Title filtered by Event Name -> State
Facility -> Program Name
Facility -> Unique Record Id
Facility -> Staffing
Facility -> Event Name

Our objective is to understand
- Do the sc codes fund specific jobs?
- What jobs are serving which areas?
- Which facilities are currently offering which programs? (This will be expanded on by research on history of HFS and facilitys.)
- Which facilities are not used as much?
- How many staff members does each facility have?
- Which events are offered at specific facilities?

```{r}
# Job Title -> SC code
#getting a subset of the NEIA data set with just the job_title, sc_code, zip and state columns
Job_SC_Zip_State41 <- subset(NEIA[, c('job_title','sc_code', 'zip', 'state')])

#Creating a data frame with only the job_title column from the Job_SC_Zip_State41 data set
df18 <- as.data.frame(table(Job_SC_Zip_State41$job_title))

#Creating a data frame with only the sc_code column from the Job_SC_Zip_State41 data set
df19 <- as.data.frame(table(Job_SC_Zip_State41$sc_code))

#Creating a data frame with only the zip column from the Job_SC_Zip_State41 data set
df20 <- as.data.frame(table(Job_SC_Zip_State41$zip))

#Creating a data frame with only the state column from the Job_SC_Zip_State41 data set
df21 <- as.data.frame(table(Job_SC_Zip_State41$state))
```

```{r}
#Calculating the sum of all the frequencies in the df19 data frame
total<-sum(df19$Freq)

#This shows the usage of each Cost Center in-terms of percentage
ggplot(df19, aes(x=reorder(Var1, Freq), y=(Freq)/total)) +
  ggtitle("Percent of each Cost Center Use")+
  xlab("SC Code") +
  ylab("Percent of Use")+
  geom_bar(stat="identity", fill="steelblue")+
  geom_text(aes(label=round(Freq/total,2)), vjust=-1, color="black", size=3.5)+theme_minimal()+theme(axis.text.x=element_text(angle=45,hjust=1))
```

**_the percent of use that half of the cost centers that are being utilized much less utilized. In future analysis the cost centers should be looked into to find where the funding is coming from and how to build up funding in certain places_**
<p  align="middle">
  <img src="https://github.com/121107/Data/blob/master/Images/58.PNG" width="700", height="300" />
</p>

```{r}
# There are 5 types of therapists. Case Coordinator,EHR specialist,office manager 2 do not have sc_codes related to pay.  Billing Specialist and OFFICE AND SYSTEMS MANAGE only have 1 entry too. We should write a paragraph about this and run this without those ones.
table2<-as.data.frame(table2)
ggplot(table2, aes(x=reorder(Var2,+Freq), y=Freq))+geom_bar(stat="identity", fill="steelblue")+theme(axis.text.x=element_text(angle=45,hjust=1))+ggtitle("Frequency of Use of Cost center compared with Job Titles")+xlab("Cost Centers")+ylab("Frequency of Use")+facet_grid(table2$Var1)+geom_text(aes(label=Freq), vjust=-1, color="black", size=3.5)
```

**_the cost centers compared by the job titles. The cost center 1314-64 is not used by any of these. We can conclude that job titles are not necessarily funded by specific cost centers. Upon further analysis we found 1314-64 is mainly used for Homeless Housing and Sanctuary Housing. Future analysis should focus on other aspects for example which facilities or other aspects that funding might focus on._**
<p  align="middle">
  <img src="https://github.com/121107/Data/blob/master/Images/59.PNG" width="700", height="300" />
</p>

```{r}
# Job Title filtered by Event Name -> Zip
#Creating a data frame with the zip column from the filterJob_SC_Zip_State42 data set
zip42<-as.data.frame(table(filterJob_SC_Zip_State42$zip, filterJob_SC_Zip_State42$job_title))

#This shows the Zip Codes filtered by Specific Events use by Frequency
ggplot(zip42, aes(x=reorder(Var1,+Freq), y=Freq, fill=Var2))+geom_bar(stat="identity", position = "dodge")+theme(axis.text.x=element_text(angle=45,hjust=1))+ggtitle("Zip Codes filtered by Specific Events use by Frequency")+xlab("Zip Codes filtered by Specific Events")+ylab("Frequency")
```

**_the frequency of clients by zip code. We can see that just as before there are many from 680, 681, and 0 zip codes. Whereas there are fewer from others_**
<p  align="middle">
  <img src="https://github.com/121107/Data/blob/master/Images/60.PNG" width="700", height="300" />
</p>

```{r}
# Facility -> Program Name
#Filtering the records which have HFS centers as facilities
facilityHFS<-Facility_Program_Staff_Event43J %>% filter(facility=="Heartland Family Service - Child and Family Center"|facility=="Heartland Family Service - Gendler"|facility=="Heartland Family Service - Heartland Homes"|facility=="Heartland Family Service - Logan"|facility=="Heartland Family Service - Sarpy"|facility=="Heartland Family Service - Lakin"|facility=="Heartland Family Service - Glenwood"|facility=="Heartland Family Service - Family Works Nebraska"|facility=="Heartland Family Service - Central")

#creating a data frame with just the program_name column from the facilityHFS data set
facilityHFSProgram<-as.data.frame(table(facilityHFS$program_name))

#This show the number of times each Program is Utilized in HFS Facilities
ggplot(facilityHFSProgram, aes(x=reorder(Var1,+Freq), y=Freq))+geom_bar( stat="identity", fill="steelblue")+ggtitle("Amount each Program is Utilized in HFS Facilities")+xlab("Program's offered at HFS Facilities")+ylab("Utilization of Programs")+geom_text(aes(label=Freq), vjust=-1, color="black", size=3.5)
```
```{r}
# Facility -> Unique Record Id
#creating data frame with just facility column from the Facility_uID44 data set
ID<-as.data.frame(table(Facility_uID44$facility))

#This shows the number of times a facility is utilized
ID<-ID %>% top_n(10,Freq)
ggplot(ID, aes(x=reorder(Var1, +Freq), y=Freq))+geom_bar(stat="identity", fill="steelblue")+theme(axis.text.x=element_text(angle=45,hjust=1))+ggtitle("Top 10 facility Patients Use")+xlab("Facility name")+ylab("Frequency of Patients")+geom_text(aes(label=Freq), vjust=-1, color="black", size=3.5)
```
```{r}
# Facility -> Staffing
#Filtering the records which have HFS centers as facilities
Facility_Program_Staff_Event43JA<- subset(NEIA[, c('facility','program_name', 'staff_name', 'event_name', 'job_title')])
facilityHFS<-Facility_Program_Staff_Event43JA %>% filter(facility=="Heartland Family Service - Child and Family Center"|facility=="Heartland Family Service - Gendler"|facility=="Heartland Family Service - Heartland Homes"|facility=="Heartland Family Service - Logan"|facility=="Heartland Family Service - Sarpy"|facility=="Heartland Family Service - Lakin"|facility=="Heartland Family Service - Glenwood"|facility=="Heartland Family Service - Family Works Nebraska"|facility=="Heartland Family Service - Central")

#Creating a data frame with just staff_name from the facilityHFS data set
facilityHFSProgram<-as.data.frame(table(facilityHFS$staff_name, facilityHFS$job_title))
facilityHFSProgram<-facilityHFSProgram %>% filter(Freq!=0)
#Getting the top 10 records
topfacilityHFSProgram<-facilityHFSProgram %>% top_n(10, Freq)
# #This shows the Top 10 Utilized Staff in HFS Facilities
ggplot(topfacilityHFSProgram, aes(x=reorder(Var1,+Freq), y=Freq, fill=Var2))+geom_bar(stat="identity")+ggtitle("Top 10 Utilized Staff in HFS Facilities")+xlab("Top 10 Utilized Staff in HFS Facilities")+ylab("Amount of Utilization")+theme(axis.text.x=element_text(angle=45,hjust=1))+geom_text(aes(label=Freq), vjust=-1, color="black", size=3.5)
```
```{r}
#Filtering the records which have schools as facilities

facilitystaffSchool<-Facility_Program_Staff_Event43JA%>% filter(facility=="Abraham Lincoln High School"|facility=="Kanesville Alternative Learning Center"|facility=="Kreft Primary School"|facility=="Lewis Central Middle School"|facility=="Thomas Jefferson High School"|facility=="Wilson Middle School"|facility=="Titan Hill Intermediate School"|facility=="Lewis Central High School"|facility=="Kirn Junior High  School")

#Creating a data frame with just staff_name from the facilitystaffSchool data set
facilitySchoolProgram<-as.data.frame(table(facilitystaffSchool$staff_name, facilitystaffSchool$job_title))
facilitySchoolProgram<-facilitySchoolProgram %>% filter(Freq!=0)
#Getting the top 10 records
topfacilitySchool<-facilitySchoolProgram %>% top_n(10, Freq)

#This shows the Top 10 Utilized Staff in School Facilities
ggplot(topfacilitySchool, aes(x=reorder(Var1,+Freq), y=Freq, fill=Var2))+geom_bar( stat="identity")+ggtitle("Top 10 Utilized Staff in School Facilities")+xlab("Top 10 Staff in School Facilities")+ylab("Frequency of Utilization")+theme(axis.text.x=element_text(angle=45,hjust=1))+geom_text(aes(label=Freq), vjust=-1, color="black", size=3.5)
```
```{r}
#Filtering the records which have facilities other than schools and HFS centers
facilityOtherProgram<-Facility_Program_Staff_Event43JA %>% filter(facility=="Center Mall Office"| facility=="North Omaha Intergenerational Campus (Service)"| facility=="Omaha (Spring) Reporting Center"| facility=="Sanctuary House"| facility=="Omaha (Blondo) Reporting Center"| facility=="Micah House"|facility=="Bellevue Reporting Center")

#Creating a data frame with just staff_name from the facilityOtherProgram data set
facilityOtherProgram<-as.data.frame(table(facilityOtherProgram$staff_name, facilityOtherProgram$job_title))

#Getting the top 10 records
topfacilityOther<-facilityOtherProgram %>% filter(Freq!=0)%>% top_n(10,Freq)

#This shows the top 10 Utilized Staff in Facilities other than schools and HFS centers
ggplot(topfacilityOther, aes(x=reorder(Var1,+Freq), y=Freq, fill=Var2))+ geom_bar(stat="identity")+ggtitle("Top 5 Utilized Staff in Other Facilities")+xlab("Top 10 Staff in Other Facilities")+ylab("Frequency of Utilization")+theme(axis.text.x=element_text(angle=45,hjust=1))+geom_text(aes(label=Freq), vjust=-1, color="black", size=3.5)
```
```{r}
# Facility -> Event Name
#creating a data frame with just event_name column from the facilityHFS data set
facilityHFSEvent<-as.data.frame(table(facilityHFS$event_name, facilityHFS$job_title))

#Getting the top 10 records
topA<-facilityHFSEvent %>% top_n(10,Freq)

#This shows the frequency of Top 10 Events offered by HFS facilities
ggplot(topA, aes(x=reorder(Var1,+Freq), y=Freq, fill=Var2))+geom_bar(stat="identity", position = "dodge", width = 0.5)+ggtitle("Frequency of Top 10 Events offered by HFS facilities")+xlab("Top 10 Events offered by HFS facilities")+ylab("Frequency")+theme(axis.text.x=element_text(angle=45,hjust=1))
```

## **_Top 10 (or 5) events and staff offerd by different facilities and programs_**

<table>
  <tr>
    <td> the number of programs offered at HFS facilities </td>
     <td>the top 10 facilities and the amount of patients that utilized care from those facilities. As we can see most are HFS facilities. Only one of the top ten are schools.</td>
  </tr>
  <tr>
    <td><img src="https://github.com/121107/Data/blob/master/Images/61.PNG" width=700 height=300></td>
    <td><img src="https://github.com/121107/Data/blob/master/Images/62.PNG" width=700 height=300></td>
  </tr>
  <tr>
    <td> the top ten utilized staff at HFS facilities. Since these were not separated by job title this shows all types of job titles. However, it looks as though the most utilized staff are other employees.</td>
     <td> the top ten staff at schools. Although there were very few other employees, there are still some in the top 10.</td>
  </tr>
  <tr>
    <td><img src="https://github.com/121107/Data/blob/master/Images/63.PNG" width=700 height=300></td>
    <td><img src="https://github.com/121107/Data/blob/master/Images/64.PNG" width=700 height=300></td>
  </tr>
  <tr>
    <td> 10 utilized staff at other facilities are mostly therapists.</td>
     <td>the top ten events offered by HFS facilities are mostly offered by therapists. The other employees who worked on individual therapy and collateral notes are by supervisors which also might be practicing social work.</td>
  </tr>
  <tr>
    <td><img src="https://github.com/121107/Data/blob/master/Images/65.PNG" width=700 height=300></td>
    <td><img src="https://github.com/121107/Data/blob/master/Images/66.PNG" width=700 height=300></td>
  </tr>
 </table>

# Final analysis of objectives in research question 4
 Our objective was to understand
- Do the sc codes fund specific jobs?

No, they do not fund specific jobs.

- What jobs are serving which areas?

This question was a little unfocused. The jobs are not serving specific areas, but the jobs serving clients from specific areas. Most people who are therapists are serving the majority of patients in each zip code. The 685 zip code had a majority of the other employees helping patients in those areas

- Which facilities are currently offering which programs?

HFS Gendler is the only one that offers all the programs. Schools only offer mental health programs. The Center Mall Office, HFS-Central, HFS-Child and Family Center, HFS Family Works Nebraska, HFS-Glenwood, HFS-Logan, HFS-Sarpy, and Omaha (Blondo) Reporting Center offer two programs. Besides the schools, Sanctuary House, Omaha (Spring) Reporting Center, North Omaha Intergenerational Campus (Service), Micah House, HFS-Lakin, HFS-Heartland Homes, Center Mall Office, and Bellevue Reporting Center only offer mental health programs.

- Which facilities are not used as much?

The schools have less instances of use. Out of the schools the facility utilized the least is Kanesville Alternative Learning Center. Out of the HFS facilities the lowest utilized facility was HFS - Heartland Home and HFS - Lakin. Heartland Home is a homeless transitional housing. Out of the other facilities the sanctuary house is the least utilized.

- How many staff members does each facility have?

We found that the number of staff at each facility seems to be extremes. It is either a high number or a low number. Some were low for a reason, such as the sanctuary houses or homeless housing. It would be more interesting to see the staff numbers for each facility with a third variable of cost centers.

- Which events are offered at specific facilities?

This question was skipped because there was too much data for events that was not specifically cleaned.

# Clustering
Clustering is the use of unsupervised technique for grouping similar objects, finding dissimilarities between groups. Clustering analysis had done in this analysis. One of the major problem is to do clustering by multiple categorical values. In this experiment (to analyze a research question), clustering represents into 2D space in stead of multi dimensional space. The clustering analysis was showed by the dissimilarities and similliraties in numerical value by using gower metric. The elbow method was used to know how many clusters do we need. t_SNE was used to avoid the using of more computation.

Several clustering analysis was analyzed, among them: clustering between, 1. program_name, facility and sc_code 2. age, gender_identity, simple_race 3. general_location, program_name, sc_code

clustering for general_location, program_name and sc_code. This cluster was showed a visualization how many observations were similar based on general_location, program_name and sc_code. Here, we showed only a clustering.

```{r}
myVars1 <- c("general_location", "program_name", "sc_code")
HFS3c <- HFS
newHFS3 <- HFS3c[myVars1]

library(cluster)
gower_df3 <- cluster::daisy(newHFS3[, 1:3], metric = "gower",
                            type = list(ordratio = 1:3))

summary(gower_df3)

silhouette <- c()
silhouette = c(silhouette, NA)
for(i in 2:10){
  pam_clusters = pam(as.matrix(gower_df3),
                     diss = TRUE,
                     k = i)
  silhouette = c(silhouette ,pam_clusters$silinfo$avg.width)
}
plot(1:10, silhouette,
     xlab = "Clusters",
     ylab = "Silhouette Width")
lines(1:10, silhouette)

pam_model3 = pam(gower_df3, diss = TRUE, k = 4)
newHFS3[pam_model3$medoids, ]

library(dplyr)
pam_summary3 <- newHFS3 %>%
  mutate(cluster = pam_model3$clustering) %>%
  group_by(cluster) %>%
  do(cluster_summary = summary(.))
pam_summary3$cluster_summary[[2]]

library(Rtsne)
library(ggplot2)
tsne_object3 <- Rtsne(gower_df3, is_distance = TRUE)
tsne_df3 <- tsne_object3$Y %>%
  data.frame() %>%
  setNames(c("X", "Y")) %>%
  mutate(cluster = factor(pam_model3$clustering))
ggplot(aes(x = X, y = Y), data = tsne_df3) +
  geom_point(aes(color = cluster))+
  stat_ellipse(aes(x=X, y=Y,color=cluster),type = "norm") +
  theme(legend.position='none')
```

**_Clustering general_location, program_name and sc_code_**
<p  align="middle">
  <img src="https://github.com/121107/Data/blob/master/Images/67.PNG" width="500", height="300" />
</p>

Among all of these, we did ANOVA analysis. However, the results was not satisfactory. Hence, we eliminate the analysis in here. In addition, we did more analysis more than the visualization analysis presented above. However, we choose the most significant results among all visualization analysis.

## Contributors for the project (name alphabetically ordered, everyone contributed equally)
##### Abu Bakar Siddiqur Rahman, Lisa Kiemde, Shravya Chandiri
##### Do not hesitate to contact us if you have any questions
##### (abubakarsiddiqurra@unomaha.edu, lgmorton@unomaha.edu, schandiri@unomaha.edu)

## Acknowledgement
###### We group members 5 shows our highly gratitute to Dr. Andrea Grover to teach us all steps in data analysis (make decisions from data including R code). We also shows our highly gratitute to Heartland Family Service (HFS) for providing the dataset for education purposes.
