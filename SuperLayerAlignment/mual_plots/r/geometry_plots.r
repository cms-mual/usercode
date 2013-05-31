library(ggplot2)

theme_set(theme_bw())

save_png <- function(fname) {
  dev.copy(png, fname, width=1400, height=800)
  dev.off()
}

#setwd("C:/Users/khotilov/Downloads")
setwd("C:\Users\khotilov\Work\alignment\mual_plots\mual_plots_20111201")


file_dd  = 'hw_sl123.txt'
file_dd0  = 'hw_sl123_nogpr.txt'
file_dd0  = 'hw_sl123_Tilt.txt'

dd = read.table(file_dd,header=T)
head(dd, n=2)

dd0 = read.table(file_dd0,header=T)
head(dd0, n=2)


### read in the sign conventions and coordinates

sstop= read.table('sign_conventions_mb.txt',header=T, nrows=1)
sstop
classes <- sapply(sstop, class)
classes
classes["label"]="character"
classes
ss = read.table('sign_conventions_mb.txt',header=T, colClasses=classes)
head(ss, n=2)

dds = merge(dd,ss)

# change to global coordinates:

d = dds

d["ch_phix"] = dds["ch_phix"]*dds["signy"]*dds["signz"]
d["ch_phiy"] = dds["ch_phiy"]*dds["signz"]*dds["signx"]
d["ch_phiz"] = dds["ch_phiz"]*dds["signx"]*dds["signy"]
d["ch_x"] = dds["ch_x"]*dds["signx"]
d["ch_y"] = dds["ch_y"]*dds["signy"]
d["ch_z"] = dds["ch_z"]*dds["signz"]
d["sl1_phix"] = dds["sl1_phix"]*dds["signy"]*dds["signz"]
d["sl1_phiy"] = dds["sl1_phiy"]*dds["signz"]*dds["signx"]
d["sl1_phiz"] = dds["sl1_phiz"]*dds["signx"]*dds["signy"]
d["sl1_x"] = dds["sl1_x"]*dds["signx"]
d["sl1_y"] = dds["sl1_y"]*dds["signy"]
d["sl1_z"] = dds["sl1_z"]*dds["signz"]
d["sl2_phix"] = dds["sl2_phix"]*dds["signy"]*dds["signz"]
d["sl2_phiy"] = dds["sl2_phiy"]*dds["signz"]*dds["signx"]
d["sl2_phiz"] = dds["sl2_phiz"]*dds["signx"]*dds["signy"]
d["sl2_x"] = dds["sl2_x"]*dds["signx"]
d["sl2_y"] = dds["sl2_y"]*dds["signy"]
d["sl2_z"] = dds["sl2_z"]*dds["signz"]
d["sl3_phix"] = dds["sl3_phix"]*dds["signy"]*dds["signz"]
d["sl3_phiy"] = dds["sl3_phiy"]*dds["signz"]*dds["signx"]
d["sl3_phiz"] = dds["sl3_phiz"]*dds["signx"]*dds["signy"]
d["sl3_x"] = dds["sl3_x"]*dds["signx"]
d["sl3_y"] = dds["sl3_y"]*dds["signy"]
d["sl3_z"] = dds["sl3_z"]*dds["signz"]

head(d, n=2)

d123 = d[d$station<4,]



dds = merge(dd0,ss)

d0 = dds

