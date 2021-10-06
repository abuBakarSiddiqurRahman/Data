## Data Exploration

# Scatter Plot with two variables
This plot will help to understand by getting the average age
for each program. The data visualization provide a quick view
that which age group prefer which program.

> library(ggplot2)
df <- group_by(dat, program_name)
df2 <- summarise(df, ageMean = mean(age))
ggplot(data = df2, mapping = aes(x = program_name, y = ageMean)) +
  geom_point()

**_Scatter plot with two variables_**
![Scatter plot with two variables](https://github.com/121107/Data/blob/master/Images/1.PNG)


> dat <- read.csv("HFS.csv") # entire data set
ggplot(data = dat, mapping = aes(x = program_name, y = age)) +
  geom_point()+
  labs(title= "Scatter Plot of 2 Variables with all values")

  **_Scatter plot with two variables with all values_**
  ![Scatter plot with two variables](https://github.com/121107/Data/blob/master/Images/2.PNG)
