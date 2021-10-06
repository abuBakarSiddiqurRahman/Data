# Data Exploration

### Scatter Plot with two variables
This plot will help to understand by getting the average age
for each program. The data visualization provide a quick view
that which age group prefer which program.


**_Scatter plot with two variables_**
![Scatter plot with two variables](https://github.com/121107/Data/blob/master/Images/1.PNG)



  **_Scatter plot with two variables with all values (two variables)_**
  ![Scatter plot with two variables](https://github.com/121107/Data/blob/master/Images/2.PNG)

### Scatter Plot of two variables with trend line
This plot shows a linear relationship between age and recordID

**_Scatter plot with two variables with all values with trend line_**
![Scatter plot with two variables with trend line](https://github.com/121107/Data/blob/master/Images/3.PNG)

### Scatter plot with three variables
This plot shows which facility has most of the recordID participated based on the gender. The plot indicates which facility has more male or female no strange outliers in the graph

```
ggplot(data = dat, mapping = aes(facility, recordID, color = gender))+
  geom_point(size = 0.8, alpha = 0.5)+
  geom_smooth(method=lm, se=FALSE, col='red', size=2)+
  theme(axis.text.x = element_text(angle=50, size = 8, face = "bold",
                                   hjust=1, vjust = 1, lineheight = 5))+
  labs(title= "Scatter Plot of 3 Variables")
```

**_Scatter plot with three variables_**
![Scatter plot with three variables](https://github.com/121107/Data/blob/master/Images/4.PNG)


### Faceted plot   
This plot shows which staff works mostly with all ethnicity
(this will identify  communication skills) and which staff works with his/her normal work schedule or not

```
ggplot(data = dat, mapping = aes(x = staff_name, y = NormalWorkHours
                              )) +
  facet_wrap(~ ethnic_identity, nrow = 5)+
  theme(axis.text.x = element_text(angle=90, size = 8, face = "bold",
                                   hjust=1, vjust = 1, lineheight = 5))+
  geom_point(size = 0.8, alpha = 0.5)+
  geom_smooth(method = "lm", se = FALSE)+
  labs(title= "faceted plot")
```

**_Faceted plot_**
![Faceted plot](https://github.com/121107/Data/blob/master/Images/5.PNG)


### Bar plot
This plot shows the average hours worked by each job_title
this gives an idea for the organizer which job holders have more work in average

```
df5 <- dat %>% group_by(job_title) %>%
  summarize(AvgTotalDuration = mean(duration_num))

ggplot(data = df5, mapping = aes(x = job_title, y = AvgTotalDuration))+
  geom_col(aes(fill=job_title))+
  theme(axis.text.x = element_text(angle=90, size = 8, face = "bold",
                                   hjust=1, vjust = 1, lineheight = 5))+
labs(title= "bar plot")
```

**_Bar plot_**
![Bar plot](https://github.com/121107/Data/blob/master/Images/6.PNG)