d0["ch_phix"] = dds["ch_phix"]*dds["signy"]*dds["signz"]
d0["ch_phiy"] = dds["ch_phiy"]*dds["signz"]*dds["signx"]
d0["ch_phiz"] = dds["ch_phiz"]*dds["signx"]*dds["signy"]
d0["ch_x"] = dds["ch_x"]*dds["signx"]
d0["ch_y"] = dds["ch_y"]*dds["signy"]
d0["ch_z"] = dds["ch_z"]*dds["signz"]
d0["sl1_phix"] = dds["sl1_phix"]*dds["signy"]*dds["signz"]
d0["sl1_phiy"] = dds["sl1_phiy"]*dds["signz"]*dds["signx"]
d0["sl1_phiz"] = dds["sl1_phiz"]*dds["signx"]*dds["signy"]
d0["sl1_x"] = dds["sl1_x"]*dds["signx"]
d0["sl1_y"] = dds["sl1_y"]*dds["signy"]
d0["sl1_z"] = dds["sl1_z"]*dds["signz"]
d0["sl2_phix"] = dds["sl2_phix"]*dds["signy"]*dds["signz"]
d0["sl2_phiy"] = dds["sl2_phiy"]*dds["signz"]*dds["signx"]
d0["sl2_phiz"] = dds["sl2_phiz"]*dds["signx"]*dds["signy"]
d0["sl2_x"] = dds["sl2_x"]*dds["signx"]
d0["sl2_y"] = dds["sl2_y"]*dds["signy"]
d0["sl2_z"] = dds["sl2_z"]*dds["signz"]
d0["sl3_phix"] = dds["sl3_phix"]*dds["signy"]*dds["signz"]
d0["sl3_phiy"] = dds["sl3_phiy"]*dds["signz"]*dds["signx"]
d0["sl3_phiz"] = dds["sl3_phiz"]*dds["signx"]*dds["signy"]
d0["sl3_x"] = dds["sl3_x"]*dds["signx"]
d0["sl3_y"] = dds["sl3_y"]*dds["signy"]
d0["sl3_z"] = dds["sl3_z"]*dds["signz"]

head(d0, n=2)

d1230 = d0[d0$station<4,]





line00 <- stat_abline(intercept=0, slope=0, color=I("grey70"))
facet_st_wh <- facet_grid(station~wheel, labeller=label_both)
facet_st_sec <- facet_grid(station~sector, labeller=label_both)
facet_wh_sec <- facet_grid(wheel~sector, labeller=label_both)

point_b <- geom_point(color="blue")
point_r0 <- geom_point(data=d0, color="red")
text_sector <- geom_text(aes(label=sector), color="grey70", size=3, hjust=-0.3, vjust=0, legend=F)

#title_sl <- opts(title="SL1=blue  SL2=green  SL3=red")
title_sl <- opts(title="SL1=blue  SL3=red")

### chamber x

y_lab <- "HW correction WRT ideal: chamber x', mm"

ggplot(d, aes(phi, ch_x)) + point_b + line00 + facet_st_wh + ylab(y_lab) + xlab("global phiz, rad") + text_sector
save_png("ch_x_vs_phi__grid-st-wh.png")

ggplot(d, aes(wheel, ch_x)) + point_b + line00 + facet_st_sec + ylab(y_lab)
save_png("ch_x_vs_wh__grid-st-sec.png")

ggplot(d, aes(station, ch_x)) + point_b + line00 + facet_wh_sec + ylab(y_lab)
save_png("ch_x_vs_st__grid-wh-sec.png")

ggplot(d, aes(phi, ch_x)) + point_b + point_r0 + line00 + facet_st_wh + ylab(y_lab) + xlab("global phiz, rad") + text_sector


### chamber y

y_lab <- "HW correction WRT ideal: chamber y', mm"

ggplot(d, aes(phi, ch_y)) + point_b + line00 + facet_st_wh + ylab(y_lab) + xlab("global phiz, rad") + text_sector
save_png("ch_y_vs_phi__grid-st-wh.png")

ggplot(d, aes(wheel, ch_y)) + point_b + line00 + facet_st_sec + ylab(y_lab)
save_png("ch_y_vs_wh__grid-st-sec.png")

ggplot(d, aes(station, ch_y)) + point_b + line00 + facet_wh_sec + ylab(y_lab)
save_png("ch_y_vs_st__grid-wh-sec.png")

### chamber z

y_lab <- "HW correction WRT ideal: chamber z', mm"

