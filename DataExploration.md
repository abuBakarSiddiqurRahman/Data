# Data Exploration

### Scatter Plot with two variables
This plot will help to understand by getting the average age
for each program. The data visualization provide a quick view
that which age group prefer which program.

```R
##### initial adjustment in R ######

setwd(dirname(rstudioapi::getActiveDocumentContext()$path))
dat <- read.csv("HFS.csv")

install.packages("dplyr")    # alternative installation of the %>%
library(dplyr)
install.packages("ggplot2")
library(ggplot2)

##### Scatter Plot with 2 Variables ###########

df <- group_by(dat, program_name)
df2 <- summarise(df, ageMean = mean(age))  

ggplot(data = df2, mapping = aes(x = program_name, y = ageMean)) +
  geom_point() +
  labs(title= "Scatter Plot of 2 Variables")
```


**_Scatter plot with two variables_**
![Scatter plot with two variables](https://github.com/121107/Data/blob/master/Images/1.PNG)


```
#### Scatter plot of 2 variables with all values #####

dat <- read.csv("HFS.csv") # entire data set
ggplot(data = dat, mapping = aes(x = program_name, y = age)) +
  geom_point()+
  labs(title= "Scatter Plot of 2 Variables with all values")
```

  **_Scatter plot with two variables with all values (two variables)_**
  ![Scatter plot with two variables](https://github.com/121107/Data/blob/master/Images/2.PNG)

### Scatter Plot of two variables with trend line
This plot shows a linear relationship between age and recordID

```
#### Scatter plot of 2 variables with trend line #####

ggplot(data = dat, mapping = aes(x = age, y = recordID)) +
  geom_point()+
  geom_smooth(method = 'lm', se= FALSE)+
  labs(title= "Scatter Plot of 2 Variables with trend line")
```

**_Scatter plot with two variables with all values with trend line_**
![Scatter plot with two variables with trend line](https://github.com/121107/Data/blob/master/Images/3.PNG)

### Scatter plot with three variables
This plot shows which facility has most of the recordID participated based on the gender. The plot indicates which facility has more male or female no strange outliers in the graph

```
#### Scatter plot of 3 variables #####

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
#### Faceted plot ##########

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
#### Bar plot #########

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
