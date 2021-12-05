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
Summary: In this graph we can see how many people are enrolled in each program. This is done by finding unique record IDs for program names. Therefore, this might include people who are in more than 1 program.
 As we can see Mental Health is more utilized currently. There are very few people who are utilizing the Gambling programs. This may be due to the fact that the Gambling program is only offered in certain places, is less funded, or is a new program.