ggplot(d, aes(phi, ch_z)) + point_b + line00 + facet_st_wh + ylab(y_lab) + xlab("global phiz, rad") + text_sector
save_png("ch_z_vs_phi__grid-st-wh.png")

ggplot(d, aes(wheel, ch_z)) + point_b + line00 + facet_st_sec + ylab(y_lab)
save_png("ch_z_vs_wh__grid-st-sec.png")

ggplot(d, aes(station, ch_z)) + point_b + line00 + facet_wh_sec + ylab(y_lab)
save_png("ch_z_vs_st__grid-wh-sec.png")


### chamber phix

y_lab <- "HW correction WRT ideal: chamber phix', mrad"

ggplot(d, aes(phi, ch_phix)) + point_b + line00 + facet_st_wh + ylab(y_lab) + xlab("global phiz, rad") + text_sector
save_png("ch_phix_vs_phi__grid-st-wh.png")

ggplot(d, aes(wheel, ch_phix)) + point_b + line00 + facet_st_sec + ylab(y_lab)
save_png("ch_phix_vs_wh__grid-st-sec.png")

ggplot(d, aes(station, ch_phix)) + point_b + line00 + facet_wh_sec + ylab(y_lab)
save_png("ch_phix_vs_st__grid-wh-sec.png")

### chamber phiy

y_lab <- "HW correction WRT ideal: chamber phiy', mrad"

ggplot(d, aes(phi, ch_phiy)) + point_b + line00 + facet_st_wh + ylab(y_lab) + xlab("global phiz, rad") + text_sector
save_png("ch_phiy_vs_phi__grid-st-wh.png")

ggplot(d, aes(wheel, ch_phiy)) + point_b + line00 + facet_st_sec + ylab(y_lab)
save_png("ch_phiy_vs_wh__grid-st-sec.png")

ggplot(d, aes(station, ch_phiy)) + point_b + line00 + facet_wh_sec + ylab(y_lab)
save_png("ch_phiy_vs_st__grid-wh-sec.png")

### chamber phiz

y_lab <- "HW correction WRT ideal: chamber phiz', mrad"

ggplot(d, aes(phi, ch_phiz)) + point_b + line00 + facet_st_wh + ylab(y_lab) + xlab("global phiz, rad") + text_sector
save_png("ch_phiz_vs_phi__grid-st-wh.png")

ggplot(d, aes(wheel, ch_phiz)) + point_b + line00 + facet_st_sec + ylab(y_lab)
save_png("ch_phiz_vs_wh__grid-st-sec.png")

ggplot(d, aes(station, ch_phiz)) + point_b + line00 + facet_wh_sec + ylab(y_lab)
save_png("ch_phiz_vs_st__grid-wh-sec.png")




### correction to SL1-SL3 x

y_lab <- "HW correction to SL1-SL3 x', mm"

ggplot(d, aes(phi, sl1_x-sl3_x)) + point_b + line00 + facet_st_wh + ylab(y_lab) + xlab("global phiz, rad") + text_sector
save_png("sl1sl3_x_vs_phi__grid-st-wh.png")

ggplot(d, aes(wheel, sl1_x-sl3_x)) + point_b + line00 + facet_st_sec + ylab(y_lab)
save_png("sl1sl3_x_vs_wh__grid-st-sec.png")

ggplot(d, aes(station, sl1_x-sl3_x)) + point_b + line00 + facet_wh_sec + ylab(y_lab)
save_png("sl1sl3_x_vs_st__grid-wh-sec.png")

### correction to SL1-SL3 y

y_lab <- "HW correction to SL1-SL3 y', mm"

ggplot(d, aes(phi, sl1_y-sl3_y)) + point_b + line00 + facet_st_wh + ylab(y_lab) + xlab("global phiz, rad") + text_sector
save_png("sl1sl3_y_vs_phi__grid-st-wh.png")

ggplot(d, aes(wheel, sl1_y-sl3_y)) + point_b + line00 + facet_st_sec + ylab(y_lab)
save_png("sl1sl3_y_vs_wh__grid-st-sec.png")

