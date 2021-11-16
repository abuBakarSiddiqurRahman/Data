# Worst Plots

### Bar Plot
This plot was tried to show which staff involve with which facility.
The plot does not provide any exact information by looking it once as visualization.
The x and y plot does not make any sense what information the plot provides.

```R
##### initial adjustment in R ######

setwd(dirname(rstudioapi::getActiveDocumentContext()$path))

library(ggplot2)

HFS <- read.csv("HFS.csv")
data("mpg")


##### Bar Plot ###########

ggplot(data = HFS, mapping = aes(x = facility, y = staff_name))+
  geom_col(aes(fill=staff_name))
```


**_Bar plot_**
![Bar plot](https://github.com/121107/Data/blob/master/Images/8.PNG)


### Mosaic Plot
This plot tried to show how the use of number of cylinder in cars was changed by changes of year.
The plot was failed to provide such information with mosaic plot.

```R
#### Mosaic Plot  #####

mosaicplot(mpg,xlab="year", ylab="cyl", col="yellow")
```

  **_Mosaic Plot_**
  ![Mosaic Plot](https://github.com/121107/Data/blob/master/Images/9.PNG)
