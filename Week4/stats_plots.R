library(RSQLite)
setwd("C:/Users/Pudders/Desktop/DBClass")

## Connect to database
db = dbConnect(SQLite(), dbname="pittsburghData.db")
## Show header of employment table
dbListFields(db, "employment")  
## Create select statement
query <- dbSendQuery(db, "SELECT * FROM employment WHERE Construction > .05" )
## dbFetch(query,n), where n is number of rows to return (-1 = All rows, default is 500)
construction <- dbFetch(query, n = -1)
class(construction)
## Just good practice
dbClearResult(query

### Mean ###
mean(construction$Construction)
### Median ###
median(construction$ArtsRecreation)
### standard deviation ###
sd(construction$Construction)

### Quartile ###
quantile(construction$ArtsRecreation) 

###### Car #####
head(mtcars)
# https://stat.ethz.ch/R-manual/R-devel/library/datasets/html/mtcars.html

# Outliers #
boxplot(mpg~cyl,data=mtcars, main="Car Milage Data", xlab="Number of Cylinders", ylab="Miles Per Gallon")

### Scatterplot ###
attach(mtcars)
plot(wt, mpg, main="Scatterplot Example", xlab="Car Weight ", ylab="Miles Per Gallon ", pch=19)
abline(lm(mpg~wt), col="red") # regression line (y~x) 
cor(mtcars$mpg, mtcars$wt)

### Scatterplot Matrices ###
pairs(~mpg+disp+drat+wt,data=mtcars, main="Simple Scatterplot Matrix")

#########################################
### Ggplot ##############################
#########################################
# http://docs.ggplot2.org/current/

head(movies)

### Histogram ###
ggplot(movies, aes(x=rating))+ geom_histogram(aes(fill = ..count..))

### violin plot ###
ggplot(mtcars, aes(factor(cyl), mpg)) + geom_violin()
ggplot(movies, aes(factor(round(rating, digits = 0)), length)) + geom_violin()