ggplot(d, aes(station, sl1_y-sl3_y)) + point_b + line00 + facet_wh_sec + ylab(y_lab)
save_png("sl1sl3_y_vs_st__grid-wh-sec.png")

### correction to SL1-SL3 z

y_lab <- "HW correction to SL1-SL3 z', mm"

ggplot(d, aes(phi, sl1_z-sl3_z)) + point_b + line00 + facet_st_wh + ylab(y_lab) + xlab("global phiz, rad") + text_sector
save_png("sl1sl3_z_vs_phi__grid-st-wh.png")

ggplot(d, aes(wheel, sl1_z-sl3_z)) + point_b + line00 + facet_st_sec + ylab(y_lab)
save_png("sl1sl3_z_vs_wh__grid-st-sec.png")

ggplot(d, aes(station, sl1_z-sl3_z)) + point_b + line00 + facet_wh_sec + ylab(y_lab)
save_png("sl1sl3_z_vs_st__grid-wh-sec.png")


### correction to SL1-SL3 phix

y_lab <- "HW correction to SL1-SL3 phix', mrad"

ggplot(d, aes(phi, sl1_phix-sl3_phix)) + point_b + line00 + facet_st_wh + ylab(y_lab) + xlab("global phiz, rad") + text_sector
save_png("sl1sl3_phix_vs_phi__grid-st-wh.png")

ggplot(d, aes(wheel, sl1_phix-sl3_phix)) + point_b + line00 + facet_st_sec + ylab(y_lab)
save_png("sl1sl3_phix_vs_wh__grid-st-sec.png")

ggplot(d, aes(station, sl1_phix-sl3_phix)) + point_b + line00 + facet_wh_sec + ylab(y_lab)
save_png("sl1sl3_phix_vs_st__grid-wh-sec.png")

### correction to SL1-SL3 phiy

y_lab <- "HW correction to SL1-SL3  phiy', mrad"

ggplot(d, aes(phi, sl1_phiy-sl3_phiy)) + point_b + line00 + facet_st_wh + ylab(y_lab) + xlab("global phiz, rad") + text_sector
save_png("sl1sl3_phiy_vs_phi__grid-st-wh.png")

ggplot(d, aes(wheel, sl1_phiy-sl3_phiy)) + point_b + line00 + facet_st_sec + ylab(y_lab)
save_png("sl1sl3_phiy_vs_wh__grid-st-sec.png")

ggplot(d, aes(station, sl1_phiy-sl3_phiy)) + point_b + line00 + facet_wh_sec + ylab(y_lab)
save_png("sl1sl3_phiy_vs_st__grid-wh-sec.png")

ggplot(d, aes(phi, sl1_phiy-sl3_phiy)) + point_b + point_r0 + line00 + facet_st_wh + ylab(y_lab) + xlab("global phiz, rad") + text_sector
save_png("sl1sl3_phiy_vs_phi__grid-st-wh__default-and-Tilt.png")

y_lab <- "HW correction to (SL1+SL3)/2  phiy', mrad"
ggplot(d, aes(phi, (sl1_phiy+sl3_phiy)/2.)) + point_b + point_r0 + line00 + facet_st_wh + ylab(y_lab) + xlab("global phiz, rad") + text_sector
save_png("sl1-plus-sl3_phiy_vs_phi__grid-st-wh__default-and-Tilt.png")

y_lab <- "Luca's correction to (SL1+SL3)/2  phiy', mrad"
dd0 = merge(d,d0, by=c("wheel","station","sector","label"))
head(dd0)
ggplot(dd0, aes(phi.x, (sl1_phiy.y+sl3_phiy.y)/2.-(sl1_phiy.x+sl3_phiy.x)/2.)) + point_b + line00 + facet_st_wh + ylab(y_lab) + xlab("global phiz, rad") + text_sector
save_png("sl1-plus-sl3_phiy_vs_phi__grid-st-wh__default-and-Tilt.png")


