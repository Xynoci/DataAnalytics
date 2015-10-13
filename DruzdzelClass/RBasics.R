### mode vs. class ###
x = 1:9
dim(x) <- c(3,3)
mode(x) 
#[1] "numeric" 

class(x)
#[1] "matrix"

## concatenate - vector ##
x = c(1,2,14,29) 
newVector = c(1,2,4,19)
newVector[2]

## dictionary ##
newDictionary = c("1.29", "2.50", "priceless") 
names(newDictionary) = c("Banana", "Apple", "Kittens") 
newDictionary["Apple"] 

## mixing scaler and vector ##
someNumbers = 1:10 
# good #
someNumbers + 1 
# bad #
someNumbers + c(1,2,3)

## matrix ##
someMatrix = matrix(1:16,4,4) 
someMatrix[10] 
#[1] 10
someMatrix[2,3] 
#[1] 10
someMatrix = matrix(1:16, 4, 4, FALSE, dimnames=list(c("A","B","C","D"),c("W","X","Y","Z"))) 
someMatrix["B","Y"] 
#[1] 10

## read table ##
fromFile = read.table("BeerAndWinePerCapita.txt", header = TRUE, sep = ",")
head(fromFile)
#> head(fromFile)
#          State Gallons.of.Beer.per.Capita.per.Year Gallons.of.Wine.per.Capita.per.Year
#1        nEVADA                                  44                                5.75
#2 nEW hAMPSHIRE                                43.4                                6.26
#3  nORTH dAKOTA                                41.7                                1.56
#4       mONTANA                                41.5                                3.06
#5  sOUTH dAKOTA                                  39                                1.50
#6     wISCONSIN                                38.2                                2.63

### factors ###
## roman numerials ##
inputData = c(1,2,3,1,2,1,1,2,3,2,1,2,2,3) 
factorData = factor(inputData) 
nlevels(factorData)
factorData = factor(inputData, ordered=TRUE) 
factorData 
#[1] 1 2 3 1 2 1 1 2 3 2 1 2 2 3 
#Levels: 1 < 2 < 3
factorData = factor(inputData, ordered=TRUE, levels=c(1,2)) 
#[1] 1 2 <NA> 1 2 1 1 2 <NA> 2 1 2 2 <NA> 

factorData = factor(inputData,labels=c("I","II","III")) 
factorData 
#[1] I II III I II I I II III II I II II III 
#Levels: I II III

monthsOfTheYear = c("March","April","January","November","January","September","October","September","November","August","January","November","November","February","May","August","July","December","August","August","September","November","February","April") 
monthsFactors = factor(monthsOfTheYear) 
table(monthsFactors)
monthsFactors = factor(monthsOfTheYear,levels=c("January","February","March","April","May","June","July","August","September","October","November","December"),ordered=TRUE) 
table(monthsFactors)

## factor to int ##
fertilizer = c(10,20,20,50,10,20,10,50,20)
mean(fertilizer) 
fertilizer = factor(fertilizer,levels=c(10,20,50),ordered=TRUE)
mean(fertilizer) 
mean(as.numeric(as.character(fertilizer))) 

## cut ##
fuelUsage = cut(mtcars$mpg, breaks=3, labels=c("high mileage", "average mileage", "low mileage")) 
table(fuelUsage)

### Mean ###
mean(mtcars$mpg)
### Median ###
median(mtcars$mpg)
### standard deviation ###
sd(mtcars$mpg)

### Quartile ###
quantile(mtcars$mpg) 

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
library(ggplot2)
ggplot(movies, aes(x=rating))+ geom_histogram(aes(fill = ..count..))

### violin plot ###
ggplot(mtcars, aes(factor(cyl), mpg)) + geom_violin()
ggplot(movies, aes(factor(round(rating, digits = 0)), length)) + geom_violin()

 
## heatmap ##
library(ggplot2)
library(scales)
library(reshape)
library(plyr)
# inspired by: https://learnr.wordpress.com/2010/01/26/ggplot2-quick-heatmap-plotting/

nba <- read.csv("http://datasets.flowingdata.com/ppg2008.csv")
nba$Name <- with(nba, reorder(Name, PTS))
head(nba)
nba.m <- melt(nba)
head(nba.m)
nba.m <- ddply(nba.m, .(variable), transform, rescale = rescale(value))
head(nba.m)
(p <- ggplot(nba.m, aes(variable, Name)) + geom_tile(aes(fill = rescale), colour = "white") + scale_fill_gradient(low = "white", high = "steelblue"))

base_size <- 9
p + theme_grey(base_size = base_size) + labs(x = "", y = "") + scale_x_discrete(expand = c(0, 0)) +
scale_y_discrete(expand = c(0, 0)) + 
theme(legend.position = "none", axis.ticks = element_blank(), axis.text.x = element_text(size = base_size *0.8, angle = 330, hjust = 0, colour = "grey50"))
nba.s <- ddply(nba.m, .(variable), transform, rescale = scale(value))
last_plot() %+% nba.s
