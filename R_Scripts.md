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