### correction to SL1-SL3 phiz

y_lab <- "HW correction to SL1-SL3 phiz', mrad"

ggplot(d, aes(phi, sl1_phiz-sl3_phiz)) + point_b + line00 + facet_st_wh + ylab(y_lab) + xlab("global phiz, rad") + text_sector
save_png("sl1sl3_phiz_vs_phi__grid-st-wh.png")

ggplot(d, aes(wheel, sl1_phiz-sl3_phiz)) + point_b + line00 + facet_st_sec + ylab(y_lab)
save_png("sl1sl3_phiz_vs_wh__grid-st-sec.png")

ggplot(d, aes(station, sl1_phiz-sl3_phiz)) + point_b + line00 + facet_wh_sec + ylab(y_lab)
save_png("sl1sl3_phiz_vs_st__grid-wh-sec.png")



### correction to Chamber-SL x

y_lab <- "HW correction to Chamber-SL  x', mm"

ggplot(d, aes(phi, ch_x-sl1_x)) + point_b + geom_point(color="red", aes(phi, ch_x-sl3_x)) + line00 + facet_st_wh + ylab(y_lab) + xlab("global phiz, rad") + text_sector + title_sl
save_png("chsl13_x_vs_phi__grid-st-wh.png")

ggplot(d, aes(wheel, ch_x-sl1_x)) + point_b + geom_point(color="red", aes(wheel, ch_x-sl3_x)) + line00 + facet_st_sec + ylab(y_lab) + title_sl
save_png("chsl13_x_vs_wh__grid-st-sec.png")

ggplot(d, aes(station, ch_x-sl1_x)) + point_b + geom_point(color="red", aes(station, ch_x-sl3_x)) + line00 + facet_wh_sec + ylab(y_lab) + title_sl
save_png("chsl13_x_vs_st__grid-wh-sec.png")

### correction to Chamber-SL y

y_lab <- "HW correction to Chamber-SL  y', mm"

ggplot(d, aes(phi, ch_y-sl1_y)) + point_b + geom_point(color="red", aes(phi, ch_y-sl3_y)) + line00 + facet_st_wh + ylab(y_lab) + xlab("global phiz, rad") + text_sector + title_sl
save_png("chsl13_y_vs_phi__grid-st-wh.png")

ggplot(d, aes(wheel, ch_y-sl1_y)) + point_b + geom_point(color="red", aes(wheel, ch_y-sl3_y)) + line00 + facet_st_sec + ylab(y_lab) + title_sl
save_png("chsl13_y_vs_wh__grid-st-sec.png")

ggplot(d, aes(station, ch_y-sl1_y)) + point_b + geom_point(color="red", aes(station, ch_y-sl3_y)) + line00 + facet_wh_sec + ylab(y_lab) + title_sl
save_png("chsl13_y_vs_st__grid-wh-sec.png")

### correction to Chamber-SL z

y_lab <- "HW correction to Chamber-SL  z', mm"

ggplot(d, aes(phi, ch_z-sl1_z)) + point_b + geom_point(color="red", aes(phi, ch_z-sl3_z)) + line00 + facet_st_wh + ylab(y_lab) + xlab("global phiz, rad") + text_sector + title_sl
save_png("chsl13_z_vs_phi__grid-st-wh.png")

ggplot(d, aes(wheel, ch_z-sl1_z)) + point_b + geom_point(color="red", aes(wheel, ch_z-sl3_z)) + line00 + facet_st_sec + ylab(y_lab) + title_sl
save_png("chsl13_z_vs_wh__grid-st-sec.png")

ggplot(d, aes(station, ch_z-sl1_z)) + point_b + geom_point(color="red", aes(station, ch_z-sl3_z)) + line00 + facet_wh_sec + ylab(y_lab) + title_sl
save_png("chsl13_z_vs_st__grid-wh-sec.png")

### correction to Chamber-SL phix

