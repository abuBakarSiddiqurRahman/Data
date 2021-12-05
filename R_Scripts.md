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

![how many people are enrolled in each program](https://github.com/121107/Data/blob/master/Images/11.PNG)

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

<table>
  <tr>
    <td>First Screen Page</td>
     <td>Holiday Mention</td>
  </tr>
  <tr>
    <td><img src="https://github.com/121107/Data/blob/master/Images/14.PNG" width=700 height=300></td>
    <td><img src="https://github.com/121107/Data/blob/master/Images/15.PNG" width=700 height=300></td>
  </tr>
  <tr>
    <td><img src="https://github.com/121107/Data/blob/master/Images/16.PNG" width=700 height=300></td>
    <td><img src="https://github.com/121107/Data/blob/master/Images/17.PNG" width=700 height=300></td>
  </tr>
  <tr>
    <td><img src="https://github.com/121107/Data/blob/master/Images/18.PNG" width=700 height=300></td>
    <td><img src="https://github.com/121107/Data/blob/master/Images/19.PNG" width=700 height=300></td>
  </tr>
  <tr>
    <td><img src="https://github.com/121107/Data/blob/master/Images/20.PNG" width=700 height=300></td>
    <td><img src="https://github.com/121107/Data/blob/master/Images/21.PNG" width=700 height=300></td>
  </tr>
  <tr>
    <td><img src="https://github.com/121107/Data/blob/master/Images/22.PNG" width=700 height=300></td>
    <td><img src="https://github.com/121107/Data/blob/master/Images/23.PNG" width=700 height=300></td>
  </tr>
  <tr>
    <td><img src="https://github.com/121107/Data/blob/master/Images/24.PNG" width=700 height=300></td>
    <td><img src="https://github.com/121107/Data/blob/master/Images/25.PNG" width=700 height=300></td>
  </tr>
  <tr>
    <td><img src="https://github.com/121107/Data/blob/master/Images/26.PNG" width=700 height=300></td>
    <td><img src="https://github.com/121107/Data/blob/master/Images/27.PNG" width=700 height=300></td>
  </tr>
  <tr>
    <td><img src="https://github.com/121107/Data/blob/master/Images/28.PNG" width=700 height=300></td>
    <td><img src="https://github.com/121107/Data/blob/master/Images/29.PNG" width=700 height=300></td>
  </tr>
  <tr>
    <td><img src="https://github.com/121107/Data/blob/master/Images/30.PNG" width=700 height=300></td>
    <td><img src="https://github.com/121107/Data/blob/master/Images/31.PNG" width=700 height=300></td>
  </tr>
  <tr>
    <td><img src="https://github.com/121107/Data/blob/master/Images/32.PNG" width=700 height=300></td>
    <td><img src="https://github.com/121107/Data/blob/master/Images/33.PNG" width=700 height=300></td>
  </tr>
  <tr>
    <td><img src="https://github.com/121107/Data/blob/master/Images/34.PNG" width=700 height=300></td>
    <td><img src="https://github.com/121107/Data/blob/master/Images/35.PNG" width=700 height=300></td>
  </tr>
  <tr> 
    <td><img src="https://github.com/121107/Data/blob/master/Images/36.PNG" width=700 height=300></td>
    <td><img src="https://github.com/121107/Data/blob/master/Images/37.PNG" width=700 height=300></td>
  </tr>

 </table>
