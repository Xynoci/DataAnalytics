library(ggplot2)
library(scales)
library(reshape)
library(plyr)
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