y_lab <- "HW correction to Chamber-SL  phix', mrad"

ggplot(d, aes(phi, ch_phix-sl1_phix)) + point_b + geom_point(color="red", aes(phi, ch_phix-sl3_phix)) + line00 + facet_st_wh + ylab(y_lab) + xlab("global phiz, rad") + text_sector + title_sl
save_png("chsl13_phix_vs_phi__grid-st-wh.png")

ggplot(d, aes(wheel, ch_phix-sl1_phix)) + point_b + geom_point(color="red", aes(wheel, ch_phix-sl3_phix)) + line00 + facet_st_sec + ylab(y_lab) + title_sl
save_png("chsl13_phix_vs_wh__grid-st-sec.png")

ggplot(d, aes(station, ch_phix-sl1_phix)) + point_b + geom_point(color="red", aes(station, ch_phix-sl3_phix)) + line00 + facet_wh_sec + ylab(y_lab) + title_sl
save_png("chsl13_phix_vs_st__grid-wh-sec.png")

### correction to Chamber-SL phiy

y_lab <- "HW correction to Chamber-SL  phiy', mrad"

ggplot(d, aes(phi, ch_phiy-sl1_phiy)) + point_b + geom_point(color="red", aes(phi, ch_phiy-sl3_phiy)) + line00 + facet_st_wh + ylab(y_lab) + xlab("global phiz, rad") + text_sector + title_sl
save_png("chsl13_phiy_vs_phi__grid-st-wh.png")

ggplot(d, aes(wheel, ch_phiy-sl1_phiy)) + point_b + geom_point(color="red", aes(wheel, ch_phiy-sl3_phiy)) + line00 + facet_st_sec + ylab(y_lab) + title_sl
save_png("chsl13_phiy_vs_wh__grid-st-sec.png")

ggplot(d, aes(station, ch_phiy-sl1_phiy)) + point_b + geom_point(color="red", aes(station, ch_phiy-sl3_phiy)) + line00 + facet_wh_sec + ylab(y_lab) + title_sl
save_png("chsl13_phiy_vs_st__grid-wh-sec.png")

y_lab <- "HW correction to Chamber-SL1  phiy', mrad"
ggplot(d, aes(phi, ch_phiy-sl1_phiy)) + point_b + point_r0 + line00 + facet_st_wh + ylab(y_lab) + xlab("global phiz, rad") + text_sector
save_png("chsl1_phiy_vs_phi__grid-st-wh__default-and-Tilt.png")

y_lab <- "HW correction to Chamber-SL3  phiy', mrad"
ggplot(d, aes(phi, ch_phiy-sl3_phiy)) + point_b + point_r0 + line00 + facet_st_wh + ylab(y_lab) + xlab("global phiz, rad") + text_sector
save_png("chsl3_phiy_vs_phi__grid-st-wh__default-and-Tilt.png")


### correction to Chamber-SL phiz

y_lab <- "HW correction to Chamber-SL  phiz', mrad"

ggplot(d, aes(phi, ch_phiz-sl1_phiz)) + point_b + geom_point(color="red", aes(phi, ch_phiz-sl3_phiz)) + line00 + facet_st_wh + ylab(y_lab) + xlab("global phiz, rad") + text_sector + title_sl
save_png("chsl13_phiz_vs_phi__grid-st-wh.png")

ggplot(d, aes(wheel, ch_phiz-sl1_phiz)) + point_b + geom_point(color="red", aes(wheel, ch_phiz-sl3_phiz)) + line00 + facet_st_sec + ylab(y_lab) + title_sl
save_png("chsl13_phiz_vs_wh__grid-st-sec.png")

ggplot(d, aes(station, ch_phiz-sl1_phiz)) + point_b + geom_point(color="red", aes(station, ch_phiz-sl3_phiz)) + line00 + facet_wh_sec + ylab(y_lab) + title_sl
save_png("chsl13_phiz_vs_st__grid-wh-sec.png")









