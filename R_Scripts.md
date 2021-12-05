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
  <img src="https://github.com/121107/Data/blob/master/Images/13.PNG" width="700", height="300" />
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

![average number of visits for each program](https://github.com/121107/Data/blob/master/Images/12.PNG)


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

![the number of therapists, specialists, and other people working for each program](https://github.com/121107/Data/blob/master/Images/13.PNG)

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
